# Botanica Indica — Scientific Data Model Review Pack

**Document status:** Draft for independent scientific, biodiversity-informatics and engineering review  
**Version:** 0.1  
**Prepared:** 16 November 2026  
**Review scope:** Task 05, Task 05B, Task 05C and Task 05D  
**Repository:** Save Tiger First / botanica-indica  
**Purpose:** Provide one coordinated review instrument before physical PostgreSQL/PostGIS design.  
**Important:** This pack is a review aid. It does not approve the underlying proposals, replace expert review, or authorize production database implementation.

---

## 1. Executive summary

Botanica Indica needs a scientific data model that can preserve the difference between a botanical name, a taxonomic concept, a source-specific taxonomic treatment, a field observation, an occurrence assertion, an identification, evidence, and expert validation. These are not interchangeable concepts.

The current Task 05 documentation proposes a provenance-aware, uncertainty-aware, modular scientific model. Tasks 05B–05D add a data dictionary, Indian botanical test cases, logical relationships and a readiness/validation gate. The overall direction is sound and appropriately cautious. It is not yet sufficient to generate a production schema without review.

This review pack asks reviewers to test the model against real scientific workflows and edge cases, not merely approve its terminology.

### Overall preliminary assessment

**Strengths**
- Correctly distinguishes TaxonName from TaxonConcept and source-specific usage.
- Separates Observation, Occurrence, Event, Identification and Evidence.
- Treats provenance, rights, uncertainty, sensitive geography and historical assertions as first-class concerns.
- Recognizes that an AI output is an assertion/run, not an authoritative taxonomic fact.
- Plans for external standards without forcing the internal model to become a copy of one exchange schema.
- Defers physical implementation until logical relationships and validation are reviewed.

**Risks requiring resolution**
- Exact cardinalities between observations, occurrences, events, specimens, identifications and evidence must be demonstrated through use cases.
- Taxonomic concepts and name usages require a clear identity and versioning strategy; a simple accepted-name/synonym graph will not be sufficient.
- The boundary between a source record, an imported record, a normalized domain entity and a curated assertion must be unambiguous.
- Rights must be represented at the asset, dataset, record and permitted-purpose levels where those levels differ.
- Geographic generalization must preserve original restricted evidence separately from public representations, with access control and audit.
- Scientific claims and AI scores need explicit semantics, provenance and lifecycle.
- Export mappings must be versioned and validated against the relevant current standard release.

**Recommendation:** Proceed to physical design only after the blocking questions in Section 8 have named decisions, evidence and accountable reviewers.

---

## 2. Documents under review

The review concerns these proposed artifacts in the repository:

1. `docs/data-architecture/DATA-ARCHITECTURE-AND-SCIENTIFIC-DATA-MODEL.md` — Task 05.
2. `docs/data-architecture/SCIENTIFIC-DATA-DICTIONARY-AND-INDIAN-TEST-CASES.md` — Task 05B.
3. `docs/data-architecture/TASK-05C-LOGICAL-DATA-MODEL.md` — Task 05C.
4. `docs/data-architecture/TASK-05D-LOGICAL-MODEL-VALIDATION-AND-PHYSICAL-DESIGN-READINESS.md` — Task 05D.

These are currently proposed documents on separate open pull requests. Reviewers should inspect the exact PR revisions and not assume that a file on one feature branch is already part of `main`.

### Review outcomes

For each issue, select one:
- **Accept:** adequately defined and supported.
- **Accept with condition:** acceptable if a specified action is completed.
- **Revise:** material clarification or model change required.
- **Defer:** intentionally outside current scope, with an explicit future boundary.
- **Reject:** scientifically or technically unsound.

Each review comment should identify the relevant document section, the scenario tested, the reason, and the proposed resolution.

---

## 3. Scientific model principles to validate

Reviewers should test whether the model consistently implements these principles.

### 3.1 Taxonomic identity
- A nomenclatural name is not itself a taxonomic concept.
- A name may be used differently by different taxonomic treatments.
- Accepted status is source- and treatment-dependent.
- Synonymy, homonymy, misapplication, inclusion, splitting and lumping are not interchangeable relations.
- Historical determinations must remain interpretable after a taxonomic update.

### 3.2 Evidence and assertions
- Every scientific assertion should identify who or what made it, when, on what evidence, under which source or method, and with what rights.
- Conflicting evidence must be retained and visible to authorized reviewers.
- Absence of evidence is not evidence of absence.
- AI similarity scores must not be represented as calibrated probabilities unless validated as such.
- Expert validation is a separately attributable assessment, not a silent overwrite of an AI or community result.

### 3.3 Field evidence
- An Observation records a human or institutional act of observing or documenting.
- An Occurrence represents evidence that an organism or taxon was present in a place/time or collection context.
- An Event records the sampling or survey context.
- A specimen or material sample has collection, custody and repository context.
- An Identification is an assertion about a subject, and can be revised without deleting its history.

### 3.4 Geography and time
- Coordinates require a datum/CRS, uncertainty, source and method where available.
- Sensitive locations must be governed separately from general public display.
- Administrative and ecological boundaries are versioned source data, not timeless truths.
- Date/time precision and uncertainty must be retained; a month-only or year-only record must not be fabricated into an exact date.
- Native, endemic, introduced, naturalized, cultivated and invasive status is geographically and temporally contextual.

### 3.5 Provenance and rights
- Original source values and normalized values must be distinguishable.
- Transformations, reconciliation decisions and import versions must be reproducible.
- A publicly viewable record is not automatically licensed for redistribution or AI training.
- Rights to code, text, taxonomic data, photographs, user contributions, derived data and model weights may differ.
- Privacy, consent and conservation sensitivity controls apply independently of copyright licenses.

---

## 4. Cross-domain workflow scenarios

The model must be tested against at least the following end-to-end scenarios. Reviewers should identify missing entities, relationships, lifecycle states and constraints.

### Scenario A — Casual plant observation with uncertain identity
A user uploads two photographs of a flowering shrub in a residential garden in Pune. The date is known only to the day. The GPS point is imprecise. The AI proposes three species, none above the acceptance threshold. The user selects “not sure”.

Expected model behaviour:
- Preserve the original media and its rights/consent metadata.
- Record the observation independently of a confirmed identification.
- Preserve location uncertainty and access classification.
- Store the identification run, model version, candidate list and score semantics.
- Represent the user's uncertainty without forcing a species assignment.
- Allow later expert identification without replacing the original run.

### Scenario B — Expert changes an identification
A field botanist identifies an observation as Species A. A taxonomic specialist later concludes the evidence supports Species B under a different taxonomic treatment.

Expected behaviour:
- Preserve both determinations and their authorship/date.
- Record the taxonomic treatment/concept used by each determination.
- Link evidence and rationale to each assertion.
- Mark the current preferred determination without deleting historical claims.
- Explain whether the difference is an identification correction, a taxonomic concept change, or both.

### Scenario C — Source taxonomies disagree
A national flora, a regional flora and a global backbone treat the same name differently.

Expected behaviour:
- Preserve source-specific TaxonNameUsage and treatment provenance.
- Avoid globally overwriting one accepted-name field.
- Support source-scoped relationships and a documented reconciliation decision.
- Make it possible to export according to a selected taxonomic treatment.

### Scenario D — Herbarium specimen record
An institution contributes a specimen-backed record with collector, collection number, herbarium code, catalog number, collection event, determination history and a digitized image.

Expected behaviour:
- Distinguish the specimen from the occurrence and from the digitized media.
- Preserve institution and collection identifiers.
- Record determinations over time.
- Preserve the media's creator, rights and permitted uses.
- Map to relevant biodiversity exchange terms without losing internal detail.

### Scenario E — Survey with repeated sampling
A research team surveys a fixed plot monthly for two years and records multiple taxa on each visit.

Expected behaviour:
- Represent the parent survey, individual sampling events, locations/plots and multiple occurrences.
- Preserve protocol, effort, observer, date precision and environmental context.
- Permit zero observations or non-detection records only when the protocol supports interpreting them.
- Avoid treating every observation as an independent survey event.

### Scenario F — Sensitive or threatened plant locality
A contributor submits a precise location for a rare or commercially exploited plant.

Expected behaviour:
- Preserve original coordinates only in an appropriately restricted store or field.
- Generate generalized/public geometry under a documented rule.
- Record who accessed or changed the restricted coordinates.
- Ensure APIs, exports, logs, analytics, backups and media metadata do not leak exact coordinates.
- Preserve the basis, authority and review date for sensitivity classification.

### Scenario G — Imported distribution record
An external dataset provides a species record with a name, locality, date and coordinates, but has unclear reuse terms.

Expected behaviour:
- Quarantine or restrict the record until rights and source terms are reviewed.
- Preserve verbatim source fields and source record identifiers.
- Record ingestion run, transformation, validation outcomes and errors.
- Prevent unauthorized redistribution and AI training.
- Allow a later rights decision without losing import history.

### Scenario H — Media reused for multiple purposes
A user uploads a plant photograph and permits display in their observation, but does not grant permission for public dataset redistribution or AI training.

Expected behaviour:
- Record purpose-specific permissions and the applicable terms/version.
- Permit only authorized uses.
- Ensure derivative crops, embeddings, thumbnails and training copies inherit or explicitly resolve rights restrictions.
- Support withdrawal, deletion or restriction workflows subject to applicable legal and retention requirements.

### Scenario I — Name changes after publication
A plant profile and observations are published under a name later treated as a synonym by an updated taxonomic source.

Expected behaviour:
- Retain historical name usage and the taxonomy version/treatment displayed at the time.
- Support current accepted treatment and historical display.
- Avoid changing the identity of an occurrence solely because its preferred name changed.
- Track the reconciliation decision and its evidence.

### Scenario J — AI model retraining
A new model is trained using selected images and observations. Some images have display permission only; some are licensed for training; some are expert-validated; some are uncertain.

Expected behaviour:
- Training dataset membership is explicit and reproducible.
- Rights and consent are evaluated for the training purpose.
- Validation status, label provenance, taxonomic treatment and uncertainty are retained.
- Model version, training data manifest, evaluation data and limitations are traceable.
- Prohibited assets are excluded from training and derived training corpora.


### 4.1 Mandatory reconciliation with Task 05C's original 15 integrity tests

The ten review workflows above supplement—not replace—the 15 mandatory acceptance scenarios already defined in Task 05C. Reviewers must record pass/fail/needs-revision for every original scenario and preserve the original test IDs:

| Task 05C test | Required model behaviour |
|---|---|
| LDM-01 | The same TaxonName can be used in two distinct taxonomic treatments with separate TaxonConcepts |
| LDM-02 | Multiple synonym names can relate to one TaxonConcept; synonym relations target names, not another concept |
| LDM-03 | Partially overlapping TaxonConcepts can be mapped with a typed relation and according-to source |
| LDM-04 | Basionym/name relationships and nomenclatural type specimens are retained separately |
| LDM-05 | An Observation with images but no identification remains valid without a fabricated taxon |
| LDM-06 | One AI IdentificationRun can return multiple candidates without automatically confirming one |
| LDM-07 | An expert's changed identification creates a new determination and preserves review history |
| LDM-08 | One Organism can be linked to repeated Occurrences over time where individual identity is meaningful |
| LDM-09 | An Occurrence can be supported by a MaterialEntity and multiple MediaAssets as distinct evidence paths |
| LDM-10 | Conflicting native-range sources remain separate scoped DistributionAssertions |
| LDM-11 | Restricted rare-plant coordinates are generalized or withheld from public API, export and search |
| LDM-12 | Dataset rights and embedded MediaAsset rights are evaluated separately |
| LDM-13 | Re-ingestion creates a new DatasetVersion/IngestionRun while preserving stable identifiers |
| LDM-14 | District boundary version history is retained and does not silently rewrite older location evidence |
| LDM-15 | When raw source payload retention is not permitted, only permitted metadata/references and provenance are retained |

Task 05C also specifies security tests and data-quality integrity rules. These must be retained in the final automated test plan, not treated as optional narrative guidance.

### 4.2 Task 05D's four distinct validation layers

Task 05D correctly separates four validation layers. Reviewers should preserve this separation in the acceptance matrix and future implementation:

1. **Structural validity:** identifiers, required fields, foreign keys, cardinalities, controlled values and geometry validity.
2. **Scientific completeness and evidence quality:** whether a record has enough relevant evidence for the scientific claim being made; completeness is claim-relative.
3. **Rights, privacy and governance eligibility:** whether the record or asset may be stored, displayed, shared, exported or used for a particular purpose.
4. **External publication readiness:** whether a record meets the chosen Darwin Core / GBIF or other exchange profile.

A record can be structurally valid while scientifically incomplete, rights-restricted or not ready for external publication. Do not compress these states into one global “valid” flag.

---

## 5. Indian botanical and ecological test coverage

The model should be tested with realistic Indian data, not only generic examples. These are test dimensions, not claims about any particular taxon.

### 5.1 Geographic coverage
- Western Ghats and associated elevational gradients.
- Eastern Himalaya and other Himalayan zones.
- Indo-Gangetic plains.
- Thar and arid/semi-arid regions.
- Central Indian forests.
- Deccan plateau.
- Northeast India.
- Coastal, estuarine, mangrove and island ecosystems.
- Urban, peri-urban, agricultural and plantation landscapes.

### 5.2 Taxonomic and life-form coverage
- Trees, shrubs, herbs, grasses, sedges, climbers, epiphytes, aquatic plants and ferns.
- Native, endemic, introduced, naturalized, cultivated and invasive taxa.
- Species complexes and difficult genera.
- Synonyms, homonyms, orthographic variants and historical combinations.
- Sterile or incomplete specimens.
- Seasonal forms and life-stage variation.

### 5.3 Evidence coverage
- Whole-plant photographs.
- Leaf, flower, fruit, bark, stem and habit photographs.
- Herbarium specimens and labels.
- Literature-backed records.
- Expert field notes.
- Georeferenced and locality-only records.
- Records with uncertain dates or locations.
- Conflicting or outdated identifications.

### 5.4 Required Indian test-record metadata
Every test record should identify:
- Test-case ID and purpose.
- Taxon name exactly as supplied.
- Taxonomic treatment/source and version/date.
- State/UT and more precise locality only where appropriate.
- Biogeographic/ecological context and its source.
- Native/introduced/cultivated status with geographic scope and source.
- Evidence type and completeness.
- Date and location precision.
- Rights and permitted uses.
- Expected model outcome and known uncertainty.
- Reviewer and review date.

Do not invent taxonomic authority, distribution or conservation status for illustrative examples. Use real records only when their authoritative sources and licenses are documented.

---

## 6. Interoperability and standards review

The internal model should be mapped to external standards through explicit, versioned mappings.

### 6.1 Darwin Core
Review mappings for:
- Occurrence and occurrenceID.
- Event and eventID.
- Taxon and taxonID.
- Identification and identificationID where relevant in the chosen exchange profile.
- Location, coordinates, datum and uncertainty.
- basisOfRecord.
- scientificName, taxonRank and taxonomic hierarchy.
- recordedBy, eventDate, occurrenceStatus and associated references where relevant.

The mapping must state which internal entity supplies each term, transformation rules, lossiness and validation rules. Do not assume every internal concept has a one-to-one Darwin Core field.

GBIF's current occurrence dataset guidance lists occurrenceID as required and identifies fields such as basisOfRecord, scientificName, eventDate, countryCode, taxonRank and coordinates as required or strongly recommended depending on the field and context. Use the current GBIF guidance and validate the intended publishing profile rather than treating a generic checklist as universal.

### 6.2 Taxon Concept Standard
Review whether the TaxonConcept and TaxonNameUsage model can express:
- according-to references;
- taxonomic concept relationships;
- source-specific classifications;
- concept congruence/inclusion/overlap where needed;
- concept references and stable identifiers.

Do not assume Darwin Core Taxon alone expresses all taxonomic-concept semantics.

### 6.3 Version control for mappings
Every mapping should specify:
- external standard and version/release;
- mapping version and date;
- source entity/attribute;
- target term;
- transformation and vocabulary mapping;
- null/unknown handling;
- validation severity;
- known information loss;
- responsible maintainer.

---

## 7. Review checklist by discipline

### 7.1 Taxonomist / botanical reviewer
- Are TaxonName, TaxonConcept, TaxonNameUsage and TaxonomicTreatment distinct and scientifically meaningful?
- Can the model preserve competing treatments and historical determinations?
- Are synonym relationships typed and source-scoped?
- Can it represent species complexes, infraspecific taxa and rank changes?
- Are botanical author citations, nomenclatural status and publication references handled appropriately?
- Does the model avoid claiming a taxon is accepted without naming the authority/treatment?
- Are native/introduced/endemic/invasive statements scoped to geography, time and source?

### 7.2 Field botanist / ecologist
- Are Observation, Occurrence, Event, Specimen and MaterialSample distinguished correctly?
- Can one survey event produce many occurrences?
- Can an observation remain unidentified?
- Can one record have multiple images and multiple identifications over time?
- Can the model represent non-detection only where survey protocol supports it?
- Are habitat, phenology and ecological context represented with suitable provenance?
- Are sensitive species and locality safeguards workable in field conditions?

### 7.3 Biodiversity informatics reviewer
- Are Darwin Core and TCS mappings accurate and versioned?
- Are identifiers stable, globally unique where needed and persistent?
- Are source records and transformed records traceable?
- Are controlled vocabularies and basisOfRecord values validated?
- Can exports preserve uncertainty and source attribution?
- Are duplicate detection and record reconciliation documented?
- Is the proposed model interoperable without becoming dependent on a single aggregator?

### 7.4 Database and geospatial architect
- Are entity cardinalities explicit and testable?
- Are many-to-many relations modeled explicitly where required?
- Are temporal assertions and version history queryable?
- Are geometry type, CRS, datum, precision and uncertainty explicit?
- Can exact and generalized coordinates coexist without accidental leakage?
- Are uniqueness constraints scoped to the correct source/treatment?
- Are transaction boundaries and lifecycle operations clear?
- Are expected query patterns and performance volumes documented?
- Are migrations and rollback/recovery strategies feasible?

### 7.5 Data rights, privacy and security reviewer
- Are license, rights holder, attribution and permitted purposes represented?
- Can rights differ between dataset, record, media asset and derived asset?
- Is AI training an explicit permission check?
- Can permissions be withdrawn or changed and propagated to derived assets?
- Are personal data, consent, deletion and retention requirements identified?
- Are sensitive coordinates protected in APIs, exports, logs and backups?
- Is access to restricted data audited?
- Are community and Indigenous knowledge rights and consent addressed?

### 7.6 AI/ML reviewer
- Are raw model output, ranked candidates, calibrated confidence and evidence quality separated?
- Is every identification run reproducible from model/configuration/input references?
- Are training data rights and label provenance traceable?
- Are evaluation datasets separated from training data?
- Are performance and calibration reported by region, taxonomic group, organ, image quality and relevant user segment?
- Is out-of-distribution and unknown detection tested?
- Can expert corrections be used without treating every user correction as ground truth?

---

## 8. Blocking decisions before physical database design

The following are proposed gates. Each must have a decision, rationale, owner and evidence before production DDL.

| ID | Decision | Why it blocks physical design | Required reviewer |
|---|---|---|---|
| B01 | Observation–Occurrence cardinality and ownership | Determines core keys and relationship tables | Field botanist + biodiversity informatician |
| B02 | Event, survey, plot and sampling hierarchy | Determines event model and repeat-survey queries | Ecologist |
| B03 | TaxonConcept identity and treatment versioning | Determines taxonomy keys, relationships and history | Taxonomist |
| B04 | TaxonNameUsage and source-specific acceptance | Prevents destructive global accepted-name field | Taxonomist |
| B05 | Identification subject and multiple determinations | Determines polymorphic or typed subject relationships | Taxonomist + architect |
| B06 | Evidence-to-assertion cardinality and contradiction model | Determines evidence relationship tables | Scientific reviewer |
| B07 | Source record vs normalized entity vs curated assertion | Determines ingestion, deduplication and provenance schema | Data architect |
| B08 | Rights granularity and derived-asset inheritance | Determines rights checks for media, datasets and AI | Rights reviewer |
| B09 | Exact/restricted/generalized geospatial design | Prevents irreversible disclosure and unsafe schema coupling | Geospatial + privacy reviewer |
| B10 | Historical versioning and supersession strategy | Determines audit/history tables and API behaviour | Data architect |
| B11 | Controlled vocabularies and Indian geography sources | Determines reference-data loading and identifiers | Domain + geospatial reviewer |
| B12 | External standard versions and export profiles | Determines mapping registry and validation | Biodiversity informatician |
| B13 | Retention, deletion, withdrawal and legal hold | Determines lifecycle and cascade rules | Privacy/legal reviewer |
| B14 | Identification score semantics and calibration | Prevents misleading confidence storage/display | AI/ML reviewer |
| B15 | Expected data volumes and query workload | Determines indexing, partitioning and performance design | Engineering lead |

A decision may be marked “deferred” only if the physical design can safely isolate it and the deferred scope is documented. Do not defer a question that determines core entity identity or cardinality.

---

## 9. Physical design readiness criteria

The model is ready for Task 05E only when:

1. Each blocking decision has a documented outcome or justified deferral.
2. Each core entity has a stable definition, identifier strategy and owner.
3. Every core relationship has cardinality, optionality and lifecycle semantics.
4. All required Indian test cases can be represented without loss or fabricated precision.
5. All ten workflow scenarios in Section 4 have been mapped to entities and validated.
6. Provenance and rights rules are defined for source, record, media and derived assets.
7. Sensitive location handling has a threat model and test cases.
8. Taxonomy history and source-specific treatments can be queried.
9. External standard mappings have explicit versions and lossiness notes.
10. Data quality rules have severity, remediation and audit behaviour.
11. Expected query workloads and data volumes have been estimated.
12. Independent reviewers have recorded their findings and conflicts of interest where relevant.
13. Unresolved issues have named owners and do not invalidate core relational design.
14. A change log records what changed after review.

### Readiness decision
- **Ready:** all blocking criteria met; physical design may begin.
- **Ready with conditions:** only non-core issues remain, each with owner and deadline.
- **Not ready:** core identity, cardinality, rights or sensitive-data decisions remain unresolved.

---

## 10. Suggested review workshop

A practical review can be completed in three structured sessions.

**Session 1 — Scientific meaning (90–120 minutes)**
- Taxon name and concept.
- Observation, occurrence, event and specimen.
- Identification, evidence and expert determination.
- Indian test cases.

**Session 2 — Data governance and interoperability (90 minutes)**
- Provenance and ingestion.
- Licensing and permitted purposes.
- Privacy and sensitive coordinates.
- Darwin Core and TCS mappings.

**Session 3 — Engineering and readiness (90 minutes)**
- Entity cardinalities and identifiers.
- Temporal/version history.
- Query workloads and PostGIS.
- Migration, validation and readiness decision.

Record decisions, dissent and unresolved issues. Do not treat silence or attendance as approval.

---

## 11. Reviewer decision record template

For each decision:

- Decision ID:
- Related Task/section:
- Scenario:
- Review discipline:
- Reviewer and role:
- Date:
- Outcome: Accept / Accept with condition / Revise / Defer / Reject
- Evidence and references:
- Concern or limitation:
- Required change:
- Owner:
- Due date:
- Re-review required: Yes / No

---

## 12. Governance and sign-off

This review pack does not imply that any named expert or institution has reviewed or endorsed Botanica Indica.

Required review roles:
- Botanical taxonomist.
- Field botanist or ecologist.
- Biodiversity informatics specialist.
- Database/geospatial architect.
- Data rights/privacy reviewer.
- AI/ML reviewer for identification-specific decisions.

One person may cover more than one role only where competence and independence are appropriate. High-risk taxonomic, privacy and licensing decisions should not be self-approved solely by the person who authored the proposal.

The final sign-off should state:
- which documents and exact revisions were reviewed;
- which scenarios were tested;
- decisions accepted and rejected;
- open conditions and owners;
- whether Task 05E is authorized to proceed.

---

## 13. Research references and standards

The following sources inform this review framework. Reviewers should check current versions at the time of implementation.

1. TDWG, Darwin Core — https://dwc.tdwg.org/
2. TDWG, Taxon Concept Standard — https://tcs.tdwg.org/
3. GBIF, Data quality requirements for occurrence datasets — https://www.gbif.org/dataset-classes
4. GBIF, Data quality requirements and recommendations — https://www.gbif.org/data-quality-requirements
5. GBIF, Data publishing standards — https://techdocs.gbif.org/en/data-publishing/standards-publishing
6. PostgreSQL documentation — https://www.postgresql.org/docs/
7. PostGIS documentation — https://postgis.net/documentation/
8. W3C, PROV-O: The PROV Ontology — https://www.w3.org/TR/prov-o/
9. SPDX specifications — https://spdx.dev/specifications/
10. OpenAPI Specification — https://spec.openapis.org/oas/latest.html

Standards are not substitutes for domain review. The internal model should document where it conforms, maps, extends or intentionally differs.

---

## 14. Proposed recommendation

The current architecture direction is promising and should be retained, subject to the blocking decisions and independent review described above.

Do not begin with SQL table generation. First establish scientific identity, cardinality, provenance, rights and location-sensitivity decisions. Then produce the physical ERD, PostgreSQL/PostGIS DDL, migrations, constraints, indexes and acceptance tests.

**The readiness gate is a quality control, not paperwork.** Its purpose is to prevent the project from turning unresolved scientific assumptions into expensive database constraints.

**Decision status: Draft review pack — no expert sign-off received; Task 05E is not yet authorized.**
