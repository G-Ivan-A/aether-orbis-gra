---
status: draft
version: 0.2
updated: 2026-11-08
temperature: 0.1
---

# Changelog

Все заметные изменения репозитория записываются здесь. Формат —
[Keep a Changelog](https://keepachangelog.com/ru/1.1.0/).

## [Unreleased]

### Added

- Issue [#5](https://github.com/G-Ivan-A/aether-orbis-gra/issues/5):
  [постановка прикладного исследования](docs/analysis/2026-11-08-issue-5-research-plan.md)
  с последовательным WBS, протоколом evidence, проверками границ и явной
  границей публикации кейса. План сам по себе не закрывает исследование.
- Issue [#3](https://github.com/G-Ivan-A/aether-orbis-gra/issues/3) — подготовка
  к удалению домена GRA из Хаба (S-1 RFC Хаба #721, снимок
  [48ebe52](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies)):
  - [список цитат курса](education/technograd-reputation-engineering/handouts/course-quotes-days-1-4-alce.md)
    с якорями строк, пересчитанными по копиям колод, и его
    [провенанс](education/technograd-reputation-engineering/handouts/course-quotes-provenance/README.md)
    (сборщик `exp/quotes-711/` Хаба, не исполняется);
  - [бэклог проекта](ops/backlog.md): S-1, задачи B-230, B-231, B-233,
    принятые из Хаба, и предложения GRA-002…GRA-006;
  - инварианты курса в CI (`tests/test_course_quotes.py`): ссылка `#Lnnn`
    указывает на строку с цитатой, плавающих ссылок на домен Хаба нет;
    проверка якорей строк в `tools/validate_repo.py`;
  - [анализ исполнения](docs/analysis/2026-11-04-hub-extraction-completion-s1.md)
    и доказательства в `experiments/`.
- Issue [#1](https://github.com/G-Ivan-A/aether-orbis-gra/issues/1) — выделение
  проекта GRA из Хаба `hybrid-Intelligence-lab` (снимок
  [32b5fa5](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/32b5fa524e542af23c1a8e67c919bd66d5f4e399/research/reputation-technologies)):
  - геном HTOM Хаба: `AGENTS.md`, правила для ИИ, `.hub-profile.json`,
    проверка структуры;
  - документация уровней L1–L4: [видение](docs/vision.md),
    [концепция](docs/concept.md), [методология](docs/methodology.md),
    [дорожная карта](docs/roadmap.md); [глоссарий](docs/glossary.md),
    [история](docs/history.md), [реестр источников](docs/sources-registry.md),
    [обзор для партнёров на английском](docs/overview.en.md);
  - решения [ADR-001–ADR-003](docs/adr/README.md): отдельный репозиторий и
    SSOT, форма методологии и структура L1–L4, лицензия и имя (предложено);
  - анализ: [экспертная команда](docs/analysis/2026-11-01-expert-team.md),
    [SSOT и источники](docs/analysis/2026-11-01-ssot-and-sources.md),
    [инвентаризация переноса](docs/analysis/2026-11-01-migration-inventory.md);
  - [исследовательская модель GRA](methodology/research-program/README.md)
    (уровень L3) и документы этапа I как исторический контекст;
  - [каталог курсов](education/README.md) и курс Технограда «Введение в
    репутационный инжиниринг» по дням (day-01–day-04);
  - инструменты `tools/import_from_hub.py` (воспроизводимый перенос) и
    `tools/validate_repo.py` (frontmatter, ссылки, имена) с тестами и CI.

### Changed

- Issue [#3](https://github.com/G-Ivan-A/aether-orbis-gra/issues/3): 167 ссылок
  на неперенесённые файлы домена Хаба закреплены на `48ebe52` вместо `main`
  (`tools/import_from_hub.py` закрепляет их сам); `last_sync` в
  `.hub-profile.json` указывает на `48ebe52`; объявлены каталоги `ops/` и
  `experiments/`.
