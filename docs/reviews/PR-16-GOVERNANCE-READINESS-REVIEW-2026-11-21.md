# PR #16 — Governance Readiness Review

- **Document ID:** STF-REV-PR16-001
- **Review date:** 21 November 2026
- **Status:** Completed desk review; remediation proposed; not approval to mark ready or merge
- **Repository:** `Save-Tiger-First/botanica-indica`
- **Reviewed branch:** `docs/repository-audit-and-ai-operating-standard`
- **Reviewed PR:** [#16](https://github.com/Save-Tiger-First/botanica-indica/pull/16)
- **Governing instruction:** `docs/governance/AI-PROJECT-OPERATING-PROMPT.md`, version 1.0, blob `53add3894d0502827e584614c70ad09cadaa637d`

## 1. Executive conclusion

PR #16 contains valuable governance work and its current PR-triggered CI run passed. The workflow uses read-only repository permissions and immutable, full-length action commit references. The reviewed changes preserve the accepted mobile technology direction and modular architecture; ADR-011 and the companion ecosystem-boundary document remain explicitly proposed.

**Recommendation: keep PR #16 open and draft. Do not mark it ready for review or merge yet.** The successful workflow is a useful narrow validation, not a complete governance assurance. The branch-routing checker has bypasses and does not enforce the owner-directed no-new-branches/seven-branch rules. Markdown validation has untested logic and a runtime warning. Several supporting governance records retain older PR #16 head snapshots. No independent review has been recorded.

This review is a desk review of repository material and official public sources. It is not independent legal advice, scientific peer review, security certification or project-owner approval.

## 2. Exact live state inspected

### 2.1 Operating prompt

Fetched in full from the required branch:

- Path: `docs/governance/AI-PROJECT-OPERATING-PROMPT.md`
- Version: 1.0, proposed project operating standard
- Blob SHA: `53add3894d0502827e584614c70ad09cadaa637d`
- Length: 258 lines

The owner instruction requires following it as the working standard even though the document itself remains proposed for adoption. The current no-new-branches directive and immediate seven-branch ceiling remain in force.

### 2.2 PR #16

| Field | Verified value |
|---|---|
| PR | #16 |
| State | Open |
| Draft | Yes |
| Merged | No |
| GitHub mergeable flag | True |
| Base | `develop` |
| Base SHA | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` |
| Head branch | `docs/repository-audit-and-ai-operating-standard` |
| Head SHA | `05bf12ec34c724ada2aec3f2631323a12878673f` |
| Commits | 106 |
| Changed files | 25 |
| Additions / deletions | 3,493 / 19 |
| Submitted reviews | 0 |
| Inline review threads | 0 |
| Requested reviewers | None reported |

A fresh comparison against `develop` returned 106 commits ahead and 0 behind. GitHub's mergeable flag is metadata only; it is not review, approval or a readiness decision.

### 2.3 Repository lifecycle state

- Live branch search: **23 branches** — 3 long-lived and 20 temporary.
- Live open-PR search: **20 open PRs** — #1–#5, #8, #9 and #11–#23.
- The seven-branch ceiling is exceeded by 16 branches.
- PR #15 remains open, non-draft and unmerged.
- Comparing PR #15's head `633105210d3a6c4c8e36287ed2dc44dee23f61ef` with PR #16's current head returns **88 ahead / 0 behind**. PR #15's head remains the merge base and is therefore an ancestor of PR #16.
- `main` is 1 commit ahead of `develop`; the only main-side addition is `docs/reviews/HORTUS-MALABARICUS-VALIDATION-CROSSWALK.md` (187 additions). The merge base is `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`.

No PR or branch lifecycle action was taken.

## 3. CI and technical verification

### 3.1 Latest workflow run

The PR-triggered GitHub Actions run associated with the reviewed head completed successfully:

- Workflow: `Repository governance`
- Run ID: `44901677252`
- Job: `Markdown integrity and branch routing`
- Job conclusion: `success`
- Synthetic PR merge commit checked out by the runner: `5d6c87a76b6a8251b4de44ee94a2109148481b9d`
- Python: 3.12.16
- Unit tests: **7 passed**
- Markdown files scanned: **22**
- Markdown-fence and PR-routing command: passed

The combined commit-status endpoint returned no status records. The workflow run is verified, but this review did not verify that it is configured as a required status check in repository rules or branch protection.

### 3.2 Action pin verification

The workflow pins actions by full commit SHA:

- `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1`, corresponding to the official v7.0.1 release.
- `actions/setup-python@6d4fd22b20465ccc0f7354476588e8df7c9ca0e0`, corresponding to the official v7.1.0 release.

The official release pages identify these release commits as GitHub-verified signed commits:
- https://github.com/actions/checkout/releases
- https://github.com/actions/setup-python/releases

The workflow declares `permissions: contents: read`, which is appropriately restrictive for its current purpose. It does not use `pull_request_target`, `workflow_run`, write permissions or deployment permissions.

**Hardening recommendation:** set `persist-credentials: false` on the checkout step because subsequent steps do not need authenticated Git operations. This reduces unnecessary exposure of the read-only checkout credential to code executed from the pull request.

### 3.3 Confirmed limitations in the governance checker

The current `scripts/check_repository_governance.py` has several gaps:

1. **Unknown target branches bypass routing validation.** `check_routing` has explicit branches for `develop`, `staging` and `main`, but no rejection path for other base branches. A PR targeting an arbitrary temporary branch can therefore pass the routing function without an error.
2. **Stacked PR routing is not explicitly governed.** Existing PRs #11, #12 and #21–#23 use temporary base branches. They need explicit, narrow, documented exceptions with dependency checks; the current checker silently bypasses them along with any other unknown base.
3. **The seven-branch ceiling is not enforced.** The script does not query or validate the live repository branch count.
4. **The no-new-branches directive is not enforced.** A valid prefix is accepted for a PR into `develop`, even though the current owner directive prohibits creating new branches.
5. **Emergency hotfix text is not owner authorization.** The checker accepts a `fix/*` PR into `main` when the body contains the phrase `Emergency hotfix exception:`. A text string cannot prove who authorized the exception.
6. **Markdown checks lack direct regression tests.** All seven tests cover routing. There are no tests for `check_fences` or `check_relative_links`.
7. **Link checking is advisory and incomplete.** Unresolved relative links are warnings, not failures; heading anchors and several Markdown link forms are not validated.
8. **The fence parser is simplistic.** Its closing-fence recognition does not fully implement CommonMark fence rules and needs targeted tests before being relied on as an integrity gate.
9. **A Python runtime warning occurs.** The workflow log reports a `FutureWarning: Possible nested set` from the regular expression in `check_relative_links`. It did not fail this run, but should be corrected.

The successful run therefore demonstrates only that the current seven routing tests pass and the current tracked Markdown files did not trigger the implemented fence/routing errors. It does not demonstrate comprehensive Markdown correctness or full branch-policy enforcement.

## 4. Cross-document consistency review

### 4.1 Accepted ADRs and proposed ADR-011

The reviewed accepted ADRs confirm:

- ADR-001: technology-independent, modular, contract-driven architecture; Dart/Flutter mobile direction; modular monolith initially; no premature microservices.
- ADR-002: modular architecture and modular monolith initially.
- ADR-003: API-first platform architecture.

The proposed ADR-011 and companion ecosystem-boundary document retain modular implementation, domain ownership and contract-based reuse. No contradiction with the reviewed accepted direction was identified. ADR-011 remains **Proposed**, not Accepted; the companion architecture document also remains Proposed.

**Minor consistency correction:** the companion architecture document's header lists related decisions ADR-001 through ADR-010 but does not list ADR-011, despite being the companion document to ADR-011. Update the relationship metadata when the document is next revised.

### 4.2 README and contributor guidance

The README correctly labels ADR-011, the operating prompt, branch policy and licensing policy as proposed review materials and says they are not merged into `main`. It also retains Dart/Flutter and the modular-monolith direction.

The contributor guide correctly states that formal contributor terms have not yet been adopted and that Apache-2.0 does not license third-party material. However, its generic instruction to create a feature/fix branch should be reconciled with the current owner directive prohibiting new branch creation. It should direct contributors to use an approved existing branch or obtain owner authorization while that directive remains active.

### 4.3 Governance snapshot freshness

The current Branch Inventory and Consolidation Register has Section 20.10, which records the 23-branch inventory, 20 open PRs and updated PR #15/#16 ancestry.

Two related documents still contain earlier PR #16 head snapshots and older ancestry counts:
- `docs/governance/BRANCH-CONSOLIDATION-PROVENANCE.md`
- `docs/governance/PR-15-PR-16-GOVERNANCE-CONTENT-RECONCILIATION.md`

Those entries are valid as dated historical snapshots, but the documents should explicitly label them historical and point to the latest register/readiness review for current state. Do not silently overwrite historical SHAs or counts.

### 4.4 Scope and reviewability

The 25-file PR combines repository audit, operating prompt, branch lifecycle policy, licensing/IP policy, proposed ADR-011, README/contributor changes, Markdown repairs and automation. Consolidation into one governance vehicle is understandable under the no-new-branch and seven-branch directives, but the package is broad.

Review should be divided into explicit approval tracks:
- Repository/Markdown audit and automation
- Branch lifecycle policy
- Asset licensing and contributor terms
- STF ecosystem boundaries / ADR-011

A positive review of the workflow must not be treated as approval of the legal policy or architecture proposal.

## 5. Legal-source spot check — not legal advice

The licensing/IP policy remains Proposed and correctly calls for qualified legal review. A limited spot check of its India-specific commencement references found:

- MeitY's G.S.R. 843(E), 13 November 2025, sets the staged commencement of the DPDP Act: specified provisions on publication, sections 6(9) and 27(1)(d) after one year, and the listed remaining provisions after eighteen months.
- MeitY's G.S.R. 846(E), 13 November 2025, sets the staged commencement of the DPDP Rules, including Rule 4 after one year and Rules 3, 5–16, 22 and 23 after eighteen months.
- The National Biodiversity Authority's official site lists the Biological Diversity Rules 2024, Amendment Rules 2025 and the 2025 Access and Benefit Sharing Regulations.

Official sources checked:
- DPDP Act commencement notification, G.S.R. 843(E): https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf
- DPDP Rules, G.S.R. 846(E): https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf
- MeitY DPDP Rules and corrigendum listing: https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-protection-rules-2025-gDOxUjMtQWa
- NBA Rules: https://nbaindia.nic.in/index.php/acts-and-rules/rules
- NBA notifications and ABS Regulations: https://www.nbaindia.nic.in/public-information/notification-guidelines

This spot check supports the policy's staged-commencement framing and the existence of the cited biodiversity instruments. It does not establish legal applicability to any particular STF activity, resolve the effect of every corrigendum or amendment, or constitute a legal opinion. The policy must remain Proposed pending qualified legal review and activity-specific assessment.

## 6. Findings ranked by severity

### Blocker — before PR #16 can be considered governance-complete

1. The live repository violates the owner-directed seven-branch ceiling: 23 branches remain. A preservation-first retirement plan exists, but the target is not achieved.
2. The routing checker does not enforce the seven-branch/no-new-branches directives and permits unrecognized target branches to bypass validation.
3. The PR has no submitted review, no inline review threads and no requested reviewers. Independent review and explicit owner disposition remain outstanding.

### Major — remediate before marking PR #16 ready

4. Add a default-deny rule for unsupported PR base branches and an explicit allowlist for legitimate stacked PR dependencies.
5. Do not treat a PR-body hotfix phrase as proof of owner approval.
6. Add regression tests for fence parsing, link handling, unsupported targets, stacked PR exceptions and hotfix authorization evidence.
7. Correct the regex FutureWarning and define whether broken relative links are warnings or merge-blocking errors.
8. Reconcile historical PR-head snapshots across the provenance and PR reconciliation documents, preserving old values as history.
9. Align contributor branch instructions with the current no-new-branches directive.
10. Keep legal/IP policy and ADR-011 as separate review decisions; neither is approved by inclusion in PR #16.

### Minor

11. Set checkout `persist-credentials: false` where feasible.
12. Add ADR-011 to the companion architecture document's related-decision metadata.
13. Verify the workflow is configured as a required status check only after testing it on representative PR types and resolving its routing exceptions.

## 7. Recommended remediation sequence

1. **Automation correctness:** fix the unknown-base bypass, explicitly model stacked PR exceptions, and clarify the hotfix approval evidence requirement.
2. **Test coverage:** test Markdown fence and link functions, plus positive and negative routing cases. Eliminate the runtime warning.
3. **Policy enforcement design:** decide how to report and enforce the seven-branch ceiling and no-new-branches directive without accidentally treating a temporary exception as authorization.
4. **Documentation alignment:** refresh the provenance and reconciliation documents with a dated addendum; align CONTRIBUTING and the companion architecture metadata.
5. **Separate policy reviews:** obtain maintainer review of branch governance, qualified legal review of licensing/contributor terms, and architecture review of ADR-011.
6. **Fresh verification:** rerun CI on the new head, inspect the exact logs, verify all files and SHAs, then request the appropriate review and only later consider marking PR #16 ready.
7. **Owner decision:** decide the disposition of PR #15 separately. Its head is preserved in PR #16 history, but do not close it or delete its branch without explicit authorization.

## 8. Work completed and not completed

**Completed in this review:**
- Re-fetched the full operating prompt and verified its blob SHA.
- Re-fetched PR #16 and PR #15 metadata, branch inventory and open PR inventory.
- Compared PR #16 against `develop`, PR #15 against PR #16, and `main` against `develop`.
- Inspected the workflow, checker, tests, README, contributor guide, accepted ADRs 001–003, proposed ADR-011, companion architecture document and key governance records.
- Inspected the latest PR-triggered workflow job steps and logs.
- Spot-checked official MeitY and NBA source references.

**Not done:**
- No PR was merged, closed, marked ready or retargeted.
- No branch was created, deleted, renamed or force-pushed.
- No repository protection, ruleset, permission or setting was changed.
- No code or policy remediation was committed as part of this review.
- No legal adviser, scientific specialist, institution or external party was contacted.
- No legal opinion, scientific sign-off or production-readiness determination was obtained.

## 9. Final recommendation

Keep PR #16 open and draft. The current implementation is a good foundation, but the routing bypasses, missing branch-cap enforcement, insufficient Markdown tests, historical snapshot drift and absence of independent review prevent a responsible readiness recommendation.

The next implementation task should be a **narrow automation-hardening pass on this same existing branch**, followed by a documentation-freshness pass. Do not create another branch. Do not merge PR #16 or close PR #15 until the owner-authorized review and branch-retirement gates are satisfied.



## 10. Automation-hardening implementation addendum — 21 November 2026

Following the review recommendation, a bounded automation-hardening pass was committed to the same existing PR #16 branch. No new branch was created.

### 10.1 Changes made

- Default-deny unsupported PR base branches.
- Replace generic stacked-PR bypasses with exact PR number/base/head allowlist entries for existing PRs #11, #12 and #21–#23.
- Remove PR-body text as hotfix authorization. The owner-approved hotfix allowlist is empty by default; any future exception requires explicit owner authorization recorded in repository state.
- Add a dated 23-branch baseline, reject unregistered branch names, verify the three required long-lived branches, and warn when the live branch count exceeds seven. The seven-branch excess remains a warning so preservation/retirement work can proceed; this is detection, not prevention of branch creation.
- Expand Markdown fence and relative-link regression coverage.
- Set checkout `persist-credentials: false`; retain `contents: read`; add a live branch-inventory workflow step.

### 10.2 Exact commits

| File | Commit SHA | Blob SHA |
|---|---|---|
| `scripts/check_repository_governance.py` | `193835b921bc4beaafd80da8de5563373fca23b8` | `7036f21a749326f27a3952504bde42b870e0b8c5` |
| `tests/test_repository_governance.py` | `326dc559c7266025c34021de384193ea1c5a29f7` | `cc96e2b4e2bb3eae7f9b8837cea2254ad5a78dc2` |
| `.github/workflows/repository-governance.yml` | `6f27e14668b4749fa1210f78c00b0d78f2b99e74` | `c977c8209791238da3a213caa9c8b4acf438ae01` |

### 10.3 Current state and verification caveat

- PR #16 remains open and draft; current head `6f27e14668b4749fa1210f78c00b0d78f2b99e74`, 110 commits, 26 changed files, 4,019 additions and 19 deletions.
- The branch comparison against `develop` is 110 ahead / 0 behind.
- Live inventory remains 23 branches and 20 open PRs.
- PR #15 remains open; fresh ancestry comparison is 92 ahead / 0 behind, with PR #15 head as merge base.
- `main` remains one commit ahead of `develop` due to the Hortus Malabaricus crosswalk.
- The workflow-run lookup for the current head returned no PR-triggered run. The previously successful run 44901677252 was on the preceding commit `05bf12ec34c724ada2aec3f2631323a12878673f`; it does **not** validate this new head.
- The three files were fetched after writing and their blob SHAs verified. Runtime execution of the new test suite and live branch API step remains **pending**.

### 10.4 Updated recommendation

Keep PR #16 open and draft. Do not mark it ready or merge it. First obtain a current-head workflow run, inspect the test output and branch API step, correct any failures, and then obtain independent maintainer review. The seven-branch ceiling remains unmet; the checker reports the excess but does not itself enforce branch-creation permissions. No repository settings were changed.


## 11. Automation-hardening verification addendum — 21 November 2026

<badge> </badge>

The updated governance workflow completed successfully on PR #16 head `c037c66865a5b576ef3a74717d803b941fb0a878`.

- Run: [44906508756](https://github.com/Save-Tiger-First/botanica-indica/actions/runs/44906508756)
- Result: success
- Unit tests: **27 passed**
- Markdown scan: **23 tracked Markdown files**
- PR #16 routing validation: passed
- Live GitHub branch API: returned 23 branches
- Seven-branch ceiling: correctly emitted a warning; it remains unmet.

The previous statement that current-head CI was pending applied to the earlier snapshot. This run closes that verification gap for commit `c037c66865a5b576ef3a74717d803b941fb0a878`.

**Important limits:** the successful run does not prove that branch creation is prevented, that the workflow is configured as a required check, or that repository rulesets are adequate. It also does not replace independent maintainer review. The seven-branch target is still unmet.

Recommendation remains: keep PR #16 open and draft until independent review and owner disposition. No PR was merged/closed or branch deleted.


## 12. Workflow activation limitation — 21 November 2026

The repository governance workflow is present on the PR #16 branch, not on `main`. Its pull-request run successfully executed the live branch inventory check on code-bearing commit `c037c66865a5b576ef3a74717d803b941fb0a878` (run 44906508756; 27 tests passed). However, the workflow's `create` event must not be represented as an active pre-merge branch-creation control while the workflow is absent from the default branch.

The current implementation:
- validates the PR's base/head routing;
- fetches and checks the live branch inventory during PR workflow runs;
- rejects branch names outside the dated known-branch allowlist;
- warns, rather than blocks, while branch count exceeds seven.

It does **not** prevent a repository user from creating a branch. The `create` trigger becomes useful only after the workflow is present on the default branch, and even then it is detection after creation, not prevention. Prevention would require appropriately configured repository permissions/rulesets or another trusted control. Those settings have not been inspected or changed here.

Keep PR #16 open and draft. Do not merge it solely to activate the workflow. Obtain independent review and owner authorization for any repository protection changes.
