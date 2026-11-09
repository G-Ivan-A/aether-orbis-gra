"""Negative cases for research provenance and the preserved release boundary."""
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
                     ('evidence.json', 'preservation.json', 'site-audit.json',
                      'inherited-site-audit.json')]

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

    def test_lost_inherited_record(self):
        self.args[0]['sources'].pop(0)
        with self.assertRaisesRegex(ValueError, 'lost inherited source'):
            CHECK.validate(*self.args)

    def test_public_visibility_is_not_authority(self):
        self.args[0]['people'][0]['authority'] = 'budget_owner'
        with self.assertRaisesRegex(ValueError, 'purchasing authority'):
            CHECK.validate(*self.args)

    def test_missing_live_catalogue_entry(self):
        self.args[2]['catalogue_ids_preserved'].pop()
        with self.assertRaisesRegex(ValueError, 'previous live IDs lost'):
            CHECK.validate(*self.args)

    def test_semantic_drift_even_if_report_says_unchanged(self):
        self.args[2]['assets']['site/data/prompts.json']['normalized_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'deployment content drift'):
            CHECK.validate(*self.args)

    def test_predecessor_modification(self):
        key = next(iter(self.args[1]['files']))
        self.args[1]['files'][key] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'predecessor changed'):
            CHECK.validate(*self.args)
