#!/usr/bin/env python3
"""Evidence for issue #9 (GRA-003, GRA-004): the re-import changed only links.

For every imported Markdown file that differs from a git revision (default
HEAD) the check requires the same number of lines and, on each changed line,
the same text outside links and the same number of links. A changed link must
be one of two intended changes:

* GRA-003: a link pinned to PIN_SHA on the catalogue #650 became a relative
  link to the local copy ``course-sources-and-presentations.md``. When the old
  link had a line anchor ``#Lnnn``, the line of the Hub file at the archive
  commit must equal the line of the copy behind the new anchor (lines are
  compared after removing link targets, which the import rewrites); a heading
  anchor must stay the same (validate_repo.py checks that it exists);
* GRA-004: a link to the personal-data file became its label followed by the
  note without personal data.

The new catalogue copy and the quotes document banner are reported separately.

Usage: python3 -I experiments/check_gra_003_004_diff.py --hub /tmp/hub [--rev HEAD]
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

HUB = "https://github.com/G-Ivan-A/hybrid-Intelligence-lab"
DOMAIN = "research/reputation-technologies"
PIN = "48ebe5230be87ca5bf8a08b385e296a2987e9958"
ARCHIVE = "51869aa50f14a0bc8f69f8b426e216244f16c970"
CATALOGUE_HUB = "2026-09-30-course-sources-and-presentations-650.md"
CATALOGUE = "education/technograd-reputation-engineering/course-sources-and-presentations.md"
PII = "2026-10-14-day1-lecturer-gra-research.md"
LINK = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)\)")
OLD_CATALOGUE = re.compile(re.escape(f"{HUB}/blob/{PIN}/{DOMAIN}/{CATALOGUE_HUB}") + r"(#L(\d+)(?:-L(\d+))?)?(#[^L].*)?$")
NEW_CATALOGUE = re.compile(
    r"(?:\.\./)*(?:education/technograd-reputation-engineering/)?course-sources-and-presentations\.md"
    r"(#L(\d+)(?:-L(\d+))?)?(#[^L].*)?$"
)
NOTE_START = "(ссылка не приводится: файл Хаба содержит персональные данные"


def git(*args: str, cwd: str | None = None) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True, cwd=cwd).stdout


def strip_targets(line: str) -> str:
    """Line text with link targets removed (labels kept), to compare Hub and copy lines."""
    return LINK.sub(lambda m: f"{m.group(1)}[{m.group(2)}]()", line).strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hub", required=True)
    parser.add_argument("--rev", default="HEAD")
    args = parser.parse_args()
    hub_lines = git("show", f"{ARCHIVE}:{DOMAIN}/{CATALOGUE_HUB}", cwd=args.hub).splitlines()
    copy_lines = Path(CATALOGUE).read_text(encoding="utf-8").splitlines()
    files = [f for f in git("diff", "--name-only", args.rev).splitlines() if f.endswith(".md")]
    bad = catalogue_links = anchored = redactions = 0
    for rel in files:
        old = git("show", f"{args.rev}:{rel}").splitlines()
        new = Path(rel).read_text(encoding="utf-8").splitlines()
        if len(old) != len(new):
            print(f"FAIL {rel}: {len(old)} -> {len(new)} lines")
            bad += 1
            continue
        for n, (a, b) in enumerate(zip(old, new), 1):
            if a == b:
                continue
            if rel.endswith("course-quotes-days-1-4-alce.md") and a.startswith("> ") and "#650" in a + b:
                print(f"banner {rel}:{n}: {b}")
                continue
            # GRA-004: the redacted link has no target any more; restore it for comparison.
            for m in LINK.finditer(a):
                if m.group(3).endswith(PII) and f"{m.group(2)} {NOTE_START}" in b:
                    redactions += 1
            b_cmp = re.sub(r" \(ссылка не приводится: [^)]*\)", "", b)
            a_cmp = re.sub(r"\[([^\]]*)\]\([^)\s]*" + re.escape(PII) + r"\)", r"\1", a)
            old_links, new_links = LINK.findall(a_cmp), LINK.findall(b_cmp)
            if LINK.sub("", a_cmp) != LINK.sub("", b_cmp) or len(old_links) != len(new_links):
                print(f"FAIL {rel}:{n} text outside links changed\n  old: {a[:300]}\n  new: {b[:300]}")
                bad += 1
                continue
            for (_, ol, ou), (_, nl, nu) in zip(old_links, new_links):
                if (ol, ou) == (nl, nu):
                    continue
                om, nm = OLD_CATALOGUE.match(ou), NEW_CATALOGUE.match(nu)
                if not (om and nm):
                    print(f"FAIL {rel}:{n} unexpected link change {ol}({ou}) -> {nl}({nu})")
                    bad += 1
                    continue
                catalogue_links += 1
                if om.group(4) != nm.group(4):
                    print(f"FAIL {rel}:{n} heading anchor changed: {ou} -> {nu}")
                    bad += 1
                    continue
                if bool(om.group(1)) != bool(nm.group(1)):
                    print(f"FAIL {rel}:{n} anchor lost or added: {ou} -> {nu}")
                    bad += 1
                    continue
                if om.group(1):
                    anchored += 1
                    pairs = [(int(om.group(2)), int(nm.group(2)))]
                    if om.group(3) or nm.group(3):
                        pairs.append((int(om.group(3) or 0), int(nm.group(3) or 0)))
                    for hub_n, copy_n in pairs:
                        if not (0 < hub_n <= len(hub_lines) and 0 < copy_n <= len(copy_lines)) or \
                                strip_targets(hub_lines[hub_n - 1]) != strip_targets(copy_lines[copy_n - 1]):
                            print(f"FAIL {rel}:{n} Hub line {hub_n} != copy line {copy_n}")
                            bad += 1
    print(f"{len(files)} changed Markdown files; {catalogue_links} catalogue #650 links made local "
          f"({anchored} with line anchors, every anchored line equal in the Hub file and the copy); "
          f"{redactions} personal-data links replaced by the note; {bad} unexpected changes")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
