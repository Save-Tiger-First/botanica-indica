# Repository and Markdown Documentation Audit

**Audit ID:** STF-AUDIT-2026-11-20-01  
**Audit date:** 20 November 2026  
**Repository:** `Save-Tiger-First/botanica-indica`  
**Default branch:** `main`  
**Audit status:** Repository inventory and priority desk audit completed; specialist, legal and implementation validation remain outstanding  
**Audit branch:** `docs/repository-audit-and-ai-operating-standard`  
**Scope:** Repository metadata, branch/PR topology, governance controls, releases/automation, all Markdown paths and the highest-risk cross-document architecture and strategy files.

---

## 1. Executive assessment

The repository has a strong early documentation foundation and several sound scientific architecture principles. However, it is not yet governed or technically ready for implementation. The most serious risks are:

1. The three-long-lived-branch policy is proposed but not yet adopted or fully enforced.
2. The repository currently has 19 branches, including 16 supporting/topic branches; only `main`, `develop` and `staging` are intended to be long-lived.
3. There were 12 open pull requests at the initial audit snapshot; after opening PR #16, the current count is 13. No submitted PR reviews were returned for the initial 12-PR snapshot. Several dependent or divergent branches remain.
4. The active `main` ruleset only blocks branch deletion and non-fast-forward updates. It does not require pull requests, approvals, status checks or conversation resolution.
5. At the audit snapshot, main had no GitHub Actions workflows, workflow runs, releases or configured commit status checks. A proposed governance workflow has since been added on this audit branch; it has not run and is not yet part of main.
6. The ten accepted ADRs contained unclosed Markdown code fences. Narrow fixes have been committed on this audit branch; they are not yet merged.
7. The review pack contained an incorrect amendment to the Darwin Core release date and a stale Task 05C source SHA. Direct checks of the official TDWG pages confirm that both the Darwin Core List of Terms and Conceptual Model were issued 2026-05-26; the List's previous version is 2025-07-10.
8. Task 05D still contains a non-detection wording defect and does not fully capture the IdentificationSubject total-participation caveat.
9. The two competing Task 05C documents, PR #5 and PR #11 dependency, and PR #8/#12 strategy dependency require preservation-first reconciliation.
10. Strategy documents are extensive but overlapping; the 1,189-line NatureTech paper has heading-order and document-structure debt.

**Overall recommendation:** keep the project in documentation, scientific reconciliation and governance-readiness mode. Do not authorize Task 05E physical schema, production ingestion, AI training, public scientific claims or field intervention until the stated gates are met.

## 2. Audit method and limitations

### 2.1 What was inspected

- GitHub repository metadata and default branch.
- Live branch inventory and recursive trees for all 18 branches present before this audit branch was created.
- Current recursive tree of `main`.
- All 33 distinct Markdown paths found across the branch trees and their 39 distinct Markdown file revisions.
- Direct contents of the README, contribution guide, all ten accepted ADRs, the ecosystem architecture document, proposed ADR-011, licensing policy, Task 05/05B/05C/05D documents, scientific review pack, branch governance documents, organisational-readiness documents, NatureTech strategy and Bengaluru pilot documents.
- All open pull request metadata, changed filenames, head/base relationships and submitted review records.
- Main branch ruleset, commit status, releases and workflow runs.

### 2.2 What this audit does not claim

- The inventory covers all discovered Markdown paths and revisions. Deep semantic review focused on the highest-risk architecture, science, governance and strategy documents; this is not a substitute for qualified taxonomist, ecologist, biodiversity-informatics, security, legal or database-architect review of every statement.
- GitHub branch metadata and the active ruleset were inspected, but the branch-protection endpoint returned 403. Therefore, detailed effective settings beyond the visible repository ruleset are not independently established.
- No source code exists in the current `main` tree beyond documentation and the root license. This is a documentation-stage repository audit, not a code-quality or runtime audit.
- No external expert review, legal opinion, certification, field verification or scientific test execution is claimed.

## 3. Verified repository snapshot

### 3.1 Repository metadata

| Item | Verified result |
|---|---|
| Repository | `Save-Tiger-First/botanica-indica` |
| Visibility | Public |
| Default branch | `main` |
| Root license | Apache-2.0 |
| Issues | Enabled; zero open/closed non-PR issues returned in the inspected list |
| Releases | Zero |
| GitHub Actions runs at snapshot | Zero |
| Commit statuses on inspected main HEAD | Zero; state pending because no statuses exist |
| Recursive tree for main | 18 entries including directories; 13 Markdown files |
| Source code / workflow implementation on main | None found in inspected tree |
| Current main HEAD at audit | `f165ecb9b4d9de115c02327cf779982b7ef4bbd4` |

The README's repository-structure example is not a complete representation of the current tree. The root `LICENSE` exists, but the example tree does not show all current documentation folders or governance files. Update it after the governance/document consolidation plan is adopted.

### 3.2 Branch inventory

**Branch-count clarification:** the earlier branch register records 18 branches at its own snapshot. This audit branch was created afterwards, bringing the current total to 19.

| Branch | Role/disposition | Current observation |
|---|---|---|
| `main` | Permanent canonical branch | Protected flag true; active ruleset exists |
| `develop` | Long-lived integration branch | Same starting SHA as main; protected flag false |
| `staging` | Long-lived release-candidate branch | Same starting SHA as main; protected flag false |
| `docs/adr-011-stf-ecosystem-boundaries` | Temporary proposal branch | Open PR #2 |
| `docs/asset-specific-licensing-policy` | Temporary policy branch | Open PR #1 |
| `docs/task-05-data-architecture` | Temporary Task 05 branch | Open PR #3 |
| `docs/task-05-data-dictionary` | Temporary Task 05B branch | Open PR #4 |
| `docs/task-05c-logical-data-model` | Canonical Task 05C candidate | Open PR #5 |
| `docs/task-05c-logical-database-model` | Competing/superseded candidate | PR #6 closed; unique content still needs preservation decision |
| `docs/task-05d-logical-model-validation` | Superseded Task 05D branch | PR #7 closed; unique content reconciliation required |
| `docs/task-05d-logical-model-validation-v2` | Superseded Task 05D branch | PR #10 closed; compare unique Task 05C history/content |
| `docs/task-05d-logical-model-validation-v3` | Current Task 05D dependent branch | Open stacked PR #11 based on PR #5 |
| `governance/branch-lifecycle-policy` | Branch governance proposal | Open PR #15 to develop |
| `governance/stf-organisational-readiness-review` | Organisational readiness proposal | Open PR #12, stacked on PR #8 |
| `proposal/bengaluru-urban-biodiversity-feasibility-pilot` | Pilot proposal | Open PR #13 |
| `research/bengaluru-pilot-site-selection` | Site assessment | Open PR #14 |
| `review/scientific-data-model-review-pack` | Scientific review pack | Open PR #9 |
| `strategy/naturetech-biodiversity-conservation-impact` | NatureTech strategy | Open PR #8 |
| `docs/repository-audit-and-ai-operating-standard` | This audit and operating-standard work | New temporary audit branch; PR not yet opened at the time of snapshot |

**Verified total at audit snapshot: 19 branches — 3 intended long-lived branches and 16 supporting/topic branches.** The branch count is not compliant with the eventual operating target yet. Topic branches are allowed temporarily, but must have a task, PR/dependency and retirement plan.

### 3.3 Pull-request inventory

At the snapshot there were 12 open PRs and three closed, unmerged PRs. All 12 open PRs had no submitted review records returned by the GitHub review-list endpoint.

| PR | Subject | Base | Status | Audit judgement |
|---:|---|---|---|---|
| #1 | Asset-specific licensing and IP policy | main | Open, draft | Proposed policy; legal/maintainer review needed |
| #2 | ADR-011 ecosystem boundaries | main | Open, draft | Proposed ADR; align with companion architecture and existing ADRs |
| #3 | Task 05 data architecture | main | Open, draft | Revised on branch; needs cross-document and specialist review |
| #4 | Task 05B data dictionary | main | Open, draft | Revised on branch; needs specialist review and test fixtures |
| #5 | Task 05C logical model | main | Open, draft | Preferred canonical review candidate; not approved |
| #8 | NatureTech and conservation strategy | main | Open, draft | Large strategy document; governance and scope review |
| #9 | Scientific data model review pack | main | Open, draft | Review instrument; not independent expert approval |
| #11 | Task 05D validation | PR #5 branch | Open, draft | Stacked; base/head diverged by one commit each at audit |
| #12 | Organisational readiness | PR #8 branch | Open, draft | Stacked; base/head diverged (four ahead, three behind) |
| #13 | Bengaluru pilot proposal | main | Open, draft | Proposal only; no site, budget or fieldwork approval |
| #14 | Bengaluru site assessment | main | Open, draft | Preliminary assessment; no site selected |
| #15 | Branching and release governance | develop | Open, ready for review | Policy proposal; should be reviewed before adoption |

Closed PRs:
- #6: competing Task 05C document; closed without merge.
- #7: earlier Task 05D validation branch; closed without merge.
- #10: Task 05D v2; closed without merge.

No PR was merged in the inspected PR inventory.

### 3.4 Dependency graph and divergence

- PR #11 is based on PR #5. Current compare result: `docs/task-05d-logical-model-validation-v3` is one commit ahead and one behind the updated `docs/task-05c-logical-data-model` base. Do not merge until the full diff is synchronized and reviewed.
- PR #12 is based on PR #8. Current compare result: four commits ahead and three behind. Reconcile the overlapping strategy files and history before merging.
- PR #14 is a separate site assessment for PR #13's pilot proposal. Review them together and preserve the no-site-selected status.
- PR #9 is a review package and must not be treated as a scientific approval or substitute for external reviewers.
- PRs #1 and #2 are proposals, not approved licensing policy or accepted ADR-011.

## 4. Branch governance and security audit

### 4.1 Active main ruleset

The GitHub API returned one active repository ruleset:
- Name: `Protect main branch`
- Target: branch
- Condition: default branch
- Rules: deletion blocked; non-fast-forward updates blocked
- Bypass actors: none
- Current user bypass: never

This is useful but insufficient. The active ruleset does **not** include:
- required pull requests;
- required approving reviews;
- required conversation resolution;
- required status checks;
- required signed commits;
- linear-history enforcement.

The branch-protection endpoint itself returned 403, so no broader branch-protection settings are asserted here.

### 4.2 Supporting branches

GitHub reports `develop` and `staging` as unprotected. They should receive appropriate rules once the owner configures the settings. Do not add required status checks until the corresponding workflows have actually run and produced stable check names.

### 4.3 Branch governance recommendation

Adopt PR #15 after review, then configure GitHub rulesets manually:
- protect main against deletion and force-push;
- require PRs and independent approval where available;
- require conversation resolution;
- add actual stable CI checks only after implementation;
- protect develop and staging against accidental deletion/force-push while allowing reviewed promotion PRs;
- maintain monthly branch inventory and pre-release audit.

A GitHub workflow can validate PR routing and Markdown structure. It cannot by itself guarantee that unused branches are deleted safely; preservation-first branch retirement remains a human governance decision.

## 5. Markdown inventory — all distinct paths discovered

The initial pre-audit branch inventory contained **33 distinct Markdown paths and 39 distinct file revisions** across the then-existing branch trees. The audit branch subsequently added two Markdown documents (this report and the permanent AI prompt), so the current audit branch contains at least 35 distinct Markdown paths; a fresh all-branch revision count was not recomputed. Most revisions are identical across branches; the following register identifies the distinct document paths and their current owning/candidate branch.

| # | Markdown path | Branch/ref | Audit observation |
|---:|---|---|---|
| 1 | `README.md` | main | Good project framing; duplicate H1; repository tree and ADR inventory need updating as docs mature |
| 2 | `CONTRIBUTING.md` | main | Strong scientific/provenance principles; development workflow says branching policy will evolve; align with PR #15 |
| 3 | `.github/pull_request_template.md` | governance/branch-lifecycle-policy | Useful branch routing/evidence checklist; proposed until PR #15 adopted |
| 4 | `docs/adr/ADR-001-architecture-principles.md` | main | Accepted; unclosed code fence fixed on audit branch |
| 5 | `docs/adr/ADR-002-modular-architecture.md` | main | Accepted; unclosed code fence fixed on audit branch |
| 6 | `docs/adr/ADR-003-api-first-platform.md` | main | Accepted; unclosed code fence fixed on audit branch |
| 7 | `docs/adr/ADR-004-data-and-scientific-provenance.md` | main | Accepted; unclosed code fence fixed on audit branch |
| 8 | `docs/adr/ADR-005-taxonomy-reconciliation.md` | main | Accepted; unclosed code fence fixed on audit branch; taxonomy vocabulary should be reconciled with Task 05B/05C |
| 9 | `docs/adr/ADR-006-identification-architecture.md` | main | Accepted; unclosed code fence fixed on audit branch; confidence/calibration implementation remains future work |
| 10 | `docs/adr/ADR-007-evidence-and-expert-validation.md` | main | Accepted; unclosed code fence fixed on audit branch; evidence relationships need controlled semantics |
| 11 | `docs/adr/ADR-008-geospatial-and-sensitive-location-data.md` | main | Accepted; unclosed code fence fixed on audit branch; needs threat-tested access/export rules |
| 12 | `docs/adr/ADR-009-observation-and-contribution-model.md` | main | Accepted; unclosed code fence fixed on audit branch; reconcile Observation vs Occurrence semantics with Task 05 |
| 13 | `docs/adr/ADR-010-data-ingestion-and-source-integration.md` | main | Accepted; unclosed code fence fixed on audit branch; rights and raw-payload rules need operational gates |
| 14 | `docs/adr/ADR-011-stf-ecosystem-boundaries.md` | docs/adr-011-stf-ecosystem-boundaries | Proposed; companion architecture document exists on main; align status, scope and ownership |
| 15 | `docs/architecture/STF-ECOSYSTEM-BOUNDARIES.md` | main | Detailed companion architecture; proposed boundary concepts, not deployed shared services |
| 16 | `docs/architecture/TASK-05C-LOGICAL-DATABASE-MODEL.md` | docs/task-05c-logical-data-model | Preferred canonical review candidate; still has unresolved Event/Occurrence, Observation/Event and total-participation issues |
| 17 | `docs/data-architecture/DATA-ARCHITECTURE-AND-SCIENTIFIC-DATA-MODEL.md` | docs/task-05-data-architecture | Proposed Task 05; Event/Survey/Occurrence wording recently improved; cross-document review remains |
| 18 | `docs/data-architecture/SCIENTIFIC-DATA-DICTIONARY-AND-INDIAN-TEST-CASES.md` | docs/task-05-data-dictionary | Proposed Task 05B; strong source-role distinctions and TCS semantics; verify examples and full subject/cardinality model |
| 19 | `docs/data-architecture/TASK-05C-LOGICAL-DATABASE-MODEL-AND-SCIENTIFIC-RELATIONSHIPS.md` | docs/task-05c-logical-database-model | Competing Task 05C; PR #6 closed; preserve useful workflows/cardinality notes selectively; do not merge wholesale |
| 20 | `docs/data-architecture/TASK-05D-LOGICAL-MODEL-VALIDATION-AND-PHYSICAL-DESIGN-READINESS.md` | docs/task-05d-logical-model-validation-v3 | Task 05D validation gate; still has a wording defect and incomplete total-participation caveat |
| 21 | `docs/governance/BRANCH-INVENTORY-AND-CONSOLIDATION-REGISTER.md` | governance/branch-lifecycle-policy | Snapshot says 18 branches before this audit branch; now stale and needs refreshed inventory |
| 22 | `docs/governance/BRANCHING-AND-RELEASE-GOVERNANCE.md` | governance/branch-lifecycle-policy | Clear three-long-lived-branch and one-branch-completion policy; proposed, not yet adopted/enforced |
| 23 | `docs/governance/LICENSING-AND-IP-POLICY.md` | docs/asset-specific-licensing-policy | Strong asset/purpose-specific policy proposal; requires legal/maintainer approval and contributor terms |
| 24 | `docs/governance/STF-ORGANISATIONAL-READINESS-AND-GOVERNANCE-REVIEW.md` | governance/stf-organisational-readiness-review | Strong evidence register; correctly says NOT ASSESSED; legal currency must be rechecked before reliance |
| 25 | `docs/reviews/SCIENTIFIC-DATA-MODEL-REVIEW-PACK.md` | review/scientific-data-model-review-pack | Good review structure; stale Darwin Core version statement and stale Task 05C blob SHA require correction |
| 26 | `docs/reviews/SCIENTIFIC-DATA-MODEL-VALIDATION-MATRIX-AND-DECISION-REGISTER.md` | review/scientific-data-model-review-pack | Good decision/test register; update Task 05D typo, DR-02 caveat and current source revisions |
| 27 | `docs/reviews/TASK-05C-COMPETING-MODEL-RECONCILIATION.md` | review/scientific-data-model-review-pack | Useful desk assessment; source revision metadata and Darwin Core version need refresh |
| 28 | `docs/strategy/INDIGENOUS-STEWARDSHIP-TEK-AND-COMMUNITY-DATA-GOVERNANCE.md` | governance/stf-organisational-readiness-review and strategy branch | Two distinct revisions exist; later strategy branch expands source-talk coverage; reconcile to one canonical document |
| 29 | `docs/strategy/STF-12-MONTH-ORGANISATIONAL-ROADMAP-AND-IMPLEMENTATION-PLAN.md` | governance/stf-organisational-readiness-review and strategy branch | Roadmap proposal; budget is indicative, not approved; preserve gates and capacity assumptions |
| 30 | `docs/strategy/STF-NATURETECH-AND-CONSERVATION-STRATEGIC-FRAMEWORK.md` | governance/stf-organisational-readiness-review and strategy branch | Strategic framework proposal; companion long strategy overlaps; choose one canonical hierarchy |
| 31 | `docs/strategy/STF-NATURETECH-BIODIVERSITY-INTELLIGENCE-AND-CONSERVATION-IMPACT.md` | strategy/naturetech-biodiversity-conservation-impact and governance branch | Very long 1,189-line paper; heading numbering/order needs cleanup; keep strategic context distinct from approved programme |
| 32 | `docs/strategy/STF-BENGALURU-URBAN-BIODIVERSITY-FEASIBILITY-PILOT-PROPOSAL.md` | proposal/bengaluru-urban-biodiversity-feasibility-pilot | Proposal only; no site selected, no permission, no partner or expenditure approval |
| 33 | `docs/strategy/STF-BENGALURU-PILOT-SITE-SELECTION-ASSESSMENT.md` | research/bengaluru-pilot-site-selection | Preliminary desk comparison; no site selected; current authority/management must be reverified |

## 6. Markdown quality findings

### 6.1 Confirmed structural defects

**Ten accepted ADRs:** ADR-001 through ADR-010 each had one unclosed fenced code block. The issue was not that there were odd numbers of code markers in a simple count alone; direct inspection showed the diagram's closing fence missing, causing following prose to render as code. A narrow closing fence has been inserted in each of the ten files on this audit branch. The fixes preserve all existing prose and diagram text.

**README:** two H1 headings (`# botanica-indica` and `# Botanica Indica`). Recommend one canonical title and remove the duplicate.

**Task 05D heading order:** section 4.2 appears before 4.1; subheadings 2.1B appears before 2.1A. Reorder without changing meaning.

**Task 05D non-detection wording:** FLD-08 currently says “no row is never interpreted as absence”, which is ambiguous/incorrect. Replace with “the absence of an Occurrence row must never be interpreted as evidence of absence.” The DR-07 row has similarly awkward “no row must never imply absence” wording and should be made consistent.

**NatureTech strategy:** section 21 subheadings are out of numerical order (21.10 and 21.11 appear before 21.8 and 21.9). This is a navigation and editorial defect in a very long document. Reorder the headings and any references without changing substantive claims.

### 6.2 Link and navigation findings

The inspected relative Markdown links in README, branch governance, NatureTech framework and Bengaluru site assessment resolve to companion files in their respective branch trees. However, a repository-wide automated relative-link check is not yet installed. Add one and review its first run for intentional cross-branch references.

The README's repository tree is incomplete compared with the live repository structure. Update it after canonical documentation paths are settled.

### 6.3 Version and metadata findings

- A subsequent review-pack amendment incorrectly claimed the Darwin Core Conceptual Model was issued 2026-10-13. Direct inspection of the official TDWG page confirms the issued version is 2026-05-26.
- The review pack/reconciliation report cites Task 05C Candidate A blob `e6131e867d4bc3dbc58aa1188d0fabc895429347`. The current PR #5 branch file is blob `4a21c0aa3b8ebfef319a9ea1ac6928274b0b3f5b`. The older `e6131e...` blob remains on the PR #11 dependent branch. Update the source revision table and re-review the dependency.
- The competing Task 05C Candidate B blob remains `239d7e9974bcb81b1154b54845a7b2d69c3775d6` on its superseded branch.
- The branch inventory register is a dated snapshot, not a live source of truth. It now needs an audit entry for this new audit branch and future refreshes.

## 7. Cross-document scientific and architecture findings

### 7.1 Taxonomy and TCS

The overall direction is sound: separate TaxonName, TaxonConcept, TaxonomicTreatment and TaxonNameUsage. TCS requires a TaxonConcept to have exactly one `taxonName` and one `accordingTo` resource. TCS synonym relations connect TaxonConcept to TaxonName, while concept mappings compare two TaxonConcepts and use the six defined mapping relations.

Remaining review:
- ensure the internal concept's according-to resource resolves to one canonical resource;
- keep name-to-name nomenclatural relationships separate from concept-to-name synonym assertions and concept-to-concept mappings;
- review treatment, source, publication and resource identity with a qualified taxonomist/biodiversity-informatics specialist;
- do not infer global accepted status from one source.

### 7.2 Event, Survey, Occurrence and Observation

The official Darwin Core Conceptual Model issued 2026-05-26 treats Survey and Occurrence as specialized Event types. It is a high-level, non-normative semantic framework and does not prescribe a database schema.

Task 05 was updated to state this. Task 05C still needs an explicit logical decision and cardinalities:
- Does the internal model use an Event supertype with Survey and Occurrence specializations/extensions?
- How are nested events represented?
- Can a contextual survey provide shared time/location to multiple Occurrences and Material Entities?
- How does contributor Observation link to capture Event, Survey and one or more Occurrences?
- How is an explicit non-detection target result represented without equating missing records with absence?

My recommendation remains to evaluate an Event supertype/shared identity with Survey and Occurrence specializations, while keeping Botanica Indica Observation as a distinct contributor/workflow record. This is a recommendation, not a final schema decision.

### 7.3 IdentificationSubject

Task 05B and Task 05C now align on one IdentificationSubject row with three nullable real target FKs and a row-local exactly-one CHECK. However, the CHECK only ensures exactly one target on an existing subject row. It does not ensure every Identification has a subject row. The model needs an explicit total-participation strategy and negative tests.

Task 05D DR-02 currently records the CHECK and typed-link decision but does not state the total-participation caveat. This must be updated before PR #11 is considered stable.

### 7.4 ScientificAssertion subject inventory

Task 05B uses explicit typed assertion-subject links, which is safer than unconstrained polymorphic subject_type/subject_id. It still needs a complete governed target inventory, predicate compatibility rules and cardinality tests. A generic list of possible subjects is not enough; each predicate must define what kinds of subjects are valid.

### 7.5 GBIF profile separation

Current GBIF technical documentation distinguishes general occurrence datasets from GBIF-managed programmes and sampling-event datasets. For general occurrence publishing, `occurrenceID` is required; `basisOfRecord`, `scientificName` and `eventDate` are strongly recommended, while GBIF-managed programmes can require them. Sampling-event datasets have distinct event/protocol/sample-size/effort expectations. Do not turn export-profile rules into universal internal validity rules.

### 7.6 PostgreSQL integrity

PostgreSQL 18 explicitly states that CHECK constraints cannot safely reference other rows/tables. Use real foreign keys and unique constraints for target integrity, plus a transactionally safe mechanism for total participation. Do not claim a row-local CHECK alone enforces cross-row existence.

## 8. Product, strategy and organisational governance findings

### 8.1 NatureTech strategy overlap

The repository contains:
- a 488-line NatureTech and Conservation Strategic Framework;
- a 1,189-line NatureTech/Biodiversity Intelligence/Conservation Impact strategy;
- a 291-line 12-month organisational roadmap;
- an Indigenous stewardship/TEK governance document in two revisions;
- an organisational readiness diagnostic.

These should be arranged as a clear document hierarchy. Recommended:
1. Strategic Framework — concise approved strategy when authorized.
2. Detailed NatureTech research paper — evidence and supporting rationale, not competing strategy.
3. 12-month roadmap — time-bound plan approved only after organizational readiness.
4. Indigenous/TEK governance — cross-cutting proposed policy requiring community and legal review.
5. Organisational readiness review — diagnostic evidence register, not a certification.

Resolve PR #8 before PR #12. The two branches are divergent and contain overlapping strategy files. Preserve unique research; do not merge both copies blindly.

### 8.2 Bengaluru pilot

The pilot proposal correctly says no site is pre-approved and fieldwork is gated. The site-selection assessment ranks candidates preliminarily, but no site should be represented as selected. Reverify current legal custodian, delegated authority, partner roles, permissions, existing survey activity and ecological protocols before site selection. The 12-week proposal cannot prove ecological improvement.

### 8.3 Organisational readiness

The readiness review correctly states NOT ASSESSED because primary evidence about legal form, governing authority, finances, registrations, FCRA/CSR eligibility, staffing and insurance has not been provided/verified. Preserve this status until primary documents and qualified professional review exist.

### 8.4 Licensing/IP

The asset-specific licensing approach is appropriate. The root Apache-2.0 license must not be interpreted as licensing datasets, photographs, user contributions, scientific publications, AI training data or trademarks. The policy remains proposed and requires legal/maintainer review plus a contributor rights process.

## 9. Priority remediation register

| ID | Severity | Finding | Required action | Gate |
|---|---|---|---|---|
| AUD-01 | Critical | Main ruleset lacks PR/review/status-check rules; develop/staging unprotected | Configure reviewed GitHub rulesets; add actual CI first | Before substantive implementation |
| AUD-02 | Critical | Branch inventory exceeds intended three long-lived branches; 16 topic branches | Preservation-first branch-by-branch register, dependency reconciliation, retirement | Monthly and before release |
| AUD-03 | Critical | No CI/workflow, no status checks, no release automation | Add Markdown/branch policy workflow now; add tests/security scans as code appears | Before merge of governance automation |
| AUD-04 | Critical | Task 05C Event/Survey/Occurrence and Observation/Event model unresolved | Formal logical decision, cardinality and fixtures with specialist review | Before Task 05E |
| AUD-05 | Critical | Task 05D DR-02 omits total participation; FLD-08 wording defective | Correct and synchronize PR #11 against latest PR #5 | Before Task 05D acceptance |
| AUD-06 | Major | Review pack has stale Darwin Core version and Task 05C SHA | Refresh citations and exact blob/commit revision references | Before external review |
| AUD-07 | Major | PR #8/#12 diverged and duplicate strategy docs exist | Compare complete file/commit history; one canonical document per subject | Before strategy consolidation |
| AUD-08 | Major | PR #11/#5 diverged | Synchronize and full-diff review; no blind merge | Before Task 05D merge |
| AUD-09 | Major | No PR reviews submitted | Recruit/record actual qualified reviewers; no self-approval claims | Before scientific approval |
| AUD-10 | Major | No automated Markdown/link validation | Add workflow and fix baseline defects | Before governance PR merge |
| AUD-11 | Major | README structure and ADR list incomplete | Update after canonical docs and ADR-011 status decision | Before first public release |
| AUD-12 | Major | Two Indigenous stewardship document versions | Preserve unique content and choose one canonical revision | Before policy approval |
| AUD-13 | Major | 1,189-line NatureTech paper heading order/structure | Reorganize without altering evidence or claims; maintain research appendix | Before strategy approval |
| AUD-14 | Major | No code, tests, API contracts or implementation in main | Do not represent repository as production-ready; plan implementation only after gates | Product implementation stage |
| AUD-15 | Major | No releases/tags | Establish release/tag process after first reviewed milestone | First release |
| AUD-16 | Moderate | PR #15 branch register is already stale after new audit branch | Refresh inventory and branch retirement status at each governance change | Monthly |
| AUD-17 | Moderate | README has duplicate H1 | Single H1 and polished navigation | Documentation release |
| AUD-18 | Moderate | Task 05D heading order inconsistent | Reorder headings and check internal references | Before review |
| AUD-19 | Moderate | No automated stale-branch age/ownership report | Add monthly inventory checklist; no auto-delete | Monthly |

## 10. Remediation work completed on this audit branch

The following changes have been made on `docs/repository-audit-and-ai-operating-standard`:
- Added a permanent AI project operating prompt.
- Added this repository/Markdown audit report.
- Added a closing code fence to each of ADR-001 through ADR-010, without changing diagram or prose content; all ten files were re-fetched and verified to have balanced fence markers.
- Removed the duplicate H1 from README and updated its repository-tree example to match the files on this audit branch; added links to the permanent AI prompt and audit report.
- Added a least-privilege GitHub Actions workflow and Python checker for Markdown fence integrity and PR branch routing. The workflow has now completed successfully on PR #16; successful run ID 44682525905 (head eddd8a012f1bdf3677271afaa02adea1714ff4f8) passed the Markdown integrity and branch-routing job. The workflow has not yet been merged into main.
- The changes have not been merged. They require review through the project's branch workflow.
- No existing branch was deleted, no existing PR was merged/closed/retargeted, and no branch-protection settings were changed.

## 11. Recommended implementation sequence

1. Review this audit and permanent AI prompt.
2. Review/adopt PR #15 branch lifecycle policy.
3. Add branch-routing and Markdown structural validation workflow; run it and inspect results.
4. Correct README title/tree and document index.
5. Refresh PR #9 standards version and exact source revisions.
6. Correct Task 05D wording and DR-02 caveat, then synchronize PR #11.
7. Resolve Event/Survey/Occurrence and Observation/Event design with specialist review.
8. Reconcile Task 05C competing document; preserve selected workflows/cardinality notes.
9. Resolve PR #8/#12 strategy overlap and choose canonical Indigenous stewardship document.
10. Review licensing, ADR-011 and organisational readiness with appropriate maintainers/professionals.
11. Complete scientific and rights test fixtures; only then assess Task 05E readiness.
12. Consolidate branches gradually to main/develop/staging; at formal project completion retire develop and staging so only main remains.

---

## 12. Research and authoritative references

Checked for this audit on 20 November 2026:

1. TDWG, Darwin Core List of Terms, version issued 2026-05-26; previous List version 2025-07-10: https://dwc.tdwg.org/list/
2. TDWG, Darwin Core Conceptual Model, version issued 2026-05-26: https://dwc.tdwg.org/cm/
3. TDWG, Taxon Concept Standard Terms: https://tcs.tdwg.org/terms/
4. GBIF, Data Quality Recommendations: https://techdocs.gbif.org/en/data-publishing/data-quality-recommendations
5. PostgreSQL 18, Constraints: https://www.postgresql.org/docs/18/ddl-constraints.html
6. GitHub repository rulesets documentation: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets
7. GitHub branch protection documentation: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches

**Final audit judgement:** The repository has a credible documentation foundation, but it is not ready for implementation or external claims of scientific validation. The immediate priority is governance automation, source/version correctness, scientific-model resolution and preservation-first branch consolidation.


## 13. Standards-date correction after direct source re-verification (20 November 2026)

The first amendment made during this audit incorrectly stated that the current Darwin Core List of Terms and Conceptual Model were issued 2026-10-13. Directly opening the official TDWG pages shows that both were issued **2026-05-26**. The List page identifies **2025-07-10** as its previous version. The `occurrenceStatus` term itself was modified **2026-05-26**. The earlier correction was wrong; affected Task 05, Task 05B, Task 05D and PR #9 review documents have been corrected to reflect the source pages. Sources: https://dwc.tdwg.org/list/ and https://dwc.tdwg.org/cm/.
