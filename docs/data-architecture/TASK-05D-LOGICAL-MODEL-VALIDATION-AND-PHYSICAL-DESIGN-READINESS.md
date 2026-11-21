# TASK 05D — Logical Model Validation and Physical Database Design Preparation

**Project:** Botanica Indica — Save Tiger First  
**Document type:** Data architecture validation and design-gate specification  
**Version:** 0.1 — Proposed for review  
**Status:** Draft; no physical schema or migrations approved  
**Baseline:** Task 05, Task 05B and Task 05C as currently proposed  
**Branch basis:** Task 05C feature branch; this document is intended to be reviewed after Task 05C

---

## 1. Purpose

Task 05D defines how Botanica Indica will validate its logical scientific data model before committing to a physical PostgreSQL/PostGIS design.

It is a **validation and decision-gate document**, not a replacement for Task 05B or Task 05C. It identifies consistency checks, unresolved design questions, representative test fixtures, acceptance criteria, expert review requirements, security and rights tests, and the evidence required to authorize physical design.

The objective is not to produce the most elaborate model. It is to produce the smallest model that preserves the scientific meaning, provenance, uncertainty, rights, history and interoperability required by Botanica Indica.

## 2. Current baseline and verification position

Task 05C proposes separate logical contexts for taxonomy, botanical knowledge, field records, identification, evidence/review, geography, media, source integration and governance. It also distinguishes Observation, Event, Organism, Occurrence and MaterialEntity, and separates a digital MediaAsset from physical material.

Task 05D treats those as **proposed design elements**. Their presence in documentation does not mean they have been scientifically validated, physically implemented or accepted by STF.

Before review begins, maintain a review register containing:
- document and version reviewed;
- Git commit SHA;
- reviewer name/role and relevant expertise;
- date and review scope;
- comments and evidence;
- decision (accept, amend, reject, defer);
- resulting document/ADR change.

Do not mark a proposal accepted solely because a pull request is mergeable or a document is present in GitHub.

## 3. Review principles

1. Scientific meaning takes precedence over implementation convenience.
2. Preserve verbatim source statements separately from normalized interpretations.
3. Do not infer missing evidence, coordinates, dates, permissions or taxonomic certainty.
4. Distinguish internal data validity from readiness to publish to an external aggregator.
5. Prefer enforceable foreign keys and typed relationships over unconstrained polymorphic references.
6. Do not require every optional concept to exist for every observation.
7. Apply privacy, sensitive-location and rights rules across APIs, exports, search, logs, analytics, caches and backups.
8. Keep search indexes, embeddings and AI outputs derived and reproducible; they are not scientific systems of record.
9. Do not introduce bitemporal machinery, partitioning, microservices or event sourcing without demonstrated requirements.
10. Record rejected alternatives and the reasons for decisions.

## 4. Cross-document consistency audit

The review must compare Task 05, Task 05B and Task 05C line by line and resolve the following areas.

| Review ID | Topic | Required reconciliation |
|---|---|---|
| DOC-01 | Entity naming | One canonical term for each concept; distinguish user-facing and standards-facing terms |
| DOC-02 | Taxonomy | TaxonName, TaxonConcept, TaxonomicTreatment, TaxonNameUsage and TCS mappings agree |
| DOC-03 | Field records | Observation, Event, Organism, Occurrence and MaterialEntity have consistent definitions |
| DOC-04 | Identification | Subject, taxon determination, candidate, model run and expert review lifecycle agree |
| DOC-05 | Evidence | Evidence type, evidence relationship and source/citation semantics agree |
| DOC-06 | Assertions | Subject, predicate, typed value, scope, source, agent and temporal semantics are explicit |
| DOC-07 | Geography | Place/geographic unit/location/geometry/representation are not conflated |
| DOC-08 | Rights | Dataset rights, media rights, user grants and purpose-specific AI permissions are distinct |
| DOC-09 | Provenance | Source record, dataset version, ingestion run, transformation and lineage are traceable |
| DOC-10 | Temporal data | Valid time, observation time, publication time, retrieval time and recorded time are distinguished |
| DOC-11 | Identifiers | Internal IDs, external IDs, source IDs and export identifiers are not mixed |
| DOC-12 | Shared platform | STF identity/media/audit infrastructure is separated from Botanica scientific domain ownership |
| DOC-13 | Vocabulary | Status, rank, basis of record, evidence role, review decision and distribution terms are versioned |
| DOC-14 | API/export | Standards mappings do not leak internal implementation or erase source semantics |
| DOC-15 | Retention | Deletion, anonymization, withdrawal, retention and provenance preservation are consistent |
| DOC-16 | Internal vs export occurrence | Internal record validity is independent of Darwin Core/GBIF export-profile completeness; no unsupported values are fabricated |
| DOC-17 | Typed scientific subjects | ScientificAssertion and Identification use typed subject links or a formally enforceable supertype; no unconstrained polymorphic FK pair |
| DOC-18 | TCS mapping vocabulary | TaxonConceptMapping uses the six TCS mapping relations with their exact semantics |
| DOC-19 | TCS accordingTo resource | Each TaxonConcept has exactly one canonical according-to resource; any treatment specialization resolves to that same resource |
| DOC-20 | Taxonomy relationship families | Concept-to-name synonym assertions, name-to-name nomenclatural relations and concept-to-concept mappings are distinct |
| DOC-21 | Synonym target semantics | TCS synonym target is TaxonName; source-specific TaxonNameUsage remains a separate record |
| DOC-22 | Source role and authority | Source type, editorial/curation model, scope, version, date and limitations are recorded; source fitness is purpose-specific |

### 4.2 Reconciliation update — repository desk review, 16 November 2026

The following document-level corrections have been applied on the current Task 05B and Task 05C proposal branches. This is an authoring/reconciliation pass, not an independent scientific sign-off.

| Review ID | Current disposition | Evidence to re-check | Remaining condition |
|---|---|---|---|
| DR-01 / DOC-16 | **Revised in 05B and 05C** | Occurrence no longer requires a Darwin Core `basisOfRecord` as a universal internal field; provenance remains required. Export mapping is profile-specific. | Re-review fixtures and exact export profiles; confirm explicit non-detection states and event evidence. |
| DR-02 / DOC-17 | **Revised in 05B and 05C** | Dictionary specifies typed FK subject links. Task 05C proposes one IdentificationSubject row with exactly one of three real target FKs, enforced by CHECK; ScientificAssertion uses explicit typed links. | Validate supported subject inventory and PostgreSQL constraints; test exactly-one subject and FK integrity. |
| DR-03 / DOC-18 | **Revised in 05B and 05C** | Mapping vocabulary names the six exact TCS relations; informal “excludes” and “not congruent” removed from the field definition. | Review directionality and semantics with a taxonomist; test mapping export/import round trips. |
| DR-04 / DOC-19 | **Revised in 05B and 05C** | One canonical `according_to_resource_id` represents TCS `accordingTo`; optional treatment specialization must resolve to the same resource. | Confirm resource registry semantics and uniqueness/integrity implementation with biodiversity-informatics reviewer. |
| DR-05 / DOC-20 | **Revised in Task 05 and 05C** | Concept-to-name synonym, name-to-name nomenclatural and concept-to-concept mapping families are explicitly distinguished. | Re-review remaining relationship labels and fixtures; ensure no generic TaxonRelationship implementation remains. |
| DR-06 | **Revised in 05B** | Current taxonomic determination is derived from the applicable Identification assertion, not stored as a mutable duplicate on Occurrence. | Confirm all read models/API views use the same derivation and preserve historical determinations. |
| DR-07 | **Revised in 05B, 05C and 05D** | Explicit absent/non-detected Occurrence state is permitted only with defined Survey/Event, protocol, effort, target and location; Task 05C adds LDM-16 and Task 05D adds FLD-08. | Confirm Darwin Core `occurrenceStatus` mapping and validate realistic sampling-event fixtures; no row must never imply absence. |
| DR-08 | **Open test case** | Mango native/introduced example remains a geographic-resolution and source-scope comparison, not a proven direct contradiction. | Normalize comparable geographic units and review source-specific treatment evidence. |
| DR-09 | **Withdrawn as erroneous** | The current official TDWG List page identifies 2026-10-13 as the current release; 2026-05-26 is the previous release. The earlier desk review used an incorrect version assumption. | Preserve the correct List release IRI and record individual term-version/modification metadata separately. |
| DR-10 | **Revised in 05B** | TaxonName, TaxonNameUsage and Occurrence source identifiers now use canonical SourceRecord FKs or constrained external-identifier tuples. | Confirm SourceRecord namespace, dataset version and ingestion-run uniqueness rules in physical design. |
| DR-11 / DOC-21 | **Revised in 05B** | TCS synonym assertions target TaxonName; TaxonNameUsage remains separate. | Validate against the Ficus fixture and TCS mapping semantics. |
| DR-12 / DOC-22 | **Revised in 05B** | Source metadata captures source type, editorial/curation model, scope, version, access date and limitations, with purpose-specific examples. | Review current source profiles and terms for IPNI, POWO/WCVP, BSI and eFlora of India. |

The corrections above address the identified documentation conflicts but do not by themselves close the findings. The official Darwin Core List of Terms page currently identifies the list release as issued 2026-10-13 (previous version 2026-05-26); individual term modification dates and term-version IRIs may differ. Reference: https://dwc.tdwg.org/list/. The current GBIF profile distinctions are supported by official technical documentation: occurrence datasets require `occurrenceID`; `basisOfRecord`, `scientificName` and `eventDate` are strongly recommended in the general profile and required in GBIF-managed programmes; sampling-event datasets have distinct requirements. See https://techdocs.gbif.org/en/data-publishing/data-quality-recommendations.

### 4.1 Known correction: internal validity vs GBIF publishing requirements

An earlier draft of Task 05C included the statement "No occurrence without basis-of-record and provenance." That statement has been revised in the current Task 05C branch: provenance remains an internal requirement, while Darwin Core `basisOfRecord` is required only when supported by the selected export mapping/profile.

GBIF's current occurrence data quality guidance lists `occurrenceID` as required for publishing; `basisOfRecord`, `scientificName`, `eventDate` and coordinates are strongly recommended or conditionally required depending on the field/programme. These external publishing expectations must not be misrepresented as universal internal database constraints.

Required revision:
- Internal records must preserve the evidence and provenance that actually exist.
- An internal occurrence may be valid but not publishable to GBIF.
- Export validation must produce field-level warnings/errors according to the selected GBIF profile and dataset type.
- Never fabricate basis-of-record, date, taxon or coordinates to satisfy an export checklist.
- A publishing profile may impose stricter rules than the core internal model.

Reference: https://techdocs.gbif.org/en/data-publishing/data-quality-recommendations

This distinction is a mandatory correction before physical design.

## 5. Domain model validation matrix

Each scenario must be tested with a source-backed fixture, expected outcome, reviewer and test evidence. The fixtures must not be treated as real field observations unless the underlying source record supports that interpretation.

### 5.1 Taxonomy and nomenclature

| ID | Fixture | Expected model behaviour | Failure condition |
|---|---|---|---|
| TAX-01 | Same name string used by two treatments | Two treatment-scoped concepts remain distinct | Concepts silently merged by name string |
| TAX-02 | One concept lists several synonym names | Synonym relations target TaxonName and retain source | Synonym incorrectly modelled only as concept-to-concept equivalence |
| TAX-03 | Two concepts partially overlap | Typed, sourced TaxonConceptMapping retained | Mapping relation omitted or direction lost |
| TAX-04 | Name has basionym/replacement-name relationship | Typed name-to-name relation retained | Relationship inferred from string similarity |
| TAX-05 | Type specimen cited by a publication | NomenclaturalType links to source and specimen reference | Specimen image treated as the type itself |
| TAX-06 | Name usage cannot be reconciled | Verbatim usage remains unresolved | Import process forces a guessed accepted name |
| TAX-07 | Treatment is revised | New treatment/concept history retained | Old source concept overwritten |

### 5.2 Observation, occurrence and material

| ID | Fixture | Expected model behaviour | Failure condition |
|---|---|---|---|
| FLD-01 | User submits a plant photograph without a name | Observation and MediaAsset exist; no forced species ID | Placeholder species created |
| FLD-02 | One observation documents several plants | Supports explicit multiple occurrence/organism relationships where evidence allows | One plant assumed without evidence |
| FLD-03 | One individual photographed repeatedly | Repeat events/occurrences can refer to the same organism when identity is justified | Each photo automatically creates a new organism |
| FLD-04 | Herbarium sheet with collection metadata | Physical MaterialEntity, Event and determination history remain distinct | Image substituted for specimen |
| FLD-05 | Leaf tissue sampled from a specimen | Derived MaterialEntity links to source material and event | Derivation provenance lost |
| FLD-06 | Field record has uncertain date | Date value, precision and uncertainty preserved | Unknown precision converted to exact timestamp |
| FLD-07 | Observation is withdrawn by contributor | Workflow status and retention policy applied without silent provenance corruption | Record disappears without audit/retention assessment |
| FLD-08 | Defined survey fails to detect a target taxon | Explicit absent/non-detected Occurrence state is linked to Event, protocol, effort, target and location; no row is never interpreted as absence | Non-detection inferred from missing Occurrence or stored without survey context |

### 5.3 Identification, evidence and review

| ID | Fixture | Expected model behaviour | Failure condition |
|---|---|---|---|
| ID-01 | AI returns ranked candidates | Run and candidates retained with score semantics | Top candidate automatically becomes verified |
| ID-02 | Raw similarity score is 0.92 | Stored as raw score, not probability unless calibrated | UI labels 0.92 as 92% certainty |
| ID-03 | Expert rejects AI suggestion | New attributable assessment and determination retained | AI output overwritten/deleted |
| ID-04 | Two experts disagree | Both assessments and evidence remain accessible to authorized reviewers | Last-write-wins hides disagreement |
| ID-05 | Candidate set generated by a new model version | Run records exact model/pipeline/backbone versions | Candidate ranking cannot be reproduced |
| ID-06 | Evidence contradicts a claim | Evidence relationship records contradiction and rationale | All evidence forced into "supports" |
| ID-07 | Identification is only at genus level | Rank and qualifier represented honestly | System requires species-level selection |

### 5.4 Geographic and distribution evidence

| ID | Fixture | Expected model behaviour | Failure condition |
|---|---|---|---|
| GEO-01 | Exact private coordinate and generalized public point | Separate representations and policy are retained | Exact coordinate overwritten or exposed |
| GEO-02 | District-level locality only | Area/uncertainty retained without fabricated point | District centroid represented as observation coordinate |
| GEO-03 | Coordinate CRS is unknown | Unknown CRS remains explicit and blocks unsafe transformation | SRID silently assigned as WGS84 |
| GEO-04 | Two sources disagree on native range | Separate source-scoped DistributionAssertions retained | One global native flag overwrites disagreement |
| GEO-05 | Administrative boundary is revised | Boundary version and valid period retained | Old record silently shifts to new geometry |
| GEO-06 | Sensitive taxon record appears in search | Restricted geometry and identifying locality are not leaked | Search result exposes hidden location |

### 5.5 Media rights, source ingestion and lineage

| ID | Fixture | Expected model behaviour | Failure condition |
|---|---|---|---|
| RGT-01 | Dataset is open but an embedded image has separate terms | Dataset and image rights evaluated separately | Dataset license assumed to cover every image |
| RGT-02 | Display permitted, redistribution prohibited | Display allowed only in authorized channel; redistribution blocked | Media is included in public export |
| RGT-03 | AI training permission absent/unclear | Training eligibility denied/pending | Absence interpreted as consent |
| RGT-04 | Contributor revokes a permission | Policy re-evaluates uses and records action | Revocation has no traceable effect |
| SRC-01 | Dataset is imported twice | Two ingestion runs and source version lineage retained | Re-import duplicates or overwrites silently |
| SRC-02 | Source payload retention prohibited | Only permitted metadata/reference/checksum retained | Restricted payload stored anyway |
| SRC-03 | Source changes its accepted-name field | Verbatim old and new source snapshots/mappings retained as permitted | Normalized record loses original source value |
| SRC-04 | Import validation fails | Record quarantined with reason and retry path | Invalid record silently discarded or accepted |

## 6. Data quality architecture: four distinct layers

Do not create one universal "quality score". Implement separate quality dimensions with explicit semantics.

### Layer 1 — Structural validity

Examples:
- required internal identifiers exist;
- foreign keys resolve;
- date/coordinate syntax is parseable;
- geometries are valid where applicable;
- typed relationships use valid vocabulary terms;
- source/version references resolve.

Structural validity is suitable for hard database constraints where the rule is local and stable.

### Layer 2 — Scientific completeness and evidence quality

Examples:
- image shows diagnostic plant organs;
- date and locality precision are adequate for the claim;
- identification has diagnostic evidence;
- source citation is sufficiently specific;
- specimen determination is attributable.

These are often graded or reviewable and should not all become database NOT NULL constraints.

### Layer 3 — Rights, privacy and governance eligibility

Examples:
- display permission;
- redistribution permission;
- commercial use permission;
- AI training permission;
- location sensitivity;
- contributor consent and retention state.

A record can be scientifically excellent but legally unavailable for a particular use.

### Layer 4 — External publication readiness

Examples:
- GBIF occurrence profile;
- Darwin Core Archive export;
- TCS export;
- research dataset publication profile.

Each profile has its own required/recommended fields and validation rules. A failure to meet an external profile does not automatically make the underlying internal record invalid.

## 7. Data validation and error model

Every validation rule must have:
- stable rule ID and version;
- scope/entity/field;
- severity (error, warning, information, review-required);
- rule description and rationale;
- machine-readable test where possible;
- remediation guidance;
- whether the rule blocks storage, publication, AI use or only a user-facing claim;
- source/standard version if externally derived.

Recommended validation result fields:
- validation result ID;
- subject entity and version;
- rule ID/version;
- outcome;
- severity;
- observed value or redacted diagnostic;
- explanation;
- evaluated time;
- validator/software version;
- remediation state;
- reviewer decision where applicable.

Never place restricted coordinates, personal data or copyrighted source payloads in general-purpose error messages or logs.

## 8. PostgreSQL/PostGIS physical design evaluation gate

PostgreSQL/PostGIS remains the recommended candidate, not a final decision. The physical design evaluation must demonstrate the following.

### 8.1 Relational capability

- primary/foreign keys for typed relationships;
- unique constraints for source-scoped identifiers;
- check constraints for row-local invariants;
- exclusion constraints where temporal/spatial overlap rules genuinely require them;
- transaction-safe updates for multi-entity scientific decisions;
- migration and rollback/recovery strategy;
- backup/restore and point-in-time recovery expectations.

Important PostgreSQL constraint guidance:
- CHECK constraints should not query other rows/tables as a substitute for relational integrity.
- Use FK, UNIQUE and EXCLUDE constraints where suitable.
- Cross-entity workflow rules may require transactions, application logic or carefully designed triggers.
- Index referencing foreign-key columns when workload justifies it; PostgreSQL does not automatically create every referencing-side index.

Reference: https://www.postgresql.org/docs/current/ddl-constraints.html

### 8.2 Geospatial capability

- explicit CRS/SRID and transformation rules;
- uncertainty and georeferencing precision;
- administrative and ecological boundary versioning;
- spatial index/query plan testing;
- exact/generalized location separation;
- row/API authorization tests;
- no coordinate disclosure through derived search, cache, analytics or export.

### 8.3 Security and privacy

- least-privilege service and human roles;
- separate public, contributor, expert, curator and administrator capabilities;
- server-side authorization;
- assess row-level security as a defence-in-depth control, not the only control;
- audit privileged access to restricted data;
- encryption in transit and at rest according to deployment threat model;
- retention, deletion and anonymization policy;
- backup and restore security;
- secrets outside source control.

### 8.4 Performance and operations

Do not set arbitrary performance numbers without workload assumptions. Build a representative workload:
- taxon name and synonym lookup;
- taxon profile and source citations;
- India/state/district distribution queries;
- nearby observations with privacy filters;
- media metadata and rights eligibility;
- source import and reconciliation;
- expert review queues;
- export validation.

Measure realistic record counts, concurrent users, image volumes, query plans and geographic selectivity before choosing partitioning, caching or specialized search services.

## 9. Required review roles and sign-off

| Reviewer role | Required review |
|---|---|
| Indian plant taxonomist | Names, concepts, treatments, synonymy, nomenclatural types and taxonomic uncertainty |
| Herbarium/data curator | MaterialEntity, specimen metadata, collection events and determinations |
| Biodiversity informatics specialist | Darwin Core, TCS, GBIF mappings and occurrence semantics |
| Field botanist/ecologist | Observation workflows, multiple plants, evidence, phenology and habitat |
| Geospatial specialist | CRS, uncertainty, distribution, boundaries and sensitive locations |
| Privacy/security reviewer | Contributor data, access control, sensitive coordinates, logs and backups |
| Rights/legal reviewer | Source terms, media permissions, user contributions and AI training |
| Database architect | Keys, constraints, transactions, migrations, indexing and operations |
| Product owner | Workflow fit, usability, priorities and acceptable uncertainty |

A reviewer may be one person for more than one role only where their competence is appropriate. Lack of a reviewer must be recorded as an unresolved risk, not treated as approval.

## 10. NatureTech and conservation-outcome design implications

The TEDxVitosha talk supplied for this project frames nature as a partner and source of evolved capabilities, with technology used alongside ecological systems. This is relevant strategic context, but it does not change Botanica Indica's core scope or authorize a NatureTech product expansion.

For any future STF/ Botanica project that supports a nature-based intervention, the data architecture should be capable of recording:
- intervention/project identity and responsible organizations;
- baseline ecosystem condition and methodology;
- site, landscape and temporal scope;
- target ecological outcomes and indicators;
- monitoring method, sensor/model versions and sampling effort;
- observed outcomes, uncertainty and independent verification;
- social/community participation and rights-holder involvement;
- safeguards, trade-offs, unintended impacts and corrective actions;
- maintenance, permanence and post-project monitoring.

Do not equate technology deployment with conservation success. A drone flight, satellite classification, tree-planting count or AI species prediction is an activity/output or evidence stream, not proof of biodiversity recovery.

The IUCN Global Standard for Nature-based Solutions provides a useful quality framework covering societal challenges, systems perspective, biodiversity/ecosystem integrity, financial feasibility, inclusive governance, trade-offs/safeguards, adaptive management and sustainability. Its criteria should inform future intervention evaluation; they should not be treated as a certification claim unless the applicable assessment process has actually been completed.

References:
- IUCN Global Standard for Nature-based Solutions: https://inbs.iucn.org/
- IUCN criteria and indicators: https://inbs.iucn.org/understand/8-criteria/
- IUCN Nature-based Solutions definition: https://inbs.iucn.org/understand/nbs-definition/
- Nature Tech Collective definition and use cases: https://www.naturetechcollective.org/stories/inside-the-process-developing-the-nature-tech-taxonomy
- Nature4Climate, State of Nature Tech: https://nature4climate.org/wp-content/uploads/2023/10/N4C-The-state-of-nature-tech-final.pdf

## 11. Physical design readiness checklist

Physical schema work may begin only when all critical items are satisfied or explicitly waived by an accountable decision-maker.

- [ ] Cross-document consistency audit completed.
- [ ] TCS name/concept/treatment semantics reviewed by taxonomic specialist.
- [ ] Darwin Core occurrence/event/material distinctions reviewed by biodiversity informatics specialist.
- [ ] Observation-to-occurrence conversion rules documented.
- [ ] Multiple-plant and clonal/group observation cases tested.
- [ ] Identification and expert disagreement lifecycle agreed.
- [ ] Scientific assertion subject relationships are enforceable.
- [ ] Rights model supports purpose-specific decisions and revocation.
- [ ] Sensitive-location access model reviewed and threat-tested.
- [ ] CRS, uncertainty and boundary-version rules agreed.
- [ ] Source lineage and retention rules agreed.
- [ ] Internal validity separated from external export readiness.
- [ ] Representative fixtures and expected outputs stored in version control.
- [ ] PostgreSQL/PostGIS evaluation completed against actual requirements.
- [ ] Backup, restore, migration and operational responsibilities documented.
- [ ] Unresolved risks and rejected alternatives recorded.

## 12. Deliverables after Task 05D approval

Only after the review gate is passed should the project produce:

1. Task 05B/05C reconciled revisions.
2. Approved logical ERD.
3. Canonical entity/attribute dictionary with nullability and ownership.
4. Relational mapping and foreign-key specification.
5. Controlled vocabulary registry and seed data plan.
6. PostgreSQL/PostGIS physical schema proposal.
7. Migration and rollback plan.
8. Index and query workload specification.
9. Privacy/security policy implementation matrix.
10. Automated schema, integrity, rights and interoperability test plan.
11. ADR for database engine and physical design decisions, if a formal decision is required.

## 13. Decision status

**Proposed validation gate — not approved.**

Task 05D does not authorize production DDL, migrations, ingestion of third-party datasets, public release of sensitive locations or AI training. It establishes the evidence and review process required before those steps.

**Recommendation:** complete the domain and scientific review first. Then design a modest PostgreSQL/PostGIS implementation with strong relational integrity and spatial controls. Keep derived search, AI and analytics systems replaceable. The database should preserve scientific evidence and history even if every AI model and user interface is replaced.
