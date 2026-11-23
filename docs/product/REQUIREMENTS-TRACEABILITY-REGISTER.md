# Botanica Indica — Requirements Traceability Register

**Document ID:** STF-BI-RTM-001  
**Version:** 0.3 — proposed controlled capability, source-provenance and ODR-01 traceability reconciliation  
**Prepared:** 23 November 2026  
**Status:** Proposed for owner review; not an approved requirements baseline  
**Decision authority:** Save Tiger First project owner  
**Scope:** Full Botanica Indica product; STF shared-platform dependencies are identified where relevant  
**Repository:** `Save-Tiger-First/botanica-indica`

---

## 1. Purpose and decision boundary

## 1.1 Task 03–04 architecture and acceptance-readiness audit

## 1.2 Offline and field synchronization architecture specification

## 1.3 API command, idempotency and conflict-resolution contract

The proposed server-side synchronization contract is documented in [STF-BI-API-SYNC-001 — API Command, Idempotency and Conflict-Resolution Contract Design](../architecture/API-COMMAND-IDEMPOTENCY-AND-CONFLICT-RESOLUTION-CONTRACT-DESIGN.md). It elaborates Task 03 §§19–20 and AC-004/AC-009/AC-010 dependencies through a versioned command envelope, durable command receipts, separate client-command and HTTP idempotency identities, conditional updates, conflict handling, media staging and cursor-based change recovery. The document is Proposed; it does not approve API routes, schemas, authentication, database design, retention periods or implementation. API-SYNC-001–042 are proposed validation scenarios and have not been executed. API-OD-01–20 remain open.



The proposed offline/field synchronization design is recorded in [STF-BI-ARCH-OFF-001 — Offline and Field Synchronization Architecture & Validation Specification](../architecture/OFFLINE-FIELD-SYNCHRONIZATION-ARCHITECTURE-AND-VALIDATION-SPECIFICATION.md). It elaborates Task 03 §§17, 20 and 28, WF-OD-10, and AC-004/AC-009/AC-010 dependencies. The document proposes a local draft/outbox, idempotent server command processing, version-aware conflict handling, rights/sensitivity revalidation and 36 validation scenarios (OFF-001–OFF-036). It remains Proposed; no ADR, API contract, physical schema, legal policy or implementation is approved by its creation. Tests are not run.



The cross-document audit is recorded in [Task 03–04 Cross-Document Architecture and Acceptance-Readiness Audit](../architecture/TASK-03-04-CROSS-DOCUMENT-READINESS-AUDIT.md) (STF-BI-AUD-034 v0.1). It identifies the shared-platform/domain ownership inconsistency, identity capability mapping defect, offline synchronization architecture gap, Task 04 decision-status ambiguity and documentation citation issues. Findings are proposals for owner review; the audit does not amend the original PRD, Task 04 source transcription, accepted ADRs or scientific data model.



This register connects source requirements to product capabilities, scientific constraints, architecture responsibilities, accepted Architecture Decision Records (ADRs), validation scenarios and evidence required for acceptance.

It is a traceability instrument, not a substitute for the source PRD, architecture document, scientific data model, ADRs, legal review or test evidence.

It does **not**:
- approve the Full Product Vision or PRD;
- amend or supersede ADR-001 through ADR-010;
- approve Task 05 scientific models or close DR findings;
- authorize physical database design, implementation, procurement or deployment;
- convert a proposal, candidate technology, AI output or user contribution into a verified scientific fact.

All requirement and capability status fields begin as **Not yet verified** unless direct evidence is recorded. A requirement appearing in this register does not mean it is implemented.



## 2. Source baseline and exact revisions inspected

| Source | Ref / branch | Blob SHA | Status at review |
|---|---|---|---|
| Permanent AI Project Operating Prompt, STF-AI-OPS-001 v1.0 | `docs/repository-audit-and-ai-operating-standard` | `53add3894d0502827e584614c70ad09cadaa637d` | Proposed standard; user instruction requires adherence |
| Task 03 PRD v0.1 transcription | `docs/canonical-task-03-04-baselines` | `8b1ca0be04b3f4ad3b543c2f9fc48d46eb37faf8` | Working baseline; not accepted |
| Task 04 architecture evaluation v0.1 transcription | `docs/canonical-task-03-04-baselines` | `abc7b721fae8d4f4adede4dd0bf5d6a32098c5a3` | Working baseline; not accepted |
| Full Product Vision and Capability Blueprint v0.2 | `docs/full-product-vision-capability-blueprint` | `d3ec150524dda4928503f43556a97cd766b71312` | Proposed in PR #17; not accepted |
| Scientific Data Model Review Pack | `review/scientific-data-model-review-pack` | `c11f4b58d0908742474d3e58b4ec0aa3739f7b99` | Review proposal; findings remain subject to validation |
| Scientific Data Model Validation Matrix and Decision Register | `review/scientific-data-model-review-pack` | `3a33dfe47657a96456f56f2c12a0b7d355b6c6a5` | Proposed reviewer/test framework; ODR-01 authorized, validation unexecuted |
| Workflow Lifecycle Specification v0.2 | `docs/requirements-traceability-register` | `498af08ec60e3626e8b60ab5047acae1a8861eb5` | Proposed state machines; `record_created`/`server_received` distinction proposed |
| Workflow-to-Requirements Crosswalk v0.2 | `docs/requirements-traceability-register` | `61d2111ace5c408eaf503bdf17b2ccb822f90978` | Proposed WF/requirement and ODR-01/EVT-27–EVT-44 traceability |
| Offline and Field Synchronization Specification v0.2 | `docs/requirements-traceability-register` | `a46c7cc1de9d1ea5c5faed7574d23de1d1a48e13` | Proposed offline design and ODR-01 offline safeguards |
| API Command and Idempotency Contract v0.2 | `docs/requirements-traceability-register` | `bc0f3e93ec6ef2d2c2039b56739db38296c03281` | Proposed API design; ODR-01 export-only constraints; IETF draft v09 |
| Task 03–04 Cross-Document Readiness Audit v0.1 with 23 November follow-up | `docs/requirements-traceability-register` | `4c4c66d6c0600c0a856ce09698769eff84e5a1c3` | Proposed findings; follow-up reconciliation recorded separately |

Original source artifacts preserved in the Project Library:
- `STF_Task_03_Product_Requirements_Document_v0.1.docx` — 16 pages / 677 extracted text lines.
- `STF_Task_04_System_Architecture_and_Technology_Evaluation_v0.1.docx` — 11 pages / 431 extracted text lines.

The repository Markdown transcriptions preserve extracted substantive text; page layout, embedded formatting, diagrams and table geometry may be simplified. The original DOCX files remain the source artifacts.

### 2.2 Source revision revalidation — 23 November 2026

The source SHAs above were re-fetched from their named refs on 23 November 2026. Earlier SHAs in prior versions of this register are historical snapshots, not current identifiers. This revision records the current blob SHAs for the operating prompt, Blueprint, scientific review artifacts, workflow, crosswalk, offline and API proposals. The original Task 03/04 transcription SHAs remain unchanged. Re-fetch all sources before a later approval or implementation decision.

### 2.1 Accepted ADR register inspected

All ten ADR files were fetched from `main`; each explicitly reports **Accepted**.

| ADR | Accepted subject | Blob SHA |
|---|---|---|
| ADR-001 | Architecture Principles and Technology Independence | `a7d3b5c6ec55278c8af70d2e25521153f7f766ad` |
| ADR-002 | Modular Architecture | `de54ad9b5dc1b6f9da8e236c29820f654c658cff` |
| ADR-003 | API-First Platform Architecture | `70aa16dd3ced7f878613254763c4ba752c4ed339` |
| ADR-004 | Data and Scientific Provenance | `75148aff6f8dfddfa8aa794b0cb064c62d6418a7` |
| ADR-005 | Taxonomy Reconciliation | `b61dcf0b9ba58fc35da5cc7ba5edfbdd5f2909e4` |
| ADR-006 | Identification Architecture | `f35345c356725d7dc4b1b64971c0ff59758c8a30` |
| ADR-007 | Evidence and Expert Validation | `7ba4874b4175707b69dc3052822f8cbeb5384b0a` |
| ADR-008 | Geospatial and Sensitive Location Data | `74cc3774799a29b28edab75fc63d129f8841b497` |
| ADR-009 | Observation and Contribution Model | `c096da58dfe0f1eb46812db46e6555ccf01b8718` |
| ADR-010 | Data Ingestion and Source Integration | `088e379513fe2c4b9471d857737f75dcdc3990cd` |

No accepted ADR was modified in preparing this register.

## 3. Traceability conventions

### 3.1 Status vocabulary

- **Source baseline:** present in Task 03 v0.1; not yet formally accepted as the canonical PRD.
- **Proposed addition:** derived from Task 03 narrative, Task 04 or the proposed full-product blueprint; owner approval required before it becomes a controlled requirement.
- **Not yet verified:** no implementation or validation evidence has been inspected.
- **Blocked:** dependent on unresolved scientific, rights, privacy, architecture or governance decisions.
- **Verified:** only after reproducible evidence and appropriate review are recorded.
- **Accepted:** only after explicit project-owner decision.

### 3.2 Requirement identifier rules

Original Task 03 identifiers remain unchanged. The former derived label `SCI-001A` is renamed to `DER-SCI-001` to keep derived requirements distinct from original `SCI-001`; `SCI-001A` is retained only as a legacy alias in this revision. No source PRD requirement is created or modified by this change.

The 19 original functional identifiers are preserved exactly. The additional `NFR-*`, `UX-*`, `DATA-*`, `AI-*`, `RIGHTS-*` and `OPS-*` identifiers below are **proposed register identifiers**, not IDs present in the original PRD. They must not be mistaken for approved requirements until accepted.

### 3.3 Traceability chain

Every controlled requirement should ultimately link to:

1. stakeholder / user need;
2. product capability and journey;
3. source requirement and priority;
4. scientific rule or data constraint, where applicable;
5. architecture module and interface;
6. accepted ADR or explicitly unresolved decision;
7. rights, privacy and security controls;
8. acceptance criteria and test cases;
9. validation evidence, reviewer role and date;
10. release and operational owner.

A missing link is recorded as a gap, not silently inferred.

## 4. Full-product capability identifiers

The canonical proposed capability IDs are `BI-CAP-01` through `BI-CAP-16`, aligned one-to-one with Blueprint Sections 5.1–5.16. They are stable traceability labels for this proposed baseline, not approved product scope until owner acceptance.

| Capability ID | Capability domain | Principal scope | Main user / operational journeys |
|---|---|---|---|
| BI-CAP-01 | Botanical knowledge and taxonomic intelligence | Names, concepts, treatments, usages, nomenclature, source reconciliation | Learn, research, curate taxonomy |
| BI-CAP-02 | Interactive identification and the Evidence Engine | Capture, image quality, candidate generation, contextual ranking, evidence synthesis, abstention | Public identification |
| BI-CAP-03 | Species and botanical knowledge profiles | Sourced descriptions, diagnostic features, names, ecology, distribution, references | Learn and explore |
| BI-CAP-04 | Observation, field documentation and survey workflows | Observations, events, surveys, effort, occurrences, organisms, material entities | Field observation and survey |
| BI-CAP-05 | Geographic and ecological intelligence | Spatial context, distributions, habitats, boundaries, sensitive location policies | Explore and research |
| BI-CAP-06 | Evidence, expert review and scientific governance | Evidence records, determinations, review workflows, disputes, history | Expert determination |
| BI-CAP-07 | Data acquisition, ingestion, curation and interoperability | Source registry, rights screening, dataset versions, ingestion, mappings, exports | Source ingestion and data exchange |
| BI-CAP-08 | Search, exploration, learning and discovery | Scientific/common-name search, filters, maps, learning and discovery | Explore and learn |
| BI-CAP-09 | Community participation and stewardship | Contributions, attribution, consent, moderation, feedback and grievance | Community contribution |
| BI-CAP-10 | Mobile application | Camera, gallery, guided capture, field workflows, offline queue and sync | Field and public use |
| BI-CAP-11 | Public web and research platform | Public knowledge, search, maps, research access and account features | Public discovery and research |
| BI-CAP-12 | Expert and scientific console | Evidence review, determinations, source comparison, curation | Expert determination |
| BI-CAP-13 | Administration and data stewardship console | Roles, permissions, moderation, publishing, audit, data quality and governance | Governance and operations |
| BI-CAP-14 | API and institutional integration platform | Versioned APIs, partner/institution access, exports and integration contracts | Research and integration |
| BI-CAP-15 | AI/ML research, evaluation and operations platform | Dataset governance, model registry, evaluation, calibration, monitoring and release | AI/ML lifecycle |
| BI-CAP-16 | Analytics, observability and operational intelligence | Product telemetry, service health, audit, reliability and cost visibility | Governance and operations |

### 4.1 Legacy identifier crosswalk

The previous RTM used provisional `CAP-01`–`CAP-16` labels. Their numbering already followed the 16-domain sequence; only the namespace is changed. The old labels are retained here as migration aliases, not as parallel canonical identifiers.

| Legacy RTM identifier | Canonical proposed identifier |
|---|---|
| CAP-01 | BI-CAP-01 |
| CAP-02 | BI-CAP-02 |
| CAP-03 | BI-CAP-03 |
| CAP-04 | BI-CAP-04 |
| CAP-05 | BI-CAP-05 |
| CAP-06 | BI-CAP-06 |
| CAP-07 | BI-CAP-07 |
| CAP-08 | BI-CAP-08 |
| CAP-09 | BI-CAP-09 |
| CAP-10 | BI-CAP-10 |
| CAP-11 | BI-CAP-11 |
| CAP-12 | BI-CAP-12 |
| CAP-13 | BI-CAP-13 |
| CAP-14 | BI-CAP-14 |
| CAP-15 | BI-CAP-15 |
| CAP-16 | BI-CAP-16 |

The prior Blueprint Section 13 identifiers used a different 15-domain sequence. Their split and renumbering are documented in Blueprint Section 13.1. Do not use the prior Blueprint IDs or the legacy RTM aliases for new work.

### 4.2 Task 03 explicit non-goals — scope guardrails

The following seven non-goals are transcribed from Task 03 v0.1, Section 34. Their wording is preserved. They define the current product boundary; they are not permanent prohibitions and do not remove the possibility of a separately governed future proposal.

| Source ID | Task 03 non-goal (source wording) | Related capability domains / interpretation | Change control |
|---|---|---|---|
| NG-01 | Do not define the product primarily as a plant-care/reminder application. | BI-CAP-03 and BI-CAP-07 may provide botanical knowledge and discovery; they do not make care reminders the product's primary purpose. | Any change to product identity requires owner approval and Blueprint/PRD revision. |
| NG-02 | Do not make disease diagnosis a core requirement at this stage. | BI-CAP-02 and BI-CAP-15 are not authorization for plant disease diagnosis. | A future disease-diagnosis proposal requires distinct scientific evidence, risk, user and regulatory assessment. |
| NG-03 | Do not add e-commerce or a marketplace as a core requirement. | No current core capability authorizes commerce or marketplace workflows. | Any proposal requires owner approval, business/legal review and explicit scope/requirements changes. |
| NG-04 | Do not make a generic AI chatbot the primary interface. | BI-CAP-02, BI-CAP-08, BI-CAP-10 and BI-CAP-11 may support appropriate guided experiences; this does not authorize a chatbot-first product. | Any primary-interface change requires user research, accessibility/safety review and owner approval. |
| NG-05 | Do not treat a large species count as sufficient evidence of product quality. | BI-CAP-01, BI-CAP-03, BI-CAP-06 and BI-CAP-07 require source quality, provenance, scientific review and fit-for-purpose validation. | Quality measures must be evidence-based; raw taxon count is not an acceptance criterion by itself. |
| NG-06 | Do not freeze a specific programming language, AI model, database or cloud provider in this PRD. | Cross-cutting; technology selection remains governed by accepted ADRs and explicit architecture decisions, not by capability IDs alone. | This Task 03 non-goal does not reverse accepted ADR-001 (Dart/Flutter) or any other accepted ADR. Other technology/provider choices remain open unless separately decided. |
| NG-07 | Do not claim scientific accuracy targets before a representative evaluation dataset and measurement protocol are defined. | BI-CAP-02 and BI-CAP-15. | Numeric accuracy targets require a representative, rights-eligible evaluation dataset, defined metrics, stratification and an approved protocol. |

These guardrails are not a feature backlog. A proposed scope change must record its rationale, user/scientific need, affected capabilities and requirements, rights/privacy/safety implications, architecture/ADR impact, acceptance evidence and project-owner decision.

### 4.3 Lifecycle-state traceability gap

The Blueprint and Task 03 describe several distinct contribution and review states, including submitted, AI-assisted, user-confirmed, community-supported, expert-reviewed and scientifically verified. They must not be collapsed into one undifferentiated confidence or status field.

The current documents do not yet establish a complete, approved state machine. Before workflow implementation, specify allowed transitions, actors and authority, required evidence, correction and appeal paths, withdrawal/restriction behavior, publication consequences and audit history. This register records the gap; it does not invent or approve transition rules.

### 4.4 Workflow-to-requirements traceability crosswalk

The lifecycle gap is now elaborated in the proposed companion artifact [Workflow-to-Requirements Traceability Crosswalk](WORKFLOW-REQUIREMENTS-TRACEABILITY-CROSSWALK.md) (STF-BI-RTM-WF-001 v0.1). It maps all 16 proposed workflow scenarios to original Task 03 requirements, the 12 acceptance criteria, proposed capability IDs, accepted ADRs and relevant Task 05 dependencies.

The crosswalk is a proposal, not an approval or test report. It explicitly identifies partial and absent coverage, including separate acceptance obligations for AC-011 (AI model replacement) and AC-012 (future STF biodiversity reuse). The original Task 03 requirements and acceptance criteria remain unchanged and authoritative pending owner approval.

The twelve original Task 03 acceptance criteria have also been decomposed into 66 proposed test cases in [Task 03 Product-Baseline Acceptance Test Plan](TASK-03-ACCEPTANCE-TEST-PLAN.md) (STF-BI-ATP-001 v0.1). All cases are **Proposed / Not run**; the plan identifies prerequisite scientific, policy, architecture, rights and privacy decisions. It is a test-design artifact, not evidence of implementation, test execution, scientific validation or release acceptance.

## 5. Original Task 03 functional requirements — controlled traceability

The requirement statements and priorities below are transcribed from Task 03 Section 32. Wording is normalized only for table readability; the original PRD remains authoritative until the project owner approves a canonical revision.

| Requirement ID | Source requirement | Priority | Capability mapping | Architecture / domain mapping | Accepted ADRs | Validation reference / evidence required | Status / gap |
|---|---|---:|---|---|---|---|---|
| ID-001 | User can submit one or more images for a plant identification session. | P1 | BI-CAP-02, BI-CAP-10, BI-CAP-11 | Media intake, identification session, mobile/web clients | ADR-002, 003, 006 | Capture/upload acceptance; multiple media associations; media provenance and rights; failure/retry tests | Not yet verified; rights and media lifecycle must be specified |
| ID-002 | System evaluates image quality before presenting a confident result. | P0 | BI-CAP-02, BI-CAP-15 | Image-quality assessment, inference orchestration | ADR-006, 007 | Reproducible image-quality protocol; low-quality fixtures; abstention/retake behavior; subgroup analysis | Not yet verified; quality thresholds and evaluation protocol open |
| ID-003 | System can request additional evidence when needed. | P1 | BI-CAP-02, BI-CAP-10 | Evidence requirements, guided capture, session state | ADR-006, 007, 009 | Test prompts for diagnostic organs/features; evidence request and response history; no fabricated evidence | Not yet verified; evidence ontology and prompt policy needed |
| ID-004 | System returns ranked candidates with confidence and uncertainty. | P1 | BI-CAP-02, BI-CAP-15 | Candidate generation/ranking, taxonomy resolution, result explanation | ADR-005, 006, 007 | Multi-candidate fixtures; model/pipeline versions; calibrated metric evidence if probability language is used; explicit uncertainty | Not yet verified; score semantics/calibration open |
| ID-005 | Evidence quality is represented separately from AI confidence. | P0 | BI-CAP-02, BI-CAP-06, BI-CAP-15 | Evidence model and inference result model | ADR-006, 007 | Independent evidence-quality and model-score fields; tests proving no conflation in API/UI/analytics | Not yet verified; evidence-quality method requires scientific validation |
| ID-006 | Geographic context can contribute to identification. | P1 | BI-CAP-02, BI-CAP-05 | Geographic context service, distribution assertions, location policy | ADR-005, 006, 008 | Scoped distribution assertions; uncertain location handling; source/time/version provenance; tests against misleading range assumptions | Not yet verified; geography granularity and rights remain dependencies |
| ID-007 | Identification results map to the platform taxonomy and synonyms. | P0 | BI-CAP-01, BI-CAP-02 | TaxonName, TaxonConcept, TaxonomicTreatment, TaxonNameUsage and reconciliation | ADR-004, 005, 010 | LDM-01–04, LDM-10; source-backed taxon fixtures; treatment-aware mapping; no name-string-only identity | Blocked by scientific-model reconciliation and taxonomist review |
| ID-008 | AI inference is distinguished from sourced scientific information. | P0 | BI-CAP-01, BI-CAP-02, BI-CAP-06, BI-CAP-15 | Assertion/evidence/provenance layer; UI/API presentation | ADR-004, 006, 007 | Provenance assertions; AI inference label; source citations; historical model/version; UI/API consistency tests | Not yet verified; display semantics and assertion classes to specify |
| ID-009 | System can return insufficient / unknown / outside-coverage states. | P0 | BI-CAP-02, BI-CAP-15 | Abstention, coverage model, result state machine | ADR-006, 007 | Out-of-coverage and insufficient-evidence fixtures; no forced top-1; safe user explanation; calibration/evaluation report | Not yet verified; coverage definition and decision thresholds open |
| OBS-001 | User can convert an identification into a structured observation. | P1 | BI-CAP-04, BI-CAP-09, BI-CAP-10 | Observation, Identification, Event and Media relationships | ADR-007, 008, 009 | LDM-05–09; create observation with/without taxon determination; attribution and evidence links | Blocked by Task 05 model validation and lifecycle specification |
| OBS-002 | Observation history is retained and traceable. | P1 | BI-CAP-04, BI-CAP-06, BI-CAP-13 | Versioned observation/contribution history and audit | ADR-004, 007, 009 | Append/supersession tests; actor/time/source history; export and retention policy checks | Not yet verified; retention and privacy rules need approval |
| VAL-001 | Eligible observations can enter community / expert review. | P1 | BI-CAP-06, BI-CAP-09, BI-CAP-12 | Eligibility rules, workflow, review queue and authorization | ADR-007, 009 | Role/eligibility tests; review lifecycle; conflict/dispute workflow; community/expert scopes | Not yet verified; reviewer eligibility and governance model open |
| VAL-002 | Expert review preserves decision history. | P1 | BI-CAP-06, BI-CAP-12, BI-CAP-13 | Versioned determination and review audit | ADR-004, 007, 009 | LDM-07; append-only determination history; attribution, evidence, timestamps and supersession | Not yet verified; no mutable overwrite of prior determinations |
| SCI-001 | Authoritative records have provenance and source metadata. | P0 | BI-CAP-01, BI-CAP-03, BI-CAP-06, BI-CAP-07 | SourceRecord, DatasetVersion, IngestionRun, assertions and MediaAsset provenance | ADR-004, 005, 010 | LDM-10, LDM-12, LDM-13, LDM-15; provenance completeness; rights screening; lineage tests | Blocked for some source/model decisions; provenance schema must be reconciled |
| SCI-002 | Taxonomic changes are versioned. | P0 | BI-CAP-01, BI-CAP-06, BI-CAP-07 | TaxonName, TaxonConcept, Treatment, mapping and determination history | ADR-004, 005, 010 | LDM-01–04; historical treatment queries; source-specific taxonomic change fixtures | Blocked by DR-01–04 and expert review |
| SEC-001 | Access is governed by least-privilege authorization. | P0 | BI-CAP-10–BI-CAP-14; cross-cutting | Identity, roles, policy enforcement, API and administrative boundaries | ADR-002, 003, 008 | Role/permission matrix; negative authorization tests; privileged-action audit; security review | Not yet verified; detailed authorization model and threat model required |
| SEC-002 | Location and media controls respect user privacy settings. | P0 | BI-CAP-04, BI-CAP-05, BI-CAP-07, BI-CAP-10, BI-CAP-11, BI-CAP-13 | Media rights/privacy, geospatial disclosure policy, APIs, exports, search and logs | ADR-004, 008, 009, 010 | LDM-11, LDM-12, LDM-15; end-to-end sensitive-location and media-rights tests | Blocked by policy/legal review and implementation of all disclosure paths |
| API-001 | Core capabilities are exposed through versioned contracts. | P0 | BI-CAP-14; all API-consuming capabilities | API gateway/contracts, schemas, versioning and compatibility | ADR-003 | OpenAPI contract tests; authorization; backward compatibility; error and pagination standards | Not yet verified; API inventory and compatibility policy needed |
| OPS-001 | Critical actions and system health are observable / auditable. | P0 | BI-CAP-13, BI-CAP-16; cross-cutting | Audit trail, logs, metrics, traces, security events, model telemetry | ADR-002, 003, 004 | Audit event coverage; observability SLOs; retention/access tests; incident reconstruction exercise | Not yet verified; operational objectives and event taxonomy needed |

## 6. Proposed derived cross-cutting requirements

These are register-level identifiers derived from the narrative requirements in Task 03 Sections 17–28 and related full-product capabilities. They are **not original Task 03 functional IDs**. Owner approval and formal PRD incorporation are required.

| Proposed ID | Source basis | Requirement intent | Capability mapping | ADR / dependency | Acceptance evidence needed |
|---|---|---|---|---|---|
| NFR-PERF-001 | Task 03 §28 Performance | Define measurable latency budgets for each user journey and background workflow; avoid unsupported universal targets | BI-CAP-02, BI-CAP-08, BI-CAP-10, BI-CAP-11, BI-CAP-14, BI-CAP-15 | ADR-002, 003, 006 | Workload model, percentile latency, field-network profile, repeatable benchmark |
| NFR-SCALE-001 | Task 03 §28 Scalability | Scale expensive workloads independently where evidence justifies it; do not infer microservices as a requirement | BI-CAP-07, BI-CAP-14, BI-CAP-15, BI-CAP-16 | ADR-001, 002 | Load model, capacity test, measured bottleneck and extraction rationale |
| NFR-AVAIL-001 | Task 03 §28 Availability | Define capability-specific availability and recovery objectives before production | BI-CAP-10–BI-CAP-16 | ADR-002, 003 | Approved SLO/SLA objectives, monitoring and recovery exercise |
| NFR-REL-001 | Task 03 §28 Reliability | Use appropriate idempotency, retry, durable job handling and recovery for asynchronous workflows | BI-CAP-02, BI-CAP-07, BI-CAP-10, BI-CAP-14, BI-CAP-15 | ADR-002, 003, 010 | Failure injection, retry/idempotency tests, queue recovery and reconciliation |
| NFR-OBS-001 | Task 03 §28 Observability | Provide useful logs, metrics, traces, model telemetry and audit events with privacy/retention safeguards | BI-CAP-13, BI-CAP-15, BI-CAP-16 | ADR-002, 004 | Traceable request/job, model version and actor; redaction and retention tests |
| NFR-MAINT-001 | Task 03 §28 Maintainability | Preserve clear modules, documented contracts and automated tests | All capabilities | ADR-001, 002, 003 | Architecture conformance, test coverage strategy, change-impact and dependency review |
| NFR-PORT-001 | Task 03 §28 Portability | Prefer open contracts and replaceable components; avoid unsupported vendor lock-in claims | BI-CAP-07, BI-CAP-14, BI-CAP-15, BI-CAP-16 | ADR-001, 003, 010 | Portability assessment and tested export/rebuild/replacement paths |
| NFR-COST-001 | Task 03 §28 Cost control | Measure storage, inference, bandwidth, data acquisition and expert-review costs | BI-CAP-02, BI-CAP-06, BI-CAP-07, BI-CAP-10, BI-CAP-15, BI-CAP-16 | ADR-002, 010 | Cost model based on measured workload and unit-cost telemetry |
| NFR-SEC-001 | Task 03 §28 Security; §25 | Apply security-by-design and continuous security testing across clients, APIs, data, media and operations | All capabilities | ADR-002, 003, 008 | Threat model, security test plan, dependency/secrets scanning and remediation evidence |
| NFR-ACC-001 | Task 03 §28 Accessibility; §22 | Define measurable accessibility requirements for supported web/mobile interfaces; status and confidence cannot rely on color alone | BI-CAP-08–BI-CAP-13 | ADR-001, 003 | Manual and automated accessibility assessment, assistive-technology test records |
| NFR-DATA-001 | Task 03 §28 Data integrity; §26 | Preserve versioning, provenance, controlled mutation and scientific history | BI-CAP-01, BI-CAP-04, BI-CAP-06, BI-CAP-07 | ADR-004, 005, 007, 009, 010 | Data integrity suite, lineage checks, historical reconstruction and migration tests |
| UX-MOB-001 | Task 03 §17, §20 | Support camera/gallery capture, multiple images, guided prompts, permission explanations, field usability, offline queues and sync status | BI-CAP-02, BI-CAP-04, BI-CAP-10 | ADR-006, 008, 009 | Device and low-connectivity tests; permission denial; interrupted upload/sync recovery |
| UX-WEB-001 | Task 03 §18 | Support responsive public exploration, search, maps, accounts, expert/admin and research interfaces with appropriate access | BI-CAP-03, BI-CAP-08, BI-CAP-11–14 | ADR-002, 003 | Journey tests across roles, devices and accessibility modes |
| API-CON-001 | Task 03 §19 | Document authentication, authorization, rate limiting, structured endpoints, machine-readable contracts and compatibility policy | BI-CAP-14 | ADR-003 | Contract tests, security tests, API lifecycle policy |
| OFFLINE-001 | Task 03 §20 | Define offline reference-data caching, queued observations, sync conflict handling, storage limits and privacy | BI-CAP-04, BI-CAP-10 | ADR-008, 009 | Offline/online transition tests; duplicate prevention; conflict resolution; local data protection |
| I18N-001 | Task 03 §21 | Separate language content from scientific identifiers; model common names with language and source; support localization architecture | BI-CAP-01, BI-CAP-03, BI-CAP-08–11 | ADR-004, 005 | Language metadata tests, script/search tests, reviewed translations for scientific claims |
| NOTIF-001 | Task 03 §23 | Make notifications consent-aware, configurable and tied to meaningful workflow/security events | BI-CAP-06, BI-CAP-09, BI-CAP-10, BI-CAP-13 | ADR-002, 003, 009 | Preference, consent, delivery, unsubscribe and duplicate-notification tests |
| ANALYTICS-001 | Task 03 §24 | Measure identification failures, uncertainty, corrections, expert review, observation, sync and model/data performance with minimization | BI-CAP-02, BI-CAP-04, BI-CAP-06, BI-CAP-15, BI-CAP-16 | ADR-004, 006, 007, 009 | Metric definitions, privacy review, data minimization, cohort/coverage reporting |
| PRIV-001 | Task 03 §25; Blueprint §8 | Define account/data lifecycle, consent, location precision, children's data and retention/deletion policy by applicable legal context | BI-CAP-04, BI-CAP-05, BI-CAP-09–14 | ADR-008, 009; legal review | Data inventory, lawful-basis/consent analysis where applicable, lifecycle and access tests |
| DER-SCI-001 | Task 03 §26 | Record taxonomic sources, geographic assertion provenance, versioned taxonomy and source-vs-inference distinctions | BI-CAP-01, BI-CAP-03, BI-CAP-05, BI-CAP-07 | ADR-004, 005, 010 | Provenance completeness and treatment-version tests |
| RIGHTS-001 | Task 03 §26; Blueprint §8 | Track rights at asset and purpose level, including source dataset, embedded media and AI use; unknown rights must not be treated as permission | BI-CAP-02, BI-CAP-03, BI-CAP-07, BI-CAP-09, BI-CAP-15 | ADR-004, 010; licensing policy review | Asset-level rights fixtures and denied-use tests; LDM-12, LDM-15 |
| AI-001 | Task 03 §27 | Keep AI modular and replaceable; retain model/pipeline/version and training/evaluation provenance | BI-CAP-02, BI-CAP-15 | ADR-001, 006, 007 | Model registry, reproducible inference and rollback/replacement test |
| AI-002 | Task 03 §27 | Evaluate across India-relevant geography, taxonomic groups, plant organs and field image conditions; monitor false confidence | BI-CAP-02, BI-CAP-15 | ADR-006, 007; dataset rights gate | Representative dataset protocol, subgroup report, calibration/abstention analysis |
| AI-003 | Task 03 §27 | Human feedback must not automatically become scientific ground truth; controlled model/data release required | BI-CAP-06, BI-CAP-09, BI-CAP-12, BI-CAP-15 | ADR-004, 006, 007, 009 | Feedback provenance, reviewer workflow, release approval and rollback evidence |
| ADMIN-001 | Task 03 §16, §29 | Separate user/role administration, moderation, source/taxonomy curation, publishing, audit, data quality and security visibility | BI-CAP-12, BI-CAP-13, BI-CAP-16 | ADR-002, 003, 004 | Role-based admin acceptance tests and complete privileged-action audit |
| DATA-ING-001 | Task 03 §26; Task 04 §§3–4 | Preserve source identity, dataset version, ingestion run, transformation and source-specific limitations | BI-CAP-01, BI-CAP-07 | ADR-004, 005, 010 | LDM-13, LDM-15; idempotent ingestion and lineage tests |
| GEO-001 | Task 03 §17, §25, §26 | Preserve location precision, source geography, boundary versions and public disclosure policy | BI-CAP-04, BI-CAP-05, BI-CAP-10, BI-CAP-11 | ADR-008, 009 | LDM-10, LDM-11, LDM-14; API/search/export/log/media tests |

**Identifier note:** `DER-SCI-001` is deliberately distinct from original `SCI-001`; the `DER-` prefix marks it as a derived proposal and avoids reusing the source requirement ID. The proposed derived requirements must be normalized during PRD revision to avoid overlapping or duplicate obligations.

## 7. Task 04 architecture responsibility crosswalk

Task 04 v0.1 proposes architecture domains and technologies. The mapping below records responsibility, not a new deployment or vendor decision.

| Architecture responsibility in Task 04 | Capability mapping | Relevant requirements | Governing ADRs | Decision status / guardrail |
|---|---|---|---|---|
| Identity, authentication, roles and permissions | STF shared-platform cross-cutting capability; no BI-CAP identifier assigned | SEC-001, PRIV-001, ADMIN-001 | ADR-002, 003 | The operating prompt assigns reusable identity/access foundations to STF shared platform. Detailed identity provider, role model and authorization policy remain open; Botanica domain permissions remain Botanica-owned. |
| Taxonomy and species knowledge | BI-CAP-01, BI-CAP-03 | ID-007, SCI-001, SCI-002, DER-SCI-001 | ADR-004, 005, 010 | Scientific model blockers remain |
| Geography and spatial intelligence | BI-CAP-04, BI-CAP-05 | ID-006, SEC-002, GEO-001 | ADR-008, 009 | Sensitive location and historical boundary requirements |
| Media storage and processing | BI-CAP-02, BI-CAP-04, BI-CAP-07, BI-CAP-10 | ID-001, SEC-002, RIGHTS-001 | ADR-004, 008, 010 | Rights per asset/purpose; original/derivative distinction |
| Evidence | BI-CAP-02, BI-CAP-06, BI-CAP-15 | ID-002, ID-003, ID-005, ID-008 | ADR-006, 007 | Evidence is a domain object; no conflation with confidence |
| Identification and AI orchestration | BI-CAP-02, BI-CAP-15 | ID-002–ID-009, AI-001–AI-003 | ADR-006, 007 | Model/provider replaceability; evaluation and abstention |
| Observations and field records | BI-CAP-04, BI-CAP-09, BI-CAP-10 | OBS-001, OBS-002, OFFLINE-001 | ADR-008, 009 | Task 05 Event/Occurrence/Observation semantics remain under review |
| Community and expert validation | BI-CAP-06, BI-CAP-09, BI-CAP-12 | VAL-001, VAL-002 | ADR-007, 009 | Expert governance and contribution states open |
| Search and discovery | BI-CAP-08, BI-CAP-11, BI-CAP-14 | API-001, I18N-001, GEO-001 | ADR-002, 003, 005 | Search index is derived/rebuildable; engine not selected |
| Data ingestion and integrations | BI-CAP-07, BI-CAP-14 | SCI-001, SCI-002, RIGHTS-001, DATA-ING-001 | ADR-004, 005, 010 | Source rights, provenance and mapping are gating |
| Notifications | BI-CAP-09, BI-CAP-10, BI-CAP-13 | NOTIF-001 | ADR-002, 003, 009 | Provider and event taxonomy open |
| Audit and observability | BI-CAP-13, BI-CAP-16 | OPS-001, NFR-OBS-001 | ADR-002, 003, 004 | Telemetry must not leak personal/sensitive location data |
| Mobile client | BI-CAP-10 | UX-MOB-001, OFFLINE-001, I18N-001 | ADR-001, 003, 006, 008, 009 | **Flutter governs under accepted ADR-001.** Task 04 React Native recommendation is historical candidate material only. |
| Web client | BI-CAP-11–BI-CAP-13 | UX-WEB-001, NFR-ACC-001 | ADR-001, 002, 003 | React/Next.js remains a candidate unless separately accepted |
| API platform | BI-CAP-14 | API-001, API-CON-001, SEC-001 | ADR-003 | API-first accepted; specific API gateway/provider open |
| AI/ML research and operations | BI-CAP-15 | ID-002–ID-009, AI-001–AI-003 | ADR-006, 007 | Model hosting, framework and vector/search components open |
| Infrastructure, CI/CD and operations | BI-CAP-16 | NFR-AVAIL-001, NFR-REL-001, NFR-COST-001, OPS-001 | ADR-001, 002 | Avoid premature microservices/Kubernetes and vendor commitment |

## 8. Scientific-model dependency and validation mapping

The following dependencies are drawn from the Scientific Data Model Review Pack and Validation Matrix fetched from branch `review/scientific-data-model-review-pack`. Their proposed-document revisions do not mean the findings are closed.

### 8.1 DR findings

| Finding | Severity / current disposition | Requirement groups affected | Capability impact | Required closure evidence |
|---|---|---|---|---|
| DR-01 — internal Occurrence validity coupled to export fields | Blocking; proposed documents revised, tests still required | OBS-001, OBS-002, SCI-001, GEO-001 | BI-CAP-04, BI-CAP-05, BI-CAP-07 | Internal occurrence fixtures independent of Darwin Core export; valid loss-aware export mapping |
| DR-02 — polymorphic subject references vs typed subject links | Blocking; proposed typed pattern exists, enforcement needs validation | ID-008, VAL-002, SCI-001 | BI-CAP-01, BI-CAP-04, BI-CAP-06 | Referential-integrity design and total-participation enforcement tests |
| DR-03 — TCS mapping relation vocabulary | Blocking; six relation terms now specified, taxonomist review remains | ID-007, SCI-002 | BI-CAP-01, BI-CAP-07 | Relation direction, semantics, fixture and round-trip mapping review |
| DR-04 — TCS accordingTo resource | Blocking; canonical resource approach proposed | ID-007, SCI-001, SCI-002 | BI-CAP-01, BI-CAP-07 | Single canonical resource invariant, uniqueness/FK and treatment resolution tests |
| DR-05 — taxonomy relationship families | Major; revised in proposals, review still needed | ID-007, SCI-002 | BI-CAP-01 | Separate concept-to-name synonym, name-to-name nomenclatural and concept-to-concept mapping tests |
| DR-06 — mutable taxon determination on Occurrence | Major; current determination proposed as derived from Identification | ID-007, OBS-002, VAL-002 | BI-CAP-01, BI-CAP-04, BI-CAP-06 | Read-model and API consistency; determination history tests |
| DR-07 — Occurrence/Event/non-detection semantics | Major; revised wording and LDM-16 proposed, semantic validation remains | OBS-001, OBS-002, SCI-001, GEO-001 | BI-CAP-04, BI-CAP-05 | Event/Survey protocol, effort, target, location and absence-vs-no-record tests |
| DR-08 — Mango native-range geographic scale | Major; open source/geographic-resolution case | ID-006, DER-SCI-001, GEO-001 | BI-CAP-01, BI-CAP-05, BI-CAP-07 | Normalize source scopes and comparable geographic units; botanical review |
| DR-09 — Darwin Core version metadata | Open — indexed TDWG metadata reports List and Conceptual Model issue date 2026-10-13 (previous 2026-05-26); direct List HTML and core term-list snapshot return 2026-05-26; exact versioned resources and term IRIs unresolved | API-001, SCI-001, DATA-ING-001 | BI-CAP-07, BI-CAP-14 | Retrieve and compare exact versioned documents and relevant term IRIs; keep document, namespace and term dates distinct |
| DR-10 — canonical source record identifiers | Major; canonical SourceRecord linkage proposed | SCI-001, DATA-ING-001 | BI-CAP-01, BI-CAP-07 | Namespace, dataset version and ingestion-run uniqueness constraints |
| DR-11 — TCS synonym target | Major; mapping clarified as TaxonConcept to TaxonName | ID-007, SCI-002 | BI-CAP-01 | TCS mapping fixture; retain TaxonNameUsage separately |
| DR-12 — source authority/evidence classes | Major; source metadata expanded in proposals | ID-008, SCI-001, RIGHTS-001 | BI-CAP-01, BI-CAP-03, BI-CAP-07 | Source role, editorial model, scope, date, limitation and rights evidence |

### 8.2 LDM-01 to LDM-16 coverage

The review pack's 16 logical-model scenarios are validation obligations, not test execution claims.

| Scenario | Main requirement groups | Capability domains | Required proof |
|---|---|---|---|
| LDM-01 — same TaxonName in two treatments | ID-007, SCI-002 | BI-CAP-01 | Distinct treatment-scoped concepts; no name-string merge |
| LDM-02 — multiple synonym names | ID-007, SCI-002 | BI-CAP-01 | Synonym targets are TaxonName; usages retained |
| LDM-03 — partially overlapping concepts | ID-007, SCI-002 | BI-CAP-01, BI-CAP-07 | Typed mapping, direction, according-to source |
| LDM-04 — basionym and nomenclatural type | ID-007, SCI-002 | BI-CAP-01 | Separate name relation and type-specimen structure |
| LDM-05 — observation without identification | OBS-001, OBS-002 | BI-CAP-04 | Valid observation/media without fabricated taxon |
| LDM-06 — multiple AI candidates | ID-004, ID-009 | BI-CAP-02, BI-CAP-15 | Multiple candidates; no automatic confirmation |
| LDM-07 — expert changes identification | VAL-002, OBS-002, ID-008 | BI-CAP-06, BI-CAP-12 | New determination; old AI/expert history retained |
| LDM-08 — repeated Occurrences for one Organism | OBS-001, OBS-002 | BI-CAP-04 | Identity evidence and valid cardinality |
| LDM-09 — MaterialEntity and multiple MediaAssets | ID-001, SCI-001, RIGHTS-001 | BI-CAP-04, BI-CAP-07 | Distinct evidence paths and media rights |
| LDM-10 — conflicting native-range sources | ID-006, DER-SCI-001 | BI-CAP-01, BI-CAP-05, BI-CAP-07 | Separate scoped DistributionAssertions |
| LDM-11 — sensitive rare-plant locality | SEC-002, GEO-001, PRIV-001 | BI-CAP-05, BI-CAP-10–14 | Generalization/withholding across API, export, search, logs, media and backups |
| LDM-12 — dataset and media rights differ | SCI-001, RIGHTS-001 | BI-CAP-07, BI-CAP-15 | Independent asset/purpose rights decision and denied-use tests |
| LDM-13 — re-ingestion and stable identifiers | SCI-001, DATA-ING-001 | BI-CAP-07 | New DatasetVersion/IngestionRun; idempotency and lineage |
| LDM-14 — district boundary history | ID-006, GEO-001 | BI-CAP-05, BI-CAP-07 | Versioned boundary; historic evidence not rewritten |
| LDM-15 — restricted raw payload | SCI-001, RIGHTS-001, PRIV-001 | BI-CAP-07, BI-CAP-13 | No prohibited payload in storage, logs, backups; permitted metadata only |
| LDM-16 — explicit survey non-detection | OBS-001, OBS-002, GEO-001 | BI-CAP-04, BI-CAP-05 | Defined survey/event, protocol, effort, target, time and place; missing record remains unknown |

### 8.3 Mandatory validation rule

A scenario is not closed because:
- the model document describes the intended solution;
- a diagram appears plausible;
- a PR is mergeable;
- a field or constraint is proposed;
- a test case is written but not executed;
- an informal review has occurred without a recorded reviewer decision.

Closure requires reproducible evidence, the appropriate discipline review, exact source/model revision, outcome, limitations and recorded disposition. A justified Not Applicable outcome must include rationale and approval.

### 8.4 ODR-01 — controlled external-export traceability

ODR-01 is an owner-authorized policy decision recorded in the Scientific Data Model Validation Matrix and Decision Register (ref `review/scientific-data-model-review-pack`, blob `3a33dfe47657a96456f56f2c12a0b7d355b6c6a5`). It authorizes Option B for controlled, profile-specific external exports only. It does not approve a final export profile, Task 05C/05D/05E, physical schema, API payload or implementation.

| ODR-01 obligation / validation cases | Requirement and capability trace | Required treatment in this register |
|---|---|---|
| Internal missing Occurrence row; EVT-37 | OBS-001/OBS-002; BI-CAP-04 | Remains unknown/not assessed. No internal absence assertion or negative Occurrence may be created from an empty result set. |
| Explicit internal survey result; EVT-36 | OBS-001/OBS-002; BI-CAP-04/05 | Requires explicit attributable evidence and defined Survey/Event, target, method, effort, time/place and agent. Keep separate from export interpretation. |
| Eligible profile-specific implicit export; EVT-27, EVT-30 | SCI-001, GEO-001; BI-CAP-04/05/07/14 | Only an approved, pinned external profile and validated mapping may generate the bounded “not detected/reported within the stated survey scope under documented survey conditions” interpretation. |
| Fail-closed completeness/method conditions; EVT-28, EVT-31, EVT-38 | SCI-001; BI-CAP-04/07/14 | Missing, incomplete, unreported, ambiguous or contradictory required evidence suppresses the interpretation. Reporting completeness, survey effort and detectability remain distinct. |
| Hierarchy and explicit scope at each applicable level; EVT-29, EVT-32, EVT-39, EVT-43, EVT-44 | OBS-001/OBS-002, GEO-001; BI-CAP-04/05 | Preserve Event/Survey hierarchy, spatiotemporal containment and explicit scope. No silent inheritance, child-to-parent completeness derivation or unjustified relationship. |
| A priori/post-facto target origin and bycatch; EVT-33, EVT-34, EVT-35, EVT-40 | OBS-001/OBS-002; BI-CAP-04/07 | Preserve target origin, author, method and timestamp. Bycatch and out-of-scope taxa do not satisfy target reporting completeness. |
| Material/media and multiple-organism edge cases; EVT-41, EVT-42 | ID-001, OBS-001, SCI-001; BI-CAP-04/07 | Keep MaterialEntity, MediaAsset, Observation, Organism and Occurrence distinct; retain grouping uncertainty and provenance. |
| Term/profile/version pins; EVT-30 and DR-09 | SCI-001, DATA-ING-001; BI-CAP-07/14 | Pin exact profile, mapping, term and controlled-value versions. DR-09 remains open pending exact versioned-resource comparison. |

**Traceability rule:** an internal absence state is never inferred from missing data. The external interpretation is generated only in a controlled export transformation after every applicable ODR-01 condition has been verified. If any condition is missing or unresolved, omit the interpretation. EVT-27–EVT-44 are proposed validation obligations, not executed tests; the internal Survey/Occurrence model and export profile remain open scientific/architecture gates.

## 9. Acceptance criteria traceability

Task 03 Section 33 includes twelve product-baseline acceptance criteria. These should be retained and converted into separately executable acceptance cases in the test plan.

| AC ID (proposed) | Task 03 acceptance criterion | Requirement links | Capability | Evidence |
|---|---|---|---|---|
| AC-001 | User completes guided identification from image capture/upload to a result or explicit unknown/insufficient-evidence state | ID-001–ID-004, ID-009 | BI-CAP-02, BI-CAP-10 | End-to-end journey tests including failure and abstention |
| AC-002 | System does not represent AI confidence as scientific certainty | ID-004, ID-005, ID-008 | BI-CAP-02, BI-CAP-06, BI-CAP-15 | UI/API semantic review and model score documentation |
| AC-003 | Results show alternatives and supporting evidence | ID-004, ID-005, ID-008 | BI-CAP-02, BI-CAP-06 | Multi-candidate/evidence fixtures |
| AC-004 | User can create a structured observation from an identification | OBS-001 | BI-CAP-04, BI-CAP-10 | Observation workflow test |
| AC-005 | Observation can enter review without automatically changing authoritative species record | VAL-001, VAL-002, OBS-002 | BI-CAP-04, BI-CAP-06, BI-CAP-12 | Authorization and determination separation tests |
| AC-006 | Species information displays accepted name, taxonomy, distribution and provenance when data exists | ID-007, ID-008, SCI-001, SCI-002 | BI-CAP-01, BI-CAP-03, BI-CAP-05 | Source-backed profile fixtures and provenance completeness |
| AC-007 | Taxonomic changes are versioned | SCI-002 | BI-CAP-01 | Treatment and version history test |
| AC-008 | Admin/expert permissions differ from ordinary user permissions | SEC-001, VAL-001, ADMIN-001 | BI-CAP-12, BI-CAP-13 | Role matrix and negative authorization tests |
| AC-009 | Core APIs are versioned and documented | API-001 | BI-CAP-14 | OpenAPI and compatibility tests |
| AC-010 | Location, media and account data have defined privacy controls | SEC-002, PRIV-001, RIGHTS-001, GEO-001 | BI-CAP-04, BI-CAP-05, BI-CAP-07, BI-CAP-10–14 | End-to-end privacy/rights tests and approved policy |
| AC-011 | Architecture supports replacing AI model without redesigning the entire product | AI-001, AI-003 | BI-CAP-02, BI-CAP-15 | Model adapter/contract test and replacement exercise |
| AC-012 | Data model can support future STF biodiversity projects | NFR-MAINT-001, NFR-PORT-001, SCI-001 | BI-CAP-01, BI-CAP-07, BI-CAP-14 | Domain boundary review; no assumption that Botanica domain semantics become universal STF schema |

## 10. Open decisions and requirement gaps

These issues must be assigned an owner, evidence requirement and decision date by the project owner. Dates are intentionally not invented here.

| Open item | Source | Affected traceability | Current position | Required next action |
|---|---|---|---|---|
| India taxonomic authorities and reconciliation policy | Task 03 §35; ADR-005 | ID-007, SCI-002 | Open; multiple source roles must remain distinguishable | Scientific governance proposal and taxonomist review |
| Dataset/media rights for storage, display, redistribution and AI | Task 03 §35; ADR-004, 010 | SCI-001, RIGHTS-001, AI-001 | Open; public accessibility is not permission | Asset-specific rights matrix and legal review |
| Representative Indian evaluation dataset | Task 03 §35; ADR-006, 007 | ID-002–ID-009, AI-002 | Open | Dataset protocol, coverage and rights evidence |
| Geographic precision and sensitive-location tiers | Task 03 §35; ADR-008 | ID-006, SEC-002, GEO-001 | Open | Threat model and disclosure policy |
| Expert governance and reviewer qualification | Task 03 §35; ADR-007 | VAL-001, VAL-002 | Open | Expert role, conflict, attribution, appeal and accountability policy |
| Priority Indian languages | Task 03 §35 | I18N-001 | Architecture should support localization; rollout not approved | Language research and content governance |
| Offline identification scope | Task 03 §35 | UX-MOB-001, OFFLINE-001 | Open | Field connectivity, storage, privacy and model feasibility study |
| Evidence-quality methodology | Task 03 §35; ADR-007 | ID-003, ID-005 | Open | Scientific protocol, repeatability and validation |
| AI production baseline | Task 03 §35; ADR-006 | ID-004, ID-009, AI-001–003 | Open | Comparative evaluation with rights-cleared data |
| Performance, availability and cost objectives | Task 03 §35 | NFR-PERF, NFR-AVAIL, NFR-COST | Open | Workload and operating-cost model |
| Sustainability model | Task 03 §35 | NFR-COST-001; operations | Open | Organizational/financial assessment; no commercial assumption |
| STF shared vs Botanica-owned capabilities | Operating Prompt §2; Task 03 §35; Blueprint §3 | All capability mappings | Governing logical boundary: STF provides reusable identity/access foundations; Botanica owns botanical taxonomy, knowledge, identification, observation, evidence and scientific governance | Do not infer separate repositories, teams, deployments or a final organizational operating model from logical boundaries; review remaining shared primitives as needed |
| Identity provider and detailed authorization | Task 04 | SEC-001, API-CON-001 | Open | Threat model, role/policy model, vendor-neutral evaluation |
| Web framework | Task 04 | UX-WEB-001 | React/Next.js candidate only | Evaluate after UX, accessibility and maintainability requirements |
| Search engine | Task 04 | Discovery, multilingual, geographic requirements | Open; derived/rebuildable index | Benchmark representative exact-name, multilingual, semantic and geo workloads |
| Cloud, storage, queue and orchestration providers | Task 04 | NFR-REL, COST, PORT, OPS | Open | Cost, portability, security and operational capability assessment |
| Legal applicability for personal/community/biodiversity data | Task 03 §25; Blueprint §8 | PRIV-001, RIGHTS-001, SEC-002 | Not a legal opinion | Current Indian legal review and qualified advice |

## 11. Cross-document consistency rules

1. Task 03 is the source for original requirements and acceptance criteria until the owner accepts a revised PRD.
2. The Full Product Vision and Capability Blueprint defines the proposed full-product capability structure; it does not replace detailed requirements.
3. Task 04 is an architecture evaluation; technology candidates are not approvals.
4. Accepted ADR-001 through ADR-010 govern approved architecture decisions. In particular:
   - Flutter remains the accepted mobile direction under ADR-001.
   - Modular architecture does not imply one microservice per capability (ADR-002).
   - API-first contracts remain a platform principle (ADR-003).
   - Provenance is a core data property (ADR-004).
   - Taxonomic source reconciliation remains treatment-aware (ADR-005).
   - Identification remains an evidence-aware pipeline (ADR-006).
   - Evidence and expert validation remain distinct (ADR-007).
   - Sensitive geographic data requires end-to-end controls (ADR-008).
   - Observation and contributions remain distinct records (ADR-009).
   - Ingestion preserves source identity and lineage (ADR-010).
5. Task 05 proposals and their DR/LDM reviews constrain scientific implementation. The register does not close them.
6. The Task 04 historical ADR numbering proposal is not imported. Repository ADR identifiers remain authoritative.
7. The same requirement must not be duplicated under different identifiers without an explicit relationship (refines, decomposes, constrains, supersedes).
8. A requirement change must record source, rationale, affected capability, ADR, tests, data/rights implications, approval and supersession history.

## 12. Governance, ownership and change control

### 12.1 Roles to assign

The following are role placeholders, not named appointments:
- Product owner / decision authority.
- Botanical taxonomist.
- Field botanist / ecologist.
- Biodiversity informatician.
- Data architect / geospatial architect.
- AI/ML reviewer.
- Security and privacy reviewer.
- Data rights / legal reviewer.
- Accessibility reviewer.
- Engineering and operations owner.
- Community knowledge governance representative, where relevant.

No role is considered filled and no independent review is claimed until an actual reviewer and review record exist.

### 12.2 Change record fields

Every requirement change should record:
- Requirement ID and version.
- Previous and proposed text.
- Change type: add / clarify / split / merge / retire / supersede.
- Source and rationale.
- Impacted capabilities, journeys, architecture modules and ADRs.
- Scientific/data model implications.
- Rights/privacy/security implications.
- Acceptance/test impact.
- Decision authority, date and status.

### 12.3 Requirement quality gate

Before a requirement is accepted, confirm it is:
- necessary and within approved product boundaries;
- unambiguous and testable;
- traceable to a user/stakeholder or scientific need;
- consistent with accepted ADRs and standards;
- feasible without violating rights/privacy/community safeguards;
- assigned an owner and acceptance evidence;
- consistent with related requirements and source records.

## 13. Recommended next actions

1. Owner reviews the proposed canonical `BI-CAP-01`–`BI-CAP-16` identifiers, the legacy crosswalks and the 19 preserved Task 03 requirement mappings.
2. Review the seven Task 03 non-goals as scope guardrails; approve, reject or revise any proposed derived cross-cutting requirements without silently adding them to the PRD.
3. Assign role owners and reviewers; no names are assumed.
4. Reconcile DR-01 through DR-04 and then DR-05 through DR-07 before physical data design.
5. Correct and re-verify DR-09 source/version references.
6. Link every accepted requirement to test specifications and LDM/discipline review evidence.
7. Produce a canonical PRD revision only after the requirement changes and ownership are approved.
8. Maintain this register as a controlled companion document and update it with each approved change.

## 14. Current decision summary

| Item | Status |
|---|---|
| Original Task 03 functional IDs | Preserved in this proposed register |
| Canonical proposed capability IDs BI-CAP-01–BI-CAP-16 | Crosswalked to legacy IDs; proposed, not yet accepted |
| Derived NFR / UX / data / AI / rights IDs, including DER-SCI-001 | Proposed; not original PRD requirements; SCI-001A retained as a legacy alias |
| Accepted ADR-001–ADR-010 | Inspected; unchanged |
| Task 03 PRD | Working baseline; not accepted |
| Task 04 architecture evaluation | Working baseline; not accepted |
| Full Product Blueprint v0.2 | Proposed in PR #17; capability identifiers aligned with Sections 5.1–5.16; not accepted |
| DR-01–DR-12 | Review findings; not all closed |
| Task 03 explicit non-goals NG-01–NG-07 | Transcribed as scope guardrails; any change remains subject to owner approval |
| Lifecycle state machine | Gap recorded; transition rules not yet specified or approved |
| LDM-01–LDM-16 | Validation obligations; execution evidence not established by this register |
| Implementation status | Not assessed / not claimed |
| Physical database design readiness | Not ready pending scientific-model gates and review |

---

**End of proposed register — v0.3.**


### DR-09 source metadata update (20 November 2026)

Latest indexed official TDWG metadata reports 2026-10-13 as the issue date for both the Darwin Core List of Terms and Conceptual Model, with 2026-05-26 as the previous version. Direct HTML retrieval of the List page and the core dwc: term-list snapshot returned 2026-05-26 metadata. Exact versioned resources and relevant term IRIs have not yet been verified. DR-09 remains open; do not close it on date metadata alone.

 
## 15. Attached research review and standards-source correction — 21 November 2026

The September 2026 Master Checklist, Task 01 Charter v0.1, Task 02 Problem & Opportunity Analysis and architecture/UI/UX/effort-estimation study were reviewed as working inputs. They do not add approved requirements. Their useful concepts map to existing proposed requirements/capabilities:
- India-first botanical intelligence and taxonomic knowledge: BI-CAP-01 / BI-CAP-03.
- Evidence Engine, photo guidance, uncertainty and abstention: BI-CAP-02; preserve Task 03 ID-005's separation of identification confidence from evidence quality.
- Observation, field documentation and community participation: BI-CAP-04 / BI-CAP-09.
- Geography and ecological context: BI-CAP-05.
- Expert review and scientific governance: BI-CAP-06.
- Rights-aware ingestion and interoperability: BI-CAP-07 / BI-CAP-14 and RIGHTS-001.
- Mobile, web, expert/admin and APIs: BI-CAP-10–BI-CAP-14.
- AI/ML evaluation and operations: BI-CAP-15.
- Analytics/observability: BI-CAP-16.

The proposed “Evidence Score” must not become one universal scalar. Preserve separate model-score/calibration, evidence-quality/completeness, taxonomic support, geographic plausibility and expert-determination states. The 4,250–5,850 hour estimate is not a budget or schedule. The legacy task numbering must not be used to create a duplicate Task 04; current repository Task 04 is System Architecture & Technology Evaluation and Task 05 is Data Architecture/Scientific Data Model.

### DR-09 source correction

- Darwin Core Conceptual Model: current official indexed metadata reports 2026-10-13; direct HTML page remains cached at 2026-05-26; exact versioned document retrieval remains open.
- Darwin Core List of Terms document: direct official page reports 2026-05-26.
- Core `dwc:` vocabulary snapshot: 2026-10-13.
- `dwc:occurrenceStatus`: term version 2026-05-26; recommended `detected` / `notDetected`.
- Humboldt hierarchy guidance: v2024-02-28, Section 3 normative.
- Humboldt Extension terms and controlled values have individual version dates; `eco:isTaxonomicScopeFullyReported` and `eco:isSurveyTargetFullyReported` are distinct; `eco:taxonCompletenessReported` and `eco:taxonCompletenessProtocols` must be version-pinned separately.
- For ODR-01, incomplete or unreported completeness and absent method evidence must fail closed under the project policy; scope, reporting completeness, sampling effort and detectability remain distinct.

DR-09 remains OPEN pending exact versioned-resource retrieval and term-by-term comparison. No requirements are approved or tests executed by this research review.
