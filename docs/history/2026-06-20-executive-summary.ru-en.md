---
status: superseded
version: 0.2
updated: 2026-10-10
temperature: 0.2
type: external-analysis
scope: repo-wide
source: "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-06-20-executive-summary.ru-en.md"
---

# Executive Summary — GRA Reputation Framework (RU + EN)

> **Исторический документ (этап I, июнь 2026). / Historical document (stage I, June 2026).**
> Текущие формулировки GRA — в документах L1–L4 ([docs/README.md](../README.md)); известные
> расхождения этого текста с ними перечислены в [docs/history.md](../history.md#известные-расхождения).
> Current GRA wording lives in the L1–L4 documents; known discrepancies are listed in docs/history.md.

> Two-to-three-page summary for decision-makers, in Russian and English. Full analysis:
> [main report](2026-06-20-founders-vision-and-framework.ru.md) ·
> [standard](2026-06-20-framework-standard.en.md) · [white paper](2026-06-20-white-paper.en.md).
>
> **Правка версии 0.2 / Revision 0.2 (issue #659).** Определения модели приведены к
> [исследовательской модели GRA](../../methodology/research-program/00-introduction.md);
> опережение рынка и цепочка до прибыли помечены как гипотезы. Model definitions follow the GRA
> research model; the market lead and the profit chain are marked as hypotheses.

---

## RU — Сводка для руководителей

### Суть

**Репутация — это измеримая, моделируемая и управляемая система связей**, а не абстрактный «образ в
голове клиента». Видение фаундера (Иван Гулиенко), очищенное от образовательной обёртки,
формализуется как фреймворк **GRA — Gravitational & Magnetic Reputation Architecture** (публичный
слоган — *Global Reputation Agreement*).

### Модель

Репутация описывается как **информационно-репутационное поле** — взвешенный направленный граф, где
сила связи **F = (Масса_A × Масса_B) / Дистанция² × Полярность** — рабочая гипотеза H1, одна из
нескольких моделей связи. Масса — наблюдаемые характеристики узла (ресурс, позиция, сеть,
репутационный капитал); Дистанция многомерна (физическая, информационная, доверие, ценности,
институциональная); Полярность ∈ {+1, 0, −1, ?} и направление потока. Гипотеза HM-I: поле
**опережает рынок на 30–180 дней**; если она подтвердится, репутация станет опережающим индикатором
выручки (Репутация → Доверие → ↓CAC → ↑LTV → Прибыль). Это не обещание эффекта. Модель работает **на всех уровнях**: индивид → бренд → компания → государство.

### Что показывает рынок (15 проектов)

Анализ 15 международных проектов (Reputation, Birdeye, Yext, Brandwatch, Meltwater, Talkwalker,
Sprinklr, RepTrak, Edelman, Harris-Fombrun RQ, Kalicube, Google KG/E-E-A-T, MSCI ESG, Gitcoin/Human
Passport, Anholt-Ipsos NBI) выявил **«белое пятно»**: ни один игрок не является одновременно
**предписывающим, графовым, кросс-уровневым и открытым стандартом**. Это и есть позиция GRA. Самая
сильная модель продвижения — **ежегодный публикуемый рейтинг** (маховик заработанных медиа). Главный
риск — **«aggregate confusion»** (расхождение оценок, как в ESG); ответ — **открытая, прозрачная,
аудируемая методология**.

### Рекомендации

1. Принять ядро видения базой фреймворка; консолидировать наименование в единый бэкроним **GRA**.
2. Базировать стандарт на **ISO/IEC/IEEE 42010:2022** и добавить **ISO/IEC 42001:2023** (управление ИИ).
3. Формализовать онтологию в **W3C RDF 1.1 + SKOS**; для МСП — вход через **Edge List**.
4. Перенять маховик **«ежегодный рейтинг» (GRA Index)**; монетизация — стандарт + индекс + advisory.
5. Создать **отдельный репозиторий** `reputation-engineering` в экосистеме Hub (не в этом репозитории).
6. Двигаться путём **«de-facto стандарт → ISO»** (как Schema.org/OpenAPI/FAIR).
7. Этика: классификация **White/Grey/Black** + соответствие **EU AI Act**; «чёрные» методы запрещены.

### Роль ИИ

ИИ выполняет четыре функции: **моделирование** (граф из текста, NLP), **управление** (агенты,
рекомендации по связям), **прогнозирование** (симуляция каскадов, опережение рынка), **автоматизация**
(no-code для МСП). Все функции — под управлением **ISO/IEC 42001** и **EU AI Act**.

---

## EN — Executive Summary

### Essence

**Reputation is a measurable, modelable, manageable system of relations** — not an abstract "image in
the customer's head". The founder's vision (Ivan Gulienko), cleaned of its educational-course
wrapping, is formalized as the **GRA — Gravitational & Magnetic Reputation Architecture** framework
(public slogan: *Global Reputation Agreement*).

### The model

Reputation is modeled as the **information-reputation field** — a weighted directed graph in which the
force of a relation is **F = (Mass_A × Mass_B) / Distance² × Polarity** — working hypothesis H1, one
of several relation models. Mass is a set of observable node characteristics (resource, position,
network, reputation capital); Distance is multidimensional (physical, informational, trust, values,
institutional); Polarity ∈ {+1, 0, −1, ?} plus flow direction. Hypothesis HM-I: the field **leads
the market by 30–180 days**; if confirmed, reputation would become a leading revenue indicator
(Reputation → Trust → ↓CAC → ↑LTV → Profit). This is not a promise of effect. The model holds **across all levels**: individual → brand → company →
state.

### What the market shows (15 projects)

A review of fifteen international projects revealed an unoccupied **white space**: no incumbent is at
once **prescriptive, graph-native, cross-level, and an open standard** — exactly GRA's position. The
strongest go-to-market is the **annual published ranking** (an earned-media flywheel). The deepest
risk is **"aggregate confusion"** (rating divergence, as in ESG); the answer is an **open,
transparent, auditable methodology**.

### Recommendations

1. Adopt the vision core as the framework base; consolidate naming into the single backronym **GRA**.
2. Base the standard on **ISO/IEC/IEEE 42010:2022**; add **ISO/IEC 42001:2023** (AI management).
3. Formalize the ontology in **W3C RDF 1.1 + SKOS**; SME entry via an **Edge List**.
4. Adopt the **annual-ranking (GRA Index)** flywheel; monetize via standard + index + advisory.
5. Create a **separate `reputation-engineering` repository** in the Hub ecosystem (not in this repo).
6. Pursue a **de-facto-standard → ISO** path (like Schema.org/OpenAPI/FAIR).
7. Ethics: **White/Grey/Black** classification + **EU AI Act** compliance; "Black" methods prohibited.

### The role of AI

AI performs four functions: **model** (graph-from-text, NLP), **manage** (agents, edge
recommendations), **predict** (cascade simulation, market lead), **automate** (no-code for SMEs). All
functions run under an **ISO/IEC 42001** management system and **EU AI Act** rules.

---

*Source materials and full evidence: issue #260
and the companion documents linked above.*
