"""Unit tests for tools/import_from_hub.py (stdlib unittest, no network).

The import tool converts Hub documents into this repository: it keeps only
the documentation frontmatter fields, drops task-execution sections, rewrites
Hub links to local paths, pins the remaining links to the GRA domain to one
Hub commit, recomputes line anchors ``#Lnnn`` for the local copies, copies the
quotes builder as provenance and marks stage I documents as historical. Each
test checks one of those rules on a small inline sample.
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
PINNED = f"{imp.HUB_URL}/blob/{COMMIT}/{imp.DOMAIN}"


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

    def test_link_to_not_imported_domain_file_is_pinned_to_commit(self) -> None:
        text = f"[каталог]({BLOB}/2026-09-30-course-sources-and-presentations-650.md#L12)"
        result = imp.rewrite_links(text, self.OWN, self.HUB_DIR, COMMIT)
        self.assertEqual(result, f"[каталог]({PINNED}/2026-09-30-course-sources-and-presentations-650.md#L12)")

    def test_relative_link_to_not_imported_domain_file_is_pinned(self) -> None:
        result = imp.rewrite_links("[RFC](2026-11-03-day4-crisis-mitigation-rfc.md)", self.OWN, self.HUB_DIR, COMMIT)
        self.assertEqual(result, f"[RFC]({PINNED}/2026-11-03-day4-crisis-mitigation-rfc.md)")

    def test_domain_directory_link_is_pinned_as_tree(self) -> None:
        text = f"[эксперимент]({imp.HUB_URL}/tree/main/{imp.DOMAIN}/exp/day3-gamma-681/)"
        result = imp.rewrite_links(text, self.OWN, self.HUB_DIR, COMMIT)
        self.assertEqual(result, f"[эксперимент]({imp.HUB_URL}/tree/{COMMIT}/{imp.DOMAIN}/exp/day3-gamma-681/)")

    def test_links_to_hub_rules_stay_on_main(self) -> None:
        text = f"[правила]({imp.HUB_URL}/blob/main/ai-rules/agent-work-rules.md)"
        self.assertEqual(imp.rewrite_links(text, self.OWN, self.HUB_DIR, COMMIT), text)
        relative = imp.rewrite_links("[стандарт](../../standards/research-standard.md)", self.OWN, self.HUB_DIR, COMMIT)
        self.assertEqual(relative, f"[стандарт]({imp.HUB_URL}/blob/main/standards/research-standard.md)")

    def test_provenance_directory_maps_to_local_copy(self) -> None:
        self.assertEqual(
            imp.target_for(f"{imp.DOMAIN}/exp/quotes-711/source-excerpts-711.txt"),
            f"{imp.COURSE}/handouts/course-quotes-provenance/source-excerpts-711.txt",
        )
        self.assertEqual(imp.target_for(f"{imp.DOMAIN}/exp/quotes-711/"), f"{imp.COURSE}/handouts/course-quotes-provenance/README.md")

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


class LineAnchorTest(unittest.TestCase):
    """Hub line numbers do not survive the import (Hub issue #711: line 591 became 581)."""

    QUOTES = f"{imp.COURSE}/handouts/course-quotes-days-1-4-alce.md"
    DECK = f"{imp.COURSE}/day-04/presentation.md"
    HUB_DECK = "2026-11-03-day4-presentation-gamma-v5.md"
    SOURCE = (
        "---\nstatus: draft\nissue: 697\nrelated_issues:\n  - x\n  - y\n---\n\n# Колода\n\n"
        "## Изменения версии\n\nстрока задачи\n\n## Слайд 1\n\nЭпиграф: «Форма следует функции»\n"
    )

    def line_map(self) -> dict[int, int]:
        copy = imp.convert(self.SOURCE, self.HUB_DECK, self.DECK, COMMIT)
        return imp.build_line_map(self.SOURCE, copy, self.HUB_DECK, self.DECK, COMMIT)

    def test_line_map_follows_dropped_sections_and_frontmatter(self) -> None:
        source = self.SOURCE.splitlines()
        copy = imp.convert(self.SOURCE, self.HUB_DECK, self.DECK, COMMIT).splitlines()
        hub_line = source.index("Эпиграф: «Форма следует функции»") + 1
        mapping = self.line_map()
        self.assertEqual(copy[mapping[hub_line] - 1], "Эпиграф: «Форма следует функции»")
        self.assertNotEqual(mapping[hub_line], hub_line)
        dropped = source.index("строка задачи") + 1
        self.assertNotIn(dropped, mapping)

    def test_anchor_and_label_are_recomputed_for_the_copy(self) -> None:
        maps = {self.DECK: self.line_map()}
        hub_line = self.SOURCE.splitlines().index("Эпиграф: «Форма следует функции»") + 1
        text = f"[{self.HUB_DECK}, строка {hub_line}]({BLOB}/{self.HUB_DECK}#L{hub_line})"
        result = imp.rewrite_links(text, self.QUOTES, imp.DOMAIN, COMMIT, maps)
        new_line = maps[self.DECK][hub_line]
        self.assertEqual(result, f"[day-04/presentation.md, строка {new_line}](../day-04/presentation.md#L{new_line})")

    def test_line_without_copy_keeps_pinned_hub_link(self) -> None:
        maps = {self.DECK: self.line_map()}
        dropped = self.SOURCE.splitlines().index("строка задачи") + 1
        text = f"[{self.HUB_DECK}, строка {dropped}]({BLOB}/{self.HUB_DECK}#L{dropped})"
        result = imp.rewrite_links(text, self.QUOTES, imp.DOMAIN, COMMIT, maps)
        self.assertEqual(result, f"[{self.HUB_DECK}, строка {dropped}]({PINNED}/{self.HUB_DECK}#L{dropped})")

    def test_heading_anchor_is_not_touched(self) -> None:
        maps = {self.DECK: self.line_map()}
        text = f"[слайд]({BLOB}/{self.HUB_DECK}#слайд-1)"
        result = imp.rewrite_links(text, self.QUOTES, imp.DOMAIN, COMMIT, maps)
        self.assertEqual(result, "[слайд](../day-04/presentation.md#слайд-1)")

    def test_pin_text_pins_only_hub_main_urls(self) -> None:
        text = f'BLOB = "{imp.HUB_URL}/blob/main/"\nother = "https://example.org/blob/main/x"\n'
        self.assertEqual(
            imp.pin_text(text, COMMIT),
            f'BLOB = "{imp.HUB_URL}/blob/{COMMIT}/"\nother = "https://example.org/blob/main/x"\n',
        )


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
            deck = Path(hub) / imp.DOMAIN / "2026-11-03-day4-presentation-gamma-v5.md"
            deck.write_text("---\nstatus: draft\nissue: 1\nmethod: m\n---\n\n# Колода\n\nЭпиграф\n", encoding="utf-8")
            quotes = Path(hub) / imp.DOMAIN / "2026-11-01-course-quotes-days-1-4-alce.md"
            quotes.write_text(
                "---\nstatus: draft\n---\n\n# Цитаты\n\n"
                f"[2026-11-03-day4-presentation-gamma-v5.md, строка 9]({BLOB}/2026-11-03-day4-presentation-gamma-v5.md#L9)\n",
                encoding="utf-8",
            )
            provenance = Path(hub) / imp.DOMAIN / "exp" / "quotes-711"
            provenance.mkdir(parents=True)
            (provenance / "README.md").write_text("---\nstatus: draft\n---\n\n# Сборщик\n", encoding="utf-8")
            (provenance / "build.py").write_text(f'BLOB = "{imp.HUB_URL}/blob/main/"\n', encoding="utf-8")
            with open(Path(root) / "log", "w", encoding="utf-8") as log:
                stdout, sys.stdout = sys.stdout, log
                try:
                    code = imp.main(["--hub", hub, "--root", root, "--commit", COMMIT])
                finally:
                    sys.stdout = stdout
            self.assertEqual(code, 0)
            for target in imp.MAPPING.values():
                self.assertTrue((Path(root) / target).is_file(), target)
            copy = (Path(root) / imp.MAPPING["2026-11-01-course-quotes-days-1-4-alce.md"]).read_text(encoding="utf-8")
            # Line 9 of the Hub deck ("Эпиграф") is line 8 of the copy: two task fields dropped, `source` added.
            self.assertIn("[day-04/presentation.md, строка 8](../day-04/presentation.md#L8)", copy)
            local = Path(root) / imp.PROVENANCE["exp/quotes-711"]
            self.assertIn(f"/blob/{COMMIT}/", (local / "build.py").read_text(encoding="utf-8"))
            manifest = (local / imp.PROVENANCE_MANIFEST).read_text(encoding="utf-8").splitlines()
            self.assertEqual([row.split("\t")[0] for row in manifest[2:]], ["README.md", "build.py"])
            self.assertIn("blob/main -> blob/<commit>", manifest[3])

    def test_main_fails_without_provenance_directory(self) -> None:
        with tempfile.TemporaryDirectory() as hub, tempfile.TemporaryDirectory() as root:
            for rel in imp.MAPPING:
                path = Path(hub) / imp.DOMAIN / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("# T\n", encoding="utf-8")
            with open(Path(root) / "log", "w", encoding="utf-8") as log:
                stdout, sys.stdout = sys.stdout, log
                try:
                    with self.assertRaises(FileNotFoundError):
                        imp.main(["--hub", hub, "--root", root, "--commit", COMMIT])
                finally:
                    sys.stdout = stdout


if __name__ == "__main__":
    unittest.main()
