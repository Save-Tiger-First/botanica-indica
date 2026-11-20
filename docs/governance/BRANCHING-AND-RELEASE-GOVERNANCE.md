# Branching, Integration and Release Governance

**Status:** Proposed for adoption through pull request  
**Applies to:** Save Tiger First / Botanica Indica repository  
**Policy owner:** Repository maintainers  
**Review point:** At each release and at project-completion review

## 1. Mandatory branch-count policy

The repository shall maintain **exactly three designated long-lived branches** during active product development: `main`, `develop` and `staging`.

| Branch | Role | Lifecycle |
|---|---|---|
| `main` | Canonical, production-ready and authoritative project history | Permanent |
| `develop` | Integration branch for accepted development work | Active development only |
| `staging` | Release-candidate validation branch | Active development and release preparation only |

There shall be exactly one permanent main branch: `main`. The two supporting branches are `develop` and `staging`.

The three-branch limit applies to long-lived branches, not short-lived task branches. Temporary branches are permitted only under the lifecycle rules in this policy. A temporary branch must never become an undocumented permanent branch.

**Completion invariant:** when the project is formally declared complete, the repository shall contain exactly one branch, `main`. The `develop` and `staging` branches and all remaining temporary branches shall be deleted only after the completion gates in Section 8 are satisfied.

## 2. Branch purposes and authority

### `main`
- The default branch and single authoritative source of completed work.
- Contains reviewed, accepted, release-quality content.
- Direct pushes are prohibited except for a documented emergency approved by repository governance.
- Must be protected against accidental deletion and force-push.
- Releases and milestone tags are created from reviewed commits on this branch.

### `develop`
- Receives completed task work through pull requests.
- Is the integration baseline for active development.
- May contain accepted work not yet approved for release.
- Must not be treated as production-ready merely because a change is present here.

### `staging`
- Contains a release candidate promoted from `develop`.
- Is used for integrated review, acceptance, regression checks and release-readiness verification.
- Must not become an independent development line. Fixes found in staging should be made on a temporary task/fix branch, merged into `develop`, and then promoted again to `staging`.
- Only approved release candidates proceed from `staging` to `main`.

## 3. Temporary branch policy

Create a temporary branch only when work benefits from isolation, review, parallelism, or a recoverable change history.

Permitted prefixes:
- `feature/<short-description>`
- `fix/<short-description>`
- `docs/<short-description>`
- `research/<short-description>`
- `governance/<short-description>`
- `test/<short-description>`
- `release/<version-or-short-description>` (only when a release task genuinely requires it)
- `proposal/<short-description>`
- `strategy/<short-description>`
- `review/<short-description>`

Rules:
1. Every temporary branch must have a clear task, owner, intended target, and expected completion.
2. The default target is `develop`. A task branch must not target `main` directly.
3. A release-preparation branch may target `staging` only when the release manager records why it is necessary.
4. A temporary branch must not be used as a substitute for `develop` or `staging`.
5. Merge or close the associated pull request, verify the resulting content, and delete the temporary branch promptly.
6. Target retirement within 30 days of merge or closure. If work remains active beyond 30 days, document the reason, owner and revised review date in the pull request.
7. Do not create parallel branches for successive versions of the same document unless the earlier branch is frozen and the replacement relationship is recorded.
8. Before deleting any branch, verify that unique commits and files are either integrated into an authoritative branch or intentionally rejected and archived where required.
9. A temporary branch must not be protected as a long-lived branch unless an explicit, time-limited exception is approved.

## 4. Standard development workflow

```text
temporary task branch
        |
        | pull request + review
        v
     develop
        |
        | release candidate promotion
        v
     staging
        |
        | acceptance + release approval
        v
      main
        |
        | version tag / release record
        v
   published release
```

Required sequence:
1. Start a task branch from the latest appropriate `develop` commit.
2. Make one coherent change and keep the pull request focused.
3. Open a pull request from the task branch to `develop`.
4. Review scope, evidence, tests, documentation, security, data rights and unresolved decisions as applicable.
5. Merge only after required review and checks.
6. Delete the task branch after verifying the merge.
7. When a release candidate is ready, promote `develop` to `staging` through a documented pull request.
8. Perform integrated acceptance and release-readiness checks on `staging`.
9. Resolve all release-blocking issues through `develop`, then re-promote and re-test.
10. Promote the approved release candidate from `staging` to `main` through a pull request.
11. Create an immutable version tag from the accepted `main` commit and publish release notes.

Do not routinely merge `main` back into `develop` as a substitute for controlled promotion. If an urgent production fix is needed, create a fix branch from `main`, open a pull request to `main`, and then back-port the same fix to `develop` and `staging` through reviewed pull requests.

## 5. Additional parallel workstreams

The three designated long-lived branches are fixed: `main`, `develop` and `staging`. No fourth long-lived branch is permitted during active development.

Additional parallel workstreams must use temporary task branches under Section 3. If many workstreams are active simultaneously:
- record the dependency graph and accountable owner for each branch;
- use stacked pull requests only when the dependency is explicit and the diff is reviewable;
- prefer task branches based on the latest appropriate `develop` commit;
- use draft PRs to make work and dependencies visible;
- archive decision records or release candidates with tags rather than creating another long-lived branch;
- review stale, duplicated and superseded branches monthly.

Operational pressure, release preparation or team parallelism does not create an exception to the three-long-lived-branch rule.

## 6. Pull request requirements

Every pull request must state:
- purpose and scope;
- source and target branches;
- related task, issue, ADR or decision record;
- files and data affected;
- evidence and tests performed, or why tests are not applicable;
- known limitations, unresolved questions and dependencies;
- licensing, attribution, privacy, security and data-rights implications where relevant;
- whether the branch is temporary and its retirement plan.

Stacked pull requests must explicitly identify their dependency order. Do not retarget or merge a dependent pull request until the dependency has been reviewed and the resulting diff is understood.

## 7. Repository maintenance and branch audit

At least monthly, and before each release:
- list all branches and classify each as one of the three long-lived branches or a temporary branch;
- identify branches with no open pull request, stale branches, duplicate document versions and branches with unique commits;
- inspect open pull requests and their base/head relationships;
- verify that merged work is present in the intended target;
- identify branches that can safely be deleted;
- record unresolved exceptions and owners.

The repository should enable automatic deletion of merged task branches where operationally suitable, but maintainers must still verify that unique work is preserved before deleting stale or superseded branches.

## 8. Project-completion and one-branch transition

The project is not considered complete merely because a first production release has been published. The project owner must formally approve the completion review.

Before deleting `develop` and `staging`, all of the following must be true:

- [ ] All approved product scope and required documentation are complete or explicitly deferred.
- [ ] All accepted changes from `develop`, `staging` and temporary branches are integrated into `main`.
- [ ] All open pull requests are merged, closed with a recorded reason, or otherwise formally resolved.
- [ ] All stacked/dependent pull requests have been resolved in dependency order.
- [ ] No unique required commit, document, test, decision or release artifact exists only on a branch scheduled for deletion.
- [ ] Automated tests, security checks, data validation and release acceptance checks have passed or have documented, approved exceptions.
- [ ] Data rights, licensing, provenance, privacy and operational handover reviews are complete.
- [ ] A final release tag and release notes exist on `main`.
- [ ] The final `main` branch is protected and remains the default branch.
- [ ] A repository backup/archive and completion record are retained.
- [ ] The project owner has explicitly approved branch retirement.

Then, in order:
1. Freeze new development and announce the completion candidate.
2. Verify the exact final commit on `main`.
3. Create and verify the final version tag and release record.
4. Confirm `develop` and `staging` contain no unique required work.
5. Delete `develop` and `staging`.
6. Delete all remaining temporary branches after the same preservation checks.
7. Re-fetch the repository branch list and verify that exactly one branch remains: `main`.
8. Record the verification date, final commit SHA, release tag and branch count in the completion record.

After completion, maintenance work should use short-lived task branches merged into `main`, then deleted. Do not recreate permanent `develop` or `staging` branches unless the project is formally reopened and the governance decision is recorded.

## 9. GitHub repository settings

Repository maintainers should configure and periodically verify GitHub rulesets or branch-protection rules for `main`, `develop` and `staging`:

- require pull requests before merging;
- require at least one approving review where an independent reviewer is available;
- require conversation resolution;
- block force pushes;
- prevent deletion of the three long-lived branches during active development;
- require linear history if the selected merge strategy and workflow support it;
- require only status checks that actually exist and are reliably maintained;
- do not configure a required status check that has not yet been implemented.

Protect `main` most strongly. Protect `develop` and `staging` against accidental direct pushes and deletion, while allowing reviewed promotion pull requests.

GitHub rulesets can govern branch creation, updates and deletion, but a naming pattern alone does not enforce a three-branch lifecycle. The branch inventory review and explicit retirement gate remain mandatory governance controls.

## 10. Current adoption note

This policy is proposed for adoption. The repository currently has more branches than the intended three-branch operating model. Existing branches and pull requests must be reconciled through a branch-by-branch preservation and dependency review. Do not delete, merge, or retarget existing work solely to make the branch count smaller.
