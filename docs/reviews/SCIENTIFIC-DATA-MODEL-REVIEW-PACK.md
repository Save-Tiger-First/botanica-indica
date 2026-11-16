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


## 4.3 Preliminary cross-document desk-review findings (16 November 2026)

**Review type:** Repository/documentation desk review by the project assistant, using the exact GitHub revisions listed below and current public standards documentation. This is not independent expert validation and must not be recorded as a taxonomist, ecologist, biodiversity-informatics or legal sign-off.

### Exact revisions inspected

| PR | Document | PR head commit | Review note |
|---|---|---|---|
| #3 | Task 05 — Data Architecture | `3804c125192f1638e5dfff2bf013b76a9ee5286b` | Draft, based on main |
| #4 | Task 05B — Data Dictionary | `f35e2d761017447edbb96cd874cb5b528072dc71` | Draft, based on main |
| #5 | Task 05C — Logical Database Model | `78565f88bd3c78650944586146693e7b6103eab4` | Draft, based on main |
| #7 | Task 05D — Validation and Readiness | `6155a87dcc92a2bd315fc6f8203a5f31012940b0` | Draft, based on PR #5 feature branch; dependent review |

The content was fetched from the named feature branches. PR #7 must be reviewed as a dependent change set on top of PR #5, not as an independent document based on `main`.

### Findings register

| ID | Severity | Documents | Finding and required resolution |
|---|---|---|---|
| DR-01 | **Blocking** | 05B, 05C, 05D | **Internal occurrence validity is still coupled to export fields.** Task 05B marks `basis_of_record` required; Task 05C's Occurrence row and integrity tests require it. Task 05D correctly says GBIF publication requirements are profile-specific and must not become universal internal constraints, but the earlier documents have not yet been reconciled. Define an internal record/evidence classification independently; derive Darwin Core `basisOfRecord` only where supported. Do not invent missing values. |
| DR-02 | **Blocking** | 05B, 05C | **Polymorphic subject references conflict with the integrity principle.** Task 05B uses `subject_type + subject_id` for ScientificAssertion and Identification. Task 05C requires typed subject links or an enforceable supertype. Reconcile the dictionary to the typed logical model, or formally define and constrain a supertype/registry. A generic pair without enforceable referential integrity is not acceptable as the canonical design. |
| DR-03 | **Blocking** | 05B, 05C | **TCS mapping vocabulary needs exact semantic mapping.** Task 05B lists values such as “excludes” and “not congruent”. TCS requires one of `isCongruentWith`, `includes`, `isIncludedIn`, `partiallyOverlaps`, `isDisjointFrom` or `intersects`. “Not congruent” is not equivalent to “disjoint”; “intersects” is a broad relation for cases where a more precise relation is not known. Define a governed internal vocabulary and explicit mappings to the six TCS terms. |
| DR-04 | **Blocking** | 05B, 05C | **The TCS `accordingTo` resource needs one unambiguous representation.** Task 05B requires both `according_to_treatment_id` and `concept_according_to_reference`. TCS requires exactly one `accordingTo` resource per TaxonConcept. These fields may be two representations of the same resource, but the document does not define that invariant. Specify whether TaxonomicTreatment is itself the referenced resource or whether it resolves to one canonical bibliographic/resource record. Do not permit two conflicting “according to” sources. |
| DR-05 | **Major** | 05, 05B, 05C | **Three different taxonomy relationship families must remain separate.** Task 05 includes a broad TaxonRelationship spanning concepts/name usages and relationship labels such as synonym, basionym and accepted-name-for. Task 05B/05C make the more precise distinction: concept-to-name synonym assertion, name-to-name nomenclatural relationship, and concept-to-concept mapping. Update the conceptual Task 05 description and terminology so that it cannot be implemented as one undifferentiated relationship table. |
| DR-06 | **Major** | 05B, 05C | **Taxonomic determination should not become a mutable occurrence fact.** Task 05B includes an optional `taxon_concept_id` on Occurrence described as the current determination target. Task 05C models Identification as a separate, revisable assertion. Define whether the occurrence's displayed taxon is a derived view from the current accepted Identification, and how the historical determination and treatment are retained. Avoid storing a mutable duplicate that can disagree with identification history. |
| DR-07 | **Major** | 05B, 05C, 05D | **Occurrence and Event semantics need one consistent internal-to-Darwin-Core mapping.** The current Darwin Core conceptual model defines an Occurrence as an Event establishing the state of an Organism at a place and time; Organism, Occurrence and MaterialEntity are distinct. Task 05C largely follows this direction, but Task 05B describes occurrence more loosely as presence/non-detection and allows event/date to be optional. Define an internal evidence/observation state separately from an exportable Darwin Core Occurrence, and document when an organism identity is meaningful or unavailable. Non-detection must be supported by a survey protocol and effort, not inferred from an empty record. |
| DR-08 | **Major** | 05B | **The Mango example is an apparent geographic-scale tension, not yet a demonstrated direct source contradiction.** POWO reports a native range including Assam and East Himalaya while its broad distribution list places “India” under introduced; eFlora of India says “native to: s Asia and India”. These geographic units are not equivalent. Preserve the example, but label it as a scale/resolution and source-scope reconciliation case until the claims are normalized to comparable geographic units and reviewed. Do not teach it as a proven contradiction. |
| DR-09 | **Major** | 05, 05B, 05C | **Darwin Core release metadata is inconsistent.** Task 05 and Task 05B refer to the List of Terms as issued 2026-10-13; the current official List page identifies the list version as 2026-05-26. Individual terms can have later modification dates (including 2026-10-13). Cite the list release and individual term version separately, and record the exact version IRI used by each mapping profile. |
| DR-10 | **Major** | 05B, 05C | **Source record identifiers need stronger canonical linkage.** Task 05B has string `source_record_id` fields on Occurrence and TaxonNameUsage. Task 05C defines SourceRecord with dataset version, ingestion run and namespace context. Use a canonical source-record reference or a formally constrained external-identifier tuple; a bare string is insufficient to guarantee uniqueness or trace lineage. |
| DR-11 | **Major** | 05B | **The synonym mapping wording should explicitly name the TCS object type.** TCS `synonym` relates a TaxonConcept to a TaxonName, not to a TaxonNameUsage object and not to another TaxonConcept. Preserve TaxonNameUsage separately as the source's usage/record, then link the TCS synonym assertion to the reusable TaxonName. |
| DR-12 | **Major** | 05B, 05D | **Source authority and evidence class should be recorded for the Indian examples.** IPNI, POWO, BSI and eFlora of India have different roles and authority models. eFlora of India includes community-submitted content and should not be described as equivalent in authority to a formal national flora or a nomenclatural index. Record source type, editorial/curation model, geographic scope, date and limitations; do not use a website's presence alone as a source-quality rating. |

### Evidence supporting the standards-related findings

1. **TCS 2025-12-11 List of Terms:** a TaxonConcept requires one `taxonName` and one `accordingTo`; `synonym` relates a TaxonConcept to a TaxonName; TaxonConceptMapping requires subject, relation and object; and the permitted mapping relations are explicitly enumerated.  
   https://tcs.tdwg.org/terms/  
   Version IRI: https://rs.tdwg.org/tcs/doc/terms/2025-12-11

2. **Darwin Core List of Terms:** the official page identifies the current list version as 2026-05-26. Individual terms carry their own modification/version dates.  
   https://dwc.tdwg.org/list/  
   Version IRI: https://rs.tdwg.org/dwc/doc/list/2026-05-26

3. **Darwin Core conceptual model:** the modern Occurrence semantics distinguish Organism, Occurrence and MaterialEntity; an Occurrence is an Event establishing the state of an Organism at a place and time.  
   https://dwc.tdwg.org/cm/

4. **GBIF data publishing recommendations:** requirements vary by dataset class and programme. For occurrence datasets, occurrenceID is required in the technical publishing guidance, while basisOfRecord, scientificName and eventDate are strongly recommended for the general profile and required for some managed programmes. Sampling-event datasets have a different profile.  
   https://techdocs.gbif.org/en/data-publishing/data-quality-recommendations  
   https://www.gbif.org/data-quality-requirements-occurrences  
   https://www.gbif.org/data-quality-requirements-sampling-events

5. **Source comparison for the Mango fixture:** POWO lists Assam and East Himalaya among native regions and India among introduced regions; eFlora of India describes the species as native to South Asia and India. This supports a test of geographic granularity and source interpretation, but not an unqualified claim that both sources make directly contradictory claims about the same geographic unit.  
   https://powo.science.kew.org/taxon/69913-1  
   https://efloraofindia.com/efi/mangifera-indica/

### Recommended disposition

- Resolve DR-01 through DR-04 before Task 05C is considered logically stable.
- Resolve DR-05 through DR-07 before physical design; they affect scientific identity, history and interoperability.
- Correct DR-08 through DR-12 in the documentation and source/fixture metadata before sign-off.
- Update Task 05D's cross-document audit table with a status, owner and evidence for each item. A list of review topics is not the same as a completed reconciliation.
- Do not mark any finding closed solely because a branch is mergeable or a document has been revised. Require a re-review against the exact new commit.

**Desk-review conclusion:** the current model is directionally strong but not yet internally reconciled. No independent expert sign-off has been received. Task 05E remains blocked.

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
3. GBIF, Data quality recommendations (including occurrence and sampling-event profiles) — https://techdocs.gbif.org/en/data-publishing/data-quality-recommendations
4. GBIF, Data quality requirements for occurrence datasets — https://www.gbif.org/data-quality-requirements-occurrences
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


## 4.4 Reconciliation pass — DR-01 to DR-04 and related occurrence semantics (16 November 2026)

Following the preliminary desk review, proposed documentation changes were made on the source branches. The exact current branch heads at the time of this update are:

| Document | PR | Branch head commit |
|---|---:|---|
| Task 05 conceptual data architecture | #3 | `bb85442cfb8e4625a242fb85442d8df5cb89118a` |
| Task 05B scientific data dictionary | #4 | `fc04dc04114be4af0097d8a778706ea50e23e62c` |
| Task 05C logical database model | #5 | `c517c00676c3a8803507443be63d46b3d28445b0` |
| Task 05D validation/readiness gate | #7 | `ca637022fd249b107200b7581aa76980956d2888` |

These changes are proposed documentation revisions. PRs remain draft and unmerged. At the latest verification on 16 November 2026, GitHub reported PRs #3, #4, #8 and #9 as `mergeable: false`, and PRs #5 and #7 as `mergeable: true`. The reason for the false states was not established and must not be inferred. Recheck PR conflict state and exact diffs before review or merge.

### Reconciliation results

| Finding | Proposed correction now present | What remains open |
|---|---|---|
| DR-01 — Internal occurrence vs export fields | Task 05B no longer requires Darwin Core `basisOfRecord` as a universal internal Occurrence field. Task 05C removes it from the core Occurrence key rule and integrity test, retaining provenance. Task 05D records the distinction. | Confirm all internal occurrence fixtures, export profiles and non-detection handling. Do not close until exact diffs and tests are reviewed. |
| DR-02 — Polymorphic subject references | Task 05B now specifies typed FK subject links for ScientificAssertion and Identification. Task 05C states the required typed-link integrity rule. | The logical model still needs a complete subject-link inventory and a physical strategy to enforce exactly one Identification subject. A prose rule alone does not create referential integrity. |
| DR-03 — TCS mapping vocabulary | Task 05B and Task 05C now identify the six exact TCS mapping relations: `isCongruentWith`, `includes`, `isIncludedIn`, `partiallyOverlaps`, `isDisjointFrom`, and `intersects`. | Taxonomist review is still needed for relation direction, interpretation and example fixtures. |
| DR-04 — TCS accordingTo resource | Task 05B and Task 05C specify one canonical according-to resource; a structured TaxonomicTreatment record is optional and must resolve to that same resource. | Confirm resource registry identity and implement uniqueness/FK constraints. |
| DR-06 — Taxon determination on Occurrence | Task 05B now treats the current taxonomic determination as a derived view from the applicable Identification rather than a mutable Occurrence taxon field. | Confirm that Task 05C read models/API views and all test cases follow the same rule. |
| DR-07 — Occurrence and non-detection | Task 05B now defines Occurrence as an evidence-backed presence/state record and states that non-detection needs a defined survey/event, protocol and effort. | A separate logical SurveyResult/absence-result entity and fixtures still need explicit design; do not encode absence as a missing occurrence. |
| DR-10 — Source record identifiers | Task 05B Occurrence now points to a canonical SourceRecord FK or a constrained external-identifier tuple. | Other entities, including TaxonNameUsage, must be checked for bare source-record strings and aligned. |

### Research verification used for this pass

The current official TCS List of Terms identifies its version as 2025-12-11. It states that a TaxonConcept requires `taxonName` and `accordingTo`; a TaxonConceptMapping requires subject, relation and object; and lists the six mapping relations used above. It also clarifies that TCS synonymy uses a TaxonConcept-to-TaxonName relation, while basionym/replaced-name relationships belong to the TaxonName vocabulary. https://tcs.tdwg.org/terms/

GBIF's current data-quality recommendations distinguish occurrence datasets from sampling-event datasets. For occurrence datasets, `occurrenceID` is required; `basisOfRecord`, `scientificName` and `eventDate` are strongly recommended in the general profile and required in GBIF-managed programmes. Sampling-event datasets have a separate set of requirements, including event and sampling-protocol fields. This supports keeping export-profile validation distinct from internal data validity. https://techdocs.gbif.org/en/data-publishing/data-quality-recommendations

### Updated disposition

- DR-01 to DR-04 are **revised in the proposed documents; not yet closed**.
- DR-06, DR-07 and DR-10 are **partially addressed; further model and fixture review required**.
- DR-05 and DR-08 to DR-12 remain subject to their previously stated dispositions.
- Physical design and Task 05E remain **not authorized**.
- No external scientific expert has signed off on these changes.

A reviewer must compare the exact branch diffs, validate the six TCS relation semantics with taxonomic examples, test typed subject integrity, and verify all occurrence/export profiles before changing any finding to “closed”.
