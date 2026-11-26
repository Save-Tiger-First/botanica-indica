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

## 3. Darwin Core Conceptual Model — version/content discrepancy

### 3.1 What is directly visible

The directly opened official page `https://dwc.tdwg.org/cm/` rendered:

- Date version issued: 2026-05-26
- This version: `http://rs.tdwg.org/dwc/doc/cm/2026-05-26`

Its content states that the Conceptual Model is a high-level semantic framework, does not prescribe formal predicates, does not mandate a particular implementation technology, and is not a strict system blueprint. All sections other than the document-status section are non-normative.

The current official TDWG search result for the latest Conceptual Model reports:

- Date version issued: 2026-10-13
- This version: `http://rs.tdwg.org/dwc/doc/cm/2026-10-13`
- Previous version: 2026-05-26.

However, the opened current landing page rendered the 2026-05-26 document. The separately indexed exact 2026-05-26 version page reports that it was replaced by a 2026-09-17 version, creating a further discrepancy with the current landing-page metadata that identifies 2026-10-13 as latest and 2026-05-26 as previous. The exact 2026-10-13 versioned URI could not be opened in this retrieval session. Therefore, **2026-10-13 is the latest version reported by current official search metadata, but its complete content has not been directly inspected**. The 2026-05-26 content is the version whose semantic text was directly inspected. Do not collapse these two evidence types.

### 3.2 Semantic content available from the directly opened model

The accessible Conceptual Model content says:

- Survey is a special type of Event.
- Occurrence is a special type of Event.
- A single Event must not be interpreted as simultaneously being a Survey, Occurrence and Organism Interaction.
- A Survey's results are expressed through the Occurrences it reports; these may be target-matching or bycatch.
- Survey Targets can be based on combinations of taxa, environmental conditions and organismal traits.
- Survey Targets can reflect a priori intention or post-facto filtering.
- Occurrence can represent direct observation, indirect inference or non-detection of an organism of a given taxon in a particular state during a bounded time interval and Location.
- A child Event is contained entirely within one parent spatially and temporally and has only one parent.
- A shared context Event may be a practical implementation choice for multiple activities with common spatiotemporal context.

**Important qualification:** these Conceptual Model sections are non-normative semantic guidance. They are not a mandated relational schema or SQL inheritance prescription.

### 3.3 Disposition

- Pin 2026-05-26 as the exact Conceptual Model content directly opened and inspected.
- Record 2026-10-13 as the latest issue metadata reported by the official page index, not as a content-level version comparison completed by this review.
- Obtain and archive the exact 2026-10-13 resource and compare the changed content before closing the Conceptual Model portion of DR-09.

Sources:
- https://dwc.tdwg.org/cm/
- https://dwc.tdwg.org/cm/2026-05-26.html
- https://rs.tdwg.org/dwc/doc/cm/2026-10-13
- https://dwc.tdwg.org/list/ (current indexed version metadata: 2026-10-13)
- https://dwc.tdwg.org/terms/ (current Quick Reference Guide; not itself part of the standard)

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

Current official TDWG search results identify the Darwin Core List of Terms version issued 2026-10-13, with version IRI `http://rs.tdwg.org/dwc/doc/list/2026-10-13` and previous version 2026-05-26. The opened HTML page and core-namespace terms page still rendered 2026-05-26 headers/snapshots during this session. The exact 2026-10-13 List resource was not successfully opened. Thus the latest issue/version metadata is verified as current official indexed metadata, while the full 2026-10-13 list content was not directly inspected. Current official term results do expose individual 2026-10-13 term-version IRIs and definitions. Keep the document issue date, namespace snapshot date and each term-version date separate.

### 5.1 Verified term-level pin

`dwc:occurrenceStatus`

- Term IRI: `http://rs.tdwg.org/dwc/terms/occurrenceStatus`
- Term version IRI: `http://rs.tdwg.org/dwc/terms/version/occurrenceStatus-2026-05-26`
- Definition: a statement about detection or non-detection of a `dwc:Organism` during a `dwc:Event`.
- Recommended default values: `detected` and `notDetected`.

The GBIF survey guide v1.0.2 examples use `present` and `absent`. These are not interchangeable by assumption. A specific export profile must define and test any mapping.

### 5.2 New 2026-10-13 core terms relevant to survey design

Current official term results identify:

- `dwc:samplingEffort` — term version 2026-10-13; amount of effort expended during an `eco:Survey`.
- `dwc:samplingProtocol` — term version 2026-10-13; names, references or descriptions of methods/protocols used during an `eco:Survey`.

The GBIF survey guide v1.0.2 §5.7 says `dwc:samplingEffort` is an unstructured field, while the Humboldt extension's structured fields are the recommended best practice: `eco:isSamplingEffortReported`, paired `eco:samplingEffortValue`/`eco:samplingEffortUnit`, `eco:samplingEffortProtocol`, and `eco:samplingPerformedBy`. It does not recommend replacing the structured Humboldt representation with only the free-text core term. For Botanica Indica, preserve numeric value, unit, method, responsible agent and reporting status as distinct internal facts; the external profile may serialize both structured and unstructured forms where its mapping calls for them. Do not double-count the same effort as two separate scientific facts.

The 2026-10-13 term definitions now scope both core `dwc:samplingEffort` and `dwc:samplingProtocol` specifically to an `eco:Survey`; the older cached 2026-05-26 HTML page still displays the previous Event-scoped definition for `dwc:samplingProtocol`. This is another reason to pin term-version IRIs rather than relying on cached landing-page rendering.

Source:
- https://dwc.tdwg.org/list/
- https://rs.tdwg.org/dwc/terms/version/occurrenceStatus-2026-05-26
- https://rs.tdwg.org/dwc/terms.htm

## 6. Humboldt Extension — term-level evidence and remaining snapshot gap

The official 2026-05-26 Humboldt snapshot is explicitly superseded and identifies 2026-10-13 as its replacement. The live current terms page and historical snapshot renderer still expose 2026-05-26 material; the exact full 2026-10-13 snapshot could not be opened directly. However, current official TDWG List/Quick Reference search results and the 2026-05-26 snapshot's term-replacement metadata provide term-level evidence for this provisional crosswalk. Exact current term-version pages and the complete snapshot should still be preserved in a reproducible evidence bundle before DR-09 is closed.

| Term | Current/relevant term-version evidence | Semantics and design consequence |
|---|---|---|
| `eco:Survey` | `Survey-2026-10-13` replaces `Survey-2026-05-26` | Current Quick Reference definition requires an intentionally designed Event to characterize a defined biotic target/domain for collective ecological or monitoring inference; not every observation is a Survey |
| `eco:SurveyTarget` | `SurveyTarget-2026-05-26`, recommended in retrieved snapshot | One or more scopes describing targets for Occurrences in a Survey; preserve scope type, inclusion/exclusion, hierarchy and a priori/post-facto origin |
| `eco:isSurveyTargetFullyReported` | `isSurveyTargetFullyReported-2026-05-26`, recommended | Target-specific: all detected Occurrences matching that SurveyTarget were fully reported; enables target-specific non-detection inference; not interchangeable with taxonomic-scope completeness |
| `eco:isTaxonomicScopeFullyReported` | `isTaxonomicScopeFullyReported-2026-10-13` replaces 2024-02-28 | Every detected Occurrence within the declared taxonomic scope was reported; scope is based on target and excluded taxonomic scope; reporting completeness, not proof of detectability or biological absence |
| `eco:taxonCompletenessReported` | `taxonCompletenessReported-2026-10-13` replaces 2025-07-10 | Whether taxonomic completeness was assessed; controlled values are `notReported`, `reportedComplete`, `reportedIncomplete` under the separate 2026-10-13 ecotcr vocabulary |
| `eco:taxonCompletenessProtocols` | `taxonCompletenessProtocols-2026-10-13` replaces 2025-07-10 | Method or reference used to assess taxonomic completeness; preserve independently from reporting completeness and sampling effort |
| `eco:isAbsenceReported` | `isAbsenceReported-2026-10-13` replaces 2024-02-28 | Indicates whether taxonomic absences are explicitly reported; GBIF's implicit pattern sets this false because no explicit absence Occurrence rows are created |
| `eco:isSamplingEffortReported` | `isSamplingEffortReported-2026-10-13` replaces 2024-02-28 | Whether Survey sampling effort is reported; pair with structured effort fields where applicable |
| `eco:samplingEffortValue` / `eco:samplingEffortUnit` | Current 2026-10-13 term versions replace earlier versions | Numeric amount and unit are a pair; do not infer effort for compiled data |
| `eco:samplingEffortProtocol` | Retrieved 2025-07-10 version; current status/version must be confirmed in the inaccessible 2026-10-13 snapshot | Method used to determine effort; distinct from the survey protocol |
| `eco:areNonTargetTaxaFullyReported` | Current 2026-10-13 term result | Completeness of reported non-target detections; bycatch remains outside absence inference |
| `dwc:samplingEffort` | `samplingEffort-2026-10-13` | Unstructured amount of effort expended during an eco:Survey |
| `dwc:samplingProtocol` | `samplingProtocol-2026-10-13` | Names, references or descriptions of methods/protocols used during an eco:Survey |
| `dwc:occurrenceStatus` | `occurrenceStatus-2026-05-26` | Recommended values `detected` and `notDetected`; GBIF guide examples use `present` and `absent`, requiring explicit profile mapping |

The current Darwin Core Quick Reference Guide (a current recommended-terms aid, explicitly not itself part of the standard) gives the updated `eco:Survey` definition: an Event intentionally designed to characterize a defined biotic target/domain so resulting Occurrences can be interpreted collectively for ecological and monitoring inference. The official 2026-05-26 Humboldt snapshot marks `Survey-2026-05-26` superseded and identifies `Survey-2026-10-13` as its replacement. The exact term-version page was not opened directly, but the current Quick Reference and supersession metadata agree on the substantive change.

The design implication is important: Botanica Indica should not label every casual observation, uploaded photograph or opportunistic sighting a Survey. A Survey is an intentionally designed activity with an inferential purpose. Individual observations can exist without belonging to a Survey.

### Disposition

- Do not claim the full 2026-10-13 Humboldt term list has been directly inspected; current indexed metadata and term-specific replacement records are not equivalent to a locally archived full snapshot.
- Preserve term-level version pins independently, including terms that remain on 2025-07-10 or 2026-05-26 versions.
- Retrieve and archive the exact current list snapshot and individual term metadata when the official resource is accessible.
- Reconcile the 2026-10-13 Survey definition, the new taxonomic-completeness vocabulary, sampling-effort/protocol terms and the distinct target/scope completeness flags against Task 05B, Candidate A, Task 05D and ODR-01 before modifying the canonical dictionary.

### Disposition

- Do not claim the full 2026-10-13 Humboldt term list has been directly inspected.
- Preserve term-level version pins independently.
- Retrieve the exact current list snapshot and archive it in the standards evidence bundle.
- Review the 2026-10-13 Survey definition and new sampling terms against Task 05B, Candidate A, Task 05D and ODR-01 before modifying the canonical dictionary.

Sources:
- https://rs.tdwg.org/eco/terms.htm
- https://rs.tdwg.org/eco/version/terms/2026-05-26.htm (explicitly superseded by 2026-10-13 snapshot)
- https://rs.tdwg.org/eco/version/terms/2026-10-13 (exact full snapshot could not be opened)
- https://dwc.tdwg.org/terms/ (current Quick Reference Guide, including current Survey and SurveyTarget guidance)

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
| STD-01 | Major | Current indexed metadata identifies the Conceptual Model as 2026-10-13, but the rendered page exposes 2026-05-26 and the old version page reports replacement by 2026-09-17 | Open; retrieve and compare exact versioned resources |
| STD-02 | Resolved at metadata level | Hierarchical-event guide current version is 2026-10-13; Section 3 is normative | Version/date resolved; preserve full source evidence before final compliance claim |
| STD-03 | Major | Current indexed Darwin Core List is 2026-10-13, while rendered core term page exposes 2026-05-26 | Open; capture exact 2026-10-13 List snapshot |
| STD-04 | Major | Humboldt 2026-05-26 term snapshot is explicitly superseded by 2026-10-13; current Quick Reference exposes updated Survey definition and current terms | Open; capture exact 2026-10-13 snapshot and pin terms |
| STD-05 | Major | Current Survey definition requires intentional design for ecological/monitoring inference, unlike the older short definition | Review product/domain boundary; do not classify casual observation as Survey |
| STD-06 | Major | New core `dwc:samplingEffort` and `dwc:samplingProtocol` term versions dated 2026-10-13 need crosswalk against Humboldt effort fields | Open; term-by-term crosswalk |
| STD-07 | Resolved at term level | `dwc:occurrenceStatus-2026-05-26` recommends `detected/notDetected`; GBIF examples use `present/absent` | Keep explicit profile mapping requirement |
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

- DR-09: partially resolved, remains OPEN. Current indexed metadata identifies 2026-10-13 versions for the Conceptual Model and Darwin Core List; direct rendered content and exact version resources remain inconsistent or inaccessible.
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

**End of document — STF-BI-REV-EVT-006 v0.1.**
