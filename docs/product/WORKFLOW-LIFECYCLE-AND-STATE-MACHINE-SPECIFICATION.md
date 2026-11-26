# Botanica Indica — Workflow Lifecycle and State-Machine Specification

**Document ID:** STF-BI-WF-001  
**Version:** 0.2 — Proposed synchronization-state terminology clarification  
**Status:** Proposed for owner and discipline review; not an approved product requirement, scientific governance policy, data model or implementation authorization  
**Prepared:** 23 November 2026  
**Owner/decision authority:** Save Tiger First project owner  
**Related documents:** Task 03 PRD working baseline; Full Product Vision and Capability Blueprint v0.2; Requirements Traceability Register v0.3; Workflow-to-Requirements Crosswalk v0.2; Offline and Field Synchronization Specification v0.2; API Command and Idempotency Contract v0.2; Task 04 architecture working baseline; accepted ADR-004, ADR-006, ADR-007 and ADR-009; Task 05 scientific data-model proposals.

---

## 1. Purpose and governing constraints

Task 03 and the Full Product Vision describe submitted, AI-assisted, user-confirmed, community-supported/reviewed, expert-reviewed, scientifically verified, disputed, rejected, withdrawn and published conditions. They do not define one complete state machine.

This proposal separates independent lifecycles that must not be compressed into one status field:

1. An identification run is not an observation.
2. A candidate taxon is not a determination.
3. User confirmation is not expert review or scientific verification.
4. Community support is not automatically scientific authority.
5. Moderation status is not scientific status.
6. Publication status is not scientific validity or rights clearance.
7. Withdrawal, restriction, deletion and retention are different operations.
8. A later determination must not erase an earlier assertion or its provenance.

The model is a set of related state machines, not one linear progression.

## 2. Terminology

| Term | Meaning in this proposal |
|---|---|
| IdentificationRun | Versioned execution of an identification pipeline against supplied evidence and context |
| Candidate | Taxon or higher-rank hypothesis returned by a run, with score semantics and supporting/contradicting evidence |
| User confirmation | Contributor's explicit response to a candidate; not an authoritative scientific determination |
| Community assessment | Scoped contribution or assessment by eligible community participants under a defined policy |
| Expert assessment | Review action by a reviewer acting within recorded qualifications and authority |
| Determination | Attributable, evidence-backed taxonomic assertion with scope, rationale and treatment context |
| Scientific verification | Governed status assigned only under an approved policy and qualified authority |
| Observation | Record of a plant encounter or observation event, independent of whether a taxon is identified |
| Contribution | Submitted content or data proposed for inclusion or use by the platform |
| Publication | Making an approved record or representation available to a defined audience/channel |
| Restriction | Limiting access, processing, display or use for a stated reason and scope |

Exact entity relationships remain subject to Task 05 model reconciliation. These terms do not settle DR-01–DR-12 or LDM-01–LDM-16.

## 3. State-machine boundaries

The following lifecycles are independent but linked by immutable or versioned references:

- IdentificationRun lifecycle.
- Observation lifecycle.
- Contribution/moderation lifecycle.
- Review case lifecycle.
- Determination lifecycle.
- Publication/distribution lifecycle.
- Rights and privacy eligibility lifecycle.

A transition in one lifecycle must not silently mutate another. Moderation rejection must not rewrite a scientific determination; publication withdrawal must not delete underlying evidence; a new expert determination must not alter the original AI run.

## 4. IdentificationRun lifecycle — proposed

### 4.1 Candidate outcomes

| State | Meaning |
|---|---|
| requested | Valid request accepted for processing |
| queued | Awaiting execution |
| processing | Pipeline execution underway |
| completed_with_candidates | One or more candidates produced |
| completed_insufficient_evidence | Pipeline completed but evidence did not support a defensible candidate |
| completed_out_of_coverage | Input or taxon outside declared supported coverage |
| completed_ambiguous | Evidence supports multiple unresolved alternatives |
| completed_no_plant_detected | System did not detect a supported plant subject; not proof of absence |
| failed_retryable | Technical failure may be retried under idempotency rules |
| failed_terminal | Processing cannot continue without a materially changed request or intervention |
| cancelled | Run cancelled before completion |

### 4.2 Rules

- Preserve pipeline, model, reference-data and taxonomy versions, input asset references, execution time, parameters and score semantics.
- Store candidates and their evidence separately from user or expert determinations.
- Do not force a top-1 result when evidence is insufficient.
- A retry creates a separately identifiable execution linked to the earlier run; do not overwrite it.
- completed_no_plant_detected is a model/input outcome, not a biodiversity non-detection survey record.
- A similarity score must not be represented as a calibrated probability unless validated and documented.
- Run completion does not imply observation publication or scientific verification.

## 5. User response and community assessment — proposed

User responses should be recorded as attributable events attached to a specific run/candidate version, not as edits to the candidate itself.

Proposed response types:

- accepted_as_personal_view;
- rejected_by_user;
- unsure;
- challenged;
- additional_evidence_submitted;
- review_requested;
- no_response.

A user response records that user's view at that time. It must not promote a candidate into an expert determination or scientific verification state.

Community assessments should be separate records with participant eligibility, scope, evidence, policy version, conflicts where relevant, timestamps and moderation controls. A count of agreeing users is not a substitute for qualified scientific review.

## 6. Observation lifecycle — proposed

### 6.1 Candidate states

| State | Meaning |
|---|---|
| draft | Locally or remotely created but not submitted |
| submitted | Submitted for platform processing or review |
| record_created (proposed replacement for the ambiguous prior label `received`) | A canonical Observation resource has actually been created and committed, with its durable domain identifier |
| needs_information | Required contextual information missing or clarification requested |
| under_review | A defined review process is active |
| accepted_for_record | Accepted for the stated internal record purpose; not necessarily public |
| restricted | Access/use limited by privacy, rights, safety or governance controls |
| withdrawn_by_contributor | Contributor requested withdrawal, subject to lawful retention and audit obligations |
| rejected_for_record | Not accepted for the stated record purpose, with reason and appeal/correction route where applicable |
| archived | Retained in a non-active state under an approved retention policy |

### 6.2 Rules

- An observation may exist without an identification or taxon determination.
- Observation, Event, Survey, Occurrence, Organism and MaterialEntity remain distinct concepts; exact links are subject to Task 05 review.
- Submission or acceptance does not mean public publication.
- A change in identification does not rewrite the original observation event.
- withdrawn_by_contributor does not itself mean immediate physical deletion from all systems.
- The observation lifecycle must support correction and supersession without erasing prior versions.
- Non-detection must be represented only in an appropriately bounded survey/event context with protocol, effort, time, place and reporting completeness.

### 6.3 Separation from synchronization receipt state — proposed clarification

The former label `received` was ambiguous because the API/offline contract separately uses `server_received` for a durable command receipt that may exist before domain processing commits. These are different state domains.

For this proposed revision:
- `server_received` belongs only to the client/API command receipt lifecycle. It means the command envelope/receipt is durably recorded; it does not prove an Observation resource exists.
- `record_created` is the proposed Observation lifecycle label for the point at which a canonical Observation resource has actually been created and committed.
- A command receipt, HTTP response, upload completion or local draft must not set the Observation state to `record_created`.
- If processing fails after durable receipt, the Observation lifecycle must not be advanced to `record_created`.
- The exact event/transaction that creates the Observation identifier remains subject to the final API and Task 05 model decisions.

This is a proposed terminology clarification, not an approved state-machine decision or implementation instruction. The project owner and product/scientific/API reviewers must review it before workflow or API freeze.

## 7. Contribution and moderation lifecycle — proposed

Contribution moderation is a trust-and-safety/content-governance process, not scientific review.

Candidate states:

- draft;
- submitted;
- screening;
- needs_clarification;
- approved_for_stated_use;
- rejected_for_stated_use;
- quarantined_pending_rights;
- restricted;
- withdrawn_or_retracted;
- archived_under_policy.

Rules:

- Approval must name the specific permitted purpose(s), channels, audience and relevant rights/consent basis.
- Rights clearance for one purpose (for example, display) does not automatically authorize redistribution, commercial use, model training, fine-tuning or embeddings.
- Dataset-level permission does not automatically clear embedded media.
- Unknown rights remain unresolved; they are not approval.
- Moderation decisions must record policy version, actor, reason, scope and appeal/reconsideration route.
- Moderation approval must not confer scientific authority or alter taxonomic determinations.

## 8. Review case lifecycle — proposed

A review case coordinates work; it does not itself contain scientific truth.

Candidate states:

- opened;
- triaged;
- assigned;
- awaiting_evidence;
- under_assessment;
- assessment_recorded;
- escalated;
- closed_with_disposition;
- reopened.

Candidate dispositions include: supports_existing_determination, proposes_new_determination, disagreement_unresolved, insufficient_evidence, outside_authority, rights_or_privacy_blocked and administrative_closure. The controlled vocabulary requires expert-governance review.

Rules:

- Record reviewer identity, role/qualification evidence, authority scope, assignment, timestamps, conflicts and policy version.
- Reviewer authority must be claim- and task-appropriate; an account role alone is insufficient.
- A reviewer may abstain, request more evidence, disagree or act only within their authority.
- Conflicting expert assessments must remain visible to authorized reviewers; do not force consensus.
- Review closure does not automatically publish a record.

## 9. Determination lifecycle — proposed

Determinations are versioned assertions, not mutable status labels.

A determination record should capture subject and scope under the approved logical model; taxon concept/name and treatment context; supporting and contradicting evidence; asserting agent and authority basis; method, rationale and date; uncertainty and limitations; source and relevant version; and supersession/correction relationship, if any.

Possible lifecycle labels:

- proposed;
- active_within_scope;
- disputed;
- superseded;
- retracted_with_reason;
- invalidated_with_reason.

These labels describe the record's governance lifecycle, not a universal confidence ranking. A later determination creates a new assertion and links to the earlier one. The earlier record remains historically interpretable.

“Scientifically verified” must be defined by a separately approved policy specifying eligible claim types, reviewer authority, evidence threshold, taxonomic treatment, scope, audit and expiry/review conditions. It must not be assigned automatically from model confidence, community agreement or unqualified user confirmation.

## 10. Publication lifecycle — proposed

Publication is channel- and audience-specific.

Candidate states:

- not_eligible;
- eligible_pending_release;
- published_internal;
- published_restricted;
- published_public;
- publication_suspended;
- withdrawn_from_channel;
- superseded_in_channel.

Publication eligibility is the conjunction of relevant gates:

- scientific status appropriate to the claim and channel;
- rights eligibility for the exact use;
- privacy and sensitive-location policy;
- moderation and safety status;
- data quality and provenance requirements;
- audience, export and API policy.

A record may be accepted internally but not eligible for public display or bulk export. Withdrawing a public representation does not erase legally or scientifically required audit history.

## 11. Rights, privacy and restriction lifecycle — proposed

Rights and privacy decisions must be purpose-specific and may change independently of scientific status.

For each asset/data element and purpose, track an eligibility result such as:

- not_assessed;
- eligible;
- eligible_with_conditions;
- ineligible;
- unknown_or_unverified;
- suspended_pending_review;
- expired_or_revoked.

Purpose dimensions should distinguish at least collection, storage, processing, internal review, public display, API access, export/redistribution, commercial use, model training, fine-tuning and embedding/index creation.

Privacy/sensitive-location restriction is a separate policy decision. It must propagate to APIs, exports, search, caches, logs, analytics, media metadata and backups as appropriate. Hiding a map pin alone is insufficient.

## 12. Cross-lifecycle invariants

1. No lifecycle status substitutes for another lifecycle's status.
2. Every consequential transition records actor/system identity, timestamp, reason, policy/model version and relevant evidence.
3. Prior assertions and decisions remain traceable; correction is append-only or versioned.
4. A failed or abstaining identification run remains a valid recorded outcome.
5. User confirmation, community assessment, expert review and scientific verification remain distinguishable.
6. Moderation does not determine taxonomy.
7. Scientific review does not grant rights.
8. Rights approval does not establish scientific correctness.
9. Publication does not imply unrestricted reuse.
10. Restriction propagates to all relevant derived and delivery paths.
11. Deletion, withdrawal, anonymization, restriction, archival and scientific audit retention require separate rules and legal review.
12. No absence claim is inferred from missing records or an unsuccessful image classifier.
13. External exports map internal statuses loss-aware; unknown or unsupported states must not be silently coerced into a stronger status.

## 13. Transition governance and event record

Before implementation, each transition must specify:

- source state and target state;
- initiating actor and required authority;
- preconditions and required evidence;
- policy/version applicable at transition time;
- reason code and rationale where appropriate;
- side effects and notifications;
- reversibility/compensation behavior;
- audit event and idempotency behavior;
- visibility and disclosure consequences;
- appeal, correction or reopening route;
- tests for allowed and prohibited transitions.

Do not use a generic administrator override to bypass scientific, rights or privacy controls. Emergency restriction may be necessary, but must be separately authorized, logged, time-bounded and reviewed.

## 14. Required validation scenarios

These are proposed acceptance scenarios, not claims of implementation or test execution.

| ID | Scenario | Required outcome |
|---|---|---|
| WF-001 | AI run returns several candidates | All candidates retained; no automatic authoritative determination |
| WF-002 | Evidence insufficient | Explicit abstention/insufficient-evidence result; no forced species |
| WF-003 | User confirms candidate | User response recorded; scientific status unchanged |
| WF-004 | Community supports candidate | Community assessment recorded separately; no automatic expert verification |
| WF-005 | Expert disagrees with AI | New attributable determination; AI run retained |
| WF-006 | Two experts disagree | Both assessments preserved; unresolved dispute supported |
| WF-007 | Observation submitted without taxon | Valid observation persists without fabricated identification |
| WF-008 | Observation withdrawn | Withdrawal recorded; retention/deletion policy applied separately |
| WF-009 | Contribution rights unknown | Relevant use quarantined/restricted pending assessment |
| WF-010 | Display permission exists but AI-training permission does not | Display may be considered under its own conditions; AI use remains ineligible |
| WF-011 | Sensitive coordinates restricted | Restriction applies to API, export, search, caches, logs and media derivatives |
| WF-012 | Expert determination superseded | New determination linked; old determination remains historically accessible under authorization |
| WF-013 | Public publication suspended | Public channel suppressed without deleting underlying evidence |
| WF-014 | Reviewer lacks authority for claim type | Transition rejected or escalated; action audited |
| WF-015 | Retry after transient inference failure | New linked run; idempotency prevents duplicate side effects |
| WF-016 | Classifier reports no plant detected | No ecological absence/non-detection assertion created |

## 15. Open decisions and approval gates

| ID | Decision required | Required reviewer |
|---|---|---|
| WF-OD-01 | Confirm separate state machines and boundaries | Product owner and architect |
| WF-OD-02 | Approve identification outcome vocabulary and retry semantics | AI/ML and product reviewers |
| WF-OD-03 | Define reviewer roles, qualifications, delegated authority and conflicts | Qualified botanical governance reviewers |
| WF-OD-04 | Define “scientifically verified” for each claim type | Scientific governance |
| WF-OD-05 | Define community assessment scope and legitimate community authority | Community governance and relevant experts |
| WF-OD-06 | Define observation correction, withdrawal, deletion and retention | Product, privacy and legal reviewers |
| WF-OD-07 | Define contribution rights/purpose eligibility and appeal | Rights/legal and community governance |
| WF-OD-08 | Define publication thresholds by audience and claim risk | Scientific, rights, privacy and product reviewers |
| WF-OD-09 | Map logical states to Task 05 entities without resolving open DR/LDM findings by assumption | Data architect and scientific reviewers |
| WF-OD-10 | Define notification, offline synchronization and concurrent transition behavior | Architecture and UX reviewers |

No named reviewer is assumed or assigned by this document.

## 16. Relationship to requirements and validation

This specification elaborates the lifecycle gap already recorded in the Requirements Traceability Register. It does not change the 19 original Task 03 functional requirement IDs, the 12 original acceptance criteria, the seven non-goals, accepted ADRs or the scientific data model.

Before implementation:
1. Link each approved workflow rule to requirements and acceptance cases.
2. Map logical states and events to the reconciled Task 05 model.
3. Resolve applicable DR/LDM blockers and major findings.
4. Define authorization, rights, privacy and publication policies.
5. Create executable transition, negative-authorization, concurrency, audit and data-retention tests.
6. Obtain owner and discipline approval.

Physical schema design remains gated by scientific-model review and other project operating gates.

---

**End of proposed specification — STF-BI-WF-001 v0.2.**
