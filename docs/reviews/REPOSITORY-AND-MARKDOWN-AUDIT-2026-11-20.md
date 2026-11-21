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
5. At the initial audit snapshot, main had no GitHub Actions workflows, workflow runs, releases or configured commit status checks. The proposed repository-governance workflow has since run successfully on the audit branch at commit `9c150d90b3d8fd627be0da1550da1acf4a90f4f1` (run #17); it is still not part of `main`, and no required status check is configured.
6. The ten accepted ADRs contained unclosed Markdown code fences. Narrow fixes have been committed on this audit branch; they are not yet merged.
7. Darwin Core version metadata requires fresh resolution: latest indexed official metadata reports 2026-10-13 for both the List of Terms and Conceptual Model, while direct HTML retrieval returned 2026-05-26 for the List. Treat DR-09 as open until exact versioned documents and term IRIs are independently verified.
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
| #11 | Task 05D validation | PR #5 branch | Open, draft | Stacked; current compare is two commits ahead and one behind |
| #12 | Organisational readiness | PR #8 branch | Open, draft | Stacked; base/head diverged (four ahead, three behind) |
| #13 | Bengaluru pilot proposal | main | Open, draft | Proposal only; no site, budget or fieldwork approval |
| #14 | Bengaluru site assessment | main | Open, draft | Preliminary assessment; no site selected |
| #16 | Repository audit and AI operating standard | develop | Open, draft | Adds audit, permanent prompt, ADR Markdown fixes, README correction and governance workflow; workflow passed on current branch |
| #15 | Branching and release governance | develop | Open, ready for review | Policy proposal; should be reviewed before adoption |

Closed PRs:
- #6: competing Task 05C document; closed without merge.
- #7: earlier Task 05D validation branch; closed without merge.
- #10: Task 05D v2; closed without merge.

No PR was merged in the inspected PR inventory.

### 3.4 Dependency graph and divergence

- PR #11 is based on PR #5. Current compare result: `docs/task-05d-logical-model-validation-v3` is two commits ahead and one behind `docs/task-05c-logical-data-model`. Task 05D's DR-02 total-participation caveat and FLD-08/DR-07 wording have been corrected on the PR #11 branch. Do not merge until the branch is synchronized with the latest PR #5 head and the full diff is re-reviewed.
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
| 1 | `README.md` | main | Good project framing; duplicate H1 in main snapshot corrected on PR #16 branch; repository tree and ADR inventory need final review |
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
| 20 | `docs/data-architecture/TASK-05D-LOGICAL-MODEL-VALIDATION-AND-PHYSICAL-DESIGN-READINESS.md` | docs/task-05d-logical-model-validation-v3 | Task 05D validation gate; DR-02 total-participation caveat and FLD-08 wording corrected on PR #11 branch; synchronization with PR #5 remains |
| 21 | `docs/governance/BRANCH-INVENTORY-AND-CONSOLIDATION-REGISTER.md` | governance/branch-lifecycle-policy | Refreshed on PR #15 branch to 19 branches and 13 open PRs; continue re-verification before each disposition |
| 22 | `docs/governance/BRANCHING-AND-RELEASE-GOVERNANCE.md` | governance/branch-lifecycle-policy | Clear three-long-lived-branch and one-branch-completion policy; proposed, not yet adopted/enforced |
| 23 | `docs/governance/LICENSING-AND-IP-POLICY.md` | docs/asset-specific-licensing-policy | Strong asset/purpose-specific policy proposal; requires legal/maintainer approval and contributor terms |
| 24 | `docs/governance/STF-ORGANISATIONAL-READINESS-AND-GOVERNANCE-REVIEW.md` | governance/stf-organisational-readiness-review | Strong evidence register; correctly says NOT ASSESSED; legal currency must be rechecked before reliance |
| 25 | `docs/reviews/SCIENTIFIC-DATA-MODEL-REVIEW-PACK.md` | review/scientific-data-model-review-pack | Corrected on PR #9 branch for TDWG release dates and current Task 05C blob SHA; specialist review remains outstanding |
| 26 | `docs/reviews/SCIENTIFIC-DATA-MODEL-VALIDATION-MATRIX-AND-DECISION-REGISTER.md` | review/scientific-data-model-review-pack | Updated for current Task 05C blob, corrected TDWG release metadata and re-opened DR-09; tests remain unexecuted |
| 27 | `docs/reviews/TASK-05C-COMPETING-MODEL-RECONCILIATION.md` | review/scientific-data-model-review-pack | Updated source revision and Darwin Core Conceptual Model issue date; still a desk assessment |
| 28 | `docs/strategy/INDIGENOUS-STEWARDSHIP-TEK-AND-COMMUNITY-DATA-GOVERNANCE.md` | governance/stf-organisational-readiness-review and strategy branch | Two distinct revisions exist; later strategy branch expands source-talk coverage; reconcile to one canonical document |
| 29 | `docs/strategy/STF-12-MONTH-ORGANISATIONAL-ROADMAP-AND-IMPLEMENTATION-PLAN.md` | governance/stf-organisational-readiness-review and strategy branch | Roadmap proposal; budget is indicative, not approved; preserve gates and capacity assumptions |
| 30 | `docs/strategy/STF-NATURETECH-AND-CONSERVATION-STRATEGIC-FRAMEWORK.md` | governance/stf-organisational-readiness-review and strategy branch | Strategic framework proposal; companion long strategy overlaps; choose one canonical hierarchy |
| 31 | `docs/strategy/STF-NATURETECH-BIODIVERSITY-INTELLIGENCE-AND-CONSERVATION-IMPACT.md` | strategy/naturetech-biodiversity-conservation-impact and governance branch | Very long 1,189-line paper; heading numbering/order needs cleanup; keep strategic context distinct from approved programme |
| 32 | `docs/strategy/STF-BENGALURU-URBAN-BIODIVERSITY-FEASIBILITY-PILOT-PROPOSAL.md` | proposal/bengaluru-urban-biodiversity-feasibility-pilot | Proposal only; no site selected, no permission, no partner or expenditure approval |
| 33 | `docs/strategy/STF-BENGALURU-PILOT-SITE-SELECTION-ASSESSMENT.md` | research/bengaluru-pilot-site-selection | Preliminary desk comparison; no site selected; current authority/management must be reverified |
| 34 | `docs/governance/AI-PROJECT-OPERATING-PROMPT.md` | docs/repository-audit-and-ai-operating-standard | Permanent project operating prompt; proposed until PR #16 is reviewed and merged |
| 35 | `docs/reviews/REPOSITORY-AND-MARKDOWN-AUDIT-2026-11-20.md` | docs/repository-audit-and-ai-operating-standard | Repository, Markdown, branch and PR audit; dated snapshot with subsequent correction log |

## 6. Markdown quality findings

### 6.1 Confirmed structural defects

**Ten accepted ADRs:** ADR-001 through ADR-010 each had one unclosed fenced code block. The issue was not that there were odd numbers of code markers in a simple count alone; direct inspection showed the diagram's closing fence missing, causing following prose to render as code. A narrow closing fence has been inserted in each of the ten files on this audit branch. The fixes preserve all existing prose and diagram text.

**README:** the audit snapshot on main had two H1 headings (`# botanica-indica` and `# Botanica Indica`). The duplicate has been removed on the PR #16 audit branch; review/merge remains pending.

**Task 05D heading order:** the audit snapshot had section 4.2 before 4.1. The sections have been reordered on the PR #11 branch. The earlier 2.1B/2.1A note was not reproduced in the latest fetched version and should not be treated as a confirmed current defect.

**Task 05D non-detection wording:** the audit snapshot used ambiguous double-negative wording in DR-07 and FLD-08. Both have now been corrected on the PR #11 branch to state that the absence of an Occurrence row must never be interpreted as evidence of absence.

**NatureTech strategy:** section 21 subheadings are out of numerical order (21.10 and 21.11 appear before 21.8 and 21.9). This is a navigation and editorial defect in a very long document. Reorder the headings and any references without changing substantive claims.

### 6.2 Link and navigation findings

The inspected relative Markdown links in README, branch governance, NatureTech framework and Bengaluru site assessment resolve to companion files in their respective branch trees. A relative-link scanner has now been added to the governance script on PR #16; unresolved paths are warnings, not failures, and its first successful run does not prove every historical branch link is valid.

The README's repository tree was incomplete in the audit snapshot. It has been updated on the PR #16 branch to reflect the current audit-branch structure; refresh again after canonical documentation paths are settled.

### 6.3 Version and metadata findings

- A subsequent review-pack amendment incorrectly claimed the Darwin Core Conceptual Model was issued 2026-10-13. Direct inspection of the official TDWG page confirms the issued version is 2026-05-26.
- The review pack/reconciliation report previously cited Task 05C Candidate A blob `e6131e867d4bc3dbc58aa1188d0fabc895429347`. The current PR #5 branch file is blob `4a21c0aa3b8ebfef319a9ea1ac6928274b0b3f5b`. The PR #9 review pack and decision register have been updated to cite the current PR #5 blob; PR #11 remains dependent on an older base and must be synchronized and re-reviewed.
- The competing Task 05C Candidate B blob remains `239d7e9974bcb81b1154b54845a7b2d69c3775d6` on its superseded branch.
- The branch inventory register is a dated snapshot, not a live source of truth. It has been refreshed on PR #15 branch to record 19 branches and 13 open PRs.

## 7. Cross-document scientific and architecture findings

### 7.1 Taxonomy and TCS

The overall direction is sound: separate TaxonName, TaxonConcept, TaxonomicTreatment and TaxonNameUsage. TCS requires a TaxonConcept to have exactly one `taxonName` and one `accordingTo` resource. TCS synonym relations connect TaxonConcept to TaxonName, while concept mappings compare two TaxonConcepts and use the six defined mapping relations.

Remaining review:
- ensure the internal concept's according-to resource resolves to one canonical resource;
- keep name-to-name nomenclatural relationships separate from concept-to-name synonym assertions and concept-to-concept mappings;
- review treatment, source, publication and resource identity with a qualified taxonomist/biodiversity-informatics specialist;
- do not infer global accepted status from one source.

### 7.2 Event, Survey, Occurrence and Observation

The Conceptual Model's latest indexed metadata reports 2026-10-13, while earlier direct retrieval showed 2026-05-26. Check the exact versioned content before making version-specific claims. It remains a high-level conceptual framework and does not prescribe a database schema.

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
| AUD-05 | Critical | Task 05D DR-02 and FLD-08 defects identified in the audit snapshot | Corrected on PR #11 branch; synchronize with latest PR #5 and independently re-review | Before Task 05D acceptance |
| AUD-06 | Major | Review pack contained an incorrect Darwin Core date amendment and stale Task 05C SHA | Corrected on PR #9 branch using live TDWG pages and current PR #5 blob; re-review before external review | Before external review |
| AUD-07 | Major | PR #8/#12 diverged and duplicate strategy docs exist | Compare complete file/commit history; one canonical document per subject | Before strategy consolidation |
| AUD-08 | Major | PR #11/#5 diverged | Synchronize and full-diff review; no blind merge | Before Task 05D merge |
| AUD-09 | Major | No PR reviews submitted | Recruit/record actual qualified reviewers; no self-approval claims | Before scientific approval |
| AUD-10 | Major | Automated Markdown/link validation was absent from main | Workflow and scanner added on PR #16; first run passed; relative-link findings are warn-only | Before governance PR merge |
| AUD-11 | Major | README structure and ADR list incomplete | Update after canonical docs and ADR-011 status decision | Before first public release |
| AUD-12 | Major | Two Indigenous stewardship document versions | Preserve unique content and choose one canonical revision | Before policy approval |
| AUD-13 | Major | 1,189-line NatureTech paper heading order/structure | Reorganize without altering evidence or claims; maintain research appendix | Before strategy approval |
| AUD-14 | Major | No code, tests, API contracts or implementation in main | Do not represent repository as production-ready; plan implementation only after gates | Product implementation stage |
| AUD-15 | Major | No releases/tags | Establish release/tag process after first reviewed milestone | First release |
| AUD-16 | Moderate | Branch register requires refresh as branch/PR topology changes | Refreshed on PR #15 branch to 19 branches and 13 open PRs; continue monthly | Monthly |
| AUD-17 | Moderate | README had duplicate H1 in main snapshot | Duplicate title removed on PR #16 branch; review/merge pending | Documentation release |
| AUD-18 | Moderate | Task 05D section 4 heading order was inconsistent | Reordered on PR #11 branch; verify all internal references | Before review |
| AUD-19 | Moderate | No automated stale-branch age/ownership report | Add monthly inventory checklist; no auto-delete | Monthly |

## 10. Remediation work completed on this audit branch

The following changes have been made on `docs/repository-audit-and-ai-operating-standard`:
- Added a permanent AI project operating prompt.
- Added this repository/Markdown audit report.
- Added a closing code fence to each of ADR-001 through ADR-010, without changing diagram or prose content; all ten files were re-fetched and verified to have balanced fence markers.
- Removed the duplicate H1 from README and updated its repository-tree example to match the files on this audit branch; added links to the permanent AI prompt and audit report.
- Added a least-privilege GitHub Actions workflow and Python checker for Markdown fence integrity and PR branch routing. The workflow has now completed successfully on PR #16; latest verified run ID 44684168599 (head dafd0629d5fc70b6e11816419edec85e7e4ac2c6) passed the Markdown integrity and branch-routing job. The workflow has not yet been merged into main.
- The changes have not been merged. They require review through the project's branch workflow.
- No existing branch was deleted, no existing PR was merged/closed/retargeted, and no branch-protection settings were changed.

## 11. Recommended implementation sequence

1. Review this audit and permanent AI prompt.
2. Review/adopt PR #15 branch lifecycle policy.
3. Review the successful branch-routing/Markdown workflow run and determine whether to adopt its check after representative PR tests.
4. Complete README navigation and canonical document index after architecture documents are settled.
5. Independently re-review PR #9 standards metadata and exact source revisions after the TDWG correction.
6. Synchronize PR #11 with the latest PR #5 head and re-review the corrected Task 05D wording and DR-02 total-participation caveat.
7. Resolve Event/Survey/Occurrence and Observation/Event design with specialist review.
8. Reconcile Task 05C competing document; preserve selected workflows/cardinality notes.
9. Resolve PR #8/#12 strategy overlap and choose canonical Indigenous stewardship document.
10. Review licensing, ADR-011 and organisational readiness with appropriate maintainers/professionals.
11. Complete scientific and rights test fixtures; only then assess Task 05E readiness.
12. Consolidate branches gradually to main/develop/staging; at formal project completion retire develop and staging so only main remains.

---

## 12. Research and authoritative references

Checked for this audit on 20 November 2026:

1. TDWG, Darwin Core List of Terms: latest indexed metadata reports version issued 2026-10-13, previous 2026-05-26; direct HTML retrieval returned 2026-05-26: https://dwc.tdwg.org/list/
2. TDWG, Darwin Core Conceptual Model: latest indexed metadata reports version issued 2026-10-13, previous 2026-05-26: https://dwc.tdwg.org/cm/
3. TDWG, Taxon Concept Standard Terms: https://tcs.tdwg.org/terms/
4. GBIF, Data Quality Recommendations: https://techdocs.gbif.org/en/data-publishing/data-quality-recommendations
5. PostgreSQL 18, Constraints: https://www.postgresql.org/docs/18/ddl-constraints.html
6. GitHub repository rulesets documentation: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets
7. GitHub branch protection documentation: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches

**Final audit judgement:** The repository has a credible documentation foundation, but it is not ready for implementation or external claims of scientific validation. The immediate priority is governance automation, source/version correctness, scientific-model resolution and preservation-first branch consolidation.


## 13. Standards-date correction after direct source re-verification (20 November 2026)

The first amendment made during this audit incorrectly stated that the current Darwin Core List of Terms and Conceptual Model were issued 2026-10-13. Directly opening the official TDWG pages shows that both were issued **2026-05-26**. The List page identifies **2025-07-10** as its previous version. The `occurrenceStatus` term itself was modified **2026-05-26**. The earlier correction was wrong; affected Task 05, Task 05B, Task 05D and PR #9 review documents have been corrected to reflect the source pages. Sources: https://dwc.tdwg.org/list/ and https://dwc.tdwg.org/cm/.


## 14. Subsequent standards-metadata re-verification — DR-09 remains open (20 November 2026)

Latest indexed metadata for both official TDWG pages reports Date version issued: 2026-10-13, with 2026-05-26 as the previous version. However, opening the live List page through the available page retrieval returned a header showing 2026-05-26 and previous version 2025-07-10. The core namespace term list at https://rs.tdwg.org/dwc/terms.htm also reports a 2026-05-26 snapshot. Search-indexed content for the 2026-10-13 List includes individual term records modified on that date, but this does not mean every term was modified then.

This is not enough to claim that the complete current versioned documents and every relevant term IRI have been verified. DR-09 remains open. Before closure, retrieve the exact versioned List, Conceptual Model, core-term and relevant term IRIs; compare their content and record each document-version date separately from term-level modification dates and namespace snapshots. Do not infer that every term changed on the document issue date. The prior Section 13 conclusion that both documents were definitively 2026-05-26 is superseded; the earlier 2026-10-13 amendment should not be labelled erroneous without resolving this retrieval conflict.

Current official page references: https://dwc.tdwg.org/list/ ; https://dwc.tdwg.org/cm/ ; https://rs.tdwg.org/dwc/terms.htm .


## 15. Subsequent repository state refresh (20 November 2026)

A further live GitHub API check after creation of PRs #17–#20 reports **23 branches**: exactly three designated long-lived branches (`main`, `develop`, `staging`) and 20 topic/workstream branches. There are **17 open PRs**: #1–#5, #8, #9, #11–#20. No PR was merged as part of this refresh. `main`, `develop` and `staging` remain identical at `f165ecb9b4d9de115c02327cf779982b7ef4bbd4`. All 20 topic branches compare ahead of `main` with zero commits behind; however, stacked PR comparisons still show divergence: PR #11 is 3 commits ahead/1 behind PR #5, and PR #12 is 4 ahead/3 behind PR #8. Preserve these dependencies and do not retarget or delete branches without a branch-by-branch review.

The active repository ruleset `Protect main branch` currently enforces only deletion prevention and non-fast-forward prevention. It does not require pull requests, approving reviews, conversation resolution or status checks. `develop` and `staging` have no active ruleset in the verified ruleset listing. The successful PR #16 workflow run validates the current script's Markdown fence and routing checks, but it does not provide merge protection because no required check is configured.

The default `main` tree remains documentation/governance-led: 18 root-tree entries and no TypeScript, JavaScript, Python, Dart or SQL application source files were found. The target application structure in PR #20 remains proposed, not implemented.


---

## 16. PR #16 governance and cross-document review — 21 November 2026

### 16.1 Review scope and repository snapshot

This follow-up review was performed against the live repository and the PR #16 review branch, not against the earlier 20 November snapshot.

- Repository: `Save-Tiger-First/botanica-indica`.
- Review branch: `docs/repository-audit-and-ai-operating-standard`.
- PR #16 head before this review record: `0a4162224ca7696a179e25054944f424b976fcfb`.
- Operating prompt: `docs/governance/AI-PROJECT-OPERATING-PROMPT.md`, proposed version 1.0, blob `ec100aec5abc09ec04ad9f4a084a0aa95a7c7558`.
- Branches: 23 (3 designated long-lived branches and 20 temporary/workstream branches).
- Open PRs: 20.
- PR #16: open, draft, base `develop`, head `docs/repository-audit-and-ai-operating-standard`; 68 commits, 21 changed files, 2,294 additions and 13 deletions at review time. GitHub reported it as mergeable, but it has no submitted reviews, no conversation comments and no inline review threads. Mergeability is not approval.
- PRs #1, #2 and #15 remain open and unmerged. Their original source branches remain present.
- No PR was merged or closed, no branch was deleted or created, and no ruleset or repository setting was changed during this review.

The current branch inventory remains a dated 20 November snapshot. Its count and open-PR count still match the live totals, but its branch heads and PR #16 commit history need a dated refresh before any branch-retirement action.

### 16.2 Accepted ADR preservation check

The ten accepted ADRs, ADR-001 through ADR-010, were compared between `main` and the PR #16 branch individually.

**Verified:** each file differs only by one inserted closing Markdown fence at the previously unclosed diagram. No prose, architecture decision, technology direction, scientific principle or status text was changed. This is an appropriate narrow correction and does not amend the accepted decisions.

ADR-001 continues to specify Dart/Flutter for mobile, TypeScript for suitable platform/API services, Python for AI/ML and scientific computing, PostgreSQL/PostGIS as the database direction, and Rust only where justified. ADR-011 correctly describes Dart/Flutter as subject to ADR-001. No mobile-framework conflict was found in the reviewed ADR-011 text.

### 16.3 Findings and required remediation

| ID | Severity | Finding | Required action |
|---|---|---|---|
| GOV-01 | Major | Branch-prefix lists disagree. The operating prompt lists feature, fix, docs, research, governance, test and release. The Branching and Release Governance policy and Python checker additionally permit proposal, strategy and review. Existing live branches use all three additional prefixes. | Align the operating prompt, branch policy and checker. Do not rename existing branches as part of this correction. |
| GOV-02 | Major | The routing checker rejects every direct-to-main PR except `staging` promotion or a documented `fix/*` emergency hotfix. Nine currently open PRs target `main`: #1–#5, #8, #9, #13 and #14. | Define a controlled legacy-PR migration/grandfathering plan before the workflow is promoted to `main` or made a required check. Do not silently retarget or close those PRs. |
| GOV-03 | Major | `CONTRIBUTING.md` section 20 says that contributing means the contributor agrees their contribution will be made available under applicable project licensing terms. The proposed Licensing and IP Policy says contributor terms are not yet approved and explicitly warns against treating the current wording as a complete contributor agreement. | Clarify the contribution wording and establish reviewed contributor terms before broad external solicitation. Do not infer a transfer of ownership or a blanket AI-training grant. |
| GOV-04 | Major | The companion `STF-ECOSYSTEM-BOUNDARIES.md` says the ecosystem must follow the “approved” STF Licensing and Intellectual Property Policy, while that policy's own status is Proposed and requires maintainer/legal review. | Change the companion wording to refer to the proposed policy until it is formally approved. Do not change the policy's status by editorial implication. |
| GOV-05 | Major | README omits ADR-011 from its ADR table and repository tree. It says licensing policy documentation will be available “when established”, although a proposed policy already exists on this branch. The companion architecture document metadata lists ADR-001 through ADR-010 but does not identify ADR-011 as its companion decision. | Update navigation and status language after the governance content is reconciled. Distinguish proposed documents on this branch from accepted material on `main`. |
| GOV-06 | Major | The Licensing and IP Policy has useful asset-by-asset controls but its official reference list does not yet include the current Indian privacy and biodiversity legal framework relevant to personal data, biological resources and associated knowledge. | Add a jurisdiction-aware legal triage and current official source register. Obtain qualified legal review; this desk review is not a legal opinion. |
| GOV-07 | Moderate | The policy's Data and Rights Registry is a good governance concept, but the proposed fields do not explicitly require a jurisdiction/legal-basis assessment or a biodiversity access-and-benefit-sharing (ABS) review outcome where relevant. | Add fields or linked assessments for jurisdiction, applicable legal instrument, ABS applicability/approval/benefit-sharing status, community authority/consent evidence where relevant, and legal review record. Do not assume every public botanical record triggers an ABS approval. |
| GOV-08 | Moderate | The workflow checks Markdown fence balance and branch routing, but it is not a full CommonMark/GFM validator, link checker, license scanner, security scan or test suite. Relative-link findings are warnings only. | Describe the check's limited scope accurately. Add separate validators only when their behavior and maintenance are justified and tested. |
| GOV-09 | Moderate | The workflow is not configured as a required status check. The active repository ruleset `Protect main branch` currently contains only deletion and non-fast-forward protections; it does not require PRs, approving reviews, conversation resolution or status checks. No active ruleset was returned for `develop` or `staging`. | Treat the workflow as informational until representative tests and a separate ruleset review are completed. Do not change repository protection without explicit approval. |
| GOV-10 | Minor | The successful current workflow run emitted a Node.js 20 deprecation warning because it uses `actions/checkout@v4` and `actions/setup-python@v5`, which were forced to Node.js 24 by the runner. | Upgrade to maintained Node.js 24-compatible action releases and pin actions to verified full commit SHAs before relying on the workflow for governance enforcement. |
| GOV-11 | Minor | ADR-011 lists only ADR-001, 002, 003, 004, 008, 009 and 010 as related decisions. ADR-005 through ADR-007 are also relevant to domain ownership, taxonomy, identification and evidence boundaries. | Confirm the intended relationship and include omitted ADRs where they materially inform the boundary decision. |

### 16.4 Workflow validation evidence

The current PR #16 head was associated with GitHub Actions run `44871101691` (workflow: Repository governance). Its job `136745610207` completed successfully on 21 November 2026.

The log confirms:
- 21 tracked Markdown files were checked.
- The Markdown fence and PR-routing checks passed for PR #16 from `docs/repository-audit-and-ai-operating-standard` to `develop`.
- The job used `actions/checkout@v4` and `actions/setup-python@v5`; the runner emitted a Node.js 20 deprecation warning and forced those actions to Node.js 24.

This is evidence that the current script passed on PR #16. It is not evidence that all current PR routes are compliant, that the workflow is a required status check, or that the repository has comprehensive Markdown, security or application test coverage.

The checker currently permits `proposal/`, `strategy/` and `review/` prefixes. The operating prompt's shorter list is inconsistent with that implementation. The checker also rejects direct-to-main PRs other than staging promotions or documented fix hotfixes. This will affect the nine existing direct-to-main PRs listed in GOV-02 if the workflow becomes active on `main` without a migration exception.

### 16.5 Indian legal and rights research — desk review only

The following official sources were checked on 21 November 2026. This section identifies governance implications, not legal conclusions about a particular dataset or proposed STF activity.

**Copyright and contributor ownership**

The Copyright Act, 1957 should be included in the policy's primary legal references. The Copyright Office's Chapter IV summary records section 17 (first ownership), section 18 (assignment) and section 19 (mode and particulars of assignment). In particular, an assignment must be in writing and identify the work and rights, duration and territorial extent. The actual statutory text and any applicable exceptions must be reviewed for each arrangement. The current policy's position that STF must not assume contributor ownership is appropriate.

Official reference: https://copyright.gov.in/Copyright_Act_1957/chapter_iv.html

**Digital personal data**

The Digital Personal Data Protection Act, 2023 and Digital Personal Data Protection Rules, 2025 must be added to the legal-source register and connected to a separate privacy/data-governance process. The Act's commencement notification is phased: certain provisions commenced on publication, specified provisions after one year, and the main provisions in sections 3–17 and other listed provisions after eighteen months from 13 November 2025. The Rules also have phased commencement; Rule 4 has a one-year commencement period and Rules 3, 5–16, 22 and 23 have an eighteen-month period from publication on 14 November 2025. Therefore, do not describe the entire substantive framework as already in force on this review date; maintain a dated implementation-readiness schedule and re-check the official notifications before launch or processing personal data at scale.

Official sources:
- Act, 2023: https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf
- Commencement notification, G.S.R. 843(E), 13 November 2025: https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf
- MeitY official DPDP Rules, 2025 listing and corrigendum: https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-protection-rules-2025-gDOxUjMtQWa

**Biological resources and associated knowledge**

The policy should include a biodiversity-law triage for activities involving access to biological resources or associated knowledge, research and commercial utilisation, transfers/exchanges and international collaboration. The official National Biodiversity Authority materials identify the Biological Diversity Act, 2002 as amended in 2023, the Biological Diversity Rules, 2024, the 2025 Amendment Rules and the Biological Diversity (Access to Biological Resources and Knowledge Associated thereto and Fair and Equitable Sharing of Benefits) Regulations, 2025. The NBA states that the 2024 Rules came into force on 21 December 2024 and the 2025 amendment rules on 1 November 2025.

This does **not** establish that merely reading or linking to every publicly accessible botanical database requires NBA approval. Applicability depends on the actual biological resource, associated knowledge, persons, purpose, activity, exemptions and current statutory/regulatory text. STF should obtain a qualified case-specific assessment before collecting biological material, accessing or using associated traditional/community knowledge, transferring biological resources/information internationally, or commercialising outputs that may fall within the regime.

Official sources:
- NBA, Acts/Rules: https://nbaindia.nic.in/acts-and-rules/rules
- NBA, Notifications and ABS Regulations: https://nbaindia.nic.in/public-information/notification-guidelines
- NBA, FAQs and implementation dates: https://nbaindia.nic.in/about-us/faqs

### 16.6 Technical reference verification

ADR-011's reference to OpenAPI Specification 3.2.1 is current and accurate as checked on 21 November 2026. The official OpenAPI Initiative specification identifies version 3.2.1 as issued on 10 September 2026. No correction is required for that reference.

Official source: https://spec.openapis.org/oas/v3.2.1.html

### 16.7 Overall PR #16 review judgement

**Recommendation: retain PR #16 as Draft / Under Review; do not mark it ready or merge it yet.**

The audit branch has valuable and verified work: the accepted ADR fence repairs are narrow, the operating prompt captures the project-owner's branch and quality constraints, the governance workflow has least-privilege read-only permissions, and the three governance source histories have been preserved through ancestry-preserving commits.

However, PR #16 is not yet review-ready because its own governance materials are not fully consistent, the contributor wording is ambiguous against the licensing policy, the branch-routing checker needs a legacy migration strategy, and the legal source register needs Indian privacy and biodiversity coverage. It also has no independent PR review. The workflow passing and GitHub reporting the PR as mergeable do not resolve these issues.

Recommended order:
1. Align the operating prompt, branch policy and checker prefix lists.
2. Define the transition treatment for existing direct-to-main PRs before routing enforcement reaches `main`.
3. Correct the proposed/approved licensing-policy wording and clarify contributor terms with qualified counsel.
4. Update README and companion-document navigation/status references.
5. Add current Indian legal references and a legal/ABS triage to the licensing and rights-governance materials.
6. Upgrade and SHA-pin the GitHub Actions dependencies; test routing behavior against representative current PRs.
7. Obtain independent maintainer review, and legal review for the rights policy, before changing PR #16 from draft.

### 16.8 Non-actions and approval boundaries

- No accepted ADR was changed.
- No policy or ADR was marked Accepted.
- No contributor agreement, DCO or CLA was selected.
- No legal opinion, compliance certification, biodiversity approval or privacy compliance conclusion was issued.
- No PR was marked ready, merged, closed or retargeted.
- No branch was created or deleted.
- No ruleset, branch protection, repository permission or default branch was changed.
- `CONTRIBUTING.md`, `README.md`, the licensing policy, ADR-011 and the companion architecture document were inspected but not edited as part of this review record.



---

## 18. PR #16 governance remediation — implementation record, 21 November 2026

### 18.1 Repository and branch context

- Repository: `Save-Tiger-First/botanica-indica`.
- Work branch: `docs/repository-audit-and-ai-operating-standard`.
- Base PR: #16, still open and draft, base `develop`.
- Operating prompt used: `docs/governance/AI-PROJECT-OPERATING-PROMPT.md`, v1.0 proposed; original reviewed blob `ec100aec5abc09ec04ad9f4a084a0aa95a7c7558`.
- No branch was created, renamed or deleted. No PR was merged, closed or retargeted. No ruleset, permission, default branch or repository setting was changed.

### 18.2 Changes implemented on the existing PR #16 branch

| File | Change |
|---|---|
| `docs/governance/AI-PROJECT-OPERATING-PROMPT.md` | Aligned the permitted prefix list with existing `proposal/`, `strategy/` and `review/` workstreams; the no-new-branches directive remains unchanged. |
| `docs/governance/BRANCHING-AND-RELEASE-GOVERNANCE.md` | Added a nine-PR exact legacy direct-to-main routing compatibility section. This is not merge permission. |
| `scripts/check_repository_governance.py` | Added exact PR-number/head allowlisting for PRs #1–#5, #8, #9, #13 and #14; requires PR number; rejects new direct-to-main task PRs; recognizes all existing workstream prefixes. |
| `.github/workflows/repository-governance.yml` | Pins `actions/checkout` v7.0.1 to commit `3d3c42e5aac5ba805825da76410c181273ba90b1` and `actions/setup-python` v7.1.0 to `6d4fd22b20465ccc0f7354476588e8df7c9ca0e0`, both verified against their GitHub tag refs. |
| `CONTRIBUTING.md` | Replaced ambiguous contribution licensing wording. States no DCO, CLA or complete contributor agreement has yet been adopted and that this guide is not an assignment or blanket grant. |
| `README.md` | Updated licensing-policy status, ADR-011 navigation and governance-document links. |
| `docs/governance/LICENSING-AND-IP-POLICY.md` | Added India-specific copyright, DPDP and biodiversity/ABS triage; expanded the Data and Rights Registry with jurisdiction, legal applicability, authority, ABS, community consent and legal-review fields; refined copyright section 19 and exemption wording. |
| `docs/adr/ADR-011-stf-ecosystem-boundaries.md` | Added ADR-005, ADR-006 and ADR-007 to related-decision metadata. ADR-011 remains Proposed. |
| `docs/architecture/STF-ECOSYSTEM-BOUNDARIES.md` | Corrected wording that had described the proposed licensing policy as already approved. |
| `tests/test_repository_governance.py` | Added regression tests for all allowed prefixes, exact grandfathered PR/head pairs, new direct-to-main rejection, staging promotion, hotfix rule and long-lived branch restrictions. |

### 18.3 CI validation

GitHub Actions run **44875418039** was triggered by PR #16 at commit `ac8c897d46092abcc039e4e39723afdecd2bdcd4` and completed successfully on 21 November 2026.

The job `Markdown integrity and branch routing` completed with conclusion `success`. The following steps passed:
- Checkout
- Python setup
- Governance routing regression tests
- Markdown integrity and PR routing checks

This verifies the workflow and test suite at the run's head commit. The subsequent copyright wording refinement in the licensing policy is documentation-only and occurred after that run; a new workflow run should verify the latest final head before PR #16 is considered review-ready.

The workflow is still **not a required status check**. No ruleset change was made. Its Markdown validation remains a limited fence/relative-link check, not a complete CommonMark/GFM validator, license scanner, security scan or application test suite.

### 18.4 Legal-source verification and qualifications

On 21 November 2026, direct official-source retrieval confirmed:

- G.S.R. 843(E), 13 November 2025, sets phased commencement for the DPDP Act. Section 6(9) and section 27(1)(d) commence one year after publication; provisions listed in clause (c), including sections 3–5, 7–17 and other specified sections, commence eighteen months after publication. Official Gazette PDF: https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf
- G.S.R. 846(E), 13 November 2025, sets phased commencement for the DPDP Rules. Rules 1, 2 and 17–21 commenced on publication; Rule 4 after one year; Rules 3, 5–16, 22 and 23 after eighteen months. Official Gazette PDF: https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf
- The Copyright Office's Chapter IV text confirms first ownership (section 17), assignment (section 18) and the written form and particulars of assignment (section 19), including consideration and default rules. Official source: https://copyright.gov.in/Copyright_Act_1957/chapter_iv.html
- NBA official search-indexed materials list the Biological Diversity Rules 2024 and Amendment Rules 2025, the 2025 ABS Regulations, and current FAQ information on exemptions and authority roles. Sources: https://nbaindia.nic.in/index.php/acts-and-rules/rules ; https://www.nbaindia.nic.in/public-information/notification-guidelines ; https://www.nbaindia.nic.in/about-us/faqs

The MeitY Gazette PDFs and Copyright Office Chapter IV page were directly opened. NBA pages were surfaced by official-domain search results; direct page retrieval returned cache-miss errors in this session. Their links are retained as official starting points, but the exact consolidated legal text and case-specific applicability must be verified with qualified counsel before action.

The biodiversity triage intentionally avoids a blanket claim that all public botanical information requires NBA approval. The amended law and current NBA guidance describe exemptions with eligibility conditions; the actual resource, actor, activity, purpose and applicable exemption must be assessed. No legal opinion, DPDP compliance certification, NBA approval, ABS determination or community consent is claimed.

### 18.5 Current repository lifecycle state at review

At the latest API check before this record:
- 23 branches remained.
- 20 PRs remained open.
- PR #16 remained open, draft, targeting `develop`.
- No branch was created, renamed or deleted.
- No PR was merged, closed or retargeted.
- The immediate seven-branch ceiling remains unmet.

### 18.6 Outstanding review gates

1. Re-run and verify the governance workflow on the final PR #16 head after the latest documentation-only changes.
2. Review the grandfathered legacy PR allowlist whenever one of those PRs is retargeted or closed; remove its exact entry at that point.
3. Decide and document a separate owner-approved retargeting plan for the nine legacy direct-to-main PRs. No retargeting has been done.
4. Obtain qualified Indian legal review of contributor terms, copyright, DPDP and biodiversity/ABS applicability before external contribution solicitation or regulated activity.
5. Review the proposed policies and ADR-011 independently. CI success and GitHub mergeability are not approval.
6. Update the branch inventory again before any retirement wave; preserve all source histories and dependencies.
