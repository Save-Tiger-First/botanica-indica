# ADR-002: Modular Architecture

- **Status:** Accepted
- **Date:** 2026-09-22
- **Decision Type:** Architecture
- **Scope:** Botanica Indica platform and ecosystem

## Context

Botanica Indica is intended to become a full-fledged botanical intelligence ecosystem supporting multiple applications, scientific workflows, data sources, AI/ML systems, expert validation, community participation, and institutional integrations.

The ecosystem contains multiple functional domains with different technical and operational requirements.

Examples include:

- Taxonomy
- Plant identification
- Observations
- Scientific evidence
- Geographic information
- Data ingestion
- Expert review
- Users and authentication
- Search
- AI/ML
- Community contributions
- Administration

If these capabilities are developed as one undifferentiated codebase, boundaries between responsibilities can become unclear and changes in one area can unnecessarily affect other areas.

Conversely, immediately implementing every capability as an independent microservice would introduce operational complexity before the boundaries and requirements are sufficiently understood.

The architecture therefore needs a middle ground that provides strong separation of responsibilities while allowing the system to evolve incrementally.

## Decision

Botanica Indica will use a **modular architecture**.

The system will be divided into clearly defined functional modules with explicit responsibilities and interfaces.

Modules should have:

- A clearly defined purpose
- Explicit inputs and outputs
- Defined ownership of data and business rules
- Minimal unnecessary coupling
- Testable boundaries
- Documented interfaces

The initial implementation may operate within a modular monolith where appropriate.

Modules may later be extracted into independent services when there is a demonstrated technical or operational reason.

## Initial Logical Modules

The following logical modules are established as the initial architectural boundaries.

### 1. Taxonomy

Responsible for botanical and taxonomic concepts.

Potential responsibilities include:

- Taxa
- Accepted names
- Synonyms
- Taxonomic relationships
- Taxonomic sources
- Taxonomic versions
- Taxonomic reconciliation

### 2. Identification

Responsible for plant identification workflows.

Potential responsibilities include:

- Image-based identification
- Candidate generation
- Candidate ranking
- Identification requests
- Identification results
- Identification confidence
- Model results
- Human confirmation

### 3. Observations

Responsible for observations of plants and associated field records.

Potential responsibilities include:

- Observation records
- Observation metadata
- Images associated with observations
- Geographic coordinates
- Observation dates
- Observer information
- Observation status

### 4. Evidence

Responsible for representing scientific and informational evidence.

Potential responsibilities include:

- Evidence records
- Source references
- Citations
- Provenance
- Evidence relationships
- Source reliability metadata
- Evidence versioning

### 5. Geography

Responsible for geographic and spatial information.

Potential responsibilities include:

- Coordinates
- Regions
- Administrative boundaries
- Ecological regions
- Distribution information
- Spatial queries
- Geographic relationships

### 6. Expert Review

Responsible for scientific and expert validation workflows.

Potential responsibilities include:

- Review requests
- Expert assessments
- Review status
- Corrections
- Validation history
- Reviewer attribution

### 7. Users and Authentication

Responsible for identity and access management.

Potential responsibilities include:

- User accounts
- Authentication
- Authorization
- Roles
- Permissions
- Sessions
- Account security

### 8. Data Ingestion

Responsible for importing and processing external datasets.

Potential responsibilities include:

- Source connectors
- Import pipelines
- Data validation
- Transformation
- Deduplication
- Provenance
- Import history
- Error handling

### 9. AI/ML

Responsible for machine-learning capabilities.

Potential responsibilities include:

- Model management
- Model inference
- Training pipelines
- Dataset management
- Model evaluation
- Benchmarking
- Model versions
- Prediction metadata

AI/ML components must remain separable from scientific authority and expert validation.

### 10. Search

Responsible for discovery and retrieval across the ecosystem.

Potential responsibilities include:

- Species search
- Taxonomic search
- Full-text search
- Geographic search
- Evidence search
- Observation search

### 11. Community

Responsible for community participation and contributions.

Potential responsibilities include:

- Contributions
- Comments
- Corrections
- Community validation
- Moderation
- Contribution history

### 12. Administration

Responsible for operational management of the platform.

Potential responsibilities include:

- Administrative controls
- Configuration
- Moderation tools
- System management
- Operational reporting
- Audit information

## Module Boundaries

Modules should communicate through defined interfaces rather than directly accessing the internal implementation details of other modules.

A module should not depend on another module's private implementation merely because both exist within the same application.

Where data must cross a module boundary, the interaction should use an explicit contract.

Examples include:

```text
Identification → Taxonomy
Identification → Observations
Observations → Geography
Evidence → Taxonomy
Expert Review → Identification
Data Ingestion → Taxonomy
Data Ingestion → Evidence
Search → Multiple domain modules

These relationships represent logical dependencies and do not necessarily imply separate network services.

Shared Infrastructure

Modules may use shared infrastructure where appropriate.

Examples include:

PostgreSQL
PostGIS
Object storage
Caching
Message queues
Logging
Metrics
Authentication infrastructure

Shared infrastructure must not be used as a reason to bypass module boundaries.

For example, sharing a database does not automatically mean that every module should freely modify every other module's tables.

Database Boundary Principle

The initial architecture may use a shared PostgreSQL/PostGIS database.

Logical ownership of data must nevertheless remain associated with the appropriate module.

For example:

Taxonomy       → Taxonomic data
Observations   → Observation data
Evidence       → Evidence data
Users          → Identity and access data
Geography      → Spatial reference data

Cross-module queries should be deliberately designed rather than emerging through unrestricted table access.

Modular Monolith

The initial platform may use a modular monolith.

A modular monolith means:

Modules are logically separated.
Modules have defined interfaces.
Modules can be tested independently.
Internal implementation details remain encapsulated.
The application may still be deployed as a single unit.

This approach allows the project to establish correct domain boundaries before introducing distributed-system complexity.

Service Extraction

A module may later become an independent service when one or more of the following conditions justify extraction:

Independent scaling requirements
Independent deployment requirements
Different runtime requirements
Significant resource requirements
Fault isolation requirements
Security isolation requirements
Independent development ownership
External integration requirements
Clear and stable service boundaries

Service extraction should preserve the previously defined contract wherever practical.

Dependency Direction

Dependencies should generally flow toward clearly defined domain capabilities rather than creating circular dependencies.

The architecture should avoid situations such as:

Module A → Module B → Module A

where the relationship can instead be represented through a shared contract, event, or better-defined domain boundary.

Circular dependencies must be treated as an architectural warning.

Events

Where appropriate, modules may communicate through domain events.

Examples may include:

ObservationCreated
IdentificationRequested
IdentificationCompleted
TaxonomicRecordUpdated
ExpertReviewSubmitted
ExpertReviewCompleted
EvidenceAdded
DatasetImported

Events must be documented and versioned where they become part of a stable integration contract.

Events should not be introduced merely for architectural fashion.

API Boundary

External clients should interact with the platform through documented APIs.

Potential clients include:

Mobile applications
Web applications
Administrative applications
Research tools
Institutional systems
Future third-party applications

Core domain logic should not be duplicated independently inside each client.

AI/ML Boundary

AI/ML systems will be treated as replaceable components.

For example:

Image
  ↓
Identification Interface
  ↓
Model Adapter
  ↓
Model
  ↓
Candidate Results
  ↓
Taxonomy / Evidence / Validation

The rest of the ecosystem should interact with an identification interface rather than depending directly on a specific model implementation.

This allows models to be replaced, compared, benchmarked, or removed without redesigning the entire platform.

External Data Provider Boundary

External biodiversity and botanical data providers should be integrated through dedicated ingestion or adapter mechanisms.

External provider-specific formats and APIs should not unnecessarily propagate throughout the core domain model.

The architecture should allow a provider to be replaced or supplemented without requiring unrelated modules to change.

All imported information must retain appropriate source and provenance information.

Client Architecture

Applications such as mobile and web clients should consume shared platform capabilities.

The intended relationship is:

                    ┌───────────────┐
                    │ Mobile Client │
                    └───────┬───────┘
                            │
                    ┌───────▼───────┐
                    │               │
                    │ Platform APIs  │
                    │               │
                    └───────┬───────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
   ┌────▼────┐        ┌─────▼─────┐       ┌────▼────┐
   │ Taxonomy│        │Observation│       │Evidence │
   └─────────┘        └───────────┘       └─────────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
                    ┌───────▼───────┐
                    │ Shared Data   │
                    │ Infrastructure│
                    └───────────────┘

Other clients such as web applications, research interfaces, and institutional integrations may use the same platform capabilities.

Testing

Each module should have tests appropriate to its responsibilities.

Testing should occur at multiple levels:

Unit tests
Module tests
Integration tests
API contract tests
End-to-end tests
Data validation tests
Scientific validation tests where applicable
AI/ML evaluation and benchmark tests where applicable

Module boundaries should make it possible to test components without requiring the entire ecosystem to run for every test.

Observability

The architecture should support observability across module boundaries.

Where appropriate, the system should provide:

Structured logging
Metrics
Error tracking
Request tracing
Audit records

Distributed tracing should be introduced when the architecture becomes sufficiently distributed to justify it.

Consequences
Positive consequences

This decision provides:

Clear separation of responsibilities
Better maintainability
Easier testing
Controlled coupling
Reusable domain capabilities
Gradual architectural evolution
Ability to begin with a modular monolith
Ability to extract services later
Reduced risk of premature microservice complexity
Better support for multiple clients
Better technology independence
Negative consequences

This architecture requires:

Careful module design
Explicit contracts
Documentation
Discipline around data ownership
Additional architectural governance
More deliberate dependency management

Incorrectly designed modules can still create coupling even when the architecture is formally modular.

Consequences for Development

Development should proceed by establishing and validating domain boundaries before optimizing deployment topology.

The project should prioritize:

Domain clarity
Contract clarity
Data ownership
Testability
Interoperability
Operational requirements
Service extraction only when justified

The physical deployment architecture may evolve without requiring the logical domain architecture to be redesigned.

Related Decisions

This ADR is related to:

ADR-001: Architecture Principles and Technology Independence
Future database architecture decisions
Future API architecture decisions
Future taxonomy architecture decisions
Future identification pipeline decisions
Future AI/ML architecture decisions
Future data provenance decisions
Future deployment and infrastructure decisions
Status

This decision is Accepted.

The logical module boundaries may evolve as the project gains scientific, technical, and operational knowledge.

Changes to major module boundaries should be documented through a new or updated Architecture Decision Record.
