# Botanica Indica — Offline and Field Synchronization Architecture & Validation Specification

**Document ID:** STF-BI-ARCH-OFF-001  
**Version:** 0.2 — Proposed source-provenance and ODR-01 offline safeguards reconciliation  
**Status:** Proposed for project-owner and specialist review; not an accepted ADR or implementation authorization  
**Date:** 23 November 2026  
**Repository:** `Save-Tiger-First/botanica-indica`  
**Working branch:** `docs/requirements-traceability-register`  
**Decision authority:** Save Tiger First project owner

---

## 1. Executive recommendation

Botanica Indica should support **offline field capture and safe deferred synchronization** on its Flutter mobile application. Offline capability should be deliberately bounded: it must protect field observations and media from connectivity loss without pretending that the device can make current authoritative scientific, rights, publication or sensitive-location decisions while disconnected.

The recommended design is a **local-first field-capture workflow with a durable client outbox, server-authoritative acceptance, idempotent command processing, version-aware reconciliation and policy-aware cache invalidation**.

The mobile client may create and edit local drafts, attach media, retain a queued submission, show synchronization status and cache a limited, versioned subset of non-sensitive reference data. Once online, it submits commands and media to the API. The server validates identity, authorization, schema, rights, location sensitivity, record version and domain invariants before accepting the operation. A server acknowledgement—not merely a successful local save or HTTP upload—marks the relevant operation as accepted by the platform.

This is a proposed design, not a final physical data model. It deliberately avoids deciding Task 05 entity cardinalities, database tables, SQL types, UUID version, encryption implementation, API endpoints or a specific Flutter plugin.

**Core rule:** offline capture must never convert a provisional local draft into a scientific determination, public observation, rights approval or authoritative server record by implication.

## 2. Scope and source baseline

### 2.1 In scope

- Flutter mobile field workflows under intermittent or absent connectivity.
- Local observation drafts and queued submissions.
- Optional locally retained media and upload staging.
- Selective, versioned reference-data cache.
- Durable outbox and retryable synchronization.
- Idempotent server command handling.
- Conflict detection and explicit resolution.
- Offline status and user feedback.
- Device-local privacy, security, storage and account lifecycle.
- Sensitive-location and rights-policy revalidation on the server.
- Validation scenarios, operational telemetry and recovery.

### 2.2 Out of scope

- Offline expert determinations, taxonomic authority changes or scientific verification.
- Guaranteed offline AI identification or on-device inference. That is a separate evaluation and rights decision under Task 03 AC-011 and ADR-006.
- Offline publication, bulk export, institutional integration or rights approval.
- Peer-to-peer device synchronization.
- A promise that background synchronization will run at an exact time or while the app is terminated.
- A physical database schema, final API specification, vendor selection or production deployment topology.
- A browser/PWA offline guarantee. The current Task 03 offline requirements principally concern the mobile field workflow; web offline scope remains an explicit product decision.

### 2.3 Exact source revisions inspected

| Source | Ref | Blob SHA | Relevant scope |
|---|---|---|---|
| AI Project Operating Prompt STF-AI-OPS-001 v1.0 | `docs/repository-audit-and-ai-operating-standard` | `53add3894d0502827e584614c70ad09cadaa637d` | Architecture, rights, scientific and branch guardrails |
| Task 03 PRD v0.1 | `docs/canonical-task-03-04-baselines` | `8b1ca0be04b3f4ad3b543c2f9fc48d46eb37faf8` | §§17, 20, 28; mobile, offline, reliability and privacy requirements |
| Task 04 Architecture v0.1 | `docs/canonical-task-03-04-baselines` | `abc7b721fae8d4f4adede4dd0bf5d6a32098c5a3` | Asynchronous work, idempotency, offline inference boundary and durable queues |
| Workflow Lifecycle Specification v0.2 | `docs/requirements-traceability-register` | `d100a988b50d128941d4823fc4a3243ca755eadd` | §§6.3 and related lifecycle sections; distinct Observation creation and command receipt semantics |
| Workflow-to-Requirements Crosswalk v0.2 | `docs/requirements-traceability-register` | `75a10b27648b0184c3956203ba49f54715bdeaf2` | WF-007, WF-008, WF-011, WF-013, WF-015, WF-OD-10 and ODR-01/EVT-27–EVT-44 export traceability |
| Acceptance Test Plan STF-BI-ATP-001 v0.1 | `docs/requirements-traceability-register` | `0e7a1d1851492bb4470b2e0fea6991e59db67f2a` | AC-004, AC-009, AC-010 and operational/security test strategy |
| ADR-006 Identification Architecture | `main` | `f35345c356725d7dc4b1b64971c0ff59758c8a30` | Identification and sensitive-input constraints |
| ADR-008 Geospatial and Sensitive Location Data | `main` | `74cc3774799a29b28edab75fc63d129f8841b497` | Precision, privacy, access and disclosure controls |
| ADR-009 Observation and Contribution Model | `main` | `c096da58dfe0f1eb46812db46e6555ccf01b8718` | Observation as a distinct, versioned scientific record |
| Task 05C Logical Database Model v0.1 | `docs/task-05d-logical-model-validation-v3` | `e6131e867d4bc3dbc58aa1188d0fabc895429347` | Logical entities and relationships; not physical design |
| Task 05D Validation & Physical Design Readiness v0.1 | `docs/task-05d-logical-model-validation-v3` | `cf0b9c10bcb2da7b102e52688f22bd8e8b69bb91` | Open scientific/data-model validation and implementation gates |
| Task 03–04 Readiness Audit STF-BI-AUD-034 v0.1 | `docs/requirements-traceability-register` | `f3e9c6998104b5435c24b4b70d136ced763245f5` | Offline synchronization identified as a major architecture gap |

Source interpretation: Task 03 requires offline-capable field workflows where feasible, selective caching, defined online/offline identification behavior, safe queued observation synchronization, visible sync status/failures and storage/privacy controls. Task 04 calls for idempotent operations and durable queues for asynchronous processing, while explicitly separating offline/on-device inference for evaluation. The workflow specification keeps observation, identification, rights, publication, restriction and deletion lifecycles distinct.

### 2.4 Governing accepted decisions

- **ADR-006:** identification is evidence-backed and must preserve uncertainty, history and sensitive-input restrictions. This specification does not approve offline inference.
- **ADR-008:** precise coordinates are not automatically public; access and geographic precision are separate; restrictions must be enforced beyond the UI.
- **ADR-009:** Observation is a first-class record distinct from identification and contribution; observation history and provenance must remain understandable.
- **ADR-004:** provenance is required for consequential transformations and assertions.
- **ADR-002/003:** preserve modular boundaries and API contracts; no requirement here mandates microservices.

No accepted ADR is amended or superseded by this specification.

## 3. Architecture principles

1. **Local draft is not server acceptance.** A local save confirms only that the device persisted the draft.
2. **Server remains authoritative for shared platform state.** The device may hold a working copy and pending commands, not an unqualified second scientific source of truth.
3. **Observation is not identification.** A draft observation can exist without any taxon or IdentificationRun.
4. **Scientific assertions are not last-write-wins documents.** Determinations and expert assessments are attributable, versioned assertions; they must not be overwritten by synchronization conflict resolution.
5. **Rights and restrictions are re-evaluated at the point of server processing and publication.** A permission or sensitivity decision cached yesterday is not proof of current eligibility.
6. **At-least-once delivery, idempotent effects.** Network retries can repeat a request. The server must make repeated submission of the same logical command safe. Do not claim exactly-once network delivery.
7. **No silent loss.** Unsynchronized user content must not be silently evicted, overwritten or deleted to satisfy a storage quota.
8. **Background work is opportunistic.** Foreground sync and explicit user retry are first-class paths; background execution is an optimization.
9. **Stale data is labelled.** Users can see when cached content was last synchronized and whether it may be out of date.
10. **Privacy defaults fail closed.** If current sensitivity or rights status cannot be established, do not disclose or process protected content through an uncertain path.
11. **The local cache is bounded and purpose-limited.** It is not a full replica of the server database.
12. **Logical design precedes physical design.** Proposed local envelopes and queue concepts do not decide Task 05 entities, database schema or identifiers.

## 4. Proposed capability and behavior matrix

| Capability | Offline behavior | Online/server behavior | Status |
|---|---|---|---|
| Create a field observation | Save local draft; mark “Not yet submitted” | Validate and accept as a platform observation after server checks | Proposed |
| Edit an unsynchronized draft | Local edits allowed; retain draft history sufficient for recovery | Submit latest valid draft/command | Proposed |
| Edit an already synchronized observation | Queue a version-aware change; show pending state | Compare base revision; accept or return conflict | Proposed |
| Capture media | Store in app-private local storage subject to quota and rights notice | Stage upload, verify checksum/content and rights, then attach | Proposed |
| Attach exact GPS | Only with explicit location permission and purpose; protect locally | Re-evaluate disclosure tier and authorization before server storage/use | Proposed; policy dependency |
| Read cached botanical reference data | Read bounded snapshot with version/date and stale indicator | Refresh using server-provided version/cursor | Proposed |
| Search cached data | Limited to cached index/data; label incomplete/stale results | Full authorized search when connected | Proposed |
| Identification request | Explain that online identification is unavailable; optionally save a request as pending only if user chooses | Execute through approved server model pipeline | Proposed |
| On-device inference | Not included by default | Separate model/rights/evaluation gate | Not approved |
| Expert review/determination | Not available offline | Online authorized workflow | Proposed |
| Community assessment | Not available offline in initial scope | Online authorized workflow | Proposed |
| Rights eligibility/publication | No offline approval or publication | Server-side current policy evaluation | Proposed |
| Sensitive-location disclosure | Do not expose cached exact protected coordinates to public/share/export surfaces | Server enforces current policy at every delivery path | Required design constraint |
| Withdraw/delete/restrict request | May record a local request and immediately suppress local display; clearly “Pending server confirmation” | Server evaluates authority, law, retention and audit rules | Proposed; policy dependency |
| Sync status | Show queued, blocked, uploading, conflict, failed or accepted state | Server returns durable acknowledgement and canonical revision | Proposed |

### 4.1 Initial offline product boundary

The recommended first offline-capable field workflow is:
- create and edit a local observation draft;
- attach one or more local media assets;
- record date/time and optional location subject to user control;
- save without a network connection;
- review pending content and its storage status;
- submit when connected;
- retry safely after interruption;
- see whether the server accepted, rejected or needs clarification.

This is not a reduced long-term product vision. It is a bounded, testable delivery of the full product's field capability. Future offline functions can be added when their scientific, rights, security and usability requirements are justified.

## 5. Logical synchronization architecture

### 5.1 Components

**A. Flutter presentation and field workflow**
- Presents local and remote state with clear source/freshness labels.
- Does not write directly to local storage or API outside the repository/application service boundary.
- Exposes explicit “Save on device”, “Submit”, “Sync now”, “Resolve conflict” and “Discard local draft” actions.
- Never labels a local draft “Submitted”, “Verified” or “Published”.

**B. Repository/application service**
- Single client-side access boundary for field data.
- Coordinates local store, remote API and sync scheduler.
- Applies local validation and prepares commands.
- Does not implement scientific authority or rights policy independently.

**C. Local field store**
- Stores drafts, command/outbox envelopes, upload state, limited cached reference data and synchronization metadata.
- Uses transactions for local state transitions.
- Keeps pending user content distinct from downloaded cache.
- Must support schema migration, integrity checking, quota visibility and recovery.

**D. Durable outbox**
- Stores logical commands and dependency relationships until server acknowledgement or explicit resolution.
- Each command has a stable client-generated opaque **client command ID** that identifies the logical user action for its full offline lifecycle. The HTTP `Idempotency-Key` is a separate request-retry identity with its own scope, fingerprint and retention policy. The client may reuse the same opaque value for both only if the server enforces their distinct semantics. Store command type/version, target reference if one exists, base server revision, local sequence/dependency, creation time, payload reference, media references, retry state and last error classification.
- Client wall-clock time is evidence metadata, not a trusted ordering or authorization source.
- A retry resends the same logical command with the same idempotency key. A materially changed user action is a new command with a new key.

**E. Sync coordinator**
- Runs a bounded push/pull cycle.
- Applies network, battery, charging and user settings.
- Enforces dependency order and per-account isolation.
- Resumes after process termination/reboot where platform scheduling permits.
- Offers foreground/manual sync regardless of background scheduling.

**F. API and server command boundary**
- Authenticates the current user/device context.
- Validates command version, authorization, rights, policy, domain constraints and target revision.
- Deduplicates idempotency keys within a defined server policy window and scope.
- Atomically records command receipt with the corresponding domain change/acknowledgement where required.
- Returns a durable operation result, canonical server revision and any conflict/validation details.
- Rechecks current location sensitivity and rights eligibility; client assertions are not trusted as authorization.

**G. Media staging**
- Uploads media before finalizing references where required.
- Supports resumable/chunked transfer only if the selected API/storage design supports it.
- Uses content checksums to detect corruption/duplicate transfer, without assuming a checksum establishes rights or identity.
- Keeps incomplete uploads private and expires abandoned staging objects under an approved retention policy.

**H. Change feed / pull synchronization**
- Provides versioned changes or snapshots with a server cursor/revision.
- Supports tombstones/restriction updates where records become unavailable or must be purged from caches.
- Detects expired cursors and triggers controlled full reconciliation.
- Does not expose restricted content in change metadata, push payloads or error messages.

### 5.2 Logical flow

1. User creates or edits a local observation draft.
2. Client validates basic completeness and persists the draft and pending command atomically.
3. UI displays “Saved on this device — not yet submitted”.
4. When sync is triggered and prerequisites are met, coordinator checks account/session, storage, connectivity and local policy.
5. Media is staged and verified where required.
6. Client submits the command with its idempotency key and base revision.
7. Server authenticates and revalidates authorization, rights, sensitivity, schema and domain rules.
8. Server either accepts, rejects, blocks or returns a conflict.
9. Client records the server response and canonical revision transactionally.
10. Client pulls authorized changes/restrictions and refreshes affected local cache entries.
11. UI reports the final state and any action required.

A successful media upload alone is not observation acceptance. A successful HTTP response is not sufficient unless the server's durable command result confirms the operation's defined outcome.

## 6. Command identity, ordering and idempotency

### 6.1 Command identity and idempotency

The client and API contract distinguish two identities:

- **Client command ID:** generate once for each logical user action and persist it across offline storage, app restart, retry, upload recovery and long disconnection. It supports long-lived reconciliation after the HTTP idempotency window expires.
- **HTTP `Idempotency-Key`:** reuse for retries of the same HTTP operation. Its scope, request fingerprint and retention are server contract decisions. It does not replace the client command ID.

The server must scope command identity to the authenticated principal and the relevant installation/tenant context without treating a client-supplied device identifier as authentication. Account switching must not expose or replay another account's receipts. A same-ID/different-command replay must be rejected and audited without disclosing another principal's receipt.

A changed user action is a new command with a new client command ID and a new HTTP idempotency key. A transport retry retains both identities. The server must return/reconcile the prior result for a duplicate request rather than repeat the domain effect.

The server's deduplication record and domain mutation must be coordinated transactionally or by a recoverable command-processing design. Expired HTTP idempotency records must not silently make an old queued command unsafe; the durable command-ID reconciliation/tombstone policy and client-visible expiry behavior remain open API-OD-03/API-OD-04 decisions.

**Do not promise exactly-once transport.** The design target is at-least-once retry delivery with idempotent server-side effects and observable acknowledgement.

The detailed server contract is proposed in [STF-BI-API-SYNC-001](API-COMMAND-IDEMPOTENCY-AND-CONFLICT-RESOLUTION-CONTRACT-DESIGN.md).

### 6.2 Ordering and dependencies

- Commands that depend on another local command must carry an explicit dependency.
- Example: media attachment references a staged asset; observation submission may depend on successful media staging or may submit a draft with pending media according to the eventual API contract.
- Preserve order for commands that mutate the same logical aggregate when order is semantically material.
- Independent observations may synchronize concurrently within a bounded policy.
- Do not infer order from device timestamps alone.
- Server receipt/commit sequence and canonical revision govern shared state.
- A failed prerequisite blocks dependent commands and exposes the reason; it does not silently drop them.

### 6.3 Retry classification

| Result class | Client behavior |
|---|---|
| Network unavailable, timeout, transient DNS/TLS connection interruption | Retry same command/key with bounded exponential backoff and jitter; allow manual retry |
| HTTP 408/429/5xx or explicit transient server outcome | Retry according to server guidance, including Retry-After where supplied; preserve same key |
| Authentication expired | Pause queue; refresh/re-authenticate; do not change command identity |
| Authorization denied (403) | Mark blocked; no automatic retry loop; explain required account/role action |
| Validation failure (4xx domain validation) | Mark rejected/action required; preserve draft and show field-level explanation |
| Stale HTTP precondition (412) or domain-state conflict (409) | Stop automatic mutation; reconcile the receipt and enter the appropriate conflict-resolution flow; never treat the two status codes as interchangeable |
| Unsupported command/schema version | Block; require compatible client or safe migration; never reinterpret payload silently |
| Media checksum mismatch/incomplete upload | Re-stage/retry safely; do not attach unverified bytes |
| Rights unknown/revoked or location policy blocks use | Block relevant operation; preserve local record under policy; no repeated blind retry |
| User cancellation | Stop eligible pending work; retain or discard local data only according to explicit user choice and policy |

Retry limits, jitter parameters, age thresholds, maximum payloads and server idempotency retention are open quantitative decisions. Do not invent numeric production targets in this specification.

## 7. Conflict detection and resolution

### 7.1 General rule

Use server revisions/ETags or an equivalent opaque version token. A command that edits an already synchronized record must state the base revision it was derived from. If the server revision changed, return a conflict rather than silently overwriting.

**Last-write-wins is prohibited for scientific assertions, determinations, rights decisions, sensitive-location restrictions and provenance.**

### 7.2 Conflict policy by data category

| Category | Proposed policy | Why |
|---|---|---|
| New local observation draft not yet submitted | Submit as a new record using a stable opaque client command ID; server assigns/returns canonical identity | No shared server version exists yet |
| Observation descriptive metadata | If independent fields changed, server may merge only under a documented field-level policy; otherwise preserve both versions and request user resolution | Avoid losing contributor edits |
| Observation date/time/location corrections | Treat as material edits with explicit before/after, reason and provenance; require revision check and user resolution on conflict | Can alter scientific interpretation |
| Media attachments | Additive attachment relationship; preserve asset identity, checksum, order/role and rights context; conflicting removal/replace actions require explicit resolution | Media are evidence, not disposable UI attachments |
| IdentificationRun and candidate results | Immutable/versioned run outputs; retry creates a linked new run, not an overwrite | Reproducibility and model provenance |
| User confirmation/community assessment | Append attributable assessment; do not overwrite another person's assessment | Preserve independent contribution |
| Expert determination | Append new determination/supersession with authority, evidence and rationale; no merge/last-write-wins | Scientific integrity |
| Rights and permissions | Re-evaluate under current policy; revocation/suspension blocks affected uses | Rights are purpose-specific and time-sensitive |
| Sensitive-location restrictions | Apply the more restrictive current policy; stale local policy must never relax a server restriction | Conservation and privacy protection |
| Taxonomy/reference cache | Replace only from versioned authoritative server response; retain snapshot version/provenance as needed | Avoid client-created taxonomic consensus |
| Deletion/withdrawal/restriction request | Treat as a request with a server decision/result, not a local hard-delete command that implies completion | Legal retention and audit requirements differ |

### 7.3 User-facing conflict flow

1. Explain which record changed and why the local edit cannot be applied automatically.
2. Show the server version and local pending version with field-level differences where safe.
3. Do not show protected values to a user who no longer has authority to view them.
4. Offer only valid actions: use server version, submit a corrected new version, retain local copy, or request authorized review.
5. Record the user's choice and the resulting server decision.
6. Keep the original local draft until a durable outcome is confirmed or the user explicitly discards it under the retention policy.

## 8. Rights, privacy and sensitive biodiversity protection

### 8.1 Offline capture and consent

- Explain why location is requested and whether exact GPS is optional.
- Do not request location permission merely because a field screen is opened.
- Store only the precision and metadata required for the user-selected workflow.
- If exact coordinates are retained locally, protect them as sensitive data and keep them out of notifications, logs, analytics and crash reports.
- User-facing privacy controls must distinguish local-only, pending upload, server-received, private, generalized and public states where those states are supported by approved policy.
- Do not imply that “saved on device” means uploaded, backed up or safely retained elsewhere.

### 8.2 Revalidation at synchronization

The server must re-evaluate, at the time of processing:
- user authentication and current authorization;
- contribution and media rights by purpose;
- source/dataset and asset-specific rights;
- current taxon/location sensitivity rules;
- observation visibility and geographic precision permissions;
- retention, restriction, withdrawal or publication suspension state;
- current API/schema and validation policy.

A stale client cache cannot grant permission. A permission to store or display media does not imply permission for AI inference, training, embeddings, redistribution or export.

### 8.3 Sensitive-location cache behavior

- Do not cache exact protected coordinates for public/offline discovery.
- If a legitimate authorized field workflow requires exact coordinates offline, use a separately protected local representation and explicit purpose/permission; this is an open policy/security approval, not a default.
- When sensitivity status is unknown or stale, suppress external disclosure and do not send exact coordinates to third-party AI or mapping providers.
- Server restriction changes must invalidate or suppress cached derivatives on the next successful sync.
- The client must not claim a restriction has been applied across all server systems until server confirmation is received.
- Push notifications and background task input must contain opaque references/status hints only, never precise coordinates, sensitive taxon details or private media URLs.
- Cache purge must cover local search indexes, thumbnails, previews, temporary files and derived media where those were stored.

### 8.4 Logout, account switching and device loss

- Pending data must be scoped to the originating account/device context.
- Account switching must not expose one user's drafts to another account.
- Logout behavior must be explicit: retain protected local drafts for re-authentication, offer user-controlled export, or securely remove them according to approved policy. Do not silently discard unsynced observations.
- A server-side account revocation cannot be instantly enforced on a permanently offline device. The residual offline risk must be explained; local data expiry and re-authentication policy need owner/security approval.
- Device loss response, remote session revocation and local cache expiration require a threat model and operational procedure.

## 9. Local storage, encryption and retention

### 9.1 Storage separation

Separate at least:
- unsynchronized user-created drafts and media;
- pending outbox commands and receipts;
- downloaded reference cache;
- authentication/session secrets;
- temporary upload/download files;
- logs/diagnostics.

Each category has its own retention, backup, eviction and privacy policy.

### 9.2 Protection requirements

- Store sensitive content only in app-private storage unless a user explicitly exports it.
- Encrypt sensitive local data at rest using a reviewed platform-compatible design. Keep key material in OS-protected key storage (Android Keystore / Apple Keychain or an appropriately reviewed platform abstraction); do not hardcode keys or store them in ordinary preferences.
- Assess encryption key lifecycle, device lock state, backup/restore, biometric changes, app reinstall, key invalidation and recovery.
- Exclude sensitive app databases/media from device/cloud backups unless a deliberate, documented backup design is approved.
- Avoid sensitive payloads in application logs, analytics, telemetry, notifications and crash diagnostics.
- Apply least privilege to local file access and use short-lived protected temporary files.
- Validate file type, size and content before parsing; treat media metadata as untrusted input.
- Use secure transport for all server synchronization and media upload.

This specification does not select a Flutter secure-storage package or assert that a package automatically provides end-to-end database encryption. Plugin maintenance, platform configuration, backup behavior, key access controls and threat-model fit require separate evaluation.

### 9.3 Storage limits and eviction

- Define visible limits for cached reference data, pending media and total local field storage.
- Pending user-created observations and outbox commands must not be silently evicted.
- Cache entries may be evicted under an explicit policy, with the user informed when useful.
- When space is low, stop accepting new large media or offer a safe user choice; never delete unsynchronized content without explicit confirmation.
- Show which items are only on this device and warn before app uninstall/device replacement.
- Provide a supported export/recovery path only after rights/privacy/security design is approved.

## 10. Reference-data cache and freshness

### 10.1 Cache scope

Potentially cacheable, subject to source rights and size:
- selected taxonomic reference records and names;
- selected profile summaries;
- approved diagnostic/reference content;
- limited geographic boundaries or offline map packages where licensing and storage allow;
- user-owned drafts and records already authorized for that user.

Do not cache full sensitive-location datasets, unrestricted raw source dumps or all media by default.

### 10.2 Version and freshness metadata

Each cache package/entry should retain where available:
- source/platform dataset identifier and version;
- retrieval/synchronization time;
- server revision/cursor;
- content checksum;
- schema/contract version;
- rights/usage scope or reference to the governing policy;
- expiry/freshness classification;
- whether the data is partial, stale or invalidated.

The UI must not present cached data as live/current if its freshness cannot be established. Cache expiry is not proof that the underlying scientific source has changed; it means the client must revalidate.

### 10.3 Pull and invalidation

- Use server-controlled cursors/revisions or a versioned snapshot mechanism.
- Support full refresh when a cursor expires or cache integrity fails.
- Apply tombstones/restriction notices before making refreshed content visible.
- If a server update removes a record or restricts a field, remove or suppress local derived copies as policy requires.
- A client that has not synchronized cannot guarantee current rights or sensitivity status; it must label cached information and avoid external disclosure.

## 11. Background and foreground execution

### 11.1 Scheduling strategy

Foreground sync is the dependable user-visible path:
- on explicit user request;
- after app launch/resume when authenticated and connectivity is available;
- after an observation is queued, while the app remains active;
- after user resolves a conflict.

Background synchronization is best effort and must be scheduled through platform-appropriate mechanisms. It is not a guarantee of prompt or periodic delivery.

### 11.2 Android

Official Android guidance recommends WorkManager for persistent work that should survive app exit/restart and device reboot. Work constraints can express network, charging, idle and storage conditions; retry/backoff is supported. Exact execution time remains subject to system scheduling and constraints.

**Proposal:** use a Flutter-compatible platform integration that delegates eligible durable background sync to Android WorkManager. Evaluate whether uploads require unmetered network, charging or foreground notification based on media size and user settings. Do not assume a Dart timer is durable background execution.

### 11.3 iOS/iPadOS

Apple's BackgroundTasks framework provides scheduled refresh and processing tasks. The system chooses when to run scheduled tasks; processing may be interrupted and must handle expiration. User-initiated long-running work has a distinct continuous-background-task path subject to platform support and policy.

**Proposal:** use an iOS-compatible Flutter integration around BGTaskScheduler for opportunistic refresh/processing, and the appropriate user-initiated path for a transfer that should continue after the user backgrounds the app where supported. Always checkpoint progress and resume safely. Do not promise exact execution time or uninterrupted background upload.

### 11.4 Cross-platform rule

- The synchronization protocol and state machine remain platform-neutral.
- Scheduling adapters are platform-specific implementation details.
- Foreground and manual sync must work even when background scheduling is unavailable.
- App process termination, force-stop, low battery, low storage, network metering, OS throttling and user revocation must be expected conditions.
- Do not use frequent polling or battery-intensive wakeups as a substitute for a durable outbox.

## 12. Synchronization state model

The following are proposed client command states. They are **not** Observation, Identification, Review, Rights or Publication lifecycle states.

| Client command state | Meaning |
|---|---|
| `local_draft` | Saved on device; not submitted |
| `queued` | Ready for synchronization |
| `waiting_dependency` | Waiting for a prerequisite command/media stage |
| `uploading` | Transfer in progress |
| `awaiting_server_result` | Request sent; durable outcome not yet known |
| `retry_wait` | Transient failure; same command/key will retry |
| `blocked_authentication` | Session requires re-authentication |
| `blocked_policy` | Rights, privacy, sensitivity or authorization requires review/action |
| `conflict` | Server revision differs; user or authorized workflow must resolve |
| `rejected_validation` | Server rejected the command; local draft remains recoverable |
| `server_received` | Server durably recorded the command and returned a receipt; domain processing may still be pending |
| `applied` | Server receipt confirms the defined platform domain operation committed and returns the canonical reference/revision |
| `cancelled_locally` | User cancelled eligible pending operation; no implication that server data was deleted |

A command's client sync state must not be copied into the Observation lifecycle or shown as scientific status.

### 12.1 User-facing wording

Use explicit language:
- “Saved on this device — not yet submitted.”
- “Waiting for connection.”
- “Uploading media.”
- “Submitted — awaiting server confirmation.”
- “Received by Botanica Indica — processing may continue.”
- “Applied — the platform operation has committed.”
- “Needs your attention — server version changed.”
- “Blocked — permission or policy review required.”
- “Could not submit — your local draft is still saved.”

Avoid ambiguous single labels such as “Synced” where media, observation and server acceptance may be at different stages.

## 13. Failure recovery and operational observability

Record non-sensitive operational metadata sufficient to reconstruct failures:
- opaque command and correlation IDs;
- app/API/schema version;
- command type/version;
- attempt count and timestamps;
- network class where privacy policy permits;
- error class and server correlation reference;
- media transfer progress/checksum result;
- base and returned server revision identifiers;
- final command state.

Never log exact coordinates, sensitive species/locality text, authentication tokens, raw media, private notes or full payloads by default.

Operations must support:
- safe resume after process death;
- detection of commands stuck in an intermediate state;
- reconciliation when a response was lost after server commit;
- retry without duplicate effects;
- manual retry or escalation;
- support diagnostics that the user can review/share knowingly;
- server-side idempotency and command audit lookup;
- queue age/blocked/failure metrics without exposing sensitive content.

A lost response is ambiguous: the server may have committed the command. The client must query/retry using the same idempotency key and reconcile the durable result rather than create a second command.

## 14. Proposed validation matrix

These cases are proposals. They have not been executed. Numeric thresholds, device matrix and release gates must be set after workload, threat-model and user research.

| ID | Scenario | Required result |
|---|---|---|
| OFF-001 | Create an observation with no connectivity | Draft persists locally; clearly marked not submitted; no taxon fabricated |
| OFF-002 | Force-close/restart app with queued draft | Draft and outbox recover without loss or duplicate command |
| OFF-003 | Reboot device with queued work | Queue remains recoverable; background execution may be deferred |
| OFF-004 | Connectivity repeatedly drops during submit | Same command key reused; eventual result reconciled; no duplicate domain effect |
| OFF-005 | Server commits but response is lost | Retry/query returns original durable result; no second observation |
| OFF-006 | Two commands have dependency ordering | Dependent command waits until prerequisite is accepted |
| OFF-007 | Independent observations queued together | Bounded concurrency; each result independently tracked |
| OFF-008 | User edits unsynchronized draft repeatedly | Local changes persist; one coherent pending submission or explicit version history |
| OFF-009 | Server revision changes before client update arrives | Conflict returned; no blind overwrite |
| OFF-010 | Two users edit separate fields on same observation | Merge only if approved field policy proves independence; otherwise explicit conflict |
| OFF-011 | Two users edit same material field | Both versions preserved; user/reviewer resolution required |
| OFF-012 | Two experts create conflicting determinations | Both assertions retained; no last-write-wins |
| OFF-013 | AI retry occurs during offline transition | New linked IdentificationRun only when online processing occurs; prior run remains unchanged |
| OFF-014 | Media upload interrupted mid-transfer | Resume/retry safely; checksum validated; incomplete media not publicly attached |
| OFF-015 | Same media is submitted twice after timeout | Idempotent attachment behavior; no duplicate unintended media relation |
| OFF-016 | Rights are revoked after media cached but before sync | Server blocks affected purpose; cache/derivative handling follows restriction policy |
| OFF-017 | Sensitive-location rule becomes more restrictive while device offline | Device cannot publish/share cached exact coordinates; restriction applied on next authorized sync |
| OFF-018 | User attempts export/share of stale protected location | Fail closed; no coordinate or reconstructable derivative disclosed |
| OFF-019 | Location permission denied or revoked | App supports manual/locality-only workflow; does not invent GPS |
| OFF-020 | Device storage becomes low with pending drafts | No silent deletion; user receives actionable storage warning |
| OFF-021 | User logs out with unsynchronized drafts | Explicit policy/choice; no cross-account leakage or silent loss |
| OFF-022 | Account authorization is revoked while device is offline | Local data remains protected; no claim that server revocation instantly erases offline copy |
| OFF-023 | Server rejects an observation for validation | Local draft retained; field-level reason and correction path shown |
| OFF-024 | API schema version is unsupported | Command blocked safely; no silent payload reinterpretation |
| OFF-025 | Server change cursor expires | Controlled full refresh/reconciliation; no silent omission |
| OFF-026 | Background task is delayed/terminated by OS | Foreground/manual sync resumes; state remains accurate |
| OFF-027 | App is force-stopped / background execution restricted | No false “automatic sync guaranteed” promise; pending work remains visible |
| OFF-028 | Cached reference data is stale | UI labels last update/version and stale status; no claim of current authoritative result |
| OFF-029 | Cache invalidation/tombstone arrives | Restricted/removed data and derivatives are suppressed/purged per policy |
| OFF-030 | Device backup/restore or app reinstall occurs | Approved backup/key policy enforced; no plaintext leakage; unsynced-data recovery limitations disclosed |
| OFF-031 | App switches between two accounts | Drafts, cache and command queue remain isolated by account |
| OFF-032 | Client clock is incorrect | Server ordering and authorization unaffected; capture time uncertainty remains explicit |
| OFF-033 | User requests withdrawal while offline | Request is pending; local display behavior is clear; no claim of server withdrawal until acknowledged |
| OFF-034 | Media has unknown rights | Relevant upload/use is blocked or quarantined according to policy; public/AI use not inferred |
| OFF-035 | Network is metered or battery low | Scheduler respects approved user/system constraints; user can choose supported manual behavior |
| OFF-036 | Diagnostic logs inspected | No sensitive coordinates, tokens, private notes or raw media leaked |

### 14.1 Test levels

- Unit: command state transitions, retry classification, dependency ordering, conflict policies and local migrations.
- Component: repository, outbox, cache, upload manager and scheduler adapters.
- Contract: API idempotency, version conflicts, command result, cursor, media staging and restriction responses.
- Integration: Flutter client, local database, API, identity, object storage, policy engine and server command receipt.
- Device/system: process death, reboot, background restrictions, low storage, key invalidation, account switch and network changes.
- Security/privacy: local storage, backup, logs, notifications, cache purge, sensitive-location leakage and authorization.
- Scientific: ensure offline capture does not fabricate identifications, occurrence states or expert/scientific validation.
- Operational: lost response, duplicate retry, stuck command, manual recovery, idempotency expiry and incident reconstruction.

## 15. Traceability

| Source obligation | Specification sections | Validation |
|---|---|---|
| Task 03 §17 — mobile offline workflows, sync/conflict, field use | §§4–13 | OFF-001–OFF-036 |
| Task 03 §20 — unreliable connectivity, selective cache, defined identification behavior, queued observations, status/failures, storage/privacy | §§4, 8–12 | OFF-001–OFF-008, OFF-017–OFF-030, OFF-033 |
| Task 03 §28 — reliability, retries, idempotency, durable queues, recovery, observability | §§5–7, 13 | OFF-002–OFF-007, OFF-014–OFF-015, OFF-025–OFF-027 |
| AC-004 — structured observation | §§4–5, 12 | OFF-001–OFF-003, OFF-023 |
| AC-009 — versioned API | §§5–7, 10, 13 | OFF-004–OFF-007, OFF-009, OFF-024–OFF-025 |
| AC-010 — privacy controls | §§8–9 | OFF-016–OFF-022, OFF-029–OFF-036 |
| WF-007 — observation without taxon | §§3–5 | OFF-001 |
| WF-008 — withdrawal and retention distinct | §§8, 12 | OFF-021, OFF-033 |
| WF-011 — sensitive coordinates restricted end-to-end | §8 | OFF-017–OFF-019, OFF-029, OFF-036 |
| WF-013 — publication suspension | §§8, 10 | OFF-016–OFF-018, OFF-029 |
| WF-015 — retry after transient failure | §§5–7, 13 | OFF-004–OFF-007, OFF-014–OFF-015 |
| WF-OD-10 — offline synchronization/concurrent transitions | Entire specification | OFF-001–OFF-036 |

## 15.1 ODR-01 offline and field-capture safeguard

ODR-01 authorizes only a controlled, profile-specific external export interpretation. It does not authorize the offline client to create or infer a non-detection result. A missing local or server Occurrence row remains unknown/not assessed. An offline draft, queued command, durable `server_received` receipt or applied observation command must not be presented as an explicit survey non-detection, an expert determination or a scientifically verified result.

If a future approved workflow captures an explicit survey result while offline, it must retain the actual actor, Survey/Event identity or unresolved reference, target scope and its a priori/post-facto origin, method/protocol, effort, time/place, applicable hierarchy, evidence and provenance. The server must revalidate the record and all applicable rights, authorization and scientific invariants on synchronization. No export-only interpretation is generated on-device. Export eligibility is evaluated later by the controlled server-side export process against a separately approved and pinned profile. Missing, ambiguous, contradictory or incomplete evidence suppresses the export interpretation. EVT-27–EVT-44 remain proposed and unexecuted.

This clarification does not resolve the internal Survey/Occurrence model, authorize a physical schema, or approve the offline feature boundary.

## 16. Open decisions and approval gates

| ID | Decision required | Why it cannot be silently assumed | Required review |
|---|---|---|---|
| OFF-OD-01 | Confirm mobile offline capability boundary and whether any web offline scope is required | Task 03 does not fully define client/platform parity | Product owner |
| OFF-OD-02 | Approve which reference data and media may be cached, with size/expiry rules | Rights, freshness, storage and source terms vary | Product, data and rights reviewers |
| OFF-OD-03 | Decide whether exact GPS may be stored locally offline and under what consent/purpose/security conditions | Sensitive species and personal-location risk | Privacy/security and conservation reviewers |
| OFF-OD-04 | Define local encryption/key lifecycle, backup exclusion and device-loss behavior | OS/platform configuration and threat model required | Security reviewer |
| OFF-OD-05 | Approve observation edit/conflict rules by field and actor | Scientific metadata cannot use generic last-write-wins | Product, scientific and data reviewers |
| OFF-OD-06 | Define API idempotency scope, key retention, command age and expiry response | Required for safe retries and server recovery | API/backend architect |
| OFF-OD-07 | Define server revision/ETag and conflict response contract | Must align with API and Task 05 logical model | API/backend architect |
| OFF-OD-08 | Define media upload staging, resumability, checksums and abandoned-upload retention | Storage provider and rights rules not selected | Media/backend/security reviewers |
| OFF-OD-09 | Define background execution and user-controlled metered-network behavior | Android/iOS scheduling differs and is not exact-time guaranteed | Mobile architect and UX |
| OFF-OD-10 | Define logout/account-switch retention and unsynced-data recovery policy | Privacy, user expectations and device risk | Product, privacy and legal reviewers |
| OFF-OD-11 | Define sensitive-location policy update propagation and maximum stale-policy exposure | Cannot guarantee instant restriction while device is offline | Conservation, privacy and security reviewers |
| OFF-OD-12 | Confirm cache invalidation/tombstone and cursor-expiry semantics | Must be defined in API/change-feed contracts | Backend/data architect |
| OFF-OD-13 | Decide if local-only records can be exported or shared and under what rights/privacy controls | Local data can still contain restricted content | Product, rights and privacy reviewers |
| OFF-OD-14 | Define supported device/OS matrix, local storage budget and performance targets | Must be based on target users/devices and field evidence | Product/mobile/QA |
| OFF-OD-15 | Decide whether on-device AI is pursued as a separate capability | Model rights, device performance, calibration and scientific evaluation | AI/ML and scientific governance |
| OFF-OD-16 | Reconcile local command envelopes with final Task 05 model and physical design | Task 05C/05D remain proposals with unresolved validation | Data architect and scientific reviewers |

No numeric target, reviewer identity, legal conclusion, package or vendor is invented here.

## 17. Implementation-readiness gates

Do not begin production implementation of offline synchronization until all of the following are satisfied:

1. Project owner approves the offline product boundary and user-facing promises.
2. API command, idempotency, revision, conflict and change-feed contracts are specified.
3. Task 05 logical model review confirms the necessary record identity, history, provenance and rights relationships; unresolved DR/LDM findings affecting the design are addressed.
4. Sensitive-location and local-data threat models are reviewed.
5. Asset/purpose rights and offline media handling are approved.
6. Logout, withdrawal, deletion, retention, backup and device-loss policies are defined.
7. Android/iOS target versions and background execution expectations are agreed.
8. Representative field-user research validates the workflow, wording and recovery experience.
9. Test fixtures and device-failure scenarios are prepared.
10. A qualified review covers scientific integrity, privacy, security, accessibility and rights.

A prototype may validate technical feasibility earlier, but it must use synthetic or appropriately authorized test data and must not be represented as production-ready.

### API contract alignment note — 21 November 2026

This specification is aligned with the proposed server-side contract in [STF-BI-API-SYNC-001](API-COMMAND-IDEMPOTENCY-AND-CONFLICT-RESOLUTION-CONTRACT-DESIGN.md). The client command ID and HTTP `Idempotency-Key` are distinct identities; a durable `server_received` receipt is not the same as an `applied` domain operation. HTTP `412` denotes a failed conditional request; `409` denotes a domain-state conflict under the API's documented semantics. These changes clarify the proposed design only and do not approve implementation or close OFF-OD-06/OFF-OD-07.

## 18. Risks and mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| Local drafts mistaken for submitted/verified records | Critical | Distinct client sync state and explicit UI wording |
| Duplicate records after lost responses/retries | Critical | Stable idempotency key, durable server receipt and reconciliation |
| Stale sensitive coordinates disclosed | Critical | No public exact-location cache; fail-closed client; server enforcement and purge |
| Expert/scientific assertions overwritten by conflict resolver | Critical | Append-only/versioned assertions; no generic merge |
| Unsynced observations silently lost | Critical | Durable outbox, no silent eviction, recovery and user-visible storage controls |
| Rights status changes while offline | Major | Server revalidation and purpose-specific blocking |
| Background scheduling unreliable | Major | Foreground/manual sync, truthful UX, platform-specific best effort |
| Device theft or shared device exposes private field records | Major | App-private storage, reviewed encryption/key lifecycle, logout and retention policy |
| Cache becomes scientifically stale | Major | Version/freshness metadata and clear stale indicators |
| Physical schema prematurely hard-coded | Major | Logical envelopes only until Task 05 gate |
| Excessive complexity in sync infrastructure | Major | Start with bounded outbox and versioned API; add complexity only from evidence |
| Platform-specific scheduler behavior differs | Major | Shared protocol, platform adapters and real-device validation |

## 19. Current official technical references checked

The following official sources were checked on 21 November 2026. They support platform capability statements; they do not establish that a specific Flutter plugin or product architecture has been selected.

1. **Flutter — Offline-first support**  
   https://docs.flutter.dev/app-architecture/design-patterns/offline-first  
   Flutter's guidance describes repositories as the single source of truth for client data access and explains local/remote data sources and alternative synchronization patterns. The guide explicitly leaves the exact write and sync strategy dependent on product requirements. This supports the repository/outbox approach, not a claim that Flutter automatically supplies durable synchronization.

2. **Android Developers — Task scheduling**  
   https://developer.android.com/develop/background-work/background-tasks/persistent  
   Android recommends WorkManager for persistent work that should survive app restarts and device reboots, with constraints and retry support. Execution remains system-scheduled.

3. **Android Developers — Define work requests**  
   https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started/define-work  
   Documents constraints and linear/exponential retry backoff. Retry timing is not an exact scheduling guarantee.

4. **Apple Developer — Background Tasks**  
   https://developer.apple.com/documentation/backgroundtasks  
   Documents scheduled background task mechanisms and the distinction between refresh, processing and user-initiated continued processing.

5. **Apple Developer — Using background tasks to update your app**  
   https://developer.apple.com/documentation/uikit/using-background-tasks-to-update-your-app  
   Explains BGAppRefreshTask and BGProcessingTask configuration and scheduling.

6. **Apple Developer — BGProcessingTask**  
   https://developer.apple.com/documentation/backgroundtasks/bgprocessingtask/  
   Processing tasks can be interrupted; expiration handling and cleanup are required.

7. **Android Developers — Android Keystore system**  
   https://developer.android.com/privacy-and-security/keystore  
   Describes cryptographic key storage and access controls, including hardware-backed options on supported devices. Device and hardware support varies.

8. **Apple Developer — Keychain Services**  
   https://developer.apple.com/documentation/security/keychain-services  
   Provides encrypted storage for small secrets and key material; it is not a general database encryption system.

9. **OWASP Mobile Application Security — MASVS Storage**  
   https://mas.owasp.org/MASVS/05-MASVS-STORAGE/  
   Covers secure local storage and prevention of sensitive-data leakage, including unintentional exposure through backups and logs.

10. **SQLite — Write-Ahead Logging**  
    https://www.sqlite.org/wal.html  
    Documents WAL concurrency advantages and limitations, including that WAL requires processes on the same host and does not work over a network filesystem. This is a local database consideration, not a proposal to use WAL without workload testing.

11. **Android Developers — Build an offline-first app**  
    https://developer.android.com/topic/architecture/data-layer/offline-first  
    Describes local/network source reconciliation, pull/push synchronization and conflict resolution as explicit offline-first design responsibilities.

### Research interpretation

- Flutter and Android guidance supports a repository boundary and local/remote source separation.
- Android and Apple documentation confirm that background scheduling is controlled by the operating system; exact execution cannot be promised.
- Android Keystore and Apple Keychain protect keys/secrets, but do not by themselves encrypt every application database or media file.
- OWASP MASVS supports testing both intended storage protection and unintended leakage.
- SQLite WAL is a possible local database mode, not a final selection; durability settings and device-specific behavior require evaluation.

## 20. Decisions intentionally not made

This specification does **not**:
- create or approve an ADR (Task 04's historical ADR-012 reference is not an accepted repository ADR);
- amend ADR-006, ADR-008, ADR-009 or any other accepted ADR;
- approve offline AI inference;
- approve a specific local database, Flutter plugin, encryption package or key-management library;
- select a media object store, queue, background scheduler package or API provider;
- define physical tables, SQL migrations, indexes or final entity cardinalities;
- define legal retention periods or declare compliance with Indian law;
- authorize collection of sensitive biodiversity or personal data;
- claim any tests were run or passed.

## 21. Recommended next steps

1. Project owner reviews OFF-OD-01 through OFF-OD-16 and approves the product boundary.
2. Backend/API architecture defines the command receipt, idempotency, revision, conflict and change-feed contracts.
3. Mobile architecture performs a bounded Flutter technical spike for local persistence, secure key handling, media staging and platform scheduler adapters using synthetic data.
4. Data architecture checks the proposed command envelopes against the reconciled Task 05C/05D logical model without starting physical design prematurely.
5. Privacy/security and rights reviewers approve local sensitive-data handling and policy propagation.
6. Update the Workflow-to-Requirements Crosswalk for WF-OD-10 and add the OFF validation IDs to the test traceability.
7. Only after these gates, authorize implementation planning.

**Specification status:** Proposed; owner and specialist review required.  
**End of document — STF-BI-ARCH-OFF-001 v0.1.**
