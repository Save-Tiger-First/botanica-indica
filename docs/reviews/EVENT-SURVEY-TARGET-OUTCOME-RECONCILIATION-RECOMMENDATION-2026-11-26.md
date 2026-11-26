# Event–Survey–Target Outcome Reconciliation — Focused Recommendation

**Document ID:** STF-BI-REV-FLD-002  
**Version:** 0.1  
**Prepared:** 26 November 2026  
**Status:** Proposed synthesis for owner and specialist review; NOT an approved scientific model  
**Review destination:** Existing PR #9 — `review/scientific-data-model-review-pack`  
**Decision authority:** Project owner, informed by qualified field ecology, botanical taxonomy, biodiversity-informatics and data-architecture review  
**Related review:** `TASK-05D-INDEPENDENT-VALIDATION-REVIEW-2026-11-26.md`

> **Decision boundary:** This document recommends a coherent direction for F-01 and F-02. It does not approve Task 05C Candidate A or B, close EVT-D01–EVT-D10, amend an accepted ADR, authorize Task 05D to pass, authorize Task 05E, freeze API contracts, or authorize physical database design.

---

## 1. Executive recommendation

Resolve F-01 and F-02 as one connected logical-model decision, using the following as the **preferred review hypothesis**:

1. Use a shared **Event identity** with mutually exclusive, typed specializations for **Survey** and **Occurrence**, while allowing generic contextual Events and other explicitly governed Event kinds.
2. Keep Botanica Indica **Observation** as a separate contributor-submission/workflow record. It is not automatically an Event or Occurrence.
3. Keep the **Event parent–child hierarchy**, **Survey-to-Occurrence reporting**, and **Observation-to-Event/Occurrence evidence links** as separate relationships with distinct meanings.
4. Treat **SurveyTarget** as a versioned, Survey-specific declaration of what was sought or later selected for analysis. Preserve a priori versus post-facto origin and the exact target scope.
5. Use **SurveyTargetAssessment** as the working name for an attributable assessment lifecycle record that captures whether/how a target was assessed, the assessment boundary, protocol, effort, coverage, completeness, limitations, evidence, agents and provenance.
6. Do not maintain two independently mutable detected/non-detected outcomes for the same taxonomic target assessment. For taxonomic/organismal detection and explicit non-detection, the linked **Occurrence** is the authoritative occurrence-level scientific record, reported by the Survey through **SurveyOccurrenceReport**.
7. **Important qualification:** not every possible SurveyTarget is taxonomic or organismal. Darwin Core allows targets based on environmental conditions and organismal traits as well as taxa. Therefore, Botanica Indica must not force every target outcome into an Occurrence. The model must provide a typed, attributable outcome/assertion path for non-occurrence target classes, preferably by reusing the existing ScientificAssertion / MeasurementOrFact pattern if it can represent the required semantics without a polymorphic integrity gap. If it cannot, a distinct typed target-outcome construct must be proposed and reviewed. This remains an open design question, not an approved new entity.

**Recommendation status:** Preferred direction for review. All related decisions remain OPEN until owner and specialist review and executable evidence.

## 2. Exact repository baseline

The governing AI Project Operating Prompt was fetched from `docs/governance/AI-PROJECT-OPERATING-PROMPT.md` on `docs/repository-audit-and-ai-operating-standard`, blob SHA:

`53add3894d0502827e584614c70ad09cadaa637d`

Live repository checked 26 November 2026:

- Repository: `Save-Tiger-First/botanica-indica`
- Branch count: 23. The owner-authorized immediate ceiling is seven branches total; the target is not met.
- Required long-lived branches: `main`, `develop`, `staging`.
- Existing review branch: `review/scientific-data-model-review-pack`, head before this document: `1be4836f5721e906bf8ef1805a1d481fa02972e1`.
- PR #9 is open and draft, based on `main`.
- PR #5 is open and draft; Candidate A head: `d443420d6b77815cb155f457ea262e621aabf7cb`.
- PR #11 is open and draft; Task 05D v3 head: `0577250c9e7cffcb3605acc782f403b7d1b422e0`, stacked on PR #5.
- No submitted reviews were found on PR #9, PR #5 or PR #11 in the current review checks.

Current source file blobs fetched for this review:

| Source | Branch | Blob SHA |
|---|---|---|
| Task 05C Candidate A | `docs/task-05c-logical-data-model` | `b447796e7da0d08d96400812667a8e67e0696144` |
| Task 05B Scientific Data Dictionary | `docs/task-05-data-dictionary` | `ddaa379d993fdf1f45684962930d16f06830ae43` |
| Event–Survey–Occurrence Conceptual Model Decision Paper | `review/scientific-data-model-review-pack` | `0a82ccd3e5de7642d53771877c7fbc896873123e` |
| EVT Decision and Validation Pack | `review/scientific-data-model-review-pack` | `4a317c4c83317e10663ba374e9e6be3100a53431` |
| Scientific Data Model Validation Matrix and Decision Register | `review/scientific-data-model-review-pack` | `3a33dfe47657a96456f56f2c12a0b7d355b6c6a5` |
| Task 05C Competing Model Reconciliation | `review/scientific-data-model-review-pack` | `e34eadf0257f38d81b4809e2477784045f460746` |
| Task 05D v3 | `docs/task-05d-logical-model-validation-v3` | `0b9a009b1c543b2450758f659c97cae3802a2f94` |

The earlier review pack and this document are preserved on the existing PR #9 branch. No new branch is created or authorized by this work.

## 3. F-01 — Event identity, Survey and Occurrence specializations

### 3.1 Verified source position

The current Candidate A main ERD and relationship summary still express Event-to-Occurrence as a contextual one-to-many relationship. Candidate A §18 proposes a shared Event identity with Survey and Occurrence specializations, but expressly says it does not supersede the earlier Candidate A content. Candidate A therefore contains two not-yet-reconciled patterns.

The Event–Survey–Occurrence decision paper and EVT pack prefer a shared Event identity/supertype with mutually distinct Survey and Occurrence specializations. The documents correctly distinguish this from Task 05C Candidate B; the phrase “Option B” in the conceptual decision paper is not the same as Candidate B's document.

The Darwin Core Conceptual Model describes Survey and Occurrence as special types of Event, but it is a conceptual semantic framework, not a prescribed relational database schema or inheritance implementation. Its sections other than document status are non-normative.

### 3.2 Recommended logical semantics

Use these distinctions:

| Concept | Responsibility | Must not be confused with |
|---|---|---|
| Event identity | Common identity and supported temporal, spatial, agent and contextual properties for an activity/process/circumstance | A universal container into which all field records are forced |
| Generic/context Event | A context such as monitoring programme, expedition, site visit or collection activity where supported | Survey or Occurrence specialization |
| Survey | A specialized Event with survey purpose/design, targets, protocol, effort, coverage and reporting context | A generic Event with an unstructured `eventType = Survey` string only |
| Occurrence | A specialized Event recording the state/detection context of an Organism or taxon at a place and interval, including a supported explicit non-detection | A user submission, a specimen, or an empty query result |
| Observation | Contributor-submitted evidence/workflow record | An automatic Event or Occurrence |
| Organism | Individual or defined group identity where scientifically meaningful and supported | A mandatory record for every plant image |
| MaterialEntity | Physical material such as a specimen, sample or collected plant part | Digital MediaAsset or Occurrence |

A single Event identity must not simultaneously be a Survey and an Occurrence. A generic/context Event may provide shared context to multiple distinct activity Events where the relationship is evidenced.

### 3.3 Keep the relationships separate

The logical model must contain distinct relationship semantics:

1. **Event parent–child hierarchy:** containment/nesting, e.g. programme → annual survey → plot visit. A child has at most one parent in the core hierarchy unless a separately justified relationship is defined. Parent spatial and temporal extents must encompass the child. This is not a reporting relationship.
2. **SurveyOccurrenceReport:** a Survey reports an Occurrence as a target-matching result, incidental/bycatch, or another governed role. This is not a parent–child relationship.
3. **ObservationEventLink:** an Observation documents or relates to an Event in a specified role.
4. **ObservationOccurrenceLink:** an Observation provides evidence for or documents an Occurrence.
5. **Event contextual association:** a separate typed link only where a real workflow requires context that is not adequately represented by parent–child containment. Do not create a generic many-to-many context link without a demonstrated use case.

Where a Survey reports an Occurrence and the Occurrence is also a child Event, both relationships may be recorded, but neither implies the other.

### 3.4 Proposed logical invariants

These are requirements for the logical model and fixtures, not physical SQL instructions:

- Every Survey specialization has exactly one Event identity.
- Every Occurrence specialization has exactly one Event identity.
- An Event identity has no more than one mutually exclusive specialization in the initial model.
- Event subtype and category must agree; a Survey Event cannot exist without its Survey specialization, and an Occurrence Event cannot exist without its Occurrence specialization.
- Generic/context Event has no Survey or Occurrence subtype record.
- An Event's parent–child hierarchy is acyclic.
- Parent–child spatial and temporal containment is validated using the precision and uncertainty of the source data; unknown bounds are not treated as exact.
- A Survey may report zero or many Occurrences.
- An Occurrence may be reported by more than one Survey only when the underlying event is legitimately the same and each report's scope/provenance is retained. Similar taxon/place/time values alone do not prove identity.
- Observation may exist without Event, Occurrence, Identification or Organism.
- MaterialEntity remains independent and may be collected during a contextual Event and/or provide evidence for an Occurrence.

**Important implementation caution:** the eventual database must enforce subtype exclusivity and required subtype participation. A diagram or a discriminator column alone is not sufficient evidence of integrity. The physical design must demonstrate a transaction-safe enforcement approach and migration/restore behavior.

## 4. F-02 — SurveyTarget, assessment and authoritative outcome

### 4.1 The naming conflict is substantive

Task 05B §16 and Candidate A §18 use `SurveyTargetResult` and currently include outcome states such as detected and explicit non-detected. The EVT pack and competing-model reconciliation use `SurveyTargetAssessment` for the assessment/completeness lifecycle.

The terms have been used for overlapping responsibilities. Keeping both as independently mutable records risks contradictory statements about the same Survey, target, place, time and assessment.

**Recommendation:** use `SurveyTargetAssessment` as the working canonical name for the assessment lifecycle. Treat `SurveyTargetResult` as superseded terminology for this purpose unless a distinct result object is justified by a concrete target class and workflow. Do not rename or delete historical terms without a controlled cross-document decision.

### 4.2 Separate declaration, assessment and outcome

| Layer | Proposed responsibility | Key semantics |
|---|---|---|
| SurveyTarget | What the Survey sought or later selected for analysis | Target type, scope, include/exclude criteria, version, origin (`A_PRIORI` / `POST_FACTO`), author, time, method, source and applicable Survey/Event scope |
| SurveyTargetAssessment | Whether/how the target was assessed in a bounded visit/period/scope | Assessment lifecycle, protocol, effort, spatial/temporal bounds, coverage, completeness dimensions, limitations, responsible agents, evidence and provenance |
| Occurrence | Taxon/organism-level occurrence state where the target/result is genuinely an organism/taxon occurrence | Canonical occurrence-level detection or explicit non-detection state, with its own Event identity and evidence |
| SurveyOccurrenceReport | Why/how a Survey reports an Occurrence | Target match, incidental/bycatch or other controlled reporting role |
| Non-occurrence target outcome | Result for a target that is not itself a taxon/organism occurrence | Typed assertion/measurement or another reviewed representation; do not fabricate an Occurrence |

### 4.3 Critical qualification: not every SurveyTarget is an Occurrence

Darwin Core Conceptual Model §2.2 says Survey Targets may be based on combinations of taxa, environmental conditions and organismal traits. It also says Survey results are expressed in the Occurrences the Survey reports, including bycatch and target-matching Occurrences. These statements do not mean every possible target's result is itself an Occurrence.

Examples:
- Target: “native tree taxa in the plot” — taxonomic/organismal; relevant positive or explicit non-detection results can be represented through Occurrence records.
- Target: “presence of a specified life stage” — may be organismal and can often be evidenced through an Occurrence plus trait/life-stage assertion.
- Target: “soil moisture above a threshold” — an environmental/measurement result; it is not a plant Occurrence.
- Target: “habitat condition or canopy-cover class” — may require a typed measurement or scientific assertion, not a taxon Occurrence.

Therefore, the EVT-D04 recommendation (assessment lifecycle plus Occurrence as the canonical positive/negative result) is suitable for taxonomic/organismal targets, but it is not a complete general-purpose model for all target classes. It must be qualified.

**Recommendation for the non-occurrence path:** first test whether the existing `ScientificAssertion` and `MeasurementOrFact` patterns can represent typed, attributable target outcomes linked to a SurveyTargetAssessment, with real subject integrity, units, method, time, location, evidence and provenance. If they can, reuse them rather than adding a duplicate target-result table. If they cannot, document the exact gap and propose a typed `SurveyTargetOutcome` or equivalent for specialist review. This is a design investigation, not authorization to add a new entity.

### 4.4 Assessment state must not duplicate the taxon-level outcome

For taxonomic/organismal target assessments:

- `SurveyTargetAssessment` records whether assessment occurred and the assessment's quality/completeness context.
- A completed assessment with one or more positive detections links to one or more positive Occurrence Events.
- A defensible explicit non-detection links to a canonical Occurrence Event with the appropriate non-detection state and target/taxon scope.
- An unassessed, incomplete or indeterminate assessment does not create a negative Occurrence.
- The same assessment must not carry a separately editable `DETECTED` / `NOT_DETECTED` summary that can contradict the linked Occurrence records.
- If a user interface needs a summary status, derive it from the authoritative evidence/outcome records or record it as a non-authoritative, versioned projection with explicit reconciliation rules.

For non-occurrence target classes, a typed outcome assertion/measurement may be necessary. It must not be confused with an Occurrence and must retain the target/assessment relationship.

### 4.5 Scope and target versioning

A SurveyTarget must preserve the target scope as declared/applied at the relevant time. In particular:

- distinguish a priori intent from post-facto analytical filtering;
- preserve exact inclusion and exclusion criteria;
- preserve taxonomic concept/treatment versions where a target is taxonomic;
- do not dynamically reinterpret historical targets merely because a source taxonomic treatment changes;
- distinguish the target definition from a reusable target template, if reuse across Surveys is needed;
- bind each assessment to the exact target version and bounded Survey/visit/period;
- do not silently inherit target scope or completeness through Event parent–child hierarchy.

## 5. Canonical example workflows and expected semantics

| Scenario | Expected model result | Must not happen |
|---|---|---|
| Fixed-plot Survey; target tree detected twice | One SurveyTarget; one assessment; two supported positive Occurrence Events; SurveyOccurrenceReport links with target-match role | One duplicated aggregate outcome treated as a third scientific record |
| Fixed-plot Survey; taxon target assessed and not detected | One complete assessment; one explicit taxon-level non-detection Occurrence; Survey report link; evidence/protocol/effort/bounds retained | Treating the empty Occurrence table as the negative result |
| Survey target not assessed | Assessment records not-assessed state if the workflow requires it; no negative Occurrence | Translating not-assessed into notDetected |
| Survey incomplete due to weather/access | Incomplete assessment with reason/limitations; no negative Occurrence | Treating incomplete as complete non-detection |
| Target detected incidentally/bycatch | Positive Occurrence reported as incidental/bycatch | Claiming it was an a priori target or using it to infer target absence |
| No predeclared target, broad inventory | Survey remains valid; Occurrences may be reported; no target-specific absence inference without justified scope | Fabricating a SurveyTarget retrospectively as original field intent |
| Habitat or soil-condition target | Typed assessment outcome via assertion/measurement path, if supported | Fabricating a taxon Occurrence to hold an environmental measurement |
| Same taxon, not detected in visit 1 and detected in visit 2 | Distinct assessment periods and Occurrence Events retained | Overwriting the earlier non-detection |
| One Observation depicts several plants | One Observation can support several Occurrences through typed links | Assuming one image equals one Occurrence or one Organism |
| One context Event supports a survey and specimen collection | Context Event and activity Events remain distinct, with justified hierarchy/context links | Conflating context, collection and Survey reporting |

## 6. Minimum acceptance tests before the logical model can be reconciled

All cases below are **proposed, not executed**. Each requires a synthetic fixture, expected entity graph, positive and negative assertions, reproducible test output and review attribution.

### Event identity and relationships
1. Generic context Event with no specialization.
2. Survey Event with exactly one Survey specialization.
3. Occurrence Event with exactly one Occurrence specialization.
4. Reject an Event simultaneously specialized as Survey and Occurrence.
5. Reject a Survey specialization without a parent Event identity.
6. Reject an Occurrence specialization without a parent Event identity.
7. Parent–child Event hierarchy with valid spatial/temporal containment.
8. Reject a hierarchy cycle and a child extent outside its parent where evidence supports comparison.
9. SurveyOccurrenceReport exists without parent–child relationship.
10. Parent–child relationship exists without SurveyOccurrenceReport.
11. Same Occurrence reported by multiple Surveys with independent scope/provenance.
12. Observation exists without Event or Occurrence.
13. Observation links to multiple Occurrences and multiple media assets.
14. MaterialEntity and MediaAsset remain distinct.

### Target and assessment
15. A priori target with immutable scope/version.
16. Post-facto target filter that does not rewrite original survey intent.
17. Taxonomic target bound to a specific TaxonConcept/treatment version.
18. Repeated assessments for different visits/periods without overwriting history.
19. Complete assessment with multiple positive Occurrences.
20. Complete assessment with explicit non-detection Occurrence.
21. Incomplete assessment cannot produce a negative Occurrence.
22. Not-assessed target cannot produce a negative Occurrence.
23. Indeterminate assessment cannot produce a negative Occurrence.
24. Bycatch is reported but is not used to infer target absence.
25. Empty Occurrence set with no explicit assessment remains unknown/not assessed.
26. Non-taxonomic target with a typed measurement/assertion result and no fabricated Occurrence.
27. Assessment correction/retraction preserves the original assertion and audit trail.
28. No independently editable contradictory outcome exists between assessment and Occurrence.

### Interoperability and ODR-01
29. Explicit internal non-detection mapping to the selected pinned profile.
30. Implicit external interpretation only when the ODR-01 conditions and exact selected profile permit it.
31. Missing, ambiguous, contradictory or unpinned scope/completeness evidence fails closed.
32. Taxonomic-scope completeness, target-level reporting completeness, taxonomic completeness, effort and detectability are separate dimensions.
33. Bycatch excluded from implicit absence inference.
34. Round-trip test records any loss and does not create an internal negative Occurrence from an export-only interpretation.

## 7. Standards and research findings checked 26 November 2026

### 7.1 Darwin Core Conceptual Model

The TDWG landing page metadata reports a 2026-10-13 version IRI, while the human-readable page retrieved in this review displayed the 2026-05-26 version. The page explains that the Conceptual Model is a high-level framework, does not prescribe a particular technology or database implementation, and that all sections other than document status are non-normative. The 2026-05-26 page's Survey section states that targets may concern taxa, environmental conditions or organismal traits and that Survey results are expressed through reported Occurrences.

**Review treatment:** use the model as semantic guidance, not as a mandate for a specific SQL inheritance pattern. Keep exact-version retrieval and term/profile pinning under DR-09 until the 2026-10-13 versioned resource and relevant terms can be reproducibly compared.

Sources:
- https://dwc.tdwg.org/cm/
- https://dwc.tdwg.org/cm/2026-05-26.html
- https://rs.tdwg.org/dwc/doc/cm/2026-10-13

### 7.2 Darwin Core List and term-level semantics

The directly retrieved List page displays version 2026-05-26. The current `dwc:occurrenceStatus` term version referenced in project research is 2026-05-26, with recommended values `detected` and `notDetected`. A vocabulary snapshot date must not be substituted for each individual term's version.

Source:
- https://dwc.tdwg.org/list/
- http://rs.tdwg.org/dwc/terms/version/occurrenceStatus-2026-05-26

### 7.3 GBIF survey publishing guide

GBIF's Guide for publishing biological survey and monitoring data to GBIF, v1.0.2 (2025-09-24), distinguishes explicit absence records from implicit absence interpretation. Its implicit pattern depends on fully reported taxonomic scope and specified target/excluded scope; it also states that absences cannot be asserted for bycatch. This is a publishing guide, not an internal database schema. Its example literals must not be assumed identical to Darwin Core recommended values without a versioned, tested profile mapping.

Source:
- https://docs.gbif.org/guide-publishing-survey-data/en/

### 7.4 PostgreSQL integrity implications

PostgreSQL documents that CHECK constraints should not reference other rows/tables; they cannot guarantee cross-row invariants. Appropriate foreign keys, unique constraints, or carefully designed triggers may be needed. This matters for eventual Event subtype exclusivity and total participation, but physical enforcement is deliberately deferred.

Source:
- https://www.postgresql.org/docs/current/ddl-constraints.html

## 8. Decisions that remain open

The following must not be marked accepted by this document:

- EVT-D01: Event identity and specialization.
- EVT-D02: Event hierarchy versus contextual association.
- EVT-D03: Survey and SurveyTarget identity/scope.
- EVT-D04: target assessment and canonical outcome.
- EVT-D05: explicit versus implicit non-detection and export mapping.
- EVT-D06 onward: SurveyOccurrenceReport cardinality/role, Observation links, Organism optionality, protocol/effort/completeness and related boundaries.
- B01, B02, B16, DR-07, DR-09, LDM-16 and FLD-08.
- Whether existing ScientificAssertion / MeasurementOrFact can support non-occurrence target outcomes without a new typed construct.
- The exact Event subtype integrity pattern and its transaction-safe physical enforcement.
- The selected GBIF publishing profile and exact term mappings.

## 9. Recommended next actions

1. Ask the project owner and qualified reviewers to review this joint F-01/F-02 proposal, particularly the non-taxonomic target qualification.
2. Record explicit dispositions for EVT-D01 through EVT-D04; do not treat a recommendation as a decision.
3. If accepted in principle, produce one clean canonical Candidate A ERD and relationship table that removes the conflicting contextual Event→Occurrence interpretation while preserving history.
4. Reconcile Task 05B terminology and scope without deleting historical content or changing approved scientific decisions silently.
5. Align Task 05D's EVT/LDM/FLD fixture definitions with the approved logical semantics.
6. Execute synthetic tests and record evidence.
7. Re-review the stacked PR #11 dependency after Candidate A changes.
8. Reassess Task 05D readiness only after model coherence, tests and specialist reviews are evidenced.

**Task 05E remains NOT READY.** No physical schema, DDL, migrations, API payload freeze or implementation is authorized by this proposal.

## 10. Work not performed

- No accepted ADR, scientific model or product requirement was amended.
- No decision EVT-D01–EVT-D10 was approved or closed.
- No Task 05B, Task 05C or Task 05D source document was changed.
- No tests were executed.
- No specialist or legal review was obtained.
- No external party was contacted.
- No PR was merged, closed or retargeted.
- No branch was created or deleted.
- No repository protections or settings were changed.
- No physical schema or application code was created.

**End of document — STF-BI-REV-FLD-002 v0.1.**
