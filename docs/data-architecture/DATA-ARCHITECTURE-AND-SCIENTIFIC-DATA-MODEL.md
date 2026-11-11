# Task 05 — Data Architecture and Scientific Data Model

**Status:** Proposed design for review  
**Version:** 0.1  
**Date:** 2026-11-11  
**Scope:** Botanica Indica domain data architecture, with explicit integration boundaries to the Save Tiger First shared platform  
**Related ADRs:** ADR-001 through ADR-011, especially ADR-004, ADR-005, ADR-007, ADR-008, ADR-009 and ADR-010

---

## 1. Purpose

This document establishes the proposed logical data architecture and scientific data model for Botanica Indica. It is the next foundation after the product requirements, modular architecture, provenance, taxonomy, identification, evidence, geography, observations and ingestion decisions.

The purpose is not to freeze a physical database schema prematurely. It is to establish:

- The major scientific and operational entities.
- The meaning and ownership of those entities.
- Their relationships and lifecycle.
- The distinction between names, taxonomic concepts, observations, occurrences, identifications and evidence.
- The provenance and rights information that must accompany data.
- How geographic uncertainty and sensitive locations are represented.
- How the model can support reliable search, identification, expert review, research and exchange with biodiversity infrastructures.

A later implementation task should convert the accepted logical model into PostgreSQL/PostGIS schemas, constraints, indexes, migrations, API contracts and validation rules.

## 2. Design principles

1. **Scientific meaning before storage convenience:** Do not collapse different scientific concepts into one table or field merely because it is easier to implement.
2. **Taxon name is not taxon concept:** A nomenclatural name and a taxonomic circumscription are related but distinct.
3. **Observation is not identification:** An observation records an event or evidence of an organism; an identification is an assertion about what it is.
4. **Occurrence is not necessarily a user observation:** Occurrence evidence may come from field observations, preserved specimens, literature, surveys or other sources.
5. **Evidence is first-class:** Assertions must be traceable to supporting, conflicting or insufficient evidence.
6. **Provenance is attached to claims and data:** Preserve source, creator, method, time, version, transformation and rights where applicable.
7. **Uncertainty is explicit:** Taxonomic, geographic, temporal, identification and measurement uncertainty must not be silently discarded.
8. **Preserve source records:** Keep verbatim source representations when legally and technically permitted; normalization must not destroy the original meaning.
9. **Version important scientific assertions:** Corrections and changed interpretations must remain traceable.
10. **Rights are data:** Licensing and permitted-use information must be available to ingestion, display, export and AI-training controls.
11. **Sensitive data is protected independently of license:** Public availability or an open license does not remove conservation or privacy risks.
12. **Interoperability without schema capture:** Adopt standards for exchange and mapping, but do not force the entire internal domain model into a single external exchange schema.
13. **Domain ownership:** Botanica Indica owns botanical domain data; STF shared services provide reusable infrastructure, not botanical scientific authority.
14. **Incremental implementation:** Begin with a coherent modular relational model; introduce distributed storage or event infrastructure only when justified.

## 3. Scope and non-goals

### 3.1 In scope

- Taxonomic names, taxon concepts, relationships and taxonomic treatments
- Botanical taxon profiles and scientific attributes
- Observations, occurrences, events and specimens/material samples where relevant
- Identifications and identification history
- Evidence, citations, scientific assertions and expert assessments
- Geographic places, geometry, distribution and sensitive coordinate handling
- Media assets and links to observations/evidence
- Sources, datasets, source versions and ingestion runs
- Provenance, transformations and data lineage
- License and rights metadata
- Controlled vocabularies, reference data and validation
- Logical module ownership and database boundaries
- Data quality, versioning, audit and lifecycle

### 3.2 Not finalized here

- Physical SQL schema and exact column types
- Final database engine or managed hosting provider
- Exact API endpoint paths and OpenAPI document
- Search engine and vector database selection
- Object-storage vendor
- Message broker or event platform
- Final taxonomy backbone or preferred taxonomic authority
- Final list of Indian administrative/ecological boundary datasets
- Legal interpretation of every external source's terms
- Exact retention periods and operational service-level objectives

These require separate evidence and implementation decisions.

## 4. Recommended conceptual architecture

The domain model is organized into related bounded areas:

```text
                         BOTANICA INDICA
                                |
      +-------------------------+---------------------------+
      |                         |                           |
  Scientific Knowledge     Field Evidence             Governance
      |                         |                           |
  Taxon Name               Observation                 Source Registry
  Taxon Concept            Occurrence                  Dataset / Version
  Taxonomic Treatment      Event / Survey              Rights / License
  Taxon Relationship       Specimen / Sample           Ingestion Run
  Taxon Profile            Media                       Provenance
      |                         |                           |
      +-------------------------+---------------------------+
                                |
                         Interpretation
                                |
                      Identification Assertion
                      Evidence / Citation
                      Expert Assessment
                      Validation History
                                |
                          Geography
                                |
                   Location / Geometry / Distribution
                   Uncertainty / Generalization
                   Sensitive-location controls
                                |
                     Search / APIs / Analytics
```

This is a logical view. It does not require separate databases or deployable services for every area.

## 5. Core entity model

The following entities are proposed as logical concepts. Names may be refined during physical modelling, but their meanings must remain distinct.

### 5.1 Taxonomy and botanical knowledge

#### TaxonName

Represents a nomenclatural name string and its nomenclatural context.

Potential attributes:
- Stable internal identifier
- Canonical scientific name
- Authorship
- Rank or name category
- Nomenclatural code, where known
- Publication reference and publication date
- Basionym or replaced synonym relationships, where applicable
- Source and source identifier
- Verbatim source name
- Normalized name components
- Name status as reported by a source

A name record must not itself imply that a taxonomic authority accepts the name or that every source uses it for the same circumscription.

#### TaxonConcept

Represents a taxonomic circumscription or taxon as understood by a particular taxonomic treatment, source or publication.

Potential attributes:
- Stable internal identifier
- Taxonomic rank
- Concept label or referenced name
- Concept author/source
- According-to reference
- Validity interval or version context where known
- Parent concept relationship within a treatment
- Concept status in that treatment
- Source provenance
- Concept description or circumscription reference

The same name may be associated with different concepts in different treatments. The model must support that possibility without pretending the concepts are identical.

#### TaxonomicTreatment

Represents a source-specific classification or treatment.

Potential attributes:
- Treatment identifier
- Source and publication
- Taxonomic authority or dataset
- Version or publication date
- Geographic or taxonomic scope
- Method or editorial basis
- Status and provenance

#### TaxonNameUsage

Represents the use of a name by a particular source or treatment.

This is important because a name may be accepted, synonymized, misapplied, doubtful or otherwise treated differently by different sources.

Potential attributes:
- Source/treatment
- Name
- Taxon concept associated by that source
- Accepted-name usage reference
- Parent-name usage reference
- Taxonomic status as asserted by source
- Verbatim usage
- Source identifier and version
- Validity or publication context

#### TaxonRelationship

Represents an explicit relationship between concepts or name usages.

Potential relationship types include:
- Accepted name for
- Synonym of
- Basionym of
- Homotypic synonym of
- Heterotypic synonym of
- Included in
- Split from
- Lumps with
- Misapplied name for
- Overlaps with
- Congruent with
- Related concept
- Parent/child in a specified classification

Do not encode every relationship as a generic synonym boolean. Relationship type, source, treatment and evidence matter.

#### TaxonProfile

Represents Botanica Indica's curated presentation of a taxon concept or selected taxonomic view.

It may aggregate:
- Preferred display name for a stated treatment
- Common names by language and region
- Morphology
- Habit and life form
- Habitat and ecology
- Phenology
- Native/introduced/cultivated status by geography and source
- Distribution summaries
- Conservation status with authority and assessment date
- Uses or ethnobotanical notes only with appropriate evidence and safety governance
- Images and media references
- Citations and expert-reviewed content

A profile is a curated view, not a replacement for the underlying source-specific records and claims.

### 5.2 Botanical attributes and scientific assertions

Avoid storing every descriptive characteristic as an unqualified text field on TaxonProfile.

Use a claim/assertion pattern for facts that may vary by source, geography, time, taxonomic treatment or evidence.

#### ScientificAssertion

Represents a claim about a subject.

Potential attributes:
- Assertion identifier
- Subject entity or taxon concept
- Predicate / property
- Value or structured value
- Unit, where applicable
- Scope and applicability
- Geographic and temporal context
- Source and evidence links
- Asserted by (source, person, organization or system)
- Assertion date
- Confidence or certainty as reported, if meaningful
- Review/validation state
- Version and supersession relationship

Examples:
- A taxon is reported as native to a specified region.
- Flowering is reported in a particular season.
- A leaf characteristic is described by a cited flora.
- A distribution record is supported by a specimen.
- A conservation assessment assigns a category at a particular date.

Assertions from different sources must coexist where they conflict. The system should not silently overwrite one source's statement with another.

#### MeasurementOrFact

Use a structured measurement/fact representation when the information is quantitative or has a defined unit, method or measurement context.

Potential attributes:
- Subject
- Measurement type
- Value
- Unit
- Method
- Sampling context
- Measurement date
- Agent
- Source/evidence
- Uncertainty or precision

Examples include leaf length, plant height, DBH, abundance or measured environmental values. Measurement semantics should be defined; avoid mixing a numeric value and an unqualified prose note in one field.

### 5.3 Observations, occurrences and field events

#### Observation

Represents a field record submitted by a user, researcher, institution or other observer.

Potential attributes:
- Stable observation identifier
- Observer or organization
- Observation date/time or interval
- Observation method
- Narrative notes
- Habitat/context notes
- Location reference and location uncertainty
- Associated media
- Submission and publication status
- Privacy and visibility settings
- Source/provenance
- Created/modified timestamps

An observation may exist before a reliable taxonomic identification is available.

#### Occurrence

Represents evidence that an organism or taxon was present at a particular place and time, or in a collection/context.

An occurrence may be supported by:
- A human observation
- A preserved specimen
- A material sample
- A literature record
- A survey or monitoring record
- An institutional collection record
- Another traceable source

Occurrence should not be treated as synonymous with a user-generated observation.

#### Event

Represents a field event, survey, sampling activity or collection event within which one or more occurrences may be recorded.

Potential attributes:
- Event identifier
- Parent event, where hierarchical
- Date/time or interval
- Location
- Sampling protocol
- Sampling effort
- Responsible people/organization
- Survey scope
- Environmental context
- Dataset/source

This supports repeated surveys, transects, plots and monitoring rather than only isolated observations.

#### MaterialSample / Specimen

Represents a physical specimen or sample where relevant, with collection and custody context.

Potential attributes:
- Sample/specimen identifier
- Institution and collection
- Catalog number
- Collector and collection number
- Collection event
- Preparation or material type
- Repository and preservation status
- Type status, where applicable
- Related media and determinations
- Source and provenance

The initial product may not need full collection-management functionality, but the data model should not make specimen-backed evidence impossible.

#### Observation and occurrence relationship

One observation may support one or more occurrence interpretations, and one occurrence may be supported by multiple sources or evidence records. The exact cardinality must be finalized with representative use cases and standards mapping. Do not assume a one-to-one relationship in the schema.

### 5.4 Identification and determinations

#### Identification

Represents a taxonomic determination or identification assertion about an observation, occurrence, specimen or other subject.

Potential attributes:
- Identification identifier
- Subject being identified
- Identified taxon concept or candidate
- Name usage as presented at time of identification
- Identifier (person, expert, community member, model or system)
- Identification date
- Identification method
- Identification remarks
- Status and supersession history
- Supporting and conflicting evidence links
- Model/version information, if AI-assisted

An identification is an assertion, not an immutable property of an observation.

#### IdentificationRun

Represents a specific execution of an identification pipeline.

Potential attributes:
- Run identifier
- Input media and evidence
- Pipeline and model versions
- Geographic/context inputs
- Candidate list and ranks
- Raw model outputs
- Calibration/evaluation version
- Processing configuration
- Start/end time and status
- Reproducibility metadata

#### IdentificationCandidate

Represents a candidate taxon concept or name usage proposed by an identification run.

Potential attributes:
- Candidate concept/name usage
- Rank/order
- Score and score semantics
- Model output and version
- Evidence features
- Geographic compatibility signals
- Alternative candidates
- Candidate generation stage

Do not expose a raw similarity score as a calibrated probability unless calibration and interpretation have been demonstrated.

#### Confidence and evidence quality

These must remain distinct:

- **Model confidence/calibrated probability:** a property of a specific model output and evaluation regime, when appropriately calibrated.
- **Evidence quality/completeness:** how sufficient, clear, diagnostic and reliable the available evidence is.
- **Expert validation state:** the result of a human review workflow.
- **Taxonomic uncertainty:** uncertainty or disagreement about the concept/name itself.

A high model score does not guarantee good input evidence or scientific correctness.

### 5.5 Evidence, citations and expert review

#### EvidenceItem

Represents a piece of evidence that supports, challenges or contextualizes an assertion or identification.

Potential types:
- Photograph or media
- Specimen or sample
- Published literature
- Herbarium record
- Geographic occurrence
- Morphological observation
- Measurement
- Expert statement
- Dataset record
- Field note
- External database record

Potential attributes:
- Evidence identifier
- Evidence type
- Subject or claim supported
- Source/media reference
- Creator/observer
- Collection or publication date
- Reliability and limitations
- License/rights reference
- Provenance
- Validation status

#### Citation

Represents a citable source or bibliographic reference.

Potential attributes:
- Citation identifier
- DOI, ISBN, URL or other persistent identifier
- Title
- Authors/editors
- Publication or institution
- Date/year
- Page, volume, issue or section
- Access date where relevant
- Source and rights metadata

Preserve structured bibliographic data rather than storing all references as free-text strings.

#### EvidenceRelationship

Represents how an evidence item relates to an assertion, identification or taxon concept.

Relationship types may include:
- Supports
- Contradicts
- Qualifies
- Derived from
- Identifies
- Cites
- Supersedes
- Requires review

#### ExpertAssessment

Represents a human expert's assessment, separate from the original AI output or community suggestion.

Potential attributes:
- Reviewer identity and relevant expertise
- Subject and assessment target
- Assessment result
- Supporting rationale and evidence
- Conflicts or dissent
- Date and version
- Review scope
- Conflict-of-interest declaration where relevant
- Validation status

Do not erase prior assessments when a reviewer changes their opinion. Preserve review history and attribution.

### 5.6 Geography and spatial information

#### Place / GeographicUnit

Represents a named administrative, ecological or other geographic unit.

Potential types:
- Country
- State/Union Territory
- District
- Sub-district or local administrative unit
- Biogeographic region
- Ecoregion
- Protected area
- Habitat unit
- User-defined survey area

Potential attributes:
- Stable identifier
- Name and language
- Unit type
- Parent unit
- Boundary source and version
- Geometry
- Validity interval
- Source/provenance

Do not assume administrative boundaries remain unchanged over time.

#### Location

Represents a point, line, polygon or descriptive locality associated with an observation, occurrence or event.

Potential attributes:
- Original coordinates or geometry, when permitted
- Coordinate reference system / geodetic datum
- Coordinate uncertainty
- Georeferencing method
- Georeferencer and date
- Verbatim locality
- Source location
- Generalized/public representation
- Access classification
- Sensitive-location reason
- Generalization method and policy version

#### DistributionAssertion

Represents a taxon's reported distribution for a defined geography, time period, taxonomic concept and source.

It must distinguish:
- Native
- Endemic
- Introduced
- Naturalized
- Cultivated
- Invasive
- Extirpated or historical
- Uncertain or unassessed

These status categories must be scoped by geography, time, source and evidence. A single global status flag on a species profile is inadequate.

#### Sensitive location model

Maintain separate representations where needed:
- Restricted original location
- Authorized internal representation
- Generalized public representation

Access control must be enforced at the API and export boundary, not merely by hiding coordinates in the user interface. Log sensitive access and define authorized roles and purposes.

### 5.7 Media and digital assets

#### MediaAsset

Represents a stored or referenced image, audio, video or document.

Potential attributes:
- Asset identifier
- Storage object key or external URI
- Media type and format
- File size and checksum
- Dimensions/duration
- Creator and rights holder
- Capture date/time and device metadata where appropriate
- Source and provenance
- License and permission references
- AI-training permission
- Privacy and sensitive-data classification
- Processing derivatives and parent asset
- Moderation and visibility status

Store large binary objects in object storage rather than relational database rows. Keep metadata, relationships and rights in the relational domain model.

Preserve original files where rights and retention policies allow. Derivatives (thumbnails, resized images, crops, embeddings) must retain lineage to the original asset and the transformation process.

### 5.8 Sources, datasets and ingestion

#### Source

Represents an external provider or originating institution.

Potential attributes:
- Source identifier
- Organization and contact
- Source type
- Website/API endpoint and documentation
- Access method
- Terms and license references
- Geographic/taxonomic scope
- Update cadence
- Reliability and known limitations
- Last checked and last successful synchronization

#### Dataset

Represents a named collection of records distributed or curated as a unit.

Potential attributes:
- Dataset identifier
- Source and publisher
- Title and description
- Dataset type
- Version
- Publication/release date
- Citation
- License and rights status
- Geographic and taxonomic scope
- Update frequency
- Persistent identifiers

#### DatasetVersion

Represents a specific immutable or reproducibly identifiable version of a dataset.

Record source-provided version identifiers where available; otherwise use retrieval metadata and a content fingerprint where lawful and practical.

#### IngestionRun

Represents an execution of a source adapter or manual import.

Record:
- Source and dataset version
- Adapter/transformation version
- Start/end timestamps
- Status
- Input and output counts
- Rejected/quarantined counts
- Validation findings
- Error summary
- Operator or system identity
- Reprocessing relationship

#### RawSourceRecord

Preserves a source-specific record or payload before normalization where permitted. It should retain the original external identifier, source version and retrieval context.

If raw retention is prohibited, retain the minimum permitted provenance and a reproducible reference to the source.

### 5.9 Rights and licensing

#### RightsRecord

Represents the assessed legal/contractual terms applicable to an asset, dataset, source or contribution.

Potential attributes:
- Rights record identifier
- Rights holder and source
- License name, version and SPDX identifier where applicable
- License URI or permission evidence
- Attribution requirements
- Permitted purposes
- Prohibited and conditional purposes
- Redistribution permission
- Commercial-use permission
- Derivative-use permission
- AI/ML training permission
- Territory or duration limits where applicable
- Assessment status and reviewer
- Review/expiry date

Rights must be linked at the narrowest level necessary to represent exceptions. A source-wide license must not be applied to every image or record if the source itself contains mixed rights.

A record marked unknown or pending rights review must be blocked from the relevant restricted operation.

## 6. Relationship summary

The following is a conceptual relationship guide, not a final cardinality specification:

- A TaxonomicTreatment contains or references many TaxonNameUsage records.
- A TaxonNameUsage refers to a TaxonName and may be associated with a TaxonConcept.
- A TaxonConcept may be associated with multiple TaxonName records or usages across treatments.
- TaxonConcept relationships are qualified by relationship type, source and treatment.
- A TaxonProfile presents curated information about a selected concept or treatment.
- ScientificAssertions describe subjects and link to one or more EvidenceItems and Citations.
- An Observation may have multiple MediaAssets and one or more Identification records over time.
- An Occurrence may be supported by an Observation, Specimen, Event or external source record.
- An Event may contain multiple Occurrence records.
- An Identification may be revised or superseded and may have multiple EvidenceRelationships.
- An IdentificationRun may produce multiple IdentificationCandidates.
- An ExpertAssessment evaluates an identification or assertion without erasing prior history.
- A Location is associated with an Observation, Occurrence or Event and may have restricted and generalized representations.
- A Source publishes or provides Datasets; DatasetVersions and IngestionRuns preserve change history.
- Imported records link to Source, DatasetVersion, IngestionRun and RightsRecord.
- MediaAssets and derived assets retain rights and transformation lineage.

Exact cardinalities and lifecycle constraints must be validated with use cases before SQL implementation.

## 7. External standards and interoperability

Standards should be used as exchange and mapping contracts where appropriate. They should not be mistaken for a complete internal application schema.

### 7.1 Darwin Core (DwC)

Darwin Core is a TDWG-maintained vocabulary intended to facilitate sharing biodiversity information. It covers taxa, occurrences, observations, specimens, samples and related information. It is an important interoperability target for Botanica Indica. [TDWG Darwin Core](https://www.tdwg.org/standards/dwc/)

Relevant classes and terms include:
- Taxon
- Occurrence
- Organism
- MaterialSample
- Event
- Location
- Identification
- MeasurementOrFact
- ResourceRelationship

Use Darwin Core mappings for import/export of compatible biodiversity records, including stable identifiers, event dates, basis of record, taxon names and geographic information.

Do not assume Darwin Core alone captures all Botanica Indica needs for versioned taxonomic concepts, rights, expert review, detailed identification runs or privacy controls.

### 7.2 Taxon Concept Standard (TCS)

TDWG's Taxon Concept Standard provides a vocabulary for taxonomic and nomenclatural data and distinguishes Taxon Concept, Taxon Name, Taxon Concept Mapping and Nomenclatural Type. It is particularly relevant to the requirement not to collapse names and taxon concepts. [TDWG TCS](https://tcs.tdwg.org/)

Evaluate TCS terms and mappings for taxonomy ingestion and exchange. Do not adopt an XML-only assumption; the current TCS vocabulary is intended to be usable across formats including CSV, JSON and RDF.

### 7.3 GBIF and Darwin Core Archive

GBIF supports dataset classes including taxonomic checklists, occurrence datasets and sampling-event datasets. Darwin Core Archive (DwC-A) packages a core data table with mapped extensions and metadata. It is a practical import/export target for biodiversity data. [GBIF data publishing](https://techdocs.gbif.org/en/data-publishing/) [GBIF dataset classes](https://techdocs.gbif.org/en/data-publishing/dataset-classes)

GBIF occurrence data quality guidance requires occurrence identifiers, basis of record, scientific name and event date for its publishing context, with geographic fields strongly recommended. Those are useful baseline checks, not a complete validation specification for Botanica Indica. [GBIF occurrence data quality](https://www.gbif.org/es/data-quality-requirements-occurrences)

### 7.4 Interoperability strategy

Create explicit mapping profiles for:
- Taxon and taxonomic name usage
- Taxon concept and taxonomic treatment
- Occurrence and Observation
- Event and survey
- MaterialSample/specimen
- Identification
- Location and coordinate uncertainty
- Media and rights metadata
- Dataset and provenance

Maintain both source verbatim values and normalized platform values. Record mapping version and validation results for every import/export.

## 8. Data storage and logical schema boundaries

### 8.1 Relational and spatial foundation

PostgreSQL with PostGIS remains the preferred candidate for the initial structured scientific and spatial data store, consistent with the earlier architecture evaluation. This is a recommendation, not a final deployment commitment.

Reasons:
- Relational integrity for scientific entities and provenance
- Transactional updates and constraints
- Spatial geometry types and spatial indexing
- Mature ecosystem and broad interoperability
- Support for modular schemas and controlled access

The model should use logical database schemas or clearly owned module tables to preserve boundaries even if one database instance is shared initially.

### 8.2 Candidate logical schemas

Possible schema groupings:
- `taxonomy`
- `botanical_knowledge`
- `observations`
- `occurrences`
- `identification`
- `evidence`
- `geography`
- `media`
- `sources`
- `provenance`
- `rights`
- `governance`

These are conceptual groupings, not a requirement to create every schema at the first migration.

### 8.3 Binary media storage

Store binary media in object storage or a suitable media service. The database stores metadata, object references, relationships, checksums, rights and access controls.

Avoid storing large image/video binaries directly in relational rows unless a narrowly justified technical requirement exists.

### 8.4 Search and vector indexes

Search indexes and embeddings are derived representations. They must:
- Retain source entity identifiers and version references.
- Be rebuildable from authorized source records.
- Respect deletion, restriction and rights changes.
- Not become the authoritative store of scientific facts.
- Record model/embedding version and generation process.
- Enforce access and sensitive-location rules.

Do not select a dedicated vector database before benchmarks and product requirements justify one. Initial relational/full-text or extension-based capabilities may be sufficient for early workloads.

## 9. Identity, identifiers and versioning

### 9.1 Stable internal identifiers

Use stable opaque identifiers for major entities. Do not use mutable scientific names, coordinates, email addresses or external provider IDs as primary keys.

External identifiers must be retained in cross-reference tables or explicit source-identifier fields with source namespace and version context.

### 9.2 Identifier scope

An identifier must make clear which entity it identifies. For example:
- TaxonName ID
- TaxonConcept ID
- Observation ID
- Occurrence ID
- Identification ID
- MediaAsset ID
- Source/Dataset ID

Do not reuse one identifier for different concepts merely because an external source does so.

### 9.3 Versioning strategy

Distinguish:
- Entity identity
- Record revision
- Source dataset version
- Taxonomic treatment version
- Model/pipeline version
- Transformation version
- API schema version

For scientific claims and expert assessments, prefer append-only revisions or explicit supersession relationships where historical interpretation matters. Do not implement a universal event-sourcing architecture without a demonstrated need.

### 9.4 Temporal information

Where relevant, distinguish:
- Event time (when an observation or collection occurred)
- Assertion time (when a claim was made)
- Ingestion time (when the platform received it)
- Publication time (when a source released it)
- Valid time (when a claim is believed to apply)

Do not overload one `created_at` timestamp to represent all of these.

## 10. Data quality and validation

Validation should be layered:

### 10.1 Structural validation
- Required fields
- Data types and formats
- Controlled vocabularies
- Identifier uniqueness
- Referential integrity
- Valid coordinate ranges and geometry
- Valid dates and intervals

### 10.2 Scientific validation
- Taxonomic name parsing and rank consistency
- Taxon concept and treatment references
- Relationship integrity
- Measurement units and methods
- Evidence completeness
- Citation validity
- Conflicting claims retained and reviewable

### 10.3 Geographic validation
- Coordinate reference system
- Coordinate uncertainty
- Administrative and ecological boundary version
- Plausibility checks without treating distribution as absolute proof
- Sensitive-location classification and generalized output

### 10.4 Rights and policy validation
- Rights record exists
- Intended operation is permitted
- Attribution can be fulfilled
- AI training permission is explicitly resolved
- Restricted and personal data rules are applied

### 10.5 Quality status

Keep quality dimensions separate, for example:
- Completeness
- Structural validity
- Source reliability
- Scientific validation
- Geographic precision
- Rights clearance
- Identification evidence quality

Avoid one opaque global quality score unless its components, use and limitations are explicit.

## 11. Data lifecycle and governance

A typical external-data lifecycle:

```text
Source / Dataset
      |
      v
Rights and source assessment
      |
      v
Raw source capture (if permitted)
      |
      v
Structural validation
      |
      v
Normalization
      |
      v
Taxonomic / geographic reconciliation
      |
      v
Scientific and rights review as required
      |
      +------> Quarantine / rejection
      |
      v
Approved domain records
      |
      v
Search / API / export / analytics
      |
      v
Versioned updates, corrections or removal
```

A typical observation lifecycle:

```text
User / Field submission
      |
      v
Observation + media + location
      |
      v
Privacy / rights / sensitive-location checks
      |
      v
Identification candidates (optional)
      |
      v
User confirmation / additional evidence
      |
      v
Expert review (where required)
      |
      v
Versioned identification and evidence history
      |
      v
Public, generalized or restricted publication
```

No workflow stage should imply scientific validation merely because a record has been imported, published or processed by AI.

## 12. Privacy and sensitive biodiversity data

The data model must support distinct access representations and controlled disclosure.

Requirements:
- Store precise coordinates only when necessary and authorized.
- Restrict precise coordinates for sensitive species or vulnerable sites according to an approved policy.
- Preserve coordinate uncertainty and georeferencing metadata.
- Generate generalized locations through documented, versioned rules.
- Avoid exposing exact coordinates through APIs, exports, logs, analytics, image metadata or cached search indexes.
- Strip or control EXIF metadata in public media derivatives where appropriate.
- Apply purpose-limited access, audit logging and retention rules.
- Support correction, withdrawal and deletion workflows consistent with legal obligations and scientific record integrity.

The sensitive-location policy must be developed with conservation experts and relevant legal requirements; this document does not set a universal list of sensitive taxa or a universal spatial generalization distance.

## 13. AI/ML data lineage

AI/ML data must be traceable from source asset to dataset release, training run, model version and prediction.

At minimum, record:
- Original asset or record identifier
- Rights status and training permission at the time of use
- Dataset membership and version
- Annotation and reviewer provenance
- Preprocessing and augmentation transformations
- Train/validation/test split
- Model architecture and code version
- Configuration and training run
- Evaluation dataset and protocol
- Model artifact/checkpoint identifier
- Inference pipeline and output
- Known limitations and intended-use statement

Training/evaluation data must be split and governed to reduce leakage, duplicate contamination and geographic or taxonomic bias. Model performance should be evaluated across relevant Indian regions, habitats, taxa, image conditions and user groups where data permit.

A model prediction must link to its model version and input evidence. Predictions must not overwrite taxonomic facts or expert determinations.

## 14. Security and operational considerations

- Apply least-privilege database roles by module and environment.
- Separate public API access from restricted scientific and personal data.
- Encrypt data in transit and at rest according to deployment risk.
- Keep credentials and secrets outside the database records and source repository.
- Audit sensitive access and material data changes.
- Back up data and test restoration.
- Define recovery objectives before production.
- Monitor ingestion, failed validations, stale sources, data freshness and rights-review exceptions.
- Use migration scripts and reviewed schema changes.
- Maintain development/test datasets with appropriate rights and privacy controls.
- Do not copy restricted production data into development environments without authorization and safeguards.

## 15. Recommended implementation sequence

### Phase 1 — Validate conceptual model
- Review entity definitions with botanists, taxonomists, field researchers and software architects.
- Validate distinctions among TaxonName, TaxonConcept, TaxonomicTreatment and TaxonNameUsage.
- Validate Observation, Occurrence, Event and Specimen relationships.
- Select representative use cases and sample records.
- Confirm rights and sensitive-location requirements.

### Phase 2 — Logical data dictionary
- Define entity attributes and definitions.
- Define controlled vocabularies and code lists.
- Define relationship types and cardinalities.
- Define required/optional/conditional fields.
- Define lifecycle states and invariants.
- Map candidate Darwin Core and TCS terms.

### Phase 3 — Physical model
- Define PostgreSQL schemas and table boundaries.
- Define PostGIS geometry strategy and coordinate reference systems.
- Define keys, constraints, indexes and uniqueness rules.
- Define history/versioning and audit approach.
- Define migration and seed-data strategy.

### Phase 4 — Data contracts
- Define import/export mapping profiles.
- Draft OpenAPI schemas for core read/write workflows.
- Define event schemas only where asynchronous integration is justified.
- Validate sample Darwin Core Archive import/export.

### Phase 5 — Prototype and validation
- Load a small, rights-cleared, representative dataset.
- Test taxonomic reconciliation and provenance.
- Test observation and identification history.
- Test sensitive coordinate access and public generalization.
- Benchmark core search and spatial queries.
- Revise the model based on actual use.

## 16. Open questions requiring domain review

1. Which Indian botanical taxonomic sources and treatments should be prioritized for the initial reference corpus?
2. What is the canonical policy for representing multiple competing taxonomic concepts in public species pages?
3. Which botanical attributes should be structured fields versus sourced scientific assertions?
4. What observation workflows are required for casual users, field researchers and institutional surveys?
5. Which specimen/herbarium workflows are in the initial product scope?
6. Which distribution/status vocabularies and authorities should be represented?
7. Which Indian administrative and biogeographic boundary datasets are suitable, current and licensed for use?
8. What location-generalization policy should apply to sensitive taxa and user observations?
9. Which sources permit storage, redistribution, derivative creation and AI training?
10. What data retention and withdrawal rules apply to user-contributed observations and media?
11. What expert-review states and dispute-resolution rules are needed?
12. Which standards and export profiles must be supported in the first implementation?

These questions should be resolved with domain experts and evidence, not by choosing arbitrary defaults in SQL.

## 17. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Treating a name as a taxon concept | Separate TaxonName, TaxonConcept and TaxonomicTreatment |
| Treating observation as identification | Keep Observation and Identification independent |
| Losing original source semantics | Preserve verbatim data and transformation lineage where permitted |
| Over-normalizing uncertain scientific data | Retain source-specific assertions and conflicts |
| Exposing sensitive locations | Separate restricted and generalized representations; enforce API-level policy |
| Ingesting data without rights | Rights registry and operation-specific ingestion gates |
| Model training on unauthorized images | Explicit training permission and dataset lineage |
| Excessive schema complexity | Phase implementation; validate representative workflows before adding tables |
| Overfitting internal schema to Darwin Core | Use explicit mapping profiles and preserve a richer domain model |
| Search/vector index becoming source of truth | Treat indexes as rebuildable derived data |
| Taxonomy changes destroying history | Version treatments and preserve superseded assertions |

## 18. Acceptance criteria for Task 05

The data architecture task should be considered ready for physical implementation when:

- The conceptual entities and definitions are reviewed by relevant botanical/scientific stakeholders.
- Taxon names, taxon concepts and taxonomic treatments are distinct.
- Observations, occurrences, events and identifications are distinct.
- Evidence and citations can support, contradict and qualify assertions.
- Source, dataset, version, ingestion run and transformation provenance are represented.
- Rights and permitted purposes can be enforced at asset/dataset level.
- Sensitive locations can be stored and disclosed at different access levels.
- Darwin Core and TCS mappings are documented for applicable entities.
- Required cardinalities, invariants and lifecycle states are specified.
- A representative dataset can be imported, reconciled, queried and exported without loss of critical provenance.
- Physical schema, migrations and API contracts can be derived without unresolved foundational ambiguity.

## 19. References and standards

Official and primary references consulted:

1. TDWG, Darwin Core standard: https://www.tdwg.org/standards/dwc/
2. TDWG, Darwin Core List of Terms (version issued 2026-10-13): https://dwc.tdwg.org/list/
3. TDWG, Taxon Concept Standard: https://tcs.tdwg.org/
4. GBIF, Data publishing technical documentation: https://techdocs.gbif.org/en/data-publishing/
5. GBIF, Dataset classes: https://techdocs.gbif.org/en/data-publishing/dataset-classes
6. GBIF, Occurrence data quality requirements: https://www.gbif.org/data-quality-requirements-occurrences
7. GBIF, Data processing: https://techdocs.gbif.org/en/data-processing/
8. GBIF, Occurrence download formats: https://techdocs.gbif.org/en/data-use/download-formats

Standards and documentation should be rechecked when implementation begins because terms, mappings, validation guidance and external APIs can evolve.

---

## 20. Final recommendation

Adopt a **rich internal scientific model with standards-based exchange mappings**.

Darwin Core should be a major interoperability layer for biodiversity occurrences, taxa, events and related records. TCS should inform the treatment of taxon concepts and nomenclatural data. Neither should be treated as a complete substitute for Botanica Indica's own versioned scientific assertions, evidence, expert review, provenance, rights and sensitive-location controls.

The most important architectural choice is to keep **TaxonName, TaxonConcept, Observation, Occurrence, Identification, Evidence and ScientificAssertion** as distinct concepts. This is the foundation for scientific integrity, future integrations and defensible AI-assisted identification.
