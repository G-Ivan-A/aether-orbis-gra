#!/usr/bin/env python3
"""Evidence for issue #3 (Hub RFC #721, step 2.2): line anchors of the quotes list.

For every link of the Hub quotes list with a ``#Lnnn`` anchor this script
compares the Hub line it pointed to (at PIN_SHA) with the line the imported
copy points to now:

* link to a copy in this repository -> the two lines must carry the same text
  once links are stripped (the copy rewrites links, nothing else);
* link pinned to the Hub -> it must be the same file and line at PIN_SHA.

Usage (Hub clone checked out at PIN_SHA, read as data only):
    python3 -I experiments/verify_quote_anchors.py --hub /tmp/hub --root .
"""
from __future__ import annotations

import argparse
import posixpath
import re
import sys
from pathlib import Path

HUB_URL = "https://github.com/G-Ivan-A/hybrid-Intelligence-lab"
DOMAIN = "research/reputation-technologies"
HUB_DOC = f"{DOMAIN}/2026-11-01-course-quotes-days-1-4-alce.md"
COPY = "education/technograd-reputation-engineering/handouts/course-quotes-days-1-4-alce.md"
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")


def strip_links(line: str) -> str:
    """Keep link labels only; drop the bookkeeping a copy may change."""
    line = LINK.sub(lambda m: m.group(1), line)
    return re.sub(r"\s+", " ", line).strip()


def line_links(text: str) -> list[tuple[str, str]]:
    return [(m.group(1), m.group(2)) for m in LINK.finditer(text) if re.search(r"#L\d+", m.group(2))]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hub", type=Path, required=True)
    parser.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()
    hub_links = line_links((args.hub / HUB_DOC).read_text(encoding="utf-8"))
    copy_links = line_links((args.root / COPY).read_text(encoding="utf-8"))
    if len(hub_links) != len(copy_links):
        print(f"FAIL: {len(hub_links)} line links in the Hub, {len(copy_links)} in the copy")
        return 1
    stats: dict[str, int] = {}
    failures = 0
    for (_, hub_url), (label, url) in zip(hub_links, copy_links):
        hub_path, _, hub_anchor = hub_url.split("/blob/main/", 1)[1].partition("#")
        hub_line = int(hub_anchor[1:].split("-")[0])
        hub_text = (args.hub / hub_path).read_text(encoding="utf-8").splitlines()[hub_line - 1]
        if url.startswith(HUB_URL):
            ok = url.split("/blob/", 1)[1].split("/", 1)[1] == hub_url.split("/blob/main/", 1)[1]
            kind = f"pinned {posixpath.basename(hub_path)}"
        else:
            path, _, anchor = url.partition("#")
            target = posixpath.normpath(posixpath.join(posixpath.dirname(COPY), path))
            line = int(anchor[1:].split("-")[0])
            copy_text = (args.root / target).read_text(encoding="utf-8").splitlines()[line - 1]
            ok = strip_links(copy_text) == strip_links(hub_text) and f"строка {line}" in label
            kind = f"copy {target} (Hub L{hub_line} -> L{line}, shift {line - hub_line:+d})"
            kind_key = f"copy {target}"
            stats[kind_key + " ok" if ok else kind_key + " FAIL"] = stats.get(kind_key + (" ok" if ok else " FAIL"), 0) + 1
            if not ok:
                print(f"FAIL: {kind}\n  hub:  {hub_text[:200]}\n  copy: {copy_text[:200]}")
                failures += 1
            continue
        stats[kind + (" ok" if ok else " FAIL")] = stats.get(kind + (" ok" if ok else " FAIL"), 0) + 1
        failures += not ok
    for key in sorted(stats):
        print(f"{stats[key]:4d}  {key}")
    print(("FAIL" if failures else "PASS") + f": {len(copy_links)} line links checked, {failures} failures")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
