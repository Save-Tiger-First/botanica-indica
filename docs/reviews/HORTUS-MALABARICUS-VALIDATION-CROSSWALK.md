# Hortus Malabaricus — Scientific Model Validation Crosswalk

- **Project:** Botanica Indica — Save Tiger First
- **Document type:** Cross-document validation crosswalk
- **Version:** 0.1
- **Status:** Proposed review aid; no model approval or test execution
- **Prepared:** 21 November 2026
- **Branch:** `review/scientific-data-model-review-pack`
- **Related PR:** [PR #9](https://github.com/Save-Tiger-First/botanica-indica/pull/9)
- **Related case study:** [Hortus Malabaricus — Historical Knowledge and Provenance Case Study](HORTUS-MALABARICUS-HISTORICAL-KNOWLEDGE-PROVENANCE-CASE-STUDY.md)

> **Decision boundary:** This crosswalk maps the Hortus case-study questions to the existing Task 05B/05C/05D and scientific-review material. It does not create new domain entities, change an accepted ADR, approve Task 05C, close a blocker, authorize Task 05E, approve source ingestion or authorize use of traditional/community-held knowledge.

## 1. Executive finding

The current proposed Candidate A model already contains several important building blocks relevant to the case:

- `TaxonName`, `TaxonConcept` and `TaxonNameUsage` preserve distinctions between a name, a treatment-scoped concept and a source's usage.
- `VernacularNameAssertion` explicitly includes language, script, geographic/language context, spelling source and community attribution.
- `Agent` can refer to a person, organization or software agent, with public attribution kept separate from authentication identity.
- `EvidenceItem` can represent physical, digital, bibliographic, measurement or testimony evidence.
- `SourceRecord`, `ProvenanceRecord` and `ProvenanceEdge` provide source identity, derivation, transformation and lineage concepts.
- `RightsRecord` is intended to distinguish rights holder, license/permission and purpose-specific conditions, including AI-training use.

The proposed Scientific Data Dictionary also specifies language tags, vernacular-name assertions, source/agent attribution, rights records and provenance fields.

**Assessment:** The current model has a credible general-purpose foundation for representing the case. The material reviewed does not yet demonstrate, through a complete worked fixture and executable tests, that it can preserve the full chain from a named or anonymous knowledge contributor through an original-language expression, transcription/transliteration/translation, editorial transformation, historical publication and later taxonomic reconciliation.

This is a validation gap, not proof that a new `KnowledgeHolder`, `KnowledgeContribution` or `TranslationChain` entity is required. Test the existing concepts first. Introduce a new model concept only if reviewers identify a specific invariant or lifecycle that cannot be represented safely and clearly with the existing model.

## 2. Exact document baseline inspected

The following source revisions were fetched for this crosswalk. Reviewers must re-fetch and record the revisions they actually assess.

| Source | Branch / PR | File blob SHA | Use in this crosswalk |
|---|---|---|---|
| AI Project Operating Prompt | `docs/repository-audit-and-ai-operating-standard` / PR #16 | `53add3894d0502827e584614c70ad09cadaa637d` | Governing safeguards, branch policy and approval boundaries |
| Candidate A — Task 05C Logical Database Model | `docs/task-05c-logical-data-model` / PR #5 | `b447796e7da0d08d96400812667a8e67e0696144` | Candidate entities and relationships |
| Candidate B — Task 05C alternative | `docs/task-05c-logical-database-model` / PR #21 | `239d7e9974bcb81b1154b54845a7b2d69c3775d6` | Competing model context; not selected or approved |
| Task 05B Scientific Data Dictionary | `docs/task-05-data-dictionary` / PR #4 | `ddaa379d993fdf1f45684962930d16f06830ae43` | Field-level language, attribution, rights and source definitions |
| Scientific Data Model Validation Matrix and Decision Register | PR #9 | `3a33dfe47657a96456f56c2f12a0b7d355b6c6a5` | Existing LDM and blocking-decision tests |
| Event–Survey–Occurrence Decision and Validation Pack | PR #9 | `4a317c4c83317e10663ba374e9e6be3100a53431` | Historical collection/material and evidence context |
| Scientific Data Model Review Pack | PR #9 | `c11f4b58d0908742474d3e58b4ec0aa3739f7b99` | Existing model review findings |
| ADR-004 — Data and Scientific Provenance | `main` | `75148aff6f8dfddfa8aa794b0cb064c62d6418a7` | Accepted provenance principles |
| ADR-005 — Taxonomy Reconciliation | `main` | `b61dcf0b9ba58fc35da5cc7ba5edfbdd5f2909e4` | Accepted source-aware taxonomy principles |
| ADR-007 — Evidence and Expert Validation | `main` | `7ba4874b4175707b69dc3052822f8cbeb5384b0a` | Accepted evidence and review principles |
| ADR-010 — Data Ingestion and Source Integration | `main` | `088e379513fe2c4b9471d857737f75dcdc3990cd` | Accepted source-aware ingestion principles |

**Version caution:** the EVT pack contains a historical source table with different ADR blob SHAs on the review branch. The SHAs above are the exact files fetched from `main` for this crosswalk; reviewers must not treat a blob SHA from one branch as the identity of a file on another branch. Reconcile branch-specific copies and content before any merge.

## 3. Crosswalk: historical case questions to existing model coverage

| Hortus test | Existing model / decision coverage | Preliminary assessment | Evidence still required |
|---|---|---|---|
| HM-01 Original plant name, language and script | Candidate A `VernacularNameAssertion`; Task 05B language tag; ADR-004; TCS `TaxonName` | **Partially covered by design** | Fixture retaining exact source string, language tag, script, source locator, page/plate and transcription status; test Unicode and alternate script forms |
| HM-02 Translation/transliteration chain | Candidate A `ProvenanceRecord` / `ProvenanceEdge`; `EvidenceRelationship`; Task 05B transformation provenance; ADR-004 | **Conceptually covered; chain semantics unproven** | Multi-step fixture with source expression, transcription, transliteration, intermediate translation, final publication form, responsible agent per step, time, method, input/output and uncertainty |
| HM-03 Same/related vernacular string in different contexts | Candidate A `TaxonName`, `TaxonNameUsage`, `TaxonConcept`; ADR-005; LDM-01–LDM-03 | **Strong conceptual coverage** | Test context-specific name usages and competing mappings; ensure matching strings never auto-merge usages or concepts |
| HM-04 Historical name mapped to modern taxon | Candidate A `TaxonNameUsage`, `TaxonConceptMapping`, `ScientificAssertion`; ADR-005; B03/B04; LDM-01–LDM-03 | **Strong conceptual coverage** | Historical and modern treatments, mapping relation, source, evidence, asserted-by agent, date, confidence/uncertainty and reviewer outcome |
| HM-05 Named and anonymous contributors | Candidate A `Agent`, `EvidenceItem`, `ProvenanceRecord`; Observation and assertion attribution; ADR-004/007 | **Partially covered; governance detail unclear** | Test named contributor, collective contributor, unknown contributor and source-anonymized contributor; separate public credit from internal identity; do not infer authority or consent |
| HM-06 Historical medicinal-use statement | Candidate A `ScientificAssertion`, `EvidenceItem`, `EvidenceRelationship`; ADR-004/007 | **Generic assertion support; domain semantics unproven** | Test source-reported historical use with exact quotation/paraphrase locator, source date, language/translation, claim status and explicit non-equivalence to contemporary clinical efficacy |
| HM-07 Historical work vs modern scan/translation/plate rights | Candidate A `RightsRecord`, `MediaAsset`, `MediaDerivative`, `Source`; B08/B18; LDM-12/LDM-15; ADR-004/010 | **Strong policy coverage; asset-level fixture required** | Separate rights decisions for underlying work, physical copy, scan, modern translation, annotations, plate photograph, derivative, video and model-training purpose |
| HM-08 Community governance / cultural interests | Candidate A `Agent`, `RightsRecord`, `ProvenanceRecord`; community-designated reviewer; B08/B13/B18; ADR-007 | **Principles present; operational representation unclear** | Qualified legal/community review of authority, permissions, customary protocols, access restrictions, attribution preferences, benefit-sharing, withdrawal and grievance workflows where applicable |
| HM-09 Conflicting expert interpretations | Candidate A `ScientificAssertion`, `EvidenceRelationship`, `ExpertAssessment`, `TaxonConceptMapping`; LDM-01–LDM-03 and LDM-07; ADR-005/007 | **Strong conceptual coverage** | Two competing, attributable determinations with source/treatment versions, evidence and preserved dissent; no destructive overwrite |
| HM-10 Proposed model training on historical assets | Candidate A `RightsRecord`, `MediaAsset`, provenance; B08/B18; ADR-004/010 | **Policy fields present; enforcement unproven** | Negative tests proving unknown/conditional/prohibited training permission blocks dataset creation, preprocessing, derivative generation, embedding and training pipeline use |

These are desk-review assessments, not Pass/Fail test outcomes. No fixture has been executed against an implemented schema.

## 4. Existing strengths worth preserving

### 4.1 Taxonomic identity is not a name-string lookup

TCS distinguishes TaxonConcept and TaxonName, and permits a TaxonName to represent vernacular or Indigenous knowledge labels. A TaxonConcept requires a name and an according-to source/treatment. The standard does not say that a name string alone establishes taxonomic identity.

This is a good fit for historical names such as “Mouringou”: retain the source expression and context, then record a separately sourced mapping to a modern name/concept. Do not normalize away the original expression.

The current TCS List of Terms (2025-12-11) states that `taxonName` can be an informal name or Indigenous knowledge label; it also explains that TCS's `TaxonName` can be used for different name types. The standard itself does not grant rights to expose, redistribute or train on such labels.

Official standard: https://tcs.tdwg.org/terms/

### 4.2 Generic provenance is preferable to a premature special-purpose schema

Candidate A already proposes provenance records and directed provenance edges, including agent, source, software, time, transformation and input/output lineage. A first test should represent the historical translation chain using those concepts.

If a reviewer finds that each transformation requires structured fields that cannot be represented without ambiguous free text—for example, source/target language, script, transformation type, translator role, editorial intervention, confidence or attestation—document the exact failure. Only then propose an explicit transformation sub-type or entity.

### 4.3 Knowledge contribution and scientific authority are different

A person may contribute local knowledge, collect a specimen, translate a name, prepare an illustration, transcribe a manuscript or provide a taxonomic determination. These are different roles and must not be collapsed into a generic “expert” label.

A knowledge contribution is evidence about provenance and authorship. It does not automatically establish that the contributor is a taxonomic authority, that the statement is scientifically verified, or that the contributor can authorize use on behalf of a wider community.

## 5. Potential model gaps requiring reviewer determination

The following are **potential gaps**, not approved requirements or confirmed missing entities.

### G-01 — Contribution role and attribution preferences

The current Agent abstraction and provenance origin types are useful, but the reviewed model summary does not yet make explicit how a source's named contributors, collective contributors, anonymous contributors, translators, scribes, collectors, artists and later editors are each linked to particular knowledge statements or transformations.

Review question: can existing Agent + provenance + evidence relationships represent these roles and attribution preferences with clear scope, without storing unnecessary identity data?

Acceptance evidence:
- One person credited for a specific plant-knowledge statement;
- One translator credited for a particular translation step;
- An anonymous contributor preserved as anonymous, without invented identity;
- A collective attribution retained without forcing a single person;
- Public credit separated from restricted identity and authentication;
- A role-specific attribution can be corrected without rewriting the source record.

### G-02 — Language/script and transformation provenance

Candidate A includes language and script on vernacular assertions and transformation lineage in provenance. The data dictionary also uses BCP 47 language tags. It is not yet demonstrated that the model can distinguish:
- Original spoken language vs language of a manuscript;
- Script used in the source vs script used in a later transcription;
- Verbatim source form vs normalized spelling;
- Transliteration vs translation vs editorial normalization;
- Uncertain reading vs verified transcription;
- Source-language and target-language identifiers;
- Responsibility and evidence for each transformation.

Review question: can these be recorded with existing assertion/provenance structures, or is a typed transformation record required?

### G-03 — Historical medicinal-use claims

The model has generic ScientificAssertion and EvidenceItem concepts, but the reviewed material does not define a dedicated controlled semantic boundary for historical medicinal-use claims.

Review question: can a source-reported historical use be distinguished from a contemporary ethnobotanical report, pharmacological finding, clinical evidence, safety assessment or medical recommendation? If not, keep such claims outside public health/medical functionality until a separate reviewed vocabulary and evidence policy exists.

### G-04 — Community governance is more than a RightsRecord

RightsRecord is necessary but may not be sufficient for customary authority, community protocols, collective consent, benefit-sharing, access restrictions, attribution preference, withdrawal, grievance and governance over future use.

Review question: which controls belong in rights/permission records, which require workflow and policy, and which should remain outside the domain model as institutional/community governance procedures? Do not turn a legal or community relationship into a simplistic Boolean consent field.

## 6. Recommended synthetic validation fixtures

Create only synthetic fixtures for model validation. Do not copy restricted historical knowledge or create fictitious historical contributors. The fixture descriptions below are abstract patterns and must be clearly labelled synthetic.

| Fixture ID | Synthetic scenario | Must prove |
|---|---|---|
| HMF-01 | One historical vernacular expression with a source language/script and a source locator | Verbatim preservation; Unicode; source/version/page/plate provenance |
| HMF-02 | One expression passed through two or more separately attributed transformations | Each transformation's type, input/output, language/script, agent, method, date and lineage are distinct |
| HMF-03 | Same written string occurs in two source contexts with different candidate taxonomic mappings | No string-only identity merge; source-specific uncertainty retained |
| HMF-04 | A historical publication cites a medicinal use | Historical source claim remains distinct from current efficacy, safety or clinical recommendation |
| HMF-05 | One named, one anonymous and one collective contributor appear in a historical source | Correct attribution, anonymity, role and identity/access separation |
| HMF-06 | A modern scan, transcription and translation have different rights states | Each asset and operation has independent rights; unknown rights block restricted use |
| HMF-07 | An expert changes a prior interpretation of a historical name | Prior assessment and evidence preserved; supersession and rationale recorded |
| HMF-08 | A source has a community protocol or purpose limitation | Access/use restrictions and permitted purposes enforced in every relevant downstream operation |

Each fixture requires: expected graph, negative assertions, source and rights assumptions, schema/API/export test, test-run evidence, reviewer and outcome. Until executed, status is **Not tested**.

## 7. Legal and governance boundaries

The Nagoya Protocol is relevant only where the facts bring the activity within its scope, including traditional knowledge associated with genetic resources. Article 7 addresses access to such knowledge with prior informed consent or approval and involvement of the relevant Indigenous and local communities and mutually agreed terms, in accordance with domestic law. Article 12 addresses customary laws, community protocols and procedures and effective participation in relevant mechanisms.

Do not assume every historical plant name or every seventeenth-century publication automatically falls within the Protocol's scope. Do not infer that historical public availability establishes contemporary community permission, nor that one contributor's historical certificate grants modern rights for all downstream purposes.

India-specific applicability requires qualified legal review of the actual resource, knowledge, parties, purpose, access, utilization, transfer and current law. This crosswalk is not legal advice and does not establish that any permission, exemption, community mandate or benefit-sharing arrangement exists.

Official references:
- Nagoya Protocol Article 7: https://www.cbd.int/abs/text/articles?sec=abs-07
- Nagoya Protocol Article 12: https://www.cbd.int/abs/text/articles?sec=abs-12
- TCS List of Terms: https://tcs.tdwg.org/terms/
- CARE Principles for Indigenous Data Governance: https://doi.org/10.5334/dsj-2020-043

## 8. Recommended reviewer decisions

1. **Do not create new domain entities yet.** First execute HMF-01–HMF-08 against the existing Candidate A concepts.
2. **Add the fixtures to the validation plan only after reviewer agreement.** Map them to B04, B06, B07, B08, B10, B13 and B18, plus the existing LDM/TAX/rights cases where applicable. Preserve the existing identifiers; do not silently renumber.
3. **Require a rights/privacy/community governance reviewer** for G-01 and G-04, and a biodiversity informatician plus language/script specialist for G-02. A historian/ethnobotanist is also needed to assess the historical source interpretation.
4. **Keep medicinal-use claims out of medical advice.** If the product later includes medicinal-use information, define a separate evidence and safety policy before user-facing claims.
5. **Record unresolved gaps in the existing decision register** only after the responsible reviewers determine that a gap is real. Do not label a potential gap as a blocker or an approved requirement prematurely.
6. **Keep the wider Indian Botanical Knowledge Heritage resource as a future content workstream**, separate from the core scientific data model. It should use the same rights, attribution, source and uncertainty controls.

## 9. Relationship to current project status

- ADR-004, ADR-005, ADR-007 and ADR-010 remain accepted and unchanged.
- Candidate A remains a proposed review candidate, not an approved model.
- Candidate B remains preserved as an alternative; this crosswalk does not resolve the competing-model decision.
- B04, B06, B07, B08, B10, B13 and B18 retain their existing status pending reviewer evidence.
- No HMF fixture has been implemented or executed.
- Task 05C remains NOT APPROVED.
- Task 05E remains NOT READY.
- No source assets, scans, translations, illustrations, video/audio or community-held knowledge have been ingested.
- No community consent, rights clearance or legal determination is claimed.

**Final disposition:** this crosswalk is a proposed validation aid. It identifies where the existing model appears capable, where capability is unproven, and what evidence would be needed before proposing a model change.
