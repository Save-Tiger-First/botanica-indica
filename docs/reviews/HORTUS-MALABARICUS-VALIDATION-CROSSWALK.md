# Hortus Malabaricus — Scientific Model Validation Crosswalk

- **Project:** Botanica Indica — Save Tiger First
- **Document type:** Cross-document validation crosswalk
- **Version:** 0.1
- **Status:** Proposed review aid; no model approval or test execution
- **Prepared:** 21 November 2026
- **Branch:** `review/scientific-data-model-review-pack`
- **Related PR:** [PR #9](https://github.com/Save-Tiger-First/botanica-indica/pull/9)
- **Related case study:** [Hortus Malabaricus — Historical Knowledge and Provenance Case Study](HORTUS-MALABARICUS-HISTORICAL-KNOWLEDGE-PROVENANCE-CASE-STUDY.md)

> **Decision boundary:** This crosswalk maps the case study to existing Task 05B/05C/05D and scientific-review material. It does not create new domain entities, change an accepted ADR, approve Task 05C, close a blocker, authorize Task 05E, approve source ingestion or authorize use of traditional/community-held knowledge.

## 1. Executive finding

The current proposed Candidate A model already contains relevant general-purpose building blocks:

- `TaxonName`, `TaxonConcept` and `TaxonNameUsage` distinguish a name, a treatment-scoped concept and a source's usage.
- `VernacularNameAssertion` includes language, script, geographic/language context, spelling source and community attribution.
- `Agent` refers to a person, organization or software agent; public attribution is separate from authentication identity.
- `EvidenceItem` can represent physical, digital, bibliographic, measurement or testimony evidence.
- `SourceRecord`, `ProvenanceRecord` and `ProvenanceEdge` provide source identity, derivation, transformation and lineage concepts.
- `RightsRecord` distinguishes rights holder, license/permission and purpose-specific conditions, including AI-training use.

The proposed Scientific Data Dictionary also specifies language tags, vernacular-name assertions, source/agent attribution, rights records and provenance fields.

**Assessment:** The proposed model has a credible general-purpose foundation. The material reviewed does not yet demonstrate, through a complete worked fixture and executable tests, that it preserves the full chain from a named or anonymous contributor through an original-language expression, transcription/transliteration/translation, editorial transformation, historical publication and later taxonomic reconciliation.

This is a validation gap, not proof that a new `KnowledgeHolder`, `KnowledgeContribution` or `TranslationChain` entity is required. Test existing concepts first. Propose a new concept only if a reviewer identifies a specific invariant or lifecycle that cannot be represented safely and clearly with the existing model.

## 2. Exact document baseline inspected

The following source revisions were fetched for this crosswalk. Reviewers must re-fetch and record the revisions they actually assess.

| Source | Branch / PR | File blob SHA |
|---|---|---|
| AI Project Operating Prompt | `docs/repository-audit-and-ai-operating-standard` / PR #16 | `53add3894d0502827e584614c70ad09cadaa637d` |
| Candidate A — Task 05C | `docs/task-05c-logical-data-model` / PR #5 | `b447796e7da0d08d96400812667a8e67e0696144` |
| Candidate B — Task 05C alternative | `docs/task-05c-logical-database-model` / PR #21 | `239d7e9974bcb81b1154b54845a7b2d69c3775d6` |
| Task 05B Scientific Data Dictionary | `docs/task-05-data-dictionary` / PR #4 | `ddaa379d993fdf1f45684962930d16f06830ae43` |
| Scientific Data Model Validation Matrix | PR #9 | `3a33dfe47657a96456f56f2c12a0b7d355b6c6a5` |
| Event–Survey–Occurrence Decision and Validation Pack | PR #9 | `4a317c4c83317e10663ba374e9e6be3100a53431` |
| Scientific Data Model Review Pack | PR #9 | `c11f4b58d0908742474d3e58b4ec0aa3739f7b99` |
| ADR-004 — Data and Scientific Provenance | `main` | `75148aff6f8dfddfa8aa794b0cb064c62d6418a7` |
| ADR-005 — Taxonomy Reconciliation | `main` | `b61dcf0b9ba58fc35da5cc7ba5edfbdd5f2909e4` |
| ADR-007 — Evidence and Expert Validation | `main` | `7ba4874b4175707b69dc3052822f8cbeb5384b0a` |
| ADR-010 — Data Ingestion and Source Integration | `main` | `088e379513fe2c4b9471d857737f75dcdc3990cd` |

**Revision caution:** the EVT pack records historical branch-specific ADR revisions with different blob SHAs. The ADR SHAs above are the exact `main` files fetched for this crosswalk. A blob SHA from one branch must not be treated as the identity of a file on another branch. Reconcile branch-specific copies and content before any merge.

## 3. Crosswalk: case-study tests to existing coverage

| Hortus test | Existing model / decision coverage | Preliminary assessment | Evidence still required |
|---|---|---|---|
| HM-01 Original plant name, language and script | Candidate A `VernacularNameAssertion`; Task 05B language tag; ADR-004; TCS `TaxonName` | Partially covered by design | Fixture retaining exact source string, language, script, source locator, page/plate and transcription status; Unicode and alternate-script tests |
| HM-02 Translation/transliteration chain | Candidate A `ProvenanceRecord`/`ProvenanceEdge`; `EvidenceRelationship`; Task 05B transformation provenance; ADR-004 | Conceptually covered; chain semantics unproven | Multi-step fixture: source expression, transcription, transliteration, intermediate translation, published form, agent per step, time, method, input/output and uncertainty |
| HM-03 Same/related vernacular string in different contexts | `TaxonName`, `TaxonNameUsage`, `TaxonConcept`; ADR-005; LDM-01–LDM-03 | Strong conceptual coverage | Competing context-specific usages and mappings; no string-only merge |
| HM-04 Historical name mapped to modern taxon | `TaxonNameUsage`, `TaxonConceptMapping`, `ScientificAssertion`; ADR-005; B03/B04; LDM-01–LDM-03 | Strong conceptual coverage | Historical/modern treatments, mapping relation, source, evidence, agent, date, uncertainty and review outcome |
| HM-05 Named and anonymous contributors | `Agent`, `EvidenceItem`, `ProvenanceRecord`; ADR-004/007 | Partially covered; governance detail unclear | Named, collective, unknown and source-anonymized contributors; public credit separate from restricted identity; no inferred authority or consent |
| HM-06 Historical medicinal-use statement | `ScientificAssertion`, `EvidenceItem`, `EvidenceRelationship`; ADR-004/007 | Generic assertion support; semantics unproven | Source-reported historical use distinct from contemporary ethnobotanical report, pharmacological finding, clinical evidence, safety assessment and medical recommendation |
| HM-07 Historical work vs modern scan/translation/plate rights | `RightsRecord`, `MediaAsset`, `MediaDerivative`, `Source`; B08/B18; LDM-12/LDM-15; ADR-004/010 | Strong policy coverage; fixture required | Separate rights decisions for underlying work, copy, scan, translation, annotations, plate photo, derivative, video and training purpose |
| HM-08 Community governance / cultural interests | `Agent`, `RightsRecord`, `ProvenanceRecord`; community-designated reviewer; B08/B13/B18; ADR-007 | Principles present; operational representation unclear | Qualified review of authority, protocols, permissions, access, attribution preferences, benefit-sharing, withdrawal and grievance processes |
| HM-09 Conflicting expert interpretations | `ScientificAssertion`, `EvidenceRelationship`, `ExpertAssessment`, `TaxonConceptMapping`; LDM-01–LDM-03/LDM-07; ADR-005/007 | Strong conceptual coverage | Competing attributable determinations, source/treatment versions, evidence and preserved dissent |
| HM-10 Proposed model training on historical assets | `RightsRecord`, `MediaAsset`, provenance; B08/B18; ADR-004/010 | Policy fields present; enforcement unproven | Negative tests block dataset creation, preprocessing, derivative generation, embedding and training when rights are unknown, conditional or prohibited |

These are desk-review assessments, not Pass/Fail test outcomes. No fixture has been executed against an implemented schema.

## 4. Existing strengths worth preserving

### 4.1 Taxonomic identity is not a name-string lookup

TCS distinguishes TaxonConcept and TaxonName, and permits TaxonName to represent vernacular or Indigenous knowledge labels. A TaxonConcept requires a name and an according-to source/treatment. A name string alone does not establish taxonomic identity.

For a historical name such as “Mouringou”, retain the source expression and context, then record a separately sourced mapping to a modern name/concept. Do not normalize away the original expression.

The TCS List of Terms (2025-12-11) states that `taxonName` can be an informal name or Indigenous knowledge label. This does not grant rights to expose, redistribute or train on such labels or knowledge.

Official standard: https://tcs.tdwg.org/terms/

### 4.2 Generic provenance should be tested before a special-purpose schema

Candidate A proposes provenance records and directed provenance edges, including agent, source, software, time, transformation and input/output lineage. First test whether those concepts can represent a historical translation chain.

If reviewers find that transformations require structured fields not safely represented by current concepts—such as source/target language, script, transformation type, translator role, editorial intervention, confidence or attestation—document the exact failure. Only then propose a typed transformation record or other extension.

### 4.3 Knowledge contribution and scientific authority differ

A person may contribute local knowledge, collect a specimen, translate a name, prepare an illustration, transcribe a manuscript or provide a taxonomic determination. These are distinct roles.

A contribution is evidence about provenance and attribution. It does not automatically establish taxonomic authority, scientific verification or authority to authorize use on behalf of a wider community.

## 5. Potential gaps requiring reviewer determination

These are potential gaps, not approved requirements or confirmed missing entities.

### G-01 — Contribution role and attribution preferences

The Agent abstraction and provenance origin types are useful, but the reviewed model summary does not yet make explicit how named, collective, anonymous contributors, translators, scribes, collectors, artists and later editors are linked to particular statements or transformations.

Review question: can Agent + provenance + evidence relationships represent these roles and attribution preferences with clear scope, without storing unnecessary identity data?

Acceptance evidence:
- A person credited for a specific plant-knowledge statement;
- A translator credited for a particular translation step;
- An anonymous contributor remains anonymous;
- A collective attribution is retained without forcing a single person;
- Public credit is separate from restricted identity and authentication;
- A role-specific attribution can be corrected without rewriting the source record.

### G-02 — Language/script and transformation provenance

Candidate A includes language and script on vernacular assertions and transformation lineage in provenance; Task 05B uses BCP 47 language tags. It is not yet demonstrated that the model distinguishes:
- Original spoken language from manuscript language;
- Script in the source from script in later transcription;
- Verbatim source form from normalized spelling;
- Transliteration from translation and editorial normalization;
- Uncertain reading from verified transcription;
- Source/target languages and scripts;
- Responsibility and evidence for each transformation.

Review question: can existing assertion/provenance structures represent these separately, or is a typed transformation record needed?

### G-03 — Historical medicinal-use claims

Generic ScientificAssertion and EvidenceItem concepts exist, but the reviewed material does not define a dedicated semantic boundary for historical medicinal-use claims.

Review question: can a source-reported historical use be distinguished from a contemporary ethnobotanical report, pharmacological finding, clinical evidence, safety assessment or medical recommendation? If not, keep such claims outside medical functionality until a separate evidence and safety policy is reviewed.

### G-04 — Community governance is more than a RightsRecord

RightsRecord is necessary but may not be sufficient for customary authority, community protocols, collective consent, benefit-sharing, access restrictions, attribution preferences, withdrawal, grievance and governance over future use.

Review question: which controls belong in permission records, which require workflow and policy, and which should remain institutional/community governance procedures? Do not reduce a legal or community relationship to a simplistic Boolean consent field.

## 6. Recommended synthetic validation fixtures

Use synthetic fixtures only. Do not copy restricted historical knowledge or invent historical contributors. Clearly label these patterns synthetic.

| Fixture ID | Synthetic scenario | Must prove |
|---|---|---|
| HMF-01 | Historical vernacular expression with source language/script and locator | Verbatim preservation; Unicode; source/version/page/plate provenance |
| HMF-02 | Expression passed through two or more separately attributed transformations | Transformation type, input/output, language/script, agent, method, date and lineage are distinct |
| HMF-03 | Same written string in two source contexts with different candidate taxonomic mappings | No string-only identity merge; source-specific uncertainty retained |
| HMF-04 | Historical publication reports a medicinal use | Historical claim distinct from current efficacy, safety or clinical recommendation |
| HMF-05 | Named, anonymous and collective contributors appear in a source | Attribution, anonymity, role and identity/access separation |
| HMF-06 | Modern scan, transcription and translation have different rights states | Asset- and operation-specific rights; unknown rights block restricted use |
| HMF-07 | Expert changes a prior interpretation of a historical name | Prior assessment and evidence preserved; supersession and rationale recorded |
| HMF-08 | Source has a community protocol or purpose limitation | Restrictions and permitted purposes enforced downstream |

Each fixture requires an expected graph, negative assertions, source/rights assumptions, schema/API/export test, test-run evidence, reviewer and outcome. Until executed, status is **Not tested**.

## 7. Legal and governance boundaries

The Nagoya Protocol is relevant only where the facts bring an activity within its scope, including traditional knowledge associated with genetic resources. Article 7 addresses access to such knowledge with prior informed consent or approval and involvement of relevant Indigenous and local communities and mutually agreed terms, in accordance with domestic law. Article 12 addresses customary laws, community protocols and procedures and effective participation in relevant mechanisms.

Do not assume every historical plant name or seventeenth-century publication automatically falls within the Protocol's scope. Do not infer that historical public availability establishes contemporary community permission, or that one contributor's historical certificate grants modern rights for all downstream purposes.

India-specific applicability requires qualified legal review of the actual resource, knowledge, parties, purpose, access, utilization, transfer and current law. This crosswalk is not legal advice and does not establish that any permission, exemption, community mandate or benefit-sharing arrangement exists.

Official references:
- Nagoya Protocol Article 7: https://www.cbd.int/abs/text/articles?sec=abs-07
- Nagoya Protocol Article 12: https://www.cbd.int/abs/text/articles?sec=abs-12
- TCS List of Terms: https://tcs.tdwg.org/terms/
- CARE Principles for Indigenous Data Governance: https://doi.org/10.5334/dsj-2020-043

## 8. Recommended reviewer decisions

1. Do not create new domain entities yet. Execute HMF-01–HMF-08 against existing Candidate A concepts first.
2. Map the fixtures to B04, B06, B07, B08, B10, B13 and B18, and relevant LDM/TAX/rights tests, only after reviewer agreement. Preserve existing IDs; do not renumber.
3. Require a rights/privacy/community governance reviewer for G-01/G-04, a biodiversity informatician and language/script specialist for G-02, and a historian/ethnobotanist for historical-source interpretation.
4. Keep medicinal-use claims out of medical advice. If the product later includes them, define a separate evidence and safety policy first.
5. Record unresolved gaps in the existing decision register only after reviewers establish that a gap is real. Do not label a potential gap as a blocker or approved requirement prematurely.
6. Keep the wider “Indian Botanical Knowledge Heritage” resource as a future content workstream, separate from the core scientific data model, using the same rights, attribution, source and uncertainty controls.

## 9. Relationship to current project status

- ADR-004, ADR-005, ADR-007 and ADR-010 remain accepted and unchanged.
- Candidate A remains a proposed review candidate, not an approved model.
- Candidate B remains preserved as an alternative; this crosswalk does not resolve the competing-model decision.
- B04, B06, B07, B08, B10, B13 and B18 retain their existing status pending reviewer evidence.
- No HMF fixture has been implemented or executed.
- Task 05C remains NOT APPROVED.
- Task 05E remains NOT READY.
- No scans, translations, illustrations, video/audio or community-held knowledge have been ingested.
- No community consent, rights clearance or legal determination is claimed.

**Final disposition:** proposed validation aid only. It identifies where the existing model appears capable, where capability is unproven, and what evidence would be needed before proposing a model change.
