#!/usr/bin/env python3
"""Length check and printable rendering of the PSB / Academy brief.

Check (stdlib only, used by unittest CI):
    python3 experiments/issue-7/brief.py check

Render a two-page A4 PDF with clickable links (needs `markdown`, `pypdf`
and a headless Chrome/Chromium; run manually, the result is committed):
    python3 experiments/issue-7/brief.py render --ref <commit-sha>

A typewritten page (машинописная страница) is counted as 1800 characters
with spaces, so the owner's limit "не более 2х машинописных листов" is
3600 visible characters: link URLs, Markdown markup and front matter are
not visible to the reader and are not counted.
"""
import argparse
import hashlib
import json
import posixpath
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPOSITORY = 'G-Ivan-A/aether-orbis-gra'
BRIEF = ROOT / 'docs/analysis/2026-11-09-issue-7-psb-academy-brief.md'
PDF = BRIEF.with_suffix('.pdf')
MANIFEST = HERE / 'brief-render.json'
PAGE_CHARS = 1800
MAX_PAGES = 2
MAX_CHARS = PAGE_CHARS * MAX_PAGES
LINK = re.compile(r'\[([^\]]*)\]\(([^)\s]+)\)')
MARKERS = re.compile('[\u25cf\u25d0\u25cb]')

CSS = """
@page { size: A4; margin: 14mm 15mm 13mm 15mm; }
body { font-family: 'DejaVu Sans', 'Liberation Sans', Arial, sans-serif;
       font-size: 10.6pt; line-height: 1.36; color: #111; }
h1 { font-size: 15pt; margin: 0 0 4pt; }
h2 { font-size: 12pt; margin: 9pt 0 3pt; border-bottom: 1px solid #bbb; }
p, ul { margin: 3pt 0; }
ul { padding-left: 14pt; }
li { margin: 1.5pt 0; }
table { border-collapse: collapse; width: 100%; margin: 3pt 0; }
th, td { border: 1px solid #bbb; padding: 1.5pt 4pt; text-align: left; }
th { background: #f0f0f0; }
a { color: #0645ad; text-decoration: none; }
/* Liberation Sans draws only half of U+25D0; FreeSans has full markers */
.mk { font-family: 'DejaVu Sans', 'FreeSans', 'FreeSerif', sans-serif; }
.footer { margin-top: 6pt; font-size: 7.5pt; color: #555; }
"""


def split_front_matter(text):
    if text.startswith('---\n'):
        end = text.index('\n---\n', 4)
        return text[4:end], text[end + 5:]
    return '', text


def visible_text(markdown_text):
    """Text a reader sees: no front matter, URLs, table rules or markup."""
    _, body = split_front_matter(markdown_text)
    body = LINK.sub(r'\1', body)
    lines = []
    for line in body.splitlines():
        if re.fullmatch(r'\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*', line):
            continue
        line = re.sub(r'^\s*#{1,6}\s+', '', line)
        line = re.sub(r'^\s*[-*]\s+', '', line)
        line = line.replace('**', '').replace('`', '')
        line = ' '.join(cell.strip() for cell in line.split('|') if cell.strip())
        lines.append(line)
    return re.sub(r'\s+', ' ', ' '.join(lines)).strip()


def links(markdown_text):
    return [url for _, url in LINK.findall(split_front_matter(markdown_text)[1])]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(brief=BRIEF, pdf=PDF, manifest_path=MANIFEST):
    text = brief.read_text(encoding='utf-8')
    chars = len(visible_text(text))
    if chars > MAX_CHARS:
        raise ValueError(f'brief has {chars} visible characters, limit {MAX_CHARS}')
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    if manifest['source_sha256'] != sha256(brief):
        raise ValueError('PDF is stale: re-render the brief')
    if manifest['pdf_sha256'] != sha256(pdf):
        raise ValueError('PDF does not match its render manifest')
    if not 1 <= manifest['pages'] <= MAX_PAGES:
        raise ValueError(f'PDF has {manifest["pages"]} pages, limit {MAX_PAGES}')
    return chars, manifest['pages']


def absolute(url, ref):
    """Relative repository link -> permalink pinned to a commit."""
    if re.match(r'^[a-z]+:', url) or url.startswith('#'):
        return url
    path, _, anchor = url.partition('#')
    target = posixpath.normpath(posixpath.join(
        posixpath.dirname(BRIEF.relative_to(ROOT).as_posix()), path))
    return (f'https://github.com/{REPOSITORY}/blob/{ref}/{target}'
            + (f'#{anchor}' if anchor else ''))


def render(ref, chrome):
    import markdown  # pylint: disable=import-outside-toplevel
    from pypdf import PdfReader  # pylint: disable=import-outside-toplevel

    text = BRIEF.read_text(encoding='utf-8')
    _, body = split_front_matter(text)
    body = LINK.sub(lambda m: f'[{m.group(1)}]({absolute(m.group(2), ref)})', body)
    html_body = markdown.markdown(body, extensions=['tables', 'sane_lists'])
    html_body = MARKERS.sub(r'<span class="mk">\g<0></span>', html_body)
    source = f'https://github.com/{REPOSITORY}/blob/{ref}/{BRIEF.relative_to(ROOT).as_posix()}'
    page = (f'<!doctype html><html lang="ru"><head><meta charset="utf-8">'
            f'<title>Резюме: Академия ПСБ и ПСБ</title><style>{CSS}</style></head>'
            f'<body>{html_body}<p class="footer">Источник документа: '
            f'<a href="{source}">{source}</a></p></body></html>')
    with tempfile.TemporaryDirectory() as tmp:
        html_path = Path(tmp) / 'brief.html'
        html_path.write_text(page, encoding='utf-8')
        subprocess.run([chrome, '--headless', '--no-sandbox', '--disable-gpu',
                        '--no-pdf-header-footer', f'--print-to-pdf={PDF}',
                        html_path.as_uri()], check=True, capture_output=True, timeout=120)
    pages = len(PdfReader(PDF).pages)
    manifest = {
        'source': BRIEF.relative_to(ROOT).as_posix(),
        'source_sha256': sha256(BRIEF),
        'links_pinned_to': ref,
        'pdf': PDF.relative_to(ROOT).as_posix(),
        'pdf_sha256': sha256(PDF),
        'pages': pages,
        'visible_characters': len(visible_text(text)),
        'limit_characters': MAX_CHARS,
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n',
                        encoding='utf-8')
    return manifest


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('check')
    sub.add_parser('count')
    rend = sub.add_parser('render')
    rend.add_argument('--ref', required=True, help='commit SHA for permalinks')
    rend.add_argument('--chrome', default=shutil.which('google-chrome')
                      or shutil.which('chromium') or 'chromium')
    args = parser.parse_args(argv)
    if args.command == 'count':
        print(len(visible_text(BRIEF.read_text(encoding='utf-8'))), 'of', MAX_CHARS)
    elif args.command == 'check':
        chars, pages = check()
        print(f'Brief: {chars}/{MAX_CHARS} visible characters, {pages} PDF page(s): OK')
    else:
        print(json.dumps(render(args.ref, args.chrome), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    sys.exit(main())
