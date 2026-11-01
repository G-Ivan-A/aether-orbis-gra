---
status: draft
version: 0.1
updated: 2026-11-01
temperature: 0.1
---

# Contributing — aether-orbis-gra

`aether-orbis-gra` is a spoke repository of the
[hybrid-Intelligence-lab](https://github.com/G-Ivan-A/hybrid-Intelligence-lab)
Hub. It holds the GRA methodology, which is still in development, and the
educational course built on it. There is no production code here. The main
artifacts are documents: the L1–L4 documentation, decision records and the
course. The Hub's governance rules are inherited and not duplicated here. The
rules for AI agents are in [AGENTS.md](AGENTS.md).

## Workflow: issue → PR → review

1. **Issue.** State the context, the scope and a measurable Definition of Done.
   Say which level the change touches (L1 vision, L2 concept, L3 methodology,
   L4 roadmap, or the course), as described in [docs/README.md](docs/README.md).
2. **PR.** One goal per PR, a green CI and no unrelated restructuring. Link the
   PR to its issue with a closing keyword.
3. **Review.** Decisions on the vision, on publication to external partners and
   on merging stay with the author of the methodology (G-Ivan-A).

## Content rules

- **Be honest about status.** Every statement of the methodology is labelled
  according to [docs/methodology.md](docs/methodology.md#статусы-утверждений):
  fixed, author's hypothesis, conceptual model, requires operationalization,
  or not developed. Do not present a hypothesis as an established result.
- **Complement, don't oppose.** Industry reputation practices (RepTrak, AMEC,
  Barcelona Principles, ISO 20671) and network science are the foundation.
  GRA is a niche addition to them; see
  [docs/analysis/2026-11-01-methodology-form-and-industry-positioning.md](docs/analysis/2026-11-01-methodology-form-and-industry-positioning.md).
- **Cite sources.** Every claim about external practice gets a source from
  [docs/sources-registry.md](docs/sources-registry.md). An unresolved source is
  recorded as a gap, not as an assumption.
- **Respect the source of truth (SSOT).** The current version of a document
  lives in this repository. The Hub stays a source of practices and of global
  research. Do not duplicate Hub rules here; link to them with absolute URLs.

## File format

- Every Markdown file starts with frontmatter that has `status`, `version`,
  `updated` (YYYY-MM-DD) and `temperature`. `ai-generated` is forbidden.
- Chronological documents carry their date at the start of the name:
  - `docs/analysis/YYYY-MM-DD-name.md`
  - `docs/rfc/YYYY-MM-name.md`
  - `docs/adr/YYYY-MM-adr-NNN-name.md`

  ADRs use the governance statuses (`proposed`, `accepted`, …) and the
  `decision-type` field.
- Top-level directories outside the Hub's canonical set are declared in
  `.hub-profile.json` with a `reason`.

## Validation

```bash
./tools/validate-repository-structure.sh     # Hub HTOM genome: required files, AGENTS.md, directories
python3 tools/validate_repo.py               # frontmatter, naming, links, structure
python3 -m unittest discover -s tests -v     # validator tests and a check of the repository itself
```

CI ([.github/workflows/validate.yml](.github/workflows/validate.yml)) runs the same
commands on every push and pull request.

## Pull Request Checklist

- [ ] The PR is linked to an issue and changes one level (L1–L4) or the course.
- [ ] The status of every new claim is labelled; hypotheses are not presented as facts.
- [ ] External practices are cited from the source registry.
- [ ] CI is green: the validator and tests pass.
- [ ] A significant decision is recorded as an ADR in `docs/adr/`, and the change is added to the `CHANGELOG.md`.
