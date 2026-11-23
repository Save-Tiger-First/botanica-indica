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


## 14. Follow-up reconciliation completed — 21 November 2026

The initial capability-identifier blocker in Section 6 has been addressed at the **proposed-document level** through source-preserving updates on the two existing product workstream branches. This resolves the direct inconsistency between the current Blueprint and RTM working copies; it does not constitute owner approval or acceptance of either document.

### 14.1 Current reconciled document revisions

| Document | Existing branch / PR | Latest commit | Latest blob SHA | State |
|---|---|---|---|---|
| Full Product Vision and Capability Blueprint v0.2 | `docs/full-product-vision-capability-blueprint` / PR #17 | `d07bf52e0c6d4fd5c089e828b0f5b9af33dcd300` | `905455233d11fc750ba3a485d5c516e01f8426ee` | Proposed; open draft |
| Requirements Traceability Register v0.2 | `docs/requirements-traceability-register` / PR #19 | `d2277d3680f828ada403632a4f30ea4e9b940f90` | `5f6862d6ece8d428714588daff54992ccaabfdf2` | Proposed; open draft |

Both revisions were fetched back from GitHub and their blob SHAs matched the write results. PR #17 and PR #19 remain open drafts, based on `develop`, with no commits behind `develop`; the GitHub API reported both as mergeable/clean at the last check. Neither has review submissions, review threads or issue comments. No check runs were returned for either head commit. Mergeability is not approval.

### 14.2 Capability map reconciliation

- Both documents now contain the same **16 unique proposed canonical identifiers**, `BI-CAP-01` through `BI-CAP-16`.
- The identifiers follow Blueprint Sections 5.1–5.16 one-to-one.
- The Blueprint's earlier 15-ID table is preserved as a historical crosswalk. Its former combined taxonomy/profile scope is explicitly split between `BI-CAP-01` (underlying taxonomy and source-attributed botanical knowledge assertions) and `BI-CAP-03` (user-facing botanical knowledge profile synthesis).
- The RTM's former `CAP-01`–`CAP-16` IDs are preserved as legacy aliases and mapped one-to-one to the new `BI-CAP` namespace.
- RTM capability references are now fully qualified; no abbreviated comma-list references remain.
- Blueprint Sections 5.1 and 5.3 now clarify that the first owns underlying source-attributed taxonomic/botanical assertions and structured diagnostic attributes, while the third owns the user-facing synthesis and organization of those records. This avoids creating a second taxonomic authority.

### 14.3 Derived requirement and scope guardrails

- Original Task 03 functional requirement IDs and priorities remain unchanged.
- The RTM's former derived identifier `SCI-001A` is now `DER-SCI-001`; the former label is retained as a legacy alias. The original `SCI-001` remains unchanged.
- Task 03 Section 34's seven explicit non-goals are transcribed as `NG-01`–`NG-07` scope guardrails in the RTM. They are not converted into feature requirements or permanent prohibitions. Any future change requires explicit owner approval and relevant product/requirements review.
- The Task 03 and Task 04 source documents were not modified.
- Accepted ADR-001–ADR-010 were not modified. Proposed ADR-011 remains proposed and is not treated as an accepted boundary decision.

### 14.4 Remaining product-baseline gaps

1. The project owner has not yet approved the proposed 16-domain map, the new namespace or either document as a canonical baseline.
2. The lifecycle-state machine remains an explicit gap. Allowed transitions, actors/authority, evidence requirements, appeals/corrections, withdrawal/restriction, publication effects and audit rules remain to be specified and approved. The documents do not invent transition rules.
3. Derived requirements still require overlap/duplication review during canonical PRD revision.
4. Task 04 architecture has not yet been fully crosswalked to the reconciled 16-domain namespace; this should follow owner review of the product map and the shared STF/Botanica boundary.
5. Task 05 DR-01–DR-12 and LDM-01–LDM-16 gates remain open or subject to validation. No physical database design or implementation readiness is conferred.

### 14.5 Verification and action boundary

The two updated files were read back from GitHub and checked for:
- all 16 unique `BI-CAP` identifiers in each document;
- 16 capability rows in each capability table;
- the seven Task 03 non-goal guardrails in the RTM;
- the legacy capability crosswalks;
- the derived requirement identifier and original Task 03 requirement IDs;
- the updated source blob SHA in the RTM.

These are document/readback consistency checks, not CI, application tests, scientific validation, legal review or independent expert approval.

No PR was merged, closed or retargeted. No branch was created, renamed or deleted. No repository setting, protection or permission was changed. The 23-branch count and seven-branch ceiling remain unchanged.

 
## 15. Review of September 2026 research and planning materials — 21 November 2026

### 15.1 Material inspected

Four uploaded working documents, all named `Create Master Checklist.txt`, were reviewed in full/available continuation ranges:
1. Save Tiger First Master Project Checklist (15 September 2026).
2. Task 01 — Project Charter v0.1 (15 September 2026).
3. Task 02 — Problem & Opportunity Analysis (September 2026).
4. Architecture, UI/UX and effort-estimation study (15 September 2026).

They are working research/planning material, not approved repository baselines. Their useful concepts are largely represented in the proposed Full Product Vision (PR #17), Task 03/04 source-preserving baselines (PR #18), RTM (PR #19) and full architecture plan (PR #20). No duplicate Task 01/02 document was created in this review.

### 15.2 Findings and required treatment

| Topic | Assessment | Recommended treatment |
|---|---|---|
| India-first botanical intelligence | Strong strategic direction; broader and more defensible than “Indian Google Lens” | Retain as product hypothesis, with measurable evidence and no unsupported superiority claim |
| Evidence Engine | Strong first-class capability; photo guidance, morphology, organ, geography, taxonomy and abstention matter | Keep confidence/probability, evidence quality, taxonomic support, geographic plausibility and expert determination as distinct dimensions; do not create one universal Evidence Score |
| Community/data flywheel | Strategically promising, but not automatic | User contributions are not automatically eligible for redistribution, derivative use or AI training; rights, consent, attribution, provenance and review are purpose-specific |
| Shared STF platform | Useful direction, but over-generalization risk | Apply proposed PR #17 boundary and ADR governance; keep domain ownership in Botanica Indica; do not create one microservice per capability |
| Competitive star table | Subjective, no common benchmark or sampling protocol | Do not use as factual ranking or public claim; build a reproducible India-relevant benchmark |
| 4,250–5,850 person-hour estimate | Early order-of-magnitude estimate only | Do not treat as budget, staffing commitment or schedule; bottom-up re-estimate after approved scope and workload/cost assumptions |
| Legacy task numbering | Conflicts with current repository numbering | Use current repository Task 03 PRD, Task 04 System Architecture & Technology Evaluation and Task 05 Data Architecture; crosswalk older checklist items rather than create duplicate tasks |

### 15.3 Updated external research

- **Pl@ntNet:** current official API documentation supports up to five images of the same individual, plant-organ inputs, project/flora-specific identification and ranked candidate results. Its current API landing page reports 87,000+ identifiable species and 62 languages. These are provider-reported, dynamic platform metrics, not independent India-specific accuracy evidence. Sources: https://my.plantnet.org/doc/api/identify and https://my.plantnet.org/
- **Flora Incognita / iNaturalist:** a May 2026 Alberta plot-survey study using 5,291 images of 119 species in 54 plots reported 79.2% species and 88.4% genus accuracy for Flora Incognita, and 66.5% species and 73.7% genus accuracy for iNaturalist. This is a specific Alberta study, not a prediction of India performance. It supports stratified field evaluation and attention to reproductive structures, growth form and image quality. Source: https://doi.org/10.1093/aobpla/plag020
- **eFlora of India:** its own About page describes a community-developed resource and warns that identification errors cannot be ruled out. Its copyright page says original text is CC BY, but member photographs remain the intellectual property of individual authors and require author permission for reuse. Do not bulk-scrape or use images for training without asset-specific permission. Sources: https://efloraofindia.com/efi/about/ and https://efloraofindia.com/efi/copyrights-permissions-credits-etc/
- **Botanical Survey of India:** the official mandate includes National, State and District Floras and development of national plant/herbarium databases. This does not establish an open API or blanket reuse rights for every publication, image or specimen record. Source: https://bsi.gov.in/page/en/Mandate
- **Plantix:** its own research page reports 150M+ field images and says research access is collaboration-based and the raw corpus is not sold. It is a crop-health data feedback-loop example, not an open botanical training set or plant-species-ID benchmark. Source: https://plantix.net/en/plantix-intelligence/research/

Portal statistics and source availability change. The India Biodiversity Portal and other Indian biodiversity platforms should be treated as complementary infrastructures, with dataset-, record- and asset-level rights checks rather than assumptions based on public access or a portal-wide “open data” statement.

### 15.4 Darwin Core / Humboldt version correction

The previous shorthand that treated the Darwin Core List document, core vocabulary snapshot and Conceptual Model as one 2026-10-13 release is inaccurate:
- Conceptual Model: current official indexed metadata reports 2026-10-13; direct HTML rendering remained cached at 2026-05-26; exact versioned document retrieval remains open.
- List of Terms document: direct official page reports 2026-05-26.
- Core `dwc:` vocabulary snapshot: official metadata reports 2026-10-13.
- `dwc:occurrenceStatus`: term version 2026-05-26; recommended literal values `detected` and `notDetected`.
- Humboldt hierarchy guidance: v2024-02-28, Section 3 normative.
- Humboldt Extension terms have their own term-version dates; `eco:isTaxonomicScopeFullyReported`, `eco:isSurveyTargetFullyReported`, `eco:taxonCompletenessReported` and `eco:taxonCompletenessProtocols` must not be conflated. Relevant 2026-10-13 term/value versions exist; pin each exact IRI for mapping.

DR-09 remains open for exact versioned-resource retrieval and term-by-term comparison. Sources: https://dwc.tdwg.org/cm/ ; https://dwc.tdwg.org/list/ ; https://rs.tdwg.org/dwc/terms.htm ; https://eco.tdwg.org/hierarchy/ ; https://rs.tdwg.org/eco/terms.htm ; https://rs.tdwg.org/ecotcr/version/values/2026-10-13.htm

### 15.5 Status boundary

This is a desk-research and source-reconciliation update. It does not approve a product baseline, Task 04 technology, vendor, data source ingestion, image rights, budget, staffing, PR, Task 05C candidate, physical schema or implementation. No independent specialist review or application test is claimed.

 
## 16. Candidate A reconciliation proposal and stacked Task 05D dependency — 21 November 2026

A source-preserving proposed reconciliation section was appended to Candidate A:
- `docs/architecture/TASK-05C-LOGICAL-DATABASE-MODEL.md`
- Branch `docs/task-05c-logical-data-model`, PR #5
- Commit `ded43eea96bcaf1cb57c0689ff2b2217da2f9764`
- Blob `2efc627683182b370fb11ab14e056aa31f894180`
- Section 18, Event–Survey–Occurrence reconciliation proposal.

This is a proposal only. It does not approve Candidate A or B, change accepted ADRs, authorize physical schema or implementation, or close DR/B/LDM/EVT findings.

The proposal recommends Candidate A as the starting document for its stronger typed relationship and provenance treatment, selectively incorporating Candidate B workflow/cardinality strengths. It proposes a shared Event identity with distinct Survey and Occurrence specializations; Observation remains a separate contributor/workflow record; SurveyTarget/SurveyTargetResult and SurveyOccurrenceReport are explicit; Event hierarchy remains separate from Survey reporting.

**PR #11 dependency status:** after Candidate A moved, comparison of base `docs/task-05c-logical-data-model` and head `docs/task-05d-logical-model-validation-v3` is `diverged`, **3 commits ahead / 2 behind**, merge base `91c82b4f136a77aaa1edb02753ed49b2fbee86ed`. PR #11 must not be merged/rebased/retargeted blindly. A full diff and reviewed synchronization plan are required.

No PR or branch lifecycle action was taken. The 23-branch count and 20-open-PR count remain unchanged.

 
## 17. Task 05B/05C/05D scientific-model reconciliation update — 21 November 2026

A further append-only consistency pass was completed across the existing scientific-model branches:

| Document | Branch / PR | Commit | Verified blob | Change |
|---|---|---|---|---|
| Task 05C Candidate A | `docs/task-05c-logical-data-model` / PR #5 | `98741843a2ba8550e2cb744658d9291fe60b8823` | `c8bddcdfda9f76f03afd389ff9c5a307b89bd906` | §19 standards-version and Event/Survey/Occurrence term correction |
| Task 05B Scientific Data Dictionary | `docs/task-05-data-dictionary` / PR #4 | `8936fe87a2c32da861c7f6a08d52603c9e545d21` | `b6827f8149313f0e70ac6a8873108aae509eb785` | §16 Event/Survey/Occurrence and SurveyTarget/SurveyTargetResult clarification |
| Task 05D v3 | `docs/task-05d-logical-model-validation-v3` / PR #11 | `9d383c4206f2d48bd31b04c6ebb5bd97bf7b87df` | `27a12b960d84b504fe915da4681d2f2511bdb086` | §14 current standards correction and synthetic EVT-34–EVT-44 fixtures |

These updates preserve earlier content and remain proposals. No fixture was executed; no independent specialist sign-off was obtained; no ADR or accepted scientific model was changed.

The exact current TDWG indexed metadata reports 2026-10-13 for the Conceptual Model, List of Terms, core term snapshot and hierarchy guide. However, the public Conceptual Model and List HTML renderers still returned 2026-05-26 during the review. DR-09 therefore remains open for exact versioned-resource capture and comparison. Individual terms have independent versions, including `dwc:occurrenceStatus-2026-05-26`, `eco:isTaxonomicScopeFullyReported-2026-10-13`, `eco:isSurveyTargetFullyReported-2026-05-26`, and the current 2026-10-13 sampling-effort/completeness-method term versions.

**PR #11 remains a stacked dependency.** Candidate A and Task 05D v3 remain diverged; do not merge, rebase or retarget automatically. The current compare baseline must be refreshed before any dependency synchronization proposal. The seven-branch ceiling remains unmet; no branch or PR lifecycle action was taken.

 
## 18. Latest Task 05D dependency comparison — 21 November 2026

After the latest append-only updates, GitHub compare reports Candidate A `docs/task-05c-logical-data-model` as base and Task 05D v3 `docs/task-05d-logical-model-validation-v3` as head: **diverged, 4 commits ahead / 3 commits behind**, merge base `91c82b4f136a77aaa1edb02753ed49b2fbee86ed`. PR #11 remains open/draft, based on Candidate A.

Current document commits:
- Task 05B PR #4: `8936fe87a2c32da861c7f6a08d52603c9e545d21`.
- Candidate A PR #5: `98741843a2ba8550e2cb744658d9291fe60b8823`.
- Task 05D v3 PR #11: `9d383c4206f2d48bd31b04c6ebb5bd97bf7b87df`.

The divergence is a commit-history relationship and does not by itself prove a content conflict. PR #11's current changed-file view is the Task 05D document. No merge, rebase, retarget, force-push or branch deletion was performed. Before a PR decision, review the complete commit graph and three-way file/content relationship and prepare a preservation-first synchronization plan for owner approval.

 
## 19. Final refreshed Task 05D comparison — 21 November 2026

After the Task 05D section-numbering correction, the latest branch comparison is:
- Base: `docs/task-05c-logical-data-model`, commit `98741843a2ba8550e2cb744658d9291fe60b8823`.
- Head: `docs/task-05d-logical-model-validation-v3`, PR #11 head commit `9d4ca85c553ef5732334322be7f598ed748d285c`.
- Status: **diverged; 6 commits ahead / 3 commits behind**.
- Merge base: `91c82b4f136a77aaa1edb02753ed49b2fbee86ed`.
- PR #11 remains open/draft and based on Candidate A. The changed-file view remains the Task 05D validation document.

The increase in ahead count reflects additional Task 05D documentation commits on the existing head branch. It does not by itself establish a content conflict. No rebase, retarget, merge, force-push or branch lifecycle action was performed. Full commit-graph and content review remains a prerequisite to any proposed synchronization.


## 20. PR #17–#20 static integration rehearsal and PR #9 mergeability investigation — 23 November 2026

**Status:** Read-only integration rehearsal and mergeability diagnosis, recorded append-only. No PR was merged, closed or retargeted. No branch was created, deleted or renamed. No scientific or product decision was approved.

### 20.1 Governing baseline and repository snapshot

The complete AI Project Operating Prompt was re-fetched from `docs/repository-audit-and-ai-operating-standard`, blob SHA `53add3894d0502827e584614c70ad09cadaa637d`. PR #16 remains open, draft and unmerged; this branch version remains the governing working prompt.

The repository has 23 branches: `main`, `develop`, `staging` and 20 temporary/workstream branches. This exceeds the owner-authorized seven-branch ceiling by 16. No new branch was created for this rehearsal.

Long-lived branch tips at this check:
- `main`: `6f2f51da093caf8183fde386dbec707cc6046d27`
- `develop`: `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`
- `staging`: `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`

The main-only Hortus crosswalk must be preserved; do not reset `main` to `develop`.

### 20.2 Current PR #17–#20 metadata

All four PRs are open drafts, based on `develop` at `f165ecb9b4d9de115c02327cf779982b7ef4bbd4), and were reported individually mergeable at this check.

| PR | Head branch | Head SHA | Commits | Changed files | Individual mergeability |
|---|---|---|---:|---:|---|
| #17 | `docs/full-product-vision-capability-blueprint` | `b66c16355d0ded4f20f1a84172eab8b47d133277` | 9 | 1 | Mergeable into develop |
| #18 | `docs/canonical-task-03-04-baselines` | `0f908f8221ad3434cc84fe2cd41b735aad0a752a` | 2 | 2 | Mergeable into develop |
| #19 | `docs/requirements-traceability-register` | `58f31a510029685d9c3447d22ec5e2a499aa13c6` | 56 | 8 | Mergeable into develop |
| #20 | `docs/full-system-architecture-and-repo-engineering-plan` | `30c07fe496fbc229933ec13ad22662e861d5927e` | 30 | 4 | Mergeable into develop |

Current file blobs re-fetched:
- Blueprint (PR #17): `d3ec150524dda4928503f43556a97cd766b71312`.
- Task 03 PRD (PR #18): `8b1ca0be04b3f4ad3b543c2f9fc48d46eb37faf8`.
- Task 04 architecture evaluation (PR #18): `abc7b721fae8d4f4adede4dd0bf5d6a32098c5a3`.
- Requirements Traceability Register v0.3 (PR #19): `95bcf2161f917b8ff824e8a075a908b090a880c7`.
- Full System Architecture Plan v0.2 (PR #20): `bcba1d052a27d7f56cc46f74f9ba87b41025bdce`.

### 20.3 Static integration rehearsal — PRs #17–#20

The branch comparisons show all four task branches diverged from the same `develop` ancestor. Comparisons of PR #18, #17 and #19 against PR #20 each report the expected source-only document additions; no changed path overlaps were found among PRs #17–#20.

| Source workstream | Files introduced | Path collision with PR #20 |
|---|---:|---|
| PR #18 — source-preserving Task 03/04 baselines | 2 | None found |
| PR #17 — Full Product Blueprint | 1 | None found |
| PR #19 — RTM and supporting specifications | 8 | None found |

**Path-level rehearsal result: PASS.** The checked changed-file inventories do not show direct path collisions among PRs #17–#20.

**Semantic integration result: CONDITIONAL.** The files are related and must be reviewed together:
1. PR #18 preserves the original Task 03 and Task 04 source text. The historical React Native candidate in Task 04 is explicitly unselected; accepted ADR-001 and the Blueprint/PR #20 plan retain Dart/Flutter. Do not rewrite the source transcription to erase history or let it override ADR-001.
2. PR #17 defines 16 proposed capability domains and explicitly preserves the full-product scope. The identifiers remain proposed until owner acceptance.
3. PR #19 maps the original Task 03 requirement IDs and proposed capability IDs to architecture, workflows and validation evidence. Its lifecycle, API and offline documents remain proposals, not approved contracts.
4. PR #20 provides the architecture destination and retains the physical-schema gate pending scientific-model approval.

**Recommended integration order remains:** PR #18 → PR #17 → PR #19 into the existing PR #20 branch, with a full readback and cross-document check after each step. This is a proposed sequence, not a completed integration.

**Important limitation:** GitHub's `mergeable` field reports a test merge of an individual PR into that PR's base branch; it does not test merging one diverged task branch into another. GitHub documents this behavior at https://docs.github.com/en/rest/pulls/pulls. The repository comparison API compares refs and changed files, but does not by itself execute the proposed branch-to-branch merge; see https://docs.github.com/en/rest/commits/commits#compare-two-commits. No actual merge simulation or merge commit was performed. A true rehearsal would require a temporary integration ref/worktree or an authorized update to an existing branch. The current no-new-branches directive and lack of merge authorization mean this audit stops at static path/dependency analysis.

### 20.4 Review and automated-validation status

At this check, PRs #17–#20 each had zero submitted reviews and zero inline review threads. Their current head commits returned no combined status contexts and no workflow runs through the available GitHub endpoints.

This means no independent review or CI pass can be claimed from the inspected evidence. It does not prove that no off-platform review exists; none was supplied in the repository records inspected here.

### 20.5 PR #9 — concrete mergeability finding

PR #9 remains open/draft and is currently reported non-mergeable. Its base is `main`; its head is `review/scientific-data-model-review-pack` at `51b909accbf052426678969d0a28408356133e61`. The comparison against `main` is diverged, 67 commits ahead and 1 behind, with common ancestor `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`.

A concrete same-path divergence was found:
- `main` contains `docs/reviews/HORTUS-MALABARICUS-VALIDATION-CROSSWALK.md`, blob `a3758743e090121a31cda9e6876f43ceb3caa3a0`.
- PR #9's review branch contains the same path, blob `6b7fd454795607b3e93cc590e7ffa562884c0a9e`.
- Both versions contain 188 lines, but their contents differ materially. Each side has content not present in the other.
- The other seven PR #9 changed paths are review-pack documents; this crosswalk is the identified same-path collision with the main-only commit.

**Assessment:** This independently added, divergent same-path file is a concrete add/add collision and is the leading explanation for PR #9's non-mergeable status. The connector did not expose GitHub's detailed merge-conflict reason, so the exact merge-state cause is not asserted as conclusively diagnosed.

**Recommendation:** reconcile the two crosswalk versions into one source-aware canonical document on the existing PR #9 branch, preserving unique content and provenance from both. Re-fetch the main and review-branch blobs immediately before that work. Then re-check PR #9's mergeability and complete diff. Do not delete or overwrite the main-only crosswalk, and do not merge, retarget or close PR #9 without explicit authorization.

PR #9 also has zero submitted reviews and zero inline review threads. Its scientific review pack remains a review instrument, not independent expert approval.

### 20.6 Branch-inventory freshness

The existing Branch Inventory and Preservation-First Consolidation Register on `governance/branch-lifecycle-policy` was re-fetched at blob `9233910471f0806435cb39c47ff074e90d382e47`. Its audit date is 20 November 2026. It remains useful for proposed dispositions but is not a current 23 November PR/branch snapshot. Refresh it before any branch retirement, PR retargeting or consolidation action.

### 20.7 Decision and action boundary

- PR #17–#20 path-level integration rehearsal: completed, static only.
- Actual branch-to-branch merge simulation: not performed.
- PR #9 same-path crosswalk divergence: identified; canonical reconciliation still required.
- No PR was merged, closed, retargeted or marked ready.
- No branch was created, deleted or renamed.
- No repository ruleset, protection or permission was changed.
- No accepted ADR, product requirement or scientific model was changed.
- No physical schema, application code or production implementation was started.
- No scientific, legal or institutional expert approval is claimed.

**Next gate:** reconcile PR #9's two crosswalk versions, then obtain the required independent review of PRs #17–#20 and prepare a genuinely tested integration rehearsal without violating the seven-branch ceiling or performing an unauthorized merge.
