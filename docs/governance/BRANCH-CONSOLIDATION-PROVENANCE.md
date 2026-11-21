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

The current source and destination file blob SHAs match exactly:

| Source PR | File | Verified blob SHA | Result |
|---|---|---|---|
| #15 | `.github/pull_request_template.md` | `1b2a71bb968cb892bc229c5ce8ac5ffb4b3d1084` | Exact match on PR #16 branch |
| #15 | `docs/governance/BRANCH-INVENTORY-AND-CONSOLIDATION-REGISTER.md` | `9233910471f0806435cb39c47ff074e90d382e47` | Exact match on PR #16 branch |
| #15 | `docs/governance/BRANCHING-AND-RELEASE-GOVERNANCE.md` | `baf085de8baea1ec7becfc15ce3f691512e91aba` | Exact match on PR #16 branch |
| #1 | `docs/governance/LICENSING-AND-IP-POLICY.md` | `b24e479559eaa6022fdc37db7ea65ded30a7c23e` | Exact match on PR #16 branch |
| #2 | `docs/adr/ADR-011-stf-ecosystem-boundaries.md` | `92c3fb551c1b0e367d748f76ce8e835959ed3957` | Exact match on PR #16 branch |

Git comparison against the current PR #16 branch reports PR #15 as 18 commits ahead / 40 behind with three added-file entries; PR #1 and PR #2 each report one commit ahead / 40 behind with one added-file entry. These are divergent histories with no shared document ancestry in the compare base. The added-file status does **not** mean the destination lacks the files: the exact blob checks above prove the current contents match.

### What is and is not preserved

- **Verified:** the final contents of all five governance files are preserved exactly on the PR #16 branch.
- **Verified:** source commit SHAs and the linear PR #15 commit sequence are now recorded in this register.
- **Not transferred:** the original source commit ancestry is not part of PR #16's commit graph merely because file contents were copied. This register records commit identifiers and provenance; it does not itself retain the underlying Git objects.
- **Review status:** none of PRs #1, #2, #15 or #16 has recorded issue comments, submitted reviews or inline review threads in the retrieved GitHub records. No independent legal, governance or architecture approval is evidenced.
- **Not approved:** PR #1's licensing policy remains proposed; PR #2's ADR-011 remains proposed; PR #15's branch policy remains proposed; PR #16 remains a draft audit/operating-standard PR.

### Retirement recommendation

Do not close or delete any of the three source branches on the strength of file equality alone. If complete Git history must remain directly reachable, retain the source ref until the owner approves a specific history-preservation method (for example, integrating the source history into the existing governance review destination or creating an approved archival ref). If the owner accepts content-level preservation plus the recorded commit-SHA provenance as sufficient, document that decision before resolving the source PR and deleting its own head branch. No retargeting, merge, closure, tag creation or branch deletion was performed in this audit.