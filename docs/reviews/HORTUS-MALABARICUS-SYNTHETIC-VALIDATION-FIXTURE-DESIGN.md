# Hortus Malabaricus — Synthetic Validation Fixture Design

- **Project:** Botanica Indica — Save Tiger First
- **Document type:** Proposed synthetic scientific-model validation specification
- **Version:** 0.1
- **Status:** Proposed; design only; no fixture executed; no model approval
- **Prepared:** 21 November 2026
- **Branch:** `review/scientific-data-model-review-pack`
- **Related PR:** [PR #9](https://github.com/Save-Tiger-First/botanica-indica/pull/9)
- **Predecessor:** [Hortus Malabaricus — Historical Knowledge and Provenance Case Study](HORTUS-MALABARICUS-HISTORICAL-KNOWLEDGE-PROVENANCE-CASE-STUDY.md)
- **Crosswalk:** [Hortus Malabaricus — Scientific Model Validation Crosswalk](HORTUS-MALABARICUS-VALIDATION-CROSSWALK.md)

> **Strict boundary:** All records, people, source documents, names, statements, permissions, protocols, mappings and outputs described as fixture data below are synthetic test inputs. They are not historical facts, real plant knowledge, real community positions, actual permissions, or real biodiversity observations. Do not populate these fixtures with content copied from *Hortus Malabaricus*, contemporary community-held knowledge, restricted archives, real personal data or unlicensed images. This document does not approve Candidate A, resolve Candidate B, amend an accepted ADR, authorize Task 05E, authorize source ingestion, or establish any rights or legal status.

## 1. Purpose

This specification turns the eight proposed HMF validation patterns into reproducible, reviewable fixture designs. Its purpose is to test whether the existing Candidate A logical model and Task 05B dictionary can preserve:

1. Original source expressions, language, script and transcription uncertainty.
2. A multi-step, separately attributable transformation chain.
3. Context-specific vernacular-name usages and taxonomic mappings.
4. A historical-use statement without turning it into contemporary medical evidence.
5. Named, anonymous, unknown and collective contribution attribution.
6. Asset-specific rights and purpose-specific permission enforcement.
7. Competing taxonomic interpretations and immutable review history.
8. Community-governed access and purpose restrictions.

The design follows the preceding case study and crosswalk. It is a test plan, not a claim that the model has passed these tests.

## 2. Status and design principles

### 2.1 Current status

| Item | Status |
|---|---|
| Eight HMF fixture specifications | Proposed in this document |
| Synthetic input records | Not yet instantiated in a test repository or test database |
| Candidate A model review | In progress; not approved |
| Candidate B comparison | Preserved as an alternative; not resolved here |
| Physical schema / DDL | Not authorized; Task 05E remains NOT READY |
| Automated test execution | None |
| Independent specialist sign-off | None |
| Source ingestion / community knowledge collection | Not authorized by this document |

### 2.2 Design principles

- **Synthetic means synthetic:** use clearly artificial identifiers and content. Never make a synthetic record resemble an actual historical certificate, contributor, herbarium accession, community protocol or taxonomic determination.
- **Preserve source form:** retain source-exact text separately from normalized, transliterated, translated, OCR-corrected or editorial forms.
- **Do not infer missing facts:** unknown language, author, date, permission, taxonomic identity or community authority remains unknown.
- **Separate people and roles:** contribution, translation, collection, illustration, editing, taxonomic determination and permission authority are not interchangeable.
- **Separate claims and evidence:** a historical source reporting a use is not proof of current efficacy or safety.
- **Separate assets and rights:** a publication, physical copy, scan, plate image, translation, transcription and derivative may have different rights and conditions.
- **Preserve disagreement:** competing interpretations remain attributable and reviewable; no forced consensus.
- **Fail closed:** unknown or ambiguous rights/access authority blocks the affected restricted operation.
- **No automatic model expansion:** first test existing `Agent`, `EvidenceItem`, `ScientificAssertion`, `VernacularNameAssertion`, `SourceRecord`, `ProvenanceRecord`, `ProvenanceEdge`, `RightsRecord`, `MediaAsset`, `MediaDerivative`, `TaxonNameUsage` and `TaxonConceptMapping` concepts.
- **Do not create duplicate state:** no separate mutable copy of a scientific or rights outcome unless its relationship and derivation are explicitly defined.

## 3. Source baseline and consistency audit

The following files were re-fetched before preparing this specification. Blob SHAs identify the exact file content, not the branch tip.

| Source | Ref | Blob SHA |
|---|---|---|
| AI Project Operating Prompt | `docs/repository-audit-and-ai-operating-standard` / PR #16 | `53add3894d0502827e584614c70ad09cadaa637d` |
| Hortus historical case study | `review/scientific-data-model-review-pack` / PR #9 | `fb51670cab36eb9cbe22ab50b48294fb31f9b35b` |
| Hortus validation crosswalk | `review/scientific-data-model-review-pack` / PR #9 | `6b7fd454795607b3e93cc590e7ffa562884c0a9e` |
| Scientific Data Model Validation Matrix and Decision Register | `review/scientific-data-model-review-pack` / PR #9 | `3a33dfe47657a96456f56c2f12a0b7d355b6c6a5` |
| Candidate A — Task 05C Logical Database Model | `docs/task-05c-logical-data-model` / PR #5 | `b447796e7da0d08d96400812667a8e67e0696144` |
| Task 05B Scientific Data Dictionary and Indian Test Cases | `docs/task-05-data-dictionary` / PR #4 | `ddaa379d993fdf1f45684962930d16f06830ae43` |
| ADR-004 — Data and Scientific Provenance | `main` | `75148aff6f8dfddfa8aa794b0cb064c62d6418a7` |
| ADR-005 — Taxonomy Reconciliation | `main` | `b61dcf0b9ba58fc35da5cc7ba5edfbdd5f2909e4` |
| ADR-007 — Evidence and Expert Validation | `main` | `7ba4874b4175707b69dc3052822f8cbeb5384b0a` |
| ADR-010 — Data Ingestion and Source Integration | `main` | `088e379513fe2c4b9471d857737f75dcdc3990cd` |

The operating prompt is the required PR #16 branch version. Its branch policy, approval boundaries, scientific safeguards and rights/privacy principles apply.

### 3.1 Existing model capabilities used as test candidates

Candidate A describes:

- `Agent` as a stable reference to a person, organisation or software agent; authentication identity is separate and public attribution remains distinct.
- `VernacularNameAssertion` as a taxon/name assertion with language, script, geographic/language context, spelling source and community attribution.
- `ScientificAssertion` as a sourced claim with typed subject links, predicate/value, source, agent, time, review status and provenance.
- `EvidenceItem` and `EvidenceRelationship` for source evidence and support/contradiction/qualification/citation relationships.
- `RightsRecord` for rights holder, license/permission, attribution, purpose conditions, AI/ML permissions and evidence.
- `ProvenanceRecord` and `ProvenanceEdge` for origin, agent, software, time, derivation, transformation and input/output lineage.
- `TaxonNameUsage` and `TaxonConceptMapping` for source-specific name use and explicit concept comparison.

These concepts appear relevant. The tests must establish whether their detailed relationships and constraints are sufficient. This document does not assume that a proposed field or relationship is already implemented.

### 3.2 Existing validation-register links

Use existing decision IDs and test IDs; do not renumber them.

| HMF fixture | Existing review links to consider | Why |
|---|---|---|
| HMF-01 | B04, B07, B10; HM-01 | Source-specific vernacular expression, source record separation and historical versioning |
| HMF-02 | B06, B07, B10; HM-02 | Transformation activities, evidence, agent attribution and lineage |
| HMF-03 | B04, B06, B10; LDM-01, LDM-03; HM-03/HM-04 | Source-specific usages, concept mapping and competing interpretations |
| HMF-04 | B06, B07, B10; HM-06 | Historical source assertion and evidence semantics |
| HMF-05 | B07, B13; HM-05 | Attribution, source lineage, anonymity and identity/retention controls |
| HMF-06 | B08, B13, B18; LDM-12, LDM-15; HM-07/HM-10 | Rights granularity, derived assets, retention and purpose-specific use |
| HMF-07 | B04, B06, B10; LDM-01, LDM-03, LDM-07; HM-04/HM-09 | Competing treatments, evidence and supersession |
| HMF-08 | B08, B13, B18; HM-08/HM-10 | Community protocols, access, purpose limitation, withdrawal and downstream enforcement |

The links above are proposed traceability. They do not mean any existing decision is closed or any existing test has passed. Where a validation-register case is not yet an executable fixture, it remains **Not tested**.

## 4. Common fixture package structure

Each HMF fixture package should be a self-contained directory or equivalent test resource containing:

1. `README.md` — fixture purpose, synthetic-data declaration, assumptions, dependencies and run instructions.
2. `input/` — synthetic source records, statements, assets and rights/policy inputs.
3. `expected/` — expected conceptual graph and allowed output views.
4. `negative/` — forbidden relationships, operations and outputs.
5. `tests/` — deterministic test definitions and assertions.
6. `evidence/` — actual run output, logs, environment, software revision and reviewer record.
7. `manifest` — fixture ID, version, checksum, creation date, dependencies and synthetic-data flag.

Do not create this package in the production database. A future test implementation should use an isolated test environment with no external publication or public search indexing.

### 4.1 Minimum reproducibility metadata

Every run must record:

- Fixture ID and fixture version.
- Source document paths and blob SHAs.
- Candidate/model revision and commit SHA.
- Test harness and dependency versions.
- Database/schema/API version if and when implemented.
- Exact command or procedure.
- Expected result and actual result.
- Output/log references and checksums.
- Reviewer name or designated reviewer identifier, discipline, qualification scope and conflict declaration where applicable.
- Date and outcome.
- Known limitations and follow-up actions.

### 4.2 Outcome vocabulary

Use the existing validation-register outcome vocabulary:

- Pass
- Pass with condition
- Fail
- Not tested
- Not applicable
- Needs domain decision

A design review alone is not a test execution. Until a reproducible run exists, outcome is **Not tested**.

## 5. Fixture specifications

## HMF-01 — Original expression, language, script and source locator

**Objective:** prove that an original source expression can be preserved without being replaced by a normalized, transliterated, translated or taxonomically interpreted value.

**Synthetic setup:**

- Create one fictional source record, `SYN-SRC-HMF01`, with a fictional publication/version and a fictional page/plate locator.
- Create one synthetic vernacular-name expression. Its language is declared as Malayalam only because the fixture is testing a hypothetical Malayalam-language source. Do not claim this string appears in *Hortus Malabaricus*.
- Use the Malayalam Unicode character `ക` (U+0D15) as a script-preservation sentinel only. It is a character-level test value, not a plant name, translation or historical quotation.
- Record the script as Malayalam script (`Mlym`) and use a valid BCP 47 language tag where the language/script combination is supported by the registry. If source language is genuinely unknown in a separate negative case, leave it unknown rather than guessing.
- Add a separate synthetic normalized/transliterated representation, each explicitly marked as a derived form with its own provenance. Do not imply the forms are linguistically equivalent unless the fixture supplies an explicit test mapping.

**Candidate concepts to exercise:** `SourceRecord`, `VernacularNameAssertion`, `EvidenceItem`, `Agent`, `ProvenanceRecord`, `ProvenanceEdge`, and `TaxonName` only if a name object is semantically justified.

**Expected behaviour:**

1. Preserve the exact source string and its code-point sequence.
2. Retain source identity/version, page/plate locator, retrieval/creation context and transcription status.
3. Keep language and script as separate metadata dimensions; do not infer script from language alone.
4. Keep verbatim form, normalized comparison form, transliteration and translation as distinct values or linked derived records.
5. Record who transcribed or normalized the expression, which method/version was used, and which input generated each output.
6. Retain uncertain or illegible characters as uncertainty, not guessed substitutions.
7. Permit a source expression to exist without an asserted TaxonConcept mapping.

**Positive assertions:**

- Original source string remains retrievable byte-for-byte/code-point-for-code-point.
- Any normalized comparison key is explicitly derived and linked to the original.
- A corrected transcription creates a new version/assertion or auditable correction; it does not erase the source reading.
- Missing language metadata does not prevent retaining the original string, where the source itself is usable.

**Negative assertions:**

- No automatic replacement of the original with NFC/NFD/NFKC/NFKD output.
- No destructive transliteration or translation overwrite.
- No automatic taxon assignment from string similarity.
- No silent conversion of uncertain characters into a plausible word.
- No false assertion that the sentinel character is an attested historical plant name.

**Technical review note:** Unicode normalization is useful for comparison, but compatibility normalization can remove distinctions. Preserve source-exact text and treat normalized values as derived representations. Unicode's guidance identifies NFC as a suitable general form and warns that NFKC/NFKD remove compatibility distinctions. The chosen comparison policy must be documented and tested rather than applied destructively.

**Required reviewers:** Malayalam language/script specialist, biodiversity informatician, data architect.

**Existing links:** B04, B07, B10; HM-01.

## HMF-02 — Multi-stage transcription, transliteration and translation provenance

**Objective:** prove that a chain of transformations can be represented as distinct activities with explicit input/output, agents, methods and uncertainty.

**Synthetic setup:**

Create a wholly fictional chain with identifiers:

- `SYN-TEXT-ORIGINAL` — synthetic source expression in a Malayalam-script source context.
- `SYN-TEXT-TRANSCRIPTION` — a transcription output.
- `SYN-TEXT-TRANSLITERATION` — a transliteration output.
- `SYN-TEXT-PT` — a hypothetical Portuguese translation output.
- `SYN-TEXT-NL` — a hypothetical Dutch translation output.
- `SYN-TEXT-LA` — a hypothetical Latin-language editorial output.

These stages are a synthetic stress-test sequence inspired by the case-study's multilingual mediation. They are **not** a claim that every *Hortus Malabaricus* entry followed this exact sequence, nor that any specific surviving plant entry passed through every stage.

Use separate synthetic Agents for each known transformation role. Leave a responsible agent unknown where the fixture says the source does not identify one.

**Candidate concepts to exercise:** `Agent`, `EvidenceItem`, `SourceRecord`, `ProvenanceRecord`, `ProvenanceEdge`, `ScientificAssertion` where a transformation makes or changes an assertion, and `VernacularNameAssertion` where a source name is asserted.

**Expected behaviour:**

1. Every transformation is represented as a distinct activity or provenance event.
2. Each activity identifies its input and output entities, transformation type, responsible agent where known, method/tool/version, timestamp or date precision, and uncertainty/limitations.
3. Transcription, transliteration, translation and editorial normalization are not collapsed into one generic “translation”.
4. The output retains lineage to the original source expression.
5. One stage can be corrected or superseded without rewriting prior source evidence or erasing the previous output.
6. If an intermediate stage is unknown or unrecorded, the system records a gap; it does not invent the missing stage.

**Positive assertions:**

- The full directed chain is traversable from final output to original source.
- Each stage's agent/role is scoped to that activity, not generalized to authorship of the entire work.
- Each output's provenance identifies the actual input used.
- The chain can express a translator, editor, transcriber or tool as separate responsible agents/roles.

**Negative assertions:**

- No direct final-to-original derivation that hides known intermediate steps.
- No cycle in the provenance graph.
- No attribution of every stage to the best-known historical figure by default.
- No claim that transliteration is translation.
- No conversion of uncertain dates into exact timestamps.
- No universal translation chain applied to all entries.

**Required reviewers:** language/script specialist, historian of science or historical bibliography specialist, provenance/data architect.

**Existing links:** B06, B07, B10; HM-02.

## HMF-03 — Same written expression, distinct source contexts and candidate taxa

**Objective:** prove that name-string equality does not merge source-specific usages or establish taxonomic identity.

**Synthetic setup:**

- Create two fictional sources, `SYN-SRC-HMF03-A` and `SYN-SRC-HMF03-B`.
- Each contains the same synthetic string, `SYN-VERNACULAR-01`.
- Give the two usages different source contexts (for example, distinct fictional region/time/source treatments) without naming a real community or claiming an actual vernacular equivalence.
- Create two separate candidate TaxonConcepts with their own according-to resources, or leave one/both unresolved if the evidence does not support a concept.
- Add competing, explicitly provisional mappings only where the synthetic scenario supplies evidence.

**Candidate concepts to exercise:** `TaxonName`, `TaxonNameUsage`, `TaxonomicTreatment` or equivalent resource, `TaxonConcept`, `TaxonConceptMapping`, `ScientificAssertion`, `EvidenceItem`.

**Expected behaviour:**

1. The same string may be represented as one shared label object or as distinct context-specific name records, depending on the selected identity rules; in either case, the separate source usages must remain distinct and traceable.
2. Each usage points to its own source/treatment and locator.
3. Taxonomic concepts remain treatment-scoped; each TCS TaxonConcept has a name and an according-to resource.
4. A mapping between concepts uses a valid, evidence-backed TCS mapping relation and a source/according-to context.
5. If evidence is insufficient, mapping remains unresolved/proposed rather than being inferred from string equality.

**Positive assertions:**

- Both source usages are retrievable independently.
- The system can display a shared string with separate contexts and different mapping states.
- Source-specific status and verbatim wording remain intact.
- Competing mappings can coexist with rationale and review state.

**Negative assertions:**

- No deduplication solely on normalized name string.
- No automatic accepted-name field written globally to TaxonName.
- No conversion of an unresolved mapping into synonymy.
- No mapping without source context, relation and evidence where required.
- No forced consensus between treatments.

**Required reviewers:** taxonomist, biodiversity informatician, regional flora specialist.

**Existing links:** B04, B06, B10; LDM-01, LDM-03; HM-03/HM-04.

## HMF-04 — Historical-use statement versus modern efficacy or safety claim

**Objective:** prove that a source-reported historical use is stored as a historically attributed claim, not as validated pharmacology, clinical evidence, safety advice or a medical recommendation.

**Synthetic setup:**

- Create a fictional publication/source `SYN-SRC-HMF04`.
- Create a fictional plant placeholder `SYN-PLANT-Q` and fictional historical-use statement `SYN-USE-CLAIM-01`.
- The statement must use abstract fictional wording only; it must not name a real medicinal plant, disease, preparation or dosage.
- Attach a source locator and a synthetic transcription/translation provenance chain.
- Add separate synthetic evidence records representing (a) the historical statement, (b) a later scholarly commentary, and (c) a hypothetical modern laboratory/clinical record. Keep the latter separate and do not invent a real study.

**Candidate concepts to exercise:** `ScientificAssertion`, `EvidenceItem`, `EvidenceRelationship`, `SourceRecord`, `Agent`, `ProvenanceRecord`, and review-state handling.

**Expected behaviour:**

1. The assertion is typed/labeled as a historical source-reported use, if the controlled vocabulary supports it; otherwise record the need for vocabulary review rather than inventing a production code.
2. The original source statement, translation and later interpretation remain distinct.
3. Evidence relationships distinguish “cites”, “supports”, “qualifies” and “contradicts” where semantically appropriate.
4. A historical claim does not become a pharmacological or clinical efficacy assertion by association.
5. A separate modern scientific assertion requires its own evidence, source, scope, method and expert review.

**Positive assertions:**

- A public view, if ever approved, labels the claim as historical and source-attributed.
- A researcher can trace the wording back through translation/transcription to its source locator.
- A later scientific study does not overwrite the historical source statement.
- The system can represent “historically reported; contemporary efficacy not assessed” without implying either efficacy or inefficacy.

**Negative assertions:**

- No recommendation, dosage, treatment advice or safety statement generated from the historical source alone.
- No inferred clinical validation.
- No conflation of traditional use, pharmacological activity and clinical effectiveness.
- No AI-generated expansion presented as source text.
- No public health claim without separately approved evidence and safety policy.

**Required reviewers:** ethnobotanist/historian, pharmacognosy or medicinal-plant researcher, scientific evidence reviewer, product safety reviewer.

**Existing links:** B06, B07, B10; HM-06.

## HMF-05 — Named, anonymous, unknown and collective contributors

**Objective:** prove that contribution attribution can be retained accurately without inventing identity, overstating authority or exposing private identity.

**Synthetic setup:**

Create one synthetic source containing four distinct contribution patterns:

1. `SYN-PERSON-01` — a named fictional contributor associated with one specific knowledge statement.
2. An explicitly anonymous contributor — the source states that a contributor is anonymous, but no identity is recorded.
3. An unknown contributor — the source does not say whether the contributor was a person, group or intermediary.
4. `SYN-COLLECTIVE-01` — a fictional collective contributor attributed to one defined activity or statement.

Add separate fictional agents for a translator, transcriber, illustrator and taxonomic reviewer. Do not assume they are the same person or share authority.

**Candidate concepts to exercise:** `Agent`, `EvidenceItem`, `ScientificAssertion`, `ProvenanceRecord`, `ProvenanceEdge`, source attribution and identity/access controls.

**Expected behaviour:**

1. Attribution is scoped to a particular source statement, contribution or transformation.
2. “Anonymous” (explicitly anonymous in the source) is distinguished from “unknown” (not established by available evidence).
3. Collective attribution is preserved without forcing an individual identity.
4. Public credit preference is separate from private identity and account authentication.
5. A contributor's role is not automatically treated as taxonomic authority, community representative or rights holder.
6. A source's statement that someone contributed does not prove their consent to modern reuse.
7. Correction of an attribution is auditable and does not rewrite the original source.

**Positive assertions:**

- Named and collective attributions remain source-backed.
- Anonymous identity remains undisclosed.
- Unknown identity remains unknown without a fabricated Agent.
- Separate transformation agents are correctly linked to separate activities.
- The public display can omit or generalize attribution where the source or governance requires it.

**Negative assertions:**

- No guessed or reconstructed personal identity.
- No linking a historical contributor to a modern account holder.
- No inference of consent, ownership, authority or endorsement from attribution.
- No forced conversion of a collective into a single person.
- No storing unnecessary sensitive identity data.

**Required reviewers:** historian, privacy/data-governance reviewer, community-governance specialist where relevant, data architect.

**Existing links:** B07, B13; HM-05.

## HMF-06 — Asset-by-asset rights and purpose-specific operations

**Objective:** prove that the rights state of one asset is not inherited blindly by other assets, and that unknown or restricted rights block the relevant downstream operation.

**Synthetic setup:**

Create a fictional publication bundle with these separate assets:

- `SYN-ASSET-WORK` — underlying historical-work record.
- `SYN-ASSET-COPY` — a particular physical copy's bibliographic/holding record.
- `SYN-ASSET-SCAN` — a hypothetical digital scan.
- `SYN-ASSET-PLATE` — a hypothetical plate image derived from the scan.
- `SYN-ASSET-TRANSLATION` — a hypothetical modern translation.
- `SYN-ASSET-TRANSCRIPT` — a hypothetical transcription/OCR output.
- `SYN-ASSET-DERIVATIVE` — a synthetic derivative prepared from one of the above.

Give each asset its own synthetic rights evidence and status. Example test conditions may include unknown, display-only permission, conditional permission, permission for a narrowly stated research purpose, redistribution prohibited, or AI training prohibited. These are fixture labels only; map them to the approved RightsRecord vocabulary and policy before implementation. Do not infer any real *Hortus Malabaricus* rights status.

**Candidate concepts to exercise:** `RightsRecord`, `MediaAsset`, `MediaDerivative`, `Source`, `Dataset`, `DatasetVersion`, `ProvenanceRecord`, operation-level authorization.

**Operations to test independently:**

- View metadata/citation.
- Retrieve or store source payload.
- Display full text/image.
- Generate transcription/OCR.
- Translate or create derivative.
- Download.
- Redistribute.
- Commercial reuse.
- Create embeddings/indexed representations.
- Use for model training/fine-tuning/evaluation.

**Expected behaviour:**

1. Rights attach to the relevant asset or dataset and rights evidence, not merely to the bundle's top-level source.
2. The effective permission is evaluated for the exact asset, operation, purpose, audience, territory, duration and conditions.
3. A derivative has a traceable parent and its own applicable rights assessment; permission does not automatically broaden through derivation.
4. Unknown or pending rights block the relevant restricted operation.
5. A dataset license does not automatically cover embedded third-party media.
6. Rights changes, expiry, correction and withdrawal are auditable.
7. If raw payload retention is not allowed, retain only permitted metadata/reference and provenance; do not retain the prohibited payload in logs, backups, caches or derivative stores.

**Positive assertions:**

- Metadata-only use can be permitted even when image redistribution is not, if the synthetic policy explicitly allows it.
- A derivative can be allowed for one purpose and prohibited for another only where the governing permission explicitly supports that distinction.
- Each decision points to evidence, reviewer and review/expiry state.
- A rights change invalidates or re-evaluates affected downstream permissions and derived assets.

**Negative assertions:**

- No copying the work's rights status to the scan, translation or plate image.
- No assuming public accessibility means redistribution or training permission.
- No embedding/training when permission is unknown, conditional but unmet, or prohibited.
- No hidden retention in temporary storage, search indexes, logs or backups where retention is prohibited.
- No claim that an SPDX identifier alone establishes rights to third-party embedded assets.

**Required reviewers:** copyright/licensing specialist, privacy/security reviewer, data architect, AI governance reviewer.

**Existing links:** B08, B13, B18; LDM-12, LDM-15; HM-07/HM-10.

## HMF-07 — Competing taxonomic interpretations and non-destructive supersession

**Objective:** prove that conflicting historical-name or illustration interpretations remain attributable, evidence-backed and versioned.

**Synthetic setup:**

- Create one fictional source entry and one fictional image/description evidence item.
- Create two synthetic taxonomic assessments by distinct fictional reviewers, `SYN-REVIEWER-A` and `SYN-REVIEWER-B`.
- Each reviewer proposes a different candidate taxon concept or leaves the identity unresolved.
- Give each candidate concept a distinct synthetic treatment/resource and evidence rationale.
- Add a later review event that may qualify or supersede one earlier assessment; do not require the later review to resolve the disagreement.

**Candidate concepts to exercise:** `TaxonName`, `TaxonNameUsage`, `TaxonomicTreatment`, `TaxonConcept`, `TaxonConceptMapping`, `ScientificAssertion`, `EvidenceItem`, `EvidenceRelationship`, `ExpertAssessment`, supersession and audit history.

**Expected behaviour:**

1. Each interpretation identifies the reviewer, date, scope, source/treatment, evidence and rationale.
2. Competing assertions coexist; their review status is explicit.
3. A new determination supersedes or qualifies an earlier one without deleting the earlier assertion.
4. TaxonConcept identity remains tied to its according-to resource.
5. A mapping between concepts uses a valid relation and explicit source context.
6. An unresolved interpretation remains an acceptable outcome.

**Positive assertions:**

- Both reviewer interpretations can be retrieved with their evidence and dates.
- A timeline shows the history of determinations and review.
- The current display can indicate disagreement or uncertainty without concealing the prior view.
- A reviewer can correct a mapping without mutating the underlying source string or source record.

**Negative assertions:**

- No “last write wins” destructive update.
- No forced consensus or automatic majority vote.
- No conversion of a confidence score into a probability without calibration evidence.
- No concept identity detached from its treatment/according-to source.
- No silent deletion of rejected or superseded evidence.

**Required reviewers:** taxonomist, herbarium curator, biodiversity informatician, scientific reviewer.

**Existing links:** B04, B06, B10; LDM-01, LDM-03, LDM-07; HM-04/HM-09.

## HMF-08 — Synthetic community protocol and purpose limitation

**Objective:** prove that community-governance conditions can restrict access and downstream uses and that ambiguous authority or permission fails closed.

**Synthetic setup:**

- Create a fictional community-governed knowledge collection and a clearly synthetic protocol, `SYN-PROTOCOL-HMF08`.
- Do not use the name, rules, language, territory or cultural practices of a real community.
- Define fictional roles and scope: who is authorized to set conditions, which records are covered, how the authority is evidenced, the effective period, review/withdrawal process and the exact permitted/prohibited purposes.
- Define separate hypothetical operations such as community-authorized review, restricted scholarly access, public display, redistribution, commercial reuse and AI training.
- Include a second negative case in which the purported authority or scope is ambiguous or cannot be verified.

**Candidate concepts to exercise:** `Agent`, `RightsRecord`, `SourceRecord`, `ProvenanceRecord`, `MediaAsset`, `MediaDerivative`, authorization policy and audit trail.

**Expected behaviour:**

1. Authority and permission are scoped to the relevant knowledge, asset, community/collective, purpose, audience and time.
2. A protocol is not reduced to a generic Boolean consent field.
3. Permission for one purpose does not imply permission for another.
4. Attribution preferences and restrictions can be applied to public and restricted views.
5. Withdrawal or changed conditions trigger an auditable review of affected records and derived assets.
6. Where authority, scope or permission is ambiguous, affected access/use is withheld pending review.
7. Access restrictions apply across APIs, search, exports, caches, analytics, logs, media stores and model pipelines—not only the user interface.

**Positive assertions:**

- A permitted operation succeeds only within the synthetic protocol's explicit scope and period.
- A restricted operation is denied and logged.
- A valid change/withdrawal event updates the effective access decision without deleting historical audit evidence.
- The system can explain why a particular operation was permitted or denied.

**Negative assertions:**

- No public availability implies community permission.
- No single contributor is assumed to represent a whole community.
- No community protocol is treated as a substitute for legal review where applicable law requires more.
- No model training, embedding, derivative generation or redistribution when the relevant purpose is prohibited or not established.
- No disclosure of restricted content through metadata, search snippets, logs, exports or backups.

**Required reviewers:** community-designated governance reviewer where a real community is ever involved; Indigenous/local data governance specialist; legal/privacy reviewer; security architect.

**Existing links:** B08, B13, B18; HM-08/HM-10.

## 6. Cross-fixture acceptance criteria

The suite should not be considered ready for execution until all of the following are satisfied:

| Gate | Acceptance criterion | Evidence |
|---|---|---|
| F-01 Synthetic provenance | Every fixture and record is visibly synthetic and has no copied real personal/community data | Manifest and fixture review |
| F-02 Model traceability | Every tested relationship maps to a Candidate A concept and a current decision/test ID | Traceability table |
| F-03 Candidate comparison | Candidate B is preserved; any material difference is recorded rather than silently ignored | Candidate comparison note |
| F-04 Source preservation | Original source values and locators are retained separately from derivatives | Positive and negative tests |
| F-05 Uncertainty | Unknown, ambiguous, disputed and not-assessed states remain distinct | Negative tests and output examples |
| F-06 Rights enforcement | Each operation is authorized against applicable asset/purpose evidence | Denial and allow tests |
| F-07 Historical integrity | Prior assertions, transformations, reviews and rights decisions remain auditable | Temporal/history tests |
| F-08 Security | Restricted data cannot leak through secondary surfaces | API/export/search/cache/log/backup tests |
| F-09 Reproducibility | Another reviewer can rerun the fixture with pinned dependencies and source revisions | Runbook, environment and logs |
| F-10 Specialist review | Each discipline reviews only within its competence; conflicts and limitations are recorded | Completed review records |

A fixture may pass its software assertions and still require a domain decision. Software correctness does not prove historical accuracy, taxonomic validity, legal eligibility or community authorization.

## 7. Specialist review plan

| Review discipline | Primary fixtures | Questions within scope |
|---|---|---|
| Malayalam language/script specialist | HMF-01, HMF-02 | Language/script tags, transcription, transliteration, orthographic variants and uncertainty |
| Historian / historical bibliography specialist | HMF-01, HMF-02, HMF-04, HMF-05 | Source context, edition/volume/page/plate citation, historical attribution and transformation history |
| Botanist/taxonomist | HMF-03, HMF-07 | Historical name usage, taxonomic concept, treatment and mapping evidence |
| Biodiversity informatician | HMF-01–HMF-07 | TCS semantics, interoperability, provenance and data-quality tests |
| Ethnobotanist / pharmacognosy specialist | HMF-04 | Distinction between historically reported use and modern scientific evidence |
| Copyright/licensing specialist | HMF-06 | Rights per work, edition, scan, image, translation and operation |
| Privacy/security specialist | HMF-05, HMF-06, HMF-08 | Identity minimization, access enforcement, retention, logs and derivative controls |
| Community-governance specialist / community-designated reviewer | HMF-05, HMF-08 | Attribution preferences, authority, protocols, purpose limitation, benefit and withdrawal |
| Data architect / database engineer | HMF-01–HMF-08 | Entity fit, constraints, versioning, referential integrity and testability |
| AI governance reviewer | HMF-06, HMF-08 | Rights-eligible training/embedding pipeline and auditability |

No reviewer is presumed appointed or available. Do not invent names, qualifications, affiliations, endorsements or sign-offs.

## 8. Legal, ethical and standards boundaries

### 8.1 Taxonomic interoperability

The TDWG Taxon Concept Standard (TCS) distinguishes TaxonName, TaxonConcept and TaxonConceptMapping. A TCS TaxonConcept requires a taxonName and an accordingTo resource. A name string alone does not establish a taxonomic concept. Preserve source-specific usage and explicit mappings rather than equating a vernacular string with a modern accepted taxon.

Reference: https://tcs.tdwg.org/terms/ (inspected version metadata: 2025-12-11).

### 8.2 Provenance

W3C PROV-O distinguishes Entities, Activities and Agents and provides relationships for usage, generation, derivation and responsibility. It is a useful interoperability reference for testing the transformation chain, not a mandate to copy PROV-O directly into Botanica Indica's internal schema.

Reference: https://www.w3.org/TR/prov-o/

### 8.3 Language tags and Unicode

IETF BCP 47 / RFC 5646 provides language tags and script subtags. Use registered tags and do not invent language/script codes. The language of a source and the script in which it is written are related but not identical metadata.

References:
- https://datatracker.ietf.org/doc/rfc5646/
- https://www.unicode.org/reports/tr15/

Preserve the source-exact string. A normalized comparison value may be stored separately under a documented policy; do not destructively replace source evidence with compatibility-normalized text.

### 8.4 Community data governance

The CARE Principles—Collective Benefit, Authority to Control, Responsibility and Ethics—are relevant design guidance when Indigenous data or community-governed knowledge is in scope. They complement rather than replace scientific interoperability or legal compliance.

Reference: Carroll et al. (2020), *The CARE Principles for Indigenous Data Governance*, Data Science Journal 19:43, https://doi.org/10.5334/dsj-2020-043. Institutional summary: https://www.rd-alliance.org/wp-content/uploads/2024/03/CARE20Principles20for20Indigenous20Data20Governance_OnePagers_FINAL20Sept2006202019.pdf

### 8.5 Nagoya Protocol and India-specific law

Nagoya Protocol Article 7 addresses access to traditional knowledge associated with genetic resources held by Indigenous and local communities, in accordance with domestic law, and refers to prior informed consent or approval and involvement and mutually agreed terms. Article 12 addresses customary laws, community protocols and procedures, as applicable.

References:
- https://www.cbd.int/abs/text/articles?sec=abs-07
- https://www.cbd.int/abs/text/articles?sec=abs-12

Do not assume that every historical vernacular name, old publication, scan or digitized text is automatically within the Protocol's scope. Equally, do not infer that historical publication or public access grants present-day permission for all uses. India-specific applicability requires a qualified legal assessment of the material, parties, access, purpose, utilization, transfer and current law. This fixture design is not legal advice and does not establish any permission, exemption, community mandate or benefit-sharing arrangement.

## 9. Test execution and review record template

Copy once for each fixture and each material test outcome.

- Fixture ID and version:
- Related HMF/HM/B/LDM/TAX/RGT decision IDs:
- Source document paths and blob SHAs:
- Candidate model branch and commit SHA:
- Test harness / environment / dependency versions:
- Reviewer name or designated identifier:
- Reviewer discipline and qualification scope:
- Affiliation (if reviewer consents):
- Conflict-of-interest declaration:
- Date:
- Synthetic-data declaration confirmed:
- Test procedure / command:
- Expected graph and result:
- Actual graph and result:
- Positive assertions passed:
- Negative assertions passed:
- Evidence links / logs / checksums:
- Outcome: Pass / Pass with condition / Fail / Not tested / Not applicable / Needs domain decision
- Findings and rationale:
- Potential model gap (if any):
- Is the gap reproducible with existing concepts?:
- Proposed action:
- Owner:
- Re-review requirement:
- Explicit approval or non-approval:

No blank field, unrecorded review or successful software test may be interpreted as scientific, legal, community or product approval.

## 10. Model-change gate

If a fixture fails, use this sequence:

1. Reproduce the failure using the pinned fixture and source/model revisions.
2. Determine whether the cause is fixture ambiguity, missing source evidence, a test-harness defect, a documentation inconsistency, a controlled-vocabulary gap, a relationship/cardinality gap or a genuine model limitation.
3. Check Candidate A, Candidate B, Task 05B, Task 05D and relevant ADRs for an existing representation or conflicting rule.
4. Record the exact invariant that cannot be represented and the smallest counterexample.
5. Ask the appropriate domain and technical reviewers whether the failure reflects a genuine requirement.
6. Compare alternatives: existing entities/relationships, typed provenance extension, vocabulary extension, workflow/policy control or a new domain concept.
7. Only after review, prepare a separate proposed model change and decision record. Do not silently edit accepted ADRs or declare a candidate approved.

**Do not introduce a dedicated `KnowledgeHolder`, `KnowledgeContribution`, `TranslationChain` or `CommunityConsent` entity solely because the historical case is complex.** Introduce a new concept only if a demonstrated invariant or lifecycle cannot be represented safely and clearly with the current model and an approved decision authorizes the change.

## 11. Project status and next actions

- ADR-004, ADR-005, ADR-007 and ADR-010 remain accepted and unchanged.
- Candidate A remains a proposed review candidate, not an approved model.
- Candidate B remains preserved as an alternative; this document does not resolve the competing-model decision.
- HMF-01–HMF-08 are proposed design specifications only.
- No synthetic data package has been instantiated or executed.
- No reviewer has signed off.
- No historical text, scan, plate, translation, audio/video or community-held knowledge has been ingested.
- No rights clearance, community permission, legal determination or endorsement is claimed.
- Task 05C remains NOT APPROVED.
- Task 05E remains NOT READY.
- No physical schema, DDL, API contract or production implementation is authorized by this document.

### Recommended next sequence

1. Have the data architect and biodiversity informatician review the fixture specifications against Candidate A and Task 05B.
2. Have the taxonomist and language/script specialist review HMF-01–HMF-03 and HMF-07.
3. Have rights/privacy and community-governance specialists review HMF-05, HMF-06 and HMF-08 before any realistic data is considered.
4. Resolve any test-design ambiguity and confirm Candidate B has not exposed a better existing representation.
5. Instantiate the fixtures in an isolated test package only after review and approval of the test inputs.
6. Execute tests and attach reproducible evidence to the existing validation register. Keep all unexecuted cases **Not tested**.
7. Reassess whether any model change is genuinely required. Only then consider a proposed Task 05C revision.

**Final disposition:** proposed fixture design only. It is intended to test the sufficiency of the existing model, not to expand or approve it.
