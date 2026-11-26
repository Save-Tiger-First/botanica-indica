# Botanica Indica — Full-Product Optimization and Delivery Plan

**Document ID:** STF-BI-OPT-001  
**Version:** 0.1 — Proposed portfolio and delivery optimization  
**Prepared:** 26 November 2026  
**Status:** Proposed for project-owner and discipline review; not an approved product, architecture, scientific-model or implementation baseline  
**Decision authority:** Save Tiger First project owner  
**Repository:** `Save-Tiger-First/botanica-indica`  
**Working branch:** `docs/full-system-architecture-and-repo-engineering-plan` (existing PR #20 branch)  
**Scope:** Optimize project execution, repository structure, decision flow and verification for the complete Botanica Indica product

---

## 1. Purpose and non-negotiable scope

Botanica Indica is a **full-fledged, full-product India-first botanical intelligence platform—not an MVP**. This plan optimizes the way the complete product is defined, governed, built, validated and operated. It does not reduce the product vision or remove capability domains. Delivery may be dependency-led and incremental; increments are steps toward the full platform, not a smaller replacement target.

The full product includes botanical taxonomy and knowledge, evidence-aware identification, observation and survey workflows, geographic/ecological intelligence, source ingestion and interoperability, community participation, expert/scientific review, public web and research access, mobile field workflows, administration, APIs, AI/ML operations, analytics, security, rights/privacy governance and long-term operations.

The project owner's ODR-02 boundary applies: **STF owns genuinely reusable platform infrastructure; Botanica Indica owns botanical scientific semantics, domain records, workflows and scientific authority.** Logical boundaries do not require separate repositories, teams, databases, deployments or microservices.

This proposal does not accept existing draft PRs, amend ADR-001–ADR-010, approve ADR-011, decide an unresolved scientific model, authorize a physical schema, or claim implementation readiness.

## 2. Current baseline and optimization diagnosis

The repository has substantial product, architecture and scientific documentation, but the inspected main branch has no application source code. Important product and engineering proposals are distributed across open workstreams, the scientific data model has unresolved blocking questions, proposed test cases have not been executed, and the repository branch count exceeds its governance ceiling.

The project is therefore **documentation- and decision-flow constrained**, not yet ready for runtime micro-optimization. The highest-return optimization is to reduce ambiguity, competing sources of truth, validation latency and rework before code and schema decisions become expensive.

### Optimize these, in order

1. **Scientific correctness and rights safety:** settle domain meanings, provenance, source permissions and sensitive-location rules before freezing payloads or schemas.
2. **Decision throughput:** establish one traceable decision/review path and explicit owners for each gate; avoid repeated parallel proposals that do not converge.
3. **Requirements-to-evidence traceability:** connect the entire product's needs to capabilities, design, implementation, executable tests and operational evidence.
4. **Repository and integration safety:** preserve source history while reducing divergent, overlapping, stale workstreams; do not merge on the basis of filenames or GitHub mergeability alone.
5. **Engineering delivery efficiency:** once the gates permit implementation, use cohesive modules, automated contracts, reproducible builds and selective service extraction.
6. **Runtime performance and cost:** instrument real workloads and optimize measured bottlenecks after a functioning end-to-end system exists.

## 3. Full-product capability portfolio

Keep the existing proposed `BI-CAP-01`–`BI-CAP-16` capability map as the full-product portfolio pending owner acceptance. It is not a service, release, repository or staffing decomposition.

| Portfolio area | Capability domains |
|---|---|
| Botanical knowledge and science | BI-CAP-01 botanical knowledge/taxonomic intelligence; BI-CAP-03 species knowledge profiles; BI-CAP-06 evidence, expert review and scientific governance |
| Identification and field evidence | BI-CAP-02 identification/Evidence Engine; BI-CAP-04 observations, field documentation and surveys; BI-CAP-05 geography and ecology |
| Data and discovery | BI-CAP-07 acquisition, ingestion and interoperability; BI-CAP-08 search, learning and discovery |
| People and user experiences | BI-CAP-09 community stewardship; BI-CAP-10 mobile; BI-CAP-11 public web and research; BI-CAP-12 expert/scientific console; BI-CAP-13 administration/data stewardship |
| Interfaces and intelligence operations | BI-CAP-14 APIs/institutional integration; BI-CAP-15 AI/ML research, evaluation and operations; BI-CAP-16 analytics, observability and operational intelligence |

Every capability remains in the target product even when a particular increment does not yet deliver it. Cross-cutting capabilities—identity/access, security, rights, privacy, accessibility, localization, audit, reliability, support and operations—must be mapped across the portfolio rather than treated as optional finishing work.

## 4. Proposed delivery architecture

### 4.1 Domain and deployment strategy

Use the accepted modular-architecture principles: define domain ownership, contracts and dependency rules first; use a domain-oriented modular monolith as the default initial deployment shape unless the approved requirements demonstrate otherwise. Extract a separately deployed service only when evidence shows that independent scaling, ownership, security, resilience or deployment cadence outweighs distributed-systems cost.

- **Botanica domain modules:** taxonomy; botanical knowledge; identification; evidence; observation/survey; geography/ecology interpretation; media domain metadata; source registry/ingestion; rights/purpose decisions; expert review; community contributions; search/discovery behavior.
- **Reusable STF platform mechanisms:** identity/access foundations; media storage and secure delivery; generic geographic primitives; search infrastructure; notification delivery; audit/observability foundations; integration/developer tooling.
- **Clients:** Flutter mobile remains governed by ADR-001; web, expert and administration experiences are full product clients with server-enforced authorization.
- **Contracts:** versioned API contracts and internal module interfaces; do not expose ORM/database tables as product contracts.
- **Data:** PostgreSQL/PostGIS remain candidates for the authoritative relational/spatial platform. Physical schema is blocked until scientific-model gates pass. Search, caches, embeddings and analytics are derived and rebuildable, with provenance and rights controls.
- **AI/ML:** Python scientific/model workflows remain replaceable and separately evaluated; models produce attributable inference, not direct writes to authoritative taxonomy or expert determinations.

### 4.2 Full-product quality attributes

Create a traceable requirements and verification plan for the whole platform, including scientific integrity, data provenance, rights, sensitive-location protection, privacy, accessibility, multilingual discovery, offline reliability, API compatibility, security, observability, backup/recovery, supportability and cost. Define numeric targets only after workload, field research, threat models, evaluation protocols and accountable review establish defensible values.

### 4.3 No premature infrastructure

Do not create a microservice per capability, multiple databases, vector store, Kubernetes platform, multi-region design or speculative Rust components by default. Evaluate each against a measured end-to-end requirement, total cost, operational ownership, portability, security and failure-recovery evidence. This is a way to deliver the complete product sustainably, not a limitation on its eventual capabilities.

## 5. Dependency-led delivery sequence for the full system

These are governance and technical dependency gates, not MVP phases. Work may proceed in parallel where dependencies allow, but an increment cannot bypass a safety or scientific blocker.

| Gate | Full-product work | Exit evidence required |
|---|---|---|
| A — Canonical foundation | Reconcile Tasks 01–04, full-product blueprint, requirements, capability IDs, owner decisions and source provenance | Owner-reviewed coherent foundation; source records preserved; conflicts and proposal status explicit |
| B — Scientific and data semantics | Reconcile Task 05C candidates and Task 05D; resolve Event/Survey/Occurrence, survey outcomes, IdentificationSubject integrity, taxonomy/treatments, provenance and DR/LDM/EVT/FLD findings | One reviewable logical model; qualified scientific/data review; reproducible positive and negative validation; exact standards/version evidence |
| C — Rights, privacy, conservation and security | Define rights by asset and purpose, community authority/consent, sensitive-location tiers, privacy lifecycle, threat model and abuse controls | Approved policies, data-flow inventory, control ownership and testable enforcement requirements |
| D — Integrated product and architecture baselines | Approve complete requirements/capability traceability, workflow lifecycles, API/offline contracts, module boundaries and technology decision status | Consistent product/architecture package linked to accepted ADRs; open choices explicitly assigned and justified |
| E — Engineering and data foundations | Build toolchains, repository layout, CI, API/schema validation, identity integration, audit, media pipeline, migration strategy and test environments | Reproducible builds; contract/architecture/security checks; reviewed data migration and recovery approach |
| F — Full capability implementation | Deliver connected vertical slices across the complete portfolio, beginning with high-dependency shared/domain foundations and continuing through every capability | Each slice links requirements → design → code → tests → evidence; deferred work remains visible in full-product traceability |
| G — Integrated assurance | Validate cross-client journeys, science, AI/ML, data ingestion, rights, security, privacy, accessibility, performance, resilience and operations | Recorded acceptance evidence, specialist dispositions, unresolved risk decisions and rollback/recovery proof |
| H — Production and stewardship | Operate, monitor, support, update taxonomy/data/models, handle corrections and maintain scientific/rights governance | Accountable operating model, service objectives, incident and change processes, cost visibility and continuous review |

A prototype, synthetic fixture, pilot or initial user release is a validation/delivery instrument within this full-system path. It must not be used to relabel the product as MVP-only or to make unsupported scientific, market or conservation-impact claims.

## 6. Requirements, decisions and test optimization

### 6.1 One traceability chain

For each original Task 03 requirement, proposed derived requirement and approved capability, maintain links to:

1. source and version;
2. owner and user/scientific need;
3. capability and workflow;
4. domain/module and API/data contract;
5. relevant accepted ADR, owner decision and open decision;
6. rights, privacy, security and accessibility controls;
7. test oracle, fixture provenance/licensing and test level;
8. execution result, build/commit, reviewer and evidence;
9. release/operational owner and monitoring or correction path.

Preserve original Task 03 identifiers and distinguish proposed derived IDs. Do not equate document presence, a written test case, a mergeable PR or an inferred Graphify relationship with acceptance or verification.

### 6.2 Turn proposals into decisions efficiently

For every open item, record one accountable decision owner, required specialist roles, evidence needed, dependencies, current proposal(s), decision date/status and downstream documents/tests affected. Batch related decisions into focused reviews: domain/data semantics; rights/privacy/conservation; API/mobile reliability; product acceptance; operational architecture. Capture accepted decisions once and propagate them through traceability; preserve rejected alternatives with rationale rather than reopening them silently.

### 6.3 Validation portfolio

Keep test suites distinct but cross-linked:
- full-product acceptance criteria AC-001–AC-012;
- workflow scenarios WF-*;
- offline scenarios OFF-*;
- API synchronization scenarios API-SYNC-*;
- scientific/data validation LDM/DR/EVT/FLD;
- security, privacy, rights, accessibility, performance, resilience and operations.

All current proposed cases remain not run until actual evidence is recorded. Expand coverage for AC-011 and AC-012 and close partial coverage for AC-006, AC-008, AC-009 and AC-010 as identified in the integration review. Maintain the ODR-01 external-export-only boundary; internal missing records remain unknown/not assessed.

## 7. Repository optimization and collaboration model

### 7.1 Preserve first, consolidate second

The current 23-branch count exceeds the seven-branch ceiling. The no-new-branches instruction remains in force. Do not delete, close or retarget PRs solely to reduce the count. Inventory every branch's unique commits, changed files, dependent PRs, source provenance and review status; compare content semantically; preserve unique science/decision records; then use only already-approved destinations and required authorization for lifecycle actions.

PR #17–#23 are not one linear stack. In particular, preserve and reconcile Task 05C/05D alternatives and the main-only Hortus crosswalk. Individual GitHub mergeability is not a branch-to-branch integration test. Do not claim integration until actual content, history and validation have been checked.

### 7.2 One navigable source of truth

- Keep `README.md` as the entry point; link product, architecture, ADR, scientific review, project-management, test and decision indexes from it when the owner approves the documentation integration.
- Use `docs/product/`, `docs/architecture/`, `docs/adr/`, `docs/reviews/`, `docs/decisions/` and `docs/project-management/` by document role, not by temporary task branch.
- Preserve source transcriptions and dated overlays separately from accepted baselines.
- Use a maintained document/source inventory with status and canonical ref; avoid copying competing full documents into multiple folders.
- Prefer small, single-purpose review changes after the current reconciliation rather than append-only status fragments scattered across unrelated files.
- Keep generated analysis artifacts, restricted datasets, credentials, personal information and sensitive biodiversity locations out of Git and external model processing unless expressly authorized.

### 7.3 CI and engineering checks

Introduce checks when corresponding artifacts exist; do not create empty workflows that imply validation. Progressively automate Markdown/link checks, OpenAPI/schema validation, document inventory consistency, code formatting/lint/type checks, unit/contract/integration tests, dependency/security scans, architecture boundaries, migration validation and reproducible builds. Scientific tests require reviewed fixtures, explicit expected outcomes and qualified scientific interpretation; CI cannot certify scientific truth by itself.

## 8. Measures of progress and optimization

Track evidence rather than activity counts. At project-control reviews, report:

- percentage of the complete requirement/capability portfolio with an owner, acceptance criteria, design contract and verification path;
- unresolved blocking scientific/data decisions and their evidence/review state;
- rights/privacy/sensitive-location controls with tested end-to-end coverage;
- proposed versus accepted decisions, duplicate/conflicting documents and stale source references;
- executable test coverage and actual pass/fail/block status by test portfolio;
- integration-ready branches/PRs, unique content preserved and branch-ceiling deviation;
- build reproducibility, escaped defects, migration/recovery evidence and support readiness once code exists;
- measured field-network, API, search, inference, storage and cost performance after representative workloads exist.

Do not invent numeric targets before baselines, workloads, denominators, risk tolerance and accountable owners are agreed. Do not use species count, PR count, lines of code, number of documents or a single AI accuracy score as a proxy for product quality or conservation impact.

## 9. Immediate recommended actions

1. **Keep the full-product scope intact** and use this plan as a proposed optimization overlay, not a replacement for the Blueprint, PRD, RTM, accepted ADRs or scientific review register.
2. **Reconcile the current integration package**: refresh live PR/source SHAs; resolve stale statements in the roadmap and connected audits; preserve branch/PR history and competing scientific work.
3. **Resolve the Task 05 scientific blockers** through the existing review workstream; do not start Task 05E or physical DDL until evidence and qualified review satisfy the existing gate.
4. **Close product baseline traceability** across all 16 proposed capabilities, 19 original Task 03 functional IDs, 12 acceptance criteria, 7 non-goals and cross-cutting policies; fill known acceptance-test gaps.
5. **Review API/offline/security/rights policies together** so command, receipt, scientific lifecycle, media rights and sensitive-location semantics remain consistent.
6. **Approve a full-system architecture and repository source-of-truth index** only after owner and discipline review; introduce engineering tooling and code structure when the implementation baseline is accepted.
7. **Begin runtime performance and cost optimization only against measured end-to-end workloads**, while delivering the complete product through dependency-aware increments.

## 10. Decision and verification boundary

This document is a proposal. It does not claim that any existing PR, requirements baseline, architecture, scientific model, test plan, technology provider or production process is approved. No Task 05 model finding is closed here. No numeric service objective, scientific accuracy threshold, budget or deadline is invented. No implementation, test run, independent specialist sign-off or legal opinion is claimed.

The source set inspected for this proposal includes the current PR #20 full-system architecture plan and roadmap, PR #17–#23 integration-readiness review, current repository README, accepted ADR-001–ADR-010, ODR-02, the proposed PRD/Blueprint/RTM, offline/API specifications and scientific validation records. Their proposals and source revisions remain governed by their respective workstreams and must be re-fetched before a formal approval decision.

---

## 11. Recommended next-step choices

Choose one focused next step; none implies reducing full-product scope:

- **A — Scientific model and validation reconciliation (recommended):** resolve the blocking Task 05C/05D semantics, preserve alternative work, and make DR/LDM/EVT evidence executable. Keep Task 05E blocked until the review gate passes.
- **B — Full-product baseline traceability:** reconcile Task 01–04, Blueprint, RTM, AC coverage and workflow decisions into one reviewable full-product baseline package.
- **C — Repository and PR integration audit:** refresh the live branch/PR inventory, correct stale status/source references, and prepare a preservation-first consolidation plan using only existing approved branches.
- **D — Full architecture and engineering foundation review:** review module boundaries, API/offline contracts, repository tree, CI/security/operations and open technology choices against the accepted ADRs and full capability map.

**Recommendation:** start with **A**, because unresolved scientific semantics constrain data contracts, API payloads, acceptance tests and eventual physical design. Continue B and C in parallel where they do not assume unresolved model decisions. Keep the full product target intact throughout.
