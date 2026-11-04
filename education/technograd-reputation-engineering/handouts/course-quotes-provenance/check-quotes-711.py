#!/usr/bin/env python3
"""Gate check of the quote list of issue #711.

Reads the generated Markdown file itself (independently of build_quotes_711.py)
and checks that:
  * the file exists, has frontmatter without "ai-generated" and the sections
    День 1 … День 4, «Границы списка», «Пробелы и решения», «Список источников (ALCE)";
  * every quote block has the fields of the issue: quote, interpretation, authors,
    date, full source title, link — plus place in source, status, repository line;
  * the source title is given without abbreviations: no author list in initials
    before it, no pp., No., №, С., «88 с.», ПАО and similar; the place in
    source has no p., с., стр., Sec., Ch., П., et al. and no status;
  * every quote is verbatim on the repository line it links to; every translation
    taken from the repository is verbatim on the line it links to; every original
    marked «Сверка с источником» is verbatim in source-excerpts-711.txt;
  * every epigraph of slide N is on its line of the Day 4 deck;
  * ALCE: every [n] resolves to an entry of the reference list, every entry is
    used, one source key per number, numbers in order of first use;
  * coverage: every quote of the #650 catalogue (extract_650.py) is in the list.

  --self-test  also checks that each artificial corruption is rejected.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(HERE))
import extract_650  # noqa: E402

REL = "research/reputation-technologies/2026-11-01-course-quotes-days-1-4-alce.md"
TARGET = REPO / REL
EXCERPTS = HERE / "source-excerpts-711.txt"
DECK = "research/reputation-technologies/2026-11-03-day4-presentation-gamma-v5.md"
CAT = "research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md"
BLOB = "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/"
DAY_TITLES = ["## День 1.", "## День 2.", "## День 3.", "## День 4."]
TAIL_SECTIONS = ["## Границы списка", "## Пробелы и решения", "## Список источников (ALCE)"]
FIELDS = ["Интерпретация для репутационных технологий", "Авторы", "Дата", "Источник", "Ссылка",
          "Место в источнике", "Статус проверки", "Где в репозитории"]
STATUSES = ("VERIFIED-FULLTEXT", "VERIFIED-SECONDARY", "VERIFIED-ABSTRACT", "VERIFIED (колода v5")
EXTRA_QUOTES = 41  # quotes outside the #650 inventory: Г12, М1–М7, R:Simini, R:Gentner, Д3-Т3…Т5, Day 4 epigraphs
LINK = re.compile(r"\[([^\]]+), строка (\d+)\]\(" + re.escape(BLOB) + r"([^)#]+)#L(\d+)\)")
HEAD = re.compile(r"^### (\d)\.(\d+)\. (.+) — (\S+) \[(\d+)\]$")
REF = re.compile(r"^\[(\d+)\] (.+) Ключ в материалах курса: (\S+)\.$")
CYR = re.compile(r"[А-Яа-яЁё]")
# «полное название источника без сокращений»: no citation-style author list in
# initials before the title and no bibliographic abbreviations.
TITLE_LEAD = re.compile(r"^(?:van den |van der )?[A-ZА-ЯЁ][^\s,.()]*(?: [A-ZА-ЯЁ]\.(?:-[A-ZА-ЯЁ]\.)?)+[ ,]")
LOCATOR_ABBREV = re.compile(r"\b(?:pp|[pP]|[сС]|стр)\. ?(?:[A-Z]-)?\d|\b(?:Sec|sect|Ch|Разд|П|п|прим|al)\. |VERIFIED")
TITLE_ABBREV = re.compile(r"\b(?:pp|No|Vol|Nr|ed|eds|et al)\.|№|(?:^|[\s(])[Сс]\. \d|\d с\.|\bПАО\b|\bСПб\b|(?:^|\s)М\.:|\bТ\. \d|\bВып\.")
OUTER = "\"«»“”„"


def strip_quote(text: str) -> str:
    text = re.sub(r" \[\d+\]$", "", text.strip())
    if len(text) > 2 and text[0] in OUTER and text.rstrip(".")[-1] in OUTER:
        text = text.rstrip(".")[1:-1]
    return text


_lines: dict[str, list[str]] = {}


def repo_line(rel: str, n: int) -> str:
    if rel not in _lines:
        path = REPO / rel
        _lines[rel] = path.read_text(encoding="utf-8").splitlines() if path.is_file() else []
    lines = _lines[rel]
    return lines[n - 1] if 0 < n <= len(lines) else ""


def excerpts(text: str) -> dict[str, str]:
    blocks = re.findall(r"^=== (\S+) \|[^\n]*\n(.*?)(?=\n\n=== |\n*\Z)", text, re.S | re.M)
    return {k: " ".join(v.split()) for k, v in blocks}


def validate(text: str, excerpt_text: str) -> list[str]:
    errors: list[str] = []
    if not text:
        return [f"{REL}: file not found"]
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not fm:
        errors.append("frontmatter missing")
    else:
        for key in ("status:", "version:", "updated:", "source:"):
            if key not in fm.group(1):
                errors.append(f"frontmatter lacks {key}")
        if "ai-generated" in fm.group(1):
            errors.append("frontmatter must not contain ai-generated")
        if "issues/711" not in fm.group(1):
            errors.append("frontmatter source does not name issue #711")
    if "ALCE" not in text.split("## День 1.")[0]:
        errors.append("intro does not explain the ALCE markup")
    lines = text.splitlines()
    pos = []
    for title in DAY_TITLES + TAIL_SECTIONS:
        idx = [i for i, l in enumerate(lines) if l.startswith(title)]
        if len(idx) != 1:
            errors.append(f"section {title!r} must appear exactly once")
            pos.append(-1)
        else:
            pos.append(idx[0])
    if -1 not in pos and pos != sorted(pos):
        errors.append("sections out of order")
    if errors:
        return errors

    # reference list
    refs: dict[int, str] = {}
    for l in lines[pos[-1] + 1:]:
        if not l.strip():
            continue
        m = REF.match(l)
        if not m:
            errors.append(f"reference list: malformed entry {l[:60]!r}")
            continue
        n, body, key = int(m.group(1)), m.group(2), m.group(3)
        if n in refs:
            errors.append(f"reference [{n}] duplicated")
        refs[n] = key
        if "https://" not in body:
            errors.append(f"reference [{n}] has no https link")
        if not any(s in body for s in STATUSES) or "UNVERIFIED" in body:
            errors.append(f"reference [{n}] has no verified status")
    if sorted(refs) != list(range(1, len(refs) + 1)):
        errors.append("reference numbers are not 1..N")

    for i, l in enumerate(lines):
        if l.startswith("- **Место в источнике:** "):
            m = LOCATOR_ABBREV.search(l)
            if m:
                errors.append(f"line {i + 1}: abbreviation {m.group(0)!r} in place in source")
        if l.startswith("- **Источник:** "):
            title = l[len("- **Источник:** "):]
            if TITLE_LEAD.match(title):
                errors.append(f"line {i + 1}: source title starts with an author list in initials: {title[:50]!r}")
            m = TITLE_ABBREV.search(title)
            if m:
                errors.append(f"line {i + 1}: abbreviation {m.group(0).strip()!r} in source title {title[:50]!r}")

    exc = excerpts(excerpt_text)
    blocks = []
    for d in range(4):
        start, end = pos[d], pos[d + 1]
        cur = None
        for i in range(start + 1, end):
            l = lines[i]
            if l.startswith("### "):
                m = HEAD.match(l)
                if not m:
                    errors.append(f"line {i + 1}: malformed quote heading")
                    cur = None
                    continue
                cur = dict(day=int(m.group(1)), k=int(m.group(2)), key=m.group(4), n=int(m.group(5)),
                           at=i + 1, quote=None, fields={}, sec=d + 1)
                blocks.append(cur)
            elif cur is not None and l.startswith("> "):
                cur["quote"] = l[2:]
            elif cur is not None and l.startswith("- **"):
                m = re.match(r"- \*\*([^*]+):\*\* (.*)$", l)
                if m:
                    cur["fields"][m.group(1)] = m.group(2)
    seen_order: list[int] = []
    used: set[int] = set()
    covered: set[tuple[str, int]] = set()
    for b in blocks:
        where = f"{b['day']}.{b['k']} ({b['key']})"
        if b["day"] != b["sec"]:
            errors.append(f"{where}: numbered for day {b['day']} but placed under day {b['sec']}")
        n = b["n"]
        if n not in refs:
            errors.append(f"{where}: [{n}] does not resolve to the reference list")
        elif refs[n] != b["key"]:
            errors.append(f"{where}: [{n}] resolves to {refs[n]}, heading names {b['key']}")
        used.add(n)
        if n not in seen_order:
            seen_order.append(n)
        f = b["fields"]
        for name in FIELDS:
            if not f.get(name, "").strip():
                errors.append(f"{where}: field «{name}» missing")
        if errors and errors[-1].startswith(where + ": field"):
            continue
        q = b["quote"]
        if not q or not q.endswith(f" [{n}]"):
            errors.append(f"{where}: quote line missing or not marked [{n}]")
            continue
        interp = f["Интерпретация для репутационных технологий"]
        if not interp.endswith(f" [{n}]") or len(interp) < 60 or "НЕТ ИНТЕРПРЕТАЦИИ" in interp:
            errors.append(f"{where}: interpretation missing, too short or not marked [{n}]")
        if not f["Ссылка"].startswith("https://"):
            errors.append(f"{where}: link is not https")
        if not f["Статус проверки"].startswith(STATUSES):
            errors.append(f"{where}: status {f['Статус проверки']!r} is not a verified status")
        for name in ("Авторы", "Дата", "Источник"):
            if "UNVERIFIED" in f[name]:
                errors.append(f"{where}: {name} mentions UNVERIFIED")
        locs = LINK.findall(f["Где в репозитории"])
        if not locs:
            errors.append(f"{where}: repository line link missing")
            continue
        label, ln, rel, ln2 = locs[0]
        if ln != ln2 or label != rel.split("/")[-1]:
            errors.append(f"{where}: repository link label and target differ")
            continue
        line = repo_line(rel, int(ln))
        quote = strip_quote(q)
        tr = f.get("Перевод", "")
        course = "перевод курса" in tr
        if not CYR.search(quote[:80]) and not tr:
            errors.append(f"{where}: quote in a foreign language without translation")
        if course:
            tr_text = strip_quote(tr.split(" (перевод курса")[0])
            if tr_text not in line:
                errors.append(f"{where}: course translation is not verbatim on {rel}:{ln}")
        elif quote not in line:
            errors.append(f"{where}: quote is not verbatim on {rel}:{ln}")
        if rel == CAT:
            covered.add((rel, int(ln)))
        if tr and "перевод наш (#711)" not in tr and not course:
            tl = LINK.findall(tr)
            if not tl:
                errors.append(f"{where}: repository translation has no line link")
            else:
                _, tln, trel, _ = tl[0]
                if strip_quote(tr.split(" (")[0]) not in repo_line(trel, int(tln)):
                    errors.append(f"{where}: translation is not verbatim on {trel}:{tln}")
        if "Сверка с источником" in f:
            key = re.search(r"под ключом `([^`]+)`", f["Сверка с источником"])
            orig = " ".join(quote.split()).strip("…").rstrip(".")
            if not key or orig not in exc.get(key.group(1), ""):
                errors.append(f"{where}: original is not verbatim in source-excerpts-711.txt")
        elif course:
            errors.append(f"{where}: course translation without «Сверка с источником»")
        slide = re.search(r"эпиграф слайда (\d+)", f["Где в репозитории"])
        if slide:
            deck_links = [x for x in locs if x[2] == DECK]
            if not deck_links:
                errors.append(f"{where}: epigraph of slide {slide.group(1)} has no deck line link")
            else:
                dline = repo_line(DECK, int(deck_links[-1][1]))
                deck_text = f["Где в репозитории"].split("в колоде: ", 1)[-1] if rel != DECK else ""
                if not dline.startswith("- Эпиграф: ") or (deck_text and deck_text not in dline):
                    errors.append(f"{where}: slide {slide.group(1)} epigraph does not match the deck line")
    if seen_order != sorted(seen_order):
        errors.append("ALCE numbers are not in order of first use")
    unused = sorted(set(refs) - used)
    if unused:
        errors.append(f"reference entries never cited: {unused}")
    body = "\n".join(lines[:pos[-1]])
    for m in re.finditer(r"(?<![\w\]])\[(\d{1,3})\](?!\()", body):
        if int(m.group(1)) not in refs:
            errors.append(f"marker [{m.group(1)}] does not resolve")
    inventory = {(CAT, it["line"]) for it in extract_650.extract()}
    missing = sorted(l for _, l in inventory - covered)
    if missing:
        errors.append(f"catalogue quotes missing from the list (lines): {missing[:10]}")
    if len(blocks) != len(inventory) + EXTRA_QUOTES:
        errors.append(f"expected {len(inventory) + EXTRA_QUOTES} quotes, found {len(blocks)}")
    return errors


def first_block(text: str, needle: str) -> tuple[int, int]:
    i = text.index(needle)
    j = text.index("\n### ", i + 1)
    return i, j


def mutate(old: str, new: str, count: int = 1):
    def f(t: str, e: str) -> tuple[str, str]:
        assert old in t, old
        return t.replace(old, new, count), e
    return f


def drop_block(t: str, e: str) -> tuple[str, str]:
    i, j = first_block(t, "\n### 1.2. ")
    return t[:i] + t[j:], e


MUTATIONS = {
    "quote word changed": mutate("The factor of distance", "The factor of distanse"),
    "interpretation removed": lambda t, e: (re.sub(r"(Интерпретация для репутационных технологий:\*\* ).*?( \[1\])", r"\1НЕТ ИНТЕРПРЕТАЦИИ\2", t, count=1), e),
    "authors field dropped": lambda t, e: (re.sub(r"\n- \*\*Авторы:\*\* [^\n]*", "", t, count=1), e),
    "date field dropped": lambda t, e: (re.sub(r"\n- \*\*Дата:\*\* [^\n]*", "", t, count=1), e),
    "source title dropped": lambda t, e: (re.sub(r"\n- \*\*Источник:\*\* [^\n]*", "", t, count=1), e),
    "link not https": lambda t, e: (re.sub(r"(\*\*Ссылка:\*\* )https://", r"\1http://", t, count=1), e),
    "marker does not resolve": lambda t, e: (t.replace("> \"The factor of distance", "> \"The factor of distance", 1).replace(" [1]\n\n- **Перевод", " [999]\n\n- **Перевод", 1), e),
    "reference entry removed": lambda t, e: (re.sub(r"\n\[1\] [^\n]*\n", "\n", t, count=1), e),
    "status UNVERIFIED": lambda t, e: (re.sub(r"(Статус проверки:\*\* )VERIFIED-FULLTEXT", r"\1UNVERIFIED", t, count=1), e),
    "repository line shifted": lambda t, e: (re.sub(r"строка 546\]\((.*?)#L546\)", r"строка 547](\1#L547)", t, count=1), e),
    "quote block dropped": drop_block,
    "day section missing": mutate("## День 3.", "## Day 3."),
    "ai-generated in frontmatter": mutate("status: draft", "status: draft\nai-generated: true"),
    "catalogue translation changed": mutate("«Фактор расстояния может", "«Фактор дистанции может"),
    "course translation changed": mutate("«видимость или потенциал активности в коммуникации»", "«заметность или потенциал активности в коммуникации»"),
    "original not in excerpts": lambda t, e: (t, e.replace("the visibility or the potential for activity in communication", "the visibility of activity in communication", 1)),
    "epigraph deck text changed": lambda t, e: (re.sub(r"(в колоде: )«", r"\1«Якобы ", t, count=1), e),
    "block under wrong day": lambda t, e: (t.replace("### 1.1. ", "### 2.1. ", 1), e),
    "heading key differs from reference": lambda t, e: (re.sub(r"— Г1 \[1\]", "— Г3 [1]", t, count=1), e),
    "source title in citation style": mutate("- **Источник:** Shaping the World", "- **Источник:** Tinbergen J. Shaping the World"),
    "abbreviated pages in source title": mutate("Trade Flows», pages 262–293", "Trade Flows», pp. 262–293"),
    "Russian abbreviations in source title": mutate("2013. Номер 4. Страницы 133–154", "2013. № 4. С. 133–154"),
    "abbreviated page in place in source": mutate("- **Место в источнике:** страница 263", "- **Место в источнике:** p. 263"),
    "foreign quote without translation": lambda t, e: (re.sub(r"\n- \*\*Перевод:\*\* [^\n]*", "", t, count=1), e),
}


def self_test(text: str, excerpt_text: str) -> int:
    failed = 0
    for name, fn in MUTATIONS.items():
        t, e = fn(text, excerpt_text)
        if (t, e) == (text, excerpt_text):
            print(f"FAIL: self-test {name!r}: mutation did not change the input")
            failed += 1
        elif not validate(t, e):
            print(f"FAIL: self-test {name!r} was not rejected")
            failed += 1
    return failed


def main() -> int:
    text = TARGET.read_text(encoding="utf-8") if TARGET.is_file() else ""
    excerpt_text = EXCERPTS.read_text(encoding="utf-8") if EXCERPTS.is_file() else ""
    errors = validate(text, excerpt_text)
    for e in errors:
        print(f"FAIL: {e}")
    if errors:
        return 1
    n = len(re.findall(r"^### \d\.\d+\. ", text, re.M))
    refs = len(re.findall(r"^\[\d+\] ", text, re.M))
    print(f"PASS: {REL}: {n} quotes, {refs} ALCE references, all fields present, all quotes verbatim")
    if "--self-test" in sys.argv:
        failed = self_test(text, excerpt_text)
        if failed:
            return 1
        print(f"PASS: {len(MUTATIONS)} broken fixtures rejected")
    return 0


if __name__ == "__main__":
    sys.exit(main())
