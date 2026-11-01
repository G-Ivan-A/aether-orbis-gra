---
status: draft
version: 0.1
updated: 2026-11-01
temperature: 0.1
---

# Changelog

Все заметные изменения репозитория записываются здесь. Формат —
[Keep a Changelog](https://keepachangelog.com/ru/1.1.0/).

## [Unreleased]

### Added

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
