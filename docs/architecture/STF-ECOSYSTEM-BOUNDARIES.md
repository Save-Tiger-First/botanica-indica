# Save Tiger First — Ecosystem Boundaries and Shared Infrastructure Architecture

**Document status:** Proposed — architecture baseline for review  
**Version:** 0.1  
**Scope:** Save Tiger First technology ecosystem  
**Initial domain application:** Botanica Indica  
**Related decisions:** ADR-001 through ADR-010

---

## 1. Purpose

Save Tiger First (STF) is intended to develop a technology ecosystem that can support multiple applications, initiatives and domain-specific platforms.

The ecosystem must avoid building the same foundational capabilities independently for every project.

At the same time, it must not force every project into one application, one database, one programming language, one deployment model or one set of domain rules.

This document defines the proposed boundaries between:

1. STF shared platform capabilities
2. Domain applications
3. Domain-specific data and services
4. Shared infrastructure and operational services
5. External systems and institutional integrations
6. Cross-project governance and standards

The objective is to establish reusable infrastructure while preserving the independence and integrity of each domain application.

## 2. Architectural vision

The STF ecosystem will follow a **shared-platform, multiple-domain-application model**.

Conceptually:

```text
                  SAVE TIGER FIRST
                  ECOSYSTEM GOVERNANCE
                           |
          +----------------+----------------+
          |                |                |
    Shared Platform   Shared Standards   Shared Operations
          |                |                |
          +----------------+----------------+
                           |
                 Versioned Contracts
                           |
          +----------------+----------------+
          |                |                |
     Botanica Indica   Domain App B    Domain App C
          |                |                |
    Botanical Domain   Domain B         Domain C
       Services        Services         Services
          |                |                |
    Domain Data       Domain Data      Domain Data
```

The shared platform provides reusable capabilities.

Each domain application owns its specialised knowledge, workflows, rules, records and user experiences.

The architecture must allow domain applications to evolve independently while using common services where doing so provides measurable value.

## 3. Fundamental architectural principles

### 3.1 Shared capabilities, not shared application logic

Common infrastructure should be implemented once where reuse is justified.

Domain-specific logic should remain within the domain that understands and governs it.

For example:

- Common identity management belongs to the shared platform.
- Botanical taxonomy belongs to Botanica Indica.
- Common media storage and processing may be shared.
- Botanical image interpretation belongs to the botanical domain.
- Common audit infrastructure may be shared.
- Scientific validation rules belong to the relevant domain.

### 3.2 Reuse through contracts

Domain applications should integrate with shared capabilities through documented and versioned interfaces.

They should not depend on undocumented internal implementation details.

Interfaces may include:

- HTTP APIs
- Event contracts
- SDKs
- Data exchange formats
- Authentication and authorization standards
- Shared libraries where appropriate

OpenAPI should be the preferred description format for HTTP APIs where applicable. It is language-independent and supports documentation, client generation and testing.

### 3.3 Technology independence

The ecosystem must not require every project to use the same programming language or framework.

A shared service may be implemented in TypeScript, Python, Dart or another justified technology.

Consumers should depend on stable contracts rather than implementation languages.

### 3.4 Modular implementation before distributed complexity

The architecture should begin with clearly separated modules and contracts.

A modular monolith is acceptable when it is the simplest reliable implementation.

A module should become an independently deployed service only when justified by one or more of:

- Independent scaling requirements
- Security isolation
- Different availability requirements
- Independent release lifecycle
- Separate ownership
- Distinct infrastructure requirements
- Operational or regulatory requirements
- A clear reduction in total system complexity

Microservices are not an objective in themselves.

### 3.5 Platform as a product

Shared infrastructure must be treated as a product with identifiable consumers.

Each shared capability should have:

- An owner
- A purpose
- Defined consumers
- Documented interfaces
- Support and operational expectations
- A versioning policy
- A lifecycle and deprecation policy
- A security model
- A roadmap where appropriate

A shared capability should not be created merely because it might be useful someday.

It should solve a real cross-project need or provide a justified strategic foundation.

## 4. STF shared platform responsibilities

The following are proposed shared capability domains. They represent architectural responsibilities, not a claim that these services have already been implemented.

### 4.1 Identity and access management

Potential shared capabilities:

- User identity
- Authentication
- Authorization integration
- Role and permission foundations
- Session management
- Account lifecycle
- Multi-factor authentication integration
- Service-to-service identity
- Identity audit events
- External identity provider integration

Domain applications remain responsible for defining their domain-specific roles and permissions.

For example, Botanica Indica may define botanical reviewer, taxonomic editor and observation moderator roles.

The shared identity capability should provide the mechanisms for identity and access, not decide botanical expertise.

### 4.2 Organization and membership management

Potential capabilities:

- Organization records
- Institutional membership
- Project membership
- Team and group management
- Invitations
- Membership lifecycle
- Organization-level access boundaries

Domain applications may extend these concepts with their own scientific or operational roles.

### 4.3 Media and file infrastructure

Potential capabilities:

- Secure media upload
- Object storage integration
- File metadata
- Image transformations
- Thumbnail generation
- Media processing jobs
- Virus and malware scanning where appropriate
- Access control
- Retention and deletion workflows
- Media provenance metadata
- Storage lifecycle policies

Media ownership and reuse permissions must remain associated with the originating contribution or source.

A common storage service must not imply common ownership or unrestricted reuse.

### 4.4 Geographic infrastructure

Potential shared capabilities:

- Coordinate and geometry handling
- Common geographic reference systems
- Spatial data services
- Administrative geography reference data
- Spatial API conventions
- Geographic search primitives
- Location generalisation mechanisms
- Sensitive-location access controls

Domain applications remain responsible for domain-specific geographic interpretation.

For Botanica Indica, habitat suitability, species distributions, occurrence evidence and sensitive plant locations remain botanical-domain responsibilities.

### 4.5 Search infrastructure

Potential shared capabilities:

- Search service integration
- Index lifecycle management
- Common query interfaces
- Search observability
- Search access controls
- Reusable search client libraries

Domain-specific search semantics must remain within the relevant application.

Botanical taxonomy search, scientific-name matching and plant identification candidate ranking must not be confused with generic platform search.

### 4.6 Notifications and messaging

Potential capabilities:

- Email delivery integration
- Push notification integration
- Notification templates
- Delivery status
- User notification preferences
- Retry and failure handling
- Event-driven notification workflows

Each domain application defines its own notification events and business rules.

### 4.7 Audit and activity infrastructure

Potential capabilities:

- Security audit events
- Administrative activity events
- Service activity metadata
- Traceable actor and timestamp information
- Correlation identifiers
- Audit retention mechanisms

Domain applications remain responsible for recording their scientific and business events.

For example, botanical identification changes, expert review decisions and taxonomy reconciliation history must remain meaningful to Botanica Indica.

### 4.8 Observability and operations

Potential shared capabilities:

- Centralized logs
- Metrics collection
- Distributed tracing
- Health checks
- Alerting integration
- Service dashboards
- Error reporting
- Operational audit
- Service-level monitoring

OpenTelemetry is a candidate standard for vendor-neutral telemetry instrumentation.

Operational visibility must not expose private user information or sensitive species coordinates through logs and traces.

### 4.9 API and integration infrastructure

Potential capabilities:

- API gateway integration
- API authentication
- Rate limiting
- API lifecycle management
- Versioning conventions
- External integration standards
- Service discovery where required
- Developer documentation
- API usage monitoring

The API gateway must not become a location for domain-specific business logic.

### 4.10 Configuration and secrets management

Potential capabilities:

- Centralized configuration patterns
- Secret management integration
- Credential rotation
- Environment separation
- Secure service configuration
- Access auditing

Secrets must not be stored in source code, public configuration files or ordinary data records.

### 4.11 Shared developer infrastructure

Potential capabilities:

- Repository templates
- Build and release conventions
- CI/CD templates
- Dependency and license scanning
- Security scanning
- Development environment standards
- Infrastructure provisioning templates
- Testing conventions
- API contract validation
- Documentation tooling

These capabilities should reduce duplicated engineering effort across STF projects.

## 5. Domain application responsibilities

A domain application owns its specialised domain model, rules and knowledge.

It may consume shared platform capabilities, but should not transfer its domain authority to the shared platform.

### 5.1 Botanica Indica

Botanica Indica owns botanical domain responsibilities, including:

- Taxonomic concepts and name reconciliation
- Botanical species and taxon records
- Botanical descriptions and morphology
- Plant identification workflows
- Identification candidate ranking
- Botanical evidence models
- Scientific validation
- Expert botanical review
- Plant observations
- Botanical distribution and occurrence interpretation
- Botanical source integration
- Botanical data quality
- Botanical research workflows
- Botanical-specific licensing and provenance decisions

Botanica Indica may use shared STF identity, media, geography, search, notifications, audit and observability capabilities.

It must retain authority over botanical scientific interpretation.

### 5.2 Future domain applications

Future STF applications should follow the same principle.

They should:

- Own their domain-specific data and rules.
- Use shared capabilities where appropriate.
- Avoid duplicating existing shared services.
- Avoid depending on another domain application's private implementation details.
- Integrate through documented contracts.
- Maintain their own scientific or operational governance.

A domain application should not be required to adopt irrelevant capabilities merely because another application uses them.

## 6. Data ownership and boundaries

Data ownership is a critical ecosystem boundary.

The architecture should distinguish:

1. Shared platform operational data
2. Domain application data
3. User-contributed data
4. External source data
5. Derived data
6. Shared reference data
7. Restricted and sensitive data

### 6.1 Shared platform data

Examples:

- User identity references
- Organization membership
- Shared service configuration
- Notification delivery metadata
- Security and platform audit events

The shared platform should store only the information required to provide shared capabilities.

### 6.2 Domain data

Examples for Botanica Indica:

- Taxonomic records
- Species profiles
- Observations
- Identification evidence
- Expert validation
- Botanical source records
- Scientific relationships

Domain data should not be copied into shared platform databases merely to make it appear reusable.

### 6.3 Cross-domain references

Where one domain needs to refer to another domain's information, it should use an explicit identifier or API contract.

The ecosystem should avoid direct cross-domain database access.

Where data exchange is necessary, the exchange must define:

- Data owner
- Purpose
- Permitted use
- Data format
- Version
- Attribution
- License
- Security classification
- Update expectations
- Error and removal behavior

### 6.4 Data and rights registry

STF should establish a reusable Data and Rights Registry capability.

It should record, where applicable:

- Source identity
- Rights holder
- Dataset or asset identifier
- License identifier
- License version
- Attribution requirements
- Permitted uses
- Redistribution rights
- Commercial-use permissions
- AI/ML training permissions
- Privacy restrictions
- Sensitive-data classification
- Source version
- Retrieval date
- Review status
- Approval history
- Expiry or review date

The registry should support both shared platform assets and domain-specific assets without assuming they have identical rights.

The registry may begin as a governed module or service within the existing architecture. It does not need to be a separate deployed microservice from day one.

## 7. Identity, security and authorization boundaries

The shared platform should provide common identity mechanisms and security foundations.

Domain applications should define the permissions required by their own workflows.

Authorization must be evaluated at the appropriate domain boundary.

For example:

- A user may have access to the STF ecosystem.
- The same user may be a member of Botanica Indica.
- Within Botanica Indica, the user may have observation-contributor permissions.
- A separate user may have expert-review permissions.
- Sensitive botanical records may require additional access restrictions.

Access to one domain application must not automatically imply access to another.

The ecosystem should use least privilege, secure service identities, auditable access and appropriate data isolation.

## 8. API and event boundaries

Shared and domain capabilities must communicate through explicit contracts.

### 8.1 HTTP APIs

OpenAPI should be used to describe HTTP APIs where appropriate.

API contracts should define:

- Authentication
- Authorization
- Request and response schemas
- Error formats
- Pagination
- Filtering
- Versioning
- Rate limits
- Idempotency where required
- Deprecation policy

### 8.2 Events

Events may be used for asynchronous workflows where appropriate.

Examples:

- Media uploaded
- Image processing completed
- User account updated
- Observation submitted
- Expert review completed
- Data ingestion completed
- Notification requested

Events should describe facts that have occurred, not expose private internal implementation details.

Event contracts should include:

- Event identifier
- Event type
- Version
- Producer
- Timestamp
- Correlation identifier
- Relevant entity identifier
- Schema
- Security classification

Domain applications remain responsible for interpreting their domain events.

### 8.3 Contract compatibility

The ecosystem should adopt backward-compatible changes where practical.

Breaking changes should require:

- Explicit versioning or migration strategy
- Consumer impact assessment
- Deprecation notice
- Migration guidance
- Release communication

## 9. Deployment and infrastructure boundaries

The architecture should distinguish logical ownership from deployment topology.

A shared capability does not automatically need a separate deployment.

A domain application may initially deploy several modules together while retaining clear internal boundaries.

The deployment model should evolve based on:

- Availability requirements
- Scaling requirements
- Security isolation
- Cost
- Operational complexity
- Team ownership
- Data residency
- Recovery requirements

The ecosystem should avoid premature Kubernetes adoption or mandatory microservice deployment.

Containerization and infrastructure-as-code may be introduced where they provide clear operational value.

Cloud portability should be pursued where practical, but not at the cost of unnecessary abstraction or operational burden.

## 10. Repository strategy

The initial repository strategy should favor clarity and low operational overhead.

Recommended logical separation:

- STF ecosystem governance and architecture
- Shared platform capabilities
- Domain application repositories

However, separate repositories should be created only when ownership, release lifecycle, security, licensing or deployment needs justify the split.

The Botanica Indica repository should remain the home for botanical domain architecture and implementation.

A future shared STF platform repository may be established when there is enough reusable implementation to justify it.

The ecosystem should not split every module into an independent repository prematurely.

## 11. Technology boundaries

The ecosystem should use a small, deliberate set of primary technologies without requiring uniformity.

Current intended baseline:

| Technology | Primary responsibility |
|---|---|
| TypeScript | Platform services, APIs and web applications |
| Python | AI/ML, scientific computing and data processing |
| Dart / Flutter | Mobile application |
| SQL | Relational and spatial data |
| PostgreSQL / PostGIS | Primary relational and spatial database candidate |
| JSON / OpenAPI | Interoperable API contracts |

A shared service may use a different implementation language when justified.

Consumers must depend on contracts, not language-specific internal details.

Technology decisions must be recorded and evaluated against actual requirements.

## 12. Licensing and intellectual property boundaries

The STF ecosystem must use asset-specific licensing.

The shared platform and domain applications may have different components and assets governed by different licenses.

The following must remain distinguishable:

- Shared software
- Domain software
- Documentation
- Scientific data
- Third-party datasets
- User contributions
- Photographs and media
- AI code and model weights
- Training datasets
- Trademarks

Shared infrastructure being open source does not make every dataset or domain record open.

A domain application may share software components while retaining restrictions on particular data assets.

The ecosystem must follow the approved STF Licensing and Intellectual Property Policy.

## 13. Operational ownership

Every shared capability should have a defined operational owner.

Ownership should include:

- Service purpose
- Maintainer
- Consumers
- Repository
- License
- API or contract documentation
- Deployment responsibility
- Monitoring
- Security responsibility
- Backup and recovery
- Version support
- Incident response
- Deprecation and retirement

A shared service without an owner, support expectations or lifecycle policy should not become a critical dependency.

Domain applications remain responsible for their own domain data quality, scientific integrity and user workflows.

## 14. Shared capability adoption criteria

A capability should become part of the shared platform when one or more of the following is demonstrated:

1. Multiple STF applications require substantially the same capability.
2. Centralized governance materially improves security or compliance.
3. Shared implementation reduces duplication and maintenance cost.
4. Common contracts improve interoperability.
5. The capability is sufficiently generic to avoid domain coupling.
6. There is a clear owner and sustainable operating model.

A capability should remain domain-specific when:

- Its rules are unique to one domain.
- It requires specialised scientific or operational knowledge.
- Generalization would create unnecessary complexity.
- It has no demonstrated cross-project reuse.
- Sharing it would weaken data ownership or governance.

## 15. Anti-patterns to avoid

The STF ecosystem should explicitly avoid:

- One giant application containing every domain.
- One shared database with unrestricted cross-domain table access.
- A microservice for every module from the beginning.
- Duplicating authentication and media infrastructure in every application.
- Forcing every domain to use the same programming language.
- Moving domain-specific scientific logic into generic platform services.
- Sharing user or scientific data without permission.
- Treating open-source software licensing as permission to reuse all data.
- Making one domain application dependent on another domain's private database.
- Building generic abstractions before real reuse requirements exist.
- Creating shared services without owners or operational plans.
- Making the shared platform a bottleneck for domain application development.

## 16. Implementation roadmap

### Phase 1 — Governance and boundaries

- Approve the ecosystem boundary model.
- Identify shared and domain-specific responsibilities.
- Establish architecture and licensing governance.
- Define shared service ownership.
- Establish API and event contract principles.

### Phase 2 — Foundational shared capabilities

Prioritize capabilities based on actual application requirements.

Potential early candidates:

- Identity and access foundations
- Media and file handling
- Common audit and security events
- Configuration and secrets management
- API conventions
- Observability foundations
- Data and Rights Registry foundations

### Phase 3 — Botanica Indica domain foundation

Develop botanical domain capabilities using the shared contracts where appropriate.

Potential areas:

- Taxonomy and scientific data model
- Provenance and source registry
- Observation and contribution model
- Identification and evidence architecture
- Expert validation
- Botanical geographic intelligence

### Phase 4 — Reuse validation

When another STF domain application is introduced:

- Identify which shared capabilities are genuinely reusable.
- Validate their interfaces with a second consumer.
- Improve documentation and versioning.
- Avoid adding abstractions without demonstrated value.

### Phase 5 — Ecosystem maturity

Introduce more advanced platform capabilities as justified:

- Developer self-service
- Service catalog
- Standardized deployment templates
- Shared integration tooling
- Cross-project analytics where permitted
- Automated policy and license checks
- Platform service-level objectives

## 17. Architecture governance

This document establishes proposed architectural boundaries.

Significant changes should be recorded through Architecture Decision Records.

Changes to shared contracts should include impact assessment for all known consumers.

Changes to domain ownership should be reviewed by the affected domain maintainers.

Changes to licensing, data access or sensitive-data handling should be reviewed by the appropriate governance roles.

The architecture should be reviewed periodically as the ecosystem and its applications evolve.

## 18. Success criteria

The ecosystem architecture will be considered successful when:

- Multiple STF applications can use common infrastructure without duplicating it.
- Domain applications retain control of their own domain models and rules.
- Shared services can evolve without unnecessary application rewrites.
- API and event contracts are documented and versioned.
- Data ownership and licensing remain traceable.
- Security and audit responsibilities are clear.
- Shared capabilities have operational owners.
- New applications can be added without rebuilding the foundational platform.
- The platform reduces total complexity rather than increasing it.

## 19. Final architectural position

Save Tiger First should be built as a reusable ecosystem with shared infrastructure and independently governed domain applications.

The platform should provide common capabilities, standards and operational foundations.

Domain applications should own their specialised knowledge, data, workflows and scientific or operational authority.

Reuse should be achieved through clear contracts, responsible data governance and sustainable shared services.

The architecture should remain modular, technology-independent and evolutionary.

**The goal is not to centralize everything. The goal is to share what should be shared, preserve what should remain domain-specific, and make the entire ecosystem easier to build, operate and extend.**
