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
  files of the GRA domain are pinned to the imported commit (``blob/<sha>``),
  because the Hub removes the domain from ``main`` (Hub RFC #721, step 2) and
  GitHub answers 404 for a removed ``blob/main`` path but 200 for a SHA
  permalink; links to the rest of the Hub (rules, standards) stay ``main``;
  links to Hub issues and pull requests are unlinked (the label text stays)
  because tasks and PRs are not transferred;
* line anchors ``#Lnnn`` into imported files are recomputed for the copies in
  this repository (the Hub line numbers do not match after sections are
  dropped and the frontmatter is cleaned - case of Hub issue #711); the label
  ``<file>, строка N`` is renamed accordingly. A line that has no copy keeps a
  Hub permalink at the imported commit;
* directories listed in PROVENANCE (the builder and data of the quotes list)
  are copied as data: Markdown is converted as above, other text files only
  get ``blob/main`` -> ``blob/<sha>``; every file is listed with the SHA-256
  of the Hub original in ``provenance-manifest.tsv``. Hub code is never
  executed here.

Usage (re-runnable while the course is still being delivered):

    git clone https://github.com/G-Ivan-A/hybrid-Intelligence-lab /tmp/hub
    git -C /tmp/hub checkout <PIN_SHA>
    python3 tools/import_from_hub.py --hub /tmp/hub --commit <PIN_SHA>

The last import used PIN_SHA from ``.hub-profile.json -> last_sync``.

Set GRA_IMPORT_DEBUG=1 to trace every rewritten link and removed section.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
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
    # Quotes of days 1-4 (Hub issue #711), created after the first snapshot
    # 32b5fa5; imported by Hub RFC #721, step 2.2 (issue #3 here).
    "2026-11-01-course-quotes-days-1-4-alce.md": f"{COURSE}/handouts/course-quotes-days-1-4-alce.md",
}
# Hub directories (relative to DOMAIN) copied as provenance data, not as
# documents: the builder and the inputs of the quotes list.
PROVENANCE = {
    "exp/quotes-711": f"{COURSE}/handouts/course-quotes-provenance",
}
PROVENANCE_MANIFEST = "provenance-manifest.tsv"
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

# Banner inserted after the first H1 of a document that is generated in the Hub
# by a builder kept here only as provenance.
GENERATED_BANNER = (
    "> **Перенесено из Хаба.** Файл собран в Хабе построителем из каталога\n"
    "> [course-quotes-provenance/](course-quotes-provenance/README.md) (провенанс, здесь не\n"
    "> исполняется). При переносе якоря строк `#Lnnn` пересчитаны по копиям материалов\n"
    "> в этом репозитории; ссылки на файлы, которые остались в Хабе (каталог источников\n"
    "> #650 и другие), закреплены на коммите Хаба из поля `source`.\n"
)
PROVENANCE_BANNER = (
    "> **Провенанс.** Копия каталога Хаба на коммите из поля `source`. Код Хаба в\n"
    "> этом репозитории не исполняется: файлы сохранены как данные, по которым\n"
    "> собран [список цитат](../course-quotes-days-1-4-alce.md). Команды ниже\n"
    "> относятся к дереву Хаба. Единственная правка текстовых файлов — ссылки\n"
    "> `blob/main` заменены ссылками на тот же коммит; SHA-256 оригиналов — в\n"
    "> [`provenance-manifest.tsv`](provenance-manifest.tsv).\n"
)
BANNERS = {
    f"{COURSE}/handouts/course-quotes-days-1-4-alce.md": GENERATED_BANNER,
    f"{COURSE}/handouts/course-quotes-provenance/README.md": PROVENANCE_BANNER,
}

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
HUB_FILE = re.compile(re.escape(HUB_URL) + r"/(blob|tree)/main/([^)#?\s]+)(\?[^)#\s]*)?(#[^)\s]*)?")
HUB_TASK = re.compile(re.escape(HUB_URL) + r"/(?:issues|pull)/\d+[^)\s]*")
LINE_ANCHOR = re.compile(r"^#L(\d+)(?:-L(\d+))?$")
LINE_LABEL = re.compile(r"^(?P<name>[^,\[\]]+), строка (?P<line>\d+)$")
# Hub line -> line of the copy, per repository path of the copy.
LineMaps = dict[str, dict[int, int]]


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
    for hub_dir, local_dir in PROVENANCE.items():
        if inner == hub_dir:
            return f"{local_dir}/README.md"
        if inner.startswith(hub_dir + "/"):
            return local_dir + inner[len(hub_dir):]
    return MAPPING.get(inner) or DIR_MAPPING.get(inner)


def in_domain(hub_path: str) -> bool:
    return hub_path == DOMAIN or hub_path.startswith(DOMAIN + "/")


def display_name(target: str) -> str:
    """Short name of a repository file for link labels (course files without the course prefix)."""
    return target[len(COURSE) + 1:] if target.startswith(COURSE + "/") else target


def remap_line_anchor(anchor: str, target: str, line_maps: LineMaps | None) -> str | None:
    """Translate ``#Lnnn[-Lmmm]`` of a Hub file into the line numbers of its copy.

    Returns the anchor unchanged when it is not a line anchor and None when a
    line has no counterpart in the copy (it was in a dropped section).
    """
    match = LINE_ANCHOR.match(anchor)
    if not match or line_maps is None:
        return anchor
    lines = [int(n) for n in match.groups() if n]
    if target not in line_maps and not target.endswith(".md"):
        return anchor  # provenance data file: copied line for line
    mapping = line_maps.get(target, {})
    if any(n not in mapping for n in lines):
        return None
    return "#" + "-".join(f"L{mapping[n]}" for n in lines)


def relabel(label: str, hub_path: str, target: str, old: str, new: str) -> str:
    """Rename ``<hub file>, строка N`` labels after a line anchor was recomputed."""
    match = LINE_LABEL.match(label)
    if not match or match.group("name") != posixpath.basename(hub_path):
        return label
    old_line, new_line = LINE_ANCHOR.match(old), LINE_ANCHOR.match(new)
    if not old_line or not new_line or match.group("line") != old_line.group(1):
        return label
    return f"{display_name(target)}, строка {new_line.group(1)}"


def rewrite_links(
    body: str, own_target: str, own_hub_dir: str, commit: str = "main", line_maps: LineMaps | None = None,
) -> str:
    """Rewrite Hub links of one document.

    ``commit`` pins links to domain files that are not imported; ``line_maps``
    (Hub line -> copy line per copy) recomputes ``#Lnnn`` anchors into copies.
    """
    own_dir = posixpath.dirname(own_target)

    def local(target: str, anchor: str) -> str:
        if target == own_target:
            return anchor or "#"
        return posixpath.relpath(target, own_dir) + anchor

    def to_copy(bang: str, label: str, title: str, hub_path: str, mapped: str, anchor: str,
                pinned: str) -> str:
        new_anchor = remap_line_anchor(anchor, mapped, line_maps)
        if new_anchor is None:
            debug(f"{own_target}: line {anchor} of {hub_path} has no copy, keep {pinned}")
            return f"{bang}[{label}]({pinned}{title})"
        if new_anchor != anchor:
            label = relabel(label, hub_path, mapped, anchor, new_anchor)
            debug(f"{own_target}: {hub_path}{anchor} -> {mapped}{new_anchor}")
        return f"{bang}[{label}]({local(mapped, new_anchor)}{title})"

    def replace(match: re.Match[str]) -> str:
        bang, label, url, title = match.groups()
        if HUB_TASK.fullmatch(url):
            debug(f"{own_target}: unlink task {url}")
            return label
        hub = HUB_FILE.fullmatch(url)
        if hub:
            kind, hub_path, query, anchor = hub.group(1), hub.group(2), hub.group(3) or "", hub.group(4) or ""
            pinned = f"{HUB_URL}/{kind}/{commit}/{hub_path}{query}{anchor}"
            mapped = target_for(hub_path)
            if mapped:
                return to_copy(bang, label, title, hub_path, mapped, anchor, pinned)
            if in_domain(hub_path.rstrip("/")):
                debug(f"{own_target}: pin {url} -> {pinned}")
                return f"{bang}[{label}]({pinned}{title})"
            return match.group(0)
        if re.match(r"^[a-z]+:|^#", url):
            return match.group(0)
        # Relative link inside the Hub: resolve against the source directory.
        path, _, anchor = url.partition("#")
        hub_path = posixpath.normpath(posixpath.join(own_hub_dir, path))
        anchor = f"#{anchor}" if anchor else ""
        kind = "tree" if path.endswith("/") or "." not in posixpath.basename(path) else "blob"
        ref = commit if in_domain(hub_path) else "main"
        absolute = f"{HUB_URL}/{kind}/{ref}/{hub_path}{anchor}"
        mapped = target_for(hub_path)
        if mapped:
            return to_copy(bang, label, title, hub_path, mapped, anchor, absolute)
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


def convert(text: str, hub_rel: str, target: str, commit: str, line_maps: LineMaps | None = None) -> str:
    lines, body = split_frontmatter(text)
    body = drop_sections(body, target)
    body = rewrite_links(body, target, posixpath.dirname(f"{DOMAIN}/{hub_rel}"), commit, line_maps)
    body = rename_path_labels(body)
    frontmatter = clean_frontmatter(lines, hub_rel, commit)
    if target.startswith("docs/history/"):
        body = add_banner(body, HISTORY_BANNER)
        # Stage I wording is replaced by the L1-L4 documents of this repository.
        frontmatter = re.sub(r"(?m)^status:.*$", "status: superseded", frontmatter)
    if target in BANNERS:
        body = add_banner(body, BANNERS[target])
    return frontmatter + body.rstrip("\n") + "\n"


def build_line_map(source: str, copy: str, hub_rel: str, target: str, commit: str) -> dict[int, int]:
    """Map 1-based lines of a Hub file to the lines of its converted copy.

    The Hub lines get the same line-local rewrites as the copy (links, path
    labels), then both sides are aligned with difflib. Equal lines map
    directly; a changed block of the same size maps line by line when the two
    lines are still similar. Lines of dropped sections stay unmapped.
    """
    hub_dir = posixpath.dirname(f"{DOMAIN}/{hub_rel}")
    left = [rename_path_labels(rewrite_links(line, target, hub_dir, commit)) for line in source.splitlines()]
    right = copy.splitlines()
    mapping: dict[int, int] = {}
    matcher = difflib.SequenceMatcher(None, left, right, autojunk=False)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal" or (tag == "replace" and i2 - i1 == j2 - j1):
            for k in range(i2 - i1):
                if tag == "equal" or difflib.SequenceMatcher(None, left[i1 + k], right[j1 + k]).ratio() >= 0.6:
                    mapping[i1 + k + 1] = j1 + k + 1
    return mapping


def pin_text(text: str, commit: str) -> str:
    """Pin ``blob|tree/main`` Hub URLs of a provenance text file to ``commit``."""
    return re.sub(re.escape(HUB_URL) + r"/(blob|tree)/main/", lambda m: f"{HUB_URL}/{m.group(1)}/{commit}/", text)


def copy_provenance(hub: Path, root: Path, commit: str, line_maps: LineMaps) -> list[str]:
    """Copy PROVENANCE directories as data and write their manifests."""
    written = []
    for hub_dir, local_dir in PROVENANCE.items():
        rows = ["path\thub_sha256\tcopy_sha256\ttransformation"]
        source_dir = hub / DOMAIN / hub_dir
        if not source_dir.is_dir():
            raise FileNotFoundError(f"provenance directory missing in the Hub clone: {source_dir}")
        (root / local_dir).mkdir(parents=True, exist_ok=True)
        for source in sorted(p for p in source_dir.rglob("*") if p.is_file()):
            rel = source.relative_to(source_dir).as_posix()
            data = source.read_bytes()
            target = f"{local_dir}/{rel}"
            if source.suffix == ".md":
                out = convert(data.decode("utf-8"), f"{hub_dir}/{rel}", target, commit, line_maps).encode("utf-8")
                how = "markdown import (frontmatter, links, banner)"
            else:
                try:
                    text = data.decode("utf-8")
                except UnicodeDecodeError:
                    out, how = data, "none"
                else:
                    out = pin_text(text, commit).encode("utf-8")
                    how = "blob/main -> blob/<commit>" if out != data else "none"
            destination = root / target
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(out)
            rows.append("\t".join((rel, hashlib.sha256(data).hexdigest(), hashlib.sha256(out).hexdigest(), how)))
            written.append(target)
        manifest = root / local_dir / PROVENANCE_MANIFEST
        manifest.write_text(
            f"# Hub {HUB_URL} commit {commit}, directory {DOMAIN}/{hub_dir}\n" + "\n".join(rows) + "\n",
            encoding="utf-8",
        )
        written.append(f"{local_dir}/{PROVENANCE_MANIFEST}")
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--hub", required=True, type=Path, help="local clone of hybrid-Intelligence-lab")
    parser.add_argument("--root", default=Path(__file__).resolve().parent.parent, type=Path)
    parser.add_argument("--commit", help="Hub commit for provenance and pinned links (default: HEAD of --hub)")
    args = parser.parse_args(argv)
    commit = args.commit or subprocess.run(
        ["git", "-C", str(args.hub), "rev-parse", "HEAD"], check=True, capture_output=True, text=True,
    ).stdout.strip()
    sources = {hub_rel: (args.hub / DOMAIN / hub_rel).read_text(encoding="utf-8") for hub_rel in MAPPING}
    # Pass 1 converts every file to learn how Hub lines move in the copies;
    # pass 2 converts again with the line maps to recompute #Lnnn anchors.
    # Pass 2 only edits link anchors and labels, so the maps stay valid.
    line_maps: LineMaps = {}
    for hub_rel, target in MAPPING.items():
        copy = convert(sources[hub_rel], hub_rel, target, commit)
        line_maps[target] = build_line_map(sources[hub_rel], copy, hub_rel, target, commit)
    for hub_rel, target in MAPPING.items():
        destination = args.root / target
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(convert(sources[hub_rel], hub_rel, target, commit, line_maps), encoding="utf-8")
        print(f"{hub_rel} -> {target}")
    for target in copy_provenance(args.hub, args.root, commit, line_maps):
        print(f"provenance -> {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
