#!/usr/bin/env python3
"""Retrieve the pinned Mango release into an external directory; read-only audit.

No checkout, dependency installation, generation or deployment. Each response is
bounded to 4 MiB; 22 candidate assets and four live responses are read serially.
"""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from urllib.parse import quote
from urllib.request import urlopen

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = 'e6a72240ba5f7b121f42e2446d9bd7fa341f753c'
LIVE = 'https://g-ivan-a.github.io/mango_ba_prompts/'
LIMIT = 4 * 1024 * 1024


def digest(body):
    return hashlib.sha256(body).hexdigest()


def normalized(value):
    if isinstance(value, dict):
        return {k: normalized(v) for k, v in value.items() if k != 'generatedAt'}
    if isinstance(value, list):
        return [normalized(v) for v in value]
    return value


def signature(body, name):
    if name.endswith('.json'):
        body = json.dumps(normalized(json.loads(body)), ensure_ascii=False,
                          sort_keys=True, separators=(',', ':')).encode()
    return digest(body)


def fetch(url):
    with urlopen(quote(url, safe=':/'), timeout=30) as response:
        body = response.read(LIMIT + 1)
    if len(body) > LIMIT:
        raise ValueError('response exceeds 4 MiB')
    return body


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True,
                        help='new external directory for site/, live/ and audit.json')
    args = parser.parse_args()
    out = args.output.resolve()
    if out == ROOT or ROOT in out.parents:
        parser.error('output must be outside this repository')
    if out.exists():
        parser.error('use a new output directory to preserve earlier observations')
    out.mkdir(parents=True)
    inherited = json.loads((HERE / 'inherited-site-audit.json').read_text())
    assets, changed = {}, []
    for name, old in inherited['assets'].items():
        path = PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or not path.parts or path.parts[0] != 'site':
            raise ValueError('unsafe deployment path')
        body = fetch(f'https://raw.githubusercontent.com/G-Ivan-A/mango_ba_prompts/{BASE}/{name}')
        target = out / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(body)
        record = {'sha256': digest(body), 'bytes': len(body)}
        if name.endswith('.json'):
            record['normalized_sha256'] = signature(body, name)
        expected = old.get('normalized_sha256', old['sha256'])
        if signature(body, name) != expected:
            changed.append(name)
        assets[name] = record
    live = {}
    for name in ('index.html', 'data/stats.json', 'data/prompts.json', 'data/test-kit.json'):
        body = fetch(LIVE + name)
        target = out / 'live' / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(body)
        live[name] = {'sha256': digest(body), 'bytes': len(body)}
    read = lambda name: json.loads((out / name).read_text())
    old_ids = {p['id'] for p in read('live/data/prompts.json')['prompts']}
    new_ids = {p['id'] for p in read('site/data/prompts.json')['prompts']}
    report = {
        'accessed_at': datetime.now(timezone.utc).isoformat(),
        'baseline_sha': BASE, 'live_url': LIVE,
        'live_version': read('live/data/stats.json')['siteVersion'],
        'candidate_version': read('site/data/stats.json')['siteVersion'],
        'live_totals': read('live/data/stats.json')['totals'],
        'candidate_totals': read('site/data/stats.json')['totals'],
        'catalogue_ids_preserved': sorted(old_ids & new_ids),
        'catalogue_ids_removed': sorted(old_ids - new_ids),
        'catalogue_ids_added': sorted(new_ids - old_ids),
        'inherited_candidate_semantic_changes': changed,
        'normalization': 'Ignore generatedAt only; inherited 22-asset manifest excludes screenshots.',
        'live': live, 'assets': assets,
    }
    (out / 'audit.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    if changed or old_ids - new_ids:
        raise SystemExit('comparison failed; inspect audit.json')
    print(f'{len(assets)} assets; {len(old_ids)} live IDs preserved; {len(new_ids-old_ids)} added')


if __name__ == '__main__':
    main()
