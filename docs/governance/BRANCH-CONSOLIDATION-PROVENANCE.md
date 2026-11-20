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
