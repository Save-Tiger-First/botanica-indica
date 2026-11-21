# Product and Architecture Baseline Audit — 21 November 2026

- **Repository:** `Save-Tiger-First/botanica-indica`
- **Review branch:** `docs/full-system-architecture-and-repo-engineering-plan` (existing branch; PR #20)
- **Scope:** PRs #17–#20 as one connected product/requirements/architecture decision package
- **Status:** Review findings and recommendations only; no product, architecture, scientific, legal or implementation approval is conferred
- **Operating prompt:** `docs/governance/AI-PROJECT-OPERATING-PROMPT.md`, PR #16 branch, blob `61059c74d4d20309ff76e055059ab33f381ca4f2`

## 1. Executive assessment

The four workstreams are directionally coherent and substantially stronger than treating the project as a single image-classification application. The proposed system preserves the full India-first botanical intelligence ambition, evidence-aware identification, taxonomy and source reconciliation, observations, expert review, data rights, privacy, interoperability and reusable STF foundations.

**The package is not ready for acceptance as a canonical product/architecture baseline.** One material identifier conflict and one important platform/domain-boundary decision must be resolved first. Requirements coverage is promising, but several lifecycle and scope controls need stronger traceability. Architecture is appropriately conservative in several areas, but its current repository snapshot and source-document references need a fresh companion snapshot before anyone relies on them as current.

No application implementation was found on `main`. These documents remain proposals or working baselines.

## 2. Verified repository snapshot

Fetched from GitHub on 21 November 2026:

| Item | Verified state |
|---|---|
| Branches | 23 total |
| Open pull requests | 20 |
| Long-lived branches | `main`, `develop`, `staging` |
| Long-lived branch tips | All three at `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` |
| PR #16 | Open draft; base `develop`; head `docs/repository-audit-and-ai-operating-standard`; head `33a4a1d7d1c8264187b2aa0840c8c18029b8ce7b` |
| PR #17 | Open draft; base `develop`; head `docs/full-product-vision-capability-blueprint`; head `234b21846db53e7dbac9b8e8f4ccad2b6c3012ff` |
| PR #18 | Open draft; base `develop`; head `docs/canonical-task-03-04-baselines`; head `0f908f8221ad3434cc84fe2cd41b735aad0a752a` |
| PR #19 | Open draft; base `develop`; head `docs/requirements-traceability-register`; head `5c4570df6c51bbb9c28fa826f04e57435f784761` |
| PR #20 | Open draft; base `develop`; head `docs/full-system-architecture-and-repo-engineering-plan`; head `b6081cafb4df8a4c2b250a0054908bcdd001f3f9` |

PR #17–#20 have no commits behind `develop`; their comparisons against `develop` are respectively 6, 2, 2 and 3 commits ahead. All four have zero issue comments, submitted reviews and review threads at this inspection.

The default-branch tree contains no application source files or application build/test pipeline. The architecture plan's proposed directory structure is a target, not an implemented repository layout.

No PR was merged, closed or retargeted. No branch was created, renamed or deleted. No repository setting or protection was changed. The seven-branch ceiling remains unmet.

## 3. Exact documents inspected

| Document | Branch | Current blob SHA | Status |
|---|---|---|---|
| AI Project Operating Prompt | PR #16 branch | `61059c74d4d20309ff76e055059ab33f381ca4f2` | Proposed repository standard; followed as user instruction |
| Task 03 PRD v0.1 | PR #18 branch | `8b1ca0be04b3f4ad3b543c2f9fc48d46eb37faf8` | Source-preserving working baseline; not accepted |
| Task 04 architecture evaluation v0.1 | PR #18 branch | `abc7b721fae8d4f4adede4dd0bf5d6a32098c5a3` | Source-preserving working baseline plus governance overlay; not accepted |
| Full Product Vision and Capability Blueprint v0.1 | PR #17 branch | `907f359be1198de3a2f550ea40584595ff7fb7f9` | Proposed; not accepted |
| Requirements Traceability Register | PR #19 branch | `d150f00fae3eac86dbae06d7e3dbc6d304c160ba` | Proposed; not accepted |
| Full System Architecture and Repository Engineering Plan v0.1 | PR #20 branch | `91fb02be87b42df51f92106f90fd536a01a5b902` | Proposed; not accepted |
| Accepted ADR-001 through ADR-010 | `main` | Current blobs fetched during this review | Accepted; unchanged |

The previous architecture-plan snapshot in its Section 2.2 cites older PR #16, #17 and #19 document blobs. Those were the versions inspected when that plan was prepared; they are not the current blobs listed above. Preserve the historical snapshot, but use the current references in any subsequent decision or implementation record.

## 4. Source preservation check — Task 03 and Task 04

The original DOCX files in Project Library `/STF app` were reopened and compared with the source portions of the PR #18 Markdown transcriptions.

| Source | Original extracted text | Repository transcription | Review result |
|---|---:|---:|---|
| Task 03 PRD v0.1 | 677 extracted lines | 712 Markdown lines, including governance overlay | No substantive source lines were found missing by a normalized line-presence comparison; repeated page markers and running headers are not reproduced |
| Task 04 architecture evaluation v0.1 | 431 extracted lines | 498 Markdown lines, including governance overlay | No substantive source lines were found missing by a normalized line-presence comparison; repeated page markers and running headers are not reproduced |

The comparison normalized whitespace, bullet glyphs and selected punctuation. It is a source-text completeness check, not proof of identical DOCX layout, table geometry, page breaks or visual rendering. The original DOCX files remain the preserved source artifacts. Neither transcription is accepted as a canonical PRD or architecture baseline.

## 5. Product scope and strategic alignment

### 5.1 Alignment with Task 01 and Task 02

The Blueprint correctly retains the Task 01 charter's full-fledged platform ambition, India-first botanical focus, plant identification as an entry point, scientific provenance, uncertainty, human review and reusable STF infrastructure.

It also respects Task 02's caution against defining the strategy as “better Google Lens”, claiming unverified superiority, or expanding immediately into every biodiversity domain. The Blueprint's exclusion of wildlife identification, crop disease diagnosis, gardening advice, commerce, generic social networking and unrelated conservation programme management is directionally consistent with Task 02.

The Blueprint is particularly strong in explicitly stating that product activity or observation volume alone is not evidence of conservation impact. Any conservation-impact claim requires a separate intervention logic, baseline, outcome measures and evidence.

### 5.2 Important refinement requiring owner decision: shared STF versus Botanica-owned domain

Task 01 lists taxonomy and geography among candidate shared STF infrastructure. The Blueprint refines this boundary:

- Shared STF candidates include identity/access, media infrastructure, reusable geographic primitives, search infrastructure where genuine cross-domain reuse exists, notifications, audit/security/observability, API lifecycle and CI/CD.
- Botanica Indica owns botanical taxonomic names, concepts, treatments and usages; botanical knowledge, identification, evidence, observations, distribution interpretation, source reconciliation and botanical review.

This is a sensible distinction between **shared technical capability** and **domain-specific scientific semantics**, but it is a substantive refinement of the charter and must not be treated as already approved. The proposed ADR-011 is the appropriate place to resolve ownership, interfaces, data stewardship and reuse boundaries. Until then, keep the boundary logical; do not assume separate services, repositories, teams, databases or deployments.

## 6. Blocking consistency finding: capability identifiers

The Blueprint's capability model is internally inconsistent:

1. Section 5 defines **16 capability domains**, numbered 5.1 through 5.16. It separates Botanical Knowledge Profiles from Botanical Knowledge and Taxonomic Intelligence.
2. Section 13 defines only **15 identifiers**, `BI-CAP-01` through `BI-CAP-15`. Its first identifier combines taxonomy and botanical knowledge, and its third identifier is Observations. There is no separate capability ID for Species/Botanical Knowledge Profiles.
3. The RTM defines **16 different identifiers**, `CAP-01` through `CAP-16`, and separates profiles as `CAP-03`. Consequently, the capability sequence shifts from observations onward compared with the Blueprint Section 13 table.
4. The RTM says its identifiers label the Blueprint's capability domains, but it does not provide a complete crosswalk between `BI-CAP` and `CAP` namespaces.

This is a **baseline blocker**, not a cosmetic naming issue. Requirement mappings, architecture ownership, acceptance tests and future implementation work could attach to different domains while appearing to use equivalent identifiers.

**Recommendation:** adopt one Botanica-specific canonical namespace, preferably `BI-CAP-01` through `BI-CAP-16`, aligned one-to-one with Blueprint Sections 5.1–5.16. Preserve the existing IDs in a migration crosswalk; do not silently renumber or discard them. Update the Section 13 table, RTM, acceptance-criteria mappings, architecture crosswalks and any downstream references together. The project owner must approve the canonical scheme before it is treated as stable.

## 7. Requirements traceability assessment

### 7.1 What is already strong

- All **19 original Task 03 functional requirement IDs** are represented in the RTM: ID-001–ID-009, OBS-001–OBS-002, VAL-001–VAL-002, SCI-001–SCI-002, SEC-001–SEC-002, API-001 and OPS-001.
- All **12 Task 03 Section 33 acceptance criteria** are represented in the RTM with proposed AC-001–AC-012 labels and links to requirements, capabilities and evidence.
- The RTM distinguishes original Task 03 IDs from proposed derived requirements and says the derived requirements need owner approval before incorporation into the PRD.
- It marks scientific-model-dependent requirements as blocked or unverified rather than claiming implementation or test completion.
- It preserves the distinction between AI confidence, evidence quality, user contribution, community review, expert determination and scientific verification.
- It correctly states that Task 03 remains the source for original requirements until a revised PRD is accepted.

### 7.2 Gaps to close before baseline acceptance

1. **Non-goals are not first-class traceability guardrails.** Task 03 Section 34 has seven explicit non-goals. The Blueprint discusses them in its Task 03 crosswalk, but the RTM has no controlled scope-exclusion register. Add a register that links each non-goal to its source, rationale, affected capabilities and change authority. This helps prevent scope creep without turning every exclusion into a product feature.
2. **Workflow states need a formal state machine.** The Blueprint crosswalk lists Submitted, AI identified, User confirmed, Community reviewed, Expert reviewed, Scientifically verified, Disputed/requires review and Rejected/invalid. The RTM should link these to explicit state-machine requirements and define actors, authority, allowed transitions, evidence, appeals, publication consequences and audit behavior. These states must not be treated as interchangeable scientific truth labels.
3. **Derived identifier `SCI-001A` is easy to confuse with original `SCI-001`.** Prefer a separate derived-requirement namespace (for example `DER-SCI-001`) and preserve a migration crosswalk. Do not reuse or silently alter the original Task 03 ID.
4. **Capability mappings depend on the Section 6 identifier resolution.** Do not approve RTM capability mappings while the Blueprint and RTM capability namespaces remain inconsistent.
5. **User-data lifecycle requirements need decomposition.** Export, deletion, withdrawal, anonymization, restriction, retention obligations and scientific audit-history preservation are different behaviors. Keep the current legal and data-governance qualification; do not promise universal deletion until the applicable policy and law are reviewed.
6. **Priority is sequencing, not final product scope.** Preserve Task 03's P0/P1/P2/P3 meaning. Lower-priority capabilities remain part of the full product unless the owner formally changes scope.

## 8. Task 04 and accepted ADR alignment

The Task 04 source document is a technology and architecture evaluation, not an approved procurement or deployment decision. Its repository overlay correctly reconciles historical candidate text with the accepted ADR register.

| Topic | Governing accepted decision | Review conclusion |
|---|---|---|
| Mobile | ADR-001: Dart / Flutter | Flutter governs. React Native remains a historical, unselected candidate. |
| Decomposition | ADR-001 and ADR-002 | Modular monolith initially; logical domain boundaries do not require one microservice per domain. |
| Interfaces | ADR-003 | API-first and versioned contracts remain governing principles. |
| Provenance | ADR-004 | Source, version, transformation and relevant rights context must be retained. |
| Taxonomy | ADR-005 | Preserve source-aware, versioned taxonomic treatments and competing assertions; no silent source overwrite. |
| Identification | ADR-006 | Evidence-aware, modular pipeline; candidates and scientific determinations remain distinct. |
| Evidence/review | ADR-007 | Evidence and expert assessment remain distinct but connected; preserve disagreement and history. |
| Geography | ADR-008 | Sensitive locations require end-to-end access/disclosure controls and appropriate precision. |
| Observations | ADR-009 | Observation, identification and contribution are distinct records. |
| Ingestion | ADR-010 | Source identity, provenance and source-specific limitations remain explicit. |

Task 04's historical proposed ADR-001–ADR-012 list conflicts with the current accepted ADR register. Its overlay correctly labels that list as historical source content only. Do not import or reuse those identifiers.

No accepted ADR was changed by this review.

## 9. Architecture assessment

### 9.1 Sound recommendations

The PR #20 plan is directionally consistent with accepted ADRs and the product requirements:

- Modular monolith first; define domain modules, contracts and ownership before service extraction.
- Flutter mobile under ADR-001.
- TypeScript for application/API direction, Python for AI/ML and scientific computing, SQL for relational/spatial data.
- PostgreSQL/PostGIS as a leading candidate, with physical design gated by scientific-model reconciliation.
- Object storage for media, with metadata, rights and lineage in the system of record.
- Search indexes, embeddings, caches and AI outputs as derived/rebuildable representations, not authoritative scientific records.
- OpenSearch remains a candidate; benchmark PostgreSQL-first search and alternatives against botanical names, synonyms, multilingual queries, spatial filtering, relevance and operating cost.
- OIDC/OAuth-compatible identity, OpenTelemetry, OCI packaging and durable asynchronous jobs are candidate patterns, not provider or deployment approvals.
- Kubernetes and independent service deployment are not required by default.
- Rust remains a bounded specialist option only after profiling and comparative evidence; no Rust component or crate is authorized.

### 9.2 Decisions still open

The following must remain open unless separately approved:

- Web framework.
- Identity provider and detailed authorization policy.
- Cloud provider and deployment topology.
- Object-storage provider and exact compatibility contract.
- Queue/event provider and operational model.
- Search provider and vector-search need.
- Monorepo versus multi-repository strategy and code-ownership model.
- Production availability, recovery, latency, scale and cost targets.
- Exact API toolchain and generator/validator compatibility.
- Data retention, offline synchronization, local storage and conflict resolution.

The proposed repository tree should not be created wholesale before the corresponding code, ownership and build/test requirements exist. A proposed directory layout is not implementation progress.

### 9.3 200-line source-file guideline

The PR #20 plan itself recognizes that no universal industry standard establishes a 200-line file limit. Its proposed non-blocking report, reviewer explanation and documented exceptions are safer than a hard build failure.

**Recommendation:** retain 200 non-blank lines only as a soft review prompt. Cohesion, correctness, testability, readability, generated/declarative content and scientific invariants must take precedence. Do not create arbitrary fragmentation or enforce an absolute line-count gate.

## 10. Current authoritative technical reference check

Checked on 21 November 2026. These sources support evaluation; they do not select a vendor or approve the project architecture.

- **Flutter:** the official architecture guide recommends separation of UI and data layers, views/view-models, repositories and services. It describes an optional domain/use-case layer for complex or reused logic, not a requirement to create a use-case for every operation: https://docs.flutter.dev/app-architecture/guide and https://docs.flutter.dev/app-architecture/recommendations
- **OpenAPI:** version 3.2.1 was issued 10 September 2026. It is a suitable current candidate for versioned API contracts, but generator, validator, gateway and client-tool compatibility must be checked before pinning: https://spec.openapis.org/oas/v3.2.1.html
- **PostgreSQL:** the current documentation identifies PostgreSQL 18.7 as the current release on 12 November 2026. The official constraints reference covers primary keys, foreign keys, unique, check and exclusion constraints: https://www.postgresql.org/docs/current/index.htm and https://www.postgresql.org/docs/18/ddl-constraints.html
- **PostGIS:** the official release page reports PostGIS 3.7.0 released 30 October 2026. Geometry and geography have different semantics and performance trade-offs; spatial indexes and query patterns require workload testing: https://www.postgis.net/documentation/getting_started/install_windows/released_versions/ ; https://postgis.net/documentation/faq/geometry-or-geography/ ; https://postgis.net/docs/using_postgis_dbmanagement.html
- **OWASP:** ASVS 5.0.0 is the stable web/API verification baseline. OWASP MASVS v2.1.0 includes a privacy category; select applicable controls and tests through threat modelling. A checklist is not certification: https://asvs.owasp.org/ ; https://github.com/OWASP/masvs/releases
- **TDWG Taxon Concept Standard:** the current TCS List of Terms reports version 2025-12-11. TCS distinguishes Taxon Concept, Taxon Name, Taxon Concept Mapping and Nomenclatural Type. A TCS TaxonConcept requires exactly one `taxonName` and one `accordingTo`; synonym is a relation from a TaxonConcept to a TaxonName, not between two taxonomic entities. The six mapping relations are `isCongruentWith`, `includes`, `isIncludedIn`, `partiallyOverlaps`, `isDisjointFrom` and `intersects`: https://tcs.tdwg.org/terms/
- **Darwin Core DR-09:** current indexed TDWG metadata surfaced 2026-10-13 for the List of Terms and Conceptual Model, while direct opens of the canonical latest pages in this review rendered 2026-05-26. The versioned 2026-10-13 resources were inaccessible through the available browser. This discrepancy is not resolved; keep DR-09 open and compare exact versioned documents and term IRIs before term-level design: https://dwc.tdwg.org/list/ ; https://dwc.tdwg.org/cm/

The TDWG TCS semantics reinforce the need to keep the Task 05 taxonomy model and its DR/LDM review gates authoritative. The architecture plan must not replace those semantics with generic name/concept relationships or use Darwin Core export terms as an unexamined internal schema.

## 11. Recommended decision and remediation sequence

### Gate 1 — Product identity and scope
1. Owner confirms the full-product definition and botanical boundary.
2. Resolve the 16-domain capability map and canonical `BI-CAP` identifier scheme.
3. Record the shared STF technical-platform versus Botanica scientific-domain boundary, aligned with proposed ADR-011.
4. Preserve Task 02 exclusions and create a controlled scope-guardrail register.

### Gate 2 — Requirements baseline
5. Preserve the 19 original Task 03 functional IDs and 12 acceptance criteria.
6. Reconcile the derived requirements, identifier namespace and workflow-state machine.
7. Map each requirement to a capability, architecture responsibility, accepted ADR, validation evidence, rights/privacy implications and owner.
8. Produce one canonical PRD revision only after owner review; retain the original DOCX and v0.1 transcription/history.

### Gate 3 — Architecture baseline
9. Reconcile Task 04 candidates with accepted ADR-001–ADR-010 and the approved requirements.
10. Decide repository topology, module ownership, dependency rules and deployment posture with explicit trade-offs.
11. Keep provider, framework, search, orchestration and production SLO decisions open until measured requirements exist.
12. Preserve a single canonical architecture baseline and decision register; do not treat PR #20 as implementation authorization.

### Gate 4 — Scientific and operational readiness
13. Resolve DR-01–DR-12 and execute or formally disposition LDM-01–LDM-16 with evidence.
14. Obtain qualified botanical, taxonomic, biodiversity-informatics, security/privacy, rights/legal, accessibility and operations review.
15. Keep physical database design and application implementation gated until the relevant scientific, rights, privacy and architecture decisions are accepted.

## 12. Final recommendation

**Do not merge PRs #17–#20 yet.** Keep them as open draft proposals while the capability identifiers, shared-platform boundary, non-goal controls and lifecycle-state traceability are reconciled.

The most important immediate task is a controlled product-baseline reconciliation across PRs #17, #18 and #19. PR #20 should remain a proposed architecture plan until that work and the Task 05 scientific-model gates are sufficiently mature.

This review does not approve any proposal, amend an ADR, accept a PRD, authorize implementation, close DR findings, approve physical database design, or authorize any branch/PR lifecycle action.


## 13. Verification boundary and CI status

- The audit file was re-fetched from the PR #20 head after creation; its content and blob were verified.
- PR #20 now contains two files: the existing full-system architecture plan and this audit report. No other file was changed by this review.
- The PR #20 base branch `develop` does not currently contain `.github/workflows/repository-governance.yml`. That workflow exists on the separate PR #16 branch, so it cannot be claimed as a CI check for PR #20.
- No check runs were returned for the PR #20 audit commit. The audit is therefore **API/readback-verified, not CI-verified**. The previous successful PR #16 governance workflow runs apply only to their own PR #16 commit SHAs and must not be represented as validation of this report.
- No application code, executable product tests, security scans or scientific-model tests were run or claimed.

This review is a desk audit and proposal. Its findings should be independently reviewed by the appropriate product, architecture and scientific reviewers before any owner decision.
