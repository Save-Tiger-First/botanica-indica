# Botanica Indica — Task 03 Product-Baseline Acceptance Test Plan

**Document ID:** STF-BI-ATP-001  
**Version:** 0.2 — Proposed ODR-01 export-validation supplement and source revalidation  
**Status:** Proposed for owner and discipline review; not approved as a release gate  
**Prepared:** 21 November 2026; updated 26 November 2026  
**Decision authority:** Save Tiger First project owner  
**Repository:** `Save-Tiger-First/botanica-indica`  
**Working branch:** `docs/requirements-traceability-register`

## 1. Purpose

This plan converts the twelve product-baseline acceptance criteria in Task 03 PRD v0.1, Section 33, into proposed test suites and evidence requirements.

It complements, but does not replace:
- Task 03 PRD v0.1, which remains the source of original acceptance-criterion wording;
- the Requirements Traceability Register (RTM);
- STF-BI-WF-001 v0.1, the proposed Workflow Lifecycle and State-Machine Specification;
- STF-BI-RTM-WF-001 v0.1, the Workflow-to-Requirements Traceability Crosswalk;
- accepted ADRs and the unresolved Task 05 scientific-model review.

This is a test-design document only. All test cases have status **Proposed / Not run**. No application implementation, executable test, test fixture, independent review or acceptance result is claimed.

## 2. Source revisions inspected

| Source | Branch/ref | File blob SHA | Role |
|---|---|---|---|
| AI Project Operating Prompt v1.0 | `docs/repository-audit-and-ai-operating-standard` | `53add3894d0502827e584614c70ad09cadaa637d` | Governing working prompt; PR #16 remains open/draft |
| Task 03 PRD v0.1 | `docs/canonical-task-03-04-baselines` | `8b1ca0be04b3f4ad3b543c2f9fc48d46eb37faf8` | Original acceptance criteria |
| Requirements Traceability Register v0.3 | `docs/requirements-traceability-register` | `fbf938235f686c7e2a9959a179a3a1a57ca6c632` | Proposed requirement, capability and ODR-01 mappings; 26 November source update |
| Workflow Lifecycle Specification v0.2 | `docs/requirements-traceability-register` | `498af08ec60e3626e8b60ab5047acae1a8861eb5` | Proposed workflow rules; `record_created` / `server_received` distinction |
| Workflow-to-Requirements Crosswalk v0.2 | `docs/requirements-traceability-register` | `61d2111ace5c408eaf503bdf17b2ccb822f90978` | Proposed scenario-to-requirement and ODR-01/EVT coverage |

The table above is the source snapshot re-fetched on 26 November 2026. The Task 03 PRD remains the original source for the twelve acceptance-criterion wordings. The RTM, workflow and crosswalk are proposals; their updated SHAs do not imply approval.

Additional scientific/export validation inputs:

| Source | Branch/ref | File blob SHA | Role |
|---|---|---|---|
| Offline and Field Synchronization Specification v0.2 | `docs/requirements-traceability-register` | `a46c7cc1de9d1ea5c5faed7574d23de1d1a48e13` | Proposed offline safeguards and export-boundary handling |
| Scientific Data Model Validation Matrix and Decision Register | `review/scientific-data-model-review-pack` | `3a33dfe47657a96456f56f2c12a0b7d355b6c6a5` | ODR-01 decision record and proposed EVT-27–EVT-44 validation obligations |

The source revision table is a review snapshot, not a claim that the referenced documents are accepted. Re-fetch all sources before formal approval or implementation.

## 3. Test governance and status

### 3.1 Status vocabulary

- **Proposed / Not run:** test design only; no execution evidence.
- **Ready for implementation:** test oracle, contract, fixtures, rights and dependencies are approved and executable.
- **Passed:** test ran in a named environment against a recorded build/commit and all expected results were observed.
- **Failed:** one or more expected results were not observed.
- **Blocked:** a prerequisite policy, scientific model, API contract, implementation or test fixture is unavailable.
- **Not applicable:** owner-approved rationale explains why a test does not apply; never use this to hide missing coverage.

No case may be marked Passed based on code review, a document review, a mock screenshot or a successful GitHub commit.

### 3.2 Required evidence record per executed test

Every execution record must include:
1. stable test ID and test-plan version;
2. requirement and acceptance-criterion IDs;
3. build/release identifier and source commit;
4. test environment, platform, device/browser and relevant configuration;
5. fixture identifier, provenance, licence/rights status and privacy classification;
6. preconditions, actor role and authority;
7. exact steps and input data or reproducible test script;
8. expected and actual results;
9. logs, screenshots, traces, API responses or other evidence references with sensitive data redacted;
10. pass/fail/blocked status, date, executor and reviewer;
11. defects, severity, linked issue and retest evidence.

### 3.3 Cross-cutting test rules

- Use synthetic or appropriately rights-cleared fixtures. Never use an image, dataset, personal record or community-held knowledge merely because it is publicly accessible.
- Include positive, negative, boundary, failure/retry, authorization and history tests where applicable.
- Do not invent accuracy thresholds, latency budgets, availability targets, sample sizes or statistical confidence criteria. These require separately approved evaluation protocols and workload evidence.
- Preserve taxonomic uncertainty and competing source assertions. Test fixtures must not encode an unresolved taxonomic interpretation as settled truth.
- Keep AI inference, user confirmation, community assessment, expert review, scientific determination, rights eligibility and publication status distinct.
- Do not expose sensitive species coordinates or personal information in test evidence.
- A passing workflow test cannot close a Task 05 DR/LDM finding or substitute for scientific/legal review.

## 4. Acceptance test catalogue

## AC-001 — Guided identification reaches a result or explicit unknown/insufficient-evidence state

**Source wording:** A user can complete a guided identification workflow from image capture/upload to a result or an explicit unknown/insufficient-evidence state.

**Traceability:** ID-001–ID-004, ID-009; WF-001, WF-002, WF-015, WF-016; BI-CAP-02, BI-CAP-10.

### Proposed cases

| Test ID | Scenario and steps | Expected result |
|---|---|---|
| ATP-001-01 | Submit one rights-cleared image through the supported capture/upload route; complete required prompts; follow the identification session to completion. | Session reaches a documented outcome; input media and session are linked; the user can understand the result or explicit abstention. |
| ATP-001-02 | Submit multiple images belonging to one identification session. | Each asset remains individually identifiable and linked to the same session; no silent replacement or loss of image provenance. |
| ATP-001-03 | Submit a deliberately blurred, dark, obstructed or otherwise unsuitable fixture. | Quality assessment is represented; the system requests additional evidence or returns an explicit insufficient-evidence outcome; no unjustified confident species result. |
| ATP-001-04 | Submit a fixture outside the documented supported coverage. | The system returns an explicit outside-coverage/unknown outcome where that state is defined; it does not force a top-ranked species. |
| ATP-001-05 | Interrupt network or inference processing and retry. | Retry behavior is documented; no duplicate observation or unintended side effect; the run history remains traceable. |
| ATP-001-06 | Use a fixture with no plant detected. | The result is an identification outcome only; it does not create an ecological absence or survey non-detection record. |

**Required evidence:** end-to-end journey, input/output linkage, failure and abstention behavior, supported-coverage definition, model/pipeline versions, and test fixture rights record.

**Open prerequisites:** supported coverage definition, evidence-quality protocol, model outcome vocabulary and product UX semantics.

## AC-002 — AI confidence is not represented as scientific certainty

**Source wording:** The system does not represent AI confidence as scientific certainty.

**Traceability:** ID-004, ID-005, ID-008; WF-001, WF-003, WF-005; BI-CAP-02, BI-CAP-06, BI-CAP-15.

### Proposed cases

| Test ID | Scenario and steps | Expected result |
|---|---|---|
| ATP-002-01 | Inspect identification result screens and labels for a result with a model score. | UI distinguishes model score/confidence from scientific certainty and expert verification; no unsupported probability or certainty wording. |
| ATP-002-02 | Inspect API payloads, schemas, exports and analytics fields for the same result. | Machine-readable fields preserve score semantics and provenance; no field silently maps a raw similarity score to a probability or verified taxon. |
| ATP-002-03 | Supply a high-scoring but deliberately misleading/out-of-distribution fixture. | The result does not imply scientific certainty; appropriate uncertainty/abstention and review pathways remain available. |
| ATP-002-04 | Compare score labels and explanatory text across mobile, web, API and notifications. | Semantics are consistent across channels and accessible without relying on color alone. |

**Required evidence:** terminology inventory, UI/API/export review, model-score documentation, calibration evidence if probability language is proposed, and adversarial/out-of-distribution fixtures.

**Open prerequisites:** score semantics, calibration protocol, uncertainty communication and approved vocabulary.

## AC-003 — Identification results show alternatives and supporting evidence

**Source wording:** Identification results can show alternatives and supporting evidence.

**Traceability:** ID-004, ID-005, ID-008; WF-001, WF-002; BI-CAP-02, BI-CAP-06.

### Proposed cases

| Test ID | Scenario and steps | Expected result |
|---|---|---|
| ATP-003-01 | Run a fixture with several plausible candidates. | Multiple candidates can be displayed with unambiguous ordering and score semantics; alternatives are not discarded solely to force a single answer. |
| ATP-003-02 | Inspect evidence linked to each candidate. | Evidence is attributed to its actual source/type and is not fabricated or incorrectly presented as a taxonomic authority. |
| ATP-003-03 | Use a fixture with conflicting or incomplete evidence. | Conflict/absence of evidence is visible; the system does not imply that every candidate has equal support. |
| ATP-003-04 | Open a candidate's cited scientific source or provenance details. | Source identity, version/date and scope are available where recorded; a platform inference is distinguishable from a source assertion. |

**Required evidence:** multi-candidate fixtures, evidence provenance, candidate-ranking explanation, and UI/API consistency review.

**Open prerequisites:** evidence ontology, ranking semantics and source-link display rules.

## AC-004 — A user can create a structured observation from an identification

**Source wording:** A user can create a structured observation from an identification.

**Traceability:** OBS-001; WF-007; BI-CAP-04, BI-CAP-09, BI-CAP-10.

### Proposed cases

| Test ID | Scenario and steps | Expected result |
|---|---|---|
| ATP-004-01 | Convert an identification session into a structured observation. | Observation is created with a traceable link to the originating session and selected evidence; user attribution and relevant time/place metadata are preserved according to permissions. |
| ATP-004-02 | Create an observation from a session with no taxon determination. | Valid observation can exist without a fabricated taxon or forced species assignment. |
| ATP-004-03 | Add more than one media asset to an observation. | Media assets remain separately identifiable, with individual provenance and rights metadata; no assumption that an image is a specimen. |
| ATP-004-04 | Retry observation creation after a transient failure. | Idempotency prevents accidental duplicate observations or duplicate linked side effects. |

**Required evidence:** observation workflow, entity relationship validation, attribution and media-rights records, retry/idempotency logs.

**Open prerequisites:** Task 05 model validation for Observation/Event/Occurrence/Organism/MaterialEntity and observation lifecycle approval.

## AC-005 — Review does not automatically change the authoritative species record

**Source wording:** An observation can be routed for review without changing the authoritative species record automatically.

**Traceability:** VAL-001, VAL-002, OBS-002; WF-003–WF-006, WF-012; BI-CAP-04, BI-CAP-06, BI-CAP-12.

### Proposed cases

| Test ID | Scenario and steps | Expected result |
|---|---|---|
| ATP-005-01 | Submit an observation to review. | Review case is created; authoritative taxonomic records remain unchanged. |
| ATP-005-02 | User confirms an AI candidate. | User response is recorded separately; no authoritative determination is created solely by user confirmation. |
| ATP-005-03 | Community participants agree with a candidate. | Community assessment is recorded separately; agreement count does not automatically create expert verification. |
| ATP-005-04 | Qualified reviewer records a determination with evidence and rationale. | New attributable determination/review record is created within the reviewer's authority; prior AI and user records remain traceable. |
| ATP-005-05 | Two reviewers disagree. | Both assessments and evidence remain represented; dispute/escalation is possible; no silent overwrite or forced consensus. |
| ATP-005-06 | A determination is superseded. | New determination links to prior determination; historical record remains accessible under authorization. |
| ATP-005-07 | A reviewer without required authority attempts a determination. | Action is denied or escalated; attempt and reason are auditable. |

**Required evidence:** authorization matrix, review/determination event history, negative tests, reviewer authority evidence, dispute and supersession reconstruction.

**Open prerequisites:** definition of scientific verification by claim type, reviewer qualifications, scope of authority, conflicts, appeals and community governance.

## AC-006 — Species information displays accepted name, taxonomy, distribution and provenance when data exists

**Source wording:** Species information can display accepted name, taxonomy, distribution and provenance when data exists.

**Traceability:** ID-007, ID-008, SCI-001, SCI-002; WF-012, WF-013; BI-CAP-01, BI-CAP-03, BI-CAP-05.

### Proposed cases

| Test ID | Scenario and steps | Expected result |
|---|---|---|
| ATP-006-01 | Render a profile from a fixture with a source-backed accepted-name assertion and taxonomic treatment. | Name and taxonomy are displayed with source/treatment context; source-specific concept is not collapsed into an unqualified universal truth. |
| ATP-006-02 | Render a profile with competing taxonomic treatments. | Competing treatment assertions remain distinguishable and appropriately attributed; unresolved disagreement is not hidden. |
| ATP-006-03 | Render distribution data from multiple sources with different geographic scopes. | Each distribution assertion retains its source, geographic scope, temporal context and status; no false contradiction or unsupported synthesis. |
| ATP-006-04 | Render a profile where distribution or provenance data is absent. | Missing information is shown as unavailable/unknown; no invented distribution or source. |
| ATP-006-05 | Inspect links and citations for scientific information. | Source identity, source version/date and relevant limitations are discoverable where available; AI-generated inference is labelled separately. |
| ATP-006-06 | Render a profile with restricted location information. | Public profile respects disclosure policy; precise sensitive coordinates do not leak through page source, API, metadata or related views. |

**Required evidence:** taxonomic fixtures with documented treatments, source-specific distribution assertions, provenance completeness report, missing-data tests and sensitive-location negative tests.

**Open prerequisites:** DR-01–DR-12 as applicable, especially source authority, treatment semantics, distribution scope, Darwin Core/TCS mapping and independent taxonomic review. This test suite does not resolve those findings.

## AC-007 — Taxonomic changes are versioned

**Source wording:** Taxonomic changes can be versioned.

**Traceability:** SCI-002; WF-012; BI-CAP-01.

### Proposed cases

| Test ID | Scenario and steps | Expected result |
|---|---|---|
| ATP-007-01 | Add a new taxonomic treatment/version for a taxon concept. | New version/treatment is recorded; prior treatment and provenance remain accessible. |
| ATP-007-02 | Change accepted-name or synonym mapping under a new source/treatment. | Change is represented as a versioned/source-scoped assertion; historical view remains reproducible. |
| ATP-007-03 | Query the taxonomic view as of an earlier date/version. | System can reconstruct the earlier source/treatment view without overwriting historical facts. |
| ATP-007-04 | Introduce conflicting source treatments. | Both assertions remain represented with attribution and scope; no automatic consensus unless an approved policy explicitly governs a derived view. |

**Required evidence:** version history, source/treatment provenance, historical query results and reconciliation tests.

**Open prerequisites:** DR-01–DR-05 and DR-08–DR-12, canonical treatment/concept/name semantics and qualified taxonomic review. Physical schema remains gated.

## AC-008 — Administrative and expert permissions differ from ordinary user permissions

**Source wording:** Administrative and expert permissions are separated from ordinary user permissions.

**Traceability:** SEC-001, VAL-001, ADMIN-001; WF-004–WF-006, WF-014; BI-CAP-12, BI-CAP-13.

### Proposed cases

| Test ID | Scenario and steps | Expected result |
|---|---|---|
| ATP-008-01 | Execute the approved role/permission matrix against ordinary user, community contributor, expert/reviewer and administrator roles. | Each role receives only the explicitly approved capabilities; no role inherits broad privileges by accident. |
| ATP-008-02 | Ordinary user attempts a restricted expert/admin action through UI and direct API call. | Both paths deny the action; hiding a UI control alone is insufficient. |
| ATP-008-03 | Expert attempts a determination outside their approved claim/taxonomic scope. | Action is denied or escalated; authority scope is checked server-side. |
| ATP-008-04 | Administrator performs moderation or configuration action. | Privileged action is authenticated, authorized, reasoned where required and audit logged; admin status does not bypass scientific or rights constraints. |
| ATP-008-05 | Revoke or change a user's role while a session/token exists. | Effective permissions update according to the approved revocation policy; stale privileges do not persist beyond the defined window. |
| ATP-008-06 | Test conflicting interests or reviewer recusal. | Conflict policy is enforced where defined; reviewer cannot silently approve their own restricted/conflicted case. |

**Required evidence:** approved role/permission/authority matrix, threat model, API negative tests, privileged-action audit and revocation tests.

**Open prerequisites:** identity model, detailed authorization policy, reviewer qualification and conflict-of-interest policy.

## AC-009 — Core APIs are versioned and documented

**Source wording:** Core APIs are versioned and documented.

**Traceability:** API-001; WF-015; BI-CAP-14.

### Proposed cases

| Test ID | Scenario and steps | Expected result |
|---|---|---|
| ATP-009-01 | Validate the published API contract against deployed API behavior. | Versioned OpenAPI or equivalent contract accurately describes routes, schemas, authentication, authorization, errors and supported operations. |
| ATP-009-02 | Run consumer contract tests against the current API version. | Request/response schemas and documented behavior match actual behavior. |
| ATP-009-03 | Introduce a backward-compatible change. | Existing supported clients continue to work under the documented compatibility policy. |
| ATP-009-04 | Introduce a deliberately breaking contract change in a test branch/environment. | Versioning/deprecation rules are applied; compatibility break is not silently introduced under the same contract version. |
| ATP-009-05 | Test errors, pagination, filtering, rate limiting and authorization. | Consistent documented behavior; no leakage of restricted records or sensitive coordinates through alternate query paths. |
| ATP-009-06 | Test API export of internal states not represented in an external profile. | Mapping is loss-aware; unknown/unsupported internal states are not coerced into stronger or false external assertions. |

**Required evidence:** API inventory, versioned contract, generated/validated docs, schema/consumer tests, compatibility report and security tests.

**Open prerequisites:** API inventory, versioning/deprecation policy, authentication/authorization contract, pagination/error conventions and export mapping specification.

## AC-010 — Location, media and account data have defined privacy controls

**Source wording:** Location, media and account data have defined privacy controls.

**Traceability:** SEC-002, PRIV-001, RIGHTS-001, GEO-001; WF-008–WF-011, WF-013; BI-CAP-04, BI-CAP-05, BI-CAP-07, BI-CAP-10–BI-CAP-14.

### Proposed cases

| Test ID | Scenario and steps | Expected result |
|---|---|---|
| ATP-010-01 | Submit an observation with a sensitive species location and inspect public/private views. | Public output follows the approved precision/disclosure policy; authorized access is separately controlled and audited. |
| ATP-010-02 | Attempt to retrieve precise coordinates through API, search, export, cached page, logs, analytics, media metadata and backup/restore paths. | No unauthorized path discloses restricted coordinates or reconstructable derivatives. |
| ATP-010-03 | Upload media with embedded EXIF/location metadata. | Metadata is handled according to the approved privacy policy; original and derivative rights/provenance remain distinguishable. |
| ATP-010-04 | Submit a media asset with unknown or purpose-limited rights. | Unknown rights do not imply permission; relevant display, redistribution, embedding or AI-training use is blocked pending documented assessment. |
| ATP-010-05 | Confirm display permission but deny AI-training permission. | Display use is considered only within its permitted scope; AI-training/fine-tuning/embedding pipeline rejects the asset for prohibited purposes. |
| ATP-010-06 | Change account privacy settings or submit a withdrawal/deletion request. | The system applies the approved lifecycle policy for access, restriction, deletion, anonymization and retention; it does not promise universal deletion where lawful retention or scientific audit duties apply. |
| ATP-010-07 | Inspect public publication suspension. | Public delivery is suppressed across API, search, caches and exports while internal records remain governed by authorized retention/access rules. |
| ATP-010-08 | Restore data from backup after a restriction/deletion event. | Approved suppression/retention controls are re-applied; backups do not silently re-expose restricted information. |

**Required evidence:** approved privacy/rights/data-retention policies, data inventory, threat model, end-to-end disclosure tests, media metadata tests, rights decision records, backup/restore tests and qualified legal review.

**Open prerequisites:** current Indian legal applicability review; data subject/account lifecycle policy; sensitive biodiversity disclosure policy; asset/purpose rights matrix; community consent and withdrawal governance. This plan is not a legal opinion or compliance certification.

## AC-011 — AI model can be replaced without redesigning the entire product

**Source wording:** The architecture can accommodate replacement of the AI model without redesigning the entire product.

**Traceability:** AI-001, AI-003; BI-CAP-02, BI-CAP-15. WF-010 concerns AI-use rights and is not by itself evidence of model replaceability.

### Proposed cases

| Test ID | Scenario and steps | Expected result |
|---|---|---|
| ATP-011-01 | Run the same rights-cleared evaluation fixture through Model A behind the approved model interface. | Product-facing request/response contract is stable and model-specific implementation remains behind the adapter boundary. |
| ATP-011-02 | Replace Model A with Model B that implements the same approved contract. | Core product workflows continue without redesigning unrelated product modules; model-specific differences are captured in metadata and evaluation results. |
| ATP-011-03 | Compare outputs across model versions. | Model, weights, pipeline, preprocessing and taxonomy reference versions are recorded; outputs are not treated as equivalent merely because schemas match. |
| ATP-011-04 | Roll back to the prior approved model version. | Rollback is controlled, auditable and does not rewrite prior identification runs. |
| ATP-011-05 | Replace model with one that lacks a capability or has different score semantics. | Capability/semantic mismatch is explicit; adapter does not fabricate equivalent fields or silently relabel scores. |
| ATP-011-06 | Attempt to use a model/data asset without documented rights eligibility. | Model release/training/inference path is blocked as required by the asset-purpose rights policy; no permission is inferred from availability. |

**Required evidence:** approved model interface/contract, two independently implemented model adapters or equivalent replacement proof, regression report, model registry/provenance, rollback exercise and rights eligibility records.

**Open prerequisites:** AI architecture contract, model registry, score semantics, evaluation protocol, rights policy and model release governance.

## AC-012 — Data model can support future STF biodiversity projects

**Source wording:** The data model can support future Save Tiger First biodiversity projects.

**Traceability:** NFR-MAINT-001, NFR-PORT-001, SCI-001; BI-CAP-01, BI-CAP-07, BI-CAP-14.

### Proposed cases

| Test ID | Scenario and steps | Expected result |
|---|---|---|
| ATP-012-01 | Review domain ownership boundaries for STF shared capabilities and Botanica Indica domain concepts. | Reusable platform services are separated from botanical semantics; botanical taxonomy/observation assumptions are not imposed as universal STF concepts. |
| ATP-012-02 | Model a second, clearly bounded biodiversity domain use case using shared platform capabilities without changing Botanica Indica scientific meaning. | Reuse is demonstrated through stable interfaces and bounded extensions; no forced reuse of plant-specific entities or vocabularies. |
| ATP-012-03 | Export/consume shared identity, media, geography, audit and API contracts from a hypothetical second STF domain. | Shared contracts are documented and portable; access, rights and privacy remain domain/purpose-specific. |
| ATP-012-04 | Review cross-domain data sharing and permissions. | No cross-domain access or reuse is implied by shared infrastructure; purpose, authority, rights and sensitive-data rules are explicit. |
| ATP-012-05 | Assess whether proposed common abstractions preserve domain-specific provenance and scientific uncertainty. | Shared platform does not erase source authority, evidence type, temporal scope or domain-specific scientific semantics. |

**Required evidence:** architecture/domain-boundary review, a bounded second-domain reference scenario, contract tests, data-flow and rights review, and explicit record of what is shared versus domain-owned.

**Open prerequisites:** STF ecosystem boundary decision, ADR-011 status/review, Task 04 architecture reconciliation, rights/privacy model and a credible second-domain use case. This criterion does not authorize broad STF platform expansion by assumption.

## 4.13 ODR-01 — Controlled external-export validation supplement

**Status:** Proposed / Not run. This is a cross-cutting scientific/export validation supplement linked to the existing Task 03 acceptance criteria; it is **not** a thirteenth Task 03 acceptance criterion and does not approve an export profile, scientific model, API or implementation.

**Policy boundary:** ODR-01 is owner-authorized for controlled, profile-specific external exports only. Missing internal records must remain unknown/not assessed; they must never create an internal absence assertion or negative Occurrence. A bounded “not detected/reported within the stated survey scope under documented survey conditions” interpretation may appear only in an eligible external export after all required scope, reporting-completeness, method, provenance, version and mapping conditions have been verified. Otherwise, fail closed and omit the interpretation.

**Traceability:** AC-004, AC-006, AC-009 and AC-010 as applicable; OBS-001/OBS-002, SCI-001 and GEO-001; ODR-01; EVT-27–EVT-44; DR-01, DR-07 and DR-09; BI-CAP-04, BI-CAP-05, BI-CAP-07 and BI-CAP-14. EVT scenarios remain proposed validation obligations, not executed tests.

| Test ID | Scenario and steps | Expected result | EVT mapping |
|---|---|---|---|
| ATP-ODR-01 | Prepare an export where an approved target profile, explicit Survey/Event scope, reporting completeness, method, effort, time/place, provenance and pinned mapping are all present and validated. | Only the controlled external export may carry the bounded not-detected/reported interpretation. The source survey evidence and export transformation are attributable and auditable. No internal negative Occurrence is created. | EVT-27, EVT-30 |
| ATP-ODR-02 | Repeat the export with required scope, completeness, method, effort or provenance missing, unreported, ambiguous or contradictory. | Export fails closed for the implicit interpretation; the interpretation is omitted. Internal state remains unknown/not assessed. | EVT-28, EVT-31, EVT-38 |
| ATP-ODR-03 | Exercise nested Event/Survey records with scope specified at each applicable level; include missing child scope, mismatched time/place and attempts to infer completeness from a parent or child. | Scope and hierarchy are explicit and valid at each applicable level. No silent inheritance, child-to-parent completeness derivation or unsupported spatiotemporal relationship is accepted. | EVT-29, EVT-32, EVT-39, EVT-43, EVT-44 |
| ATP-ODR-04 | Compare a priori and post-facto target declarations; include taxa recorded as bycatch or outside the declared target scope. | Target origin, author, method and timestamp remain attributable. Bycatch and out-of-scope taxa do not satisfy target reporting completeness. | EVT-33, EVT-34, EVT-35, EVT-40 |
| ATP-ODR-05 | Query an internal Event/Survey scope for which no Occurrence row exists, without an explicit qualifying survey result. | No internal absence assertion and no negative Occurrence are inferred from the missing row. State remains unknown/not assessed. | EVT-37 |
| ATP-ODR-06 | Record an explicit, attributable survey result and compare it with the controlled export interpretation. | Explicit survey evidence remains distinct from an implicit export transformation; the export does not rewrite or back-propagate an internal scientific assertion. | EVT-36 |
| ATP-ODR-07 | Exercise MaterialEntity, MediaAsset, Observation, Organism and Occurrence combinations, including one media asset depicting multiple organisms and uncertain grouping. | Each entity/evidence type remains distinct; grouping uncertainty, attribution and provenance are retained. Media is not treated as a specimen or proof of an occurrence by itself. | EVT-41, EVT-42 |
| ATP-ODR-08 | Generate the export using pinned Conceptual Model, term, profile and mapping versions; deliberately substitute an unpinned or incompatible version. | Export records exact version identifiers and uses only validated mappings. Unpinned, incompatible or unresolved terms cause the relevant interpretation to be omitted or export to fail closed. DR-09 remains open until exact versioned resources and term semantics are verified. | EVT-30; DR-09 |

**Required evidence before any case can be finalized:** approved target export profile and version; approved mapping and term pins; validated Event/Survey/Occurrence semantics; reproducible synthetic fixtures; expected-result oracle reviewed by qualified biodiversity-informatics and field-ecology specialists; and auditable execution records. The tests must use synthetic or rights-cleared data and must not expose sensitive species locations or personal information.

**Open prerequisites:** ODR-01 conditions are authorized as policy interpretation only; the export profile, Task 05C/05D model, DR/LDM findings, DR-09 term-version comparison, API contract and validation oracles remain open. These test designs do not authorize Task 05E or physical schema design.

## 5. Coverage and dependency summary

| AC | Test cases | Principal dependencies | Proposed readiness |
|---|---:|---|---|
| AC-001 | 6 | ID workflow, model outcomes, coverage, rights-cleared fixtures | Blocked pending workflow/AI definitions |
| AC-002 | 4 | Score semantics, uncertainty and calibration policy | Blocked pending AI evaluation definitions |
| AC-003 | 4 | Candidate/evidence model and source provenance | Blocked pending evidence model |
| AC-004 | 4 | Observation lifecycle and Task 05 entity semantics | Blocked pending Task 05 validation |
| AC-005 | 7 | Reviewer authority, determination model, disputes and history | Blocked pending scientific governance |
| AC-006 | 6 | Taxonomy, source authority, distribution and provenance model | Blocked by applicable DR findings and expert review |
| AC-007 | 4 | Versioned taxonomic treatment/concept model | Blocked by DR-01–DR-04 and expert review |
| AC-008 | 6 | Identity, role/authority matrix, threat model | Blocked pending authorization policy |
| AC-009 | 6 | API inventory, contract and compatibility policy | Blocked pending API design |
| AC-010 | 8 | Privacy, rights, location, retention and legal review | Blocked pending policy/legal review |
| AC-011 | 6 | Model interface, registry, evaluation and rights policy | Blocked pending AI architecture and evaluation |
| AC-012 | 5 | STF/BI domain boundary, shared contracts, second-domain scenario | Blocked pending architecture and boundary review |
| ODR-01 export-validation supplement (cross-cutting; not a new AC) | 8 | Approved profile, survey scope/completeness, method, hierarchy, bycatch, version pins and scientific validation | Blocked pending profile, scientific and specialist review |
| **Total** | **74** |  | **All proposed / not run** |

“Blocked” here means the test cannot yet be finalized as an executable acceptance gate. It does not imply that the eventual product cannot meet the criterion.

## 6. Test-level strategy

When implementation begins, execute tests at multiple levels:

1. **Unit tests:** deterministic state transitions, authorization predicates, rights eligibility rules, schema validators and mapping functions.
2. **Component tests:** media intake, identification orchestration, taxon resolution, observation/review modules, publication and privacy enforcement.
3. **Contract tests:** API schemas, model adapter contract, source adapters and export mappings.
4. **Integration tests:** identity, media storage, database, queues, search, model services, audit and publication channels.
5. **End-to-end tests:** user journeys and cross-role workflows across supported clients.
6. **Security/privacy tests:** negative authorization, sensitive-location leakage, media metadata, logs, caches, exports, backup/restore and retention.
7. **Scientific validation:** representative rights-cleared evaluation datasets, taxonomic expert review, source provenance and uncertainty/calibration assessment. These are not reducible to software QA.
8. **Operational tests:** retry, idempotency, recovery, observability, backup restoration and incident reconstruction.

The same test may have several levels. A unit test passing does not prove an end-to-end acceptance criterion.

## 7. Release acceptance and evidence gates

A future release may claim an AC is accepted only when:
- its test cases and expected outcomes have been approved;
- all required policies, scientific definitions and API contracts are stable enough to test;
- fixtures are representative enough for the stated claim and rights-cleared for the test purpose;
- execution records identify exact build, environment and test evidence;
- all failures are resolved or covered by a documented, owner-approved exception with risk and expiry;
- relevant scientific, privacy, security, rights and accessibility reviews are completed by qualified reviewers;
- no blocking Task 05 scientific-model issue invalidates the test's data assumptions.

A test-plan approval is not a release approval. A software test pass is not a scientific validation certificate or legal compliance certificate.

## 8. Open decisions requiring owner/reviewer direction

| ID | Decision | Affected AC |
|---|---|---|
| ATP-OD-01 | Supported plant/geographic/taxonomic coverage and abstention vocabulary | AC-001, AC-002, AC-003 |
| ATP-OD-02 | Model score semantics, calibration and uncertainty language | AC-002, AC-003, AC-011 |
| ATP-OD-03 | Evidence quality ontology and evaluation protocol | AC-001, AC-003, AC-006 |
| ATP-OD-04 | Reviewer qualification, authority scope, conflict and appeal policy | AC-005, AC-008 |
| ATP-OD-05 | Definition of scientifically verified by claim type | AC-005, AC-006, AC-007 |
| ATP-OD-06 | Canonical taxonomic treatment/concept and source reconciliation model | AC-006, AC-007 |
| ATP-OD-07 | Privacy, account lifecycle, withdrawal, deletion, anonymization and retention | AC-010 |
| ATP-OD-08 | Rights matrix by asset and purpose, including AI training and embeddings | AC-003, AC-010, AC-011 |
| ATP-OD-09 | Sensitive biodiversity location tiers and disclosure paths | AC-006, AC-010 |
| ATP-OD-10 | API versioning, compatibility, errors, pagination and loss-aware export | AC-009 |
| ATP-OD-11 | Model adapter contract, model registry and rollback semantics | AC-011 |
| ATP-OD-12 | STF shared-platform boundaries and approved second-domain scenario | AC-012 |

No reviewer or owner is assigned by this document. Dates and numeric thresholds are intentionally not invented.

## 9. Review checklist

- [ ] All twelve Task 03 acceptance criteria are retained without rewriting their source wording.
- [ ] Test cases are sufficiently specific to become executable.
- [ ] Every test has positive and negative coverage appropriate to its risk.
- [ ] Fixtures have documented provenance, rights and privacy classification.
- [ ] Scientific and AI evaluation criteria are reviewed by qualified people.
- [ ] Rights and privacy cases are reviewed by qualified legal/privacy advisers.
- [ ] Sensitive biodiversity information is protected across all delivery and derivative paths.
- [ ] API/model contracts and domain boundaries are consistent with Task 04 and accepted ADRs.
- [ ] Task 05 DR/LDM blockers are not misrepresented as resolved.
- [ ] Test evidence and exception handling are auditable.
- [ ] Test-plan approval is distinguished from product/release approval.

## 10. Recommended next action

Review this proposed test plan with the project owner and relevant product, architecture, botanical, AI/ML, security, privacy and rights specialists. Then:
1. accept, revise or reject the proposed test cases;
2. resolve prerequisite policies and scientific-model blockers;
3. prepare test fixtures and contracts with documented rights/provenance;
4. convert ready cases into executable tests only after implementation design is stable;
5. retain all execution evidence in the project repository or approved evidence system.

Keep Task 03 v0.1 unchanged until an explicitly approved PRD revision is prepared.

**End of proposed test plan — STF-BI-ATP-001 v0.2.**
