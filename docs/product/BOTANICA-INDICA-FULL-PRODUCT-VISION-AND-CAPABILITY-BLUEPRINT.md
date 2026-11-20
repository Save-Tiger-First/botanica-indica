# Botanica Indica — Full Product Vision and Capability Blueprint

**Document ID:** STF-BI-FP-001  
**Version:** 0.1 — Proposed product and capability baseline  
**Status:** Proposed for owner review; not an approved PRD, scientific model, architecture amendment or implementation authorization  
**Prepared:** 20 November 2026  
**Product:** Botanica Indica  
**Organization/ecosystem:** Save Tiger First (STF)  
**Repository:** Save Tiger First / botanica-indica  
**Owner/decision authority:** Save Tiger First project owner  
**Related decisions:** Accepted ADR-001 through ADR-010  
**Related proposals:** Task 05, Task 05B, Task 05C, Task 05D; PRs #1–#5, #9 and #11; proposed ADR-011  
**Review basis:** Task 01 Project Charter v0.1; Task 02 Problem & Opportunity Analysis (September 2026); Task 03 full-detail Product Requirements working baseline (September 2026); Task 04 System Architecture & Technology Evaluation working baseline (September 2026); current repository documents fetched 20 November 2026.

---

## Document control and interpretation

This document describes the intended comprehensive product and the capabilities required to support it over its life. It is a product vision and capability blueprint, not a substitute for detailed requirements, scientific review, architecture decisions, legal advice, budgets, delivery plans or implementation specifications.

The document deliberately distinguishes:

- **Accepted decision:** explicitly recorded as accepted in an applicable ADR or formally approved project record.
- **Existing project baseline:** a direction or requirement present in the earlier working documents and discussions, but not necessarily approved through repository governance.
- **Proposed capability:** a capability recommended for the complete product; it requires detailed requirements, feasibility, rights and validation work.
- **Open decision:** a matter that must be resolved by an accountable owner using evidence before dependent implementation.
- **External requirement:** a standard, law, regulation, contract or source condition whose current applicability must be checked for the particular use.

The blueprint does not silently promote proposed capabilities or working-document statements to approved decisions. A capability appearing here does not mean it has been funded, built, tested, legally cleared, scientifically validated or approved for public release.

## 1. Executive product vision

### 1.1 Product definition

**Botanica Indica is an India-first botanical intelligence platform that connects botanical knowledge, taxonomic interpretation, evidence-based plant identification, geographic and ecological context, field observations, scientific review and responsible biodiversity data exchange.**

AI-assisted plant identification is a major entry point, not the product's entire purpose.

The platform should help people move from a photograph or field encounter to a transparent, evidence-aware understanding of a plant: what it may be, which taxonomic treatment is being used, why a candidate is plausible, what evidence is missing, what similar taxa may be confused with it, where relevant sources report it, and how the record can be reviewed or contributed responsibly.

The product should serve both public learning and serious scientific workflows without pretending that every user submission is a verified scientific record.

### 1.2 Vision

To build a scientifically credible, accessible and sustainable digital platform that helps people understand, document and investigate India's botanical diversity, while enabling responsible collaboration and interoperability with the wider botanical and biodiversity knowledge ecosystem.

### 1.3 Mission

Make reliable botanical knowledge and evidence-aware plant identification accessible to the public, students, educators, enthusiasts, researchers, botanists, field professionals and conservation practitioners, while preserving scientific uncertainty, provenance, rights and community authority.

### 1.4 Product promise

Botanica Indica should not promise that every photograph can be identified to species level. It should promise a transparent process that:

1. evaluates the available evidence;
2. presents defensible candidate taxa where possible;
3. explains important supporting and conflicting evidence;
4. communicates uncertainty and limitations honestly;
5. requests additional observations when they could materially help;
6. preserves the original observation and every subsequent determination;
7. supports qualified human review where required; and
8. protects personal, community-held and conservation-sensitive information.

### 1.5 Strategic positioning

The opportunity is not a claim that existing global plant-identification products are incapable of identifying Indian plants. Task 02 correctly warns against building the strategy around an unverified comparison with Google Lens or claiming uniqueness for capabilities already demonstrated by products such as Pl@ntNet, Flora Incognita and iNaturalist.

The intended differentiation is the quality and coherence of the India-first botanical knowledge layer: carefully governed Indian taxonomic and regional context, source-aware reconciliation, field evidence, expert workflows, transparent provenance, responsible multilingual knowledge and integrations with existing biodiversity infrastructures.

The platform should complement appropriate external knowledge systems and institutions, not assume it must replace them.

## 2. Product outcomes and measures of success

Success must be assessed across multiple dimensions. No single usage, model-accuracy or record-count metric is sufficient.

### 2.1 Scientific outcomes

- Taxonomic assertions retain source, treatment, version and temporal context.
- Identification results preserve candidate alternatives, uncertainty and abstention.
- Observations remain useful even when no identification is available.
- Expert corrections and disagreements remain attributable and historically interpretable.
- Distribution and occurrence claims retain geographic scope, evidence and source context.
- Data exports preserve meaning and disclose transformations and limitations.

### 2.2 User outcomes

- Public users can obtain understandable results without needing botanical training.
- Learners can explore diagnostic features and reliable references.
- Field users can capture useful records under realistic connectivity and device conditions.
- Researchers can inspect provenance, uncertainty, methods and data limitations.
- Experts can review efficiently without losing scientific context.
- Contributors understand consent, rights, attribution and the future use of their material.

### 2.3 Platform outcomes

- Mobile, web, expert, administrative and authorized external clients use coherent versioned contracts.
- Shared STF capabilities are reusable without transferring botanical domain ownership into generic platform modules.
- The system can evolve without unnecessary coupling to a single model, provider or deployment topology.
- Data ingestion, model evaluation, release and incident processes are reproducible and auditable.
- Operating costs, support obligations and data stewardship remain sustainable.

### 2.4 Conservation and public-interest outcomes

The platform may improve botanical awareness, documentation and access to evidence. Any claim of ecological or conservation impact must be separately evaluated with an appropriate intervention logic, baseline, outcome measures and evidence. Product activity or observation volume alone is not proof of conservation impact.

## 3. Product boundaries and ecosystem ownership

### 3.1 STF shared platform

Shared STF services should be created only where reuse is genuine and the service has a clear owner, contract and operating model. Candidate shared capabilities include:

- identity, authentication, authorization and account lifecycle;
- shared user, role and organization foundations;
- media/object-storage infrastructure and secure upload processing;
- reusable geographic primitives and spatial infrastructure;
- search infrastructure where cross-domain reuse is justified;
- notification delivery;
- audit, security event and observability foundations;
- API lifecycle, developer documentation and integration tooling;
- deployment, CI/CD, secrets and infrastructure automation.

A shared service does not automatically imply a separate microservice, repository, database or deployment.

### 3.2 Botanica Indica domain ownership

Botanica Indica owns the botanical domain semantics and product workflows, including:

- taxonomic names, concepts, treatments and source-specific usages;
- botanical knowledge profiles and diagnostic characteristics;
- identification runs, candidates, evidence and determinations;
- botanical observations, occurrence assertions and field workflows;
- distribution assertions and botanical geographic interpretation;
- botanical source ingestion, reconciliation and curation;
- botanical expert review and scientific quality governance;
- botanical contribution, research and education workflows.

### 3.3 External authorities and rights-holders

Botanical institutions, taxonomic databases, biodiversity portals, publications, image contributors, community knowledge holders and data publishers remain independent sources, authorities or rights-holders within their respective scopes. Integration does not transfer ownership or imply endorsement.

### 3.4 Adjacent and separate programme boundaries

The core product is botanical intelligence: identification, botanical knowledge, observations, evidence, taxonomy, geography, research and responsible biodiversity exchange.

The following are not assumed to be core Botanica Indica capabilities merely because they are nature-related: crop disease diagnosis, agricultural treatment recommendations, gardening reminders, fertilizer advice, plant commerce, a general-purpose social network, wildlife identification, habitat intervention management or every STF conservation programme. They may be separately assessed as integrations, future domain applications or distinct programmes with their own requirements and governance.

## 4. Stakeholders, user groups and access contexts

Personas describe needs, not automatic permissions. Roles and access must be separately governed.

| User/stakeholder group | Primary needs | Product experience |
|---|---|---|
| General public and curious observers | Understand an unfamiliar plant; receive clear, cautious results | Mobile identification, public web, plant profiles |
| Students and educators | Learn plant characteristics, names, ecology and reliable sources | Learning journeys, species profiles, curated educational content |
| Nature and plant enthusiasts | Identify, save, explore and document plants | Mobile, collections, maps, observations |
| Citizen contributors | Submit observations and media with clear rights and privacy controls | Contribution workflow, consent and record status |
| Botanists and taxonomic experts | Inspect evidence, treatments, nomenclature and determinations | Expert console, taxonomy workspace, review queues |
| Researchers and biodiversity professionals | Search, analyze, export and cite traceable records | Research web workspace, API and controlled data access |
| Field teams and survey professionals | Capture repeatable observations and survey context | Field capture, offline/deferred synchronization, survey workflows |
| Data curators and ingestion stewards | Import, reconcile, quality-check and govern external datasets | Data stewardship console and ingestion tooling |
| Scientific governance reviewers | Review methods, model performance, taxonomy and quality | Review dashboards, decision/evidence registers |
| Platform and security administrators | Manage identities, permissions, configuration and operations | Administrative console and audit tooling |
| Institutional/API consumers | Access permitted, documented and versioned data/services | API, export packages and integration documentation |
| STF leadership and programme owners | Govern strategy, risk, resources and public-interest outcomes | Governance reporting and operational dashboards |

The platform must support role separation, least privilege, conflict-of-interest declarations where relevant, reviewer qualification records, delegated authority and auditable changes. A user account, contributor badge or community agreement must not automatically confer scientific authority.

## 5. Complete product capability domains

The following capability map describes the intended product. Each domain requires a detailed requirements specification, ownership, dependencies, acceptance evidence and operational responsibility.

### 5.1 Botanical knowledge and taxonomic intelligence

- Maintain source-aware taxonomic names, taxon concepts, treatments and taxon-name usages.
- Preserve accepted names, synonyms, nomenclatural relationships, taxonomic placements and concept mappings as distinct relationship types.
- Record source, authority, publication/release version, retrieval time and taxonomic context.
- Represent competing treatments and unresolved reconciliation without manufacturing consensus.
- Maintain taxonomic hierarchy and rank, including higher-rank identifications where species-level determination is not justified.
- Support botanical descriptions, diagnostic morphology, growth form, phenology and relevant habitat information with source attribution.
- Curate common, vernacular and regional names with language, script, geography, source and confidence/provenance.
- Record distribution assertions with geographic and temporal scope and source-specific native/introduced/cultivated status.
- Preserve taxonomic history so earlier identifications and published records remain interpretable.
- Support review, correction, versioning, publication and retirement workflows for knowledge records.

### 5.2 Interactive identification and the Evidence Engine

The Evidence Engine is a first-class product capability. It connects image acquisition, quality checks, botanical evidence, candidate generation, taxonomy, geography, explanation and human review.

- Capture or upload one or more images associated with one observation or identification request.
- Support plant-part context such as leaf, flower, fruit, bark, stem, whole plant and other diagnostic structures where appropriate.
- Detect image quality problems, multiple plants, irrelevant scenes, missing diagnostic views and unsupported input.
- Guide users to capture additional evidence where it could materially improve discrimination.
- Generate ranked taxonomic candidates from one or more replaceable models or permitted external services.
- Combine image evidence with morphology, geography, season, habitat and taxonomic context through an explicit, evaluated pipeline.
- Preserve model, pipeline, taxonomy and reference-data versions used for each run.
- Store raw scores with their semantics; do not present similarity scores as calibrated probabilities unless calibration and validation support that interpretation.
- Explain the evidence available, missing evidence, conflicts and important alternatives without fabricating model reasoning.
- Distinguish candidate generation from user confirmation, community assessment, expert review and scientific verification.
- Support genus-, family- or higher-rank results when the evidence does not support species-level identification.
- Support unknown, insufficient evidence, outside supported coverage, ambiguous multiple taxa, poor image and processing failure as distinct outcomes.
- Permit users to challenge results and provide additional images or field context.
- Preserve all prior identification runs and determinations; never silently overwrite them.
- Support escalation to qualified experts under transparent review rules.

### 5.3 Species and botanical knowledge profiles

A botanical profile should be a source-aware synthesis, not an unqualified static encyclopedia page.

Potential profile sections:

- accepted/display name under a clearly stated taxonomic treatment;
- nomenclatural name, authorship, rank and relevant synonyms;
- taxonomic hierarchy and concept/treatment context;
- vernacular and regional names with language and source;
- description and diagnostic morphological characters;
- photographs and media with asset-level rights and attribution;
- habitat and ecological context;
- geographic distribution and distribution-source differences;
- native, endemic, introduced, naturalized, cultivated or invasive assertions with scope and source;
- flowering/fruiting or seasonal information where adequately supported;
- similar or easily confused taxa;
- conservation status only with named source, assessment scope and date;
- uses or ethnobotanical information only where rights, safety, context and evidence permit;
- references, source versions, data limitations and last review;
- links to observations and expert-reviewed evidence where sharing is permitted.

Safety-sensitive uses, toxicity, medicinal claims and ethnobotanical information require dedicated evidence and review controls. The platform must not turn unverified community statements or AI-generated text into authoritative advice.

### 5.4 Observation, field documentation and survey workflows

- Create an observation independently of whether a taxon is known.
- Capture date/time with original precision and uncertainty.
- Capture location with CRS/datum, method, uncertainty and access classification where available.
- Attach multiple media assets and preserve their separate creators, rights and metadata.
- Record observer, notes, habitat, plant-part context and relevant field attributes.
- Support repeat observations and links to an organism only where individual identity is scientifically justified.
- Support events, surveys, protocols, sampling effort, plots and repeated visits.
- Represent occurrence assertions separately from contributor submissions and AI identifications.
- Preserve non-detection only as an explicit, bounded survey outcome with target, protocol, effort, place, time and reporting completeness.
- Support drafts, submissions, review, correction, withdrawal/restriction and publication states with audit history.
- Provide field data capture under low connectivity, local queues and controlled synchronization where justified.
- Preserve original field values and subsequent normalized or curated values.

### 5.5 Geographic and ecological intelligence

- Represent India at appropriate national, state/UT, district, biogeographic, habitat and site scales.
- Support global geographic entities and international extension without making India-first scope a technical limitation.
- Preserve source geometry, CRS, scale, uncertainty, valid period and transformation provenance.
- Distinguish observed location, locality description, administrative area, distribution range and modeled habitat.
- Keep source-specific distribution assertions separate where sources disagree.
- Treat geography as contextual evidence, not as a deterministic identification rule.
- Support elevation, habitat, season and environmental context only where source quality and semantics justify them.
- Maintain versioned administrative and ecological boundary sources.
- Apply sensitive-species and personal-location policies to storage, APIs, search, maps, exports, analytics, logs, media metadata and backups.
- Support public generalization and restricted precise representations with authorization and audit.

### 5.6 Evidence, expert review and scientific governance

- Store evidence as a first-class, attributable and versioned resource.
- Link evidence to the claim it supports, contradicts, qualifies or contextualizes.
- Record reviewer identity, qualifications/role, date, method, rationale, conflicts and decision scope.
- Preserve multiple expert opinions and disagreements.
- Separate taxonomic treatment change from correction of an identification.
- Support queues, assignment, triage, escalation, review deadlines and quality sampling.
- Allow reviewers to request more evidence, abstain, reject, correct or accept within their authority.
- Maintain scientific decision histories and appeal/correction paths.
- Define publication thresholds and review policies by claim type and risk; do not invent one universal confidence threshold.
- Provide quality dashboards without reducing scientific completeness to one opaque score.

### 5.7 Data acquisition, ingestion, curation and interoperability

- Maintain a source registry containing owner, authority type, scope, coverage, versioning, access method, update cadence and known limitations.
- Assess rights and permitted purposes before ingestion, storage, display, redistribution, derivation, indexing, model training or embedding.
- Preserve source identifiers, verbatim fields, dataset versions, ingestion runs and transformation lineage where retention is permitted.
- Quarantine records with unknown rights, invalid semantics, unresolved identifiers or material quality issues.
- Support deduplication without destroying distinct source records or independent assertions.
- Normalize and reconcile data using explicit, versioned mappings.
- Maintain source-specific taxonomic usages rather than flattening all sources into one accepted-name field.
- Provide repeatable validation, error reports, re-ingestion and rollback/reconciliation workflows.
- Support controlled exports and mappings to Darwin Core, TCS, GBIF profiles and other relevant standards.
- Treat exchange profiles as mappings from the internal model, not as the internal database schema.
- Preserve unmapped internal detail and report information loss in each export mapping.
- Maintain dataset citations, attribution and data-use notices.

### 5.8 Search, exploration, learning and discovery

- Search by scientific name, synonym, vernacular/regional name, family, genus, rank, trait, habitat and permitted geographic context.
- Support spelling variants, transliteration and language-aware search with transparent matching behavior.
- Provide faceted exploration of flora, habitats, regions and curated themes.
- Support maps and spatial exploration with generalized or restricted results according to policy.
- Explain why a result matched and distinguish exact, synonym, fuzzy, semantic and geographic matching.
- Offer learning content tied to reliable sources and reviewed botanical profiles.
- Allow users to save plants, observations and searches under clear privacy controls.
- Support citations and stable links for public knowledge records.
- Ensure search indexes and embeddings are derived, rights-aware and rebuildable; they are not authoritative scientific records.

### 5.9 Community participation and stewardship

- Support contributor profiles and contribution history with privacy controls.
- Make consent, attribution preferences, permitted uses and withdrawal/restriction options understandable.
- Distinguish submitted, AI-assisted, user-confirmed, community-supported, expert-reviewed and scientifically verified states.
- Provide moderation, abuse reporting, spam controls and contributor safety.
- Support regional-name and local knowledge contributions with source, language, place, consent and authority context.
- Do not assume that a person can authorize disclosure or reuse of knowledge held collectively by a community.
- Require appropriate community authority, purpose limitation, access controls, benefit-sharing consideration and grievance processes before handling community-held or traditional ecological knowledge.
- Avoid gamification that rewards volume at the expense of accuracy, safety or responsible data sharing.

### 5.10 Mobile application

The mobile application is the primary field-facing client.

- Onboarding, consent, accessible settings and account controls.
- Camera capture, gallery upload and guided multi-image capture.
- Image quality and plant-part guidance.
- Identification status, candidates, explanation, alternatives and abstention.
- Botanical profiles, maps and references.
- Observation creation, drafts, saved records and contribution.
- Offline/low-connectivity capture and deferred synchronization where technically and scientifically safe.
- Clear handling of location permissions and sensitive coordinates.
- Multilingual interface and language-aware botanical names.
- Notifications, saved plants and personal collections.
- Accessible interaction, screen-reader support and adaptable text/display.
- Secure local storage, session handling, upload controls and account/data lifecycle.

**Technology constraint:** ADR-001 is accepted and establishes the current mobile technology direction as Dart/Flutter. The earlier Task 04 discussion treated React Native as a candidate, not an approved decision. This blueprint does not reopen or change ADR-001. Any change requires a documented ADR amendment or superseding decision authorized by the project owner.

### 5.11 Public web and research platform

The web experience is not merely a larger mobile screen.

- Public product and project information.
- Botanical search, profile and knowledge discovery.
- Accessible identification workflow where browser capabilities and privacy controls permit.
- Flora, family, region and habitat exploration.
- Public observation and map views with sensitive data controls.
- Contributor and educational experiences.
- Research workspaces for advanced search, filters, evidence and citations.
- Controlled downloads and data access with rights and publication-readiness checks.
- Documentation, API reference, methodology, data limitations and scientific governance information.
- Search-engine-friendly public pages that do not disclose restricted information.

### 5.12 Expert and scientific console

- Review dashboard and assignment queues.
- Observation and identification evidence viewer.
- Candidate comparisons and taxonomic treatment context.
- Taxonomy and source-reconciliation workspace.
- Expert determinations, disagreement and correction history.
- Data-quality and scientific completeness review.
- Distribution assertion review.
- Media rights and source provenance visibility.
- Reviewer qualifications, authority and conflict declarations.
- Decision audit, publication controls and review analytics.

### 5.13 Administration and data stewardship console

- User, role, organization and permission administration.
- Source and dataset registry.
- Ingestion runs, validation errors, quarantines and reprocessing.
- Taxonomy curation and version publication controls.
- Media and asset rights management.
- Sensitive location policy administration and access audit.
- Moderation, abuse, reports and contribution management.
- Model registry and deployment governance interfaces.
- System configuration, feature controls and release status.
- Security events, audit trails, operational health and incident workflows.
- Data retention, deletion, restriction and export request handling.
- Governance registers and policy review dates.

Administrative privilege must not bypass scientific review, rights restrictions or audit requirements.

### 5.14 API and institutional integration platform

- Versioned APIs for botanical profiles, taxonomy, identification, observations, evidence and authorized search.
- Authentication, scopes, quotas, rate limits and usage audit.
- Explicit rights and sensitive-data enforcement on every access path.
- Stable identifiers and documented lifecycle behavior.
- Machine-readable error, uncertainty and validation states.
- Webhooks or asynchronous notifications where justified.
- Export and bulk access controls.
- Developer portal, schemas, examples, changelog and deprecation policy.
- Integration adapters for permitted external sources and institutional systems.
- Clear distinction between public, authenticated, partner, research and restricted access.

### 5.15 AI/ML research, evaluation and operations platform

- Dataset manifests and rights eligibility checks.
- Training, validation and test lineage.
- Label provenance, taxonomic treatment and reviewer status.
- Reproducible preprocessing and model training pipelines.
- Model registry, versioning, deployment approval and rollback.
- Candidate-generation and ranking components that can be replaced independently.
- Calibration and threshold evaluation where probability-like outputs are proposed.
- Evaluation by taxon, family, region, habitat, plant part, image quality, season and relevant user context.
- Open-set and out-of-distribution detection, abstention and failure analysis.
- Bias, coverage and robustness monitoring.
- Human review and feedback integration with safeguards against feedback contamination.
- Model cards, limitations, intended use and evaluation evidence.
- Monitoring for data drift, performance drift and rights-policy changes.
- Reproducible release manifests and model retirement procedures.

AI outputs, embeddings, similarity indexes and caches remain derived artifacts, not scientific systems of record.

### 5.16 Analytics, observability and operational intelligence

- Product usage and workflow completion, with privacy-preserving measurement.
- Identification outcome, abstention, correction and expert-review rates.
- Scientific quality and coverage measures with explicit denominators and sampling methods.
- Data ingestion throughput, errors, source freshness and rights status.
- Model performance and drift by meaningful evaluation strata.
- API reliability, latency, queue depth and resource use.
- Security, abuse, privacy and sensitive-data access monitoring.
- Cost by workload, inference pathway, storage and external provider.
- Incident, backup, recovery and service-level reporting.
- Conservation and educational outcome measurement only through separately designed evaluation.

Analytics must not turn sensitive species locations or personal observation histories into unrestricted secondary data.

## 6. End-to-end user journeys

These journeys describe product behavior across clients and roles. Detailed screens, state machines and acceptance tests belong in the PRD and UX specifications.

### Journey A — Public plant identification

1. User opens mobile or web identification.
2. User captures or uploads plant imagery.
3. System checks whether the image is suitable and whether multiple plants or missing context may affect the result.
4. User may add plant-part, location or other context with clear permission choices.
5. Identification pipeline generates candidates and records its versions and evidence.
6. Product presents candidate(s), score semantics, supporting context, alternatives and limitations.
7. If evidence is insufficient, product abstains or requests useful additional evidence.
8. User may save the result, provide feedback or create an observation.
9. Any later review creates a new attributable determination without erasing the earlier result.

### Journey B — Learn and explore a plant

1. User searches a name, regional name, family, characteristic or region.
2. Search explains matching and resolves names within source/treatment context.
3. User opens a botanical profile.
4. Profile presents taxonomic context, diagnostic features, distribution assertions, references and limitations.
5. User explores similar taxa and related observations.
6. User saves or shares only information permitted for public use.

### Journey C — Field observation

1. Field user creates an observation or survey event.
2. System records date/time precision, locality, coordinate uncertainty, observer and protocol where applicable.
3. User attaches media and records relevant field notes.
4. System stores an observation independently of identification.
5. User may run identification or submit for review.
6. Synchronization handles connectivity interruption without duplicating or silently overwriting records.
7. Sensitive location and media policies are enforced before sharing or publication.

### Journey D — Expert determination

1. An observation enters an appropriate review queue.
2. Reviewer inspects original media, field context, source evidence, candidate runs and taxonomic treatments.
3. Reviewer may request more evidence, abstain, disagree, correct or determine a taxon within their authority.
4. System records reviewer, rationale, evidence, date, scope and any conflict declaration.
5. Prior determinations remain available to authorized users.
6. Publication status and any downstream export eligibility are recalculated separately.

### Journey E — Data source ingestion

1. Steward registers source, dataset version and access conditions.
2. Rights and purpose eligibility are assessed.
3. Ingestion run records retrieval and source identifiers.
4. Data is validated, normalized and mapped while verbatim source values are preserved where permitted.
5. Invalid, ambiguous or rights-unclear records are quarantined.
6. Curators reconcile taxonomic and geographic assertions.
7. Accepted records are published internally or externally according to review and rights rules.
8. Re-ingestion preserves lineage and identifies changed records.

### Journey F — Research and institutional access

1. Researcher identifies an authorized use and access scope.
2. Search or API returns records with relevant provenance and uncertainty.
3. Sensitive or rights-restricted data is withheld or generalized.
4. Researcher inspects source versions, methods, limitations and review status.
5. Export mapping validates the target profile and reports omitted or transformed information.
6. Dataset citation and terms accompany the export.

### Journey G — Community or regional knowledge contribution

1. Contributor submits a regional name, observation or knowledge item.
2. Product explains the intended uses, visibility, attribution and withdrawal limitations.
3. Contributor authority and consent are checked at the appropriate level.
4. The submission is stored with source and context, not treated as verified fact.
5. Qualified reviewers assess the contribution under the relevant policy.
6. Any approved use and benefit-sharing obligations are recorded.

### Journey H — Governance and operations

1. Authorized steward reviews system, source, scientific, rights and security dashboards.
2. A policy or model change is proposed with impact analysis.
3. Required scientific, legal, security or owner approvals are obtained.
4. Change is versioned, tested and released through governed environments.
5. Monitoring checks intended behavior and detects adverse effects.
6. Rollback, correction or incident response preserves evidence and accountability.

## 7. Scientific and data integrity requirements

These principles are non-negotiable design constraints inherited from accepted ADRs and the operating prompt. Detailed entity semantics remain subject to the Task 05 review process.

### 7.1 Taxonomy and nomenclature

- TaxonName, TaxonConcept, TaxonomicTreatment and TaxonNameUsage must remain distinct.
- Preserve competing treatments and source-specific accepted status.
- Keep concept-to-name synonym assertions, name-to-name nomenclatural relationships and concept-to-concept mappings separate.
- Retain according-to context and historical taxonomic determinations.
- Never equate name-string similarity with taxonomic identity.
- Record authority, source version, temporal scope and reconciliation rationale.

### 7.2 Observation, event, occurrence and material

- Observation, Event, Survey, Occurrence, Organism and MaterialEntity are distinct concepts.
- A photograph is a MediaAsset, not a specimen.
- An observation may be valid without an identification.
- An occurrence assertion is not automatically identical to a user submission.
- Repeated observations of one organism require justified identity evidence.
- Non-detection requires explicit survey/event context, target, protocol, effort, time/place and completeness.
- Missing records must never be interpreted as absence.

### 7.3 Identification and evidence

- Identification is a versioned assertion about a defined subject.
- AI runs, candidate lists, user confirmations, community assessments and expert determinations remain distinct.
- Preserve uncertainty, alternatives, disagreements and abstention.
- Raw similarity scores are not probabilities unless calibrated and validated.
- Evidence may support, contradict or qualify a claim.
- No automated candidate becomes scientifically verified merely because it ranks first.

### 7.4 Geography and time

- Preserve coordinate reference system, source, method, uncertainty and precision where known.
- Do not invent exact coordinates, dates, CRS or administrative areas.
- Keep source-specific distribution assertions and geographic scales distinct.
- Retain valid time, source publication/release time, retrieval/ingestion time and transaction history as relevant.
- Sensitive location generalization must be policy-based, reversible only by authorized processes and auditable.

### 7.5 Four independent validation dimensions

Do not collapse these into a single global validity flag:

1. **Structural validity:** identifiers, relationships, constraints and data types.
2. **Scientific completeness/evidence quality:** adequacy of evidence for a particular scientific claim.
3. **Rights, privacy and governance eligibility:** permission for a particular processing or disclosure purpose.
4. **External publication readiness:** compliance with the selected exchange profile and publisher requirements.

A record may pass one dimension and fail another.

## 8. Data rights, privacy, community authority and responsible AI

### 8.1 Asset- and purpose-specific rights

For each dataset, record, image, text, model, embedding and derived asset, determine applicable permissions separately for:

- access and retrieval;
- storage and retention;
- internal display;
- public display;
- adaptation and derivative works;
- redistribution and export;
- commercial use;
- model training and fine-tuning;
- embedding generation and similarity search;
- onward sharing and institutional integration.

Dataset-level permission does not automatically cover embedded media or every downstream derivative. Unknown or incompatible rights mean the relevant use remains restricted, quarantined or excluded pending review.

### 8.2 Personal data and privacy

- Minimize personal data collection.
- Separate account identity from public attribution where appropriate.
- Define lawful purpose, notice, consent/other lawful basis, retention, access, correction, deletion and grievance workflows after qualified review.
- Treat photographs and metadata as potentially identifying.
- Apply access control to precise location and private observations.
- Ensure restrictions propagate to caches, exports, logs, analytics, derived assets and backups according to policy.
- Maintain incident response and accountable data stewardship.

### 8.3 Community-held and traditional knowledge

- Identify the legitimate authority for knowledge sharing and permitted use.
- Do not assume an individual contributor can authorize collective knowledge.
- Use meaningful, informed and purpose-specific consent where required.
- Record attribution preferences, access restrictions, benefit-sharing conditions and withdrawal/grievance mechanisms.
- Avoid treating community knowledge as freely available model-training material.
- Seek qualified legal and community-governance advice before any collection, processing or publication.

### 8.4 AI safeguards

- AI remains assistive and does not confer scientific authority.
- Training and evaluation data require documented rights eligibility.
- Record model, data, pipeline, evaluation and deployment versions.
- Evaluate uncertainty, calibration, open-set performance, bias and real-world failure modes.
- Preserve human review and correction histories.
- Do not use sensitive or restricted data for training, indexing or inference without explicit eligibility.
- Do not claim conservation impact from model performance or platform usage.

## 9. Architecture alignment and technology posture

This section describes the product architecture needs. It does not replace accepted ADRs or Task 04's detailed evaluation.

### 9.1 Governing accepted architecture decisions

The current accepted ADR baseline is:

- **ADR-001:** technology-independent, modular, contract-driven architecture; accepted mobile direction is Dart/Flutter.
- **ADR-002:** modular architecture with explicit responsibilities and interfaces.
- **ADR-003:** API-first platform architecture.
- **ADR-004:** provenance-aware data architecture.
- **ADR-005:** source-aware, versioned taxonomic reconciliation.
- **ADR-006:** modular evidence-aware identification pipeline.
- **ADR-007:** first-class evidence and distinct expert validation.
- **ADR-008:** first-class geospatial capability with sensitive-location protection.
- **ADR-009:** observation as a first-class record, separate from identifications and contributions.
- **ADR-010:** source-aware, provenance-preserving modular ingestion.

These ADRs must not be silently amended by this blueprint.

### 9.2 Logical architecture domains

A coherent logical architecture should include:

1. Identity, access and organization foundations.
2. Botanical taxonomy and knowledge.
3. Media and rights management.
4. Observation, event, survey and occurrence workflows.
5. Identification orchestration and model integration.
6. Evidence, determination and expert review.
7. Geographic and distribution intelligence.
8. Source registry, ingestion and reconciliation.
9. Search and discovery.
10. Community contribution and moderation.
11. API and integration layer.
12. Administration, governance and audit.
13. Analytics, observability and operational controls.

These are logical ownership boundaries. They do not require one service or deployment per domain.

### 9.3 Technology evaluation posture

The earlier Task 04 baseline identified candidates such as PostgreSQL/PostGIS, object storage, Python for AI/scientific computing, TypeScript for suitable web/API services, search/cache infrastructure and standard identity protocols. The accepted ADRs and current operating prompt govern how those candidates are treated.

Recommendations:

- Retain a modular monolith as the default deployment starting point unless evidence justifies extraction.
- Evaluate PostgreSQL/PostGIS as the leading relational/spatial system of record candidate; do not finalize physical schema while Task 05 blockers remain.
- Keep original media in controlled object storage with independent metadata, rights and retention.
- Use Python where it materially benefits AI/ML and scientific computing.
- Keep API contracts and external interfaces technology-neutral where practical.
- Evaluate search, vector search, caches, queues and asynchronous processing against measured use cases and rights controls.
- Use containers and automated deployment where justified; Kubernetes is not a default requirement.
- Provide structured logs, metrics, traces, audit events, backups and tested recovery.
- Document identity, authorization, secrets, encryption, file-upload and API threat models.

### 9.4 Technology decisions that remain open

Unless separately accepted in an ADR, the following remain evaluation items: cloud provider, hosting region, object-storage provider, search engine, vector-search implementation, cache/queue technology, authentication provider, API gateway, model hosting/inference provider, monitoring stack, specific web framework, CI/CD service, costs and service-level objectives.

The prior Task 04 React Native discussion is not authority to change ADR-001. Any proposed mobile-framework change must be handled explicitly through ADR governance.

## 10. Cross-cutting non-functional requirements

Detailed numeric targets must be established through workload analysis, user research, risk assessment and service-cost evaluation. This blueprint does not invent latency, availability, accuracy or recovery targets.

### 10.1 Reliability and resilience

- Defined service boundaries and failure behavior.
- Retry, idempotency and duplicate protection for asynchronous workflows.
- Backup, restore and disaster-recovery procedures tested at defined intervals.
- Graceful degradation when AI, maps, external sources or connectivity are unavailable.
- No loss of original scientific assertions during downstream service failure.

### 10.2 Performance and scalability

- Measure API, search, media, inference, ingestion and synchronization workloads separately.
- Support asynchronous long-running inference and ingestion where appropriate.
- Optimize image upload, compression and delivery without altering preserved originals.
- Plan storage lifecycle and compute allocation.
- Scale based on measured workload rather than speculative infrastructure complexity.

### 10.3 Security

- Threat modeling for public, contributor, expert, admin and API access.
- Least privilege and role/scope separation.
- Secure authentication, authorization, session/token handling and secrets management.
- File validation, malware/content checks and safe media processing.
- Encryption in transit and at rest where appropriate.
- Rate limiting, abuse prevention and audit trails.
- Vulnerability management, dependency review and secure release process.

### 10.4 Privacy and data governance

- Data inventory, purpose register and retention schedule.
- Access, correction, deletion, export and grievance workflows as applicable.
- Privacy impact assessment for high-risk processing.
- Sensitive location protection across all system layers.
- Clear contributor terms and consent/permission capture.
- Reassessment when sources, purposes, models or jurisdictions change.

### 10.5 Accessibility and inclusion

- Design to recognized accessibility standards, with a target level to be specified and tested.
- Screen-reader support, keyboard access on web, adequate contrast and scalable text.
- Plain-language explanations and clear scientific terminology.
- Multilingual interface architecture and regional-script support.
- Avoid treating translation as simple string substitution; botanical names and local-name mappings require curated provenance.
- Support low-bandwidth contexts and appropriate offline workflows.

### 10.6 Maintainability and portability

- Versioned contracts, documented module boundaries and automated tests.
- Reproducible builds and data/model pipelines.
- Migration and deprecation policies.
- Replaceable external providers and model components.
- Avoid unnecessary vendor lock-in and premature distributed architecture.
- Developer onboarding and operational runbooks.

## 11. Product quality, validation and acceptance framework

Every capability must have measurable acceptance evidence appropriate to its risk.

### 11.1 Software quality

- Unit, integration, contract, end-to-end and regression tests.
- Accessibility, usability, security and performance testing.
- Mobile device/browser compatibility and low-connectivity testing.
- Data migration, backup restoration and disaster-recovery exercises.
- API versioning and backward-compatibility tests.

### 11.2 Scientific quality

- Representative test collections with documented provenance and rights.
- Taxonomic expert review for high-impact taxonomy and determination workflows.
- Stratified evaluation across taxa, families, regions, habitats, plant parts and image conditions.
- Explicit measures for top-k retrieval, rank-level correctness, abstention, calibration where applicable, error severity and coverage.
- Independent holdout data and leakage controls.
- Evaluation of false positive and false negative consequences.
- Review of source conflicts, taxonomic changes and historical reproducibility.

### 11.3 Data quality and interoperability

- Validate source identifiers, provenance, dates, coordinates, CRS, rights and relationship integrity.
- Preserve verbatim and normalized values separately where permitted.
- Test loss-aware export mappings against the current version of each target standard.
- Validate dataset metadata, citations, licenses and publisher responsibilities.
- Test restricted data suppression and generalization through every export and API path.

### 11.4 Operational quality

- Service health and incident measures.
- Source freshness and ingestion success.
- Model and data drift monitoring.
- Cost and capacity monitoring.
- Support, moderation and expert-review capacity.
- Governance review cadence and policy expiry checks.

## 12. Product information architecture

The product should present a coherent navigation model while allowing each client to emphasize its own user context.

### 12.1 Public/mobile conceptual areas

- Identify
- Explore Flora
- Plant Profiles
- Maps and Regions
- Observations
- Saved Plants
- Learn
- Contribute
- Profile, Settings and Privacy

### 12.2 Research and expert conceptual areas

- Search and Discovery
- Observation Workspace
- Identification Runs
- Evidence Viewer
- Taxonomy and Treatments
- Distribution Assertions
- Review Queues
- Data Sources and Provenance
- Exports and API Access
- Review History and Governance

### 12.3 Administration conceptual areas

- Users and Organizations
- Roles and Permissions
- Source Registry
- Dataset Ingestion
- Rights and Licenses
- Taxonomy Curation
- Media and Sensitive Data
- AI Models and Evaluation
- Moderation
- Audit and Security
- Operations and Analytics
- Policies and Registers

These are information-architecture proposals, not final screen specifications. Detailed flows should be validated with representative users before visual design is frozen.

## 13. Full product capability traceability map

This is the initial capability-level traceability structure. Each row must be expanded into stable requirement IDs in the canonical PRD.

| Capability ID | Capability domain | User/stakeholder outcome | Required design evidence | Validation evidence |
|---|---|---|---|---|
| BI-CAP-01 | Taxonomy and botanical knowledge | Reliable, source-aware plant information | Conceptual model, source registry, profile requirements | Taxonomic fixtures, expert review, source reconciliation tests |
| BI-CAP-02 | Identification and Evidence Engine | Defensible candidates and honest uncertainty | Identification pipeline, score semantics, workflow states | Stratified model evaluation, abstention and failure tests |
| BI-CAP-03 | Observations and surveys | Durable field records independent of identification | Observation/event/survey/occurrence semantics | LDM scenarios, field workflow tests |
| BI-CAP-04 | Geography and distribution | Useful geographic context without false precision | CRS, uncertainty, boundary and sensitivity model | Spatial fixtures, restricted-location leakage tests |
| BI-CAP-05 | Evidence and expert review | Attributable and reviewable scientific determinations | Reviewer roles, evidence relations, decision lifecycle | Disagreement, correction and audit tests |
| BI-CAP-06 | Data ingestion and interoperability | Responsible reuse and reliable exchange | Source registry, rights matrix, mapping specifications | Re-ingestion, rights, export and provenance tests |
| BI-CAP-07 | Search, discovery and learning | Accessible botanical exploration | Search semantics, multilingual IA, profile content model | Relevance, accessibility and source-attribution tests |
| BI-CAP-08 | Community and stewardship | Safe, respectful and useful participation | Consent, authority, attribution and moderation policies | Permission, withdrawal, moderation and governance tests |
| BI-CAP-09 | Mobile field client | Usable capture and field workflow | Flutter architecture, offline/sync and accessibility specs | Device, connectivity, security and usability tests |
| BI-CAP-10 | Web and research client | Rich discovery, analysis and data access | Web IA, research workflow and export controls | Browser, accessibility, API and export tests |
| BI-CAP-11 | Expert console | Efficient, accountable scientific review | Review queue, authority and determination workflows | Expert workflow simulation and audit verification |
| BI-CAP-12 | Admin/data stewardship | Governed platform and data operations | Admin roles, source and rights workflows | Privilege, audit, ingestion and incident tests |
| BI-CAP-13 | API and integrations | Safe reuse by authorized clients | Versioned OpenAPI contracts and access scopes | Contract, security, compatibility and quota tests |
| BI-CAP-14 | AI/ML platform | Reproducible, evaluated and replaceable intelligence | Model registry, data manifests and evaluation plan | Reproducibility, calibration, drift and rights tests |
| BI-CAP-15 | Analytics and operations | Sustainable, observable operation | Metrics, logs, traces, SLOs and cost model | Monitoring, restore, incident and cost evidence |

### 13.1 Required traceability chain

Every detailed requirement must link to:

**Stakeholder need → user journey → requirement ID → scientific/data rule → ADR or approved decision → architecture module → API/data contract → implementation item → test case → evidence → release record → operational owner.**

Unlinked requirements and implementation work should be treated as governance gaps.

## 14. Open decisions and required investigations

The following are not settled by this blueprint. Assign an accountable owner, evidence, decision date and affected requirements before resolving each.

| ID | Open decision / investigation | Why it matters | Required evidence or approval |
|---|---|---|---|
| BI-OD-01 | Formal approval and versioning of the complete product vision and capability map | Establishes authoritative product scope | Project-owner review and decision record |
| BI-OD-02 | Canonical Task 03 PRD and traceability IDs | Prevents competing requirements baselines | Reconcile full-detail PRD with this blueprint and repository inventory |
| BI-OD-03 | Canonical Task 04 architecture baseline | Prevents architecture drift | Reconcile prior architecture evaluation with accepted ADRs |
| BI-OD-04 | Reconcile earlier mobile-framework exploration with the accepted decision | ADR-001 specifies Dart/Flutter; the earlier Task 04 React Native discussion is not an accepted replacement | Align Task 04 and downstream implementation specifications with Flutter; any change requires an explicit superseding ADR and project-owner approval |
| BI-OD-05 | Taxonomic backbone and treatment policy | Affects every name, concept, profile and identification | Source evaluation, scope analysis and qualified botanical review |
| BI-OD-06 | Indian flora coverage and scope model | Determines dataset strategy, evaluation and product claims | Coverage inventory, source evidence and explicit exclusions |
| BI-OD-07 | Image/data source rights and AI-purpose eligibility | Determines lawful and ethical data availability | Asset-level rights matrix and qualified legal review |
| BI-OD-08 | Taxonomic reconciliation and update governance | Prevents false consensus and destructive updates | Approved source hierarchy/decision protocol with exceptions |
| BI-OD-09 | Identification evaluation and abstention policy | Prevents misleading confidence and unsafe outputs | Representative datasets, calibration and expert-approved criteria |
| BI-OD-10 | Expert authority, qualification and conflict policy | Determines who may make which scientific decisions | Governance design and qualified reviewer input |
| BI-OD-11 | Sensitive species and personal location classification | Prevents harmful disclosure | Risk policy, access matrix and legal/scientific review |
| BI-OD-12 | Community and traditional knowledge governance | Protects authority, consent and benefit-sharing | Community-informed process and qualified legal review |
| BI-OD-13 | Offline scope and synchronization semantics | Impacts field use, security and record integrity | Connectivity/device research and sync failure tests |
| BI-OD-14 | Authentication, identity provider and organization model | Impacts all clients and external access | Threat model, operational assessment and ADR |
| BI-OD-15 | Cloud, storage, search, queue and model hosting providers | Impacts cost, security, residency and maintainability | Comparative evaluation and cost/risk evidence |
| BI-OD-16 | Multilingual and regional-name governance | Impacts accessibility and scientific interpretation | Language priorities, scripts, source and review process |
| BI-OD-17 | API openness, tiers and data access terms | Impacts sustainability, abuse and rights | Access policy, user research and rights review |
| BI-OD-18 | Financial and organizational sustainability | Determines realistic operations and support | Bottom-up cost model, capacity plan and governing-body authority |
| BI-OD-19 | International extension and standards mapping | Prevents India-first scope from becoming a technical ceiling | Interoperability scenarios and loss-aware mapping tests |
| BI-OD-20 | Public scientific claims and conservation impact evaluation | Protects credibility | Claim review, evidence standard and independent evaluation design |

## 15. Dependencies and gated development sequence

The complete product is the destination. The sequence below governs dependency order and evidence quality; it does not reduce the intended capability scope.

1. **Product and governance foundation:** approve product boundaries, stakeholders, capability map, ownership and decision authority.
2. **Requirements consolidation:** reconcile Task 01–04 working baselines, create canonical PRD and requirement traceability.
3. **Scientific foundation:** resolve taxonomy, observation, occurrence, evidence, provenance and distribution semantics with qualified review.
4. **Data rights and source strategy:** establish source registry, asset-level rights, consent, data quality and ingestion eligibility.
5. **Logical and platform architecture:** reconcile Task 05–05D, accepted ADRs and shared STF boundaries; define contracts and module ownership.
6. **Experience and workflow design:** validate mobile, web, expert, research and admin journeys; establish accessibility and multilingual requirements.
7. **Detailed engineering design:** API specifications, physical data design after scientific gates, security architecture, AI/ML pipeline and deployment design.
8. **Integrated product implementation:** develop all product domains through traceable increments and controlled integration.
9. **System-wide validation:** scientific, rights, privacy, security, accessibility, performance, operational and user validation.
10. **Controlled deployment and production operation:** release governance, monitoring, support, incident response and continuous improvement.

No downstream phase should be declared ready merely because its documents exist. Readiness requires evidence and resolution of blocking dependencies.

## 16. Risks and mitigations

| Risk | Severity | Recommended control |
|---|---|---|
| Taxonomic disagreement flattened into one answer | Critical | Source-scoped concepts, treatments and explicit reconciliation |
| Incorrect AI result presented as certainty | Critical | Abstention, calibrated semantics, alternatives and human review |
| Rights unclear for images or datasets | Critical | Purpose-specific rights checks, quarantine and lineage |
| Sensitive locations exposed through secondary paths | Critical | End-to-end classification, authorization, generalization and leakage tests |
| Community knowledge used without authority | Critical | Community governance, consent, purpose limitation and benefit-sharing review |
| Dataset bias creates uneven identification quality | Major | Stratified evaluation and transparent coverage limitations |
| Observation and occurrence semantics confused | Major | Scientific model review and executable fixtures |
| Platform expands into unrelated STF programmes | Major | Explicit domain boundaries and separate programme governance |
| Over-engineered infrastructure increases operating burden | Major | Modular monolith default and evidence-based extraction |
| Expert review capacity is insufficient | Major | Capacity planning, qualification rules and queue policy |
| Multilingual names are mapped incorrectly | Major | Source-aware curation and qualified language/botanical review |
| Operational costs become unsustainable | Major | Workload-based cost model, budgets and monitoring |
| External source changes break ingestion | Major | Versioned adapters, schema monitoring and quarantine |
| Public claims exceed evidence | Major | Claim review and documented evaluation methodology |

## 17. Current scientific and technical standards reference baseline

Standards must be rechecked at the point of detailed design, mapping and release. This section records the public reference versions found during preparation on 20 November 2026.

- **Darwin Core List of Terms:** the official TDWG page directly checked on 20 November 2026 reports **Date version issued: 2026-05-26**, with 2025-07-10 as the previous List version. The `occurrenceStatus` term is also marked modified 2026-05-26; a term modification date must not be mistaken for a separate List release. https://dwc.tdwg.org/list/
- **Darwin Core Conceptual Model:** the official TDWG page directly checked on 20 November 2026 reports **Date version issued: 2026-05-26**. It is a high-level semantic reference, not a prescribed internal database schema; its sections other than the status section are marked non-normative. https://dwc.tdwg.org/cm/
- **Taxon Concept Standard (TCS) List of Terms:** TDWG page reports version created 2025-12-11. It provides separate TaxonConcept, TaxonName, TaxonConceptMapping and NomenclaturalType classes and explicit mapping semantics. https://tcs.tdwg.org/terms/
- **GBIF data publishing:** GBIF publishes defined dataset classes and uses Darwin Core Archive and related profiles; occurrence and sampling-event requirements differ. These are publication requirements, not universal internal entity constraints. https://techdocs.gbif.org/en/data-publishing/ and https://techdocs.gbif.org/en/data-publishing/data-quality-recommendations
- **Indian biodiversity law and administration:** the National Biodiversity Authority's official material records the Biological Diversity Act framework, 2023 amendments, Biological Diversity Rules 2024 and 2025 amendment, and the Biological Diversity (Access to Biological Resources and Knowledge Associated thereto and Fair and Equitable Sharing of Benefits) Regulations, 2025. Applicability depends on the resource, person, activity, transaction and jurisdiction. This blueprint is not a legal opinion. https://nbaindia.nic.in/about-us/faqs and https://www.nbaindia.nic.in/public-information/notification-guidelines
- **Digital personal data protection:** the Digital Personal Data Protection Act, 2023 commencement notification G.S.R. 843(E), dated 13 November 2025, brought sections 1(2), 2, 18–26, 35, 38–43 and 44(1), (3) into force on publication; section 6(9) and section 27(1)(d) one year later; and sections 3–5, 6(1)–(8), 6(10), 7–17, 27 except clause (d), 28–34, 36, 37 and 44(2) eighteen months later. Accordingly, as at 20 November 2026, the one-year cohort has commenced and the eighteen-month cohort is scheduled for 13 May 2027. The Digital Personal Data Protection Rules, 2025 were notified separately by G.S.R. 846(E) on 13 November 2025: Rules 1, 2 and 17–21 commenced on publication; Rule 4 commenced one year later; Rules 3, 5–16, 22 and 23 commence eighteen months after publication. This is a commencement summary, not a determination of STF's applicability, legal basis or compliance. Obtain qualified Indian legal advice before processing or launch decisions, and do not assume that phased commencement displaces other applicable privacy or sectoral laws. https://egazette.gov.in/WriteReadData/2025/267647.pdf and https://egazette.gov.in/WriteReadData/2025/267650.pdf

Additional standards, laws, source terms and institutional policies may apply. Legal eligibility must be assessed for the specific dataset, contributor, purpose, processing, disclosure and jurisdiction by qualified counsel or competent authority.

## 18. Relationship to existing project documents

This blueprint consolidates direction; it does not supersede these documents.

| Document / decision | Current status at review | Relationship |
|---|---|---|
| Task 01 Project Charter v0.1 | Working draft supplied in project conversation; not established here as an accepted repository baseline | Vision, mission, users, principles, risks and success dimensions |
| Task 02 Problem & Opportunity Analysis | September 2026 working analysis supplied in project conversation | Competitive positioning, opportunity, assumptions and differentiation |
| Task 03 PRD v0.1 | Full-detail working baseline in prior project discussion; canonical repository path/status not established in this review | Detailed functional and non-functional requirements and acceptance criteria to be reconciled |
| Task 04 Architecture & Technology Evaluation v0.1 | Full-detail working baseline in prior project discussion; canonical repository path/status not established in this review | Architecture evaluation and technology alternatives to be reconciled with accepted ADRs |
| ADR-001–ADR-010 | Accepted in main | Governing architecture decisions; no silent amendments |
| ADR-011 | Proposed in PR #2 | Ecosystem boundary proposal; not treated as accepted |
| Task 05 / 05B / 05C / 05D | Proposed on open PRs #3, #4, #5 and #11 | Scientific/data architecture proposals; subject to reconciliation and review |
| Scientific Data Model Review Pack | Draft in PR #9 | Review instrument; not independent expert approval |
| Licensing and IP Policy | Proposed in PR #1 | Rights governance proposal; requires maintainer and legal review |
| STF organisational readiness review | Proposed in PR #12 | Organizational readiness remains unverified |

### 18.1 Important current scientific-model gate

The 20 November 2026 Scientific Data Model Review Pack and Validation Matrix record the following current dispositions. Documentation revisions have been made on the proposed Task 05 / 05B / 05C branches, but no finding is closed merely because wording changed:

- **DR-01 to DR-07:** revised in proposed documents; require reproducible tests and relevant discipline review before closure. These include internal occurrence validity versus export fields, typed identification subjects and total participation, exact TCS mapping vocabulary, canonical `accordingTo` resource, taxonomy relationship families, derived taxonomic determination and Event/Occurrence/non-detection semantics.
- **DR-08:** remains open as a source/geographic-resolution test case; normalize geographic units and source scopes before treating apparently conflicting native-range claims as comparable.
- **DR-09:** re-opened after direct TDWG verification. Both the Darwin Core List of Terms and Conceptual Model are reported by their official pages as issued 2026-05-26; the previous List version is 2025-07-10.
- **DR-10 to DR-12:** revised in proposed documents; require source-identifier, rights, source-authority and taxonomic review before closure.

The Task 05C competing-model assessment recommends PR #5's document as the canonical review candidate, while preserving selected useful content from the competing document. This remains a desk-review recommendation, not an approved scientific model. PR #11 remains stacked on PR #5 and is two commits ahead and one behind the current PR #5 branch; it must be synchronized and its full diff re-reviewed before any merge decision.

The current validation matrix contains **LDM-01 through LDM-16**, including the explicit survey non-detection scenario. These scenarios remain review criteria, not passed tests. Task 05D remains a proposed validation gate, and Task 05E / physical database design remains **NOT READY** pending reproducible evidence, qualified discipline review and project-owner authorization.

## 19. Governance, ownership and change control

Each capability domain must have:

- accountable product owner;
- scientific/domain owner where relevant;
- engineering owner;
- data steward;
- security/privacy/rights owner where applicable;
- acceptance authority;
- operational owner;
- documented dependencies and risks.

Changes to accepted ADRs, scientific semantics, approved product requirements, rights policy or public claims require explicit decision records and approval by the appropriate authority.

A capability may be proposed, researched, designed, implemented, tested or released. These are different states and must be reported accurately.

The project should maintain one canonical PRD, one canonical architecture baseline, one capability map, one decision register, one unresolved-issues register and a versioned traceability matrix. This blueprint should be updated when the owner accepts or rejects its proposals, not silently overwritten.

## 20. Decisions requested from the project owner

The following are the specific decisions needed to turn this proposal into an approved product baseline:

1. Accept, amend or reject the product definition and positioning in Sections 1–3.
2. Confirm whether the capability domains in Section 5 represent the intended complete product scope.
3. Confirm the stakeholder and access contexts in Section 4.
4. Confirm that the scientific and rights safeguards in Sections 7–8 are mandatory product constraints.
5. Confirm that ADR-001 through ADR-010 remain governing decisions unless formally amended.
6. Authorize consolidation of Task 03 and Task 04 into canonical repository documents, with explicit reconciliation and no silent replacement.
7. Confirm the proposed dependency gates in Section 15.
8. Assign accountable owners and qualified reviewers for the open decisions in Section 14.

Until those decisions are recorded, this document remains **Proposed**.

---

**End of document — STF-BI-FP-001, Version 0.1**
