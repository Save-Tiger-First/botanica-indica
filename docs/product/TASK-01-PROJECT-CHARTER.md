# Task 01 — Project Charter v0.1

**Repository status:** Working baseline / source-preserving transcription for owner review  
**Original source version:** v0.1  
**Source:** Project Library original DOCX; provenance recorded below.

> This document preserves the complete extracted substantive text of the original Task 01 source. The source text is kept separate from the proposed governance and alignment overlay at the end. This is not an accepted or revised charter.

---

# SAVE TIGER FIRST

**STF Botanical Intelligence Platform**  
**Task 01 — Project Charter v0.1**

Foundation charter for the first major Save Tiger First technology ecosystem

| Document item | Value |
|---|---|
| Status | Working baseline / v0.1 |
| Vision | Technology-driven platform to help people understand India's plant and biodiversity wealth |
| Entry point | Plant identification |
| Long-term direction | Reusable biodiversity/conservation technology ecosystem |
| Product stance | Full-fledged platform; not an MVP |
| Architecture stance | Shared, modular STF infrastructure |

## 1. Vision

Save Tiger First will build a technology-driven platform that helps people identify, understand, explore, document and validate India's plant diversity, with plant identification as the initial entry point and a foundation for future biodiversity and conservation projects.

## 2. Mission

Provide reliable, understandable and scientifically grounded plant intelligence for the public, students, enthusiasts, researchers, field professionals and experts, while building reusable infrastructure for future STF projects.

## 3. Product Concept

The product is not simply “image species.” The intended model combines image evidence, geography, morphology, taxonomy and context, then presents an uncertainty-aware result with evidence and a path to confirmation or review.

## 4. Target Users

- General public
- Students and educators
- Plant enthusiasts
- Researchers
- Field professionals
- Botanical/scientific experts
- Administrators and data curators
- AI/ML and data teams

## 5. Core Capabilities

- Plant identification
- Plant knowledge/species profiles
- Geographic intelligence
- Structured observations
- Search and exploration
- Community contribution
- Expert validation
- Research/data access

## 6. Scientific and Trust Model

- Explicit High / Moderate / Low / Insufficient / Unknown states.
- “I don't know” is an acceptable and desirable outcome when evidence is insufficient.
- AI inference must be distinguished from established scientific information.
- Authoritative taxonomy, accepted names, synonyms, distribution, habitat, morphology and references should be source-aware.
- Expert validation, provenance and version history are core data properties.

## 7. India-First Scope

- States and union territories
- Biogeographic regions
- Habitats
- Native/endemic/introduced/naturalized/invasive/cultivated status where supported
- Indian taxonomic and geographic context

## 8. AI Philosophy

AI is a component rather than the whole product. Candidate approaches may include computer vision, embeddings, multimodal models, retrieval, geographic filtering and hybrid ranking. The model/framework is intentionally not frozen at charter stage.

## 9. Human-in-the-Loop

AI candidate → user confirmation/correction → expert review where needed → validated record → controlled dataset/model improvement.

## 10. Shared STF Infrastructure

- Identity/authentication
- Users/roles/permissions
- Media storage
- Taxonomy
- Geography
- Search/vector search
- Data services
- Notifications
- Analytics
- Monitoring
- Audit logging
- API gateway
- Security
- Cloud/infrastructure
- CI/CD

## 11. Interfaces

- Mobile app
- Public web platform
- Expert portal
- Admin platform
- API platform
- AI/ML platform

## 12. Technology Principles

- Do not depend on one programming language.
- Select technology by suitability, maintainability, maturity, performance, security, interoperability, scalability, cost and long-term sustainability.
- Use modular APIs and replaceable components.
- Prefer open standards where practical.
- Avoid premature vendor/framework lock-in.

## 13. Security, Privacy and Accessibility

- Security-by-design
- Privacy-aware location and media handling
- Role-based access
- Auditability
- Accessibility
- Offline/field-use considerations
- Observability and operational controls

## 14. Strategic Positioning

Working positioning: “scientifically grounded plant intelligence and biodiversity technology platform.” The project should not be framed merely as a Google Lens clone, static plant database, generic chatbot or unverified crowdsourced database.

## 15. Preliminary Effort Estimate

| Estimate | Planning range |
|---|---:|
| Initial central estimate | ~4,600 person-hours |
| Planning range | ~4,250–5,850 person-hours |
| Multidisciplinary team | ~9–15 months |
| Solo development | ~18–30+ months |

These are preliminary planning figures and should be replaced by bottom-up estimates after requirements and architecture are sufficiently defined.

## 16. Major Deliverables

- Project charter
- Problem/opportunity analysis
- PRD
- Scientific/data strategy
- System/data/API/AI architecture
- UI/UX and Figma specification
- GitHub organization/repository strategy
- Development standards
- CI/CD
- Mobile/web/expert/admin platforms
- Scientific validation
- Testing
- Deployment
- Documentation
- Privacy/legal framework
- Operations

## 17. Charter Decision

Proceed with a full-fledged India-first Botanical Intelligence Platform, with plant identification as the entry point and reusable STF infrastructure as a foundational architectural requirement.

---

# Repository governance and decision-alignment overlay

**Overlay date:** 26 November 2026  
**Overlay status:** Proposed alignment notes; not a retroactive alteration of source v0.1  
**Governing reference:** AI Project Operating Prompt STF-AI-OPS-001 v1.0 on branch docs/repository-audit-and-ai-operating-standard, blob 53add3894d0502827e584614c70ad09cadaa637d.

## Source preservation and provenance

- **Original filename:** STF_Task_01_Project_Charter_v0.1.docx
- **Project Library path:** /STF app/
- **Library file ID:** libfile_20376f1353588191ae8048e3943f5a52
- **Original extent:** 5 pages; 143 extracted text lines
- **Original size:** 40,239 bytes
- **Library created:** 22 September 2026, 17:23:17 UTC
- **Library modified:** 22 September 2026, 17:23:17 UTC (recorded timestamp: 17:23:17.302 UTC)
- **Source version:** v0.1; working baseline

The original DOCX remains in the Project Library. The repository file is a text transcription from the Library's extracted content. The Project file service did not provide an authorized raw-byte materialization path, so the original DOCX has not been copied into GitHub and no binary checksum has been computed. The transcription preserves the extracted substantive wording and section sequence; original page layout, typography and table geometry are not reproduced.

## Current alignment notes

1. **Product scope:** The full-fledged India-first botanical intelligence vision and “not an MVP” position remain consistent with the governing operating prompt. Phased delivery is a validation and sequencing method; it must not reduce the approved full-product vision.
2. **Domain ownership:** The project owner confirmed the logical boundary in ODR-02 on 26 November 2026. STF owns genuinely reusable platform infrastructure; Botanica Indica owns botanical taxonomy, taxon concepts and treatments, botanical knowledge, identification, observations, occurrences, evidence, botanical geographic interpretation and scientific governance. The placement of “Taxonomy” and broad data services under shared STF infrastructure in source Section 10 is historical wording and must not be read as transferring botanical semantics or authority to STF. The decision does not settle legal-entity, organizational, staffing, repository, database or deployment boundaries.
3. **Geography:** Shared geographic primitives may be reusable, but botanical distribution, biogeographic interpretation and taxon-specific geographic assertions remain domain-governed scientific content. Do not collapse these into a generic shared geography service.
4. **Scientific trust:** The original High / Moderate / Low / Insufficient / Unknown states must not be treated as a complete scientific confidence model. AI confidence, evidence quality, expert determination and unknown/abstention states require distinct definitions. Confidence is not scientific certainty; raw similarity scores are not probabilities unless calibrated and documented.
5. **Human review:** The human-in-the-loop sequence is a conceptual workflow, not permission to treat every user confirmation or correction as ground truth or automatic model-training data. Preserve source, rights, consent, review authority and version history.
6. **Technology:** The charter deliberately does not freeze a programming language or framework. Its polyglot and replaceable-component principles are consistent with the current technology direction. Accepted ADR-001 governs Dart/Flutter for mobile; no later candidate may silently replace it.
7. **Effort estimate:** The person-hour and duration figures are preliminary planning estimates, not an approved budget, staffing commitment, schedule or delivery promise. Replace them only through a separately documented bottom-up estimate.
8. **Positioning:** The proposed “scientifically grounded plant intelligence and biodiversity technology platform” positioning is a working statement. It is not evidence of market fit, scientific performance or conservation impact.

## Status boundary

This transcription remains a working baseline for owner review. ODR-02 confirms the logical STF / Botanica Indica domain boundary only; it does not approve an organizational or deployment structure, technology procurement, budget, delivery schedule, scientific model, data rights or implementation. Accepted ADRs and product requirements are not changed by this overlay. See docs/decisions/ODR-02-STF-BOTANICA-LOGICAL-DOMAIN-BOUNDARY.md on the PR #20 workstream.
