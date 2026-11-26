# Task 01–04 Foundation Baseline Reconciliation

**Document ID:** STF-BI-FND-001  
**Version:** 0.1 — Proposed cross-document review  
**Audit date:** 26 November 2026  
**Status:** Proposed findings and recommendations; not an approved product, requirements, scientific or architecture baseline  
**Decision authority:** Save Tiger First project owner  
**Repository:** \`Save-Tiger-First/botanica-indica\`  
**Working branch:** \`docs/full-system-architecture-and-repo-engineering-plan\` (PR #20)  
**Governing instruction:** AI Project Operating Prompt STF-AI-OPS-001 v1.0, branch \`docs/repository-audit-and-ai-operating-standard\`, blob \`53add3894d0502827e584614c70ad09cadaa637d\`

---

## 1. Executive conclusion

**Overall foundation status: NOT READY for formal baseline acceptance, architecture freeze or implementation authorization.**

The four foundational tasks establish a coherent strategic direction:

- an India-first botanical intelligence platform;
- plant identification as an entry point, not the complete product;
- a full-product scope rather than an MVP-limited vision;
- evidence-aware identification, explicit uncertainty and human scientific review;
- source-aware taxonomy, provenance and geographic context;
- field observations, community contribution and expert workflows;
- reusable STF infrastructure without erasing Botanica Indica's scientific ownership.

The proposed Full Product Vision and Capability Blueprint and the current Requirements Traceability Register substantially improve the connection between those original tasks. The 19 original Task 03 functional requirement identifiers and 12 acceptance criteria are retained in the RTM. The blueprint defines 16 proposed capability domains. The RTM now correctly represents identity/authentication as an STF shared-platform cross-cutting capability rather than assigning it to unrelated Botanica Indica capability identifiers.

However, the source documents and proposed companions are not yet a single accepted foundation. The most important remaining issue is a **critical STF shared-platform versus Botanica Indica domain-ownership inconsistency** that appears in Task 01, Task 03 and the opening summary of Task 04. Task 04 also contains unresolved decision-status language and its source architecture does not itself specify the offline synchronization behavior now described in a separate proposed specification. Scientific semantics, rights, market evidence and several implementation gates remain open.

The recommended next step is not to rewrite the four original v0.1 documents. Preserve them as historical source records, obtain owner review of the proposed boundary interpretation, and prepare controlled canonical revisions or dated reconciliation overlays with explicit change records. Keep Task 05E and physical schema design blocked until the scientific-model gates are met.

This audit is a documentation consistency review. It does not approve a product baseline, change an ADR, resolve a scientific model, validate market claims, provide legal advice or authorize implementation.

## 2. Repository, governance and source revisions inspected

### 2.1 Governing prompt and repository state

The complete operating prompt was re-fetched from \`docs/repository-audit-and-ai-operating-standard\` on 26 November 2026. Its blob SHA is \`53add3894d0502827e584614c70ad09cadaa637d\`.

The prompt requires a full-product vision, scientific and rights safeguards, preservation-first documentation, no new branches under the current owner directive, a maximum of seven total branches during development, and no irreversible GitHub actions without authorization.

Live repository state at this audit:

| Item | Verified value |
|---|---|
| Repository | \`Save-Tiger-First/botanica-indica\` |
| \`main\` | \`6f2f51da093caf8183fde386dbec707cc6046d27\` |
| \`develop\` | \`f165ecb9b4d9de115c02327cf779982b7ef4bbd4\` |
| \`staging\` | \`f165ecb9b4d9de115c02327cf779982b7ef4bbd4\` |
| Total branches | 23 |
| Long-lived branches | 3: \`main\`, \`develop\`, \`staging\` |
| Temporary/workstream branches | 20 |
| Required ceiling | 7 total branches; currently unmet |

The \`main\` branch remains one commit ahead of \`develop\` and \`staging\`. Preserve the main-only Hortus Malabaricus validation crosswalk in any future synchronization. No synchronization was performed in this audit.

### 2.2 Relevant pull requests

| PR | Purpose | Head SHA | Base | Current status |
|---|---|---|---|---|
| #17 | Full Product Vision and Capability Blueprint | \`b66c16355d0ded4f20f1a84172eab8b47d133277\` | develop | Open / draft |
| #18 | Task 03 and Task 04 source transcriptions | \`0f908f8221ad3434cc84fe2cd41b735aad0a752a\` | develop | Open / draft |
| #19 | RTM, workflows, acceptance and synchronization proposals | \`a068bd2be88c2b9a685b274318b7c9de9e6b6eda\` | develop | Open / draft |
| #20 | Architecture and repository engineering plan; Task 01/02 transcriptions | \`f6cb41d963d168b7f04928f5b7684d58596932da\` | develop | Open / draft |

PRs #18, #19 and #20 had no submitted reviews and no check runs on the inspected heads. GitHub mergeability is not approval. PR #16 remains open/draft and unchanged.

PR #18 and PR #20 have diverged from their common \`develop\` base. The compare API reported PR #20 as 37 commits ahead and 2 commits behind PR #18. Do not blindly retarget, rebase or merge these workstreams. PR #18 contains the Task 03 and Task 04 source files; PR #20 contains Task 01/02 and the current architecture plan. Preserve both histories until an explicit integration plan is approved.

### 2.3 Exact documents inspected

| Document | Ref | Blob SHA | Status |
|---|---|---|---|
| AI Project Operating Prompt v1.0 | \`docs/repository-audit-and-ai-operating-standard\` | \`53add3894d0502827e584614c70ad09cadaa637d\` | Proposed standard; user instruction requires adherence |
| Task 01 — Project Charter v0.1 | \`docs/full-system-architecture-and-repo-engineering-plan\` | \`f79abc985efa4e4f17b6cc0db36cdc56788ba693\` | Working baseline / source transcription |
| Task 02 — Problem & Opportunity Analysis v0.1 | \`docs/full-system-architecture-and-repo-engineering-plan\` | \`55959e1a324262f3c21f9173e9109556b97652fb\` | Working baseline / source transcription |
| Task 03 — PRD v0.1 | \`docs/canonical-task-03-04-baselines\` | \`8b1ca0be04b3f4ad3b543c2f9fc48d46eb37faf8\` | Working baseline / source transcription |
| Task 04 — Architecture & Technology Evaluation v0.1 | \`docs/canonical-task-03-04-baselines\` | \`abc7b721fae8d4f4adede4dd0bf5d6a32098c5a3\` | Working baseline / source transcription |
| Full Product Vision and Capability Blueprint v0.2 | \`docs/full-product-vision-capability-blueprint\` | \`d3ec150524dda4928503f43556a97cd766b71312\` | Proposed; PR #17 |
| Requirements Traceability Register v0.3 | \`docs/requirements-traceability-register\` | \`fbf938235f686c7e2a9959a179a3a1a57ca6c632\` | Proposed; PR #19 |
| Task 03–04 Cross-Document Readiness Audit v0.1 | \`docs/requirements-traceability-register\` | \`b4efa0c93f7f1d541cbc5976944ebc36e3216de0\` | Proposed audit; PR #19 |
| Task 03 Acceptance Test Plan v0.2 | \`docs/requirements-traceability-register\` | \`76f3fa8d24baa022fa3056c0694c2462876f5f2a\` | Proposed / not run |
| Offline and Field Synchronization Specification v0.2 | \`docs/requirements-traceability-register\` | \`6a25055c51cd5d16e8a9da8964f5f5e2c9bfbc0a\` | Proposed; not an accepted ADR or implementation authorization |
| Workflow Lifecycle Specification v0.2 | \`docs/requirements-traceability-register\` | \`498af08ec60e3626e8b60ab5047acae1a8861eb5\` | Proposed |
| Workflow-to-Requirements Crosswalk v0.2 | \`docs/requirements-traceability-register\` | \`61d2111ace5c408eaf503bdf17b2ccb822f90978\` | Proposed |

The accepted ADR register contains ADR-001 through ADR-010. They remain unchanged. ADR-011 remains a proposal and is not used as an accepted decision in this audit.

### 2.4 Source provenance

The four original Word documents were located in the Project Library and represented in GitHub as Markdown transcriptions:

| Task | Original filename | Library file ID | Original extent |
|---|---|---|---|
| 01 | \`STF_Task_01_Project_Charter_v0.1.docx\` | \`libfile_20376f1353588191ae8048e3943f5a52\` | 5 pages; 40,239 bytes |
| 02 | \`STF_Task_02_Problem_and_Opportunity_Analysis_v0.1.docx\` | \`libfile_80b3016cb76881919e137bf021347c93\` | 4 pages; 40,848 bytes |
| 03 | \`STF_Task_03_Product_Requirements_Document_v0.1.docx\` | \`libfile_e70117518880819196ddad429bf22b84\` | 16 pages; 677 extracted text lines |
| 04 | \`STF_Task_04_System_Architecture_and_Technology_Evaluation_v0.1.docx\` | \`libfile_79fbbfd739fc81918ef8543727931b96\` | 11 pages; 431 extracted text lines |

The original DOCX files remain in the Project Library. The repository records are extracted-text transcriptions; original page layout, typography, embedded diagrams and table geometry may not be reproduced. The file service did not authorize raw-byte materialization for Tasks 01/02, and no binary identity or checksum is claimed for those transcriptions. Do not describe the Markdown files as byte-identical copies of the Word documents.

## 3. Four-task foundation assessment

### 3.1 Task 01 — Project Charter

**Assessment: Strong strategic foundation; domain allocation needs explicit reconciliation.**

The charter establishes the full-fledged India-first Botanical Intelligence Platform, plant identification as the entry point, multiple user groups, uncertainty-aware results, human review, reusable STF infrastructure and multiple client surfaces.

Its strongest principles are:
- plant identification is not merely image-to-name classification;
- AI is a component, not the whole product;
- “I don't know” is a legitimate outcome;
- provenance, version history and expert validation matter;
- the product should not be reduced to a Google Lens clone or a static plant database.

The original effort estimate (approximately 4,600 person-hours; 4,250–5,850 planning range; 9–15 months for a multidisciplinary team) is explicitly preliminary. It is not an approved budget, staffing plan or delivery commitment.

**Main concern:** Task 01 §10 lists taxonomy and geography as shared STF infrastructure. That wording predates the more precise current operating boundary. Preserve it as source history, but do not use it as the final allocation of scientific authority or domain ownership.

### 3.2 Task 02 — Problem & Opportunity Analysis

**Assessment: Good product hypothesis; insufficient evidence for a current market or investment decision.**

The strongest hypothesis is “interactive, evidence-based identification of Indian plants.” It correctly moves beyond a single image classifier and emphasizes morphology, geography, taxonomy, season, evidence, uncertainty and expert review.

The competitive landscape includes Pl@ntNet, Flora Incognita, Google Lens, India Biodiversity Portal, eFlora of India, iNaturalist India and Plantix. However, the source notes name broad documentation/research sources without claim-level URLs, publication dates or retrieval dates. Its comparison is a historical source snapshot, not a current competitive audit.

The proposed differentiation—India-specific botanical knowledge, field data, validation, geography and provenance—is a **moat hypothesis**, not a demonstrated moat. Evidence is still needed for:
- lawful and durable access to relevant images and datasets;
- India-wide taxonomic and geographic coverage;
- measurable quality improvement over appropriate existing systems;
- user willingness to provide additional images and contextual evidence;
- expert review capacity and cost;
- sustainable operating economics and user value.

Task 02's “Evidence Score” is undefined. It must not become a single universal scalar or be conflated with AI confidence, calibrated probability, evidence completeness, taxonomic support, geographic plausibility or expert determination.

### 3.3 Task 03 — Product Requirements Document

**Assessment: Useful full-product requirements baseline; not yet accepted or sufficiently resolved for implementation.**

Task 03 v0.1 explicitly defines a full-fledged product rather than an MVP-only scope. Its priority levels P0–P3 are sequencing priorities, not permanent exclusions from the final product.

The source contains:
- 19 original functional requirement identifiers;
- 12 product-baseline acceptance criteria;
- 7 explicit non-goals;
- open decisions covering taxonomy, rights, evaluation data, geography, expert governance, languages, offline functionality, evidence methodology, AI baseline, performance/cost, sustainability and STF/BI boundaries.

The RTM retains the original requirement identifiers and maps the 12 acceptance criteria to proposed test evidence. The proposed 16-domain capability map is a companion structure; it must not replace or silently renumber the original PRD requirements.

**Main concern:** Task 03 §6.2 places a Taxonomy service, Geography service, Evidence service and Observation service in the “Shared STF platform services” list. Under the governing operating prompt, botanical taxonomy, evidence, observations and botanical geographic interpretation belong to Botanica Indica. Only genuinely reusable geographic primitives and infrastructure belong in the STF shared layer.

Task 03's glossary also describes an Observation as a “user/field record of a specimen.” This is too compressed to govern a scientific data model. The operating prompt requires explicit distinction among Observation, Event, Survey, Occurrence, Organism and MaterialEntity; a photograph is a MediaAsset, not a specimen. Task 05 scientific-model work must resolve these semantics before physical design.

### 3.4 Task 04 — System Architecture & Technology Evaluation

**Assessment: Broadly sensible architectural direction; source text contains internal and governance ambiguities.**

Strengths:
- domain-oriented modularity and a deliberate polyglot strategy;
- PostgreSQL/PostGIS as a leading relational/spatial candidate;
- object storage for media;
- replaceable search and AI/ML components;
- asynchronous processing for appropriate long-running work;
- security, privacy, provenance and observability as cross-cutting concerns;
- recognition that Kubernetes and other operational complexity should not be mandatory from day one.

Important historical conflicts are already correctly identified in its governance overlay:
- React Native is an unselected historical candidate; accepted ADR-001 governs Dart/Flutter.
- The source's proposed ADR-001–ADR-012 numbering is historical material and does not replace the repository's accepted ADR-001–ADR-010 register.
- Technology matrix entries are candidates, not vendor, provider, deployment or procurement decisions.

**Remaining concerns:**
1. The opening summary puts taxonomy and geography in the shared STF layer, while Task 04 §3 places taxonomy and botanical geographic intelligence in the Botanica Indica domain. This is an internal inconsistency.
2. Task 04's concluding “Adopt” language overstates the status of a source-preserving working document whose status remains not accepted.
3. The original architecture evaluation does not define offline/field synchronization with enough detail to implement safely. A separate proposed synchronization specification now exists, but Task 04 must explicitly cross-reference it in a canonical revision.
4. Temporary web citation tokens in the original source are not durable repository references. A canonical revision needs organization/document title, stable URL, version/date and access date.
5. The source's “domain-oriented services” wording must be interpreted as logical modules and contracts, not one microservice or deployment per domain.

## 4. Cross-document findings ranked by severity

### FND-01 — Critical: STF shared-platform and Botanica Indica domain ownership are inconsistent

**Evidence**
- Task 01 §10 lists Taxonomy and Geography under Shared STF Infrastructure.
- Task 03 §6.2 lists Taxonomy, Geography, Evidence and Observation services as Shared STF platform services.
- Task 04's opening decision summary lists taxonomy and geography in the shared STF layer.
- Task 04 §3 separately places Taxonomy and species knowledge, Evidence Engine, Observations and Botanical geographic intelligence in the Botanical Intelligence domain.
- The operating prompt §2 assigns botanical taxonomy, names/concepts/treatments, botanical knowledge, identification, observations, occurrences, evidence and scientific governance to Botanica Indica.
- The proposed Blueprint §§3.1–3.2 makes the same distinction.
- The current RTM §7 maps taxonomy and species knowledge to Botanica Indica capabilities and identity/authentication to an STF shared-platform cross-cutting capability.

**Why it matters**

This is not merely a service naming issue. If the earlier shared-service wording is implemented literally, STF could unintentionally own botanical taxonomic concepts, source reconciliation, scientific evidence and observation semantics. These are domain responsibilities, not generic platform primitives. It could also encourage premature universal schemas for future STF domains.

**Recommended treatment**

For the next canonical revisions, distinguish:

**STF shared platform**
- identity, authentication, authorization primitives and account/organization foundations;
- media/object-storage infrastructure and secure upload processing;
- reusable geographic primitives and spatial infrastructure;
- search infrastructure where cross-domain reuse is justified;
- notification delivery;
- audit/security-event and observability foundations;
- API lifecycle, integration tooling, CI/CD, secrets and deployment foundations.

**Botanica Indica domain**
- botanical taxonomy, taxonomic names/concepts/treatments and reconciliation;
- botanical knowledge profiles and diagnostic characteristics;
- identification runs, candidates, evidence and determinations;
- botanical observations, occurrences, surveys and field workflows;
- botanical distribution assertions and geographic interpretation;
- botanical source ingestion, reconciliation and curation;
- expert review and scientific governance.

A shared platform may host infrastructure used by a Botanica-owned module. That does not transfer ownership of botanical semantics, records or scientific authority. A shared geography primitive is not the same as Botanica Indica's botanical distribution model.

Do not edit the original v0.1 source transcriptions. Record this as a dated, explicit reconciliation overlay in a future reviewed canonical revision. The operating prompt is the governing instruction for this work; proposed ADR-011 is not an accepted decision and must not be presented as one.

### FND-02 — Major: Task 04 has internal decision-status ambiguity

**Evidence**

Task 04 §24 says “Adopt” a modular, domain-oriented, polyglot architecture with PostgreSQL/PostGIS, object storage, replaceable search, Python AI/ML, standards-based identity, OpenTelemetry and containerized deployment. The document remains a working transcription and its overlay states that candidates are not accepted selections.

**Recommendation**

In a future canonical Task 04 revision, separate:
1. accepted architecture decisions governed by ADR-001–ADR-010;
2. accepted technology roles/preferences where explicitly established by those ADRs;
3. recommended candidates requiring evaluation;
4. open provider, hosting, search, queue, cache, identity-provider and orchestration selections;
5. scientific-model-dependent details that remain blocked.

Preserve the original “Adopt” wording as source history, but make the current decision status unmistakable in the canonical summary. Do not treat Task 04 as an ADR or procurement authorization.

### FND-03 — Major: Offline/field requirements need a controlled companion architecture

**Evidence**

Task 03 §§17, 20 and 28 require defined online/offline identification behavior, queued observation synchronization, visible sync status/failure, storage limits and privacy protections. Task 04 does not specify local storage, device loss/logout, queue identity, idempotency, duplicate prevention, concurrency/conflicts, ordering/retry, rejection, or propagation of rights and sensitive-location restrictions.

A separate Offline and Field Synchronization Specification v0.2 now exists on PR #19. It proposes a local-first field-capture workflow, durable client outbox, server-authoritative acceptance, idempotent command processing, version-aware reconciliation and policy-aware cache invalidation. It contains 36 proposed validation scenarios. It remains Proposed; no test has been run and it is not an accepted ADR or implementation authorization.

**Recommendation**

Retain the companion specification, link it explicitly from the canonical Task 04 architecture and RTM, and validate the entity-specific conflict rules. Do not apply generic last-write-wins to scientific determinations, taxonomy, rights decisions, withdrawals or sensitive-location restrictions. Keep offline draft creation, queued submission, cached reference data and on-device inference as separate capabilities.

### FND-04 — Major: Observation and specimen-related concepts need scientific-model alignment

**Evidence**

Task 03's glossary uses the compressed phrase “user/field record of a specimen.” The operating prompt and the proposed Blueprint require separation of Observation, Event, Survey, Occurrence, Organism and MaterialEntity; media assets are also distinct. The current RTM links LDM-05, LDM-08, LDM-09 and LDM-16 to important validation scenarios.

**Recommendation**

Do not settle this by editorially redefining Task 03. Preserve the original wording, then align the canonical PRD and workflow specifications to the reviewed Task 05 scientific model. An observation may exist without an identification; media alone does not prove an occurrence; multiple organisms/media/material entities and survey effort need explicit treatment. Keep Task 05C/05D validation open until reproducible fixtures and qualified review exist.

### FND-05 — Major: Evidence Score and AI confidence must not be collapsed

**Evidence**

Task 02 proposes an “Evidence Score” separate from identification confidence. Task 03 distinguishes confidence and evidence quality and includes explicit unknown/insufficient-evidence states. Accepted ADR-006 and ADR-007 require evidence-aware identification and distinct evidence/expert assessment. The Blueprint and RTM further separate confidence/calibration, evidence quality/completeness, taxonomic support, geographic plausibility and expert determination.

**Recommendation**

Do not adopt one universal score. Define each dimension, its inputs, scale, interpretation, calibration (where probability is claimed), versioning and intended user. Preserve unknown/abstention and conflicting evidence. Do not design or implement scoring until the scientific evaluation protocol and qualified review are approved.

### FND-06 — Major: Task 02 market comparison and moat remain unverified hypotheses

**Evidence**

Task 02's source list does not provide direct claim-level URLs, publication dates or retrieval dates. Its competitive table is not a current market benchmark. The proposed moat is not supported by comparative performance, rights-cleared coverage, user research, expert capacity or cost evidence.

**Recommendation**

Retain Task 02 v0.1 as historical source material. Conduct a separate, current market and user validation study before using it for public claims, investment, partnership or procurement decisions. Compare the products on defined tasks and India-relevant datasets; do not claim that global products cannot identify Indian plants without representative evidence. Validate user willingness to supply multiple images/context and quantify expert-review economics.

### FND-07 — Major: Rights, privacy and community authority remain gating dependencies

**Evidence**

Task 02 identifies image/dataset licensing and AI training rights as unknowns. Task 03 requires image licensing, permitted training use and privacy controls. The Blueprint §8 and RTM RIGHTS-001/PRIV-001 require asset- and purpose-specific rights, privacy, consent, community authority and withdrawal controls. Accepted ADR-004, ADR-008 and ADR-010 preserve provenance, sensitive-location protection and source restrictions.

**Recommendation**

Treat access, storage, display, transformation, redistribution, commercial use, AI training, fine-tuning and embeddings as separate purposes requiring evidence. Unknown rights mean restrict/quarantine/exclude for the relevant use, not assumed permission. Do not promise universal deletion or retention; distinguish user withdrawal, legal erasure, scientific audit and derived-data obligations. Obtain qualified legal/privacy and community-governance review before collection or reuse of restricted material.

### FND-08 — Major: Requirements and capability identifiers are proposals, not approvals

**Verified current position**

- Task 03 has 19 original functional requirement identifiers, 12 acceptance criteria and 7 explicit non-goals.
- The Blueprint defines 16 proposed BI-CAP capability domains and a legacy crosswalk.
- The RTM retains original Task 03 IDs and maps the 12 acceptance criteria.
- The earlier identity mapping defect identified in AUD-034-02 has been corrected in the current RTM: identity/authentication is now an STF shared-platform cross-cutting capability with no BI-CAP identifier assigned.
- BI-CAP-01–BI-CAP-16, derived requirements, workflow states and crosswalks remain proposed pending owner review.

**Recommendation**

Preserve all 19 original Task 03 IDs, all 12 acceptance criteria and all 7 non-goals. Do not reuse legacy BI-CAP identifiers without the recorded crosswalk. Accept the capability namespace and derived requirements only through an explicit product-owner decision and controlled PRD revision. The old identity-mapping finding should be marked resolved in a future audit update, not left as a current defect.

### FND-09 — Major: Scientific and implementation readiness gates remain open

**Evidence**

The RTM and Task 04 overlay retain DR-01–DR-12 and LDM-01–LDM-16 as review/validation obligations. DR-09 remains open pending exact versioned Darwin Core resources and term-level comparison. EVT-27–EVT-44, OFF-001–OFF-036 and API-SYNC-001–042 remain proposed and unexecuted. Task 05C remains unapproved; Task 05E and physical schema design remain not ready.

**Recommendation**

Do not start physical schema design, SQL migrations, production database relationships or scientific API implementation until the relevant Task 05 model questions are reconciled, tested with reproducible fixtures and reviewed by qualified specialists. A document, diagram or written test case is not proof that a scientific model has passed.

### FND-10 — Major: Task 04 source citations are not durable

**Evidence**

The source transcription contains temporary citation tokens such as \`turn1search1\` and \`turn0search1\`, rather than stable repository-readable references.

**Recommendation**

In the future canonical architecture revision, replace temporary tokens with source organization, document title, canonical URL, version/release date, date checked and the specific claim supported. Preserve the source transcription unchanged.

### FND-11 — Minor: Acceptance Test Plan v0.2 has a stale footer version

**Evidence**

The current ATP header says v0.2, but the final line still says “End of proposed test plan — STF-BI-ATP-001 v0.1.” The plan lists 74 proposed cases, all Proposed / Not run. The eight ATP-ODR cases are a cross-cutting export-validation supplement, not a thirteenth Task 03 acceptance criterion.

**Recommendation**

Correct the footer on the existing PR #19 workstream as a documentation-only version consistency fix. Do not change test semantics or imply execution.

### FND-12 — Observation: Preliminary effort estimates are not a delivery plan

Task 01's 4,250–5,850 person-hour and 9–15 month estimates are preliminary. They are not a funded budget, team commitment, schedule or launch target. Replace them only with a bottom-up estimate after requirements, architecture, scientific review, operating model and resourcing are sufficiently understood.

## 5. What is aligned and should be preserved

The following are strong common threads across Tasks 01–04, the Blueprint, RTM and accepted ADRs:

1. **Full-product intent:** retain the complete target product. Phased delivery is dependency sequencing, not a reduction to an MVP.
2. **India-first botanical focus:** retain Indian taxonomic, geographic and ecological context while designing standards-aware interoperability.
3. **Identification as an evidence-aware workflow:** preserve candidate alternatives, evidence, uncertainty and abstention rather than a single unqualified label.
4. **Taxonomic pluralism and provenance:** preserve source-specific treatments and assertions; do not manufacture consensus.
5. **Observation independence:** observations remain valid without an identification; determinations and expert contributions do not overwrite original observations.
6. **Human scientific review:** community participation, user confirmation, expert review and scientific verification are distinct states and authorities.
7. **Rights and privacy by design:** enforce controls across APIs, exports, search, caches, logs, media and backups.
8. **Replaceable technology:** preserve modularity and contracts without premature microservices, Kubernetes, multiple databases or dedicated vector infrastructure.
9. **Flutter mobile:** accepted ADR-001 governs; React Native in Task 04 is historical and unselected.
10. **Traceability:** preserve the chain from stakeholder need through requirement, decision, architecture, contract, implementation, test, evidence, release and operational owner.

## 6. Recommended consolidated baseline treatment

Do not replace the source documents with the Blueprint or RTM. Use the following hierarchy:

| Layer | Document | Role |
|---|---|---|
| Foundational source | Task 01 v0.1 | Original charter and project intent; historical source preserved |
| Foundational source | Task 02 v0.1 | Original problem/opportunity analysis; historical source preserved |
| Detailed requirements source | Task 03 PRD v0.1 | Original requirement IDs, acceptance criteria and non-goals until an approved revision |
| Architecture evaluation source | Task 04 v0.1 | Original architecture exploration and candidate recommendations; not an accepted ADR |
| Product structure proposal | Full Product Vision and Capability Blueprint v0.2 | Proposed full-product capability domains and crosswalk |
| Traceability proposal | RTM v0.3 | Proposed requirement/capability/ADR/test relationships |
| Validation proposals | ATP, workflow, offline and API specifications | Proposed test and design obligations; not execution evidence |
| Approved architecture decisions | ADR-001 through ADR-010 | Governing accepted architecture decisions |
| Scientific model gate | Task 05C/05D review and validation records | Scientific-model proposals and unresolved validation obligations |

### Proposed sequence

1. Project owner reviews and confirms the STF/BI logical domain boundary already required by the operating prompt.
2. Prepare a controlled Task 01–04 reconciliation overlay or canonical revision without altering source v0.1 transcriptions.
3. Reconcile Task 03 §6.2 and Task 04's opening summary/§3 with the boundary; distinguish shared geographic primitives from botanical geography and botanical domain semantics.
4. Align Task 04 with the proposed offline synchronization companion and clearly separate accepted decisions, preferences, candidates and open selections.
5. Correct the ATP v0.2 footer on the existing PR #19 branch.
6. Review the 19 Task 03 requirements, 12 acceptance criteria, 7 non-goals and 16 proposed capabilities as one controlled requirements package.
7. Refresh Task 02 market evidence separately before using it for public or investment claims.
8. Resolve scientific, rights, privacy and standards gates with reproducible evidence and qualified review.
9. Only then consider architecture freeze and downstream implementation readiness.

## 7. Verification and non-actions

This review was read-only with respect to PRs #17–#19 and accepted ADRs. The audit report was prepared on the existing PR #20 workstream only.

No PR was merged, closed, retargeted or marked ready. No branch was created, deleted, renamed or force-pushed. No repository protection, permission or setting was changed. No accepted ADR, product requirement or scientific model was modified. No external party was contacted. No application code, physical schema, migration or production API was created. No test was executed. No independent specialist review, legal opinion, market validation or scientific sign-off was obtained.

**Final disposition:** retain all four original task documents as working source baselines; keep PRs #17–#20 open and draft; do not authorize architecture freeze, physical database design or implementation from this audit alone.
