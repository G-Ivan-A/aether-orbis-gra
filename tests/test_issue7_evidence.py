"""Negative cases for Academy provenance and separation from other projects."""
import importlib.util
import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    'issue7_evidence', ROOT / 'experiments/issue-7/validate_evidence.py')
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class ResearchBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.args = [deepcopy(CHECK.load(name)) for name in
                     ('evidence.json', 'preservation.json')]

    def test_current_package(self):
        CHECK.validate(*self.args)
        CHECK.main()

    def test_missing_quote_location(self):
        self.args[0]['sources'][0]['locator'] = ''
        with self.assertRaisesRegex(ValueError, 'missing locator'):
            CHECK.validate(*self.args)

    def test_search_index_cannot_be_promoted_to_document(self):
        self.args[0]['sources'][2]['status'] = 'VERIFIED'
        with self.assertRaisesRegex(ValueError, 'index-only'):
            CHECK.validate(*self.args)

    def test_index_name_cannot_be_promoted(self):
        self.args[0]['people'][-1]['name_status'] = 'VERIFIED'
        with self.assertRaisesRegex(ValueError, 'name promoted'):
            CHECK.validate(*self.args)

    def test_lost_source(self):
        self.args[0]['sources'].pop(0)
        with self.assertRaisesRegex(ValueError, 'source inventory incomplete'):
            CHECK.validate(*self.args)

    def test_lost_person(self):
        self.args[0]['people'].pop()
        with self.assertRaisesRegex(ValueError, 'person inventory incomplete'):
            CHECK.validate(*self.args)

    def test_public_visibility_is_not_authority(self):
        self.args[0]['people'][0]['authority'] = 'budget_owner'
        with self.assertRaisesRegex(ValueError, 'purchasing authority'):
            CHECK.validate(*self.args)

    def test_foreign_baseline_repository(self):
        self.args[0]['baseline']['repository'] = 'G-Ivan-A/unrelated-project'
        with self.assertRaisesRegex(ValueError, 'out-of-scope baseline repository'):
            CHECK.validate(*self.args)

    def test_foreign_source_url(self):
        self.args[0]['sources'][0]['url'] = 'https://github.com/G-Ivan-A/unrelated-project'
        with self.assertRaisesRegex(ValueError, 'out-of-scope project link'):
            CHECK.validate(*self.args)

    def test_foreign_project_metadata(self):
        self.args[0]['inherited'] = {'repository': 'G-Ivan-A/unrelated-project'}
        with self.assertRaisesRegex(ValueError, 'out-of-scope evidence metadata'):
            CHECK.validate(*self.args)

    def test_foreign_record_metadata(self):
        self.args[0]['sources'][0]['inherited_record_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'out-of-scope source metadata'):
            CHECK.validate(*self.args)

    def test_foreign_preservation_metadata(self):
        self.args[1]['release_manifest_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'out-of-scope preservation metadata'):
            CHECK.validate(*self.args)

    def test_foreign_link_in_research_prose(self):
        with self.assertRaisesRegex(ValueError, 'out-of-scope project link'):
            CHECK.validate_links('Приложение: [сайт](https://github.com/G-Ivan-A/unrelated-project).')

    def test_foreign_link_inside_source_limits(self):
        self.args[0]['sources'][0]['limits'] += ' https://unrelated-project.invalid/release'
        with self.assertRaisesRegex(ValueError, 'out-of-scope source link'):
            CHECK.validate(*self.args)

    def test_foreign_release_artifact(self):
        with self.assertRaisesRegex(ValueError, 'out-of-scope or missing research artifact'):
            CHECK.validate_artifacts(CHECK.PACKAGE_FILES | {'release-manifest.json'})

    def test_predecessor_modification(self):
        key = next(iter(self.args[1]['files']))
        self.args[1]['files'][key] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'predecessor changed'):
            CHECK.validate(*self.args)


BRIEF_SPEC = importlib.util.spec_from_file_location(
    'issue7_brief', ROOT / 'experiments/issue-7/brief.py')
BRIEF = importlib.util.module_from_spec(BRIEF_SPEC)
BRIEF_SPEC.loader.exec_module(BRIEF)


class BriefTests(unittest.TestCase):
    """Owner limit: brief of at most two typewritten pages with clickable links."""

    def copy_package(self, tmp, text=None):
        brief, pdf, manifest = (Path(tmp) / name for name in
                                ('brief.md', 'brief.pdf', 'brief-render.json'))
        brief.write_text(text if text is not None
                         else BRIEF.BRIEF.read_text(encoding='utf-8'), encoding='utf-8')
        pdf.write_bytes(BRIEF.PDF.read_bytes())
        manifest.write_text(BRIEF.MANIFEST.read_text(encoding='utf-8'), encoding='utf-8')
        return brief, pdf, manifest

    def test_current_brief(self):
        chars, pages = BRIEF.check()
        self.assertLessEqual(chars, 3600)
        self.assertLessEqual(pages, 2)

    def test_rector_is_priority_and_details_are_linked(self):
        text = BRIEF.BRIEF.read_text(encoding='utf-8')
        self.assertLess(text.index('Ректор'), text.index('ПСБ — учредитель'))
        relative = [url for url in BRIEF.links(text) if not url.startswith('https://')]
        self.assertTrue(any('decision-makers' in url for url in relative))
        self.assertTrue(any('evidence.json' in url for url in relative))

    def test_markup_and_urls_are_not_counted(self):
        self.assertEqual(BRIEF.visible_text(
            '---\na: b\n---\n## Заголовок\n- **Да** [текст](https://psb-academy.ru/x)\n'
            '| A | B |\n| --- | --- |\n| 1 | 2 |\n'), 'Заголовок Да текст A B 1 2')

    def test_over_length_brief(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = self.copy_package(tmp, 'слово ' * 700)
            with self.assertRaisesRegex(ValueError, 'visible characters'):
                BRIEF.check(*paths)

    def test_stale_pdf(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = self.copy_package(tmp)
            paths[0].write_text(paths[0].read_text(encoding='utf-8') + '\nПравка.\n',
                                encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'stale'):
                BRIEF.check(*paths)

    def test_pdf_replaced_without_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = self.copy_package(tmp)
            paths[1].write_bytes(b'%PDF-1.4\n')
            with self.assertRaisesRegex(ValueError, 'does not match'):
                BRIEF.check(*paths)

    def test_too_many_pages(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = self.copy_package(tmp)
            manifest = json.loads(paths[2].read_text(encoding='utf-8'))
            manifest['pages'] = 3
            paths[2].write_text(json.dumps(manifest), encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'pages'):
                BRIEF.check(*paths)

    def test_relative_link_pinned_to_commit(self):
        self.assertEqual(
            BRIEF.absolute('2026-11-09-issue-7-academy-decision-makers.md#именная-карта', 'abc'),
            'https://github.com/G-Ivan-A/aether-orbis-gra/blob/abc/docs/analysis/'
            '2026-11-09-issue-7-academy-decision-makers.md#именная-карта')
        self.assertEqual(BRIEF.absolute('../../experiments/issue-7/evidence.json', 'abc'),
                         'https://github.com/G-Ivan-A/aether-orbis-gra/blob/abc/'
                         'experiments/issue-7/evidence.json')

    def test_foreign_link_in_brief(self):
        with self.assertRaisesRegex(ValueError, 'out-of-scope project link'):
            CHECK.validate_links('[x](https://github.com/G-Ivan-A/unrelated-project)',
                                 CHECK.SOURCE_HOSTS | CHECK.FOUNDER_HOSTS)

    def test_founder_host_is_not_academy_evidence(self):
        args = [deepcopy(CHECK.load(name)) for name in ('evidence.json', 'preservation.json')]
        args[0]['sources'][0]['url'] = 'https://www.psbank.ru/bank/press/news/2025/10/09-05'
        with self.assertRaisesRegex(ValueError, 'Academy research publisher|out-of-scope source link'):
            CHECK.validate(*args)
