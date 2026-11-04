---
status: superseded
version: 0.2
updated: 2026-10-10
temperature: 0.1
type: external-analysis
scope: repo-wide
source: "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-06-20-framework-standard.en.md"
---

# GRA Framework Standard — Draft (International Format)

> **Исторический документ (этап I, июнь 2026). / Historical document (stage I, June 2026).**
> Текущие формулировки GRA — в документах L1–L4 ([docs/README.md](../README.md)); известные
> расхождения этого текста с ними перечислены в [docs/history.md](../history.md#известные-расхождения).
> Current GRA wording lives in the L1–L4 documents; known discrepancies are listed in docs/history.md.

> Draft standard for the **GRA reputation-technology framework**, structured to
> **ISO/IEC/IEEE 42010** (architecture description) and anchored to **ISO/IEC 42001** (AI
> management). This is a **research proposal for a standard**, not a ratified standard and not an
> implementation. It accompanies the main report
> [2026-06-20-founders-vision-and-framework.ru.md](2026-06-20-founders-vision-and-framework.ru.md) and the
> [white paper](2026-06-20-white-paper.en.md). Terminology is in the
> [glossary](2026-06-20-glossary.ru-en.md).
>
> **Revision 0.2 (issue #659).** Definitions of mass, distance and polarity and the
> grounding of the formula follow the [GRA research model](../../methodology/research-program/00-introduction.md).
> The rest of the draft is unchanged.

**GRA** — *Gravitational & Magnetic Reputation Architecture* (public slogan: *Global Reputation
Agreement*). Curator: Ivan Gulienko. License: CC BY-NC-SA 4.0.

## 0. Status of this document

This draft consolidates the founder's three-level naming (`0_2-standard.txt`) and the team-Q/team-G
dialogues into a single, internationally legible standard skeleton. It supersedes the fragmented
naming and the 2011 edition reference of the source material (see normative references). It is
offered for community review on the **de-facto-standard** track (see roadmap in the main report,
Part XI), not yet submitted to a formal standards body.

## 1. Scope

### 1.1 Purpose

This standard specifies how to **describe, instantiate, and validate** a reputation system as a
governed, measurable, manageable graph — the **information-reputation field** — across levels from
**individual** to **brand**, **company**, and **state**, and how **AI** is applied to model, manage,
predict, and automate within it.

### 1.2 Field of application

In scope: ontology, methodology (Gravity + Magnetism), data model, AI methodology, domain
adaptation, validation, governance/ethics. Out of scope: any specific commercial implementation,
proprietary scoring weights, or a ratified conformance-certification scheme (future work).

### 1.3 Conformance

A description **conforms** to this standard if it provides every normative element in §6
(Architecture Description Elements) and complies with the governance clauses in §8. Conformance is
**self-declared** at this draft stage; third-party conformance assessment is reserved for a future
edition.

## 2. Normative references

| Reference | Edition | Role |
| --- | --- | --- |
| ISO/IEC/IEEE 42010 | **2022** | Primary — architecture description (stakeholders, concerns, viewpoints, views). *Corrects the source's 2011 citation.* |
| ISO/IEC 42001 | **2023** | AI management system — governs every AI function in §7. *Key reference added vs. source.* |
| W3C RDF 1.1; OWL 2; SKOS; PROV-O | current | Ontology, controlled vocabulary, provenance |
| TOGAF Standard (ADM) | 10th | Iterative development & validation cycle (§9) |
| IMRaD | — | Structure of supporting scientific publications |
| GOST R 7.0.5 | 2008 | Bibliographic citation for Russian-language outputs |
| ISO 20671-1; ISO 10668 | 2021; 2010 | Brand evaluation (adjacent measurement) |
| ISO 31000; 37000; 26000; 30401; 22301 | current | Risk; governance; social responsibility; knowledge; continuity |
| GRI Standards; SASB/ISSB | current | Disclosure analogues for transparent methodology |
| EU AI Act (Reg. 2024/1689); OECD AI Principles; NIST AI RMF | current | AI governance, transparency, prohibited practices |

## 3. Terms and definitions

The normative vocabulary is maintained in the [glossary](2026-06-20-glossary.ru-en.md). Core terms:

- **Reputation** — the dynamic state of the information-reputation field; not a label but a graph
  configuration. «Reputation lives not in the customer's head, but in the links between customers.»
- **Information-reputation field** — a weighted, directed graph of nodes and edges that **contains
  and is hypothesised to lead the market** (lag 30–180 days; hypothesis HM-I, not yet tested).
- **Node (subject/object)** — an entity at any level (individual…state) with a **mass** and an
  **Identity–Capability–Impact** triad.
- **Edge (development edge)** — a relation with type, weight, **polarity** (+1/0/−1), distance, and
  trust-transfer risk.
- **Mass** — observable node characteristics (resource, position, network, reputation capital); for
  a group, the aggregate mass of the holding. Influence on a specific decision is recorded separately.
- **Distance** — multidimensional: physical/temporal, informational (channel), trust, values,
  institutional; at least the physical and informational axes. Axes are not merged into one number.
- **Polarity** — sign of an edge: +1 attraction, 0 neutral, −1 repulsion, ? unknown; time- and
  signal-dependent. Each edge also has a flow direction (A→B ≠ B→A).
- **Gravity / Magnetism** — external structural attraction (mass/distance²) / internal
  polarity-setting contour.
- **Trust Equity** — accumulated positive reputation capital.

## 4. Naming (normative)

The framework is named **GRA = Gravitational & Magnetic Reputation Architecture**. The public-facing
slogan **Global Reputation Agreement** MAY be used in marketing. The earlier methodological label
"Gravity–Resonance Architecture" and the scientific label "GRANIT" are **deprecated** in favour of
the single backronym to avoid brand fragmentation and to resolve the *Resonance vs. Magnetism*
inconsistency (Magnetism/polarity is the operational term). Rationale and trade-offs: main report §8.1.

## 5. Conceptual model (architecture rationale)

### 5.1 Axioms

1. Reputation is **measurable, modelable, manageable**.
2. Its substrate is **relations** (a graph), not individual minds.
3. The field **leads** the market; managing the field is a leading indicator of revenue.
4. AI is the **instrument** that makes modelling and management tractable.

### 5.2 Interaction model

$$ F(t) = \frac{Mass_A \times Mass_B}{Distance^2} \times Polarity(t) $$

The formula is working hypothesis H1, one of the competing relation models H0–H6. GRA originated as
the founder's authorial hypothesis of a structural correspondence with physical regularities
([origin, verbatim](../../methodology/research-program/10-theory.md#1-происхождение-gra)). The Gravity Model of Trade (Tinbergen, 1962) is a precedent and a possible
research environment, not a source; its distance exponent is estimated from data and is close to 1.
Elements of the model draw on Force Field Analysis (Lewin, 1947) and the ABI trust model
(Mayer–Davis–Schoorman, 1995). The "force field" is an **operational metaphor**
over graph mathematics and trust theory; its rigorous home is **sociophysics** (Castellano et al.,
2009) — this disclaimer is **normative** to prevent "aggregate-confusion" misuse.

### 5.3 Control contours

Internal contour (Magnetism, 80–100% control: identity, capabilities, processes, resources) /
External contour (Gravity, 0–50% influence: stakeholders/influence nodes, events, media, regulators)
/ Environment (macro-trends, 0% control).

## 6. Architecture description elements (normative checklist)

A conforming description SHALL provide:

1. **Passport** — name, version, status, curator, license, changelog.
2. **Stakeholders & concerns** — researchers, educators, practitioners, partners, regulators (ISO 42010 §5.3).
3. **Ontology** — RDF/SKOS vocabulary, taxonomy, semantic network, extension principles.
4. **Methodology viewpoint** — gravity/magnetism, contours, Identity–Capability–Impact triad, control cycles (Governance→Reputation→Action; PDCA + OODA).
5. **Data model viewpoint** — node schema, edge schema, serialization (Edge List / RDF / GraphML), data-quality requirements.
6. **AI methodology viewpoint** — model/manage/predict/automate functions mapped to NLP/CV/Predictive/Simulation/Agent-based, each governed per §8.
7. **Domain adaptation** — SME, corporation, government/GR, NGO, personal brand, education.
8. **Validation & evolution** — TOGAF-ADM cycle, pilots, metrics, versioning, risks.
9. **Governance & ethics** — §8.
10. **References** — normative + scientific + tooling.

## 7. AI methodology (normative requirements)

| Function | Required AI capability | Output |
| --- | --- | --- |
| Model | Entity/relation extraction (NLP), graph construction | RDF triples |
| Manage | Recommendation / agentic action on edges | Action proposals (24–48h rule) |
| Predict | Time-series, agent-based simulation | Cascade forecasts, field→market lead |
| Automate | RPA + LLM pipelines, no-code for SME | Monitoring → labeling → visualization → alerts |
| Perceive | Sentiment (polarity), computer vision | Edge polarity, visual signals |

Every AI function SHALL be operated under an AI management system conforming to **ISO/IEC 42001**
and SHALL comply with **EU AI Act** transparency and prohibited-practice provisions. Manipulative
or deceptive reputation interventions ("Black" class, §8.2) are **non-conforming**.

## 8. Governance and ethics (normative)

### 8.1 Methodological transparency

To avoid "aggregate confusion" (ESG-style rating divergence), any published reputation score SHALL
ship with an **open, reproducible, graph-auditable** methodology. Closed-weight scoring without
published methodology is **non-conforming**.

### 8.2 Ethical classification

| Class | Meaning | Conformance |
| --- | --- | --- |
| White | transparent strengthening of real reputation | conforming |
| Grey | presentation optimization without deception (SEO/GEO, timing) | conforming **with disclosure** |
| Black | manipulation, fabrication (fake reviews, astroturfing) | **non-conforming** (prohibited) |

### 8.3 Data protection

Cross-level graphs containing personal nodes SHALL undergo a **DPIA** and comply with applicable
law (GDPR / 152-FZ) before any public release.

## 9. Validation and evolution (TOGAF ADM)

MVP → Pilot (3–5 calibration pilots for mass/distance) → Scale (graph tooling, AI pipeline, GRA
Index v0) → Ecosystem (separate repository, international contributors, annual published ranking).
Each cycle feeds back to the axioms (§5.1). Versioning follows semantic `MAJOR.MINOR[.PATCH]`.

## 10. References

Normative references — §2. Scientific and project references are consolidated in the main report
[Sources](2026-06-20-founders-vision-and-framework.ru.md#источники). Source materials of issue
#260: the founder's framework,
standard, strategic-session, gravity-magnetism, and RDF documents, plus team-Q and team-G dialogues.

---

*Editorial note.* This draft updates two premises of the source `0_2-standard.txt`: (a) ISO/IEC/IEEE
42010 is cited at its **2022** edition (the source cited 2011); (b) **ISO/IEC 42001:2023** is added as
a normative AI-governance reference (absent in the source). Both changes are required for an
internationally credible 2026 standard.
