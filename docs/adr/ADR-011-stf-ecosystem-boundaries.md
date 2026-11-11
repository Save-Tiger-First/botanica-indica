# ADR-011: Save Tiger First Ecosystem Boundaries and Shared Platform

- **Status:** Proposed
- **Date:** 2026-11-11
- **Decision Type:** Architecture / Governance
- **Scope:** Save Tiger First technology ecosystem and all current/future STF domain applications
- **Related document:** `docs/architecture/STF-ECOSYSTEM-BOUNDARIES.md`
- **Related ADRs:** ADR-001, ADR-002, ADR-003, ADR-004, ADR-008, ADR-009, ADR-010

---

## 1. Context

Save Tiger First (STF) intends to develop more than one technology-enabled domain application. Botanica Indica is the first domain application and the initial proving ground for reusable platform capabilities.

If every application independently builds identity, media handling, authorization, audit, notifications, observability and integration infrastructure, STF risks duplicating work and creating inconsistent security and operational practices.

However, centralizing every capability, data model and workflow into a single generic platform would create a different problem: domain knowledge and domain-specific authority could be diluted, shared services could become bottlenecks, and future applications could be forced into abstractions that do not fit their needs.

The architecture therefore needs explicit boundaries between:

1. STF-wide shared platform capabilities.
2. Domain-specific applications and their domain services.
3. External systems and data providers.
4. Cross-domain integrations and shared reference capabilities.

The existing architecture direction in ADR-001 and ADR-002 already establishes modularity, technology independence, contract-driven integration and a preference for a modular monolith before premature service distribution. This ADR extends those principles from the Botanica Indica ecosystem to the wider STF ecosystem.

The companion architecture document describes the proposed logical boundaries and implementation roadmap. This ADR records the governing decision and its consequences.

## 2. Decision

STF will use a **federated ecosystem architecture** consisting of:

- A set of reusable, independently governed shared platform capabilities.
- Multiple domain applications, each responsible for its own domain model, business rules, specialist workflows and domain authority.
- Explicit, versioned contracts for communication and controlled data sharing.
- Common governance principles for security, privacy, licensing, provenance, auditability and operational responsibility.

The shared platform will be built and operated as an internal product for STF domain application teams, not as a central authority that owns every domain capability.

**Shared infrastructure is reusable; domain knowledge and authority remain with the domain application that owns them.**

This is a logical ownership and contract model. It does not require every shared capability or domain module to run as a separate microservice, use a separate repository, or use a single programming language.

## 3. Architectural model

The ecosystem is organized conceptually as:

```text
                  Save Tiger First (STF)
                           |
             Shared Platform Capabilities
                           |
          +----------------+----------------+
          |                |                |
    Botanica Indica   Domain App B     Future Domain App C
          |                |                |
    Botanical domain   Domain B         Domain C
    services/data      services/data    services/data
          |                |                |
          +-------- Contracted integrations --------+
                           |
                 External systems and sources
```

This diagram describes logical relationships and ownership, not a mandatory deployment topology.

### 3.1 Shared platform

The shared platform may provide capabilities such as:

- Identity integration and authentication foundations
- Common authorization primitives and policy enforcement mechanisms
- Organization, membership and account lifecycle capabilities where genuinely reusable
- Media and file storage abstractions
- Common geographic primitives and spatial infrastructure
- Search infrastructure and indexing capabilities
- Notification delivery infrastructure
- Audit events and security event foundations
- API conventions, gateway or edge capabilities where justified
- Event and integration infrastructure
- Configuration and secrets-management patterns
- Observability, logging, metrics and tracing foundations
- CI/CD templates, developer tooling and operational conventions
- Data and Rights Registry infrastructure or shared governance tooling, when justified by more than one consumer

A capability is not automatically shared merely because two applications have a superficially similar feature. Its responsibilities, data sensitivity, legal basis, lifecycle and operational needs must be evaluated before common ownership is assigned.

### 3.2 Domain applications

Each domain application owns its specialist knowledge and workflows.

For Botanica Indica, domain ownership includes:

- Botanical taxonomy and taxonomic concepts
- Accepted names, synonyms and taxonomic treatments
- Botanical knowledge and species profiles
- Plant identification workflows and candidate ranking
- Botanical evidence and scientific interpretation
- Plant observations and associated field evidence
- Botanical occurrence and distribution interpretation
- Expert botanical review and validation
- Botanical source reconciliation and scientific governance

Future STF applications should similarly retain their own domain-specific models, policies and authorities.

### 3.3 External systems

External data providers, scientific institutions, identity providers, cloud services and other external systems remain external dependencies.

They must be integrated through explicit interfaces and source-specific agreements. Their data, terms and availability must not be assumed to be controlled by STF.

## 4. Data ownership and access boundaries

The shared platform must not become a universal data warehouse with unrestricted access by all STF applications.

Data should be classified by ownership and purpose, for example:

1. **Shared operational data:** platform account, service configuration, delivery metadata and common audit events.
2. **Domain data:** data owned by a particular application, such as botanical taxonomic and observation records.
3. **User-contributed data:** submissions whose rights, privacy, retention and permitted uses are governed by explicit contribution terms.
4. **External-source data:** material governed by upstream licenses, contracts and access terms.
5. **Derived data:** information produced through transformations, aggregation, reconciliation, indexing or model processing, with source lineage retained.
6. **Shared reference data:** genuinely common reference data with an identified owner, source and reuse policy.
7. **Restricted or sensitive data:** data subject to privacy, security, conservation, contractual or other access restrictions.

### 4.1 Domain data ownership

A domain application is the authoritative owner of its domain model and business rules. Other applications should consume permitted information through published contracts or approved exports rather than querying or modifying the owning application's private database.

### 4.2 Shared data does not mean unrestricted data

A shared service may provide common storage, identity or search infrastructure without granting every application permission to read every record.

Authorization must be enforced at the appropriate resource, tenant, domain and purpose boundary. Sensitive data access must be limited, logged and reviewable.

### 4.3 Cross-domain references

Where one domain application needs to refer to another domain's record, it should use a stable identifier and an authorized API or event contract.

Cross-domain references must not create implicit ownership transfer, license transfer or unrestricted data access.

## 5. Contracts and integration

Cross-boundary communication must use documented and versioned contracts.

### 5.1 Synchronous interfaces

HTTP APIs should use documented contracts. OpenAPI is the preferred candidate for describing HTTP APIs because it is programming-language independent and supports tooling for discovery, client generation, testing and governance.

The exact OpenAPI version and tooling should be selected when API implementation begins, based on current tool support and compatibility requirements.

### 5.2 Asynchronous interfaces

Events and messages should use explicit schemas and documented semantics, including:
- Event identity and type
- Producer and owning domain
- Schema version
- Event occurrence time
- Correlation and causation identifiers where needed
- Data classification and access constraints
- Delivery, retry and idempotency expectations
- Compatibility and deprecation policy

Events should communicate facts or requests with clear ownership. They must not become an undocumented alternative database interface.

### 5.3 Contract governance

A contract change must identify known consumers, compatibility impact, migration path and deprecation timeline. Breaking changes require explicit versioning or a coordinated migration.

Contracts should avoid exposing internal database schemas or framework-specific implementation details.

## 6. Deployment and repository strategy

Logical separation does not require immediate physical distribution.

### 6.1 Initial deployment approach

STF should begin with modular applications and a modular monolith where that is the simplest reliable implementation. Components may share infrastructure while retaining clear module ownership, interfaces and data boundaries.

A shared capability may initially be a well-defined module, library or managed external service. It need not be independently deployed before there is a demonstrated need.

### 6.2 Service extraction criteria

A capability may be extracted into an independently deployed service when evidence supports one or more of the following:
- Independent scaling or resource isolation
- Independent deployment cadence
- Strong security or fault-isolation requirements
- Distinct availability or reliability objectives
- Clear operational ownership and support capacity
- A stable contract and well-understood domain boundary
- A material benefit that outweighs distributed-system complexity

The existence of a separate logical module alone is not sufficient reason to create a microservice.

### 6.3 Repository strategy

STF should not split the current Botanica Indica repository into multiple repositories solely to reflect the conceptual platform/domain split.

Repository boundaries should be decided when there are concrete needs involving ownership, access control, release cadence, dependency management, compliance or independent contribution.

A future shared-platform repository may be justified when shared code is actually reused by multiple applications and has clear maintainers, versioning, compatibility and release practices.

## 7. Shared capability lifecycle and ownership

Every shared capability adopted as a supported platform offering must have:

- A named accountable owner or maintainer role
- A defined set of consumers and supported use cases
- A documented interface and onboarding guidance
- Security, privacy and data-classification expectations
- Operational responsibility and escalation route appropriate to its criticality
- Versioning and compatibility policy
- A maintenance and upgrade approach
- A deprecation and exit plan
- A way to collect consumer feedback and measure usefulness

A capability without a maintainer, support model or lifecycle plan must not be represented as a production-ready shared service.

STF should treat the platform as a product: discoverability, usability, documentation, reliability and consumer experience matter as much as technical implementation.

## 8. Shared capability adoption criteria

A domain application may propose a capability for shared adoption. The proposal should answer:

1. What repeated problem does the capability solve?
2. Which current applications need it?
3. What is genuinely common and what remains domain-specific?
4. Is there a stable contract and clear data owner?
5. What are the security, privacy, licensing and operational implications?
6. What are the costs of sharing versus keeping it local?
7. Who will maintain and support it?
8. How will adoption and value be measured?
9. What is the migration or exit path if the shared service is unsuitable?

Prefer a small number of proven shared capabilities over a large catalogue of speculative abstractions.

The first proving ground should be Botanica Indica. Reuse should be validated with a second real STF application before broad generalization wherever practical.

## 9. Technology principles

The ecosystem remains technology-independent as established by ADR-001.

Current intended technology roles remain:
- TypeScript for suitable platform, API and application services
- Python for AI/ML and scientific computing
- Dart/Flutter for mobile applications, subject to the existing ADR-001 decision and future evidence
- PostgreSQL/PostGIS for relational and spatial data where appropriate
- JSON and OpenAPI for HTTP contracts
- Explicit schema formats for asynchronous integration

These are current preferences, not a mandate that every shared service use the same stack. Technology selection should consider interoperability, maintainability, team capability, operational cost, security and reversibility.

No framework, cloud provider, database, identity vendor, search engine or AI provider is mandated by this ADR.

## 10. Security, privacy, licensing and scientific governance

Shared platform services must provide appropriate common mechanisms, but each domain application remains accountable for applying domain-specific rules.

The architecture must preserve:
- Least-privilege access and separation of duties
- Tenant and domain isolation where applicable
- Data minimization and purpose limitation
- Auditability for sensitive actions
- Appropriate retention, deletion and correction workflows
- Source and data provenance
- Asset-specific licensing and attribution
- Explicit permissions for redistribution and AI/ML training
- Protection of sensitive conservation and species-location information
- Clear distinction between AI-generated inference and validated domain information

A shared identity service does not decide whether a user is a qualified botanical expert. The Botanica Indica domain must own domain-specific expert qualifications, review assignments and scientific validation rules.

A shared data registry does not automatically grant permission to use the registered data. Rights and access decisions must be enforced by the relevant application and workflow.

## 11. Alternatives considered

### Alternative A — Every application builds all infrastructure independently

**Advantages**
- Maximum local autonomy
- No central platform dependency
- Simple ownership within each application

**Disadvantages**
- Duplicated engineering and operational work
- Inconsistent security, identity and audit practices
- Divergent integrations and developer experience
- Higher long-term maintenance burden

**Reason not selected:** It does not support STF's stated goal of reusable infrastructure across multiple applications.

### Alternative B — One centralized application and database for all STF domains

**Advantages**
- Centralized operations
- Potentially shared data and user experiences
- Fewer deployment units initially

**Disadvantages**
- Domain boundaries become difficult to enforce
- Domain-specific workflows and data models become coupled
- One application's changes may affect unrelated applications
- Shared database access can bypass ownership and security boundaries
- Central platform becomes a delivery bottleneck

**Reason not selected:** It centralizes domain authority and creates unnecessary coupling.

### Alternative C — Microservices for every shared and domain capability from the beginning

**Advantages**
- Independent deployment and scaling in theory
- Technology diversity
- Potentially strong runtime isolation

**Disadvantages**
- Distributed-system complexity before boundaries are proven
- More infrastructure, monitoring, security and deployment work
- Network and data consistency challenges
- Higher operational demands for a small or early-stage ecosystem

**Reason not selected:** ADR-001 and ADR-002 already favor modularity and evidence-based service extraction.

### Alternative D — Federated ecosystem with shared capabilities and domain-owned applications

**Advantages**
- Reuse without erasing domain ownership
- Independent domain evolution
- Clear data and contract boundaries
- Incremental implementation
- Supports different technologies where justified

**Disadvantages**
- Requires explicit governance and ownership
- Cross-domain integration needs careful design
- Shared services can become bottlenecks if not managed as products
- Requires lifecycle, support and compatibility discipline

**Reason selected:** Best alignment with STF's multi-application strategy while preserving domain autonomy and incremental delivery.

## 12. Consequences

### Positive consequences

- Reusable capabilities can reduce duplication across STF applications.
- Domain-specific data, workflows and authority remain protected.
- Cross-domain integration becomes more explicit and auditable.
- Platform services can evolve independently when justified.
- The ecosystem can grow without forcing all applications into one technology stack.
- Governance for licensing, security and data access becomes clearer.

### Negative consequences and trade-offs

- Requires ongoing architecture and platform governance.
- Contract design and compatibility add work.
- Shared capability ownership and operational support must be funded or explicitly assigned.
- Cross-domain data access requires additional design and authorization.
- Some capabilities may remain duplicated until common requirements are proven.
- A platform that is too generic or centrally controlled can slow domain delivery.

STF accepts these trade-offs but will prioritize proven reuse, clear ownership and sustainable operations over speculative platform breadth.

## 13. Implementation guidance

The recommended order is:

### Phase 1 — Establish governance
- Approve this ADR and the companion ecosystem boundary document.
- Identify maintainers and decision rights for shared and domain capabilities.
- Establish security, licensing, contribution and data-governance policies.
- Maintain an inventory of proposed shared capabilities and their consumers.

### Phase 2 — Build only the foundations Botanica Indica needs
- Define domain boundaries and data ownership.
- Establish identity and authorization integration requirements.
- Establish media, audit, observability and configuration patterns where needed.
- Design the Data and Rights Registry as a governed capability.
- Document API and event contract conventions.

### Phase 3 — Validate operational use
- Implement capabilities within a modular architecture.
- Measure whether they reduce duplication and delivery effort.
- Review consumer experience, reliability and maintenance burden.
- Extract services only when justified by observed requirements.

### Phase 4 — Validate reuse with another STF application
- Identify which capabilities are genuinely reusable.
- Test contracts and onboarding with a second consumer.
- Revise abstractions based on actual use rather than hypothetical future requirements.

## 14. Open decisions not resolved by this ADR

This ADR does not select or finalize:
- Cloud provider or hosting topology
- Identity provider or full authorization product
- API gateway or event broker
- Exact service deployment boundaries
- Shared platform repository structure
- Multi-tenancy implementation model
- Data residency and backup strategy
- Service-level objectives or support hours
- Organization-wide staffing and funding model
- Exact licensing terms for every asset class

These require separate requirements, evaluation and ADRs when implementation decisions are imminent.

## 15. Acceptance criteria for this decision

This decision can be considered implemented progressively when:

- Shared and domain-specific responsibilities are documented.
- Each domain application has a named owner for its domain data and rules.
- Shared capabilities have maintainers and lifecycle plans.
- Cross-domain access uses documented, authorized contracts.
- Sensitive and licensed data are protected by purpose-aware controls.
- Platform capabilities have consumer-facing documentation.
- Service extraction is justified by evidence rather than fashion.
- A second STF application validates the shared capabilities before broad ecosystem standardization.

## 16. References

- CNCF TAG App Delivery, **Platform Engineering Maturity Model**: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/
- CNCF TAG App Delivery, **Platforms White Paper**: https://tag-app-delivery.cncf.io/whitepapers/platforms/
- OpenAPI Initiative, **OpenAPI Specification v3.2.1**: https://spec.openapis.org/oas/v3.2.1.html
- Existing project decisions: ADR-001 and ADR-002.
- Companion project document: `docs/architecture/STF-ECOSYSTEM-BOUNDARIES.md`

---

## 17. Decision status

This ADR is **Proposed**. It should be reviewed against the companion architecture document, the current repository governance model and the actual capacity of STF to own and operate shared services.

It should be marked **Accepted** only after maintainer review and explicit approval. Acceptance does not mean every capability listed above must be implemented immediately.
