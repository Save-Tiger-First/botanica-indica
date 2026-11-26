# Task 03 — Product Requirements Document (PRD) v0.1

**Document ID:** STF-BI-PRD-003  
**Repository status:** Working baseline / source-preserving transcription for owner review  
**Source:** Project Library original DOCX; see governance overlay at end.  

> This repository transcription preserves the complete extracted source text. It is not yet an accepted PRD. The original DOCX remains the preserved source artifact.

---

SAVE TIGER FIRST
Botanical Intelligence Platform
Task 03 — Product Requirements Document (PRD) v0.1
India-first • Evidence-based • Scientifically grounded • Reusable STF infrastructure
Document Item Value
Document status Working baseline / v0.1
Project Save Tiger First — Botanical Intelligence Platform
Primary entry point Interactive plant identification
Strategic scope Full-fledged production platform; not an MVP
Architecture principle Reusable/shared infrastructure for future STF 
projects
Technology decision Not frozen in this document
Primary geography India, with architecture capable of later expansion
Next major phase System architecture, data architecture, technology 
evaluation and UX specification
1. Purpose of This PRD
This Product Requirements Document converts the previously agreed project charter and 
opportunity analysis into a more precise product specification. Its purpose is to define what the 
platform should do, who it serves, how major workflows behave, and what quality, scientific, 
security, accessibility and operational expectations must be met before architecture and 
technology are frozen.
This is deliberately a full-platform requirements document. It does not reduce the project to a 
minimum viable product. At the same time, requirements are separated into priority levels so 
implementation can be sequenced without weakening the long-term product architecture.
2. Product Vision
Create an India-first Botanical Intelligence Platform that helps people identify, understand, 
explore, document and validate plants using images, geography, morphology, taxonomy, scientific 
knowledge and human expertise.
The platform should evolve beyond a simple image-to-name tool into reusable biodiversity 
infrastructure for Save Tiger First.

3. Product Positioning
The platform is The platform is not
India-first botanical intelligence A Google Lens clone
Evidence-based identification AI-only identification
Scientifically grounded and source-aware An unverified crowdsourced database
Interactive identification workflow A single-shot image classifier only
A reusable biodiversity technology foundation A plant-care-only application
Designed for public, education, field, expert and 
research use A social feed or marketplace
4. Product Principles
 Scientific integrity before apparent certainty.
 The platform must be allowed to say “I don't know,” “insufficient evidence,” or “outside current
coverage.”
 AI confidence and evidence quality are separate concepts and should not be conflated.
 Every scientifically important data point should have provenance where practical.
 Identification should use multiple evidence dimensions rather than image similarity alone.
 Human confirmation and expert review are first-class workflows, not afterthoughts.
 Geography is a core identification signal and knowledge dimension.
 Taxonomy must be versioned and reconcilable rather than treated as a static list.
 User contributions should improve the knowledge base without allowing uncontrolled 
degradation of scientific quality.
 The platform should be modular so individual AI models, search engines, databases and 
interfaces can be replaced.
 Shared infrastructure should be reusable across future Save Tiger First biodiversity projects.
 Privacy, accessibility, security, observability and maintainability are product requirements, not
only engineering concerns.
5. Target Users and Personas
Persona Primary need Key capabilities
General public Identify an unfamiliar plant and 
understand what it is
Capture/upload, identification, 
evidence, species profile, 
save/share
Student / learner Learn plant diversity and 
terminology
Guided ID, explanations, 
taxonomy, glossary, learning 
content
Plant enthusiast Explore and document plants Identification, observations, 
collections, maps, history
Field professional Reliable field identification and 
records
Offline-capable workflows, 
GPS/context, observations, 
exports
Researcher Structured, traceable biodiversity 
data
Advanced search, provenance, 
observation datasets, API/export

Botanical expert Review and validate difficult 
identifications
Expert queue, evidence review, 
taxonomy tools, comments
Scientific/data curator Maintain authoritative 
knowledge
Sources, taxonomy, species 
profiles, provenance, versioning
Administrator Operate and govern the platform Users, roles, moderation, audit, 
system controls, analytics
AI/ML/data team Improve identification systems 
safely
Datasets, evaluation, model 
versions, feedback and 
monitoring
6. Product Scope
6.1 Core product domains
 Identify — interactive plant identification.
 Explore — search and browse species, taxonomy, geography and observations.
 Observe — create structured field observations.
 Learn — understand plant characteristics, taxonomy, habitat and related knowledge.
 Validate — community and expert review workflows.
 Contribute — user submissions, corrections and evidence.
 Research — structured data access, exports and future API capabilities.
6.2 Shared STF platform services
 Identity and authentication
 Users, roles and permissions
 Media management
 Taxonomy service
 Geography service
 Search and discovery
 Evidence service
 Observation service
 Notifications
 Audit logging
 Analytics and telemetry
 API gateway/service layer
 Security and privacy controls
 Infrastructure, monitoring and CI/CD
7. Identification Workflow
The primary identification journey should be evidence-driven:
1. User starts an identification session.
2. User captures or uploads one or more images.

3. The system performs image-quality and plausibility checks.
4. The system identifies visible plant organ/context where possible (for example leaf, flower, fruit,
bark, whole plant).
5. The system requests additional evidence when the available image is insufficient.
6. Geographic context is obtained from GPS, selected location, or user-provided context subject to 
privacy settings.
7. Season/date and optional habitat/context are incorporated when available.
8. AI produces candidate taxa and associated confidence values.
9. Taxonomy and geographic intelligence validate, filter or reorder candidates.
10. The system presents the leading candidate(s), alternative candidates, evidence and uncertainty.
11. The user can confirm, reject, provide another image, or report that the plant is not represented.
12. The completed interaction can become a structured observation.
13. Low-confidence or disputed cases can enter community/expert review.
8. Evidence Engine Requirements
The Evidence Engine is a first-class product capability. It should sit between raw user input and 
final identification and should also explain why a result is considered stronger or weaker.
Evidence dimension Requirement
Image quality
Detect blur, darkness, obstruction, insufficient detail
and other conditions that materially reduce 
reliability.
Plant organ Capture or infer whether the image shows leaf, 
flower, fruit, bark, habit/whole plant, etc.
Morphology
Use visible characteristics such as leaf arrangement,
shape, venation, margins, inflorescence and other 
relevant traits where feasible.
Geography Use location/range as supporting evidence, with 
uncertainty where location is approximate.
Season / date Use phenology when it is scientifically useful and 
available.
Habitat / context Allow structured or optional contextual 
observations.
Taxonomy Check candidates against the platform's accepted 
taxonomy and synonym relationships.
Source evidence Expose relevant references or provenance for 
scientific claims.
Uncertainty Represent missing, conflicting and insufficient 
evidence explicitly.
9. Identification Result Requirements
 Show the leading identification without implying certainty beyond the evidence.
 Show an explicit identification confidence level.

 Show an evidence quality level separately.
 Show alternative candidates when ambiguity is material.
 Explain the principal supporting evidence in user-understandable language.
 Distinguish AI-generated inference from established scientific information.
 Show taxonomy status and accepted scientific name where available.
 Show common/local names only when sourced or appropriately labelled.
 Provide a path to confirm, challenge, retry or request expert review.
 Provide an 'unknown / insufficient evidence / outside coverage' path.
10. Confidence and Uncertainty Model
State Meaning Expected product behavior
High confidence Strong candidate with strong 
supporting evidence
Present result clearly but retain 
evidence/verification context
Moderate confidence Plausible candidate but 
meaningful uncertainty remains
Show alternatives and request 
additional evidence where useful
Low confidence Weak or ambiguous evidence Avoid overclaiming; ask for more 
evidence or offer expert review
Insufficient evidence Input does not support a reliable 
identification
Guide the user to better 
images/context
Unknown / unsupported No reliable supported match Clearly state that the system 
cannot currently identify it
Conflicting evidence Image, geography or taxonomy 
signals disagree
Explain conflict and escalate/retry
where appropriate
11. Species Profile Requirements
A species profile should be structured, source-aware and extensible. Potential fields include:
 Accepted scientific name
 Author citation where appropriate
 Taxonomic hierarchy
 Synonyms and historical names
 Common/local names with language and source context
 Identification characteristics
 Morphology
 Habit and growth form
 Flowering/fruiting or phenology information
 Habitat
 Geographic distribution in India
 Biogeographic region(s)
 Native / endemic / introduced / naturalized / invasive / cultivated status where supported
 Conservation-related information where authoritative sources support it
 Similar species and distinguishing characteristics

 Images and media with licensing/provenance
 References and source citations
 Taxonomic version / last reviewed date
 Expert validation status
12. Search and Exploration Requirements
 Search by scientific name.
 Search by common/local name where indexed.
 Search by taxonomy.
 Search/filter by state or union territory.
 Search/filter by geographic region and habitat where data exists.
 Search/filter by observation status and validation status.
 Search for visually or taxonomically similar species.
 Provide map-based exploration where appropriate.
 Support future multilingual search without requiring a redesign of the data model.
 Clearly distinguish authoritative species information from user observations.
13. Observation Requirements
 Create an observation from an identification session or independently.
 Store one or more media items.
 Record date/time with appropriate privacy controls.
 Record location at a privacy-preserving precision appropriate to the use case.
 Record observed taxon/candidate(s) and identification state.
 Allow notes and structured context.
 Track whether the identification was AI-generated, user-confirmed, community-confirmed or 
expert-reviewed.
 Maintain observation history and changes.
 Allow users to export or remove their own eligible observations subject to platform policy.
14. Community Contribution and Validation
Recommended contribution states:
 Submitted
 AI identified
 User confirmed
 Community reviewed
 Expert reviewed
 Scientifically verified
 Disputed / requires review

 Rejected / invalid
The platform should preserve the distinction between a user's observation and the authoritative 
species record. A community observation must not silently rewrite authoritative taxonomy.
15. Expert Workflow
 Expert queue for low-confidence, disputed or selected observations.
 Review original images and all supporting evidence.
 See AI candidates and confidence without being forced to accept them.
 Add identification, correction and rationale.
 Request additional evidence from contributor when appropriate.
 Record expert identity and review timestamp according to privacy and governance policy.
 Support escalation for taxonomically difficult cases.
 Maintain a review history rather than overwriting prior decisions.
16. Admin and Governance Requirements
 User and role administration.
 Permission management.
 Content moderation.
 Taxonomy/data-source management.
 Species record publishing workflow.
 Expert role management.
 Audit log access.
 System configuration.
 Data quality monitoring.
 Security event visibility.
 Operational dashboards.
 Data export and retention controls.
17. Mobile Application Requirements
 Camera-first identification experience.
 Gallery upload.
 Multiple images for one specimen.
 Guided capture prompts.
 Location permission with clear explanation and user control.
 Offline-capable workflows where technically and economically appropriate.
 Sync and conflict handling after connectivity returns.
 Observation history.
 Species exploration.
 Accessible touch targets and readable layouts.

 Low-bandwidth considerations for field use.
18. Web Platform Requirements
 Responsive public species exploration.
 Identification workflow where appropriate.
 Advanced search and filtering.
 Observation and map exploration.
 Educational and scientific content.
 User account and observation management.
 Expert portal.
 Administrative portal.
 Research/data access interfaces as permissions allow.
19. API Requirements
 Versioned API contracts.
 Authentication and authorization.
 Rate limiting and abuse protection.
 Structured taxonomy endpoints.
 Species/profile endpoints.
 Identification endpoints.
 Observation endpoints.
 Media upload/reference endpoints.
 Search endpoints.
 Expert review endpoints.
 Audit and administrative endpoints with appropriate privilege controls.
 Machine-readable documentation.
 Backward-compatibility strategy.
20. Offline and Field Requirements
 The product should support field conditions with unreliable or absent connectivity where 
feasible.
 Core reference data should be cacheable selectively.
 Identification requests should have a defined online/offline behavior.
 Queued observations should synchronize safely.
 The user should see synchronization status and failures.
 Offline data must have defined storage limits and privacy protections.

21. Multilingual Requirements
India-first design requires multilingual capability to be architecturally possible from the beginning,
even if every language is not launched simultaneously.
 Separate language content from core scientific identifiers.
 Preserve scientific names independently of translation.
 Support regional/common names as structured data with language and source.
 Avoid machine-translating scientific claims without review for high-value content.
 Design UI localization into the platform rather than hard-coding English text.
22. Accessibility Requirements
 Target recognized web/mobile accessibility practices appropriate to each platform.
 Support scalable text and readable contrast.
 Provide meaningful labels for controls.
 Do not rely on color alone for status or confidence.
 Support screen readers where applicable.
 Provide non-visual alternatives for critical actions.
 Use plain-language explanations for uncertainty and evidence.
23. Notifications
 Identification completed.
 Expert review requested/completed.
 Observation or contribution status changed.
 Community response or relevant validation update.
 Security/account notifications.
 System announcements where necessary.
Notifications must be consent-aware, non-spammy and configurable.
24. Analytics and Product Telemetry
 Identification attempts and completion rates.
 Image-quality failure rates.
 Identification confidence distribution.
 Evidence quality distribution.
 User correction/rejection rates.
 Unknown/outside-coverage rates.
 Expert review volume and turnaround.
 Observation creation and retention.
 Search behavior.
 Offline sync success/failure.

 Performance and error telemetry.
 Model/data version performance.
Analytics must be designed with privacy, consent, minimization and retention controls. Product 
analytics must not become an excuse to collect unnecessary personal data.
25. Security and Privacy Requirements
 Secure authentication and session/token management.
 Role-based or policy-based authorization.
 Least-privilege access.
 Secrets must never be embedded in source code.
 Encryption in transit and appropriate encryption at rest.
 Secure media upload and content validation.
 Abuse prevention and rate limiting.
 Audit logging for security-sensitive actions.
 Account/data deletion and retention policies.
 Location privacy controls, including coarse location options where appropriate.
 Clear consent for camera, location and notifications.
 Privacy-aware handling of children's data and other protected contexts where applicable.
 Security testing integrated into the SDLC.
26. Scientific Data Requirements
 Every authoritative species record should have provenance.
 Taxonomic sources should be recorded.
 Taxonomic changes should be versioned.
 Synonyms should be represented explicitly.
 Geographic claims should have source/provenance where feasible.
 Scientific content should distinguish source-derived facts from platform inference.
 Image licensing must be tracked.
 Training-data rights and permitted uses must be established before datasets are used for model
training.
 Expert validation must be attributable in the internal audit trail.
 Data correction should preserve historical state rather than silently destroying it.
27. AI / ML Requirements
 AI should be modular and replaceable.
 Support multiple candidate species rather than forcing a single answer.
 Record model/version information for identification events.
 Support evaluation on India-specific and field-realistic datasets.
 Measure performance by taxonomic level (species/genus/family) where relevant.

 Measure performance by geography, plant group, image quality and organ type where 
possible.
 Monitor false-confidence and systematic failure modes.
 Provide a safe fallback when model confidence is insufficient.
 Support human feedback without automatically treating every user correction as ground truth.
 Maintain a controlled model/data release process.
28. Non-Functional Requirements
Area Requirement direction
Performance Fast interactive UI; identification latency should be 
measurable and budgeted by workflow.
Scalability Services and data layers should scale independently
where justified.
Availability Define service-level targets per capability before 
production launch.
Reliability Use retries, idempotency, durable queues and 
failure recovery where applicable.
Observability Logs, metrics, traces, model telemetry and audit 
events.
Maintainability Modular services, documented contracts and 
automated testing.
Portability Avoid unnecessary lock-in; prefer open standards 
and replaceable components.
Cost control Track storage, inference, bandwidth and expert￾review costs.
Security Security-by-design and continuous testing.
Accessibility Accessible design across supported interfaces.
Data integrity Versioning, validation, provenance and controlled 
mutations.
29. Suggested Product Information Architecture
Primary user-facing navigation:
 Identify
 Explore
 Observe
 Learn
 My Activity
 Contribute
Specialized interfaces:
 Expert Portal
 Scientific/Data Curation
 Administration

 Research/API
 AI/ML Operations
30. Core Entities (Conceptual)
Entity Purpose
User Account and identity
Role / Permission Authorization and governance
Taxon Scientific taxonomic entity
Taxon Version Versioned taxonomic state
Synonym Taxonomic relationship
Species Profile Human-facing knowledge record
Observation User/field record of a specimen
Media Image or other evidence
Identification Event A specific AI/user/expert identification decision
Evidence Supporting evidence dimensions
Expert Review Formal expert validation activity
Source Origin/provenance of scientific or dataset 
information
Geography Location/region representation
Model Version AI model/version used for inference
Audit Event Traceable system/governance action
31. Priority Framework
Priority is a sequencing mechanism, not a statement that lower-priority capabilities are 
unimportant to the final product.
Priority Meaning Examples
P0 — Foundation Must be resolved in 
product/architecture baseline
Identity, taxonomy model, 
provenance, security, media, 
evidence model
P1 — Core Core production capabilities Identification, species profiles, 
search, observations, validation
P2 — Expansion Important platform capabilities 
after core foundations
Advanced research tools, richer 
multilingual support, advanced 
maps
P3 — Future Potential future ecosystem 
capabilities
Broader biodiversity domains, 
additional intelligence products
32. Initial Functional Requirements Matrix
ID Domain Requirement Priority
ID-001 Identification
User can submit one or 
more images for a plant 
identification session.
P1

ID-002 Identification
System evaluates image 
quality before 
presenting a confident 
result.
P0
ID-003 Identification
System can request 
additional evidence 
when needed.
P1
ID-004 Identification
System returns ranked 
candidates with 
confidence and 
uncertainty.
P1
ID-005 Evidence
Evidence quality is 
represented separately 
from AI confidence.
P0
ID-006 Evidence
Geographic context can 
contribute to 
identification.
P1
ID-007 Taxonomy
Identification results 
map to the platform 
taxonomy and 
synonyms.
P0
ID-008 Transparency
AI inference is 
distinguished from 
sourced scientific 
information.
P0
ID-009 Safety
System can return 
insufficient/unknown/ou
tside-coverage states.
P0
OBS-001 Observations
User can convert an 
identification into a 
structured observation.
P1
OBS-002 Observations Observation history is 
retained and traceable. P1
VAL-001 Validation
Eligible observations can
enter community/expert 
review.
P1
VAL-002 Validation Expert review preserves 
decision history. P1
SCI-001 Scientific data
Authoritative records 
have provenance and 
source metadata.
P0
SCI-002 Scientific data Taxonomic changes are 
versioned. P0
SEC-001 Security
Access is governed by 
least-privilege 
authorization.
P0
SEC-002 Privacy
Location and media 
controls respect user 
privacy settings.
P0
API-001 API
Core capabilities are 
exposed through 
versioned contracts.
P0

OPS-001 Operations
Critical actions and 
system health are 
observable/auditable.
P0
33. Acceptance Criteria for the Product Baseline
 A user can complete a guided identification workflow from image capture/upload to a result or 
an explicit unknown/insufficient-evidence state.
 The system does not represent AI confidence as scientific certainty.
 Identification results can show alternatives and supporting evidence.
 A user can create a structured observation from an identification.
 An observation can be routed for review without changing the authoritative species record 
automatically.
 Species information can display accepted name, taxonomy, distribution and provenance when 
data exists.
 Taxonomic changes can be versioned.
 Administrative and expert permissions are separated from ordinary user permissions.
 Core APIs are versioned and documented.
 Location, media and account data have defined privacy controls.
 The architecture can accommodate replacement of the AI model without redesigning the entire
product.
 The data model can support future Save Tiger First biodiversity projects.
34. Explicit Non-Goals for the Current Product Definition
 Do not define the product primarily as a plant-care/reminder application.
 Do not make disease diagnosis a core requirement at this stage.
 Do not add e-commerce or a marketplace as a core requirement.
 Do not make a generic AI chatbot the primary interface.
 Do not treat a large species count as sufficient evidence of product quality.
 Do not freeze a specific programming language, AI model, database or cloud provider in this 
PRD.
 Do not claim scientific accuracy targets before a representative evaluation dataset and 
measurement protocol are defined.
35. Open Questions Requiring Resolution Before Architecture Freeze
14. Which taxonomic authorities and reconciliation strategy will be the authoritative baseline for 
India?
15. Which source datasets can legally be stored, transformed, displayed and used for model 
training?
16. What is the first scientifically representative evaluation dataset and how will it be maintained?

17. What geographic precision should be stored/displayed for different observation types?
18. What expert governance model will be used?
19. Which Indian languages should be prioritized for the first multilingual content architecture?
20. What offline identification functionality is technically and economically justified?
21. What evidence score methodology should be adopted and validated?
22. Which AI approach should be used as the first production baseline?
23. What performance, availability and cost targets are appropriate for production?
24. What business/sustainability model, if any, is required to support long-term operations?
25. Which capabilities should be shared at the STF platform layer versus specific to the Botanical 
Intelligence product?
36. Recommended Next Task
Task 04 should be the System Architecture & Technology Evaluation phase. It should translate this 
PRD into a production-grade architecture without prematurely locking the implementation to one 
language or vendor.
 Logical system architecture
 Shared STF platform architecture
 Botanical Intelligence domain architecture
 Mobile/web/expert/admin interfaces
 Identity and authorization architecture
 Taxonomy and scientific data architecture
 Evidence Engine architecture
 AI/ML architecture
 Media and storage architecture
 Search/vector/geospatial architecture
 API and event architecture
 Security architecture
 Observability and operations
 CI/CD and environment strategy
 Technology selection matrix with alternatives and trade-offs
 Preliminary infrastructure cost model
 Architecture decision records (ADRs) to be created as decisions are finalized
37. Relationship to Earlier STF Work
This PRD follows the agreed sequence: project charter problem/opportunity analysis product → →
requirements architecture and technology evaluation. It retains the central decisions already →
established: India-first scope, plant identification as the entry point, evidence-based identification, 
scientific validation, geographic context, community observations, expert review, reusable STF 
infrastructure, and a deliberate refusal to freeze technology too early.

Appendix A — Product Workflow at a Glance
User Capture/Upload Image & Evidence Quality Additional Evidence (if needed) AI → → → →
Candidates Taxonomy + Geography Check Evidence Synthesis Result + Alternatives + → → →
Uncertainty Confirm/Challenge Observation Community/Expert Review Validated → → → →
Knowledge/Data Evaluation & Improvement →
Appendix B — Decision Log for v0.1
Decision Status
Full-fledged platform rather than MVP-only scope Agreed direction
India-first botanical focus Agreed direction
Plant identification as entry point Agreed direction
Botanical Intelligence positioning Recommended / baseline
Evidence Engine as first-class capability Recommended / baseline
Scientific provenance and validation Agreed requirement
Reusable STF shared infrastructure Agreed requirement
Multi-language strategy Architecture requirement; exact rollout TBD
Technology/language/vendor choices Deliberately not frozen
Architecture diagrams and Figma Next phases after/alongside architecture and UX 
specification


---

# Repository governance and traceability overlay

**Overlay date:** 20 November 2026  
**Overlay status:** Proposed alignment notes; not a retroactive alteration of source v0.1  
**Governing references:** AI Project Operating Prompt STF-AI-OPS-001; accepted ADR-001 through ADR-010; proposed Full Product Vision and Capability Blueprint in PR #17.

## Source preservation

This repository document is a text transcription of the complete extracted text of the original Project Library source:

- **Original filename:** `STF_Task_03_Product_Requirements_Document_v0.1.docx`
- **Library path:** `/STF app/`
- **Library file ID:** `libfile_e70117518880819196ddad429bf22b84`
- **Original extent:** 16 pages; 677 extracted text lines
- **Source version:** v0.1; working baseline

The original DOCX remains the preserved source artifact. This Markdown transcription retains the source's substantive text; page layout, embedded visual formatting and table geometry may be simplified by text extraction. Any future editorial or substantive change must be recorded separately and must not be presented as part of the original v0.1.

## Current governance interpretation

1. This PRD describes the intended full product. Priority levels P0–P3 govern sequencing and dependency, not permanent exclusion of lower-priority capabilities from the approved full-product scope.
2. All original requirement identifiers, including ID-001–ID-009, OBS-001–OBS-002, VAL-001–VAL-002, SCI-001–SCI-002, SEC-001–SEC-002, API-001 and OPS-001, must be retained in a controlled requirements register.
3. Identification confidence and evidence quality remain separate dimensions. Similarity scores must not be represented as calibrated probabilities without validation.
4. Submitted, AI identified, user confirmed, community reviewed, expert reviewed, scientifically verified, disputed and rejected states are workflow states. They are not interchangeable assertions of scientific truth.
5. User data export, withdrawal, deletion, anonymization, restriction and scientific audit retention require separate policy and legal review. No universal deletion promise is implied.
6. Children's data, precise locations, sensitive biodiversity information, analytics and notifications require specific privacy, security and rights controls.
7. Accepted ADR-001 through ADR-010 govern architecture where the historical PRD is silent or inconsistent. This document does not amend an ADR.
8. The PRD remains a working baseline until the project owner accepts it. Its acceptance criteria and non-goals must be retained and expanded, not replaced by the higher-level capability map in PR #17.

## Related documents

- [Full Product Vision and Capability Blueprint](BOTANICA-INDICA-FULL-PRODUCT-VISION-AND-CAPABILITY-BLUEPRINT.md) — proposed in PR #17; not yet approved.
- `docs/adr/` — accepted architecture decision records.
- Scientific data model review pack — proposed and still subject to scientific validation.

**Status:** Working baseline / transcription for owner review. Not an accepted PRD and not implementation authorization.



---

# Owner decision alignment overlay — ODR-02 (26 November 2026)

**Overlay status:** Owner-authorized logical boundary clarification; source v0.1 wording preserved  
**Decision record:** [ODR-02 — STF / Botanica Indica Logical Domain Boundary](https://github.com/Save-Tiger-First/botanica-indica/blob/64664c398dcb74c99cdbb9252d3e41d68d36b17f/docs/decisions/ODR-02-STF-BOTANICA-LOGICAL-DOMAIN-BOUNDARY.md) (PR #20 architecture workstream; pinned to commit `64664c398dcb74c99cdbb9252d3e41d68d36b17f`)  
**Governing prompt:** STF-AI-OPS-001 v1.0 on `docs/repository-audit-and-ai-operating-standard`

## 1. Owner-confirmed interpretation of Section 6.2

The project owner confirmed that STF owns genuinely reusable platform infrastructure and Botanica Indica owns botanical scientific semantics, domain records, workflows and scientific authority.

Accordingly, the original Section 6.2 entries “Taxonomy service”, “Geography service”, “Evidence service” and “Observation service” are preserved as source wording and must not be read as transferring botanical domain ownership to STF.

Interpret the boundary as follows:

| Concern | STF shared-platform responsibility | Botanica Indica responsibility |
|---|---|---|
| Taxonomy | No botanical taxonomy authority or canonical botanical model | Taxon names, concepts, treatments, reconciliation and botanical source assertions |
| Geography | Coordinate/geometry primitives, CRS conventions, spatial infrastructure and generic location mechanisms | Botanical distribution assertions, occurrence interpretation, habitat/biogeographic meaning and sensitive botanical location policy |
| Evidence | Generic media/file storage, provenance metadata infrastructure and audit mechanisms | Botanical evidence model, evidence evaluation, identification support and scientific interpretation |
| Observation | Generic contribution infrastructure only where truly reusable | Botanical observations, events, surveys, occurrences, field workflows and scientific governance |

The original product requirements remain in force: taxonomy, geography, evidence and observation are essential Botanica Indica product capabilities. Their classification as domain responsibilities does not remove them from scope or defer them to a future STF platform.

## 2. Important distinction

A shared STF service may provide infrastructure consumed by a Botanica Indica module. That does not make the service the owner of botanical concepts, assertions, data quality, scientific workflows or determinations.

A shared geographic primitive is not a botanical distribution model. A generic media service is not a botanical evidence engine. A common account system does not confer scientific-review authority.

## 3. Status and limits

This overlay records the owner's logical boundary decision only. It does not accept the PRD, change its 19 original functional requirement identifiers, 12 acceptance criteria or 7 non-goals, amend ADR-001 through ADR-010, accept ADR-011, approve a physical schema, or authorize implementation.

The original Task 03 v0.1 source text and its requirement IDs remain preserved. Future canonical PRD revisions must reconcile Section 6.2 and any related service-boundary language against ODR-02 without deleting requirements or silently changing scope.

**Status:** PRD remains a working baseline / transcription for owner review, not an accepted requirements baseline.
