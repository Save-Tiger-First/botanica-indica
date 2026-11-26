# ODR-02 — STF / Botanica Indica Logical Domain Boundary

**Decision ID:** ODR-02  
**Decision type:** Owner Decision Record (not an Architecture Decision Record)  
**Status:** Owner-authorized — 26 November 2026  
**Decision authority:** Save Tiger First project owner  
**Project:** Save Tiger First / Botanica Indica  
**Repository:** Save-Tiger-First/botanica-indica  
**Recorded in:** PR #20 workstream, branch docs/full-system-architecture-and-repo-engineering-plan

## 1. Owner authorization

On 26 November 2026, the project owner instructed the adviser to proceed with the recommended STF / Botanica Indica logical ownership boundary following the explicit recommendation presented for confirmation.

This record captures that authorization narrowly. It does not claim that the owner approved every proposal in the architecture, blueprint, PRD, RTM or scientific model.

## 2. Decision

**STF owns genuinely reusable platform infrastructure. Botanica Indica owns botanical scientific semantics, domain records, workflows and scientific authority.**

### 2.1 STF shared-platform responsibilities

STF may provide reusable infrastructure where there is a demonstrated or justified cross-domain need, including:

- identity, authentication and authorization mechanisms, account and organization foundations;
- media upload, storage, processing and secure delivery infrastructure;
- common geographic primitives, coordinate/geometry handling, CRS conventions and spatial infrastructure;
- generic search infrastructure and reusable query/index lifecycle mechanisms;
- notification delivery infrastructure;
- platform security and audit-event foundations;
- observability, integration, API lifecycle, developer tooling, CI/CD, configuration and secrets-management foundations.

A shared capability must have a defined purpose, owner, consumers, contract, security model and sustainable operating expectations. Reuse is not justification to centralize domain logic or data.

### 2.2 Botanica Indica domain responsibilities

Botanica Indica owns, governs and interprets:

- botanical taxonomic names, concepts, treatments and source-specific reconciliation;
- taxon profiles, botanical knowledge, morphology and diagnostic characteristics;
- identification runs, candidate sets, evidence, confidence/uncertainty and determinations;
- botanical observations, events, surveys, occurrences and field workflows;
- botanical distribution assertions, habitat interpretation, biogeographic context and sensitive botanical locations;
- botanical source ingestion, curation, scientific validation and expert review;
- botanical domain permissions, scientific workflow rules and domain-specific data-quality decisions.

### 2.3 Boundary examples

- Shared coordinate handling does not own botanical distribution assertions.
- Shared search infrastructure does not own taxonomic matching or botanical candidate ranking.
- Shared media storage does not confer ownership or reuse rights over images or contributions.
- Shared identity mechanisms do not decide who is scientifically qualified to review a taxon.
- A common audit pipeline does not replace Botanica Indica's scientific determination and taxonomy history.

## 3. Explicit non-decisions

This decision does **not** determine:

- legal-entity, organizational, staffing or institutional ownership;
- a separate STF platform team, repository, database, deployment, cloud account or service;
- physical database boundaries, schemas, tables, migrations or API implementation;
- final technology, vendor, provider, hosting or procurement selections;
- ownership title or license terms for external datasets, photographs, user contributions or community-held knowledge;
- acceptance of Task 01–04, the full-product blueprint, RTM, Task 05C/05D/05E or any test plan;
- amendment or supersession of ADR-001 through ADR-010.

Logical ownership boundaries must not be converted automatically into separate microservices, repositories, databases or organizations. ADR-002 and the operating prompt's modular-monolith guardrail remain in force.

## 4. Consequences and required reconciliation

1. Task 01 §10, Task 03 §6.2 and Task 04's opening decision summary must be read with this decision and their source-preserving governance overlays.
2. The original Task 01–04 v0.1 source transcriptions remain preserved. This decision does not rewrite their original wording.
3. The Task 03 and Task 04 repository overlays must explicitly state the boundary interpretation and link to this record.
4. The proposed STF Ecosystem Boundaries document remains a proposed architecture baseline overall; this owner decision confirms the logical boundary only.
5. The RTM and capability crosswalks should use STF shared-platform classification only for actual reusable infrastructure. Botanical semantics and scientific authority remain Botanica Indica responsibilities.
6. Future changes to this boundary require an explicit owner decision and, where architecture consequences warrant it, a reviewed ADR or superseding ADR.

## 5. Relationship to ADR-011 and accepted ADRs

ODR-02 is an owner-authorized logical boundary decision. It is not ADR-011, does not accept ADR-011, and does not change any accepted ADR.

ADR-001 through ADR-010 remain unchanged. Any future ADR must be assessed against this owner decision and the operating prompt.

## 6. Verification status

The decision record and related overlays are documentation changes only. No PR was merged, no branch was deleted or created, no repository protection was changed, and no application code, schema or deployment was modified.

**Owner decision:** STF shared infrastructure; Botanica Indica botanical domain ownership.  
**Remaining status:** canonical PRD/architecture acceptance, organizational/deployment design and scientific-model approval remain separate open work.
