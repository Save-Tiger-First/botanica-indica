# Task 05C / Task 05D — Source-by-Source Scientific Model Reconciliation

**Document ID:** STF-BI-REV-SM-003  
**Version:** 0.1  
**Review date:** 26 November 2026  
**Status:** Proposed adviser synthesis for owner and qualified specialist review — NOT an approved scientific model  
**Review branch:** review/scientific-data-model-review-pack (PR #9)  
**Repository:** Save-Tiger-First/botanica-indica  
**Governing standard:** STF-AI-OPS-001 v1.0, blob 53add3894d0502827e584614c70ad09cadaa637d, branch docs/repository-audit-and-ai-operating-standard

> **Decision boundary:** This document reconciles the currently available source documents and recommends a coherent review direction. It does not approve Candidate A or B, amend an accepted ADR, close EVT decisions, pass Task 05D, authorize Task 05E, freeze an API contract, or authorize physical database design. No source model or requirement is changed by this report.

---

## 1. Executive conclusion

**Recommendation: retain Candidate A (PR #5) as the canonical review starting document, selectively preserve Candidate B (PR #21) material, and reconcile the Event/Survey/Occurrence and target-assessment semantics before any model approval.**

Candidate A is stronger in taxonomy semantics, typed subject references, relational integrity, rights, provenance, geography and explicit validation scenarios. It is not internally coherent yet: its original ERD/cardinality table still models Event-to-Occurrence as a one-to-many contextual relation, while later sections propose Occurrence as a specialization sharing Event identity.

Candidate B is a useful alternative source for workflow descriptions, Observation-to-Event grouping, material derivation and operational cardinality examples. It should not be merged wholesale. Its Event-to-Occurrence one-to-many model conflicts with the preferred Event-specialization hypothesis; its Identification description does not define Candidate A's typed, real-FK subject pattern; and its TCS mapping examples need stricter separation between TCS relations and local workflow states.

The existing Task 05B dictionary and Task 05D v3 do not yet consistently apply the later Event and target-outcome recommendations. In particular, Task 05B §16 and Candidate A §18 still describe SurveyTargetResult as an outcome-bearing record, while later review sections recommend SurveyTargetAssessment for assessment lifecycle and Occurrence for the taxon/organism-level detection outcome. Task 05D EVT-36/EVT-37 still use SurveyTargetResult in their expected results.

**My preferred review hypothesis is:**
1. Event is the shared identity and semantic supertype.
2. Survey and Occurrence are distinct, mutually exclusive typed specializations of an Event identity; a generic/context Event may also exist.
3. Observation remains a separate contributor-submission/workflow record.
4. Event parent-child hierarchy, Survey-to-reported-Occurrence, context association and Observation evidence links are separate relationships.
5. SurveyTarget declares what was sought or later analysed.
6. SurveyTargetAssessment records whether and how a target was assessed, including protocol, effort, scope, completeness, limitations and provenance — not a second independently mutable detection outcome.
7. For taxonomic/organismal targets, the canonical detected or explicit non-detected result is represented by the relevant Occurrence, linked to the Survey through SurveyOccurrenceReport.
8. Non-taxonomic targets require a typed ScientificAssertion / MeasurementOrFact result path, or a separately reviewed typed outcome construct. They must not be forced into an organism Occurrence.
9. An empty Occurrence set with no explicit assessment remains unknown/not assessed.
10. ODR-01 remains an owner-authorized, controlled external-export interpretation only; it does not authorize internal absence inference.

This is a recommended model direction, not a decision. EVT-D01–D10, B01/B02/B16, DR-07/DR-09 and the relevant LDM/FLD cases remain open.

## 2. Live repository and review state

Verified on 26 November 2026:

| Item | Current state |
|---|---|
| Repository | Save-Tiger-First/botanica-indica |
| Total branches | 23 |
| Open pull requests | 19; all 19 are draft |
| Long-lived branches | main, develop, staging |
| PR #9 | Open / draft; base main |
| PR #9 head before this report | 08987d8a01b411cb167c16ae0edbf0d914036d06 |
| PR #5 | Open / draft; Candidate A |
| PR #11 | Open / draft; Task 05D v3, stacked on Candidate A |
| PR #21 | Open / draft; Candidate B |
| PR #22 | Open / draft; earlier Task 05D revision |
| PR #23 | Open / draft; Task 05D v2 revision |

No submitted reviews were found on PRs #5, #9, #11, #21, #22 or #23 in the current review check. This is not independent specialist sign-off. No branch was created or deleted for this review.

### 2.1 Exact current source inventory

File blob SHAs below were fetched from the named refs for this reconciliation. Commit SHAs are branch heads, not file blob SHAs.

| Source | PR / branch | Branch head SHA | File blob SHA |
|---|---|---|---|
| Task 05 conceptual architecture | PR #3 / docs/task-05-data-architecture | 2b02ab3cd115691841889ed77d453b31ab0bed16 | a3255dcf2d1bd4dfa982b381b061051b6c2c8b0b |
| Task 05B scientific data dictionary | PR #4 / docs/task-05-data-dictionary | e11fd943e59c81ea8b464ef6a84ac4bcdbcccfd4 | ddaa379d993fdf1f45684962930d16f06830ae43 |
| Task 05C Candidate A | PR #5 / docs/task-05c-logical-data-model | d443420d6b77815cb155f457ea262e621aabf7cb | b447796e7da0d08d96400812667a8e67e0696144 |
| Task 05C Candidate B | PR #21 / docs/task-05c-logical-database-model | 8d4fef2d726aac79dd684856d924b171e44d0b93 | 239d7e9974bcb81b1154b54845a7b2d69c3775d6 |
| Task 05D v3 | PR #11 / docs/task-05d-logical-model-validation-v3 | 0577250c9e7cffcb3605acc782f403b7d1b422e0 | 0b9a009b1c543b2450758f659c97cae3802a2f94 |
| Competing-model reconciliation | PR #9 / review/scientific-data-model-review-pack | 08987d8a01b411cb167c16ae0edbf0d914036d06 | e34eadf0257f38d81b4809e2477784045f460746 |
| Event–Survey–target outcome recommendation | PR #9 / review/scientific-data-model-review-pack | 08987d8a01b411cb167c16ae0edbf0d914036d06 | 29e72d4d4e0b25d52ca61bb1ba2a9e5a6ee0dd37 |
| Task 05D independent desk review | PR #9 / review/scientific-data-model-review-pack | 08987d8a01b411cb167c16ae0edbf0d914036d06 | a9e2c50c30eb4da1993a7522797c59b1fd799654 |
| EVT decision and validation pack | PR #9 / review/scientific-data-model-review-pack | 08987d8a01b411cb167c16ae0edbf0d914036d06 | 4a317c4c83317e10663ba374e9e6be3100a53431 |
| Scientific validation matrix / decision register | PR #9 / review/scientific-data-model-review-pack | 08987d8a01b411cb167c16ae0edbf0d914036d06 | 3a33dfe47657a96456f56f2c12a0b7d355b6c6a5 |

The earlier Task 05D v1 and v2 documents remain historical alternatives. The active validation review baseline is Task 05D v3 on PR #11. A historical v2 disposition must not supersede the current v3 and PR #9 decision register.

### 2.2 Branch divergence and preservation

Live comparisons:

| Comparison | Result | Interpretation |
|---|---|---|
| Candidate A vs Candidate B | Diverged; Candidate B is 1 commit ahead and 10 behind Candidate A | Candidate B has a unique 647-line document; Candidate A has later independent history |
| Candidate A vs Task 05D v3 | Diverged; Task 05D v3 is 7 commits ahead and 4 behind Candidate A | PR #11 is not synchronized to the current Candidate A head |
| PR #9 review branch vs Candidate B | Diverged; Candidate B is 1 ahead and 88 behind PR #9 | Candidate B's unique material is preserved on its own branch |
| PR #9 review branch vs Task 05D v1/v2 | Diverged; each is 7 ahead and 88 behind PR #9 | Preserve the historical validation revisions until their unique content is dispositioned |

These are source-history comparisons, not proof of content conflict or mergeability. Do not merge, rebase, retarget, force-update or delete any of these branches as part of this review.

## 3. Source-by-source findings

### 3.1 Task 05 — conceptual architecture

**Source-derived position:** Task 05 now explicitly describes Occurrence as a specialized Event and Survey as a specialized Event. It also keeps a generic/context Event capable of providing shared spatial-temporal context to multiple activities. It distinguishes Observation, Occurrence, Event and MaterialEntity and treats the Darwin Core Conceptual Model as semantic guidance rather than a prescribed database implementation.

**Assessment:** This is the strongest high-level conceptual direction among the source documents. It is consistent with the current Darwin Core Event and Occurrence class definitions retrieved for this review.

**Required follow-through:** Task 05C must implement the distinction coherently in its logical ERD, keys, cardinalities and relationships. A statement in Task 05 does not resolve the contradictions still present in Candidate A and B.

### 3.2 Task 05B — Scientific Data Dictionary

**Source-derived strengths:**
- TaxonName, TaxonConcept, TaxonomicTreatment and TaxonNameUsage are separate.
- TCS according-to resource and name semantics are addressed.
- IdentificationSubject is described as one row per Identification with three real target foreign keys and a row-local exactly-one check.
- The dictionary distinguishes contributor Observation, Event, Occurrence, Organism and MaterialEntity.
- Section 16 introduces SurveyTarget and SurveyTargetResult, and distinguishes Event hierarchy from Survey reporting.

**Blocking inconsistency:** §16 defines SurveyTargetResult as an outcome-bearing assessment, including DETECTED and NOT_DETECTED_EXPLICIT states. §17.2 later recommends SurveyTargetAssessment for the assessment lifecycle and Occurrence for the taxon/organism-level outcome. Both representations remain in the same file.

**Recommendation:** retain SurveyTarget as the versioned target declaration; use SurveyTargetAssessment as the working name for the assessment lifecycle; remove detection/non-detection as a second independently mutable outcome in that assessment record. For organismal/taxonomic targets, use the authoritative Occurrence result and a SurveyOccurrenceReport link. For environmental or trait targets, use a typed assertion/measurement result path. This is not yet an approved entity design.

### 3.3 Task 05C Candidate A — PR #5

**Strengths:**
- More explicit TCS treatment: concept-to-name synonym, name-to-name nomenclatural relations, concept-to-concept mapping and nomenclatural types are separate.
- One canonical according-to resource is specified for a TaxonConcept.
- IdentificationSubject uses a single typed association with real foreign keys rather than an unconstrained subject_type/subject_id pointer.
- ScientificAssertion uses typed subject links.
- Rights, provenance, location generalization, temporal history and source-record lineage are more thoroughly developed.
- Sixteen LDM scenarios and separate security/data-quality tests are provided.

**Blocker A-01 — Candidate A contradicts itself on Event/Occurrence.**

- The original field-record ERD in §4.2 still expresses Event as contextualizing one or more Occurrences.
- The original relationship table in §7 still says Event → Occurrence is one-to-many.
- §18.3–§18.4 later proposes a shared Event identity and Occurrence specialization, with at most one Occurrence specialization per Event identity.
- §18 expressly says it does not supersede the earlier Candidate A content.
- §19–§20 continue to discuss the reconciliation rather than providing one clean, consolidated ERD and cardinality set.

**Required correction:** a future canonical Candidate A revision must replace the earlier contradictory ERD/cardinality wording, not merely append another clarification. It must state exactly how Event identity, Survey subtype, Occurrence subtype, generic/context Event, context association, parent-child hierarchy and SurveyOccurrenceReport differ.

**Blocker A-02 — Candidate A still uses SurveyTargetResult as an outcome-bearing record in §18.**

This conflicts with the later assessment/outcome separation proposal and Task 05B §17.2. The working direction should be SurveyTargetAssessment for assessment lifecycle and Occurrence for organismal/taxonomic outcome. Non-taxonomic targets remain a separate typed-result design question.

**Major A-03 — LDM-16 vocabulary needs precision.**

LDM-16 refers to an “explicit absent/non-detected Occurrence state”. Use the internal governed state name only after the vocabulary is decided, and map it explicitly to the selected export term/profile. The current Darwin Core occurrenceStatus term version retrieved for this review recommends detected and notDetected; GBIF guide examples use present and absent. Do not use “absent” as a universal internal scientific assertion or silently equate these literals.

**Major A-04 — IdentificationSubject total participation remains unproven.**

The row-local check can require exactly one target FK within an IdentificationSubject row. It does not guarantee that every Identification has a corresponding subject row. A unique Identification FK and a transaction-safe strategy for mandatory subject-row creation are still required. PostgreSQL CHECK constraints cannot enforce arbitrary cross-table conditions.

### 3.4 Task 05C Candidate B — PR #21

**Useful content to preserve selectively:**
- Clearer workflow description of contributor Observation records and their possible links to multiple Events.
- Explicit cardinality discussion for Observation, Event, Occurrence and MaterialEntity.
- MaterialEntity derivation and collection context.
- Additional practical domain examples and end-to-end workflows.
- Helpful separation of Observation from formal taxon determination.

**Major B-01 — Event and Occurrence remain separate linked entities.**

Candidate B's ERD and §7.6 use Event → Occurrence as one-to-many, and its Event description says an Event may have one or more Occurrences. This is not the preferred shared Event identity / Occurrence-specialization hypothesis. It must not be copied into Candidate A without reconciling the semantics.

**Major B-02 — Identification subject integrity is underspecified.**

Candidate B describes Identification as having a subject and subject type but does not provide Candidate A's explicit one-row, real-FK, exactly-one target pattern. A generic subject type plus identifier is not an adequate substitute unless a formally enforceable supertype/registry is specified and validated.

**Major B-03 — TCS mapping vocabulary needs normalization.**

Candidate B gives examples such as congruent, included-in, includes, overlaps, excludes and unresolved. The TCS mapping vocabulary is specifically isCongruentWith, includes, isIncludedIn, partiallyOverlaps, isDisjointFrom and intersects. “Unresolved” is a mapping/review status, not one of the six TCS mapping relations. “Excludes” is not a direct TCS relation label and must not be exported as if it were. Retain local workflow states separately and map only where semantics justify it.

**Major B-04 — Survey target/assessment lifecycle is not sufficiently developed.**

Candidate B does not provide the current SurveyTarget, assessment completeness, explicit non-detection and ODR-01 controls at the level now required by the EVT decision pack.

**Disposition:** Candidate B is a preserved reference source. Do not merge it wholesale. Reuse only content that is semantically compatible and carries clear provenance to its source.

### 3.5 Task 05D v3 — PR #11

**Strengths:** Task 05D v3 distinguishes structural validity, scientific completeness/evidence quality, rights/privacy/governance eligibility and external publishing readiness. It records the total-participation caveat for IdentificationSubject, keeps DR-09 open, and provides Event/Survey/Occurrence and synthetic fixture material.

**Blocker D-01 — validation expectations are not aligned with the recommended target/outcome separation.**

- EVT-36 currently expects SurveyTargetResult to record explicit NOT_DETECTED.
- EVT-37 still describes the empty state in terms of no SurveyTargetResult.
- The focused 26 November recommendation instead assigns the taxonomic/organismal outcome to Occurrence and uses SurveyTargetAssessment for the assessment process.

**Required correction after owner/specialist disposition:** rewrite the EVT-36/EVT-37 expected results to test Occurrence as the authoritative organismal/taxonomic outcome, assessment lifecycle separately, and empty Occurrence plus no assessment as unknown/not assessed. Do not change Task 05D merely to match this report before the conceptual decision is accepted.

**Major D-02 — Task 05D v3's source inventory is stale.**

Its current source inventory must be refreshed to the exact current Candidate A and Task 05B file blobs before it can be used as an acceptance record. The live PR #11 branch is also diverged from Candidate A. A source inventory copied from an earlier review date is not a current validation baseline.

**Major D-03 — tests are proposed, not executed.**

EVT-34–EVT-44 and LDM/FLD cases remain proposed specifications. No executable fixture outputs or test run evidence were found in the reviewed documents. Do not mark them pass.

### 3.6 Existing PR #9 review documents

The existing Task 05C competing-model assessment already recommends Candidate A as the review starting document, not an approved model. The 26 November Event–Survey–target outcome recommendation already proposes Event identity/specializations and SurveyTargetAssessment. The EVT pack and validation register retain open decisions and unexecuted tests.

This report therefore acts as a source-by-source reconciliation update, not a replacement for those documents. It clarifies the specific unresolved source contradictions and provides a consolidated review hypothesis.

## 4. Recommended logical responsibilities

The following is the recommended conceptual responsibility split for review. It is not a physical schema.

| Concept | Recommended responsibility | Must not become |
|---|---|---|
| Event | Stable identity for an action/process/circumstance at place and time; shared event-level context | A generic parent row that every Observation must create |
| Survey | A typed Event specialization with survey purpose, protocol, effort, scope and reporting context | A synonym for Event hierarchy or a result table |
| Occurrence | A typed Event specialization representing the state of an Organism at a place/time, including a supported detection or explicit non-detection | A row inferred from missing data or a duplicate SurveyTargetResult |
| Observation | Contributor-submitted workflow/evidence record | An automatic Event, Survey or Occurrence |
| Organism | Individual or defined taxonomically homogeneous group where identity is meaningful and supported | A mandatory identity for every plant photograph |
| MaterialEntity | Physical material, specimen, sample or plant part | A photograph or digital MediaAsset |
| SurveyTarget | Versioned a priori target declaration or post-facto analytical filter | A retrospective rewrite of original survey intent |
| SurveyTargetAssessment | Attributable assessment lifecycle: whether/how target was assessed, method, effort, scope, completeness, limitations, time/place and provenance | A second independently mutable detection/non-detection outcome |
| SurveyOccurrenceReport | Typed Survey-to-Occurrence reporting relation with target-match/bycatch/other role | Event parent-child containment |
| ScientificAssertion / MeasurementOrFact | Typed, attributable outcome path for environmental/trait/non-organismal targets where justified | An unconstrained polymorphic target pointer |

### 4.1 Relationship distinctions

Keep these relationships separate and independently testable:

1. Event parent-child hierarchy: genuine nested programme/site/plot/visit/collection containment. Parent and child time/spatial extents must be semantically compatible.
2. SurveyOccurrenceReport: a Survey reports an Occurrence, with explicit target-match/bycatch role.
3. Generic context Event association: shared site/time context where documented, not automatically parent-child.
4. ObservationEventLink: a contributor Observation documents or supports an Event.
5. ObservationOccurrenceLink: a contributor Observation provides evidence for an Occurrence.
6. OccurrenceMaterialEntity evidence link: physical material supports or evidences an Occurrence; it does not replace it.

### 4.2 Proposed conceptual sketch

Event identity
- Generic/context Event
- Survey specialization
  - SurveyTarget (versioned; a priori or post-facto)
  - SurveyTargetAssessment (assessment lifecycle/completeness)
  - SurveyOccurrenceReport → Occurrence specialization
- Occurrence specialization
  - organism/taxon state and explicit occurrenceStatus
  - evidence and provenance
- Event parent-child hierarchy is separate.
- Observation links to Event and/or Occurrence through typed, role-bearing associations.
- Non-taxonomic SurveyTarget outcomes use typed ScientificAssertion/MeasurementOrFact or a separately reviewed typed outcome construct.

A single Event identity must not simultaneously be both a Survey and an Occurrence specialization. The final model must also state how a generic/context Event relates to the Survey and Occurrence Events it contextualizes.

## 5. Standards findings and implications

### 5.1 Taxon Concept Standard

The official TCS List of Terms inspected for this review is version 2025-12-11. It requires a TaxonConcept to have exactly one taxonName and exactly one accordingTo resource. TCS synonymy links a TaxonConcept to a TaxonName; it is not a generic concept-to-concept synonym edge. TCS concept mapping uses six defined relations: isCongruentWith, includes, isIncludedIn, partiallyOverlaps, isDisjointFrom and intersects.

Candidate A aligns more closely with these distinctions. Candidate B's loose mapping examples need a controlled, loss-aware mapping before reuse.

Official source: https://tcs.tdwg.org/terms/

### 5.2 Darwin Core

The official Darwin Core List of Terms retrieved for this review identifies the Event and Occurrence classes and the occurrenceStatus term. The retrieved Occurrence definition describes it as an Event establishing the state of an Organism at a particular place and time. The retrieved occurrenceStatus term version is 2026-05-26 and recommends detected and notDetected.

This supports the Event/Occurrence semantic distinction. It does not prescribe a SQL inheritance pattern. The project must not infer that the DwC-A file layout is the internal relational schema.

Official sources:
- https://dwc.tdwg.org/list/
- https://dwc.tdwg.org/terms/

### 5.3 GBIF survey publishing guide

GBIF's Guide for publishing biological survey and monitoring data, v1.0.2 (2025-09-24), describes survey context through a Darwin Core Event core and related Occurrence records. It also describes each Occurrence record as mapped to a single survey Event in that publishing structure.

**Important implication:** if Botanica Indica internally permits one occurrence interpretation to be reported by multiple Surveys through SurveyOccurrenceReport, the GBIF export mapping must explicitly decide how to represent that. Do not assume that a many-to-many internal relationship maps directly to one GBIF occurrence row. A profile-specific duplication/identifier strategy or a restriction may be required; evaluate and test it before export design.

The guide's example literals present/absent must not silently replace the Darwin Core occurrenceStatus recommended values detected/notDetected. Treat the mapping as profile-specific and test it.

Official source: https://docs.gbif.org/guide-publishing-survey-data/en/

### 5.4 PostgreSQL integrity

PostgreSQL documentation states that CHECK constraints cannot safely reference data in other rows or tables. Candidate A's row-local exactly-one target check is useful for a populated IdentificationSubject row, but it cannot alone guarantee that every Identification has a subject row.

The eventual logical/physical design must prove:
- exactly one IdentificationSubject per Identification;
- exactly one valid target FK within each subject row;
- no orphan or invalid target;
- safe creation/update/deletion behavior;
- a restore-safe and concurrency-safe enforcement strategy.

Do not choose a trigger or application transaction design in this review; compare and test enforcement options during the physical-design gate.

Official source: https://www.postgresql.org/docs/current/ddl-constraints.html

### 5.5 DR-09 status

DR-09 remains OPEN. The TCS term resource and current Darwin Core term page were retrieved, but the exact versioned Darwin Core Conceptual Model / Humboldt term resources and the selected GBIF export profile still require a reproducible pinned evidence bundle. Do not close DR-09 on a version date alone.

## 6. Required validation corrections

All cases below are proposed synthetic tests, not executed tests.

| Test ID | Synthetic scenario | Required expected result |
|---|---|---|
| RSM-01 | Generic context Event shared by a Survey Event and multiple Occurrence Events | Shared context is explicit; each activity has its own Event identity and subtype |
| RSM-02 | One Event identity attempts to be both Survey and Occurrence | Rejected by the logical invariant |
| RSM-03 | Survey reports a target-matching detected Occurrence | Occurrence carries the organismal/taxonomic result; SurveyOccurrenceReport records target-match |
| RSM-04 | Survey reports incidental/bycatch Occurrence | Report role is bycatch; it does not satisfy target completeness or imply target detection |
| RSM-05 | Survey explicitly assesses a target and does not detect it | Explicit non-detection Occurrence is attributable and bounded; assessment records method/effort/completeness/limitations; SurveyOccurrenceReport connects it to the Survey |
| RSM-06 | No Occurrence and no assessment exists | State remains unknown/not assessed; no negative assertion or implicit ODR-01 export |
| RSM-07 | Assessment is incomplete, indeterminate or not assessed | No explicit non-detection is manufactured; implicit export fails closed |
| RSM-08 | Target is an environmental condition or trait, not an organism/taxon | Typed assertion/measurement result; no fabricated organism Occurrence |
| RSM-09 | A priori target versus post-facto analytical filter | Origin, author, method, time and target version retained; original survey scope unchanged |
| RSM-10 | SurveyOccurrenceReport exists but parent-child Event containment does not | Reporting relation remains valid; no hierarchy is inferred |
| RSM-11 | One Occurrence is reported by multiple Surveys | Internal links remain separately attributable; selected GBIF profile mapping is explicitly tested for single-Event export semantics |
| RSM-12 | Observation exists without Event, Occurrence or identification | Valid contributor workflow record; no automatic scientific assertion |
| RSM-13 | One Identification has no IdentificationSubject row | Rejected by total-participation invariant |
| RSM-14 | One IdentificationSubject row has zero or multiple target FKs | Rejected by exactly-one target invariant |
| RSM-15 | TaxonConcept lacks one TCS taxonName or accordingTo | Invalid TCS-aligned concept |
| RSM-16 | TCS mapping relation is “unresolved” or “excludes” | Not exported as a TCS mapping relation without a justified explicit mapping; unresolved remains workflow status |
| RSM-17 | One source term/version changes | Exact version and mapping provenance retained; prior mapping remains reproducible |
| RSM-18 | Rights or sensitive-location controls differ across internal and exported views | Restricted data do not leak through API, export, search, cache, logs, media metadata or backups |

### 6.1 Required changes to existing EVT fixtures after decision

- EVT-34: target detection — Occurrence is the canonical result; SurveyOccurrenceReport records target-match; assessment records assessment/completeness.
- EVT-35: bycatch — Occurrence is reported as bycatch; it does not satisfy target completeness.
- EVT-36: explicit non-detection — Occurrence carries the explicit not-detected result; SurveyTargetAssessment records how the target was assessed. Do not make SurveyTargetAssessment a duplicate outcome record.
- EVT-37: empty Occurrence set and no assessment — unknown/not assessed.
- EVT-38: missing/incomplete/ambiguous scope or completeness — ODR-01 implicit export suppressed.
- EVT-39: parent/child Event containment — no automatic scope/completeness inheritance.
- EVT-40: post-facto target — preserve analytical origin and do not rewrite a priori scope.
- EVT-41: material collection — MaterialEntity and MediaAsset remain distinct.
- EVT-42: multiple plants in one image — create distinct Occurrences/Organisms only where evidence supports them.
- EVT-43: generic context Event — context association and Event subtype identity remain distinct.
- EVT-44: Survey reporting versus Event hierarchy — test both relations independently.

Do not modify Task 05D's test specifications until the owner/specialist disposition is recorded. The table above is the proposed correction target.

## 7. Decision register and current disposition

| ID | Topic | Recommended disposition | Status |
|---|---|---|---|
| EVT-D01 | Event identity and Survey/Occurrence specialization | Shared Event identity with mutually exclusive typed specializations as preferred hypothesis | Open |
| EVT-D02 | Event hierarchy vs contextual association | Separate, typed relationships; enforce containment only where justified | Open |
| EVT-D03 | SurveyTarget identity/scope | Versioned target; preserve a priori/post-facto origin | Open |
| EVT-D04 | Target assessment vs outcome | Assessment lifecycle separate from canonical Occurrence result | Open |
| EVT-D05 | Explicit vs implicit non-detection | Explicit internal result; ODR-01 export-only and fail-closed | Open |
| EVT-D06 | SurveyOccurrenceReport cardinality | Explicit target-match/bycatch roles; resolve multiple-Survey export mapping | Open |
| EVT-D07 | Observation/Event/Occurrence relationships | Separate typed evidence links; no automatic conversion | Open |
| EVT-D08 | Organism optionality/grouping | Optional identity; define aggregate cases with evidence | Open |
| EVT-D09 | Location/time/protocol/effort/completeness | Bounded, provenance-aware and no implicit inheritance | Open |
| EVT-D10 | Standards and export profiles | Pin exact term/profile versions and round-trip tests | Open |
| B01 / B02 / B16 | Cross-domain cardinalities and survey semantics | Reconcile source documents and execute fixtures | Open |
| DR-02 | IdentificationSubject integrity | Prove total participation and exactly-one target | Open |
| DR-07 | Explicit non-detection semantics | Reconcile Event/Occurrence model and validate realistic survey fixtures | Open |
| DR-09 | Standards version / term pinning | Exact versioned resources and export profile evidence | Open |
| LDM-16 / FLD-08 | Explicit non-detection and missing-row negative test | Align with Occurrence result and assessment lifecycle | Proposed / not run |

## 8. Recommended next steps

1. **Owner and specialist disposition:** review EVT-D01–D04 and the preferred responsibilities in Section 4. Obtain input from qualified field ecology, botanical taxonomy, biodiversity informatics and data architecture reviewers.
2. **Canonical Candidate A revision:** only after that disposition, consolidate the ERD, relationship table, cardinalities, key strategy and target/assessment model in the existing PR #5 workstream. Remove contradictions rather than append another competing addendum.
3. **Task 05B reconciliation:** align the dictionary's §16 and §17 so SurveyTargetAssessment and Occurrence have one consistent responsibility split; retain the historical source and change history.
4. **Task 05D synchronization:** refresh source SHAs and update EVT-34–EVT-44/LDM/FLD expected graphs on the existing PR #11 branch after the logical decision is settled. Do not rebase or retarget automatically.
5. **Standards evidence bundle:** pin exact TCS, Darwin Core, Humboldt and GBIF profile/term resources; keep DR-09 open until reproducible.
6. **Synthetic fixture execution:** implement the approved logical tests with expected graphs, negative cases, actual run outputs and evidence. Mark each test outcome honestly.
7. **Independent review:** record reviewer competence, scope, conflicts, date, findings, dissent and disposition.
8. **Task 05D gate:** pass only when the model is coherent, tests have executed, standards mappings are pinned and required specialist review is recorded.
9. **Task 05E:** remains blocked until the above gate passes and the project owner authorizes physical design.

## 9. Work completed and not completed

### Completed by this review

- Retrieved the complete governing operating prompt from the required PR #16 branch.
- Re-fetched the live repository branch list, open PR list, relevant branch heads and PR metadata.
- Re-fetched Task 05, Task 05B, Candidate A, Candidate B, Task 05D v3 and the PR #9 review sources at exact refs.
- Compared Candidate A, Candidate B, Task 05D v3 and historical Task 05D branch histories.
- Checked current official TCS, Darwin Core, GBIF and PostgreSQL sources.
- Prepared this source-by-source reconciliation on the existing PR #9 review branch.

### Not performed

- No Candidate A, Candidate B, Task 05B or Task 05D source model was edited.
- No accepted ADR or product requirement was amended.
- No scientific decision was accepted or closed.
- No tests were executed.
- No external specialist, institution or rights-holder was contacted.
- No PR was merged, closed or retargeted.
- No branch was created or deleted.
- No repository protection, permission or setting was changed.
- No physical schema, DDL, migration, API payload freeze or application code was created.

## 10. Authoritative references checked on 26 November 2026

1. TDWG, Taxon Concept Standard List of Terms, version 2025-12-11: https://tcs.tdwg.org/terms/
2. TDWG, Darwin Core List of Terms: https://dwc.tdwg.org/list/
3. TDWG, Darwin Core Quick Reference Guide: https://dwc.tdwg.org/terms/
4. GBIF, Guide for publishing biological survey and monitoring data, v1.0.2 (2025-09-24): https://docs.gbif.org/guide-publishing-survey-data/en/
5. PostgreSQL, Constraints documentation: https://www.postgresql.org/docs/current/ddl-constraints.html
6. TDWG, Darwin Core Conceptual Model: https://dwc.tdwg.org/cm/ — the exact 2026-10-13 versioned resource was not re-fetched and compared in this review; DR-09 remains open.

**Closing status:** Candidate A remains the preferred review starting point, not an approved model. Candidate B remains a preserved alternative. Task 05D remains PROPOSED / NOT PASSED. Task 05E and physical schema design remain NOT READY.
