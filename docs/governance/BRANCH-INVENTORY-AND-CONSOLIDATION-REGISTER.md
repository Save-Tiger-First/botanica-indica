# Branch Inventory and Preservation-First Consolidation Register

**Audit date:** 20 November 2026  
**Repository:** Save-Tiger-First/botanica-indica  
**Status:** Verified snapshot and proposed disposition; no existing branch or pull request has been deleted, merged or retargeted by this audit  
**Related policy:** [Branching and Release Governance](BRANCHING-AND-RELEASE-GOVERNANCE.md)

## 1. Verified snapshot

The GitHub API returned 23 branches on 20 November 2026 after creation of PR #20:

- 1 permanent branch: `main`
- 2 intended long-lived supporting branches: `develop`, `staging`
- 20 additional topic/governance branches, including the temporary branches carrying the policy, audit, product, requirements, architecture and scientific workstreams

At audit time:
- `main` was the default branch, marked protected by GitHub, at `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`.
- `develop` and `staging` both existed at the same commit as `main`; GitHub reported both as unprotected.
- The repository had 17 open pull requests at the latest verification: #1–#5, #8, #9, #11–#20. PR #15 is ready for review; the other 16 are drafts. PRs #17–#20 add the full-product blueprint, source-preserving Task 03/04 baselines, requirements traceability register and full-system architecture plan.
- All supporting branches contain or carried task-specific commits/files relative to `main`; none should be deleted merely because it is not one of the three long-lived branches. Re-check every branch's current unique commits before retirement.

This is a dated snapshot. Re-fetch branches, pull requests and comparisons before acting on any disposition.

## 2. Long-lived branch status

| Branch | Verified commit | GitHub protected flag | Intended disposition |
|---|---|---|---|
| `main` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | true | Retain permanently; default and canonical branch |
| `develop` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | false | Retain as integration branch; configure protection |
| `staging` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | false | Retain as release-candidate branch; configure protection |

The GitHub protected flag is not a complete inspection of all effective settings. A prior branch-protection read returned an integration permission error. Therefore, detailed settings for `main` have not been independently verified in this audit.

## 3. Topic branch and pull-request register

| Branch | PR | Current PR base | Content / relationship | Proposed disposition |
|---|---:|---|---|---|
| `docs/asset-specific-licensing-policy` | #1 | `main` | Asset-specific licensing and IP policy; proposed, not approved | Preserve; obtain legal/IP and data-rights review; integrate only after review |
| `docs/adr-011-stf-ecosystem-boundaries` | #2 | `main` | Proposed ecosystem-boundary ADR | Preserve; review against existing ADRs and product boundaries |
| `docs/task-05-data-architecture` | #3 | `main` | Task 05 data architecture | Preserve; review as the parent scientific data architecture baseline |
| `docs/task-05-data-dictionary` | #4 | `main` | Task 05B scientific dictionary and Indian test cases | Preserve; reconcile with Task 05 and source authority/evidence classes |
| `docs/task-05c-logical-data-model` | #5 | `main` | Task 05C logical model; current principal review branch | Preserve; resolve blocking scientific model findings before approval |
| `docs/task-05d-logical-model-validation-v3` | #11 | `docs/task-05c-logical-data-model` | Task 05D validation; explicitly stacked on PR #5 | Preserve; do not retarget or merge before its Task 05C dependency is resolved |
| `review/scientific-data-model-review-pack` | #9 | `main` | Scientific review pack and validation/decision register | Preserve; use as a review instrument; do not treat desk review as external expert approval |
| `strategy/naturetech-biodiversity-conservation-impact` | #8 | `main` | STF NatureTech and conservation strategy | Preserve; strategy remains proposed pending governance and evidence review |
| `governance/stf-organisational-readiness-review` | #12 | `strategy/naturetech-biodiversity-conservation-impact` | Organisational readiness review plus updated strategy materials; stacked on PR #8 | Preserve; resolve after PR #8 in dependency order; no organisational readiness conclusion is implied |
| `proposal/bengaluru-urban-biodiversity-feasibility-pilot` | #13 | `main` | Proposed 12-week feasibility/baseline pilot; not an approved programme | Preserve; partner, authority, budget, scientific and governance gates remain |
| `research/bengaluru-pilot-site-selection` | #14 | `main` | Preliminary site assessment; no site selected | Preserve; reconcile candidate recommendation with pilot proposal and verify current permissions/custody |
| `governance/branch-lifecycle-policy` | #15 | `develop` | Branch lifecycle policy, pull request template and consolidation register | Temporary policy branch; retain until PR #15 is reviewed and resolved, then delete after verifying merge/closure |
| `docs/repository-audit-and-ai-operating-standard` | #16 | `develop` | Repository/Markdown audit, permanent AI operating prompt, ADR Markdown fixes, README correction and governance workflow | Temporary audit branch; retain until PR #16 is reviewed and resolved, then delete after verifying merge/closure |
| `docs/full-product-vision-capability-blueprint` | #17 | `develop` | Proposed full-product capability blueprint | Preserve as the product-scope proposal; review with PRs #18–#20 |
| `docs/canonical-task-03-04-baselines` | #18 | `develop` | Source-preserving Task 03 PRD and Task 04 architecture transcriptions | Preserve originals; reconcile without silently replacing source documents |
| `docs/requirements-traceability-register` | #19 | `develop` | Proposed capability/requirement/ADR/science/test traceability register | Review with PRs #17, #18 and #20; not an approved requirements baseline |
| `docs/full-system-architecture-and-repo-engineering-plan` | #20 | `develop` | Proposed full system architecture, target repo structure and 200-line guideline | Review against accepted ADRs, PRD, Blueprint, RTM and scientific gates; not implementation authorization |

## 4. Orphaned or superseded branches requiring content reconciliation

These branches had no corresponding open pull request in the verified snapshot. They are not safe to delete until their unique content is reconciled.

### 4.1 `docs/task-05c-logical-database-model`

- Commit: `8d4fef2d726aac79dd684856d924b171e44d0b93`
- One unique added file: `docs/data-architecture/TASK-05C-LOGICAL-DATABASE-MODEL-AND-SCIENTIFIC-RELATIONSHIPS.md` (647 lines in the compare summary).
- PR #5 instead carries a different Task 05C file path: `docs/architecture/TASK-05C-LOGICAL-DATABASE-MODEL.md`.
- Recommendation: compare the two complete models section by section, identify unique scientific semantics and decisions, and reconcile into one canonical Task 05C document. Do not merge both wholesale and do not delete this branch until the comparison is signed off.

### 4.2 `docs/task-05d-logical-model-validation`

- Commit: `3efd80e5e28b2a916e63c85808ef3aba9d35e4ac`
- Adds a Task 05C document and a Task 05D validation document.
- The Task 05D file differs from the v2/v3 copy (29,326 characters versus 29,512 characters in the retrieved versions).
- Recommendation: inspect its unique changes against v3, record any retained findings, and then mark as superseded if no unique required material remains.

### 4.3 `docs/task-05d-logical-model-validation-v2`

- Commit: `76bd88980bb2536db63bbde76e3fa687503bdda1`
- The retrieved Task 05D file is byte-for-byte identical to the v3 Task 05D file.
- However, comparison of v2 and v3 reports divergent branch histories (two commits ahead and two behind) and a difference in the separate Task 05C model file.
- Recommendation: compare the Task 05C file and commit history against v3. Preserve any unique required decisions; otherwise mark v2 superseded by v3.

### 4.4 `docs/task-05d-logical-model-validation-v3`

- This is not orphaned: it is the head branch for open PR #11.
- Recommendation: retain until PR #11 and its dependency on PR #5 are fully resolved.

## 5. Critical dependency and content risks

1. **Task 05C / 05D:** PR #11 is based on PR #5. The latest compare on 20 November 2026 shows the PR #11 head is **3 commits ahead and 1 behind** the PR #5 branch; synchronize and re-review the complete diff before merge. The PR #9 decision register reports DR-01 to DR-07 as document-level revisions in proposed materials, DR-08 as an open source/geographic-scope test case, DR-09 as open following a TDWG metadata retrieval conflict, and DR-10 to DR-12 as document-level revisions still requiring specialist review. These are not validated closures: reproducible fixtures, standards round-trip tests and independent discipline review remain outstanding. Resolve the competing Task 05C document and the PR #5/#11 dependency before authorizing physical design.
2. **NatureTech / organisational readiness:** PR #12 is based on PR #8. The latest compare on 20 November 2026 shows the PR #12 head is **4 commits ahead and 3 behind** the PR #8 branch. It also includes overlapping strategy material. Reconcile the divergence and compare repeated files; resolve #8 before #12.
3. **Bengaluru pilot:** PR #14 is related to PR #13 but currently targets `main` independently. The site-selection document must remain preliminary. Reconcile its current Kaikondrahalli-first recommendation with the proposal's non-selection status and all later partner/authority evidence before any site decision.
4. **Scientific review pack:** PR #9 is a review instrument and should not be represented as independent expert approval. Its current source revision also records Task 05E as NOT READY and requires real reviewer identities, qualifications, evidence and outcomes before sign-off.
5. **Licensing and ecosystem governance:** PRs #1 and #2 are proposals. Do not describe them as approved policy or ADRs until reviewed and merged through the agreed governance process.
6. **Legacy PR routing transition:** PRs #1–#5, #8, #9, #13 and #14 currently target `main`, while the proposed branch policy and PR #16 routing check require normal task work to target `develop` and only a `staging` promotion to target `main`. Do not merge these legacy PRs directly merely because they are open. Review each dependency and diff, then obtain an explicit owner-approved retarget/closure plan. The current routing script also does not allow the existing `proposal/`, `strategy/` or `review/` prefixes for PRs into `develop`; reconcile those naming exceptions before enforcing the check on all workstreams.

## 6. Recommended consolidation sequence

This is a preservation-first sequence, not authorization to merge:

1. Review and adopt the branch lifecycle policy PR #15. If accepted, the repository has a written operating rule.
2. Review PR #3 (Task 05 architecture), then PR #4 (Task 05B), and reconcile the competing Task 05C documents before finalizing PR #5.
3. Resolve DR-01 to DR-12 and the LDM test scenarios; update the review pack and decision register. Only then resolve PR #11.
4. Review PR #8, then PR #12 in its stacked dependency order.
5. Review PRs #13 and #14 together, preserving the no-site-selected/no-fieldwork-authorized position until gates are satisfied.
6. Review PRs #1 and #2 through the appropriate legal, governance and architecture review.
7. After each PR is merged or closed, verify that its content is on the intended integration branch and delete its temporary branch only after confirming no unique required commits remain.
8. Promote a coherent release candidate from `develop` to `staging`, validate it, and then promote to `main` through reviewed PRs.
9. Repeat branch inventory until only `main`, `develop` and `staging` remain as active long-lived branches, with no unnecessary topic branches.
10. At project completion, apply the formal completion gates in the Branching and Release Governance policy and retire both supporting branches.

## 7. Explicit non-actions in this audit

- No existing topic branch was deleted.
- No existing pull request was merged, closed or retargeted.
- No branch-protection or ruleset settings were changed.
- No proposal, ADR, scientific model or pilot was approved.
- No external expert, legal or institutional review is claimed.

## 8. Evidence sources

This register was refreshed against GitHub API branch and pull-request listings and direct document retrieval on 20 November 2026. Latest snapshot: 23 branches (3 designated long-lived, 20 topic/workstream); 17 open PRs. `main`, `develop` and `staging` are identical at `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`. Re-run branch, PR and comparison checks immediately before any merge, retarget, archive or deletion action.
