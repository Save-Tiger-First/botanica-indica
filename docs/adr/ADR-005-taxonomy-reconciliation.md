# ADR-005: Taxonomy Reconciliation

- **Status:** Accepted
- **Date:** 2026-09-22
- **Decision Type:** Scientific Data Architecture
- **Scope:** Botanica Indica taxonomy and taxonomic data ecosystem

## Context

Botanical taxonomy is not represented by a single universally immutable classification.

Different authoritative sources may differ in:

- Accepted names
- Synonyms
- Taxonomic rank
- Species concepts
- Genus placement
- Family placement
- Authorship
- Nomenclatural interpretation
- Taxonomic history
- Source version
- Geographic treatment

Botanica Indica is expected to use information from multiple botanical and biodiversity sources.

Examples may include:

- World Flora Online
- Plants of the World Online
- International Plant Names Index
- India Flora Online
- eFlora of India
- India Biodiversity Portal
- GBIF
- iNaturalist
- Other institutional or scientific sources

These sources should not be treated as interchangeable databases containing identical taxonomic knowledge.

Simply selecting one source and overwriting information from other sources would result in loss of scientific context and make it difficult to represent disagreements or historical changes.

The platform therefore requires a deliberate approach to taxonomic reconciliation.

## Decision

Botanica Indica will implement a **source-aware, versioned taxonomic reconciliation system**.

The system will distinguish between:

1. Taxonomic entities
2. Taxonomic names
3. Taxonomic relationships
4. Source-specific taxonomic treatments
5. Reconciled platform relationships
6. Taxonomic versions
7. Evidence supporting reconciliation decisions

The platform will not silently overwrite source-specific taxonomic information merely to create a single simplified classification.

## Taxonomic Entity

A taxonomic entity represents the conceptual taxon tracked by the platform.

A taxonomic entity should be distinguishable from any single scientific name.

For example:

```text
Taxonomic Entity
      │
      ├── Accepted Name
      ├── Synonym
      ├── Historical Name
      ├── Source-specific Name
      └── Alternative Treatment

This separation is important because the same biological concept may be represented by different names across sources or through time.

The exact data model will be defined separately.

Scientific Names

Scientific names should be represented independently from their use within a particular taxonomic treatment.

Relevant information may include:

Scientific name
Authorship
Rank
Nomenclatural status
Identifier
Source
Source version
Publication or nomenclatural reference where available

A name should not automatically be interpreted as the currently accepted name merely because it exists in the system.

Taxonomic Relationships

The system should represent relationships explicitly.

Potential relationships include:

accepted name
synonym of
basionym of
homotypic synonym of
heterotypic synonym of
parent of
child of
congruent with
alternative treatment of
replaced by

Only relationships that are scientifically justified and supported by appropriate sources should be established.

The final relationship vocabulary will be defined in the taxonomy data model.

Source-Specific Treatments

Each major source may have its own taxonomic treatment.

For example:

Source A
Species X → accepted

Source B
Species X → synonym of Species Y

Source C
Species X → historical name

The platform should preserve these source-specific interpretations.

A source-specific treatment should include, where available:

Source
Source version
Taxon identifier
Name
Rank
Parent relationships
Accepted status
Synonym relationships
Relevant references
Retrieval information
Reconciled Taxonomy

Botanica Indica may maintain a reconciled taxonomic layer for platform-wide use.

The reconciled layer should not be interpreted as an assertion that every source agrees with it.

Instead, it represents the platform's documented reconciliation of available information.

A reconciliation should be supported by:

Source records
Taxonomic identifiers
Evidence
Rules or mappings
Review where appropriate
Version information

Where reconciliation is uncertain, the uncertainty should be represented.

No Silent Overwriting

The system must not perform transformations such as:

Source A name
      ↓
Platform name
      ↓
Discard Source A interpretation

without preserving the original source information.

Instead:

Source A treatment ──┐
                     │
Source B treatment ──┼──> Reconciliation
                     │
Source C treatment ──┘
                           │
                           ▼
                  Platform Taxonomy

The original source-specific information remains traceable.

Taxonomic Versioning

Taxonomic information must be version-aware.

A taxonomic record should be associated with the source version from which it originated where the source provides version information.

The platform should also maintain versions of its own reconciled taxonomy.

For example:

Source A
  Version 2026.1

Source B
  Version 2026.09

Botanica Indica
  Taxonomy Release 2026.09

A later release may change relationships without erasing the historical state.

Historical Taxonomy

Historical taxonomic information should be preserved where scientifically useful and legally permissible.

The platform should support questions such as:

What was this species called previously?
Which source used this name?
When did the relationship change?
What is the current treatment in a particular source?
Which taxonomic treatment applied to a historical record?

Historical information should not automatically be treated as current classification.

Synonyms

Synonyms should be represented explicitly.

A synonym relationship should retain:

The name
The related taxon
The relationship type where known
Source
Source version
Evidence or reference where available

The platform should distinguish between different kinds of synonymy where the underlying source supports such distinctions.

Accepted Names

"Accepted" must be interpreted in relation to a taxonomic treatment.

The platform should avoid treating:

Accepted

as an absolute property independent of source and time.

Instead, the system should be capable of representing:

Source A
Species X → accepted

Source B
Species X → synonym

and:

Source A, Version 2025
Species X → accepted

Source A, Version 2026
Species X → synonym
Taxonomic Identifiers

External taxonomic identifiers should be retained where available.

Examples include identifiers supplied by:

Taxonomic databases
Biodiversity platforms
Institutional datasets
Published datasets

External identifiers should not automatically become Botanica Indica's internal identifiers.

The platform should maintain its own stable identifiers while preserving mappings to external identifiers.

For example:

Botanica Indica Taxon ID
        │
        ├── Source A ID
        ├── Source B ID
        ├── Source C ID
        └── Source D ID

This allows external identifiers to change without necessarily changing the identity of the platform's records.

Taxonomic Matching

When importing records from different sources, the platform may perform taxonomic matching.

Matching may use combinations of:

Scientific name
Authorship
Rank
External identifiers
Synonym relationships
Parent taxonomy
Nomenclatural information
Source references
Other scientifically relevant evidence

Name-string equality alone should not automatically establish biological or taxonomic equivalence.

Matching Confidence

Automated taxonomic matching may produce uncertainty.

The system should support states such as:

Exact Match
Strong Match
Probable Match
Ambiguous Match
Unmatched

The final vocabulary and thresholds will be defined separately.

Automated matching should not be treated as equivalent to expert taxonomic review.

Human and Expert Review

Taxonomic reconciliation may require human or expert review.

Review may be required when:

Multiple sources conflict
Automated matching is ambiguous
Species concepts differ
Taxonomic changes are complex
The source relationship is unclear
A high-impact platform relationship is being established

The platform should preserve the review history where appropriate.

Taxonomic Evidence

Reconciliation decisions should be traceable to relevant evidence.

Evidence may include:

Taxonomic databases
Botanical literature
Floras
Nomenclatural references
Institutional records
Expert assessments
Other documented scientific sources

The reconciliation system should distinguish between:

Source says X

and:

Botanica Indica reconciles X with Y

These are different statements and should not be conflated.

Conflicting Taxonomies

When authoritative sources disagree, the platform should preserve the disagreement where scientifically relevant.

The platform may present:

Source-specific treatments
Reconciled treatment
Alternative classifications
Supporting evidence
Version information

The system should not manufacture consensus where none is documented.

Geographic Context

Taxonomic reconciliation may require geographic context.

A name or taxonomic treatment may have different relevance depending on:

Geographic region
Flora
Native range
Introduced range
Cultivated status
Historical distribution

Geographic information should therefore remain available to taxonomy workflows where scientifically appropriate.

Identification Integration

The identification system must not assume that an AI model's output is automatically the platform's accepted taxon.

The intended workflow is:

Image
  ↓
AI Candidate
  ↓
Taxonomic Resolution
  ↓
Source Mapping
  ↓
Reconciliation
  ↓
Candidate Platform Taxon
  ↓
User / Expert Validation

This allows AI models to produce candidates even when their taxonomic nomenclature differs from the platform's current treatment.

Data Import

Taxonomic data imported from external sources must retain:

Source
Source identifier
Source version where available
Original name
Original rank
Original relationships
Retrieval information
License information where applicable

Normalization must not destroy scientifically meaningful source information.

Taxonomic Release Process

Changes to the reconciled taxonomy should eventually be released through controlled versions.

A taxonomy release may contain:

Added taxa
Removed or deprecated mappings
Name changes
Synonym changes
Relationship changes
Source updates
Reconciliation decisions

Each release should be identifiable and reproducible where practical.

Taxonomic Corrections

Corrections should not erase historical information unnecessarily.

Where a taxonomic relationship is found to be incorrect, the system should preserve an appropriate audit history.

For example:

Previous Relationship
        ↓
Correction
        ↓
Current Relationship

The correction should identify the relevant evidence or source where practical.

Taxonomic Authority

Botanica Indica will not assume that one external database permanently represents the universal taxonomic authority for every purpose.

Different sources may have different strengths and scopes.

The platform should therefore remain source-aware and capable of representing multiple authoritative treatments.

A future governance or scientific policy may establish how reconciled treatments are approved for specific use cases.

Consequences
Positive consequences

This decision provides:

Preservation of scientific context
Support for multiple taxonomic authorities
Better handling of synonyms
Historical taxonomic traceability
Improved data interoperability
More reliable cross-source matching
Better integration with identification systems
Easier correction of taxonomic relationships
Greater scientific transparency
Reduced dependence on a single taxonomic provider
Negative consequences

This approach introduces:

More complex data models
More storage requirements
More complicated reconciliation workflows
Additional source-management requirements
Potential ambiguity in user-facing experiences
Need for scientific governance
Need for expert review in difficult cases

The project accepts this complexity because taxonomic reconciliation is a core scientific function of the ecosystem.

Consequences for User Experience

The user interface should provide understandable current information while preserving scientific context.

For example, a species page may eventually show:

Current platform treatment
        ↓
Accepted name

Also known as
        ↓
Synonyms / historical names

Taxonomic sources
        ↓
Source-specific treatments

Evidence
        ↓
References and provenance

The interface should avoid overwhelming ordinary users while allowing researchers and experts to access deeper taxonomic information.

Consequences for Search

Search should be capable of resolving:

Accepted names
Synonyms
Common names
Historical names
External identifiers where appropriate

A search for a synonym should be capable of reaching the corresponding taxonomic entity without falsely implying that the synonym is necessarily the current accepted treatment.

Consequences for API Design

Taxonomy APIs should expose sufficient information for clients to distinguish:

Taxonomic entity
Scientific name
Accepted status
Source
Source version
Synonym relationship
Reconciliation status
Confidence
Evidence

The exact API schema will be defined separately.

Consequences for AI/ML

AI/ML systems should consume normalized and versioned taxonomic identifiers where possible.

Model outputs using external identifiers or names should be mapped through the taxonomy reconciliation layer.

This allows models trained using different taxonomic datasets to interact with the platform without forcing the platform to adopt the model's taxonomy wholesale.

Related Decisions

This decision is related to:

ADR-001: Architecture Principles and Technology Independence
ADR-002: Modular Architecture
ADR-003: API-First Platform Architecture
ADR-004: Data and Scientific Provenance

Future ADRs should define:

Taxonomy data model
Taxonomic identifier strategy
Taxonomic matching algorithms
Source ingestion architecture
Scientific review and governance
Taxonomy API
Taxonomic release management
AI taxonomy mapping
Status

This decision is Accepted.

The specific taxonomy schema, reconciliation algorithms, source priority rules, review procedures, and release mechanisms will be defined through subsequent scientific and technical decisions.

No source-priority hierarchy is established by this ADR.
