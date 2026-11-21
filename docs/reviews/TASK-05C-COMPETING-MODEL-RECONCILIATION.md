# Task 05C Competing Logical-Model Reconciliation Assessment

**Assessment date:** 20 November 2026  
**Status:** Desk-review recommendation; not an approved scientific model or external expert sign-off  
**Purpose:** Compare the two extant Task 05C documents and recommend a safe canonical-document path without discarding useful content.

## 1. Executive recommendation

Use the Task 05C document currently carried by PR #5 as the **canonical review candidate**, subject to the unresolved design questions and corrections in this assessment.

Do not merge the competing document wholesale. Preserve it as a source for selected workflow examples, cardinality explanations and operational scenarios. Port only content that survives semantic review and is reconciled with Task 05B, the current review pack and authoritative standards.

This recommendation is based on document structure and standards alignment, not on a completed scientific review. Neither document is approved, and neither authorizes physical database implementation.

## 2. Exact source documents inspected

| Candidate | Branch | File | Blob SHA | Length |
|---|---|---|---|---:|
| A — PR #5 | `docs/task-05c-logical-data-model` | `docs/architecture/TASK-05C-LOGICAL-DATABASE-MODEL.md` | `4a21c0aa3b8ebfef319a9ea1ac6928274b0b3f5b` | 647 lines |
| B — no open PR in audit snapshot | `docs/task-05c-logical-database-model` | `docs/data-architecture/TASK-05C-LOGICAL-DATABASE-MODEL-AND-SCIENTIFIC-RELATIONSHIPS.md` | `239d7e9974bcb81b1154b54845a7b2d69c3775d6` | 648 lines |

The files are not identical and have different section structures. Candidate A is organized around entity relationship diagrams, canonical entity inventory, keys, cardinality, temporal strategy, geospatial/privacy rules, rights/provenance, identification/evidence integrity, standards mappings, tests and open decisions. Candidate B is organized by domain and includes four end-to-end workflows.

## 3. Why Candidate A is the stronger canonical review candidate

Candidate A makes the following distinctions more explicit:

1. **TCS taxonomy semantics**
   - TaxonConcept, TaxonName, TaxonNameUsage, TaxonConceptSynonym, TaxonConceptMapping, TaxonNameRelationship and NomenclaturalType are separately represented.
   - Synonym relations target TaxonName, not another TaxonConcept.
   - Nomenclatural name-to-name relationships are not conflated with concept-to-concept mappings.
   - The canonical according-to resource is distinguished from optional treatment metadata.

2. **Typed subject references and referential integrity**
   - Identification uses an IdentificationSubject association with actual foreign keys to Observation, Occurrence or MaterialEntity.
   - ScientificAssertion uses typed subject-link rows rather than an unconstrained polymorphic `subject_type + subject_id` pair.
   - Candidate A explicitly notes that a row-local CHECK does not by itself guarantee that every Identification has a subject row; this cross-table participation requirement needs a separately designed and tested enforcement mechanism.

3. **Field records and evidence**
   - Observation, Occurrence, Event, Organism, MaterialEntity and MediaAsset are not treated as interchangeable.
   - Occurrence–Observation and Occurrence–MaterialEntity links are explicit.
   - AI candidates, expert assessments and accepted/revised identifications are distinct.
   - Rights and provenance are separate concerns.

4. **Validation**
   - Candidate A has 16 named LDM scenarios, including non-detection, rights separation, source re-ingestion, boundary versioning and restricted coordinates.
   - It includes separate security and data-quality tests.

These strengths make Candidate A more suitable as the canonical review baseline. They do not establish that its semantics or cardinalities are fully correct.

## 4. Useful content in Candidate B to preserve selectively

Candidate B contains useful material that should not be lost:

- Four end-to-end workflows:
  - citizen observation with uncertain identity;
  - herbarium specimen with multiple determinations;
  - conflicting distribution claims;
  - AI training eligibility.
- Clear explanations of valid time, transaction time, source publication/release time, retrieval time and observation/event time.
- Detailed cardinality discussion for Observation, Event, Occurrence, Organism and MaterialEntity.
- Practical source and dataset ingestion lifecycle descriptions.
- Explicit warning that Observation-to-Event and Occurrence-to-Organism cardinalities require domain-expert review.

Recommendation: port the four workflows into Candidate A as **illustrative, non-normative workflows** only after their steps are checked against the reconciled entity model. Preserve the cardinality questions as open decisions, not as settled design rules.

## 5. Candidate B issues requiring correction before any reuse

### 5.1 TaxonConcept mapping vocabulary

Candidate B §6.3 gives examples including `excludes` and `unresolved` in the concept-mapping relationship list, while saying the vocabulary will be mapped to TCS.

TCS `mappingRelation` requires one of exactly six TCS mapping properties: `isCongruentWith`, `includes`, `isIncludedIn`, `partiallyOverlaps`, `isDisjointFrom` or `intersects`.

If Botanica Indica needs additional internal relationship or review states, they must be represented separately and mapped only where semantically justified. Do not serialize unsupported internal values as TCS mappingRelation values.

### 5.2 Identification subject modelling

Candidate B's ERD directly connects Identification to Observation and optionally Occurrence, while its narrative describes a subject and subject type. It does not provide the same explicit typed subject-link design as Candidate A and does not clearly include MaterialEntity as an Identification target in the ERD.

Candidate B should not be copied into the canonical ERD without resolving this discrepancy.

### 5.3 TCS synonym and nomenclatural type detail

Candidate B discusses taxonomy relationships generally but does not explicitly model the TCS NomenclaturalType class or a dedicated TaxonConcept-to-TaxonName synonym association in the same way as Candidate A.

The distinction between:
- concept-to-name synonym relations;
- name-to-name nomenclatural relations; and
- concept-to-concept mappings

must remain explicit.

### 5.4 Diagram simplifications

Candidate B's Observation-to-Event and Event-to-Occurrence relationships are useful conceptual prompts, but the diagram is not sufficient to decide whether Event and Occurrence are separate context entities, specialized event records, or a more nuanced relationship in the internal model. That decision requires the Darwin Core Conceptual Model and field workflow to be considered together.

## 6. Important unresolved issues in Candidate A

Candidate A is the preferred review candidate, but it must not be treated as ready for approval.

### 6.1 Event and Occurrence semantics — high priority

The current Darwin Core Conceptual Model treats Occurrence and Survey as specialized types of Event. Candidate A has separate logical Event and Occurrence entities with a relationship. That can be implemented relationally as a supertype/subtype or shared-identity extension pattern, but the model must make the subtype semantics explicit. The Darwin Core Conceptual Model is a high-level, non-normative framework (except its status section), not a prescribed database schema. It explicitly allows internal entities and relationships beyond the conceptual model and notes that one contextual Event may provide shared spatio-temporal context to multiple Occurrences and Material Entities.

**Recommended pattern to evaluate:** an Event supertype with Survey and Occurrence specializations/extensions, plus an explicit parent/child Event relationship for nested survey structure. Keep Botanica Indica Observation as a distinct contributor/workflow record. It may link to capture Events, contextual Surveys, and/or Occurrences through explicit associations whose roles/cardinalities are defined.

Required review:
- Is Event the shared identity/supertype for Survey and Occurrence in the internal relational model, or is there an alternative with demonstrably loss-aware Darwin Core mapping?
- How are parent/child Events represented?
- Can one Survey/Event report multiple Occurrences?
- Can a single contextual Event support multiple Occurrences and MaterialEntities?
- Can one Observation refer to one capture Event, a Survey Event, multiple Events, or none where context is unavailable?
- What does a non-detection record target and how is it bounded by survey target, protocol, effort, time, location and reporting completeness?

Do not settle this by renaming tables. Add an explicit conceptual model, cardinality rules and executable fixtures.

### 6.2 Observation-to-Event linkage — high priority

Candidate A has Observation-to-Occurrence and Event-to-Occurrence links but does not make the Observation-to-Event association sufficiently explicit in its ERD. Candidate B has a direct Observation-to-Event relationship, but its cardinality is not validated.

The model must distinguish a contributor's submission/workflow record from the scientific Event or Survey. Determine whether an Observation can:
- refer to one capture Event;
- group multiple Events;
- contribute to an Event/Survey without owning it; or
- have no Event where the time/location context is unavailable.

Use explicit link entities if the relationship carries role, provenance or protocol metadata. Validate with mobile capture, repeated plot survey and herbarium/collection workflows.

### 6.3 LDM-16 editorial defect

Candidate A currently says: “no Occurrence row is never interpreted as absence”. This is grammatically ambiguous.

Replace with:

> “The absence of an Occurrence row must never be interpreted as evidence of absence.”

The intended scientific rule should remain: a non-detection is an explicit, bounded survey result; missing data is not evidence of absence.

### 6.4 Non-detection export profile

Do not assume the same literal vocabulary is used by every exchange profile. The current GBIF sampling-event guidance describes `present` and `absent` for associated occurrence data, while Darwin Core's conceptual and term guidance must be considered separately. Keep a stable internal detection state and test each target export mapping against its current profile.

### 6.5 IdentificationSubject total participation

Candidate A correctly identifies that a CHECK across nullable FK columns can enforce exactly one populated target on a subject row, but it does not guarantee every Identification has a corresponding subject row. The physical design must specify a safe transaction/trigger/constraint strategy or an equivalent supertype model and prove it with negative tests.

### 6.6 ScientificAssertion target inventory

The allowed subject types and cardinalities need to be exhaustive and governed. Do not leave the target inventory as an open-ended polymorphic extension. Confirm which types are valid for each assertion predicate.

## 7. External standards verification

### 7.1 Taxon Concept Standard

The TDWG TCS List of Terms currently identifies version 2025-12-11. It requires a TaxonConcept to have exactly one `taxonName` and one `accordingTo` resource. TCS synonym is a relation between a TaxonConcept and a TaxonName. Basionym and replaced-name relationships are TaxonName relationships. TCS concept mappings require subject, relation and object, and the relation must be one of the six defined mapping properties.

Official source: https://tcs.tdwg.org/terms/

### 7.2 Darwin Core Conceptual Model

Latest indexed official page metadata reports the Darwin Core Conceptual Model version issued 2026-10-13 (previous 2026-05-26); direct retrieval of the exact versioned content remains to be verified. The earlier 2026-05-26 version was used for the semantic summary below.
- Event as an action/process/set of circumstances at a place during an interval;
- Survey as a type of Event;
- Occurrence as a type of Event that can represent direct observation, indirect inference or absence of detection;
- Organism as a particular organism or defined taxonomically homogeneous group;
- MaterialEntity as physical matter gathered or sampled during an Event.

The conceptual model is a non-normative framework and does not prescribe one database implementation. The internal model therefore needs an explicit, loss-aware mapping rather than a claim that its table names are identical to Darwin Core classes.

Official source: https://dwc.tdwg.org/cm/

### 7.3 GBIF publishing profiles

GBIF's current technical documentation distinguishes general occurrence datasets from sampling-event datasets. General occurrence publishing has its own field requirements/recommendations. Sampling-event publishing expects event/protocol/sample-size/effort context and can support absence inference when sampling effort and protocol are documented.

Do not impose export-specific requirements on every internal record. Do not claim that a record is publishable until the exact current target profile and its required fields have been tested.

Official source: https://techdocs.gbif.org/en/data-publishing/data-quality-recommendations

### 7.4 PostgreSQL constraints

PostgreSQL 18 documentation states that CHECK constraints cannot safely enforce conditions that depend on other table rows. Use real foreign keys, unique constraints and appropriate transactional or trigger-based enforcement for cross-row participation requirements.

Official source: https://www.postgresql.org/docs/18/ddl-constraints.html

## 8. Reconciliation decision proposal

| Item | Proposed disposition | Status |
|---|---|---|
| Canonical document | Candidate A (PR #5) | Recommended, not approved |
| Candidate B | Preserve as reference; do not merge wholesale | Recommended |
| Candidate B workflows | Port selectively after semantic review | Pending |
| Candidate B cardinality detail | Retain as open questions and test cases | Pending |
| TCS-specific taxonomy model | Retain Candidate A's explicit classes/relations, subject to taxonomist review | Pending |
| Event/Occurrence model | Re-open and resolve using current Darwin Core Conceptual Model | Blocking |
| Observation/Event association | Define and test cardinality | Blocking |
| Identification subject integrity | Retain typed FKs; specify total-participation enforcement | Blocking |
| LDM-16 typo | Correct wording without changing intended semantics | Editorial correction |
| Physical schema / Task 05E | Remain blocked | Not ready |

## 9. Required test additions before Task 05E

Add or extend fixtures for:

1. A Survey/Event with multiple Occurrences and explicit target list, protocol, effort and survey completion status.
2. One contributor Observation linked to a capture Event and a separate multi-day Survey/Event.
3. An Occurrence represented as an Event in the external Darwin Core mapping without conflating the internal contextual Survey.
4. An Event with multiple MaterialEntities and multiple Occurrences.
5. An Identification with no subject row (must fail) and one with two target FKs populated (must fail).
6. A ScientificAssertion with an unsupported subject type for its predicate (must fail).
7. An explicit non-detection target result and a missing Occurrence row (must remain unknown/not surveyed).
8. An export test proving profile-specific mapping for GBIF sampling-event publication.

Each fixture must record expected result, actual result, source version, implementation revision, reviewer and evidence. Until executed, status remains Not tested.

## 10. Next actions

1. Correct the LDM-16 wording in Candidate A as a narrow editorial change.
2. Add this reconciliation assessment to the scientific review pack and link it from the decision register.
3. Ask the Task 05C authors to resolve the Event/Occurrence and Observation/Event design questions before considering the logical model stable.
4. Port the four Candidate B workflows only after they are checked against the revised model.
5. Update Task 05B/05C/05D together where the resolved semantics affect multiple documents.
6. Obtain qualified taxonomist, ecologist/biodiversity-informatics and database-architect review.
7. Keep Task 05E blocked until the documented readiness gate is passed.

**No branch has been merged or deleted as part of this assessment. No expert review or model approval is claimed.**


## 11. Cross-document consistency findings from Task 05, Task 05B and Task 05D

The reconciliation was extended to the exact current documents on PR #3, PR #4 and PR #11. This revealed two additional cross-document issues and one standards-description issue.

### 11.1 Event, Survey and Occurrence semantics

- Task 05 initially described Occurrence as evidence of presence and Event as a contextual container for occurrences, without explicitly stating that the current Darwin Core Conceptual Model treats Occurrence and Survey as specialized Event types.
- Task 05B defines Occurrence as a state record with optional `event_id`, while Task 05C separately models Event and Occurrence.
- The 2026-05-26 Darwin Core Conceptual Model version reviewed at the time states that Occurrence and Survey are specialized Event types, and that one contextual Event may provide shared spatio-temporal context to multiple Occurrences and Material Entities. Latest indexed metadata now reports a 2026-10-13 version; compare that version's exact content before treating the earlier semantic summary as current. The model does not prescribe a database schema.

**Change made:** Task 05 (PR #3) was updated to clarify the Event supertype/subtype design option, Occurrence's event semantics, Survey as a specialized Event, contextual Events, and the difference between Observation and Occurrence. This is a proposed logical direction, not a finalized schema.

### 11.2 Identification subject pattern mismatch

Task 05B contained two inconsistent patterns:
- the Identification field table required one `IdentificationSubject` row with exactly one populated target FK; but
- a later paragraph proposed three separate link entities (`IdentificationObservationSubject`, `IdentificationOccurrenceSubject`, `IdentificationMaterialEntitySubject`).

Task 05C proposes one `IdentificationSubject` row with three nullable target FK columns, each a real FK, and a row-local exactly-one CHECK. This is a logical-pattern mismatch across documents and within Task 05B.

**Change made:** Task 05B (PR #4) now uses one canonical `IdentificationSubject` row per Identification, with three nullable real FK columns, row-local exactly-one CHECK, unique Identification FK, and a separate total-participation enforcement requirement. It explicitly states that CHECK alone cannot guarantee every Identification has a subject row. This aligns the logical pattern with Task 05C without claiming physical implementation.

### 11.3 GBIF occurrence requirements in Task 05

Task 05 initially stated that GBIF occurrence publishing guidance requires occurrenceID, basisOfRecord, scientificName and eventDate without distinguishing general occurrence datasets from GBIF-managed programmes. Current GBIF technical documentation states that `occurrenceID` is required; `basisOfRecord`, `scientificName` and `eventDate` are strongly recommended in the general occurrence profile and required for GBIF-managed programmes. Sampling-event datasets have a distinct profile.

**Change made:** Task 05 (PR #3) now describes the profile-specific status and explicitly says export requirements are not universal internal database constraints.

### 11.4 Task 05D dependency and outstanding synchronization

PR #11 is stacked on PR #5. After the latest PR #5 and PR #11 document updates, GitHub's compare endpoint reports the PR #11 head branch as two commits ahead and one commit behind the current PR #5 base branch. The PR #11 head has not been rebased/synchronized to the latest PR #5 head in this pass. Do not merge or retarget PR #11 until its base is synchronized and its diff is re-reviewed.

The PR #11 document's DR-02 row has now been updated to state that a row-local CHECK does not ensure every Identification has a subject row; total participation requires a separate transactionally safe enforcement strategy. Its DR-07/FLD-08 wording has also been corrected. Event/Occurrence assumptions still require design review, and the stacked branch must be synchronized before merge.

### 11.5 Verification state of the cross-document edits

The Task 05 and Task 05B edits were committed on their existing PR branches and must be reviewed in PR #3 and PR #4. They are document-level proposals only. No PR was merged, no external expert approval is claimed, and Task 05E remains NOT READY.

## 12. Updated recommendation

1. Retain PR #5 Task 05C as the canonical review candidate, subject to resolution of the Event/Survey/Occurrence pattern and Observation/Event cardinalities.
2. Retain the single-row typed-FK `IdentificationSubject` pattern as the preferred logical option, with total participation treated as a separate integrity requirement.
3. Review the Task 05 / Task 05B edits in PRs #3 and #4 for scientific and editorial correctness.
4. Synchronize PR #11 with the latest PR #5 head and reconcile its DR-02 and Event/Occurrence wording before any merge decision.
5. Keep all four scientific architecture PRs in draft until their blocking questions and independent discipline reviews are complete.
6. Keep Task 05E blocked.


**Standards metadata re-verification (20 November 2026):** latest indexed official TDWG metadata reports 2026-10-13 as the issue date for both the List and Conceptual Model, with 2026-05-26 as previous. Direct HTML retrieval of the List page returned the 2026-05-26 header, and the core term-list snapshot remains 2026-05-26. Exact current versioned resources and relevant term IRIs remain unverified. DR-09 stays open; the earlier claim that 2026-10-13 was erroneous is withdrawn pending direct versioned-resource verification. Sources: https://dwc.tdwg.org/cm/ ; https://dwc.tdwg.org/list/ ; https://rs.tdwg.org/dwc/terms.htm .


**DR-09 source retrieval addendum (20 November 2026):** official indexed metadata now reports 2026-10-13 for both Darwin Core documents, previous 2026-05-26; direct page retrieval and core namespace term list expose 2026-05-26 metadata. Reconcile the exact versioned documents and term IRIs before asserting the current baseline or closing DR-09.


---

## 13. Standards metadata and non-detection mapping refresh — 21 November 2026

The prior Sections 7.2 and 11–12 recorded a retrieval conflict between 2026-10-13 indexed metadata and direct 2026-05-26 page rendering. A fresh check of TDWG's official publication metadata and its 19 October 2026 ratification announcement identifies 2026-10-13 as the newer publication version for the Darwin Core Conceptual Model and List of Terms. The current Hierarchical Events guidance and maintained schemas are also dated 2026-10-13.

Version IRIs to pin:
- Conceptual Model: `http://rs.tdwg.org/dwc/doc/cm/2026-10-13`
- List of Terms: `http://rs.tdwg.org/dwc/doc/list/2026-10-13`
- Hierarchical Events: `http://rs.tdwg.org/dwc/doc/hierarchy/2026-10-13`
- Schemas: `http://rs.tdwg.org/dwc/doc/schemas/2026-10-13`

**Retrieval qualification:** direct page rendering in this review session still exposed cached 2026-05-26 headers for the Conceptual Model/List pages. The current official metadata and ratification announcement support the 2026-10-13 publication baseline, but the exact versioned resources and their substantive differences must still be retrieved and compared before the standards gate is closed.

The individual `dwc:occurrenceStatus` term has its own version metadata: modification date 2026-05-26 and term-version IRI `http://rs.tdwg.org/dwc/terms/version/occurrenceStatus-2026-05-26`. The current term notes recommend `detected` and `notDetected`. This term-level date is not evidence that the containing List document remains at its previous publication version.

GBIF's biological survey guide v1.0.2 (2025-09-24) describes explicit non-detection/absence using `occurrenceStatus = absent` in its DwC-A sampling-event guidance. Therefore, the current internal result state must not be equated automatically with either external literal. Select and test the mapping against the exact GBIF profile, DwC-A/DwC-DP schema, extension and term versions. Preserve the internal assessment, completeness, protocol, effort and provenance even if the external representation is less expressive.

**DR-09 disposition: partially resolved, not closed.** Publication metadata has been refreshed; exact versioned-resource comparison, term pinning and profile-specific export mapping remain open. This update does not approve either Task 05C candidate, close any scientific-model decision, represent an external expert review or change Task 05E's NOT READY status.

Sources:
- https://dwc.tdwg.org/cm/
- https://dwc.tdwg.org/list/
- https://dwc.tdwg.org/hierarchy/
- https://dwc.tdwg.org/schemas/
- https://www.tdwg.org/news/2026/dwc-oct-nov-announcement/
- https://docs.gbif.org/guide-publishing-survey-data/en/


---

## 14.1 Additional semantic reconciliation: non-detection as an Occurrence-level result — 21 November 2026

The current TDWG Conceptual Model §2.3 describes Occurrence as an Event that may represent direct observation, indirect inference, or absence of detection of an Organism of a given Taxon/state during a bounded time interval and Location. Section 2.2 says Survey results are expressed in the Occurrences it reports. GBIF's survey guide v1.0.2 likewise places explicit absence records at Occurrence level and says absence cannot be asserted for bycatch.

This creates an unresolved semantic question in the proposed Task 05C/decision-paper pattern: is SurveyTargetResult itself the internal representation of a target-specific non-detection, or is it an assessment/completeness record that relates to a distinct Occurrence Event representing that non-detection?

**Recommended disposition:** model the target assessment/completeness process separately only where it has distinct lifecycle/provenance needs; make the taxon-specific non-detection an Occurrence-level scientific result or define a rigorously governed assessment-to-Occurrence relation. Prevent two independently mutable records from asserting contradictory outcomes for the same Survey/target/scope. A non-detection has no positive Organism instance merely by virtue of being an Occurrence; it refers to the Taxon/target assessed. Do not assert absence for bycatch or outside the declared target scope.

Add EVT-19–EVT-22 from the decision paper and validation matrix. Keep these scenarios Not tested until executed with fixtures. This issue is blocking for Task 05E and should be included in EVT-D03, EVT-D04, EVT-D09 and EVT-D10. It does not approve Option B or change the overall Task 05E NOT READY status.

Sources: https://dwc.tdwg.org/cm/ ; https://docs.gbif.org/guide-publishing-survey-data/en/.


---

## 15. Cross-document Event–Survey–Occurrence consistency audit — 21 November 2026

**Status:** Desk review completed against the exact source revisions listed below. Findings are proposed corrections and unresolved decisions, not scientific approval. No accepted ADR was changed. No specialist was contacted and no acceptance scenario was executed.

### 15.1 Exact repository baseline inspected

| Source | Branch | Blob SHA | Finding scope |
|---|---|---|---|
| AI Project Operating Prompt | \`docs/repository-audit-and-ai-operating-standard\` | \`61059c74d4d20309ff76e055059ab33f381ca4f2\` | Governing scientific rules, no-absence rule, authority and approval boundaries |
| Task 05B — Data Architecture and Scientific Data Model | \`docs/task-05-data-architecture\` | \`a3255dcf2d1bd4dfa982b381b061051b6c2c8b0b\` | Event/Occurrence semantics and shared Event supertype recommendation |
| Task 05C Candidate A | \`docs/task-05c-logical-data-model\` | \`4a21c0aa3b8ebfef319a9ea1ac6928274b0b3f5b\` | Event–Occurrence relationship, cardinalities and LDM-16 |
| Task 05C Candidate B | \`docs/task-05c-logical-database-model\` | \`239d7e9974bcb81b1154b54845a7b2d69c3775d6\` | Separate Event/Occurrence records, cardinalities and acceptance tests |
| Task 05D v3 | \`docs/task-05d-logical-model-validation-v3\` | \`cf0b9c10bcb2da7b102e52688f22bd8e8b69bb91\` | DR-07, FLD-08, physical design gate |
| Event–Survey–Occurrence Decision Paper | \`review/scientific-data-model-review-pack\` | \`eb513cde11f3013c31102318c78e278bc274ec91\` | Option comparison and earlier EVT decision framing |
| Scientific Data Model Validation Matrix | \`review/scientific-data-model-review-pack\` | \`5eeff39d5362a70ca43b6711062742526b733dc1\` | DR-01–DR-12 and current test register |
| Task 05C Competing Model Reconciliation | \`review/scientific-data-model-review-pack\` | \`eeb15a19f93df5b4feaee3b2b0481b24a59d3c23\` | Existing comparison and DR status before this addendum |
| EVT Decision and Validation Pack | \`review/scientific-data-model-review-pack\` | \`694a2b057b60036bdc961191daa94566830b7e91\` | EVT-D01–D10 and EVT-01–22 |
| ADR-005 Taxonomy Reconciliation | \`review/scientific-data-model-review-pack\` | \`b61dcf0b9ba58fc35da5cc7ba5edfbdd5f2909e4\` | Accepted source-aware taxonomy principles |
| ADR-007 Evidence and Expert Validation | \`review/scientific-data-model-review-pack\` | \`7ba4874b4175707b69dc3052822f8cbeb5384b0a\` | Accepted evidence provenance and history principles |

### 15.2 Blocking finding: Event and Occurrence identity is not reconciled across Task 05B and Task 05C

Task 05B §5.3 states that Occurrence is a specialized Event, says a Survey is a specialized Event, and recommends evaluating a shared Event identity/supertype with Survey and Occurrence specializations/extensions.

Task 05C Candidate A instead presents Event → Occurrence as a 1-to-many contextual relationship and describes Event as contextualizing Occurrence. Candidate B likewise models Event → Occurrence as 1-to-many and lists them as separate field-record entities. Neither candidate currently provides a complete, explicit specialization model that demonstrates how an Occurrence is an Event while a separate generic/context Event may provide shared context.

The decision paper and EVT pack recommend a shared Event identity/common properties with distinct Survey and Occurrence specializations, plus a way to represent broader context. This is a plausible direction, but it is not yet embodied consistently in either Task 05C candidate.

**Required resolution before Task 05C approval:**
1. Define the internal identity model explicitly: shared Event identity/supertype, specialization, or another justified mapping.
2. Distinguish the contextual Event relationship from the Event specialization relationship.
3. Show how a generic context Event may provide spatio-temporal context to multiple Occurrences and MaterialEntities without making one Event instance simultaneously an incompatible combination of Survey, Occurrence and Organism Interaction.
4. State which attributes belong to Event generally and which belong only to Survey or Occurrence.
5. Validate the model against casual observations, repeated surveys, collection events, specimens, multiple Occurrences from one image and one context Event shared by several activities.

**Disposition:** BLOCKER. Option B in the EVT pack remains a recommendation for review, not an approved decision.

### 15.3 Blocking finding: Survey and SurveyTarget are not yet fully modelled

Task 05B mentions Survey targets and reporting-completeness state as potential Event attributes but does not define SurveyTarget as a first-class internal concept. Task 05C Candidate A and Candidate B do not provide a complete Survey / SurveyTarget model. Their field-record diagrams and cardinality tables do not express the full target-scope, reporting-completeness and Survey-to-Occurrence reporting semantics.

The EVT pack introduces Survey, SurveyTarget, SurveyOccurrenceReport and a proposed SurveyTargetAssessment. This is an important improvement, but these are proposals and must be reconciled into one canonical Task 05C design.

The current Darwin Core Conceptual Model describes SurveyTarget as the declared scope of what was sought, either through a priori intention or post facto filtering. It may combine taxonomic, environmental and organismal-trait criteria. The EVT pack should explicitly retain both target-intent and post-facto filtering use cases; it must not imply that every SurveyTarget is necessarily a pre-fieldwork target.

**Required resolution:**
- Separate Survey identity from SurveyTarget identity.
- Define target type, value, unit, include/exclude semantics, source/taxonomic treatment context, validity period and provenance.
- Preserve the distinction between a priori target intent and post facto filtering.
- Allow a Survey without a target while prohibiting unsupported target-specific non-detection claims.
- Define the typed relationship by which a Survey reports target-matching and incidental/bycatch Occurrences.

**Disposition:** BLOCKER.

### 15.4 Blocking finding: SurveyTargetAssessment must not duplicate standards-defined result semantics

The EVT pack proposes SurveyTargetAssessment as an internal assessment/completeness record and recommends that Occurrence carry the authoritative positive or explicit negative scientific result. This is a reasonable hypothesis, but it is not a TDWG class and has not been approved.

The pack currently needs a more precise boundary between:
- SurveyTarget declaration (what was sought or filtered);
- actual protocol and effort performed;
- whether the target was assessed;
- whether all detected target-matching Occurrences were reported;
- the scientific Occurrence result (detected or explicitly not detected);
- profile-specific implicit absence interpretation.

In particular, the Humboldt term \`eco:isSurveyTargetFullyReported\` is defined in its 2026-05-26 term version as whether all counts of detected Occurrences matching a SurveyTarget were fully reported, enabling inference of absence of detection. It does **not** mean that the field search was exhaustive, that every organism was detectable, or that detection probability was 100%.

Likewise, the taxonomic-scope completeness terms concern reporting of detected organisms within the stated scope. They must not be used as synonyms for protocol completion, spatial coverage, temporal coverage or ecological detectability.

**Required resolution:**
1. Retain separate, explicitly named dimensions for sampling design, protocol execution, effort, assessment status, reporting completeness and detection limitations.
2. Define which dimensions are stored on Survey, SurveyTarget, an internal assessment record or Occurrence.
3. Prevent one independently mutable record from contradicting another.
4. Do not use a Boolean called simply \`complete\` to represent all these dimensions.
5. Preserve the evidence, agent, time, target version and correction history for each assessment.

**Disposition:** BLOCKER until the entity boundary and validation semantics are approved.

### 15.5 Policy interpretation requiring project-owner decision: implicit absence

The AI Project Operating Prompt §3.8 states: “Never infer absence from a missing record.” Task 05B, Candidate A, Task 05D FLD-08 and the validation matrix similarly prohibit treating a missing Occurrence row as evidence of absence.

The EVT pack adds a profile-specific export proposal: an external DwC-A may permit implicit absence interpretation when the taxonomic scope is fully reported and the applicable target/excluded scope is declared. The GBIF survey guide v1.0.2 (2025-09-24) does describe such implicit reporting; it is not a permission to infer absence from a missing row alone.

There is a wording/policy ambiguity that must not be silently resolved. The safe technical distinction is:
- **Prohibited:** absence inferred from a missing row alone, with no explicit target/scope and completeness evidence.
- **Potentially supportable external interpretation:** a selected, version-pinned publishing profile interprets an unreported taxon as implicitly not detected only where the explicit survey scope and the applicable reporting-completeness conditions are satisfied.
- **Internal scientific record:** do not silently create an explicit negative Occurrence merely because an export profile derives an implicit result.

**Project-owner decision required:** confirm whether the operating prompt's no-inference rule permits this tightly bounded, export-only interpretation, or whether Botanica Indica must prohibit implicit absence even in external exports and emit only explicit negative Occurrence records. Until that decision is recorded, do not implement implicit absence generation.

**Disposition:** BLOCKER for export behaviour; no change to the operating prompt is made by this review.

### 15.6 Major finding: Event hierarchy rules need to be strengthened in the EVT pack

The current TDWG Hierarchical Events guidance, version issued 2026-10-13, states in its normative usage guidance that:
- a child Event is linked to its broader parent through parentEventID;
- the parent Event must spatially and temporally contain its child Events;
- a child Event must not be assumed to inherit any property implicitly from a parent;
- a parent property should not be populated by deriving or summarizing values from child Events.

The EVT pack correctly distinguishes parent/child hierarchy from SurveyOccurrenceReport and warns against silent inheritance of protocol/effort. However, it does not yet state the full spatial-temporal containment condition or the general non-inheritance/non-derivation rule for all Event properties.

**Required correction to EVT pack and Task 05C:**
- Keep strict hierarchy cardinality (one parent at most per child) separate from contextual links.
- Require parent spatial and temporal coverage to contain child coverage where a true hierarchy is asserted.
- Do not silently inherit any property from parent to child, or derive parent values from children.
- Repeat scope, protocol, effort, agent and completeness values at every Event level where they are explicitly applicable.
- Add tests for spatial-temporal containment violations, property inheritance and parent aggregation.

**Disposition:** MAJOR, blocking for Event hierarchy acceptance.

### 15.7 Major finding: standards version statements are not yet reproducible

The EVT pack and reconciliation materials correctly distinguish publication-version dates from term-version dates, but the version baseline still needs an exact, reproducible pinning pass.

Verified during this audit:
- TDWG's current indexed publication metadata identifies 2026-10-13 versions for the Darwin Core Conceptual Model, List of Terms, Hierarchical Events guidance and schemas.
- Direct rendering of the Darwin Core Conceptual Model page still returned a 2026-05-26 header during this review. Therefore the exact 2026-10-13 Conceptual Model resource and its substantive diff were not independently retrieved here.
- The 2026-10-13 Hierarchical Events guidance page is available and explicitly states the hierarchy requirements summarized above.
- The Darwin Core \`occurrenceStatus\` term version is 2026-05-26 and its recommended default values are \`detected\` and \`notDetected\`.
- The 2026-05-26 Humboldt term-list snapshot identifies some term versions as superseded by 2026-10-13 (including Survey and absentTaxa), while SurveyTarget and isSurveyTargetFullyReported remain at 2026-05-26 in that snapshot. Other terms, including sampling-effort and taxonomic-scope reporting terms, also have 2026-10-13 replacements.
- The current Humboldt landing page still renders 2026-05-26 list metadata. Exact retrieval of the 2026-10-13 versioned Humboldt list and every term required by Botanica Indica remains outstanding.

Consequently:
- Task 05B's statement that the 2026-05-26 Conceptual Model is the current version needs qualification/update after exact-resource comparison.
- The EVT pack's 2026-10-13 baseline should be labelled “publication metadata identified; exact content comparison outstanding” where appropriate.
- Its Humboldt table must be checked term by term against the 2026-10-13 list, not treated as a complete pin set.
- DR-09 remains OPEN. Do not close it on search-result metadata alone.

### 15.8 Major finding: GBIF guide and Darwin Core term vocabularies need a profile-specific crosswalk

GBIF's Guide for publishing biological survey and monitoring data to GBIF v1.0.2 (2025-09-24) describes explicit zero-count absence records using \`occurrenceStatus = absent\` and uses \`present/absent\` examples. The current Darwin Core \`occurrenceStatus\` term recommends \`detected/notDetected\`.

The EVT pack recognizes this difference but has not yet supplied a reproducible profile/schema test. The guide predates the newer 2026 Humboldt term changes, so it must not be treated as a substitute for pinning the current extension terms.

**Required resolution:**
- Select the exact target GBIF dataset class and publishing package/profile.
- Pin the exact DwC-A or DwC-DP schema and Humboldt extension version.
- Map internal detected and explicit non-detection states to that profile with a documented, reversible or loss-declared transformation.
- Test bycatch, unassessed, incomplete, unknown and implicit absence separately.
- Do not make external vocabulary values universal internal enum values.

**Disposition:** MAJOR; export implementation remains blocked.

### 15.9 Cross-document alignment matrix

| Topic | Task 05B | Task 05C A | Task 05C B | Task 05D v3 | EVT pack | Required action |
|---|---|---|---|---|---|---|
| Event is shared conceptual parent/supertype | Recommends evaluation | Not fully represented | Not fully represented | Inherits Candidate A baseline | Proposed Option B | Resolve identity/specialization before selecting candidate |
| Generic contextual Event | Described | Event contextualizes Occurrence | Event context supports Occurrence | Not fully tested | Explicitly proposed | Add contextual Event and multi-activity fixtures |
| Survey specialization | Described | Not fully modelled | Not fully modelled | No full Survey entity | Proposed | Add canonical Survey model |
| SurveyTarget | Attributes mentioned | Not a first-class model | Not a first-class model | No target model | Proposed class | Define scope, target, version and lifecycle |
| SurveyTargetAssessment | Not present | Not present | Not present | Not present | Proposed internal concept | Approve only if distinct lifecycle/provenance need is demonstrated |
| Occurrence-level non-detection | Described | LDM-16 | Not sufficiently tested | FLD-08 | EVT-19–22 | Define one canonical scientific result and relationship |
| Implicit absence | Not supported internally | Not specified | Not specified | Not supported | Proposed export interpretation | Obtain owner policy interpretation; test profile |
| Event hierarchy | Parent event mentioned | Optional parent | Optional parent | Limited hierarchy checks | Parent/child distinction | Add spatial-temporal containment and no-inheritance tests |
| Reporting completeness | Event attribute mentioned | No multi-dimensional model | No multi-dimensional model | Data-quality layers | Multi-dimensional proposal | Separate effort, coverage, assessment and reporting completeness |
| External standards versions | 2026-05-26 CM statement | 2026-05-26 references | Requires current mapping | DR-09 open | 2026-10-13 metadata baseline | Pin exact documents and term IRIs; keep DR-09 open |

### 15.10 Accepted ADR consistency

No conflict requiring amendment to accepted ADR-005 or ADR-007 was identified in this Event-focused audit.

- ADR-005 remains authoritative for source-aware, versioned taxonomy. SurveyTarget taxonomic scope must preserve the taxonomic concept/treatment and source/version used when the target was defined or assessed.
- ADR-007 remains authoritative for evidence provenance, conflicting evidence and attributable expert assessment. A positive or negative survey result must preserve its evidence and review history.

This finding does not constitute a full re-audit of every clause in either ADR. No ADR was modified.

### 15.11 Candidate recommendation and next decision sequence

**Recommendation:** retain Task 05C Candidate A as the current principal review candidate, consistent with the existing reconciliation recommendation, but do not approve it or treat it as the final canonical model. Preserve useful Candidate B material selectively. Neither candidate should be merged wholesale into the other.

Required sequence:
1. Resolve EVT-D01 and EVT-D02: Event identity, contextual Event and hierarchy.
2. Resolve EVT-D03: Survey and SurveyTarget identity/scope, including post facto filtering.
3. Resolve EVT-D04 and EVT-D05: assessment lifecycle, canonical non-detection and owner policy for implicit export interpretation.
4. Resolve EVT-D06 to EVT-D09: reporting links, Observation/Event/Occurrence cardinalities, Organism optionality, protocol/effort/completeness and location/time.
5. Resolve EVT-D10 and DR-09: exact term/version and publishing-profile mapping.
6. Update one canonical Task 05C proposal and the Task 05B, Task 05D, decision paper and validation matrix references together.
7. Execute EVT-01–EVT-22 and existing LDM/FLD scenarios using source-backed fixtures; record actual outcomes and reviewer evidence.
8. Obtain independent field ecology/botany and biodiversity-informatics review.
9. Reassess Task 05E readiness only after the blocking items close.

### 15.12 Readiness and change control

**Task 05C: NOT APPROVED. Task 05E: NOT READY.**

This audit is a document-level consistency review. It does not:
- approve Option B or any cardinality;
- change an accepted ADR;
- modify Task 05B, either Task 05C candidate or Task 05D v3;
- execute any validation test;
- constitute independent specialist sign-off;
- authorize physical database design or DDL;
- authorize PR merge, closure, retargeting or branch deletion.

### 15.13 External authoritative sources checked 21 November 2026

- Darwin Core Conceptual Model: https://dwc.tdwg.org/cm/
- Darwin Core List of Terms: https://dwc.tdwg.org/list/
- Darwin Core Quick Reference: https://dwc.tdwg.org/terms/
- Hierarchical Events guidance, version 2026-10-13: https://dwc.tdwg.org/hierarchy/
- Darwin Core schemas, version 2026-10-13: https://dwc.tdwg.org/schemas/
- Humboldt Extension vocabulary: https://rs.tdwg.org/eco.htm
- Humboldt Extension terms: https://rs.tdwg.org/eco/terms.htm
- Humboldt 2026-05-26 term-list snapshot and replacement metadata: https://rs.tdwg.org/eco/version/terms/2026-05-26.htm
- Humboldt \`isSurveyTargetFullyReported\` term version 2026-05-26: https://rs.tdwg.org/eco/terms/version/isSurveyTargetFullyReported-2026-05-26.htm
- GBIF Guide for publishing biological survey and monitoring data to GBIF v1.0.2 (2025-09-24): https://docs.gbif.org/guide-publishing-survey-data/en/
- GBIF sampling-event data quality requirements: https://www.gbif.org/data-quality-requirements-sampling-events


---

## 16. Further TDWG/Humboldt interpretation correction — 21 November 2026

**Purpose:** refine Sections 15.2–15.8 in light of direct retrieval of the current Darwin Core Conceptual Model, List of Terms, Humboldt term definitions and GBIF survey guidance. This addendum supersedes any broader wording in Section 15 that could be read as prohibiting all hierarchy-aware interpretation or requiring a particular SQL inheritance implementation.

### 16.1 Conceptual specialization is not a mandated SQL inheritance pattern

The directly retrieved Darwin Core Conceptual Model page displays 2026-05-26 as its version and states that the model does not prescribe a technology or strict implementation blueprint. It distinguishes Occurrence, Organism Interaction, Survey and generic Event as Event types. It also explains that a single generic/context Event may provide shared spatio-temporal context to multiple activities. A single Event instance must not be treated as a combination of the special classes merely because the conceptual diagram connects them to Event.

Therefore, Task 05C does not have to implement SQL table inheritance. It must demonstrate a semantically faithful implementation. A separate Event table and Occurrence table may be appropriate if:
- the Occurrence's Event nature and distinct occurrence-specific state are represented;
- the separate contextual Event identity is not confused with the Occurrence's own Event identity;
- Survey is modelled with its own distinct characteristics;
- contextual and reporting relationships are explicitly typed; and
- no contradictory or duplicated event facts are created.

The existing Candidate A and Candidate B 1-to-many Event→Occurrence relationship is not, by itself, proof that the design is wrong. The unresolved issue is whether that link means contextualization, hierarchy, specialization or reporting. The candidates must state and enforce the intended semantics rather than leave the relationship label ambiguous.

### 16.2 SurveyTarget supports both a priori intention and post-facto filtering

Directly retrieved Darwin Core Conceptual Model §2.2 states that a SurveyTarget may declare what was sought either through a priori intention or through post-facto filtering. The same section says Survey results are expressed through reported Occurrences, which may match target criteria or be incidental/bycatch.

Consequences:
- EVT-D03 must not restrict SurveyTarget to pre-fieldwork intention.
- Preserve target origin/mode (a priori intent, post-facto filter, or other explicitly justified mode), criteria, author/agent, time and provenance.
- Never rewrite a post-facto filter as original field intent.
- Do not retrospectively invent a scope to justify an absence inference.
- Include target include/exclude criteria and combinations of taxonomic, environmental and organismal scope where relevant.

### 16.3 Reporting completeness, sampling completeness and detectability are distinct

Directly retrieved List of Terms definitions confirm:
- eco:isSurveyTargetFullyReported (term version 2026-05-26): whether all counts of detected Occurrences matching an eco:SurveyTarget were fully reported.
- eco:isTaxonomicScopeFullyReported (term version 2026-10-13): whether every detected Occurrence within the stated taxonomic scope was reported.
- dwc:occurrenceStatus (term version 2026-05-26): a statement about detection or non-detection of an Organism during an Event; recommended default values are detected and notDetected.

These reporting-completeness terms do not establish exhaustive field coverage, perfect protocol execution, detectability or 100% detection probability. The logical model must distinguish target intent, protocol selected, protocol performed, effort expended, assessment status, spatial/temporal coverage, reporting completeness, detectability limitations and explicit Occurrence result.

### 16.4 Hierarchy rules: no implicit property inheritance, but explicit scope propagation and bounded inference

The GBIF survey guide v1.0.2 §3.2.2 says:
- child Event values must not be assumed to inherit from parent Events;
- parent Event values must not be derived or summarized from child Events;
- values applicable at multiple levels should be explicitly reported at each level.

The Humboldt hierarchical-event guidance's Principle of Inference separately says that scope/completeness terms can support interpretation across a hierarchy. Such terms MUST be populated at the highest-level Survey to which they apply and at every descendant Survey to which the same scope/completeness statement applies. Scope terms must be populated whenever the scope was in effect and must not be inferred retrospectively.

These are compatible rules:
- no silent copying of parent values into child records;
- no calculation of parent values from child records;
- explicit repeated reporting of scope/completeness at each applicable Survey level;
- profile- and scope-bounded inference only when the exact conditions are satisfied.

The TDWG hierarchy guidance also defines a child Event as wholly contained within its single parent in both space and time, with a dependent connection. Add a test for containment violations.

### 16.5 Standards publication version discrepancy remains unresolved

Direct retrieval of the current Darwin Core Conceptual Model and List pages displays 2026-05-26 as the current page version. Search-indexed metadata in this review session has also surfaced 2026-10-13 publication dates for TDWG resources. Direct retrieval of exact 2026-10-13 versioned Conceptual Model/List resources was unavailable, and the hierarchy landing page retrieval returned a cache miss. Do not state that the 2026-10-13 Conceptual Model or List publication is verified.

At the same time, the directly retrieved List contains individual Humboldt term versions dated 2026-10-13, including eco:isTaxonomicScopeFullyReported, eco:protocolDescriptions, eco:protocolReferences and several organismal-scope completeness terms. Other terms remain at 2026-05-26, including eco:isSurveyTargetFullyReported and dwc:occurrenceStatus. This confirms that publication date and individual term-version date must not be conflated.

**DR-09 remains OPEN.** Pin the exact resource and term-version IRIs only after reproducible retrieval. The direct page display and search-index metadata discrepancy must be recorded, not guessed away.

### 16.6 Owner policy decision still required: implicit absence in external exports

GBIF guide v1.0.2 explicitly describes implicit absence in DwC-A when eco:isTaxonomicScopeFullyReported is true and a target or excluded taxonomic scope is specified. It explains that an unreported taxon within the fully reported scope can then be interpreted as not detected. The guide also states that absence cannot be asserted for bycatch.

This is not inference from a missing row alone: it depends on explicit scope and reporting-completeness metadata. Nevertheless, the permanent AI Project Operating Prompt says “Never infer absence from a missing record.”

**Project-owner clarification is still required:** does the no-inference rule prohibit implicit absence even in a strictly scoped, profile-specific export, or may Botanica Indica support that external interpretation when all Humboldt/GBIF prerequisites are explicitly satisfied? No implementation of implicit absence export should begin until the owner decision is recorded. This review does not change the operating prompt.

### 16.7 Validation suite extension

The EVT pack now contains EVT-23–EVT-26. The complete proposed suite is EVT-01–EVT-26. All remain **Not tested** until executable fixtures, expected results, implementation revision and reviewer evidence are recorded.

### 16.8 Source references

- Darwin Core Conceptual Model, direct page: https://dwc.tdwg.org/cm/
- Darwin Core List of Terms, direct page: https://dwc.tdwg.org/list/
- Darwin Core occurrenceStatus term: http://rs.tdwg.org/dwc/terms/version/occurrenceStatus-2026-05-26
- Humboldt isSurveyTargetFullyReported term: http://rs.tdwg.org/eco/terms/version/isSurveyTargetFullyReported-2026-05-26
- Humboldt isTaxonomicScopeFullyReported term: http://rs.tdwg.org/eco/terms/version/isTaxonomicScopeFullyReported-2026-10-13
- GBIF Guide for publishing biological survey and monitoring data v1.0.2 (2025-09-24): https://docs.gbif.org/guide-publishing-survey-data/en/
- Humboldt hierarchical-event guidance: https://dwc.tdwg.org/hierarchy/

No accepted ADR or Task 05B/05C/05D proposal was changed. No model decision was approved. No test was executed. Task 05C remains NOT APPROVED; Task 05E remains NOT READY.

 
## 17. Owner decision ODR-01 — 21 November 2026

The project owner authorized Option B: controlled, profile-specific implicit non-detection interpretation in external exports only.

This resolves the owner-policy question raised in §16.6; it does not resolve the underlying scientific-model or mapping blockers. The internal rule remains that a missing Occurrence row alone is unknown/not assessed and must not create an internal absence assertion. An external export may derive “not detected/reported within the stated survey scope” only with explicit scope and applicable completeness, correct Survey hierarchy, attributable evidence/provenance, pinned term/profile/mapping versions, and a reproducible audit trail. Bycatch and taxa outside scope are excluded. Any missing, ambiguous, contradictory or unvalidated condition causes the export to fail closed.

For the GBIF DwC-A taxonomic-scope pattern, GBIF Guide v1.0.2 §7.3 requires `eco:isTaxonomicScopeFullyReported=true` and either `eco:targetTaxonomicScope` or `eco:excludedTaxonomicScope`; its implicit pattern does not create Occurrence rows for implicitly absent taxa and uses `eco:isAbsenceReported=false` for the relevant Events. This must not be confused with explicit Occurrence-level non-detection.

EVT-27–EVT-30 are added as proposed, unexecuted export tests. B16 remains open for scientific semantics and mapping. LDM-16/FLD-08 remain required for explicit internal non-detection and missing-row negative tests. DR-09 remains open. No Task 05C candidate was modified or approved; Task 05E remains NOT READY.

Sources: GBIF Guide v1.0.2 (2025-09-24), §§5.6 and 7.3 (https://docs.gbif.org/guide-publishing-survey-data/en/); TDWG List of Terms (https://dwc.tdwg.org/list/); Humboldt hierarchy guidance (https://dwc.tdwg.org/hierarchy/).
