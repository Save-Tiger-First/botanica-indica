# Branch Consolidation Provenance Register

**Repository:** Save-Tiger-First/botanica-indica  
**Recorded:** 20 November 2026  
**Status:** Content copied to the existing PR #16 branch; source branches and PRs remain open. No branch history has been rewritten, no PR has been merged or closed, and no branch has been deleted.

## Purpose

Record exact source blob identifiers and destination commits for preservation-first content consolidation. This register proves which file contents were copied; it does not claim that the original source commit histories were transferred. The source branches remain available for review until their PRs are formally resolved.

## Verified content transfers

| File | Source branch | Source blob SHA | Destination branch | Destination commit SHA | Source PR |
|---|---|---|---|---|---:|
| `.github/pull_request_template.md` | `governance/branch-lifecycle-policy` | `1b2a71bb968cb892bc229c5ce8ac5ffb4b3d1084` | `docs/repository-audit-and-ai-operating-standard` | `cb65eb2d885db9e51255e44e39aa500e88b51725` | #15 |
| `docs/governance/BRANCH-INVENTORY-AND-CONSOLIDATION-REGISTER.md` | `governance/branch-lifecycle-policy` | `9233910471f0806435cb39c47ff074e90d382e47` | `docs/repository-audit-and-ai-operating-standard` | `db96677ffdaf10c1ae309cee6362b92c0b53e807` | #15 |
| `docs/governance/BRANCHING-AND-RELEASE-GOVERNANCE.md` | `governance/branch-lifecycle-policy` | `baf085de8baea1ec7becfc15ce3f691512e91aba` | `docs/repository-audit-and-ai-operating-standard` | `bef3b2d70629902b805b2b743657ff0e7411d262` | #15 |
| `docs/governance/LICENSING-AND-IP-POLICY.md` | `docs/asset-specific-licensing-policy` | `b24e479559eaa6022fdc37db7ea65ded30a7c23e` | `docs/repository-audit-and-ai-operating-standard` | `64da21bd32d20210b42935603a31ea610f5c9317` | #1 |
| `docs/adr/ADR-011-stf-ecosystem-boundaries.md` | `docs/adr-011-stf-ecosystem-boundaries` | `92c3fb551c1b0e367d748f76ce8e835959ed3957` | `docs/repository-audit-and-ai-operating-standard` | `6d2359a6be8d99da6ac730bde4189e5b1dca2f5b` | #2 |

The source files were fetched immediately before copying and their blob SHAs were checked against the recorded values. Each destination commit was subsequently fetched by exact SHA; GitHub reported the expected file path as the sole changed file in each commit.

## Governance and review status

- PR #16 remains open and draft. Its current head is `6d2359a6be8d99da6ac730bde4189e5b1dca2f5b`.
- PR #15 remains open and non-draft. Its source branch still carries the original governance files and has not been retired.
- PR #1 remains open and draft. The licensing/IP policy remains **proposed**, not approved or legal advice.
- PR #2 remains open and draft. ADR-011 remains **proposed**, not accepted.
- Copying content into PR #16 does not approve either proposal, merge any PR, or authorize deletion of any source branch.
- Original Git commit ancestry is not copied by file-content transfer. The source blob SHA and destination commit SHA above provide a verifiable content-provenance trail.

## Repository state at recording

The live repository still contains 23 branches: three designated long-lived branches and 20 temporary branches. There are 20 open PRs. No branch was created, merged, closed or deleted as part of this consolidation.

## Next retirement gates

1. Review the copied documents in PR #16 for consistency with the operating prompt and accepted ADRs.
2. Resolve PR #15's governance changes through the approved review path.
3. Resolve PRs #1 and #2 without treating copied content as approval.
4. Obtain the required explicit approval before merging or closing any of these PRs.
5. Delete a source branch only after its PR is resolved, no other open PR references that branch, and the live repository confirms the branch can safely be retired.
6. Re-fetch the complete branch list after every retirement operation.


## Governance source-history and review audit — 21 November 2026

**Scope:** PRs #1, #2 and #15 were compared with the existing PR #16 destination branch. The complete AI Project Operating Prompt was re-fetched from `docs/governance/AI-PROJECT-OPERATING-PROMPT.md` on `docs/repository-audit-and-ai-operating-standard` (blob SHA `ec100aec5abc09ec04ad9f4a084a0aa95a7c7558`). The live PR #16 head at audit time was `1a8a52284b7a159f8ba08b8b912f6413ec99047c`.

### Verified source PR state

| PR | Source branch | Source head / commit | State at audit | Review record |
|---|---|---|---|---|
| #1 | `docs/asset-specific-licensing-policy` | `15fd4edef9afa8d22df9e23f66296ef09423d8cf` (1 commit) | Open, draft, unmerged; base `main` | 0 issue comments, 0 submitted reviews, 0 inline review threads |
| #2 | `docs/adr-011-stf-ecosystem-boundaries` | `e900b64c90df08f5c98181af54bf2ab0b7096759` (1 commit) | Open, draft, unmerged; base `main` | 0 issue comments, 0 submitted reviews, 0 inline review threads |
| #15 | `governance/branch-lifecycle-policy` | `633105210d3a6c4c8e36287ed2dc44dee23f61ef` (18 commits) | Open, non-draft, unmerged; base `develop` | 0 issue comments, 0 submitted reviews, 0 inline review threads |
| #16 | `docs/repository-audit-and-ai-operating-standard` | `1a8a52284b7a159f8ba08b8b912f6413ec99047c` (40 commits) | Open, draft, unmerged; base `develop` | 0 issue comments, 0 submitted reviews, 0 inline review threads |

### Source commit history for PR #15

The 18 commits on PR #15 form a linear chain from the original parent `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` to head `633105210d3a6c4c8e36287ed2dc44dee23f61ef`. The source commits, in chronological order, are:

1. `9abb8a1b8de930cd09219c2187b799cc9218d203` — define branch lifecycle and one-branch completion policy
2. `f04c0e08b543b9783fd6d949af91ff3da4a4fdca` — add pull request governance template
3. `56322dccdb9f9c1f15d4659f2fd8bdf969179b71` — add preservation-first branch consolidation register
4. `f0fd73486ed077ca91277423ab09f66461a55a5b` — align branch register with scientific review dispositions
5. `e2af4281a675e1ab942c0604501c46feb807a5ac` — correct verified branch inventory count
6. `b4e0c19a594d5a35172d53513e99ef02e9cf6aa0` — refresh branch and PR inventory after audit PR
7. `dcecf8d16b4cfec93e03c06a1d55f728b5a1421b` — align scientific review status with corrected TDWG verification
8. `70743ceff66eeebe2d2dc31bd06c681643b7a63b` — add PR #16 to branch consolidation register
9. `86b1aec95b6aad03bf3c072242543dcae2dcc06d` — require exactly three long-lived branches
10. `7e0f8fc79686a6c6de88ba2512d1ddf652cbd944` — refresh branch inventory and PR register
11. `1a27519a64bf20f5b6fa82bbf1c2dea5ce7d961b` — record PR divergence and legacy routing risks
12. `ac1600950a017e7aae86d7d08468c045ea787b88` — recognize proposal, strategy and review task branches
13. `ae32d9d3d6d385930f70cf047b4bb8083ba9d6d6` — align consolidation sequence with current PR dependencies
14. `becd8c261b1cb548f14fe1d064f50f7ad8098535` — add strict branch minimisation directive
15. `eee75db01834f321f527fc6b24539922d9fe10ce` — refresh branch minimisation inventory
16. `703efaece11127ffcb99b21c6e14018d43c095f0` — set immediate seven-branch ceiling
17. `fc43126f5f31d159806de1ac5be78f7a61098a61` — record seven-branch consolidation plan
18. `633105210d3a6c4c8e36287ed2dc44dee23f61ef` — update seven-branch retirement PR register

PRs #1 and #2 each contain one source commit, respectively the head SHAs shown in the table; each has parent `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`.

### Content-preservation verification

Four of the five current source and destination files have identical blob SHAs. The branch inventory file is the deliberate exception: its original source blob remains intact on `governance/branch-lifecycle-policy`, while the PR #16 destination version replaces the inaccurate Task 05D v2/v3 comparison with a verified correction. A direct comparison confirmed that the destination is exactly the source file with only that specific passage corrected:

| Source PR | File | Verified blob SHA | Result |
|---|---|---|---|
| #15 | `.github/pull_request_template.md` | `1b2a71bb968cb892bc229c5ce8ac5ffb4b3d1084` | Exact match on PR #16 branch |
| #15 | `docs/governance/BRANCH-INVENTORY-AND-CONSOLIDATION-REGISTER.md` | `9233910471f0806435cb39c47ff074e90d382e47` | Source version retained on source branch; destination intentionally corrected (blob `cd8933f2dab5411c003b12505e3ddcd9f02f2f3e`) |
| #15 | `docs/governance/BRANCHING-AND-RELEASE-GOVERNANCE.md` | `baf085de8baea1ec7becfc15ce3f691512e91aba` | Exact match on PR #16 branch |
| #1 | `docs/governance/LICENSING-AND-IP-POLICY.md` | `b24e479559eaa6022fdc37db7ea65ded30a7c23e` | Exact match on PR #16 branch |
| #2 | `docs/adr/ADR-011-stf-ecosystem-boundaries.md` | `92c3fb551c1b0e367d748f76ce8e835959ed3957` | Exact match on PR #16 branch |

Git comparison against the current PR #16 branch reports PR #15 as 18 commits ahead / 40 behind with three added-file entries; PR #1 and PR #2 each report one commit ahead / 40 behind with one added-file entry. These are divergent histories with no shared document ancestry in the compare base. The added-file status does **not** mean the destination lacks the files: the exact blob checks above prove the current contents match.

### What is and is not preserved

- **Verified:** four governance files remain byte-identical between source and destination. The fifth (branch inventory) is preserved in its original form on the source branch and intentionally corrected on the PR #16 destination; the destination differs only by the documented Task 05D v2/v3 correction.
- **Verified:** source commit SHAs and the linear PR #15 commit sequence are now recorded in this register.
- **Not transferred:** the original source commit ancestry is not part of PR #16's commit graph merely because file contents were copied. This register records commit identifiers and provenance; it does not itself retain the underlying Git objects.
- **Review status:** none of PRs #1, #2, #15 or #16 has recorded issue comments, submitted reviews or inline review threads in the retrieved GitHub records. No independent legal, governance or architecture approval is evidenced.
- **Not approved:** PR #1's licensing policy remains proposed; PR #2's ADR-011 remains proposed; PR #15's branch policy remains proposed; PR #16 remains a draft audit/operating-standard PR.

### Retirement recommendation

Do not close or delete any of the three source branches on the strength of file equality alone. If complete Git history must remain directly reachable, retain the source ref until the owner approves a specific history-preservation method (for example, integrating the source history into the existing governance review destination or creating an approved archival ref). If the owner accepts content-level preservation plus the recorded commit-SHA provenance as sufficient, document that decision before resolving the source PR and deleting its own head branch. No retargeting, merge, closure, tag creation or branch deletion was performed in this audit.

## Owner-selected original-history preservation — 21 November 2026

**Owner direction:** The project owner selected Option A: preserve original Git history wherever it contains meaningful decisions. Use existing branches only. No new branches are authorized. The owner has expressly retained the requirement for separate approval before any merge, PR closure, branch deletion or other irreversible action.

### Current reachability of governance source histories

| Source branch | Current head | Original history | Current preservation state |
|---|---|---|---|
| `governance/branch-lifecycle-policy` | `633105210d3a6c4c8e36287ed2dc44dee23f61ef` | 18 linear commits from `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | Reachable through the existing source branch ref; PR #15 remains open |
| `docs/asset-specific-licensing-policy` | `15fd4edef9afa8d22df9e23f66296ef09423d8cf` | 1 original policy commit from `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | Reachable through the existing source branch ref; PR #1 remains open |
| `docs/adr-011-stf-ecosystem-boundaries` | `e900b64c90df08f5c98181af54bf2ab0b7096759` | 1 original ADR proposal commit from `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` | Reachable through the existing source branch ref; PR #2 remains open |

These source refs currently keep the original commit objects reachable. The source branches must not be deleted until their ancestry has been made reachable from an approved retained ref and the relevant PR/branch retirement gates are satisfied.

### Assessment of meaningful history

**PR #15 — retain all 18 commits in the ancestry.** The sequence is not merely 18 interchangeable snapshots:

- Commits 1–3 establish three distinct governance artifacts: branch lifecycle policy, PR template and consolidation register.
- Commits 4–8 record successive corrections to the inventory, scientific-review status and PR dependency record.
- Commits 9–14 refine the branch model, long-lived-branch rule, branch inventory, dependency routing and minimisation policy.
- Commits 15–18 record the seven-branch ceiling, consolidation plan and current retirement register.

Some later commits are inventory refreshes rather than new standalone policies, but they record the evolution of verified repository state and owner-directed constraints. Preserve the complete 18-commit ancestry; use the commit messages and this register to explain the sequence rather than attempting to squash it.

**PR #1 — retain its one original commit.** It is the origin of the proposed asset-specific licensing/IP policy. The policy's proposed status and lack of independent legal approval remain explicit.

**PR #2 — retain its one original commit.** It is the origin of proposed ADR-011 on STF ecosystem boundaries. It remains proposed and must be checked against existing accepted ADRs before acceptance.

### Proposed history-preserving integration method — not yet authorized

The existing PR #16 branch already contains the source documents. Four source/destination file blobs match exactly. The branch inventory file was intentionally corrected on PR #16; its original form remains on the source branch, and the destination's only difference from the source file is the verified Task 05D v2/v3 correction.

After a separate explicit authorization, the technically cleanest candidate is to preserve each source head as a parent of a merge commit on the **existing** `docs/repository-audit-and-ai-operating-standard` branch, retaining the destination tree as the canonical tree. This is equivalent to an ancestry-preserving 'ours' integration: it records the original source history as reachable ancestry without reverting the destination's reconciled content. It does not require creating a new branch. The operation must be tested/reviewed against the exact current tree and parent SHAs immediately before execution.

Sequence, if separately authorized:

1. Re-fetch PR #16 head, source branch heads, destination tree SHA and all five source/destination file blobs.
2. Confirm no source branch has advanced and no new PR depends on a different source state.
3. Create a two-parent history-preserving merge commit for one source branch at a time on the existing PR #16 branch, with the current destination commit as first parent, source head as second parent, and the reconciled destination tree unchanged.
4. Verify the merge commit has both expected parents, the expected tree, and the complete original source ancestry is reachable from the destination branch.
5. Repeat for the other two source branches, re-fetching and verifying after each write.
6. Only after PR #16 is reviewed and its integration is separately approved may the source PRs be resolved. Branch deletion remains a separate approval and must wait until no open PR references the branch.

**Approval boundary:** The owner's selection of Option A authorizes the preservation objective and the planning work. It does not authorize creation of merge commits, PR merges/closures, retargeting, or branch deletion. No history-integration merge has been performed.

### Verified repository state after this decision

- 23 branches remain, including all three governance source refs and the PR #16 destination ref.
- 20 PRs remain open; PRs #1, #2 and #15 remain unmerged, and PR #16 remains draft.
- The PR #16 destination branch was at `69d3636b0e15254ef5973ace3b53e6816a253b37` immediately before this provenance update.
- No new branch was created. No merge commit, PR merge, PR closure, retarget, tag, branch deletion or protection change was performed.

## History-preservation technical preflight — 21 November 2026

**Purpose:** establish whether the three governance source histories can be made reachable from the existing PR #16 destination branch without creating a branch, changing the destination tree, force-updating a ref, or retiring a source ref.

### Snapshot re-verified for this preflight

- Repository: `Save-Tiger-First/botanica-indica`.
- Operating prompt: `docs/governance/AI-PROJECT-OPERATING-PROMPT.md`, branch `docs/repository-audit-and-ai-operating-standard`, blob `ec100aec5abc09ec04ad9f4a084a0aa95a7c7558`.
- Destination branch before this preflight record: `docs/repository-audit-and-ai-operating-standard` at commit `136f6e045ebac42a1f6a9b4e8e7259f41a9fe325`, tree `287077e58f3e3d3d77650c7d8c8fdf822e8b319c`, parent `69d3636b0e15254ef5973ace3b53e6816a253b37`.
- Source `governance/branch-lifecycle-policy`: head `633105210d3a6c4c8e36287ed2dc44dee23f61ef`, 18 commits in a linear chain from base `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`.
- Source `docs/asset-specific-licensing-policy`: head `15fd4edef9afa8d22df9e23f66296ef09423d8cf`, one commit parented by `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`.
- Source `docs/adr-011-stf-ecosystem-boundaries`: head `e900b64c90df08f5c98181af54bf2ab0b7096759`, one commit parented by `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`.
- Repository inventory: 23 branches and 20 open PRs. PRs #1, #2, #15 and #16 remain open and unmerged; PR #16 remains draft. The three source refs remain present.

### Ancestry and divergence verification

All three source branches share merge base `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` with the PR #16 destination. None of the source histories is currently an ancestor of the destination.

| Source | Commits unique to source relative to PR #16 | Commits unique to PR #16 relative to source | Compare status |
|---|---:|---:|---|
| `governance/branch-lifecycle-policy` | 18 | 43 | Diverged |
| `docs/asset-specific-licensing-policy` | 1 | 43 | Diverged |
| `docs/adr-011-stf-ecosystem-boundaries` | 1 | 43 | Diverged |

PR #15's 18 commits are a linear chain. Per-commit file inspection confirms the sequence creates the branch lifecycle policy, PR template and consolidation register, then records subsequent scientific-status, inventory, dependency, three-long-lived-branch and seven-branch-ceiling updates. These changes are meaningful as an auditable governance evolution and should be retained intact. PR #1 and PR #2 each contain one distinct proposal-origin commit.

### Tree and file preservation check

The PR #16 destination tree before this preflight record was `287077e58f3e3d3d77650c7d8c8fdf822e8b319c` (33 entries; not truncated). Source and destination file checks confirmed:

- `.github/pull_request_template.md`: identical blob `1b2a71bb968cb892bc229c5ce8ac5ffb4b3d1084`.
- `docs/governance/BRANCHING-AND-RELEASE-GOVERNANCE.md`: identical blob `baf085de8baea1ec7becfc15ce3f691512e91aba`.
- `docs/governance/LICENSING-AND-IP-POLICY.md`: identical blob `b24e479559eaa6022fdc37db7ea65ded30a7c23e`.
- `docs/adr/ADR-011-stf-ecosystem-boundaries.md`: identical blob `92c3fb551c1b0e367d748f76ce8e835959ed3957`.
- `docs/governance/BRANCH-INVENTORY-AND-CONSOLIDATION-REGISTER.md`: source blob `9233910471f0806435cb39c47ff074e90d382e47`; destination blob `cd8933f2dab5411c003b12505e3ddcd9f02f2f3e`. This is the deliberate Task 05D v2/v3 correction recorded above; a direct content comparison confirmed the destination is the source version with that targeted passage corrected.

### Proposed integration sequence — design only, not executed

GitHub's official REST API supports creating a commit with multiple parents and a specified tree, and updating an existing branch reference without force when the update is a fast-forward. See:

- GitHub REST API, [Create a commit](https://docs.github.com/en/rest/git/commits): multiple parent SHAs create a merge commit; the API defaults author/committer identity and date to the authenticated user/current date when not supplied.
- GitHub REST API, [Update a reference](https://docs.github.com/en/rest/git/refs): `force=false` requires a fast-forward update.
- GitHub REST API, [Git database overview](https://docs.github.com/en/rest/guides/using-the-rest-api-to-interact-with-your-git-database): Git objects are created first, then a branch ref is updated to point to the commit.

After a separate explicit authorization, the proposed sequence on the existing `docs/repository-audit-and-ai-operating-standard` branch is:

1. Re-fetch the destination branch head and tree, all three source heads, the PR states and the relevant file blobs immediately before the first write. Abort if any ref, PR dependency or required blob has changed.
2. Create merge commit M1 with first parent = current destination head, second parent = `633105210d3a6c4c8e36287ed2dc44dee23f61ef`, and tree = the exact current destination tree. This preserves all 18 PR #15 commits without replacing the corrected destination inventory.
3. Update only the existing destination branch ref to M1 using a non-force fast-forward update and an expected-head lease. Re-fetch and verify both parents, unchanged tree and source ancestry reachability.
4. Create merge commit M2 with first parent = verified M1, second parent = `15fd4edef9afa8d22df9e23f66296ef09423d8cf`, and the same destination tree; update the same existing branch non-force with an expected-head lease; verify.
5. Create merge commit M3 with first parent = verified M2, second parent = `e900b64c90df08f5c98181af54bf2ab0b7096759`, and the same destination tree; update the same existing branch non-force with an expected-head lease; verify.
6. Verify the final destination tree equals the pre-integration tree, all three source heads are ancestors of the destination, all 20 original source commits remain reachable, and the source branches and PRs remain open and unchanged.

**Important implementation detail:** because this preflight record itself updates PR #16, the tree SHA `287077e58f3e3d3d77650c7d8c8fdf822e8b319c` is a historical preflight snapshot, not the tree to hard-code at execution. The exact then-current tree must be fetched again and used for all three merge commits. The three resulting commit SHAs cannot be truthfully precomputed: Git commit identity includes commit metadata (including author/committer and dates). The API wrapper available for this task defaults that metadata to the authenticated integration identity/current time. Original source commits and their authorship remain unchanged.

### Preflight decision

- **Technically feasible:** yes, using the GitHub Git database create-commit operation with two parents and the existing destination tree, followed by a non-force fast-forward update of the existing destination branch.
- **Tree-preservation risk:** controlled by explicitly reusing the latest destination tree and verifying it after every update. Do not use the source branch tree.
- **History-preservation result:** source commits become reachable through second-parent ancestry; no source commits are rewritten.
- **Branch-count effect:** none. No new branch is required or proposed.
- **Source-retirement effect:** none at this stage. All source branches and PRs remain open until separately reviewed and approved.
- **Execution status:** not executed. No commit object was created, no branch ref was updated, no PR was merged or closed, and no branch was deleted.
- **Approval required:** explicit authorization to create the three merge commits and advance the existing PR #16 branch. This is separate from the already approved preservation objective.


## Governance history-preserving integrations — completed 21 November 2026

**Status: Implemented and verified on the existing PR #16 branch.** The project owner explicitly authorized three ancestry-preserving, two-parent commits on `docs/repository-audit-and-ai-operating-standard`, retaining the destination tree and leaving all PRs and source branches open.

### Integration commits

| Order | Source PR / branch | Destination merge commit | First parent | Second parent (original source head) |
|---|---|---|---|---|
| 1 | PR #15 — `governance/branch-lifecycle-policy` | `0dbde2a31c4c8c0dd24e84789aee7f690237465e` | `0086c739379a5b8d6c107780e314ef8fb0d1f98f` | `633105210d3a6c4c8e36287ed2dc44dee23f61ef` |
| 2 | PR #1 — `docs/asset-specific-licensing-policy` | `8822e8e6690e7959e8226ae338ff04205c55d1ec` | `0dbde2a31c4c8c0dd24e84789aee7f690237465e` | `15fd4edef9afa8d22df9e23f66296ef09423d8cf` |
| 3 | PR #2 — `docs/adr-011-stf-ecosystem-boundaries` | `8118f633d026fe05573160562e3d76defa3e6ea7` | `8822e8e6690e7959e8226ae338ff04205c55d1ec` | `e900b64c90df08f5c98181af54bf2ab0b7096759` |

All three commits were created with the exact same destination tree `590689102dc583fe16a0fa7c5aae4cb36d6d5eef`. Each existing destination ref update used `force=false` and an expected-head SHA. After each write, the destination head, tree and exact two-parent ordering were fetched and verified.

### Ancestry verification

GitHub compare checks were run with each source head as the base and the final integrated PR #16 head as the comparison target:

| Source head | Compare result | Ahead from source | Behind from destination |
|---|---|---:|---:|
| PR #15 `633105210d3a6c4c8e36287ed2dc44dee23f61ef` | `ahead` | 49 | 0 |
| PR #1 `15fd4edef9afa8d22df9e23f66296ef09423d8cf` | `ahead` | 66 | 0 |
| PR #2 `e900b64c90df08f5c98181af54bf2ab0b7096759` | `ahead` | 66 | 0 |

Each source head is therefore an ancestor of the integrated PR #16 head. The complete 18-commit PR #15 sequence and the original one-commit PR #1 and PR #2 histories remain reachable without rewriting those source commits.

### Scope and safety verification

- PR #16 remains open and draft; its head is `8118f633d026fe05573160562e3d76defa3e6ea7` at the time of this record.
- PRs #1, #2 and #15 remain open and unmerged, with their original head SHAs unchanged.
- The three source branches remain present at their original source head SHAs.
- Repository branch count remains 23; open PR count remains 20.
- No branch was created or deleted. No PR was merged or closed. No PR was retargeted. No branch protection, ruleset, repository permission or default-branch setting was changed.
- The exact destination tree was preserved across all three history integrations. This statement concerns the integration commits themselves; this provenance update is a subsequent documentation commit and will create a new tree.

### Remaining work

These integrations preserve ancestry; they do **not** constitute approval or merge of the licensing policy, ADR-011, branch lifecycle policy, or PR #16 into `develop`. The content and decisions still require review under the operating prompt. The source PRs and branches must not be closed or deleted until the owner separately authorizes those actions and all relevant PR dependencies, review requirements and preservation gates have been resolved.



## Current-state addendum — 21 November 2026, automation-hardening pass

The historical snapshots above remain unchanged and should be read as records of their respective audit dates. Current live state is recorded in `docs/governance/BRANCH-INVENTORY-AND-CONSOLIDATION-REGISTER.md` Section 20.11 and `docs/reviews/PR-16-GOVERNANCE-READINESS-REVIEW-2026-11-21.md` Section 10.

- PR #16 current head: `6f27e14668b4749fa1210f78c00b0d78f2b99e74`; open, draft, base `develop`.
- PR #16 vs `develop`: 110 ahead / 0 behind.
- PR #15 head remains an ancestor of PR #16: 92 ahead / 0 behind.
- Live inventory: 23 branches; 20 open PRs.
- The three automation files were updated and verified by blob SHA as recorded in Section 20.11.3 of the branch register.
- Current-head CI is not verified. The earlier successful run 44901677252 belongs to commit `05bf12ec34c724ada2aec3f2631323a12878673f`, not the current head.
- No PR lifecycle or branch lifecycle action was taken. No policy/ADR was approved.

## Live consolidation ancestry refresh — 21 November 2026

The historical provenance records above remain intact. Current branch inventory and source/destination ancestry are recorded in Branch Inventory and Consolidation Register Section 20.17.

Fresh source-to-destination comparisons show:
- PR #15, #1 and #2 source heads are already ancestors of the governance destination; no further ancestry integration is needed for those three.
- Product/architecture sources #17, #18 and #19 have respectively 9, 2 and 27 source-only commits relative to the existing architecture destination.
- Scientific sources #3, #4, #5, #11, #21, #22 and #23 have respectively 5, 14, 10, 13, 1, 7 and 7 source-only commits relative to the existing scientific review destination.
- Strategy sources #12, #13 and #14 have respectively 4, 1 and 1 source-only commits relative to the strategy destination; PR #12 is diverged and overlaps two destination files.

These counts describe Git ancestry, not unique file counts or content approval. Before any history-preserving integration, inspect full commit graphs and diffs. Preserve the main-only Hortus crosswalk separately; its current main blob is a3758743e090121a31cda9e6876f43ceb3caa3a0, and the review-branch copy is 6b7fd454795607b3e93cc590e7ffa562884c0a9e. The two copies differ and require reconciliation.

The latest PR #16 head at this audit was f6f661b97376323aba36b91725aca483af9e7d35. PR #16 remains open/draft; no PR was merged or closed and no source branch was deleted. No content approval or scientific sign-off is implied.
