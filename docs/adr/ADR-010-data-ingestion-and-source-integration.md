# ADR-010: Data Ingestion and Source Integration

**Status:** Accepted  
**Date:** 2026-09-23

## Context

Botanica Indica will depend on information from many botanical, biodiversity, taxonomic, geographic, scientific, and institutional sources.

Potential sources may include:

- Taxonomic databases
- Botanical nomenclatural resources
- Floras
- Herbarium collections
- Biodiversity observation platforms
- Species distribution datasets
- Scientific publications
- Institutional databases
- Government datasets
- Community-contributed datasets
- External APIs
- Open data repositories
- Licensed commercial data sources

These sources differ in:

- Data structure
- Taxonomic treatment
- Identifiers
- Naming conventions
- Geographic standards
- Update frequency
- Versioning
- Licensing
- Attribution requirements
- Data quality
- Completeness
- Availability
- API capabilities
- Reliability

The platform must therefore avoid treating external sources as if they were a single unified database.

Data ingestion must preserve source identity and provenance while allowing the platform to build a coherent botanical knowledge system.

## Decision

Botanica Indica will implement a **source-aware, provenance-preserving, modular data ingestion architecture**.

External sources will be integrated through explicit ingestion or integration boundaries.

The platform will distinguish between:

- Source data
- Imported data
- Normalized data
- Reconciled data
- Derived data
- Platform-original data

No external source will automatically become the authoritative representation of the platform's entire botanical knowledge.

## 1. Source Registry

The platform should maintain a registry of external data sources.

A source record may contain:

- Source name
- Source identifier
- Organization
- Source type
- Website or API endpoint
- Documentation reference
- Data format
- License
- Attribution requirements
- Version information
- Update frequency
- Geographic scope
- Taxonomic scope
- Integration method
- Access requirements
- Reliability or availability information
- Date of last successful synchronization

The source registry provides a consistent way to understand where platform data originated.

## 2. Source Adapters

External systems should be integrated through source-specific adapters or connectors.

Conceptually:

```text
Botanica Indica
       │
       ├── Source Adapter A
       │       ↓
       │   External Source A
       │
       ├── Source Adapter B
       │       ↓
       │   External Source B
       │
       └── Source Adapter C
               ↓
           External Source C

Source-specific implementation details should remain isolated from the platform's core domain model.

Changing an external API should therefore require changes primarily within the relevant adapter rather than throughout the platform.

3. API and File-Based Sources

The ingestion architecture must support multiple source delivery mechanisms.

Examples include:

REST APIs
GraphQL APIs
Bulk downloads
CSV files
JSON files
Darwin Core datasets
Parquet files
GeoJSON
Scientific databases
Institutional exports
Manually curated datasets

The platform should not assume that every important source provides a modern API.

4. Raw Source Preservation

Where licensing and storage permissions allow, the platform should preserve an appropriate representation of the original source data before transformation.

Conceptually:

External Source
      ↓
Raw Source Representation
      ↓
Normalization
      ↓
Reconciliation
      ↓
Platform Data

Raw source preservation supports:

Reproducibility
Debugging
Reprocessing
Auditing
Historical comparison
Transformation verification

Where raw storage is not permitted, the platform should retain sufficient source references and metadata to reproduce or verify the ingestion process where possible.

5. Source Identifiers

External identifiers must be preserved.

Examples include:

Taxon identifiers
Observation identifiers
Specimen identifiers
Publication identifiers
Dataset identifiers
Geographic identifiers
Media identifiers

External identifiers must not be replaced by platform identifiers.

The platform should maintain its own stable identifiers while retaining relationships to external identifiers.

6. Normalization

Source data may be normalized into platform-compatible structures.

Normalization may include:

Field mapping
Data type conversion
Character normalization
Date normalization
Geographic normalization
Identifier normalization
Media reference normalization
Name normalization

Normalization must not silently alter scientific meaning.

The transformation should be documented and reproducible where appropriate.

7. Taxonomic Reconciliation

Taxonomic information from external sources must pass through the taxonomy architecture defined in ADR-005: Taxonomy Reconciliation.

Ingestion must therefore distinguish between:

Source Taxonomy
      ↓
Normalized Taxonomic Information
      ↓
Taxonomic Reconciliation
      ↓
Platform Taxonomic Representation

An imported name must not automatically become the platform's accepted taxon.

Conflicting taxonomic treatments must remain distinguishable.

8. Geographic Reconciliation

Geographic information from external sources may use different:

Coordinate systems
Administrative boundaries
Place names
Spatial resolutions
Georeferencing methods
Uncertainty models

Ingested geographic information must retain its source and uncertainty.

Geospatial handling follows ADR-008: Geospatial and Sensitive Location Data.

9. Provenance

Every imported or derived record should retain appropriate provenance.

Where applicable, provenance should include:

Source
External identifier
Dataset
Dataset version
Import run
Retrieval date
Transformation
Reconciliation process
License
Attribution requirements

The provenance architecture follows ADR-004: Data and Scientific Provenance.

10. Licensing and Usage Rights

Data may only be ingested, stored, transformed, redistributed, or displayed according to the applicable rights.

The platform must distinguish between:

Data that can be freely redistributed
Data that can be used with attribution
Data that permits derivatives under specified conditions
Data that is non-commercial
Data that can be queried but not redistributed
Data requiring permission
Data that cannot be imported

A source being publicly accessible does not automatically mean that its data can be copied or redistributed.

Licensing information must therefore be treated as part of source metadata and provenance.

11. Attribution

Where attribution is required, the platform should preserve the information necessary to provide it.

Attribution may apply to:

Dataset
Organization
Individual contributor
Publication
Software
Taxonomic authority
Image contributor

Attribution requirements should not be separated from the imported data in a way that makes compliance difficult.

12. Source Updates

External sources may change over time.

The ingestion system should support:

Initial import
Incremental synchronization
Full refresh
Versioned imports
Corrections
Retractions
Source deletions
Schema changes

A newer source version must not automatically destroy historical provenance.

The platform should be able to determine which source version contributed to a particular record where practical.

13. Ingestion Runs

Each ingestion operation should have an identifiable run.

An ingestion run may record:

Source
Source version
Start time
Completion time
Status
Records discovered
Records imported
Records changed
Records rejected
Records requiring review
Validation errors
Transformation version
Software version

This supports reproducibility and operational troubleshooting.

14. Validation During Ingestion

Imported data should pass appropriate validation before entering production domain structures.

Validation may include:

Required-field validation
Schema validation
Identifier validation
Date validation
Geographic validation
Taxonomic validation
Duplicate detection
License validation
Referential integrity
Data-quality checks

Validation failures should be recorded rather than silently discarded.

15. Quarantine and Rejection

Records that cannot safely be imported should be isolated from validated production data.

Conceptually:

Source Data
    ↓
Validation
    ├── Valid → Normalization → Platform
    │
    └── Invalid → Quarantine / Review

Quarantined records may require:

Correction
Manual review
Source clarification
Transformation updates
Reprocessing

Rejected records should retain enough information to understand why they were rejected where permitted.

16. Idempotency and Duplicate Prevention

Ingestion operations should be designed to be repeatable without creating uncontrolled duplicates.

The system should use appropriate combinations of:

Source identifiers
Dataset identifiers
Version information
Stable platform identifiers
Content fingerprints
Transformation metadata

Re-running an ingestion process should produce predictable results.

Idempotency must not rely solely on matching scientific names because names may change or be shared across taxonomic contexts.

17. Derived Data

Ingestion may produce derived data.

Examples include:

Normalized names
Geographic representations
Taxonomic mappings
Aggregated distributions
Search indexes
Statistical summaries
Candidate relationships

Derived data must remain distinguishable from original source data.

The system should retain sufficient lineage to understand how derived information was produced.

18. Source Conflicts

Different sources may disagree.

Conflicts may involve:

Scientific names
Taxonomic status
Synonyms
Distribution
Geographic coordinates
Dates
Species descriptions
Identification
Conservation information

The ingestion system must preserve source-specific information rather than silently selecting one source as universally correct.

Resolution of scientific conflicts belongs to the appropriate domain architecture.

For taxonomy, this follows ADR-005.

For identification and evidence, this follows ADR-006 and ADR-007.

19. Source Reliability and Availability

External sources may become:

Temporarily unavailable
Permanently unavailable
Rate limited
Reconfigured
Deprecated
Changed without notice

The platform must avoid making its core scientific data permanently dependent on live availability of an external provider.

Where legally and technically appropriate, the platform should maintain cached or imported representations.

External providers should not become mandatory runtime dependencies for basic platform operation unless explicitly required by a particular feature.

20. External API Rate Limits

Source integrations must respect applicable:

Rate limits
Terms of service
Authentication requirements
Usage restrictions
Attribution requirements

Ingestion processes should support:

Backoff
Retry
Scheduling
Incremental synchronization
Caching
Failure recovery

The platform must not attempt to bypass source restrictions.

21. Source Schema Evolution

External source schemas may change.

Adapters should therefore:

Validate expected schemas
Detect incompatible changes
Record integration failures
Avoid silently misinterpreting changed fields
Support adapter versioning where necessary

A source schema change should not silently produce scientifically incorrect platform data.

22. Manual and Curated Sources

Not all scientific information will originate from automated ingestion.

The architecture must support controlled manual or curated imports.

Examples include:

Expert-curated datasets
Institutional spreadsheets
Historical herbarium records
Research datasets
Digitized publications
Manually reconciled taxonomic records

Manual ingestion should follow the same provenance, licensing, validation, and source-tracking principles as automated ingestion.

23. Source Removal

If an external source requests removal of its data, or the platform determines that continued use is not permitted, the ingestion architecture must support controlled removal.

Removal should consider:

Licensing obligations
Derived data
Search indexes
Cached representations
Public pages
Attribution
Historical records
Downstream datasets

The platform should preserve a record of the removal event where appropriate without retaining data that must legally be deleted.

24. Data Refresh and Reprocessing

The architecture should allow previously ingested data to be reprocessed when:

A transformation is corrected
A source publishes a new version
Taxonomy reconciliation improves
Geographic processing improves
Data quality rules change

Reprocessing should not require obtaining the source data again when a legally retained raw representation is available.

25. Operational Monitoring

The ingestion system should provide operational visibility into:

Source availability
Import failures
Schema changes
Record counts
Validation failures
Processing duration
Rate limiting
Synchronization status
Data freshness

Operational monitoring should distinguish technical failures from scientific data-quality problems.

26. Security

Source credentials and authentication information must be managed separately from imported scientific data.

The system should support:

Secure credential storage
Credential rotation
Least-privilege access
Access logging
Secret isolation
Secure transmission

Credentials must never be stored in source records, committed to source control, or exposed through public APIs.

27. API and Platform Integration

Ingestion is a platform capability rather than a client-side responsibility.

Mobile and web applications should consume reconciled platform data through APIs rather than independently importing and reconciling external sources.

This preserves:

Consistency
Provenance
Licensing controls
Taxonomic reconciliation
Geographic protections
Scientific governance
28. Architectural Consequences

This decision provides:

Source independence
Reproducible ingestion
Strong provenance
Licensing awareness
Taxonomic consistency
Geographic consistency
Better resilience to external-source changes
Support for automated and manual datasets
Controlled data quality
Reprocessing capability

It also introduces additional complexity in:

Source adapters
Ingestion pipelines
Data validation
Licensing management
Schema evolution
Synchronization
Source conflict handling
Operational monitoring
Storage requirements

This complexity is intentional because the botanical intelligence ecosystem will depend on multiple scientific and institutional sources and must remain trustworthy even when those sources differ or change.

Related ADRs
ADR-001: Architecture Principles & Technology Independence
ADR-002: Modular Architecture
ADR-003: API-First Platform Architecture
ADR-004: Data and Scientific Provenance
ADR-005: Taxonomy Reconciliation
ADR-006: Identification Architecture
ADR-007: Evidence and Expert Validation
ADR-008: Geospatial and Sensitive Location Data
ADR-009: Observation and Contribution Model
