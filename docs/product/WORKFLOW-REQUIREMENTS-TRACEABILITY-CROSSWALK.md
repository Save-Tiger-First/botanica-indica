# Botanica Indica — Workflow-to-Requirements Traceability Crosswalk

**Document ID:** STF-BI-RTM-WF-001  
**Version:** 0.2 — Proposed source-provenance and ODR-01 traceability reconciliation  
**Status:** Proposed for owner and discipline review; not an approved requirement, acceptance plan, scientific policy or implementation authorization  
**Prepared:** 23 November 2026  
**Decision authority:** Save Tiger First project owner  
**Repository:** `Save-Tiger-First/botanica-indica`  
**Working branch:** `docs/requirements-traceability-register`

## 1. Purpose and decision boundary

This crosswalk links the 16 proposed workflow validation scenarios in STF-BI-WF-001 v0.1 to the original Task 03 requirements, Task 03 acceptance criteria, proposed capability identifiers, accepted ADRs and relevant Task 05 scientific-model review items.

It is a traceability aid. It does not:
- add, amend or approve a Task 03 requirement;
- convert a proposed workflow state into an approved product status;
- close DR-01–DR-12 or LDM-01–LDM-16;
- approve a reviewer qualification, rights basis, retention rule or publication policy;
- assert that any test has been implemented or passed;
- authorize physical database design or application implementation.

Task 03 remains authoritative for original requirement and acceptance-criterion wording until the project owner accepts a revised PRD. The Requirements Traceability Register remains the current working traceability source.

## 2. Source revisions inspected

| Source | Branch/ref | File blob SHA | Use |
|---|---|---|---|
| AI Project Operating Prompt v1.0 | `docs/repository-audit-and-ai-operating-standard` | `53add3894d0502827e584614c70ad09cadaa637d` | Operating and approval rules |
| Task 03 PRD working baseline | `docs/canonical-task-03-04-baselines` | `8b1ca0be04b3f4ad3b543c2f9fc48d46eb37faf8` | Original requirements, acceptance criteria and non-goals |
| Requirements Traceability Register v0.3 | `docs/requirements-traceability-register` | `1c799a2ae2f4580e216f8b03be369f15d62e224c` | Requirement, capability, ADR, LDM and ODR-01 mappings |
| Workflow Lifecycle Specification v0.1 | `docs/requirements-traceability-register` | `03ca940095a9e39c5608548bdeec1ce0166bf76d` | Sixteen proposed workflow scenarios |

These are the source revisions revalidated for this crosswalk on 23 November 2026. Earlier SHAs in v0.1 are historical snapshots. Re-fetch before any later approval or implementation decision.

## 3. Mapping conventions

- Requirement IDs and acceptance-criterion IDs are reproduced from the current RTM. They are not renumbered here.
- Capability IDs `BI-CAP-01`–`BI-CAP-16` remain proposed pending owner approval.
- ADR references identify existing accepted architectural decisions; this crosswalk does not amend them.
- DR/LDM references identify dependencies or relevant validation cases, not resolved findings.
- A blank dependency is intentionally not inferred.
- Test descriptions are proposed verification obligations, not evidence of execution.
- Where a scenario has no direct Task 03 acceptance criterion, that gap is stated rather than forcing a weak mapping.

## 4. Workflow scenario traceability matrix

| Workflow scenario | Scenario summary | Original Task 03 requirement links | Task 03 acceptance criteria | Proposed capability links | Accepted ADRs | Task 05 dependency / validation | Proposed evidence / test obligation |
|---|---|---|---|---|---|---|---|
| WF-001 | One AI run returns multiple candidates | ID-004, ID-005, ID-008 | AC-001, AC-002, AC-003 | BI-CAP-02, BI-CAP-06, BI-CAP-15 | ADR-004, ADR-006, ADR-007 | DR-02, DR-05, DR-06; LDM-06 | Deterministic multi-candidate fixture; candidate ordering and score semantics; prove candidate list does not create an authoritative determination; retain model, pipeline and taxonomy versions |
| WF-002 | Evidence insufficient for a defensible identification | ID-002, ID-003, ID-009 | AC-001, AC-003 | BI-CAP-02, BI-CAP-10, BI-CAP-15 | ADR-006, ADR-007 | LDM-05, LDM-06 | Low-quality/partial-evidence fixtures; explicit abstention; request additional evidence where appropriate; no forced species-level result |
| WF-003 | User confirms an AI candidate | ID-008; OBS-001 only if the interaction is separately converted to an observation | AC-002, AC-005 | BI-CAP-02, BI-CAP-04, BI-CAP-06, BI-CAP-09, BI-CAP-10 | ADR-006, ADR-007, ADR-009 | DR-06; LDM-05–LDM-07 | Record attributable user response against exact run/candidate version; verify authoritative determination status remains unchanged; test UI/API wording |
| WF-004 | Community participants support a candidate | VAL-001; VAL-002 only where a review disposition is recorded | AC-005, AC-008 | BI-CAP-06, BI-CAP-09, BI-CAP-12, BI-CAP-13 | ADR-007, ADR-009 | DR-05, DR-06; LDM-07 | Community assessment stored separately from expert determination; eligibility, policy version, conflicts and moderation recorded; no automatic scientific verification from agreement count |
| WF-005 | Expert assessment disagrees with AI result | ID-008, VAL-002, OBS-002 | AC-002, AC-005 | BI-CAP-02, BI-CAP-06, BI-CAP-12, BI-CAP-13 | ADR-004, ADR-006, ADR-007, ADR-009 | DR-02, DR-05, DR-06; LDM-07 | Create new attributable determination or assessment; preserve AI run and earlier assertions; record rationale, authority scope and evidence |
| WF-006 | Two experts disagree | VAL-001, VAL-002, OBS-002 | AC-005, AC-008 | BI-CAP-06, BI-CAP-12, BI-CAP-13 | ADR-004, ADR-007, ADR-009 | DR-05, DR-06; LDM-07 | Preserve both expert assessments, authority scopes and evidence; unresolved dispute remains representable; prohibit forced consensus or silent overwrite |
| WF-007 | Observation submitted without a taxon determination | OBS-001, OBS-002 | AC-004 | BI-CAP-04, BI-CAP-09, BI-CAP-10 | ADR-007, ADR-008, ADR-009 | DR-07; LDM-05, LDM-08, LDM-09 | Create valid observation with media/context and no fabricated taxon; test distinction among Observation, Event, Survey, Occurrence, Organism and MaterialEntity against approved model |
| WF-008 | Contributor withdraws an observation | OBS-002, SEC-002; PRIV-001 is a proposed derived requirement in the RTM | AC-010 | BI-CAP-04, BI-CAP-06, BI-CAP-09, BI-CAP-13 | ADR-004, ADR-008, ADR-009 | LDM-11, LDM-12, LDM-15 | Record withdrawal request and disposition; separately test restriction, export suppression, lawful retention, deletion/anonymization policy and audit trail; no universal deletion promise |
| WF-009 | Contribution has unknown or unverified rights | ID-001, SCI-001; RIGHTS-001 is proposed derived requirement | AC-010 | BI-CAP-02, BI-CAP-07, BI-CAP-09, BI-CAP-13, BI-CAP-15 | ADR-004, ADR-010 | LDM-12, LDM-15; DR-10, DR-12 | Unknown rights do not authorize the proposed use; quarantine/restrict relevant processing; preserve asset-level and source/dataset-level rights provenance |
| WF-010 | Display permission exists but AI-training permission does not | SCI-001; RIGHTS-001 and AI-001 are proposed derived requirements | AC-010; AC-011 only for the separate model-provider replaceability aspect, not rights permission itself | BI-CAP-07, BI-CAP-09, BI-CAP-15 | ADR-004, ADR-006, ADR-010 | LDM-12, LDM-15; DR-10, DR-12 | Purpose-specific rights test: permitted display does not imply training, fine-tuning, embedding or redistribution permission; deny disallowed AI pipeline use and record decision basis |
| WF-011 | Sensitive coordinates are restricted | ID-006, SEC-002; PRIV-001 and GEO-001 are proposed derived requirements | AC-010 | BI-CAP-04, BI-CAP-05, BI-CAP-07, BI-CAP-10, BI-CAP-11, BI-CAP-13, BI-CAP-14 | ADR-004, ADR-008, ADR-009, ADR-010 | LDM-11, LDM-14, LDM-15; DR-08 | End-to-end negative disclosure tests for API, export, search, caches, logs, analytics, media metadata and backups; test permitted generalized precision and boundary-version provenance |
| WF-012 | Expert determination is superseded | VAL-002, OBS-002, SCI-002 | AC-005, AC-006, AC-007 | BI-CAP-01, BI-CAP-04, BI-CAP-06, BI-CAP-12, BI-CAP-13 | ADR-004, ADR-005, ADR-007, ADR-009, ADR-010 | DR-05, DR-06; LDM-01–LDM-04, LDM-07 | New determination linked to prior one; preserve prior evidence and treatment context; verify historical queries and current-view derivation without mutating source assertions |
| WF-013 | Public publication is suspended | SCI-001, SEC-002; RIGHTS-001 and PRIV-001 are proposed derived requirements | AC-006, AC-010 | BI-CAP-03, BI-CAP-05, BI-CAP-06, BI-CAP-07, BI-CAP-11, BI-CAP-13, BI-CAP-14 | ADR-004, ADR-008, ADR-010 | LDM-11, LDM-12, LDM-15; DR-08, DR-10, DR-12 | Public channel suppression while authorized internal record/evidence remains governed; verify caches, APIs, exports, search and derived assets; record reason, scope and authority |
| WF-014 | Reviewer lacks authority for the claim type | VAL-001, SEC-001 | AC-008 | BI-CAP-06, BI-CAP-12, BI-CAP-13 | ADR-007, ADR-009; ADR-002, ADR-003 for authorization enforcement | DR-05, DR-12; LDM-07 | Negative authorization tests by claim type, taxonomic scope and reviewer authority; reject/escalate action; audit attempted and authorized transitions |
| WF-015 | Retry after transient inference failure | ID-001, ID-003, ID-009, API-001, OPS-001; NFR-REL-001 is proposed derived requirement | AC-001, AC-009 | BI-CAP-02, BI-CAP-07, BI-CAP-10, BI-CAP-14, BI-CAP-15, BI-CAP-16 | ADR-002, ADR-003, ADR-006, ADR-010 | DR-10; LDM-13 | Failure injection, idempotency and duplicate-side-effect tests; linked run history; preserve model/pipeline versions and source input references |
| WF-016 | Classifier reports no plant detected | ID-002, ID-009 | AC-001 | BI-CAP-02, BI-CAP-10, BI-CAP-15 | ADR-006, ADR-007 | DR-07; LDM-05 | No-plant-detected outcome must not create an ecological absence/non-detection record; test that only a properly scoped survey/event can represent non-detection |

## 5. Acceptance-criterion coverage review

All twelve Task 03 acceptance criteria were inspected. The following table distinguishes direct coverage from partial or absent coverage.

| Acceptance criterion | Workflow scenario coverage | Assessment |
|---|---|---|
| AC-001 — guided identification to result or unknown/insufficient state | WF-001, WF-002, WF-015, WF-016 | Direct coverage; end-to-end UI and capture details still require broader journey tests |
| AC-002 — confidence is not scientific certainty | WF-001, WF-003, WF-005 | Direct semantic coverage; score calibration remains separate AI evaluation work |
| AC-003 — alternatives and supporting evidence | WF-001, WF-002 | Direct coverage |
| AC-004 — structured observation from identification | WF-007 | Direct coverage for observation creation without forcing taxon assignment |
| AC-005 — observation review does not rewrite authoritative species record | WF-003, WF-004, WF-005, WF-006, WF-012 | Direct governance coverage |
| AC-006 — species information displays accepted name, taxonomy, distribution and provenance where data exists | WF-012, WF-013 | Partial; profile rendering and source-backed content require separate acceptance tests |
| AC-007 — taxonomic changes are versioned | WF-012 | Direct lifecycle coverage; treatment-aware scientific-model validation remains open |
| AC-008 — admin/expert permissions differ from ordinary users | WF-004, WF-006, WF-014 | Partial; full role matrix and administrative journeys require separate security tests |
| AC-009 — core APIs are versioned and documented | WF-015 | Partial; API contract, compatibility, error, pagination and authorization tests are not supplied by workflow scenarios |
| AC-010 — location, media and account data have privacy controls | WF-008, WF-009, WF-010, WF-011, WF-013 | Partial; account-data controls and comprehensive privacy/legal review require separate coverage |
| AC-011 — replace AI model without redesigning product | None directly | Gap; requires a separate model-adapter/contract and replacement acceptance case |
| AC-012 — data model supports future STF biodiversity projects | None directly | Gap; requires a separate domain-boundary and portability architecture acceptance case |

**Coverage finding:** the 16 workflow scenarios do not replace the 12 acceptance criteria. AC-011 and AC-012 are architectural acceptance obligations outside the workflow lifecycle. AC-006, AC-008, AC-009 and AC-010 also need additional tests beyond the current workflow scenarios.

## 6. Original requirement coverage and scope protection

The crosswalk uses only original Task 03 identifiers present in the current RTM. It does not renumber the 19 original functional requirements.

The seven Task 03 non-goals remain unchanged. No workflow scenario authorizes:
- redefining the product as a plant-care/reminder application;
- making disease diagnosis a core requirement;
- adding e-commerce or marketplace functionality as a core requirement;
- making a generic AI chatbot the primary interface;
- treating species count as sufficient evidence of quality;
- freezing a programming language, AI model, database or cloud provider in the PRD;
- claiming scientific accuracy targets before representative data and a measurement protocol exist.

The proposed workflow states do not create a new product capability domain or change the proposed `BI-CAP-01`–`BI-CAP-16` map.

## 7. Task 05 dependency handling

This crosswalk references DR/LDM items only where the current RTM already links them or where the scenario directly depends on the stated model distinction. It does not resolve any scientific-model issue.

Mandatory safeguards:
- DR-01–DR-04 remain blocking before logical model stabilization.
- DR-05–DR-07 remain necessary for determination, observation and relationship semantics.
- DR-08–DR-12 remain open according to the scientific review register.
- LDM-01–LDM-16 remain validation obligations; references here do not mean tests passed.
- Physical schema design remains gated by the Task 05 scientific-model reconciliation and independent review.

### 7.1 ODR-01 controlled external-export traceability

ODR-01 is owner-authorized for controlled, profile-specific external exports only. The internal rule remains unchanged: a missing Occurrence row alone is unknown/not assessed and never creates an internal absence assertion. ODR-01 does not approve Task 05C/05D/05E, a final export profile, physical schema, API payload or implementation.

| Validation cases | Workflow / requirement relationship | Required workflow behavior |
|---|---|---|
| EVT-27, EVT-30 | Survey/non-detection and export-specific acceptance obligations; BI-CAP-04/05/07/14 | Apply only inside a separately approved, version-pinned external export profile; do not add an export interpretation to the internal Observation lifecycle. |
| EVT-28, EVT-31, EVT-38 | WF-007, WF-011; OBS-001/OBS-002, SCI-001 | Missing, incomplete, unreported, ambiguous or contradictory completeness/method evidence fails closed; no interpretation is emitted. |
| EVT-29, EVT-32, EVT-39, EVT-43, EVT-44 | WF-007 and relevant event/survey workflows; OBS-001/OBS-002, GEO-001 | Explicit scope at every applicable level; parent/child spatiotemporal containment; no silent inheritance or child-derived parent completeness. |
| EVT-33, EVT-34, EVT-35, EVT-40 | Survey target workflow; OBS-001/OBS-002 | Preserve a priori/post-facto origin, author, method and timestamp. Bycatch/out-of-scope taxa do not satisfy target reporting completeness. |
| EVT-36, EVT-37 | WF-007; OBS-001/OBS-002 | Explicit internal result must be attributable and survey-bounded; no Occurrence row without an explicit result remains unknown/not assessed. |
| EVT-41, EVT-42 | WF-007 and media/observation workflows; ID-001, OBS-001, SCI-001 | Keep MaterialEntity, MediaAsset, Observation, Organism and Occurrence distinct; retain grouping uncertainty. |

These are proposed validation obligations, not executed tests. Reporting completeness, sampling effort and detectability remain separate. The export wording is “not detected/reported within the stated survey scope under documented survey conditions”, not biological absence. DR-09 remains open for exact versioned-resource reconciliation.

## 8. Proposed test-case decomposition

Before implementation, decompose each WF scenario into:
1. positive transition test(s);
2. prohibited transition / negative authorization test(s);
3. persistence and history test(s);
4. concurrency/idempotency test(s), where relevant;
5. privacy/rights disclosure test(s), where relevant;
6. export/API mapping test(s), where relevant;
7. audit reconstruction test(s);
8. test fixture provenance and rights eligibility record.

Each executable case should have a stable test ID, preconditions, actor/authority, input fixture, action, expected state/event, prohibited side effects, evidence artifact, test environment and result. No test should be marked passed until an actual run and retained evidence exist.

## 9. Open decisions and gaps

| ID | Open item | Impact | Required decision/evidence |
|---|---|---|---|
| RTM-WF-OD-01 | Definition of scientifically verified by claim type | WF-005, WF-006, WF-012 | Approved scientific governance policy and qualified review |
| RTM-WF-OD-02 | Reviewer qualification, authority scope and conflicts | WF-004–WF-006, WF-014 | Role/authority matrix and conflict/appeal policy |
| RTM-WF-OD-03 | Rights purpose vocabulary and evidence standard | WF-009, WF-010, WF-013 | Asset/purpose rights policy and legal review |
| RTM-WF-OD-04 | Withdrawal, deletion, anonymization and retention | WF-008, WF-013 | Current Indian legal/privacy review and approved retention schedule |
| RTM-WF-OD-05 | Sensitive biodiversity location tiers and propagation | WF-011, WF-013 | Threat model, disclosure policy and end-to-end verification |
| RTM-WF-OD-06 | API state vocabulary and loss-aware export mapping | All relevant WF cases | Versioned contract and export mapping review |
| RTM-WF-OD-07 | AC-011 model replacement test | AC-011 | Separate architecture acceptance case |
| RTM-WF-OD-08 | AC-012 STF biodiversity reuse test | AC-012 | Domain-boundary and portability acceptance case |
| RTM-WF-OD-09 | AC-006 species profile acceptance coverage | AC-006 | Separate profile rendering/source evidence test suite |
| RTM-WF-OD-10 | AC-009 complete API acceptance coverage | AC-009 | Contract, compatibility, authorization and operational tests |
| RTM-WF-OD-11 | Offline synchronization, local storage and concurrent field updates | WF-OD-10; Task 03 §§17, 20, 28; AC-004, AC-009, AC-010 | Proposed Offline and Field Synchronization Architecture & Validation Specification; OFF-001–OFF-036; owner and specialist decisions remain open |
| RTM-WF-OD-12 | Command identity, idempotent replay, durable receipts, revision conflicts and change-feed recovery | WF-OD-10; Task 03 §§19–20; AC-004, AC-009, AC-010 | Proposed API Command, Idempotency and Conflict-Resolution Contract Design; API-SYNC-001–042; API-OD-01–20 open |

### 9.1 Offline and field synchronization specification

The offline/field synchronization design and proposed validation matrix are documented separately in [STF-BI-ARCH-OFF-001 — Offline and Field Synchronization Architecture & Validation Specification](../architecture/OFFLINE-FIELD-SYNCHRONIZATION-ARCHITECTURE-AND-VALIDATION-SPECIFICATION.md). It elaborates WF-OD-10 and Task 03 §§17, 20 and 28. The specification is Proposed; it does not create an accepted ADR, authorize implementation or resolve Task 05 logical-model blockers. Its OFF-001–OFF-036 cases are not executed.

### 9.2 API command and synchronization contract

The server-side command contract is documented in [STF-BI-API-SYNC-001 — API Command, Idempotency and Conflict-Resolution Contract Design](../architecture/API-COMMAND-IDEMPOTENCY-AND-CONFLICT-RESOLUTION-CONTRACT-DESIGN.md). It elaborates the offline architecture and AC-004/AC-009/AC-010 dependencies. It is Proposed; endpoints, schemas, status semantics and numeric policies are not approved or implemented. API-SYNC-001–042 are proposed scenarios and have not been executed.

Keep three state domains separate: (1) client synchronization states such as queued, uploading, server_received and applied; (2) the Observation lifecycle in the Workflow Lifecycle specification; and (3) scientific identification, expert-review, rights and publication decisions. A server receipt or applied command is not scientific validation, public acceptance or publication. The offline and API proposals distinguish durable server receipt from committed domain effect, and persistent client-command identity from HTTP request-retry idempotency. HTTP 412 is a failed conditional precondition; HTTP 409 is a documented domain/idempotency conflict, not an interchangeable synonym.

The generic command endpoint and any synchronous resource-write façade must share the same domain command processor, authorization, idempotency, revision, audit and receipt controls. The route choice remains open. API-OD-01–20 and OFF-OD-01–16 remain open pending owner and specialist review. The IETF Idempotency-Key document is an active Internet-Draft, not a published RFC.

## 10. Review and approval checklist

The project owner and relevant discipline reviewers should confirm:

- [ ] The scenario-to-requirement mappings are correct and do not alter source requirements.
- [ ] The capability references use the proposed 16-domain map.
- [ ] All 12 original acceptance criteria remain in scope.
- [ ] Partial and absent acceptance coverage is accepted as explicitly recorded.
- [ ] No Task 05 blocker is treated as resolved by this crosswalk.
- [ ] Reviewer authority and scientific verification remain subject to qualified governance.
- [ ] Rights, privacy and sensitive-location controls remain purpose- and channel-specific.
- [ ] Test evidence requirements are sufficient for future independent review.

No reviewer is named or assumed. No approval is implied by this document's creation.

## 11. Next recommended action

After owner and discipline review, incorporate accepted mappings into the canonical RTM and create a separate acceptance-test plan covering all twelve ACs, including AC-011 and AC-012. Keep the original Task 03 source unchanged until an explicitly approved PRD revision is prepared.

**End of proposed crosswalk — STF-BI-RTM-WF-001 v0.2.**
