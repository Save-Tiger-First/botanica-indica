# Task 03–04 Cross-Document Architecture and Acceptance-Readiness Audit

**Document ID:** STF-BI-AUD-034  
**Version:** 0.1 — Proposed audit record  
**Status:** Proposed findings for project-owner review; not an approval or architecture baseline  
**Audit date:** 21 November 2026  
**Repository:** `Save-Tiger-First/botanica-indica`  
**Working branch:** `docs/requirements-traceability-register`  
**Decision authority:** Save Tiger First project owner

## 1. Executive conclusion

**Overall readiness: NOT READY for architecture freeze or implementation authorization.**

Task 03, Task 04, the Full Product Vision and Capability Blueprint, the Requirements Traceability Register (RTM), the workflow specification and the proposed acceptance-test plan form a useful and increasingly connected documentation set. The original twelve Task 03 acceptance criteria are traceable to a proposed 66-case test plan. The product capability map provides a useful full-product target and the accepted ADRs provide meaningful architecture constraints.

However, the documents are not yet a fully coherent approved baseline. The audit identifies:

1. **One critical product-boundary inconsistency:** Task 03 and part of Task 04 describe botanical domain services as shared STF platform services, while the permanent operating prompt and the proposed product blueprint distinguish reusable infrastructure from Botanica Indica-owned botanical semantics and authority.
2. **One major traceability defect:** the RTM maps identity/authentication architecture to BI-CAP-09 through BI-CAP-14, which are community, mobile, web, expert, administration and API capabilities—not an identity capability.
3. **One major architecture coverage gap:** offline/field synchronization is a Task 03 requirement but Task 04 does not yet define a sufficiently testable synchronization architecture.
4. **One major decision-status ambiguity:** Task 04's source text uses the word “Adopt” in its concluding decision while the document remains a working transcription and its overlay says the recommendations are not all accepted decisions.
5. **A documentation integrity issue:** Task 04 retains temporary web citation tokens rather than durable source references.

These issues are correctable without changing accepted ADRs or rewriting the original Task 03/04 source documents. The recommended approach is a clearly versioned reconciliation overlay and controlled updates to the RTM after the project owner has reviewed the proposed boundary interpretation.

No application implementation, production architecture, physical schema, vendor procurement or acceptance-test execution is authorized or evidenced by this audit.

## 2. Scope, method and source revisions inspected

The audit compared product scope, original requirements, capability ownership, architecture responsibilities, accepted ADRs, workflow lifecycles, acceptance criteria, test coverage and relevant current official technical documentation.

### 2.1 Repository and governance snapshot

Repository: `Save-Tiger-First/botanica-indica`  
Default branch: `main`

At audit time:
- 23 branches existed.
- 20 pull requests were open.
- The three long-lived branches `main`, `develop` and `staging` pointed to `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`.
- The immediate seven-branch ceiling remained unmet.
- PR #17 (product blueprint), PR #18 (Task 03/04 source baselines), PR #19 (RTM/workflows/test plan) and PR #20 (system architecture/repository engineering plan) were open and draft.
- PR #19 head at the start of this audit was `a3c5f596461895e657a2f18e23dec387593081c7`, targeting `develop`.

No PR was merged or closed; no branch was created or deleted; no repository protection or setting was changed.

### 2.2 Exact source revisions

| Source | Ref | Blob SHA | Status/role |
|---|---|---|---|
| AI Project Operating Prompt STF-AI-OPS-001 v1.0 | `docs/repository-audit-and-ai-operating-standard` | `61059c74d4d20309ff76e055059ab33f381ca4f2` | Working governance standard; user has directed compliance |
| Task 03 PRD v0.1 | `docs/canonical-task-03-04-baselines` | `8b1ca0be04b3f4ad3b543c2f9fc48d46eb37faf8` | Source-preserving working baseline, not accepted |
| Task 04 Architecture & Technology Evaluation v0.1 | `docs/canonical-task-03-04-baselines` | `abc7b721fae8d4f4adede4dd0bf5d6a32098c5a3` | Source-preserving working baseline, not accepted |
| Full Product Vision and Capability Blueprint | `docs/full-product-vision-capability-blueprint` | `905455233d11fc750ba3a485d5c516e01f8426ee` | Proposed product reference |
| Requirements Traceability Register | `docs/requirements-traceability-register` | `3b64cccd9fc40fbfca23043a781491c8efd7982a` | Proposed traceability register |
| Workflow Lifecycle Specification v0.1 | `docs/requirements-traceability-register` | `03ca940095a9e39c5608548bdeec1ce0166bf76d` | Proposed workflow/state model |
| Workflow-to-Requirements Crosswalk v0.1 | `docs/requirements-traceability-register` | `87dc1ba325238289a030e9e8ef07a8fc903f51a9` | Proposed mapping |
| Acceptance Test Plan STF-BI-ATP-001 v0.1 | `docs/requirements-traceability-register` | `0e7a1d1851492bb4470b2e0fea6991e59db67f2a` | Proposed; 66 cases not run |
| ADR-001 Architecture Principles | `main` | `a7d3b5c6ec55278c8af70d2e25521153f7f766ad` | Accepted |
| ADR-002 Modular Architecture | `main` | `de54ad9b5dc1b6f9da8e236c29820f654c658cff` | Accepted |
| ADR-003 API-First Architecture | `main` | `70aa16dd3ced7f878613254763c4ba752c4ed339` | Accepted |
| ADR-004 Data and Scientific Provenance | `main` | `75148aff6f8dfddfa8aa794b0cb064c62d6418a7` | Accepted |
| ADR-005 Taxonomy Reconciliation | `main` | `b61dcf0b9ba58fc35da5cc7ba5edfbdd5f2909e4` | Accepted |
| ADR-006 Identification Architecture | `main` | `f35345c356725d7dc4b1b64971c0ff59758c8a30` | Accepted |
| ADR-007 Evidence and Expert Validation | `main` | `7ba4874b4175707b69dc3052822f8cbeb5384b0a` | Accepted |
| ADR-008 Geospatial and Sensitive Location Data | `main` | `74cc3774799a29b28edab75fc63d129f8841b497` | Accepted |
| ADR-009 Observation and Contribution Model | `main` | `c096da58dfe0f1eb46812db46e6555ccf01b8718` | Accepted |
| ADR-010 Data Ingestion and Source Integration | `main` | `088e379513fe2c4b9471d857737f75dcdc3990cd` | Accepted |
| ADR-011 STF Ecosystem Boundaries | `docs/adr-011-stf-ecosystem-boundaries` | `92c3fb551c1b0e367d748f76ce8e835959ed3957` | Proposed; not accepted |

ADR-011 is treated as a proposal only. The product-boundary analysis also relies on the permanent operating prompt and the proposed blueprint; it does not claim ADR-011 is an accepted decision.

## 3. Readiness summary

| Area | Audit result | Status |
|---|---|---|
| Full-product intent and scope | Task 03 and blueprint consistently reject MVP-only scope | Aligned in principle |
| Original Task 03 requirements | Original IDs and wording retained in RTM | Traceable; not approved |
| Capability architecture | Sixteen proposed capability domains provide a broad target | Proposed |
| STF/shared vs Botanica/domain ownership | Contradictory lists remain in Task 03 and Task 04 | **Critical gap** |
| Accepted ADR alignment | Task 04 overlay correctly identifies Flutter and modularity constraints | Mostly aligned; see findings |
| Architecture-to-capability mapping | Most domains mapped; identity mapping is inaccurate | **Major gap** |
| Offline/field architecture | Requirement exists; detailed synchronization semantics are missing | **Major gap** |
| Workflow lifecycles | Sixteen proposed workflow scenarios and separate lifecycle states | Proposed; open decisions |
| Acceptance criteria | All twelve mapped to a proposed test plan | Traceable; not executed |
| Scientific data model | DR-01–DR-12 and LDM-01–LDM-16 remain open review dependencies | **Blocking dependency** |
| Rights/privacy/security | Principles present; policies and legal applicability remain open | Not implementation-ready |
| Technology selection | Some accepted preferences; several candidates remain open | Partially decided |
| Architecture freeze | No accepted Task 03/04 baseline and unresolved dependencies | **Not ready** |

## 4. Findings ranked by severity

## AUD-034-01 — Botanical domain services are inconsistently classified as shared STF services

**Severity: Critical**

### Evidence

- Task 03 §6.2 lists a “Taxonomy service”, “Evidence service” and “Observation service” under “Shared STF platform services”.
- Task 04's opening decision summary lists taxonomy within the shared STF layer.
- Task 04 §3 subsequently places taxonomy, the Evidence Engine and observations in the Botanical Intelligence domain.
- The permanent AI Operating Prompt §2 explicitly distinguishes reusable STF infrastructure from Botanica Indica's botanical taxonomy, identification, observations, evidence and scientific governance.
- The proposed Blueprint §3.1–3.2 likewise places identity/media/geographic/search/notification/audit/observability foundations in the shared platform and botanical semantics/workflows in Botanica Indica.
- Proposed ADR-011 §3.1–3.2 makes the same distinction, but remains Proposed.

### Why this matters

If the phrase “shared taxonomy service” is implemented literally, STF could accidentally become the owner of botanical taxonomic concepts, treatments and reconciliation rules. The same risk applies to botanical evidence and observations. A future wildlife, habitat or other biodiversity application may have different scientific entities, authorities and evidence semantics.

The risk is not that code or infrastructure is reused. The risk is that domain ownership, authority and meaning are centralized in a generic service before another domain demonstrates that the abstraction is valid.

### Recommendation

Adopt the following proposed boundary interpretation for the next canonical revision:

**Shared STF platform capabilities**
- identity, authentication, authorization primitives and account/organization foundations;
- media/file storage infrastructure and secure upload processing;
- reusable geographic primitives and spatial infrastructure;
- search infrastructure and indexing mechanisms;
- notification delivery;
- audit/security event foundations and observability;
- API conventions, integration tooling, CI/CD, secrets and deployment foundations;
- reusable rights/data-governance tooling only where more than one domain has a demonstrated need.

**Botanica Indica-owned domain capabilities**
- botanical taxonomy, names, concepts, treatments and reconciliation;
- botanical knowledge profiles and diagnostic characteristics;
- identification runs, candidates, botanical evidence and determinations;
- botanical observations, occurrence assertions, surveys and field workflows;
- botanical distribution interpretation;
- botanical source ingestion and curation;
- botanical expert review and scientific governance.

A shared platform may host infrastructure used by a Botanica-owned domain module. That does not transfer ownership of botanical rules, records or scientific authority.

### Required document treatment

Do not rewrite the original Task 03/04 source transcription. Add a dated, explicit boundary-reconciliation overlay to the canonical working revisions after owner review. The overlay should identify the source passages that remain historical and explain the governing interpretation.

## AUD-034-02 — Identity/authentication capability mapping is inaccurate

**Severity: Major**

### Evidence

The RTM §7 row “Identity, authentication, roles and permissions” maps to BI-CAP-09–BI-CAP-14.

The proposed capability map defines:
- BI-CAP-09: Community participation and stewardship;
- BI-CAP-10: Mobile application;
- BI-CAP-11: Public web and research platform;
- BI-CAP-12: Expert and scientific console;
- BI-CAP-13: Administration and data stewardship console;
- BI-CAP-14: API and institutional integration platform.

These capabilities consume identity and authorization foundations; they are not the identity capability itself.

### Recommendation

Represent identity as a **cross-cutting STF platform capability**, not as a false range of six Botanica product capabilities. Use a separate shared-platform identifier namespace only if the project owner approves one (for example, a clearly marked proposed `STF-PLAT-IDENTITY`). Map the relevant requirements (SEC-001, account/privacy requirements and API authorization requirements) to that platform capability. Map BI-CAP-13 to administration functions and other BI-CAPs only where the user journey genuinely depends on authentication.

Recheck all other RTM capability mappings after correcting this row. Do not silently renumber or repurpose BI-CAP identifiers.

## AUD-034-03 — Offline and field synchronization are not sufficiently architected

**Severity: Major**

### Evidence

Task 03 §20 requires:
- field use under unreliable or absent connectivity where feasible;
- selectively cacheable core reference data;
- defined online/offline identification behavior;
- safe synchronization of queued observations;
- visible synchronization status and failures;
- storage limits and privacy protections for offline data.

Task 04 identifies field/offline workflows as an architecture goal and durable asynchronous jobs as an architecture pattern. It does not yet define:
- which data is available offline and for how long;
- local encryption, device loss, account logout and data expiry behavior;
- whether identification is on-device, deferred, or online-only;
- queue identity, idempotency and duplicate prevention;
- conflict detection and resolution for concurrent edits;
- ordering, retry, cancellation and dead-letter semantics;
- how corrections, withdrawals, rights restrictions and sensitive-location restrictions propagate to disconnected devices;
- what the user sees when synchronization is partial or permanently rejected.

Task 04 §20 contains an historical proposed ADR-012 for offline/mobile synchronization. The repository's accepted ADR register currently contains ADR-001 through ADR-010; the historical ADR-012 list does not create an accepted decision.

### Recommendation

Create a dedicated offline/field synchronization architecture decision and test matrix before implementation of offline workflows. Keep online-only, queued, cached and on-device inference as distinct capabilities. Define conflict semantics per entity type; do not apply generic last-write-wins to scientific determinations, rights decisions or sensitive-location restrictions.

Any future ADR must be assigned an identifier only after checking the live ADR inventory and must be created on an existing approved workstream branch, not a new branch under the current no-new-branches directive.

## AUD-034-04 — Task 04's concluding “Adopt” language overstates its decision status

**Severity: Major**

### Evidence

Task 04 §24 says: “Adopt a modular, domain-oriented, deliberately polyglot architecture with PostgreSQL/PostGIS at the transactional/spatial core, object storage for media, a replaceable search layer, Python-centric AI/ML services, standards-based identity, OpenTelemetry-based observability and containerized deployment.”

The repository document identifies Task 04 v0.1 as a source-preserving working baseline, not an accepted architecture baseline. Its governance overlay says its technology matrix is evaluation/candidate material and not by itself an accepted vendor, framework, deployment or procurement decision.

The accepted ADRs and operating prompt do establish some preferences:
- ADR-001 accepts technology-independent, modular, contract-driven architecture and identifies TypeScript, Python, Dart/Flutter, PostgreSQL/PostGIS, JSON/OpenAPI and Rust where justified as technology roles/preferences.
- ADR-002 accepts modular architecture and permits a modular monolith.
- The operating prompt says to prefer a modular monolith and avoid premature microservices/Kubernetes/vector stores without evidence.
- Flutter is the accepted mobile direction; React Native in Task 04 is historical and unselected.

### Recommendation

In the next canonical Task 04 revision, distinguish:
1. **Accepted architectural decisions** — directly governed by accepted ADRs.
2. **Accepted technology preferences** — such as Dart/Flutter mobile and the ADR-001 technology-role preferences, subject to their stated flexibility.
3. **Recommended candidates** — PostgreSQL/PostGIS, OpenSearch, object storage patterns, OpenTelemetry, OIDC/OAuth-compatible identity, React/Next.js web and container patterns where not already decided.
4. **Open selections** — provider, hosting region, search engine, queue, cache, identity provider, API gateway, telemetry backend, orchestration, cost/SLO targets and deployment topology.
5. **Blocked design details** — physical schema and detailed data relationships gated by Task 05 scientific-model reconciliation.

Do not interpret the Task 04 §24 wording as a new accepted ADR or procurement decision.

## AUD-034-05 — Architecture responsibility crosswalk needs a full mapping review

**Severity: Major**

The identity mapping in AUD-034-02 is a confirmed defect. The remaining RTM responsibility rows broadly align with the capability map, but several responsibilities intentionally span multiple domains and should be checked against the shared/domain ownership distinction.

### Recommendation

Review each architecture row against three separate concepts:
- **platform capability** — reusable infrastructure and shared contracts;
- **Botanica domain capability** — botanical rules, records and scientific authority;
- **client capability** — mobile, web, expert, admin or institutional user interface.

Do not use a product capability ID to represent an infrastructure component merely because the component supports that product capability. Keep requirement links and architecture module ownership distinct.

## AUD-034-06 — Task 04 research citations are not durable repository references

**Severity: Major**

The Task 04 source transcription contains temporary citation tokens such as `citeturn1search1` and `citeturn0search2`. These do not provide a stable, independently readable source reference in the repository.

### Recommendation

In a future reviewed architecture revision, replace temporary citation tokens with:
- source organization/document title;
- canonical URL;
- version/release or page update date where available;
- date accessed;
- concise statement of the specific claim supported.

Do not silently alter the source-preserving transcription. Add durable references in a dated overlay or canonical revision.

## AUD-034-07 — Acceptance test plan is a sound proposal, not evidence of readiness or implementation

**Severity: Observation / readiness gate**

The current ATP contains 66 proposed cases across all 12 original acceptance criteria. It correctly labels them Proposed / Not run and identifies scientific, privacy, rights, architecture and policy dependencies.

The plan is appropriately cautious about accuracy thresholds, latency targets, sample sizes and legal compliance. These must be defined using workload evidence, representative rights-cleared datasets, qualified review and approved policies.

### Recommendation

Retain the test plan as a test-design baseline. Before cases become executable:
- approve test oracles and role/authority policies;
- resolve the relevant Task 05 scientific-model blockers;
- establish API/model contracts;
- prepare representative fixtures with provenance, rights and privacy classification;
- define offline synchronization tests;
- assign qualified reviewers for scientific, security, privacy, rights and accessibility evidence.

No case is Passed or release-accepted merely because the document is committed.

## 5. Current official technical-source checks

These checks validate selected capability claims in Task 04. They do **not** prove that a product/vendor is suitable for Botanica Indica or authorize procurement.

| Topic | Official source checked | Finding and limitation |
|---|---|---|
| Flutter platform support | Flutter supported-platforms documentation, Flutter 3.50 | Flutter documents supported mobile, desktop and web targets. This supports the feasibility of the accepted Flutter direction, but does not replace device, accessibility, offline, performance or UX evaluation. |
| Flutter architecture | Flutter architectural overview | Flutter is designed for code reuse across operating systems while retaining access to platform services. Product-specific architecture and plugin quality still need assessment. |
| PostGIS | PostGIS official documentation | PostGIS extends PostgreSQL with spatial types, indexes and spatial functions. This supports the stated relational/spatial capability, not a decision that every botanical or spatial workload must use one database. |
| OpenSearch | OpenSearch official search documentation | OpenSearch supports lexical, vector and hybrid search. Its documentation also makes clear that hybrid relevance requires tuning and evaluation. Suitability requires representative botanical names, synonyms, scripts, geographic queries, rights filtering, operational and cost benchmarks. |
| OpenTelemetry | OpenTelemetry official documentation | OpenTelemetry is a vendor/tool-agnostic framework for generating, collecting and exporting telemetry. It is not itself the storage, analytics or visualization backend. |

### Official references

- Flutter supported platforms: https://docs.flutter.dev/reference/supported-platforms
- Flutter architectural overview: https://docs.flutter.dev/resources/architectural-overview
- PostGIS introduction: https://postgis.net/docs/manual-dev/en/postgis_introduction.html
- PostGIS spatial indexes: https://postgis.net/documentation/faq/spatial-indexes/
- OpenSearch search methods: https://docs.opensearch.org/latest/search-plugins/
- OpenSearch hybrid search: https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/
- OpenSearch hybrid relevance optimization: https://docs.opensearch.org/latest/search-plugins/search-relevance/optimize-hybrid-search/
- OpenTelemetry overview: https://opentelemetry.io/docs/what-is-opentelemetry/

The PostGIS introduction URL currently points to the development manual; it is useful for confirming the capability description but must not be used as a pinned production-version reference. A future technology selection should pin supported stable releases and verify compatibility with the selected PostgreSQL version.

No Indian legal opinion or legal-compliance assessment was undertaken in this architecture audit. The legal applicability review recorded in the ATP remains an open dependency and must use current official Indian sources and qualified advice.

## 6. Acceptance-criterion readiness review

All twelve Task 03 acceptance criteria have a proposed mapping and proposed test cases. None is currently demonstrated as implemented or passed.

| AC | Current verification path | Main unresolved dependency | Readiness |
|---|---|---|---|
| AC-001 Guided identification | End-to-end capture/upload, candidate, unknown and abstention tests | Supported coverage, model outcome vocabulary, evidence protocol | Blocked |
| AC-002 Confidence vs scientific certainty | UI/API/export semantics and model score documentation | Score semantics, calibration and uncertainty language | Blocked |
| AC-003 Alternatives and evidence | Multi-candidate fixtures and evidence provenance | Evidence ontology and ranking semantics | Blocked |
| AC-004 Structured observations | Observation creation, history and idempotency tests | Task 05 Observation/Event/Occurrence/Organism semantics | Blocked |
| AC-005 Review without automatic authoritative change | Role, determination, disagreement and supersession tests | Reviewer authority and scientific verification policy | Blocked |
| AC-006 Sourced species profiles | Source-backed profile, conflicting-treatment and distribution tests | DR findings, source authority and rights | Blocked |
| AC-007 Versioned taxonomy | Treatment/version reconstruction tests | DR-01–DR-05 and DR-08–DR-12, qualified taxonomic review | Blocked |
| AC-008 Permission separation | Role matrix and direct API negative tests | Approved role/authority and conflict policies | Blocked |
| AC-009 Versioned/documented APIs | Contract and consumer compatibility tests | API inventory and version/deprecation policy | Blocked |
| AC-010 Privacy controls | End-to-end location/media/account and backup/restore tests | Rights/privacy policies, threat model and legal review | Blocked |
| AC-011 Replaceable AI model | Adapter contract, replacement and rollback tests | Model interface, registry, evaluation and rights policy | Blocked |
| AC-012 Future STF biodiversity reuse | Bounded second-domain contract/reference scenario | Approved STF/domain boundary and credible second-domain case | Blocked |

“Blocked” means the acceptance test cannot yet be finalized as an executable release gate. It does not mean the product cannot meet the criterion.

## 7. Scientific and data-model dependencies

The RTM and Task 05 review materials identify DR-01 through DR-12 and LDM-01 through LDM-16 as unresolved review findings and validation scenarios. They remain material to architecture readiness.

At minimum:
- DR-01–DR-04 affect the validity of taxonomic and TCS representations.
- DR-05–DR-07 affect name/concept relationships, determination history and observation/event semantics.
- DR-08–DR-12 affect distribution scope, Darwin Core versioning, source-record identity, TCS synonym mapping and source authority.
- LDM tests protect multiple taxonomic treatments, uncertain observations, multiple candidates, expert disagreement, separate evidence paths, conflicting distribution assertions, sensitive coordinates, rights and dataset version history.

The Task 03/04 audit does not close or reinterpret these findings. Physical database design remains not ready until the required reconciliation and qualified review are complete.

## 8. Recommended remediation sequence

### Gate 1 — Owner direction on domain boundaries
1. Confirm that STF shared platform owns reusable infrastructure and common contracts, not botanical scientific authority.
2. Confirm that Botanica Indica owns botanical taxonomy, evidence, observations, identifications and botanical source reconciliation.
3. Decide whether any shared domain-neutral data/rights registry is justified, and define its scope and owner.

### Gate 2 — Traceability correction
4. Correct the RTM identity/authentication mapping.
5. Recheck every architecture-to-capability mapping using separate platform/domain/client categories.
6. Preserve existing BI-CAP identifiers and their proposed status; do not silently renumber.

### Gate 3 — Task 04 architecture reconciliation
7. Clarify Task 04 §24 as a proposed architecture recommendation, not an accepted decision beyond the accepted ADRs.
8. Make the shared/domain boundary consistent throughout Task 04, including the opening summary and §3.
9. Replace temporary citation tokens in the future canonical revision with durable references.
10. Add explicit offline/synchronization architecture coverage and a separate test matrix.
11. Keep Flutter as the accepted mobile direction unless a formally approved superseding ADR changes it.

### Gate 4 — Acceptance and scientific readiness
12. Resolve the relevant Task 05 DR/LDM blockers.
13. Finalize policies and contracts needed by AC-001–AC-012.
14. Have qualified botanical, AI/ML, security, privacy, rights and accessibility reviewers assess the relevant evidence.
15. Reassess architecture readiness and only then authorize detailed implementation design.

## 9. Work performed and not performed

### Completed
- Retrieved the full operating prompt from the required PR #16 branch.
- Re-fetched the live branch and open-PR inventory.
- Inspected the exact Task 03, Task 04, Blueprint, RTM, workflow and acceptance-test-plan revisions listed above.
- Inspected accepted ADR-001 through ADR-010 and proposed ADR-011.
- Checked selected official technical documentation for Flutter, PostGIS, OpenSearch and OpenTelemetry.
- Recorded the findings and recommended remediation sequence in this audit document.

### Not performed
- No accepted ADR, PRD, scientific model or source-preserving transcription was changed.
- No new branch was created.
- No PR was merged, closed or retargeted.
- No branch was deleted.
- No repository setting, protection or permission was changed.
- No application code, database schema, API implementation or infrastructure was created.
- No tests were executed.
- No scientific, legal, privacy, security or institutional approval was obtained.
- No vendor or hosting provider was selected.
- No production or release readiness claim is made.

## 10. Decision request and next recommended action

**Recommendation:** Review and decide AUD-034-01 (shared platform vs Botanica domain ownership) first. It is the most consequential architectural boundary and affects Task 03, Task 04, the capability map, RTM and future STF applications.

After owner direction, update the proposed architecture overlay and RTM on the existing workstream branch. Do not change accepted ADRs or source-preserving Task 03/04 text as part of this audit.

The next technical task should then be a focused offline/field synchronization architecture and test design, followed by a final consistency pass over the corrected RTM and Task 04 baseline.

**Audit status:** Findings recorded; owner review required.  
**End of audit — STF-BI-AUD-034 v0.1.**
