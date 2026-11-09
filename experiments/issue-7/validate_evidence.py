#!/usr/bin/env python3
"""Offline integrity and scope checks for the Academy meeting research."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPOSITORY = 'G-Ivan-A/aether-orbis-gra'
# Publishers actually used by this research; this is not a repository policy.
SOURCE_HOSTS = frozenset((
    'psb-academy.ru', 'storage.psb-academy.ru', 'rrmag.ru', 'dialogmanag.com',
    'www.vedomosti.ru', 'teachbase.ru', 'workspace.ru', 'spb.ranepa.ru',
    'raex-rr.com',
))
# Founder (bank) sources of the accepted GRA #5 registry B01/B02/B06, cited by
# the PSB / Academy brief only; they are not Academy evidence records.
FOUNDER_HOSTS = frozenset(('www.cbr.ru', 'sanctionssearch.ofac.treas.gov',
                           'www.psbank.ru'))
PACKAGE_FILES = frozenset(('README.md', 'evidence.json', 'preservation.json',
                           'validate_evidence.py', 'brief.py', 'brief-render.json'))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load(name):
    return json.loads((HERE / name).read_text(encoding='utf-8'))


def validate_artifacts(paths):
    require(set(paths) == PACKAGE_FILES, 'out-of-scope or missing research artifact')


def validate_links(text, hosts=SOURCE_HOSTS):
    """Reject links to unrelated projects, including links inside prose fields."""
    for url in re.findall(r'https?://[^\s<>"\')]+', text):
        parsed = urlsplit(url)
        if parsed.hostname == 'github.com':
            project = '/'.join(unquote(parsed.path).strip('/').split('/')[:2])
            require(project in (REPOSITORY, 'G-Ivan-A/hybrid-Intelligence-lab'),
                    f'out-of-scope project link: {url}')
        else:
            require(parsed.scheme == 'https' and parsed.hostname in hosts,
                    f'out-of-scope source link: {url}')


def validate(evidence, preservation):
    require(evidence.get('schema_version') == 3, 'unexpected evidence schema')
    require(set(evidence) == {'schema_version', 'scope', 'accessed_at', 'baseline',
                              'sources', 'people'}, 'out-of-scope evidence metadata')
    require(evidence['scope'] == 'academy_decision_makers_meeting', 'wrong research scope')
    baseline = evidence['baseline']
    require(baseline['repository'] == REPOSITORY, 'out-of-scope baseline repository')
    require(set(baseline) == {'repository', 'sha', 'pull_request'},
            'out-of-scope baseline metadata')
    require(set(preservation) == {'baseline_sha', 'files'},
            'out-of-scope preservation metadata')
    require(baseline['sha'] == preservation['baseline_sha'], 'baseline mismatch')
    validate_links(json.dumps(evidence, ensure_ascii=False))
    sources = {s['id']: s for s in evidence['sources']}
    people = {p['id']: p for p in evidence['people']}
    require(len(sources) == len(evidence['sources']), 'duplicate source ID')
    require(len(people) == len(evidence['people']), 'duplicate person ID')
    require(set(sources) == {f'N{i:02}' for i in range(1, 21)}, 'source inventory incomplete')
    require(set(people) == {f'P{i:02}' for i in range(1, 11)}, 'person inventory incomplete')
    source_fields = {'id', 'previous', 'url', 'publisher', 'title', 'published_at',
                     'event_date', 'access', 'locator', 'quote', 'status', 'origin',
                     'claim', 'limits', 'accessed_at', 'recheck', 'document_sha256',
                     'document_bytes'}
    for source in sources.values():
        require(set(source) <= source_fields, 'out-of-scope source metadata')
        for key in ('url', 'publisher', 'title', 'access', 'locator', 'quote',
                    'status', 'origin', 'claim', 'limits', 'accessed_at', 'recheck'):
            require(bool(source.get(key)), f'{source["id"]}: missing {key}')
        require(urlsplit(source['url']).hostname in SOURCE_HOSTS,
                'source must point directly to an Academy research publisher')
        require(source['url'].startswith('https://'), 'source URL must be HTTPS')
        require(source['status'] in ('VERIFIED', 'PARTIAL', 'CONFLICT'), 'unknown status')
        require(source['access'] != 'search_index' or source['status'] != 'VERIFIED',
                'index-only evidence cannot become VERIFIED')
        for key in ('published_at', 'event_date'):
            require(key in source, f'{source["id"]}: missing explicit date or null')
    person_fields = {'id', 'name', 'role', 'name_status', 'name_source', 'role_sources',
                     'mentions', 'authority', 'current_mandate', 'role_evidence'}
    for person in people.values():
        require(set(person) == person_fields, 'unexpected person fields')
        refs = [person['name_source']] + person['role_sources'] + person['mentions']
        require(set(refs) <= sources.keys(), 'dangling source reference')
        name_source = sources[person['name_source']]
        require(person['name_status'] != 'VERIFIED' or
                (name_source['access'] != 'search_index' and name_source['status'] == 'VERIFIED'),
                'name promoted without a verified document')
        require(person['authority'] == 'unknown' and person['current_mandate'] == 'unknown',
                'public mention cannot establish purchasing authority')
    require(people['P10']['name_status'] == 'PARTIAL', 'platform identity conflict lost')
    require(people['P09']['role_evidence'] == 'undated_programme_and_course_card',
            'programme role promoted to current appointment')
    require(len(preservation['files']) == 10, 'predecessor inventory incomplete')
    for name, expected in preservation['files'].items():
        path = ROOT / name
        require(path.resolve().is_relative_to(ROOT), 'predecessor path outside repository')
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        require(actual == expected, f'predecessor changed: {name}')


def main():
    validate_artifacts(p.relative_to(HERE).as_posix() for p in HERE.rglob('*')
                       if p.is_file() and p.suffix != '.pyc')
    validate(load('evidence.json'), load('preservation.json'))
    documents = [HERE / 'README.md', *sorted((ROOT / 'docs/analysis').glob('*issue-7-*.md'))]
    for path in documents:
        validate_links(path.read_text(encoding='utf-8'), SOURCE_HOSTS | FOUNDER_HOSTS)
    print('Academy research scope, provenance and predecessor preservation: OK')


if __name__ == '__main__':
    main()
