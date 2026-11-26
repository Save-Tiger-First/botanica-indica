# EVT-D01–EVT-D04 — Owner Disposition and Specialist Review Brief

**Document ID:** STF-BI-REV-EVT-004  
**Version:** 0.1  
**Date:** 26 November 2026  
**Status:** Owner accepted preferred direction for specialist validation; NOT final scientific approval  
**Repository:** `Save-Tiger-First/botanica-indica`  
**Review branch:** `review/scientific-data-model-review-pack`  
**Related PR:** #9 — Add consolidated scientific data model review pack

> **Decision boundary:** The project owner’s instruction to “go ahead with your recommendation” is recorded as acceptance of the four recommended dispositions as the preferred direction for specialist validation. It does not close EVT-D01–EVT-D04, approve Candidate A, amend an accepted ADR, approve Task 05B/05C, pass Task 05D, authorize Task 05E, freeze API/export contracts, authorize physical database design, or constitute external specialist sign-off.

---

## 1. Owner disposition recorded

On 26 November 2026, the project owner instructed the AI adviser to proceed with the preceding recommendations. The accepted scope is:

- use the recommended EVT-D01–EVT-D04 directions as the preferred working hypotheses for specialist validation;
- prepare a controlled review brief and identify unresolved semantic, interoperability and integrity questions;
- preserve Candidate A, Candidate B, the current Task 05B dictionary, Task 05D v3 and all review history;
- do not silently amend canonical model documents or convert a recommendation into a final scientific decision.

This is a **process/working-direction authorization**, not approval of the underlying scientific model.

## 2. Verified repository baseline

The complete governing prompt was retrieved from:

- Path: `docs/governance/AI-PROJECT-OPERATING-PROMPT.md`
- Branch: `docs/repository-audit-and-ai-operating-standard`
- Blob SHA: `53add3894d0502827e584614c70ad09cadaa637d`
- PR #16 remains open, draft and unmerged.

Repository state rechecked on 26 November 2026:

- 23 branches exist; the owner’s immediate seven-branch ceiling is not met.
- `main`, `develop` and `staging` exist.
- The no-new-branches directive remains in force.
- PR #9 is open and draft, base `main`, head `review/scientific-data-model-review-pack`.
- PR #5 (Candidate A) and PR #11 (Task 05D v3) remain open and draft.
- No PR was merged or closed, no branch was created or deleted, and no repository setting was changed.

Current relevant branch heads:

| Workstream | Branch | Head SHA |
|---|---|---|
| Scientific review pack | `review/scientific-data-model-review-pack` | `90ecb1ff52f0de173ff669d0896315c09b1e772d` |
| Task 05C Candidate A | `docs/task-05c-logical-data-model` | `d443420d6b77815cb155f457ea262e621aabf7cb` |
| Task 05B dictionary | `docs/task-05-data-dictionary` | `e11fd943e59c81ea8b464ef6a84ac4bcdbcccfd4` |
| Task 05D v3 | `docs/task-05d-logical-model-validation-v3` | `0577250c9e7cffcb3605acc782f403b7d1b422e0` |

Current relevant file blob SHAs fetched for this review:

| File | Branch | Blob SHA |
|---|---|---|
| EVT-D01–D04 decision-readiness review | review branch | `ab7872f44d9f49cad762e64f9a147a98eee53fbc` |
| Event–Survey–Target Outcome reconciliation recommendation | review branch | `29e72d4d4e0b25d52ca61bb1ba2a9e5a6ee0dd37` |
| EVT Decision and Validation Pack | review branch | `4a317c4c83317e10663ba374e9e6be3100a53431` |
| Scientific Data Model Validation Matrix and Decision Register | review branch | `3a33dfe47657a96456f56f2c12a0b7d355b6c6a5` |
| Task 05C Candidate A | Candidate A branch | `b447796e7da0d08d96400812667a8e67e0696144` |
| Task 05B Scientific Data Dictionary | Task 05B branch | `ddaa379d993fdf1f45684962930d16f06830ae43` |
| Task 05D v3 | Task 05D branch | `0b9a009b1c543b2450758f659c97cae3802a2f94` |

These are the sources inspected for this disposition. Historical SHAs recorded inside older documents are not substituted for the live values above.

## 3. Accepted working direction for specialist validation

| Decision | Preferred direction accepted for review | Still unresolved |
|---|---|---|
| EVT-D01 — Event identity | Shared Event identity with distinct, mutually exclusive Survey and Occurrence specializations; generic/context Event remains available where justified | Exact subtype participation, context semantics, multi-faceted workflows and enforceable integrity |
| EVT-D02 — Hierarchy vs context/reporting | Parent-child hierarchy only for genuine containment; typed reporting and contextual relationships are separate | Single-parent rule, acyclicity, spatial-temporal containment, context-link scope and no inheritance of unreported scope |
| EVT-D03 — Survey and SurveyTarget | Survey as an Event specialization; structured/versioned SurveyTarget; preserve a priori intent and post-facto filtering; zero-target inventory remains possible | Target dimensions, scope ownership at each Event level, target versioning, taxonomic concept pinning and deterministic inclusion/exclusion |
| EVT-D04 — Assessment and outcome | Use `SurveyTargetAssessment` as the working name for assessment lifecycle; avoid a second independently mutable taxon/organism detected/non-detected state; use the appropriate Occurrence-level record and typed Survey reporting relationship for supported organism/taxon outcomes | Canonical naming, negative Occurrence unit and scope, multiple assessment/reporting cases, profile mapping and correction/retraction lifecycle |

**Terminology note:** `SurveyTargetAssessment` is a working name for specialist review. Task 05B §16 and Candidate A §18 still use `SurveyTargetResult`. Do not rename the canonical dictionary or model until an explicit terminology disposition is approved.

## 4. New interoperability qualification requiring specialist review

### 4.1 Darwin Core Conceptual Model

The official TDWG Darwin Core Conceptual Model page retrieved on 26 November 2026 identifies the inspected version as **2026-05-26**, with version IRI:

`http://rs.tdwg.org/dwc/doc/cm/2026-05-26`

The page states that the model is a high-level semantic framework and does not prescribe a particular technology, relational schema or inheritance implementation. All sections other than the document-status section are marked non-normative.

Relevant semantics in the inspected version:

- Survey is a special type of Event.
- Occurrence is a special type of Event and represents the state of an Organism at a place and time.
- Event hierarchies represent containment; a child is entirely within one parent spatially and temporally, and an Event can have only one parent.
- A single Event is not to be interpreted as a combination of Survey, Occurrence and Organism Interaction special types.
- A context Event may, as an implementation choice, provide shared spatiotemporal context to multiple distinct activities.
- Survey results are expressed in the Occurrences the Survey reports; those may be target matches or bycatch.
- Survey Targets may combine taxa, environmental conditions and organismal traits.
- Occurrence can represent non-detection of any Organism of a given Taxon in a particular state during a defined time interval at a Location.

**Disposition:** The 2026-05-26 Conceptual Model is the directly inspected version. Earlier search-index metadata in project documents suggesting 2026-10-13 for this Conceptual Model is not confirmed by the current official page and must not be repeated as a verified version. DR-09 remains open for the exact current List of Terms, Humboldt Extension term-list snapshot and term-level IRIs/version status. Do not collapse document version, namespace snapshot and individual term version into one date.

Source:
- https://dwc.tdwg.org/cm/
- https://rs.tdwg.org/dwc/doc/cm/2026-05-26

### 4.2 GBIF survey publishing guide — one Occurrence row maps to one Event

The current official GBIF Guide for publishing biological survey and monitoring data to GBIF is v1.0.2, dated 2025-09-24.

The guide states that any Darwin Core Event may be associated with one or more Occurrence records. It also says that each Occurrence record in a Darwin Core Archive can be linked to only a single survey Event, and recommends linking the Occurrence to the lowest possible Event level in a nested hierarchy.

This is an important qualification to the broad internal discussion about one Occurrence being relevant to more than one Survey.

**Required specialist question:** Does Botanica Indica need one canonical internal scientific Occurrence to be referenced by multiple survey reports, or should each survey-specific occurrence assertion be a distinct Occurrence record that may share organism/evidence identity? If the internal model permits broader relationships than a selected GBIF profile, define a loss-aware, reproducible export mapping. Do not assume that an internal many-to-many relationship can be emitted directly as one GBIF occurrence row with multiple survey Event links.

The review must explicitly distinguish:
1. internal scientific identity;
2. a Survey's report/association to that record;
3. Darwin Core Archive row identity and its single Event link;
4. evidence or organism identity shared across survey records.

Source:
- https://docs.gbif.org/guide-publishing-survey-data/en/ (v1.0.2, 2025-09-24; section 7, Occurrence information)

### 4.3 Scope, completeness and bycatch

The GBIF guide states that target/excluded scope terms capture survey intent and should be recorded at each Event level where explicitly applicable; scope must not be inferred up or down the Event hierarchy, and should not be retrospectively inferred. It also states that absence claims are meaningful only when the relevant taxonomic scope is fully reported, and absence cannot be asserted for bycatch.

The guide separately describes extended Measurement or Fact (eMoF) for additional measurements about a site linked to an Event, and a Relevé extension for vegetation-plot measurements. These are publishing mappings, not instructions to copy the extension structure into Botanica Indica's internal schema.

**Disposition:** Preserve the distinction between target scope, actual observation, assessment completeness, sampling effort and measured environmental/site properties. A habitat scope can qualify which Occurrences are sought; it does not automatically make a habitat measurement a SurveyTarget outcome. Any first-class internal environmental-measurement capability must be justified by a concrete product/scientific workflow and designed separately.

Source:
- https://docs.gbif.org/guide-publishing-survey-data/en/ (sections 5.6, 5.7 and 6.1–6.2)

### 4.4 Database integrity

PostgreSQL documentation states that CHECK constraints cannot safely enforce conditions involving other rows/tables. This is relevant to subtype exclusivity, mandatory subtype participation, IdentificationSubject total participation and other cross-table invariants.

**Disposition:** The logical model must state the invariant independently of the eventual enforcement technique. The physical design must later prove a transaction-safe and restore-safe implementation using appropriate keys/constraints and, where justified, triggers. A row-local CHECK is not proof of total participation.

Source:
- https://www.postgresql.org/docs/current/ddl-constraints.html

## 5. Questions that specialists must answer

### 5.1 Field ecology / survey-method specialist

1. Are Survey and Occurrence best represented as distinct Event specializations for the actual Botanica Indica workflows?
2. Which examples genuinely require a generic/context Event, and which can use a direct Event hierarchy?
3. What is the scientifically defensible unit of a non-detection: taxon, taxonomic concept, organismal state/trait, spatial unit, temporal interval or a defined combination?
4. What minimum protocol, effort, detectability, scope and completeness evidence is required before explicit non-detection is defensible?
5. How should repeated visits, incomplete assessments, incidental detections and bycatch be represented without conflation?
6. Which target scopes are practical for botanical field surveys, and which require separate measurement records?

### 5.2 Botanical taxonomist / taxonomic data specialist

1. How should taxonomic targets be pinned to a taxon concept and treatment version at the time of survey?
2. How should a later taxonomic split, lump, synonymy or changed circumscription affect historical target interpretation?
3. What is the appropriate scope of explicit non-detection when the taxonomic concept changes?
4. How should uncertain, aggregate, genus-level and unresolved identifications be represented without false species-level absence?
5. What is the appropriate relationship between an Occurrence, its organismal state and one or more determinations?

### 5.3 Biodiversity informatics / TDWG specialist

1. Does the proposed Event/Survey/Occurrence distinction faithfully represent the inspected Darwin Core Conceptual Model?
2. Which relationships should be internal-only and which map cleanly to Darwin Core Event, Occurrence and Humboldt terms?
3. How should one internal Occurrence referenced by multiple Survey reports map to the GBIF guide's one-Event-per-Occurrence-row rule?
4. Which exact Darwin Core and Humboldt term versions apply to the chosen export profile?
5. How should explicit internal non-detection map to the selected profile, given differences between Darwin Core recommended values and GBIF guide examples?
6. What evidence is needed to support ODR-01's restricted export-only implicit interpretation, and what conditions require fail-closed behaviour?

### 5.4 Data architect / database integrity specialist

1. What logical pattern best enforces Event identity and mutually exclusive specializations without assuming a particular SQL inheritance technique?
2. How will mandatory subtype participation, exclusivity and referential integrity be proven?
3. How will Event hierarchy acyclicity, single-parent cardinality and spatiotemporal containment be enforced?
4. How will SurveyOccurrenceReport remain independent from Event parent-child hierarchy?
5. How will Observation, Occurrence, Organism, MaterialEntity and MediaAsset avoid identity conflation?
6. What are the transaction, concurrent-write, migration, restore and correction/retraction implications?

### 5.5 Product owner / domain workflow review

1. Which Survey workflows are in scope for Botanica Indica's full product vision?
2. Which user roles can declare a target, change a target, complete an assessment, create an Occurrence or assert non-detection?
3. How will a post-facto filter be visibly distinguished from original survey intent?
4. Which parts are essential to the domain model and which are optional integrations/export capabilities?

## 6. Minimum evidence required before canonical reconciliation

The specialist review should not be a generic endorsement. It should produce attributable answers and testable evidence for the following cases:

1. Generic/context Event supporting multiple distinct activities without subtype identity conflation.
2. Survey and Occurrence as distinct Event specializations.
3. Survey reports target-matching and bycatch Occurrences through a typed report relationship.
4. Parent-child hierarchy and reporting association tested independently.
5. Event hierarchy with one parent, acyclicity and spatial-temporal containment.
6. Survey target declared a priori and post-facto, with preserved authorship and timestamps.
7. Multi-dimensional target scope involving taxon plus organismal trait/life stage.
8. Target scope stated at a child Event but not inferred from parent, and vice versa.
9. Complete positive assessment with one or more Occurrences.
10. Defensible explicit non-detection for a bounded taxon/organismal state.
11. Incomplete, not assessed and indeterminate cases do not create negative Occurrences.
12. Bycatch cannot satisfy target reporting completeness or support absence inference.
13. Taxonomic split/lump does not silently rewrite historical target meaning.
14. One internal Occurrence referenced across multiple Survey reports, with a tested GBIF export strategy or explicit rejection of that internal cardinality.
15. Event measurement (eMoF/Relevé-style use case) remains distinct from SurveyTarget and Occurrence.
16. Sensitive location generalization/withholding is preserved in exports and audit trails.

All cases are proposed. No test is claimed executed.

## 7. Required deliverable from specialist validation

Before changing Candidate A or Task 05B, prepare a review record containing:

- reviewer role and relevant competence;
- date, document/version and exact sections reviewed;
- each question answered, with rationale and references;
- accepted, rejected or conditional recommendations;
- unresolved disagreements and minority positions;
- required model changes and their consequences;
- test cases and expected entity/relationship graphs;
- export profile and version assumptions;
- any conflicts with accepted ADRs or requirements;
- explicit limits of the review (what the reviewer did not assess).

No reviewer name, affiliation, approval or external sign-off may be invented. No external party has been contacted as part of this work.

## 8. Next controlled sequence

1. Obtain and record attributable specialist responses against this brief.
2. Resolve any semantic disagreements and update the EVT decision register with evidence.
3. If the owner then approves the resulting model direction, prepare one consolidated Candidate A ERD, entity/relationship specification and cardinality table.
4. Preserve the previous Candidate A content and Candidate B as historical/review sources; document supersession rather than deleting material.
5. Reconcile Task 05B terminology and relationship definitions against the authorized Candidate A baseline.
6. Synchronize Task 05D v3 through a non-destructive dependency plan; inspect the diverged PR #5/PR #11 histories before any synchronization action.
7. Execute synthetic fixtures and record actual evidence.
8. Reassess Task 05D readiness only after required reviews, model coherence and test evidence exist.

## 9. Current status and explicit non-actions

- EVT-D01–EVT-D04: preferred direction accepted for specialist validation; scientific decisions remain OPEN.
- Candidate A: preferred review starting point; NOT APPROVED.
- Candidate B: preserved alternative source; NOT APPROVED.
- Task 05B: proposed dictionary; not reconciled.
- Task 05D: PROPOSED / NOT PASSED.
- Task 05E and physical database design: NOT READY.
- ODR-01: owner-authorized export-only policy; selected profile, mapping and implementation remain pending.
- DR-09: remains OPEN. Directly inspected Darwin Core Conceptual Model version is 2026-05-26; exact current List/Humboldt term snapshots and relevant term IRIs still require reproducible verification.
- No tests were executed.
- No independent specialist review was obtained.
- No external party was contacted.
- No accepted ADR or product requirement was changed.
- No canonical scientific model was amended.
- No PR was merged, closed or retargeted.
- No branch was created or deleted.
- No repository protection or setting was changed.
- No physical schema, DDL, migration or API contract was created or frozen.

**End of document — STF-BI-REV-EVT-004 v0.1.**

## 10. Standards evidence correction — 26 November 2026

The standards assumptions in this specialist brief must be read with the current [Standards Version Verification Addendum](EVT-D01-D04-STANDARDS-VERSION-VERIFICATION-ADDENDUM-2026-11-26.md), blob `85bf0e6e85025a6a8d19f463f743a728a0b6857a`.

Current evidence identifies the Darwin Core Conceptual Model and List issue version as 2026-10-13. The current List identifies `dwc:samplingEffort-2026-10-13` and `dwc:samplingProtocol-2026-10-13`; `dwc:occurrenceStatus-2026-05-26` continues to recommend `detected` / `notDetected`. Humboldt terms must be pinned individually: `eco:Survey` and `eco:isTaxonomicScopeFullyReported` are 2026-10-13, whereas `eco:SurveyTarget` and `eco:isSurveyTargetFullyReported` are 2026-05-26. The full 2026-10-13 Humboldt snapshot remains to be archived.

The GBIF v1.0.2 implicit-absence recipe must not be misrepresented as requiring `eco:taxonCompletenessReported=reportedComplete` universally. Specialists should advise whether Botanica Indica should impose that additional, stricter policy safeguard.

This correction updates the evidence baseline only. It does not approve EVT-D01–D04, Candidate A, Task 05D or Task 05E.

## 11. Further qualification — direct List retrieval conflict

Official indexed metadata reports the Darwin Core List issue version as 2026-10-13, but direct retrieval of the current List landing page in this review still renders the 2026-05-26 header and vocabulary version. Treat the document-level version discrepancy as unresolved; do not claim the full 2026-10-13 List content has been inspected.

The current core Darwin Core namespace term page independently verifies `dwc:samplingEffort-2026-10-13` and `dwc:samplingProtocol-2026-10-13`. The directly rendered List verifies `dwc:occurrenceStatus-2026-05-26`. The directly rendered Humboldt term list remains 2026-05-26; its metadata marks some older terms superseded by 2026-10-13 replacements, but the full replacement snapshot and definitions still need retrieval.

This qualification supersedes any wording above that states the complete 2026-10-13 List or Humboldt snapshot has been directly verified. See the corrected [Standards Version Verification Addendum](EVT-D01-D04-STANDARDS-VERSION-VERIFICATION-ADDENDUM-2026-11-26.md). DR-09 remains OPEN.
