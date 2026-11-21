# Botanica Indica — Full System Architecture and Repository Engineering Plan

**Document ID:** STF-BI-ARCH-PLAN-001  
**Version:** 0.1 — Proposed target architecture and engineering plan  
**Prepared:** 20 November 2026  
**Status:** Proposed for project-owner review; not an accepted architecture baseline or implementation authorization  
**Decision authority:** Save Tiger First project owner  
**Repository:** `Save-Tiger-First/botanica-indica`  
**Scope:** Full Botanica Indica product and its logical relationship to STF shared capabilities  
**Governing decisions:** Accepted ADR-001 through ADR-010  
**Related proposals:** Full Product Vision and Capability Blueprint (PR #17), Task 03/04 source-preserving baselines (PR #18), Requirements Traceability Register (PR #19), Task 05 scientific model and review proposals

---

## 1. Executive recommendation

Adopt a **domain-oriented modular monolith with API-first contracts, one authoritative relational/spatial data platform, independently replaceable AI/ML capabilities, and separate client applications** as the target starting architecture.

The architecture must be comprehensive enough to support the full intended product: botanical knowledge and taxonomy, evidence-aware identification, observations and surveys, geographic intelligence, source ingestion, expert and community workflows, public discovery, research access, administration, APIs, analytics and operations.

This is a full-product architecture. It is not a reduced feature set or a launch-only design. Delivery can be phased, but the long-term capability map remains intact.

### 1.1 Recommended architectural shape

- **Mobile:** Dart / Flutter, governed by accepted ADR-001.
- **Web:** TypeScript web application; React/Next.js remains a candidate pending explicit evaluation and decision.
- **Backend:** TypeScript API application organized as strongly bounded domain modules; deploy as a modular monolith initially.
- **Scientific and AI/ML computing:** Python packages and controlled workers, isolated behind stable internal contracts. Separate deployment only when workload, security or operational evidence justifies it.
- **System of record:** PostgreSQL with PostGIS as the leading candidate, consistent with the existing project direction. Physical schema design remains blocked by scientific-model gates.
- **Media:** object storage behind a media abstraction, with asset-level metadata, provenance, rights and access policy in the authoritative database.
- **Search:** begin with database-backed and derived search capabilities; adopt a dedicated search engine only after workload and relevance evaluation.
- **API contracts:** versioned JSON/HTTP APIs described with OpenAPI; asynchronous job/event contracts only where they solve a defined need.
- **Operations:** automated CI, test gates, observability, backups, recovery, security controls and governed deployment environments.

### 1.2 The most important architecture rule

**Logical modules are not automatically separate microservices.** A module boundary defines ownership, contracts and allowed dependencies. It does not require its own process, database, repository, cloud account or deployment.

This follows accepted ADR-002 and avoids turning a scientifically complex product into a prematurely distributed system.

## 2. What was inspected and current baseline

### 2.1 Repository and governance

Repository: `Save-Tiger-First/botanica-indica`  
Default branch: `main`  
Main commit inspected: `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`  
Main commit SHA: `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`  
Root Git tree SHA: `cc15676cd415057ed927af22fba57dc147ea1e8f`

The complete `docs/governance/AI-PROJECT-OPERATING-PROMPT.md` was fetched from `docs/repository-audit-and-ai-operating-standard`; blob SHA:

`65cb5ac58c79f2bf14a1e7df1d9b18ea608850ed`

It is followed as the working operating standard until PR #16 is accepted and merged.

At the inspection point:
- `main`, `develop` and `staging` were identical at the SHA above.
- At the time of the initial architecture-plan snapshot, the repository had 22 branches (3 designated long-lived and 19 topic branches) and 16 open PRs; this snapshot preceded the creation/opening of PR #20.
- A fresh verification after PR #20 opened reports 23 branches (3 designated long-lived and 20 topic branches) and 17 open PRs. All 17 are currently open; no PR has been merged in the current inventory.
- `main`, `develop` and `staging` remain identical at `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`.
- PRs #17, #18 and #19 remain proposals, not approved baselines.
- The default-branch tree contained 18 entries and **no application source-code files**. The repository is currently documentation/governance-led; no application implementation was verified.
- No branch was deleted, no PR merged, and no repository protection or setting changed during this work.

The branch count is not itself a violation: only three branches are designated long-lived. The growing topic-branch inventory does, however, need a dependency and preservation register before any cleanup.

### 2.2 Exact project documents inspected

| Document | Ref | Blob SHA | Status |
|---|---|---|---|
| AI Project Operating Prompt | `docs/repository-audit-and-ai-operating-standard` | `65cb5ac58c79f2bf14a1e7df1d9b18ea608850ed` | Proposed standard; user instruction requires adherence |
| README | `main` | `366e856fdf28a26a4799c9f3ae7341d3d8ae1c2f` | Current repository overview |
| Task 03 PRD v0.1 | `docs/canonical-task-03-04-baselines` | `8b1ca0be04b3f4ad3b543c2f9fc48d46eb37faf8` | Complete extracted source transcription; working baseline |
| Task 04 architecture evaluation v0.1 | `docs/canonical-task-03-04-baselines` | `abc7b721fae8d4f4adede4dd0bf5d6a32098c5a3` | Complete extracted source transcription plus governance overlay; working baseline |
| Full Product Vision and Capability Blueprint v0.1 | `docs/full-product-vision-capability-blueprint` | `ccfeb15d86bc832e61590028d57c08c4ce4fbbed` | Proposed in PR #17 |
| Requirements Traceability Register v0.1 | `docs/requirements-traceability-register` | `1e65218f2b63aad9ea1f078d71594de53999990f` | Proposed in PR #19 |
| Scientific Data Model Review Pack | `review/scientific-data-model-review-pack` | `f8ce8caab31d02a38e2f3deb957b67af77decad6` | Review proposal; not scientific sign-off |

Accepted ADR-001 through ADR-010 were also fetched from `main`; all ten report Accepted. This plan does not amend them.

### 2.3 Consistency audit — findings

**Finding A — full-product scope is aligned.** Task 03 explicitly describes a full-platform requirements document. The proposed Blueprint covers 16 capability domains. The RTM maps the 19 original Task 03 functional IDs, proposed cross-cutting requirements and acceptance criteria. The architecture plan therefore preserves the comprehensive product scope.

**Finding B — mobile framework conflict is resolved by existing governance, not by preference.** Task 04's historical source table recommends React Native as a candidate. Accepted ADR-001 establishes Dart/Flutter. The Task 04 repository overlay and Blueprint already recognize this conflict. Flutter governs unless the owner explicitly approves an ADR amendment or superseding ADR. This plan does not reopen the decision.

**Finding C — service decomposition requires careful interpretation.** Task 04 uses “domain-oriented services” and describes independently deployable AI/ML components. Accepted ADR-002 prefers a modular monolith initially and requires evidence before service extraction. The reconciled interpretation is domain modules first; deployment separation only where justified.

**Finding D — candidate technologies are not approved vendor choices.** React/Next.js, OpenSearch, S3-compatible object storage, OIDC-compatible identity, containers and any cloud provider remain candidates unless separately accepted. PostgreSQL/PostGIS is the leading system-of-record direction, but physical schema and production topology are not authorized by this plan.

**Finding E — STF shared-platform ownership remains partly open.** The README and Blueprint describe shared STF capabilities, but proposed ADR-011 / PR #2 has not been accepted. Keep logical boundaries visible, but do not assume separate repositories, teams, deployments or ownership arrangements before that decision.

**Finding F — scientific data architecture is a hard gate.** DR-01–DR-04 are blocking findings; DR-05–DR-07 and the remaining DR/LDM scenarios also require resolution and validation. Task 05E / physical database design is not ready. This plan describes architectural responsibilities and repository organization, not tables or production migrations.

**Finding G — no codebase exists on main yet.** The current main tree has no TypeScript, Dart, Python, SQL or application build files. The directory structure below is a target proposal, not a description of existing implementation.

**Finding H — document status must remain explicit.** PR #17, #18 and #19 are open proposals. Their contents may inform this plan, but they do not constitute accepted product, architecture or scientific baselines.

## 3. Architecture principles and module boundaries

### 3.1 Governing principles

1. Respect accepted ADR-001 through ADR-010.
2. Use a modular monolith as the initial deployment shape, with domain-oriented modules and explicit contracts.
3. Keep domain logic out of controllers, UI widgets, ORM models and infrastructure adapters.
4. Keep the system of record authoritative; search indexes, embeddings, caches, analytics projections and AI outputs are derived.
5. Treat taxonomy, identifications, evidence, observations, occurrences, media, rights and geography as separate scientific concepts.
6. Make all external-source integration rights-aware, versioned and provenance-preserving.
7. Enforce sensitive-location and personal-data policy at every access path.
8. Keep clients replaceable and API-first.
9. Prefer one primary relational/spatial database until measured requirements justify additional stores.
10. Extract independently deployed services only when measurable operational or organizational needs justify the additional distributed-systems burden.

### 3.2 Proposed logical module catalogue

These are logical modules, not a commitment to separate services.

| Module | Responsibility | Owns / governs | Must not absorb |
|---|---|---|---|
| Identity and Access | Authentication integration, authorization policy, roles and sessions | Identity references, access policies | Botanical permissions or scientific determinations |
| Taxonomy | Names, concepts, treatments, usages and reconciliation | Taxonomic records and source-scoped mappings | Observation or AI inference lifecycle |
| Botanical Knowledge | Taxon profiles, traits, morphology, habitat and curated knowledge | Profile composition and sourced knowledge assertions | Unqualified static “truth” |
| Identification | Identification sessions, runs, candidate orchestration and outcomes | Versioned identification assertions and pipeline coordination | Expert determinations or taxon master data |
| Evidence | Evidence records, evidence relationships, quality and review context | Evidence provenance and claim links | Raw AI scores as scientific certainty |
| Observation and Survey | Observations, events, surveys, effort, occurrences and field workflow | Field records and their lifecycle | Taxonomic concept governance |
| Geography | Places, boundaries, spatial operations, uncertainty and disclosure rules | Geographic reference and policy services | Unqualified public exposure of coordinates |
| Media | MediaAsset lifecycle, storage abstraction, derivatives and metadata | Media identity, lineage and technical processing | Automatic reuse permission |
| Rights and Consent | Asset/purpose permissions, consent, restrictions and withdrawal records | Rights decisions and policy evaluations | Assumption that public access equals permission |
| Source Registry and Ingestion | Source catalogue, dataset versions, adapters, validation and ingestion runs | Source lineage and ingestion state | Silent source authority ranking |
| Expert Review | Review queues, reviewer roles, determinations and disputes | Attributable review history | Overwriting previous determinations |
| Community and Contributions | Contributions, attribution, moderation and community safeguards | Contribution lifecycle and consent context | Treating submissions as verified science |
| Search and Discovery | Search API, indexing, relevance and discovery projections | Rebuildable search indexes | Authoritative taxonomy or scientific facts |
| Notifications | User and workflow notifications | Delivery preferences and delivery records | Unconsented marketing |
| Audit and Governance | Security/audit events, administrative actions and decision trace | Audit history | Unrestricted personal or sensitive content in logs |
| Analytics and Operations | Service health, product metrics, cost and quality indicators | Aggregated operational views | Secondary disclosure of sensitive observations |

Module boundaries should be refined using actual workflows, data ownership and dependency tests. Do not create one module per screen or one microservice per capability label.

### 3.3 Dependency direction

Recommended dependency direction:

```
Clients (Flutter / Web / Admin / Research)
                  |
            Versioned API
                  |
        Application / Use Cases
                  |
       Domain Modules and Policies
                  |
      Ports / Repository Interfaces
                  |
     Infrastructure Adapters / SQL
                  |
       PostgreSQL + PostGIS / Object
       Storage / External Providers
```

- Domain modules own their invariants and write operations.
- Other modules use documented application interfaces or read projections; they do not write directly into another module's tables.
- Infrastructure depends inward on domain/application contracts, not the reverse.
- UI clients never connect directly to the database.
- AI/ML adapters return attributable candidate/evidence outputs; they do not directly mutate accepted taxonomic records.
- Cross-module workflows should use explicit application orchestration. Use transactional outbox/async messaging only where durable decoupling is required; do not adopt event sourcing by default.

## 4. Full target architecture

### 4.1 Client layer

**Flutter mobile application**
- Public identification and botanical learning.
- Camera/gallery and guided evidence capture.
- Observation and survey workflows.
- Offline drafts and safe synchronization.
- Accessible, localized experience.
- Secure local storage and permission-aware location/media access.

**Web application**
- Public discovery, botanical profiles, search and maps.
- Identification entry points where browser capability permits.
- Contributor workflows and personal collections.
- Research and institutional data access, subject to authorization.

**Expert and administration interfaces**
- Initially these may be separate route areas or applications within a coherent web codebase.
- Keep role boundaries, authorization and audit independent of frontend navigation.
- Split into separately deployed web applications only if access/security or team ownership warrants it.

### 4.2 API and application layer

One API codebase initially, with:
- Authentication and authorization middleware.
- Versioned REST/JSON endpoints and OpenAPI contract.
- Request validation, pagination, idempotency where needed and consistent errors.
- Application use cases and domain orchestration.
- Rights, consent and sensitive-location policy enforcement before returning data.
- Background-job submission and status endpoints.
- Rate limiting, quotas, audit and request correlation.

Do not expose ORM entities or internal database table shapes as public API contracts.

### 4.3 Scientific and data layer

**Authoritative data**
- PostgreSQL is the leading relational system-of-record candidate.
- PostGIS supports geographic objects and spatial operations.
- Use explicit identifiers, constraints, foreign keys, uniqueness rules, temporal/provenance fields and transactions.
- Domain ownership should be reflected in schema ownership and controlled write paths.
- Database migrations must be reviewed, reversible where feasible and tested against representative data.

**Media and files**
- Store binary media in object storage; store metadata, provenance, rights and storage references in the database.
- Keep original assets, derivatives and thumbnails distinguishable.
- Enforce access and purpose checks before retrieval, transformation, publication or AI processing.
- Retain raw source payloads only when rights and retention rules permit.

**Derived stores**
- Search indexes, embeddings, caches, map tiles, analytics aggregates and model outputs must be rebuildable from authorized source records or retained manifests.
- Every derived pipeline must retain version, source lineage and rights eligibility.
- A derived index must not become the only record of a scientific assertion.

### 4.4 AI/ML and scientific computing

Separate two concerns:

1. **Model research/training:** dataset manifests, label provenance, rights screening, taxonomic version context, train/validation/test separation, reproducibility, evaluation and model registry.
2. **Inference/runtime:** image-quality assessment, candidate generation, feature/context extraction, geographic context, taxonomy resolution, evidence aggregation, calibrated score handling and abstention.

The API orchestrates identification and records a versioned IdentificationRun. Python components are called through internal contracts or job interfaces. Do not let a model write directly to TaxonConcept, expert determination or authoritative profile tables.

Training, evaluation and inference may share packages but must have distinct permissions, data access, reproducibility and release gates. A dedicated GPU inference service is conditional on measured workload, latency and operating-cost evidence.

### 4.5 Background processing

Use background jobs for tasks that are slow, retryable or resource-intensive:
- image processing and derivative generation;
- AI inference;
- bulk source ingestion and validation;
- search-index rebuilds;
- notifications;
- exports and reports;
- analytics aggregation.

Use idempotency keys, retry limits, dead-letter handling, job status, correlation IDs and audit records. Separate worker processes may use the same modular-monolith codebase and database; a separate microservice is not required merely because a task is asynchronous.

### 4.6 Search and discovery

Begin with PostgreSQL capabilities and a well-defined search abstraction. Benchmark exact scientific names, synonyms, vernacular names, spelling variants, transliteration, faceted filters, spatial filters and relevance.

A dedicated search engine (for example, OpenSearch) is a candidate, not a decision. Adopt it only when measured requirements show a material advantage. Maintain a rebuildable index pipeline, source version tracking and access/rights filters. Do not put sensitive coordinates or restricted content into an index that cannot enforce the same policy.

### 4.7 STF shared platform boundary

Keep the codebase logically prepared for shared STF capabilities, but do not create separate infrastructure or repositories prematurely.

Potential shared concerns:
- identity and access primitives;
- media infrastructure;
- geographic primitives;
- notifications;
- audit and observability;
- integration and developer tooling.

Botanica-specific concerns remain:
- botanical taxonomy and source treatment;
- identification and botanical evidence;
- observations, occurrences and surveys;
- taxon profiles and distribution assertions;
- botanical expert governance.

Until proposed ADR-011 is accepted, treat this as a logical boundary, not a settled ownership or deployment decision.

## 5. Proposed GitHub repository structure

The following is a target structure for this repository. It is intentionally modular and explicit, but folders should be introduced when the corresponding implementation exists. Do not create dozens of empty placeholder packages.

```text
botanica-indica/
├── .github/
│   ├── CODEOWNERS
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE/
│   └── workflows/
│       ├── ci.yml
│       ├── security.yml
│       ├── docs.yml
│       └── release.yml
│
├── apps/
│   ├── api/
│   │   ├── src/
│   │   │   ├── bootstrap/
│   │   │   ├── config/
│   │   │   ├── modules/
│   │   │   │   ├── taxonomy/
│   │   │   │   ├── botanical-knowledge/
│   │   │   │   ├── identification/
│   │   │   │   ├── evidence/
│   │   │   │   ├── observations/
│   │   │   │   ├── geography/
│   │   │   │   ├── media/
│   │   │   │   ├── rights/
│   │   │   │   ├── ingestion/
│   │   │   │   ├── expert-review/
│   │   │   │   ├── community/
│   │   │   │   ├── search/
│   │   │   │   ├── notifications/
│   │   │   │   └── audit/
│   │   │   ├── platform/
│   │   │   └── main.ts
│   │   └── tests/
│   │
│   ├── web/
│   │   ├── src/
│   │   │   ├── app/
│   │   │   ├── features/
│   │   │   ├── components/
│   │   │   ├── api/
│   │   │   ├── accessibility/
│   │   │   └── localization/
│   │   └── tests/
│   │
│   └── mobile_flutter/
│       ├── lib/
│       │   ├── app/
│       │   ├── core/
│       │   └── features/
│       │       ├── identification/
│       │       ├── botanical_knowledge/
│       │       ├── observations/
│       │       ├── maps/
│       │       ├── search/
│       │       ├── profile/
│       │       └── settings/
│       ├── test/
│       └── integration_test/
│
├── ml/
│   ├── pyproject.toml
│   ├── src/
│   │   └── botanica_ml/
│   │       ├── image_quality/
│   │       ├── candidate_generation/
│   │       ├── evaluation/
│   │       ├── datasets/
│   │       ├── pipelines/
│   │       └── inference/
│   ├── tests/
│   └── model_cards/
│
├── packages/
│   ├── api-contracts/
│   │   ├── openapi/
│   │   ├── schemas/
│   │   └── examples/
│   ├── generated-clients/
│   └── shared-typescript/
│
├── database/
│   ├── migrations/
│   ├── reference-data/
│   ├── test-fixtures/
│   └── validation/
│
├── data-governance/
│   ├── source-registry/
│   ├── dataset-manifests/
│   ├── rights/
│   └── data-quality/
│
├── tests/
│   ├── contract/
│   ├── integration/
│   ├── end-to-end/
│   ├── architecture/
│   ├── security/
│   ├── scientific/
│   └── performance/
│
├── infra/
│   ├── containers/
│   ├── environments/
│   ├── deployment/
│   ├── monitoring/
│   └── backup-recovery/
│
├── docs/
│   ├── adr/
│   ├── architecture/
│   ├── api/
│   ├── product/
│   ├── science/
│   ├── security/
│   ├── privacy-rights/
│   ├── operations/
│   ├── testing/
│   └── governance/
│
├── scripts/
├── CONTRIBUTING.md
├── README.md
└── LICENSE
```

### 5.1 Directory rules

- `apps/` contains deployable client/API entry points, not shared business logic.
- `apps/api/src/modules/` contains domain modules with explicit boundaries.
- `packages/` contains code/contracts genuinely shared across applications. Do not create a generic shared-kernel dumping ground.
- `ml/` contains Python scientific/AI code and its independent packaging/test configuration.
- `database/` contains reviewed schema migrations and controlled reference/test data; not arbitrary SQL scripts.
- `data-governance/` contains manifests and rights/quality metadata, not unauthorized copies of source datasets.
- `tests/` contains cross-module and system-level tests; unit tests remain close to their modules.
- `infra/` contains infrastructure as code and deployment configuration. Secrets are never committed.
- `docs/` remains the authoritative location for architecture, science, policy and operational documentation.
- Do not split into multiple Git repositories until independent release cadence, ownership, security boundary or access control makes that necessary.

## 6. Internal code organization patterns

### 6.1 TypeScript API module pattern

Each domain module should use only the layers it needs:

```text
modules/taxonomy/
├── domain/
│   ├── entities/
│   ├── value-objects/
│   ├── policies/
│   └── errors/
├── application/
│   ├── commands/
│   ├── queries/
│   ├── services/
│   └── ports/
├── adapters/
│   ├── inbound/
│   │   └── http/
│   └── outbound/
│       ├── persistence/
│       └── external-sources/
├── contracts/
└── tests/
```

Rules:
- Domain layer contains scientific/business invariants and has no dependency on HTTP, ORM or cloud SDKs.
- Application layer coordinates use cases and defines ports.
- Inbound adapters validate transport and map requests/responses.
- Outbound adapters implement persistence and external provider interfaces.
- Contracts expose only what other modules/clients are allowed to depend on.
- Keep repositories module-owned. Do not allow cross-module direct writes.
- Avoid speculative generic frameworks and abstractions without two or more real use cases.

### 6.2 Flutter feature pattern

Use the Flutter team's current separation-of-concerns guidance: UI and data layers, views/view-models, repositories and services; add use-cases/domain orchestration where complexity warrants it.

```text
features/identification/
├── presentation/
│   ├── views/
│   ├── view_models/
│   └── widgets/
├── domain/
│   ├── models/
│   └── use_cases/
├── data/
│   ├── repositories/
│   ├── services/
│   └── dto/
└── test/
```

Prefer immutable state models, unidirectional data flow, abstract repositories and testable view models. Do not force every small feature to have empty layers or unnecessary use-case classes.

### 6.3 Web application pattern

Organize around product features and user journeys, not a giant global components folder. Keep:
- route/page composition thin;
- business logic in feature/application hooks or services;
- API access behind typed clients;
- authorization enforced by the backend;
- accessible design-system primitives in shared UI;
- localization and scientific-name rendering tested independently.

### 6.4 Python AI/ML package pattern

Use a `src/` package layout with a `pyproject.toml`, reproducible dependencies, typed interfaces and tests. Separate:
- data manifests and dataset validation;
- preprocessing;
- training and experiment code;
- evaluation and calibration;
- inference runtime;
- model packaging and deployment metadata.

Do not commit restricted training images or model weights unless rights, size, provenance and repository policy permit. Use authorized storage and manifests for large artifacts.

## 7. Code file size and maintainability standard

### 7.1 Recommended 200-line guideline

Adopt **200 non-blank physical source lines per hand-maintained code file as the normal target**.

This is a maintainability guideline, not a hard architectural law, compiler limit or quality guarantee.

| File size | Recommended treatment |
|---|---|
| 1–150 non-blank lines | Preferred range for focused source files |
| 151–200 | Normal target; no special explanation needed |
| 201–250 | Acceptable exception where the file remains cohesive; add a short rationale in the PR |
| 251–300 | Review whether responsibilities can be separated without harming cohesion; record why it remains one file if retained |
| Above 300 | Exceptional; obtain explicit reviewer agreement and record the structural reason, unless it is a generated or machine-maintained artifact |

**Count rule:** count non-blank physical lines in hand-maintained source files, including comments and docstrings. Do not count blank lines. The purpose is to expose responsibility growth, not to reward compressed formatting.

### 7.2 Files that may legitimately exceed 200 lines

A larger file may be justified when splitting it would weaken correctness, readability or structural integrity. Examples:
- generated code or generated API clients;
- machine-generated schema snapshots and lockfiles;
- a cohesive declarative OpenAPI/schema document where references would make the contract harder to review;
- an atomic database migration or data transformation whose steps must be reviewed together;
- a mathematically or scientifically cohesive algorithm with tightly coupled invariants;
- a platform-specific integration that must remain in one compilation unit;
- test fixtures or golden files where fragmentation would make the fixture less understandable.

Generated files should be marked as generated and never hand-edited. Large test data should generally live in fixture files rather than be embedded in source.

### 7.3 When a file exceeds the target

Before splitting, ask:
1. Does the file contain more than one responsibility?
2. Can the parts be named and tested independently?
3. Would splitting create circular imports or a misleading abstraction?
4. Are invariants or transactions required to remain together?
5. Is the file large because of repetitive generated/declarative content rather than complexity?

Split by responsibility, not by arbitrary line ranges. Never split one coherent algorithm, transaction or scientific rule merely to meet a numeric target.

### 7.4 Function and class size

Use additional complexity guidance:
- Prefer functions/methods under approximately 40 lines where practical.
- Functions beyond 40–50 lines trigger a review question, not an automatic failure.
- Avoid deep nesting; extract named predicates or steps where it clarifies the domain logic.
- Classes should have one coherent reason to change.
- Prefer explicit types and meaningful names over comments that restate the code.
- Comments should explain scientific rationale, invariants, safety constraints or non-obvious trade-offs.

Google's TypeScript style guidance similarly recommends small focused methods and suggests reconsidering methods around 40 lines; it does not impose a universal hard method-length limit.

### 7.5 Line width is a separate concern

Do not confuse file length with the width of an individual line. Use language formatters and lint rules. A reasonable starting convention is 100–120 characters where supported, with exceptions for URLs, generated strings, schemas and unavoidable literals. Language-specific formatters take precedence.

### 7.6 Enforcement

- Add a non-blocking CI report for source files above 200 lines.
- Require a short PR explanation for hand-maintained files above 200.
- Require reviewer agreement for files above 300, unless a documented exception applies.
- Maintain an exception register only for recurring or material exceptions; do not create bureaucracy for one-off small deviations.
- Do not fail builds solely because a cohesive file is 201 lines.
- Review the policy after real code and contributor experience exist.

**Recommendation:** 200 lines is a sensible default for this project. Cohesion, correctness, testability and clarity outrank the number.

## 8. API and contract strategy

- Treat API contracts as first-class artifacts, versioned and reviewed before clients depend on them.
- Use OpenAPI as the machine-readable HTTP interface contract; pin a specific supported version and toolchain rather than automatically adopting every latest feature.
- The OpenAPI Initiative lists 3.2.1 (10 September 2026) as current at the research check. Confirm generator and validator support before selecting it for implementation.
- Define stable identifiers, pagination, filtering, error shape, authentication scopes, rate limits, idempotency and deprecation policy.
- Distinguish source facts, AI inference, expert determinations, confidence semantics and uncertainty in the API schema.
- Represent withheld or generalized sensitive location explicitly without leaking original coordinates.
- Generate typed clients where reliable; generated output is not hand-maintained source.
- Test compatibility and schema validation in CI.

Do not expose database table names, internal ORM objects or provider-specific model payloads as permanent public contracts.

## 9. Database and scientific data safeguards

This plan does not authorize physical database design.

When the scientific-model gate is closed, the implementation design should:
- use PostgreSQL constraints and transactions to enforce integrity;
- use PostGIS geometry/geography only after defining coordinate reference, precision, uncertainty and calculation requirements;
- use spatial indexes based on measured query patterns;
- preserve source-specific taxonomy, provenance, rights and temporal context;
- keep observation, event, survey, occurrence, organism, material entity, identification, evidence and media distinct;
- enforce sensitive-location policy across read paths and derived systems;
- make migrations reviewable, tested, sequenced and backed by recovery procedures.

Do not assume all location data should use one spatial type or SRID. Geometry and geography have different computational semantics and performance characteristics. Choose by documented use case and spatial reference requirements.

### 9.1 Scientific readiness gate before physical schema

Physical schema work may proceed only after:
1. DR-01–DR-04 have a documented disposition and required validation.
2. DR-05–DR-07 have been reconciled with scientific semantics and workflow tests.
3. DR-08–DR-12 have documented source/standards dispositions.
4. LDM-01–LDM-16 are executed or formally dispositioned with evidence.
5. Qualified taxonomic/biodiversity-informatics review is recorded.
6. Rights and retention rules are mapped to the affected data and media.
7. Sensitive-location threat and disclosure policies are reviewed.
8. The project owner approves the logical model baseline.

A diagram, PR, proposed field or written test case is not evidence that the model has passed.

## 10. Security, privacy and rights architecture

Security and rights controls must be cross-cutting and enforceable in code.

### 10.1 Minimum architecture controls

- Centralized identity integration; authorization checked on the server for every protected operation.
- Least privilege, role/scope separation and administrative action audit.
- Secure secrets management; no credentials in source, logs or test fixtures.
- Encryption in transit and appropriate encryption at rest.
- Input validation, output encoding, secure file upload and malware/content validation as appropriate.
- Rate limits, abuse detection and resource quotas.
- Dependency, secret, static-analysis and container scanning.
- Backup encryption, restoration tests and access controls.
- Data minimization and retention/deletion/restriction policy.
- Threat models for sensitive workflows and high-risk assets.

### 10.2 Scientific and biodiversity-specific controls

- Exact rare/sensitive plant locations must not be exposed through public APIs, search, tiles, exports, logs or media metadata by default.
- Store precise and generalized representations separately or derive generalized views under explicit policy; never overwrite the precise scientific record with a public approximation.
- Record policy version and authorization for access to restricted coordinates.
- Rights must be evaluated per asset and purpose: storage, display, transformation, redistribution, commercial use, AI training, fine-tuning and embeddings.
- Unknown rights mean restricted/quarantined/excluded for the relevant use, not assumed permission.
- Community-held knowledge requires authority, meaningful consent, purpose limitation, access control, attribution preferences, benefit-sharing consideration, grievance and withdrawal processes.

### 10.3 Security verification references

Use OWASP ASVS 5.0.0 as a baseline for web/API verification and OWASP MASVS with its testing guidance for the Flutter mobile application. Select the applicable controls through threat modelling and risk assessment; do not claim certification merely because a checklist is present.

## 11. Testing and quality architecture

Testing must cover ordinary software correctness and scientific integrity.

| Test layer | Purpose | Required examples |
|---|---|---|
| Unit | Local deterministic logic | Taxonomy relation rules, rights policy, uncertainty mapping |
| Module integration | Internal adapters and persistence | Repository behavior, transactions, authorization |
| Contract | API and inter-module compatibility | OpenAPI validation, generated client compatibility |
| Architecture | Dependency and boundary enforcement | No UI-to-DB dependency, no cross-module writes |
| Scientific model | Domain invariants and scenarios | LDM-01–LDM-16, DR closure tests |
| AI/ML evaluation | Model behavior and failure analysis | Calibration, abstention, taxon/geography subgroup coverage |
| Security | Abuse and access controls | Negative authorization, sensitive-location leakage, upload safety |
| Privacy/rights | Purpose and disclosure enforcement | Dataset/media rights mismatch, withdrawal/restriction |
| Accessibility | Inclusive interaction | Screen readers, keyboard, contrast, scalable text |
| End-to-end | Complete user journeys | Identify → evidence → observation → review |
| Performance/resilience | Measured system behavior | Field-network upload, ingestion load, spatial search, recovery |

Tests must be reproducible and linked to the requirement, model version, fixture provenance and acceptance decision. A passing unit test does not prove botanical correctness.

## 12. CI/CD and GitHub engineering controls

### 12.1 Pull request checks

For each code PR, progressively introduce:
1. Formatting and lint checks.
2. Type checks and static analysis.
3. Unit tests.
4. Module and architecture dependency checks.
5. API/schema validation.
6. Scientific data-model invariant tests where relevant.
7. Security and dependency checks.
8. Build/package checks.
9. Integration and end-to-end tests for affected journeys.
10. Documentation and migration checks.

The exact CI matrix should reflect actual languages and packages after the repository begins implementation. Do not create empty workflows that pretend to test code which does not exist.

### 12.2 Branch workflow

Continue the approved lifecycle:
- temporary task branch → PR to `develop`;
- reviewed promotion `develop` → `staging`;
- acceptance checks;
- reviewed promotion `staging` → `main`.

Only `main`, `develop` and `staging` are long-lived during development. Topic branches are retired only after dependency, unique-content and owner-authorization checks. At formal completion, preserve all accepted work and then leave only `main`, with explicit owner approval.

### 12.3 Commit and PR discipline

- One coherent purpose per PR.
- Include tests for changed behavior.
- Keep generated files identifiable.
- Include migration and rollback implications.
- Include rights/privacy/scientific impact when affected.
- Use review checklists for code size, module boundaries and provenance.
- Do not merge or close PRs without explicit authorization.

## 13. Observability, deployment and operations

### 13.1 Observability

Use vendor-neutral telemetry interfaces where practical:
- structured logs with correlation IDs;
- service metrics and SLOs;
- distributed traces for API and asynchronous workflows;
- audit events separated from ordinary debug logs;
- AI/model version and evaluation telemetry;
- ingestion source freshness and failure metrics;
- storage, inference and provider cost metrics.

Never put secrets, raw personal data or precise sensitive species locations into ordinary logs or unrestricted telemetry.

### 13.2 Deployment shape

Start with the smallest operational topology that supports required controls:
- API application;
- web client;
- Flutter mobile release pipeline;
- PostgreSQL/PostGIS;
- object storage;
- background worker process;
- Python AI/ML runtime where required;
- monitoring, backups and secrets management.

A worker process or model runtime may be deployed separately without turning every domain module into a microservice.

Do not commit to Kubernetes, multi-region active-active, service mesh, multiple databases, dedicated vector database or a large event platform without a documented requirement and operational capacity.

### 13.3 Reliability and recovery

Before production, define:
- capability-specific service-level objectives;
- recovery time and recovery point objectives;
- backup frequency and retention;
- tested restoration procedures;
- schema migration and rollback strategy;
- incident response, access revocation and notification procedures;
- disaster recovery responsibilities and evidence.

No availability or recovery target is invented in this proposal.

## 14. Technology decisions — recommended status

| Area | Recommendation | Decision status |
|---|---|---|
| Mobile | Dart / Flutter | Accepted by ADR-001 |
| Backend/API | TypeScript modular monolith | Existing direction; implementation details open |
| Web | TypeScript; React/Next.js candidate | Not approved |
| AI/ML/scientific computing | Python | Existing direction; framework/provider open |
| Relational database | PostgreSQL | Leading candidate; physical design gated |
| Spatial database | PostGIS | Leading candidate with PostgreSQL; model/CRS decisions open |
| Media storage | S3-compatible object abstraction | Candidate; provider and policy open |
| API contract | JSON / OpenAPI | Accepted API-first principle; exact OAS/toolchain to be selected |
| Search | PostgreSQL first; benchmark dedicated search | Provider not approved |
| Identity | OIDC/OAuth-compatible integration | Candidate; identity provider not approved |
| Observability | OpenTelemetry-compatible approach | Directional recommendation; implementation open |
| Containers | OCI-compatible packaging where useful | Candidate; topology open |
| Orchestration | Start simple; evaluate later | Kubernetes not approved or required |
| Vector database | Do not add initially without evidence | Not selected |
| Additional languages | Rust/Go/Kotlin/Swift only for justified components | Not selected as general platform languages |
| Rust specialist use | Permitted only after the adoption gate in §14.1 | Allowed by ADR-001; no component approved |

## 14.1 Rust as a specialist implementation language

### Policy position

Rust is **permitted as a specialist implementation language under accepted ADR-001**, but it is not a core or default platform language. The core technology roles remain unchanged:

- TypeScript for platform/API/application services and web.
- Python for AI/ML, scientific computing, data science and model workflows.
- Dart / Flutter for mobile.
- PostgreSQL / PostGIS for the leading relational/spatial data platform.
- Rust only for a bounded component where measured technical evidence justifies its additional language, build, testing and operational costs.

This interpretation implements the existing phrase “Rust where justified” in ADR-001. It does not amend or supersede that accepted ADR, approve a Rust component, or authorize implementation.

### Suitable candidate areas — subject to evidence

Potential candidates include:

1. **High-throughput image/media processing:** CPU-intensive decoding, transformation, feature extraction or batch processing where profiling shows the existing Python/TypeScript implementation is a material bottleneck.
2. **Specialized scientific data processing:** parsing, normalization, validation, deduplication or streaming transformations over large datasets where memory use or throughput is demonstrably limiting.
3. **Specialized geospatial computation:** algorithms not adequately served by PostgreSQL/PostGIS or mature existing libraries, and only where correctness, CRS semantics and reproducibility can be independently tested.
4. **Python native extensions:** a narrow computational kernel called from the Python scientific/AI stack where a stable Python-facing interface is useful.
5. **WebAssembly computation:** portable, bounded browser-side computation where profiling demonstrates a material benefit and browser support, download size, memory limits and accessibility are addressed.

These are candidate use cases, not a commitment to use Rust in all or any of them. Existing libraries and database capabilities should be evaluated before writing a custom implementation.

### Explicit non-goals

Do not use Rust merely to:

- replace TypeScript for ordinary API, web or business-application logic;
- replace Python's model training, experimentation, evaluation or scientific ecosystem;
- duplicate PostgreSQL/PostGIS capabilities or move authoritative data invariants out of their governed data layer;
- create a separate microservice solely because a component is written in Rust;
- pursue language novelty, benchmark vanity or speculative future scaling;
- create an empty Rust workspace or placeholder crates before a real component is approved.

### Mandatory adoption gate

A Rust component may be proposed only when all of the following are documented:

1. **Representative baseline:** a reproducible workload and representative data set, with rights and privacy eligibility established.
2. **Measured problem:** profiling identifies a material CPU, memory, throughput, latency or capability bottleneck in the current design.
3. **Comparative implementation:** a credible baseline in the existing language/library stack is compared with a Rust alternative. Include the simplest suitable optimized baseline, not an intentionally weak implementation.
4. **Evidence:** benchmark methodology, environment, input sizes, warm-up, repeated runs, variance, correctness checks and results are recorded. Compare end-to-end performance as well as kernel performance; include serialization, copying, FFI and deployment overhead.
5. **Total cost:** assess developer skills, build and cross-compilation, CI, packaging, debugging, observability, dependency/security updates, platform coverage and long-term maintainability.
6. **Bounded responsibility:** the component has one clear responsibility, explicit inputs/outputs, stable versioned interfaces and a named owning module. It must not bypass module ownership or write around domain invariants.
7. **Correctness and safety:** unit, property-based, fuzz, integration and regression tests are appropriate to the component; compare outputs against trusted reference implementations and preserve errors, uncertainty and provenance.
8. **Operational readiness:** supported operating systems/architectures, reproducible builds, artifact provenance, dependency review, vulnerability handling and rollback/replacement are defined.
9. **Approval:** the proposal is reviewed by the architecture owner and relevant scientific/security/operations owners before implementation is treated as an approved project decision.

A performance improvement alone is not sufficient if the resulting component is harder to operate, validate or maintain than the original.

### Integration and repository rules

- Keep Rust behind a narrow internal interface. Do not expose Rust-specific types or implementation details in public API contracts.
- For Python integration, evaluate PyO3 with Maturin or a process/job boundary; choose based on packaging, runtime isolation, data-copying and failure-handling requirements.
- For browser integration, evaluate WebAssembly only for bounded computation. Keep UI, DOM interaction, authorization and sensitive-data disclosure policy in the established web application.
- Define ownership and lifetime of buffers explicitly; avoid unnecessary copies of large image or scientific-data payloads.
- Preserve deterministic behaviour where required, version information, source lineage, rights eligibility, error semantics and reproducible test fixtures.
- Keep Rust crates in a clearly named location such as `native/rust/<component>/` only after an actual component is approved. Do not create speculative empty crates.
- Pin and review toolchains and dependencies; build and test supported targets in CI. Do not assume that a successful local build proves cross-platform compatibility.

### Decision record

| Question | Current position |
|---|---|
| Is Rust a core platform language? | No |
| Is Rust allowed by accepted architecture? | Yes, for justified performance-critical components under ADR-001 |
| Is any Rust component approved? | No |
| Is a Rust workspace/crate authorized now? | No |
| What permits adoption? | Measured comparative evidence, bounded responsibility, tests, operational readiness and explicit review |

## 15. Full architecture delivery and decision plan

This is a dependency-led plan, not a deadline commitment. No phase reduces the full-product scope.

| Stage | Work | Exit evidence / gate |
|---|---|---|
| A. Governance baseline | Review PRs #15/#16 and topic-branch dependencies; establish canonical doc inventory | Owner-approved governance and safe branch plan |
| B. Product baseline | Review PRs #17–#19 as a connected set; reconcile PRD, Blueprint and RTM | Approved full-product vision, canonical PRD and traceability baseline |
| C. Scientific model | Resolve DR-01–DR-12; execute LDM-01–LDM-16; independent discipline review | Approved logical scientific model and recorded validation evidence |
| D. Rights, privacy and security | Asset/purpose rights, community knowledge, location sensitivity, threat model and legal review | Approved policies, data inventory and security/privacy controls |
| E. Logical architecture | Module ownership, API contracts, dependency rules, workflows, data ownership and deployment view | Approved architecture baseline and required ADRs |
| F. Physical data design | PostgreSQL/PostGIS schema, constraints, migrations, indexes and retention design | Reproducible model tests, migration review and owner authorization |
| G. Engineering foundation | Repository code layout, language toolchains, CI, test harness, lint/type checks, security scans | Clean reproducible build and architecture checks |
| H. Platform implementation | API, identity integration, media, rights, audit, ingestion and core domain modules | Contract, integration, security and data-integrity evidence |
| I. Full client implementation | Flutter, web, expert and admin workflows | Accessibility, usability, client integration and end-to-end evidence |
| J. AI/ML system | Dataset governance, evaluation, inference, calibration, abstention and model operations | Rights-cleared evaluation evidence and controlled model release |
| K. System verification | Performance, resilience, security, privacy, scientific quality and operational exercises | System-wide acceptance and risk disposition |
| L. Production readiness | Runbooks, monitoring, support, backup/restore, incident response, cost and governance | Explicit production-readiness decision |
| M. Release and improvement | Controlled release, monitoring, correction, maintenance and new capability evolution | Release evidence and ongoing ownership |

Stages may overlap where dependencies permit, but scientific, rights, privacy and security gates cannot be bypassed for convenience.

## 16. Principal risks and controls

| Risk | Severity | Recommended control |
|---|---|---|
| Physical schema created before scientific model reconciliation | Blocker | Enforce Stage C exit gate |
| React Native introduced despite Flutter ADR | Critical | Keep ADR-001 authoritative; block conflicting implementation |
| Modular architecture becomes premature microservices | Critical | Module contracts first; deployment extraction evidence required |
| Cross-module direct database writes | Critical | Module-owned writes and architecture tests |
| Rights-unclear source/media enters training or public display | Critical | Asset-purpose policy gate and quarantine |
| Sensitive plant coordinates leak through derived systems | Critical | End-to-end disclosure policy and negative tests |
| AI confidence presented as verified species identity | Critical | Distinct inference/determination types, abstention and UX/API semantics |
| 200-line guideline causes artificial fragmentation | Major | Soft threshold, documented exceptions and cohesion-first review |
| Shared STF boundaries are assumed before ADR-011 | Major | Logical boundary only until owner decision |
| Search/vector infrastructure is selected without workload | Major | Benchmark first; derived/rebuildable architecture |
| Too many topic branches and stacked PR dependencies | Major | Inventory, dependency graph and preservation-first retirement |
| No accountable scientific/security/operations reviewers | Critical | Assign actual roles and record qualified review before relevant gates |

## 17. Decisions requested from the project owner

1. Accept, amend or reject the proposed modular-monolith target architecture.
2. Confirm that the proposed logical module catalogue is an appropriate full-product decomposition.
3. Accept the proposed repository structure as a target, subject to introducing folders only when code exists.
4. Adopt the 200 non-blank source-line guideline with the stated exception and review process.
5. Confirm that files above 300 lines require explicit reviewer agreement unless generated or otherwise documented.
6. Confirm that Flutter remains the mobile direction under ADR-001.
7. Confirm that React/Next.js, OpenSearch, object-storage provider, identity provider, cloud and orchestration remain open candidates.
8. Confirm that physical schema work remains blocked until the scientific-model gate is closed.
9. Assign accountable architecture, scientific, security/privacy, rights/legal, accessibility and operations reviewers.
10. Authorize a subsequent, separately scoped implementation-foundation task only after the relevant product, scientific and architecture baselines are approved.

## 18. Research references checked

External technical references checked on 20 November 2026. These support architectural guidance; they do not independently approve a project decision.

1. Flutter — [Guide to app architecture](https://docs.flutter.dev/app-architecture/guide) and [Architecture recommendations](https://docs.flutter.dev/app-architecture/recommendations). The Flutter guidance recommends separation of UI/data layers, views/view-models, repositories/services, unidirectional data flow, immutable models and testing; it describes guidance rather than inflexible rules.
2. TypeScript — [Project References](https://www.typescriptlang.org/docs/handbook/project-references). Supports structuring TypeScript programs into smaller logical projects and enforcing separation; adoption should follow actual package/build needs.
3. Python Packaging Authority — [src layout vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) and [Packaging Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/). Basis for a packaged Python source layout and reproducible package structure.
4. OpenAPI Initiative — [OpenAPI Specification versions](https://spec.openapis.org/oas/). Version 3.2.1 was listed as current at the research check; confirm ecosystem/tool support before pinning it.
5. PostgreSQL — [Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html). Documents database-level integrity mechanisms including primary keys, foreign keys, unique, check and exclusion constraints.
6. PostGIS — [Spatial data management](https://postgis.net/docs/using_postgis_dbmanagement.html), [Geometry or geography FAQ](https://postgis.net/documentation/faq/geometry-or-geography/) and [Spatial indexes](https://postgis.net/documentation/faq/spatial-indexes/). Geometry/geography have different semantics and performance characteristics; GiST spatial indexing is important for supported spatial query patterns.
7. OWASP — [Application Security Verification Standard 5.0.0](https://asvs.owasp.org/) for web/API verification.
8. OWASP Mobile Application Security — [MASVS](https://mas.owasp.org/MASVS/) and [Using the MASVS](https://mas.owasp.org/MASVS/03-Using_the_MASVS/), for mobile security and privacy controls and their testing relationship.
9. Google Engineering Practices — [Small CLs](https://github.com/google/eng-practices/blob/master/review/developer/small-cls.md) and [TypeScript style guide](https://google.github.io/styleguide/tsguide.html). These support focused reviewable changes and small functions; they do not establish a universal 200-line source-file limit.
10. The Rust Project — [The Rust Programming Language](https://doc.rust-lang.org/book/), including ownership and compiler-checked memory management. Language capabilities are not evidence that a Rust component is needed in this product.
11. PyO3 — [User Guide](https://pyo3.rs/main/) and [Maturin](https://github.com/PyO3/maturin). These document a supported route for exposing Rust native modules to Python; packaging and ABI/platform support still require project validation.
12. wasm-bindgen — [Guide](https://wasm-bindgen.github.io/wasm-bindgen/). Documents Rust/WebAssembly interoperability with JavaScript; it does not remove browser compatibility, payload-size, security or performance testing requirements.

---

## 19. Current decision and implementation status

| Item | Status |
|---|---|
| Full product scope | Described in proposed Blueprint; not owner-approved |
| Task 03 PRD | Source-preserving working baseline; not accepted |
| Task 04 architecture evaluation | Source-preserving working baseline; historical candidates reconciled by overlays |
| Requirements Traceability Register | Proposed in PR #19 |
| ADR-001 through ADR-010 | Accepted and unchanged by this plan |
| ADR-011 / STF boundary | Proposed; not accepted |
| Modular monolith target | Recommended here; not yet accepted as a new decision |
| Flutter mobile | Accepted under ADR-001 |
| TypeScript / Python / PostgreSQL / PostGIS roles | Existing direction or leading candidates; details not all frozen |
| Physical database design | Not ready; scientific-model gates remain |
| Target repository structure | Proposed; not implemented |
| 200-line source-file guideline | Proposed; not yet adopted as repository policy |
| Application source code on main | None found in inspected main tree |
| Build/test/security pipeline for application code | Not assessed as implemented; no application code found |
| Production deployment | Not present / not claimed |

**End of proposed architecture plan — STF-BI-ARCH-PLAN-001, Version 0.1.**
