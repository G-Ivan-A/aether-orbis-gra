#!/usr/bin/env python3
"""Inventory helper for issue #711.

Extracts every verbatim quote from the course source catalogue of #650
(series Г, Д, С, Н, П, О) into a JSON list: source ID, catalogue line,
locator, quote body exactly as written in the catalogue, and the
translation line that follows it. The script only reads the catalogue.

Usage: python3 extract_650.py [--json OUT] [--dump]
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOGUE = ROOT / "2026-09-30-course-sources-and-presentations-650.md"
REL = "research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md"

ENTRY = re.compile(r"^#{4,5} ([ГДСНПО]\d+[ab]?)[ .(]")
BOLD = re.compile(r"^\s*-\s*\*\*(Цитат[^*]*?)(?::)?\*\*:?\s*(.*)$")
NUMBERED = re.compile(r"^\s{1,4}(\d+)\.\s+(.*)$")
BLOCK = re.compile(r"^\s*-\s*\*\*Цитаты\*\*\s*(?:\((.*)\))?")
TRANSLATION = re.compile(r"(?:Наш перевод|Перевод наш|перевод наш)\*?:\*?\s*(.*)$")
QUOTE_START = ('"', "«", "“", "…", "Галлюцинация")
LOCATOR_LINE = re.compile(r"^\s*-\s*\*\*Локатор:?\*\*:?\s*(.*)$")


def split_numbered(body: str) -> tuple[str | None, str]:
    """Split "p. 4, D.6.d: "quote"" into locator and quote body."""
    if body.startswith(QUOTE_START):
        return None, body
    m = re.match(r'^(.*?):\s+(["«“…].*)$', body)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return None, body


def extract() -> list[dict]:
    lines = CATALOGUE.read_text(encoding="utf-8").splitlines()
    out: list[dict] = []
    current = None
    block_loc = None
    for no, line in enumerate(lines, 1):
        m = ENTRY.match(line)
        if m:
            current, block_loc = m.group(1), None
            continue
        if line.startswith("#"):
            current = None
            continue
        if current is None:
            continue
        t = TRANSLATION.search(line)
        if t and out and out[-1]["id"] == current and "translation" not in out[-1]:
            out[-1]["translation"] = t.group(1).strip()
            out[-1]["translation_line"] = no
            continue
        b = BLOCK.match(line)
        if b:
            block_loc = b.group(1)
            continue
        bm = BOLD.match(line)
        if bm:
            marker, body = bm.group(1), bm.group(2).strip()
            loc = None
            pm = re.search(r"\((.*)\)", marker)
            if pm:
                loc = pm.group(1)
            if ":" in marker and not pm:
                loc = marker.split(":", 1)[1].strip() or None
            if not body or len(body) < 20:
                continue
            if not body.startswith(QUOTE_START):
                inner, body = split_numbered(body)
                loc = inner or loc
            out.append({"id": current, "line": no, "locator": loc or block_loc, "quote": body})
            continue
        nm = NUMBERED.match(line)
        if nm:
            loc, body = split_numbered(nm.group(2).strip())
            if not body.startswith(QUOTE_START) or len(body) < 20:
                continue
            out.append({"id": current, "line": no, "n": int(nm.group(1)), "locator": loc or block_loc, "quote": body})
            continue
        lm = LOCATOR_LINE.match(line)
        if lm:
            block_loc = lm.group(1).rstrip(".")
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json")
    parser.add_argument("--dump", action="store_true")
    args = parser.parse_args()
    items = extract()
    for it in items:
        it["file"] = REL
    if args.json:
        Path(args.json).write_text(json.dumps(items, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if args.dump:
        for it in items:
            print(f"{it['id']}\tL{it['line']}\t[{it.get('locator')}]\t{it['quote'][:90]}\t|T: {it.get('translation','-')[:40]}")
    print(f"quotes: {len(items)}; sources: {len({i['id'] for i in items})}")


if __name__ == "__main__":
    main()
