#!/usr/bin/env python3
"""Repository validator for aether-orbis-gra.

Stdlib-only checks that keep the documentation repository consistent with the
Hub conventions (https://github.com/G-Ivan-A/hybrid-Intelligence-lab):

* frontmatter  - every tracked Markdown artifact starts with a YAML frontmatter
                 block that has `status`, `version`, `updated`, `temperature`;
                 `status` is from the allowed set; `ai-generated` is forbidden;
* naming       - dated naming of chronological documents in docs/analysis,
                 docs/rfc and docs/adr (Hub file naming convention);
* links        - every relative Markdown link resolves to an existing file
                 (and, for links to Markdown headings, to an existing anchor;
                 a GitHub line anchor ``#Lnnn`` or ``#Lnnn-Lmmm`` must name
                 lines that exist in the target file);
* structure    - every top-level directory is canonical or declared in
                 `.hub-profile.json -> project_specific_directories` with a
                 non-empty reason;
* placeholders - no unresolved `{{placeholder}}` template markers.

Usage:
    python3 tools/validate_repo.py [--root PATH] [--only CHECK[,CHECK...]]

Exit code 0 when all checks pass, 1 otherwise. Set GRA_VALIDATE_DEBUG=1 to
print every checked file (tracing is off by default).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from pathlib import Path
from typing import Callable, Iterable

DEBUG = os.environ.get("GRA_VALIDATE_DEBUG") == "1"

REQUIRED_FIELDS = ("status", "version", "updated", "temperature")
KNOWLEDGE_STATUSES = {"draft", "reviewed", "canonical", "superseded", "deprecated"}
GOVERNANCE_STATUSES = {"draft", "proposed", "accepted", "rejected", "deprecated", "superseded"}

# Files that are not knowledge artifacts and therefore carry no frontmatter.
FRONTMATTER_EXEMPT = {"LICENSE", "LICENSE.md", "CITATION.cff"}
FRONTMATTER_EXEMPT_DIRS = (".github/",)

NAMING_EXCEPTIONS = re.compile(
    r"^(README|CHANGELOG|CONTRIBUTING|CODE_OF_CONDUCT|LICENSE|AI_GOVERNANCE)\.md$"
    r"|-registry\.md$|-index\.md$|-Index\.md$"
)
DAILY = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9]+(-[a-z0-9]+)*(\.[a-z]{2}(-[a-z]{2})*)?\.md$")
MONTHLY = re.compile(r"^(\d{4}|\d{4}-\d{2})-[a-z0-9]+(-[a-z0-9]+)*(\.[a-z]{2}(-[a-z]{2})*)?\.md$")
ADR = re.compile(r"^\d{4}-\d{2}-adr-\d{3}-[a-z0-9]+(-[a-z0-9]+)*(\.[a-z]{2}(-[a-z]{2})*)?\.md$")

# Canonical top-level directories of a Hub spoke (core + docs/education homes).
CANONICAL_TOP_DIRS = {".github", "docs", "tools", "tests", "ai-rules", "ops", "standards", "examples", "experiments"}
ARCHETYPES = {"A", "B", "C", "D"}
ENVIRONMENTS = {"local", "gigacode", "serverless"}
# Required sections of /AGENTS.md (Hub standards/agents-md-bootstrap-standard.md).
AGENTS_SECTIONS = (
    "scope", "hard_rules", "forbidden", "guidelines", "hybrid_work", "project_specific_rules",
    "routing", "artifact_homes", "issue_levels", "missing_tags", "context_scope", "validation",
    "models", "escalation",
)
AGENTS_WARN_TOKENS = 4000
AGENTS_HARD_TOKENS = 8000

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)|!\[[^\]]*\]\(([^)\s]+)\)")
PLACEHOLDER_RE = re.compile(r"\{\{[a-z_]+\}\}")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
LINE_ANCHOR_RE = re.compile(r"^L(\d+)(?:-L(\d+))?$")


def debug(msg: str) -> None:
    if DEBUG:
        print(f"[debug] {msg}", file=sys.stderr)


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def fail(self, msg: str) -> None:
        self.errors.append(msg)


def markdown_files(root: Path) -> list[Path]:
    result = []
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        if rel.startswith(".git/") or "/node_modules/" in rel:
            continue
        result.append(path)
    return result


def read_frontmatter(text: str) -> dict[str, str] | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip('"').strip("'")
    return None  # frontmatter never closed


def check_frontmatter(root: Path, report: Report) -> None:
    for path in markdown_files(root):
        rel = path.relative_to(root).as_posix()
        if path.name in FRONTMATTER_EXEMPT or rel.startswith(FRONTMATTER_EXEMPT_DIRS):
            continue
        debug(f"frontmatter: {rel}")
        fields = read_frontmatter(path.read_text(encoding="utf-8"))
        if fields is None:
            report.fail(f"frontmatter: missing or unclosed frontmatter block: {rel}")
            continue
        for name in REQUIRED_FIELDS:
            if not fields.get(name):
                report.fail(f"frontmatter: missing field '{name}': {rel}")
        if "ai-generated" in fields:
            report.fail(f"frontmatter: forbidden field 'ai-generated': {rel}")
        governance = rel.startswith("docs/adr/") and path.name != "README.md"
        allowed = GOVERNANCE_STATUSES if governance else KNOWLEDGE_STATUSES
        status = fields.get("status")
        if status and status not in allowed:
            report.fail(f"frontmatter: invalid status '{status}' (allowed: {sorted(allowed)}): {rel}")
        if governance and not fields.get("decision-type"):
            report.fail(f"frontmatter: ADR requires 'decision-type': {rel}")
        updated = fields.get("updated", "")
        if updated and not re.match(r"^\d{4}-\d{2}-\d{2}$", updated):
            report.fail(f"frontmatter: 'updated' must be YYYY-MM-DD, got '{updated}': {rel}")


def check_naming(root: Path, report: Report) -> None:
    rules: list[tuple[str, re.Pattern[str], str]] = [
        ("docs/analysis", DAILY, "YYYY-MM-DD-name.md"),
        ("docs/audit", DAILY, "YYYY-MM-DD-name.md"),
        ("docs/history", DAILY, "YYYY-MM-DD-name.md"),
        ("docs/rfc", MONTHLY, "YYYY-MM-name.md or YYYY-name.md"),
        ("docs/adr", ADR, "YYYY-MM-adr-NNN-name.md"),
    ]
    for directory, pattern, expected in rules:
        base = root / directory
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.md")):
            debug(f"naming: {path.relative_to(root)}")
            if NAMING_EXCEPTIONS.search(path.name):
                continue
            if not pattern.match(path.name):
                report.fail(f"naming: {path.relative_to(root).as_posix()} must use {expected}")


def github_anchor(heading: str) -> str:
    """Approximate GitHub's heading slug algorithm (works for Cyrillic)."""
    text = re.sub(r"<[^>]+>", "", heading).strip().lower()
    text = re.sub(r"`", "", text)
    out = []
    for ch in text:
        if ch in (" ", "-"):
            out.append("-")
        elif ch == "_" or ch.isalnum():
            out.append(ch)
        else:
            cat = unicodedata.category(ch)
            if cat.startswith("M"):  # combining marks (e.g. й decomposed)
                out.append(ch)
    return "".join(out)


def anchors_of(path: Path, cache: dict[Path, set[str]]) -> set[str]:
    if path in cache:
        return cache[path]
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    in_fence = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", line)
        if match:
            slug = github_anchor(match.group(1))
            n = counts.get(slug, 0)
            anchors.add(slug if n == 0 else f"{slug}-{n}")
            counts[slug] = n + 1
        for explicit in re.findall(r"<a\s+(?:name|id)=\"([^\"]+)\"", line):
            anchors.add(explicit)
    cache[path] = anchors
    return anchors


def iter_links(text: str) -> Iterable[tuple[int, str]]:
    in_fence = False
    for number, line in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        stripped = re.sub(r"`[^`]*`", "", line)
        for match in LINK_RE.finditer(stripped):
            target = match.group(1) or match.group(2)
            if target:
                yield number, target


def check_links(root: Path, report: Report) -> None:
    cache: dict[Path, set[str]] = {}
    for path in markdown_files(root):
        rel = path.relative_to(root).as_posix()
        debug(f"links: {rel}")
        for number, target in iter_links(path.read_text(encoding="utf-8")):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                continue  # http(s), mailto, etc.
            file_part, _, anchor = target.partition("#")
            if file_part == "":
                dest = path
            else:
                dest = (path.parent / file_part).resolve()
                try:
                    dest.relative_to(root.resolve())
                except ValueError:
                    report.fail(f"links: {rel}:{number} points outside the repository: {target}")
                    continue
                if not dest.exists():
                    report.fail(f"links: {rel}:{number} broken relative link: {target}")
                    continue
            line_anchor = LINE_ANCHOR_RE.match(anchor) if anchor and dest.is_file() else None
            if line_anchor:
                count = len(dest.read_text(encoding="utf-8").splitlines())
                lines = [int(n) for n in line_anchor.groups() if n]
                if any(n < 1 or n > count for n in lines) or lines != sorted(lines):
                    report.fail(f"links: {rel}:{number} line anchor '#{anchor}' is not an ascending range within 1..{count} of {dest.relative_to(root.resolve()).as_posix()}")
                continue
            if anchor and dest.is_file() and dest.suffix == ".md":
                if anchor not in anchors_of(dest, cache):
                    report.fail(f"links: {rel}:{number} missing anchor '#{anchor}' in {dest.relative_to(root.resolve()).as_posix()}")


def check_structure(root: Path, report: Report) -> None:
    profile_path = root / ".hub-profile.json"
    if not profile_path.is_file():
        report.fail("structure: .hub-profile.json is missing")
        return
    try:
        profile = json.loads(profile_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.fail(f"structure: .hub-profile.json is not valid JSON: {exc}")
        return
    for key in ("profile_version", "archetype", "environment", "project_specific_directories"):
        if key not in profile:
            report.fail(f"structure: .hub-profile.json misses '{key}'")
    declared = set()
    for entry in profile.get("project_specific_directories", []):
        path = str(entry.get("path", "")).strip("/")
        if not path or not str(entry.get("reason", "")).strip():
            report.fail(f"structure: project_specific_directories entry needs path and non-empty reason: {entry}")
            continue
        declared.add(path)
        if not (root / path).is_dir():
            report.fail(f"structure: declared directory does not exist: {path}")
    for child in sorted(root.iterdir()):
        if not child.is_dir() or child.name == ".git":
            continue
        if child.name not in CANONICAL_TOP_DIRS and child.name not in declared:
            report.fail(f"structure: top-level directory '{child.name}' is neither canonical nor declared in .hub-profile.json")
    if profile.get("archetype") not in ARCHETYPES:
        report.fail(f"structure: archetype must be one of {sorted(ARCHETYPES)}")
    envs = [profile.get("environment", "local")] + list(profile.get("secondary_environments", []))
    for env in envs:
        if env not in ENVIRONMENTS:
            report.fail(f"structure: environment '{env}' must be one of {sorted(ENVIRONMENTS)}")
    agents = root / "AGENTS.md"
    if not agents.is_file():
        report.fail("structure: AGENTS.md is missing")
        return
    text = agents.read_text(encoding="utf-8")
    for key in ("archetype", "environment"):
        value = profile.get(key)
        if value and f"- {key}: `{value}`" not in text:
            report.fail(f"structure: AGENTS.md does not mirror .hub-profile.json {key}={value}")
    for section in AGENTS_SECTIONS:
        if f"<{section}>" not in text or f"</{section}>" not in text:
            report.fail(f"structure: AGENTS.md misses required section <{section}>")
    meta = read_frontmatter(text) or {}
    if meta.get("status") != "canonical" or meta.get("entrypoint") != "true":
        report.fail("structure: AGENTS.md frontmatter needs status: canonical and entrypoint: true")
    tokens = len(text) // 4
    if tokens > AGENTS_HARD_TOKENS:
        report.fail(f"structure: AGENTS.md is ~{tokens} tokens, above the {AGENTS_HARD_TOKENS} hard limit")
    elif tokens > AGENTS_WARN_TOKENS:
        print(f"warning: AGENTS.md is ~{tokens} tokens (soft limit {AGENTS_WARN_TOKENS})", file=sys.stderr)


def check_placeholders(root: Path, report: Report) -> None:
    for path in markdown_files(root):
        rel = path.relative_to(root).as_posix()
        in_fence = False
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            if PLACEHOLDER_RE.search(re.sub(r"`[^`]*`", "", line)):
                report.fail(f"placeholders: {rel}:{number} unresolved template placeholder")


CHECKS: dict[str, Callable[[Path, Report], None]] = {
    "frontmatter": check_frontmatter,
    "naming": check_naming,
    "links": check_links,
    "structure": check_structure,
    "placeholders": check_placeholders,
}


def run(root: Path, only: Iterable[str] | None = None) -> list[str]:
    report = Report()
    for name, check in CHECKS.items():
        if only and name not in only:
            continue
        check(root, report)
    return report.errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=Path(__file__).resolve().parent.parent, type=Path)
    parser.add_argument("--only", default="", help="comma-separated subset of: " + ",".join(CHECKS))
    args = parser.parse_args(argv)
    only = [c for c in args.only.split(",") if c]
    unknown = set(only) - set(CHECKS)
    if unknown:
        parser.error(f"unknown checks: {sorted(unknown)}")
    errors = run(args.root.resolve(), only)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1
    print("Validation passed: " + ", ".join(only or CHECKS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
