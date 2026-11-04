"""Course invariants owned by this repository (issue #3, Hub RFC #721 S-1).

The Hub RFC leaves it to the spoke to pick the course invariants CI checks
(the Hub builder of the quotes list is not executed here). Two are checked:

1. Every ``#Lnnn`` link of the quotes list to a local file points to a line
   that carries the quoted text. Anchors are line numbers: an edit above the
   quote shifts it, and the link silently points to a wrong line. This is the
   failure the Hub hit in #711 (Hub L591 is L581 in the course copy).
2. No tracked text file links the Hub domain ``research/reputation-technologies``
   on the floating ``main`` branch: the Hub removes the domain (RFC step 3),
   such links return 404 then; they must be pinned to a commit.

Run: python3 -m unittest discover -s tests -v
"""
from __future__ import annotations

import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUOTES = ROOT / "education/technograd-reputation-engineering/handouts/course-quotes-days-1-4-alce.md"
LINE_LINK = re.compile(r"\[([^\]]*)\]\(([^)\s#]+)#L(\d+)(?:-L\d+)?\)")
GUILLEMETS = re.compile(r"«([^«»]{8,})»")
FLOATING = re.compile(r"hybrid-Intelligence-lab/(?:blob|tree)/main/research/reputation-technologies")
MIN_FRAGMENT = 8


def norm(text: str) -> str:
    """Drop link targets and emphasis, collapse spaces."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.replace(" ", " ").replace("**", "").replace("*", "")
    return re.sub(r"\s+", " ", text).strip()


def fragments(entry: list[str]) -> list[str]:
    """Quoted text of one entry: the blockquote, translations «…», deck wording."""
    raw = []
    for line in entry:
        if line.startswith("> "):
            quote = re.sub(r"\s*\[\d+\]\s*$", "", line[2:]).strip()
            raw.append(quote.strip('"«»“”'))
        raw.extend(GUILLEMETS.findall(line))
    out = []
    for frag in raw:
        for piece in re.split(r"…|\.\.\.|\[…\]", frag):
            piece = norm(piece).strip(" .,;:—-\"'“”")
            if len(piece) >= MIN_FRAGMENT:
                out.append(piece)
    return out


def entries(text: str) -> list[list[str]]:
    """Quote entries are ``### `` sections; a ``## `` heading closes the entry."""
    found: list[list[str]] = []
    current: list[str] | None = None
    for line in text.splitlines():
        if line.startswith("### "):
            current = [line]
            found.append(current)
        elif line.startswith("## "):
            current = None
        elif current is not None:
            current.append(line)
    return found


def anchor_problems(text: str, base: Path) -> tuple[int, list[str]]:
    """Return (local line links checked, problems); links resolve from ``base``."""
    checked, problems = 0, []
    for entry in entries(text):
        frags = fragments(entry)
        for line in entry:
            for _, target, number in LINE_LINK.findall(line):
                if target.startswith(("http://", "https://")):
                    continue
                checked += 1
                where = f"{entry[0][:60]} -> {target}#L{number}"
                lines = (base / target).read_text(encoding="utf-8").splitlines()
                n = int(number)
                if not 1 <= n <= len(lines):
                    problems.append(f"{where}: line out of range 1..{len(lines)}")
                elif not any(f in norm(lines[n - 1]) for f in frags):
                    problems.append(f"{where}: quoted text not on the line: {norm(lines[n - 1])[:120]}")
    return checked, problems


class QuoteAnchorsTest(unittest.TestCase):
    def test_every_local_line_link_points_to_the_quote(self) -> None:
        checked, problems = anchor_problems(QUOTES.read_text(encoding="utf-8"), QUOTES.parent)
        self.assertGreater(checked, 0, "no local #L links found: the check would pass vacuously")
        self.assertEqual(problems, [], "\n".join(problems))

    def test_shifted_anchor_is_detected(self) -> None:
        """Mutation: anchors moved by an edit above the quotes must fail the check.

        The shift is 10 lines: with 1 line two quotes still match by chance,
        because the next deck line repeats a name from the epigraph.
        """
        shifted = LINE_LINK.sub(
            lambda m: m.group(0) if m.group(2).startswith("http")
            else m.group(0).replace(f"#L{m.group(3)}", f"#L{int(m.group(3)) + 10}", 1),
            QUOTES.read_text(encoding="utf-8"),
        )
        checked, problems = anchor_problems(shifted, QUOTES.parent)
        self.assertGreater(checked, 0)
        self.assertEqual(len(problems), checked, "every shifted anchor must be reported")


class FloatingHubLinksTest(unittest.TestCase):
    def test_no_floating_links_to_hub_domain(self) -> None:
        files = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "-z"], capture_output=True, text=True, check=True
        ).stdout.split("\0")
        hits = []
        for rel in filter(None, files):
            path = ROOT / rel
            if not path.is_file():
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            hits += [f"{rel}:{i}" for i, line in enumerate(text.splitlines(), 1) if FLOATING.search(line)]
        self.assertEqual(hits, [], "pin Hub domain links to a commit (tools/import_from_hub.py --commit)")


if __name__ == "__main__":
    unittest.main()
