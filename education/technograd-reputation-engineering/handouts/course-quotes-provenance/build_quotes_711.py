#!/usr/bin/env python3
"""Build the quote list of issue #711 (one file, ALCE markup).

Reads the quotes from their repository lines (catalogue of #650 via
extract_650.py plus EXTRAS from quotes_711_data.py), the interpretations
from interpretations-711.json and writes
research/reputation-technologies/2026-11-01-course-quotes-days-1-4-alce.md.

Usage:
  python3 build_quotes_711.py            # write the Markdown file
  python3 build_quotes_711.py --check    # exit 1 if the file is out of date
  python3 build_quotes_711.py --worklist OUT.json   # items for writing interpretations
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import extract_650  # noqa: E402
from quotes_711_data import (  # noqa: E402
    CAT, EPIGRAPH_OF, EXTRAS, LOCATOR, NEW, NEW_TRANSLATIONS, NOT_QUOTED_IN_DAY,
    SOURCES, SPLIT, TRIMS, D4,
)

REPO = HERE.parents[3]
OUT_REL = "research/reputation-technologies/2026-11-01-course-quotes-days-1-4-alce.md"
OUT = REPO / OUT_REL
INTERP = HERE / "interpretations-711.json"
EXCERPTS = HERE / "source-excerpts-711.txt"
BLOB = "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/"
DAYS = {
    1: "День 1. Гравитационная модель репутации, сети, доверие и репутационный капитал",
    2: "День 2. Достоверность данных, разведывательный анализ и работа с ИИ",
    3: "День 3. Стейкхолдеры, точки влияния и каналы коммуникации",
    4: "День 4. Имидж-технологии: внешность, одежда, первое впечатление",
}
# Extra trims that cut a citation or an editorial comment off the quote body.
EXTRA_TRIMS = {
    1191: (" (Freeman 1984: 46)", "Freeman 1984, p. 46, цитируется по Mitchell et al. 1997, p. 854"),
    1869: (" (в оригинале слово взято в «ёлочки») Это собственная формулировка автора статьи.", None),
}
NOTES = {
    1869: "В оригинале слово «живописное» взято в «ёлочки»; это собственная формулировка автора статьи, а не Вёльфлина.",
    1679: "Слова Г. И. Ибрагимова о принципах контекстного обучения А. А. Вербицкого.",
}
CYR = re.compile(r"[А-Яа-яЁё]")


def file_lines(rel: str) -> list[str]:
    return (REPO / rel).read_text(encoding="utf-8").splitlines()


def resolve_locator(loc: str | None, prev: str | None) -> str:
    if not loc:
        return "место в источнике в каталоге не указано"
    if loc.startswith("Там же") and prev:
        rest = loc[len("Там же"):].lstrip(" ,")
        return f"{prev}; {rest}" if rest else prev
    return loc


def collect() -> list[dict]:
    items: list[dict] = []
    prev_loc: dict[str, str] = {}
    for it in extract_650.extract():
        line = it["line"]
        quote = it["quote"]
        loc = LOCATOR.get(line) or resolve_locator(it.get("locator"), prev_loc.get(it["id"]))
        if not (it.get("locator") or "").startswith("Там же"):
            prev_loc[it["id"]] = loc
        if line in TRIMS:
            quote = quote.removesuffix(TRIMS[line]).rstrip()
        if line in EXTRA_TRIMS:
            cut, new_loc = EXTRA_TRIMS[line]
            quote = quote.removesuffix(cut).rstrip()
            loc = new_loc or loc
        n = it.get("n") or 1
        src = SPLIT.get((it["id"], n), it["id"])
        if it.get("translation"):
            translation = it["translation"]
            tmark = f"перевод из каталога #650: {CAT}:{it['translation_line']}"
        elif line in NEW_TRANSLATIONS:
            translation, tmark = NEW_TRANSLATIONS[line], NEW
        else:
            translation, tmark = None, None
        item = dict(uid=f"{it['id']}-L{line}", src=src, file=CAT, line=line, quote=quote,
                    check=quote, translation=translation, tmark=tmark, locator=loc,
                    note=NOTES.get(line))
        if line in EPIGRAPH_OF:
            slide, dline = EPIGRAPH_OF[line]
            deck = file_lines(D4)[dline - 1].split("Эпиграф: ", 1)[1].rsplit(" — ", 1)[0]
            item.update(slide=slide, deck_line=dline, deck_text=deck)
        items.append(item)
    for e in EXTRAS:
        russian_original = e["tmark"].startswith("русский оригинал")
        course_translation = e["tmark"].startswith("перевод курса")
        item = dict(uid=e["key"], src=e["src"], file=e["file"], line=e["line"], check=e["repo"],
                    locator=e["locator"], note=None, original_check=e.get("original"))
        if course_translation:
            item.update(quote=f"\"{e['original']}\"", translation=e["repo"], tmark=e["tmark"])
        elif russian_original:
            item.update(quote=e["repo"], translation=None, tmark=None)
            if e["key"] == "E15":
                item["note"] = ("В колоде слово «формула» согласовано с контекстом («…формулу…») и короткое тире "
                                "заменено длинным; на странице издательства: «" + e["original"] + "».")
        else:
            q = e["repo"] if e["repo"].startswith(("\"", "«")) else f"\"{e['repo']}\""
            item.update(quote=q, translation=e["translation"], tmark=e["tmark"])
        if e.get("slide"):
            item.update(slide=e["slide"], deck_line=e["line"])
        items.append(item)
    order = {k: i for i, k in enumerate(SOURCES)}
    for it in items:
        s = SOURCES[it["src"]]
        it["day"] = s["day"]
        if it["src"] in NOT_QUOTED_IN_DAY:
            it["note"] = ((it["note"] + " ") if it["note"] else "") + "В материалах Дня 2 прямо не цитируется; источник из каталога курса для самостоятельной работы."
    items.sort(key=lambda x: (x["day"], order[x["src"]], x["line"], x["uid"]))
    return items


def worklist(items: list[dict]) -> list[dict]:
    out = []
    for it in items:
        s = SOURCES[it["src"]]
        out.append(dict(uid=it["uid"], day=it["day"], src=it["src"], authors=s["authors"], title=s["title"],
                        status=s["status"], locator=it["locator"], quote=it["quote"],
                        translation=it.get("translation"), note=it.get("note"),
                        slide=it.get("slide"), repo=f"{it['file']}:{it['line']}"))
    return out


def full_locator(loc: str) -> str:
    """Spell out page and section abbreviations of a locator: p. 5 → страница 5."""
    def pages(m: re.Match) -> str:
        num = m.group(2)
        return ("страницы " if "–" in num or m.group(1).lower() == "pp." else "страница ") + num
    loc = re.sub(r"^VERIFIED-[A-Z]+, ", "", loc)  # the status has its own field
    loc = re.sub(r"\b(pp\.|[pP]\.|[сС]\.|стр\.) ?((?:[A-Z]-)?\d[\d–]*)", pages, loc)
    loc = loc.replace("на страница ", "на странице ")
    for short, full in (("Sec. ", "раздел "), ("sect. ", "раздел "), ("Ch. ", "глава "), ("Разд. ", "Раздел "),
                        ("П. ", "Пункт "), ("п. ", "пункт "), ("прим. ", "примечание ")):
        loc = re.sub(r"(?<![\w.])" + re.escape(short), full, loc)
    return loc.replace(" et al. ", " и соавторы, ")


def link(rel: str, line: int) -> str:
    return f"[{rel.split('/')[-1]}, строка {line}]({BLOB}{rel}#L{line})"


def tmark_text(tmark: str) -> str:
    if tmark == NEW:
        return "перевод наш (#711)"
    kind, ref = tmark.split(": ", 1)
    rel, line = ref.rsplit(":", 1)
    return f"{kind}, {link(rel, int(line))}"


HEADER = """---
status: draft
version: 1.0
updated: 2026-11-01
temperature: 0.2
source: "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/711"
scope: reputation-engineering-course-quotes-days-1-4
method: alce-citation-markup-with-traceable-evidence
related_issues:
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/650"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/653"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/683"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/697"
---

# Цитаты курса «Репутационный инжиниринг»: Дни 1–4 с разметкой ALCE

Единый список всех дословных цитат из исследований курса в `research/reputation-technologies` (issue [#711](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/711)). Его можно использовать на лекциях и раздавать слушателям. Цитаты сгруппированы по дням курса. У каждой цитаты есть:

- **цитата** — дословно, на языке источника, и перевод (если источник не на русском);
- **интерпретация** — как её читать в контексте репутационных технологий;
- **авторы** — ФИО полностью, насколько их удалось установить;
- **дата** события или публикации;
- **источник** — полное название без сокращений;
- **ссылка** на источник;
- место в источнике, статус проверки и строка репозитория, откуда цитата взята.

Файл собран скриптом [`build_quotes_711.py`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/exp/quotes-711/build_quotes_711.py); не редактируйте его вручную. Проверка — [`check-quotes-711.py`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/exp/quotes-711/check-quotes-711.py): каждая цитата дословно совпадает с указанной строкой репозитория, каждая ссылка [n] ведёт в список источников.

## Как устроена разметка ALCE

Разметка следует стандарту ALCE (Tianyu Gao, Howard Yen, Jiatong Yu, Danqi Chen. Enabling Large Language Models to Generate Text with Citations, 2023; в каталоге курса — источник Н4, см. День 2):

1. Каждое утверждение несёт маркер `[n]`. Маркер стоит после цитаты и после интерпретации.
2. Маркер `[n]` ведёт к записи `n` в разделе «Список источников (ALCE)» в конце файла. Там — авторы, дата, полное название, ссылка и статус проверки.
3. Опорный фрагмент (passage) для каждого утверждения — сама цитата. Интерпретация опирается только на неё и на источник `[n]`; если вывод выходит за пределы источника, это сказано прямо.
4. Номера `[n]` присвоены по порядку первого появления источника в файле.

Статусы проверки (как в каталоге [#650](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md)):

- `VERIFIED-FULLTEXT` — цитата сверена с полным текстом источника;
- `VERIFIED-ABSTRACT` — сверена с официальной аннотацией;
- `VERIFIED-SECONDARY` — сверена по вторичному источнику, который назван в поле «Источник»;
- `VERIFIED (колода v5, решение 7)` — эпиграф Дня 4, сверенный с источником из подписи слайда; исходный текст для #711 сверен ещё раз и сохранён в [`source-excerpts-711.txt`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/exp/quotes-711/source-excerpts-711.txt).

Источники со статусом `UNVERIFIED` цитат не дают и в список не входят.

Переводы: «перевод из каталога #650» и «перевод курса» — уже принятые в репозитории; «перевод наш (#711)» — сделан для этого списка, потому что в репозитории перевода не было.

## Как пользоваться

- Для слайда или раздаточного материала берите цитату вместе с маркером `[n]` и записью `n` из списка источников.
- Интерпретация — это подсказка лектору, а не слова автора. Не выдавайте её за цитату.
- Цитаты со статусом `VERIFIED-SECONDARY` приводите с пометкой «цитируется по…».
- Цитаты, помеченные «слова автора статьи» или «слова обзора», не приписывайте классику, о котором идёт речь.
"""

BOUNDARY = """## Границы списка

**Что входит.** Дословная цитата с указанием автора и источника, проверенная по источнику, из этих мест репозитория:

- каталог источников курса [#650](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md) — все цитаты серий Г, Д, С, Н, П, О;
- таблица источников М1–М7 в [обосновании Дня 1](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-10-07-day1-rationale-and-method-653.md);
- записи R:Simini и R:Gentner в [программе исследований GRA](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/gra-research-program/50-open-research.md);
- таблица источников Д3-Т3…Д3-Т5 в [обосновании Дня 3](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-11-02-day3-rationale-and-method.md);
- эпиграфы всех слайдов [презентации Дня 4, версия 5](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-11-03-day4-presentation-gamma-v5.md).

**Что не входит и почему.**

- Эпиграфы и тезисы презентаций Дней 1–3 — это формулировки самого курса, а не цитаты источников.
- Высказывания основателей кейсов и формулировки лектора — не опубликованные источники.
- Пересказы (например, Д3-Т1 и Д3-Т2 в обосновании Дня 3) — не дословные цитаты.
- Короткие цитатные фрагменты в тексте модуля `image-technologies` — те же источники уже есть в списке через каталог #650 или эпиграфы Дня 4.
- Источники со статусом `UNVERIFIED` в каталоге #650 (Г2, Д14, Н13, П5, П6, П11, О2) и определение репутации у Fombrun (1996, страница 72): каталог прямо говорит, что их не цитируют.
"""

GAPS = """## Пробелы и решения

- **ФИО не установлены полностью.** Отчество Г. И. Идрисова (Г4) и О. И. Шипкова (О7); полные имена И. Джонек-Ковальской (С7), Ю. А. Моисеенковой (С9), М. С. Ковалёвой (О21), О. Серовой (О6) и A. W. van den Ban (С4). В открытых источниках, доступных при подготовке, их нет; в полях «Авторы» это сказано прямо.
- **Переводчики** русского издания К. Левина (Г7) не установлены.
- **Выходные данные Г7.** Каталог указывает издательство «Сенсор», а у В. А. Лукова — «Речь»; противоречие записано, не разрешено.
- **Дата принятия Кодекса этики в сфере ИИ (Н10)** в извлечённом тексте не найдена; адрес PDF в каталоге повреждён, поэтому дана ссылка на сайт кодекса.
- **«Кодекс стиля».** По решению [RFC v5](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-11-03-rfc-presentation-update-v5.md) (строка 36) имена авторов справочника в материалах курса не воспроизводятся; список следует этому решению. Расшифровка аббревиатуры «НИА» в репозитории не найдена, поэтому она дана как в колоде.
- **Номера страниц «Кодекса стиля».** В записях указан номер страницы PDF-файла, где найдена цитата, и диапазон из подписи слайда.
- **Эпиграфы Дня 4 — переводы курса.** Колода часто переводит часть длинной фразы. В поле «Цитата» стоит точный отрезок оригинала, которому соответствует перевод; полные фразы — в [`source-excerpts-711.txt`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/exp/quotes-711/source-excerpts-711.txt).
- **И. Иттен (слайд 4).** Экземпляр archive.org из подписи слайда выдаётся только по записи; текст сверен по другому открытому скану того же издания 1973 года (`johannes-ittens-the-art-of-color`).
- **Г. Зиммель (слайд 19).** Фраза эпиграфа — первое предложение аннотации редакции к публикации 1957 года, а не текст самого Зиммеля.
- **M. M. Baker (слайд 21).** Пособие датировано «Reviewed 11-2020»; год первого выпуска в PDF не указан.
"""


def render(items: list[dict], interp: dict[str, str]) -> str:
    refs: dict[str, int] = {}
    for it in items:
        refs.setdefault(it["src"], len(refs) + 1)
    out = [HEADER]
    counts = {d: sum(1 for i in items if i["day"] == d) for d in DAYS}
    out.append("## Содержание\n")
    for d, title in DAYS.items():
        out.append(f"- [{title}](#{anchor(title)}) — {counts[d]} цитат")
    out.append(f"\nВсего цитат: {len(items)}; источников: {len(refs)}.\n")
    for d, title in DAYS.items():
        out.append(f"## {title}\n")
        k = 0
        for it in (i for i in items if i["day"] == d):
            k += 1
            n = refs[it["src"]]
            s = SOURCES[it["src"]]
            out.append(f"### {d}.{k}. {short_author(it['src'], s['authors'])} — {it['src']} [{n}]\n")
            out.append(f"> {it['quote']} [{n}]\n")
            if it.get("translation"):
                out.append(f"- **Перевод:** {it['translation']} ({tmark_text(it['tmark'])})")
            elif not CYR.search(it["quote"][:80]):
                out.append("- **Перевод:** перевода нет")
            text = interp.get(it["uid"], "").strip()
            out.append(f"- **Интерпретация для репутационных технологий:** {text or 'НЕТ ИНТЕРПРЕТАЦИИ'} [{n}]")
            out.append(f"- **Авторы:** {s['authors']}")
            out.append(f"- **Дата:** {s['date']}")
            out.append(f"- **Источник:** {s['title']}")
            out.append(f"- **Ссылка:** {s['url']}")
            out.append(f"- **Место в источнике:** {full_locator(it['locator'])}")
            out.append(f"- **Статус проверки:** {s['status']}")
            if it.get("original_check") and it["uid"] != "E15":
                out.append(f"- **Сверка с источником:** текст источника сохранён в [{EXCERPTS.name}]({BLOB}{EXCERPTS.relative_to(REPO).as_posix()}) под ключом `{it['uid']}`")
            where = link(it["file"], it["line"])
            if it.get("slide") and it["file"] != D4:
                where += f"; эпиграф слайда {it['slide']}: {link(D4, it['deck_line'])}, в колоде: {it['deck_text']}"
            elif it.get("slide"):
                where = f"эпиграф слайда {it['slide']}, {where}"
            out.append(f"- **Где в репозитории:** {where}")
            if it.get("note"):
                out.append(f"- **Примечание:** {it['note']}")
            out.append("")
    out.append(BOUNDARY)
    out.append(GAPS)
    out.append("## Список источников (ALCE)\n")
    for src, n in refs.items():
        s = SOURCES[src]
        authors = s['authors'] if s['authors'].endswith(".") else s['authors'] + "."
        out.append(f"[{n}] {authors} {s['title']}. Дата: {s['date']}. {s['url']} — {s['status']}. Ключ в материалах курса: {src}.\n")
    return "\n".join(out).rstrip() + "\n"


HEAD_AUTHOR = {
    "E-kodeks": "«Кодекс стиля» (Бератор-паблишинг)",
    "E-belyaeva": "Беляева-Экземплярская С. Н., аннотация URSS",
    "E-eksmo": "Трубецкова И. А., Найденская Н. Г., аннотация «Эксмо»",
}


def short_author(src: str, authors: str) -> str:
    if src in HEAD_AUTHOR:
        return HEAD_AUTHOR[src]
    plain = re.sub(r"\([^)]*\)", "", authors)
    people = [p.strip() for p in plain.split(";") if p.strip() and p.strip()[0].isupper()]
    first = re.split(r"[;(]| — ", authors, maxsplit=1)[0].strip().rstrip(",")
    return first + (" и соавторы" if len(people) > 1 else "")


def anchor(title: str) -> str:
    a = title.lower()
    a = re.sub(r"[^\w\- ]", "", a)
    return a.replace(" ", "-")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--worklist")
    args = ap.parse_args()
    items = collect()
    if args.worklist:
        Path(args.worklist).write_text(json.dumps(worklist(items), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"worklist: {len(items)} items")
        return 0
    interp = json.loads(INTERP.read_text(encoding="utf-8")) if INTERP.exists() else {}
    text = render(items, interp)
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            print(f"FAIL: {OUT_REL} is out of date; run build_quotes_711.py")
            return 1
        print(f"OK: {OUT_REL} is up to date ({len(items)} quotes)")
        return 0
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT_REL}: {len(items)} quotes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
