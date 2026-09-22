# ADR-001: Architecture Principles and Technology Independence

- **Status:** Accepted
- **Date:** 2026-09-22
- **Decision Type:** Architecture
- **Scope:** Entire Botanica Indica ecosystem

## Context

Botanica Indica is being developed as a full-fledged botanical intelligence ecosystem rather than as a single application.

The ecosystem is expected to support multiple clients and capabilities, including:

- Mobile applications
- Web applications
- Public APIs
- Botanical and taxonomic data services
- Plant identification and AI/ML services
- Scientific evidence and provenance
- Geographic and ecological information
- Observation and contribution workflows
- Expert validation
- Community participation
- Research and institutional integrations

The ecosystem may evolve over many years. Technologies, programming languages, frameworks, cloud providers, databases, AI models, and external data providers may change during that period.

Therefore, the architecture must avoid unnecessary dependence on any single technology or external provider.

## Decision

Botanica Indica will follow a **technology-independent, modular, contract-driven architecture**.

The architecture will be organized conceptually into three layers:

```text
Contracts
   ↓
Services
   ↓
Clients

1. Contracts

Communication between major components will use documented and versioned contracts.

Where appropriate, the ecosystem will use:

JSON
OpenAPI
REST APIs
Standard authentication protocols
Standard data formats
Versioned schemas

Bulk and scientific data may use appropriate interoperable formats such as:

CSV
Parquet
GeoJSON
Other documented scientific or geographic formats where required

Contracts should remain as independent as reasonably possible from the implementation language or framework.

2. Services

The system will be divided into clearly defined functional modules.

Examples include:

Taxonomy
Observations
Identification
Evidence
Geography
Expert review
Users and authentication
Data ingestion
AI/ML
Search
Community contributions

The initial implementation may use a modular monolithic architecture where appropriate.

Individual components may later be extracted into independent services when there is a demonstrated architectural or operational reason to do so.

The project will not adopt microservices solely for the sake of using microservices.

3. Clients

Applications will consume the underlying platform through documented contracts rather than implementing independent copies of core business logic.

Potential clients include:

Mobile applications
Web applications
Administrative interfaces
Scientific/research interfaces
Institutional integrations
Future applications and services

This allows multiple clients to share the same underlying botanical intelligence infrastructure.

Technology Strategy

The project will not require a single programming language for the entire ecosystem.

The following technology roles are currently intended:

Area	Primary Technology
Platform/API/application services	TypeScript
AI/ML/scientific computing/data science	Python
Mobile application	Dart / Flutter
Database	PostgreSQL / PostGIS
API/data contracts	JSON / OpenAPI
Bulk data	CSV / Parquet / GeoJSON
Performance-critical components	Rust where justified
Native platform integration	Kotlin / Swift where required

These are architectural preferences rather than permanent restrictions.

A component may use another technology when there is a documented technical reason to do so.

Technology Independence Principles

The ecosystem should avoid unnecessary dependence on:

A single programming language
A single application framework
A single cloud provider
A single database vendor
A single AI model
A single plant-identification provider
A single external biodiversity database
A single authentication provider
A single deployment platform

External providers should be integrated through clearly defined interfaces wherever practical.

Replacing an external provider should not require rewriting unrelated parts of the ecosystem.

Data Independence

Core scientific and botanical knowledge should not be permanently coupled to a single external data provider.

External data sources may be used for:

Taxonomic information
Species information
Observations
Images
Geographic information
Scientific literature
Biodiversity records
Identification signals

However, each external source must retain appropriate provenance, attribution, licensing information, and source-specific restrictions.

The system must distinguish between:

Original project data
External source data
Derived data
AI-generated information
Expert-reviewed information
User-contributed information
AI Independence

AI and machine-learning systems are considered components of the ecosystem rather than the ultimate authority on botanical truth.

The architecture should allow identification models to be:

Added
Replaced
Retrained
Benchmarked
Compared
Removed

without requiring fundamental changes to the rest of the platform.

AI-generated identification should remain distinguishable from scientific or expert validation.

The system must be capable of representing uncertainty and cases where the available evidence is insufficient for a reliable identification.

Scientific Independence

Taxonomic and scientific information should be represented in a way that permits multiple authoritative sources and taxonomic treatments to be compared or reconciled.

The architecture must support:

Taxonomic versioning
Source attribution
Synonyms
Accepted names
Alternative taxonomic treatments
Historical classifications
Conflicting sources
Evidence and provenance
Expert review

No single external taxonomy should automatically be treated as the permanent and universal authority for the entire ecosystem.

Interoperability

Components should communicate using documented interfaces and standards wherever practical.

The project should prefer:

Open standards
Portable data formats
Versioned schemas
Documented APIs
Reproducible workflows
Exportable data

over proprietary or tightly coupled integrations.

Reversibility

Where practical, major technology decisions should preserve the ability to replace a component later.

Examples include:

Database replacement
AI model replacement
Cloud provider migration
Authentication provider replacement
Search engine replacement
External biodiversity data provider replacement

Architecture decisions should therefore consider both current requirements and future migration costs.

Consequences
Positive consequences

This decision provides:

Greater long-term flexibility
Reduced vendor lock-in
Reusable infrastructure
Multiple application clients
Easier integration with scientific institutions
Easier replacement of AI models
Better interoperability
Clear separation between scientific data and application code
Greater potential for long-term open-source collaboration
Negative consequences

This approach introduces additional complexity.

It requires:

More careful API design
Version management
Strong documentation
Data provenance management
Clear module boundaries
More deliberate architectural decisions
Additional testing between components

The project accepts this complexity because the intended lifetime and scope of the ecosystem justify a durable architecture.

Implementation Guidance

The project should initially prioritize clear module boundaries and well-defined contracts rather than prematurely distributing every component into separate network services.

A modular monolith may therefore be used where appropriate.

Components should be extracted into independent services when justified by factors such as:

Independent scaling requirements
Independent deployment requirements
Clear ownership boundaries
Resource isolation
Reliability requirements
Technology-specific runtime requirements
Significant operational benefits
Related Decisions

Future ADRs should document significant decisions concerning:

Repository and project structure
Backend architecture
Database architecture
Taxonomy reconciliation
Data provenance
AI/ML architecture
Identification pipeline
Authentication and authorization
Scientific validation
Geographic data
Licensing
Privacy
Security
Deployment and infrastructure
Observability
API versioning
Status

This decision is Accepted and establishes the architectural direction for the Botanica Indica ecosystem.

Future ADRs may refine or supersede specific parts of this decision where new evidence or requirements justify doing so.
