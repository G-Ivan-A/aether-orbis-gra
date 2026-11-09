#!/usr/bin/env python3
"""Offline integrity checks; they cannot establish the truth of a web claim."""
import hashlib
import json
import re
from pathlib import Path, PurePosixPath

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load(name):
    return json.loads((HERE / name).read_text())


def validate(evidence, preservation, site, inherited_site):
    sources = {s['id']: s for s in evidence['sources']}
    people = {p['id']: p for p in evidence['people']}
    require(len(sources) == len(evidence['sources']), 'duplicate source ID')
    require(len(people) == len(evidence['people']), 'duplicate person ID')
    require(set(evidence['inherited']['source_ids']) <= sources.keys(), 'lost inherited source')
    require(set(evidence['inherited']['person_ids']) <= people.keys(), 'lost inherited person')
    for source in sources.values():
        for key in ('url', 'publisher', 'title', 'access', 'locator', 'quote',
                    'status', 'origin', 'claim', 'limits', 'accessed_at', 'recheck'):
            require(bool(source.get(key)), f'{source["id"]}: missing {key}')
        require(source['url'].startswith('https://'), 'source URL must be HTTPS')
        require(source['status'] in ('VERIFIED', 'PARTIAL', 'CONFLICT'), 'unknown status')
        require(source['access'] != 'search_index' or source['status'] != 'VERIFIED',
                'index-only evidence cannot become VERIFIED')
        for key in ('published_at', 'event_date'):
            require(key in source, f'{source["id"]}: missing explicit date or null')
        if source['id'] in evidence['inherited']['source_ids']:
            require(bool(re.fullmatch('[0-9a-f]{64}', source.get('inherited_record_sha256', ''))),
                    'missing inherited record hash')
    for person in people.values():
        refs = [person['name_source']] + person['role_sources'] + person['mentions']
        require(set(refs) <= sources.keys(), 'dangling source reference')
        name_source = sources[person['name_source']]
        require(person['name_status'] != 'VERIFIED' or
                (name_source['access'] != 'search_index' and name_source['status'] == 'VERIFIED'),
                'name promoted without a verified document')
        require(person['authority'] == 'unknown' and person['current_mandate'] == 'unknown',
                'public mention cannot establish purchasing authority')
    # P09/P10 are documented gaps: no automatic appointment from a course or index.
    require(people['P10']['name_status'] == 'PARTIAL', 'platform identity conflict lost')
    require(people['P09']['role_evidence'] == 'undated_programme_and_course_card',
            'programme role promoted to current appointment')
    require(len(preservation['files']) == 10, 'predecessor inventory incomplete')
    for name, expected in preservation['files'].items():
        actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        require(actual == expected, f'predecessor changed: {name}')
    old_hash = hashlib.sha256((HERE / 'inherited-site-audit.json').read_bytes()).hexdigest()
    require(old_hash == preservation['inherited_site_audit_sha256'], 'inherited manifest changed')
    require(site['baseline_sha'] == inherited_site['baseline_sha'], 'site baseline changed')
    require(site['catalogue_ids_removed'] == [], 'live catalogue IDs removed')
    require(set(inherited_site['catalogue_ids_preserved']) <= set(site['catalogue_ids_preserved']),
            'previous live IDs lost')
    require(site['inherited_candidate_semantic_changes'] == [], 'candidate content changed')
    require(len(site['assets']) == 22 and site['assets'].keys() == inherited_site['assets'].keys(),
            'deployment asset set changed')
    for name, asset in site['assets'].items():
        path = PurePosixPath(name)
        require(not path.is_absolute() and '..' not in path.parts and bool(path.parts) and path.parts[0] == 'site',
                'unsafe deployment path')
        old = inherited_site['assets'][name]
        key = 'normalized_sha256' if name.endswith('.json') else 'sha256'
        require(asset[key] == old[key], f'deployment content drift: {name}')


def main():
    validate(load('evidence.json'), load('preservation.json'), load('site-audit.json'),
             load('inherited-site-audit.json'))
    browser = load('browser-result.json')
    require(browser['pageErrors'] == [] and browser['copies'] == 24 and
            browser['archiveCopies'] == 4 and browser['errorReload'], 'browser check incomplete')
    for name in browser['screenshots']:
        require((HERE / name).read_bytes().startswith(b'\x89PNG\r\n\x1a\n'), 'invalid screenshot')
    print('Evidence, predecessor preservation, deployment manifest and browser record: OK')


if __name__ == '__main__':
    main()
