# ADR-008: Geospatial and Sensitive Location Data

**Status:** Accepted  
**Date:** 2026-09-22

## Context

Geographic information is an important component of botanical intelligence.

The location of an observation can improve:

- Species identification
- Taxonomic interpretation
- Distribution analysis
- Habitat assessment
- Ecological analysis
- Conservation research
- Scientific validation

However, precise locations can also create privacy, conservation, and security risks.

Examples include:

- Locations of threatened or rare species
- Nesting or breeding locations
- Sensitive populations
- Private properties
- Personally identifying observation locations
- Locations of economically or ecologically valuable plants
- Locations that could facilitate exploitation or illegal collection

The platform therefore needs a geospatial architecture that supports scientific usefulness without assuming that every geographic coordinate should be publicly exposed.

## Decision

Botanica Indica will treat geographic information as a first-class domain capability with explicit support for:

- Geographic context
- Spatial queries
- Multiple levels of geographic precision
- Sensitive-location protection
- Access control
- Privacy-aware data sharing
- Geospatial provenance
- Geographic uncertainty
- Scientific and conservation use cases

Precise location will not automatically imply public location.

## 1. Geographic Information as Evidence

Geographic information may contribute to identification and scientific interpretation.

Examples include:

- Country
- State
- District
- Locality
- Protected area
- Ecological region
- Habitat
- Elevation
- Latitude and longitude
- Observation range
- Historical distribution

Geographic information should be treated as evidence or context rather than absolute proof of species identity.

A species being geographically plausible does not establish that it is present at a particular location.

## 2. Geographic Precision

The platform should support multiple geographic precision levels.

Conceptually:

```text
Exact Coordinates
      ↓
Approximate Coordinates
      ↓
Locality
      ↓
District
      ↓
State / Region
      ↓
Country

The appropriate precision may depend on:

User privacy
Conservation sensitivity
Species sensitivity
Scientific requirements
Observation visibility
Research permissions
Institutional policies

The original precise location should be preserved only where there is a legitimate reason to retain it and where applicable permissions and policies allow it.

3. Public and Private Location Representations

An observation may have more than one geographic representation.

For example:

Observation
    │
    ├── Private Location
    │      └── Exact coordinates
    │
    └── Public Location
           └── Generalized coordinates / locality

The public representation must not allow unauthorized users to reconstruct a protected precise location.

Public geographic information should therefore be generated according to defined privacy and sensitivity rules.

4. Sensitive Species and Locations

The platform should support identification of observations requiring additional geographic protection.

Sensitivity may be associated with:

Species
Taxonomic groups
Populations
Habitats
Protected areas
Specific locations
Conservation circumstances

Sensitivity rules may change over time and should therefore be versionable.

The system should avoid assuming that all observations of a taxon have the same sensitivity.

5. Access Control

Geographic access should be governed independently from general observation visibility where necessary.

Potential access levels include:

Public
Generalized public
Contributor only
Approved researchers
Experts
Institutional users
Administrators

The exact access-control model will be defined through future security and authorization architecture decisions.

Access to precise coordinates should be auditable where appropriate.

6. Location Privacy

Location information may constitute sensitive personal information when combined with other information.

The platform should therefore consider:

Whether the location is associated with a private individual
Whether the observation can identify a person's residence or routine
Whether precise coordinates expose private property
Whether location combined with timestamps or media creates additional privacy risk

The system should minimize unnecessary exposure of precise location data.

7. Geographic Uncertainty

Not every observation will have an exact or reliable coordinate.

The system should support geographic uncertainty such as:

Approximate location
Locality-only information
Historical locality
Georeferenced historical records
Coordinate uncertainty radius
Unknown location
User-provided location without verification

Geographic uncertainty should not be silently converted into false precision.

Where a source provides coordinate uncertainty, that uncertainty should be preserved.

8. Geospatial Provenance

Geographic information must retain appropriate provenance.

Where available, the system should preserve:

Original coordinates
Original coordinate system
Source
Source identifier
Georeferencing method
Georeferencing date
Coordinate uncertainty
Transformation history
Accuracy information
Geographic precision
Privacy transformation history

Geospatial provenance follows the broader provenance principles established in ADR-004: Data and Scientific Provenance.

9. Coordinate Reference Systems

The platform must explicitly represent coordinate reference systems where relevant.

Geospatial data should not assume that every coordinate is expressed in the same reference system.

The production geospatial data model should support:

Coordinate reference system identification
Standard geographic coordinates
Spatial transformations
Validation of coordinate ranges
Preservation of source coordinate information where necessary

PostgreSQL/PostGIS is identified in ADR-001 as the initial preferred geospatial data technology, but the domain model must not depend on database-specific representations.

10. Spatial Queries

The platform should support spatial operations required by botanical and ecological use cases.

Examples include:

Observations near a location
Observations within a region
Species distribution areas
Habitat intersection
Protected-area intersection
Geographic candidate filtering
Spatial clustering
Distribution mapping
Range analysis

Spatial queries must respect observation visibility and location-access restrictions.

A query requesting nearby observations must not bypass geographic privacy controls.

11. Geographic Context in Identification

Geographic information may be provided to identification systems as contextual evidence.

However:

Geographic compatibility
        ≠
Species confirmation

Identification systems must not force a candidate solely because it is geographically expected.

Geographic context should be combined with visual, taxonomic, morphological, and other available evidence.

This follows the identification architecture defined in ADR-006.

12. Sensitive Location Protection During AI Processing

When identification or other processing uses external AI or data providers, precise location must not automatically be transmitted.

The platform should determine what geographic information is necessary for the specific processing operation.

Where appropriate, the system may provide:

Generalized coordinates
Administrative region
Ecological region
Habitat
No geographic information

External providers must receive only the information permitted by applicable privacy, licensing, and data-sharing requirements.

13. Location Generalization

The platform should support controlled geographic generalization.

Possible approaches include:

Coordinate rounding
Grid-based generalization
Radius-based uncertainty
Administrative-area representation
Locality representation
Controlled spatial masking

The selected method should depend on the sensitivity and scientific requirements of the observation.

Generalization must not be presented as an exact original location.

14. Conservation and Scientific Use

Protected geographic information may still be valuable for legitimate scientific purposes.

The architecture should therefore support controlled access for use cases such as:

Conservation planning
Species distribution research
Population monitoring
Ecological research
Expert validation
Institutional collaboration
Biodiversity assessments

Scientific usefulness should be preserved without requiring public disclosure of sensitive coordinates.

15. Historical and External Geographic Data

External biodiversity and botanical sources may provide geographic records with different:

Coordinate precision
Geographic standards
Uncertainty
Licensing
Temporal coverage
Georeferencing methodologies

Imported geographic information must retain its source and provenance.

The platform must not imply that externally sourced coordinates were collected or verified by Botanica Indica.

16. Geographic Data Corrections

Geographic information may be incorrect or incomplete.

The system should support:

Coordinate corrections
Location uncertainty updates
Georeferencing corrections
Duplicate-location corrections
Historical location corrections
User or expert reports of geographic errors

Corrections should preserve an audit history where appropriate.

The original source information should not be silently destroyed when historical preservation is necessary.

17. Location and Observation Visibility

Observation visibility and geographic precision should be independently controllable.

For example:

Observation: Public
Location: Generalized

Observation: Public
Location: Restricted

Observation: Private
Location: Exact

Observation: Research-access
Location: Exact

This separation allows scientific observations to remain discoverable while protecting sensitive geographic information.

18. API Requirements

The platform API should support explicit geographic visibility and precision.

API responses should not expose precise coordinates merely because the underlying observation contains them.

The API should distinguish between:

Stored location
User-visible location
Generalized location
Geographic uncertainty
Access permissions

Geographic fields should be subject to authorization and sensitivity rules before serialization into API responses.

19. Data Retention and Deletion

Geographic information must follow applicable data-retention and deletion requirements.

When a user requests deletion of an observation or associated personal information, geographic data must be considered as part of that request.

Where scientific or legal requirements require retention of derived or historical records, the system should document the applicable retention basis and minimize unnecessary personal information.

20. Architectural Consequences

This decision provides:

Stronger location privacy
Support for sensitive species observations
Scientifically useful spatial analysis
Geographic uncertainty representation
Controlled research access
Privacy-aware AI processing
Reusable geospatial infrastructure
Better integration with biodiversity and conservation workflows

It also introduces additional complexity in:

Access control
Spatial data modelling
Location generalization
Sensitivity rules
Geospatial provenance
Privacy management
Spatial query authorization
Data retention

This complexity is intentional because geographic information is simultaneously a scientific resource and a potential privacy or conservation risk.

Related ADRs
ADR-001: Architecture Principles & Technology Independence
ADR-002: Modular Architecture
ADR-003: API-First Platform Architecture
ADR-004: Data and Scientific Provenance
ADR-005: Taxonomy Reconciliation
ADR-006: Identification Architecture
ADR-007: Evidence and Expert Validation
