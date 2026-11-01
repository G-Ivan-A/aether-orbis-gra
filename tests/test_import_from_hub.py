"""Unit tests for tools/import_from_hub.py (stdlib unittest, no network).

The import tool converts Hub documents into this repository: it keeps only
the documentation frontmatter fields, drops task-execution sections, rewrites
Hub links to local paths and marks stage I documents as historical. Each test
checks one of those rules on a small inline sample.
Run: python3 -m unittest discover -s tests -v
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import import_from_hub as imp  # noqa: E402

COMMIT = "0" * 40
BLOB = f"{imp.HUB_URL}/blob/main/{imp.DOMAIN}"


class FrontmatterTest(unittest.TestCase):
    def test_keeps_documentation_fields_and_adds_source(self) -> None:
        lines = ["status: draft", "version: 0.3", "issue: 700", "ai-generated: true",
                 "scope:", "  - course", "temperature: 0.2"]
        result = imp.clean_frontmatter(lines, "a.md", COMMIT)
        self.assertIn("status: draft", result)
        self.assertIn("scope:\n  - course", result)
        self.assertNotIn("issue:", result)
        self.assertNotIn("ai-generated", result)
        self.assertIn(f'source: "{imp.HUB_URL}/blob/{COMMIT}/{imp.DOMAIN}/a.md"', result)

    def test_split_without_frontmatter(self) -> None:
        self.assertEqual(imp.split_frontmatter("# Title\n"), ([], "# Title\n"))


class DropSectionsTest(unittest.TestCase):
    def test_drops_task_sections_up_to_same_level(self) -> None:
        body = (
            "# Doc\n\n## Суть\n\nтекст\n\n## Отклонения от постановки\n\nлишнее\n\n"
            "### Подраздел\n\nтоже лишнее\n\n## Источники\n\nссылки\n"
        )
        result = imp.drop_sections(body, "x.md")
        self.assertIn("## Суть", result)
        self.assertIn("## Источники", result)
        self.assertNotIn("Отклонения", result)
        self.assertNotIn("тоже лишнее", result)

    def test_ignores_headings_inside_code_fences(self) -> None:
        body = "# Doc\n\n```\n## Gaps\n```\n\nтекст\n"
        self.assertEqual(imp.drop_sections(body, "x.md"), body)

    def test_exact_gate_dropped_numbered_gate_kept(self) -> None:
        body = "# Doc\n\n## Гейт-проверка\n\nчеклист задачи\n\n## 5. Гейт-проверка слайда\n\nстандарт\n"
        result = imp.drop_sections(body, "x.md")
        self.assertNotIn("чеклист задачи", result)
        self.assertIn("стандарт", result)

    def test_renames_heading_for_external_reader(self) -> None:
        result = imp.drop_sections("# Doc\n\n## КРИТИЧЕСКАЯ АППЕЛЯЦИЯ\n\nтекст\n", "x.md")
        self.assertIn("## Ключевые решения по логике курса", result)


class RewriteLinksTest(unittest.TestCase):
    OWN = f"{imp.COURSE}/day-03/presentation.md"
    HUB_DIR = imp.DOMAIN

    def rewrite(self, text: str) -> str:
        return imp.rewrite_links(text, self.OWN, self.HUB_DIR)

    def test_absolute_hub_link_to_imported_file_becomes_relative(self) -> None:
        text = f"[день 1]({BLOB}/2026-10-14-day1-presentation-gamma.md#слайд-3)"
        self.assertEqual(self.rewrite(text), "[день 1](../day-01/presentation.md#слайд-3)")

    def test_relative_hub_link_resolved_against_source_directory(self) -> None:
        text = "[модель](gra-research-program/10-theory.md)"
        self.assertEqual(self.rewrite(text), "[модель](../../../methodology/research-program/10-theory.md)")

    def test_link_to_not_imported_file_points_to_hub(self) -> None:
        text = "[RFC](2026-11-03-day4-crisis-mitigation-rfc.md)"
        self.assertEqual(self.rewrite(text), f"[RFC]({BLOB}/2026-11-03-day4-crisis-mitigation-rfc.md)")

    def test_task_and_pr_links_are_unlinked(self) -> None:
        text = f"см. [issue #700]({imp.HUB_URL}/issues/700) и [PR]({imp.HUB_URL}/pull/701)"
        self.assertEqual(self.rewrite(text), "см. issue #700 и PR")

    def test_self_link_keeps_anchor_only(self) -> None:
        text = f"[выше]({BLOB}/2026-11-02-day3-presentation-gamma.md#слайд-1)"
        self.assertEqual(self.rewrite(text), "[выше](#слайд-1)")

    def test_external_and_anchor_links_unchanged(self) -> None:
        text = "[сайт](https://example.org/a) и [раздел](#итог)"
        self.assertEqual(self.rewrite(text), text)

    def test_links_inside_code_fences_unchanged(self) -> None:
        text = "```\n[x](gra-research-program/10-theory.md)\n```\n"
        self.assertEqual(self.rewrite(text), text)


class ConvertTest(unittest.TestCase):
    def test_history_document_gets_banner_and_superseded_status(self) -> None:
        text = "---\nstatus: canonical\nversion: 1.0\n---\n\n# White paper\n\nтекст\n"
        target = "docs/history/2026-06-20-white-paper.en.md"
        result = imp.convert(text, "2026-06-20-white-paper.en.md", target, COMMIT)
        self.assertIn("status: superseded", result)
        self.assertNotIn("status: canonical", result)
        head, _, rest = result.partition("# White paper\n")
        self.assertTrue(rest.startswith("\n" + imp.HISTORY_BANNER))

    def test_add_banner_without_h1_prepends(self) -> None:
        self.assertEqual(imp.add_banner("текст\n", "> B\n"), "> B\n\nтекст\n")

    def test_path_labels_renamed_in_prose(self) -> None:
        text = f"Каталог `{imp.DOMAIN}/gra-research-program/` описывает модель."
        self.assertIn("`methodology/research-program/`", imp.rename_path_labels(text))

    def test_target_for_outside_domain_is_none(self) -> None:
        self.assertIsNone(imp.target_for("docs/README.md"))
        self.assertEqual(imp.target_for(f"{imp.DOMAIN}/image-technologies/"), f"{imp.IMAGE}/README.md")


class MainTest(unittest.TestCase):
    def test_main_writes_every_mapped_file(self) -> None:
        with tempfile.TemporaryDirectory() as hub, tempfile.TemporaryDirectory() as root:
            for rel in imp.MAPPING:
                path = Path(hub) / imp.DOMAIN / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("---\nstatus: draft\n---\n\n# T\n", encoding="utf-8")
            with open(Path(root) / "log", "w", encoding="utf-8") as log:
                stdout, sys.stdout = sys.stdout, log
                try:
                    code = imp.main(["--hub", hub, "--root", root, "--commit", COMMIT])
                finally:
                    sys.stdout = stdout
            self.assertEqual(code, 0)
            for target in imp.MAPPING.values():
                self.assertTrue((Path(root) / target).is_file(), target)


if __name__ == "__main__":
    unittest.main()
