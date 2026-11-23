# PR #15 / PR #16 — Governance Content and History Reconciliation

- **Document ID:** STF-GOV-REC-015-016
- **Version:** 1.0
- **Prepared:** 21 November 2026
- **Status:** Verified content/history audit; proposed PR disposition; owner authorization required for lifecycle actions
- **Repository:** `Save-Tiger-First/botanica-indica`
- **Audit branch:** `docs/repository-audit-and-ai-operating-standard`
- **Related PRs:** [#15](https://github.com/Save-Tiger-First/botanica-indica/pull/15), [#16](https://github.com/Save-Tiger-First/botanica-indica/pull/16)

## 1. Executive conclusion

The governance content and commit history introduced by PR #15 have been preserved on the existing PR #16 branch. PR #16 is a strict content superset for the three overlapping paths: the pull-request template is byte-identical, the branch governance policy retains PR #15's content and adds a legacy-routing section, and the branch inventory retains the earlier content while correcting a Task 05D version statement and adding subsequent audit snapshots.

The Git commit graph independently confirms preservation of PR #15's entire head history: comparing PR #15 head `633105210d3a6c4c8e36287ed2dc44dee23f61ef` to PR #16 head `6a1a5c7392610ec2f4ff5f365f084995d333bad0` returns **85 commits ahead, 0 behind**, with PR #15 head as the merge base. Therefore PR #15's head commit is an ancestor of PR #16's current head.

**Recommendation:** treat PR #15 as a superseded, content- and history-preserved governance workstream, with PR #16 as the continuing governance review vehicle. This is a proposed disposition only. Do not merge or close PR #15, close PR #16, or delete either branch without explicit owner authorization.

## 2. Exact source state inspected

| Item | PR #15 | PR #16 |
|---|---|---|
| State | Open, not draft | Open, draft |
| Base | `develop` | `develop` |
| Base SHA | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` |
| Head branch | `governance/branch-lifecycle-policy` | `docs/repository-audit-and-ai-operating-standard` |
| Head SHA | `633105210d3a6c4c8e36287ed2dc44dee23f61ef` | `6a1a5c7392610ec2f4ff5f365f084995d333bad0` |
| Commits | 18 | 103 |
| Changed files | 3 | 24 |

All values above were fetched from live PR metadata immediately before preparing this reconciliation.

## 3. File-level disposition

| Path | PR #15 blob SHA | PR #16 blob SHA | Comparison | Proposed disposition |
|---|---|---|---|---|
| `.github/pull_request_template.md` | `1b2a71bb968cb892bc229c5ce8ac5ffb4b3d1084` | `1b2a71bb968cb892bc229c5ce8ac5ffb4b3d1084` | Exact byte-identical content (28 lines) | Retain PR #16 copy; PR #15 contribution fully represented |
| `docs/governance/BRANCHING-AND-RELEASE-GOVERNANCE.md` | `baf085de8baea1ec7becfc15ce3f691512e91aba` | `34113278067336572529fe61e647d9c28bdf4042` | PR #16 retains the PR #15 policy content and adds Section 4.1, “Temporary grandfathering of existing direct-to-main PRs” (20 added lines; no PR #15 policy lines removed) | Retain PR #16 version as the current governance review copy; keep grandfathering narrowly scoped to exact legacy PR/head pairs |
| `docs/governance/BRANCH-INVENTORY-AND-CONSOLIDATION-REGISTER.md` | `9233910471f0806435cb39c47ff074e90d382e47` | `2d5bec2b22fb7f14edf8243ce3473f2e00b1d140` | PR #16 retains the PR #15 register, replaces a three-line incorrect v2/v3 byte-identical claim with corrected blob/length evidence, and appends live audit history through Section 20.8 | Retain PR #16 version; it is the materially more complete and corrected register |

### 3.1 Pull-request template

The two versions are byte-identical. No merge conflict or content decision is required.

### 3.2 Branching and release governance

PR #16 adds a narrowly scoped Section 4.1 listing the nine pre-existing direct-to-main PR/head pairs. The section explicitly says grandfathering is for informational CI recognition only; it is not merge approval, a precedent for new PRs or a waiver of owner approval. It directs that entries be removed when their PR is retargeted or closed.

This is a useful compatibility clarification for the current legacy PR set. It does not change the three-long-lived-branch rule, seven-branch ceiling, no-new-branches directive or one-branch completion requirement.

### 3.3 Branch inventory and consolidation register

The PR #16 register corrects an earlier inaccurate statement that the Task 05D v2 and v3 documents were byte-identical. It records their different blob SHAs and character lengths, and requires section-by-section comparison of both Task 05C and Task 05D material before any retirement decision.

PR #16 also carries the subsequent live branch/PR snapshots, scientific review status, ODR-01 boundary, dependency comparisons and branch retirement safeguards. The historical PR #15 file is preserved in Git history; the current PR #16 file is the preferred working register.

## 4. Commit-history preservation

The direct GitHub compare of PR #15 head to PR #16 head returned:

- Status: `ahead`
- Ahead by: `85`
- Behind by: `0`
- Total commits after merge base: `85`
- Merge base: `633105210d3a6c4c8e36287ed2dc44dee23f61ef` (the PR #15 head itself)

This establishes that PR #15's 18-commit head is contained in PR #16's ancestry. It is stronger than a file-copy-only assertion: the original PR #15 commit chain is preserved in the PR #16 branch history. The PR #16 branch also includes the later governance, licensing and ecosystem-boundary preservation commits and subsequent audit work.

The existing `docs/governance/BRANCH-CONSOLIDATION-PROVENANCE.md` remains the detailed content-transfer register. This document adds a current PR #15/#16 comparison and does not rewrite the prior provenance entries.

## 5. Decision and approval boundaries

**Verified facts:**
- PR #15 is open and non-draft; PR #16 is open and draft.
- Both target `develop` at the same base SHA.
- All three overlapping file paths are present in PR #16.
- The PR template is byte-identical.
- The PR #16 branch governance policy contains the PR #15 policy content plus the additional Section 4.1.
- The PR #16 branch inventory contains the PR #15 register with a documented correction and subsequent append-only updates.
- PR #15's head commit is an ancestor of PR #16's current head.

**Not established by this audit:**
- That either PR has received the required independent review or owner approval.
- That the proposed branch policy, licensing policy or ADR-011 has been adopted.
- That PR #16 is ready to merge.
- That any source branch can be deleted without checking all current open-PR references and obtaining authorization.

## 6. Proposed PR and branch disposition

| Item | Recommendation | Required approval / gate |
|---|---|---|
| PR #15 | Mark as superseded by PR #16 and close without merging, after recording this reconciliation in the PR conversation | Explicit project-owner authorization to close |
| `governance/branch-lifecycle-policy` | Retain until PR #15 is formally resolved; then consider deleting its head branch | Explicit authorization to delete; recheck no other open PR references it |
| PR #16 | Continue as the single governance review vehicle; keep draft until its own outstanding review gates are satisfied | Independent review and explicit owner approval before marking ready/merging |
| `docs/repository-audit-and-ai-operating-standard` | Retain as the current governance workstream branch | No branch retirement now |
| Policy/ADR status | Keep branch policy proposed; keep licensing policy and ADR-011 proposed | Separate explicit policy/ADR decisions; consolidation is not approval |

Closing PR #15 and deleting its head branch would reduce the live branch count by one only after the required approvals. The branch count remains 23 until such an authorized retirement is actually completed and verified.

## 7. Remaining PR #16 review gates

This reconciliation does not declare PR #16 review-ready. The existing PR #16 audit records additional review gates, including:
1. Re-run and verify the governance workflow on the final PR #16 head.
2. Review the legacy direct-to-main allowlist and remove entries when PRs are retargeted or closed.
3. Obtain qualified Indian legal review of contributor terms, copyright, DPDP and biodiversity/ABS applicability before relevant external activity.
4. Obtain independent maintainer review of the proposed governance materials.
5. Keep licensing policy and ADR-011 proposed until their own review and decision processes are complete.

The governance workflow's successful historical runs do not automatically verify every later commit or substitute for review.

## 8. Actions and non-actions

- This document records a content and commit-history reconciliation proposal.
- No PR was merged, closed, marked ready or retargeted.
- No branch was created, renamed, deleted or force-pushed.
- No ruleset, branch protection, repository permission or default branch changed.
- No policy, ADR, scientific model or product requirement was approved.
- No legal opinion, compliance certification or independent review is claimed.

**Final assessment:** PR #15's content and complete head ancestry are preserved in PR #16. PR #15 is now a reasonable candidate for owner-authorized closure as superseded, but not for merge merely to retire the branch. PR #16 remains the active governance review vehicle and must pass its own review gates.



## Current-state addendum — 21 November 2026, after automation hardening

The exact values in Sections 1–4 above are historical snapshots and are not overwritten. Current state has been re-fetched and is recorded in the Branch Inventory and Consolidation Register Section 20.11.

- PR #16 remains open and draft, base `develop`, current head `6f27e14668b4749fa1210f78c00b0d78f2b99e74`; 110 commits, 26 changed files, 4,019 additions and 19 deletions.
- PR #16 compares 110 ahead / 0 behind `develop`.
- PR #15 remains open, non-draft, unmerged; its head remains an ancestor of PR #16 (fresh compare 92 ahead / 0 behind).
- Live inventory remains 23 branches and 20 open PRs.
- `main` remains one commit ahead of `develop` due to `docs/reviews/HORTUS-MALABARICUS-VALIDATION-CROSSWALK.md`.
- The PR #16 branch now contains the automation-hardening commits and a dated 23-branch baseline. Current-head CI is not yet verified; the previous successful workflow run belongs to an earlier head.
- No PR was merged or closed, no branch was created or deleted, and no policy or ADR was approved.

For current review findings and next actions, see `docs/reviews/PR-16-GOVERNANCE-READINESS-REVIEW-2026-11-21.md` Section 10. Preserve the earlier source SHAs and counts above as historical provenance.

## Current governance ancestry refresh — 21 November 2026

A fresh compare confirms the source heads of PR #15 (633105210d3a6c4c8e36287ed2dc44dee23f61ef), PR #1 (15fd4edef9afa8d22df9e23f66296ef09423d8cf) and PR #2 (e900b64c90df08f5c98181af54bf2ab0b7096759) are all ancestors of the current PR #16 branch. The respective destination comparisons are 105, 122 and 122 commits ahead / 0 behind.

This ancestry preservation does not resolve the source PRs. PR #15 remains open/non-draft; PRs #1 and #2 remain open/draft. The licensing policy and ADR-011 remain proposals, not approvals. Their PR closure and source-branch retirement require separate owner authorization after review.
