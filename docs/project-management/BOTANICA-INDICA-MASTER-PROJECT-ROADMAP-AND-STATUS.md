# Botanica Indica — Master Project Roadmap and Status

- **Document ID:** STF-BI-PMO-001
- **Version:** 0.2 — Reconciled master roadmap and 23 November source/status update
- **Status:** Proposed project-control document; owner review required
- **Prepared:** 21 November 2026
- **Decision authority:** Save Tiger First project owner
- **Repository:** `Save-Tiger-First/botanica-indica`
- **Working branch:** `docs/full-system-architecture-and-repo-engineering-plan`
- **Related PR:** [PR #20](https://github.com/Save-Tiger-First/botanica-indica/pull/20)
- **Supersedes:** The September 2026 conversation-level “Save Tiger First — Master Project Checklist” as the current status/sequence reference. The original checklist is retained as historical planning input, not deleted or rewritten.

> **Decision boundary:** This document reconciles the original master checklist with the current repository. It does not approve the product blueprint, PRD, architecture, scientific data model, any ADR amendment, implementation, budget, schedule, external partnership, field pilot or release. It does not merge or close PRs, delete branches, change protections or authorize irreversible actions.

## 1. Executive position

Botanica Indica has progressed substantially beyond the original September checklist. The project has moved from a broad idea and initial task planning into a documentation-led product, architecture and scientific-data design programme.

The project is **not yet in production implementation**. The repository contains extensive proposals, source-preserving working baselines, architecture decisions, validation plans and governance controls. These are valuable deliverables, but their presence must not be confused with owner acceptance, independent specialist approval, executable test evidence or operational software.

The governing product ambition remains a **full-fledged, full-product India-first botanical intelligence platform**, not an MVP. Prototypes, test fixtures, pilots and staged releases are validation and delivery mechanisms; they do not reduce the target product scope. There is no artificial launch deadline.

### Current overall assessment

| Area | Current position |
|---|---|
| Project vision and full capability scope | Extensively documented in proposed blueprint; owner acceptance pending |
| Tasks 01–02 | Referenced as source inputs in the product blueprint; canonical repository copies were not found in the inspected branch trees |
| Task 03 — PRD | Complete source-preserving repository transcription; working baseline, not accepted |
| Task 04 — System Architecture & Technology Evaluation | Complete source-preserving repository transcription with governance overlay; working baseline, not accepted |
| Task 05 — Data Architecture / Scientific Data Model | Extensive proposals and review package; scientific decisions remain open |
| Task 05E — Physical database design | **NOT READY** |
| Full system architecture | Proposed target architecture and engineering plan; not accepted |
| Requirements and capability traceability | Extensive proposed register and crosswalks; owner approval and test evidence pending |
| Application implementation | No application source code verified on `main` |
| Scientific validation | Plans and synthetic fixture designs exist; no execution or independent specialist sign-off claimed |
| Repository governance | Substantial work completed; branch consolidation target remains unmet |
| Production deployment | Not implemented or claimed |

## 2. How to use this roadmap

This is the project-level navigation and status register. It does not replace the detailed source documents, ADRs, scientific decision register, requirements traceability register or branch inventory.

Use these status definitions consistently:

- **Completed — artifact:** a document or scoped task artifact exists and has been fetched/verified. This does not mean it is approved.
- **Proposed:** a recommendation or design exists but has not been accepted by the project owner or relevant authority.
- **Under review:** evidence or specialist/owner review is required.
- **Not tested:** no reproducible execution evidence exists.
- **Blocked:** a prerequisite or decision prevents safe progression.
- **Not started:** no verified work product or execution exists.
- **Accepted:** explicitly approved by the appropriate authority and recorded in the relevant decision source.
- **Implemented:** software or operational capability exists and has been verified in its intended environment.

Never convert a proposed document into an accepted requirement merely by copying it into another document.

## 3. Canonical task numbering and reconciliation

The September checklist contains a numbering inconsistency: it describes Task 04 once as “Scientific Requirements” and later as “System Architecture & Technology Evaluation”; it also places system architecture at Task 06 and technology selection at Task 07.

The current repository sequence is different and must be used unless the project owner explicitly approves a controlled renumbering:

| Canonical task | Subject | Current interpretation |
|---|---|---|
| Task 01 | Save Tiger First / Botanica Indica Project Charter | Project purpose, mandate, scope, boundaries, governance and success |
| Task 02 | Problem & Opportunity Analysis | India-focused botanical problem, user needs, evidence and opportunity |
| Task 03 | Product Requirements Document | Product requirements, journeys, constraints and acceptance criteria |
| Task 04 | System Architecture & Technology Evaluation | System architecture, technology evaluation and architecture trade-offs |
| Task 05 | Data Architecture and Scientific Data Model | Data sources, domain concepts, data governance and scientific data architecture |
| Task 05B | Scientific Data Dictionary and Indian Test Cases | Definitions, fields, controlled values and representative cases |
| Task 05C | Logical Data Model | Candidate logical entities, relationships, integrity and semantics |
| Task 05D | Logical Model Validation | Reconciliation, scenarios, validation criteria and evidence |
| Task 05E | Physical Database Design | Future physical schema and database implementation design; currently blocked |

Scientific requirements are cross-cutting across Tasks 02–05 and the accepted ADRs. Do not create a duplicate “Task 04 — Scientific Requirements” or renumber current repository work informally.

The full-system architecture plan and full-product blueprint are additional proposed planning artifacts. They do not silently replace Task 03, Task 04 or the accepted ADRs.

## 4. Current task and workstream register

### 4.1 Foundation and product definition

| Work item | Evidence / location | Status | Required next action |
|---|---|---|---|
| Task 01 — Project Charter | Referenced as a source input in PR #17 Blueprint; no canonical Task 01 file found in the inspected GitHub branch trees | Source artifact/repository status requires reconciliation | Preserve the original full-detail source; verify its version and transcribe it into the canonical repository baseline before acceptance |
| Task 02 — Problem & Opportunity Analysis | Referenced as a source input in PR #17 Blueprint; no canonical Task 02 file found in the inspected GitHub branch trees | Source artifact/repository status requires reconciliation | Preserve the original full-detail source; reconcile its research claims, assumptions and estimates against current evidence |
| Task 03 — Product Requirements Document v0.1 | PR #18, `docs/product/TASK-03-PRODUCT-REQUIREMENTS-DOCUMENT.md` | Complete source-preserving transcription; working baseline, not accepted | Owner review; resolve traceability gaps and complete acceptance-test design |
| Task 04 — System Architecture & Technology Evaluation v0.1 | PR #18, `docs/architecture/TASK-04-SYSTEM-ARCHITECTURE-AND-TECHNOLOGY-EVALUATION.md` | Complete source-preserving transcription plus governance overlay; working baseline, not accepted | Owner/architecture review; reconcile with PR #20 target architecture and accepted ADRs |
| Full Product Vision and Capability Blueprint v0.2 | PR #17, `docs/product/BOTANICA-INDICA-FULL-PRODUCT-VISION-AND-CAPABILITY-BLUEPRINT.md` | Proposed; owner review required | Confirm full-product boundaries, capability scope, success measures and capability ownership |
| Requirements Traceability Register v0.3 | PR #19, `docs/product/REQUIREMENTS-TRACEABILITY-REGISTER.md` | Proposed; not approved requirements baseline | Review identity/shared-platform mapping, ODR-01/EVT-27–EVT-44 traceability, source SHAs and acceptance criteria |
| Workflow Lifecycle and State-Machine Specification v0.2 | PR #19, `docs/product/WORKFLOW-LIFECYCLE-AND-STATE-MACHINE-SPECIFICATION.md` | Proposed; not approved workflow policy or implementation; `record_created` versus `server_received` is a proposed clarification | Validate lifecycle terminology with product, scientific, API, rights, privacy and operational reviewers |

**Important:** The current inspected repository tree on the PR #16 branch does not contain canonical Task 01 or Task 02 files. PR #17 references those materials as inputs, so they should not be treated as nonexistent; their original source versions and exact provenance must be retrieved and reconciled before a formal baseline is declared.

### 4.2 Scientific data architecture and validation

| Work item | Evidence / location | Status | Required next action |
|---|---|---|---|
| Task 05 — Data Architecture | PR #3, `docs/task-05-data-architecture` | Proposed | Reconcile with Task 05B/05C/05D and PR #9 review findings |
| Task 05B — Scientific Data Dictionary and Indian Test Cases | PR #4, `docs/task-05-data-dictionary` | Proposed; updated source branch | Review definitions, source semantics, term versions and Indian coverage |
| Task 05C Candidate A | PR #5, `docs/task-05c-logical-data-model` | Principal review candidate only; **not approved** | Resolve all blocking DR/LDM findings and compare with Candidate B |
| Task 05C Candidate B | PR #21, `docs/task-05c-logical-database-model` | Alternative preserved for comparison | Preserve unique semantics and compare field/relationship/cardinality differences; do not merge wholesale |
| Scientific Data Model Review Pack | PR #9 | Draft review instrument; not expert approval | Complete discipline-specific review and reconcile all blocking decisions |
| Validation Matrix and Decision Register | PR #9 | Proposed; LDM/EVT/FLD scenarios are not tested unless actual run evidence is recorded | Keep stable IDs; attach reproducible evidence and review outcomes |
| Task 05D v3 | PR #11, stacked on PR #5 | Proposed validation gate; dependency-sensitive | Reconcile its base and unique content with Candidate A and PR #9 |
| Earlier Task 05D material | PRs #22 and #23 | Preserved alternatives/history | Compare and retain unique findings; avoid reintroducing superseded positions |
| Hortus Malabaricus historical provenance case | PR #9 | Proposed historical case study and review aid | Use only as a provenance/rights/attribution stress case; verify historical claims independently before treating them as facts |
| Hortus validation crosswalk | Main and PR #9 workstream | Proposed mapping to existing model and review scenarios | Reconcile the main-branch commit with the PR #9 version and branch history |
| Hortus synthetic fixture design HMF-01–HMF-08 | PR #9, `docs/reviews/HORTUS-MALABARICUS-SYNTHETIC-VALIDATION-FIXTURE-DESIGN.md` | Design only; fixtures not instantiated or executed | Specialist review, then isolated synthetic test package and reproducible execution |
| Event/Survey/Occurrence validation | PR #9 decision register; EVT-27 onward | Proposed tests; not executed | Resolve event/survey hierarchy, reporting completeness, occurrence semantics and ODR-01 validation |
| Task 05E — Physical database design | Gated by PR #9 review package | **NOT READY** | Do not begin until model decisions, specialist reviews and test evidence meet the readiness gate |

**Scientific blockers remain material.** Among them: canonical Event–Survey–Occurrence relationships; assessment versus occurrence outcome representation; TCS concept/treatment semantics; typed scientific-assertion subjects; source-specific name usage; identification versioning; non-detection/export semantics; rights/provenance; and Candidate A's internal relationship/cardinality reconciliation.

ODR-01 authorizes only a narrow, profile-specific external export interpretation under explicit scope, completeness, version, mapping and audit conditions. It does not create internal absence assertions and does not approve Task 05C, Task 05D, Task 05E, an API, schema or implementation.

### 4.3 System architecture and engineering

| Work item | Evidence / location | Status | Required next action |
|---|---|---|---|
| Task 04 architecture baseline | PR #18 | Working baseline, not accepted | Owner/architecture review |
| Full System Architecture and Repository Engineering Plan v0.2 | PR #20, `docs/architecture/BOTANICA-INDICA-FULL-SYSTEM-ARCHITECTURE-AND-REPOSITORY-ENGINEERING-PLAN.md` | Proposed target architecture and refreshed source inventory; not accepted or implementation authorization | Review modular-monolith recommendation, module boundaries, repository plan, security and operations controls |
| API command/idempotency/conflict-resolution design v0.2 | PR #19 | Proposed design; ODR-01 export-only constraints and IETF draft v09 recorded; not implemented | Review command semantics, identity, concurrency, authorization, export gates and failure recovery |
| Offline/field synchronization architecture v0.2 | PR #19 | Proposed design; ODR-01 offline safeguards recorded; not implemented | Review offline security, conflict handling, sensitive data and rights revalidation |
| Technology decisions | Accepted ADRs and proposed Task 04/PR #20 | Mixed: some accepted, many remain candidates | Preserve ADR-001 Flutter direction; evaluate open candidates with explicit evidence |
| Repository engineering structure | PR #20 | Proposed; not implemented | Do not create multiple repositories or deployable services before approved ownership and dependency boundaries |

Current technology posture:

- **Accepted:** Dart / Flutter mobile direction under ADR-001.
- **Existing direction / leading candidates:** TypeScript for suitable platform/API/web services; Python for AI/ML and scientific computing; PostgreSQL/PostGIS for relational/spatial persistence.
- **Open:** web framework, cloud/provider, object storage, identity provider, search engine, vector technology, orchestration, and any Rust components.
- **Recommended but not yet accepted in PR #20:** start with a domain-oriented modular monolith, API contracts and explicit module boundaries; extract services only when workload, security, ownership or operational evidence justifies it.
- **Blocked:** physical database schema while scientific model gates remain open.

### 4.4 Governance, rights and adjacent STF programmes

| Workstream | Evidence / PR | Status | Required next action |
|---|---|---|---|
| Permanent AI operating standard and repository audit | PR #16 | Open draft; user instruction requires adherence to its branch version | Owner review; retain as governing working standard until accepted and merged |
| Branch lifecycle policy | PR #15 | **Closed 23 November 2026, unmerged, as superseded by PR #16** | Source branch `governance/branch-lifecycle-policy` remains present at `633105210d3a6c4c8e36287ed2dc44dee23f61ef`; delete only after fresh preservation/reference checks. Owner authorization was given; deletion has not yet been completed. |
| Asset-specific licensing/IP policy | PR #1 | Proposed | Reconcile duplicates and obtain qualified legal/licensing review |
| STF ecosystem boundaries / proposed ADR-011 | PR #2 and related architecture documents | Proposed; ADR-011 not accepted | Keep STF shared capabilities separate from Botanica domain ownership until owner decision |
| STF NatureTech/conservation impact strategy | PR #8 | Strategic proposal, not an approved Botanica requirement | Preserve as a separate STF strategic workstream |
| STF organisational readiness | PR #12, stacked on PR #8 | Proposed review | Verify governance, capacity and operational readiness; no organizational approval implied |
| Bengaluru urban biodiversity feasibility pilot | PR #13 | Proposal only | No site, funding, partner, fieldwork or intervention approved |
| Bengaluru pilot site-selection assessment | PR #14 | Preliminary research only | No site selected; retain feasibility-only status |

The STF strategy and Bengaluru pilot are adjacent or separate programmes. They must not silently expand Botanica Indica's product scope or be presented as funded/approved work.

## 5. Consolidated delivery gates

The original checklist's 22 phases overlap, duplicate capabilities and mix product scope, technical components, operational processes and release activities. Retain it as a broad capability inventory, but use the following gated sequence for project control.

| Gate | Purpose | Exit evidence | Current position |
|---|---|---|---|
| G0 — Governance and repository integrity | Stable authority, branch lifecycle, source preservation, document control | Accepted governance, current branch/PR inventory, traceable source versions | In progress; branch consolidation blocked |
| G1 — Project and problem foundation | Charter, problem/opportunity, target users, scope and success | Reconciled Task 01/02 sources and owner-approved foundation | Repository baseline incomplete |
| G2 — Product requirements | Complete user journeys, requirements, non-functional needs and acceptance criteria | Owner-approved Task 03, capability map and traceability | Proposed; review pending |
| G3 — Scientific/data architecture | Taxonomy, observations, evidence, provenance, rights, geography and data exchange | Resolved model decisions, reproducible tests and qualified specialist reviews | Major blocker; Task 05E not ready |
| G4 — System architecture and technology | Module boundaries, contracts, deployment shape, security, operations and technology decisions | Owner-approved Task 04/architecture baseline with ADR alignment | Proposed; review pending |
| G5 — Design and capability validation | UX, accessibility, prototypes, synthetic fixtures, integration and performance validation | Approved design decisions and reproducible validation evidence | Not yet established as an approved baseline |
| G6 — Engineering foundation | Repository/code structure, CI, environments, secrets, observability, test harness and developer setup | Repeatable development environment and quality gates | Not started for application code |
| G7 — Integrated full-product implementation | Build the full capability map in dependency-aware increments | Requirement-to-code-to-test-to-evidence traceability | Not started |
| G8 — System assurance and controlled release | Software, scientific, security, rights, privacy, accessibility and operational assurance | Release evidence, accountable approvals and recovery readiness | Not started |
| G9 — Operations and continuous improvement | Monitoring, taxonomy/data/model updates, corrections, support and governance | Sustainable operating ownership and improvement cycle | Not started |

Gates may overlap where dependencies permit, but a later gate cannot bypass a blocking scientific, rights, privacy, security or owner-approval requirement.

## 6. Full-product capability map

The proposed Blueprint v0.2 defines 16 capability domains. Preserve them as the intended full-product map; do not treat each domain as a separate microservice, repository or launch phase.

1. Botanical knowledge and taxonomic intelligence.
2. Interactive identification and the Evidence Engine.
3. Species and botanical knowledge profiles.
4. Observation, field documentation and survey workflows.
5. Geographic and ecological intelligence.
6. Evidence, expert review and scientific governance.
7. Data acquisition, ingestion, curation and interoperability.
8. Search, exploration, learning and discovery.
9. Community participation and stewardship.
10. Mobile application.
11. Public web and research platform.
12. Expert and scientific console.
13. Administration and data stewardship console.
14. API and institutional integration platform.
15. AI/ML research, evaluation and operations platform.
16. Analytics, observability and operational intelligence.

The proposed capability identifiers and legacy crosswalk in PR #17/PR #19 must remain the controlled traceability source until approved. Do not invent replacement identifiers or silently renumber existing Task 03 requirements.

## 7. Repository and branch governance status

### 7.1 Verified live baseline — 23 November 2026

Repository: `Save-Tiger-First/botanica-indica`  
Default branch: `main`

| Branch | Live head SHA |
|---|---|
| `main` | `6f2f51da093caf8183fde386dbec707cc6046d27` |
| `develop` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` |
| `staging` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` |

- Live branch count: **23**.
- Open PR count: **19**.
- PR #15 is closed without merge; its source branch still exists and remains pending authorized retirement.
- Owner's immediate ceiling: **7 branches total**.
- Intended final seven: three long-lived branches plus four existing consolidation destinations.
- No new branches are authorized.
- The four existing consolidation destinations are:
  1. `docs/repository-audit-and-ai-operating-standard` — PR #16.
  2. `docs/full-system-architecture-and-repo-engineering-plan` — PR #20.
  3. `review/scientific-data-model-review-pack` — PR #9.
  4. `strategy/naturetech-biodiversity-conservation-impact` — PR #8.

### 7.2 Open pull requests

Nineteen PRs are currently open: #1–#5, #8, #9, #11–#14 and #16–#23. All 19 are drafts. PR #15 was closed unmerged on 23 November 2026. Mergeability is volatile and not an acceptance signal. At the live check on 23 November 2026, PRs #17, #18, #19 and #20 are all reported mergeable; all remain open drafts and their documentation changes are proposals, not approvals. Mergeability is volatile and is not review approval, owner acceptance or scientific sign-off. Mergeability is not review approval, owner acceptance or scientific sign-off. Re-fetch immediately before any authorized integration.

The main consolidation routes recorded in the branch inventory are:

- Governance: PRs #1, #2 and #15 → PR #16 destination, after content-level reconciliation.
- Product/architecture: PRs #17, #18 and #19 → PR #20 destination, preserving unique content.
- Scientific data model: PRs #3, #4, #5, #11, #21, #22 and #23 → PR #9 destination, resolving stacked dependencies and competing versions.
- STF strategy: PRs #12, #13 and #14 → PR #8 destination, preserving feasibility-only status.

Do not retarget, merge, close or delete branches based solely on this routing summary. Use the live branch inventory and exact PR dependencies immediately before any proposed retirement.

### 7.3 Newly observed base-branch drift

Since the prior baseline, `main` has advanced by one commit from `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` to `6f2f51da093caf8183fde386dbec707cc6046d27`. The new commit adds `docs/reviews/HORTUS-MALABARICUS-VALIDATION-CROSSWALK.md`. `develop` and `staging` remain at the earlier SHA, and current open PR base snapshots still reference the earlier commit.

This is a real branch-synchronization and provenance issue to reconcile. The commit is not recorded as a PR merge in the current open-PR inventory. Do not cherry-pick, rebase or overwrite any branch until the exact crosswalk versions, commit provenance, PR #9 content and branch dependencies have been compared.

### 7.4 Branch retirement controls

The seven-branch ceiling is **not met**. PR #15 has been closed unmerged after a 131-commit ancestry and changed-file preservation check against PR #16. A post-closure check found no other open PR referencing `governance/branch-lifecycle-policy`; the branch still exists at SHA `633105210d3a6c4c8e36287ed2dc44dee23f61ef`. The owner authorized its deletion, but the available connected GitHub actions did not expose a branch/ref deletion operation, so deletion remains pending and must not be reported as complete. For all other branches, preserve unique content and provenance first; resolve or formally reject/close the relevant PR; confirm no open PR references the source branch; then obtain the required authorization before deleting that PR's own head branch.

At formal project completion, only `main` may remain, but that is a separate final lifecycle gate—not a reason to delete `develop`, `staging` or task branches prematurely.

## 8. Critical risks and open blockers

| Severity | Risk / issue | Current control or required response |
|---|---|---|
| **Blocker** | Scientific model not approved; Task 05E physical design is not ready | Close DR/LDM/EVT/FLD decisions with reproducible evidence and qualified review |
| **Blocker** | 23 branches against seven-branch ceiling | Preservation-first consolidation using only the four existing destinations |
| **Critical** | Main/develop/staging and PR bases have diverged | Refresh exact refs and reconcile the main-only Hortus crosswalk commit |
| **Critical** | Candidate A and Candidate B have not been conclusively reconciled | Preserve both, compare semantics, record owner/domain decision |
| **Critical** | No independent scientific, language, rights, privacy or community-governance sign-off recorded | Assign real qualified reviewers; do not invent endorsements |
| **Critical** | Data and media rights differ by asset and purpose | Asset-level rights evidence and fail-closed policy before ingestion, display, redistribution or AI use |
| **Critical** | Identification confidence may be mistaken for scientific certainty | Keep model score, calibrated probability, expert determination and taxonomic status distinct |
| **Major** | Task 01/02 canonical repository sources are not present in inspected branch trees | Retrieve exact originals, preserve provenance and add source-preserving repository baselines |
| **Major** | Proposed Task 03/04/Blueprint/RTM/Architecture documents may drift | Maintain one approved baseline per subject and cross-document traceability |
| **Major** | Task 03 acceptance criteria and lifecycle requirements are not yet fully evidenced | Complete acceptance-test traceability and resolve coverage gaps |
| **Major** | No application implementation or operational environment is verified | Do not report product capabilities as implemented |
| **Major** | Old effort estimates may be misread as commitments | Treat as historical planning assumptions; re-estimate after stable scope and architecture |

## 9. Historical estimate and resourcing

The original checklist's planning estimate of approximately **4,620 person-hours** (range approximately **4,250–5,850**) is a historical, high-level estimate. It is not a budget, funding commitment, staffing plan, delivery forecast or contractual estimate.

It should be replaced by a bottom-up estimate only after:
- Task 01–04 baselines and full-product capability scope are reviewed;
- scientific model and data dependencies are stable;
- non-functional, rights, privacy and security requirements are traceable;
- architecture and technology decisions are sufficiently mature;
- staffing assumptions and reviewer availability are known.

Do not infer a calendar launch date by dividing the hours by a hypothetical team size. The project has no artificial launch deadline.

## 10. Recommended priority sequence

### Priority 1 — Stabilize project governance and source control

1. Refresh the Branch Inventory and Consolidation Register against the live 23-branch list and all 20 open PRs.
2. Record the main-only crosswalk commit, current base drift, exact source-to-destination file mappings and stacked PR dependencies.
3. Reconcile PR #15 with PR #16; preserve unique content and do not merge/close without authorization.
4. Continue preservation-first consolidation toward the seven-branch ceiling; do not delete branches before the documented gates.

### Priority 2 — Establish an owner-reviewable product baseline

1. Retrieve and verify the original Task 01 and Task 02 files and their versions.
2. Preserve them in the repository as source-preserving baselines, with clear status and provenance.
3. Review Task 01–04 together with PR #17, PR #18, PR #19 and PR #20.
4. Resolve conflicting task numbering, scope boundaries, acceptance criteria, capability identifiers and architecture assumptions.
5. Obtain explicit owner decisions; until then, keep these documents Proposed/Working baseline.

### Priority 3 — Resolve scientific-data blockers before physical design

1. Reconcile Candidate A and Candidate B, including unique content and cardinality differences.
2. Resolve Event–Survey–Occurrence and assessment/outcome representation.
3. Complete taxonomic, nomenclatural, identification, provenance, rights and sensitive-location decisions.
4. Complete standards-version and term-level pinning, including DR-09.
5. Review HMF-01–HMF-08 and other synthetic fixtures with appropriate specialists.
6. Execute reproducible LDM/EVT/FLD tests in an isolated environment and attach actual evidence.
7. Only then reconsider Task 05E readiness.

### Priority 4 — Approve architecture and validate capabilities

1. Review PR #20's modular-monolith recommendation, module boundaries, contracts, repository layout and engineering controls.
2. Confirm accepted ADR alignment, especially Flutter under ADR-001.
3. Keep open technology choices open until workload and operational evidence justify selection.
4. Validate key journeys and cross-cutting workflows with prototypes and test harnesses without reducing the full-product scope.

### Priority 5 — Begin implementation only after gates

1. Approve engineering foundation, repository structure, CI, test strategy, environments, secrets and observability.
2. Build the system incrementally against the approved full-product capability map.
3. Preserve requirement → decision → implementation → test → evidence → release traceability.
4. Conduct integrated scientific, security, privacy, rights, accessibility and operational verification before controlled deployment.

## 11. Decisions requested from the project owner

The following are decisions requested, not presumed approvals:

1. Confirm this document as the canonical project-level roadmap/status register.
2. Confirm the canonical task numbering in Section 3.
3. Confirm the priority order in Section 10.
4. Confirm that Task 01 and Task 02 source originals should be reconciled into the repository as source-preserving baselines.
5. Confirm that no application implementation begins until product, scientific-data and architecture gates are sufficiently approved.
6. Confirm that the seven-branch ceiling remains in force and that the four existing consolidation destinations remain the only allowed workstream branches.
7. Assign accountable reviewers for product, architecture, taxonomy, field ecology, biodiversity informatics, language/script, rights/legal, privacy/security, community governance, accessibility and operations.

## 12. Verification record and limitations

### Exact source revisions inspected for this reconciliation

| Source | Ref | Blob SHA | Use |
|---|---|---|---|
| AI Project Operating Prompt | `docs/repository-audit-and-ai-operating-standard` | `53add3894d0502827e584614c70ad09cadaa637d` | Governing working standard; full content retrieved |
| Branch Inventory and Consolidation Register | `docs/repository-audit-and-ai-operating-standard` | `023a59ef9a6e3608b12ba463fce5b72db4f1b2bc` | Live branch/PR consolidation policy and status |
| Full Product Vision and Capability Blueprint v0.2 | `docs/full-product-vision-capability-blueprint` | `d3ec150524dda4928503f43556a97cd766b71312` | Full-product scope and canonical task-numbering correction |
| Task 03 PRD v0.1 | `docs/canonical-task-03-04-baselines` | `8b1ca0be04b3f4ad3b543c2f9fc48d46eb37faf8` | Product baseline |
| Task 04 architecture evaluation v0.1 | `docs/canonical-task-03-04-baselines` | `abc7b721fae8d4f4adede4dd0bf5d6a32098c5a3` | Architecture baseline |
| Requirements Traceability Register v0.2 | `docs/requirements-traceability-register` | `5636760faed6c7c7be0363d68afc203dd48e7e33` | Requirements/capability traceability |
| Workflow Lifecycle Specification v0.1 | `docs/requirements-traceability-register` | `03ca940095a9e39c5608548bdeec1ce0166bf76d` | Proposed lifecycle workflows |
| Full System Architecture Plan v0.1 | `docs/full-system-architecture-and-repo-engineering-plan` | `91fb02be87b42df51f92106f90fd536a01a5b902` | Proposed target architecture |
| Scientific Data Model Review Pack | `review/scientific-data-model-review-pack` | `c11f4b58d0908742474d3e58b4ec0aa3739f7b99` | Scientific review scope and blockers |
| Scientific Data Model Validation Matrix | `review/scientific-data-model-review-pack` | `3a33dfe47657a96456f56c2f12a0b7d355b6c6a5` | LDM/EVT decisions and Task 05E gate |

### Live repository facts checked

- `main`: `6f2f51da093caf8183fde386dbec707cc6046d27`
- `develop`: `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`
- `staging`: `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`
- Branch count: 23.
- Open PRs: 19 (#1–#5, #8, #9, #11–#14, #16–#23); all 19 are drafts; PR #15 is closed unmerged.
- PR #20 remains open and draft; this document is added to its existing head branch.
- No application source code was found in the inspected `main` tree.
- No external expert review, test execution, physical schema, application implementation, production deployment, funding, institutional partnership or fieldwork authorization is claimed.

### Actions not taken

- No PR merged, closed or retargeted.
- No branch created, deleted, renamed or force-pushed.
- No repository protection, ruleset, permission or default-branch setting changed.
- No accepted ADR amended.
- No scientific model approved.
- No source dataset, historical scan, personal information or community-held knowledge ingested.
- No application code or physical database schema implemented.

**Final status:** this roadmap is a proposed, evidence-linked project-control document. Owner review is required before it becomes the accepted master roadmap.


### 7.5 Graphify tooling assessment update — 23 November 2026

The Graphify assessment on this same PR #20 branch has been updated with a release/provenance and connected-workspace recheck. Its current blob SHA is `3face0ee6ec84aa4b90ded193938eb65eea7590e`. The proposal now distinguishes the Graphify v8 branch head from the latest PyPI 0.9.115 attested source commit, records the package artifact checksum and exact-version security policy, adds local query-log and semantic-backend controls, and records the connected Free workspace's README-only indexing and lack of PR #19/#20 review records. This remains a local-only tooling proposal; no CLI installation, extraction, MCP service, cloud connection or CI integration is claimed.


### 7.6 Earlier product/architecture comparison snapshot — superseded by Section 7.7

Fresh commit comparisons were run on 23 November 2026 using current source heads PR #17 `b66c16355d0ded4f20f1a84172eab8b47d133277`, PR #18 `0f908f8221ad3434cc84fe2cd41b735aad0a752a`, PR #19 `d40f9c4d2e97e68d6b55bd86b1cb0df046136f2a` and PR #20 `bbf2e95a4efc95029f266a7da06da5adedbe604a`.

| Comparison | Common ancestor | PR #20-only commits | Source-branch-only commits | Result |
|---|---|---:|---:|---|
| PR #17 vs PR #20 | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` (`develop`) | 20 | 9 | Diverged |
| PR #18 vs PR #20 | same | 20 | 2 | Diverged |
| PR #19 vs PR #20 | same | 20 | 51 | Diverged |

**Interpretation:** PR #17, #18, #19 and #20 are parallel workstreams, not a linear stack. Their heads share `develop` as the merge base, but none of the three source heads is an ancestor of PR #20. PR #19 has the largest source-only history and must receive particular care.

The changed-file inventories also show that PR #20 currently contains its own architecture plan, Graphify assessment, roadmap and baseline audit; it does not yet contain the Task 03/04, Blueprint or RTM files carried by PRs #17–#19.

**Required preservation-first route:**
1. Compare the source commits and file-level diffs of PR #17, #18 and #19 with PR #20's target architecture and audit.
2. Identify genuinely shared paths, unique files, and content already reproduced or superseded in PR #20.
3. Preserve original source documents and their provenance; reconcile only with explicit crosswalks and status labels.
4. Prepare a sequenced integration proposal for the project owner. Do not retarget, merge, cherry-pick or close any of these PRs merely because the roadmap groups them into one workstream.
5. Re-run commit comparisons and changed-file inventories immediately before any authorized integration or source-branch retirement.

This check does not approve the PR #20 architecture, the PR #17 Blueprint, the PR #18 Task 03/04 baselines or the PR #19 RTM. It does not authorize any PR or branch lifecycle action.


### 7.7 Current PR #17–#20 comparison and changed-file check — 23 November 2026

**Live PR heads checked:** PR #17 `b66c16355d0ded4f20f1a84172eab8b47d133277` (9 commits; 1 changed file); PR #18 `0f908f8221ad3434cc84fe2cd41b735aad0a752a` (2 commits; 2 changed files); PR #19 `dc97f578eeab26f97ac09c8060403b770fbdcfa7` (53 commits; 8 changed files); PR #20 `d1b9fc38fdc4777d7c522f8959437cc2e9171018` (25 commits; 4 changed files). All four PRs are open drafts and were reported mergeable at the live metadata check.

| Comparison | Merge base | PR #20-only commits | Source-branch-only commits | Status |
|---|---|---:|---:|---|
| PR #17 vs PR #20 | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` (`develop`) | 27 | 9 | Diverged |
| PR #18 vs PR #20 | same | 27 | 2 | Diverged |
| PR #19 vs PR #20 | same | 25 | 53 | Diverged |

**Changed-file overlap check:** PR #17 changes only the product Blueprint; PR #18 changes the Task 03 PRD and Task 04 architecture baseline; PR #19 changes its eight traceability/workflow/API/offline/audit documents; PR #20 changes its architecture plan, Graphify assessment, roadmap and baseline audit. No changed paths overlap among PRs #17–#20 in the inventories checked.

**Interpretation:** These are parallel, diverged workstreams sharing `develop` as their merge base, not a linear stack. PR #19 has the largest source-only history (53 commits) and requires the most careful preservation review. No-path-overlap reduces direct file collision risk but does not establish semantic compatibility or safe merge order.

**Recommendation:** Continue treating PR #20 as the existing documentation-integration destination, but do not merge PRs #17–#19 based on these comparisons alone. Preserve source provenance, inspect semantic dependencies, verify each destination change and obtain the required authorization. Keep all PRs draft until review and acceptance gates are met.
### 12.1 PR #19 / PR #20 integration revalidation — 23 November 2026

This follow-up revalidates the current product/requirements/architecture documentation after the PR #19 traceability reconciliation and Graphify tooling assessment update. The source SHAs in Section 12's original table remain the historical revisions inspected when v0.1 was prepared; the following table records the newer revisions re-fetched for this follow-up.

| Source | Ref | Blob SHA | Current status |
|---|---|---|---|
| Requirements Traceability Register v0.3 | `docs/requirements-traceability-register` | `c4b4ef1a5adfd367edcf982c1f9b115fa5d8aad6` | Proposed; identity mapping and ODR-01/EVT-27–EVT-44 traceability reconciled |
| Workflow Lifecycle Specification v0.2 | `docs/requirements-traceability-register` | `498af08ec60e3626e8b60ab5047acae1a8861eb5` | Proposed; `record_created` versus `server_received` terminology clarification only |
| Workflow-to-Requirements Crosswalk v0.2 | `docs/requirements-traceability-register` | `61d2111ace5c408eaf503bdf17b2ccb822f90978` | Proposed; ODR-01 and EVT-27–EVT-44 mapped |
| Offline/Field Synchronization Specification v0.2 | `docs/requirements-traceability-register` | `a46c7cc1de9d1ea5c5faed7574d23de1d1a48e13` | Proposed; offline ODR-01 safeguards recorded |
| API Command/Idempotency Contract v0.2 | `docs/requirements-traceability-register` | `bc0f3e93ec6ef2d2c2039b56739db38296c03281` | Proposed; export-only API constraints and IETF draft v09 reference |
| Task 03–04 Cross-Document Readiness Audit with follow-up | `docs/requirements-traceability-register` | `d01ec7041ca2571ae8c11c4a0d95816c7d2daa7c` | Proposed audit/follow-up; no approval conferred |
| Full System Architecture Plan v0.2 | `docs/full-system-architecture-and-repo-engineering-plan` | `33c42ead0d32f24530d28fdbcfd1024c2495a5eb` | Proposed; source inventory refreshed |
| Graphify Repository Intelligence Tooling Assessment | `docs/full-system-architecture-and-repo-engineering-plan` | `3face0ee6ec84aa4b90ded193938eb65eea7590e` | Proposed local-only tooling pilot; not executed |
| Scientific Data Model Validation Matrix | `review/scientific-data-model-review-pack` | `3a33dfe47657a96456f56f2c12a0b7d355b6c6a5` | ODR-01 authorized; EVT-27–EVT-44 proposed and unexecuted |

**Integration interpretation:** PR #17–#20 remain parallel workstreams, not a safe linear stack. The comparison counts recorded in this earlier follow-up are historical and superseded by the fresh PR #17–#20 comparison in Section 7.7. PR #19's larger divergence reflects its accumulated traceability and audit revisions. Preserve unique content and provenance; do not merge, retarget or close PRs based on commit counts alone.

**Graphify interpretation:** the connected Graphify Free workspace currently indexes only README.md for this documentation-led repository (17 nodes, 29 edges) and has no automated review record for PR #19 or PR #20. A local CLI evaluation remains the recommended way to test document-rich graphing, but it is not yet approved or executed.

**No implementation readiness change:** Task 05C remains unapproved; Task 05E remains not ready. EVT-27–EVT-44, OFF-001–OFF-036 and API-SYNC-001–042 remain proposed and unexecuted. No API schema, physical database design, application implementation or production release is authorized by this follow-up.
