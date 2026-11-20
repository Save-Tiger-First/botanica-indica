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

The current Darwin Core Conceptual Model page identifies version issued 2026-05-26. It describes:
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
- The current Darwin Core Conceptual Model (issued 2026-05-26) states that Occurrence and Survey are specialized Event types, and that one contextual Event may provide shared spatio-temporal context to multiple Occurrences and Material Entities. It also expressly says the conceptual model is non-normative and does not prescribe a database schema.

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

The PR #11 document's DR-02 row currently describes the row-local CHECK pattern but must also be reconciled with the total-participation caveat now recorded in Task 05B, Task 05C and the validation register. Its Event/Occurrence assumptions also need to be updated after the design review.

### 11.5 Verification state of the cross-document edits

The Task 05 and Task 05B edits were committed on their existing PR branches and must be reviewed in PR #3 and PR #4. They are document-level proposals only. No PR was merged, no external expert approval is claimed, and Task 05E remains NOT READY.

## 12. Updated recommendation

1. Retain PR #5 Task 05C as the canonical review candidate, subject to resolution of the Event/Survey/Occurrence pattern and Observation/Event cardinalities.
2. Retain the single-row typed-FK `IdentificationSubject` pattern as the preferred logical option, with total participation treated as a separate integrity requirement.
3. Review the Task 05 / Task 05B edits in PRs #3 and #4 for scientific and editorial correctness.
4. Synchronize PR #11 with the latest PR #5 head and reconcile its DR-02 and Event/Occurrence wording before any merge decision.
5. Keep all four scientific architecture PRs in draft until their blocking questions and independent discipline reviews are complete.
6. Keep Task 05E blocked.


**Standards-date correction (20 November 2026):** the live TDWG Conceptual Model page states `Date version issued: 2026-05-26`. The live List of Terms page also states `Date version issued: 2026-05-26`, with previous List version 2025-07-10. The `occurrenceStatus` term was modified 2026-05-26. A previous review-pack amendment claiming a 2026-10-13 release was erroneous and has been corrected. Official sources: https://dwc.tdwg.org/cm/ and https://dwc.tdwg.org/list/.
