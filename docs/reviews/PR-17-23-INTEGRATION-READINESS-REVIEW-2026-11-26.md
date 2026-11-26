# PR #17–#23 Integration Readiness Review

**Document ID:** STF-BI-INT-REV-001  
**Version:** 0.1 — Adviser-led repository and cross-document review  
**Review date:** 26 November 2026  
**Status:** Proposed review findings; not an approval, merge recommendation or independent specialist sign-off  
**Repository:** Save-Tiger-First/botanica-indica  
**Working branch:** `docs/full-system-architecture-and-repo-engineering-plan` (PR #20)  
**Governing standard:** STF-AI-OPS-001 v1.0, blob `53add3894d0502827e584614c70ad09cadaa637d`, from `docs/repository-audit-and-ai-operating-standard`

---

## 1. Executive conclusion

**Overall conclusion: NOT READY for integration, baseline acceptance, Task 05D pass, physical database design or implementation authorization.**

The current documentation is substantially more coherent than the earlier Task 01–04 working materials. The full-product blueprint, source-preserving Task 03/04 transcriptions, requirements traceability, architecture plan and scientific review pack now provide a useful connected evidence base.

However, these documents remain proposals and are spread across divergent branches. The scientific model is not yet a single internally consistent, executable and independently reviewed logical design. The project also remains materially outside its branch-lifecycle policy.

**Recommendation:** preserve the current workstreams; do not merge, rebase, retarget or delete branches as a shortcut. Complete a bounded content reconciliation and scientific validation sequence on the existing branches, then seek independent reviews and owner decisions. Task 05E must remain blocked.

This report is an adviser-led documentation and repository review. It is not a qualified taxonomic, ecological, biodiversity-informatics, legal, privacy, security or independent maintainer approval.

## 2. What was inspected

### 2.1 Governing prompt and repository

The complete AI Project Operating Prompt was retrieved from the PR #16 branch. Its controlling requirements include:

- exactly three long-lived branches: `main`, `develop`, `staging`;
- no new branches under the current owner directive;
- maximum seven branches total, including temporary branches;
- preserve unique content and provenance before retirement;
- final formal completion leaves only `main`;
- no merge, PR closure, branch deletion, protection change or other irreversible action without authorization;
- scientific-model and physical-schema gates must not be bypassed.

Live repository snapshot on 26 November 2026:

| Item | Verified state |
|---|---|
| Branch count | 23 |
| Open PR count | 19 |
| Open PR state | All 19 are draft |
| Long-lived branches | `main`, `develop`, `staging` |
| `main` | `6f2f51da093caf8183fde386dbec707cc6046d27` |
| `develop` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` |
| `staging` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` |
| Branch ceiling | 7 total; currently exceeded by 16 |

`main` remains one commit ahead of `develop` and `staging`. Its main-only file is the Hortus Malabaricus validation crosswalk. Preserve and reconcile that content; do not reset or overwrite `main`.

### 2.2 Current PR heads

| PR | Workstream | Current head | Base | State |
|---|---|---|---|---|
| #16 | Operating standard / repository governance | `16fd00e0e6719026a9c937c19c7409b13eb35f98` | develop | Open / draft |
| #17 | Full-product capability blueprint | `b66c16355d0ded4f20f1a84172eab8b47d133277` | develop | Open / draft |
| #18 | Task 03/04 source baselines | `4d57b2c390f8c342459fb4310e30ed8d382790b6` | develop | Open / draft |
| #19 | RTM, workflows, acceptance and API/offline proposals | `43d1c909055bbe321f8d9c6b163ae454ec6ac914` | develop | Open / draft |
| #20 | Full architecture and repository engineering | `64664c398dcb74c99cdbb9252d3e41d68d36b17f` | develop | Open / draft |
| #9 | Scientific data model review pack | `08987d8a01b411cb167c16ae0edbf0d914036d06` | main | Open / draft |
| #5 | Task 05C Candidate A | `d443420d6b77815cb155f457ea262e621aabf7cb` | main | Open / draft |
| #11 | Task 05D v3 | `0577250c9e7cffcb3605acc782f403b7d1b422e0` | Candidate A branch | Open / draft |
| #21 | Alternate Task 05C Candidate B | `8d4fef2d726aac79dd684856d924b171e44d0b93` | PR #9 review branch | Open / draft |
| #22 | Earlier Task 05D revision | `3efd80e5e28b2a916e63c85808ef3aba9d35e4ac` | PR #9 review branch | Open / draft |
| #23 | Task 05C/05D v2 revision | `76bd88980bb2536db63bbde76e3fa687503bdda1` | PR #9 review branch | Open / draft |

GitHub's mergeable value is only a transient repository calculation. It is not a review, approval, scientific sign-off or permission to merge.

### 2.3 Review and CI evidence

Submitted review-list checks for PRs #9, #11 and #16–#23 returned no submitted reviews; PR #5's review-list check also returned none. Inline review-thread checks for PRs #9, #11 and #16–#23 returned no threads.

Workflow-run queries for the reviewed product, architecture and scientific workstream branches returned no matching runs. This is not a claim that no workflow has ever run anywhere in the repository; it means no current-head validation evidence was found for these inspected workstream branches in the checks performed.

The PR #16 governance workflow's earlier passing runs do not validate PR #17–#23 documents or scientific semantics.

## 3. Product and requirements integration

### 3.1 What is aligned

- The Full Product Blueprint proposes 16 capability domains, `BI-CAP-01` through `BI-CAP-16`.
- The original Task 03 source remains preserved with 19 functional requirement identifiers, 12 acceptance criteria and 7 non-goals.
- The RTM maps the original Task 03 requirements to proposed capabilities, workflows, ADRs, scientific-model dependencies and test evidence.
- The owner-confirmed ODR-02 boundary is reflected in the Task 03 and Task 04 overlays on PR #18.
- Flutter remains governed by accepted ADR-001; the historical React Native candidate in Task 04 does not override it.
- The architecture retains a modular monolith under ADR-002 rather than turning logical modules into mandatory microservices.

### 3.2 Issues requiring correction before acceptance

**Major — proposed identifiers must not be represented as approved scope.** The `BI-CAP-01`–`BI-CAP-16` namespace is a useful proposed capability map, but it remains proposed until owner acceptance. It supplements rather than replaces the original Task 03 requirement IDs.

**Major — acceptance-test count needs consistent wording.** The current Acceptance Test Plan contains 66 core test cases plus 8 ODR-01 export-validation supplement cases: 74 total, all Proposed / Not run. The RTM and older audit narratives still refer to 66 cases in places. Update the wording consistently to distinguish 66 core cases, 8 supplemental export cases and 74 total. The eight cases are not a thirteenth acceptance criterion.

**Major — full-product acceptance remains incomplete.** The workflow crosswalk identifies gaps for AC-011 (AI model replacement) and AC-012 (future STF biodiversity reuse), and partial coverage for AC-006, AC-008, AC-009 and AC-010. These require additional acceptance cases, not a claim that the 16 workflow scenarios cover the full product.

**Major — source inventory and status need one authoritative refresh.** Historical SHAs in older PR #17–#20 audit sections must remain labelled historical. The current Task 03/04 file blobs changed again on PR #18 when the ODR-02 links were pinned. Use the exact current blobs listed in Section 7 of this report.

## 4. Architecture and domain-boundary review

### 4.1 Strong direction

The proposed architecture is directionally sound:

- Flutter mobile client;
- TypeScript API/application layer;
- Python for scientific computing and AI/ML;
- modular monolith with explicit domain ownership;
- PostgreSQL/PostGIS as leading relational/spatial candidates;
- replaceable search, AI/ML, media and integration adapters;
- derived search indexes, embeddings and caches rather than scientific systems of record.

No microservices, Kubernetes, vector database or additional data platform should be introduced without measured requirements and an explicit decision.

### 4.2 ODR-02 is a logical ownership decision

The owner confirmed that STF owns genuinely reusable platform infrastructure and Botanica Indica owns botanical scientific semantics, records, workflows and scientific authority.

The PR #18 PRD and Task 04 overlays now link directly to the pinned ODR-02 record on PR #20 commit `64664c398dcb74c99cdbb9252d3e41d68d36b17f`. The source Task 03/04 text remains intact.

This does not accept either baseline, approve ADR-011, require separate deployments or change accepted ADR-001–ADR-010.

### 4.3 Architecture remains proposed

PostgreSQL/PostGIS is not a finalized physical database decision. React/Next.js, OpenSearch, object storage provider, identity provider, cloud provider, orchestration and deployment topology remain subject to evaluation. The physical schema gate remains closed.

## 5. Scientific data model — critical findings

### F-01 — BLOCKER: Event, Survey and Occurrence do not yet have one canonical logical representation

Candidate A's earlier ERD and cardinality summary represent Event-to-Occurrence as a contextual one-to-many relationship. Its later Section 18 proposes a shared Event identity with distinct Survey and Occurrence specializations, but explicitly does not supersede the earlier content.

The PR #9 Event–Survey–Occurrence decision paper and EVT materials recommend a shared Event identity/supertype, distinct Survey and Occurrence specializations, a separate Observation workflow record and separate relationships for:
- Event parent/child containment;
- Survey-to-Occurrence reporting;
- Observation-to-Event association;
- Observation-to-Occurrence evidence.

This is the preferred review hypothesis, not an approved schema. One coherent ERD, textual cardinalities and executable positive/negative fixtures are required.

### F-02 — BLOCKER: SurveyTargetAssessment and SurveyTargetResult responsibilities overlap

Task 05B and Candidate A use `SurveyTargetResult`; EVT materials use `SurveyTargetAssessment`. Their current definitions overlap with the Occurrence-level detected/non-detected state.

The preferred review direction is:
- SurveyTarget declares what was sought or later selected for analysis, retaining a priori/post-facto origin and scope;
- SurveyTargetAssessment records the bounded assessment process, protocol, effort, coverage, completeness, limitations, agent and provenance;
- taxonomic/organismal outcomes use the authoritative Occurrence-level scientific record and a typed SurveyOccurrenceReport relationship;
- non-occurrence targets (e.g. environmental conditions or habitat measurements) need a typed attributable assertion/measurement route, not a fabricated Occurrence.

This is not an approved entity design. Do not allow two independently mutable outcome states for the same assessment.

### F-03 — BLOCKER: IdentificationSubject total participation is not proven

Candidate A's proposed row-local CHECK can enforce exactly one target foreign key within a populated IdentificationSubject row. It does not alone guarantee every Identification has a subject row. A relational/transaction-safe enforcement strategy and negative tests are required. PostgreSQL's constraints guidance cautions that CHECK constraints cannot safely enforce cross-table conditions.

### F-04 — MAJOR: DR-09 is partially clarified, not closed

The current PR #9 independent validation review records the 2026-10-13 Darwin Core Conceptual Model/List metadata and later Humboldt term metadata. It also records that the exact 2026-10-13 Humboldt term-list page and exact `isTaxonomicScopeFullyReported-2026-10-13` resource were not directly retrieved in that review.

Pin exact versioned resources and individual term IRIs, retrieve their definitions/status, and compare them with the selected GBIF export profile. Keep DR-09 open until reproducible evidence is archived. Do not treat a landing-page issue date, vocabulary snapshot date and individual term-version date as interchangeable.

### F-05 — MAJOR: ODR-01 remains export-only

The owner-authorized ODR-01 interpretation applies only to controlled, profile-specific external exports. It does not authorize internal absence inference from missing rows and does not create an internal negative Occurrence.

Missing, ambiguous, contradictory or unvalidated scope/completeness/provenance/mapping evidence must fail closed. Explicit internal non-detection must be attributable and survey-bounded. Do not equate non-detection with biological absence.

### F-06 — MAJOR: DR-08 remains a source/geographic-scope comparison

The Mango native/introduced example is not established as a direct source contradiction. Normalize taxonomic concepts, geographic units, time periods and source purposes before deciding whether claims conflict.

### F-07 — MAJOR: proposed test cases are not execution evidence

LDM-01–LDM-16, FLD scenarios and EVT-27–EVT-44 remain validation obligations. The 74 Task 03 acceptance-test cases remain Proposed / Not run. No scientific test run or independent reviewer disposition was found in the inspected evidence.

### F-08 — MAJOR: specialist review remains absent

The scientific review register requires qualified review across taxonomy, herbarium/collections, biodiversity informatics, field ecology, geospatial controls, rights/legal, privacy/security and database architecture. No submitted PR reviews were found on PR #5, #9, #11 or #21–#23. The existing desk reviews are not independent discipline sign-off.

### F-09 — MAJOR: v1/v2 validation documents contain stale dispositions

Task 05D v2 contains a DR-09 “Withdrawn as erroneous” statement. The current Task 05D v3 and PR #9 scientific review register retain DR-09 as open. Do not carry the v2 closure statement into the current baseline. Preserve v2 as historical evidence and use the current v3/PR #9 review record for the active disposition.

## 6. Scientific-model branch dependency and preservation

Live comparisons show:

- PR #11 Task 05D v3 is **7 commits ahead and 4 behind** the current Candidate A branch; the branches are diverged.
- PR #21 Candidate B contains one unique 647-line Task 05C document and is **1 commit ahead / 88 behind** the current PR #9 review branch.
- PR #22 contains a Task 05C document and earlier Task 05D document; it is **7 ahead / 88 behind** PR #9.
- PR #23 contains a different Task 05C and Task 05D v2 revision; it is **7 ahead / 88 behind** PR #9.

The PR #22 and PR #23 Task 05D files are not byte-identical; the Task 05C copies are also different. Their unique content and decision provenance must be reviewed. Do not delete them or label them duplicate solely by filename or approximate length.

The appropriate route is a section-by-section semantic reconciliation on the existing PR #9 review branch, preserving each source revision, unique finding, and rejected alternative. This report does not authorize merging PR #21–#23 or PR #11.

## 7. Exact source revisions re-fetched for this review

| Artifact | Branch | Current blob SHA |
|---|---|---|
| Task 03 PRD with ODR-02 link | `docs/canonical-task-03-04-baselines` | `b92b0b74db7a02081da05713b88b9a9062a1964c` |
| Task 04 architecture with ODR-02 link | `docs/canonical-task-03-04-baselines` | `d3ac9c9eecc818b53ca85a667adc7898c2b47c7a` |
| Full Product Blueprint | `docs/full-product-vision-capability-blueprint` | `d3ec150524dda4928503f43556a97cd766b71312` |
| Requirements Traceability Register | `docs/requirements-traceability-register` | `fbf938235f686c7e2a9959a179a3a1a57ca6c632` |
| Acceptance Test Plan v0.2 | `docs/requirements-traceability-register` | `87385b0aa7d96bc14d969c5697318bd2590af5fc` |
| Workflow-to-Requirements Crosswalk v0.2 | `docs/requirements-traceability-register` | `61d2111ace5c408eaf503bdf17b2ccb822f90978` |
| Task 05C Candidate A | `docs/task-05c-logical-data-model` | `b447796e7da0d08d96400812667a8e67e0696144` |
| Task 05C Candidate B | `docs/task-05c-logical-database-model` | `239d7e9974bcb81b1154b54845a7b2d69c3775d6` |
| Task 05D v3 | `docs/task-05d-logical-model-validation-v3` | `0b9a009b1c543b2450758f659c97cae3802a2f94` |
| Scientific Data Model Validation Matrix / Decision Register | `review/scientific-data-model-review-pack` | `3a33dfe47657a96456f56f2c12a0b7d355b6c6a5` |
| Task 05D Independent Desk Validation Review | `review/scientific-data-model-review-pack` | `a9e2c50c30eb4da1993a7522797c59b1fd799654` |
| Event–Survey–Occurrence Recommendation | `review/scientific-data-model-review-pack` | `29e72d4d4e0b25d52ca61bb1ba2a9e5a6ee0dd37` |

These are current file blobs at the stated refs as fetched during this review; they are not approvals.

## 8. Prioritized remediation sequence

1. **Freeze the source inventory for this review.** Keep historical revisions and exact SHAs; do not rewrite history.
2. **Reconcile Task 05C Candidate A.** Resolve the Event identity/specialization representation, assessment/outcome ownership, relationship cardinalities and IdentificationSubject total participation. Preserve Candidate B's unique useful material in the review record.
3. **Reconcile Task 05D v3.** Align its exact source inventory to the current Candidate A and Task 05B files; correct stale historical DR-09 disposition references; define test oracles for each blocking decision.
4. **Pin standards evidence.** Archive exact TDWG Conceptual Model, Darwin Core List, Humboldt term resources, relevant term IRIs and the selected GBIF export profile. Keep DR-09 open until this is reproducible.
5. **Complete the product traceability corrections.** Clarify 66 core + 8 supplemental = 74 proposed tests; add missing AC-011/AC-012 acceptance coverage and fill partial AC-006/008/009/010 coverage.
6. **Prepare synthetic executable fixtures.** Keep them clearly synthetic, with expected graphs, negative tests, test environment, actual outputs and reproducible evidence. Do not represent test designs as executed tests.
7. **Obtain discipline-specific reviews.** Record reviewer identity, competence, scope, conflicts, date, findings and disposition. No silent consensus or invented reviewer approval.
8. **Seek owner acceptance of connected baselines.** Review the Blueprint, Task 03 PRD, Task 04 architecture, RTM and acceptance plan as one connected product baseline; separately decide Task 05C/05D only after scientific review.
9. **Only after the scientific gate passes**, prepare Task 05E and a PostgreSQL/PostGIS physical design evaluation. Do not start DDL/migrations before that decision.
10. **Run a preservation-first branch integration plan.** Keep the exact three long-lived branches; reduce to seven total only after source content, dependent PRs and unique history are preserved and explicit authorization is obtained.

## 9. What this review did and did not do

### Completed

- Retrieved the complete governing operating prompt from the required PR #16 branch.
- Re-fetched live branches, PRs, refs and current PR heads.
- Inspected changed-file lists for PRs #1–#5, #8–#9, #11–#14 and #16–#23.
- Inspected the current product blueprint, PRD, Task 04, RTM, acceptance plan, workflow crosswalk and architecture plan.
- Inspected Candidate A, Candidate B, Task 05D v2/v3, the scientific validation register, Event–Survey–Occurrence recommendation and Task 05D desk validation review.
- Compared the relevant branch histories and preserved the current divergence findings.
- Recorded a bounded ODR-02 cross-branch link correction on PR #18 (no source wording or requirement was changed).

### Not performed

- No PR was merged, closed or retargeted.
- No branch was created or deleted.
- No repository protection, permission, billing or Copilot account setting was changed.
- No accepted ADR was amended.
- No product requirement was accepted or removed.
- No scientific model was approved.
- No independent scientific, legal, privacy, security or institutional sign-off was obtained.
- No test was executed.
- No physical schema, SQL/DDL, migration, API implementation or application code was produced.
- No external party was contacted.

## 10. Authoritative source register

The current scientific review references the following primary sources; re-fetch exact versioned artifacts before closing DR-09 or freezing an export mapping:

1. TDWG, Darwin Core Conceptual Model, version 2026-10-13: https://dwc.tdwg.org/cm/ and http://rs.tdwg.org/dwc/doc/cm/2026-10-13
2. TDWG, Darwin Core List of Terms: https://dwc.tdwg.org/list/
3. TDWG, core Darwin Core term metadata: https://rs.tdwg.org/dwc/terms.htm
4. TDWG, Humboldt Extension term metadata: https://rs.tdwg.org/eco/terms.htm
5. TDWG, hierarchical-event guidance, version 2026-10-13: https://dwc.tdwg.org/hierarchy/
6. GBIF, Guide for publishing biological survey and monitoring data, v1.0.2 (2025-09-24): https://docs.gbif.org/guide-publishing-survey-data/en/
7. GBIF, Data Quality Recommendations: https://techdocs.gbif.org/en/data-publishing/data-quality-recommendations
8. TDWG, Taxon Concept Standard terms (version 2025-12-11): https://tcs.tdwg.org/terms/
9. PostgreSQL, Constraints documentation: https://www.postgresql.org/docs/current/ddl-constraints.html

**Closing status:** PRs #17–#23 remain open/draft. Product and architecture baselines remain proposed. Task 05C remains unapproved. Task 05D remains not passed. Task 05E and physical schema design remain not ready. The repository remains at 23 branches against the seven-branch ceiling.
