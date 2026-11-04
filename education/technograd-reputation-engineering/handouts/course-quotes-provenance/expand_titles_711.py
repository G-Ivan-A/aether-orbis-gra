#!/usr/bin/env python3
"""One-off rewrite of the source titles in quotes_711_data.py (issue #711).

The issue asks for the full title of the source without abbreviations. The first
data draft stored titles in citation style: «Tinbergen J. Shaping the World
Economy… pp. 262–293», «Каукин А. С., Идрисов Г. И. … № 4. С. 133–154».
The author names are already given in full in the «Авторы» field, so this script

  * removes the leading author list in initials (and corporate-author prefixes),
  * removes author lists in initials inside «цитируется по: …» parts,
  * spells out bibliographic abbreviations: pp. → pages, No. → Number,
    № → номер, С. → страницы, «88 с.» → «88 страниц», ПАО → Публичное акционерное общество.

Run once: python3 -I expand_titles_711.py [--write]; without --write it prints
the old and new title of every changed source for review. check-quotes-711.py
then rejects any title that still starts with initials or contains these
abbreviations.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "quotes_711_data.py"

UP = "A-ZА-ЯЁ"
NAME = rf"(?:van den |van der )?[{UP}][^\s,.()]*"
INITS = rf"(?: [{UP}]\.(?:-[{UP}]\.)?)+"
AUTHOR = NAME + INITS
LIST = rf"{AUTHOR}(?:, {AUTHOR})*(?:, Jr\.)?(?: et al\.)?"
LEAD = re.compile(rf"^{LIST} ")
CITED = re.compile(rf"(цитируется по: ){LIST}(?: |, )")

# Titles that need a hand-written form (embedded editors, corporate authors,
# a first author without initials).
MANUAL = {
    "Д1": "PROV-DM: The PROV Data Model / edited by Luc Moreau, Paolo Missier. World Wide Web Consortium Recommendation, 30 April 2013",
    "Д2": "Intelligence Community Directive 203: Analytic Standards",
    "Д5": "Field Manual 2-22.3 (Field Manual 34-52): Human Intelligence Collector Operations. Washington, District of Columbia: Headquarters, Department of the Army, 2006. Appendix B «Source and Information Reliability Matrix»",
    "Д7": "Barcelona Principles 4.0 (электронная книга)",
    "Н6": "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)",
    "Н7": "Reduce Hallucinations // Claude Documentation: Test and Evaluate — Strengthen Guardrails",
    "Н8": "Prompt Engineering // OpenAI Application Programming Interface Documentation: Guides",
    "Н9": "Основы промпт-инжиниринга // Документация GigaChat API, раздел Prompts Hub",
    "Н10": "Кодекс этики в сфере искусственного интеллекта",
    "П8": "Концепция «спирали молчания» в контексте политической коммуникации // Litera. 2025. Номер 12. Страницы 240–254",
    "С4a": "The People's Choice: How the Voter Makes Up His Mind in a Presidential Campaign. 2nd edition. New York: Columbia University Press, 1948, page 151, цитируется по: A Revision of the Two-Step Flow of Communications Hypothesis, 1964",
    "С4b": "The Two-Step Flow of Communication: An Up-To-Date Report on an Hypothesis // Public Opinion Quarterly. 1957. Volume 21, Number 1. Pages 61–78, цитируется по: A Revision of the Two-Step Flow of Communications Hypothesis, 1964 (точная страница не установлена)",
    "С5a": "Strategic Management, Publics, and Issues // Excellence in Public Relations and Communication Management / edited by James E. Grunig. Hillsdale, New Jersey: Lawrence Erlbaum Associates, 1992, page 128, цитируется по: Identifying and Prioritizing Stakeholders for Public Relations — A Guide for Students and Practitioners. Gainesville, Florida: Institute for Public Relations, 2023, page 5",
    "Д3-Т3": "Centrality in Social Networks: Conceptual Clarification // Social Networks. 1978–1979. Volume 1. Pages 215–239",
    "Д3-Т4": "Structural Holes versus Network Closure as Social Capital // Social Capital: Theory and Research / edited by Nan Lin, Karen S. Cook, Ronald S. Burt. New York: Aldine de Gruyter, 2001 (препринт 2000)",
    "О19": "Silent Messages — страница автора с описанием книги на сайте kaaj.com",
    "О21": "Представление себя другим в повседневной жизни / перевод с английского и вступительная статья Александра Дмитриевича Ковалёва; научный редактор М. С. Ковалёва. Москва: КАНОН-пресс-Ц; Кучково поле, 2000",
}


def expand(title: str) -> str:
    t = LEAD.sub("", title, count=1)
    t = CITED.sub(r"\1", t)
    t = re.sub(r"\bpp\. ", "pages ", t)
    t = re.sub(r"\bNo\. ", "Number ", t)
    t = re.sub(r"(^|\. )№ ", r"\1Номер ", t)
    t = t.replace("№ ", "номер ")
    t = re.sub(r"(^|\. )С\. (\d)", r"\1Страницы \2", t)
    t = re.sub(r"(\d) с\. \(", r"\1 страниц (", t)
    t = re.sub(r"(\d) с\.", r"\1 страниц.", t)
    t = re.sub(r"\bс\. (\d)", r"страницы \1", t)
    t = t.replace("ПАО ", "Публичное акционерное общество ")
    return t


def main() -> int:
    sys.path.insert(0, str(HERE))
    import quotes_711_data as q
    text = DATA.read_text(encoding="utf-8")
    changed = 0
    for key, s in q.SOURCES.items():
        old = s["title"]
        new = MANUAL.get(key) or expand(old)
        if new == old:
            continue
        literal = f'title="{old}"'
        assert text.count(literal) == 1, key
        text = text.replace(literal, f'title="{new}"')
        changed += 1
        print(f"{key}\n  - {old}\n  + {new}")
    print(f"{changed} titles changed")
    if "--write" in sys.argv:
        DATA.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
