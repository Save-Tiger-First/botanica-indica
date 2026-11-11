# Task 05B — Scientific Data Dictionary and Representative Indian Botanical Records

- **Status:** Proposed for scientific and architecture review
- **Version:** 0.1
- **Date:** 2026-11-11
- **Scope:** Botanica Indica domain model
- **Related documents:** `docs/data-architecture/DATA-ARCHITECTURE-AND-SCIENTIFIC-DATA-MODEL.md`; ADR-004; ADR-005; ADR-007; ADR-008; ADR-009; ADR-010
- **Purpose:** Translate the Task 05 conceptual model into a reviewable data dictionary, relationship rules and source-grounded test cases before physical SQL design.

---

## 1. How to read this document

This document is a proposed logical data dictionary, not a physical database schema. It defines recommended meanings, fields, data types at a conceptual level, cardinalities, constraints and example records. Exact SQL types, table names, key strategies and indexes belong to the later physical-model task.

The examples below are **source-grounded test fixtures**, not claims that Botanica Indica has independently verified the records, owns the content, or has permission to bulk ingest it. Facts are attributed to the specific public source that reports them. Where sources differ, both statements are preserved.

### 1.1 Evidence labels

Use these labels in review and future implementation:

- **Source fact:** explicitly reported by the named source.
- **Platform assertion:** a statement created or adopted by Botanica Indica.
- **Illustrative value:** a suggested value used to explain a field, not an assertion about a real specimen or observation.
- **Open decision:** requires domain expert, legal, policy or implementation approval.

Never present an illustrative value as an actual field observation, verified distribution, herbarium accession or expert determination.

## 2. Critical refinement from standards review

The first Task 05 draft correctly separates names and concepts, but the detailed implementation should align more carefully with the current TDWG Taxon Concept Standard (TCS) semantics.

TCS defines a Taxon Concept as an identifiable taxonomic position combining a taxon name with an `accordingTo` source. It requires both properties. TCS also models a synonym as a relationship from a Taxon Concept to a Taxon Name; combinations and nomenclatural relationships belong with Taxon Name information. Therefore, do not implement every synonym category as an unqualified relationship between two taxon concepts. Retain the source's actual assertion and map it to TCS carefully.

Reference: https://tcs.tdwg.org/terms/

The current Darwin Core vocabulary also includes classes and terms relevant to Observation, Machine Observation, Identification, Event, Occurrence, Location, Material Entity, Provenance and Usage Policy. Map these deliberately rather than assuming older simplified Darwin Core field lists are complete.

Reference: https://dwc.tdwg.org/list/ (version issued 2026-10-13)

## 3. Core identifier and data-type conventions

These are proposed conventions for logical modelling:

| Conceptual type | Meaning | Example |
|---|---|---|
| `ID` | Stable opaque internal identifier | `taxon-name:...` |
| `ExternalID` | Identifier within a named external namespace | IPNI LSID |
| `String` | Unicode text | `Azadirachta indica` |
| `Text` | Long-form prose | Field notes |
| `Code` | Controlled vocabulary value | `HUMAN_OBSERVATION` |
| `URI` | Web URI or persistent identifier | `https://...` |
| `Date` | Calendar date | `1830-01-01` only if source provides exact date |
| `DateTime` | Timestamp with timezone | ISO 8601 |
| `DateInterval` | Start/end or verbatim uncertain interval | `2025-06` |
| `Decimal` | Numeric value with defined precision | Coordinate |
| `Integer` | Whole-number quantity | Number of images |
| `Boolean` | True/false only when known | Rights-cleared |
| `JSON` | Structured source payload or extension | Verbatim API response |
| `Geometry` | Point/line/polygon with CRS | PostGIS geometry |
| `LanguageTag` | BCP 47 language tag where possible | `kn`, `hi`, `en` |
| `Checksum` | Cryptographic content digest with algorithm | SHA-256 |

All timestamps should be stored with timezone context. A source date that is only a year or month must not be fabricated into an exact day; preserve its precision or verbatim representation.

## 4. Entity data dictionary

Field requirement labels:
- **R** — required for a valid record of this entity.
- **C** — conditionally required when the relevant context applies.
- **O** — optional.
- **Derived** — generated from other fields and should not be treated as the sole authoritative value.

### 4.1 TaxonName

**Definition:** A nomenclatural or other name string used to refer to a taxon. It is not, by itself, proof of acceptance or a complete taxon concept.

| Field | Type | Req. | Definition / rule |
|---|---|---:|---|
| taxon_name_id | ID | R | Stable Botanica Indica identifier |
| name_string | String | R | Name string without authorship where the source's model distinguishes it |
| authorship | String | O | Name authorship, kept separate from name string |
| rank | Code | O | Rank as represented by source; use controlled mapping |
| nomenclatural_code | Code | O | Applicable nomenclatural code if known |
| publication_reference_id | ID | O | Link to publication/protologue |
| publication_date_verbatim | String | O | Source's original date text |
| publication_date | Date/DateInterval | O | Normalized date with precision retained |
| basionym_name_id | ID | O | Link to a basionym where applicable |
| replaced_name_id | ID | O | Link to replaced name where applicable |
| source_id | ID | C | Required for source-originated name record |
| source_record_id | ID | C | Original source record identifier |
| verbatim_name | String | O | Exact source string |
| created_at / updated_at | DateTime | R | Platform record timestamps |

**Invariants**
- A TaxonName may exist without a TaxonConcept.
- A name may occur in several source treatments.
- Do not make `is_accepted` a global field on TaxonName.
- Do not strip authorship from the preserved verbatim source value.

### 4.2 TaxonomicTreatment

**Definition:** A source-specific classification, checklist, flora, revision or taxonomic treatment.

| Field | Type | Req. | Definition / rule |
|---|---|---:|---|
| treatment_id | ID | R | Stable internal identifier |
| source_id | ID | R | Publisher/authority/source |
| dataset_version_id | ID | C | Version of dataset if distributed as a dataset |
| bibliographic_resource_id | ID | C | Publication or treatment reference |
| title | String | R | Treatment title |
| treatment_type | Code | R | Checklist, flora, revision, database release, etc. |
| publication_date | Date/DateInterval | O | Preserve precision |
| taxonomic_scope | Text/JSON | O | Taxa or ranks covered |
| geographic_scope_id | ID | O | Geographic coverage |
| source_identifier | ExternalID | O | Identifier in originating system |
| rights_record_id | ID | C | Required where rights assessment is applicable |
| retrieved_at | DateTime | O | When retrieved by STF |

### 4.3 TaxonConcept

**Definition:** A taxonomic position according to a specific source or treatment. Follow TCS: a concept combines a name with an `accordingTo` reference.

| Field | Type | Req. | Definition / rule |
|---|---|---:|---|
| taxon_concept_id | ID | R | Stable internal identifier |
| taxon_name_id | ID | R | Name used as the concept label |
| according_to_treatment_id | ID | R | Treatment defining the concept |
| concept_according_to_reference | ID/URI | R | Citable source/authority for the concept |
| rank | Code | O | Rank in this treatment |
| parent_concept_id | ID | O | Parent in this specific classification |
| concept_status | Code | O | Status within the treatment; not global |
| circumscription_reference | URI/Text | O | Evidence or description of included material |
| source_concept_identifier | ExternalID | O | External concept ID |
| valid_from / valid_to | DateInterval | O | Temporal validity if known |
| created_at | DateTime | R | Platform timestamp |

**Invariants**
- Do not create a fully specified TCS concept without a taxon name and an according-to source.
- A concept ID identifies the concept in its according-to context; it is not interchangeable with the name ID.
- Parent-child relations must be scoped to the same treatment or explicitly mapped across treatments.

### 4.4 TaxonNameUsage

**Definition:** A source's use of a name in a particular context, including its status and source-specific interpretation.

| Field | Type | Req. | Definition / rule |
|---|---|---:|---|
| name_usage_id | ID | R | Stable internal identifier |
| treatment_id | ID | R | Treatment containing the usage |
| taxon_name_id | ID | R | Name used |
| taxon_concept_id | ID | O | Associated concept, if resolvable |
| accepted_name_usage_id | ID | O | Source's accepted usage, if asserted |
| parent_name_usage_id | ID | O | Parent usage in this treatment |
| taxonomic_status | Code | O | Source's exact status mapped to controlled vocabulary |
| verbatim_status | String | O | Original source wording |
| source_record_id | String | O | Original source identifier |
| source_page_or_locator | String | O | Page, row, URL fragment or record locator |
| evidence_reference_id | ID | O | Source evidence |
| retrieved_at | DateTime | O | Retrieval timestamp |

Do not convert absent status into accepted, or unresolved into synonym. Unknown is a valid state.

### 4.5 TaxonConceptMapping

**Definition:** A source-supported mapping or comparison between two taxon concepts from potentially different treatments.

| Field | Type | Req. | Definition / rule |
|---|---|---:|---|
| concept_mapping_id | ID | R | Stable mapping identifier |
| subject_concept_id | ID | R | First concept |
| object_concept_id | ID | R | Second concept |
| mapping_relation | Code | R | E.g. congruent, includes, included in, overlaps, excludes, not congruent; use a governed vocabulary |
| according_to_reference_id | ID | R | Source for mapping |
| mapping_agent_id | ID | O | Person/organization/system |
| mapping_date | DateTime | O | When asserted |
| mapping_confidence | Decimal/Code | O | Only with defined semantics |
| review_status | Code | R | Proposed, reviewed, accepted, rejected, superseded |
| evidence_set_id | ID | O | Supporting evidence |

A mapping is not a synonym relationship. A synonym in TCS links a concept to a name; a concept mapping compares taxonomic concepts.

### 4.6 ScientificAssertion

**Definition:** A sourced claim about a subject, property and value, with context and provenance.

| Field | Type | Req. | Definition / rule |
|---|---|---:|---|
| assertion_id | ID | R | Stable identifier |
| subject_type | Code | R | TaxonConcept, Occurrence, Observation, etc. |
| subject_id | ID | R | Subject identifier |
| predicate | Code/URI | R | Controlled property or URI |
| value_type | Code | R | Text, number, boolean, concept, geometry, etc. |
| value | Structured value | R | Typed value, not unqualified string only |
| unit | Code/URI | C | Required for measured quantities |
| geographic_scope_id | ID | O | Geographic applicability |
| temporal_scope | DateInterval | O | Time applicability |
| source_id | ID | C | Required for externally sourced claim |
| evidence_set_id | ID | O | Evidence supporting or qualifying claim |
| asserted_by | ID | R | Person, organization, source or software agent |
| asserted_at | DateTime | R | Assertion time |
| certainty | Code | O | Only with documented semantics |
| review_status | Code | R | Workflow status |
| supersedes_assertion_id | ID | O | Prior assertion superseded |
| provenance_record_id | ID | R | Provenance link |

Different sources may assert different values. Preserve both and record reconciliation separately.

### 4.7 Observation

**Definition:** A record that an observer recorded an organism or plant-related evidence at a time and place. It can exist without identification.

| Field | Type | Req. | Definition / rule |
|---|---|---:|---|
| observation_id | ID | R | Stable identifier |
| observer_agent_id | ID | R | User, organization or anonymous/withheld agent reference |
| observed_at | DateInterval | C | Observation time; precision may be coarse |
| recorded_at | DateTime | R | Platform submission time |
| observation_method | Code | O | Casual, protocol-based, camera, etc. |
| field_notes | Text | O | Observer's notes |
| habitat_verbatim | String | O | Observer's original habitat note |
| place_id | ID | O | Named place, where known |
| location_id | ID | O | Georeferenced location |
| privacy_state | Code | R | Private, community, public, restricted |
| publication_state | Code | R | Draft, submitted, moderated, published, withdrawn |
| rights_record_id | ID | C | Contributor terms/permission |
| source_id | ID | O | If imported from another platform |
| created_at / updated_at | DateTime | R | Platform timestamps |

### 4.8 Occurrence

**Definition:** A record of the presence or non-detection of an organism or taxon in a defined context. It may be derived from an observation, specimen, event, literature or source dataset.

| Field | Type | Req. | Definition / rule |
|---|---|---:|---|
| occurrence_id | ID | R | Stable identifier |
| basis_of_record | Code | R | Map to Darwin Core controlled values |
| occurrence_status | Code | O | Present/absent or applicable controlled term |
| organism_id | ID | O | Biological individual/group if modelled |
| observation_id | ID | O | Supporting observation if applicable |
| event_id | ID | O | Related event |
| material_entity_id | ID | O | Specimen/material evidence |
| taxon_concept_id | ID | O | Current determination target, if known |
| location_id | ID | O | Location representation |
| event_date | DateInterval | O | Time of occurrence |
| source_record_id | String | O | External identifier |
| source_id | ID | C | Required for imported occurrence |
| provenance_record_id | ID | R | Origin/lineage |

Occurrence must not be treated as merely a field on Observation. Multiple evidence records can support one occurrence interpretation, and an observation may be revised or interpreted in multiple ways.

### 4.9 Event

**Definition:** A field event, collection event, survey or sampling activity during a time interval at a location.

| Field | Type | Req. | Definition / rule |
|---|---|---:|---|
| event_id | ID | R | Stable identifier |
| event_type | Code | R | Survey, collection, observation event, etc. |
| parent_event_id | ID | O | Hierarchical event |
| event_start / event_end | DateTime/DateInterval | O | Event interval |
| location_id | ID | O | Event location |
| sampling_protocol | URI/Text | O | Protocol |
| sampling_effort | Structured value | O | Effort and unit |
| responsible_agent_id | ID | O | Organization/person |
| source_id | ID | O | Imported event source |
| event_notes | Text | O | Notes |

### 4.10 MaterialEntity / Specimen / MaterialSample

Use a common material-entity abstraction where useful, with subtype or category-specific attributes. Do not assume every plant observation has a preserved specimen.

| Field | Type | Req. | Definition / rule |
|---|---|---:|---|
| material_entity_id | ID | R | Stable identifier |
| material_entity_category | Code | R | Preserved specimen, living specimen, sample, etc. |
| institution_id | ID | O | Holding institution |
| collection_id | ID | O | Collection |
| catalog_number | String | O | Institution catalog number |
| collector_agent_id | ID | O | Collector |
| collection_event_id | ID | O | Collection event |
| type_status | Code | O | Nomenclatural type status where applicable |
| preparation | String | O | Preparation/preservation |
| repository_uri | URI | O | Repository record |
| rights_record_id | ID | O | Rights/access restrictions |
| provenance_record_id | ID | R | Source and custody lineage |

### 4.11 Identification

**Definition:** A taxonomic determination about an Observation, Occurrence, MaterialEntity or other subject. It is a revisable assertion.

| Field | Type | Req. | Definition / rule |
|---|---|---:|---|
| identification_id | ID | R | Stable identifier |
| subject_type | Code | R | Observation, Occurrence, MaterialEntity |
| subject_id | ID | R | Subject being identified |
| taxon_concept_id | ID | O | Proposed/selected concept |
| taxon_name_id | ID | O | Name used if concept not resolved |
| identifier_agent_id | ID | R | Human, expert, community or AI system |
| identification_method | Code | R | Human, AI-assisted, automated, literature, etc. |
| identified_at | DateTime | R | Assertion time |
| identification_qualifier | Code/String | O | cf., aff., genus-only, etc., where applicable |
| identification_remarks | Text | O | Rationale |
| identification_status | Code | R | Proposed, supported, disputed, confirmed, rejected, superseded |
| previous_identification_id | ID | O | Previous determination |
| evidence_set_id | ID | O | Evidence set |
| model_run_id | ID | O | AI run, if applicable |
| according_to_treatment_id | ID | O | Taxonomic context |

Do not overwrite the old identification when a new identification is added. Use a history/supersession relationship.

### 4.12 IdentificationRun and Candidate

**IdentificationRun** records a single execution of an AI or automated pipeline.

Required logical fields:
- run ID
- input observation/media identifiers
- pipeline and model versions
- taxonomic backbone/release
- context inputs used (location/date/organ)
- configuration and preprocessing version
- start/end time and status
- evaluation/calibration reference
- rights eligibility snapshot or dataset policy reference

**IdentificationCandidate** records one candidate produced by that run:
- candidate ID
- run ID
- rank/order
- taxon concept or unresolved external taxon reference
- raw score and score type
- calibrated probability only if genuinely calibrated
- evidence signals/features
- geographic compatibility result
- taxonomy mapping result
- candidate explanation reference

A score must never be labelled a probability unless the calibration method and applicable evaluation regime justify that interpretation.

### 4.13 EvidenceItem and EvidenceRelationship

**EvidenceItem** represents a photograph, specimen, publication, field note, measurement, expert statement or external record.

Core fields:
- evidence item ID
- evidence type
- creator/observer/source
- created or collected date (with precision)
- media/citation/material/source reference
- rights record
- provenance record
- quality/limitations
- visibility/access state

**EvidenceRelationship** connects evidence to an assertion or identification:
- relationship ID
- evidence item ID
- target assertion/identification ID
- relation: supports, contradicts, qualifies, derived-from, cites
- rationale
- asserted by
- asserted at

Do not store one universal evidence score on EvidenceItem. Evidence quality depends on the claim being evaluated.

### 4.14 ExpertAssessment

Core fields:
- assessment ID
- target type and ID
- reviewer agent ID
- reviewer expertise/credential reference
- review scope
- outcome
- rationale
- evidence set
- conflicts/dissent
- conflict-of-interest declaration where required
- reviewed at
- supersedes assessment ID

An expert's qualification should be validated through a governed domain workflow; a shared platform login or generic role does not prove botanical expertise.

### 4.15 Place, GeographicUnit and Location

**Place/GeographicUnit** represents named administrative or ecological areas with source/version context.

Core fields:
- place ID
- place type
- preferred name and language
- alternative names
- parent place ID
- boundary geometry
- geometry CRS
- source and boundary version
- valid-from/to
- provenance

**Location** represents a particular locality or geometry associated with an event, observation or occurrence.

Core fields:
- location ID
- verbatim locality
- original geometry/coordinates where permitted
- CRS/geodetic datum
- coordinate uncertainty in metres
- georeferencing method/source/agent/date
- restricted/public access classification
- generalized geometry
- generalization method and policy version
- sensitive-location reason
- source/provenance

Never overwrite original coordinates with generalized coordinates. Keep access control at service/API/export level, not only in UI.

### 4.16 DistributionAssertion

Core fields:
- distribution assertion ID
- taxon concept ID
- geographic unit ID
- status code
- source/treatment
- temporal applicability
- evidence
- asserted by/at
- review state
- provenance

Status vocabulary should distinguish native, endemic, introduced, naturalized, cultivated, invasive, extirpated/historical, uncertain and not assessed. These labels are not interchangeable, and a status must be scoped to a geography, time and source.

### 4.17 MediaAsset

Core fields:
- media asset ID
- media type and MIME type
- object storage key or external URI
- file checksum and algorithm
- dimensions/duration/file size
- creator and rights holder
- capture date/time and precision
- source and uploader
- rights record
- privacy/sensitive classification
- derivative/parent asset
- transformation lineage
- moderation/visibility status
- EXIF handling state

A photograph's visibility online does not prove redistribution or AI-training rights.

### 4.18 Source, Dataset, DatasetVersion and IngestionRun

**Source** fields:
- source ID, name, publisher/organization, source type
- official URL/API/documentation
- access method and update cadence
- source contact
- terms/rights references
- geographic/taxonomic scope
- last checked, last successful access
- known limitations

**Dataset** fields:
- dataset ID, source ID, title, description
- publisher, citation, persistent identifier
- dataset class and scope
- rights record and attribution
- update cadence

**DatasetVersion** fields:
- dataset version ID, dataset ID
- source version label
- publication/release date
- retrieved date
- checksum/fingerprint where permitted
- archive URI or source reference
- rights status snapshot

**IngestionRun** fields:
- ingestion run ID
- source and dataset version
- adapter and mapping version
- start/end and status
- input/accepted/rejected/quarantined counts
- validation results
- operator/system
- error report reference
- reprocessing lineage

**RawSourceRecord** fields:
- raw record ID
- source and source record identifier
- dataset version and ingestion run
- verbatim payload or lawful reference
- content checksum
- retrieval time
- rights and retention status

If raw payload retention is not permitted, do not store it. Retain only permitted metadata and source references.

### 4.19 RightsRecord

Core fields:
- rights record ID
- rights holder/source
- license name and version
- SPDX identifier where applicable
- license URI or permission evidence
- attribution requirements
- redistribution/derivative/commercial-use permissions
- AI/ML training permission (explicit yes/no/conditional/unknown)
- permitted purpose and prohibited purpose
- territorial/duration conditions
- assessment status and reviewer
- review/expiry date
- evidence document reference

Unknown or pending rights status must block the relevant operation until reviewed. A general license for one dataset must not automatically cover third-party photographs embedded in it.

### 4.20 ProvenanceRecord

Core fields:
- provenance record ID
- origin type (source, user, expert, AI, platform, transformation)
- source/agent/software identifiers
- source version
- generated/retrieved time
- derivation links
- transformation name/version/configuration
- input and output identifiers
- rights snapshot
- validation/review status
- lineage reference

Provenance should be attached to scientific assertions and important derived outputs, not merely stored as one free-text note on the top-level species record.

## 5. Relationship and cardinality rules

The following is the recommended baseline. Cardinalities may be refined but must not contradict the scientific meaning.

| Relationship | Cardinality | Notes |
|---|---|---|
| TaxonomicTreatment → TaxonNameUsage | 1 to many | Each usage belongs to one treatment |
| TaxonNameUsage → TaxonName | many to 1 | Same name can be used in multiple treatments |
| TaxonConcept → TaxonName | many to 1 or 1 to 1 per concept | Concept has one defining name in TCS |
| TaxonConcept → Treatment | many to 1 | A concept is defined according to a treatment |
| TaxonConcept → TaxonConceptMapping | many to many via mapping | Mapping is explicit and source-qualified |
| Observation → MediaAsset | many to many | An asset may be reused only when rights allow |
| Observation → Identification | 1 to many | Multiple determinations over time |
| IdentificationRun → Candidate | 1 to many | One run returns ranked alternatives |
| Observation/Occurrence/MaterialEntity → Identification | 1 to many | Subject must be explicit |
| Occurrence → EvidenceItem | many to many | Multiple supporting evidence items |
| Event → Occurrence | 1 to many | Events may record many occurrences |
| Event → Location | many to 1 or 1 to many via event-location | Define for complex surveys |
| ScientificAssertion → EvidenceItem | many to many | Evidence can support or challenge multiple claims |
| Source → Dataset | 1 to many | A source can publish multiple datasets |
| Dataset → DatasetVersion | 1 to many | Versions are immutable snapshots where feasible |
| DatasetVersion → IngestionRun | 1 to many | Repeated imports/reprocessing |
| IngestionRun → RawSourceRecord | 1 to many | If retention is permitted |
| Record → RightsRecord | many to many where exceptions apply | Resolve effective rights before use |
| Location → Public/generalized representation | 1 to 0..many | Multiple policies/purposes may produce views |

## 6. Controlled vocabularies requiring governance

Do not hard-code user-facing labels as the data values. Store stable codes and localized labels.

Initial vocabulary families:
- Taxonomic rank
- Taxonomic name usage status
- Taxon concept mapping relation
- Identification method
- Identification status
- Evidence type and evidence relationship
- Observation method and publication/privacy status
- Basis of record
- Event type/category
- Occurrence status
- Establishment means and degree of establishment
- Distribution status
- Habitat and growth form
- Life form and plant habit
- Plant organ/structure
- Phenological stage
- Measurement type and unit
- Coordinate reference system
- Sensitive-location classification
- Rights assessment status and permitted purpose
- Expert assessment outcome

Each vocabulary should include:
- code
- preferred label
- definition
- language
- source/authority
- version
- broader/narrower/related mappings where applicable
- deprecated/replaced-by metadata
- effective dates

## 7. Source-grounded Indian botanical test cases

These examples are deliberately small and illustrate different modelling problems. They are not a proposed taxonomic backbone and must not be bulk-ingested solely from these pages.

### 7.1 Case A — Neem: nomenclatural identity vs taxonomic acceptance

**Source facts**
- IPNI records the name `Azadirachta indica A.Juss.`, with LSID `urn:lsid:ipni.org:names:1213180-2`, and publication details in *Mémoires du Museum d'Histoire Naturelle* 19:221 (1830). IPNI also links the nomenclatural name `Melia azadirachta L.`.
- POWO presents `Azadirachta indica A.Juss.` as an accepted species and reports a native range from Assam to Indo-China.

Sources:
- https://www.ipni.org/n/1213180-2
- https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:1213180-2/general-information

**Modelling**
- Create a TaxonName for the scientific name using IPNI's name identifier.
- Create a separate TaxonomicTreatment for the POWO taxonomic backbone/version context.
- Create a TaxonConcept according to that treatment.
- Record the link to `Melia azadirachta L.` according to the source's nomenclatural relationship semantics; do not infer the complete relationship graph from a short page excerpt.
- Preserve the original publication date text and any normalized date separately; the source presentation of 1830 vs publication issuance nuance must not be silently rewritten.

**Do not infer**
- A specific wild occurrence in a particular Indian district.
- That every Neem tree is wild/native at its observation location.
- Rights to copy the IPNI or POWO dataset at scale.

### 7.2 Case B — Mango: source disagreement in native/introduced distribution

**Source facts**
- POWO presents `Mangifera indica L.` as accepted and reports a native range of Assam to southern Yunnan; its displayed distribution lists India among introduced areas.
- eFlora of India presents `Mangifera indica L.`, lists Indian-language common names including Kannada `ಮಾವು`, and describes it as native to southern Asia and India.

Sources:
- https://powo.science.kew.org/taxon/69913-1
- https://efloraofindia.com/efi/mangifera-indica/

**Modelling**
- Store the scientific name and source-specific treatment records separately.
- Store POWO's geographic assertion with its source and treatment context.
- Store eFlora of India's geographic assertion separately with its source and context.
- Do not force a single global `native = true` field on the taxon.
- Model Kannada common name as a vernacular-name assertion with language tag `kn`, source and provenance. Verify spelling and regional usage with a qualified language/botanical reviewer before treating it as a canonical common name.
- Keep the difference visible for scientific review; do not decide which source is correct based only on these pages.

**Why this case matters**
This is a practical test of the ADR-004 provenance and ADR-005 source-aware reconciliation decisions. It demonstrates why geographic status belongs in scoped assertions rather than a universal species attribute.

### 7.3 Case C — Banyan: a name treated as a synonym

**Source facts**
- POWO presents `Ficus benghalensis L.` as accepted, reports the native range as the Indian Subcontinent, and lists `Ficus indica L.` among its heterotypic synonyms.
- POWO's page for `Ficus indica L.` says the name is a synonym of `Ficus benghalensis` and names the taxonomic sources it follows for that treatment.

Sources:
- https://powo.science.kew.org/taxon/852482-1
- https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:853013-1

**Modelling**
- Create distinct TaxonName records for `Ficus benghalensis L.` and `Ficus indica L.`.
- Create the POWO treatment and its source-specific concept.
- Record the synonym relation as a concept-to-name usage in a way consistent with TCS, rather than assuming it is simply a relationship between two biological entities.
- Retain the source and cited taxonomic treatment supporting the synonym assertion.
- Do not globally delete or merge the `Ficus indica` name record.

**Why this case matters**
It tests synonymy, accepted-name presentation, historical search and preservation of source name identity.

### 7.4 Case D — Herbarium specimen record: specimen is not an observation photo

**Source facts**
The Botanical Survey of India's Indian Virtual Herbarium describes specimen records that can include family, genus, species, author citation, infraspecific information, collector, collection number, collection date, herbarium region, locality, plant description, habitat and comments.

Source:
- https://ivh.bsi.gov.in/
- https://bsi.gov.in/page/en/Virtual-Herbarium

**Modelling**
- Represent the specimen as a MaterialEntity/PreservedSpecimen.
- Represent collector, collection event, collection date and locality distinctly.
- Represent the specimen's determinations as one or more Identification records.
- Link digitized specimen images as MediaAssets with their own rights and access conditions.
- Do not represent a herbarium specimen as a casual citizen Observation without retaining its specimen and collection context.

**Important limitation**
This source description establishes the types of specimen label information available in the system; it does not provide a specific accession record in this example. Do not invent an accession number, collector, date or locality.

### 7.5 Case E — Flora publication as structured scientific source

**Source facts**
The Botanical Survey of India describes a flora as a systematic enumeration for a geographic area and says floras may include scientific/common names, literature references, taxonomic descriptions, habit, habitat, distribution, flowering/fruiting times, uses, notes and illustrations. BSI describes national, state, district and special-habitat flora work.

Source:
- https://www.bsi.gov.in/page/en/flora

**Modelling**
- Treat a flora publication as a bibliographic resource and/or TaxonomicTreatment, depending on the content.
- Extract individual taxon usages, assertions and citations with page-level locators.
- Scope distribution and phenology assertions to the geographic area and taxonomic treatment.
- Do not flatten the flora into one list of names without retaining page, publication, treatment and evidence references.

## 8. Sample record representation (illustrative JSON)

The following is a logical example for a source-scoped Mango distribution assertion. The IDs are illustrative and the object is not a real imported record.

```json
{
  "assertion_id": "assertion-example-001",
  "subject": {
    "type": "TaxonConcept",
    "id": "taxon-concept-mangifera-powo-example"
  },
  "predicate": "distribution.nativeRange",
  "value": {
    "geographicText": "Assam to southern Yunnan",
    "status": "native"
  },
  "according_to": {
    "source": "Plants of the World Online",
    "uri": "https://powo.science.kew.org/taxon/69913-1"
  },
  "asserted_at": "2026-11-11",
  "review_status": "source-reported-not-independently-validated",
  "provenance": {
    "origin_type": "external-source",
    "source_record_identifier": "69913-1"
  }
}
```

A production representation should use controlled geography identifiers and structured relations rather than relying on a free-text range string.

## 9. Validation and integrity rules

Before a record is eligible for public display, export or downstream processing, apply the relevant validations:

### 9.1 Taxonomy
- A fully specified TaxonConcept has a name and according-to treatment/reference.
- TaxonName identity is not duplicated solely because a source uses different formatting.
- Name usages preserve treatment-specific status.
- A synonym assertion links the relevant concept and name usage with source context.
- A taxon concept mapping has both subject and object concepts plus a mapping relation and reference.
- Name-string equality alone does not establish concept equivalence.

### 9.2 Observation and occurrence
- An Observation can be submitted without an identification.
- An Identification must identify its subject and method/agent.
- An Occurrence must have a basis-of-record and provenance.
- A specimen record retains collection and institution context.
- Event time and record submission time are distinct.

### 9.3 Evidence and assertions
- An external scientific assertion has source/provenance.
- Evidence relationships specify whether evidence supports, contradicts or qualifies a claim.
- Expert review retains reviewer, time, scope and outcome.
- AI output is distinguishable from user and expert determinations.

### 9.4 Geography
- Coordinates include CRS/datum and uncertainty where known.
- Original and generalized locations are distinct.
- A distribution assertion is scoped by taxon concept, geography, source and time.
- Unknown geographic precision remains unknown, not zero.

### 9.5 Rights
- An asset or dataset used in an operation has an effective rights decision.
- AI-training permission is explicit; unknown does not mean yes.
- Attribution requirements are machine-readable where possible.
- Third-party media embedded in a source dataset can have different rights from the dataset itself.

## 10. Recommended initial controlled values

These are proposed starting codes, not final vocabulary standards.

### Identification method
- `HUMAN_FIELD`
- `HUMAN_EXPERT`
- `COMMUNITY_SUGGESTION`
- `AI_ASSISTED`
- `AI_AUTOMATED`
- `LITERATURE_DETERMINATION`
- `INSTITUTIONAL_DETERMINATION`

### Identification status
- `PROPOSED`
- `SUPPORTED`
- `DISPUTED`
- `CONFIRMED`
- `REJECTED`
- `SUPERSEDED`
- `UNRESOLVED`

### Rights assessment
- `CLEARED`
- `CLEARED_WITH_CONDITIONS`
- `PERMISSION_REQUIRED`
- `PROHIBITED`
- `UNKNOWN`
- `EXPIRED_REVIEW_REQUIRED`

### Review state
- `UNREVIEWED`
- `IN_REVIEW`
- `REVIEWED`
- `ACCEPTED`
- `REJECTED`
- `NEEDS_MORE_EVIDENCE`
- `SUPERSEDED`

Controlled vocabularies must be versioned and have definitions. These labels should not be treated as interchangeable with Darwin Core or TCS terms without explicit mappings.

## 11. Open scientific and policy decisions

1. Which taxonomic authority or combination of authorities should Botanica Indica use for each purpose (name nomenclature, accepted checklist, species concepts, Indian distribution)?
2. Should the platform expose one default treatment for casual users while preserving alternate treatments for researchers?
3. Which flora publications and Indian institutional datasets can be licensed for ingestion, redistribution and derivative extraction?
4. How should source disagreements about native/introduced status be reviewed and presented?
5. Which vernacular names require region/dialect/script variants and community attribution?
6. Which herbarium specimen metadata can be retained and republished, and under what terms?
7. What is the domain review workflow for expert credentials and taxonomic disputes?
8. What sensitive-location policy applies to rare, threatened, endemic or commercially targeted taxa?
9. Which occurrence/observation export profile is required for GBIF/Darwin Core compatibility?
10. Which TCS mappings can be represented natively in JSON and which require richer graph relationships?

## 12. Recommended review exercise before SQL design

Use the following test scenarios to review the model with botanists, taxonomists, herbarium staff and data engineers:

1. Same scientific name, different taxonomic treatments.
2. One name treated as synonym by one source and accepted by another.
3. A common cultivated plant with disagreement about native/introduced status.
4. An observation with three photographs and no identification.
5. An AI identification with three candidates and no expert confirmation.
6. A herbarium specimen with collector, collection number, date, locality and multiple determinations.
7. A district flora assertion with a page-level citation.
8. A rare plant observation whose precise coordinates must not be public.
9. A source dataset containing records and images with different rights.
10. A taxonomic correction that must preserve the old identification and prior public page history.

The model should pass these scenarios without overwriting source facts, losing uncertainty or conflating evidence with conclusions.

## 13. Acceptance criteria

The data dictionary is ready to inform physical schema design when:
- Domain experts approve or amend entity definitions and relationships.
- TCS and Darwin Core mappings are documented at term level.
- The Mango source disagreement example is represented without forced global consensus.
- The Ficus synonym example is modelled without deleting the name record.
- The Neem nomenclatural example preserves publication and identifier provenance.
- Herbarium specimen and casual observation records remain distinct.
- Controlled vocabularies have owners and versioning.
- Rights and sensitive-location constraints are demonstrably enforceable.
- All sample data clearly distinguishes source facts from illustrative values.
- The ten review scenarios can be represented and validated.

## 14. References consulted

1. TDWG Darwin Core List of Terms, version issued 2026-10-13: https://dwc.tdwg.org/list/
2. TDWG Taxon Concept Standard terms: https://tcs.tdwg.org/terms/
3. IPNI — Azadirachta indica A.Juss.: https://www.ipni.org/n/1213180-2
4. Kew Plants of the World Online — Azadirachta indica: https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:1213180-2/general-information
5. Kew Plants of the World Online — Mangifera indica: https://powo.science.kew.org/taxon/69913-1
6. eFlora of India — Mangifera indica: https://efloraofindia.com/efi/mangifera-indica/
7. Kew Plants of the World Online — Ficus benghalensis: https://powo.science.kew.org/taxon/852482-1
8. Kew Plants of the World Online — Ficus indica: https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:853013-1
9. Botanical Survey of India — Virtual Herbarium: https://bsi.gov.in/page/en/Virtual-Herbarium
10. Indian Virtual Herbarium: https://ivh.bsi.gov.in/
11. Botanical Survey of India — Flora programme: https://www.bsi.gov.in/page/en/flora

---

## 15. Recommendation

Proceed to a reviewed logical schema only after the scientific test cases are approved. The most important correction is to implement TCS semantics precisely: a taxon concept is according to a source, a taxon name is a separate reusable nomenclatural object, and synonymy is not simply an equivalence edge between two taxon concepts.

Use the Mango distribution disagreement as a mandatory test fixture. It demonstrates that Botanica Indica must preserve source-scoped geographic assertions rather than compressing complex botanical knowledge into a single global field.
