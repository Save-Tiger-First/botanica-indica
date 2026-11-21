# Event–Survey–Occurrence Decision and Validation Pack

- **Project:** Botanica Indica — Save Tiger First
- **Document type:** Scientific/domain-model review pack
- **Version:** 1.0
- **Prepared:** 21 November 2026
- **Status:** Proposed for specialist review; not approved
- **Review branch:** \`review/scientific-data-model-review-pack\`
- **Related PR:** [PR #9](https://github.com/Save-Tiger-First/botanica-indica/pull/9)

> **Decision status warning:** This document is a structured proposal and review instrument. It does not approve Option B, amend an accepted ADR, approve Task 05C, authorize Task 05E, freeze an API contract, or authorize physical database design. Decision IDs EVT-D01–EVT-D10 remain OPEN until the required disciplines provide attributable decisions and evidence.

---

## 1. Purpose

This pack turns the existing Event–Survey–Occurrence discussion into a reviewable set of ten decisions, worked workflows, cardinality hypotheses and 22 acceptance scenarios.

Its purpose is to resolve scientific and domain semantics before physical database design. It is not a physical schema, implementation specification or replacement for the Task 05C logical model.

The pack addresses a material gap found during the current repository audit: both Task 05C candidate documents model Event and Occurrence but do not yet express the complete Survey / SurveyTarget / completeness semantics required for robust ecological inventory and monitoring workflows. Task 05D v3 has an EVT decision register and 18 initial Event scenarios, but the non-detection identity and updated Humboldt Extension semantics require further explicit treatment.

## 2. Authority, source documents and evidence baseline

### 2.1 Repository documents inspected

The following are the exact document versions inspected for this review. Blob SHAs are recorded so later reviewers can reproduce the comparison.

| Document | Branch | Blob SHA | Relevance |
|---|---|---|---|
| AI Project Operating Prompt | \`docs/repository-audit-and-ai-operating-standard\` | \`61059c74d4d20309ff76e055059ab33f381ca4f2\` | Governing operating rules |
| Event–Survey–Occurrence Decision Paper | \`review/scientific-data-model-review-pack\` | \`eb513cde11f3013c31102318c78e278bc274ec91\` | Existing semantic alternatives, workflows and EVT decisions |
| Scientific Data Model Validation Matrix | \`review/scientific-data-model-review-pack\` | \`5eeff39d5362a70ca43b6711062742526b733dc1\` | Cross-document decisions and test status |
| Task 05C Competing Model Reconciliation | \`review/scientific-data-model-review-pack\` | \`eeb15a19f93df5b4feaee3b2b0481b24a59d3c23\` | Candidate comparison and DR-01–DR-12 |
| Task 05C Candidate A | \`docs/task-05c-logical-data-model\` | \`4a21c0aa3b8ebfef319a9ea1ac6928274b0b3f5b\` | Current PR #5 logical model |
| Task 05C Candidate B | \`docs/task-05c-logical-database-model\` | \`239d7e9974bcb81b1154b54845a7b2d69c3775d6\` | Alternative model in PR #21 |
| Task 05D v3 | \`docs/task-05d-logical-model-validation-v3\` | \`cf0b9c10bcb2da7b102e52688f22bd8e8b69bb91\` | Current Task 05D validation/readiness proposal in PR #11 |
| Task 05D v2 | \`docs/task-05d-logical-model-validation-v2\` | \`acf446b1bf0204fa0400621711603ab23cc80ff2\` | Preserved alternative; not the current v3 baseline |
| Scientific Data Dictionary | \`docs/task-05-data-dictionary\` | \`eda2608e3d2281299d62ebf85bf16a2d2e796411\` | Entity and Indian test-case context |
| Task 05B data architecture | \`docs/task-05-data-architecture\` | \`a3255dcf2d1bd4dfa982b381b061051b6c2c8b0b\` | Domain baseline and earlier model decisions |
| ADR-005 Taxonomy Reconciliation | \`review/scientific-data-model-review-pack\` | \`b61dcf0b9ba58fc35da5cc7ba5edfbdd5f2909e4\` | Accepted source-aware taxonomy decision |
| ADR-007 Evidence and Expert Validation | \`review/scientific-data-model-review-pack\` | \`7ba4874b4175707b69dc3052822f8cbeb5384b0a\` | Accepted evidence and review principles |

The accepted status of ADR-005 and ADR-007 is preserved. This pack does not modify or reinterpret their decisions.

### 2.2 Current standards baseline checked on 21 November 2026

| Resource | Version / term-level finding | Use in this review |
|---|---|---|
| Darwin Core Conceptual Model | Version issued 2026-10-13; IRI: \`http://rs.tdwg.org/dwc/doc/cm/2026-10-13\` | Event, Survey, Occurrence and conceptual relationship semantics |
| Darwin Core List of Terms | Version issued 2026-10-13; IRI: \`http://rs.tdwg.org/dwc/doc/list/2026-10-13\` | Current consolidated vocabulary list |
| Hierarchical Events guidance | Version issued 2026-10-13; IRI: \`http://rs.tdwg.org/dwc/doc/hierarchy/2026-10-13\` | Parent/child Event hierarchy and Humboldt application |
| Darwin Core schemas | Version issued 2026-10-13; IRI: \`http://rs.tdwg.org/dwc/doc/schemas/2026-10-13\` | Exchange schema reference; not an internal database design |
| Darwin Core occurrenceStatus | Term version remains 2026-05-26; IRI: \`http://rs.tdwg.org/dwc/terms/version/occurrenceStatus-2026-05-26\` | Term recommends detected / notDetected as default values |
| Humboldt eco:Survey | Current term version 2026-10-13; 2026-05-26 version is superseded | Survey class semantics |
| Humboldt eco:SurveyTarget | Term version 2026-05-26 | Target scope definition for Occurrences in a Survey |
| Humboldt eco:isSurveyTargetFullyReported | Term version 2026-05-26 | Target-level completeness and possible implicit non-detection inference |
| Humboldt eco:absentTaxa | Current term version 2026-10-13 | Absent taxa list associated with an eco:Survey |
| Humboldt scope/completeness terms | Multiple terms updated to 2026-10-13; pin each term separately | Do not infer term version from list publication date |

**Versioning rule:** publication date of a document/list and modification/version date of an individual term are different. Pin exact document IRIs and exact term-version IRIs. A cached page rendering with a 2026-05-26 header was encountered during retrieval; current TDWG metadata identifies the 2026-10-13 publication/list versions. The older page rendering must not be treated as evidence that the newer release does not exist.

### 2.3 Important standards distinctions

1. The Darwin Core Conceptual Model is a high-level semantic reference, not a prescribed database schema or implementation blueprint.
2. Survey and Occurrence are specialized Event concepts with distinct characteristics. A generic contextual Event may provide shared context to multiple related activities, but one Event instance must not be treated as an arbitrary combination of incompatible specialized records.
3. The Event parent/child hierarchy expresses a hierarchical sampling/event structure. It is not the same relationship as a Survey reporting an Occurrence.
4. The Humboldt Extension defines an eco:Survey class and an eco:SurveyTarget class. Do not reduce these to an unstructured text field or assume that the string value dwc:eventType = Survey is identical to the eco:Survey class.
5. A Survey may exist without a predeclared taxonomic/organismal target; absence inference requires a defined and sufficiently complete scope.
6. The current dwc:occurrenceStatus term recommends detected and notDetected. GBIF's Guide for publishing biological survey and monitoring data v1.0.2 (2025-09-24) describes explicit zero-count absence records using absent and examples present/absent. These values must be treated as profile/version-specific mapping choices, not silently equated.
7. GBIF guidance permits implicit absence interpretation in a published dataset only when the applicable target/scope and completeness conditions are met. That is an export interpretation, not permission for Botanica Indica to silently create an internal scientific absence assertion from an empty table.

## 3. Existing model audit: what is present and what is missing

### 3.1 Task 05C Candidate A

Candidate A currently has:
- Observation, Event, Organism, Occurrence and MaterialEntity as distinct concepts.
- Event-to-Occurrence contextualization.
- Observation-to-Occurrence associative links.
- Event-to-MaterialEntity collection relationships.
- Explicit statement that a missing Occurrence row is not evidence of absence.
- Explicit non-detection as a possible Occurrence state when tied to a defined Survey/Event, protocol, effort, target and location.

**Gap:** it does not yet define Survey, SurveyTarget, a survey-specific completeness object, Survey-to-Occurrence reporting roles or the distinction between explicit non-detection and export-level implicit absence.

### 3.2 Task 05C Candidate B

Candidate B currently has:
- Observation grouping zero or more Events.
- Event establishing zero or more Occurrences.
- Event gathering zero or more MaterialEntities.
- A generic Event definition that includes field visit, photograph capture, collection event or survey.
- Observation, Event, Occurrence and MaterialEntity cardinality statements.

**Gap:** it also lacks an explicit Survey specialization/record, SurveyTarget model, target-level completeness, explicit SurveyOccurrenceReport semantics and a governed non-detection model. Its broad Event description does not by itself supply those semantics.

### 3.3 Task 05D v3

Task 05D v3 contains:
- EVT-D01 to EVT-D10 reviewer decision prompts.
- EVT-01 to EVT-18 proposed scenarios.
- FLD-08 for a defined survey failing to detect a target taxon.
- DR-07 discussion of explicit absent/non-detected Occurrence state.
- A requirement that internal validity and GBIF export readiness remain distinct.

**Gap:** EVT-09 and EVT-18 do not yet settle whether the target assessment and the taxon-specific non-detection Occurrence are one record or separate linked records. EVT-19 to EVT-22 are required to test this. The current Task 05D v3 PR remains stacked on Task 05C Candidate A and must be re-reviewed against the final accepted model.

### 3.4 ADR constraints

Accepted ADR-005 requires source-aware, versioned taxonomic reconciliation and forbids silent overwriting of source-specific taxonomic interpretations.

Accepted ADR-007 requires evidence to be first-class, attributable and provenance-preserving; conflicting evidence and expert assessments must not silently overwrite earlier statements.

Consequences:
- A SurveyTarget taxon must preserve the taxonomic concept/treatment and source/version used to define it.
- A later taxonomic reclassification must not silently rewrite the historical scope of an earlier Survey.
- A Survey's historical target must remain interpretable against the taxonomic treatment applicable when the target was defined or assessed.
- Evidence for a positive or negative result must remain attributable and versioned.
- An AI candidate or missing data must never be promoted into a scientific non-detection assertion.

## 4. Proposed conceptual model direction

### 4.1 Recommended model hypothesis

**Recommendation for review, not an approved decision:**

1. Retain Event as the common event identity and shared event-property concept.
2. Represent a Survey as a distinct specialized Event with survey-specific purpose, scope, targets, protocol, effort and completeness semantics.
3. Represent an Occurrence as a distinct specialized Event representing a taxon/organism state at a bounded place and interval, including a supported taxon-specific non-detection.
4. Use a separate generic contextual Event where one expedition, site visit, plot visit or collection context provides common context to several Survey/Occurrence/MaterialEntity records.
5. Keep the contextual Event distinct from the Survey and Occurrence identities it contextualizes.
6. Keep Observation as a contributor workflow/submission record. It is not automatically an Event, Survey or Occurrence.
7. Keep MaterialEntity and MediaAsset distinct.
8. Use SurveyTarget to describe declared target scope. Do not limit targets to species names: taxonomic, habitat, organismal, life-stage, growth-form, establishment, trait/measurement and other supported scopes may be relevant.
9. Use a proposed internal SurveyTargetAssessment (working name) to preserve whether a target was assessed, the assessment boundary, completeness and evidence. It must not duplicate the authoritative occurrence outcome.
10. Use SurveyOccurrenceReport as an explicit typed association between a Survey and an Occurrence. Do not overload Event parent/child hierarchy to express reporting.

### 4.2 Event identity and contextual Event distinction

The model must distinguish three things:

- **Event identity:** the real-world activity/interval being represented.
- **Specialized Event record:** Survey or Occurrence attributes attached to that Event identity.
- **Contextual Event:** a separate broader Event (e.g., expedition, project, site visit) that supplies context to one or more more-specific Events or material collection activities.

A shared contextual Event can be associated with multiple Occurrences and MaterialEntities. That does not mean the same Event identity is simultaneously a Survey, Occurrence and MaterialEntity.

### 4.3 Proposed relationships and cardinality hypotheses

These are candidate cardinalities for review, not database constraints already approved.

| Relationship | Proposed cardinality | Notes / validation needed |
|---|---|---|
| Event parent → child Event | One parent to zero or many children; each child has zero or one parent in strict hierarchy | Parent/child is containment/hierarchy, not Survey reporting |
| Event context → contextualized Event | One contextual Event may provide context to many Events; an Event may have zero or more typed context links | Separate typed association if the relationship is not true parent/child; prevent cycles where relevant |
| Event → Survey specialization | An Event identity has zero or one Survey specialization | Survey has exactly one Event identity; do not duplicate common Event properties |
| Event → Occurrence specialization | An Event identity has zero or one Occurrence specialization | Occurrence has exactly one Event identity; no multiple incompatible specializations on the same identity |
| Survey → SurveyTarget | One Survey may declare zero or many SurveyTargets | Zero-target inventory remains valid but cannot support target-specific absence claims |
| SurveyTarget → SurveyTargetAssessment | One target may have zero or many assessment instances across applicable visits/periods | Repeated visits must not overwrite earlier assessments |
| SurveyTargetAssessment → Occurrence | One assessment may relate to zero or many Occurrences | Detected result may link to one or many positive Occurrences; explicit non-detection should link to a single canonical negative Occurrence for the defined assessment scope unless a documented scope split requires more |
| Survey → SurveyOccurrenceReport | One Survey may report zero or many Occurrences | Includes target-matching and incidental/bycatch reports |
| Occurrence → SurveyOccurrenceReport | One Occurrence may be reported by zero or many Surveys | Reuse only when the same underlying occurrence is legitimately within multiple surveys; do not merge separate detections merely because taxon/place/time are similar |
| Observation → ObservationEventLink | One Observation may link to zero or many Events | No forced Event when capture context is unknown |
| Observation → ObservationOccurrenceLink | One Observation may support zero or many Occurrences | A photo may document several plants; an Occurrence may have multiple independent Observation submissions |
| Event → MaterialEntity | One Event may gather zero or many MaterialEntities | MaterialEntity remains physical material |
| Occurrence → Organism | Zero or one Organism in the initial model is a candidate, not a final universal rule | A non-detection Occurrence has no positive Organism instance; group/aggregate semantics need review |

### 4.4 Relationship semantics that must never be conflated

- Event parent/child hierarchy ≠ SurveyOccurrenceReport.
- Event contextualization ≠ Event hierarchy unless containment semantics genuinely apply.
- SurveyTarget declaration ≠ SurveyTarget assessment.
- SurveyTarget assessment/completeness ≠ Occurrence outcome.
- Observation submission ≠ real-world Event.
- Observation submission ≠ Occurrence.
- Occurrence ≠ Organism.
- Occurrence ≠ MaterialEntity.
- MediaAsset ≠ MaterialEntity.
- Explicit non-detection ≠ missing Occurrence row.
- Export-level implicit absence ≠ a stored internal non-detection record.
- Incidental/bycatch detection ≠ target-matching detection.
- Not assessed ≠ assessed and not detected.

## 5. Ten decisions for specialist review

All ten decisions remain **OPEN**. The recommended disposition is a proposal only.

### EVT-D01 — Event identity, contextual Event and specialized Event semantics

**Question:** Should Botanica Indica use a shared Event identity with distinct Survey and Occurrence specializations, while representing broader context as a separate generic Event?

**Options:**
- A. Separate Survey and Occurrence records with only loose, generic links to Event.
- B. Shared Event identity/common properties, Survey and Occurrence specializations, plus separate generic contextual Event records.
- C. One generic Event record with a type field and no distinct specialized records.
- D. Another model with explicit semantic mapping and demonstrated loss analysis.

**Recommendation:** B.

**Reason:** It preserves shared event properties while keeping Survey and Occurrence semantics distinct. Option C risks flattening distinct lifecycle/attribute requirements into a type string. Option A risks duplicated time/location/agent context and weak event identity. Candidate B's generic Event language alone does not yet implement Survey targets or completeness.

**Acceptance evidence:**
- A mapping of the current Darwin Core Conceptual Model and Humboldt Survey class.
- Repeated-survey, shared-context, multi-occurrence and specimen workflows.
- Demonstration that one Event identity cannot accidentally carry incompatible specialized records.
- A clear distinction between contextual Event and specialized Survey/Occurrence Event.

**Required reviewers:** field ecologist, biodiversity informatician, data architect.

### EVT-D02 — Event hierarchy versus contextual association

**Question:** When is a parent/child Event relationship appropriate, and when is a separate contextual association required?

**Options:**
- A. Use parentEventID for every Event association.
- B. Use parent/child only for genuine hierarchical containment; use a typed context link for other relationships.
- C. Use only flat Events and generic links.

**Recommendation:** B.

**Reason:** Parent/child hierarchy is a sampling/event structure. It must not be overloaded to mean "reported by", "same site", "same expedition" or "same observation context". A child Event has at most one parent in the strict hierarchy. Context links may have different cardinalities and semantics.

**Acceptance evidence:**
- One project containing multiple expeditions, surveys, visits and plots.
- One contextual Event supporting multiple Occurrences and MaterialEntities.
- A test for multiple parents and cycle prevention.
- Proof that protocol, effort, target and completeness are not silently inherited.

**Required reviewers:** field ecologist, biodiversity informatician, data architect.

### EVT-D03 — Survey identity and SurveyTarget scope

**Question:** How should Survey and SurveyTarget be represented, and what forms of target scope must be supported?

**Options:**
- A. Survey is only a string value in Event.eventType.
- B. Survey is a distinct specialization/record with SurveyTarget records and versioned scope values.
- C. A generic Survey JSON payload with no enforceable target structure.

**Recommendation:** B, while mapping eventType separately where required by the export profile.

**Reason:** Humboldt defines eco:Survey and eco:SurveyTarget. A SurveyTarget can express one or more scopes; it is not limited to a single species identifier. Target scope may include taxon, habitat, establishment means, growth form, sex, life stage, minimum/maximum dimensions and other supported categories.

**Acceptance evidence:**
- A botanical survey targeting native trees but excluding planted/invasive forms.
- A habitat-level survey with no single target taxon.
- A Survey with no declared targets that remains valid but cannot support target-specific absence inference.
- Historical target scope remains stable when a TaxonConcept or source treatment changes.
- Include/exclude scope logic is explicit and reproducible.

**Required reviewers:** botanist, field ecologist, biodiversity informatician.

### EVT-D04 — Canonical identity of target assessment and non-detection

**Question:** Is SurveyTargetResult the non-detection record, or is it a separate assessment record related to a canonical Occurrence?

**Options:**
- A. SurveyTargetResult itself is the sole authoritative negative scientific record; it is mapped to Occurrence only during export.
- B. SurveyTargetAssessment records assessment/completeness; Occurrence is the canonical positive or explicit negative scientific result.
- C. Occurrence alone stores all assessment and completeness information, with no separate target assessment.
- D. A different model supported by worked examples and explicit lifecycle semantics.

**Recommendation:** B, subject to specialist validation. Use SurveyTargetAssessment as a working name; do not silently rename an accepted model entity.

**Reason:** The assessment lifecycle and completeness evidence have a distinct purpose from the occurrence-level scientific state. The current Conceptual Model and GBIF survey guide express survey results through Occurrences. A separate assessment record can explain why a negative Occurrence is justified, without duplicating its outcome in two independently mutable records.

**Proposed rule:**
- The assessment record captures the target, survey/visit boundary, whether assessment occurred, completeness, protocol/effort references, responsible agents, evidence and limitations.
- The Occurrence record carries the authoritative occurrence state, including explicit non-detection where justified.
- A completed assessment with positive detections links to one or more positive Occurrences.
- A completed assessment with a defensible explicit non-detection links to the corresponding negative Occurrence.
- An unassessed, incomplete or indeterminate assessment must not create a negative Occurrence.
- The same target/scope/assessment must not have contradictory independently mutable outcomes.

**Acceptance evidence:**
- A complete target assessment with no detection.
- An incomplete target assessment.
- A target not assessed.
- A positive target result with multiple Occurrences.
- A single canonical outcome with no duplicated conflicting state.
- An audit trail for correction/retraction of an erroneous negative record.

**Required reviewers:** field ecologist/survey-method specialist, botanist, biodiversity informatician.

### EVT-D05 — Explicit versus implicit non-detection and external representation

**Question:** Which non-detection states are stored internally, and which are derived only for a selected export profile?

**Options:**
- A. Treat every missing Occurrence as absence.
- B. Store explicit non-detection only when supported by an assessment; permit profile-specific implicit absence inference only when the exact scope/completeness conditions are satisfied.
- C. Never support implicit absence in any export.

**Recommendation:** B.

**Reason:** A missing record is unknown internally. However, GBIF/Humboldt publishing guidance supports implicit absence interpretation where target scope and completeness metadata allow it. The system must distinguish internal assertion from downstream inference.

**Acceptance evidence:**
- Explicit negative Occurrence fixture.
- Complete target scope with all detected Occurrences reported, supporting an export-level implicit absence calculation.
- Incomplete scope where implicit absence is prohibited.
- Bycatch excluded from absence inference.
- A round-trip test showing no unrecorded internal negative assertion is created by export.

**Required reviewers:** biodiversity informatician, survey-method specialist, data architect.

### EVT-D06 — SurveyOccurrenceReport cardinality and role

**Question:** Can one Occurrence be reported by multiple Surveys, and how are target-matching versus incidental/bycatch reports represented?

**Options:**
- A. Each Occurrence belongs to exactly one Survey.
- B. SurveyOccurrenceReport is an associative record; one Survey reports many Occurrences and an Occurrence may be reported by multiple Surveys where the same underlying event is genuinely shared.
- C. Duplicate Occurrences for every Survey regardless of whether the underlying occurrence is the same.

**Recommendation:** B, with strict evidence and identity rules.

**Reason:** It preserves independent Survey reporting context while avoiding artificial duplicate Occurrences. The link must carry the report role and any target association. A bycatch Occurrence is a detection outside the declared target scope; it must not be reclassified as a target or used to assert its absence.

**Acceptance evidence:**
- One Survey reports multiple target-matching Occurrences.
- One Survey reports incidental/bycatch Occurrence.
- Two overlapping Surveys legitimately reference the same underlying Occurrence.
- Two independent detections at similar places/times remain distinct where evidence shows they are separate.
- No absence claim is made for bycatch.

**Required reviewers:** ecologist, biodiversity informatician, field botanist.

### EVT-D07 — Observation/Event/Occurrence relationships

**Question:** What cardinalities and link roles are required between contributor Observations, Events and Occurrences?

**Options:**
- A. One Observation equals one Event equals one Occurrence.
- B. Separate identities with explicit links supporting zero-to-many and many-to-many cases.
- C. Observation is the only field record and Event/Occurrence are derived views.

**Recommendation:** B.

**Reason:** A single photograph may show several plants; one Occurrence may have multiple independent submissions; imported specimen records may have no platform Observation; some Observations have insufficient context to create an Event or Occurrence.

**Acceptance evidence:**
- One Observation with three distinct supported Occurrences.
- Multiple Observations supporting one Occurrence.
- Observation without known Event context.
- Historical herbarium record without a platform Observation.
- No forced taxon, Organism or Occurrence from an unreviewed AI candidate.

**Required reviewers:** field botanist, product/domain architect, biodiversity informatician.

### EVT-D08 — Organism optionality and group/aggregate treatment

**Question:** How should the model handle an individual, colony, clone, population/group, multiple organisms and non-detection?

**Options:**
- A. Require one Organism for every Occurrence.
- B. Permit optional Organism identity; represent taxonomically homogeneous groups where identity is useful; represent absence without a positive Organism instance.
- C. Replace Organism with an untyped count field.

**Recommendation:** B.

**Reason:** Darwin Core distinguishes Organism, Occurrence and MaterialEntity. An Organism may be a biological individual or a defined taxonomically homogeneous group such as a clone or colony. A non-detection result has no positive Organism identity merely because it is an Occurrence.

**Acceptance evidence:**
- Known individual plant tracked across multiple Occurrences.
- Clonal colony or homogeneous group.
- Unidentified individual.
- Multiple taxa in one image represented by separate Occurrences where evidence supports them.
- Negative Occurrence linked to a taxon/target, with no fabricated Organism.

**Required reviewers:** botanist, field ecologist, biodiversity informatician.

### EVT-D09 — Location, time, protocol, effort and completeness

**Question:** What context is necessary for a defensible survey result, and what may or may not be inherited across Event hierarchy levels?

**Options:**
- A. Inherit protocol, effort, location and time from parent Event automatically.
- B. Preserve event-specific values and explicit applicability; no silent inheritance; allow documented unknown/not-applicable/withheld states.
- C. Require all values on every Event even when scientifically unavailable.

**Recommendation:** B.

**Reason:** Event hierarchy is not a license to infer missing properties. The Humboldt hierarchical-event guidance and GBIF quick-start guidance require relevant protocol and scope values to be supplied at each applicable Event level; protocol inheritance in either direction must not be assumed. Completeness is multi-dimensional and scope-specific.

**Acceptance evidence:**
- Parent project and child surveys with different protocols.
- Repeated plot visits with different effort and duration.
- Unknown or generalized location.
- Historical date with year/month precision only.
- Incomplete effort record that cannot support non-detection.
- Scope completeness explicitly distinguished from protocol completion and data publication completeness.

**Required reviewers:** ecologist, geospatial specialist, biodiversity informatician, privacy reviewer.

### EVT-D10 — Standards versions, term mappings and publishing profiles

**Question:** Which Darwin Core/Humboldt term versions and GBIF profiles govern exchange, and how are internal states mapped without loss?

**Options:**
- A. Hard-code one vocabulary and profile throughout the domain model.
- B. Keep internal semantics stable and use a versioned mapping registry for each external profile.
- C. Avoid interoperability mapping.

**Recommendation:** B.

**Reason:** The current Darwin Core term recommends detected/notDetected, while GBIF's survey guide v1.0.2 uses present/absent examples for its explicit absence workflow. Humboldt terms have their own individual version history. The correct export depends on the pinned target profile and package format.

**Acceptance evidence:**
- Exact target profile, schema, core terms and Humboldt extension versions pinned.
- Explicit non-detection mapped to the chosen profile.
- Implicit absence mapping tested only when scope/completeness requirements are satisfied.
- Not assessed/incomplete/indeterminate/unknown do not map to a negative value.
- Export/import round trip preserves source meaning or records loss explicitly.
- No export rule is imposed as a universal internal validity constraint.

**Required reviewers:** biodiversity informatician, survey-method specialist, data architect.

---

## 6. Recommended internal semantic vocabulary (proposal only)

The following are conceptual states, not a final controlled vocabulary or schema.

### 6.1 Assessment state

The SurveyTargetAssessment should distinguish at least:
- not assessed;
- assessment in progress;
- completed assessment;
- incomplete assessment;
- indeterminate assessment;
- assessment not applicable;
- assessment withdrawn or superseded, with history retained.

Exact values, transitions and authorization rules require domain review.

### 6.2 Occurrence state

The Occurrence should carry the authoritative occurrence-level state:
- detected;
- not detected (explicit, bounded and evidence-backed);
- other justified states only where the domain and export semantics require them.

Do not store the same occurrence outcome independently in both SurveyTargetAssessment and Occurrence.

### 6.3 Completeness dimensions

Do not collapse all completeness into one Boolean. Review the applicability of:
- taxonomic scope completeness;
- SurveyTarget completeness;
- life-stage scope completeness;
- growth-form scope completeness;
- establishment-means scope completeness;
- non-target/bycatch reporting completeness;
- spatial coverage completeness;
- temporal coverage completeness;
- sampling effort reporting/completion;
- occurrence/record reporting completeness.

The relevant Humboldt terms and their versions must be pinned individually. A value of "fully reported" means the relevant defined reporting scope is complete; it does not mean that the biological world was exhaustively sampled or that detection probability was 100%.

## 7. Worked workflows and expected outcomes

### WF-01 — Casual photograph, no Survey

A contributor uploads a photograph of an unidentified flowering plant. No formal survey was conducted.

Expected:
- Observation and MediaAsset exist.
- An Event may be created only if capture context is defensible.
- No SurveyTarget or SurveyTargetAssessment is fabricated.
- No non-detection claim is possible.
- AI candidates remain candidates; no automatic Identification is accepted.

### WF-02 — Complete fixed-plot survey, target detected

A botanist surveys a fixed plot for specified native tree taxa using a documented protocol and effort. Two target taxa are detected.

Expected:
- Survey Event and target scope are recorded.
- Assessment records preserve the target and completeness.
- Positive Occurrence Events are reported by the Survey.
- Identifications remain separate, versioned determinations.
- Evidence and protocol provenance are retained.

### WF-03 — Complete fixed-plot survey, one target not detected

The same survey assesses a declared taxon target, completes the relevant search and reporting scope, but does not detect the target.

Expected:
- SurveyTargetAssessment records the completed assessment and its context.
- One explicit, taxon-specific non-detection Occurrence is represented, linked to the Survey and assessment.
- The Occurrence has no fabricated positive Organism identity.
- The result is described as "not detected under this protocol, effort, place and interval", not as proof of absolute absence.
- Export value follows the pinned profile.

### WF-04 — Survey interrupted by weather

The team stops early and does not complete the target checklist.

Expected:
- Survey and actual effort are retained.
- Assessment is incomplete or indeterminate.
- No explicit non-detection Occurrence is created for targets not validly assessed.
- Positive detections already supported remain valid.
- No implicit absence export is permitted for the incomplete scope.

### WF-05 — Incidental/bycatch detection

A pollinator-focused Survey records a plant species that was not a declared target.

Expected:
- Positive Occurrence is retained.
- SurveyOccurrenceReport role is incidental/bycatch.
- The plant is not retroactively added to the target list without an explicit, attributable correction to the survey design.
- No absence is asserted for bycatch.

### WF-06 — Multi-plant photograph

One photograph shows three distinct plants.

Expected:
- One Observation may support multiple Occurrences where evidence supports separate occurrence interpretations.
- Each Occurrence retains its own identity and identification history.
- A shared capture Event may contextualize them.
- Do not assume one photograph equals one plant or one Organism.

### WF-07 — Herbarium specimen imported after collection

A herbarium sheet is digitized decades after collection.

Expected:
- Historical collection Event, MaterialEntity, MediaAsset, SourceRecord and provenance are represented.
- The historical date precision and locality uncertainty are preserved.
- No synthetic platform Observation or contemporary Survey is created.
- Historical identifications remain source-aware and versioned.

### WF-08 — Repeated monitoring visits

A fixed plot is monitored monthly for two years.

Expected:
- A parent monitoring/project Event may contain distinct Survey/visit Events where the design justifies hierarchy.
- Each visit retains its own date, protocol, effort, scope applicability and completeness.
- Earlier not-detected outcomes are not overwritten by later detections.
- A later positive detection does not retroactively falsify a properly bounded earlier non-detection.

### WF-09 — Broad target scope and implicit absence export

A published Survey reports all detected occurrences for a fully declared taxonomic scope. No explicit zero-count Occurrence is created for every undetected taxon.

Expected:
- Internal records do not fabricate individual negative Occurrences merely because rows are missing.
- Export may derive profile-specific implicit absence only if the pinned Humboldt/GBIF profile's target-scope and completeness requirements are met.
- Export documents which terms, scopes and completeness evidence justify the inference.
- No inference is made outside the declared scope or for bycatch.

### WF-10 — Overlapping surveys and shared underlying occurrence

Two overlapping Surveys legitimately include the same documented biological encounter.

Expected:
- The same Occurrence may be associated with both Surveys only if evidence establishes that it is the same underlying occurrence and both Survey reporting contexts are valid.
- Each SurveyOccurrenceReport retains its own target/role/context.
- Similar taxon, date and coordinates alone are insufficient to merge records.
- Independent detections remain separate.

---

## 8. Acceptance scenarios EVT-01 to EVT-22

These extend the current decision paper and Task 05D v3. They are proposals, not executed tests. Do not mark any test Passed until fixtures, expected outcomes, actual results, implementation revision and reviewer evidence are attached.

| ID | Scenario | Required result |
|---|---|---|
| EVT-01 | One monitoring programme contains multiple repeated Surveys | Parent/child hierarchy retains each Survey's distinct identity, time, place, agent and protocol |
| EVT-02 | One Survey reports multiple target-matching Occurrences | SurveyOccurrenceReport preserves all Occurrences and target relation |
| EVT-03 | One Survey reports incidental/bycatch Occurrence | Report role records incidental result without adding it to the target list |
| EVT-04 | One contextual Event supports several Occurrences and MaterialEntities | Shared context is represented once; no duplicated/conflicting time/location data |
| EVT-05 | One Observation documents three plants | One Observation can link to three supported Occurrences; no one-photo/one-plant assumption |
| EVT-06 | One Occurrence is supported by multiple Observation submissions | Evidence/provenance links retain all contributors and their roles |
| EVT-07 | One Observation has no known Event context | Observation remains valid; no fabricated Event/date/location |
| EVT-08 | A Survey has no predeclared targets | Survey remains valid as an inventory; no target-specific non-detection is inferred without a defined target and assessment |
| EVT-09 | SurveyTargetAssessment is complete and a target was not detected | Explicit bounded non-detection is represented by one canonical Occurrence-level result linked to the assessment and Survey |
| EVT-10 | Survey target is not assessed | Assessment is not_assessed; no negative Occurrence is generated |
| EVT-11 | Survey is incomplete due to weather/access | Assessment is incomplete/indeterminate; no not_detected state |
| EVT-12 | Same taxon is not detected in one visit but detected in a later visit | Separate target assessments and Occurrence Events are retained; earlier result is not overwritten |
| EVT-13 | A historical specimen record has no platform Observation | MaterialEntity, collection Event and provenance are valid without a synthetic Observation |
| EVT-14 | Event location is withheld or unknown | Event context retains explicit location state without fabricated coordinates |
| EVT-15 | Child Event is linked to two parents | Rejected in strict hierarchy unless a separately typed contextual association is justified and approved |
| EVT-16 | Occurrence has no known individual Organism identity | Record remains representable without inventing an individual |
| EVT-17 | Assessment says not detected but reporting completeness is false | Validation rejects or downgrades the negative outcome; no explicit negative Occurrence is accepted |
| EVT-18 | Internal records exported to Darwin Core/GBIF | Mapping is validated against exact pinned version/profile; unsupported internal detail is retained and loss documented |
| EVT-19 | A target is assessed and not detected during a complete Survey | One authoritative taxon-specific non-detection result is represented; relationship to Occurrence is explicit; no duplicate contradictory result exists |
| EVT-20 | SurveyTargetAssessment is incomplete or not assessed | No not-detected Occurrence is created; assessment state remains incomplete/not assessed |
| EVT-21 | A bycatch taxon is incidentally recorded but was not searched for | Positive incidental Occurrence may be reported; no absence/non-detection claim is generated for that taxon |
| EVT-22 | Explicit and implicit non-detection are exported to the selected GBIF/Humboldt profile | Export follows pinned profile, scope/completeness terms and vocabulary; internal semantics and provenance remain traceable; no unsupported inference is introduced |

### 8.1 Required test evidence record

Each executed scenario must record:
- scenario ID and version;
- fixture identifier and provenance;
- source model/document versions;
- standard/profile/term versions, if export-related;
- expected result;
- actual result;
- implementation commit/build;
- validator/test-suite version;
- reviewer identity and discipline;
- pass/fail/blocked result;
- defect or exception reference;
- data-loss/uncertainty/security observations.

A document edit is not test execution. A mergeable PR is not scientific approval. An unexecuted scenario remains **Not tested**.

## 9. Non-detection safeguards

The following are mandatory safeguards for the proposed model:

1. A missing Occurrence row is unknown/not recorded internally, not evidence of biological absence.
2. A negative Occurrence is an explicit, bounded scientific record with target, Survey/Event, place, interval, assessment and provenance.
3. A negative Occurrence must not be generated for an unassessed or incomplete target.
4. A negative Occurrence must not be generated for bycatch or for a taxon outside the declared target scope.
5. A non-detection does not establish absolute absence, extinction, local extirpation, zero population size or absence beyond the surveyed interval.
6. Detection probability and detectability limitations must remain visible where scientifically relevant.
7. Implicit absence is a profile-specific export inference, permitted only when the exact target/scope and completeness requirements are met.
8. An implicit export inference must not be silently persisted as an internal explicit negative Occurrence.
9. Export mapping must pin exact versions and document vocabulary conversions.
10. Corrections to a negative result must preserve the previous assertion, evidence and audit history.

## 10. Standards mapping work still required

Before any production mapping is approved:

1. Retrieve exact versioned Darwin Core Conceptual Model, List of Terms, Hierarchical Events guidance and schema resources.
2. Retrieve exact 2026-10-13 Humboldt term-list/version resources and compare them with 2026-05-26.
3. Pin the current versions of eco:Survey, eco:SurveyTarget, eco:absentTaxa, eco:isSurveyTargetFullyReported, target/excluded scope terms, completeness terms, protocol and effort terms.
4. Pin dwc:occurrenceStatus term version separately; current term version is 2026-05-26 and its recommended default values are detected / notDetected.
5. Identify the intended GBIF dataset profile and packaging format. The GBIF survey guide v1.0.2 uses present/absent examples for explicit absence, while the current Darwin Core term recommends detected/notDetected. Resolve this through a tested profile-specific mapping; do not invent a universal equivalence.
6. Test explicit negative Occurrence export.
7. Test implicit absence export with complete target scope and no Occurrence row.
8. Test incomplete scope, bycatch, not-assessed and indeterminate cases.
9. Test import/export round trips and document any loss of internal detail.
10. Ensure internal validation remains independent from the external publishing profile.

## 11. Cross-document changes required after decisions

No underlying Task 05C or ADR model should be changed by this review pack alone.

After the EVT decisions are approved:
- Update Task 05C Candidate A and Candidate B comparison and record which model is selected.
- Update Task 05B only if a documented semantic correction is approved.
- Update Task 05D v3 with accepted decisions and executable acceptance evidence.
- Update the scientific validation matrix with outcome, rationale, owner, evidence and re-review trigger.
- Update API command/read-model contracts only after the domain semantics are stable.
- Reconcile the stacked dependency of PR #11 against the final Task 05C branch and review the full diff.
- Preserve Task 05D v2 and PR #23 as historical comparison material until its review/retirement conditions are satisfied.
- Update ADRs only through explicit decision records and the project's ADR process.
- Do not begin Task 05E until all blocking scientific and integrity gates are closed.

## 12. Review and sign-off protocol

| Reviewer discipline | Required review |
|---|---|
| Field ecologist / survey-method specialist | Survey design, protocol, effort, target scope, detectability, completeness and non-detection validity |
| Indian field botanist | Realistic botanical survey, multi-plant, growth-form, life-stage, clonal/group and herbarium workflows |
| Biodiversity-informatics specialist | Darwin Core, Humboldt Extension, GBIF profiles, term versions, mappings and exchange loss |
| Data architect | Event identity, specialization, cardinalities, integrity, history and implementability |
| Geospatial/privacy specialist | Location uncertainty, restricted coordinates, hierarchy and derived export/search leakage |
| Rights/provenance reviewer | Source, media, evidence, attribution, rights and retention consequences |

For each EVT-D decision, record:
- Accepted / Rejected / Deferred / Needs revision;
- exact decision text;
- rationale;
- evidence and fixtures reviewed;
- reviewer name/role/affiliation where disclosure is authorized;
- date and version;
- dissenting views;
- conditions and re-review triggers.

No reviewer should be represented as having approved this model until their attributable review is actually received and recorded. No external reviewer has been contacted as part of preparing this pack.

## 13. Readiness decision

**Task 05E: NOT READY.**

Reasons:
- EVT-D01–EVT-D10 remain open.
- The canonical relationship between SurveyTargetAssessment and non-detection Occurrence is not approved.
- Task 05C Candidate A and Candidate B both need explicit Survey/SurveyTarget/completeness reconciliation.
- EVT-01–EVT-22 are proposals and have not been executed.
- Exact 2026-10-13 Humboldt term-version comparison and selected GBIF profile mapping remain outstanding.
- Independent field ecology and biodiversity-informatics review has not been obtained.
- PR #11 remains stacked on Task 05C Candidate A and needs a complete post-decision consistency review.

The recommended next gate is discipline-specific review of this pack and the underlying worked fixtures. Only after documented decisions and test evidence should Task 05C be revised and Task 05E readiness be reassessed.

## 14. Authoritative references checked 21 November 2026

### TDWG / Darwin Core
- Darwin Core Conceptual Model: https://dwc.tdwg.org/cm/
- Darwin Core List of Terms: https://dwc.tdwg.org/list/
- Darwin Core schemas: https://dwc.tdwg.org/schemas/
- Hierarchical Events guidance: https://dwc.tdwg.org/hierarchy/
- TDWG October 2026 ratification announcement: https://www.tdwg.org/news/2026/dwc-oct-nov-announcement/
- Darwin Core occurrenceStatus term: http://rs.tdwg.org/dwc/terms/version/occurrenceStatus-2026-05-26

### Humboldt Extension
- Humboldt Extension vocabulary: https://rs.tdwg.org/eco.htm
- Humboldt Extension terms: https://rs.tdwg.org/eco/terms.htm
- Humboldt Extension quick reference: https://eco.tdwg.org/terms/
- Humboldt hierarchical-event guidance: https://dwc.tdwg.org/hierarchy/
- Humboldt Extension 2026-10-13 term list: http://rs.tdwg.org/eco/version/terms/2026-10-13

### GBIF
- Guide for publishing biological survey and monitoring data to GBIF, v1.0.2 (2025-09-24): https://docs.gbif.org/guide-publishing-survey-data/en/
- Survey and Monitoring Data Quick-Start Guide: https://docs.gbif.org/survey-monitoring-quick-start/en/
- Sampling-event data quality requirements: https://www.gbif.org/data-quality-requirements-sampling-events

This pack is a proposed review artifact. It does not claim that the current logical model conforms to every standard term, that any test has passed, or that scientific/domain decisions have been approved.
