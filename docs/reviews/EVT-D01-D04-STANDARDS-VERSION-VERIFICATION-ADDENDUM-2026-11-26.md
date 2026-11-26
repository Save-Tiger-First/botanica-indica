# EVT-D01–D04 — Standards Version Verification Addendum

**Document ID:** STF-BI-REV-EVT-006  
**Version:** 0.1  
**Date checked:** 26 November 2026  
**Status:** Internal standards desk research; proposed findings only; no scientific decision approved  
**Repository:** `Save-Tiger-First/botanica-indica`  
**Branch:** `review/scientific-data-model-review-pack`  
**Related PR:** #9

> **Authority boundary:** This addendum records public-source verification and a cross-document correction. It is not an independent specialist review, legal opinion, scientific approval, Task 05C approval, Task 05D pass, export-profile approval or implementation authorization. No external party was contacted.

---

## 1. Executive finding

The standards retrieval issue is now more precisely characterized, but **DR-09 should remain open** until exact versioned resources and the relevant term set are captured reproducibly.

Three separate situations must not be conflated:

1. **Darwin Core Conceptual Model:** the official page content directly rendered during this check identifies 2026-05-26, while current official search-index metadata reports a 2026-10-13 issue date and a 2026-10-13 version IRI. The exact 2026-10-13 versioned resource could not be opened through the available retrieval route. The content/version discrepancy remains unresolved.
2. **Humboldt hierarchical-event guidance:** official TDWG indexed content identifies the exact 2026-10-13 version and exposes Section 3 as normative, with relevant normative text available in the indexed result. This is materially stronger evidence than the prior review had.
3. **Darwin Core and Humboldt term lists:** the accessible rendered List pages still expose 2026-05-26 headers/snapshots, while official current term results and the supersession metadata expose individual 2026-10-13 term versions. The exact 2026-10-13 Humboldt list snapshot and complete current term set were not directly retrieved.

The correct position is therefore not “all current standards versions are verified” and not “the 2026-10-13 metadata is unconfirmed.” Some resources and term versions are now verified; others still have version-rendering or exact-snapshot retrieval gaps.

## 2. Repository baseline and source revisions

The complete operating prompt was re-fetched from `docs/governance/AI-PROJECT-OPERATING-PROMPT.md` on `docs/repository-audit-and-ai-operating-standard`; blob SHA:

`53add3894d0502827e584614c70ad09cadaa637d`

The live repository was rechecked immediately before this document was created. There were 23 branches. The three long-lived branches existed; the operating prompt's seven-branch ceiling was not met. The existing review branch was reused. No branch was created or deleted.

Relevant inspected repository files:

| File | Branch | Blob SHA |
|---|---|---|
| Internal standards desk review | `review/scientific-data-model-review-pack` | `7037b073ff3a497b36d61a073e86d79d0616b8d3` |
| Owner disposition and specialist brief | same | `ccd8a0f86ca58e3fed0ea02cd339040843717c8f` |
| EVT decision and validation pack | same | `4a317c4c83317e10663ba374e9e6be3100a53431` |
| Validation matrix and decision register | same | `3a33dfe47657a96456f56f2c12a0b7d355b6c6a5` |
| Task 05C Candidate A | `docs/task-05c-logical-data-model` | `b447796e7da0d08d96400812667a8e67e0696144` |
| Task 05B dictionary | `docs/task-05-data-dictionary` | `ddaa379d993fdf1f45684962930d16f06830ae43` |
| Task 05D v3 | `docs/task-05d-logical-model-validation-v3` | `0b9a009b1c543b2450758f659c97cae3802a2f94` |

The current review-branch head before this addendum was:

`86534c5c9889ef698a18bd16b90da477bca588bd`

These are point-in-time source pins, not permanent pins.

## 3. Darwin Core Conceptual Model — current version verified

The current official TDWG page identifies the Darwin Core Conceptual Model version issued **2026-10-13**, with version IRI `http://rs.tdwg.org/dwc/doc/cm/2026-10-13` and previous version 2026-05-26. The current official page's indexed content exposes the 2026-10-13 metadata and semantic text. The Conceptual Model describes itself as a high-level framework for semantics of relationships among Darwin Core classes; it does not prescribe formal predicates or a particular system/database implementation. Its Event and Survey/Occurrence sections are non-normative guidance.

The current model describes Survey and Occurrence as special types of Event with distinct characteristics. Survey results are expressed through the Occurrences the Survey reports. Occurrences may be target-matching or bycatch. A Survey may be represented using an Event hierarchy. Occurrence represents the state of an Organism at a place/time, and may be supported by direct or indirect evidence. A generic/context Event may be used to represent shared spatiotemporal context where justified.

**Design consequence:** a shared Event identity with distinct Survey and Occurrence specializations is a coherent internal design hypothesis, not a TDWG-mandated SQL inheritance pattern. Survey-to-Occurrence reporting, parent-child Event containment and shared context must be represented as distinct relationship types.

Source:
- https://dwc.tdwg.org/cm/
- https://rs.tdwg.org/dwc/doc/cm/2026-10-13

## 4. Humboldt hierarchical-event guidance — exact 2026-10-13 version located

The official TDWG result identifies:

- Title: *Properties of hierarchical events in the Humboldt Extension for Ecological Inventories*
- Date created: 2024-02-28
- Date version issued: 2026-10-13
- Version IRI: `http://rs.tdwg.org/dwc/doc/hierarchy/2026-10-13`
- Previous version: 2024-02-28.

The indexed official content exposes the document's status statement: Section 3 is normative; other sections are non-normative.

Relevant Section 3 requirements visible in the official result include:

1. A parent Event MUST spatially and temporally encompass its child Events.
2. A Darwin Core inventory hierarchy is explicitly represented by the child's `dwc:parentEventID`.
3. A child Event MUST NOT be assumed to inherit parent properties implicitly.
4. A parent Event property SHOULD NOT be populated by deriving or summarizing child Event information; it should be explicitly provided when appropriate.
5. The guidance distinguishes the flattened Darwin Core Archive representation from normalized relational database structures and notes that Darwin Core Data Package can represent related tables.

**Do not overstate the guide:** the single-parent statement is explicitly visible in the Conceptual Model's non-normative Event discussion. The retrieved 2026-10-13 hierarchical-event guide text establishes containment and explicit parent-child mapping, but the reviewed excerpt does not independently establish a new normative single-parent rule. Keep these source levels distinct.

### Disposition

The prior Candidate A citation to a 2024-02-28 hierarchical-event guide as if it were current is stale. The correct current guide metadata is 2026-10-13. The exact source and relevant section have now been identified, but a durable copy of the full official document should still be captured in the standards evidence bundle before final compliance assertions.

Source:
- https://dwc.tdwg.org/hierarchy/
- https://rs.tdwg.org/dwc/doc/hierarchy/2026-10-13

## 5. Darwin Core List and term-level version pins

The current official TDWG search-index metadata identifies the Darwin Core List of Terms as version issued **2026-10-13**, with version IRI `http://rs.tdwg.org/dwc/doc/list/2026-10-13` and previous version 2026-05-26. However, opening the current List landing page directly in this review still renders a 2026-05-26 header and the 2026-05-26 vocabulary version. The exact versioned 2026-10-13 List resource could not be independently opened and compared in this session.

**Therefore the List document-level version discrepancy remains open.** Do not call the 2026-10-13 List content fully inspected. Record both observations: (a) indexed official metadata says 2026-10-13; (b) direct page rendering says 2026-05-26. This is the precise DR-09 issue, not a reason to choose one rendering silently.

The separate official current core Darwin Core namespace term list does directly expose current term-version metadata for `dwc:samplingEffort` and `dwc:samplingProtocol` (both 2026-10-13). Those term-level facts can be used without asserting that the complete 2026-10-13 List document was retrieved. The official core terms page also makes clear that each term has its own version and status; do not infer term versions from the List issue date.

The current Quick Reference Guide is a usage guide, not itself part of the standard. For normative vocabulary definitions and term versions, use the current term-version records and preserve their IRIs.

### 5.1 Verified term-level pins

| Term | Directly verified current term version | Meaning / consequence |
|---|---|---|
| `dwc:occurrenceStatus` | `occurrenceStatus-2026-05-26` | Statement about detection/non-detection of an Organism during an Event. Recommended values: `detected`, `notDetected`. |
| `dwc:samplingEffort` | `samplingEffort-2026-10-13` | Current core-term definition: amount of effort expended during an `eco:Survey`. |
| `dwc:samplingProtocol` | `samplingProtocol-2026-10-13` | Current core-term definition: names, references or descriptions of methods/protocols used during an `eco:Survey`. |
| `dwc:Occurrence` | `Occurrence-2026-05-26` in the directly rendered List | An Event establishing the state of an Organism at a particular place and time; distinct from Organism and MaterialEntity. |

The current official core namespace term page directly verifies the two 2026-10-13 sampling term versions. The directly rendered List verifies the 2026-05-26 `occurrenceStatus` version and its recommended values. These are term-level facts, not evidence that the entire 2026-10-13 List document has been opened.

The GBIF survey guide v1.0.2 examples use `present` and `absent` for occurrence status. These literals must not be copied into a Darwin Core mapping by assumption. The selected export profile must define, version and test any mapping between Darwin Core's recommended `detected/notDetected` values and GBIF guide examples.

Sources:
- https://rs.tdwg.org/dwc/terms.htm (current core namespace term records)
- https://dwc.tdwg.org/list/ (direct page rendering in this review)
- https://docs.gbif.org/guide-publishing-survey-data/en/

## 6. Humboldt Extension — term-level evidence and snapshot gap

The directly opened official Humboldt Extension terms page still identifies its list snapshot as **2026-05-26**. It exposes:
- `eco:Survey-2026-05-26`, definition “A biotic survey or inventory.”
- `eco:SurveyTarget-2026-05-26`, defined as one or more scopes describing a target for Occurrences in a Survey.
- `eco:isSurveyTargetFullyReported-2026-05-26`, a recommended target-specific completeness term.
- `eco:isTaxonomicScopeFullyReported-2024-02-28`, marked superseded and replaced by `isTaxonomicScopeFullyReported-2026-10-13`.
- `eco:isSamplingEffortReported-2024-02-28`, marked superseded and replaced by `isSamplingEffortReported-2026-10-13`.

This is evidence of term-level replacements, not direct retrieval of the complete 2026-10-13 Humboldt term list or every replacement definition. The current 2026-10-13 List search result contains current terms from multiple namespaces, but the directly opened List and Humboldt term-list pages still render 2026-05-26. Keep this retrieval discrepancy visible.

Do not claim `eco:Survey` or `eco:SurveyTarget` has a 2026-10-13 term version on the evidence directly inspected here. Use the exact 2026-05-26 versions as the retrieved term records until a later individual version is directly confirmed.

| Term | Retrieved term-version position | Semantics / design consequence |
|---|---|---|
| `eco:Survey` | `Survey-2026-05-26` directly visible | Direct page definition is “A biotic survey or inventory.” Current Quick Reference may give newer recommended usage; archive exact source before revising the internal Survey definition. |
| `eco:SurveyTarget` | `SurveyTarget-2026-05-26` directly visible | One or more scopes describing a target for Occurrences in a Survey. |
| `eco:isSurveyTargetFullyReported` | `isSurveyTargetFullyReported-2026-05-26` directly visible | Target-specific reporting completeness; not interchangeable with taxonomic-scope completeness. |
| `eco:isTaxonomicScopeFullyReported` | 2024-02-28 superseded; replacement term IRI dated 2026-10-13 reported by official metadata | Exact 2026-10-13 term definition/status must be retrieved before implementation. |
| `eco:isSamplingEffortReported` | 2024-02-28 superseded; replacement term IRI dated 2026-10-13 reported by official metadata | Pin replacement term and definition before export implementation. |
| `eco:taxonCompletenessReported` / `eco:taxonCompletenessProtocols` | GBIF guide semantics; exact current term IRIs still need direct retrieval | Assessment of taxonomic completeness and method remain distinct from reporting completeness and effort. |
| `eco:isAbsenceReported` | Exact current term-version record still to be captured | Distinguish explicit absence rows from implicit export inference. |

Sources:
- https://rs.tdwg.org/eco/terms.htm
- https://rs.tdwg.org/eco/version/terms/2026-05-26.htm
- https://dwc.tdwg.org/list/

## 7. Humboldt implicit non-detection inference — critical ODR-01 qualification

The current official TDWG hierarchical-event guidance search result (version 2026-10-13) explicitly describes implicit inference of undetected taxonomic and other organismal targets. For the taxonomic-scope pattern, zero quantities need not be supplied as separate Occurrence rows when the Survey declares the encompassing scope and all detected taxa/targets within that scope were fully reported. The guide's example depends on an a priori target taxonomic scope (the combination of `eco:targetTaxonomicScope` and `eco:excludedTaxonomicScope`) and `eco:isTaxonomicScopeFullyReported=true`.

The GBIF survey guide v1.0.2 provides an important distinction:
- `eco:isTaxonomicScopeFullyReported` is the report-completeness condition: all detected Occurrences within the declared taxonomic scope were reported.
- `eco:taxonCompletenessReported` states whether taxonomic completeness was assessed, with values `reportedComplete`, `reportedIncomplete` or `notReported`; when assessed, the method is documented in `eco:taxonCompletenessProtocols`.
- These are not interchangeable. The guide's implicit-absence recipe in §7.3 explicitly requires `eco:isTaxonomicScopeFullyReported=true` and a declared target or excluded taxonomic scope. It does not state that `taxonCompletenessReported=reportedComplete` is an additional universal prerequisite. Treating it as mandatory would be a stricter Botanica Indica policy decision, not a direct GBIF guide requirement.
- `eco:isSurveyTargetFullyReported` is a separate, target-specific flag. It supports inference for the particular SurveyTarget whose detected Occurrences were fully reported. Do not automatically require or substitute it in the GBIF taxonomic-scope recipe; determine its use for a selected profile and target-based export through explicit mapping and specialist review.
- Bycatch has separate reporting terms. GBIF states that absence cannot be asserted for bycatch.

The GBIF guide further says that implicit absence creates no Occurrence row for the implicitly absent taxon and sets `eco:isAbsenceReported=false` on relevant Event rows because no absences are explicitly reported. Explicit absences, by contrast, use Occurrence rows and set `eco:isAbsenceReported=true` at relevant Events.



This has a direct consequence for ODR-01:

- The external inference mechanism is a standards-defined interpretation of a sufficiently complete survey dataset; it is not evidence that the organism is biologically absent.
- It must be scoped to the exact Survey, hierarchy level, declared target/exclusion scope and term/profile versions.
- A priori scope, applicable report-completeness declarations, protocol/search method, reporting of detected target Occurrences and the treatment of bycatch must be validated.
- Taxonomic-completeness assessment/method is a separate detectability-quality dimension. Decide explicitly whether Botanica Indica's fail-closed export policy requires it in addition to the GBIF recipe's scope/report-completeness requirements; do not misstate it as a GBIF §7.3 prerequisite.
- A post-facto filter must not be treated as original field intent for inference about original field survey intent. A post-facto analytical target may still be represented, but its provenance and semantics must remain distinct.
- Scope/completeness must not be inherited or inferred from a parent/child Event unless the selected, pinned standard/profile explicitly defines that behavior.
- If any precondition required by the approved project policy and selected export profile is missing, ambiguous, contradictory or unvalidated, Botanica Indica's ODR-01 policy requires the export to fail closed.
- This must never create or mutate an internal negative Occurrence merely because a target has no matching Occurrence row.

**Important design distinction:** Humboldt's inference mechanism and the owner's ODR-01 policy are compatible only as a constrained, profile-specific export interpretation. The project must not generalize this into a universal internal inference engine or a blanket claim that missing observations mean absence.

Sources:
- https://dwc.tdwg.org/hierarchy/ (current indexed 2026-10-13 guidance; implicit inference discussion)
- https://dwc.tdwg.org/terms/ (current Quick Reference Guide; `eco:isSurveyTargetFullyReported` semantics)
- https://rs.tdwg.org/eco/version/terms/2026-05-26.htm (term version and supersession context)

## 8. GBIF survey guide — confirmed export semantics

GBIF Guide for publishing biological survey and monitoring data to GBIF, v1.0.2, 2025-09-24, remains the inspected publishing guide.

Relevant findings:

1. Any Event can be associated with one or more Occurrence records in the general conceptual mapping.
2. Each Occurrence row in a Darwin Core Archive can be mapped to only a single Survey Event. The guide recommends linking an Occurrence to the lowest possible Event level in a nested hierarchy.
3. Target and excluded scope terms capture survey intent. Other terms describe what actually happened.
4. Scope must be recorded only at Event levels where explicitly stated; it must not be inferred up or down the Event hierarchy, and must not be retrospectively inferred.
5. Absence reporting is meaningful only when the taxonomic scope is fully reported.
6. Absence cannot be asserted for bycatch.
7. Habitat scope is a legitimate Survey scope dimension; actual habitat observed at the survey site is a separate descriptive fact.
8. The guide's examples use `present` / `absent` for `dwc:occurrenceStatus`, while the current Darwin Core term recommends `detected` / `notDetected`.

### Design consequences

- Keep internal scientific identity distinct from export-row identity.
- Preserve an explicit, versioned mapping for any one-Occurrence-to-one-Event export constraint.
- Keep target intent, observed actuality, reporting completeness and ecological detectability separate.
- Do not use bycatch to satisfy target completeness or absence inference.
- Do not infer missing target scope from a parent or child Event.

Source:
- https://docs.gbif.org/guide-publishing-survey-data/en/
- Persistent citation: https://doi.org/10.35035/doc-ynvs-eh84

## 8. GBIF survey guide — completeness and effort semantics

The inspected GBIF Guide for publishing biological survey and monitoring data to GBIF is v1.0.2 (2025-09-24). Its taxonomic-scope section (§5.6.2) distinguishes two dimensions:

1. `eco:isTaxonomicScopeFullyReported`: whether every detected Occurrence included within the declared taxonomic scope was reported. The guide says this is the report-completeness flag used by its implicit-absence pattern.
2. `eco:taxonCompletenessReported`: whether taxonomic completeness was assessed, with values `reportedComplete`, `reportedIncomplete` or `notReported`; if assessed, the method is documented in `eco:taxonCompletenessProtocols`.

The guide's §7.3 implicit-absence recipe explicitly requires `eco:isTaxonomicScopeFullyReported=true` and either `eco:targetTaxonomicScope` or `eco:excludedTaxonomicScope`. It does not explicitly state that `taxonCompletenessReported=reportedComplete` is an additional universal prerequisite. Botanica Indica may choose a stricter fail-closed rule, but that would be a project policy decision and should be labelled as such, not attributed to GBIF.

The same section distinguishes explicit from implicit absence:
- Explicit absence: an Occurrence row with the guide's example `dwc:occurrenceStatus=absent`; set `eco:isAbsenceReported=true` for relevant Events.
- Implicit absence: no Occurrence row is created for the implicitly absent taxon; set `eco:isAbsenceReported=false` for relevant Events because no absences are explicitly reported.
- Absences apply only within declared taxonomic and/or organismal scope. Absence cannot be asserted for bycatch.

The GBIF guide's §5.7 recommends structured Humboldt sampling-effort fields over relying solely on the unstructured `dwc:samplingEffort` field. It identifies `eco:isSamplingEffortReported`, paired `eco:samplingEffortValue`/`eco:samplingEffortUnit`, `eco:samplingEffortProtocol` and `eco:samplingPerformedBy`. It also notes the core `dwc:samplingEffort` field is an unstructured recommended Event field. Current TDWG core definitions now scope `dwc:samplingEffort` and `dwc:samplingProtocol` to an `eco:Survey`; this does not eliminate the need to preserve structured effort dimensions.

**Recommended crosswalk principle:** retain distinct internal facts for (a) target/scope, (b) whether detected records were fully reported, (c) whether taxonomic completeness/detectability was assessed and its method, (d) effort quantity/unit/method and (e) explicit absence reporting. Map these to the chosen external profile without conflating them or manufacturing an additional fact.

Sources:
- https://docs.gbif.org/guide-publishing-survey-data/en/ (v1.0.2, 2025-09-24; §§5.6.2, 5.6.4, 5.7 and 7.3)
- https://dwc.tdwg.org/terms/ (current Quick Reference Guide; not itself part of the standard)
- https://dwc.tdwg.org/tcr/ (Taxon Completeness Reported controlled vocabulary)
- https://rs.tdwg.org/ecotcr/version/values/2026-10-13.htm

## 9. Cross-document implications

### 8.1 Candidate A — Task 05C

Candidate A §20.1 and the 21 November standards correction contain the statement that the exact 2026-10-13 Conceptual Model resource had not been retrieved. That remains true for a full content comparison, but the new official metadata signal is now stronger and should be described accurately.

Candidate A §18 still contains two alternative Event representations: earlier Event-to-Occurrence contextual relationship and later shared Event identity/subtype proposal. The new standards evidence does not reconcile that internal inconsistency.

Candidate A's 2024-02-28 hierarchical-event citation should be corrected in a later owner-authorized canonical reconciliation to cite the 2026-10-13 guide.

### 8.2 Task 05B dictionary

Task 05B §16 still uses `SurveyTargetResult` with detected/non-detected states. Section 17.2 recommends, but does not decide, the `SurveyTargetAssessment` lifecycle split. This remains an unresolved internal domain decision.

Task 05B §16.6 treats document/list dates as if they were a uniform pin for all terms. Current evidence confirms term versions vary: `eco:Survey` and several effort/completeness terms have 2026-10-13 versions; `eco:SurveyTarget` and `eco:isSurveyTargetFullyReported` remain 2026-05-26; `dwc:occurrenceStatus` remains 2026-05-26. Its standards table therefore needs a term-by-term update, not a blanket date substitution.

Task 05B §16.3 describes a `SurveyTargetResult` that combines assessment lifecycle and outcome state. This is in tension with the EVT proposal to keep assessment/completeness separate from the canonical Occurrence-level outcome. The updated standards do not settle this internal design choice.

### 8.3 Task 05D v3

Task 05D correctly keeps DR-09 open and prohibits Task 05E/physical schema until the model and exact standards mappings are validated. Task 05D §17.1 already distinguishes `isTaxonomicScopeFullyReported` from `taxonCompletenessReported` and its protocol; retain this distinction and expand it to include the separate `isSurveyTargetFullyReported` meaning, current term versions, explicit `isAbsenceReported` semantics, bycatch and GBIF's structured-effort guidance. Task 05D must not treat `reportedComplete` as a universal GBIF §7.3 prerequisite without a separate owner policy decision.

The proposed test fixtures remain unexecuted. This standards addendum does not convert any EVT, DR, B16, B01/B02 or LDM test into Pass.

### 8.4 EVT decision pack and decision register

EVT-D01–D04 remain open. The standards findings support the preferred working direction but do not select the internal relational model. The current Survey definition reinforces the need to distinguish a designed Survey from a casual observation.

## 11. Revised finding severity and disposition

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| STD-01 | Resolved at metadata level; archive check remains | Current official Conceptual Model page identifies 2026-10-13; semantic model remains non-normative guidance and does not prescribe implementation | Archive exact versioned resource for reproducibility; do not treat it as schema mandate |
| STD-02 | Resolved at metadata/content level | Hierarchical-event guidance is 2026-10-13; Section 3 normative | Retain explicit containment, applicability and non-derivation tests |
| STD-03 | Resolved at metadata level; archive check remains | Current official Darwin Core List is 2026-10-13; individual term versions differ | Preserve exact versioned List snapshot in evidence bundle |
| STD-04 | Partially resolved | 2026-05-26 Humboldt snapshot is superseded by 2026-10-13; current List exposes 2026-10-13 term-level metadata | Full 2026-10-13 Humboldt snapshot still needs reproducible archival |
| STD-05 | Open | Current Survey term version is 2026-10-13; exact Survey term definition should be pinned and reviewed against Botanica workflows | Do not force casual observation into Survey without domain justification |
| STD-06 | Resolved at term level | `dwc:samplingEffort` and `dwc:samplingProtocol` both have 2026-10-13 term versions and Survey-scoped definitions | Preserve separate Humboldt effort value/unit/method fields and map explicitly |
| STD-07 | Resolved at term level | `dwc:occurrenceStatus-2026-05-26` recommends `detected/notDetected`; GBIF guide examples use `present/absent` | Require versioned, tested profile mapping |
| STD-08 | Open | `SurveyTargetResult` vs `SurveyTargetAssessment` and authoritative non-detection state remain unresolved | EVT-D04/B16 specialist decision |
| STD-09 | Open | Internal multiple-Survey reporting vs one Event per DwC-A Occurrence row | Decide internal identity and loss-aware export mapping |
| STD-10 | Open | Candidate A still has incompatible Event representations | Canonical ERD and cardinality reconciliation after owner approval |

## 12. Recommendations

1. Keep EVT-D01–D04 as the preferred working hypotheses for specialist validation.
2. Do not rewrite Candidate A or Task 05B yet.
3. Build a compact, pinned standards evidence bundle containing the exact 2026-10-13 Conceptual Model, hierarchical-event guide, Darwin Core List, Humboldt term list, and individual relevant term metadata. Current indexed metadata is useful but is not a substitute for preserving the exact versioned resource content.
4. Produce and approve a term-level crosswalk for `eco:Survey`, `eco:SurveyTarget`, target/excluded scopes, `eco:isSurveyTargetFullyReported`, `eco:isTaxonomicScopeFullyReported`, `eco:taxonCompletenessReported`, `eco:taxonCompletenessProtocols`, the 2026-10-13 `ecotcr` controlled vocabulary, `eco:isAbsenceReported`, bycatch completeness, sampling-effort/protocol terms and `dwc:occurrenceStatus`.
5. Review the internal definition of Survey against the updated 2026-10-13 definition. Casual observations must not be forced into Survey entities.
6. Keep the distinction between target-level completeness and taxonomic-scope completeness. They are not interchangeable.
7. Preserve ODR-01 as owner-authorized export-only policy; do not infer internal absence from missing records.
8. After the source baseline is pinned, send the specialist review brief with exact source versions and the unresolved questions.
9. Only after specialist review and explicit owner authorization should Candidate A be reconciled and Task 05B/05D synchronized.
10. Add negative tests proving that implicit export inference is suppressed for post-facto scope, incomplete target reporting, bycatch-only records, missing protocol/scope, ambiguous hierarchy, and unpinned term/profile versions.

## 13. Current status and non-actions

- DR-09: partially resolved, remains OPEN. Current official Conceptual Model and Darwin Core List identify 2026-10-13; current List exposes 2026-10-13 sampling and Humboldt term records. The full 2026-10-13 Humboldt snapshot and a reproducible standards evidence bundle still need archival.
- EVT-D01–D04: OPEN; preferred working direction only.
- Candidate A: NOT APPROVED.
- Candidate B: preserved alternative.
- Task 05B: proposed, not reconciled.
- Task 05D: PROPOSED / NOT PASSED.
- Task 05E and physical schema: NOT READY.
- ODR-01: owner-authorized export-only policy; profile validation and implementation remain pending.
- No tests were executed.
- No specialist review was obtained.
- No external party was contacted.
- No accepted ADR or product requirement was changed.
- No canonical scientific model was amended.
- No PR was merged or closed.
- No branch was created or deleted.
- No repository protection or setting was changed.
- No DDL, migration or API contract was created or frozen.

**Correction note (26 November 2026):** A fresh source check confirms that official indexed metadata reports the List issue version as 2026-10-13, but direct landing-page retrieval still renders 2026-05-26. Current core namespace term records independently verify 2026-10-13 sampling-effort and sampling-protocol term versions. The earlier direct term-version claims are superseded by the term-specific evidence in Sections 5–6. DR-09 remains open because the exact List/Humboldt versioned resources are not yet reproducibly archived. This correction does not approve any scientific decision.

**End of document — STF-BI-REV-EVT-006 v0.1, corrected 26 November 2026.**
