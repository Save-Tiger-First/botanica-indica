# Botanica Indica — API Command, Idempotency and Conflict-Resolution Contract Design

**Document ID:** STF-BI-API-SYNC-001  
**Version:** 0.1 — Proposed contract design  
**Status:** Proposed for project-owner, architecture, mobile, security and scientific-data review; not an accepted ADR, approved API baseline or implementation authorization  
**Prepared:** 21 November 2026  
**Repository:** `Save-Tiger-First/botanica-indica`  
**Working branch:** `docs/requirements-traceability-register`  
**Decision authority:** Save Tiger First project owner  
**Depends on:** ADR-003, ADR-004, ADR-006–ADR-010; Task 03; Task 04; STF-BI-ARCH-OFF-001; Task 05C/05D review gates

---

## 1. Executive recommendation

Define one stable, versioned HTTP contract for deferred field commands, durable server receipts, media staging and incremental change retrieval. The mobile client should submit **commands**, not attempt to replicate server database tables or directly synchronize mutable rows.

The proposed design has five governing properties:

1. **Durable acknowledgement:** a response distinguishes receipt of a command from successful domain processing and from scientific review or publication.
2. **At-least-once delivery with idempotent effects:** clients retry the same logical command safely; the platform does not claim exactly-once network delivery.
3. **Two layers of identity:** a persistent client command identity survives long offline periods; an HTTP idempotency key protects transport retries within a documented retention policy.
4. **Optimistic concurrency:** updates to existing shared resources carry a server revision precondition. Stale edits are returned for explicit resolution, never silently overwritten.
5. **Policy-aware synchronization:** identity, authorization, rights, privacy and sensitive-location policy are re-evaluated by the server when a command is received and when protected data is read or delivered.

This document proposes a contract boundary and illustrative payloads. It intentionally does **not** approve a physical database schema, final domain entity cardinalities, authentication provider, endpoint deployment topology, retry timings, retention periods, data-protection policy or legal interpretation.

## 2. Decision boundary and terminology

### 2.1 Status vocabulary

The terms below must not be collapsed into a single “synced” or “accepted” state.

| Term | Meaning |
|---|---|
| Locally saved | The client durably stored a draft on the device. No server receipt exists. |
| Queued | The client has a durable outbox command awaiting transmission or a prerequisite. |
| Received | The server durably recorded the command envelope/receipt. |
| Processing | The server is validating or applying the command. |
| Applied | The defined domain operation committed successfully. |
| Rejected | The server refused the command; the response includes a stable reason code. |
| Conflict | The command cannot safely apply against current server state or domain rules. |
| Blocked | A policy, authorization, rights or prerequisite condition prevents processing pending an explicit action. |
| Expert-reviewed / scientifically validated | A separate scientific workflow outcome, governed by reviewer authority and evidence. |
| Published / externally released | A separate controlled disclosure decision. |

**A command receipt is not scientific validation.** “Applied” means the defined platform operation was committed; it does not mean an observation is taxonomically correct, an identification is confirmed, media rights are cleared for every purpose, or a record is publicly publishable.

### 2.2 Contract terms

- **Command:** an immutable client request to perform one named domain action.
- **Client command ID:** stable opaque identifier assigned once to a logical user action and retained across offline retries, app restarts and upload recovery.
- **Idempotency key:** HTTP request key used by the server to recognize transport-level retries.
- **Command receipt:** durable server-side record of the command's processing state and outcome.
- **Aggregate revision:** opaque server version token for a resource or consistency boundary.
- **Change cursor:** opaque server-issued continuation token for incremental synchronization.
- **Media upload session:** server-authorized staging process for transferring bytes before a domain record references the verified asset.

### 2.3 Scope

In scope:
- Observation creation and eligible observation edits.
- Media upload staging and attachment.
- Command receipt, status polling and reconciliation.
- Version preconditions and conflict responses.
- Incremental change feed and cursor expiry.
- Authorization, rights and sensitivity revalidation at API boundaries.
- Contract examples, error semantics and validation scenarios.

Out of scope:
- Final taxonomy, occurrence, organism, identification or evidence schema.
- Full identity-provider / OAuth deployment architecture.
- Final media storage provider and signed URL implementation.
- Offline AI inference model or on-device taxonomy package.
- Public API publication, institutional data exchange and Darwin Core/TCS mapping.
- Final account deletion, retention, consent, community-knowledge or legal policy.

## 3. Source alignment and governing constraints

### 3.1 Repository sources inspected

| Source | Version / branch | Relevant constraint |
|---|---|---|
| Permanent AI Operating Prompt | v1.0, `docs/repository-audit-and-ai-operating-standard` | No new branches; preserve ADRs; no physical design while scientific blockers remain. |
| Task 03 PRD | Current preserved baseline, `docs/canonical-task-03-04-baselines` | Offline workflows, safe queued observation synchronization, visible sync status/failures, versioned APIs, media upload/reference and privacy controls. |
| Task 04 architecture | Current preserved baseline, `docs/canonical-task-03-04-baselines` | API-first contracts, REST/HTTP for ordinary resource operations, asynchronous job APIs for long-running work, asynchronous processing and Flutter governing ADR correction. |
| ADR-003 | Accepted | API-first platform, contract-first where practical, OpenAPI, versioning, authorization, predictable errors, provenance and security. |
| ADR-004 | Accepted | Provenance, source and transformation context, rights and validation history persist through the data lifecycle. |
| ADR-006 / ADR-007 | Accepted | Identification outputs, evidence and expert determinations remain distinct, attributable and historically preserved. |
| ADR-008 / ADR-009 | Accepted | Sensitive geographic information and observation/contribution lifecycles require explicit protection and provenance. |
| ADR-010 | Accepted | External source integrations remain source-aware and provenance-preserving. |
| STF-BI-ARCH-OFF-001 | v0.1 Proposed | Durable outbox, idempotent processing, version-aware reconciliation, media staging, cache invalidation and policy-aware behavior. |
| Task 05C / 05D | Proposed; review gates open | Logical scientific model is not approved for physical schema implementation. |

### 3.2 Compatibility findings

1. The contract is consistent with accepted ADR-003's API-first and contract-first principles.
2. It extends, but does not alter, Task 03 requirements for queued observations, media endpoints, sync status and privacy.
3. It makes the offline specification's distinction between client command state and domain lifecycle explicit.
4. It preserves ADR-004 provenance and the immutability/history requirements in ADR-006/007.
5. It does not decide unresolved Task 05C/05D relationships or introduce SQL tables.
6. Task 04's early React Native candidate is not adopted. The preserved architecture audit records Flutter/Dart as the governing accepted ADR-001 direction. This contract is client-framework-neutral and does not change that decision.

### 3.3 Important scientific constraint

The API must not use one generic mutable `species`, `taxon`, `verified` or `status` field as a substitute for the scientific concepts defined in the project. Observation, Event, Organism, Occurrence, Identification, IdentificationRun, evidence, TaxonName, TaxonConcept and expert determination remain distinct according to the eventual approved model. API representations must be derived from that model only after Task 05 review.

## 4. Contract-wide conventions

### 4.1 API version and representation

**Proposal:** version the public HTTP contract in the path, initially `/api/v1`, subject to the final API inventory and deployment convention. Do not version individual resources independently without a documented compatibility reason.

- JSON request/response bodies use UTF-8 and `application/json`.
- Errors use `application/problem+json` following RFC 9457.
- OpenAPI is the machine-readable contract; examples and narrative documentation are maintained alongside it.
- Timestamps use RFC 3339 date-time with an explicit offset or UTC `Z`; retain original observation time-zone/context where scientifically relevant.
- Opaque identifiers and revision tokens are not to be interpreted or generated by clients.
- Unknown response fields should be tolerated by clients where practical; clients must not silently discard unknown command semantics.
- Numeric units, coordinate reference systems, precision and temporal meaning must be explicit in the relevant resource contract.

**Versioning recommendation:** use the latest stable OpenAPI 3.2 line at contract publication if the selected toolchain supports it. The official specification currently identifies 3.2.1 (10 September 2026). Pin the exact version in the contract repository and validate it in CI; do not assume all generators fully support every feature.

### 4.2 Common request headers

| Header | Proposed use |
|---|---|
| `Authorization: Bearer …` | Authenticated access token where required. Never place credentials in URLs or command bodies. |
| `Accept` | Response media type negotiation. |
| `Content-Type` | Request representation media type. |
| `Accept-Language` | Optional human-readable error/message localization; stable machine codes remain language-neutral. |
| `X-Request-ID` | Optional client correlation ID, validated and treated as untrusted input; server also issues its own trace/correlation ID. |
| `Idempotency-Key` | Required on command-creating POST operations designated idempotent by this contract. Same key for retries of the same HTTP operation only. |
| `If-Match` | Required for edits to an existing versioned resource where lost-update prevention is required. Uses a strong ETag obtained from the server. |
| `If-None-Match` | Optional conditional read/cache validation where appropriate. |

Do not put sensitive coordinates, private media URLs, personal data or full command payloads in headers used for tracing.

### 4.3 Response headers

- `ETag`: strong opaque representation revision for versioned resources.
- `Location`: canonical URL of a newly created operation/receipt or upload session.
- `Retry-After`: server-directed retry delay for throttling or a documented transient condition.
- `Cache-Control`: explicit policy. Sensitive, account-specific or authorization-dependent representations should default to `private, no-store` unless a reviewed cache design proves otherwise.
- `X-Request-ID` (or the chosen standard trace header): server-generated correlation identifier, not an authorization token.

### 4.4 Authentication and authorization

Authentication proves an identity; authorization evaluates whether that identity may perform this action on this resource for this purpose.

- Apply authorization server-side on every command and protected read.
- Check role, capability, ownership, expert authority scope, moderation scope and relevant policy conditions as applicable.
- Re-check permissions when processing queued commands. A role held when the device went offline does not guarantee that it remains valid later.
- Use short-lived access tokens and a reviewed mobile authorization-code flow with PKCE if OAuth 2.0 / OpenID Connect is selected. Follow current OAuth security BCP; do not use the Resource Owner Password Credentials or implicit grant.
- Do not persist bearer tokens in the outbox, logs, crash reports, analytics or command payload.
- Refresh credentials through the approved secure client mechanism. If authentication cannot be renewed, pause synchronization without changing command identity.
- Revocation, account suspension, logout and account switching must have defined local-draft and pending-command behavior before release.
- An idempotency receipt must never be disclosed to a different principal merely because a key is known.

No identity provider or complete authorization policy is selected by this document.

## 5. Proposed API surface

These paths are **illustrative proposals**, not deployed endpoints or a final route inventory.

| Operation | Method and proposed path | Purpose |
|---|---|---|
| Submit command | `POST /api/v1/sync/commands` | Submit one immutable command envelope. |
| Get receipt | `GET /api/v1/sync/commands/{receiptId}` | Retrieve processing state and outcome for an authorized caller. |
| Reconcile client command | `GET /api/v1/sync/commands/by-client-id/{clientCommandId}` | Recover outcome after a lost response or long interruption. |
| Read changes | `GET /api/v1/sync/changes?cursor=…` | Obtain authorized incremental changes. |
| Start media upload | `POST /api/v1/media/upload-sessions` | Request a bounded, authorized staging session. |
| Upload media bytes | `PUT` to the returned upload target | Transfer bytes using the server-authorized mechanism. |
| Complete media upload | `POST /api/v1/media/upload-sessions/{uploadSessionId}/complete` | Verify staged bytes and finalize the asset as attachable. |
| Read observation | `GET /api/v1/observations/{observationId}` | Retrieve an authorized observation representation and ETag. |
| Edit observation | `PATCH /api/v1/observations/{observationId}` | Apply an eligible version-checked edit. |
| Request withdrawal/restriction | Command type via sync endpoint | Submit a request for server policy evaluation; not a client-side hard delete. |

Do not expose a generic endpoint that lets clients write arbitrary database entities or bypass domain workflows. Do not create a universal “sync all local tables” API.

**Important contract-coherence gate:** the proposed generic command endpoint and the illustrative direct `PATCH /observations/{id}` route must not become two independent mutation pipelines. Before OpenAPI freeze, choose one of two patterns: (a) route all offline-queueable writes through the command endpoint; or (b) allow synchronous resource routes as façades that invoke the same domain command processor, idempotency, authorization, revision, audit and receipt semantics. No write route may bypass those controls. This choice remains API-OD-01/API-OD-05 and is not decided here.

## 6. Command envelope

### 6.1 Proposed request

```json
{
  "clientCommandId": "0194f5b2-opaque-example",
  "commandType": "observation.create",
  "commandSchemaVersion": "1",
  "client": {
    "installationId": "opaque-installation-reference",
    "appVersion": "0.1.0",
    "platform": "android"
  },
  "createdAt": "2026-11-21T09:30:00Z",
  "aggregate": {
    "type": "observation",
    "clientReference": "local-observation-7f3a"
  },
  "baseRevision": null,
  "dependsOn": [],
  "payload": {
    "observationDraft": {
      "observedAt": "2026-11-20T16:45:00+05:30",
      "location": {
        "coordinateReferenceSystem": "EPSG:4326",
        "latitude": 12.9,
        "longitude": 77.6,
        "precisionMetres": null,
        "captureMethod": "device_gnss"
      },
      "mediaAssetReferences": ["local-media-2a1"]
    }
  },
  "clientContext": {
    "locale": "en-IN",
    "timeZone": "Asia/Kolkata"
  }
}
```

The values above are illustrative only. The sample coordinates are not a field site or a claim about a real observation. The final payload must use the approved Task 05 model and approved location/privacy policy. The client must not infer or fabricate coordinate precision, CRS, observation time or taxonomic identification.

### 6.2 Envelope rules

- `clientCommandId` is generated once, persisted with the outbox entry and never reused for a different logical command.
- `commandType` is from a server-published allow-list. Unknown command types are rejected, not guessed.
- `commandSchemaVersion` identifies the command payload contract independently of the API major version.
- `createdAt` is client-reported context, not a trusted server timestamp. Server receipt and processing timestamps are recorded separately.
- `client.installationId` is an opaque installation reference, not a secret or proof of identity.
- `aggregate.clientReference` supports local-to-server identity reconciliation; it is not a canonical server identifier.
- `baseRevision` is required for updates to an existing server resource and absent for a genuinely new local draft.
- `dependsOn` references earlier client commands or completed upload sessions. Dependencies must be validated server-side.
- `payload` is command-type-specific and schema-validated. It must not contain access tokens, passwords, private signing keys or unbounded binary data.
- Client-supplied actor identity is never authoritative; actor identity comes from authenticated server context.
- Server receipt, authorization decision, policy version, canonical IDs and server revisions are generated by the server.
- The command must be immutable after first submission. A changed user intent is a new command with a new client command ID and idempotency key, with a causal link where required.

### 6.3 Initial command types proposed

| Command type | Intended effect | Guardrail |
|---|---|---|
| `observation.create` | Create a user observation using approved fields. | Does not assert a confirmed taxon or overwrite authoritative taxonomy. |
| `observation.update` | Apply eligible corrections to an existing observation. | Requires base revision and explicit change semantics; conflict if stale. |
| `observation.withdrawal.request` | Ask the server to evaluate withdrawal/restriction. | Does not imply deletion or override retention/legal/audit policy. |
| `media.attach` | Attach a verified staged asset to an authorized record. | Asset must be uploaded, integrity-checked and rights/purpose eligible. |
| `identification.request` | Request a server-side identification run, if enabled. | Creates a new attributable run; never overwrites prior candidates or expert determinations. |

Expert determinations, publication approvals, rights grants, sensitive-location overrides and administrative actions should **not** be enabled as ordinary offline field commands. Any future offline privileged workflow requires separate authority, conflict, audit and policy design.

## 7. Idempotency and duplicate-command prevention

### 7.1 Two distinct identifiers

A critical design distinction:

**Client command ID** protects logical identity over the entire offline lifecycle. It must remain stable through long disconnections, app restarts, retries and lost responses. Server-side reconciliation must be possible by authenticated principal + installation scope + client command ID (or a carefully designed equivalent).

**Idempotency-Key** protects repeated HTTP submissions of one operation. It is an HTTP request-level key governed by a documented server scope, fingerprint and retention policy. It is not sufficient by itself for an observation that may remain offline longer than the key-retention window.

The same random opaque value may be used for both fields in an initial client implementation only if the server still enforces and documents their separate semantics. Do not make the long-lived client-command identity expire merely because an HTTP idempotency cache entry expires.

### 7.2 Required behavior

| Situation | Proposed server behavior |
|---|---|
| First request with valid key and command ID | Authenticate, authorize, validate, durably register the command and return a receipt. |
| Same key + same fingerprint after completion | Return the prior operation result/receipt; do not apply the domain effect again. |
| Same key + same fingerprint while processing | Return a documented in-progress response or conflict with a safe receipt/status reference; never start a second effect. |
| Same key + different fingerprint | Reject with `422 Unprocessable Content`; do not execute either a modified replay or a second effect. |
| Same client command ID + same logical command after HTTP key expiry | Return/reconcile the existing command receipt; do not create a duplicate. |
| Same client command ID + materially different command | Reject and flag a client integrity/logic error; do not reinterpret the prior command. |
| Key/command ID belongs to another principal or installation scope | Do not disclose the other receipt. Apply a non-enumerating authorization/not-found policy. |
| Server cannot establish whether a prior effect committed | Reconcile the durable command record before retrying the domain mutation. Never blindly execute again. |

### 7.3 Scope, fingerprint and retention

The server must define:
- key syntax and maximum length;
- uniqueness scope (at minimum authenticated principal, operation family and client/tenant context as appropriate);
- canonical request fingerprint algorithm and which fields are included;
- treatment of semantically equivalent JSON encodings;
- behavior for concurrent duplicates;
- completed and failed result replay policy;
- retention/expiry policy and client-visible expiry behavior;
- long-lived client-command tombstone/reconciliation policy;
- privacy and access control for stored request metadata.

Fingerprint inputs should include the command type/version and semantically relevant request body, not volatile tracing headers. Do not store raw sensitive payloads in an idempotency cache merely to compare retries. A cryptographic digest plus necessary receipt metadata is preferable, subject to security review.

A client must never generate a new key merely because a request timed out. A new key is for a new logical request, not a retry.

### 7.4 Processing and atomicity

For synchronous domain mutations, command receipt and domain effect must commit atomically where possible. For asynchronous processing, durably record the receipt and enqueue work through a recoverable transactional-outbox or equivalent pattern. A process crash between recording receipt and dispatch must not strand a command invisibly or execute it twice.

Do not claim “exactly once” delivery. The design objective is at-least-once request delivery with deduplicated, recoverable server-side effects.

### 7.5 Draft standard status

The IETF Idempotency-Key header document is an Internet-Draft, not a published RFC. Its current version and syntax may change. Use it as work-in-progress guidance only; pin and re-check the version before API contract freeze. The server's own published contract remains authoritative for Botanica Indica's actual scope, fingerprint and expiry behavior.

## 8. Command receipt and acknowledgement contract

### 8.1 Proposed receipt representation

```json
{
  "receiptId": "opaque-server-receipt-id",
  "clientCommandId": "0194f5b2-opaque-example",
  "commandType": "observation.create",
  "commandSchemaVersion": "1",
  "state": "received",
  "receivedAt": "2026-11-21T09:31:12Z",
  "updatedAt": "2026-11-21T09:31:12Z",
  "result": null,
  "problem": null,
  "links": {
    "self": "/api/v1/sync/commands/opaque-server-receipt-id"
  }
}
```

### 8.2 State machine

```text
received
   |
   v
processing ----------------------+
   |                             |
   +--> applied                  |
   +--> rejected                 |
   +--> conflict                 |
   +--> blocked                  |
   +--> retryable_failure -------+
```

A transient infrastructure failure may leave a receipt in a retryable state. The server owns retry orchestration if processing has been accepted. A client retry of the same command must not create a second logical operation.

Terminal states and whether a blocked command can resume must be documented. A policy decision changing from blocked to allowed does not silently authorize replay; the server re-evaluates the command under current policy and records the new decision.

### 8.3 Submission response

**Proposal:** `202 Accepted` with a `Location` pointing to the durable command receipt when the command has been durably recorded but processing is asynchronous. A `202` means accepted for processing, not that the observation was committed, reviewed or published.

For a command processed synchronously, use the appropriate successful response and return the final receipt. The exact status selection must be consistent per command type and pinned in OpenAPI.

### 8.4 Receipt result

An applied result may include:
- canonical server resource identifier(s);
- canonical revision/ETag;
- server processing time;
- stable result code;
- safe links to authorized resource representations;
- media references after integrity and policy checks.

A rejected/conflicted/blocked result includes a stable machine-readable reason code and safe, actionable detail. Never include restricted coordinates, private media URLs, raw exception traces or other users' data.

## 9. Concurrency and conflict resolution

### 9.1 Revision model

Every mutable shared resource representation that supports conditional updates should expose a strong opaque `ETag`. The client sends that exact value in `If-Match` when editing.

- Missing required precondition: reject according to the documented policy (recommended `428 Precondition Required`).
- Stale `If-Match`: return `412 Precondition Failed` and current safe revision metadata; do not apply the edit.
- Domain-level conflict not expressible as a simple revision mismatch: return `409 Conflict`.
- A successful update returns a new ETag.
- Clients must not manufacture ETags, compare their internal contents or use timestamps as a substitute for revision tokens.

RFC 9110 defines conditional request semantics and specifically describes `If-Match` as a way to prevent lost updates. A server must use strong comparison for `If-Match`.

### 9.2 Field/category conflict rules

| Data category | Proposed rule |
|---|---|
| New observation draft | Create as a new resource after validation; use stable client command identity. |
| Observation descriptive correction | Apply only against the submitted base revision; conflicting edits require user resolution or an explicit policy. |
| Observation time/location correction | Treat as scientifically material; preserve before/after, actor, reason and provenance; no silent merge. |
| Media attachment | Additive only when safe; retain asset identity, checksum, role/order and rights context. Removal/replacement conflicts require explicit resolution. |
| Identification run/candidates | Immutable/versioned result; a new run creates a new result set. |
| Expert determination/review | Append a new attributable assertion or decision under authority rules; never last-write-wins. |
| Taxon name/concept/treatment assertion | Preserve source/treatment scope and history; never merge competing assertions automatically. |
| Rights or consent state | Apply current authoritative policy; cached client permission cannot override revocation or scope. |
| Sensitive-location classification | Apply current server policy on read, write, export and publication; do not resolve by choosing the least restrictive value. |
| Withdrawal/deletion/restriction | Create a request and server decision workflow; do not equate a local delete with completed erasure. |

### 9.3 Explicit resolution flow

1. Client receives `412` or `409` with a stable conflict type and safe current revision.
2. Client pauses dependent commands for that aggregate.
3. Client fetches the current authorized server representation.
4. Client compares its local base, local intended changes and current server state.
5. User or an explicitly approved deterministic field-level policy resolves the conflict.
6. A resolution creates a **new** command with a new client command ID and current base revision; it references the superseded command/receipt for audit.
7. Server revalidates authorization, rights, scientific constraints and current policy.
8. Client retains the full local/server resolution history according to retention policy.

Do not present a blind “overwrite server” button for scientific records.

## 10. Media staging and attachment

### 10.1 Proposed lifecycle

```text
local media draft
   -> upload session requested
   -> authorized upload target issued
   -> bytes transferred
   -> checksum / size / content verification
   -> media asset staged
   -> rights and metadata assessment
   -> authorized attachment command
   -> server confirms attachment
```

### 10.2 Contract requirements

The upload-session request should describe only necessary metadata:
- client media reference;
- declared media category and format;
- byte length;
- cryptographic content checksum and algorithm;
- capture time/context where permitted;
- rights/consent declaration references where applicable;
- intended use/purpose context;
- relationship to a pending command, if known.

The server returns:
- opaque upload-session ID;
- upload target and required headers;
- expiry time;
- allowed content types and size limits;
- required checksum behavior;
- completion URL;
- safe upload status.

The upload target may be a short-lived signed URL or another provider-neutral mechanism. Treat it as a bearer capability: do not log it, place it in analytics, expose it in notifications or persist it beyond its necessary lifetime. Never assume possession of a signed URL grants rights to use the content for any purpose beyond the upload operation.

On completion the server verifies the uploaded bytes, content type, size and checksum. Only then may the staged asset be referenced by a domain command. An upload success is not an observation acceptance or a rights clearance.

### 10.3 Rights and media metadata

- Rights are evaluated per asset and purpose: storage, display, derivative creation, redistribution, export, AI inference, training, fine-tuning and embeddings are separate purposes.
- Unknown or ambiguous rights must not be treated as permission.
- Original and derivative media must remain distinguishable with provenance and rights links.
- EXIF/GPS and other embedded metadata must be handled under the approved privacy and sensitive-location policy.
- Do not expose raw media object-store keys or unrestricted storage URLs.
- Malware/content scanning, format validation and decompression/resource-exhaustion defenses are required before processing untrusted media.
- A restriction/revocation must propagate to derivatives, thumbnails, caches, search and exports under the approved policy.

## 11. Incremental change feed and reconciliation

### 11.1 Proposed change endpoint

`GET /api/v1/sync/changes?cursor={opaqueCursor}`

The response should contain:
- opaque next cursor;
- server snapshot/change sequence context;
- changes visible to the authenticated principal at the time of evaluation;
- tombstone/restriction markers where disclosure is authorized;
- resource type, opaque identifier, change type and current revision;
- a policy/scope version or invalidation signal where appropriate.

Do not expose an unrestricted global event log. The change feed is a **filtered read model**, not a replacement for domain authorization.

### 11.2 Cursor requirements

- Cursor is opaque, integrity-protected and bound to the relevant user/tenant/device scope and query semantics.
- A cursor is not an authorization credential. Every returned record is independently authorized.
- Cursor ordering must be stable and support pagination without skipped changes under the documented consistency model.
- A cursor must not encode raw personal data or sensitive coordinates.
- When cursor expires or becomes invalid, return a documented problem (proposed `410 Gone` for expired continuation state) and require a controlled snapshot/full reconciliation.
- Client stores the next cursor only after it has durably applied the corresponding page.
- If a page is replayed, applying it must be safe and idempotent.
- Permission or sensitivity changes may require invalidation/purge signals even when a record's ordinary content has not changed.
- A client must not infer deletion from absence in a filtered page.

### 11.3 Snapshot recovery

The server should provide a bounded snapshot/bootstrap mechanism for a new device, an expired cursor or local cache corruption. The snapshot must be scoped by authorization and approved cache policy. It must not include unrestricted raw data, sensitive coordinates or media by default.

The exact snapshot consistency strategy (snapshot token, high-water mark, change sequence and pagination) remains an API design decision before implementation.

## 12. Error contract

Use RFC 9457 Problem Details for machine-readable API errors, with Botanica Indica extension members defined in OpenAPI.

### 12.1 Proposed problem object

```json
{
  "type": "https://api.example.invalid/problems/stale-revision",
  "title": "The observation has changed",
  "status": 412,
  "detail": "Refresh the observation and resolve the pending edit.",
  "instance": "/api/v1/observations/opaque-id",
  "code": "SYNC_STALE_REVISION",
  "requestId": "opaque-server-correlation-id",
  "retryable": false,
  "currentRevision": "\"opaque-strong-etag\"",
  "fieldErrors": []
}
```

The `.invalid` domain above is deliberately a placeholder and must be replaced only when a real project-controlled documentation domain exists. Problem `type` URIs must be stable and resolvable before public API release.

### 12.2 Proposed status mapping

| HTTP status | Meaning in this contract | Client behavior |
|---|---|---|
| 400 | Malformed request/header/envelope | Do not retry unchanged. |
| 401 | Missing/expired/invalid authentication | Pause; re-authenticate securely; preserve command ID and key. |
| 403 | Authenticated but not authorized | Block; no blind retry. |
| 404 | Resource/receipt not visible or does not exist | Follow non-enumerating policy; do not infer global absence. |
| 409 | Domain conflict or same idempotency key still processing | Reconcile receipt or enter conflict flow; do not create a new logical command. |
| 410 | Cursor/upload session/continuation expired where documented | Re-bootstrap or obtain a new upload session; preserve logical command identity. |
| 412 | `If-Match` precondition failed | Fetch current version and resolve. |
| 413 | Payload too large | Reduce or stage appropriately; never silently discard local media. |
| 415 | Unsupported media/request content type | Correct client encoding. |
| 422 | Semantically invalid payload or idempotency key reused with different fingerprint | Correct by creating a new command if user intent changes; preserve original failure. |
| 428 | Required conditional precondition missing | Fetch revision and resubmit a new appropriately based command. |
| 429 | Rate limited | Honor `Retry-After`; bounded retry with same key. |
| 5xx | Server-side/transient failure where indicated | Retry same command/key according to policy; reconcile before assuming no effect. |

Status codes must retain their standard HTTP meanings. Do not overload `200` for every outcome or encode failure only in a success-shaped body.

### 12.3 Stable machine codes

Illustrative codes:
- `COMMAND_SCHEMA_UNSUPPORTED`
- `COMMAND_DEPENDENCY_PENDING`
- `COMMAND_DEPENDENCY_FAILED`
- `COMMAND_ID_REUSE_MISMATCH`
- `IDEMPOTENCY_KEY_REUSE_MISMATCH`
- `IDEMPOTENCY_REQUEST_IN_PROGRESS`
- `SYNC_STALE_REVISION`
- `SYNC_DOMAIN_CONFLICT`
- `AUTHENTICATION_REQUIRED`
- `AUTHORIZATION_DENIED`
- `RIGHTS_PURPOSE_NOT_PERMITTED`
- `SENSITIVE_LOCATION_RESTRICTED`
- `MEDIA_CHECKSUM_MISMATCH`
- `MEDIA_UPLOAD_EXPIRED`
- `SYNC_CURSOR_EXPIRED`
- `POLICY_REVALIDATION_REQUIRED`

Codes are stable identifiers, not a substitute for HTTP semantics. Human-readable `detail` may be localized and may change without breaking clients.

## 13. Retry, ordering and back-pressure

- Retry only errors documented as transient.
- Honor `Retry-After` when present.
- Use bounded exponential backoff with jitter, with user-visible manual retry.
- Keep the same client command ID and Idempotency-Key for a retry of the same request.
- Do not retry authorization denial, unsupported schema, rights restriction, invalid payload or unresolved conflict automatically.
- Preserve dependency order where the domain semantics require it.
- A failed prerequisite blocks dependent commands and exposes the reason.
- Limit concurrency and payload sizes according to server-published limits; do not invent final numerical limits here.
- Media byte transfer and command submission are separate recoverable operations.
- On app restart, reconstruct queue state from durable local storage, not volatile in-memory tasks.
- Background sync is opportunistic; foreground/manual sync remains available.

## 14. Security, privacy and sensitive biodiversity controls

### 14.1 Threat-oriented requirements

- Enforce TLS and validate certificates; do not disable verification to make field connectivity work.
- Authenticate and authorize every command, receipt read, media operation and change-feed request.
- Bind receipts and idempotency lookup to principal/client scope to prevent cross-account data leakage.
- Validate all IDs, enum values, lengths, schema versions, timestamps, media metadata and checksums.
- Apply payload size/rate limits and abuse controls.
- Do not log command bodies, exact coordinates, private media URLs, bearer tokens or sensitive taxon details.
- Use opaque correlation identifiers; redact or generalize operational telemetry.
- Do not place sensitive information in push notifications or background-task payloads.
- Re-evaluate location disclosure and media rights at read/export/publication time; cache state is not authority.
- Use no-store or appropriately private cache directives for sensitive/authorization-dependent resources.
- Ensure cursor, ETag, receipt and upload-session identifiers are not treated as standalone authorization.
- Maintain audit evidence for privileged decisions without turning the audit log into an uncontrolled copy of sensitive payloads.
- Design backup, restore, revocation and cache invalidation so that a restored or long-offline device does not re-expose restricted information.

### 14.2 Sensitive coordinates

The API should support server-side disclosure transformations (e.g. generalized, withheld or exact) based on a future approved policy. It must not assume a single precision tier for all taxa, locations, users or purposes.

A client-supplied precision value is descriptive metadata, not permission to disclose. Public APIs, exports, search indexes, media derivatives and change feeds must apply the same approved disclosure decision. Do not send exact coordinates to devices unless the user's role, purpose, retention and local-security requirements permit it.

### 14.3 Offline revocation limitation

A device that is fully offline cannot learn instantly that access has been revoked or that a species location has become newly restricted. The architecture must therefore minimize sensitive data cached locally, limit its permitted offline use, expire or invalidate it when reconnecting, and avoid representing offline cached data as current authorization. This residual risk must be explicitly accepted by the project owner and privacy/conservation specialists before release.

## 15. Observability and audit

Capture operational metadata sufficient to diagnose synchronization without duplicating sensitive scientific or personal content.

Recommended metadata:
- server request/correlation ID;
- receipt ID and client command ID (appropriately protected);
- authenticated actor reference and client installation reference;
- command type/schema version;
- receipt state transitions and server timestamps;
- retry/attempt counts and safe error code;
- aggregate identifier and revision reference, subject to sensitivity controls;
- policy/authorization decision reference;
- processing duration and outcome.

Do not use raw payloads as logs. Audit events and operational logs have different purposes, access controls and retention requirements. Their retention periods and legal basis remain open.

## 16. Compatibility and command evolution

- API major version and command schema version are distinct.
- A client declares the command schema version it can produce.
- The server publishes supported versions and a retirement/deprecation policy.
- Unknown command type or unsupported schema version is rejected with a stable error; never silently reinterpret it.
- Additive optional response fields may be compatible if clients are tolerant.
- Removing/renaming fields, changing semantics, tightening required fields, changing authorization meaning or changing state transitions may be breaking.
- A server may support a documented migration adapter for old queued commands, but migration must be deterministic, auditable and rights/science-safe.
- Never silently upgrade a scientific assertion or taxonomic concept embedded in an old command to a newer meaning.
- Retain enough compatibility to process commands created by supported offline clients, or provide a safe user-visible export/recovery path when support ends.
- Contract tests must include old-client fixtures and unsupported-version behavior.

## 17. Acceptance and contract validation scenarios

These are proposed scenarios, not executed tests.

| ID | Scenario | Expected result |
|---|---|---|
| API-SYNC-001 | First valid observation command | One durable receipt; command follows defined processing path. |
| API-SYNC-002 | Same key and identical request replayed after success | Same logical result; no duplicate observation. |
| API-SYNC-003 | Same key replayed while first request is processing | No parallel domain effect; documented in-progress response. |
| API-SYNC-004 | Same key reused with altered payload | 422; no second effect. |
| API-SYNC-005 | Same clientCommandId retried after idempotency cache expiry | Existing receipt reconciled; no duplicate. |
| API-SYNC-006 | Same clientCommandId reused for different intent | Rejected; original receipt unchanged. |
| API-SYNC-007 | Server commits but response is lost | Client retrieves existing receipt by client command ID. |
| API-SYNC-008 | Server crashes between receipt persistence and async dispatch | Recoverable processing; no lost or duplicate command. |
| API-SYNC-009 | Command references media not yet staged | Dependency pending/blocked; no dangling attachment. |
| API-SYNC-010 | Upload interrupted and resumed | Same asset identity/checksum verified; no corrupt attachment. |
| API-SYNC-011 | Uploaded bytes differ from declared checksum | Rejected; asset not attachable. |
| API-SYNC-012 | Media upload succeeds but observation command fails | Media remains unattached/staged under cleanup policy; observation not falsely marked applied. |
| API-SYNC-013 | Stale If-Match on observation update | 412; no lost update. |
| API-SYNC-014 | Missing required If-Match | 428 or documented precondition error; no blind update. |
| API-SYNC-015 | Two devices update different fields on same aggregate | Apply only if explicit field merge policy is approved; otherwise conflict and user resolution. |
| API-SYNC-016 | Two devices correct observation location differently | Conflict; preserve both histories and reasons. |
| API-SYNC-017 | Expert determination changes while field device is offline | Offline command cannot overwrite expert determination; server applies domain policy. |
| API-SYNC-018 | User role revoked after command queued | Server denies/blocks on processing; no stale offline privilege. |
| API-SYNC-019 | Rights permission revoked before media attachment | Attachment/use blocked according to current policy. |
| API-SYNC-020 | Sensitive location reclassified while device offline | Reconnection purges/restricts cache; public read/export remains protected. |
| API-SYNC-021 | Receipt ID guessed by another account | No disclosure of receipt or command result. |
| API-SYNC-022 | Cursor reused under another account | Denied or non-enumerating response; no cross-account changes. |
| API-SYNC-023 | Cursor expires | Documented expiry response; safe snapshot reconciliation. |
| API-SYNC-024 | Change feed paginated during concurrent updates | No skipped/duplicated logical changes under documented cursor model. |
| API-SYNC-025 | Permission removed between change pages | Subsequent page suppresses newly unauthorized data and signals invalidation safely. |
| API-SYNC-026 | Old client submits unsupported command schema | Rejected; command remains recoverable locally. |
| API-SYNC-027 | Client retries after 429 with Retry-After | Same command/key retained; bounded retry. |
| API-SYNC-028 | Client receives 401 during queue processing | Queue pauses; re-authentication does not mutate command identity. |
| API-SYNC-029 | Client receives 403/rights restriction | Command blocked; no automatic retry loop. |
| API-SYNC-030 | Client receives 5xx after uncertain commit | Receipt reconciliation before a new logical operation. |
| API-SYNC-031 | Notification generated for restricted record | No exact coordinates, sensitive taxon detail or private URL in payload. |
| API-SYNC-032 | Logs/traces inspected for sensitive values | No token, raw payload, exact restricted coordinates or signed upload URL. |
| API-SYNC-033 | Account switches while commands are pending | Commands remain bound to original account context; no cross-account submission. |
| API-SYNC-034 | User logs out with unsynchronized local content | Approved local retention/secure deletion/export policy is applied and communicated. |
| API-SYNC-035 | Device backup/restore contains a pending command | Restored command cannot bypass current authentication, rights or sensitivity checks. |
| API-SYNC-036 | Old client replays command after long offline period | Server reconciles command identity and returns safe expired/unsupported/policy result; no duplicate effect. |
| API-SYNC-037 | A withdrawal request is synchronized | Server creates a reviewable request; no unsupported claim that all copies are erased. |
| API-SYNC-038 | A new IdentificationRun is requested twice after timeout | One logical run request; prior run and candidates remain immutable. |
| API-SYNC-039 | API error contains internal exception text | Internal details are suppressed; stable Problem Details response is returned. |
| API-SYNC-040 | Public cache/CDN receives private response | Cache policy prevents shared caching or leakage. |
| API-SYNC-041 | Command includes untrusted client timestamp | Server retains it as client-reported context and records independent receipt time. |
| API-SYNC-042 | Client submits unsupported or fabricated CRS | Validation rejects or preserves unknown explicitly; no silent SRID assumption. |

## 18. Open decisions before contract freeze

| ID | Decision | Why it remains open |
|---|---|---|
| API-OD-01 | Final route naming and API base path | Requires complete API inventory and architecture review. |
| API-OD-02 | Exact command allow-list and aggregate boundaries | Must follow approved Task 05C scientific model and workflow semantics. |
| API-OD-03 | Client command ID format, scope and long-term uniqueness/tombstone policy | Needs offline duration, account lifecycle and storage threat analysis. |
| API-OD-04 | Idempotency-Key syntax, scope, fingerprint and retention | IETF draft is still work in progress; operational policy must be published. |
| API-OD-05 | Receipt persistence, processing model and transactional outbox design | Must fit selected modular backend and failure/recovery model. |
| API-OD-06 | Exact status codes and receipt state transitions by command type | Requires consistent API and product workflow semantics. |
| API-OD-07 | Revision granularity and strong ETag representation | Must align with Task 05C aggregate boundaries and update rules. |
| API-OD-08 | Deterministic field-level merge eligibility | Requires scientific and product review; default remains explicit conflict. |
| API-OD-09 | Change-feed cursor consistency, retention and snapshot model | Depends on data volume, authorization filtering and cache design. |
| API-OD-10 | Media provider, multipart/resumable upload protocol and expiry | Requires storage, cost, security and mobile reliability evaluation. |
| API-OD-11 | Authentication provider, OAuth/OIDC client registration and token lifecycle | Requires identity architecture and security review. |
| API-OD-12 | Authorization/role/authority and revocation semantics | Requires accepted security and scientific governance policy. |
| API-OD-13 | Rights checks and policy-version propagation | Requires asset-purpose rights model and governance. |
| API-OD-14 | Sensitive-location tiers, local cache eligibility and offline expiry | Requires conservation, privacy and qualified specialist decisions. |
| API-OD-15 | Account switching, logout, deletion, withdrawal and local-data retention | Requires product policy and current legal review. |
| API-OD-16 | Rate, size, concurrency and retry limits | Requires measured workloads and operational capacity evidence. |
| API-OD-17 | Observability, audit event taxonomy and retention | Requires security, privacy and operations review. |
| API-OD-18 | Backward-compatibility support window for long-offline clients | Requires supported-device and release policy. |
| API-OD-19 | Error taxonomy and stable Problem Details type URI registry | Requires API governance and a project-controlled documentation host. |
| API-OD-20 | Whether any expert workflow may operate offline | Default proposal is no; requires separate authority and conflict design to change. |

### 18.1 Recommended disposition for owner and specialist review

The following are **recommendations, not approved decisions**. They are intended to make the next review concrete while preserving the open-decision status of API-OD-01–20. A recommendation may be accepted, modified or rejected only by the appropriate decision authority after its stated dependencies are satisfied.

| ID | Recommended direction | Decision gate / evidence still required |
|---|---|---|
| API-OD-01 | Retain one versioned API base path (proposed `/api/v1`). Route offline-queueable writes through the command interface. Permit resource-specific synchronous routes only as façades over the same domain command processor, authorization, idempotency, revision, audit and receipt controls. | Complete API inventory; confirm client needs and route conventions. Do not freeze exact paths yet. |
| API-OD-02 | Start with a deliberately narrow allow-list for ordinary field workflows: observation creation/correction, withdrawal or restriction requests, verified media attachment, and identification-run requests where enabled. Do not expose generic entity writes. | Task 05C/05D aggregate and relationship validation; workflow lifecycle review. Privileged expert, publication, rights-grant and sensitive-location override commands remain excluded from ordinary offline queues. |
| API-OD-03 | Generate a cryptographically random opaque client command ID once per logical action; persist it through app restart and long disconnection. Scope reconciliation to authenticated principal plus installation/account context. Treat installation IDs as identifiers, never credentials. Preserve a durable deduplication/tombstone strategy independent of the shorter HTTP idempotency cache. | Threat model for installation reset, account deletion, shared devices, restore-from-backup and long-offline clients. Decide tombstone retention only after privacy, legal and operational review. |
| API-OD-04 | Keep HTTP `Idempotency-Key` distinct from client command identity. Bind it to authenticated principal and operation scope; fingerprint the semantic command payload and schema version while excluding volatile trace metadata. Reuse it only for retries of the same HTTP operation. | Recheck the IETF draft at contract freeze; define syntax, concurrency, replay and expiry behavior. Set retention from measured maximum supported offline/retry windows and risk, not an invented fixed number. |
| API-OD-05 | Prefer a durable receipt plus recoverable asynchronous processing. Where receipt and domain mutation share a transaction, commit atomically. Where work is asynchronous, use a transactional outbox or equivalent recoverable dispatch and idempotent consumer. Keep one domain mutation path. | Backend failure model, selected persistence technology and transaction boundaries; verify crash/replay scenarios with executable tests. |
| API-OD-06 | Use a small receipt lifecycle such as `received`, `processing`, `applied`, `rejected`, `conflict`, `blocked` and `retryable_failure`, with documented allowed transitions and terminal/resumable behavior. Use `202` only when durable receipt and asynchronous processing are confirmed. | Map each command type to response semantics; reconcile with the separate Observation, Identification, review, rights and publication state machines. Do not let a receipt imply scientific validation. |
| API-OD-07 | Use strong opaque ETags for mutable shared representations and require `If-Match` for updates where lost-update protection is needed. Prefer revision scope aligned to validated domain aggregates, not individual database columns. | Task 05C relationship/aggregate validation. Missing required precondition should have a documented response (recommended `428`); stale precondition `412`; semantic domain conflict `409`. |
| API-OD-08 | Default to explicit conflict for concurrent scientific, location, time, taxonomic, rights, review and determination changes. Consider automatic merging only for demonstrably independent, non-scientific fields with deterministic semantics, auditability and tests. | Scientific and product reviewers must approve each merge-eligible field class. No generic last-write-wins. |
| API-OD-09 | Use opaque, authorization-bound cursors over a consistent change sequence/snapshot. Filter by current authorization and sensitivity policy on every page. Provide explicit cursor-expiry recovery using a fresh snapshot plus tombstones or equivalent deletion/restriction markers. | Data-volume and query-plan evidence; prove no missed/duplicated changes under concurrent writes, policy changes, pagination and cursor expiry. Define retention after operational testing. |
| API-OD-10 | Use staged, resumable uploads with server-issued bounded upload authorization, content-length/type validation, cryptographic checksum verification and quarantine/scanning before an asset becomes attachable. Upload success must not itself publish or attach media. | Compare provider and protocol options against Flutter/Android/iOS reliability, cost, security, rights and storage lifecycle. Provider and expiry values remain open. |
| API-OD-11 | For native Flutter public clients, prefer OpenID Connect/OAuth 2.0 Authorization Code with PKCE through a standards-conforming identity provider. Do not use implicit or resource-owner-password grants. Keep provider selection separate from protocol requirements. | Identity-provider threat model, account recovery, MFA needs, federation, accessibility, cost, data residency and operational review. Follow RFC 9700. |
| API-OD-12 | Use server-side policy evaluation combining role/capability with resource ownership, expert authority scope, relationship/context and property-level permissions. Enforce object-level authorization on every identifier-based operation. Actor identity comes from authenticated context, not client payload. | Approve role/authority matrix, delegation, conflict-of-interest, revocation and audit rules. Security review must include OWASP API1/API3/API5 classes. |
| API-OD-13 | Evaluate rights per asset and intended purpose, including storage, display, derivative creation, redistribution, export and AI/embedding use. Revalidate rights at upload completion, attachment and each controlled downstream use; retain policy version and decision provenance. | Approved asset-specific licensing policy and rights model; qualified rights/legal review. Unknown rights remain blocking for restricted uses. |
| API-OD-14 | Do not cache exact sensitive species coordinates as general reference data. If exact coordinates are necessary for a user's own field capture, collect only for an explicit purpose, protect in encrypted local storage, separate from general caches, and re-evaluate server policy on synchronization. Public and export representations must apply current generalization/withholding rules. | Conservation, privacy and security reviewers must set sensitivity tiers, offline eligibility, stale-policy exposure and incident response. Offline devices cannot guarantee instant revocation; state this limitation plainly. |
| API-OD-15 | Isolate local drafts/outboxes by account. Never replay a prior account's commands under a newly authenticated account. On logout/account switch, pause sync, protect or quarantine pending data and present a documented recovery choice; do not silently erase or transfer it. | Product, privacy and qualified legal review of retention, withdrawal, erasure, backup and account recovery. Do not equate withdrawal with physical deletion. |
| API-OD-16 | Establish per-operation limits for payload size, media size, concurrency, rate, queue age and retry behavior. Apply adaptive back-pressure and observable throttling. | Derive limits from representative field-network/device tests, load tests, storage budgets and cost/security threat models. No numeric values before evidence. |
| API-OD-17 | Separate immutable domain/audit events from operational telemetry. Minimize logged fields; never log bearer tokens, full command payloads, private media URLs or exact sensitive coordinates by default. Define role-restricted access, purpose and retention for each log class. | Security/privacy review, incident-response needs and current legal retention analysis. |
| API-OD-18 | Support a documented compatibility window for clients that may remain offline. Version command schemas independently, retain only explicitly supported handlers, and provide safe upgrade/reconciliation behavior for expired clients. Never silently reinterpret an old command under new semantics. | Establish supported app/OS matrix, release cadence and maximum offline interval using user/device research and operational capacity. |
| API-OD-19 | Use RFC 9457 Problem Details with stable machine-readable project error codes and documented type identifiers. Keep human detail localizable and safe; do not disclose restricted data or internals. | Establish a project-controlled documentation/URI namespace and API governance process before freezing the registry. |
| API-OD-20 | Keep expert determinations, publication approvals, rights grants, sensitive-location overrides and administrative actions online-only in the initial contract. | Any exception requires a separate privileged offline threat model, authority, signing/audit, conflict and revocation design plus explicit approval. |

### 18.2 Recommended decision order

Do not attempt to close all 20 decisions in one workshop. Resolve them in dependency order:

1. **Domain boundary first:** API-OD-02, API-OD-06, API-OD-07 and API-OD-08, together with Task 05C/05D and the workflow state machines.
2. **Command reliability:** API-OD-03, API-OD-04 and API-OD-05. Prove duplicate replay, lost response, process crash and long-offline reconciliation.
3. **Security and rights:** API-OD-11 through API-OD-15 and API-OD-17. These require security, conservation, privacy and rights expertise; the present design is not a legal or security approval.
4. **Data synchronization and media:** API-OD-09 and API-OD-10, with cursor correctness, media integrity and policy invalidation tests.
5. **Operational policy:** API-OD-16 and API-OD-18, based on measurements and an agreed support model.
6. **Contract publication:** API-OD-01 and API-OD-19, followed by version-pinned OpenAPI and executable contract tests.
7. **Privileged offline scope:** API-OD-20 remains closed to ordinary field synchronization unless a separate proposal passes all required reviews.

**Standards checked 21 November 2026:** OpenAPI Specification 3.2.1 (10 September 2026); RFC 9110; RFC 9457; RFC 9700 (OAuth 2.0 Security BCP); OWASP API Security Top 10:2023; and `draft-ietf-httpapi-idempotency-key-header-08` (active Internet-Draft dated 22 October 2026, not an RFC). The IETF draft must be rechecked before contract freeze.

No numeric timeout, retention period, request size, retry count, cache duration, precision threshold or service-level objective is invented here.

## 19. Task 05 dependency and physical-design gate

This contract does not resolve Task 05 scientific-model findings. In particular:
- DR-01 through DR-04 require the relevant occurrence/export, typed subject, TCS relation and `accordingTo` semantics to remain consistent.
- DR-05 through DR-07 affect synonym relationships, determination history and observation/event/occurrence semantics.
- DR-08 through DR-12 affect source scope, standards mapping, identifiers and authority/evidence interpretation.
- LDM-01 through LDM-16 remain proposed validation scenarios, including rights, sensitive location, source versioning and provenance.

The API can be designed at a stable boundary before the physical schema, but command payloads and canonical representations cannot be frozen until their scientific meaning and aggregate boundaries are validated. No Task 05E physical database design or migration is authorized by this document.

## 20. Recommended implementation sequence after approval

1. Approve the command/receipt vocabulary and domain command boundaries.
2. Resolve the applicable Task 05C/05D scientific semantics and aggregate boundaries.
3. Approve identity, authorization, rights, privacy and sensitive-location policy dependencies.
4. Produce the API inventory and versioning/deprecation policy.
5. Create a version-controlled OpenAPI description for the agreed first contract slice.
6. Define server receipt persistence and recoverable processing design without prematurely selecting infrastructure.
7. Prototype duplicate replay, lost-response recovery, stale revision and cursor expiry.
8. Define media staging and integrity verification.
9. Generate consumer contract tests and negative authorization/privacy tests.
10. Validate against Android/iOS offline execution constraints and the Flutter client architecture.
11. Run security, privacy, scientific and operational reviews before implementation release.

## 21. Acceptance checklist for this specification

- [ ] Owner accepts the command and receipt terminology.
- [ ] Product owner confirms command types and non-goals.
- [ ] Architecture reviewer confirms API-first compatibility and modular boundary.
- [ ] Scientific-data reviewers confirm no conflict with Task 05C/05D semantics.
- [ ] Mobile reviewer validates client command identity, local persistence and long-offline recovery.
- [ ] Security reviewer validates idempotency scope, authorization, upload capabilities and receipt access.
- [ ] Privacy/conservation reviewer validates sensitive-location and offline cache treatment.
- [ ] Rights reviewer validates asset-purpose gating and media lifecycle.
- [ ] API error/status and compatibility policies are agreed.
- [ ] OpenAPI contract is generated and validated before implementation.
- [ ] All numeric operational policies have evidence and accountable owners.
- [ ] Tests are implemented and executed; results are recorded separately from this proposed test matrix.

## 22. References and research notes

The following primary sources were checked on 21 November 2026. Standards and drafts must be rechecked before contract freeze.

1. **OpenAPI Initiative**, OpenAPI Specification v3.2.1, dated 10 September 2026. The official specification defines a language-agnostic description for HTTP APIs.  
   https://spec.openapis.org/oas/v3.2
2. **IETF RFC 9110**, HTTP Semantics (June 2022), especially conditional requests, ETags, `If-Match`, and status semantics. Strong `If-Match` comparison supports lost-update prevention.  
   https://www.rfc-editor.org/rfc/rfc9110.html
3. **IETF RFC 9457**, Problem Details for HTTP APIs (July 2023), defining machine-readable problem details and `application/problem+json`.  
   https://www.rfc-editor.org/rfc/rfc9457.html
4. **IETF RFC 9700 / BCP 240**, Best Current Practice for OAuth 2.0 Security (January 2025). Apply current OAuth security recommendations if OAuth is selected.  
   https://www.rfc-editor.org/rfc/rfc9700.html
5. **IETF HTTPAPI Working Group**, The Idempotency-Key HTTP Header Field, active Internet-Draft version 08 (22 October 2026; work in progress, not an RFC). Recheck the current version, status and syntax before adoption.  
   https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/
6. **Flutter**, Offline-first architecture guidance.  
   https://docs.flutter.dev/app-architecture/design-patterns/offline-first
7. **Android Developers**, Persistent background work / WorkManager.  
   https://developer.android.com/develop/background-work/background-tasks/persistent
8. **Apple Developer Documentation**, Background Tasks.  
   https://developer.apple.com/documentation/backgroundtasks
9. **OWASP**, Mobile Application Security Verification Standard (MASVS).  
   https://mas.owasp.org/MASVS/

**Research limitation:** this is a technical contract-design review, not a security certification, legal opinion, privacy impact assessment, or independent scientific validation. No implementation, deployment, API runtime, load test, penetration test or field trial was performed.

---

**End of proposed contract design — STF-BI-API-SYNC-001 v0.1.**
