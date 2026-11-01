---
status: superseded
version: 0.2
updated: 2026-10-10
temperature: 0.2
type: external-analysis
scope: repo-wide
source: "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/32b5fa524e542af23c1a8e67c919bd66d5f4e399/research/reputation-technologies/2026-06-20-white-paper.en.md"
---

# GRA — A Graph-Native, Cross-Level Standard for Reputation Engineering (White Paper)

> **Исторический документ (этап I, июнь 2026). / Historical document (stage I, June 2026).**
> Текущие формулировки GRA — в документах L1–L4 ([docs/README.md](../README.md)); известные
> расхождения этого текста с ними перечислены в [docs/history.md](../history.md#известные-расхождения).
> Current GRA wording lives in the L1–L4 documents; known discrepancies are listed in docs/history.md.

> International-audience white paper for the **GRA reputation-technology framework**. Companion to the
> Russian research report [2026-06-20-founders-vision-and-framework.ru.md](2026-06-20-founders-vision-and-framework.ru.md)
> and the draft [standard](2026-06-20-framework-standard.en.md). Terms: [glossary](2026-06-20-glossary.ru-en.md).

**Author/Curator:** Ivan Gulienko · **License:** CC BY-NC-SA 4.0 · **Status:** draft for community review.

> **Revision 0.2 (issue #659).** The origin of GRA now follows the founder's verbatim
> wording. The Gravity Model of Trade and Force Field Analysis are named as precedents, not as the
> foundation of the formula. Mass is a set of observable node characteristics, distance is
> multidimensional, and polarity carries both sign and flow direction. The rest of the text is unchanged.

## Abstract

Reputation is usually treated either as a **survey score** (perception indices) or as an
**operational dashboard** (online-reputation management). Neither treats it as what it structurally
is: a **measurable, manageable graph** of relations that spans levels from the individual to the
nation-state and that **leads** market outcomes. **GRA — Gravitational & Magnetic Reputation
Architecture** — formalizes reputation as the **information-reputation field**, a weighted directed
graph in which the force of any relation is `F = (Mass_A × Mass_B) / Distance² × Polarity`. A review
of fifteen leading international projects shows an unoccupied **white space**: no incumbent is
simultaneously **prescriptive**, **graph-native**, **cross-level**, and an **open standard**. This
paper presents the model, the evidence, and a standardization and ecosystem roadmap.

## 1. The problem

Organizations and individuals manage reputation with fragmented tools: listening platforms tell them
*what is being said*, indices tell them *how they rank*, and SEO/entity tools tell them *what
machines believe*. None of these tells them, in one model, **why** reputation moves, **which
relations** drive it, and **what to do next** — across levels and in an auditable, portable way.
Three structural gaps recur:

1. **Perception vs. structure.** Survey indices (RepTrak, Edelman, Anholt-Ipsos NBI) measure
   *perception* but do not expose the *relational structure* that produces it.
2. **Description vs. prescription.** Listening suites describe sentiment; they rarely prescribe a
   causal, testable intervention on a specific relationship.
3. **Silos vs. cross-level continuity.** A person, a brand, a company, and a state are scored by
   different vendors with incompatible methods — yet reputation propagates *across* these levels.

## 2. The founder's insight, formalized

The founder's vision — cleaned of its educational-course wrapping — rests on three axioms: reputation
is **measurable, modelable, manageable**; its substrate is **relations** («reputation lives not in
the customer's head, but in the links between customers»); and **AI** is the instrument that makes
modelling and management tractable. GRA turns these into an operational model.

### 2.1 The field

The **information-reputation field** is a weighted directed graph `G = (V, E)`. Nodes `V` are
subjects/objects at any level; edges `E` are **development edges** carrying type, weight, distance,
trust-transfer risk, and a **polarity** sign. The field **contains** the market. Hypothesis HM-I (not yet tested): the field **leads** the market by
roughly **30–180 days**; if confirmed, reputation would be a *leading indicator* of revenue
(`Reputation → Trust → ↓CAC → ↑LTV → Profit`). This chain is a hypothesis, not a promise of business effect.

### 2.2 The force law (an operational metaphor)

```
F(t) = ( Mass_A × Mass_B ) / Distance(t)²  ×  Polarity(t)
```

The formula is working hypothesis H1, one of several competing relation models (H0–H6, see the
[GRA research model taxonomy](../../methodology/research-program/20-taxonomy.md#5-конкурирующие-модели-связи-h0h6)). The square of distance is not calibrated.

- **Mass** — observable node characteristics: resource (revenue, budget), position (share, formal
  status), network, reputation capital; for a group of companies, the aggregate mass of the holding.
  Components may diverge and are not merged into one number. Influence on a specific decision is
  recorded separately.
- **Distance** — multidimensional: physical and temporal, informational (channel), trust, values,
  institutional. At least two axes (physical and informational) are always used. Trust is one axis,
  not the definition of distance.
- **Polarity ∈ {+1, 0, −1, ?}** — attraction / neutral / repulsion / unknown; time-dependent (events
  flip signs) and signal-dependent. Every relation also has a flow direction: A→B is not B→A
  (hypothesis HP-D).

**Origin.** In the founder's words (Russian original, translation ours): "GRA originated solely as the founder's authorial hypothesis that social and informational relations may be described structurally, by analogy with physical regularities. Any mathematical or economic models (including gravity models) are treated only as one of the possible practical environments for researching or implementing this hypothesis, with no status of a primary source or a special reference point"
([original](../../methodology/research-program/10-theory.md#1-происхождение-gra)). Accordingly, the **Gravity Model of Trade** (Tinbergen, 1962) is a precedent and a
possible research environment, not the source of the formula: Tinbergen estimated exponents from
data, and the empirical distance exponent in trade is closer to 1 than to 2. **Force Field Analysis**
(Lewin, 1947), with Lewin's caveat that the absolute strength of social forces cannot be determined,
supports the language of forces, and the **ABI trust model** (Mayer–Davis–Schoorman, 1995) supports
edge signs. We state plainly:
the "force field" is a **metaphor** over graph mathematics; its rigorous scientific home is
**sociophysics** (Castellano, Fortunato & Loreto, 2009). This honesty is a feature — it is what keeps
a published score auditable rather than mystical.

### 2.3 Contours and the node triad

Management splits into an **internal contour** (Magnetism — identity, capabilities, processes,
resources; 80–100% controllable), an **external contour** (Gravity — stakeholders, events, media,
regulators; 0–50% influenceable), and the **environment** (macro-trends; uncontrollable). Every node
carries an **Identity–Capability–Impact** triad — a cross-level "passport" with analogues at Stanford
GSB, the US Army's *Be-Know-Do*, and INSEAD's *Character-Competence-Contribution*.

## 3. Evidence from the field: fifteen projects, one white space

We reviewed fifteen leading projects across eight categories: ORM/RXM platforms (Reputation, Birdeye,
Yext), social/media intelligence (Brandwatch, Meltwater, Talkwalker, Sprinklr), perception indices
(RepTrak, Edelman Trust Barometer, Harris-Fombrun RQ), AI/entity reputation (Kalicube, Google
Knowledge Graph + E-E-A-T), ESG (MSCI), web3 reputation (Gitcoin/Human Passport), and nation branding
(Anholt-Ipsos NBI). Mapped on two axes — *descriptive↔prescriptive* and *survey↔graph* — they cluster
into recognizable quadrants but leave one cell empty.

**The white space:** no incumbent is at once **prescriptive/engineering**, **graph-native**,
**cross-level (individual→nation)**, and an **open standard**. The closest fragments each miss one
dimension: Kalicube is prescriptive and graph-based but proprietary and brand-level; OpenRank/web3 is
open and graph-native but limited to individuals; RepTrak/Edelman/Anholt own legitimacy but are
survey-based and descriptive. That empty cell is GRA's position.

Two lessons transfer directly. First, the **strongest go-to-market in the category is the "annual
published ranking" flywheel** — Edelman at Davos, the Global RepTrak 100, the NBI — which manufactures
earned media on a schedule, makes the publisher the category's "scorekeeper", and turns ranked
entities into a sales funnel. Second, the **deepest risk is "aggregate confusion"** — ESG ratings
correlate only 0.38–0.71 across providers; any opaque score inherits that critique. GRA's answer is
an **open, reproducible, graph-auditable** methodology.

## 4. The GRA framework

GRA is layered: **philosophy/axioms → ontology (RDF/SKOS) → methodology (gravity/magnetism) → data
model (Edge List / RDF / GraphML) → tooling + AI → domain adaptation → validation (TOGAF ADM)**.
The data model meets users where they are: an **Edge List in a spreadsheet** is the recommended SME
entry point, while **RDF triples (Subject-Predicate-Object)** provide the interoperable, AI-ready
backbone. A business is modeled as a **sub-graph** (legal entity ← owner → employees) with a
cross-role trust-transfer coefficient `α ∈ [0,1]` and explicit **Key-Man-Risk** detection.

AI spans four functions — **model** (extract a graph from text), **manage** (recommend/act on edges),
**predict** (simulate cascades; lead the market), **automate** (no-code pipelines) — each operated
under an **ISO/IEC 42001** AI-management system and **EU AI Act** transparency rules. Interventions
are ethically classified **White / Grey / Black**; the Black class (fabrication, astroturfing) is
prohibited.

## 5. Standardization

GRA is structured to **ISO/IEC/IEEE 42010:2022** (architecture description) and anchored to
**ISO/IEC 42001:2023** (AI management) — the latter being the key reference absent from the founder's
source documents. The recommended path to recognition is **de-facto first** (in the manner of
Schema.org, OpenAPI, NIST CSF, and FAIR): publish an open v1.0 standard plus glossary, build a
contributor community and an annual index, then approach a formal body (ISO PAS or a W3C Community
Group). The trade-off is explicit: de-facto is faster and community-building but lacks an ISO seal;
the formal route confers legitimacy but costs years and committee membership.

## 6. Go-to-market: own the standard and the index

The most defensible commercial position in this category is to **own a standard or an index**, not to
sell another dashboard. GRA should therefore (a) publish the open standard as marketing-grade IP,
(b) launch an **annual, cross-level GRA Index** to become the "scorekeeper" of a space no incumbent
covers end-to-end, and (c) monetize through **advisory and certification** layered on the open core.
Thought-leadership and academic legitimacy compound the flywheel; the principal risk to manage is
**Key-Man-Risk** around a single founder-evangelist (the Kalicube pattern).

## 7. Ecosystem and repository

GRA should live in a **separate repository** — the `reputation-engineering` spoke already reserved in
the Hub ecosystem research — inheriting the Hub's governance (frontmatter standard, validators,
research profile, AI-governance baseline) via the spoke template, and implementing the
EvidenceObject / ReputationClaim / ScoringPolicy / ReputationScore / AppealRecord object model
sketched there. Public-facing publication (the annual index, the standard) can surface through the
ecosystem's public portal. This keeps the framework's implementation **out of the Hub** (per the
issue's constraint) while binding it into the ecosystem's shared governance.

## 8. Roadmap

**Framework (TOGAF ADM):** MVP (ontology + force law + Edge List + one SME case) → Pilot (3–5
calibration pilots) → Scale (graph tooling, AI pipeline, GRA Index v0) → Ecosystem (separate repo,
international contributors, annual ranking). **Standardization:** open v1.0 (0–6 mo) → GRA Index v1
and earned media (6–12 mo) → contributor community + RFC process + IMRaD publications (12–24 mo) →
ISO/IEC PAS or W3C CG submission aligned with 42001/42010 (24–36 mo).

## 9. Conclusion

GRA reframes reputation from a score you *receive* to a field you *engineer* — measurable, auditable,
and continuous from the individual to the state. The international landscape confirms the opportunity:
the prescriptive, graph-native, cross-level, open-standard cell is empty. By owning an open standard
and an annual index, and by binding AI under credible governance, GRA can become the **de-facto
standard for reputation engineering**.

## References

Consolidated in the main report's [Sources](2026-06-20-founders-vision-and-framework.ru.md#источники)
section (issue #260 source materials, scientific foundations, the fifteen projects, and standards).
Key anchors: Tinbergen 1962 (precedent, not a source of GRA); Lewin 1947; Mayer-Davis-Schoorman 1995; Barabási-Albert 1999; Coombs
2007; Castellano-Fortunato-Loreto 2009; ISO/IEC/IEEE 42010:2022; ISO/IEC 42001:2023; W3C RDF 1.1;
EU AI Act (Reg. 2024/1689).
