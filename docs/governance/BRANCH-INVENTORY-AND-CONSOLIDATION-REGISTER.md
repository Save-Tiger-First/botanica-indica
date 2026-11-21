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
- The repository had **20 open pull requests** at the latest verification: #1–#5, #8, #9, #11–#23. PR #15 is ready for review; the other 19 are drafts. PRs #21–#23 were opened as preservation/reconciliation PRs from the three formerly unassociated Task 05C/05D branches into the existing PR #9 review branch. They do not approve the scientific models or authorize physical design.
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

## 4. Superseded Task 05C/05D branches requiring content reconciliation

The following three branches had no associated open PR before the current cleanup action. Draft preservation PRs #21–#23 now provide reviewable paths into the existing scientific review branch. They remain unsafe to retire until their unique content is reconciled and the relevant PRs are reviewed and resolved.

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
- **Correction from the earlier inventory:** the retrieved Task 05D v2 and v3 files are not byte-for-byte identical. Their blob SHAs differ: v2 `acf446b1bf0204fa0400621711603ab23cc80ff2` (29,512 characters) and v3 `cf0b9c10bcb2da7b102e52688f22bd8e8b69bb91` (31,197 characters).
- Their Task 05C model files also differ: v2 `71d682da0c495b4497b6e01895ca2b75fccc3824` (43,627 characters) and v3 `e6131e867d4bc3dbc58aa1188d0fabc895429347` (44,118 characters).
- Therefore, v2 must not be classified as a byte-identical duplicate or retired on that assumption. Compare both Task 05C and Task 05D content section by section, preserve unique findings and decision provenance, and only then determine whether v2 can be marked superseded.

### 4.4 `docs/task-05d-logical-model-validation-v3`

- This is not orphaned: it is the head branch for open PR #11.
- Recommendation: retain until PR #11 and its dependency on PR #5 are fully resolved.

## 4.5 Immediate seven-branch target and current retirement status — 20 November 2026

The project owner has explicitly directed that the repository be reduced to **no more than seven branches total, including temporary branches**, immediately, with no new branch creation. The seven comprise the three long-lived branches plus at most four temporary workstream branches.

**Latest verified position after opening preservation PRs #21–#23:**
- Total branches: **23** = 3 long-lived + 20 temporary.
- Open PRs: **20** = #1–#5, #8, #9, #11–#23.
- All 20 PRs remain open and unmerged. PR #15 is ready for review; the other 19 are drafts.
- The three previously unassociated branches now have preservation PRs #21–#23. The branch count has **not** fallen.
- No branch was created, merged, closed or deleted during this update.

### Four provisional retained workstream branches

| Retained branch | Existing PR | Consolidation scope | Conditions |
|---|---:|---|---|
| `docs/repository-audit-and-ai-operating-standard` | #16 | AI operating prompt, repository audit, branch governance, licensing/IP policy proposal and ecosystem-boundary proposal | Keep PR #16's prompt version authoritative until PR #16 is accepted and merged. Reconcile PR #15 governance documents and PRs #1/#2 proposals only after consistency review. Consolidation is not policy/ADR approval. |
| `docs/full-system-architecture-and-repo-engineering-plan` | #20 | Full Product Blueprint, Task 03/04 source-preserving baselines, Requirements Traceability Register and system architecture | Reconcile PRs #17–#20; preserve Task 03/04 source provenance and accepted ADR constraints. |
| `review/scientific-data-model-review-pack` | #9 | Task 05 architecture, Task 05B dictionary/test cases, Task 05C competing models, Task 05D validation and scientific review/decision records | Reconcile PRs #3/#4/#5/#11/#21/#22/#23. Do not close scientific findings or authorize physical design through consolidation. |
| `strategy/naturetech-biodiversity-conservation-impact` | #8 | STF strategy, organisational readiness, Bengaluru feasibility proposal and site-selection research | Reconcile PRs #8/#12/#13/#14; preserve preliminary/no-site-selected/no-fieldwork-authorized status. |

These are the proposed four workstream destinations. They are not approvals to merge, close or delete. If a destination cannot safely preserve the source material, stop and report the specific conflict rather than discarding content.

### Three preservation PRs opened on existing branches

| PR | Existing head branch | Destination | Purpose |
|---|---|---|---|
| [#21](https://github.com/Save-Tiger-First/botanica-indica/pull/21) | `docs/task-05c-logical-database-model` | `review/scientific-data-model-review-pack` | Preserve and compare the alternate 647-line Task 05C proposal against PR #5 |
| [#22](https://github.com/Save-Tiger-First/botanica-indica/pull/22) | `docs/task-05d-logical-model-validation` | `review/scientific-data-model-review-pack` | Preserve earlier Task 05C/05D content and identify unique findings |
| [#23](https://github.com/Save-Tiger-First/botanica-indica/pull/23) | `docs/task-05d-logical-model-validation-v2` | `review/scientific-data-model-review-pack` | Preserve v2 content, reconcile Task 05C differences and prevent the superseded DR-09 closure claim being reused |

All three PRs are draft, open and unmerged. They use existing branches; no new branch was created. They are review and preservation mechanisms, not permission to merge.

### Retirement/consolidation register

| Source branch | PR | Proposed destination | Retirement gate |
|---|---:|---|---|
| `governance/branch-lifecycle-policy` | #15 | PR #16 branch | Transfer and verify both governance documents and their complete histories/references; resolve PR #15 and retire its head branch only after approval |
| `docs/asset-specific-licensing-policy` | #1 | PR #16 branch | Preserve policy proposal and legal-review caveats; do not imply approval |
| `docs/adr-011-stf-ecosystem-boundaries` | #2 | PR #16 branch | Preserve as proposed ADR; review against accepted ADRs |
| `docs/task-05-data-architecture` | #3 | PR #9 branch | Reconcile Task 05 architecture content and dependencies |
| `docs/task-05-data-dictionary` | #4 | PR #9 branch | Preserve dictionary, source authority distinctions and Indian botanical test cases |
| `docs/task-05c-logical-data-model` | #5 | PR #9 branch | Preserve current Task 05C proposal and PR #11 dependency evidence |
| `docs/task-05d-logical-model-validation-v3` | #11 | PR #9 branch | Preserve latest validation findings and DR/LDM status; resolve stacked dependency |
| `docs/task-05c-logical-database-model` | #21 | PR #9 branch | Compare competing 05C model; preserve unique valid semantics before retirement |
| `docs/task-05d-logical-model-validation` | #22 | PR #9 branch | Reconcile unique validation content; superseded material must be explicitly recorded |
| `docs/task-05d-logical-model-validation-v2` | #23 | PR #9 branch | Preserve any unique Task 05C material; do not carry forward withdrawn DR-09 conclusion |
| `docs/full-product-vision-capability-blueprint` | #17 | PR #20 branch | Preserve complete capability map and product boundaries |
| `docs/canonical-task-03-04-baselines` | #18 | PR #20 branch | Preserve exact source transcriptions and provenance |
| `docs/requirements-traceability-register` | #19 | PR #20 branch | Reconcile identifiers and source-to-acceptance traceability |
| `governance/stf-organisational-readiness-review` | #12 | PR #8 branch | Resolve stacked divergence; preserve findings as proposals |
| `proposal/bengaluru-urban-biodiversity-feasibility-pilot` | #13 | PR #8 branch | Preserve feasibility-only scope and all approval gates |
| `research/bengaluru-pilot-site-selection` | #14 | PR #8 branch | Preserve research evidence; do not declare a site selected |

### Required PR-based retirement sequence

1. Inspect each source branch's complete diff, unique commits, files and dependent PRs against the latest live target.
2. Reconcile required content into the specified existing destination branch. Use only existing branches; do not create a branch.
3. Verify that the destination contains required content, citations, provenance, statuses and decision history. Fetch and compare exact file contents and SHAs.
4. Use each source branch's existing PR. For branches without an open PR, create a preservation PR from that existing head to an existing retained destination only where a meaningful reviewable diff remains.
5. Obtain review and explicit approval before merging. After merge, delete that PR's own head branch only when no other open PR references it. If work is rejected or obsolete, record the reason, close the PR with approval, then delete its head branch.
6. Resolve dependent PRs before deleting any branch they use as a base.
7. Re-fetch the complete live branch list after each retirement wave. Do not claim the target is achieved until exactly seven or fewer branches are verified.

**GitHub rule:** A branch associated with an open PR cannot be deleted via the PR's Delete branch action. The PR must first be merged or closed, and no other open PR may reference the branch. GitHub documents the supported process here: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/deleting-and-restoring-branches-in-a-pull-request

**Status:** The seven-branch plan is recorded, and preservation PRs #21–#23 have been opened. No PR has been merged or closed and no branch has been deleted. The live branch count remains **23**. Achieving seven requires resolving and retiring 16 temporary branches; this cannot be truthfully described as completed yet.

## 5. Critical dependency and content risks

1. **Task 05C / 05D:** PR #11 is based on PR #5. The latest compare on 20 November 2026 shows the PR #11 head is **3 commits ahead and 1 behind** the PR #5 branch; synchronize and re-review the complete diff before merge. The PR #9 decision register reports DR-01 to DR-07 as document-level revisions in proposed materials, DR-08 as an open source/geographic-scope test case, DR-09 as open following a TDWG metadata retrieval conflict, and DR-10 to DR-12 as document-level revisions still requiring specialist review. These are not validated closures: reproducible fixtures, standards round-trip tests and independent discipline review remain outstanding. Resolve the competing Task 05C document and the PR #5/#11 dependency before authorizing physical design.
2. **NatureTech / organisational readiness:** PR #12 is based on PR #8. The latest compare on 20 November 2026 shows the PR #12 head is **4 commits ahead and 3 behind** the PR #8 branch. It also includes overlapping strategy material. Reconcile the divergence and compare repeated files; resolve #8 before #12.
3. **Bengaluru pilot:** PR #14 is related to PR #13 but currently targets `main` independently. The site-selection document must remain preliminary. Reconcile its current Kaikondrahalli-first recommendation with the proposal's non-selection status and all later partner/authority evidence before any site decision.
4. **Scientific review pack:** PR #9 is a review instrument and should not be represented as independent expert approval. Its current source revision also records Task 05E as NOT READY and requires real reviewer identities, qualifications, evidence and outcomes before sign-off.
5. **Licensing and ecosystem governance:** PRs #1 and #2 are proposals. Do not describe them as approved policy or ADRs until reviewed and merged through the agreed governance process.
6. **Legacy PR routing transition:** PRs #1–#5, #8, #9, #13 and #14 currently target `main`, while the proposed branch policy and PR #16 routing check require normal task work to target `develop` and only a `staging` promotion to target `main`. Do not merge these legacy PRs directly merely because they are open. Review each dependency and diff, then obtain an explicit owner-approved retarget/closure plan. The current routing script also does not allow the existing `proposal/`, `strategy/` or `review/` prefixes for PRs into `develop`; reconcile those naming exceptions before enforcing the check on all workstreams.

## 6. Recommended consolidation sequence

This is a preservation-first sequence, not authorization to merge:

1. Review PRs #15 and #16 as the connected governance baseline. PR #15 defines the exact three-long-lived-branch policy; PR #16 carries the operating prompt, audit and initial automation. Do not merge either without owner review.
2. Review PRs #17–#20 as one connected product/architecture package: Full Product Blueprint, source-preserving Task 03/04 baselines, Requirements Traceability Register and Full System Architecture Plan. Reconcile scope, requirements, architecture and technology decision status.
3. Review PR #3 (Task 05 architecture), then PR #4 (Task 05B), and reconcile the competing Task 05C documents before finalizing PR #5.
4. Resolve DR-01 to DR-12 and the LDM test scenarios; update the review pack and decision register. Only then resolve PR #11, after synchronizing its 3-ahead/1-behind dependency with PR #5.
5. Review PR #8, then PR #12 in its stacked dependency order; reconcile the current 4-ahead/3-behind divergence before merge.
6. Review PRs #13 and #14 together, preserving the no-site-selected/no-fieldwork-authorized position until gates are satisfied.
7. Review PRs #1 and #2 through the appropriate legal, governance and architecture review.
8. Reconcile legacy PR routing: PRs #1–#5, #8, #9, #13 and #14 currently target `main`; retarget only after an explicit dependency/diff review and owner authorization. Do not merge these directly to make progress faster.
9. After each PR is merged or closed, verify that its content is on the intended integration branch and delete its temporary branch only after confirming no unique required commits remain.
10. Promote a coherent release candidate from `develop` to `staging`, validate it, and then promote to `main` through reviewed PRs.
11. Repeat branch inventory until only `main`, `develop` and `staging` remain as active long-lived branches, with no unnecessary topic branches.
12. At project completion, apply the formal completion gates in the Branching and Release Governance policy and retire both supporting branches.

## 7. Explicit non-actions in this audit

- No existing topic branch was deleted.
- No existing pull request was merged, closed or retargeted.
- No branch-protection or ruleset settings were changed.
- No proposal, ADR, scientific model or pilot was approved.
- No external expert, legal or institutional review is claimed.

## 8. Evidence sources

This register was refreshed against GitHub API branch and pull-request listings and direct document retrieval on 20 November 2026. Latest snapshot: 23 branches (3 designated long-lived, 20 topic/workstream); 20 open PRs (#1–#5, #8, #9, #11–#23), including preservation PRs #21–#23. `main`, `develop` and `staging` are identical at `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`. Re-run branch, PR and comparison checks immediately before any merge, retarget, archive or deletion action.


---

## 10. Live repository snapshot — 21 November 2026, after PR #16 governance remediation

This is the latest verified inventory snapshot fetched from the GitHub API after the governance remediation and its successful CI run.

- **Total branches:** 23 (3 designated long-lived branches and 20 temporary/workstream branches).
- **Open PRs:** 20 (#1–#5, #8, #9, #11–#23).
- **PR #16:** open draft, base `develop`, head `docs/repository-audit-and-ai-operating-standard`, current head `a3b73f75ae4ff175796bbc2eb2f7c9f5c38047e3`.
- **Long-lived branch tips:** `main`, `develop` and `staging` remain at `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`.
- **No lifecycle action:** no PR was merged, closed or retargeted; no branch was created, renamed or deleted.

### 10.1 All live branch tips

| Branch | Current tip SHA |
|---|---|
| `develop` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` |
| `docs/adr-011-stf-ecosystem-boundaries` | `e900b64c90df08f5c98181af54bf2ab0b7096759` |
| `docs/asset-specific-licensing-policy` | `15fd4edef9afa8d22df9e23f66296ef09423d8cf` |
| `docs/canonical-task-03-04-baselines` | `0f908f8221ad3434cc84fe2cd41b735aad0a752a` |
| `docs/full-product-vision-capability-blueprint` | `234b21846db53e7dbac9b8e8f4ccad2b6c3012ff` |
| `docs/full-system-architecture-and-repo-engineering-plan` | `b6081cafb4df8a4c2b250a0054908bcdd001f3f9` |
| `docs/repository-audit-and-ai-operating-standard` | `a3b73f75ae4ff175796bbc2eb2f7c9f5c38047e3` |
| `docs/requirements-traceability-register` | `5c4570df6c51bbb9c28fa826f04e57435f784761` |
| `docs/task-05-data-architecture` | `2b02ab3cd115691841889ed77d453b31ab0bed16` |
| `docs/task-05-data-dictionary` | `71444caa3cee16a0c5afd33f70aabf11e90a6b37` |
| `docs/task-05c-logical-data-model` | `27d905c26217cc127de63449ce342d3bf2723016` |
| `docs/task-05c-logical-database-model` | `8d4fef2d726aac79dd684856d924b171e44d0b93` |
| `docs/task-05d-logical-model-validation` | `3efd80e5e28b2a916e63c85808ef3aba9d35e4ac` |
| `docs/task-05d-logical-model-validation-v2` | `76bd88980bb2536db63bbde76e3fa687503bdda1` |
| `docs/task-05d-logical-model-validation-v3` | `1bcbb46890788b0296884228e44c867965bc8381` |
| `governance/branch-lifecycle-policy` | `633105210d3a6c4c8e36287ed2dc44dee23f61ef` |
| `governance/stf-organisational-readiness-review` | `bd5b18fe5d68f50e25f0453eb792d0c44bc700d0` |
| `main` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` |
| `proposal/bengaluru-urban-biodiversity-feasibility-pilot` | `7f7a3be03d68d5595465279ad22407ea983f046e` |
| `research/bengaluru-pilot-site-selection` | `ee71dc0da319e7b3c69572f9c6f015298e3c8c2e` |
| `review/scientific-data-model-review-pack` | `1be0975e457d56152ad57a1cd6bb5d941328fbda` |
| `staging` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` |
| `strategy/naturetech-biodiversity-conservation-impact` | `9d76328df8112922df818f01c27e297b3ee1b76a` |

### 10.2 All open PR relationships

| PR | Base | Head | Head SHA | Draft/review state |
|---:|---|---|---|---|
| #1 | `main` | `docs/asset-specific-licensing-policy` | `15fd4edef9afa8d22df9e23f66296ef09423d8cf` | Draft |
| #2 | `main` | `docs/adr-011-stf-ecosystem-boundaries` | `e900b64c90df08f5c98181af54bf2ab0b7096759` | Draft |
| #3 | `main` | `docs/task-05-data-architecture` | `2b02ab3cd115691841889ed77d453b31ab0bed16` | Draft |
| #4 | `main` | `docs/task-05-data-dictionary` | `71444caa3cee16a0c5afd33f70aabf11e90a6b37` | Draft |
| #5 | `main` | `docs/task-05c-logical-data-model` | `27d905c26217cc127de63449ce342d3bf2723016` | Draft |
| #8 | `main` | `strategy/naturetech-biodiversity-conservation-impact` | `9d76328df8112922df818f01c27e297b3ee1b76a` | Draft |
| #9 | `main` | `review/scientific-data-model-review-pack` | `1be0975e457d56152ad57a1cd6bb5d941328fbda` | Draft |
| #11 | `docs/task-05c-logical-data-model` | `docs/task-05d-logical-model-validation-v3` | `1bcbb46890788b0296884228e44c867965bc8381` | Draft |
| #12 | `strategy/naturetech-biodiversity-conservation-impact` | `governance/stf-organisational-readiness-review` | `bd5b18fe5d68f50e25f0453eb792d0c44bc700d0` | Draft |
| #13 | `main` | `proposal/bengaluru-urban-biodiversity-feasibility-pilot` | `7f7a3be03d68d5595465279ad22407ea983f046e` | Draft |
| #14 | `main` | `research/bengaluru-pilot-site-selection` | `ee71dc0da319e7b3c69572f9c6f015298e3c8c2e` | Draft |
| #15 | `develop` | `governance/branch-lifecycle-policy` | `633105210d3a6c4c8e36287ed2dc44dee23f61ef` | Ready for review |
| #16 | `develop` | `docs/repository-audit-and-ai-operating-standard` | `a3b73f75ae4ff175796bbc2eb2f7c9f5c38047e3` | Draft |
| #17 | `develop` | `docs/full-product-vision-capability-blueprint` | `234b21846db53e7dbac9b8e8f4ccad2b6c3012ff` | Draft |
| #18 | `develop` | `docs/canonical-task-03-04-baselines` | `0f908f8221ad3434cc84fe2cd41b735aad0a752a` | Draft |
| #19 | `develop` | `docs/requirements-traceability-register` | `5c4570df6c51bbb9c28fa826f04e57435f784761` | Draft |
| #20 | `develop` | `docs/full-system-architecture-and-repo-engineering-plan` | `b6081cafb4df8a4c2b250a0054908bcdd001f3f9` | Draft |
| #21 | `review/scientific-data-model-review-pack` | `docs/task-05c-logical-database-model` | `8d4fef2d726aac79dd684856d924b171e44d0b93` | Draft |
| #22 | `review/scientific-data-model-review-pack` | `docs/task-05d-logical-model-validation` | `3efd80e5e28b2a916e63c85808ef3aba9d35e4ac` | Draft |
| #23 | `review/scientific-data-model-review-pack` | `docs/task-05d-logical-model-validation-v2` | `76bd88980bb2536db63bbde76e3fa687503bdda1` | Draft |

### 10.3 Governance workstream status

The PR #16 governance remediation is implemented on the existing branch and the current PR #16 head passed workflow run [44875559325](https://github.com/Save-Tiger-First/botanica-indica/actions/runs/44875559325). This does not make PR #16 approved or ready for merge.
The immediate seven-branch ceiling remains unmet. The live inventory still contains 23 branches, including 20 temporary/workstream branches. The four proposed retained workstream destinations remain provisional; no source PR has been merged or closed and no branch has been retired. Continue preservation-first reconciliation in dependency order and obtain the required approvals before any retirement action.


---

## 11. Live repository snapshot — 21 November 2026, after standards-currentness updates

Fetched from the GitHub API after the three scientific review documents were updated and verified.

- Total branches: **23**.
- Open pull requests: **20**.
- PR #9: open, draft, base `undefined`, head `undefined`, head SHA `undefined`.
- PR #16: open, draft, base `undefined`, head `undefined`, head SHA `undefined`.
- No branch was created, deleted or renamed. No PR was merged, closed or retargeted.

### 11.1 Live branch tips

| Branch | Current tip SHA |
|---|---|
| `develop` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` |
| `docs/adr-011-stf-ecosystem-boundaries` | `e900b64c90df08f5c98181af54bf2ab0b7096759` |
| `docs/asset-specific-licensing-policy` | `15fd4edef9afa8d22df9e23f66296ef09423d8cf` |
| `docs/canonical-task-03-04-baselines` | `0f908f8221ad3434cc84fe2cd41b735aad0a752a` |
| `docs/full-product-vision-capability-blueprint` | `d07bf52e0c6d4fd5c089e828b0f5b9af33dcd300` |
| `docs/full-system-architecture-and-repo-engineering-plan` | `9fb57b9aabe526808352a51fa9c87ecdbf2cd585` |
| `docs/repository-audit-and-ai-operating-standard` | `33a4a1d7d1c8264187b2aa0840c8c18029b8ce7b` |
| `docs/requirements-traceability-register` | `01ec0d356fa5db2da5469b89955764eb9e11b0f6` |
| `docs/task-05-data-architecture` | `2b02ab3cd115691841889ed77d453b31ab0bed16` |
| `docs/task-05-data-dictionary` | `71444caa3cee16a0c5afd33f70aabf11e90a6b37` |
| `docs/task-05c-logical-data-model` | `27d905c26217cc127de63449ce342d3bf2723016` |
| `docs/task-05c-logical-database-model` | `8d4fef2d726aac79dd684856d924b171e44d0b93` |
| `docs/task-05d-logical-model-validation` | `3efd80e5e28b2a916e63c85808ef3aba9d35e4ac` |
| `docs/task-05d-logical-model-validation-v2` | `76bd88980bb2536db63bbde76e3fa687503bdda1` |
| `docs/task-05d-logical-model-validation-v3` | `1bcbb46890788b0296884228e44c867965bc8381` |
| `governance/branch-lifecycle-policy` | `633105210d3a6c4c8e36287ed2dc44dee23f61ef` |
| `governance/stf-organisational-readiness-review` | `bd5b18fe5d68f50e25f0453eb792d0c44bc700d0` |
| `main` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` |
| `proposal/bengaluru-urban-biodiversity-feasibility-pilot` | `7f7a3be03d68d5595465279ad22407ea983f046e` |
| `research/bengaluru-pilot-site-selection` | `ee71dc0da319e7b3c69572f9c6f015298e3c8c2e` |
| `review/scientific-data-model-review-pack` | `2968572d394ca11b8b46a0191fd7e409220a5e22` |
| `staging` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` |
| `strategy/naturetech-biodiversity-conservation-impact` | `9d76328df8112922df818f01c27e297b3ee1b76a` |

### 11.2 Live open PR relationships

| PR | Base | Head | Head SHA | Review state |
|---:|---|---|---|---|
| #23 | `review/scientific-data-model-review-pack` | `docs/task-05d-logical-model-validation-v2` | `76bd88980bb2536db63bbde76e3fa687503bdda1` | Draft |
| #22 | `review/scientific-data-model-review-pack` | `docs/task-05d-logical-model-validation` | `3efd80e5e28b2a916e63c85808ef3aba9d35e4ac` | Draft |
| #21 | `review/scientific-data-model-review-pack` | `docs/task-05c-logical-database-model` | `8d4fef2d726aac79dd684856d924b171e44d0b93` | Draft |
| #20 | `develop` | `docs/full-system-architecture-and-repo-engineering-plan` | `9fb57b9aabe526808352a51fa9c87ecdbf2cd585` | Draft |
| #19 | `develop` | `docs/requirements-traceability-register` | `01ec0d356fa5db2da5469b89955764eb9e11b0f6` | Draft |
| #18 | `develop` | `docs/canonical-task-03-04-baselines` | `0f908f8221ad3434cc84fe2cd41b735aad0a752a` | Draft |
| #17 | `develop` | `docs/full-product-vision-capability-blueprint` | `d07bf52e0c6d4fd5c089e828b0f5b9af33dcd300` | Draft |
| #16 | `develop` | `docs/repository-audit-and-ai-operating-standard` | `33a4a1d7d1c8264187b2aa0840c8c18029b8ce7b` | Draft |
| #15 | `develop` | `governance/branch-lifecycle-policy` | `633105210d3a6c4c8e36287ed2dc44dee23f61ef` | Ready for review |
| #14 | `main` | `research/bengaluru-pilot-site-selection` | `ee71dc0da319e7b3c69572f9c6f015298e3c8c2e` | Draft |
| #13 | `main` | `proposal/bengaluru-urban-biodiversity-feasibility-pilot` | `7f7a3be03d68d5595465279ad22407ea983f046e` | Draft |
| #12 | `strategy/naturetech-biodiversity-conservation-impact` | `governance/stf-organisational-readiness-review` | `bd5b18fe5d68f50e25f0453eb792d0c44bc700d0` | Draft |
| #11 | `docs/task-05c-logical-data-model` | `docs/task-05d-logical-model-validation-v3` | `1bcbb46890788b0296884228e44c867965bc8381` | Draft |
| #9 | `main` | `review/scientific-data-model-review-pack` | `2968572d394ca11b8b46a0191fd7e409220a5e22` | Draft |
| #8 | `main` | `strategy/naturetech-biodiversity-conservation-impact` | `9d76328df8112922df818f01c27e297b3ee1b76a` | Draft |
| #5 | `main` | `docs/task-05c-logical-data-model` | `27d905c26217cc127de63449ce342d3bf2723016` | Draft |
| #4 | `main` | `docs/task-05-data-dictionary` | `71444caa3cee16a0c5afd33f70aabf11e90a6b37` | Draft |
| #3 | `main` | `docs/task-05-data-architecture` | `2b02ab3cd115691841889ed77d453b31ab0bed16` | Draft |
| #2 | `main` | `docs/adr-011-stf-ecosystem-boundaries` | `e900b64c90df08f5c98181af54bf2ab0b7096759` | Draft |
| #1 | `main` | `docs/asset-specific-licensing-policy` | `15fd4edef9afa8d22df9e23f66296ef09423d8cf` | Draft |

### 11.3 Standards-review documentation commits

The following append-only updates were committed on the existing `review/scientific-data-model-review-pack` branch and fetched again to verify the new blob SHA and addendum heading:

| File | Commit | Verified blob |
|---|---|---|
| `docs/reviews/EVENT-SURVEY-OCCURRENCE-CONCEPTUAL-MODEL-DECISION-PAPER.md` | `d39e244c16ee472d5ff09433e0e0eeeed7c63dd7` | `0feb63649328e438959a8e8b2927697aea7cbdab` |
| `docs/reviews/SCIENTIFIC-DATA-MODEL-VALIDATION-MATRIX-AND-DECISION-REGISTER.md` | `eb96a0d0e061a70f033b49ad334af7ce233b24b6` | `d890dce836f9694d8472c380f3ac617a1a75cd32` |
| `docs/reviews/TASK-05C-COMPETING-MODEL-RECONCILIATION.md` | `2968572d394ca11b8b46a0191fd7e409220a5e22` | `4762c2896645a7a020c72f8f863382119e0dede1` |

These are documentation updates, not scientific-model approvals, test executions, external specialist reviews or authorization to begin Task 05E. The seven-branch target remains unmet until the live list confirms seven or fewer.


### 11.4 Metadata correction to the snapshot narrative

The PR wrapper response used during preparation did not expose base/head fields, so the corresponding interpolated values in the first draft of Section 11 were not populated. This correction is based on direct GitHub REST pull-request objects:

- PR #9: `open`, draft `true`, base `main`, head `review/scientific-data-model-review-pack`, head SHA `2968572d394ca11b8b46a0191fd7e409220a5e22`.
- PR #16: `open`, draft `true`, base `develop`, head `docs/repository-audit-and-ai-operating-standard`, head SHA `8cb5530bdcc1960631bd70d639904f9cfa7759c0`.

The authoritative full branch and PR tables in Sections 11.1 and 11.2 are retained. Their data were fetched directly from the repository API. This correction does not change any branch or PR state.


### 11.5 Scientific-model addendum refresh — 21 November 2026

After Section 11.3 was first recorded, three further append-only updates were made to the scientific review documents to capture an additional blocking semantic issue: Darwin Core Conceptual Model §§2.2–2.3 describe Survey results through Occurrences reported by the Survey and allow an Occurrence to represent a taxon-specific non-detection; the GBIF survey guide places explicit absences at Occurrence level and prohibits absence assertions for bycatch. The new EVT-19–EVT-22 scenarios are proposals and remain Not tested.

Verified latest document blobs:
- Decision paper: `eb513cde11f3013c31102318c78e278bc274ec91`
- Validation matrix/decision register: `5eeff39d5362a70ca43b6711062742526b733dc1`
- Task 05C competing-model reconciliation: `eeb15a19f93df5b4feaee3b2b0481b24a59d3c23`

Current live repository counts: **23 branches** and **20 open PRs**.
- PR #9: `open`, draft `true`, base `main`, head `review/scientific-data-model-review-pack`, head SHA `5bc19c190687ffcfa602d8862edca58201b37ace`.
- PR #16: `open`, draft `true`, base `develop`, head `docs/repository-audit-and-ai-operating-standard`, head SHA `3e42ec6cd2021526663090b7419457893ddde87a`.

The seven-branch ceiling remains unmet. No PR was merged, closed or retargeted; no branch was created, renamed or deleted. No external specialist review or test execution is claimed.


---

## 12. EVT decision-and-validation pack added — 21 November 2026

A new review artifact was created on the existing branch `review/scientific-data-model-review-pack` and fetched again to verify its contents:

- File: `docs/reviews/EVT-DECISION-AND-VALIDATION-PACK.md`
- Commit: `15efc472095d94a5540f4655bbb66b196e6842ab`
- Blob: `694a2b057b60036bdc961191daa94566830b7e91`
- Verified length: 725 lines
- Includes EVT-D01–EVT-D10, EVT-01–EVT-22, ten worked workflows, source/document SHAs, standards/version baseline, candidate model gap analysis, explicit/implicit non-detection safeguards and Task 05E readiness gate.
- Status: proposed for specialist review; no decision accepted; no test executed; Task 05E NOT READY.

The artifact distinguishes shared contextual Event records from Survey and Occurrence specializations and proposes (for review only) a SurveyTargetAssessment separate from the canonical Occurrence-level result. It also records that implicit absence may be a profile-specific export inference only when target scope and completeness requirements are met.

### 12.1 Live repository state after pack creation

- Branch count: **23**.
- Open PR count: **20**.
- PR #9: `open`, draft `true`, base `main`, head `review/scientific-data-model-review-pack`, head SHA `15efc472095d94a5540f4655bbb66b196e6842ab`.
- PR #16: `open`, draft `true`, base `develop`, head `docs/repository-audit-and-ai-operating-standard`, head SHA `4082edffef2b04a765fa57a0f1af7f77ddd852d3`.

No PR was merged, closed or retargeted. No branch was created, renamed or deleted. No external specialist was contacted.


---

## 13. Cross-document Event–Survey–Occurrence audit recorded — 21 November 2026

The scientific review branch now contains the append-only cross-document audit in:

- `docs/reviews/TASK-05C-COMPETING-MODEL-RECONCILIATION.md`
- Review branch: `review/scientific-data-model-review-pack`
- Commit: `e782d4c86b341da194e27130bc3de14826e96d89`
- Blob: `888643133a7ae8c6c9f10b9279d7347310c8ce27`
- Verified file length: 542 lines.

The addendum records the exact source blob SHAs inspected and the consistency findings across Task 05B, Task 05C Candidates A/B, Task 05D v3, the EVT pack, the decision paper, the validation matrix and accepted ADR-005/ADR-007.

Key findings recorded:
- Task 05B recommends a shared Event identity/supertype with Survey and Occurrence specializations, but neither Task 05C candidate fully implements this identity/specialization semantics.
- Survey and SurveyTarget are not yet first-class, fully specified concepts in either Task 05C candidate.
- The proposed SurveyTargetAssessment boundary and its relationship to canonical Occurrence results remain unresolved.
- The operating prompt's no-inference rule requires owner clarification before implicit absence is implemented in exports.
- The EVT pack must add parent-child spatial/temporal containment and general no-inheritance/no-derivation rules from the current Hierarchical Events guidance.
- DR-09 remains open pending exact, reproducible standards/term-version pinning.
- GBIF and Darwin Core occurrence-status mappings remain profile-specific and require executable tests.

No accepted ADR, Task 05B, Task 05C, Task 05D or EVT decision was changed by this audit. No test was executed and no external specialist approval is claimed. Task 05C remains NOT APPROVED; Task 05E remains NOT READY.

### 13.1 Live repository snapshot after audit write

- Branch count: **23**.
- Open PR count: **20**.
- PR #9: `open`, draft `true`, base `main`, head `review/scientific-data-model-review-pack`, head SHA `e782d4c86b341da194e27130bc3de14826e96d89`.
- PR #16: `open`, draft `true`, base `develop`, head `docs/repository-audit-and-ai-operating-standard`, head SHA `40cbe6e8787c118eddcc5c09de4227e8e0fbb143`.

The seven-branch ceiling remains unmet. No PR was merged, closed or retargeted; no branch was created, renamed or deleted. No external specialist was contacted.


---

## 14. Standards interpretation errata recorded — 21 November 2026

The scientific review branch has received two verified, append-only documentation updates:

1. `docs/reviews/EVT-DECISION-AND-VALIDATION-PACK.md`
   - Commit: `4b5225dd19bda60a96018eee062c5b46afa642fb`
   - Blob: `11e7fe930291e19ff7fb13b59d037c8d0b24cebe`
   - Verified length: 832 lines.
   - Adds §15 errata, qualifies Event identity/implementation, adds post-facto SurveyTarget filtering, distinguishes reporting completeness from field completeness/detectability, clarifies hierarchy no-inheritance versus explicit scope/completeness inference, records version retrieval discrepancy and adds EVT-23–EVT-26.

2. `docs/reviews/TASK-05C-COMPETING-MODEL-RECONCILIATION.md`
   - Commit: `3bde5ed8a6b7c8c65923c2cddde4aaa353ca6e8a`
   - Blob: `a113eef540c3270f4b4c5bdd21cbbf7709dc5f9d`
   - Verified length: 630 lines.
   - Adds §16 with the same interpretation corrections and owner decision requirement for implicit absence in exports.

Important correction: Darwin Core's conceptual model does not prescribe SQL table inheritance. The unresolved issue is faithful representation of Event identity, special Event semantics, generic contextual Event references and typed relationships. The GBIF guide's no-inheritance/no-parent-derivation rules are distinct from Humboldt's explicit scope/completeness reporting and bounded hierarchy-aware inference rules.

**Status:** documentation errata only. No decision accepted, no ADR changed, no Task 05B/05C/05D candidate modified, no tests executed, no external expert approval. Task 05C remains NOT APPROVED; Task 05E remains NOT READY.

### 14.1 Live repository snapshot after standards errata

- Branch count: **23**.
- Open PR count: **20**.
- PR #9: `open`, draft `true`, base `main`, head `review/scientific-data-model-review-pack`, head SHA `3bde5ed8a6b7c8c65923c2cddde4aaa353ca6e8a`.
- PR #16: `open`, draft `true`, base `develop`, head `docs/repository-audit-and-ai-operating-standard`, head SHA `a45c8d71b1fd0f57f402c89f8fce54396501ce16`.

The seven-branch ceiling remains unmet. No PR was merged, closed or retargeted; no branch was created, renamed or deleted. No external specialist was contacted.

 
## 15. Owner decision ODR-01 recorded — 21 November 2026

The project owner authorized Option B: controlled, profile-specific implicit non-detection interpretation in external exports only. The complete decision and safeguards are recorded in:
- `docs/reviews/SCIENTIFIC-DATA-MODEL-VALIDATION-MATRIX-AND-DECISION-REGISTER.md`, ODR-01;
- `docs/reviews/EVT-DECISION-AND-VALIDATION-PACK.md`, §16;
- `docs/reviews/EVENT-SURVEY-OCCURRENCE-CONCEPTUAL-MODEL-DECISION-PAPER.md`, §14; and
- `docs/reviews/TASK-05C-COMPETING-MODEL-RECONCILIATION.md`, §17.

The operating prompt on this branch has an appended §14.1 clarification. The original Principle 8 is retained: a missing internal record alone never proves absence. The authorized exception is export-only, requires explicit scope/completeness and pinned, validated mappings, excludes bycatch, fails closed, and does not create an internal negative Occurrence.

EVT-27–EVT-30 are proposed and untested. No Task 05C candidate or Task 05D validation document was modified. Task 05C remains NOT APPROVED; Task 05E remains NOT READY. No branch or PR was created, merged, closed, deleted or retargeted.

 
## 16. Task 05C reconciliation proposal added — 21 November 2026

A proposed Event–Survey–Occurrence reconciliation section was appended to Candidate A on its existing branch:
- File: `docs/architecture/TASK-05C-LOGICAL-DATABASE-MODEL.md`
- Branch / PR: `docs/task-05c-logical-data-model` / PR #5
- Commit: `ded43eea96bcaf1cb57c0689ff2b2217da2f9764`
- Blob: `2efc627683182b370fb11ab14e056aa31f894180`
- Section: §18, “Event–Survey–Occurrence reconciliation proposal”
- Status: Proposed; not accepted; no physical schema or implementation authorized.

The proposal retains Candidate A's original content and recommends a shared Event identity with distinct Survey and Occurrence specializations, separate Observation workflow records, explicit SurveyTarget/SurveyTargetResult, a SurveyOccurrenceReport link separate from parent-child Event hierarchy, and typed Observation links. It selectively incorporates Candidate B's useful workflow/cardinality cases. It records ODR-01 and EVT-27–EVT-33 as validation requirements. Neither Candidate A nor Candidate B is approved.

**Stacked dependency warning:** PR #11 (Task 05D v3) remains open/draft and is based on Candidate A. After the Candidate A update, the GitHub compare result is **diverged**, with Task 05D v3 **3 commits ahead and 2 commits behind** Candidate A; merge base `91c82b4f136a77aaa1edb02753ed49b2fbee86ed`. Do not merge, rebase, retarget or otherwise alter this dependency automatically. Reconcile the Task 05D diff and synchronize it through an explicit, reviewed plan before any PR decision.

No branch or PR was created, merged, closed, deleted or retargeted. The seven-branch ceiling remains unmet.

 
## 17. Scientific model and validation documentation updates — 21 November 2026

Append-only documentation updates were verified on existing branches:

- Task 05C Candidate A / PR #5: commit `98741843a2ba8550e2cb744658d9291fe60b8823`, blob `c8bddcdfda9f76f03afd389ff9c5a307b89bd906`.
- Task 05B dictionary / PR #4: commit `8936fe87a2c32da861c7f6a08d52603c9e545d21`, blob `b6827f8149313f0e70ac6a8873108aae509eb785`.
- Task 05D v3 / PR #11: commit `9d383c4206f2d48bd31b04c6ebb5bd97bf7b87df`, blob `27a12b960d84b504fe915da4681d2f2511bdb086`.

The new sections clarify Event special types, generic/context Event use, Survey reporting of Occurrences, bycatch, explicit non-detection, target origin and current standards metadata. Synthetic fixtures EVT-34–EVT-44 are proposed only; none has been executed.

Current repository audit at the start of this work found 23 branches and 20 open PRs. The long-lived branches remain `main`, `develop` and `staging`. The immediate ceiling of seven total branches is not met. No branch was created, deleted, renamed or retargeted; no PR was merged or closed; no protection setting was changed.

PR #11 remains based on Candidate A and has diverged from its updated branch. Its dependency requires a full diff review and a separately approved synchronization plan. Do not merge, rebase or retarget it blindly.

No scientific model, ADR, physical schema, API contract, export profile or implementation was approved by these documentation updates.

 
## 18. Latest Task 05D dependency comparison — 21 November 2026

Latest compare for Candidate A `docs/task-05c-logical-data-model` → Task 05D v3 `docs/task-05d-logical-model-validation-v3` is **diverged: 4 ahead / 3 behind**, merge base `91c82b4f136a77aaa1edb02753ed49b2fbee86ed`. PR #11 remains open/draft with Candidate A as its base.

The updated document commits are Candidate A `98741843a2ba8550e2cb744658d9291fe60b8823`, Task 05D `9d383c4206f2d48bd31b04c6ebb5bd97bf7b87df`, and Task 05B `8936fe87a2c32da861c7f6a08d52603c9e545d21`.

Do not treat divergence alone as a content conflict or as an instruction to rebase. Full graph and content review is required before a synchronization plan. No branch or PR lifecycle action has occurred. Branch count remains 23; seven-branch ceiling remains unmet.

 
## 19. Final refreshed Task 05D comparison — 21 November 2026

Latest comparison:
- Candidate A base commit: `98741843a2ba8550e2cb744658d9291fe60b8823`.
- Task 05D v3 head / PR #11: `9d4ca85c553ef5732334322be7f598ed748d285c`.- Branch status: **diverged; 6 ahead / 3 behind**.
- Merge base: `91c82b4f136a77aaa1edb02753ed49b2fbee86ed`.

PR #11 remains open/draft and based on Candidate A. The compare result is a history relationship, not a content-conflict verdict. No rebase, retarget, merge, force-push, branch creation or deletion was performed. Any synchronization plan requires full graph and content review.


---

## 20. Live repository baseline refresh and preservation-first consolidation status — 21 November 2026

**Audit method:** Direct GitHub REST reads of the repository branch collection, individual branch refs, pull-request metadata, current file contents and compare endpoints. This section supersedes earlier branch/PR counts and current-head assertions where they conflict with the live records below. Earlier dated records are retained as history, not silently rewritten.

### 20.1 Repository and branch baseline

- Repository: Save-Tiger-First/botanica-indica
- Default branch: main
- Repository archived: false
- Branches returned by the live GitHub branch collection: **23**
- Required long-lived branches: main, develop, staging — all present.
- Temporary/workstream branches: **20**
- Immediate owner-authorized ceiling: **7 total branches** (3 long-lived + no more than 4 temporary/workstream branches).
- Current excess over the ceiling: **16 branches**.
- The target is **not met**.

| Branch | Live head SHA | GitHub branch API protected flag |
|---|---|---|
| develop | f165ecb9b4d9de115c02327cf779982b7ef4bbd4 | false |
| docs/adr-011-stf-ecosystem-boundaries | e900b64c90df08f5c98181af54bf2ab0b7096759 | false |
| docs/asset-specific-licensing-policy | 15fd4edef9afa8d22df9e23f66296ef09423d8cf | false |
| docs/canonical-task-03-04-baselines | 0f908f8221ad3434cc84fe2cd41b735aad0a752a | false |
| docs/full-product-vision-capability-blueprint | b66c16355d0ded4f20f1a84172eab8b47d133277 | false |
| docs/full-system-architecture-and-repo-engineering-plan | b478add74f277daaedd555fcc58670ebd2059601 | false |
| docs/repository-audit-and-ai-operating-standard | ff960523be4fbeae98d7aed33a155f05a682d5ba | false |
| docs/requirements-traceability-register | b2e8728e5e725b844a41438260e3a40f77ca65db | false |
| docs/task-05-data-architecture | 2b02ab3cd115691841889ed77d453b31ab0bed16 | false |
| docs/task-05-data-dictionary | e11fd943e59c81ea8b464ef6a84ac4bcdbcccfd4 | false |
| docs/task-05c-logical-data-model | d443420d6b77815cb155f457ea262e621aabf7cb | false |
| docs/task-05c-logical-database-model | 8d4fef2d726aac79dd684856d924b171e44d0b93 | false |
| docs/task-05d-logical-model-validation | 3efd80e5e28b2a916e63c85808ef3aba9d35e4ac | false |
| docs/task-05d-logical-model-validation-v2 | 76bd88980bb2536db63bbde76e3fa687503bdda1 | false |
| docs/task-05d-logical-model-validation-v3 | 0577250c9e7cffcb3605acc782f403b7d1b422e0 | false |
| governance/branch-lifecycle-policy | 633105210d3a6c4c8e36287ed2dc44dee23f61ef | false |
| governance/stf-organisational-readiness-review | bd5b18fe5d68f50e25f0453eb792d0c44bc700d0 | false |
| main | f165ecb9b4d9de115c02327cf779982b7ef4bbd4 | true |
| proposal/bengaluru-urban-biodiversity-feasibility-pilot | 7f7a3be03d68d5595465279ad22407ea983f046e | false |
| research/bengaluru-pilot-site-selection | ee71dc0da319e7b3c69572f9c6f015298e3c8c2e | false |
| review/scientific-data-model-review-pack | b9a5a7a0b93a448c392dff4db19fd8d02ed7dfc4 | false |
| staging | f165ecb9b4d9de115c02327cf779982b7ef4bbd4 | false |
| strategy/naturetech-biodiversity-conservation-impact | 9d76328df8112922df818f01c27e297b3ee1b76a | false |

main, develop and staging currently point to the same commit. The GitHub branch API marks only main as protected. This flag is not a complete statement of all effective protection: the only active repository ruleset retrieved is ID 23822734, “Protect main branch”, targeting the default branch, with deletion and non-fast-forward rules. It has no pull-request or review requirement. No ruleset targeting develop or staging was returned. No protection setting was changed.

### 20.2 Live pull-request inventory

The live PR search and individual PR metadata reads returned **20 open PRs** and **3 closed, unmerged PRs**. Of the open PRs, **19 are drafts** and **PR #15 is open and not draft (ready for review)**. No PR is merged.

| PR | State | Draft | Base branch | Head branch | Current head SHA |
|---:|---|---|---|---|---|
| #1 | open | yes | main | docs/asset-specific-licensing-policy | 15fd4edef9afa8d22df9e23f66296ef09423d8cf |
| #2 | open | yes | main | docs/adr-011-stf-ecosystem-boundaries | e900b64c90df08f5c98181af54bf2ab0b7096759 |
| #3 | open | yes | main | docs/task-05-data-architecture | 2b02ab3cd115691841889ed77d453b31ab0bed16 |
| #4 | open | yes | main | docs/task-05-data-dictionary | e11fd943e59c81ea8b464ef6a84ac4bcdbcccfd4 |
| #5 | open | yes | main | docs/task-05c-logical-data-model | d443420d6b77815cb155f457ea262e621aabf7cb |
| #6 | closed, unmerged | — | main | docs/task-05c-logical-database-model | 8d4fef2d726aac79dd684856d924b171e44d0b93 |
| #7 | closed, unmerged | — | docs/task-05c-logical-data-model | docs/task-05d-logical-model-validation | 3efd80e5e28b2a916e63c85808ef3aba9d35e4ac |
| #8 | open | yes | main | strategy/naturetech-biodiversity-conservation-impact | 9d76328df8112922df818f01c27e297b3ee1b76a |
| #9 | open | yes | main | review/scientific-data-model-review-pack | b9a5a7a0b93a448c392dff4db19fd8d02ed7dfc4 |
| #10 | closed, unmerged | — | docs/task-05c-logical-data-model | docs/task-05d-logical-model-validation-v2 | 76bd88980bb2536db63bbde76e3fa687503bdda1 |
| #11 | open | yes | docs/task-05c-logical-data-model | docs/task-05d-logical-model-validation-v3 | 0577250c9e7cffcb3605acc782f403b7d1b422e0 |
| #12 | open | yes | strategy/naturetech-biodiversity-conservation-impact | governance/stf-organisational-readiness-review | bd5b18fe5d68f50e25f0453eb792d0c44bc700d0 |
| #13 | open | yes | main | proposal/bengaluru-urban-biodiversity-feasibility-pilot | 7f7a3be03d68d5595465279ad22407ea983f046e |
| #14 | open | yes | main | research/bengaluru-pilot-site-selection | ee71dc0da319e7b3c69572f9c6f015298e3c8c2e |
| #15 | open | no | develop | governance/branch-lifecycle-policy | 633105210d3a6c4c8e36287ed2dc44dee23f61ef |
| #16 | open | yes | develop | docs/repository-audit-and-ai-operating-standard | ff960523be4fbeae98d7aed33a155f05a682d5ba |
| #17 | open | yes | develop | docs/full-product-vision-capability-blueprint | b66c16355d0ded4f20f1a84172eab8b47d133277 |
| #18 | open | yes | develop | docs/canonical-task-03-04-baselines | 0f908f8221ad3434cc84fe2cd41b735aad0a752a |
| #19 | open | yes | develop | docs/requirements-traceability-register | b2e8728e5e725b844a41438260e3a40f77ca65db |
| #20 | open | yes | develop | docs/full-system-architecture-and-repo-engineering-plan | b478add74f277daaedd555fcc58670ebd2059601 |
| #21 | open | yes | review/scientific-data-model-review-pack | docs/task-05c-logical-database-model | 8d4fef2d726aac79dd684856d924b171e44d0b93 |
| #22 | open | yes | review/scientific-data-model-review-pack | docs/task-05d-logical-model-validation | 3efd80e5e28b2a916e63c85808ef3aba9d35e4ac |
| #23 | open | yes | review/scientific-data-model-review-pack | docs/task-05d-logical-model-validation-v2 | 76bd88980bb2536db63bbde76e3fa687503bdda1 |

The three closed PRs (#6, #7 and #10) were not merged. Their source branches remain live and are now also heads of preservation PRs #21, #22 and #23 respectively. Do not delete those branches while the preservation PRs remain open or before their unique content and provenance have been reconciled.

### 20.3 Current dependency comparisons

Direct compare results were refreshed against the current branch refs:

| Dependency | Current comparison | Merge base | Assessment |
|---|---|---|---|
| PR #11: Candidate A → Task 05D v3 | Head has 7 commits not in base; base has 4 commits not in head | 91c82b4f136a77aaa1edb02753ed49b2fbee86ed | Diverged; reconcile complete diff and dependency before any synchronization |
| PR #12: NatureTech strategy → organisational readiness | Head has 4 commits not in base; base has 3 commits not in head | 44b7ed4dab20c2a76c2357d284dc956baaf067a9 | Diverged; reconcile overlapping strategy content before any synchronization |
| PR #21: scientific review pack → alternate Task 05C | Head has 1 commit not in base; base has 64 commits not in head | f165ecb9b4d9de115c02327cf779982b7ef4bbd4 | Severely stale/diverged preservation PR; inspect current diff and preserve unique model content |
| PR #22: scientific review pack → earlier Task 05D | Head has 7 commits not in base; base has 64 commits not in head | f165ecb9b4d9de115c02327cf779982b7ef4bbd4 | Severely stale/diverged preservation PR; inspect current diff and preserve unique validation content |
| PR #23: scientific review pack → Task 05D v2 | Head has 7 commits not in base; base has 64 commits not in head | f165ecb9b4d9de115c02327cf779982b7ef4bbd4 | Severely stale/diverged preservation PR; inspect current diff and preserve unique v2 content |

“Ahead” and “behind” are relative to the comparison's base and head refs. Divergence is a history relationship, not proof of a textual conflict and not permission to rebase, retarget or merge.

### 20.4 Current document and decision-status verification

The following current file blobs were fetched from the live refs during this refresh:

| Document | Branch | Current blob SHA | Verified status |
|---|---|---|---|
| docs/governance/AI-PROJECT-OPERATING-PROMPT.md | docs/repository-audit-and-ai-operating-standard | 53add3894d0502827e584614c70ad09cadaa637d | Governing prompt; includes ODR-01 clarification |
| docs/governance/BRANCH-INVENTORY-AND-CONSOLIDATION-REGISTER.md | docs/repository-audit-and-ai-operating-standard | 83ad24642eb632e95b3000eafa331e902b5f09c0 | This register, before this refresh addendum |
| docs/governance/BRANCHING-AND-RELEASE-GOVERNANCE.md | docs/repository-audit-and-ai-operating-standard | 34113278067336572529fe61e647d9c28bdf4042 | Proposed branch policy; not yet adopted by merge |
| docs/architecture/TASK-05C-LOGICAL-DATABASE-MODEL.md | docs/task-05c-logical-data-model | b447796e7da0d08d96400812667a8e67e0696144 | Candidate A remains proposed and unreconciled; Task 05C NOT APPROVED |
| docs/data-architecture/TASK-05D-LOGICAL-MODEL-VALIDATION-AND-PHYSICAL-DESIGN-READINESS.md | docs/task-05d-logical-model-validation-v3 | 0b9a009b1c543b2450758f659c97cae3802a2f94 | Draft validation gate; Task 05E NOT READY |
| docs/reviews/SCIENTIFIC-DATA-MODEL-VALIDATION-MATRIX-AND-DECISION-REGISTER.md | review/scientific-data-model-review-pack | 3a33dfe47657a96456f56f2c12a0b7d355b6c6a5 | Proposed review package; no external review/sign-off recorded |
| docs/reviews/EVT-DECISION-AND-VALIDATION-PACK.md | review/scientific-data-model-review-pack | 4a317c4c83317e10663ba374e9e6be3100a53431 | Proposed for specialist review; EVT decisions remain open and scenarios unexecuted |

The live Task 05C Candidate A still states that its earlier Event-to-Occurrence relationship and its later shared Event identity/specialization proposal are not yet reconciled into one coherent ERD, key strategy and cardinality set. Task 05D still identifies unresolved assessment/result semantics and validation cases. ODR-01 remains owner-authorized for bounded, profile-specific external exports only; it does not approve Candidate A/B, Task 05C, Task 05D, Task 05E, a physical schema, an API contract or implementation. Internal absence is not inferred from a missing Occurrence. Task 05C remains NOT APPROVED and Task 05E remains NOT READY.

### 20.5 Historical inventory discrepancies requiring provenance reconciliation

Earlier Sections 14–19 record several commit IDs as later/current PR heads. Those identifiers do not match the live branch refs and PR head SHAs returned in this refresh. Examples include:

- Sections 17–19 record Candidate A / Task 05D commits 98741843a2ba8550e2cb744658d9291fe60b8823 and 9d4ca85c553ef5732334322be7f598ed748d285c; current PR #5 / #11 heads are d443420d6b77815cb155f457ea262e621aabf7cb and 0577250c9e7cffcb3605acc782f403b7d1b422e0.
- Section 14.1 records PR #9 head 3bde5ed8a6b7c8c65923c2cddde4aaa353ca6e8a; current PR #9 head is b9a5a7a0b93a448c392dff4db19fd8d02ed7dfc4.
- Section 14.1 records PR #16 head a45c8d71b1fd0f57f402c89f8fce54396501ce16; current PR #16 head is ff960523be4fbeae98d7aed33a155f05a682d5ba.

These earlier SHAs may be historical commits, but this refresh does not establish that they are current branch tips or that all associated changes are present in the live PR heads. Do not rely on them as current head identifiers. Preserve the historical statements and investigate commit reachability/provenance before classifying them as erroneous, superseded or abandoned. The live refs and PR metadata in Sections 20.1–20.4 are the current baseline for subsequent work.

### 20.6 Recommended consolidation routing — reaffirmed, not an approval to merge

Retain the four existing workstream destinations:

1. Governance: docs/repository-audit-and-ai-operating-standard (PR #16). Reconcile PR #15 and the licensing / proposed ADR material from PRs #1–#2 without implying policy or ADR approval.
2. Product and architecture: docs/full-system-architecture-and-repo-engineering-plan (PR #20). Reconcile PRs #17–#19 and #20 while preserving Task 03/04 source provenance and accepted ADR constraints.
3. Scientific review: review/scientific-data-model-review-pack (PR #9). Preserve and reconcile PRs #3–#5, #11 and #21–#23. Resolve the Task 05C/05D dependency and competing models before any physical-design gate.
4. STF strategy: strategy/naturetech-biodiversity-conservation-impact (PR #8). Reconcile PRs #12–#14 in dependency order; retain feasibility-only, no-site-selected and no-fieldwork-authorized status.

No new branches are authorized. The four destinations plus main, develop and staging are the only seven branches intended to remain after the preservation, review and retirement gates have been satisfied. The sequence is not to delete source branches first: reconcile unique content, review and resolve the relevant PR, confirm no open PR references the source branch, then retire that branch with explicit authorization.

### 20.7 Actions and non-actions in this refresh

- This addendum records a fresh live baseline; it does not approve any PR, ADR, scientific model, policy, pilot or architecture decision.
- No branch was created, renamed, deleted or moved.
- No PR was merged, closed or retargeted.
- No ruleset, branch protection, permission or repository setting was changed.
- No external expert, institution, partner or legal adviser was contacted.
- No scientific test was executed and no independent specialist review is claimed.
- The seven-branch target remains unmet: 23 branches are live.

**Next task:** conduct a preservation-first, content-level reconciliation of the four workstreams, beginning with the governance PR #15 / #16 package and then the product/architecture PR #17–#20 package. Before any source-branch retirement, update this register with the exact source-to-destination content mapping, duplicate/collision decisions, retained provenance, PR resolution evidence and owner approval.


## 20.8 Live baseline refresh after PR #20 roadmap commit — 21 November 2026, 17:07 IST

**Purpose:** Record the latest live repository state after the master roadmap document was committed to the existing PR #20 branch. This addendum supersedes earlier current-head assertions in Sections 20.1–20.4 where the live values below differ. Prior snapshots remain historical evidence and are not silently rewritten.

### 20.8.1 Repository and branch heads

Direct GitHub REST reads at 17:07 IST returned a public, non-archived repository with default branch `main`. The branch collection returned **23 branches**: the three required long-lived branches and 20 temporary/workstream branches. The immediate ceiling of seven remains exceeded by 16 branches.

| Branch | Current head SHA | Branch API protected flag |
|---|---|---|
| `develop` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | false |
| `docs/adr-011-stf-ecosystem-boundaries` | `e900b64c90df08f5c98181af54bf2ab0b7096759` | false |
| `docs/asset-specific-licensing-policy` | `15fd4edef9afa8d22df9e23f66296ef09423d8cf` | false |
| `docs/canonical-task-03-04-baselines` | `0f908f8221ad3434cc84fe2cd41b735aad0a752a` | false |
| `docs/full-product-vision-capability-blueprint` | `b66c16355d0ded4f20f1a84172eab8b47d133277` | false |
| `docs/full-system-architecture-and-repo-engineering-plan` | `98f5bd498a92af5d1c9a79ad038fe33741959079` | false |
| `docs/repository-audit-and-ai-operating-standard` | `d52dfef64cb6eee218cc2a7b02c80e6b1dcfd66c` | false |
| `docs/requirements-traceability-register` | `b2e8728e5e725b844a41438260e3a40f77ca65db` | false |
| `docs/task-05-data-architecture` | `2b02ab3cd115691841889ed77d453b31ab0bed16` | false |
| `docs/task-05-data-dictionary` | `e11fd943e59c81ea8b464ef6a84ac4bcdbcccfd4` | false |
| `docs/task-05c-logical-data-model` | `d443420d6b77815cb155f457ea262e621aabf7cb` | false |
| `docs/task-05c-logical-database-model` | `8d4fef2d726aac79dd684856d924b171e44d0b93` | false |
| `docs/task-05d-logical-model-validation` | `3efd80e5e28b2a916e63c85808ef3aba9d35e4ac` | false |
| `docs/task-05d-logical-model-validation-v2` | `76bd88980bb2536db63bbde76e3fa687503bdda1` | false |
| `docs/task-05d-logical-model-validation-v3` | `0577250c9e7cffcb3605acc782f403b7d1b422e0` | false |
| `governance/branch-lifecycle-policy` | `633105210d3a6c4c8e36287ed2dc44dee23f61ef` | false |
| `governance/stf-organisational-readiness-review` | `bd5b18fe5d68f50e25f0453eb792d0c44bc700d0` | false |
| `main` | `6f2f51da093caf8183fde386dbec707cc6046d27` | true |
| `proposal/bengaluru-urban-biodiversity-feasibility-pilot` | `7f7a3be03d68d5595465279ad22407ea983f046e` | false |
| `research/bengaluru-pilot-site-selection` | `ee71dc0da319e7b3c69572f9c6f015298e3c8c2e` | false |
| `review/scientific-data-model-review-pack` | `51b909accbf052426678969d0a28408356133e61` | false |
| `staging` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | false |
| `strategy/naturetech-biodiversity-conservation-impact` | `9d76328df8112922df818f01c27e297b3ee1b76a` | false |

Only `main` is marked protected by the branch collection. The active repository ruleset read at this refresh is ID `23822734`, “Protect main branch”, targeting the default branch, with deletion and non-fast-forward restrictions. It does not contain a pull-request or review requirement. This is not a full claim about every classic branch-protection endpoint; no protection settings were changed.

### 20.8.2 Current long-lived branch drift

- `main` is at `6f2f51da093caf8183fde386dbec707cc6046d27`.
- `develop` and `staging` remain at `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`.
- Direct compare confirms `main` is **one commit ahead** of `develop` / `staging`, with no commits behind.
- The sole main-only commit is `6f2f51da093caf8183fde386dbec707cc6046d27`, message “docs(science): map Hortus case to model validation”; it adds `docs/reviews/HORTUS-MALABARICUS-VALIDATION-CROSSWALK.md` (187 additions, no deletions).
- The current open PR base snapshots continue to reference the earlier `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` for their main/develop targets. This is a synchronization and traceability issue, not permission to cherry-pick, rebase or merge.

### 20.8.3 Current open PR metadata

Twenty PRs remain open. Nineteen are drafts; PR #15 is the sole non-draft open PR. None is merged. PR #9 is currently reported by GitHub as non-mergeable; all other open PRs are currently reported mergeable. “Mergeable” is only a GitHub metadata signal and is not approval, review or proof that a PR is ready.

| PR | State | Draft | Base branch | Base SHA in PR metadata | Head branch | Current head SHA | GitHub mergeable |
|---:|---|---|---|---|---|---|---|
| #1 | open | yes | main | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | `docs/asset-specific-licensing-policy` | `15fd4edef9afa8d22df9e23f66296ef09423d8cf` | true |
| #2 | open | yes | main | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | `docs/adr-011-stf-ecosystem-boundaries` | `e900b64c90df08f5c98181af54bf2ab0b7096759` | true |
| #3 | open | yes | main | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | `docs/task-05-data-architecture` | `2b02ab3cd115691841889ed77d453b31ab0bed16` | true |
| #4 | open | yes | main | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | `docs/task-05-data-dictionary` | `e11fd943e59c81ea8b464ef6a84ac4bcdbcccfd4` | true |
| #5 | open | yes | main | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | `docs/task-05c-logical-data-model` | `d443420d6b77815cb155f457ea262e621aabf7cb` | true |
| #8 | open | yes | main | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | `strategy/naturetech-biodiversity-conservation-impact` | `9d76328df8112922df818f01c27e297b3ee1b76a` | true |
| #9 | open | yes | main | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | `review/scientific-data-model-review-pack` | `51b909accbf052426678969d0a28408356133e61` | false |
| #11 | open | yes | `docs/task-05c-logical-data-model` | `91c82b4f136a77aaa1edb02753ed49b2fbee86ed` | `docs/task-05d-logical-model-validation-v3` | `0577250c9e7cffcb3605acc782f403b7d1b422e0` | true |
| #12 | open | yes | `strategy/naturetech-biodiversity-conservation-impact` | `44b7ed4dab20c2a76c2357d284dc956baaf067a9` | `governance/stf-organisational-readiness-review` | `bd5b18fe5d68f50e25f0453eb792d0c44bc700d0` | true |
| #13 | open | yes | main | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | `proposal/bengaluru-urban-biodiversity-feasibility-pilot` | `7f7a3be03d68d5595465279ad22407ea983f046e` | true |
| #14 | open | yes | main | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | `research/bengaluru-pilot-site-selection` | `ee71dc0da319e7b3c69572f9c6f015298e3c8c2e` | true |
| #15 | open | no | develop | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | `governance/branch-lifecycle-policy` | `633105210d3a6c4c8e36287ed2dc44dee23f61ef` | true |
| #16 | open | yes | develop | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | `docs/repository-audit-and-ai-operating-standard` | `d52dfef64cb6eee218cc2a7b02c80e6b1dcfd66c` | true |
| #17 | open | yes | develop | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | `docs/full-product-vision-capability-blueprint` | `b66c16355d0ded4f20f1a84172eab8b47d133277` | true |
| #18 | open | yes | develop | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | `docs/canonical-task-03-04-baselines` | `0f908f8221ad3434cc84fe2cd41b735aad0a752a` | true |
| #19 | open | yes | develop | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | `docs/requirements-traceability-register` | `b2e8728e5e725b844a41438260e3a40f77ca65db` | true |
| #20 | open | yes | develop | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | `docs/full-system-architecture-and-repo-engineering-plan` | `98f5bd498a92af5d1c9a79ad038fe33741959079` | true |
| #21 | open | yes | `review/scientific-data-model-review-pack` | `1be0975e457d56152ad57a1cd6bb5d941328fbda` | `docs/task-05c-logical-database-model` | `8d4fef2d726aac79dd684856d924b171e44d0b93` | true |
| #22 | open | yes | `review/scientific-data-model-review-pack` | `1be0975e457d56152ad57a1cd6bb5d941328fbda` | `docs/task-05d-logical-model-validation` | `3efd80e5e28b2a916e63c85808ef3aba9d35e4ac` | true |
| #23 | open | yes | `review/scientific-data-model-review-pack` | `1be0975e457d56152ad57a1cd6bb5d941328fbda` | `docs/task-05d-logical-model-validation-v2` | `76bd88980bb2536db63bbde76e3fa687503bdda1` | true |

### 20.8.4 Refreshed dependency comparisons

Comparisons were run using the current live branch tips rather than only the base/head SHAs stored in the original PR creation metadata:

| Dependency | Current comparison | Merge base | Assessment |
|---|---|---|---|
| PR #11 — Candidate A → Task 05D v3 | 7 commits ahead / 4 behind | `91c82b4f136a77aaa1edb02753ed49b2fbee86ed` | Diverged; reconcile complete diff and dependency before synchronization |
| PR #12 — NatureTech strategy → organisational readiness | 4 commits ahead / 3 behind | `44b7ed4dab20c2a76c2357d284dc956baaf067a9` | Diverged; reconcile overlapping strategy content before synchronization |
| PR #21 — alternate Task 05C → scientific review pack | 1 commit ahead / 67 behind | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | Severely stale/diverged preservation PR; preserve unique model content and provenance |
| PR #22 — earlier Task 05D → scientific review pack | 7 commits ahead / 67 behind | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | Severely stale/diverged preservation PR; preserve unique validation content |
| PR #23 — Task 05D v2 → scientific review pack | 7 commits ahead / 67 behind | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | Severely stale/diverged preservation PR; preserve unique v2 findings |

The PR #21–#23 comparisons are now 67 commits behind the current scientific-review branch, not the 64 commits reported in the earlier snapshot. This is a history comparison, not proof of textual conflict or permission to rebase, retarget, merge or close.

### 20.8.5 Consolidation assessment and next safe action

The same four existing consolidation destinations remain the only permitted workstream destinations. The immediate ceiling is still 7; current total is 23. No branch retirement is safe yet because the preservation mapping, review/PR resolution and source-branch dependencies remain outstanding.

**Recommendation:** start with a content-level governance reconciliation of PR #15 and PR #16, then reconcile PR #1 and #2 into the governance workstream without silently accepting proposed licensing policy or ADR-011. The main/develop/staging drift and PR #9 non-mergeable state should be tracked as separate blockers. Do not retarget or merge PRs merely to reduce the branch count.

### 20.8.6 Verification and non-actions

- Operating Prompt fetched from `docs/repository-audit-and-ai-operating-standard`; blob SHA `53add3894d0502827e584614c70ad09cadaa637d`. The current owner directives and ODR-01 remain unchanged.
- Master Project Roadmap v0.1 fetched from PR #20 branch; blob SHA `60fba1bdb5d2b3fe299847225d21aee18641ad48`. It remains Proposed / owner review required; the user's “go ahead with your recommendation” is treated as authorization to continue the recommended reversible audit sequence, not as a formal acceptance of the roadmap, task numbering or architecture.
- PR #20 remains open and draft, based on `develop`; its head is `98f5bd498a92af5d1c9a79ad038fe33741959079`.
- PR #16 remains open and draft, based on `develop`; its head is `d52dfef64cb6eee218cc2a7b02c80e6b1dcfd66c`.
- PR #9 remains open and draft; GitHub currently reports it non-mergeable.
- No PR was merged, closed or retargeted.
- No branch was created, renamed, deleted or force-pushed.
- No repository protection, ruleset, permission or default-branch setting was changed.
- No scientific model, ADR, product requirement, strategy, pilot or architecture proposal was approved.
- No external party was contacted and no scientific test or independent specialist review was performed.

**Next task:** perform a preservation-first content reconciliation of PR #15 against PR #16, including duplicate-path and policy-semantic comparison, and produce a file-level disposition proposal. Do not merge/close PR #15 or #16 or delete any source branch without explicit authorization.


## 20.9 PR #15 / PR #16 governance content and history reconciliation — 21 November 2026

The dedicated audit `docs/governance/PR-15-PR-16-GOVERNANCE-CONTENT-RECONCILIATION.md` was added on this branch and verified after commit.

**Verified file-level result:**
- `.github/pull_request_template.md`: PR #15 and PR #16 have identical blob SHA `1b2a71bb968cb892bc229c5ce8ac5ffb4b3d1084`.
- `docs/governance/BRANCHING-AND-RELEASE-GOVERNANCE.md`: PR #16 retains PR #15's policy content and adds the exact legacy direct-to-main PR/head grandfathering section. PR #15 blob: `baf085de8baea1ec7becfc15ce3f691512e91aba`; PR #16 blob: `34113278067336572529fe61e647d9c28bdf4042`.
- `docs/governance/BRANCH-INVENTORY-AND-CONSOLIDATION-REGISTER.md`: PR #16 retains the PR #15 register, corrects its earlier Task 05D v2/v3 byte-identity error and adds subsequent audit snapshots. PR #15 blob: `9233910471f0806435cb39c47ff074e90d382e47`; PR #16 blob: `2d5bec2b22fb7f14edf8243ce3473f2e00b1d140`.

**Verified Git history:** comparing PR #15 head `633105210d3a6c4c8e36287ed2dc44dee23f61ef` to PR #16 head `6a1a5c7392610ec2f4ff5f365f084995d333bad0` returns 85 commits ahead and 0 behind, with PR #15 head as merge base. PR #15's entire head ancestry is therefore contained in PR #16.

**Proposed disposition:** PR #16 is the continuing governance review vehicle. PR #15 is a candidate for owner-authorized closure as superseded, without merging. Its source branch may be considered for deletion only after PR #15 is formally resolved, no other open PR references the branch, and the project owner explicitly authorizes deletion.

This is a content/history reconciliation, not approval of the proposed branch policy, licensing policy, ADR-011 or PR #16. No PR or branch lifecycle action was taken.


## 20.10 Live branch and PR register refresh — 21 November 2026

**Purpose:** Record a fresh verification of the branch inventory, open PR set and governance ancestry after the 20.9 reconciliation. This addendum supersedes earlier current-state counts and the 20.9 ancestry count where the live comparisons below differ. Earlier snapshots remain historical evidence.

### 20.10.1 Repository and branch inventory

The live branch search returned **23 branches**. The seven-branch ceiling remains exceeded by **16**. The exact branch set is:

| Branch | Classification |
|---|---|
| `main` | Long-lived canonical branch |
| `develop` | Long-lived integration branch |
| `staging` | Long-lived release-candidate branch |
| `docs/adr-011-stf-ecosystem-boundaries` | Temporary governance/ADR proposal |
| `docs/asset-specific-licensing-policy` | Temporary licensing/IP proposal |
| `docs/canonical-task-03-04-baselines` | Temporary source-baseline workstream |
| `docs/full-product-vision-capability-blueprint` | Temporary product-vision workstream |
| `docs/full-system-architecture-and-repo-engineering-plan` | Temporary architecture consolidation destination |
| `docs/repository-audit-and-ai-operating-standard` | Temporary governance consolidation destination |
| `docs/requirements-traceability-register` | Temporary requirements workstream |
| `docs/task-05-data-architecture` | Temporary scientific architecture workstream |
| `docs/task-05-data-dictionary` | Temporary scientific dictionary workstream |
| `docs/task-05c-logical-data-model` | Temporary Task 05C candidate workstream |
| `docs/task-05c-logical-database-model` | Temporary alternate Task 05C workstream |
| `docs/task-05d-logical-model-validation` | Temporary earlier Task 05D workstream |
| `docs/task-05d-logical-model-validation-v2` | Temporary Task 05D v2 workstream |
| `docs/task-05d-logical-model-validation-v3` | Temporary Task 05D v3 workstream |
| `governance/branch-lifecycle-policy` | Temporary branch-policy workstream |
| `governance/stf-organisational-readiness-review` | Temporary organisational-readiness workstream |
| `proposal/bengaluru-urban-biodiversity-feasibility-pilot` | Temporary feasibility proposal |
| `research/bengaluru-pilot-site-selection` | Temporary site-research workstream |
| `review/scientific-data-model-review-pack` | Temporary scientific-review consolidation destination |
| `strategy/naturetech-biodiversity-conservation-impact` | Temporary STF strategy consolidation destination |

The three required long-lived branches are present. No branch was created, renamed, deleted or force-pushed during this refresh. The four proposed consolidation destinations remain proposals; their existence does not authorize retirement of source branches.

### 20.10.2 Open pull requests

A fresh GitHub search returned **20 open pull requests**: #1–#5, #8, #9 and #11–#23. The existing PR metadata snapshot in Section 20.8 identifies PR #15 as open/non-draft and PR #16 as open/draft; the fresh search confirms both remain in the open set. The search result did not provide a complete refreshed draft/mergeability matrix for every PR, so this addendum does not assert that all other draft flags or mergeability values remain unchanged.

No PR was merged or closed in this refresh. The PR inventory still includes stacked dependencies and preservation PRs; open status alone is not evidence that a PR is current, conflict-free, reviewed or ready to merge.

### 20.10.3 PR #15 / PR #16 current ancestry comparison

A fresh live compare of `governance/branch-lifecycle-policy` (PR #15 head) against `docs/repository-audit-and-ai-operating-standard` (PR #16 head) returned:

- Status: `ahead`
- Ahead by: **87 commits**
- Behind by: **0 commits**
- Merge base: `633105210d3a6c4c8e36287ed2dc44dee23f61ef` (the PR #15 head)

This confirms that the PR #15 head remains an ancestor of the current PR #16 branch. The 20.9 reconciliation recorded 85 commits ahead using an earlier PR #16 head snapshot (`6a1a5c7392610ec2f4ff5f365f084995d333bad0`). The new comparison is **87**, so the earlier 85-commit count is retained only as historical evidence and must not be reused as the current count.

The content-level findings in 20.9 remain the documented file comparison: identical PR template; PR #16 branch policy retains PR #15 policy content plus a legacy-routing clarification; PR #16 register retains and extends the PR #15 register. This ancestry comparison does not approve either PR or the proposed branch policy.

### 20.10.4 Long-lived branch drift

A fresh comparison of `develop` to `main` returned:

- `main` is **1 commit ahead** of `develop`.
- `develop` is **0 commits ahead** of `main`.
- The sole main-only file is `docs/reviews/HORTUS-MALABARICUS-VALIDATION-CROSSWALK.md` (187 additions).

The merge base is `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`. This is a real integration/traceability divergence. Do not cherry-pick, rebase, retarget or merge solely to make branch counts or PR metadata look tidy. Review the crosswalk's provenance and intended target through the normal change-control process.

### 20.10.5 Consolidation assessment and recommendations

1. **Do not close PR #15 yet solely because its head is contained in PR #16.** The history/content preservation case is strong, but the owner must decide whether PR #15 should be closed as superseded. Closure is an explicit lifecycle action.
2. **Keep PR #16 as the continuing governance review vehicle, but do not mark it ready or merge it on this audit alone.** Its workflow must be rerun on the current head, and its remaining independent maintainer/legal/policy review gates must be addressed.
3. **Do not delete `governance/branch-lifecycle-policy` as part of this refresh.** First obtain explicit authorization to close PR #15; then verify that no other open PR references its head branch; obtain separate explicit deletion authorization; only then consider deletion.
4. **Treat the 23-to-7 reduction as a controlled sequence, not a cleanup sweep.** Preserve unique content and history, reconcile destination documents, resolve dependent PRs in order, and verify each branch's remaining references before retirement.
5. **Track `main`/ `develop` drift separately.** The Hortus crosswalk is on main only; its presence must be reviewed rather than silently discarded or synchronized.

### 20.10.6 Verification and non-actions

- AI Project Operating Prompt: fetched from `docs/repository-audit-and-ai-operating-standard`; blob SHA `53add3894d0502827e584614c70ad09cadaa637d`. Owner clarification ODR-01 remains limited to controlled, profile-specific external exports; it does not authorize a final export profile, scientific model, physical schema or implementation.
- Branch inventory: 23 live branches; exact names are listed in 20.10.1.
- Open PR inventory: 20 open PRs; PR #15 and PR #16 remain open.
- PR #15 head remains an ancestor of PR #16; current comparison is 87 ahead / 0 behind.
- `main` remains 1 commit ahead of `develop`; the difference is the Hortus Malabaricus crosswalk file.
- No PR was merged, closed, marked ready or retargeted.
- No branch was created, renamed, deleted or force-pushed.
- No repository protection, ruleset, permission, default branch or repository setting was changed.
- No ADR, scientific model, product requirement, policy, strategy or pilot was approved.
- No scientific test, independent specialist review or legal review was performed or claimed.

**Next recommended task:** prepare the PR #15 owner decision (close as superseded or retain) and a separate, file-level governance readiness checklist for PR #16. Do not perform either PR lifecycle action or delete the PR #15 head branch without the required explicit authorization.



## 20.11 Automation-hardening implementation snapshot — 21 November 2026

**Scope:** PR #16 governance automation remediation. This is an append-only current-state record; earlier snapshots above remain historical evidence.

### 20.11.1 Current repository and PR state

- PR #16 remains **open and draft**, targeting `develop`.
- Current PR #16 head: `6f27e14668b4749fa1210f78c00b0d78f2b99e74`.
- PR #16 metadata: 110 commits, 26 changed files, 4,019 additions and 19 deletions.
- Comparison against `develop`: 110 ahead / 0 behind; merge base `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`.
- Live branch inventory remains 23; the no-new-branches and immediate seven-branch directives remain unmet.
- Live open PR inventory remains 20.
- PR #15 remains open and non-draft. Its head `633105210d3a6c4c8e36287ed2dc44dee23f61ef` is still an ancestor of PR #16. Fresh comparison: 92 ahead / 0 behind, merge base equal to PR #15 head.
- `main` remains 1 commit ahead of `develop`, with the Hortus Malabaricus crosswalk as the sole main-only file.

### 20.11.2 Automation changes committed on the existing PR #16 branch

1. `scripts/check_repository_governance.py` now default-denies unsupported PR base branches, permits only exact existing stacked-PR number/base/head combinations, and removes PR-body text as a hotfix authorization input. The owner-approved hotfix allowlist is empty by default.
2. The checker now has a dated 23-branch baseline, rejects unregistered branch names, verifies that `main`, `develop` and `staging` remain present, and warns while the live count exceeds seven. The seven-branch excess is deliberately a warning rather than a hard failure so the cleanup PRs can continue to run. This check detects inventory drift; it does not technically prevent an authorized GitHub user from creating a branch.
3. Markdown fence checking now handles matching backtick/tilde fence characters, minimum closing-fence length, closing-line whitespace and the backtick info-string restriction. Relative-link checks have a documented limited scope and remain advisory.
4. `tests/test_repository_governance.py` adds regression tests for default-deny routing, exact legacy/stacked exceptions, branch inventory, required long-lived branches, fence parsing and relative links.
5. `.github/workflows/repository-governance.yml` sets checkout `persist-credentials: false`, retains `contents: read`, and adds a live branch-inventory step.

### 20.11.3 Exact commit and blob provenance

| File | Commit SHA | Resulting blob SHA |
|---|---|---|
| `scripts/check_repository_governance.py` | `193835b921bc4beaafd80da8de5563373fca23b8` | `7036f21a749326f27a3952504bde42b870e0b8c5` |
| `tests/test_repository_governance.py` | `326dc559c7266025c34021de384193ea1c5a29f7` | `cc96e2b4e2bb3eae7f9b8837cea2254ad5a78dc2` |
| `.github/workflows/repository-governance.yml` | `6f27e14668b4749fa1210f78c00b0d78f2b99e74` | `c977c8209791238da3a213caa9c8b4acf438ae01` |

All three files were fetched again from the target branch after the writes and their resulting blob SHAs were verified. The final workflow commit is the current PR #16 head.

### 20.11.4 Verification status and limitations

- The workflow-run lookup for current head `6f27e14668b4749fa1210f78c00b0d78f2b99e74` returned no PR-triggered run. The previously inspected successful run 44901677252 is associated with the earlier commit `05bf12ec34c724ada2aec3f2631323a12878673f`, not the current head. **Do not report CI as passing on the current head.**
- The three updated files were fetched and their content/blob SHAs verified. This is repository-write verification, not runtime test execution.
- No local test runner or current-head workflow execution was verified in this step. The new tests and branch-inventory API call remain pending execution on the current head.
- The branch baseline is an explicit allowlist. It detects unregistered names during workflow execution but cannot prevent branch creation itself. GitHub rulesets/permissions would be needed for stronger prevention; no such settings were changed.
- The branch count remains 23, so the seven-branch requirement is not met.

### 20.11.5 Non-actions

No PR was merged, closed, marked ready or retargeted. No branch was created, renamed, deleted or force-pushed. No repository protection, ruleset, permission, default branch or repository setting was changed. No ADR, scientific model, product requirement, licensing policy or strategy was approved.

**Next recommended action:** obtain a current-head workflow run and inspect all test/log output; fix any failures before treating this automation pass as validated. Then update the historical governance snapshot cross-references and request independent maintainer review. Keep PR #16 draft and PR #15 open pending explicit owner decisions.


## 20.12 Follow-up live snapshot after governance record addenda — 21 November 2026

This snapshot was taken after the automation implementation and four append-only documentation updates recorded in Section 20.11. It supersedes earlier counts for current-state reporting while preserving those entries as dated snapshots.

- PR #16 remained open and draft, base `develop`, head `71f9c4ade8fce1eb140f825fa858cc88fd0a1f56` at the start of this snapshot.
- PR #16 metadata at that point: 114 commits, 26 changed files, 4,135 additions and 19 deletions.
- PR #16 vs `develop`: 114 ahead / 0 behind; merge base `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`.
- PR #15 remained open, non-draft and unmerged. Its head remained an ancestor of PR #16: 96 ahead / 0 behind, merge base `633105210d3a6c4c8e36287ed2dc44dee23f61ef`.
- Live branch count: 23. Live open PR count: 20.
- `main` remained one commit ahead of `develop`; the sole main-only file remained `docs/reviews/HORTUS-MALABARICUS-VALIDATION-CROSSWALK.md`.
- The complete operating prompt was re-fetched; blob SHA remains `53add3894d0502827e584614c70ad09cadaa637d`.
- Workflow-run lookup for head `71f9c4ade8fce1eb140f825fa858cc88fd0a1f56` returned no PR-triggered workflow run. The successful run 44901677252 belongs to earlier commit `05bf12ec34c724ada2aec3f2631323a12878673f`; it is not evidence of a successful run on the current head.
- The automation files and the four documentation addenda were fetched after their writes and blob SHAs verified. Runtime execution of the newly expanded tests and branch inventory step remains pending.

**No lifecycle action:** no PR was merged, closed, marked ready or retargeted; no branch was created, renamed, deleted or force-pushed; no repository protection, ruleset, permission or setting was changed; no ADR, policy, scientific model or product requirement was approved.

**Next gate:** obtain and inspect a successful current-head workflow run, then request independent maintainer review. Keep PR #16 draft and PR #15 open until the relevant owner decisions are made.


## 20.13 Current-head automation verification — 21 November 2026

The current automation implementation was executed successfully on PR #16 head `c037c66865a5b576ef3a74717d803b941fb0a878`.

- Workflow run: [44906508756](https://github.com/Save-Tiger-First/botanica-indica/actions/runs/44906508756)
- Event: `pull_request`
- Workflow: Repository governance
- Job: Markdown integrity and branch routing
- Conclusion: **success**
- Unit tests: **27 passed**, including routing, exact legacy/stacked exceptions, branch inventory, fenced-code parsing and relative-link checks.
- Markdown scan: **23 tracked Markdown files**.
- Routing check: passed for PR #16 targeting `develop`.
- Live branch API check: successfully retrieved **23 branches**.
- Branch-count output: warning that 23 exceeds the seven-branch ceiling; this is expected and correctly non-blocking during preservation-first cleanup.
- No Python regex FutureWarning appeared in the inspected job output.

The job log and step conclusions were inspected. This verifies the current code and workflow on commit `c037c66865a5b576ef3a74717d803b941fb0a878`; it does not certify branch-creation prevention, repository ruleset configuration, independent review, legal compliance or scientific correctness.

The workflow remains a monitoring/routing control. The live branch count remains 23. No PR or branch lifecycle action was taken.


## 20.14 Workflow activation and latest PR metadata clarification — 21 November 2026

At the time of this addendum, PR #16 remained open/draft with head `a7284da4e2b8910d57e98ca7c7beb7124c0817a1`, 117 commits, 26 changed files, 4,196 additions and 19 deletions. It was 117 commits ahead / 0 behind `develop`. PR #15's head remained an ancestor (99 ahead / 0 behind). Live repository inventory remained 23 branches and 20 open PRs.

The successful run 44906508756 validated the code-bearing commit `c037c66865a5b576ef3a74717d803b941fb0a878`: 27 tests passed, 23 Markdown files scanned, PR routing passed, and the live branch API returned 23 branches with the expected seven-branch warning. Later commits were documentation-only.

**Activation limitation:** the workflow file is proposed on PR #16 and is not yet present on `main`. Therefore the `create` event cannot be relied upon to detect standalone branch creation until a copy of this workflow exists on the default branch. The pull-request run did execute the live inventory check, so an unregistered branch used by a PR is detected. This is not branch-creation prevention and does not enforce the seven-branch ceiling. Do not merge PR #16 merely to activate this trigger; repository protections and owner authorization remain separate decisions.

No PR or branch lifecycle action was taken; no repository settings were changed.


## 20.15 Workflow verification after workflow-activation clarification — 21 November 2026

The workflow completed successfully on PR #16 head `63bc943ccdce3cdfde5a2af48e549ac374f3873c`.

- Run: [44906587030](https://github.com/Save-Tiger-First/botanica-indica/actions/runs/44906587030)
- Event: `pull_request`; conclusion: **success**.
- Unit tests: **27 passed**.
- Markdown scan: **23 tracked Markdown files**.
- PR #16 routing validation: passed.
- Live GitHub branch inventory: 23 branches; the seven-branch ceiling warning was emitted as designed.
- No `FutureWarning` appeared in the inspected job log.

This validates the automation and workflow at commit `63bc943ccdce3cdfde5a2af48e549ac374f3873c`. The `create` trigger limitation remains as described in Section 20.14. The workflow is not a branch-creation prevention mechanism, and the seven-branch target remains unmet.


## 20.16 Final verification of PR #16 documentation head — 21 November 2026

The subsequent documentation-only head `8771925b6b1e8a8b590a775d36bec537da43e37b` also completed the governance workflow successfully:

- Run: [44906629254](https://github.com/Save-Tiger-First/botanica-indica/actions/runs/44906629254)
- Event: `pull_request`; job and run conclusion: **success**.
- Unit tests: **27 passed**.
- Markdown scan: **23 tracked Markdown files**.
- PR #16 routing validation: passed.
- Live branch inventory: 23 branches; seven-branch excess warning emitted.
- No Python `FutureWarning` appeared in the job log.

This verifies the PR #16 head before this append-only record. The workflow remains a monitoring/routing control, not a branch-creation prevention mechanism. No PR or branch lifecycle action was taken.

## 20.17 Live branch consolidation audit and next-step plan — 21 November 2026

Fresh GitHub reads re-verified the branch collection, PRs, refs, comparisons, changed-file lists, selected documents and active repository ruleset. Earlier snapshots remain historical.

### 20.17.1 Current repository state

- Repository: Save-Tiger-First/botanica-indica; default branch: main.
- Live branches: **23** (3 long-lived + 20 temporary); ceiling: **7**; excess: **16**.
- Live open PRs: **20**; all unmerged. PR #16 remains open/draft; PR #15 remains open/non-draft.
- PR #16 head after documentation corrections: f6f661b97376323aba36b91725aca483af9e7d35; 125 commits, 26 changed files, 4,291 additions and 25 deletions; 125 ahead / 0 behind develop.
- PR #15 head 633105210d3a6c4c8e36287ed2dc44dee23f61ef is an ancestor of PR #16 (105 ahead / 0 behind).
- PR #1 head 15fd4edef9afa8d22df9e23f66296ef09423d8cf and PR #2 head e900b64c90df08f5c98181af54bf2ab0b7096759 are also ancestors of PR #16 (each 122 ahead / 0 behind).
- main is 1 commit ahead / 0 behind develop; its sole main-only file is docs/reviews/HORTUS-MALABARICUS-VALIDATION-CROSSWALK.md. The copy on the scientific review branch has a different blob and 83 differing lines. Reconcile before treating PR #9 as merge-ready.
- All three required long-lived branches exist. Branch API flags main protected and develop/staging unprotected.

### 20.17.2 Active repository ruleset and protection limits

The only active repository ruleset returned was ID 23822734, “Protect main branch”, targeting the default branch. Its visible rules are deletion and non-fast-forward protection only. It does not list required reviews or required status checks. The branch-protection endpoint for develop returned 403 “Resource not accessible by integration”; therefore full effective protection settings could not be inspected. No ruleset or protection settings were changed.

Recommendation: before enabling a required-check policy, inspect all effective settings using an appropriately authorized maintainer account and design protections for develop and staging. Do not infer full protection from the GitHub branch API boolean flag.

### 20.17.3 Proposed four retained workstreams and 16 source branches

The four retained workstream branches remain provisional destinations. This map identifies source branches and PRs, not authorization to merge or delete.

| Retained destination | Source branch / PR | Source-only commits relative to destination | Disposition / critical condition |
|---|---|---:|---|
| docs/repository-audit-and-ai-operating-standard | governance/branch-lifecycle-policy / #15 | 0 | Original head is already an ancestor; preserve review/owner decision before closing #15 and retiring its branch |
| same | docs/asset-specific-licensing-policy / #1 | 0 | Original head is already an ancestor; policy remains proposed and requires qualified legal review |
| same | docs/adr-011-stf-ecosystem-boundaries / #2 | 0 | Original head is already an ancestor; ADR-011 remains proposed |
| docs/full-system-architecture-and-repo-engineering-plan | docs/full-product-vision-capability-blueprint / #17 | 9 | Diverged histories; preserve source history and reconcile product scope |
| same | docs/canonical-task-03-04-baselines / #18 | 2 | Diverged histories; preserve original Task 03/04 source baselines |
| same | docs/requirements-traceability-register / #19 | 27 | Diverged histories; preserve requirements, acceptance tests, workflow and offline-sync contracts |
| review/scientific-data-model-review-pack | docs/task-05-data-architecture / #3 | 5 | Preserve parent scientific architecture and reconcile with review pack |
| same | docs/task-05-data-dictionary / #4 | 14 | Preserve Task 05B definitions and Indian test cases |
| same | docs/task-05c-logical-data-model / #5 | 10 | Candidate A; preserve and compare with Candidate B |
| same | docs/task-05c-logical-database-model / #21 | 1 | Candidate B; preserve as a competing model, not an approved duplicate |
| same | docs/task-05d-logical-model-validation / #22 | 7 | Preserve v1 validation findings and its differing Task 05C file |
| same | docs/task-05d-logical-model-validation-v2 / #23 | 7 | Preserve v2; not byte-identical to v1 or v3 |
| same | docs/task-05d-logical-model-validation-v3 / #11 | 13 | Preserve v3 and resolve its stacked dependency on PR #5 |
| strategy/naturetech-biodiversity-conservation-impact | governance/stf-organisational-readiness-review / #12 | 4 | Diverged histories and overlapping edits in two strategy files; reconcile line-by-line |
| same | proposal/bengaluru-urban-biodiversity-feasibility-pilot / #13 | 1 | Preserve feasibility proposal; no programme or fieldwork approval implied |
| same | research/bengaluru-pilot-site-selection / #14 | 1 | Preserve site assessment; no site selection or permission implied |

Source-only counts are fresh compare results in the direction source branch to destination branch. They are Git ancestry counts, not unique-file counts or content approval. Inspect full commit graphs and changed-file contents before any history-preserving integration.

### 20.17.4 Competing document and cross-branch conflicts

1. Task 05C Candidate A (docs/architecture/TASK-05C-LOGICAL-DATABASE-MODEL.md, blob b447796e7da0d08d96400812667a8e67e0696144) and Candidate B (docs/data-architecture/TASK-05C-LOGICAL-DATABASE-MODEL-AND-SCIENTIFIC-RELATIONSHIPS.md, blob 239d7e9974bcb81b1154b54845a7b2d69c3775d6) are different documents. Neither is approved.
2. Task 05D v1 blob a194d8ed4c98bb3cda6834c73ce73c8f6e03eb4f (29,326 characters), v2 blob acf446b1bf0204fa0400621711603ab23cc80ff2 (29,512 characters), and v3 blob 0b9a009b1c543b2450758f659c97cae3802a2f94 (44,958 characters) are different revisions. Their embedded Task 05C copies also differ. Preserve all unique decisions and test cases before selecting a canonical revision.
3. PR #12's organisational-readiness branch modifies two strategy files also present on the strategy destination. These are not safe to overwrite wholesale.
4. The Hortus crosswalk on main and PR #9 differ (83 changed lines; different blob SHAs). Keep the main copy reachable and reconcile it with the expanded PR #9 version.
5. PRs #17–#20 have diverged histories. Reconcile the full-product blueprint, original Task 03/04 baselines, RTM, acceptance plan, API idempotency and offline synchronization specifications.

### 20.17.5 Workflow and contributor guidance

- CONTRIBUTING.md now states that the current no-new-branches directive overrides generic feature/fix branch guidance; it requires reuse of an approved existing workstream or stopping for explicit owner authorization.
- STF-ECOSYSTEM-BOUNDARIES.md now lists ADR-011 as a related proposal while retaining Proposed status.
- The governance workflow is still only on PR #16, not main. Treat its create event as unverified for pre-merge enforcement; regardless, it is detection, not prevention.
- The workflow does not make the seven-branch excess a failing condition; it warns so cleanup PRs can proceed.
- The visible main ruleset has no review/status-check requirements; full protection configuration for other branches could not be inspected.

### 20.17.6 Safe consolidation sequence

1. Keep the four provisional destination branches and three long-lived branches. Create no new branch.
2. Resolve PR #16 review readiness and obtain independent maintainer review. PRs #1, #2 and #15 are already ancestors of the governance destination; retain them until their content/policy reviews and owner disposition are complete.
3. On the existing product/architecture destination, preserve source commit ancestry for #17–#19 using owner-authorized history-preserving integrations; reconcile their documents and PR dependencies.
4. On the existing scientific destination, preserve source histories for #3–#5, #11 and #21–#23. Compare Candidate A/B and all Task 05D revisions. Resolve scientific decision-register items and the Hortus crosswalk divergence; obtain specialist review before scientific approval.
5. On the existing strategy destination, reconcile PR #12's overlapping edits and preserve PR #13/#14 proposal/research content. Keep no-site-selected/no-fieldwork-authorized status until gates are met.
6. For every source PR: verify destination tree/content, source-head ancestry, no unique unpreserved commit, no other open PR dependency, and explicit owner disposition. Only then request approval to close its PR and delete its own head branch.
7. After each authorized retirement, re-fetch branch and PR inventories; update the allowlist and provenance record only after the live ref is gone.
8. Target no more than seven branches (three long-lived plus four workstream branches). At formal completion, apply the one-branch-only rule and retain only main.

No consolidation merges, PR closures, branch deletions, retargeting, ruleset changes or approvals were performed in this audit.

## 20.18 Latest-head verification after consolidation documentation updates — 21 November 2026

PR #16 current head at this verification: 0e5d3ac070932bdbe0a98c7cc824a71d15dc1745; open/draft, base develop, 129 commits, 26 changed files, 4,428 additions and 25 deletions; 129 ahead / 0 behind develop.

Workflow run 44908219565 completed successfully on this exact head:
- 27 unit tests passed.
- 23 tracked Markdown files scanned.
- PR #16 routing validation passed.
- Live branch inventory retrieved 23 branches.
- Expected warning: 23 exceeds the seven-branch ceiling.
- No Python FutureWarning appeared in the inspected job log.

The seven-branch target remains unmet. This run verifies the current automation on the recorded head; it does not certify independent review, repository-wide branch creation prevention, scientific/legal approval or branch protection beyond the visible ruleset. No PR or branch lifecycle action was taken.

## 20.19 Final current-head CI confirmation — 21 November 2026

The documentation head 32b5fa0f5f192fa3d3948038a79a10ae41b5c630 completed workflow run 44908268217 successfully. The run verified 27 unit tests, 23 tracked Markdown files, PR #16 routing, and live branch inventory retrieval (23 branches). The expected warning that 23 exceeds the seven-branch ceiling appeared. No Python FutureWarning appeared in the inspected job log.

This result applies to head 32b5fa0f5f192fa3d3948038a79a10ae41b5c630, before this final append-only record. The seven-branch target remains unmet; no PR or branch lifecycle action was taken.


## 20.20 Current branch-to-main consolidation baseline — 21 November 2026

This section supersedes earlier live-state snapshots (including 20.18 and 20.19) for the values below. The complete governing prompt was re-fetched from this branch: 259 lines, blob SHA `53add3894d0502827e584614c70ad09cadaa637d`.

### 20.20.1 Current refs and inventory

- Repository: `Save-Tiger-First/botanica-indica`.
- Branch count: **23** — exactly 3 long-lived branches and 20 temporary/workstream branches. The immediate owner ceiling is 7, so 16 branches must be safely retired after preservation and approval.
- `main`: `6f2f51da093caf8183fde386dbec707cc6046d27` (protected).
- `develop`: `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` (API reports unprotected).
- `staging`: `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` (API reports unprotected; identical to develop at this snapshot).
- `docs/repository-audit-and-ai-operating-standard`: `5797330bac2735b5f35054d39a7ade4243de84ec`.
- PR #16 is open/draft, targets `develop`, and has head `5797330bac2735b5f35054d39a7ade4243de84ec`; 134 commits, 26 changed files, 4,466 additions, 25 deletions; compare to develop is 134 ahead / 0 behind.
- Workflow run 44908360788 completed successfully on that exact PR #16 head. It passed 27 tests, checked 23 tracked Markdown files, passed routing validation and retrieved the live branch count; the expected warning for 23 branches exceeding the seven-branch ceiling appeared.
- PR #15 remains open/non-draft. PRs #1–#5, #8–#14, and #16–#23 remain open/draft. No PR has been merged in this consolidation exercise.

### 20.20.2 Current PR routing

The 20 open PRs do not yet follow the operating prompt's default promotion flow consistently:

| Current base | PRs | Assessment |
|---|---|---|
| `develop` | #15, #16, #17, #18, #19, #20 | Correct integration destination in principle; still requires review and acceptance |
| `main` | #1, #2, #3, #4, #5, #8, #9, #13, #14 | Direct-to-main routing conflicts with the documented task → develop → staging → main workflow; do not merge directly |
| Stacked on another workstream | #11 (base #5 branch), #12 (strategy branch), #21, #22, #23 (scientific review branch) | Dependencies must be resolved in order; do not flatten or retarget blindly |

Any PR retargeting requires an explicit owner decision. Draft PRs cannot be merged under GitHub's normal pull-request workflow. PR #16 must remain draft until its governance content has independent review and the owner approves the next state.

### 20.20.3 Fresh source-to-workstream comparisons

Current comparisons were run from each existing source branch to its proposed existing workstream destination. “Ahead” is source-only commit count; “behind” is destination-only commit count.

| PR | Source branch | Existing destination | Ahead | Behind | Status |
|---|---|---|---:|---:|---|
| #15 | `governance/branch-lifecycle-policy` | governance | 0 | 116 | source head already contained |
| #1 | `docs/asset-specific-licensing-policy` | governance | 0 | 133 | source head already contained |
| #2 | `docs/adr-011-stf-ecosystem-boundaries` | governance | 0 | 133 | source head already contained |
| #17 | `docs/full-product-vision-capability-blueprint` | product/architecture | 9 | 12 | diverged |
| #18 | `docs/canonical-task-03-04-baselines` | product/architecture | 2 | 12 | diverged |
| #19 | `docs/requirements-traceability-register` | product/architecture | 27 | 12 | diverged |
| #3 | `docs/task-05-data-architecture` | scientific review | 5 | 67 | diverged |
| #4 | `docs/task-05-data-dictionary` | scientific review | 14 | 67 | diverged |
| #5 | `docs/task-05c-logical-data-model` | scientific review | 10 | 67 | diverged |
| #21 | `docs/task-05c-logical-database-model` | scientific review | 1 | 67 | diverged |
| #22 | `docs/task-05d-logical-model-validation` | scientific review | 7 | 67 | diverged |
| #23 | `docs/task-05d-logical-model-validation-v2` | scientific review | 7 | 67 | diverged |
| #11 | `docs/task-05d-logical-model-validation-v3` | scientific review | 13 | 67 | diverged |
| #12 | `governance/stf-organisational-readiness-review` | STF strategy | 4 | 3 | diverged |
| #13 | `proposal/bengaluru-urban-biodiversity-feasibility-pilot` | STF strategy | 1 | 24 | diverged |
| #14 | `research/bengaluru-pilot-site-selection` | STF strategy | 1 | 24 | diverged |

These are ancestry comparisons, not content approval. Divergence means both sides contain unique commits. Preserve all unique source commits and reconcile changed files before integration. The three governance source heads being contained does not mean their PRs are approved or may be closed.

### 20.20.4 Main/develop/staging synchronization

- `main` is 1 commit ahead and 0 behind `develop`; its only main-only file is `docs/reviews/HORTUS-MALABARICUS-VALIDATION-CROSSWALK.md` (187 additions).
- The scientific review branch contains a different version of that crosswalk. Preserve both and reconcile the scientific content before any scientific-workstream promotion.
- `staging` and `develop` currently point to the same commit. They are not yet a tested release-candidate promotion.

### 20.20.5 Recommended route to a single main branch

1. Freeze branch creation and preserve a verified inventory/backup of all refs.
2. Complete PR #16 governance review; resolve its draft status only after independent review and owner decision. Resolve the already-contained PRs #15, #1 and #2 through separate documented decisions; do not close them merely because their commits are ancestors.
3. Preserve and reconcile the product sources #17–#19 on the existing product/architecture destination.
4. Preserve and reconcile scientific sources #3–#5, #11 and #21–#23 on the existing scientific review destination. Keep competing Task 05C and Task 05D versions visible until scientific review resolves them. Reconcile the Hortus crosswalk.
5. Preserve and reconcile strategy sources #12–#14 on the existing strategy destination; no pilot/site/fieldwork approval is implied.
6. Once each workstream is coherent and reviewed, integrate its accepted content into `develop` via reviewed PRs. Resolve the current direct-to-main and stacked-PR routing conflicts through explicit owner-approved PR handling; do not bypass review.
7. Reconcile the main-only Hortus crosswalk into the integration history without losing its provenance; confirm `develop` is the complete integration baseline.
8. Promote `develop` to `staging` through a release-candidate PR and run full integrated, scientific, security, rights, privacy, accessibility and operational acceptance checks.
9. Promote the accepted `staging` release to `main) through a reviewed PR. Verify the exact resulting main tree and release record.
10. Retire temporary workstream/source branches only after every source commit and unique file is preserved, dependent PRs are resolved, and the owner explicitly authorizes each retirement. During active development, stop at the seven-branch ceiling (3 long-lived + 4 workstreams).
11. At formal project completion only, verify all work is on `main`, resolve all PRs, archive/tag the final state and obtain owner approval; then retire `develop`, `staging` and all remaining workstream branches. Re-fetch the branch list and verify exactly one branch remains: `main`.

**No merge, retarget, PR closure, branch deletion, protection change or scientific/policy approval was performed while preparing this baseline.**
