---
status: reviewed
version: 1.1
updated: 2026-11-04
temperature: 0.1
type: analysis
source: "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/32b5fa524e542af23c1a8e67c919bd66d5f4e399/research/reputation-technologies"
---

# Инвентаризация переноса из Хаба

> Что перенесено из каталога Хаба `research/reputation-technologies` (снимок
> 32b5fa5, 159 файлов), что осталось и почему. Правила переноса — issue
> [#1](https://github.com/G-Ivan-A/aether-orbis-gra/issues/1) и
> [ADR-001](../adr/2026-11-adr-001-separate-repository-and-ssot.md). Перенос
> выполняет `tools/import_from_hub.py`.

## Правила

1. **Переносится** то, что описывает проект и позволяет его развивать:
   текущая исследовательская модель, текущие материалы курса, ранние
   документы как история.
2. **Не переносится:** задачи, PR, рабочие версии, эксперименты, устаревшие
   документы, глобальные исследования. На них даются абсолютные ссылки на
   зафиксированный коммит Хаба.
3. **При переносе** из файлов удаляются разделы, документирующие исполнение
   задач (самопроверки против issue, решения исполнителя, апелляции, журналы
   версий по задачам). Ссылки на перенесённые файлы становятся
   относительными, ссылки на задачи и PR Хаба — простым текстом. Текст по
   существу не меняется.
4. **Ссылки на домен Хаба, который не перенесён**, закрепляются на коммите
   Хаба из поля `source`, а не на `main`: Хаб убирает домен из дерева (RFC
   Хаба #721), и ссылки `blob/main` начнут отдавать 404. Якоря строк `#Lnnn`
   пересчитываются по строкам копии. Правило добавлено задачей
   [#3](https://github.com/G-Ivan-A/aether-orbis-gra/issues/3).

## Перенесено (35 файлов)

| Что | Откуда (в Хабе) | Куда | Статус |
| --- | --- | --- | --- |
| Исследовательская модель GRA, 6 файлов | `gra-research-program/00…50` | [methodology/research-program/](../../methodology/research-program/README.md) | Текущая версия |
| Логика курса (RFC дней 1–4) | `2026-10-12-rfc-days-1-3-logic.md` | `education/…/course-logic.md` | Текущая версия (v0.3) |
| День 1: колода, сценарий, обоснование, стандарт слайда | `2026-10-14-day1-presentation-gamma.md`, `2026-10-14-day1-lecturer-script.md`, `2026-10-07-day1-rationale-and-method-653.md`, `2026-10-15-day1-slide-standard-and-gate-677.md` | `education/…/day-01/` | Текущие версии |
| День 2: колода, сценарий, обоснование | `2026-10-30-day2-{presentation-gamma,lecturer-script,rationale-and-method}.md` | `education/…/day-02/` | Текущие версии |
| День 3: колода, сценарий, обоснование, стандарт слайда | `2026-11-02-day3-{presentation-gamma,lecturer-script,rationale-and-method,slide-standard-and-gate}.md` | `education/…/day-03/` | Текущие версии |
| День 4: колода, сценарий, промпты изображений | `2026-11-03-day4-{presentation-gamma-v5,lecturer-script-v5,image-prompts-v5-couturier-constructor}.md` | `education/…/day-04/` | Вариант 5 — текущий |
| Имидж-технологии, 6 файлов (не GRA) | `image-technologies/00…50` | [day-04/resources/image-technologies/](../../education/technograd-reputation-engineering/day-04/resources/image-technologies/README.md) | Справочник дня 4 |
| Раздаточные материалы и реестр промптов | `2026-10-24-handout-materials-master-prompt-registry-days-1-4.md`, `2026-10-30-day1-osint-pipeline-design.md`, `exp/day1-osint-709/2026-10-30-ten-company-example.md` | `education/…/handouts/` | Текущие версии |
| Документы этапа I, 5 файлов | `2026-06-20-*` | [docs/history/](../history.md#документы-этапа-i) | `superseded`, с предупреждением |

## Осталось в Хабе

| Файл или каталог | Почему не перенесён | Где используется здесь |
| --- | --- | --- |
| `README.md` домена | Индекс Хаба с историей задач; заменён документами L1–L4 | — |
| [`2026-06-29-partner-attraction-strategy.ru.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/32b5fa524e542af23c1a8e67c919bd66d5f4e399/research/reputation-technologies/2026-06-29-partner-attraction-strategy.ru.md) | Стратегическое исследование Хаба; часть выводов устарела (ранний «индекс» до операционализации) | Учтено в треке C [дорожной карты](../roadmap.md) |
| [`2026-09-24-introductory-course-options-610.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/32b5fa524e542af23c1a8e67c919bd66d5f4e399/research/reputation-technologies/2026-09-24-introductory-course-options-610.md) | Сравнение вариантов курса до выбора программы | — |
| [`2026-09-30-course-sources-and-presentations-650.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/32b5fa524e542af23c1a8e67c919bd66d5f4e399/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md) | Исследование источников курса (глобальное исследование) | Коды `[650:X]` в материалах курса ведут на него |
| `2026-10-07-day1-{lecturer-script,presentation}-653.md` | Ранние версии дня 1, заменены версиями 14.10 | — |
| `2026-10-13-day1-rebuild-task-671.md` | Постановка задачи | — |
| [`2026-10-14-day1-lecturer-gra-research.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/32b5fa524e542af23c1a8e67c919bd66d5f4e399/research/reputation-technologies/2026-10-14-day1-lecturer-gra-research.md) | Исследование открытых данных о конкретном человеке (лекторе): персональные данные не тиражируются | Ссылка из колоды дня 2 |
| `2026-10-30-day2-presentation.md`, `2026-11-02-day3-presentation.md` | Предыдущий формат колод (тезисы и промпты), заменён версиями для Gamma | — |
| `2026-11-03-day4-presentation-gamma{,-v2,-v3,-v4}.md`, `…-lecturer-script{,-v3}.md`, `…-rationale-and-method{,-v2}.md` | Варианты 1–4 дня 4; вариант 1 — исторический документ провала интерпретации | — |
| [`2026-11-03-rfc-presentation-update-v5.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/32b5fa524e542af23c1a8e67c919bd66d5f4e399/research/reputation-technologies/2026-11-03-rfc-presentation-update-v5.md) | Описание изменений колоды v4 → v5 (рабочий документ задачи) | Ссылка из справочника имидж-технологий |
| [`2026-11-03-day4-ai-interpretation-analysis.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/32b5fa524e542af23c1a8e67c919bd66d5f4e399/research/reputation-technologies/2026-11-03-day4-ai-interpretation-analysis.md) | Разбор провала интерпретации ИИ (рабочий документ задачи) | Урок 2 в [history.md](../history.md#уроки) |
| [`2026-11-03-day4-crisis-mitigation-rfc.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/32b5fa524e542af23c1a8e67c919bd66d5f4e399/research/reputation-technologies/2026-11-03-day4-crisis-mitigation-rfc.md) | План замен в днях 1–3, `draft`, не применён без согласования автора | Известная проблема в [карте курса](../../education/technograd-reputation-engineering/README.md#известная-проблема-формулировки-дней-13-за-границей-gra) |
| `gra-research-program/presentation-rfc/` | RFC отклонён (`rejected`) | — |
| `exp/` (21 каталог, 102 файла) | Эксперименты и проверки задач | Один учебный пример перенесён в handouts |

## Доимпорт 2026-11-04 (issue #3)

Снимок Хаба — [`48ebe52`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies),
слияние PR #722 Хаба (RFC #721). После снимка `32b5fa5` в домене изменились
15 файлов. Как обработан каждый:

| Что | Откуда (в Хабе) | Куда | Почему |
| --- | --- | --- | --- |
| Список цитат курса (дни 1–4, ALCE) | `2026-11-01-course-quotes-days-1-4-alce.md` | [education/…/handouts/course-quotes-days-1-4-alce.md](../../education/technograd-reputation-engineering/handouts/course-quotes-days-1-4-alce.md) | Создан после снимка `32b5fa5` (класс R3 инвентаря Хаба). Якоря строк пересчитаны по копиям колод: эпиграф слайда 24 дня 4 — строка 581 копии, а не 591 Хаба |
| Сборщик и журналы списка цитат, 13 файлов | `exp/quotes-711/` | [education/…/handouts/course-quotes-provenance/](../../education/technograd-reputation-engineering/handouts/course-quotes-provenance/README.md) | Исключение из правила 2 по RFC #721 (Ш2.2): провенанс списка. Не исполняется; SHA-256 оригиналов — в `provenance-manifest.tsv` |
| `README.md` домена | `README.md` | — | Добавлена строка индекса о списке цитат; индекс не переносится (см. выше) |

35 ранее перенесённых файлов импортированы заново с того же снимка. По
существу они не изменились: поменялись только поле `source` и 167 ссылок на
неперенесённые файлы домена, которые теперь закреплены на `48ebe52` (правило 4).
Источники #650 (Q-3 RFC) и файл с персональными данными (Q-4) остались в Хабе,
ссылки на них закреплены. Пункт 2 предложений для Хаба ниже заменён решением
Хаба: RFC #721 и ADR-022 убирают домен из дерева и оставляют архив тегом.

## Что не переносилось в принципе

- Задачи и PR Хаба (по постановке issue #1).
- Файл с перепиской и вспомогательный текст, приложенные к issue: это
  источники для [истории](../history.md), а не документы проекта.
- Правила Хаба: на них даются абсолютные ссылки, копируется только набор
  файлов HTOM, который Хаб предписывает проектам.

## Предложения для Хаба (вне этого репозитория)

1. ADR в Хабе о выделении GRA в отдельный проект со ссылкой на этот
   репозиторий.
2. Указатель в `research/reputation-technologies/README.md` Хаба: текущая
   версия — здесь. Файлы в Хабе не удаляются, чтобы не ломать ссылки.
