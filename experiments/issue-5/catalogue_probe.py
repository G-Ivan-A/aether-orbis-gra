#!/usr/bin/env python3
"""Read public catalogue pages; retain programme metadata, never people fields.

Usage: python3 experiments/issue-5/catalogue_probe.py --output /tmp/catalogue.json
       python3 experiments/issue-5/catalogue_probe.py --check /tmp/catalogue.json
No authentication, enrolment or form submission. At most 30 pages, sequential I/O.
"""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlparse, urlunparse
from urllib.request import urlopen

BASE = 'https://psb-academy.ru'


def validate(snapshot):
    pages, items = snapshot['pages'], snapshot['programmes']
    assert pages and len(pages) <= 30, 'missing or unbounded pages'
    assert len(items) == pages[0]['count'], 'incomplete inventory'
    assert len({x['id'] for x in items}) == len(items), 'duplicate programme IDs'
    assert pages[-1]['next'] is None, 'pagination not exhausted'
    assert all(p['count'] == len(items) for p in pages), 'count changed during retrieval'
    assert all(5 in x['category_ids'] for x in items), 'category filter failed'
    assert all(x['updated_at'][:10] <= snapshot['accessed_at'][:10] for x in items), 'future update'
    assert all(set(x) == {'id', 'name', 'url', 'category_ids', 'price', 'started_at',
                         'flexible_start', 'updated_at'} for x in items), 'unexpected fields'


def collect():
    result = {'accessed_at': datetime.now(timezone.utc).isoformat(),
              'category': 5, 'pages': [], 'programmes': []}
    url = BASE + '/api/v1/metaprograms/metaprogram?categories=5&page=1&per_page=6'
    for _ in range(30):
        parsed = urlparse(url)
        assert parsed.hostname == 'psb-academy.ru' and parsed.path == '/api/v1/metaprograms/metaprogram'
        assert parse_qs(parsed.query).get('categories') == ['5']
        # The public API emits HTTP next links; retain query/path, always request HTTPS.
        url = urlunparse(parsed._replace(scheme='https'))
        with urlopen(url) as response:
            raw = response.read(2_000_001)
        assert len(raw) <= 2_000_000, 'unexpected response size'
        data = json.loads(raw)
        result['pages'].append({'url': url, 'count': data['count'], 'next': data['next'],
                                'sha256': hashlib.sha256(raw).hexdigest()})
        for row in data['results']:
            result['programmes'].append({
                'id': row['id'], 'name': row['name'].strip(),
                'url': BASE + '/education/' + str(row['id']),
                'category_ids': [c['id'] for c in row['categories']],
                'price': row['price'], 'started_at': row['started_at'],
                'flexible_start': row['is_flexible_start'], 'updated_at': row['updated_at'],
            })
        if data['next'] is None:
            break
        url = data['next']
    validate(result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--output', type=Path)
    mode.add_argument('--check', type=Path)
    args = parser.parse_args()
    if args.check:
        snapshot = json.loads(args.check.read_text(encoding='utf-8'))
        validate(snapshot)
    else:
        snapshot = collect()
        args.output.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"OK: {len(snapshot['programmes'])} unique programmes; {len(snapshot['pages'])} pages exhausted")


if __name__ == '__main__':
    main()
