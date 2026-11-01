#!/usr/bin/env python3
"""Import the current GRA materials from the Hub into this repository.

The Hub (https://github.com/G-Ivan-A/hybrid-Intelligence-lab) kept GRA under
research/reputation-technologies/. Issue #1 of aether-orbis-gra moves the
project here. This tool copies ONLY the current documents listed in MAPPING and
adapts them for an external reader:

* frontmatter keeps status/version/updated/temperature/type/scope, drops
  task-bound fields (related_issues, related_artifacts, based_on, method,
  context) and records provenance as ``source:`` = Hub permalink at the
  imported commit;
* sections that only document task execution (gate self-checks against an
  issue, executor decisions, deviations from the task statement, appeals,
  version-by-issue changelogs) are removed - their history stays in the Hub;
* links to Hub files that were imported become relative links; links to other
  Hub files stay absolute ``blob/main`` URLs; links to Hub issues and pull
  requests are unlinked (the label text stays) because tasks and PRs are not
  transferred.

Usage (re-runnable while the course is still being delivered):

    git clone --depth 1 https://github.com/G-Ivan-A/hybrid-Intelligence-lab /tmp/hub
    python3 tools/import_from_hub.py --hub /tmp/hub

Set GRA_IMPORT_DEBUG=1 to trace every rewritten link and removed section.
"""
from __future__ import annotations

import argparse
import os
import posixpath
import re
import subprocess
import sys
from pathlib import Path

HUB_URL = "https://github.com/G-Ivan-A/hybrid-Intelligence-lab"
DOMAIN = "research/reputation-technologies"
DEBUG = os.environ.get("GRA_IMPORT_DEBUG") == "1"

COURSE = "education/technograd-reputation-engineering"
IMAGE = f"{COURSE}/day-04/resources/image-technologies"
HISTORY = (
    "founders-vision-and-framework.ru", "white-paper.en", "framework-standard.en",
    "executive-summary.ru-en", "glossary.ru-en",
)
# Hub path relative to DOMAIN -> path in this repository.
MAPPING: dict[str, str] = {
    "2026-10-12-rfc-days-1-3-logic.md": f"{COURSE}/course-logic.md",
    "2026-10-14-day1-presentation-gamma.md": f"{COURSE}/day-01/presentation.md",
    "2026-10-14-day1-lecturer-script.md": f"{COURSE}/day-01/lecturer-script.md",
    "2026-10-07-day1-rationale-and-method-653.md": f"{COURSE}/day-01/rationale-and-method.md",
    "2026-10-15-day1-slide-standard-and-gate-677.md": f"{COURSE}/day-01/slide-standard-and-gate.md",
    "2026-10-30-day2-presentation-gamma.md": f"{COURSE}/day-02/presentation.md",
    "2026-10-30-day2-lecturer-script.md": f"{COURSE}/day-02/lecturer-script.md",
    "2026-10-30-day2-rationale-and-method.md": f"{COURSE}/day-02/rationale-and-method.md",
    "2026-11-02-day3-presentation-gamma.md": f"{COURSE}/day-03/presentation.md",
    "2026-11-02-day3-lecturer-script.md": f"{COURSE}/day-03/lecturer-script.md",
    "2026-11-02-day3-rationale-and-method.md": f"{COURSE}/day-03/rationale-and-method.md",
    "2026-11-02-day3-slide-standard-and-gate.md": f"{COURSE}/day-03/slide-standard-and-gate.md",
    "2026-11-03-day4-presentation-gamma-v5.md": f"{COURSE}/day-04/presentation.md",
    "2026-11-03-day4-lecturer-script-v5.md": f"{COURSE}/day-04/lecturer-script.md",
    "2026-11-03-day4-image-prompts-v5-couturier-constructor.md": f"{COURSE}/day-04/image-prompts.md",
    "2026-10-24-handout-materials-master-prompt-registry-days-1-4.md": f"{COURSE}/handouts/prompt-and-handout-registry.md",
    "2026-10-30-day1-osint-pipeline-design.md": f"{COURSE}/handouts/osint-pipeline-design.md",
    "exp/day1-osint-709/2026-10-30-ten-company-example.md": f"{COURSE}/handouts/ten-company-example.md",
    **{f"gra-research-program/{n}.md": f"methodology/research-program/{n}.md" for n in (
        "00-introduction", "10-theory", "20-taxonomy", "30-decision-framework",
        "40-practice-and-cases", "50-open-research")},
    # The image-technologies module feeds Day 4 of the course. It is NOT part of
    # GRA: the author excluded image technologies from the GRA boundary.
    **{f"image-technologies/{n}.md": f"{IMAGE}/{n}.md" for n in (
        "00-introduction", "10-theory", "20-taxonomy", "30-decision-framework",
        "40-practice-and-cases", "50-open-research")},
    # Stage I (June 2026) documents: historical context for an external reader.
    **{f"2026-06-20-{n}.md": f"docs/history/2026-06-20-{n}.md" for n in HISTORY},
}
# Directory links (tree/main/...) that have an imported equivalent.
DIR_MAPPING = {
    "gra-research-program": "methodology/research-program/README.md",
    "image-technologies": f"{IMAGE}/README.md",
}
# Banner inserted after the first H1 of every historical document.
HISTORY_BANNER = (
    "> **Исторический документ (этап I, июнь 2026). / Historical document (stage I, June 2026).**\n"
    "> Текущие формулировки GRA — в документах L1–L4 ([docs/README.md](../README.md)); известные\n"
    "> расхождения этого текста с ними перечислены в [docs/history.md](../history.md#известные-расхождения).\n"
    "> Current GRA wording lives in the L1–L4 documents; known discrepancies are listed in docs/history.md.\n"
)

KEEP_FIELDS = ("status", "version", "updated", "temperature", "type", "scope")
# A level-2+ heading whose text matches starts a section that documents task
# execution rather than the subject; the section is dropped up to the next
# heading of the same or a higher level.
DROP_SECTION = re.compile(
    r"^(?:\d+\.\s*)?(?:"
    r"Аппеляции версии|Аппеляции$|Апелляции$|Гейт-проверка issue|Решения исполнителя|"
    r"Отклонения от постановки|Gaps\b|Как опровергнуть этот RFC|Решения, которые нужны от фаундера|"
    r"Изменения версии|Самоаудит против условий задачи|"
    r"Приложение [А-Я]\. Сравнение версий|Приложение [А-Я]\. Расхождения с другими файлами|"
    r"Как запустить проверку"
    r")",
    re.IGNORECASE,
)
# Unnumbered "Гейт-проверка" sections in the Day 4 files are checklists of a
# Hub task; the numbered ones in slide-standard files are the slide standard.
DROP_EXACT = {"Гейт-проверка"}
# Headings kept for their content but renamed for an external reader.
RENAME_HEADING = {"КРИТИЧЕСКАЯ АППЕЛЯЦИЯ": "Ключевые решения по логике курса"}
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
LINK = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)((?:\s+\"[^\"]*\")?)\)")
HUB_FILE = re.compile(re.escape(HUB_URL) + r"/(blob|tree)/main/([^)#?\s]+)(?:\?[^)#\s]*)?(#[^)\s]*)?")
HUB_TASK = re.compile(re.escape(HUB_URL) + r"/(?:issues|pull)/\d+[^)\s]*")


def debug(msg: str) -> None:
    if DEBUG:
        print(f"[import] {msg}", file=sys.stderr)


def split_frontmatter(text: str) -> tuple[list[str], str]:
    if not text.startswith("---\n"):
        return [], text
    end = text.index("\n---\n", 4)
    return text[4:end].splitlines(), text[end + 5:]


def clean_frontmatter(lines: list[str], hub_rel: str, commit: str) -> str:
    kept, current = [], None
    for line in lines:
        key = re.match(r"^([A-Za-z_-]+):", line)
        if key:
            current = key.group(1)
            if current in KEEP_FIELDS:
                kept.append(line)
        elif current in KEEP_FIELDS and line.startswith((" ", "\t")):
            kept.append(line)
    kept.append(f'source: "{HUB_URL}/blob/{commit}/{DOMAIN}/{hub_rel}"')
    return "---\n" + "\n".join(kept) + "\n---\n"


def drop_sections(body: str, rel: str) -> str:
    out, skip_level, in_fence = [], 0, False
    for line in body.splitlines(keepends=True):
        if FENCE.match(line):
            in_fence = not in_fence
        match = None if in_fence else HEADING.match(line)
        if match:
            level = len(match.group(1))
            if skip_level and level <= skip_level:
                skip_level = 0
            if not skip_level and level >= 2 and (
                DROP_SECTION.match(match.group(2)) or match.group(2) in DROP_EXACT
            ):
                skip_level = level
                debug(f"{rel}: drop section '{match.group(2)}'")
        if not skip_level:
            if match and match.group(2) in RENAME_HEADING:
                line = f"{match.group(1)} {RENAME_HEADING[match.group(2)]}\n"
            out.append(line)
    return "".join(out)


def target_for(hub_path: str) -> str | None:
    """Repository path for a Hub path (relative to the Hub root) or None."""
    path = hub_path.rstrip("/")
    if not path.startswith(DOMAIN + "/"):
        return None
    inner = path[len(DOMAIN) + 1:]
    return MAPPING.get(inner) or DIR_MAPPING.get(inner)


def rewrite_links(body: str, own_target: str, own_hub_dir: str) -> str:
    own_dir = posixpath.dirname(own_target)

    def local(target: str, anchor: str) -> str:
        if target == own_target:
            return anchor or "#"
        return posixpath.relpath(target, own_dir) + anchor

    def replace(match: re.Match[str]) -> str:
        bang, label, url, title = match.groups()
        if HUB_TASK.fullmatch(url):
            debug(f"{own_target}: unlink task {url}")
            return label
        hub = HUB_FILE.fullmatch(url)
        if hub:
            mapped = target_for(hub.group(2))
            if mapped:
                return f"{bang}[{label}]({local(mapped, hub.group(3) or '')}{title})"
            return match.group(0)
        if re.match(r"^[a-z]+:|^#", url):
            return match.group(0)
        # Relative link inside the Hub: resolve against the source directory.
        path, _, anchor = url.partition("#")
        hub_path = posixpath.normpath(posixpath.join(own_hub_dir, path))
        mapped = target_for(hub_path)
        if mapped:
            return f"{bang}[{label}]({local(mapped, '#' + anchor if anchor else '')}{title})"
        kind = "tree" if path.endswith("/") or "." not in posixpath.basename(path) else "blob"
        absolute = f"{HUB_URL}/{kind}/main/{hub_path}" + (f"#{anchor}" if anchor else "")
        debug(f"{own_target}: relative {url} -> {absolute}")
        return f"{bang}[{label}]({absolute}{title})"

    out, in_fence = [], False
    for line in body.splitlines(keepends=True):
        if FENCE.match(line):
            in_fence = not in_fence
        out.append(line if in_fence else LINK.sub(replace, line))
    return "".join(out)


# Hub path mentions in prose/inline code (not inside URLs) -> new location.
PATH_LABELS = {
    f"{DOMAIN}/gra-research-program/": "methodology/research-program/",
    f"{DOMAIN}/image-technologies/": f"{IMAGE}/",
}


def rename_path_labels(body: str) -> str:
    for old, new in PATH_LABELS.items():
        body = re.sub(r"(?<![/\w.-])" + re.escape(old) + r"(?!presentation-rfc)", new, body)
    return body


def add_banner(body: str, banner: str) -> str:
    """Insert ``banner`` after the first H1 (or at the top if there is none)."""
    lines = body.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if line.startswith("# "):
            return "".join(lines[: index + 1] + ["\n", banner] + lines[index + 1:])
    return banner + "\n" + body


def convert(text: str, hub_rel: str, target: str, commit: str) -> str:
    lines, body = split_frontmatter(text)
    body = drop_sections(body, target)
    body = rewrite_links(body, target, posixpath.dirname(f"{DOMAIN}/{hub_rel}"))
    body = rename_path_labels(body)
    frontmatter = clean_frontmatter(lines, hub_rel, commit)
    if target.startswith("docs/history/"):
        body = add_banner(body, HISTORY_BANNER)
        # Stage I wording is replaced by the L1-L4 documents of this repository.
        frontmatter = re.sub(r"(?m)^status:.*$", "status: superseded", frontmatter)
    return frontmatter + body.rstrip("\n") + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--hub", required=True, type=Path, help="local clone of hybrid-Intelligence-lab")
    parser.add_argument("--root", default=Path(__file__).resolve().parent.parent, type=Path)
    parser.add_argument("--commit", help="Hub commit for provenance (default: HEAD of --hub)")
    args = parser.parse_args(argv)
    commit = args.commit or subprocess.run(
        ["git", "-C", str(args.hub), "rev-parse", "HEAD"], check=True, capture_output=True, text=True,
    ).stdout.strip()
    for hub_rel, target in MAPPING.items():
        source = args.hub / DOMAIN / hub_rel
        text = source.read_text(encoding="utf-8")
        destination = args.root / target
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(convert(text, hub_rel, target, commit), encoding="utf-8")
        print(f"{hub_rel} -> {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
