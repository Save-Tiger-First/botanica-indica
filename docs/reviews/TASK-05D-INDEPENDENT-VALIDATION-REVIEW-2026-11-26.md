# Task 05D — Independent Desk Validation Review

**Document ID:** STF-BI-REV-05D-001  
**Review date:** 26 November 2026  
**Version:** 0.1  
**Status:** Internal AI desk review; proposed findings, not an approval or external specialist sign-off  
**Review destination:** Existing PR #9 — `review/scientific-data-model-review-pack`  
**Purpose:** Assess whether Task 05D and its linked scientific-model documents provide sufficient coherent, testable evidence to pass the logical-model validation gate and authorize Task 05E.

> **Decision boundary:** This review does not approve Task 05C Candidate A or B, settle EVT-D01–EVT-D10, amend an accepted ADR, approve a physical schema, or authorize DDL, migrations, API payload freeze or implementation. The project owner retains decision authority. No external specialist review or executable test run is represented here.

---

## 1. Executive conclusion

**Recommendation: Task 05D remains NOT PASSED. Task 05E and physical database design remain NOT READY.**

The repository has made meaningful progress: Candidate A contains stronger typed-subject integrity and taxonomy semantics; the review pack now articulates an Event–Survey–Occurrence model hypothesis; ODR-01 has an owner-authorized, narrowly bounded export-only interpretation; and the validation matrix identifies the disciplines and evidence required.

However, the evidence is not yet coherent enough to pass the gate. The most consequential unresolved matters are:

1. **Event identity and specialization:** the candidate model, Task 05D and the review pack do not yet present one reconciled logical representation for Event, Survey and Occurrence.
2. **Target assessment versus scientific outcome:** `SurveyTargetResult` and `SurveyTargetAssessment` are used for overlapping responsibilities. The authoritative detected/non-detected outcome must not be stored twice as independently mutable facts.
3. **Identification subject total participation:** the proposed row-local CHECK and foreign keys do not alone guarantee that every Identification has exactly one subject row.
4. **Standards version and term pinning:** document-level and term-level version claims have been mixed. Current TDWG publication metadata resolves part of the earlier uncertainty, but the exact Humboldt term resources and selected GBIF export profile still require reproducible pinning and mapping tests.
5. **Stale source baselines and branch divergence:** Task 05D's own source inventory no longer matches the current source file blobs and branch heads. Its PR branch has diverged from the current Candidate A branch.
6. **No execution or discipline sign-off:** the synthetic fixtures remain proposals, and no submitted reviews were found on PR #9, PR #11 or PR #5.

The right next step is not physical design. It is a controlled scientific-model reconciliation, followed by executable synthetic fixtures and attributable specialist review.

## 2. Exact repository and document baseline

The governing AI Project Operating Prompt was retrieved from `docs/governance/AI-PROJECT-OPERATING-PROMPT.md` on `docs/repository-audit-and-ai-operating-standard`, blob SHA:

`53add3894d0502827e584614c70ad09cadaa637d`

The prompt remains the governing working instruction under the project owner's direction while PR #16 is open and unmerged.

### 2.1 Live branch and PR snapshot

Verified 26 November 2026:

| Item | Current state |
|---|---|
| Repository | `Save-Tiger-First/botanica-indica` |
| Total branches | 23 |
| Required long-lived branches | `main`, `develop`, `staging` |
| `main` | `6f2f51da093caf8183fde386dbec707cc6046d27`, protected |
| `develop` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` |
| `staging` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` |
| PR #9 | Open, draft; head `78d247730b8bfcf7d1e61b73d8e6882d70365af8` |
| PR #11 | Open, draft; head `0577250c9e7cffcb3605acc782f403b7d1b422e0` |
| PR #5 | Open, draft; Candidate A branch head `d443420d6b77815cb155f457ea262e621aabf7cb` |
| PR #16 | Open, draft; head `16fd00e0e6719026a9c937c19c7409b13eb35f98` |

The operating prompt's immediate ceiling is seven branches in total, while the live repository has 23. The three required long-lived branches exist; the remaining 20 are temporary/workstream branches. This review does not authorize any branch deletion or consolidation action.

PR #9, PR #11 and PR #5 have no submitted reviews in the current review-list checks. GitHub's mergeable status is not approval.

### 2.2 Exact files fetched for this review

| Document | Branch | Current file blob SHA |
|---|---|---|
| Task 05D v3 — Logical Model Validation and Physical Design Readiness | `docs/task-05d-logical-model-validation-v3` | `0b9a009b1c543b2450758f659c97cae3802a2f94` |
| Task 05C Candidate A — Logical Database Model | `docs/task-05c-logical-data-model` | `b447796e7da0d08d96400812667a8e67e0696144` |
| Task 05B Scientific Data Dictionary | `docs/task-05-data-dictionary` | `ddaa379d993fdf1f45684962930d16f06830ae43` |
| Event–Survey–Occurrence Decision Paper | `review/scientific-data-model-review-pack` | `0a82ccd3e5de7642d53771877c7fbc896873123e` |
| EVT Decision and Validation Pack | `review/scientific-data-model-review-pack` | `4a317c4c83317e10663ba374e9e6be3100a53431` |
| Scientific Data Model Validation Matrix and Decision Register | `review/scientific-data-model-review-pack` | `3a33dfe47657a96456f56f2c12a0b7d355b6c6a5` |
| Task 05C Competing Model Reconciliation | `review/scientific-data-model-review-pack` | `e34eadf0257f38d81b4809e2477784045f460746` |

The current Task 05D source inventory in §16 still cites older file blobs for Task 05B, Candidate A and Task 05D itself. For example, it records Candidate A blob `c8bddcdfda9f76f03afd389ff9c5a307b89bd906` and Task 05D blob `27a12b960d84b504fe915da4681d2f2511bdb086`, whereas the current fetched blobs are `b447796e7da0d08d96400812667a8e67e0696144` and `0b9a009b1c543b2450758f659c97cae3802a2f94`. Historical snapshots are legitimate evidence, but they must be labelled historical rather than presented as current.

### 2.3 Stacked branch comparison

A live compare of current Candidate A branch head `d443420d6b77815cb155f457ea262e621aabf7cb` against current Task 05D v3 head `0577250c9e7cffcb3605acc782f403b7d1b422e0` reports:

- Status: **diverged**
- Task 05D head: 7 commits ahead
- Task 05D head: 4 commits behind Candidate A
- Merge base: `91c82b4f136a77aaa1edb02753ed49b2fbee86ed`

This is a source-history dependency, not proof of a content conflict. Do not rebase, retarget, merge or force-update either branch automatically. Reconcile the content and commit graph first, then document a non-destructive synchronization plan.

## 3. Findings ranked by severity

### F-01 — BLOCKER: no single reconciled Event–Survey–Occurrence logical model

Task 05C Candidate A's earlier ERD still represents Event-to-Occurrence as a contextual relationship. Candidate A's later §18 proposes a shared Event identity with mutually distinct Survey and Occurrence specializations, but the document itself says this proposal does not silently supersede the earlier model. The Task 05D v3 baseline does not provide a single final ERD and relational mapping resolving the difference.

The PR #9 Event decision paper recommends a shared Event identity/supertype with Survey and Occurrence specializations, a separate contextual Event where justified, and a separate contributor/workflow Observation. This is a coherent hypothesis, not an approved internal schema. Darwin Core's conceptual semantics do not force a particular relational inheritance implementation.

**Required evidence:**
- one canonical entity/relationship diagram and accompanying textual cardinalities;
- explicit shared Event identity and subtype exclusivity;
- explicit distinction between Event parent/child containment and Survey reporting of Occurrences;
- Observation-to-Event and Observation-to-Occurrence relationship roles and cardinalities;
- treatment of MaterialEntity and MediaAsset as distinct concepts;
- positive and negative fixtures for each relationship.

### F-02 — BLOCKER: SurveyTargetResult versus SurveyTargetAssessment and duplicate outcome risk

Task 05B §16 and Candidate A §18 use `SurveyTargetResult`. The EVT pack and competing-model reconciliation use `SurveyTargetAssessment`. The current descriptions overlap:

- `SurveyTargetAssessment` is intended to capture whether/how a target was assessed, scope, method, effort, completeness, limitations and provenance.
- `SurveyTargetResult` has also been described as carrying a result state such as detected or not detected.
- The model separately proposes a detected/non-detected state at Occurrence level.

If all three can carry independently editable outcomes, the database could preserve contradictory states for one target and survey scope.

**Recommendation, not decision:** use one attributable target-assessment lifecycle record for assessment context and completeness; use the canonical Occurrence representation for the taxon/organism-level detected or explicit non-detected scientific outcome; and use a typed `SurveyOccurrenceReport` association for the Survey's reporting relationship and role (target match, bycatch or another justified role). If the project retains `SurveyTargetResult`, define it as either the one authoritative result or a derived/non-authoritative view. Do not permit a second independently mutable outcome.

This needs field-ecology and biodiversity-informatics review. It is not settled by naming a table.

### F-03 — BLOCKER: IdentificationSubject total participation is not enforced by the proposed row-local CHECK

Candidate A proposes one `IdentificationSubject` row per `Identification`, with real foreign keys to Observation, Occurrence or MaterialEntity and a row-local CHECK requiring exactly one populated target FK. This enforces exactly one target within a subject row, but does not alone enforce that every Identification has a subject row.

PostgreSQL explicitly warns that CHECK constraints cannot safely reference other rows or tables; use appropriate relational constraints or a carefully designed trigger for cross-table rules. A parent-side FK, deferrable circular relationship or constraint-trigger strategy may be evaluated, but none should be selected without a complete transaction and migration design.

**Required evidence:** prove unique Identification participation, target FK integrity, exactly-one-target-per-subject, total participation, transaction safety under concurrent writes, rollback behavior and dump/restore validity. Include a negative test that creates an Identification without a subject and confirms the database rejects the committed state.

### F-04 — MAJOR: DR-09 standards version inventory needs a precise, term-level update

The older repository notes correctly warned that document issue dates, vocabulary snapshot dates and individual term-version dates are different. Current TDWG web evidence now resolves part of the earlier publication-date uncertainty:

- the Darwin Core Conceptual Model landing page identifies version 2026-10-13 and the version IRI `http://rs.tdwg.org/dwc/doc/cm/2026-10-13`;
- the Darwin Core List landing page identifies version 2026-10-13;
- the core Darwin Core term list metadata identifies the 2026-10-13 snapshot;
- `dwc:occurrenceStatus` remains term version 2026-05-26 and recommends `detected` / `notDetected`;
- `eco:isSurveyTargetFullyReported` is term version 2026-05-26 and is target-specific;
- TDWG's 2026-05-26 Humboldt list records `eco:isTaxonomicScopeFullyReported` 2024-02-28 as superseded by term version 2026-10-13.

The exact 2026-10-13 Humboldt term-list page and exact `isTaxonomicScopeFullyReported-2026-10-13` resource were not directly retrieved in this review. DR-09 should therefore be **partially resolved, not closed**. Retrieve and archive exact versioned resources/term IRIs, confirm their definitions/status and pin the selected export profile and mappings.

Do not conflate:
- taxonomic-scope reporting completeness;
- target-level reporting completeness;
- sampling effort reported;
- target scope;
- detectability or survey method.

### F-05 — MAJOR: explicit non-detection and export-only implicit interpretation must remain separate

The project owner's ODR-01 authorizes a controlled, profile-specific implicit non-detection interpretation in external exports only. It does not authorize internal inference from a missing Occurrence row and does not approve the final profile or implementation.

GBIF Guide v1.0.2 §7.3 explains that implicit absences are meaningful only when the taxonomic scope is fully reported. The GBIF guide's publishing conventions and Darwin Core's recommended `detected/notDetected` values are not automatically interchangeable.

**Required evidence:**
- internal missing-row state remains unknown/not assessed;
- explicit internal non-detection is an attributable, bounded scientific assertion;
- ODR-01 export interpretation is derived only from the permitted scope/completeness evidence and pinned versions;
- bycatch is excluded from target absence inference;
- missing, ambiguous, contradictory or incomplete evidence fails closed;
- export mapping is round-trip tested and audited.

### F-06 — MAJOR: event hierarchy, survey reporting and completeness semantics need executable tests

The TDWG hierarchical-event guidance (2026-10-13) states that a parent Event must spatially and temporally encompass its child Events. A parent/child hierarchy is not the same as a Survey reporting an Occurrence. The current review documents understand this distinction conceptually, but the fixtures must prove it.

No scope, completeness, protocol or effort should silently inherit from a parent or be inferred from child summaries unless a formally justified and versioned rule explicitly permits it. A post-facto analytical filter must not be represented as the original a priori survey target.

### F-07 — MAJOR: DR-08 mango native/introduced example remains a research comparison, not a proven contradiction

The model notes correctly identify this as a source-scope and geographic-resolution comparison. Normalize the geographic units, taxonomic concepts/treatments, temporal validity and source purpose before deciding whether sources actually conflict. Preserve source-specific claims; do not force a single global native/introduced flag.

### F-08 — MAJOR: validation cases are specifications, not test evidence

EVT-27–EVT-44, LDM-01–LDM-16 and FLD-01–FLD-08 remain proposed unless executable tests, expected graphs, negative assertions, run outputs and reviewer evidence are recorded. The review pack's existence and the CI success on unrelated repository governance checks do not demonstrate scientific-model validation.

### F-09 — MAJOR: independent discipline review is absent

The required review roles include Indian plant taxonomist, herbarium/data curator, biodiversity-informatics specialist, field botanist/ecologist, geospatial specialist, privacy/security reviewer, rights/legal reviewer, database architect and product owner. PR #9, PR #11 and PR #5 currently have no submitted reviews in the live review-list checks.

This is an internal desk review only. It cannot substitute for qualified specialist review, institutional approval or legal advice.

## 4. Test programme required before Task 05D can pass

At minimum, create versioned synthetic fixtures with expected entity graphs, negative assertions and executable outcomes for:

| Test group | Required cases |
|---|---|
| Event identity | Generic contextual Event; Survey specialization; Occurrence specialization; subtype exclusivity |
| Hierarchy | Parent spatial/temporal containment; multiple child Events; no silent inheritance; hierarchy distinct from reporting |
| Survey reporting | Target detection; bycatch; multiple Occurrences; repeated visits; SurveyOccurrenceReport independent of parent-child links |
| Target assessment | A priori target; post-facto filter; repeated assessment; incomplete/ambiguous scope; protocol and effort provenance |
| Non-detection | Explicit supported non-detection; empty Occurrence set remains unknown; no fabricated absence; fail-closed export |
| Identification subject | Missing subject; duplicate subject; zero or multiple target FKs; concurrent/transactional behavior |
| Taxonomy | Historical target concept/treatment remains interpretable after taxonomic revision |
| Rights/privacy | Restricted media; AI-training permission absent; revoked permission; sensitive coordinate hidden in search/export/logs |
| Interoperability | Exact pinned DwC/Humboldt/GBIF profile mapping; detected/notDetected mapping; round-trip and loss report |

All fixture data must be clearly synthetic. Do not use the fixtures as real occurrence records or as evidence of Indian plant distribution.

## 5. Recommended disposition and sequence

1. **Keep Task 05E blocked.** No physical schema, DDL, migrations or API payload freeze.
2. **Treat Candidate A as the preferred review starting document only.** Preserve Candidate B as an alternative source of useful workflow and cardinality cases; do not wholesale merge it.
3. **Resolve F-01 and F-02 first.** They determine the Event/Survey/Occurrence and target-assessment/outcome structure on which the remaining fixtures depend.
4. **Resolve F-03 before physical design.** Total participation is a database integrity requirement, not a diagram annotation.
5. **Refresh the source inventory and standards pins.** Preserve historical SHAs as historical; record current file blobs and branch heads separately.
6. **Reconcile Task 05D with current Candidate A using a preservation-first synchronization plan.** The branches are diverged (7 ahead / 4 behind); do not automatically rebase or retarget PR #11.
7. **Execute the synthetic validation suite.** Record test harness, version, environment, expected and actual outcomes, negative tests and reviewer attribution.
8. **Obtain discipline-specific review.** Record each reviewer's expertise, scope, date, evidence and disposition.
9. **Only then prepare a Task 05D pass/conditional-pass decision for project-owner authorization.**

The existing PR #9 review branch is the appropriate place to retain this desk-review report. No new branch is required. The seven-branch ceiling remains unmet and should be handled as a separate preservation-first governance workstream, not mixed into the scientific-model decision.

## 6. What this review did and did not do

### Completed
- Retrieved the complete governing operating prompt from the required PR #16 branch.
- Re-fetched the live repository, branch inventory, relevant PR metadata and review submissions.
- Fetched the current Task 05D v3, Candidate A, Task 05B dictionary, Event decision paper, EVT pack, validation matrix and competing-model reconciliation.
- Compared current Candidate A and Task 05D branch heads.
- Rechecked current official TDWG Darwin Core, Humboldt Extension, GBIF and PostgreSQL sources.
- Prepared this internal desk-review report on the existing PR #9 review branch.

### Not performed
- No accepted ADR was changed.
- No scientific model or product requirement was approved or amended.
- No tests were executed.
- No independent scientific, legal, privacy, security or institutional sign-off was obtained.
- No external reviewer or institution was contacted.
- No PR was merged, closed or retargeted.
- No branch was created or deleted.
- No repository protection, permission or setting was changed.
- No physical schema, DDL, migration, production API or application code was created.

## 7. Authoritative references checked on 26 November 2026

1. TDWG, Darwin Core Conceptual Model, version 2026-10-13: https://dwc.tdwg.org/cm/ and http://rs.tdwg.org/dwc/doc/cm/2026-10-13
2. TDWG, Darwin Core List of Terms, current landing page: https://dwc.tdwg.org/list/
3. TDWG, core Darwin Core terms: https://rs.tdwg.org/dwc/terms.htm
4. TDWG, Humboldt Extension terms: https://rs.tdwg.org/eco/terms.htm
5. TDWG, Humboldt Extension 2026-05-26 term-list snapshot (records replacement of selected terms by 2026-10-13 versions): https://rs.tdwg.org/eco/version/terms/2026-05-26.htm
6. TDWG, hierarchical-event guidance, version 2026-10-13: https://dwc.tdwg.org/hierarchy/
7. GBIF, Guide for publishing biological survey and monitoring data, v1.0.2 (2025-09-24), especially §7.3: https://docs.gbif.org/guide-publishing-survey-data/en/
8. PostgreSQL, Constraints documentation: https://www.postgresql.org/docs/current/ddl-constraints.html

**End of review — STF-BI-REV-05D-001 v0.1.**
