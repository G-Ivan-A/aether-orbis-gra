#!/usr/bin/env python3
"""Evidence for issue #3: the re-import at PIN_SHA changed only bookkeeping.

For every imported file (frontmatter ``source:`` on the Hub) that differs from
a git revision (default HEAD), undo the two intended changes and require the
rest to be identical:

* the ``source:`` frontmatter line (Hub commit of the copy);
* links to the Hub domain pinned to PIN_SHA -> the old form (``main`` or the
  old commit). Other Hub links (rules, standards) must stay as they were.

Usage: python3 -I experiments/check_reimport_diff.py [--rev HEAD] [--pin SHA]
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys

HUB = "https://github.com/G-Ivan-A/hybrid-Intelligence-lab"
DOMAIN = "research/reputation-technologies"


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rev", default="HEAD")
    parser.add_argument("--pin", default="48ebe5230be87ca5bf8a08b385e296a2987e9958")
    args = parser.parse_args()
    pinned = re.compile(re.escape(HUB) + r"/(blob|tree)/" + args.pin + "/(?=" + DOMAIN + ")")
    old_ref = re.compile(re.escape(HUB) + r"/(blob|tree)/(main|[0-9a-f]{40})/(?=" + DOMAIN + ")")
    files = [f for f in git("diff", "--name-only", args.rev).splitlines() if f.endswith(".md")]
    bad = links = checked = 0
    for rel in files:
        old = git("show", f"{args.rev}:{rel}").splitlines()
        if not any(line.startswith(f"source: \"{HUB}/blob/") for line in old[:15]):
            continue
        checked += 1
        new = open(rel, encoding="utf-8").read().splitlines()
        if len(old) != len(new):
            print(f"FAIL {rel}: {len(old)} -> {len(new)} lines")
            bad += 1
            continue
        for n, (a, b) in enumerate(zip(old, new), 1):
            if a == b or (a.startswith("source:") and b.startswith("source:")):
                continue
            links += len(pinned.findall(b))
            if old_ref.sub(r"\1/X/", a) != pinned.sub(r"\1/X/", b):
                print(f"FAIL {rel}:{n}\n  old: {a[:200]}\n  new: {b[:200]}")
                bad += 1
    print(f"{checked} changed imported files ({len(files)} changed Markdown files), {links} pinned links on changed lines, {bad} unexpected changes")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
