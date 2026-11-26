# EVT-D01–EVT-D04 — Decision Readiness and Cross-Document Disposition Review

**Document ID:** STF-BI-REV-EVT-003  
**Version:** 0.1  
**Review date:** 26 November 2026  
**Status:** Internal desk-review recommendation; NOT an approved decision or specialist sign-off  
**Destination:** Existing PR #9 — `review/scientific-data-model-review-pack`  
**Decision authority:** Project owner, informed by qualified field ecology, botanical taxonomy, biodiversity-informatics and data-architecture review  
**Related documents:** STF-BI-REV-05D-001; STF-BI-REV-FLD-002; EVT Decision and Validation Pack; Task 05C Candidate A; Task 05B Scientific Data Dictionary; Task 05D v3

> **Decision boundary:** This review recommends dispositions for EVT-D01 through EVT-D04. It does not close those decisions, approve Candidate A or B, amend an accepted ADR, pass Task 05D, authorize Task 05E, freeze an API, or authorize physical database design or implementation. All four EVT decisions remain OPEN until the project owner records an explicit decision after appropriate specialist review and evidence.

---

## 1. Executive conclusion

**Recommendation:** retain the existing EVT decision pack's preferred direction, with two important refinements:

1. For **EVT-D01–D03**, the existing proposed direction is coherent and supported by the current Darwin Core/Humboldt semantics, subject to the internal modelling and test qualifications in this review.
2. For **EVT-D04**, retain the proposed separation between an assessment lifecycle record and the authoritative Occurrence-level organism/taxon result, but narrow the treatment of non-taxonomic SurveyTarget scopes. Do not create a separate generic SurveyTargetOutcome entity or route all non-taxonomic target results through ScientificAssertion/MeasurementOrFact merely because the Conceptual Model mentions environmental conditions and organismal traits.

The critical standards nuance is this: the Darwin Core Conceptual Model says Survey Targets can be based on taxa, environmental conditions and organismal traits, but it also says Survey results are expressed in the Occurrences reported by the Survey. The Humboldt term definition describes an `eco:SurveyTarget` as one or more scopes describing a target for `dwc:Occurrences` in an `eco:Survey`. Therefore, a habitat or environmental scope may qualify which Occurrences are being sought; it does not, by itself, prove that every environmental measurement is a SurveyTarget outcome or that every such measurement should become an Occurrence.

For pure environmental measurements (for example, soil moisture or canopy-cover values), use the appropriate Event measurement / measurement-or-fact / scientific-assertion design if the product requires it. The current Candidate A logical model does not yet demonstrate a complete, typed Event-measurement path. That gap should be assessed as its own bounded data-model requirement, not silently solved by adding a new SurveyTarget outcome entity.

**Task 05E remains NOT READY.** The four decisions are still proposals. No tests were executed and no specialist review was obtained in this work.

## 2. Repository and governance baseline

The complete AI Project Operating Prompt was fetched from:

- Path: `docs/governance/AI-PROJECT-OPERATING-PROMPT.md`
- Branch: `docs/repository-audit-and-ai-operating-standard`
- Blob SHA: `53add3894d0502827e584614c70ad09cadaa637d`
- Version: 1.0 — proposed project operating standard, followed as the owner's current instruction.

Live repository state checked on 26 November 2026:

- Repository: `Save-Tiger-First/botanica-indica`
- Branches: 23 total.
- Required long-lived branches: `main`, `develop`, `staging`.
- Owner's immediate ceiling: seven branches total; not met.
- Owner's no-new-branches directive: in force.
- PR #9: open, draft, base `main`, head `review/scientific-data-model-review-pack`.
- PR #16: open, draft, unmerged; the required operating-prompt branch therefore remains authoritative.
- No PR was merged or closed, no branch was created or deleted, and no repository setting was changed.

Existing PR #9 branch head before this document: `1e989c92bda5bafccc322629ff4adde8f64d9dd5`.

### 2.1 Exact source files fetched for this review

| Source | Branch | File blob SHA |
|---|---|---|
| Event–Survey–Occurrence Conceptual Model Decision Paper | `review/scientific-data-model-review-pack` | `0a82ccd3e5de7642d53771877c7fbc896873123e` |
| EVT Decision and Validation Pack | `review/scientific-data-model-review-pack` | `4a317c4c83317e10663ba374e9e6be3100a53431` |
| Scientific Data Model Validation Matrix and Decision Register | `review/scientific-data-model-review-pack` | `3a33dfe47657a96456f56f2c12a0b7d355b6c6a5` |
| Task 05C Competing Model Reconciliation | `review/scientific-data-model-review-pack` | `e34eadf0257f38d81b4809e2477784045f460746` |
| Task 05D Independent Validation Review | `review/scientific-data-model-review-pack` | `a9e2c50c30eb4da1993a7522797c59b1fd799654` |
| Event–Survey–Target Outcome Reconciliation Recommendation | `review/scientific-data-model-review-pack` | `29e72d4d4e0b25d52ca61bb1ba2a9e5a6ee0dd37` |
| Task 05C Candidate A | `docs/task-05c-logical-data-model` | `b447796e7da0d08d96400812667a8e67e0696144` |
| Task 05B Scientific Data Dictionary | `docs/task-05-data-dictionary` | `ddaa379d993fdf1f45684962930d16f06830ae43` |
| Task 05D v3 | `docs/task-05d-logical-model-validation-v3` | `0b9a009b1c543b2450758f659c97cae3802a2f94` |

Historical source inventories inside the decision paper, EVT pack, dictionary and Task 05D contain older blob SHAs. They remain useful historical snapshots but must not be presented as current file contents. Refresh the canonical source inventory when the review pack is next reconciled.

## 3. Cross-document audit — confirmed inconsistencies and current position

### 3.1 Event representation is still duplicated in Candidate A

Candidate A's earlier ERD and relationship table model Event-to-Occurrence as a contextual one-to-many relationship. Candidate A §18 later proposes a shared Event identity with Survey and Occurrence specializations, but expressly says it does not supersede the earlier content. The document still does not contain one reconciled canonical ERD and relationship set.

Task 05B §16 describes Event, Survey and Occurrence as distinct concepts and proposes a shared Event identity/subtype pattern, but its older cardinality and field tables remain inconsistent with that pattern. The EVT pack, decision paper, validation matrix and Task 05D are review proposals and do not themselves amend Candidate A.

**Disposition:** F-01 remains a real blocker. The new review pack does not close it. One canonical Candidate A model must be prepared only after the owner authorizes the disposition and the relevant specialists review it.

### 3.2 Target result/assessment naming and responsibility conflict persists

- Task 05B §16 calls the record `SurveyTargetResult` and includes result states such as `DETECTED` and `NOT_DETECTED_EXPLICIT`.
- Candidate A §18 also calls it `SurveyTargetResult`.
- The EVT pack and competing-model reconciliation use `SurveyTargetAssessment` for the assessment/completeness lifecycle.
- The validation matrix explicitly records the naming conflict and duplicate-state risk.

**Disposition:** F-02 remains open. The working name `SurveyTargetAssessment` is a reasonable proposed canonical term for the assessment lifecycle, but this is not an approved rename. Preserve the old terminology in historical documents and record a controlled terminology disposition before changing the canonical dictionary/model.

### 3.3 Existing model does not yet demonstrate a generic Event measurement path

Candidate A includes `ScientificAssertion` and several typed assertion concepts, with typed subject links. It does not currently establish a complete Event-linked environmental measurement design with measurement type, value, unit, method/protocol, spatial-temporal scope, agent, evidence, rights and provenance.

It would therefore be premature to claim that Candidate A's existing ScientificAssertion/MeasurementOrFact concepts already solve all environmental measurement use cases. Equally, it would be premature to create a new `SurveyTargetOutcome` entity without a demonstrated domain requirement.

**Disposition:** create a separate, bounded requirements/design investigation if Botanica Indica must record pure environmental measurements as first-class scientific data. Do not make this a hidden prerequisite for the taxonomic Survey/Occurrence model unless a concrete workflow proves the dependency.

### 3.4 Existing decisions and statuses remain open

The validation matrix explicitly leaves B01, B02, B16 and DR-09 open. It also records that EVT/LDM/FLD cases remain unexecuted unless actual run evidence exists. ODR-01 is owner-authorized as an export-only policy, but the selected profile, mapping and implementation are not approved.

No wording change in a proposal should be used to close those statuses.

## 4. Recommended disposition for EVT-D01 — Event identity and specializations

**Recommended option:** EVT Decision Pack Option B, with the clarifications below.

### 4.1 Proposed logical semantics

- **Event identity:** stable identity and shared properties of a real-world action, process or set of circumstances at a place and interval.
- **Survey specialization:** a Survey is a distinct kind of Event with survey-specific scope, target, protocol, effort and reporting information.
- **Occurrence specialization:** an Occurrence is a distinct kind of Event representing the state of an Organism at a place and time, including a supported explicit non-detection for a defined taxon/organismal state.
- **Observation:** remains a separate Botanica Indica contribution/workflow record. It is not automatically an Event, Survey or Occurrence.
- **MaterialEntity:** remains physical material, distinct from both Occurrence and MediaAsset.
- **Context Event:** a generic or explicitly contextual Event may provide shared spatiotemporal context to multiple distinct activities where the real-world workflow warrants it.

### 4.2 Important qualifications

1. The Darwin Core Conceptual Model is a semantic reference and explicitly does not prescribe a relational schema, inheritance implementation or strict database blueprint. The internal shared-identity/subtype pattern is a Botanica Indica design recommendation, not a TDWG database mandate.
2. The Conceptual Model allows an Event to provide shared spatiotemporal context to multiple activities and notes that a multi-faceted context Event may be useful. Do not force every context into a parent-child hierarchy or require a separate context Event when no such real-world context needs representation.
3. The recommendation that a single internal Event identity has at most one Survey or Occurrence specialization is an internal integrity hypothesis. Validate it against real workflows and explicit examples before approving it. It should not be described as a universal Darwin Core rule.
4. A Survey reporting an Occurrence is not the same relationship as the Survey and Occurrence being parent/child Events. Use a typed report association.

### 4.3 Required acceptance evidence

- One generic/context Event supporting multiple distinct activities.
- A Survey with one Event identity and Survey-specific attributes.
- An Occurrence with one Event identity and occurrence-specific attributes.
- A Survey reporting multiple Occurrences, including target match and bycatch.
- A context Event supporting a Survey and separate Occurrence Events without identity conflation.
- A test proving that the chosen internal specialization constraints can be enforced and restored safely.
- A reasoned exception analysis for any proposed multi-faceted Event case.

**Recommended status:** preferred for owner/specialist review; EVT-D01 remains OPEN.

## 5. Recommended disposition for EVT-D02 — Hierarchy versus context/reporting

**Recommended option:** EVT Decision Pack Option B.

### 5.1 Rule

Use parent-child Event hierarchy only for genuine nested event/inventory containment. Use separate typed relationships for:
- Survey reports Occurrence;
- Observation documents/supports Event or Occurrence;
- shared context between distinct activities;
- collection/evidence relationships.

Do not use `parentEventID` as a generic foreign key for “related to”, “reported by”, “same site”, “same expedition” or “same Observation”.

### 5.2 Standards finding

The TDWG hierarchical-event guidance version 2026-10-13, Section 3, is normative. Its principle of spatiotemporal coverage says a parent Event MUST encompass its child Events spatially and temporally. The hierarchy may represent an inventory dataset with broader parent Events and narrower child Events. This is stronger than a mere diagram convention.

### 5.3 Required acceptance evidence

- A monitoring programme with repeated surveys, sites and visits.
- A parent Event whose spatial and temporal extents encompass all child Events.
- A deliberately invalid child whose extent exceeds the parent, rejected where the relevant extents are sufficiently known to compare.
- A cycle-prevention test.
- A multi-parent test against the chosen strict hierarchy rule.
- A SurveyOccurrenceReport link without a parent-child relation.
- A parent-child relation without a SurveyOccurrenceReport.
- Proof that parent scope/completeness is not silently inherited by children and child summaries do not silently determine parent completeness.

**Recommended status:** preferred for owner/specialist review; EVT-D02 remains OPEN.

## 6. Recommended disposition for EVT-D03 — Survey and SurveyTarget

**Recommended option:** EVT Decision Pack Option B.

### 6.1 Proposed semantics

- Survey is a distinct specialization/record sharing one Event identity.
- SurveyTarget is a structured, versioned declaration of one or more scopes describing what the Survey sought or selected for analysis.
- Preserve a priori intent versus post-facto analytical filtering, author, date/time, method, scope, inclusion/exclusion, source and relevant taxonomic treatment.
- A Survey with zero declared targets can still be valid as a general inventory; it cannot support target-specific absence inference merely because it has no target rows.
- The target scope may be multi-dimensional and may describe taxa, habitat, organismal traits, life stage, growth form, degree of establishment or other supported dimensions.
- Taxonomic target scope must preserve the exact taxonomic concept/treatment and source/version applicable at the time.

### 6.2 Important standards nuance

The directly retrieved Darwin Core Conceptual Model text states that Survey Targets may be based on combinations of taxa, environmental conditions and organismal traits, and that Survey results are expressed in the Occurrences the Survey reports. The Humboldt term definition describes `eco:SurveyTarget` as one or more scopes that describe a target for `dwc:Occurrences` in an `eco:Survey`.

Therefore:

- Do not restrict SurveyTarget to one species name.
- Do not interpret the environmental/habitat/trait examples as proof that every measurement of those properties is itself a SurveyTarget result.
- Do not create an Occurrence for a free-standing soil-moisture or canopy-cover measurement.
- If the platform must store pure environmental measurements, model them as measurements/assertions associated with the relevant Event/Survey (or other appropriate subject) and review that design separately.
- Do not create a generic SurveyTargetOutcome entity until a real use case and the existing measurement/assertion model have been evaluated.

### 6.3 Required acceptance evidence

- A priori taxonomic target with source/treatment version.
- A target with multiple scope dimensions (e.g. taxon plus life-stage or growth-form scope).
- Inclusion and exclusion criteria with deterministic interpretation.
- Post-facto target filter that does not rewrite original field intent.
- A habitat-scoped survey with Occurrence reporting.
- A zero-target general inventory with no target-specific absence inference.
- A pure environmental measurement example stored as an Event-linked measurement/assertion, if that capability is in scope.
- Historical target remains interpretable after taxonomic source/treatment changes.

**Recommended status:** preferred for owner/specialist review; EVT-D03 remains OPEN.

## 7. Recommended disposition for EVT-D04 — Assessment and canonical outcome

**Recommended option:** EVT Decision Pack Option B, subject to a narrower target/outcome boundary.

### 7.1 Proposed separation

Use the following distinct responsibilities:

| Concept | Responsibility | Must not contain |
|---|---|---|
| SurveyTarget | Versioned target scope and origin | Assessment result or mutable detection state |
| SurveyTargetAssessment (working name) | Whether/how a target was assessed within a defined visit/period/scope; protocol, effort, completeness, limitations, agents, evidence and provenance | A second independently mutable detected/not-detected outcome that can contradict Occurrence |
| Occurrence | Canonical organism/taxon-level occurrence state, including a supported explicit non-detection for a defined taxon/organismal state | Duplicate assessment lifecycle and all survey-wide completeness dimensions |
| SurveyOccurrenceReport | Typed link stating that a Survey reports an Occurrence, including target-match/bycatch role | Event parent-child hierarchy or duplicated result state |

The assessment record may have lifecycle states such as not assessed, in progress, completed, incomplete, indeterminate, not applicable, withdrawn or superseded. These describe the assessment process, not the ecological detection outcome.

### 7.2 Explicit non-detection

For a taxonomic/organismal target:
- an attributable, bounded assessment establishes whether the relevant target was actually assessed and what completeness/limitations apply;
- the canonical Occurrence carries the explicit organism/taxon-level detected or not-detected state, where that representation is scientifically justified;
- the Survey reports the Occurrence through SurveyOccurrenceReport;
- a missing Occurrence row alone remains unknown/not assessed;
- an incomplete, not-assessed or indeterminate assessment cannot produce a negative Occurrence;
- corrections/retractions preserve history and provenance.

Do not assume that a single negative Occurrence necessarily captures every possible multi-scope target without a scope decomposition rule. The unit of a negative Occurrence must be explicit: taxon/concept, organismal state/trait, time interval, location and assessment boundary.

### 7.3 Environmental and non-taxonomic target caution

The prior joint recommendation suggested investigating a non-occurrence target-outcome path through ScientificAssertion/MeasurementOrFact. Keep that as a separate modelling question, not a default extension of EVT-D04.

The standards evidence supports multi-dimensional SurveyTarget scopes but does not, by itself, establish that all environmental target measurements should be stored as SurveyTarget outcomes. Candidate A's current ScientificAssertion model has typed subject links but does not yet prove a complete Event measurement model. A separate Event-measurement requirement should be raised only if a concrete Botanica Indica workflow needs it.

### 7.4 Required acceptance evidence

- Complete taxonomic target assessment with one or multiple positive Occurrences.
- Complete, bounded explicit non-detection.
- Incomplete assessment; no negative Occurrence.
- Not-assessed target; no negative Occurrence.
- Indeterminate assessment; no negative Occurrence.
- Bycatch Occurrence reported without satisfying target detection/completeness.
- Repeated visits retained as separate assessments and Occurrence Events.
- Empty Occurrence query with no assessment remains unknown.
- Correction/retraction of a negative Occurrence preserves original assertion and audit trail.
- No independently mutable contradictory outcome between assessment and Occurrence.

**Recommended status:** preferred for owner/specialist review; EVT-D04 remains OPEN.

## 8. Standards version and semantic findings checked 26 November 2026

### 8.1 Darwin Core Conceptual Model

The official search metadata reports a 2026-10-13 version IRI, but direct HTML retrieval still rendered the 2026-05-26 document header and version IRI. The exact 2026-10-13 versioned document could not be directly opened in this review. The directly retrieved 2026-05-26 text states:

- Survey is a type of Event.
- Survey results are expressed in Occurrences it reports.
- Occurrences may be target matches or incidental/bycatch.
- Survey Targets may combine taxa, environmental conditions and organismal traits.
- Occurrence is an Event establishing the state of an Organism at a place and time, including direct observation, indirect inference or supported absence of detection for a given taxon/state.
- The Conceptual Model is a high-level semantic framework and does not prescribe a technology or database implementation.
- All sections other than document-status section 1.4 are non-normative.

Sources:
- https://dwc.tdwg.org/cm/
- https://rs.tdwg.org/dwc/doc/cm/2026-05-26
- https://rs.tdwg.org/dwc/doc/cm/2026-10-13 (exact versioned content not directly retrieved)

### 8.2 Darwin Core List and occurrenceStatus

The directly rendered List page still identifies 2026-05-26. The `dwc:occurrenceStatus` term version is 2026-05-26 and recommends `detected` and `notDetected`. This must not be silently replaced with the GBIF guide's example literals `present` and `absent`; the export mapping must be profile-specific and tested.

Sources:
- https://dwc.tdwg.org/list/
- http://rs.tdwg.org/dwc/terms/version/occurrenceStatus-2026-05-26

### 8.3 Humboldt Extension term inventory

The directly retrieved current Humboldt term-list page identifies a 2026-05-26 snapshot and lists versions including:
- `eco:Survey` and `eco:SurveyTarget` term versions 2026-05-26;
- `eco:isSurveyTargetFullyReported` term version 2026-05-26, recommended, with a target-specific definition concerning whether all detected Occurrences matching a SurveyTarget were fully reported;
- `eco:isTaxonomicScopeFullyReported` 2024-02-28 marked superseded and replaced by term version 2026-10-13.

The 2026-10-13 replacement term IRI could not be directly retrieved. Do not claim the complete 2026-10-13 Humboldt list or all of its term statuses have been verified.

Sources:
- https://rs.tdwg.org/eco/terms.htm
- https://rs.tdwg.org/eco/version/terms/2026-05-26.htm
- http://rs.tdwg.org/eco/terms/version/isTaxonomicScopeFullyReported-2026-10-13 (not directly accessible in this retrieval)

### 8.4 Hierarchical Event guidance

Official TDWG metadata identifies the hierarchical-event guidance as version 2026-10-13. Section 3 is normative and states that a parent Event MUST encompass child Events spatially and temporally. This is a stronger and more precise basis for the hierarchy acceptance tests than the Conceptual Model's non-normative description.

Source:
- https://dwc.tdwg.org/hierarchy/

### 8.5 GBIF survey guide

GBIF Guide for publishing biological survey and monitoring data to GBIF, v1.0.2 (2025-09-24), §7.3, describes explicit and implicit absence publishing. It says implicit absence interpretation requires fully reported taxonomic scope and explicit target or excluded scope, and that absence cannot be asserted for bycatch. This is publishing guidance, not an internal database schema or proof of biological absence.

Source:
- https://docs.gbif.org/guide-publishing-survey-data/en/

### 8.6 PostgreSQL constraint note

PostgreSQL documentation states that CHECK constraints cannot safely reference other rows or tables and recommends UNIQUE, EXCLUDE or FOREIGN KEY constraints for cross-row/cross-table restrictions where possible. This is relevant to eventual Event specialization integrity and IdentificationSubject total participation; physical enforcement remains deferred.

Source:
- https://www.postgresql.org/docs/current/ddl-constraints.html

## 9. Consolidated acceptance matrix

| Decision | Recommended disposition | Remaining blockers |
|---|---|---|
| EVT-D01 | Shared Event identity with Survey and Occurrence specializations; context is separately represented only where justified | Candidate A canonical ERD/key/cardinality reconciliation; real workflow fixtures; discipline review; integrity proof |
| EVT-D02 | Parent-child only for true hierarchy; typed reporting/context links separately | Normative hierarchy fixtures; spatial-temporal containment; cycles/multiple parents; no silent inheritance |
| EVT-D03 | Structured, versioned SurveyTarget scopes; preserve a priori/post-facto origin; allow zero-target inventory | Target scope semantics; taxonomic treatment pinning; habitat/trait scope fixtures; measurement boundary |
| EVT-D04 | SurveyTargetAssessment lifecycle plus Occurrence as authoritative organism/taxon result; SurveyOccurrenceReport association | Canonical naming decision; exact negative Occurrence unit/scope; no duplicate state; executed positive/negative/incomplete/bycatch tests |

All four decisions remain OPEN. B01, B02, B16, DR-07 and DR-09 remain open. EVT-27–EVT-44 and related LDM/FLD fixtures remain proposed until executable test evidence is committed.

## 10. Recommended next actions

1. Obtain project-owner disposition on the four recommendations and the explicit qualifications in this document.
2. Obtain field ecologist/survey-method specialist and biodiversity-informatics review for EVT-D01–D04; include botanical taxonomic review for taxonomic target/version semantics and database architecture review for identity/integrity.
3. After owner authorization, prepare one consolidated Candidate A ERD and relationship specification. Do not overwrite or delete the earlier model; preserve its history and document supersession.
4. Reconcile Task 05B §16 terminology and relationship/cardinality tables with the authorized Candidate A model.
5. Reconcile Task 05D v3 fixtures and acceptance criteria with the exact Candidate A baseline.
6. Separately scope the Event-measurement requirement if pure environmental measurements are part of the full product capability map.
7. Execute synthetic fixtures and preserve expected/actual outputs, environment, test versions, negative assertions and reviewer attribution.
8. Reassess Task 05D readiness only after the scientific model is coherent, required tests are executed, and specialist reviews are recorded.

**No new branch is required or permitted under the current owner directive.** Retain this report on the existing PR #9 review branch. Branch consolidation to the seven-branch ceiling remains a separate preservation-first governance workstream.

## 11. Work not performed

- No EVT decision was approved or closed.
- No accepted ADR, scientific model or product requirement was changed.
- No Task 05B, Task 05C or Task 05D source file was edited.
- No test was executed.
- No independent specialist, institutional, legal, privacy or security review was obtained.
- No external party was contacted.
- No PR was merged, closed or retargeted.
- No branch was created or deleted.
- No repository protection or setting was changed.
- No physical schema, DDL, migration, API payload freeze or application code was created.

**End of document — STF-BI-REV-EVT-003 v0.1.**

## 12. Standards evidence correction — 26 November 2026

This correction supersedes the older List/term-version descriptions in Sections 8.1–8.3 where they conflict with the current official TDWG List metadata checked in the Standards Version Verification Addendum (blob `85bf0e6e85025a6a8d19f463f743a728a0b6857a`).

- Current official Darwin Core Conceptual Model and List metadata identify 2026-10-13 as the current issue version. The Conceptual Model is non-normative semantic guidance and does not mandate a database inheritance strategy.
- Current List term metadata identifies `dwc:samplingEffort-2026-10-13` and `dwc:samplingProtocol-2026-10-13`, both Survey-scoped. The older 2023-06-28 and 2026-05-26 pins must not be used as the current terms.
- `dwc:occurrenceStatus-2026-05-26` remains the relevant term version and recommends `detected` / `notDetected`; GBIF v1.0.2 examples use `present` / `absent`, so any mapping remains profile-specific and must be tested.
- Humboldt term versions vary independently: notably `eco:Survey` and `eco:isTaxonomicScopeFullyReported` have 2026-10-13 term versions, while `eco:SurveyTarget` and `eco:isSurveyTargetFullyReported` remain 2026-05-26. The complete 2026-10-13 Humboldt snapshot still requires archival.
- GBIF v1.0.2 §7.3 explicitly uses taxonomic-scope reporting completeness and declared target/excluded scope for its implicit-absence recipe. It does not state that `eco:taxonCompletenessReported=reportedComplete` is a universal additional prerequisite. Any stricter Botanica Indica requirement must be labelled as project policy.

This correction changes standards evidence only. It does not change the recommended dispositions, close EVT-D01–D04, approve Candidate A, pass Task 05D or authorize Task 05E.

Source: [EVT-D01–D04 Standards Version Verification Addendum](EVT-D01-D04-STANDARDS-VERSION-VERIFICATION-ADDENDUM-2026-11-26.md).
