# ADR-006: Identification Architecture

**Status:** Accepted  
**Date:** 2026-09-22

## Context

Plant identification is a core capability of the Botanica Indica ecosystem.

However, identification should not be treated as a single AI model returning a species name. A scientifically responsible identification system must account for uncertainty, geographic context, taxonomy, evidence, provenance, and human validation.

The architecture must also remain independent of any particular AI model, commercial identification provider, framework, or machine-learning technology.

An identification result may therefore represent a candidate hypothesis rather than a scientifically validated conclusion.

## Decision

Botanica Indica will implement identification as a modular, evidence-aware pipeline rather than as a direct image-to-species operation.

The conceptual identification pipeline is:

```text
Image / Observation
        ↓
Candidate Generation
        ↓
Geographic & Contextual Signals
        ↓
Taxonomic Resolution
        ↓
Evidence Aggregation
        ↓
Confidence & Explanation
        ↓
User Validation
        ↓
Expert Review / Scientific Validation

Each stage will have a defined responsibility and contract.

1. Candidate Generation

The identification system may use one or more AI/ML models or external identification providers to generate possible taxa.

Candidate generation may consider:

Plant images
Multiple images of the same observation
Image quality
Plant structures visible in the image
Geographic location
Habitat information
Observation date or season
User-provided contextual information
Model predictions
External identification services

The system must support multiple candidate results rather than assuming that the first prediction is correct.

Candidate generation is an assistive process and does not constitute scientific validation.

2. Geographic and Contextual Signals

Geographic and contextual information may be used to improve identification.

Examples include:

Country
State or administrative region
Ecological region
Habitat
Elevation
Season
Observation date
Cultivated versus wild context
Known species distribution

Geographic information must be treated as evidence rather than absolute proof.

Sensitive geographic information may require restricted storage, access control, or reduced precision where disclosure could create conservation or privacy risks.

3. Taxonomic Resolution

AI-generated names and external provider results must be resolved against the platform's taxonomy system.

Identification must therefore distinguish between:

A model-generated label
A scientific name
A taxonomic entity
A synonym
An accepted name under a particular taxonomic treatment
A source-specific taxonomic concept
A reconciled platform taxon

Taxonomic reconciliation will follow the principles defined in ADR-005: Taxonomy Reconciliation.

An identification result must not silently change because an external taxonomy changes.

4. Evidence Aggregation

Identification results should be accompanied by relevant evidence wherever available.

Evidence may include:

Taxonomic sources
Flora records
Herbarium records
Distribution records
Verified observations
Scientific literature
Expert annotations
Morphological characteristics
Geographic compatibility
Model predictions
External identification results

Evidence must retain provenance according to ADR-004: Data and Scientific Provenance.

The system should distinguish between evidence supporting an identification and evidence that merely provides contextual information.

5. Confidence and Uncertainty

Identification results must communicate uncertainty.

The system may use:

Confidence scores
Candidate rankings
Confidence categories
Evidence completeness
Model agreement
Geographic compatibility
Taxonomic certainty
Validation state

Confidence must not be presented as scientific certainty.

Where evidence is insufficient, conflicting, or outside the supported scope of the system, the system should be capable of returning an explicit abstention or uncertainty state such as:

Unable to determine reliably

The architecture must therefore support an "I don't know" outcome.

6. AI/ML Model Independence

The identification architecture must not depend on a single AI/ML model.

Models must be replaceable through defined interfaces.

The system should support:

Multiple identification models
Multiple model versions
Different model providers
Self-hosted models
External commercial or open identification services
Future models that do not yet exist

Model-specific implementation details must remain behind adapters or service boundaries.

Changing an identification model must not require redesigning the rest of the platform.

7. External Provider Isolation

External identification providers may be used where appropriate.

However, provider-specific APIs, credentials, response formats, limitations, and commercial dependencies must not become part of the platform's core domain model.

External providers should be accessed through adapters.

Conceptually:

Identification Domain
        ↓
Provider Adapter Interface
        ↓
 ┌──────────────┬──────────────┬──────────────┐
 │ Internal ML  │ Provider A   │ Provider B   │
 │ Model        │              │              │
 └──────────────┴──────────────┴──────────────┘

This preserves technology independence and makes provider replacement possible.

8. Human-in-the-Loop Validation

User and expert validation are distinct from AI prediction.

The system should support validation states including:

Submitted
AI Identified
User Confirmed
Expert Reviewed
Scientifically Verified

These states must not be collapsed into a single concept of "identified."

Users may provide corrections, additional photographs, contextual information, or competing identifications.

Experts may review observations and provide scientific assessments where appropriate.

The distinction between AI-generated information and human/scientific validation must remain explicit.

9. Image and Media Provenance

Images used for identification must retain appropriate provenance.

Where available, the system should preserve:

Observation identifier
Image identifier
Image source
Contributor
Capture date
Geographic context
Original media reference
Processing history
Image transformations
Licensing information

Derived images or processed media must not be confused with the original observation media.

Media provenance follows the principles defined in ADR-004: Data and Scientific Provenance.

10. Identification API Contract

Identification functionality must be exposed through a stable API contract rather than exposing model-specific implementation details.

A conceptual request may contain:

{
  "observation_id": "obs-123",
  "images": [
    {
      "media_id": "media-456"
    }
  ],
  "location": {
    "latitude": 12.97,
    "longitude": 77.59
  },
  "context": {
    "habitat": "urban garden"
  }
}

A conceptual response may contain:

{
  "identification_id": "id-789",
  "status": "candidate",
  "candidates": [
    {
      "taxon_id": "taxon-123",
      "confidence": 0.82,
      "evidence": [],
      "model": {
        "name": "example-model",
        "version": "1.0"
      }
    }
  ],
  "uncertainty": {
    "abstained": false
  }
}

The exact production schema will be defined separately through the API design process.

The API must preserve:

Identification provenance
Model identity
Model version
Candidate information
Confidence or uncertainty
Taxonomic references
Evidence references
Validation state
11. Model Versioning and Reproducibility

Identification results must be traceable to the model and configuration that produced them.

Where practical, the system should retain:

Model name
Model version
Provider
Configuration
Input references
Processing timestamp
Taxonomy version
Relevant geographic or contextual inputs

Re-running an identification with a newer model must not silently overwrite the historical result.

Historical identification results should remain auditable.

12. Benchmarking and Evaluation

Identification models must be evaluated independently from production identification workflows.

The ecosystem should support dedicated benchmarks covering relevant dimensions such as:

Species-level accuracy
Genus-level accuracy
Family-level accuracy
Geographic performance
Habitat variation
Image quality
Common versus rare species
Taxonomic ambiguity
Confidence calibration
Abstention performance

Benchmark datasets and evaluation methodology must retain appropriate provenance and licensing information.

The benchmark system should make it possible to compare models without coupling the platform to a particular model provider.

13. Privacy and Sensitive Data

Identification may involve sensitive observation information, particularly precise geographic coordinates.

The identification architecture must therefore support:

Access-controlled coordinates
Reduced geographic precision
Private observations
Restricted expert access
Separation of public and sensitive location data
Appropriate handling of user-contributed media

Identification providers must not automatically receive sensitive information unless the applicable data-sharing rules and user permissions allow it.

14. Failure and Abstention

The system must treat uncertainty and failure as valid outcomes.

Examples include:

Image quality too poor
Plant structure not sufficiently visible
Species outside the supported model domain
Conflicting model predictions
Insufficient geographic compatibility
Taxonomic ambiguity
Insufficient evidence
Conflicting scientific sources

The system should prefer an explicit uncertain result over presenting an unsupported species identification as authoritative.

15. Architectural Consequences

This decision provides:

Replaceable AI/ML models
Provider independence
Explicit uncertainty
Human and expert validation
Reproducible identification results
Strong identification provenance
Integration with the taxonomy system
Integration with the evidence system
Separation between prediction and scientific validation
A stable API for multiple clients

It also introduces additional complexity in:

Model management
Evaluation
Provenance tracking
Taxonomic reconciliation
Evidence aggregation
Validation workflows
API design
Storage and processing requirements

This complexity is intentional because identification is a scientific and evidence-producing capability rather than merely a classification feature.

Related ADRs
ADR-001: Architecture Principles & Technology Independence
ADR-002: Modular Architecture
ADR-003: API-First Platform Architecture
ADR-004: Data and Scientific Provenance
ADR-005: Taxonomy Reconciliation
