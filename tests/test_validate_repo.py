"""Unit tests for tools/validate_repo.py (stdlib unittest, no network).

Each test builds a tiny throw-away repository in a temp directory, so a
failure points at one rule. Run: python3 -m unittest discover -s tests -v
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import validate_repo  # noqa: E402

FM = "---\nstatus: draft\nversion: 0.1\nupdated: 2026-11-01\ntemperature: 0.1\n---\n\n"
SECTIONS = "".join(f"<{name}>\n</{name}>\n" for name in validate_repo.AGENTS_SECTIONS)
AGENTS = (
    FM.replace("status: draft", "status: canonical").replace("---\n\n", "entrypoint: true\n---\n\n", 1)
    + "# AGENTS\n\n- archetype: `C`\n- environment: `local`\n\n" + SECTIONS
)


class Fixture:
    def __init__(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.write(".hub-profile.json", json.dumps({
            "profile_version": "1.0",
            "archetype": "C",
            "environment": "local",
            "project_specific_directories": [],
        }))
        self.write("AGENTS.md", AGENTS)
        self.write("README.md", FM + "# Readme\n")

    def write(self, rel: str, text: str) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def errors(self, *checks: str) -> list[str]:
        return validate_repo.run(self.root, checks or None)

    def close(self) -> None:
        self._tmp.cleanup()


class ValidateRepoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.fx = Fixture()

    def tearDown(self) -> None:
        self.fx.close()

    def test_clean_fixture_passes(self) -> None:
        self.assertEqual(self.fx.errors(), [])

    def test_missing_frontmatter_fails(self) -> None:
        self.fx.write("docs/vision.md", "# Vision\n")
        self.assertTrue(any("missing or unclosed frontmatter" in e for e in self.fx.errors("frontmatter")))

    def test_forbidden_ai_generated_and_bad_status(self) -> None:
        self.fx.write("docs/a.md", FM.replace("status: draft", "status: final") .replace("---\n\n", "ai-generated: true\n---\n\n", 1))
        errors = self.fx.errors("frontmatter")
        self.assertTrue(any("ai-generated" in e for e in errors))
        self.assertTrue(any("invalid status 'final'" in e for e in errors))

    def test_adr_requires_decision_type(self) -> None:
        self.fx.write("docs/adr/2026-11-adr-001-x.md", FM.replace("draft", "accepted"))
        self.assertTrue(any("decision-type" in e for e in self.fx.errors("frontmatter")))

    def test_naming_rules(self) -> None:
        self.fx.write("docs/analysis/bad-name.md", FM)
        self.fx.write("docs/analysis/2026-11-01-good-name.md", FM)
        self.fx.write("docs/adr/2026-11-adr-001-ok.md", FM)
        self.fx.write("docs/adr/adr-002-bad.md", FM)
        errors = self.fx.errors("naming")
        self.assertEqual(len(errors), 2, errors)

    def test_broken_link_and_anchor(self) -> None:
        self.fx.write("docs/a.md", FM + "## Видение и цели\n\n[ok](#видение-и-цели) [bad](#nope) [file](missing.md) [ext](https://x.y)\n")
        errors = self.fx.errors("links")
        self.assertEqual(len(errors), 2, errors)
        self.assertTrue(any("missing anchor '#nope'" in e for e in errors))
        self.assertTrue(any("broken relative link: missing.md" in e for e in errors))

    def test_line_anchor_must_name_existing_lines(self) -> None:
        self.fx.write("docs/b.md", FM + "один\nдва\n")  # 9 lines: 7 of frontmatter and blank line, 2 of text
        self.fx.write("docs/a.md", FM + "[ok](b.md#L9) [range](b.md#L2-L9) [far](b.md#L10) [back](b.md#L5-L3)\n")
        errors = self.fx.errors("links")
        self.assertEqual(len(errors), 2, errors)
        self.assertTrue(any("'#L10' is not an ascending range within 1..9" in e for e in errors))
        self.assertTrue(any("'#L5-L3' is not an ascending range within 1..9" in e for e in errors))

    def test_links_in_code_are_ignored(self) -> None:
        self.fx.write("docs/a.md", FM + "```\n[x](nowhere.md)\n```\n`[y](nowhere.md)`\n")
        self.assertEqual(self.fx.errors("links"), [])

    def test_link_outside_repo_fails(self) -> None:
        self.fx.write("docs/a.md", FM + "[hub](../../hub/AGENTS.md)\n")
        self.assertTrue(any("outside the repository" in e for e in self.fx.errors("links")))

    def test_undeclared_top_level_directory_fails(self) -> None:
        self.fx.write("education/README.md", FM)
        self.assertTrue(any("'education'" in e for e in self.fx.errors("structure")))
        profile = json.loads((self.fx.root / ".hub-profile.json").read_text())
        profile["project_specific_directories"] = [{"path": "education", "reason": "owner permission"}]
        self.fx.write(".hub-profile.json", json.dumps(profile))
        self.assertEqual(self.fx.errors("structure"), [])

    def test_agents_must_mirror_profile(self) -> None:
        self.fx.write("AGENTS.md", AGENTS.replace("`C`", "`B`"))
        self.assertTrue(any("does not mirror" in e for e in self.fx.errors("structure")))

    def test_agents_required_sections_and_entrypoint(self) -> None:
        self.fx.write("AGENTS.md", AGENTS.replace("<routing>", "").replace("entrypoint: true\n", ""))
        errors = self.fx.errors("structure")
        self.assertTrue(any("<routing>" in e for e in errors), errors)
        self.assertTrue(any("entrypoint: true" in e for e in errors), errors)

    def test_closed_profile_vocabulary(self) -> None:
        self.fx.write(".hub-profile.json", json.dumps({
            "profile_version": "1.0", "archetype": "E", "environment": "cloud",
            "project_specific_directories": [],
        }))
        errors = self.fx.errors("structure")
        self.assertTrue(any("archetype must be one of" in e for e in errors), errors)
        self.assertTrue(any("environment 'cloud'" in e for e in errors), errors)

    def test_placeholders(self) -> None:
        self.fx.write("docs/a.md", FM + "Project {{project_name}}\n`{{ok_in_code}}`\n")
        self.assertEqual(len(self.fx.errors("placeholders")), 1)


class RealRepositoryTest(unittest.TestCase):
    """The repository itself must pass every check (same as CI)."""

    def test_repository_is_valid(self) -> None:
        root = Path(__file__).resolve().parent.parent
        self.assertEqual(validate_repo.run(root), [])


if __name__ == "__main__":
    unittest.main()
