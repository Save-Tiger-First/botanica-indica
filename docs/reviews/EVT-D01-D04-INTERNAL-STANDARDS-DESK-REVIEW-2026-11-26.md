# EVT-D01–D04 — Internal Standards Desk Review and Cross-Document Gap Report

**Document ID:** STF-BI-REV-EVT-005  
**Version:** 0.1  
**Date checked:** 26 November 2026  
**Status:** Internal AI-assisted desk review; NOT independent specialist review, NOT scientific approval  
**Repository:** `Save-Tiger-First/botanica-indica`  
**Branch:** `review/scientific-data-model-review-pack`  
**Related PR:** #9

> **Authority boundary:** This report is a desk review of repository documents and public standards sources. No external specialist was contacted, no field study was conducted, and no independent scientific sign-off was obtained. It records evidence, inconsistencies and recommendations only. EVT-D01–D04 remain OPEN. Candidate A remains NOT APPROVED. Task 05D remains PROPOSED / NOT PASSED. Task 05E and physical database design remain NOT READY.

---

## 1. Purpose and review scope

The project owner accepted the preferred EVT-D01–D04 directions as the working direction for specialist validation. This report performs the next permissible step without representing an AI desk review as a substitute for the required specialists.

Reviewed repository sources:

| Source | Ref/branch | Blob SHA inspected |
|---|---|---|
| AI Project Operating Prompt | `docs/repository-audit-and-ai-operating-standard` | `53add3894d0502827e584614c70ad09cadaa637d` |
| Owner Disposition and Specialist Review Brief | review branch | `ccd8a0f86ca58e3fed0ea02cd339040843717c8f` |
| EVT-D01–D04 Decision Readiness Review | review branch | `ab7872f44d9f49cad762e64f9a147a98eee53fbc` |
| EVT Decision and Validation Pack | review branch | `4a317c4c83317e10663ba374e9e6be3100a53431` |
| Scientific Data Model Validation Matrix and Decision Register | review branch | `3a33dfe47657a96456f56f2c12a0b7d355b6c6a5` |
| Candidate A — Task 05C | `docs/task-05c-logical-data-model` | `b447796e7da0d08d96400812667a8e67e0696144` |
| Task 05B Scientific Data Dictionary | `docs/task-05-data-dictionary` | `ddaa379d993fdf1f45684962930d16f06830ae43` |
| Task 05D v3 validation gate | `docs/task-05d-logical-model-validation-v3` | `0b9a009b1c543b2450758f659c97cae3802a2f94` |

The review focuses on semantic coherence, source/version correctness, internal-vs-export boundaries and unresolved test obligations. It does not approve the data model or make a final scientific judgement.

## 2. Executive findings

1. **The preferred Event / Survey / Occurrence direction is conceptually defensible**, but it is not yet a canonical relational model. Candidate A still preserves earlier Event-to-Occurrence content and later shared-identity subtype content as separate proposals.
2. **The assessment/outcome issue is substantive, not merely terminological.** Task 05B and Candidate A use `SurveyTargetResult` with detected/non-detected states. The EVT decision pack recommends `SurveyTargetAssessment` for assessment/completeness and Occurrence for the authoritative organism/taxon outcome. These patterns must not coexist as two independently editable outcome authorities.
3. **Survey-to-Occurrence reporting and Event parent-child hierarchy must remain separate relationships.** The GBIF guide's export-row constraints need an explicit mapping strategy if an internal Occurrence can be referenced by multiple Surveys.
4. **The Conceptual Model itself is non-normative apart from its document-status section.** Its semantic content is useful design guidance, not a mandated relational schema or a set of database implementation constraints.
5. **DR-09 is not closed.** The live official pages and indexed version metadata remain inconsistent across the Conceptual Model, Darwin Core List and Humboldt term resources. The exact versioned resources and term IRIs must be fetched and pinned.
6. **No test evidence exists in the inspected records to support a pass.** EVT-27–EVT-44 and the relevant LDM/FLD cases remain proposed unless actual run evidence is added.

## 3. Findings by decision

### 3.1 EVT-D01 — Event identity and specializations

**Finding:** Candidate A §18 and Task 05B §16 propose one shared Event identity with distinct Survey and Occurrence specializations. This aligns with the Darwin Core Conceptual Model's semantic distinction: Survey and Occurrence are special types of Event, and a single Event instance must not be interpreted as simultaneously being both.

**Important qualification:** The Darwin Core Conceptual Model says it does not prescribe a system implementation, a formal predicate ontology or a strict system blueprint. All content outside its status section is explicitly non-normative. Therefore:
- shared Event identity is a sound candidate pattern, not a mandatory SQL inheritance strategy;
- Botanica Indica may choose a different logical/physical representation if it preserves the semantics and demonstrates lossless mappings;
- the model must not imply that a shared Event table is required by Darwin Core.

**Recommendation:** Retain shared Event identity with distinct typed Survey and Occurrence specializations as the preferred review hypothesis. Keep generic/context Events distinct. Require worked examples for context Events, Survey reporting, Occurrence evidence, material gathering and repeated visits before final approval.

**Unresolved:** subtype total participation/exclusivity, exact generic/context semantics, and whether all product workflows fit the proposed specialization rule.

### 3.2 EVT-D02 — Hierarchy, reporting and context

**Finding:** The project consistently identifies three different relationship meanings:
- parent-child Event hierarchy;
- Survey reports Occurrence;
- generic context Event is associated with one or more activity Events.

The Darwin Core Conceptual Model describes a strict Event hierarchy as a child wholly contained within one parent in space and time, with a dependent connection, and says a child has only one parent. It separately notes that a context Event may provide shared spatiotemporal context to multiple activities.

**Critical standards qualification:** In the directly opened Darwin Core Conceptual Model, the Event-hierarchy section is marked non-normative. Candidate A §18.6 refers to a separate Humboldt hierarchical-event guidance and calls Section 3 normative, but the exact versioned guidance resource and its Section 3 were not retrieved during this review. Do not transfer the “normative” label from one resource to another without fetching that exact resource.

**Recommendation:** Keep the three relationships separate in the logical model. Treat single-parent, acyclicity and spatial/temporal containment as proposed internal integrity rules pending exact standards pinning and product workflow validation. Do not call the rule a verified normative requirement until the referenced versioned Humboldt guidance is directly inspected.

**Unresolved:** exact Humboldt guidance version and normative text; whether context should be a role on a generic Event, a typed association, or both; and how unknown spatial/temporal extents are handled without false validation.

### 3.3 EVT-D03 — Survey and SurveyTarget

**Finding:** The Darwin Core Conceptual Model describes a Survey as a type of Event. It says a Survey Target declares what was sought, either a priori or through post-facto filtering; Survey results are expressed in Occurrences reported by the Survey; targets may combine taxa, environmental conditions and organismal traits.

The Humboldt `eco:SurveyTarget` term definition retrieved from the official term-list search result is “One or more scopes that describe a target for dwc:Occurrences in an eco:Survey.” This is important: it qualifies the Occurrences sought/reported. It does not turn every environmental measurement into an Occurrence or make every measurement a SurveyTarget result.

**Recommendation:** Keep SurveyTarget structured and versioned, with explicit target origin (a priori vs post-facto), inclusion/exclusion semantics, taxonomic treatment/version where relevant, author/time and provenance. Do not infer a priori intent from a later analytical filter. Keep pure environmental/site measurements separate from Occurrence reporting and design them only against explicit product workflows.

**Unresolved:** target-scope vocabulary and supported combinations; taxon-concept pinning; event-level scope applicability; and the exact versioned term set for export.

### 3.4 EVT-D04 — Assessment lifecycle and canonical outcome

**Finding:** Current source documents conflict materially:
- Task 05B §16 defines `SurveyTargetResult` with states such as `DETECTED`, `NOT_DETECTED_EXPLICIT`, `INCONCLUSIVE` and `NOT_ASSESSED`.
- Candidate A §18.3–§18.5 also defines `SurveyTargetResult` as a result for one Survey, target and scope/period.
- The EVT decision pack recommends `SurveyTargetAssessment` as a record of whether/how a target was assessed, with protocol, effort, completeness, agents, evidence and limitations.
- The same EVT proposal places the canonical organism/taxon-level detection or explicit non-detection state on the Occurrence.

These patterns are not equivalent. If both entities store independently mutable detected/non-detected state, they can contradict one another. If the assessment record stores only lifecycle/completeness, it is not itself the canonical scientific outcome.

**Recommendation:** Preferred pattern for specialist review:
- `SurveyTarget`: versioned declared or post-facto scope/filter;
- `SurveyTargetAssessment` (working name): whether/how that target was assessed for a defined survey/visit/time/place, with protocol, effort, completeness, limitations, agent and provenance;
- `Occurrence`: authoritative organism/taxon-level state, including explicit non-detection only where scientifically justified;
- `SurveyOccurrenceReport`: typed association between a Survey and the Occurrence it reports, including target match/bycatch role.

Do not keep a second independently editable detected/non-detected state in `SurveyTargetAssessment`. If specialists conclude the SurveyTargetResult is instead the sole canonical outcome, the model must explicitly remove or derive the duplicate Occurrence state. Do not combine both patterns.

**Unresolved:** the scientifically appropriate unit of negative Occurrence; whether the unit is TaxonConcept, Taxon plus organismal state, or a more specific bounded target; handling of taxonomic change; repeated assessments; correction/retraction; and the required evidence threshold for explicit non-detection.

## 4. Cross-document contradictions requiring controlled resolution

| ID | Contradiction / gap | Risk | Required action |
|---|---|---|---|
| X-01 | Candidate A earlier sections model Event-to-Occurrence as contextual one-to-many; §18 proposes Occurrence as Event specialization | Two incompatible identity models in one document | Produce one canonical ERD and retire/mark earlier pattern as superseded only after approval |
| X-02 | Task 05B §16 and Candidate A §18 use SurveyTargetResult; EVT pack uses SurveyTargetAssessment | Duplicate or ambiguous outcome authority | Explicitly choose lifecycle-vs-outcome responsibility and controlled terminology |
| X-03 | Candidate A §18.3 permits one Occurrence to be reported by multiple Surveys; GBIF DwC-A guide says each Occurrence row can link to only one Survey Event | Internal cardinality may not export directly | Decide whether multiple internal report links are needed; define row identity, duplication/shared-evidence and loss-aware export mapping |
| X-04 | Candidate A §18.6 says Humboldt hierarchical-event guidance version 2024-02-28, Section 3 normative; review pack says 2026-10-13 | Unsupported or inconsistent standards claim | Retrieve exact versioned guidance and quote exact section/status before claiming normative |
| X-05 | Task 05C §18.1/§20.1 and Task 05D describe conflicting Darwin Core Conceptual Model version evidence | Wrong standards baseline could propagate | Keep DR-09 open; record document version, list snapshot, namespace snapshot and individual term versions separately |
| X-06 | Candidate A §18.6 and Task 05D imply hierarchy/containment as standards requirement without consistently distinguishing conceptual guidance from normative terms | Overstates standards compliance | Separate standard requirements, non-normative semantic guidance and internal design invariants |
| X-07 | Explicit non-detection represented as Occurrence but the supporting assessment and SurveyTargetResult remain under-specified | False or untraceable absence claims | Define bounded target, time/place, protocol/effort, completeness, evidence, agent, uncertainty and correction history |
| X-08 | EVT-27–EVT-44 and LDM/FLD tests remain proposed | Documentation may be mistaken for validation | Execute tests against a frozen candidate model only after decisions; record results and failures |

## 5. Current authoritative source findings checked 26 November 2026

### 5.1 Darwin Core Conceptual Model

The official page at https://dwc.tdwg.org/cm/ was opened. The rendered page identifies:
- Date version issued: 2026-05-26;
- This version: `http://rs.tdwg.org/dwc/doc/cm/2026-05-26`;
- latest version IRI: `http://rs.tdwg.org/dwc/doc/cm/`.

However, a separate current indexed search result for the same official page reports:
- Date version issued: 2026-10-13;
- This version: `http://rs.tdwg.org/dwc/doc/cm/2026-10-13`;
- Previous version: 2026-05-26.

The exact 2026-10-13 versioned resource could not be opened in this review. Therefore the conflict is not resolved. Do not claim either metadata view alone is conclusive. Pin the directly opened 2026-05-26 content for the semantics actually inspected, record the indexed 2026-10-13 metadata as an unresolved newer-version signal, and retrieve/compare the exact 2026-10-13 resource before closing DR-09.

The page states the Conceptual Model is a high-level semantic framework and does not prescribe a system technology or strict blueprint. It marks all sections other than the document-status section non-normative.

Sources:
- https://dwc.tdwg.org/cm/
- https://dwc.tdwg.org/cm/2026-05-26.html
- https://rs.tdwg.org/dwc/doc/cm/2026-10-13 (exact versioned resource not successfully opened)
- https://dwc.tdwg.org/list/

### 5.2 Darwin Core List of Terms

The official List search result reports version issued 2026-10-13, previous version 2026-05-26. The term-level version of `dwc:occurrenceStatus` must be recorded separately from the List snapshot date. The previously inspected term version 2026-05-26 recommends `detected` and `notDetected`; the GBIF survey guide uses `present` and `absent` in its examples.

Do not treat the List issue date, a namespace snapshot, an individual term's version IRI and GBIF profile examples as interchangeable.

Source:
- https://dwc.tdwg.org/list/

### 5.3 Humboldt Extension terms

The official Humboldt term-list search result reports a 2026-05-26 list version and shows term-specific version IRIs including:
- `eco:Survey`: `http://rs.tdwg.org/eco/terms/version/Survey-2026-05-26`;
- `eco:SurveyTarget`: `http://rs.tdwg.org/eco/terms/version/SurveyTarget-2026-05-26`;
- `eco:isSurveyTargetFullyReported`: `http://rs.tdwg.org/eco/terms/version/isSurveyTargetFullyReported-2026-05-26`.

A historical 2026-05-26 term-list snapshot reports that it was superseded/replaced by a 2026-10-13 list snapshot. The current term-list page search result still surfaces 2026-05-26 metadata. The exact 2026-10-13 list was not successfully retrieved. DR-09 remains open.

Sources:
- https://rs.tdwg.org/eco/terms.htm
- https://rs.tdwg.org/eco/version/terms/2026-05-26.htm
- https://rs.tdwg.org/eco/version/terms/2026-10-13.htm (exact versioned resource not successfully opened)

### 5.4 GBIF survey guide

The official guide is v1.0.2, published 2025-09-24. It states:
- any Event may be associated with one or more Occurrence records;
- each Occurrence record in a Darwin Core Archive can be linked to only one survey Event;
- recommended best practice is to link an Occurrence to the lowest possible Event level in a nested hierarchy;
- scope terms should be populated only at Event levels where explicitly stated, not inferred up or down the hierarchy;
- absence/non-detection inference requires appropriate stated scope and completeness;
- absence cannot be asserted for bycatch;
- eMoF and Relevé extensions can carry additional Event/site measurement information.

This is publishing guidance for GBIF, not a mandatory internal Botanica Indica database schema. It does, however, require an explicit mapping design for internal multi-Survey reporting.

Source:
- https://docs.gbif.org/guide-publishing-survey-data/en/

### 5.5 PostgreSQL constraints

PostgreSQL documentation states that CHECK constraints cannot safely reference other table rows and that such designs may fail under later changes or dump/restore. It recommends using UNIQUE, EXCLUDE or FOREIGN KEY constraints where possible; triggers may be appropriate for other cross-row invariants.

Source:
- https://www.postgresql.org/docs/current/ddl-constraints.html

## 6. Proposed disposition matrix — for specialist review only

| Decision | Preferred working direction | Required proof before closure |
|---|---|---|
| EVT-D01 | Shared Event identity with distinct Survey and Occurrence specializations; generic/context Event kept separate | Field workflow examples; subtype exclusivity/participation; context semantics; mapping to exact pinned DwC version |
| EVT-D02 | Parent-child only for true hierarchy; separate Survey report and context links | Exact hierarchical-event source/version; cycle/single-parent/containment tests; explicit scope ownership |
| EVT-D03 | Structured/versioned SurveyTarget with a priori/post-facto provenance; target scope is not a generic measurement outcome | Taxonomic change examples; habitat/trait scope examples; no-target Survey; deterministic inclusion/exclusion |
| EVT-D04 | Assessment lifecycle separated from canonical Occurrence-level outcome; no duplicated mutable negative state | Field-ecology and taxonomy review of negative Occurrence unit; repeat/incomplete/bycatch/correction cases; export mapping |

These are recommendations, not approved scientific decisions.

## 7. Minimum executable scenarios before Task 05D can pass

The following are minimum proposed cases; no test is claimed executed:

1. One Survey Event with multiple target-matching Occurrences.
2. One Survey Event reporting a bycatch Occurrence that does not satisfy target completeness.
3. A generic context Event associated with distinct Survey and Occurrence Events without identity conflation.
4. A genuine nested parent-child Event with spatial and temporal containment.
5. An invalid multi-parent child and an Event hierarchy cycle rejected.
6. Parent scope not silently inherited by a child; child scope not silently promoted to parent.
7. A priori target and later post-facto filter retained as separate versioned records.
8. A Survey with no declared target remains valid but cannot support target-specific non-detection inference.
9. Explicit non-detection with bounded taxon concept/organismal state, place, time, protocol, effort, completeness, agent and evidence.
10. Incomplete/not-assessed/inconclusive cases do not create a negative Occurrence.
11. A taxonomic split/lump does not silently rewrite historical target meaning or non-detection.
12. One internal Occurrence associated with two Survey reports, with a declared GBIF export strategy or a justified rejection of the internal cardinality.
13. Environmental/site measurement mapped separately from Occurrence and SurveyTarget.
14. Export mapping tests for `detected/notDetected` versus `present/absent` under a pinned profile and term set.
15. Fail-closed export if any required scope, completeness, provenance, hierarchy, term version or mapping is missing or contradictory.
16. Sensitive location generalization/withholding remains effective in exports, media, logs and derived products.

Tests must run against an explicitly identified candidate model revision. Record fixtures, expected results, actual results, test code/tool, environment, date, reviewer and failure disposition. Synthetic test data validates logic only; it is not ecological field evidence.

## 8. Recommended controlled next sequence

1. Obtain attributable field-ecology, botanical-taxonomy, biodiversity-informatics and data-architecture reviews against STF-BI-REV-EVT-004.
2. Resolve the exact TDWG Conceptual Model, List, Humboldt term-list and hierarchical-event guidance versions; keep DR-09 open until exact versioned resources and relevant term IRIs are directly retrievable and compared.
3. Decide the internal Occurrence/reporting cardinality separately from Darwin Core Archive row mapping.
4. Resolve the SurveyTargetResult versus SurveyTargetAssessment responsibility split.
5. After specialist findings, update the EVT decision register with accepted/rejected/conditional outcomes and unresolved disagreements.
6. Only with explicit owner approval, produce one canonical Candidate A ERD, entity/relationship specification and cardinality/invariant table.
7. Reconcile Task 05B and Task 05D against that exact approved baseline.
8. Execute the synthetic tests and record actual evidence.
9. Reassess Task 05D readiness; do not start Task 05E until its gate passes.

## 9. Repository and action boundaries

Repository state rechecked on 26 November 2026:
- 23 branches exist, including the required `main`, `develop` and `staging`.
- The governing prompt requires an immediate maximum of seven branches, with no new branches permitted. This target remains unmet.
- PR #9 remains open and draft, based on `main`.
- Review branch head before this report: `8c4e7d7e6db0cd32602077da6fdb24095f275df0`.
- No branch was created or deleted.
- No PR was merged, closed or retargeted.
- No repository protection, permission or setting was changed.
- No external party was contacted.
- No specialist sign-off was obtained.
- No tests were executed.
- No accepted ADR, approved product requirement or canonical scientific model was changed.
- No DDL, migration, physical schema, API contract or implementation was authorized.

**End of document — STF-BI-REV-EVT-005 v0.1.**

## 10. Standards evidence correction — 26 November 2026

This correction supersedes older List/term-version statements in Section 5 where inconsistent with the current official TDWG metadata checked in the Standards Version Verification Addendum (blob `85bf0e6e85025a6a8d19f463f743a728a0b6857a`).

- The current official Darwin Core Conceptual Model and List identify 2026-10-13 as the current issue version. The Conceptual Model remains non-normative semantic guidance; it does not prescribe a relational schema or inheritance implementation.
- `dwc:samplingEffort` and `dwc:samplingProtocol` have 2026-10-13 term versions and Survey-scoped definitions.
- `dwc:occurrenceStatus-2026-05-26` recommends `detected` / `notDetected`. GBIF guide examples `present` / `absent` require an explicit export-profile mapping.
- Relevant Humboldt term versions are not uniform: `eco:Survey` and `eco:isTaxonomicScopeFullyReported` are 2026-10-13; `eco:SurveyTarget` and `eco:isSurveyTargetFullyReported` are 2026-05-26. Archive the complete current Humboldt snapshot before closing DR-09.
- GBIF v1.0.2 §7.3 does not make `eco:taxonCompletenessReported=reportedComplete` a universal additional prerequisite to its taxonomic-scope implicit-absence recipe. A stricter rule is a Botanica Indica policy choice, not a GBIF requirement.

The decision recommendations in this desk review remain proposals. EVT-D01–D04 remain open; no canonical model is approved and Task 05E remains not ready.

Source: [EVT-D01–D04 Standards Version Verification Addendum](EVT-D01-D04-STANDARDS-VERSION-VERIFICATION-ADDENDUM-2026-11-26.md).
