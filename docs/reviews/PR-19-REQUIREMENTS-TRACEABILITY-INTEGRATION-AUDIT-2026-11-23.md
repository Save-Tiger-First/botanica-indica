# PR #19 — Requirements Traceability and Integration Audit

**Document ID:** STF-BI-AUD-PR19-001  
**Version:** 0.1 — Proposed audit record  
**Audit date:** 23 November 2026  
**Status:** Findings and recommendations for project-owner and discipline review; not an approval, requirements baseline or implementation authorization  
**Repository:** Save Tiger First / botanica-indica  
**Working branch:** docs/requirements-traceability-register  
**Pull request:** #19 — Product: propose full-product requirements traceability register  
**Decision authority:** Save Tiger First project owner

---

## 1. Executive conclusion

**Recommendation: keep PR #19 open and draft. Do not merge or treat its contents as an approved requirements baseline yet.**

PR #19 is a substantial and useful improvement. It preserves the original Task 03 functional requirement identifiers, establishes the proposed BI-CAP-01–BI-CAP-16 capability map, links the twelve acceptance criteria, identifies scientific-model dependencies, and adds workflow, offline synchronization and API contract proposals. It also correctly distinguishes proposed test designs from executed evidence.

The audit nevertheless identifies material work required before acceptance:

1. The RTM still contains the identity/authentication capability mapping defect that its own companion audit explicitly identifies.
2. Multiple source-revision tables contain stale blob SHAs, including the operating prompt, Blueprint, scientific review pack, validation register, workflow crosswalk and prior audit. This weakens reproducibility and can cause a reviewer to audit a different document version from the one actually used.
3. The owner-authorized ODR-01 export-only clarification and its EVT-27–EVT-44 validation obligations are not fully carried through the RTM, workflow crosswalk, offline specification and API contract.
4. The proposed Observation lifecycle state named “received” is semantically ambiguous with the distinct server command receipt state “server_received”.
5. The STF shared-platform versus Botanica Indica domain boundary remains unresolved in the original Task 03/04 source material and must not be treated as settled by the proposed capability map.
6. PR #20's architecture snapshot still cites earlier versions of the operating prompt, Blueprint and RTM. The PR #17–#20 integration package therefore needs a source-version refresh.

The most important positive finding is that the PR #19 documents generally preserve uncertainty and approval boundaries. The remediation should strengthen this work rather than replace it.

## 2. What was inspected

### 2.1 Governing instructions and live repository

The complete AI Project Operating Prompt was retrieved from branch docs/repository-audit-and-ai-operating-standard.

| Item | Verified value |
|---|---|
| Operating prompt blob SHA | 53add3894d0502827e584614c70ad09cadaa637d |
| PR #19 state | Open |
| PR #19 draft status | Draft |
| PR #19 head branch | docs/requirements-traceability-register |
| PR #19 head SHA | b2e8728e5e725b844a41438260e3a40f77ca65db |
| PR #19 base branch | develop |
| PR #19 base SHA | f165ecb9b4d9de115c02327cf779982b7ef4bbd4 |

The live branch list contains 23 branches. The live open-PR search returned 19 open PRs, all drafts. The seven-branch ceiling is not met. PR #15 is closed unmerged, but its source branch remains present. No branch retirement is claimed in this audit.

Long-lived branch heads at the review:

| Branch | SHA |
|---|---|
| main | 6f2f51da093caf8183fde386dbec707cc6046d27 |
| develop | f165ecb9b4d9de115c02327cf779982b7ef4bbd4 |
| staging | f165ecb9b4d9de115c02327cf779982b7ef4bbd4 |

### 2.2 PR #19 changed-file inventory

All seven current PR #19 files were fetched from the exact source branch and their blob SHAs recorded.

| File | Blob SHA | Lines |
|---|---|---:|
| docs/architecture/API-COMMAND-IDEMPOTENCY-AND-CONFLICT-RESOLUTION-CONTRACT-DESIGN.md | 6ffb50286c59449773caf574d4236d6e0b2208e0 | 882 |
| docs/architecture/OFFLINE-FIELD-SYNCHRONIZATION-ARCHITECTURE-AND-VALIDATION-SPECIFICATION.md | 4403d335dab5851eda90bdf41bfecc58be9b5840 | 701 |
| docs/architecture/TASK-03-04-CROSS-DOCUMENT-READINESS-AUDIT.md | f3e9c6998104b5435c24b4b70d136ced763245f5 | 411 |
| docs/product/REQUIREMENTS-TRACEABILITY-REGISTER.md | 5636760faed6c7c7be0363d68afc203dd48e7e33 | 510 |
| docs/product/TASK-03-ACCEPTANCE-TEST-PLAN.md | 0e7a1d1851492bb4470b2e0fea6991e59db67f2a | 415 |
| docs/product/WORKFLOW-LIFECYCLE-AND-STATE-MACHINE-SPECIFICATION.md | 03ca940095a9e39c5608548bdeec1ce0166bf76d | 340 |
| docs/product/WORKFLOW-REQUIREMENTS-TRACEABILITY-CROSSWALK.md | 9ab92566c80997436d4f03c05511f9c91960756b | 177 |

### 2.3 Related sources inspected

| Source | Ref | Current blob SHA |
|---|---|---|
| Task 03 PRD v0.1 source-preserving transcription and overlay | docs/canonical-task-03-04-baselines | 8b1ca0be04b3f4ad3b543c2f9fc48d46eb37faf8 |
| Task 04 architecture v0.1 source-preserving transcription and overlay | docs/canonical-task-03-04-baselines | abc7b721fae8d4f4adede4dd0bf5d6a32098c5a3 |
| Full Product Vision and Capability Blueprint v0.2 | docs/full-product-vision-capability-blueprint | d3ec150524dda4928503f43556a97cd766b71312 |
| Full System Architecture and Repository Engineering Plan v0.1 | docs/full-system-architecture-and-repo-engineering-plan | 91fb02be87b42df51f92106f90fd536a01a5b902 |
| Scientific Data Model Review Pack | review/scientific-data-model-review-pack | c11f4b58d0908742474d3e58b4ec0aa3739f7b99 |
| Scientific Data Model Validation Matrix and Decision Register | review/scientific-data-model-review-pack | 3a33dfe47657a96456f56f2c12a0b7d355b6c6a5 |

Accepted ADR-001 through ADR-010 remain the governing accepted architecture decisions. No ADR was amended or superseded in this audit.

## 3. Positive findings

### 3.1 Source requirements are preserved

The RTM preserves the 19 original Task 03 functional requirement identifiers and distinguishes them from proposed derived requirements. It retains the seven Task 03 non-goals as scope guardrails. The source PRD itself remains a source-preserving transcription and is not silently rewritten.

### 3.2 Capability identifier reconciliation is explicit

The proposed BI-CAP-01–BI-CAP-16 namespace is aligned to the sixteen capability domains in Blueprint Sections 5.1–5.16. The RTM retains a legacy CAP-01–CAP-16 crosswalk rather than silently reusing old labels. The Blueprint also records its earlier fifteen-domain numbering and split of taxonomy from botanical knowledge profiles.

These identifiers remain proposed until owner acceptance.

### 3.3 Acceptance coverage is candid

The acceptance plan contains 66 proposed test cases across all twelve acceptance criteria. It explicitly states that all are Proposed / Not run and that the criteria remain blocked by unresolved product, scientific, policy, rights, privacy, architecture and security dependencies.

### 3.4 Workflow coverage is appropriately qualified

The workflow crosswalk maps sixteen proposed workflow scenarios to Task 03 requirements, acceptance criteria, capability IDs, ADRs and Task 05 dependencies. It explicitly identifies partial or absent workflow coverage for AC-006, AC-008, AC-009, AC-010, AC-011 and AC-012 rather than pretending that lifecycle scenarios cover every product acceptance obligation.

### 3.5 Offline and API proposals preserve important distinctions

The offline and API proposals distinguish:
- local draft and queued command states;
- durable server receipt and committed domain operation;
- client command identity and HTTP request idempotency;
- Observation lifecycle and scientific determination;
- moderation, rights, privacy, publication and scientific review;
- retryable transport failures and domain conflicts.

The proposals also prohibit generic last-write-wins for scientific determinations, rights decisions and sensitive-location restrictions. These are appropriate design guardrails, subject to owner and specialist review.

## 4. Findings ranked by severity

### PR19-AUD-01 — Identity/authentication capability mapping defect remains in the RTM

**Severity: Major — unresolved internal inconsistency**

The RTM Section 7 row “Identity, authentication, roles and permissions” maps to BI-CAP-09–BI-CAP-14.

That range is not an identity capability. In the proposed Blueprint:
- BI-CAP-09 is Community participation and stewardship;
- BI-CAP-10 is Mobile application;
- BI-CAP-11 is Public web and research platform;
- BI-CAP-12 is Expert and scientific console;
- BI-CAP-13 is Administration and data stewardship console;
- BI-CAP-14 is API and institutional integration platform.

The companion audit already records this exact defect as AUD-034-02 and recommends representing identity as a cross-cutting STF platform capability. The current RTM mapping remains unchanged, so the audit and register contradict one another.

**Recommendation**

Do not create or assign a new STF platform identifier without owner approval. In the next controlled RTM revision:
1. Remove the false BI-CAP-09–BI-CAP-14 identity mapping.
2. Classify identity/authentication/authorization primitives as a proposed cross-cutting STF platform capability, with identifier left unassigned until approved.
3. Link each Botanica capability only where its actual journey consumes identity or authorization.
4. Keep administration capability BI-CAP-13 distinct from identity infrastructure.
5. Recheck all Task 04 architecture responsibility rows using separate platform, Botanica domain and client-capability columns.

Do not renumber or repurpose any BI-CAP identifier.

### PR19-AUD-02 — Source-revision tables contain stale blob SHAs

**Severity: Major — provenance and reproducibility**

Several source tables identify revisions that no longer match the exact current source files fetched during this audit.

| Document containing stale reference | Recorded SHA | Current SHA |
|---|---|---|
| RTM — AI Project Operating Prompt | 61059c74d4d20309ff76e055059ab33f381ca4f2 | 53add3894d0502827e584614c70ad09cadaa637d |
| RTM — Blueprint v0.2 | 905455233d11fc750ba3a485d5c516e01f8426ee | d3ec150524dda4928503f43556a97cd766b71312 |
| RTM — Scientific Data Model Review Pack | f8ce8caab31d02a38e2f3deb957b67af77decad6 | c11f4b58d0908742474d3e58b4ec0aa3739f7b99 |
| RTM — Validation Matrix and Decision Register | f1d8c927b54c74fc33be9eedcdf2b8dfc533dda7 | 3a33dfe47657a96456f56f2c12a0b7d355b6c6a5 |
| Workflow crosswalk — AI Project Operating Prompt | 61059c74d4d20309ff76e055059ab33f381ca4f2 | 53add3894d0502827e584614c70ad09cadaa637d |
| Workflow crosswalk — RTM v0.2 | 5f6862d6ece8d428714588daff54992ccaabfdf2 | 5636760faed6c7c7be0363d68afc203dd48e7e33 |
| Offline specification — AI Project Operating Prompt | 61059c74d4d20309ff76e055059ab33f381ca4f2 | 53add3894d0502827e584614c70ad09cadaa637d |
| Offline specification — Workflow crosswalk | 87dc1ba325238289a030e9e8ef07a8fc903f51a9 | 9ab92566c80997436d4f03c05511f9c91960756b |
| Offline specification — Task 03/04 readiness audit | 25084a9f4146aecb76b6cc1d4fc658b665a017f9 | f3e9c6998104b5435c24b4b70d136ced763245f5 |

PR #20's architecture plan also contains an older source inventory:
- operating prompt recorded as 65cb5ac58c79f2bf14a1e7df1d9b18ea608850ed rather than current 53add3894d0502827e584614c70ad09cadaa637d;
- Blueprint recorded as v0.1 / ccfe15d86bc832e61590028d57c08c4ce4fbbed rather than current v0.2 / d3ec150524dda4928503f43556a97cd766b71312;
- RTM recorded as v0.1 / 1e65218f2b63aad9ea1f078d71594de53999990f rather than current v0.2 / 5636760faed6c7c7be0363d68afc203dd48e7e33.

The historical SHAs are not inherently wrong for the dates when they were captured. The defect is that the documents do not clearly distinguish historical source snapshots from the current revisions on which the current cross-document claims depend.

**Recommendation**

Add dated source-revalidation notes to the RTM, workflow crosswalk and offline specification. Preserve the original snapshot as history; do not silently replace historical evidence. Refresh PR #20's architecture inventory separately on its existing branch. Before future approval, record exact file path, branch/ref, blob SHA, version and date checked.

### PR19-AUD-03 — ODR-01 and EVT-27–EVT-44 are not fully integrated into requirements traceability

**Severity: Major; implementation blocker for the affected external-export interpretation**

The current scientific validation register records owner-authorized ODR-01:

- Option B is authorized for controlled, profile-specific implicit non-detection interpretation in external exports only.
- A missing internal Occurrence row remains unknown/not assessed.
- No internal absence assertion may be created from an empty result set.
- Export interpretation requires applicable scope and reporting-completeness evidence, pinned term/profile/mapping versions, correct hierarchy, provenance and auditability.
- Bycatch and taxa outside declared scope are excluded.
- Ambiguous, incomplete, contradictory or insufficient evidence must fail closed.
- The final wording is “Not detected/reported within the stated survey scope under documented survey conditions”, never biological absence.
- ODR-01 does not approve a final export profile, Task 05C, Task 05E, physical schema, API or implementation.

The validation register adds EVT-27–EVT-44 obligations, including fail-closed completeness/method evidence, hierarchical Event scope, a priori versus post-facto survey target scope, version changes and additional non-detection edge cases. These remain proposed and unexecuted.

The RTM mentions ODR-01 in its standards/source-correction material, but the RTM's principal scientific dependency crosswalk, workflow crosswalk, offline specification and API contract do not provide a complete ODR-01-to-requirement-to-API/export-to-test mapping. The API contract discusses DR-01 and explicit non-detection generally, but does not map the owner-authorized ODR-01 conditions or EVT-27–EVT-44 as explicit contract acceptance obligations.

**Recommendation**

Add a dedicated ODR-01 traceability row and a controlled export-specific crosswalk:
1. Link the owner decision to the affected requirements, relevant capability, export contract and test obligations.
2. Map each applicable EVT case to the responsible export/profile behavior and its required evidence.
3. Preserve the distinction between internal unknown/not assessed, explicit internal survey non-detection and profile-specific external export interpretation.
4. Require explicit scope at every applicable hierarchy level; do not infer or silently inherit it.
5. Keep reporting completeness, survey effort, detectability and taxonomic scope completeness separate.
6. Keep bycatch and out-of-scope taxa excluded.
7. Pin the exact external profile, Darwin Core/Humboldt terms and mapping versions before implementation.
8. Add negative tests proving missing/ambiguous/contradictory evidence suppresses the export interpretation.
9. Keep the final profile and API payload undecided until the scientific and specialist review gates are met.

Do not create an internal negative Occurrence from a missing row. Do not treat ODR-01 as authorization to implement a final export profile.

### PR19-AUD-04 — Observation “received” state overlaps server command receipt semantics

**Severity: Major — state-machine/API ambiguity**

The Workflow Lifecycle Specification defines an Observation state named “received” as “Server acknowledged and assigned a durable identifier”.

The offline and API specifications separately define client synchronization / command receipt state “server_received” as a durable command receipt where domain processing may still be pending. The API contract explicitly distinguishes receipt from the committed domain operation.

This creates a possible semantic collision: an Observation may appear “received” even though the command receipt exists but the Observation domain operation has not yet committed or received its canonical Observation identifier.

**Recommendation**

Before workflow/API freeze:
- Define “received” as a domain-record state only if it means a canonical Observation resource has actually been created and committed.
- Otherwise rename the Observation state to an unambiguous domain term such as “record_created” or remove it as a lifecycle state and record the creation event separately.
- Keep client sync “server_received” and API command receipt states in their own state domain.
- Define the exact transition that creates the canonical Observation ID.
- Add tests for durable receipt without domain commit, failed processing after receipt, and successful commit after retry.

This is a clarification proposal only; no state name is changed by this audit.

### PR19-AUD-05 — STF shared-platform and Botanica domain boundary remains unresolved

**Severity: Major — architecture ownership dependency**

The source-preserving Task 03 and Task 04 material contains historical classifications that place taxonomy, evidence and observation services under shared STF platform services. The operating prompt and proposed Blueprint instead distinguish reusable platform infrastructure from Botanica-owned botanical taxonomy, evidence, observations, identification and scientific governance.

The RTM and companion audit correctly identify this as an open boundary question. The Task 04 overlay preserves the original text and explicitly says its historical material is not an accepted ownership decision.

**Recommendation**

Keep the boundary as an open owner decision. Do not treat the Blueprint or RTM capability map as a formal ownership transfer. When the owner decides:
- preserve original Task 03/04 source text;
- add a dated reconciliation overlay;
- distinguish shared infrastructure from domain-owned scientific rules and records;
- do not create a universal STF taxonomy/evidence/observation service by analogy alone;
- do not infer separate repositories, teams or deployments from logical boundaries.

Proposed ADR-011 remains unaccepted and must not be treated as the decision.

### PR19-AUD-06 — Task 04 source citation tokens remain non-durable

**Severity: Minor to Major — research traceability**

The Task 04 source-preserving transcription contains temporary citation tokens that cannot serve as durable repository references. The Task 04 overlay acknowledges this and recommends replacing them in a future canonical revision with source organization/title, canonical URL, version/date, access date and the claim supported.

**Recommendation**

Retain the original transcription unchanged. In the future canonical Task 04 revision, provide durable references and re-verify changing technical claims. Do not represent the overlay as a retroactive correction to the original DOCX.

### PR19-AUD-07 — Acceptance and workflow test coverage is proposed, not executable evidence

**Severity: Observation / mandatory readiness gate**

The Acceptance Test Plan contains 66 proposed cases across AC-001–AC-012. All are Proposed / Not run. The workflow crosswalk covers sixteen scenarios, but it explicitly records:
- partial workflow-scenario coverage for AC-006, AC-008, AC-009 and AC-010;
- no direct workflow-scenario coverage for AC-011 and AC-012.

The separate acceptance plan does include proposed cases for AC-011 and AC-012. Therefore, this is not a missing-AC defect in the combined PR #19 package. It is important that reviewers do not mistake the workflow crosswalk alone for complete acceptance coverage.

**Recommendation**

Retain separate traceability for:
- product acceptance criteria AC-001–AC-012;
- workflow scenarios WF-001–WF-016;
- offline validation cases OFF-001–OFF-036;
- API contract scenarios API-SYNC-001–API-SYNC-042;
- scientific validation scenarios LDM and EVT.

Create explicit links between them where they overlap, but do not force a one-to-one mapping. No test is passed until it has an approved oracle, eligible fixture, actual execution, retained evidence and appropriate review.

### PR19-AUD-08 — Offline and API designs remain proposals with unresolved decision gates

**Severity: Major — implementation readiness**

The offline specification records OFF-OD-01–OFF-OD-16 as open. The API contract records API-OD-01–API-OD-20 as open. The command allow-list, aggregate boundaries, idempotency retention, receipt persistence, revision scope, merge eligibility, cursor model, media provider, identity provider, authorization policy, rights checks, sensitive-location tiers, account lifecycle, limits and observability policy are not frozen.

The API contract appropriately defers survey/non-detection commands and several domain payloads until Task 05 semantics are resolved. The offline specification also correctly avoids guaranteeing exact-time background execution or instant revocation while a device is disconnected.

**Recommendation**

Keep both documents Proposed. Use them as design-review inputs only. Do not create production OpenAPI schemas, physical tables, migrations or offline command implementations until:
- the relevant Task 05 scientific model semantics are reviewed;
- ODR-01 export behavior is mapped and profile-pinned;
- product and API state semantics are reconciled;
- security, rights, privacy, conservation and mobile review gates are satisfied;
- test fixtures and acceptance oracles are approved.

### PR19-AUD-09 — PR #20 architecture source inventory is stale relative to PR #17–#19

**Severity: Major — cross-workstream integration**

The current PR #20 architecture plan still identifies earlier versions of the operating prompt, Blueprint and RTM. The PR #17 Blueprint has moved to v0.2 and the PR #19 RTM to v0.2. The PR #20 source inventory should not be treated as a current cross-workstream baseline until refreshed.

**Recommendation**

On the existing PR #20 branch, update the source inventory only after re-fetching each source and recording its exact branch, blob SHA, version and status. Then re-run the architecture-to-capability and requirements-to-module crosswalk. Do not retarget, merge or close PR #17, #18, #19 or #20 merely because their documents are grouped into one workstream.

## 5. Cross-document readiness matrix

| Area | Current finding | Status |
|---|---|---|
| Original Task 03 requirements | 19 identifiers preserved | Structurally sound; proposed |
| Task 03 non-goals | Seven source guardrails preserved | Structurally sound; proposed |
| Capability map | BI-CAP-01–BI-CAP-16 reconciled with Blueprint v0.2 | Proposed; owner approval pending |
| Identity mapping | Incorrect BI-CAP-09–BI-CAP-14 range remains | Major correction required |
| Task 04 architecture mapping | Responsibilities mapped, but platform/domain/client categories need review | Partially aligned |
| Workflow scenarios | Sixteen scenarios mapped | Proposed; transition authority and tests remain open |
| Acceptance criteria | AC-001–AC-012 mapped; 66 proposed test cases | Proposed / not run |
| Offline synchronization | OFF-001–OFF-036 and OFF-OD-01–16 | Proposed / not run / decisions open |
| API command contract | API-SYNC-001–042 and API-OD-01–20 | Proposed / not run / decisions open |
| ODR-01 and export validation | Decision exists, but traceability into API/export tests incomplete | Major integration required |
| Scientific model | DR-01–DR-12, LDM-01–LDM-16 and EVT tests remain review obligations | Blocking dependencies remain |
| Rights/privacy/security | Principles present; policies and legal applicability remain open | Not implementation-ready |
| Source provenance | Multiple stale blob SHAs | Major correction required |
| Implementation | No implementation or test execution established by these documents | Not claimed |

## 6. Recommended remediation sequence

The following order minimizes rework and preserves the current source documents.

### Gate A — repair traceability and provenance

1. Revalidate source revision tables in the RTM, workflow crosswalk and offline specification.
2. Add a controlled ODR-01 export traceability crosswalk, including applicable EVT-27–EVT-44 obligations.
3. Correct the identity/authentication mapping only after owner direction on the shared-platform boundary; until then mark it explicitly as unresolved rather than mapping it to unrelated BI-CAP IDs.
4. Clarify Observation “received” versus command “server_received”.
5. Preserve the original Task 03/04 source transcriptions.

### Gate B — reconcile product and architecture sources

6. Refresh PR #20's source inventory using current PR #16, #17, #18 and #19 blob SHAs.
7. Review the complete PR #17 Blueprint against the PR #18 source-preserving Task 03/04 baselines.
8. Review PR #19's RTM architecture mapping against the current proposed architecture plan.
9. Resolve shared platform/domain/client responsibility categories without silently approving ADR-011.

### Gate C — scientific and API readiness

10. Preserve all Task 05 DR/LDM/EVT issues and their current statuses.
11. Obtain appropriate scientific review of Observation/Event/Survey/Occurrence and ODR-01 export semantics.
12. Reconcile workflow, offline and API state vocabularies.
13. Keep physical schema and production API payload freeze blocked until the applicable scientific and policy gates are met.

### Gate D — acceptance readiness

14. Assign actual accountable reviewer roles; no reviewer is assumed appointed.
15. Approve test oracles and rights/privacy-eligible fixtures.
16. Convert ready proposed cases into executable tests only after the relevant contracts and policies stabilize.
17. Record execution evidence and independent review separately from the proposed test documents.

## 7. External technical-source recheck

The following official sources were rechecked on 23 November 2026:

- IETF Idempotency-Key HTTP Header Field: current datatracker search result identifies draft-ietf-httpapi-idempotency-key-header-09, published 21 November 2026, active Internet-Draft, intended Standards Track, expiring 25 May 2027. It remains a work in progress, not an RFC. The API contract's reference to version 08 dated 22 October 2026 is stale and should be refreshed.
- RFC 9110: strong If-Match comparison is intended to prevent lost updates; a failed precondition can be represented by 412 Precondition Failed. Domain conflicts remain a distinct application/API decision.
- RFC 9457: defines Problem Details for HTTP APIs and application/problem+json.
- RFC 9700: current OAuth 2.0 Security Best Current Practice.
- Flutter's official offline-first guide describes repository-mediated local/remote data and alternative synchronization approaches; it does not guarantee a particular background scheduling behavior.

Sources:
- https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/
- https://www.rfc-editor.org/rfc/rfc9110.html
- https://www.rfc-editor.org/rfc/rfc9457.html
- https://www.rfc-editor.org/rfc/rfc9700.html
- https://docs.flutter.dev/app-architecture/design-patterns/offline-first

These sources support technical design review only. They do not establish legal compliance, scientific validation, security certification or project-owner approval.

## 8. Work performed and not performed

### Completed

- Retrieved the complete governing operating prompt from the required PR #16 branch.
- Re-fetched the live repository branch list, open PR inventory, relevant PR metadata and long-lived branch heads.
- Re-fetched the current PR #19 changed-file list and all seven current files.
- Inspected the Task 03 and Task 04 source-preserving baselines and overlays.
- Inspected the PR #17 Blueprint and PR #20 architecture plan.
- Inspected the current scientific review pack and validation/decision register, including ODR-01 and EVT test extensions.
- Rechecked current official IETF and Flutter technical references.
- Recorded findings and remediation recommendations in this audit report.

### Not performed

- No accepted ADR was changed.
- No original Task 03/04 source transcription was rewritten.
- No scientific model or product requirement was approved or amended.
- No PR was merged, closed or retargeted.
- No branch was created or deleted.
- No repository protection, setting or permission was changed.
- No production API schema, application code, database schema or migration was created.
- No tests were executed.
- No scientific, legal, security, privacy, rights or institutional approval was obtained.
- No external institution or reviewer was contacted.
- No Graphify installation or execution was performed.

## 9. Decision and next action

**Recommendation:** retain PR #19 as an open draft and use this report as its review companion. Do not mark the RTM, workflow specification, offline specification, API contract or acceptance plan Accepted yet.

The next implementation of this audit should be a bounded documentation reconciliation on the existing PR #19 branch:
1. refresh source revision references while preserving the historical snapshots;
2. add ODR-01 / EVT traceability;
3. clarify the Observation “received” state boundary;
4. record the identity mapping as unresolved pending owner boundary direction;
5. prepare the PR #20 source-inventory refresh as a separate follow-up on its existing branch.

The project owner remains the decision authority. This report is an audit recommendation, not approval to change accepted ADRs, scientific models, product scope, merge PRs or retire branches.

**End of audit — STF-BI-AUD-PR19-001 v0.1.**

---

## 10. Follow-up finding disposition — 23 November 2026

**Status:** Dated follow-up to the original v0.1 audit. The original findings and their historical source snapshots are preserved. This addendum records later documentation changes and current residual gaps; it does not retroactively rewrite the original audit or confer approval.

| Finding | Follow-up disposition |
|---|---|
| PR19-AUD-01 — identity/authentication mapping | **Addressed at documentation level.** The current RTM classifies identity/access foundations as an STF shared-platform cross-cutting concern without assigning an unrelated BI-CAP identifier. This is not final approval of the wider STF/Botanica ownership boundary or an architecture baseline. |
| PR19-AUD-02 — stale source SHAs | **Partially addressed.** The RTM source snapshot and some linked proposals have been refreshed. Remaining stale references were found in the PR #20 architecture inventory and the Task 03–04 readiness audit; these are being corrected in the same documentation reconciliation. Historical SHAs remain historical evidence, not current identifiers. |
| PR19-AUD-03 — ODR-01 / EVT traceability | **Addressed at proposal/documentation level.** RTM, workflow crosswalk v0.2, offline specification v0.2 and API contract v0.2 now record export-only safeguards and EVT-27–EVT-44 relationships. The validation cases remain Proposed / Not run; no final export profile or implementation is approved. |
| PR19-AUD-04 — Observation “received” ambiguity | **Clarified as a proposal.** Workflow lifecycle v0.2 proposes `record_created` for the committed Observation domain record and keeps `server_received` as command-receipt terminology. Owner, product, scientific and API review remains outstanding; no lifecycle is approved or implemented. |
| PR19-AUD-05 — STF/Botanica boundary | **Partially addressed.** The operating prompt and proposed documents distinguish reusable STF infrastructure from Botanica-owned botanical scientific capabilities. Further ownership of shared primitives, organizational boundaries and deployment topology remains open; ADR-011 remains Proposed. |
| PR19-AUD-06 — Task 04 citation tokens | **Open.** The source-preserving Task 04 transcription retains its historical citation tokens. A future canonical revision or dated reference overlay must provide durable source references without silently rewriting the transcription. |
| PR19-AUD-07 — acceptance/workflow tests | **Open validation gate.** The 66 acceptance cases and workflow scenarios remain proposed and unexecuted. No test result or release acceptance is claimed. |
| PR19-AUD-08 — offline/API decisions | **Partially addressed.** Offline and API specifications exist at v0.2, but API-OD-01–20 and OFF-OD-01–16 remain open; specialist review and executable validation remain outstanding. |
| PR19-AUD-09 — PR #20 architecture inventory | **Partially addressed.** The architecture plan has a refreshed inventory, but the current file still contains a stale RTM SHA, a duplicate workflow lifecycle row, contradictory branch-count wording and reversed §2.3/§2.4 ordering. The roadmap also contains stale PR #20 mergeability and comparison metadata. These are the subject of the companion PR #20 corrections. |

### 10.1 Revalidated source revisions

| Document | Ref | Current blob SHA | Status |
|---|---|---|---|
| Operating prompt v1.0 | `docs/repository-audit-and-ai-operating-standard` | `53add3894d0502827e584614c70ad09cadaa637d` | Governing working prompt under user instruction; PR #16 remains open draft |
| RTM v0.3 | `docs/requirements-traceability-register` | `c4b4ef1a5adfd367edcf982c1f9b115fa5d8aad6` | Proposed; lifecycle and crosswalk sections require this follow-up correction |
| Workflow lifecycle v0.2 | `docs/requirements-traceability-register` | `498af08ec60e3626e8b60ab5047acae1a8861eb5` | Proposed; `record_created` / `server_received` distinction not approved |
| Workflow crosswalk v0.2 | `docs/requirements-traceability-register` | `61d2111ace5c408eaf503bdf17b2ccb822f90978` | Proposed; ODR-01 and EVT-27–EVT-44 mapped |
| Offline specification v0.2 | `docs/requirements-traceability-register` | `a46c7cc1de9d1ea5c5faed7574d23de1d1a48e13` | Proposed; validation unexecuted |
| API contract v0.2 | `docs/requirements-traceability-register` | `bc0f3e93ec6ef2d2c2039b56739db38296c03281` | Proposed; API-OD decisions remain open |
| Task 03–04 readiness audit | `docs/requirements-traceability-register` | `d01ec7041ca2571ae8c11c4a0d95816c7d2daa7c` | Proposed; follow-up section numbering and RTM SHA being corrected |
| PR #20 architecture plan v0.2 | `docs/full-system-architecture-and-repo-engineering-plan` | `33c42ead0d32f24530d28fdbcfd1024c2495a5eb` | Proposed; correction required |
| PR #20 roadmap v0.2 | `docs/full-system-architecture-and-repo-engineering-plan` | `2ec317a01a2d295b073c95ee8427d4e2d865635c` | Proposed; correction required |

### 10.2 Current repository and readiness boundary

- PR #19 remains open, draft and mergeable at head `d40f9c4d2e97e68d6b55bd86b1cb0df046136f2a`; PR #20 remains open, draft and mergeable at head `d1b9fc38fdc4777d7c522f8959437cc2e9171018`.
- The live repository has 23 branches against the seven-branch ceiling. No branch retirement is claimed in this addendum.
- Accepted ADR-001 through ADR-010 remain unchanged. ADR-011 remains Proposed.
- DR-01–DR-12 and LDM-01–LDM-16 remain scientific review/validation obligations. Task 05C remains unapproved; Task 05E remains not ready.
- EVT-27–EVT-44, OFF-001–OFF-036 and API-SYNC-001–042 remain proposed and unexecuted. API-OD-01–20 and OFF-OD-01–16 remain open.
- No physical schema, migration, production API, application implementation, legal opinion or independent specialist approval is established by these documents.

**Updated recommendation:** keep PR #19 and PR #20 open and draft. Complete the scoped documentation corrections, re-fetch and verify the resulting files, then seek owner and discipline review. Do not merge or retire any source branch until preservation, dependency and approval gates are separately satisfied.
