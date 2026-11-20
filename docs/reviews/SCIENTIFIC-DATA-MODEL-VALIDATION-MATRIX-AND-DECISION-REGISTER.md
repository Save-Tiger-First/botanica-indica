# Botanica Indica — Scientific Data Model Validation Matrix and Decision Register

**Document type:** Independent-review working package  
**Version:** 0.1 — Proposed for external review  
**Status:** Draft; no external review or sign-off recorded  
**Prepared:** 16 November 2026  
**Repository:** `Save-Tiger-First/botanica-indica`  
**Related review pack:** `docs/reviews/SCIENTIFIC-DATA-MODEL-REVIEW-PACK.md`

---

## 1. Purpose and decision boundary

This package turns the existing Task 05C integrity scenarios LDM-01 through LDM-16 and Task 05D validation scenarios into a reviewer-ready test and decision framework.

It is intended to help qualified reviewers determine whether the proposed logical model preserves botanical meaning, evidence, source provenance, temporal history, rights and spatial sensitivity. It is not a claim that the model has passed review.

**No reviewer, institution, Indigenous community or knowledge holder is represented as having approved this document.** Reviewer names, qualifications, affiliations, conflicts, findings and sign-off must be entered by the actual reviewers.

This package does not authorize physical SQL design, implementation, ingestion of external datasets or collection of community-held knowledge. Task 05E remains blocked until the readiness criteria in Section 8 are met and the project owner explicitly authorizes the next task.

### 1.1 Review outcomes

Use only these controlled outcomes for each test or decision:

- **Pass:** the cited document revision and supplied reproducible test evidence meet the stated acceptance criteria.
- **Pass with condition:** the core requirement is met, but a bounded non-core condition remains with owner and due date.
- **Fail:** the model or evidence does not meet the criterion.
- **Not tested:** no reproducible evidence was supplied.
- **Not applicable:** reviewer explains why the scenario is outside the agreed scope.
- **Needs domain decision:** the model cannot be judged without a named scientific, legal, community or engineering decision.

A statement in a document is not test evidence. A diagram is not proof of referential integrity. A GitHub mergeable flag is not scientific approval.

## 2. Exact source revisions for this review

The following repository branch heads and file blob SHAs were fetched for this review preparation. Reviewers must re-fetch and record the revisions actually reviewed; these are a baseline snapshot, not a permanent pin.

| Source document | PR / branch | File blob SHA at preparation |
|---|---|---|
| Task 05 — Data Architecture | PR #3 / `docs/task-05-data-architecture` | `3c011c1256eb69f1e7170c23e8515da23323d912` |
| Task 05B — Scientific Data Dictionary | PR #4 / `docs/task-05-data-dictionary` | `f7fe078fe2749d558a1e099ef45b5e5d990df558` |
| Task 05C — Logical Database Model | PR #5 / `docs/task-05c-logical-data-model` | `e6131e867d4bc3dbc58aa1188d0fabc895429347` |
| Task 05D — Validation and Readiness | PR #11 / `docs/task-05d-logical-model-validation-v3` | `acf446b1bf0204fa0400621711603ab23cc80ff2` |
| Scientific Data Model Review Pack | PR #9 / `review/scientific-data-model-review-pack` | `dab7427c7c1724dbda1f375289ecde0a286e21c6` |

**Revision note:** Task 05B's file blob SHA must be filled from the exact fetch performed by the reviewer before sign-off. Do not substitute a branch head commit SHA for a file blob SHA. The reviewer must also record the corresponding commit SHA and date for every document reviewed.

## 3. Discipline-specific review responsibilities

| Discipline | Review scope | Minimum reviewer capability | Cannot approve alone |
|---|---|---|---|
| Botanical taxonomist | TaxonName, TaxonConcept, treatments, nomenclature, synonymy, rank and concept mappings | Relevant botanical taxonomic expertise and familiarity with applicable nomenclatural code(s) | Database integrity, rights or legal compliance |
| Field botanist / ecologist | Observation, Occurrence, Organism, Event, survey effort, material evidence and non-detection | Field survey / plant ecology experience relevant to intended use | Taxonomic nomenclature or production security |
| Biodiversity informatician | TCS, Darwin Core, GBIF profiles, identifiers, source mappings and exchange lossiness | Practical biodiversity data standards experience | Community authorization or legal interpretation |
| Database / geospatial architect | Keys, cardinalities, constraints, transactions, versioning, spatial reference and query patterns | Production relational database and geospatial design experience | Scientific correctness of taxonomy |
| Rights / privacy / security reviewer | Source rights, media rights, consent, sensitive locations, access, retention, deletion and downstream use | Relevant legal, privacy, licensing or security competence | Taxonomic authority |
| AI/ML reviewer | Candidate scores, calibration, model provenance, evaluation and data rights | Applied ML evaluation and model governance experience | Botanical identification validation without relevant domain expertise |
| Community-designated reviewer, where community-held knowledge is in scope | Authority, knowledge categories, permissions, interpretation, benefits and governance | Designated through the relevant community's own process | The authority of other communities or rights holders |

One reviewer may cover multiple disciplines only where competence and independence are documented. The author of a design should not be the sole approver of a high-risk decision they authored.

## 4. LDM-01 to LDM-16 acceptance matrix

The scenarios below preserve Task 05C's original intent. The test IDs in Task 05D are cross-references; if a test fixture does not exist yet, mark it **Not tested**, not Pass.

| LDM ID | Scenario and invariant | Task 05D cross-reference | Required reviewer(s) | Required evidence for Pass |
|---|---|---|---|---|
| LDM-01 | Same TaxonName used in two treatments: two distinct treatment-scoped TaxonConcepts can coexist; identity is not inferred from name string alone. | TAX-01, TAX-07 | Taxonomist; biodiversity informatician | Two source-grounded treatments, two concept records, stable distinct identifiers, query output showing no name-only merge, and documented accordingTo resources. |
| LDM-02 | One TaxonConcept has multiple synonym names; each TCS synonym target is a TaxonName, not another TaxonConcept or TaxonNameUsage. | TAX-02 | Taxonomist; biodiversity informatician | Fixture with at least two synonym names; relationship target types inspected; source treatment and name usage retained; valid TCS mapping/export example. |
| LDM-03 | Two TaxonConcepts partially overlap; mapping records subject, object, exact relation and mapping source without losing direction. | TAX-03 | Taxonomist; biodiversity informatician | Source-backed or explicitly illustrative concepts; relation semantics reviewed; directionality test; mapping source; round-trip mapping test; no inference from name similarity. |
| LDM-04 | Basionym/name relationship and nomenclatural type specimen are separate structures and are not inferred from textual similarity. | TAX-04, TAX-05 | Taxonomist; collection/specimen specialist | Name-to-name nomenclatural relation plus separate NomenclaturalType record and specimen reference; code-specific terminology and cited source verified. |
| LDM-05 | Observation with images but no identification remains valid; no placeholder or fabricated TaxonConcept is created. | FLD-01 | Field botanist; architect | Insert/read test with media and no taxon determination; API and search output preserve unidentified status; no placeholder taxon. |
| LDM-06 | One AI IdentificationRun can return multiple candidates; no candidate is automatically a confirmed identification. | ID-01, ID-05 | AI/ML reviewer; botanist | Reproducible run fixture, three or more candidates, rank/score semantics, model/pipeline/backbone versions, and proof that no accepted determination is created without an explicit workflow action. |
| LDM-07 | Expert changes an identification: new determination and review history are retained; prior AI and expert assertions are not overwritten. | ID-03, ID-04, ID-06 | Botanist; AI/ML reviewer; architect | Append/supersession test, two disagreeing assessments, attribution and timestamps, evidence relationships, and authorized history query. |
| LDM-08 | One Organism can link to repeated Occurrences over time where individual/group identity is genuinely justified. | FLD-03 | Field botanist / ecologist; architect | Fixture with repeated events and observations, explicit organism identity evidence, cardinality checks, and negative test preventing automatic organism creation per photo. |
| LDM-09 | One Occurrence may be supported by a MaterialEntity and multiple MediaAssets as distinct evidence paths. | FLD-04, FLD-05; evidence relationships | Field botanist; collection specialist; architect | Specimen/material and at least two media assets linked independently; material derivation provenance preserved; media rights separately evaluated. |
| LDM-10 | Conflicting native-range sources remain separate scoped DistributionAssertions; no global native/introduced Boolean overwrites the evidence. | GEO-04; Indian test fixtures | Botanist / biogeographer; biodiversity informatician | Two source-backed assertions with source, geography, date/version, scope and verbatim values; normalized comparable geographic units; conflict visible in query/report. |
| LDM-11 | Restricted rare-plant coordinate is generalized or withheld from public API, export and search. | GEO-01, GEO-06; security tests | Geospatial architect; security/privacy reviewer; conservation specialist | Threat model; role-based tests across API, search, export, logs, media metadata and backups; public response contains no exact coordinate or reconstructable sensitive locality. |
| LDM-12 | Dataset license and embedded MediaAsset license are evaluated separately. | RGT-01, RGT-02 | Rights reviewer; data architect | Fixture with differing dataset and image terms; policy decision for display, download, redistribution and derivative use; denied operation test. |
| LDM-13 | Re-ingestion creates a new DatasetVersion/IngestionRun and preserves stable source/internal identifiers without silent duplication or overwrite. | SRC-01, SRC-03, SRC-04 | Data architect; biodiversity informatician | Two source versions, two runs, idempotency/reconciliation report, stable identifier comparison, changed source value retained verbatim, quarantine/retry evidence. |
| LDM-14 | District boundary revision is versioned; historical location evidence is not silently rewritten when boundaries change. | GEO-05 | Geospatial architect; GIS/domain reviewer | Two boundary versions with valid-time/provenance; record query against original and current boundaries; proof that historical source geometry/administrative context remains traceable. |
| LDM-15 | When raw source payload retention is prohibited, the payload is not stored; only specifically permitted metadata, references and provenance are retained. | SRC-02; rights review | Rights reviewer; data architect; security reviewer | Source terms/permission analysis; ingestion fixture; storage/object-store/log/backup checks; proof no prohibited payload persists; approved retention decision. |
| LDM-16 | Defined survey does not detect a target taxon: an explicit absent/non-detected Occurrence is linked to the relevant Survey/Event, protocol, effort, target and location. Absence of an Occurrence row is never interpreted as evidence of absence. | FLD-08; Darwin Core sampling-event mapping | Ecologist; biodiversity informatician; architect | Survey fixture with target list, protocol, effort, time and location; explicit internal non-detection state; negative test showing missing row is unknown/not surveyed, not non-detected; validate the chosen Darwin Core/GBIF profile vocabulary (Darwin Core `occurrenceStatus` recommends `detected` / `notDetected`; GBIF guidance also describes `present` / `absent` values in its sampling-event recommendations). |

### 4.1 Global acceptance rules for all LDM scenarios

Every test must also demonstrate, where applicable:

1. Stable internal identifiers and source identifiers are not conflated.
2. Source, version, retrieval/access date and provenance are retained.
3. Uncertainty and unknown values are not silently converted to precise values.
4. Conflicting evidence is retained rather than overwritten.
5. Permissions are evaluated for the specific operation, not inferred from public visibility.
6. Sensitive data is protected in derived systems, not just the primary database.
7. A reviewer can reproduce the test from the fixture, test instructions and recorded software revision.

### 4.2 Editorial correction required in Task 05C

The current LDM-16 wording contains the phrase “no Occurrence row is never interpreted as absence”, which is grammatically ambiguous. Replace it with:

> “The absence of an Occurrence row must never be interpreted as evidence of absence.”

This is a documentation correction, not a change to the intended model rule.

## 5. Standards and semantic verification notes

### 5.1 Taxon Concept Standard

The current TDWG TCS List of Terms identifies version 2025-12-11. It requires a TCS TaxonConcept to have exactly one `taxonName` and one `accordingTo` resource. A TaxonConceptMapping requires subject, mapping relation and object, with one of six mapping relations: `isCongruentWith`, `includes`, `isIncludedIn`, `partiallyOverlaps`, `isDisjointFrom` or `intersects`. TCS synonym is a TaxonConcept-to-TaxonName relation; nomenclatural name relations such as basionym belong to TaxonName semantics.

Official source: https://tcs.tdwg.org/terms/

Reviewer implications:
- Test exactly-one canonical accordingTo resource, not merely a non-empty string.
- Test that treatment specialization resolves to the same resource.
- Test relation direction and subject/object semantics, not only allowed enum values.
- Do not map an informal “not congruent” assertion automatically to “disjoint”.
- TCS permits taxonName labels beyond formal scientific names, including vernacular or Indigenous knowledge labels. This does not grant permission to expose, redistribute or train on community-held labels or knowledge; rights and access controls remain independent.

### 5.2 Darwin Core Conceptual Model and non-detection

The current Darwin Core Conceptual Model page identifies version 2026-10-13. It describes Occurrence as an Event establishing the state of an Organism at a particular place and time. The model describes an Occurrence as potentially representing direct observation, indirect inference, or absence of detection of an Organism of a given Taxon in a specified state during an Event at a Location. Events may be hierarchical and must have a location context, even if that location is unknown or withheld.

Official source: https://dwc.tdwg.org/cm/

Reviewer implications:
- Do not model an Occurrence as merely a row asserting “species present”.
- Keep Event, Survey, Occurrence, Organism and MaterialEntity semantics distinct.
- Define how the internal Survey/Event model maps to the current Darwin Core conceptual model.
- Test non-detection as an explicit, bounded survey result; no row means unknown/not recorded, not absent.

### 5.3 GBIF occurrence vs sampling-event publishing profiles

GBIF's current technical recommendations distinguish occurrence datasets from sampling-event datasets. The technical recommendations table describes `basisOfRecord`, `scientificName` and `eventDate` as strongly recommended for the general occurrence profile and required for GBIF-managed programmes; sampling-event datasets have separate event, protocol, sample-size and effort expectations. The sampling-event guidance specifically notes that negative occurrences may be useful where sampling effort and protocol are documented.

Sources:
- https://techdocs.gbif.org/en/data-publishing/data-quality-recommendations
- https://www.gbif.org/data-quality-requirements-occurrences

**Documentation discrepancy to resolve before implementation:** the GBIF general requirements page and the current technical recommendations page do not present every occurrence field with identical status wording. Do not hard-code one blanket interpretation into the internal model. The export validator must be configured against the exact current GBIF dataset profile, programme requirements and publishing guidance being targeted, with version/date recorded. This review does not settle that publisher-specific discrepancy.

### 5.4 PostgreSQL constraints

PostgreSQL documents that CHECK constraints are evaluated on the row being inserted/updated and must not be used to enforce arbitrary conditions against other table rows. Foreign keys enforce referential integrity to referenced rows. A row-local exactly-one-non-null check across the three nullable subject FK columns is a plausible constraint pattern, but it does not replace the three actual foreign keys, uniqueness constraints or validation of the intended subject inventory.

Official source: https://www.postgresql.org/docs/current/ddl-constraints.html

Reviewer implications:
- Verify one IdentificationSubject per Identification if that is the intended invariant.
- Verify exactly one target FK is non-null.
- Verify each target FK references an existing row.
- Verify deletion/update behaviour and transaction semantics.
- Verify ScientificAssertion subject links separately; do not assume its subject inventory is identical to IdentificationSubject.
- Do not rely on CHECK for cross-table consistency.

## 6. Cross-document and unresolved design decision register

The following are decision prompts, not decisions already approved. For every row, the reviewer must record outcome, rationale, evidence, owner and re-review requirement.

| Decision ID | Question to resolve | Required discipline | Minimum acceptance evidence |
|---|---|---|---|
| B01 | Observation–Occurrence cardinality and ownership | Field botanist + biodiversity informatician | Cardinality diagram and test fixtures covering one-to-many/many-to-many cases |
| B02 | Event, Survey, plot and sampling hierarchy | Ecologist + architect | Survey protocol, effort, parent/child Event and repeat-survey fixtures |
| B03 | TaxonConcept identity and treatment versioning | Taxonomist | TCS-conformant concept examples, stable identity and treatment-version tests |
| B04 | TaxonNameUsage and source-specific acceptance | Taxonomist + informatician | Competing treatments and source usage fixtures; no global accepted-name field |
| B05 | Identification subject inventory and FK integrity | Taxonomist + architect | Complete target-type inventory, row-level CHECK and FK tests, deletion policy |
| B06 | Evidence-to-assertion cardinality and contradiction model | Scientific reviewer + architect | Supporting, contradicting and qualifying evidence fixtures |
| B07 | Source record vs normalized entity vs curated assertion | Informatician + architect | Re-ingestion, mapping, deduplication and lineage tests |
| B08 | Rights granularity and derived-asset inheritance | Rights/privacy reviewer | Dataset/media/record/derivative permissions and denied-operation tests |
| B09 | Exact/restricted/generalized geospatial design | Geospatial + privacy reviewer | Threat model and API/export/search/log/backup leak tests |
| B10 | Historical versioning and supersession | Architect + domain reviewer | Temporal queries and immutable history tests |
| B11 | Controlled vocabularies and Indian geography sources | Domain + geospatial reviewer | Source/version registry and geographic reconciliation fixtures |
| B12 | External standard versions and export profiles | Biodiversity informatician | Pinned TCS/Darwin Core/GBIF profile versions and loss-aware mappings |
| B13 | Retention, deletion, withdrawal and legal hold | Privacy/legal reviewer | Retention schedule, rights/consent withdrawal and audit tests |
| B14 | Identification score semantics and calibration | AI/ML reviewer | Calibration evidence and UI/API score semantics |
| B15 | Expected data volumes and query workload | Engineering lead | Workload estimates, representative queries and measured query plans |
| B16 | Internal non-detection semantics and external sampling-event mapping | Ecologist + biodiversity informatician | Survey fixture, negative-occurrence semantics and target-profile export validation |
| B17 | ScientificAssertion subject target inventory | Domain architect + scientific reviewers | Exhaustive subject-type list, enforceable FK design and unsupported-target negative tests |
| B18 | Source rights and reuse by operation | Rights reviewer | Separate permissions for access, ingestion, storage, display, derivative creation, redistribution and AI training |

### 6.1 DR finding disposition

The prior desk-review findings are not automatically closed by documentation edits.

| Finding | Current disposition for external review |
|---|---|
| DR-01 to DR-07 | Revised in proposed documents; require test and discipline review before closure |
| DR-08 | Open source/geographic-resolution case; normalize geographic units and source scopes |
| DR-09 | Withdrawn as erroneous; the earlier review misread the Darwin Core release date |
| DR-10 to DR-12 | Revised in proposed documents; require source, rights and taxonomic review before closure |

No finding should be marked closed solely because wording changed.

## 7. Required reviewer test record

Copy this record once per LDM test and once per blocking decision.

### Review record template

- Review record ID:
- LDM / FLD / TAX / ID / GEO / RGT / SRC / B decision ID:
- Source document path:
- Source file blob SHA:
- Source branch and commit SHA:
- Reviewer name:
- Reviewer role / discipline:
- Relevant qualifications / experience:
- Affiliation (if reviewer consents to record it):
- Conflict-of-interest declaration:
- Date:
- Fixture identifier and provenance:
- Test environment / software version:
- Test procedure:
- Expected result:
- Actual result:
- Evidence links / logs / screenshots / query outputs:
- Outcome: Pass / Pass with condition / Fail / Not tested / Not applicable / Needs domain decision
- Findings and rationale:
- Required document/model change:
- Owner:
- Due date:
- Re-review required:
- Reviewer sign-off (or explicit non-approval):

**No blank reviewer fields may be interpreted as approval.**

## 8. Task 05E readiness gate

Task 05E (physical database design) remains **Blocked** until all of the following are true:

1. LDM-01 through LDM-16 each have an outcome and reproducible evidence, or a documented justified Not applicable outcome.
2. All blocking decisions B01 through B15 in the current review pack have a documented disposition, accountable owner and evidence. Core identity/cardinality/rights/sensitive-location decisions cannot be deferred.
3. Taxonomic identity, synonym, nomenclatural and concept-mapping semantics have been reviewed by a qualified botanical taxonomist.
4. TCS and Darwin Core mappings have been reviewed by a biodiversity-informatics specialist against pinned current versions.
5. Event, Occurrence and non-detection semantics have been reviewed by an ecologist/field specialist.
6. Typed subject references and source-record references have been validated by a database architect with integrity test evidence.
7. Sensitive-location and personal-data risks have a reviewed threat model and negative tests.
8. Rights and permitted uses are evaluated separately for datasets, records, media and derivatives, including AI/ML training.
9. Indian botanical source profiles and the Mango geographic-resolution case are reviewed at claim level.
10. Independent reviewer findings, dissent and conflicts of interest are recorded.
11. Task 05B, 05C and 05D are reconciled to the exact reviewed revisions; no contradictory field or cardinality definitions remain.
12. The project owner records an explicit Ready / Ready with conditions / Not ready decision.

**Current readiness: NOT READY.** This package has been prepared for review; it is not itself a review result. No external reviewer sign-off has been received.

## 9. Proposed review sequence

1. **Desk review:** taxonomist and biodiversity informatician review Sections 4 and 5, especially LDM-01 to LDM-04 and the standards mappings.
2. **Field/ecology review:** review LDM-05, LDM-08, LDM-09, LDM-10 and LDM-16 using realistic Indian botanical and survey cases.
3. **Architecture review:** review typed references, keys, cardinalities, versioning, geospatial handling and all negative integrity tests.
4. **Rights/privacy review:** review LDM-11, LDM-12, LDM-15 and B08/B09/B13/B18.
5. **AI/ML review:** review LDM-06/LDM-07 and score semantics.
6. **Reconciliation:** authors update the source documents only after review comments are captured; maintain a change log and do not erase dissent.
7. **Readiness meeting:** all relevant reviewers state their outcome; project owner decides whether Task 05E can proceed.

Attendance, silence, a positive GitHub mergeability value or an empty CI status is not sign-off.

## 10. Research and standards register

The following authoritative sources were checked during preparation. Reviewers should re-check current versions before implementation and record the version identifiers they used.

1. TDWG Taxon Concept Standard, List of Terms (version 2025-12-11): https://tcs.tdwg.org/terms/
2. TDWG Darwin Core List of Terms (version issued 2026-10-13; `occurrenceStatus` term version modified 2026-05-26): https://dwc.tdwg.org/list/ and Darwin Core Conceptual Model: https://dwc.tdwg.org/cm/
3. GBIF Data Quality Recommendations, including occurrence and sampling-event profiles: https://techdocs.gbif.org/en/data-publishing/data-quality-recommendations
4. GBIF Data Quality Recommendations (occurrence and sampling-event profiles, including profile-specific status vocabulary): https://techdocs.gbif.org/en/data-publishing/data-quality-recommendations
5. PostgreSQL 18, Constraints (CHECK is row-local; use FKs/UNIQUE for referential and cardinality integrity; cross-row requirements may need transaction/trigger design): https://www.postgresql.org/docs/18/ddl-constraints.html
6. PostGIS documentation: https://postgis.net/documentation/
7. W3C PROV-O: https://www.w3.org/TR/prov-o/
8. CARE Principles for Indigenous Data Governance: https://doi.org/10.5334/dsj-2020-043
9. Convention on Biological Diversity, Article 8(j): https://www.cbd.int/traditional

## 11. Decision status

**Draft independent-review package.** The logical model is not yet approved. Task 05E remains blocked. This document must be completed by actual reviewers with evidence and decisions; it must not be populated with invented reviewer identities, assumed approvals or retrospective claims of validation.


## 12. Additional implementation cautions identified during standards verification

### 12.1 A row-local CHECK is necessary but not sufficient for total participation

The Task 05C `IdentificationSubject` proposal can use a row-local CHECK to require exactly one of its three target FK columns to be non-null, with each FK enforcing target existence. A UNIQUE constraint on the Identification FK prevents multiple subject rows for one Identification. However, these constraints alone do not guarantee that every Identification has a corresponding subject row: that is a cross-table existence/cardinality requirement.

PostgreSQL documentation explicitly cautions that CHECK constraints cannot safely enforce conditions depending on other table rows. The implementation must choose and test an appropriate transactionally safe design, such as creating Identification and its subject link in one controlled transaction with appropriate privileges and deferred/constraint-trigger enforcement if database-level total participation is required. The physical design reviewer must decide and prove the approach; do not claim that the CHECK alone enforces exactly one subject for every Identification.

Official reference: https://www.postgresql.org/docs/18/ddl-constraints.html

### 12.2 Non-detection vocabulary must be mapped, not assumed identical

The current Darwin Core List of Terms was issued 2026-10-13, but the individual `occurrenceStatus` term was modified 2026-05-26. Its definition concerns detection or non-detection of an Organism during an Event and recommends `detected` and `notDetected` as default vocabulary values.

GBIF's sampling-event recommendations describe `occurrenceStatus` and give `present` and `absent` as standard values in that publishing context. GBIF also explains that sampling-event datasets can support absence inference only when sampling method and effort are described.

Therefore, Botanica Indica must retain a well-defined internal detection state and an explicit, profile-specific mapping. It must not silently assume `notDetected` and `absent` are interchangeable literal values across all exports. Test both the internal semantics and each target publishing profile.

Official references:
- https://dwc.tdwg.org/list/
- https://techdocs.gbif.org/en/data-publishing/data-quality-recommendations

### 12.3 Review status is not execution status

The LDM matrix is a test plan until reproducible fixtures, database constraints, API/export tests, logs and reviewer outcomes are attached. At preparation time, these scenarios have been mapped to the documents but have not been executed against a physical schema. All such cases must remain **Not tested** until actual evidence exists.


## 13. Competing Task 05C model reconciliation

A full desk comparison of the two competing Task 05C documents is recorded in [Task 05C Competing Model Reconciliation Assessment](TASK-05C-COMPETING-MODEL-RECONCILIATION.md) and summarized in Section 4.6 of the Scientific Data Model Review Pack.

**Proposed canonical review candidate:** the Task 05C document in PR #5. The alternative Task 05C document is retained as a reference source; do not merge it wholesale. Its workflows and cardinality discussions may be ported selectively after semantic reconciliation.

**New blocking design questions:**
- Model Darwin Core Event as the contextual supertype and evaluate Survey and Occurrence as specialized event types/extensions. A shared contextual Event may provide time/location context to multiple Occurrences and Material Entities.
- Define how Botanica Indica's contributor Observation relates to one or more Events/Surveys and Occurrences without equating a user submission with a scientific event.
- Prove Identification subject total participation and exactly-one-target integrity; a row-local CHECK alone does not prove that every Identification has a subject row.
- Define and test the complete ScientificAssertion subject-type inventory.

The LDM-16 sentence in the PR #5 Task 05C document has received a narrow editorial correction to state: “the absence of an Occurrence row must never be interpreted as evidence of absence.” No scientific meaning or model cardinality was changed by that edit.

These are proposed dispositions, not expert sign-off. All LDM cases remain Not tested until executable fixtures and actual implementation evidence are recorded. Task 05E remains NOT READY.


## 14. Cross-document reconciliation updates (20 November 2026)

See [Task 05C Competing Model Reconciliation Assessment](TASK-05C-COMPETING-MODEL-RECONCILIATION.md), Sections 11–12, and Section 4.7 of the Scientific Data Model Review Pack.

| Topic | Current proposed alignment | Remaining validation |
|---|---|---|
| Event / Survey / Occurrence | Task 05 now describes Survey and Occurrence as specialized Event types, with a contextual Event capable of providing shared context to multiple Occurrences and Material Entities | Review Event supertype/subtype implementation, nested Events, Survey targets/completeness, Observation links and Darwin Core mapping with ecologist and biodiversity informatician |
| IdentificationSubject | Task 05B and Task 05C now align on one IdentificationSubject row per Identification with three nullable real target FKs and a row-local exactly-one CHECK | Prove unique Identification FK, target FK integrity and total participation; CHECK alone does not ensure a subject row exists |
| GBIF profiles | Task 05 now distinguishes general occurrence, GBIF-managed and sampling-event publishing profiles | Pin the exact target profile/version and execute export validation; do not convert publishing expectations into internal validity rules |
| PR #11 stacked dependency | PR #11 branch diverges from the updated PR #5 base by one commit each | Synchronize/rebase PR #11 onto the latest PR #5 head, reconcile DR-02 and Event/Occurrence text, then re-review full diff |

The Task 05 and Task 05B edits are present on their existing PR branches but are not merged. No LDM test has been executed by these documentation edits. Task 05E remains NOT READY.
