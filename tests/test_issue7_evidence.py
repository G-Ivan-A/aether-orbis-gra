"""Negative cases for Academy provenance and separation from other projects."""
import importlib.util
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
