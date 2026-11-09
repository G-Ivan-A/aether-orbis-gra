"""Small offline checks for the research inventory's completeness and data boundary."""
import importlib.util
import json
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    'catalogue_probe', ROOT / 'experiments/issue-5/catalogue_probe.py')
PROBE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PROBE)


class OpenResponse:
    """A complete JSON body whose HTTP connection has not closed yet."""
    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def read(self, size):
        raise AssertionError('bounded read waits for EOF on an open connection')

    def read1(self, size):
        assert size <= 65536
        return b'{"count":0,"next":null,"results":[]}'


class CatalogueEvidenceTests(unittest.TestCase):
    def test_complete_json_does_not_wait_for_connection_close(self):
        with patch.object(PROBE, 'urlopen', return_value=OpenResponse()):
            result = PROBE.collect(None)
        self.assertEqual(result['programmes'], [])
        self.assertEqual(len(result['pages']), 1)

    def test_missing_page_is_not_a_complete_inventory(self):
        data = json.loads((ROOT / 'experiments/issue-5/catalogue-2026-11-08.json').read_text())
        data['programmes'].pop()
        with self.assertRaisesRegex(AssertionError, 'incomplete'):
            PROBE.validate(data)

    def test_people_fields_are_rejected(self):
        data = json.loads((ROOT / 'experiments/issue-5/catalogue-2026-11-08.json').read_text())
        data['programmes'][0]['teacher'] = 'unexpected field'
        with self.assertRaisesRegex(AssertionError, 'unexpected fields'):
            PROBE.validate(data)

    def test_filtered_snapshot_matches_whole_catalogue(self):
        folder = ROOT / 'experiments/issue-5'
        digital = json.loads((folder / 'catalogue-2026-11-08.json').read_text())
        whole = json.loads((folder / 'all-catalogue-2026-11-08.json').read_text())
        PROBE.validate(whole)
        self.assertEqual({x['id'] for x in digital['programmes']},
                         {x['id'] for x in whole['programmes'] if 5 in x['category_ids']})
