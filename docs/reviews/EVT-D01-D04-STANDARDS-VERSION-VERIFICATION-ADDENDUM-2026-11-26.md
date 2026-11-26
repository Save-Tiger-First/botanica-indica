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

This is a material vocabulary change for the project. The Task 05B dictionary and Candidate A must not continue to rely on older assumptions about where sampling effort/protocol terms live without a term-by-term mapping review. The exact relationship between the new core terms and any retained Humboldt terms/fields must be established from their definitions and version metadata, not guessed.

Source:
- https://dwc.tdwg.org/list/
- https://rs.tdwg.org/dwc/terms/version/occurrenceStatus-2026-05-26
- https://rs.tdwg.org/dwc/terms.htm

## 6. Humboldt Extension — term-level evidence and remaining snapshot gap

The directly opened current Humboldt terms page renders a 2026-05-26 list header. The versioned 2026-05-26 snapshot is explicitly marked superseded and says it was replaced by the 2026-10-13 snapshot. The exact 2026-10-13 full list URI could not be opened.

The following term-level facts are supported by the current official Quick Reference Guide, current indexed List results, and/or the 2026-05-26 snapshot's explicit replacement metadata:

| Term | Verified term-version position | Design relevance |
|---|---|---|
| `eco:Survey` | 2026-05-26 version is superseded by 2026-10-13 | Do not rely on old short definition without checking current one |
| `eco:SurveyTarget` | 2026-05-26 term version is recommended in the retrieved snapshot | Target describes one or more scopes for Occurrences in a Survey |
| `eco:isSurveyTargetFullyReported` | 2026-05-26 term version; recommended in retrieved term metadata | Target-level reporting completeness; not the same as taxonomic completeness |
| `eco:isTaxonomicScopeFullyReported` | 2024-02-28 version is superseded by 2026-10-13 | Pin the current version and its definition; do not use the superseded term version |
| `eco:isSamplingEffortReported` | 2024-02-28 version is superseded by 2026-10-13 | Verify how current reporting semantics interact with the new `dwc:samplingEffort` term |
| `eco:isAbsenceReported` | 2026-10-13 term version appears in the current official List result | Export completeness/absence declaration needs a pinned version |

The current Darwin Core Quick Reference Guide (a current recommended-terms aid, explicitly not itself part of the standard) defines `eco:Survey` as a `dwc:Event` intentionally designed to characterize a defined biotic target or domain so resulting `dwc:Occurrences` can be interpreted collectively to support ecological and monitoring inference, rather than merely documenting individual observations or gathered material. This is materially richer than the older `eco:Survey-2026-05-26` definition “A biotic survey or inventory.” The 2026-05-26 Humboldt snapshot marks that Survey term version superseded and points to `Survey-2026-10-13`.

The Quick Reference definition is current guidance for use, but the exact `Survey-2026-10-13` term-version record was not separately opened in this session. Pin that exact term-version IRI in the evidence bundle. The design implication is nevertheless clear enough for a requirement review: Botanica Indica should not label every casual observation or uploaded photograph a Survey. A Survey is an intentionally designed activity with an inferential purpose. Individual observations can exist without belonging to a Survey.

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

## 7. GBIF survey guide — confirmed export semantics

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

## 8. Cross-document implications

### 8.1 Candidate A — Task 05C

Candidate A §20.1 and the 21 November standards correction contain the statement that the exact 2026-10-13 Conceptual Model resource had not been retrieved. That remains true for a full content comparison, but the new official metadata signal is now stronger and should be described accurately.

Candidate A §18 still contains two alternative Event representations: earlier Event-to-Occurrence contextual relationship and later shared Event identity/subtype proposal. The new standards evidence does not reconcile that internal inconsistency.

Candidate A's 2024-02-28 hierarchical-event citation should be corrected in a later owner-authorized canonical reconciliation to cite the 2026-10-13 guide.

### 8.2 Task 05B dictionary

Task 05B §16 still uses `SurveyTargetResult` with detected/non-detected states. Section 17.2 recommends, but does not decide, the `SurveyTargetAssessment` lifecycle split. This is still an unresolved internal domain decision.

Task 05B §16.6 lists the 2026-10-13 standards pins but the exact List/term snapshots are not all directly retrievable from the current page rendering. It also needs review of the new `dwc:samplingEffort` and `dwc:samplingProtocol` terms and the updated Survey definition.

### 8.3 Task 05D v3

Task 05D correctly keeps DR-09 open and prohibits Task 05E/physical schema until the model and exact standards mappings are validated. Its standards addenda need a new evidence note reflecting the 2026-10-13 hierarchical-event guide and the precise Conceptual Model/term-list rendering discrepancy.

The proposed test fixtures remain unexecuted. This standards addendum does not convert any EVT, DR, B16, B01/B02 or LDM test into Pass.

### 8.4 EVT decision pack and decision register

EVT-D01–D04 remain open. The standards findings support the preferred working direction but do not select the internal relational model. The current Survey definition reinforces the need to distinguish a designed Survey from a casual observation.

## 9. Revised finding severity and disposition

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

## 10. Recommendations

1. Keep EVT-D01–D04 as the preferred working hypotheses for specialist validation.
2. Do not rewrite Candidate A or Task 05B yet.
3. Build a compact, pinned standards evidence bundle containing the exact 2026-10-13 Conceptual Model, hierarchical-event guide, Darwin Core List, Humboldt term list, and individual relevant term metadata. Current indexed metadata is useful but is not a substitute for preserving the exact versioned resource content.
4. Produce a term-level crosswalk for `eco:Survey`, `eco:SurveyTarget`, all relevant target-scope terms, `eco:isSurveyTargetFullyReported`, `eco:isTaxonomicScopeFullyReported`, `eco:isAbsenceReported`, `eco:isSamplingEffortReported`, `dwc:samplingEffort`, `dwc:samplingProtocol`, and `dwc:occurrenceStatus`.
5. Review the internal definition of Survey against the updated 2026-10-13 definition. Casual observations must not be forced into Survey entities.
6. Keep the distinction between target-level completeness and taxonomic-scope completeness. They are not interchangeable.
7. Preserve ODR-01 as owner-authorized export-only policy; do not infer internal absence from missing records.
8. After the source baseline is pinned, send the specialist review brief with exact source versions and the unresolved questions.
9. Only after specialist review and explicit owner authorization should Candidate A be reconciled and Task 05B/05D synchronized.

## 11. Current status and non-actions

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
