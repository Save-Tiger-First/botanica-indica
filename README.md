# botanica-indica
India's botanical knowledge is distributed across many scientific databases, floras, observation platforms and institutional resources.
# Botanica Indica

**An India-first Botanical Intelligence Platform**

Botanica Indica is a Save Tiger First (STF) initiative to build a scientifically grounded, technology-enabled platform for understanding, identifying, documenting and exploring the botanical diversity of India.

India's botanical knowledge is distributed across scientific databases, floras, institutional publications, observation platforms, research collections and local knowledge systems. These resources differ in coverage, structure, taxonomy, accessibility, provenance and licensing.

Botanica Indica aims to connect and make responsible use of this knowledge through an integrated platform combining botanical science, field observations, geographic context, evidence-based identification and expert participation.

---

## 1. Vision

To make reliable botanical knowledge more accessible, connected, explainable and useful for people, researchers, institutions and conservation initiatives.

## 2. Mission

To develop a durable botanical intelligence ecosystem that brings together:

- Scientific and taxonomic knowledge
- Plant identification and evidence assessment
- Geographic and ecological information
- Field observations and documentation
- Expert and community participation
- Research and institutional integrations
- Responsible artificial intelligence

Plant identification is an important entry point, but the long-term objective is much broader than a plant-identification application.

## 3. Relationship with Save Tiger First

Botanica Indica is part of the wider Save Tiger First ecosystem.

The long-term STF direction is to develop reusable technology, infrastructure, standards and governance capabilities that can support multiple domain applications.

The intended architectural relationship is:

- **STF shared platform:** common infrastructure and capabilities reusable across STF initiatives.
- **Domain applications:** specialised applications that use shared STF capabilities while retaining their own domain models, rules, workflows and knowledge.

The shared platform may include identity and access management, media services, common geographic capabilities, search, notifications, audit, analytics, observability and integration infrastructure.

Botanica Indica's domain responsibilities include botanical taxonomy, plant identification, botanical evidence, species knowledge, observations, scientific validation and expert review.

This is the intended logical ownership model. Individual shared services will be implemented and governed through separate architecture decisions. Their presence in this description does not imply that they are already operational.

## 4. Product direction

Botanica Indica is intended to support the following capabilities.

### Plant identification
- Image-assisted plant identification
- Guided image and evidence collection
- Geographic and ecological context
- Candidate ranking and alternative possibilities
- Explicit confidence and uncertainty
- Explanations of supporting and conflicting evidence

### Botanical knowledge
- Scientific species profiles
- Accepted names and synonyms
- Taxonomic relationships and alternative treatments
- Morphological characteristics
- Habitat and distribution information
- Native, endemic, introduced, naturalised and other relevant status classifications
- Source references and provenance

### Geography and ecology
- State, district and regional exploration
- Habitat and ecological context
- Distribution information
- Geographic evidence and uncertainty
- Appropriate protection of sensitive species locations

### Observations and contributions
- Field observations
- Photographic documentation
- User corrections and additional evidence
- Observation history
- Community participation
- Expert review and validation

### Scientific and institutional collaboration
- Data-source integrations
- Research workflows
- Expert and institutional participation
- Documented APIs and exportable data
- Reproducible data processing

## 5. Core principles

The ecosystem will be developed around these principles:

1. **Scientific credibility:** botanical information must have identifiable sources and appropriate validation.
2. **Evidence before assertion:** identification results should explain the evidence supporting them.
3. **Uncertainty is acceptable:** the platform must be able to return insufficient evidence or an unknown result.
4. **Explainability:** AI-generated inference must remain distinguishable from established scientific information and expert validation.
5. **Taxonomic integrity:** multiple sources, synonyms, alternative treatments and historical classifications must be representable.
6. **Geographic intelligence:** location and ecological context are important identification and knowledge signals.
7. **Provenance:** source, contributor, date, license, validation status and relevant version information should be retained.
8. **Human expertise:** expert review and scientific disagreement must be supported.
9. **Responsible AI:** models must be evaluable, replaceable and governed by data permissions.
10. **Privacy and conservation:** personal information and sensitive species locations require appropriate protection.
11. **Interoperability:** documented contracts and standard data formats should be preferred.
12. **Reusable infrastructure:** common capabilities should be shared across STF initiatives where appropriate.
13. **Technology independence:** the architecture should avoid unnecessary dependence on a single language, framework, cloud provider, database or AI model.
14. **Long-term maintainability:** decisions should consider operational sustainability and future migration costs.

## 6. Architecture direction

The ecosystem follows a contract-driven architecture organised conceptually around:

**Contracts → Services → Clients**

- Contracts define documented and versioned communication interfaces.
- Services implement reusable platform and domain capabilities.
- Clients include mobile applications, web applications, administrative tools, research interfaces and external integrations.

The initial architecture may use a modular monolith where appropriate. Components should become independently deployed services only when justified by ownership, scaling, reliability, security or operational requirements.

The architecture should not adopt microservices simply for the sake of adopting microservices.

## 7. Technology direction

The current intended technology roles are:

| Area | Intended technology |
|---|---|
| Platform, APIs and application services | TypeScript |
| AI/ML and scientific computing | Python |
| Mobile applications | Dart / Flutter |
| Relational and spatial database | PostgreSQL / PostGIS |
| API contracts | JSON / OpenAPI |
| Scientific and bulk data | CSV / Parquet / GeoJSON |
| Performance-critical components | Rust where justified |
| Native mobile integrations | Kotlin / Swift where required |

These are architectural preferences, not permanent restrictions. Technology choices must be supported by documented requirements and decisions.

## 8. Scientific data and responsible integration

Botanica Indica may integrate information from scientific institutions, botanical databases, floras, observation platforms, publications and other appropriate sources.

Every integrated source must be assessed for:

- Scientific relevance and authority
- Taxonomic coverage and treatment
- Geographic coverage
- Data quality and completeness
- Provenance and attribution
- License and redistribution permissions
- Commercial-use permissions
- AI training and derivative-use permissions
- Update frequency and versioning
- Applicable privacy and conservation restrictions

Public accessibility does not automatically mean permission to scrape, redistribute, commercially reuse or train AI models on a source.

The platform must distinguish original project data, external source data, derived information, user contributions, AI-generated inference and expert-reviewed information.

## 9. Licensing direction

Botanica Indica is part of a multi-project ecosystem. A single license will not necessarily be appropriate for every asset.

Licensing will be determined by asset and component type. Software, shared infrastructure, documentation, datasets, photographs, scientific content, AI models, user contributions and trademarks may have different licensing terms.

Each repository, component and dataset release must clearly identify its applicable license and third-party obligations.

See the licensing policy documentation when established. No third-party material may be assumed to be freely reusable merely because it is publicly accessible.

## 10. Current project status

**Current stage: project definition, architecture and scientific-data strategy.**

The repository currently establishes the project's initial documentation and architecture decisions. It should not be interpreted as a completed or production-ready application.

The next stages include:

1. Repository documentation and governance alignment
2. STF shared-platform and Botanica domain boundary definition
3. Data architecture and scientific data model
4. Taxonomy, evidence, observation and provenance models
5. API contracts and integration strategy
6. Backend and database foundations
7. Mobile and web application foundations
8. AI/ML experimentation and evaluation
9. Security, testing, deployment and operational readiness

Progress should be recorded through reviewed documentation, architecture decisions, issues, pull requests and implementation milestones.

## 11. Architecture decision records

Architecture decisions are maintained under `docs/adr/`.

| ADR | Subject |
|---|---|
| ADR-001 | Architecture principles and technology independence |
| ADR-002 | Modular architecture |
| ADR-003 | API-first platform |
| ADR-004 | Data and scientific provenance |
| ADR-005 | Taxonomy reconciliation |
| ADR-006 | Identification architecture |
| ADR-007 | Evidence and expert validation |
| ADR-008 | Geospatial and sensitive location data |
| ADR-009 | Observation and contribution model |
| ADR-010 | Data ingestion and source integration |

New significant decisions should be documented through ADRs. Existing accepted decisions should be amended or superseded explicitly rather than silently contradicted.

## 12. Repository structure

```text
botanica-indica/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
└── docs/
    └── adr/
        ├── ADR-001-architecture-principles.md
        ├── ADR-002-modular-architecture.md
        ├── ADR-003-api-first-platform.md
        ├── ADR-004-data-and-scientific-provenance.md
        ├── ADR-005-taxonomy-reconciliation.md
        ├── ADR-006-identification-architecture.md
        ├── ADR-007-evidence-and-expert-validation.md
        ├── ADR-008-geospatial-and-sensitive-location-data.md
        ├── ADR-009-observation-and-contribution-model.md
        └── ADR-010-data-ingestion-and-source-integration.md
```

This structure will evolve as implementation and governance documentation are added.

## 13. Contribution

Contributions should support scientific credibility, responsible data use, maintainable architecture, security, interoperability and the long-term objectives of the ecosystem.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes.

Scientific data, photographs, datasets, code and documentation must have clear provenance and appropriate rights for contribution and reuse.

## 14. License

The existing repository software license is Apache License 2.0. Its scope must not be interpreted as licensing all third-party data, photographs, scientific publications, user contributions or other materials associated with the project.

The project will establish an asset-specific licensing policy as part of its governance documentation.
