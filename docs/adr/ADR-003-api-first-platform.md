# ADR-003: API-First Platform Architecture

- **Status:** Accepted
- **Date:** 2026-09-22
- **Decision Type:** Architecture
- **Scope:** Botanica Indica platform and ecosystem

## Context

Botanica Indica is intended to support multiple applications and users over time.

Potential clients include:

- Mobile applications
- Web applications
- Administrative interfaces
- Scientific and research interfaces
- Institutional integrations
- Future third-party applications

The ecosystem contains shared capabilities such as:

- Taxonomic information
- Plant identification
- Observations
- Scientific evidence
- Geographic information
- Expert validation
- User accounts
- Search
- Data ingestion
- AI/ML capabilities

If these capabilities are implemented independently inside each application, the ecosystem may develop duplicated business logic, inconsistent data, different scientific interpretations, and unnecessary maintenance requirements.

A shared platform layer is therefore required.

## Decision

Botanica Indica will follow an **API-first platform architecture**.

Core platform capabilities will be exposed through documented interfaces that can be consumed by multiple clients.

The intended architectural relationship is:

```text
                    ┌─────────────────────┐
                    │    Mobile Client    │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │                     │
                    │    Platform APIs    │
                    │                     │
                    └──────────┬──────────┘
                               │
       ┌───────────────────────┼────────────────────────┐
       │                       │                        │
┌──────▼──────┐       ┌────────▼────────┐      ┌────────▼────────┐
│   Taxonomy  │       │ Identification  │      │    Evidence     │
└─────────────┘       └─────────────────┘      └─────────────────┘
       │                       │                        │
       └───────────────────────┼────────────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │ Shared Platform     │
                    │ Infrastructure      │
                    └─────────────────────┘

Other clients may consume the same APIs:

Mobile
   │
Web
   │
Research Tools
   │
Institutional Integrations
   │
Administrative Interfaces
   │
Future Applications
   │
   ▼
Platform APIs
   │
   ▼
Botanica Indica Domain Modules
API as a Product Boundary

The API is not merely an implementation detail of the backend.

The API represents a stable boundary between the platform and its clients.

API design should therefore consider:

Consistency
Discoverability
Versioning
Security
Backward compatibility
Error handling
Documentation
Performance
Rate limiting
Observability

API contracts should be treated as first-class project artifacts.

Contract-First Principle

Where practical, important APIs should be designed as explicit contracts before implementation.

The project should use documented schemas and interfaces.

OpenAPI should be used for HTTP API contracts where appropriate.

A simplified example:

Client
  ↓
HTTP Request
  ↓
API Contract
  ↓
Platform Module
  ↓
Domain Logic
  ↓
Data / External Services
  ↓
API Response
  ↓
Client

The API contract should define the expected structure of requests and responses without exposing internal implementation details.

Client Independence

Clients should not depend directly on internal backend implementation details.

For example, a mobile application should not require knowledge of:

Database tables
Internal ORM models
Internal service classes
Internal filesystem structure
Internal AI model implementation
External provider-specific APIs

Instead, the client should communicate through stable platform interfaces.

Shared Business Logic

Core business and scientific logic should reside within the platform rather than being independently reimplemented in each client.

For example, taxonomic resolution should not have one implementation in the mobile application and another implementation in the web application.

Instead:

Mobile ──────┐
             │
Web ─────────┤
             │
Research ────┤
             ▼
       Taxonomy API
             │
             ▼
       Taxonomy Module

This reduces the possibility of inconsistent results between applications.

API Domains

The platform API will eventually expose capabilities corresponding to the major logical modules.

Potential API domains include:

Authentication
Users
Taxonomy
Identification
Observations
Evidence
Geography
Expert review
Community
Search
Data ingestion
AI/ML
Administration

These domains do not necessarily imply separate services.

They represent logical API boundaries.

API Versioning

Public or externally consumed APIs must support a controlled versioning strategy.

Changes should be classified according to their compatibility impact.

Examples:

Backward-compatible changes

Potentially include:

Adding optional response fields
Adding new endpoints
Adding optional request fields
Adding new supported query parameters where existing behavior remains valid
Breaking changes

May include:

Removing endpoints
Removing required fields
Changing the meaning of an existing field
Changing response structures incompatibly
Changing authentication requirements incompatibly

Breaking changes require deliberate versioning and migration planning.

Internal and External APIs

Not every internal interface needs to be exposed publicly.

The platform may distinguish between:

Internal module interfaces
Internal platform APIs
Authenticated public APIs
Public read APIs
Institutional or partner APIs

Access levels should be determined by security, privacy, scientific, operational, and product requirements.

Authentication and Authorization

API access must use explicit authentication and authorization mechanisms where required.

Authentication establishes who or what is accessing the platform.

Authorization determines what that identity is permitted to do.

The API architecture must not assume that authentication alone provides authorization.

Permissions should be associated with clearly defined roles, capabilities, or policies.

Security

APIs must be designed with security as a core architectural requirement.

Relevant considerations include:

Input validation
Authentication
Authorization
Rate limiting
Abuse prevention
Secure credential handling
Secure token handling
Audit logging
Error handling
Data privacy
Sensitive geographic information

Secrets must never be embedded in source code or API responses.

Error Handling

APIs should return predictable and documented error structures.

Errors should provide enough information for clients to respond appropriately without exposing sensitive internal implementation details.

A consistent error model should eventually be defined for the platform.

Pagination and Querying

Collection endpoints should use consistent pagination and querying conventions.

Examples include:

Observations
Species
Evidence records
Search results
Contributions

The exact pagination strategy will be documented separately as the API specification develops.

Geographic Queries

Because botanical information is strongly associated with geography, the API architecture must support spatial operations where required.

Potential capabilities include:

Coordinate-based queries
Bounding-box queries
Administrative-region queries
Ecological-region queries
Distribution queries

Geographic APIs must consider privacy and protection of sensitive species locations.

Scientific Provenance

API responses involving scientific or externally sourced information should preserve appropriate provenance.

Where applicable, responses should allow clients to distinguish:

Source
Taxonomic authority
Data origin
Version
Evidence
AI-generated information
User contribution
Expert validation

The API should not obscure important uncertainty or provenance information merely for presentation convenience.

AI/ML APIs

AI/ML capabilities should be exposed through stable interfaces rather than forcing clients to depend on a specific model.

For example:

Image
  ↓
Identification API
  ↓
Identification Service
  ↓
Model Adapter
  ↓
Model
  ↓
Candidate Results

A model may be replaced without requiring clients to change their fundamental identification workflow.

AI-generated results should remain distinguishable from expert or scientifically verified results.

External Provider Isolation

External services and biodiversity data providers should generally be accessed through platform-side adapters or ingestion mechanisms.

Clients should not directly depend on external provider APIs when the platform is intended to provide the capability itself.

For example:

             ┌──────────────┐
             │ External     │
             │ Data Source  │
             └──────┬───────┘
                    │
              Provider Adapter
                    │
                    ▼
             Platform Model
                    │
                    ▼
                Platform API
                    │
                    ▼
                 Clients

This reduces client coupling to external providers.

Data Transfer Formats

JSON will generally be used for standard API request and response payloads unless another format provides a clear technical benefit.

Other formats may be used when appropriate, including:

GeoJSON for geographic information
CSV for suitable data exchange
Parquet for large analytical datasets
Binary formats where performance requirements justify them

The choice should be documented for each major interface.

API Documentation

API documentation should be maintained as part of the project.

Documentation should eventually cover:

Endpoint definitions
Request parameters
Request schemas
Response schemas
Authentication requirements
Authorization requirements
Error responses
Examples
Rate limits
Versioning
Deprecation policies

OpenAPI specifications should be version controlled alongside the relevant implementation.

Testing

APIs should be tested at multiple levels.

Relevant testing includes:

Unit tests
Integration tests
API contract tests
Authentication tests
Authorization tests
Validation tests
Error handling tests
Performance tests
Security tests
End-to-end tests

Contract tests should help ensure that clients and platform implementations remain compatible.

Observability

API requests should support appropriate observability.

Depending on the deployment architecture, this may include:

Request identifiers
Structured logs
Metrics
Latency measurements
Error rates
Tracing
Audit records

Sensitive information must not be unnecessarily included in logs.

Rate Limiting

Public and externally accessible APIs may require rate limiting.

Rate limits should be designed according to:

Resource cost
Abuse risk
User type
Authentication state
Endpoint sensitivity
Scientific or operational requirements

The exact limits will be established later as usage patterns become known.

Caching

Caching may be used where appropriate to improve performance and reduce unnecessary computation or external requests.

Caching must not compromise:

Scientific correctness
Data freshness requirements
Taxonomic versioning
User privacy
Authorization
Provenance

Cache invalidation and versioning strategies should be documented where caching affects correctness.

Consequences
Positive consequences

This decision provides:

One shared platform for multiple clients
Reduced duplication of business logic
Consistent scientific and taxonomic behavior
Easier development of mobile and web applications
Easier institutional integration
Greater technology independence
Clearer separation between clients and backend implementation
Better long-term maintainability
Ability to evolve clients independently of backend implementation
Negative consequences

This approach requires:

Careful API design
API documentation
Contract management
Versioning discipline
Compatibility testing
Security controls
Additional development effort before some client features can be implemented

Poorly designed APIs can become long-term constraints, so API design decisions should be treated carefully.

Consequences for Development

Platform capabilities should generally be developed as reusable services behind documented interfaces.

Client-specific presentation logic should remain in the relevant client.

For example:

Platform
  → Identifies candidate species

Mobile
  → Presents candidate species to the user

Web
  → Presents candidate species through the web interface

Research Interface
  → Presents candidate species with scientific context

The underlying identification capability remains shared.

Relationship to Other ADRs

This decision depends on and extends:

ADR-001: Architecture Principles and Technology Independence
ADR-002: Modular Architecture

Future ADRs should define:

API technology and framework
API schema conventions
Authentication architecture
Authorization architecture
API versioning strategy
Event contracts
Data contracts
Search API
Identification API
Taxonomy API
External integration architecture
Status

This decision is Accepted.

The exact API technology, endpoint structure, schemas, and implementation details will be established through subsequent architectural decisions and API specifications.
