# Task 04 — System Architecture & Technology Evaluation v0.1

**Document ID:** STF-BI-ARCH-004  
**Repository status:** Working baseline / source-preserving transcription for owner review  
**Source:** Project Library original DOCX; see governance overlay at end.  

> This repository transcription preserves the complete extracted source text. It is not yet an accepted architecture baseline. The original DOCX remains the preserved source artifact.

---

SAVE TIGER FIRST
STF Botanical Intelligence Platform
Task 04 — System Architecture & Technology Evaluation v0.1
Production-grade architecture baseline — modular, polyglot, reusable and cloud-portable
Decision Baseline recommendation
Architecture style Modular platform with domain-oriented services; start 
operationally simple and split services where justified
Shared STF layer
Identity, authorization, media, taxonomy, geography, 
search, audit, notifications, observability and platform 
tooling
Primary system of record PostgreSQL + PostGIS
Object/media storage S3-compatible object storage with versioning/lifecycle 
controls
Search Dedicated search layer; OpenSearch is a strong 
candidate for lexical + semantic/hybrid search
AI/ML Python-centric model/data services, independently 
deployable
Web React/Next.js candidate
Mobile React Native candidate to maximize TypeScript reuse
Observability OpenTelemetry-based, backend-agnostic
Identity OIDC/OAuth 2.0 compatible identity layer
Containerization OCI-compatible containers; Kubernetes considered for 
later scale, not mandatory on day one
Cloud strategy Cloud-neutral interfaces with one reference 
deployment
Language strategy Polyglot by domain: TypeScript + Python + SQL 
initially; add Go/Rust only where justified
1. Architecture Goals
 Support the full PRD rather than an MVP-only implementation.
 Keep the STF shared platform reusable across future conservation/biodiversity projects.
 Allow AI models, search engines, storage providers and cloud services to be replaced.
 Maintain scientific data integrity and provenance.
 Support mobile, web, expert, admin and API clients.
 Support field/offline workflows.
 Scale expensive workloads independently from ordinary application workloads.
 Provide strong observability and auditability.
 Control infrastructure cost and operational complexity.

2. Architecture Principles
 Domain boundaries before microservices: define modules and contracts first; do not create 
dozens of services prematurely.
 Polyglot where the workload benefits: TypeScript for product applications, Python for 
AI/science/data, SQL for relational and spatial data.
 PostgreSQL as the authoritative transactional data foundation unless a concrete requirement 
proves otherwise.
 Object storage for media; database stores metadata and references, not large binary payloads.
 Asynchronous processing for image analysis, model inference, indexing, notifications and long￾running jobs.
 Version everything that affects scientific reproducibility: taxonomy, source data, models, 
pipelines and important transformations.
 Treat Evidence as a domain object, not merely a UI explanation.
 Keep external integrations behind adapters.
 Prefer open protocols and standards.
 Security, privacy and observability are cross-cutting architecture concerns.
Figure 1. Logical architecture baseline. The boundaries are architectural responsibilities, not a 
commitment to one deployment topology.
3. Shared STF Platform vs Botanical Domain
Shared STF platform Botanical Intelligence domain
Identity and authentication Plant identification
Users / roles / permissions Taxonomy and species knowledge

Media storage and processing foundation Evidence Engine
Notifications Observations
Audit logging Expert/community validation
Search infrastructure Botanical geographic intelligence
Observability Botanical scientific sources
API gateway / common API conventions Botanical AI ranking and evaluation
Security controls Botanical content and curation
CI/CD and infrastructure patterns Botanical research/data pipelines
4. Domain Decomposition
Domain Responsibilities Likely implementation
Identity Accounts, sessions, authentication, 
roles
OIDC provider + platform auth 
services
Taxonomy Taxa, synonyms, authorities, 
versions
PostgreSQL domain + ingestion 
pipelines
Species Knowledge Profiles, references, structured 
botanical facts PostgreSQL + search index
Geography Locations, regions, ranges, spatial 
relations PostGIS
Media Uploads, derivatives, metadata, 
licensing Object storage + media service
Evidence Image quality, organ, morphology, 
geo/season/context signals Application service + ML services
Identification Candidate generation, ranking, 
confidence Python AI service + orchestration
Observations User field records and lifecycle PostgreSQL/PostGIS
Validation Community/expert review Application service + workflow/job 
system
Search Keyword, semantic, hybrid and 
faceted discovery OpenSearch candidate
Notifications Email/push/in-app events Event-driven service
Audit Security and governance history Append-only/event-oriented storage
5. Recommended Data Architecture
PostgreSQL + PostGIS is the leading baseline because the platform needs relational integrity, 
versioned scientific entities and substantial geospatial querying. PostGIS extends PostgreSQL with 
spatial types, indexes and functions, allowing location-aware queries to coexist with ordinary 
relational queries. citeturn1search1turn1search2
The database should hold structured metadata and authoritative relationships. Large images and 
media should live in object storage, with database records holding immutable identifiers, 
metadata, licensing/provenance and storage references.
 Transactional database: PostgreSQL.
 Spatial extension: PostGIS.
 Object/media store: S3-compatible object storage.

 Search index: separate search system when query complexity/scale justifies it.
 Analytical lake/warehouse: introduce later when operational data volume and research 
requirements justify it.
 Cache: use only for measured hot paths; avoid making cache the source of truth.
6. Media Architecture
 Direct client upload to object storage using short-lived authorized upload mechanisms.
 Store original media separately from derived thumbnails/normalized images.
 Record content hash and metadata.
 Track license/usage rights.
 Keep original media immutable where possible.
 Generate derivatives asynchronously.
 Apply lifecycle policies to temporary processing artifacts.
 Use object versioning where recovery/provenance needs justify it.
S3 documentation supports object versioning and lifecycle rules for retaining versions and 
transitioning/deleting objects according to policy; these capabilities are useful reference patterns 
even if STF ultimately uses another S3-compatible provider. citeturn0search13turn0search3
7. Search Architecture
A dedicated search layer is recommended once the product has substantial species content, 
observations and multilingual discovery needs. OpenSearch is a strong candidate because its 
current documentation supports lexical, semantic, vector, multimodal and hybrid search patterns. 
Hybrid search combines keyword and semantic retrieval through configurable scoring pipelines. 
citeturn0search2turn0search7
 Authoritative data remains in PostgreSQL.
 Search index is a derived representation.
 Use lexical search for scientific names, synonyms and exact terms.
 Use semantic/vector retrieval for natural-language exploration and knowledge discovery.
 Use hybrid ranking for queries where exact botanical terms and semantic meaning both 
matter.
 Use geospatial filters/queries where appropriate.
 Rebuild indexes from source data rather than treating the index as the system of record.
8. Identity and Authorization
Use an OpenID Connect/OAuth 2.0-compatible identity architecture. OpenID Connect is an identity 
layer on OAuth 2.0 that enables clients to verify end-user identity and obtain claims. 
citeturn1search0
 Central identity provider boundary for STF.

 Short-lived access tokens where appropriate.
 Separate authentication from application authorization.
 RBAC/ABAC-style policy layer for user, expert, curator and administrator permissions.
 MFA for privileged roles.
 Audit security-sensitive actions.
 Do not store provider credentials or secrets in application repositories.
9. API Architecture
 Public API contracts should be versioned.
 Use REST/HTTP for ordinary resource operations and asynchronous job APIs for long-running 
workflows.
 Internal service contracts should be explicit and testable.
 Use event/message patterns for asynchronous processing rather than forcing every operation 
into synchronous request chains.
 Generate machine-readable API documentation.
 Maintain compatibility policy and deprecation process.
 Use idempotency for operations that may be retried.
10. AI / ML Architecture
 Python is the recommended primary language for AI/ML, scientific pipelines and evaluation 
because it provides a broad ecosystem for machine learning and data science.
 AI inference should be isolated behind stable service contracts.
 Model registry and model-version metadata are required for reproducibility.
 Evaluation datasets must be versioned.
 Candidate generation, geographic filtering, taxonomy validation and evidence synthesis should 
be separable stages.
 Do not automatically treat user corrections as ground truth.
 Offline/on-device inference should be evaluated as a separate deployment target rather than 
assumed.
Recommended conceptual pipeline: Media Quality Check Plant/Organ Evidence Candidate → → →
Model(s) Candidate Retrieval Geographic/Taxonomic Constraints Evidence Synthesis → → → →
Ranked Result User Feedback Review/Observation. → →
11. Application Language Strategy
Layer Candidate technology Reason Decision status
Web UI TypeScript + React/Next.js
Strong React ecosystem 
and production web 
capabilities; Next.js 
describes itself as a React 
framework for full-stack 
Recommended candidate

web applications.
Mobile TypeScript + React Native
Allows substantial 
TypeScript/React sharing 
with web while producing
native mobile 
applications.
Recommended candidate
Application APIs TypeScript (Node.js) or Go
TypeScript maximizes 
ecosystem reuse; Go 
remains a strong 
alternative for high￾throughput/simple 
services.
Evaluate before freeze
AI/ML Python
Strong ML/data/scientific 
ecosystem and easy 
model integration.
Recommended
Data SQL
Best fit for relational, 
transactional and 
geospatial data.
Required
Performance-specialized 
components
Go/Rust
Use only where profiling 
or system constraints 
justify another language.
Future option
Next.js currently documents itself as a React framework for full-stack web applications. The 
architecture should treat this as a candidate rather than an irreversible commitment. 
citeturn0search1
12. Why Not One Language Everywhere?
The project has materially different workloads: user interfaces, transactional APIs, scientific/ML 
pipelines, geospatial data and infrastructure. A controlled polyglot architecture reduces the 
temptation to force every problem into one language. The trade-off is higher operational 
complexity, so the number of languages should remain deliberately small.
 TypeScript: product interfaces and potentially general application services.
 Python: AI/ML, scientific computing and data pipelines.
 SQL: data model and geospatial querying.
 Go/Rust: only when a concrete performance/operational need is demonstrated.
13. Container and Orchestration Strategy
Containerize deployable services using OCI-compatible images. Kubernetes is a powerful 
production-grade orchestration option and supports portability across on-premises, hybrid and 
public-cloud infrastructure. However, the architecture should not require a large Kubernetes 
footprint before operational scale justifies it. citeturn0search20
Stage Recommended operational posture
Local development Docker/Compose-style local environment
Early shared environments Managed container runtime or small managed 

Kubernetes where appropriate
Production growth Managed Kubernetes if service count, scale or 
portability justifies it
AI workloads Separate scalable compute pools; GPU only where 
measured benefit exists
14. Observability
Use OpenTelemetry as the instrumentation standard. OpenTelemetry is vendor/tool-agnostic and 
covers generation, collection and export of telemetry such as traces, metrics and logs. This is 
particularly useful for a polyglot system because instrumentation conventions can remain stable 
even when backend vendors change. citeturn0search0turn0search12
 Distributed traces across API evidence AI data/search flows. → → →
 Application and infrastructure metrics.
 Structured logs with correlation IDs.
 Model inference latency and error metrics.
 Identification confidence/evidence telemetry.
 Audit logs kept distinct from ordinary debug logs.
15. Event and Job Architecture
 Use a durable queue/event mechanism for media processing, AI inference, indexing, 
notifications and data ingestion.
 Events should be versioned.
 Consumers should be idempotent.
 Long-running AI jobs should expose explicit job state.
 Dead-letter/retry handling is required for production workflows.
 Avoid introducing a heavyweight event platform until actual throughput/decoupling needs 
justify it.
16. Security Architecture
 Centralized identity boundary.
 Least privilege.
 Network segmentation between public edge, application, data and AI layers.
 Secrets manager rather than environment files committed to Git.
 Encrypted transport everywhere practical.
 Private database/network endpoints.
 Signed/authorized media access.
 Input validation and malware/content checks for uploads.
 Rate limiting and abuse detection.
 Dependency and container scanning.

 Regular backup/restore tests.
17. Deployment Model
Figure 2. Reference deployment topology. Exact cloud services remain an implementation decision.
18. Technology Evaluation Matrix
Capability Leading candidate Alternatives Why candidate 
leads
Freeze?
Relational + spatial 
DB
PostgreSQL + 
PostGIS
Cloud-specific 
spatial DBs
Strong relational 
integrity + mature 
spatial capabilities
Later
Search OpenSearch
Elasticsearch, 
PostgreSQL-first 
search
Hybrid/vector 
capabilities plus 
conventional search
Later
Web React + Next.js Vue/Nuxt, SvelteKit
Large ecosystem 
and TypeScript 
alignment
Later
Mobile React Native Flutter, native 
Kotlin/Swift
High reuse with 
web TypeScript 
strategy
Later
AI/ML Python C++/Java/other ML 
runtimes
ML/data/scientific 
ecosystem
Baseline
Identity OIDC-compatible 
provider
Self-hosted/provider
alternatives
Interoperable 
identity standard Later
Observability OpenTelemetry Vendor SDKs Vendor-neutral 
instrumentation Baseline
Object storage S3-compatible Provider-specific Portable API pattern Later

object storage
and 
lifecycle/versioning 
support
Orchestration
Containers; 
Kubernetes when 
justified
Managed container 
platforms
Avoid premature 
operational 
complexity
Later
19. Architecture Risks
Risk Mitigation
Overengineering too early Start with modular boundaries; split deployment units 
when justified.
Cloud lock-in Use open interfaces, portable data formats and 
adapters.
Taxonomy inconsistency Central taxonomy service + versioned source 
mappings.
AI overconfidence Evidence Engine + uncertainty states + evaluation 
gates.
Search drift Treat indexes as derived; rebuild from source.
Media cost growth Lifecycle rules, deduplication and storage classes.
Expert bottleneck Prioritized review queues and confidence-based 
routing.
Privacy/location exposure Granular location controls and privacy-aware defaults.
Polyglot complexity Keep initial language set small and establish 
coding/contract standards.
20. Architecture Decision Records to Create
 ADR-001 — Repository and organization strategy.
 ADR-002 — Authentication and authorization architecture.
 ADR-003 — Taxonomy source and reconciliation strategy.
 ADR-004 — PostgreSQL/PostGIS as system of record.
 ADR-005 — Media/object storage architecture.
 ADR-006 — Search architecture.
 ADR-007 — AI/ML service boundary and model lifecycle.
 ADR-008 — API versioning and service contract strategy.
 ADR-009 — Observability standard.
 ADR-010 — Deployment/orchestration strategy.
 ADR-011 — Data provenance and scientific versioning.
 ADR-012 — Offline/mobile synchronization strategy.
21. Architecture Freeze Gates
 PRD requirements are accepted or explicitly deferred.
 Taxonomy authorities and licensing assumptions are documented.

 Data ownership/licensing/training rights are understood.
 Security and privacy threat model is completed.
 Representative AI evaluation dataset is defined.
 Initial cost model is reviewed.
 API boundaries and core data model are stable enough for implementation.
 Architecture decisions are recorded as ADRs.
 UX/wireframe flows are sufficiently specified to validate API and domain assumptions.
22. Recommended Implementation Sequence After Task 04
1. Finalize architecture ADRs and repository structure.
2. Establish STF shared platform foundation.
3. Implement identity, authorization, audit and developer environments.
4. Implement core taxonomy/data model and ingestion pipeline.
5. Implement media pipeline.
6. Implement Evidence Engine baseline.
7. Build AI evaluation harness before committing to a production model.
8. Build identification API and user workflow.
9. Build species knowledge/search.
10. Build observations and review workflows.
11. Build mobile/web/expert/admin interfaces.
12. Run scientific validation and field testing.
13. Harden security, performance, observability and operations.
14. Prepare production deployment and governance.
23. Current Technology Research Notes
This task uses current public documentation as a technology sanity check. Key sources include 
PostgreSQL/PostGIS, OpenSearch, OpenTelemetry, Kubernetes, OpenID Foundation, AWS S3 
documentation and Next.js documentation. The sources support the capabilities described above; 
they do not by themselves constitute a final STF vendor selection.
 PostGIS official documentation: spatial types, spatial indexes and spatial processing integrated 
with PostgreSQL. citeturn1search1
 OpenSearch documentation: vector search, semantic search and hybrid search. 
citeturn0search2turn0search7
 OpenTelemetry documentation: vendor-neutral telemetry instrumentation and collection. 
citeturn0search0turn0search12
 Kubernetes official site: container orchestration and portability across infrastructure 
environments. citeturn0search20
 OpenID Connect Core: interoperable identity layer over OAuth 2.0. citeturn1search0

 Amazon S3 documentation: object versioning and lifecycle management. 
citeturn0search13turn0search3
 Next.js documentation: React-based full-stack web application framework. citeturn0search1
24. Task 04 Decision
Adopt a modular, domain-oriented, deliberately polyglot architecture with PostgreSQL/PostGIS at 
the transactional/spatial core, object storage for media, a replaceable search layer, Python-centric 
AI/ML services, standards-based identity, OpenTelemetry-based observability and containerized 
deployment. Keep cloud/provider choices and detailed service decomposition open until cost, scale,
security and operational requirements are evaluated.


---

# Repository governance and decision-alignment overlay

**Overlay date:** 20 November 2026  
**Overlay status:** Proposed alignment notes; not a retroactive alteration of source v0.1  
**Governing references:** AI Project Operating Prompt STF-AI-OPS-001; accepted ADR-001 through ADR-010; proposed Full Product Vision and Capability Blueprint in PR #17.

## Source preservation

This repository document is a text transcription of the complete extracted text of the original Project Library source:

- **Original filename:** `STF_Task_04_System_Architecture_and_Technology_Evaluation_v0.1.docx`
- **Library path:** `/STF app/`
- **Library file ID:** `libfile_79fbbfd739fc81918ef8543727931b96`
- **Original extent:** 11 pages; 431 extracted text lines
- **Source version:** v0.1; working baseline

The original DOCX remains the preserved source artifact. This Markdown transcription retains the source's substantive text; page layout, embedded diagrams and table geometry may be simplified by text extraction. Any future editorial or substantive change must be recorded separately and must not be presented as part of the original v0.1.

## Current accepted-decision alignment

The source document's technology matrix is an evaluation and candidate recommendation. It is not, by itself, an accepted vendor, framework, deployment or procurement decision.

| Topic | Current governing position | Interpretation of Task 04 v0.1 |
|---|---|---|
| Mobile framework | **ADR-001: Dart / Flutter** | React Native is a historical, unselected candidate. It does not supersede Flutter. |
| Architecture decomposition | **ADR-002: modular architecture** | Domain boundaries are logical ownership boundaries. Do not infer one microservice or deployment per domain. |
| Platform interfaces | **ADR-003: API-first architecture** | Versioned contracts and multiple clients remain governing principles. |
| Scientific provenance | **ADR-004: provenance-aware data architecture** | Source, version, transformation, rights and validation context must be retained. |
| Taxonomy | **ADR-005: source-aware, versioned reconciliation** | No single source or treatment should silently overwrite competing taxonomic assertions. |
| Identification | **ADR-006: modular evidence-aware pipeline** | Candidate generation, contextual signals, taxonomy, evidence and validation remain distinct stages. |
| Evidence and expert review | **ADR-007: distinct but interconnected capabilities** | Evidence and expert assessment must not overwrite observations or identification history. |
| Geography | **ADR-008: geospatial context and sensitive-location protection** | Precise location is not automatically public; geographic uncertainty and access controls are required. |
| Observations | **ADR-009: observation as a first-class scientific record** | Observation, identification and contribution remain distinct records. |
| Ingestion | **ADR-010: source-aware, provenance-preserving integration** | External data remains attributable and subject to rights and source-specific limitations. |

## Historical ADR numbering in source Section 20

The ADR-001 through ADR-012 list in the original Task 04 document conflicts with the accepted repository ADR register. It is preserved above as historical source text only. It is **not** an instruction to create or renumber ADRs. The current repository ADR identities and subjects govern. Future ADR identifiers must be assigned only after checking the live repository inventory.

## Technology candidates that remain open

The following are candidates or patterns, not finalized provider selections merely because they appear in Task 04:

- PostgreSQL/PostGIS as the leading relational/spatial foundation; physical schema design remains gated by scientific-model reconciliation and review.
- OpenSearch or alternative search architecture; benchmark with representative botanical, multilingual, geographic and cost workloads.
- S3-compatible object storage; provider, lifecycle, retention, rights and recovery design remain open.
- OIDC/OAuth-compatible identity; identity provider and detailed authorization policy remain open.
- TypeScript/Node.js versus Go for application services; evaluate against team capability, operational complexity and measured workload.
- React/Next.js for web; candidate, not accepted framework selection.
- Queue/event infrastructure, container platform, cloud provider and orchestration; select only after requirements, threat model, cost and operating capability are assessed.
- OpenTelemetry is a strong standards-aligned instrumentation direction, but the telemetry backend and operational model remain open.

The accepted modular architecture and the operating prompt's avoid-premature-complexity guardrails take precedence over any interpretation that would require immediate microservices, Kubernetes, multiple databases or a dedicated vector database.

## Scientific-data and physical-design gate

Task 04's architecture sequence must be read together with the current Task 05 scientific data model review. DR-01 through DR-12 and LDM-01 through LDM-16 remain review findings and test scenarios, not automatically closed by this transcription. Task 05E / physical database design remains **NOT READY** until the required model reconciliation, reproducible validation evidence, qualified discipline review and owner authorization are complete.

## Relationship to the full-product blueprint

The Full Product Vision and Capability Blueprint in PR #17 is a higher-level proposed product reference. It does not replace this architecture evaluation or amend accepted ADRs. The canonical architecture baseline should eventually contain a reconciled current architecture view, with historical candidate material preserved and decision status explicit.

**Status:** Working baseline / transcription for owner review. Not an accepted architecture baseline, vendor selection, procurement approval or implementation authorization.

