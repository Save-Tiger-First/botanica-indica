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
