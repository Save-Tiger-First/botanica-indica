# ADR-009: Observation and Contribution Model

**Status:** Accepted  
**Date:** 2026-09-22

## Context

Observations are the fundamental records through which botanical information enters the Botanica Indica ecosystem.

An observation may contain:

- One or more images
- Geographic information
- Date and time
- Habitat information
- User-provided descriptions
- Identification suggestions
- Taxonomic information
- Evidence
- Validation history
- Contributor information

However, an observation is not the same thing as an identification.

A single observation may receive multiple identifications, evidence items, corrections, expert assessments, and other contributions over time.

The architecture therefore needs to distinguish the original observation from the contributions and interpretations associated with it.

## Decision

Botanica Indica will model an **observation as a first-class scientific record** and will treat contributions, identifications, evidence, and validation activities as related but distinct records.

The observation should represent the documented encounter or specimen-related record, while interpretations and contributions should remain separately attributable and auditable.

Conceptually:

```text
Observation
    │
    ├── Media
    ├── Location
    ├── Observation Metadata
    │
    ├── Identifications
    │
    ├── Evidence
    │
    ├── Community Contributions
    │
    └── Expert Reviews

1. Observation as the Core Record

An observation represents a documented occurrence or encounter with a plant or other botanical subject within the scope of the platform.

An observation may be created before its taxonomic identity is known.

Therefore:

Observation ≠ Identification

An observation should remain valid even when:

No identification exists
The identification is uncertain
Multiple identifications exist
Identifications conflict
The taxonomy changes
An identification is later corrected
2. Observation Identity

Each observation must have a stable platform identifier.

The identifier should remain stable even when:

The observation receives new identifications
Metadata is corrected
Taxonomic relationships change
New evidence is added
The observation is reviewed
Additional media is added

External source identifiers should also be retained where the observation originated from an external source.

The platform's internal identifier must not depend on an external provider's identifier.

3. Observation Metadata

An observation may contain metadata such as:

Observation date
Observation time
Geographic information
Habitat
Growth form
Phenological information
Environmental context
User description
Media
Source information
Contributor information

Metadata should distinguish between:

User-provided information
Automatically derived information
Externally sourced information
Expert-provided information

The origin of important metadata should be traceable.

4. Media

An observation may contain multiple media items.

Examples include:

Whole-plant photographs
Leaf photographs
Flower photographs
Fruit photographs
Bark photographs
Habit photographs
Microscopic images
Herbarium images
Other supporting media

Each media item should have its own identity and provenance.

Media may be added after the original observation was created.

The observation should not depend on a single image.

5. Multiple Media and Identification

Identification systems should be able to use multiple media associated with the same observation.

For example:

Observation
    ├── Whole plant image
    ├── Leaf image
    ├── Flower image
    └── Fruit image
              ↓
       Identification

The identification system should retain appropriate references to the media used for a prediction or assessment where practical.

This supports reproducibility and scientific review.

6. Contributor Attribution

Contributions must be attributable to their source where appropriate.

Possible contributors include:

Observation creator
Community contributor
Expert reviewer
Institutional contributor
Automated system
External data provider

Automated contributions must be distinguishable from human contributions.

The platform should preserve contributor attribution without unnecessarily exposing personal information.

7. Observation Ownership and Stewardship

Creation of an observation does not necessarily imply permanent ownership of all subsequent scientific interpretations.

The original contributor should retain appropriate attribution and control according to platform policies.

Other users, experts, or automated systems may contribute:

Identifications
Evidence
Corrections
Additional media
Contextual information
Validation

Such contributions should not silently replace the original contribution.

8. Identification Contributions

Multiple identification records may be associated with a single observation.

For example:

Observation
    │
    ├── Identification A → Taxon A
    ├── Identification B → Taxon B
    ├── Identification C → Taxon A
    └── Expert Review → Taxon B

The architecture must preserve these contributions.

A current or accepted interpretation may be exposed to users while the underlying history remains available for appropriate audit and scientific purposes.

Identification architecture follows ADR-006.

9. Community Contributions

Community participation may include:

Suggested identification
Confirmation
Correction
Additional media
Habitat information
Distribution information
Scientific references
Discussion
Reports of possible errors

Community contributions should remain distinguishable from expert validation.

Community participation should not automatically imply scientific verification.

10. Expert Contributions

Experts may contribute:

Identification assessments
Taxonomic interpretations
Morphological observations
Evidence references
Corrections
Review comments
Validation decisions

Expert contributions should retain their own provenance and review history.

Expert contributions must not silently modify the original observation record without an auditable relationship to the change.

Expert validation follows ADR-007.

11. Automated Contributions

Automated systems may generate information associated with an observation.

Examples include:

AI identification candidates
Image quality assessments
Geographic classifications
Habitat classifications
Derived measurements
Metadata extraction
Duplicate detection
Taxonomic matching

Automated contributions must be explicitly identified as machine-generated.

The system should retain:

Model or algorithm identity
Version
Processing time
Input references
Relevant configuration
Result provenance

Automated information must not be represented as human or expert validation.

12. Observation Lifecycle

An observation may pass through different states over time.

A conceptual lifecycle is:

Created
   ↓
Submitted
   ↓
Identified / Unidentified
   ↓
Community Contributions
   ↓
Expert Review
   ↓
Validated / Unresolved

This is not intended to be a mandatory linear workflow.

An observation may:

Remain unidentified
Return to an unresolved state
Receive competing identifications
Receive additional evidence
Be corrected
Be withdrawn
Be subject to later scientific review

The architecture must support non-linear scientific workflows.

13. Corrections

Observation information may be corrected over time.

Examples include:

Incorrect date
Incorrect location
Incorrect habitat
Incorrect media metadata
Incorrect taxonomic identification
Duplicate observation
Incorrect attribution

Corrections should preserve sufficient history to understand what changed and why.

Where appropriate, the system should retain:

Previous value
New value
Contributor
Timestamp
Reason
Supporting evidence

The exact audit implementation will be defined through future platform and security architecture decisions.

14. Duplicate Observations

The system should support detection and management of duplicate observations.

Potential duplicate indicators may include:

Identical or near-identical media
Same contributor
Same location
Similar observation time
Similar metadata
External source identifiers

Automated duplicate detection should produce a candidate relationship rather than automatically deleting or merging records without appropriate validation.

Where observations are merged, the provenance of the original records must be preserved.

15. Observation Deletion and Withdrawal

The architecture must distinguish between:

User-requested deletion
Withdrawal from public display
Administrative removal
Invalid or duplicate records
Source withdrawal
Legal or privacy-related removal

Deletion or withdrawal must not unnecessarily destroy scientific provenance where retention is required or appropriate.

Where information must be retained, access and visibility should be controlled according to applicable policies.

16. External Observations

Observations may be imported or referenced from external biodiversity and botanical systems.

External observations must retain:

Source
External identifier
Import or synchronization information
Source version where available
Licensing information
Original contributor information where permitted
Transformation history

Imported observations must not automatically be represented as observations originally collected by Botanica Indica.

17. Observation Provenance

Observation provenance follows ADR-004: Data and Scientific Provenance.

The system should be able to distinguish:

Original Observation
       ↓
Derived Information
       ↓
Identification
       ↓
Evidence
       ↓
Validation

Each stage should retain appropriate relationships to its source.

This supports scientific reproducibility and auditability.

18. Sensitive Observation Information

Some observation data may require restricted access.

Examples include:

Precise geographic coordinates
Private property information
Sensitive conservation locations
Private contributor information
Restricted research material

Geographic privacy follows ADR-008: Geospatial and Sensitive Location Data.

Observation visibility and geographic precision must therefore remain independently controllable.

19. Observation Versioning

Important observation changes should be versionable.

Versioning may apply to:

Metadata
Geographic information
Media associations
Descriptions
Taxonomic interpretation
Visibility
Validation state

The platform should avoid rewriting historical scientific records without preserving the relevant history.

20. API Representation

The observation API should distinguish between the observation itself and associated contributions.

A conceptual response may contain:

{
  "observation_id": "obs-123",
  "media": [],
  "location": {},
  "metadata": {},
  "identifications": [],
  "evidence": [],
  "contributions": [],
  "validation": {}
}

The exact production API schema will be defined separately.

Clients should not create their own independent representations of observation lifecycle or scientific validation.

21. Contribution Permissions

The platform should support different contribution permissions.

Possible permissions include:

Create observation
Edit own observation
Add identification
Add evidence
Add media
Comment
Review
Validate
Moderate
Administrate

Permissions should be separated from scientific status.

Having permission to contribute does not itself establish scientific authority.

22. Architectural Consequences

This decision provides:

Clear separation between observations and interpretations
Multiple identification support
Strong contributor attribution
Preservation of scientific history
Support for community participation
Support for expert review
Support for automated processing
Better provenance
Flexible observation lifecycle
Integration with future research and institutional workflows

It also introduces additional complexity in:

Contribution modelling
Versioning
Audit history
Access control
Duplicate management
External data integration
Observation lifecycle management

This complexity is intentional because observations are the foundational scientific records of the ecosystem and must remain useful independently of any single identification or interpretation.

Related ADRs
ADR-001: Architecture Principles & Technology Independence
ADR-002: Modular Architecture
ADR-003: API-First Platform Architecture
ADR-004: Data and Scientific Provenance
ADR-005: Taxonomy Reconciliation
ADR-006: Identification Architecture
ADR-007: Evidence and Expert Validation
ADR-008: Geospatial and Sensitive Location Data
