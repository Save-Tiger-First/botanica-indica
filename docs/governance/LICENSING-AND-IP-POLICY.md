# Save Tiger First — Licensing and Intellectual Property Policy

**Status:** Proposed — requires maintainer approval and legal review  
**Version:** 0.1  
**Scope:** Save Tiger First (STF) ecosystem, including shared infrastructure and domain applications  
**Initial domain application:** Botanica Indica

---

## 1. Purpose

Save Tiger First is intended to develop multiple applications, reusable software infrastructure, scientific resources, datasets, media collections and educational materials. These assets do not all have the same legal character or reuse requirements.

STF therefore adopts an **asset-specific, component-specific and purpose-aware licensing approach**. A single license must not be assumed to cover every asset in the ecosystem.

This policy establishes a governance framework for selecting, recording, reviewing and communicating licenses and permissions. It is a project policy proposal, not legal advice or a substitute for review by qualified counsel in the relevant jurisdictions.

## 2. Core principles

1. **Rights before reuse:** Do not ingest, publish, redistribute, adapt or use an asset for model training until the relevant rights and permissions have been assessed.
2. **License each asset at the right level:** Select terms appropriate to software, documentation, data, photographs, models and other asset types.
3. **Preserve provenance:** Retain creator, source, rights holder, license, attribution, version and retrieval information where applicable.
4. **No implied permissions:** Public visibility, a public download URL, API access or an institutional source does not by itself grant redistribution, commercial-use or AI-training rights.
5. **Separate purposes:** Permission to display or analyse material does not automatically include permission to redistribute it, create derivatives, use it commercially or train machine-learning models.
6. **Respect upstream terms:** STF cannot grant rights it does not own or control.
7. **Make restrictions machine-readable:** Use standard license identifiers and structured rights metadata wherever practical.
8. **Protect sensitive information:** A license does not override privacy, conservation, contractual, security or access-control obligations.
9. **Keep shared infrastructure reusable:** Shared software may be openly licensed while connected domain data remains separately licensed or restricted.
10. **Resolve uncertainty conservatively:** Quarantine or exclude assets when ownership, terms or permitted uses cannot be established.

## 3. Asset classes and licensing approach

The following are preferred starting points, not automatic grants. A maintainer must verify ownership, compatibility, intended use and applicable legal terms before assigning a license.

| Asset class | Preferred approach | Important qualification |
|---|---|---|
| STF-owned shared software | Apache-2.0 as the default candidate | Confirm STF has the rights to license all included code and dependencies |
| STF-owned domain software | Apache-2.0 as the default candidate | Domain-specific components may use another approved software license where justified |
| Documentation and educational material | CC-BY-4.0 as a default candidate for clearly separable original content | Code examples, third-party excerpts and embedded media may have different terms |
| Open scientific datasets | CC0-1.0, CC-BY-4.0, ODbL-1.0 or ODC-By-1.0, selected after rights analysis | These licenses are not interchangeable; database rights, attribution and share-alike effects differ |
| Photographs, illustrations, audio and video | Creator-selected approved license or explicit written permission | Record the actual creator and rights holder; do not assume the uploader owns the work |
| Third-party scientific publications and books | Use only under the applicable license, permission or legal exception | Do not copy full text or figures merely because a publication is accessible |
| User contributions | Explicit contribution terms selected before submission | Explain display, storage, moderation, redistribution, research and model-training purposes separately |
| AI source code | License as software | Code rights do not determine model-weight or training-data rights |
| Model weights and checkpoints | Separate license and use restrictions for each release | Record training data provenance, model lineage, evaluation and redistribution conditions |
| Training and evaluation datasets | Dataset-specific license and explicit purpose permissions | Training permission must not be inferred from permission to view, download or display |
| Embeddings and derived datasets | Document source lineage and assess upstream terms and applicable rights | Transformation does not automatically remove upstream obligations |
| Trademarks, names and logos | Separate trademark and brand-use policy | Open-source software licensing does not grant trademark rights |
| Sensitive or restricted records | Access policy plus underlying rights assessment | Restriction may apply regardless of whether some underlying facts are public |

## 4. Software licensing

### 4.1 Default candidate

Apache License 2.0 is the proposed default for software authored and controlled by STF, including reusable shared infrastructure and Botanica Indica software, unless a documented decision selects another license.

Apache-2.0 is a permissive software license that includes an express patent license and conditions concerning notices and attribution. It is not a data license and does not grant rights to unrelated third-party content, trademarks or personal information.

### 4.2 Repository-level license scope

The existing root `LICENSE` file in this repository contains Apache License 2.0. Until a more granular notice is adopted, repository users should treat that as the repository's stated software license while checking every file, dependency, dataset and media asset for separate notices and upstream terms.

A repository-level license must never be represented as overriding third-party rights or as licensing material that STF does not own or have authority to license.

Where different asset classes coexist, use explicit directory-level or file-level notices, a rights manifest and clear README guidance. Avoid ambiguous or conflicting license statements.

### 4.3 Dependencies and generated code

Every software dependency must be checked for:
- License identifier and version
- Compatibility with the relevant STF component
- Attribution and notice obligations
- Source-disclosure or network-use obligations, where applicable
- Patent, trademark or other special terms
- Known license exceptions

Generated code, copied snippets, templates and vendored dependencies must be reviewed; generated output is not automatically free of upstream obligations.

Use SPDX identifiers and expressions where supported. Maintain a software bill of materials (SBOM) as implementation matures.

## 5. Documentation and educational content

CC-BY-4.0 is a suitable default candidate for original STF documentation and educational material intended for broad reuse, subject to confirmation of ownership and separation from code or third-party content.

Attribution should identify the creator or STF as appropriate, link to the license, preserve required notices and indicate modifications where required.

Do not apply a Creative Commons license to software source code where a software license is more appropriate. Do not apply a CC license to third-party quotations, images or diagrams unless STF has the authority to do so.

## 6. Scientific data and database licensing

Scientific datasets require a dataset-level assessment. Consider:
- Copyright in original records, descriptions, images and other expressive material
- Database rights, where applicable
- Contractual terms and API terms
- Government or institutional reuse policies
- Attribution and citation requirements
- Share-alike obligations
- Redistribution and commercial-use permissions
- Restrictions on extraction, bulk access or automated collection
- Privacy, Indigenous/local knowledge and conservation sensitivities
- Whether the proposed use includes model training or other machine processing

Potential licenses include:

- **CC0-1.0:** A public-domain dedication intended to maximize reuse where the rights holder can validly apply it.
- **CC-BY-4.0:** Allows broad reuse subject to attribution and other license terms; assess database rights and all relevant rights in the material.
- **ODbL-1.0:** A database license with attribution and share-alike obligations for adapted databases; assess whether its obligations fit the intended database and downstream distribution.
- **ODC-By-1.0:** An attribution-focused database license; assess the exact legal text and rights it covers.

Do not select a license solely because it is permissive. The rights holder must have authority to apply it, and the license must cover the relevant rights. A dataset can contain records, images or texts whose rights differ from the database structure itself.

Do not assume factual observations, scientific names or taxonomic facts have the same copyright status as photographs, descriptions, maps, curated databases or publications containing them. Assess each layer.

## 7. Photographs and media

Photographs and other media must have an identifiable creator or rights holder and a recorded basis for use.

For every media asset, record where available:
- Asset identifier and file checksum
- Creator / photographer
- Rights holder
- Original source and source URL
- Date created and date acquired
- Exact license name, version and URL, or permission reference
- Required attribution text
- Allowed display, adaptation and redistribution uses
- Commercial-use permission
- AI/ML training permission
- Model-training opt-out or restrictions, if applicable
- Geographic and privacy sensitivity
- Review status and reviewer

Do not treat a user who uploads a photograph as necessarily owning the copyright. Obtain an explicit grant sufficient for the intended platform functions. If the platform intends to use user media for model training, request a separate, understandable and affirmative permission rather than burying it in a general upload permission.

## 8. AI, machine learning and derived assets

AI development requires rights assessment across the complete lifecycle:

1. Source material acquisition
2. Dataset assembly and annotation
3. Training, fine-tuning and evaluation
4. Model weights and checkpoints
5. Embeddings and vector indexes
6. Inference outputs
7. Derived datasets and synthetic data
8. Distribution, deployment and commercial use

For every dataset or asset considered for training, record an explicit training-use status:
- Permitted
- Prohibited
- Permitted subject to conditions
- Unclear / pending review
- Not assessed

Only assets marked permitted, or permitted subject to satisfied conditions, may enter the relevant training pipeline.

Permission to use a dataset for research or display must not be interpreted as permission to train or fine-tune a model. Permission to train must not be interpreted as permission to redistribute source images, datasets, embeddings or model weights.

For each released model, document model identifier, version, architecture where publishable, training/evaluation dataset references, data-use permissions, known limitations, evaluation results, intended use, prohibited use, license and distribution conditions.

The legal status of AI outputs and derived representations can be fact-specific and jurisdiction-dependent. Do not promise that outputs, embeddings or trained weights are free of upstream obligations without legal and technical assessment.

## 9. User contributions and contributor rights

STF should not assume that a contributor transfers ownership merely by submitting a contribution.

Before accepting contributions at scale, establish clear contributor terms that:
- Identify the rights the contributor retains
- Grant STF the permissions needed to host, display, moderate, back up, transform and distribute the contribution for stated platform purposes
- Distinguish optional or separate permissions for research, commercial use and AI/ML training
- Explain attribution and removal limitations
- Address third-party rights and warranties in a proportionate manner
- State the license applicable to code, text, data and media contributions

For code contributions, decide whether to adopt a Developer Certificate of Origin (DCO), a Contributor License Agreement (CLA), or another reviewed process. Do not combine these mechanisms casually: they serve different governance purposes.

Until approved contributor terms exist, do not solicit broad grants of rights or represent the current CONTRIBUTING.md wording as a fully developed contributor agreement.

## 10. Data and Rights Registry

STF should maintain a Data and Rights Registry. It may begin as a controlled manifest or governed module; it does not need to be a separately deployed service initially.

Each source, dataset, asset collection or material license unit should record, as applicable:

| Field | Purpose |
|---|---|
| Rights record ID | Stable internal reference |
| Asset / dataset ID | Identifies the covered material |
| Asset class | Software, dataset, image, text, model, etc. |
| Source and source URL | Provenance |
| Creator / rights holder | Identifies who controls relevant rights |
| License name and SPDX identifier | Standardized license identification, when available |
| License version and URL | Exact legal terms |
| Attribution text | Required credit |
| Permitted purposes | Display, research, redistribution, commercial use, training, etc. |
| Prohibited / conditional purposes | Explicit restrictions and conditions |
| Redistribution status | Whether the asset may be shared onward |
| AI/ML training status | Separate training permission |
| Derivative-use status | Whether adaptation or derived works are allowed |
| Access classification | Public, internal, restricted or sensitive |
| Source version and retrieval date | Reproducibility |
| Review status and reviewer | Governance evidence |
| Review / expiry date | Reassessment trigger |
| Evidence of permission | License snapshot, agreement or correspondence reference |

The registry should support source-level defaults only where the source terms genuinely apply uniformly. Record exceptions at dataset, record or asset level where required.

A registry entry is evidence of the project's assessment, not proof that a rights holder's claim is legally correct. Preserve the underlying license text or permission evidence where lawful and practical.

## 11. Ingestion and publication gates

Before an external or contributed asset is imported into a production dataset, training corpus or public release, the responsible workflow must confirm:

1. The source and rights holder are identified to a reasonable standard.
2. The applicable license or permission is recorded.
3. The intended use is permitted.
4. Attribution and notice requirements can be met.
5. Share-alike or other downstream obligations are understood.
6. Privacy, sensitive-location and conservation controls are addressed.
7. Provenance and source version are retained.
8. The asset is approved by the designated reviewer.

If any material condition is unknown, mark the asset **pending rights review** and prevent the unapproved use. Do not silently downgrade an unknown permission into an assumed permission.

## 12. Licensing governance and responsibilities

Each repository or domain application should nominate a maintainer responsible for license metadata and release checks. Scientific/data owners should review source suitability and scientific provenance. Security and privacy reviewers should assess sensitive data. Legal questions and non-standard grants should be escalated for qualified legal review.

Changes to a license must not be made retroactively on behalf of a rights holder without authority. Maintain version history for license decisions and asset rights records.

For a dataset or model release, publish a clear license and attribution notice alongside a data/model card or equivalent documentation. If a release contains multiple license classes, provide a per-component manifest rather than implying one blanket license.

## 13. Practical implementation sequence

### Phase 1 — Governance baseline
- Approve this policy after maintainer and legal review.
- Confirm the scope of the existing root Apache-2.0 license.
- Identify all current repository assets and their rights status.
- Establish a pending-rights-review state.
- Select DCO, CLA or another contributor process before scaling external contributions.

### Phase 2 — Repository controls
- Add SPDX identifiers where appropriate.
- Add third-party notices and a dependency license inventory.
- Introduce a rights manifest for external data and media.
- Add license checks to CI when software and datasets are introduced.
- Document the policy from the README and contribution guide.

### Phase 3 — Data and AI controls
- Establish the Data and Rights Registry.
- Add ingestion gates for display, redistribution and training.
- Record dataset/model lineage and versioning.
- Publish data and model documentation with each relevant release.

### Phase 4 — Ecosystem adoption
- Reuse the registry and governance process across STF domain applications.
- Keep domain-specific rights decisions under the relevant domain owner.
- Audit shared assets and cross-project transfers before reuse.

## 14. Review triggers

Review this policy when:
- A new asset class or data source is introduced.
- A new commercial, redistribution or AI-training use is proposed.
- A license changes or a source updates its terms.
- A contributor agreement is adopted or amended.
- A new domain application joins the STF ecosystem.
- A rights holder raises a claim or requests correction/removal.
- Applicable law or institutional policy changes.

## 15. Official references

The following are starting points for policy interpretation. Always read the actual license text and source-specific terms before use.

- Apache License 2.0: https://www.apache.org/licenses/LICENSE-2.0
- Creative Commons Attribution 4.0: https://creativecommons.org/licenses/by/4.0/
- Creative Commons data and database guidance: https://wiki.creativecommons.org/wiki/Data
- Open Data Commons ODbL 1.0: https://opendatacommons.org/licenses/odbl/
- Open Data Commons ODC-By 1.0: https://opendatacommons.org/licenses/by/
- SPDX License List: https://spdx.org/licenses/
- SPDX license identifiers and expressions: https://spdx.dev/learn/handling-license-info/
- Intellectual Property India — Copyright basics: https://ipindia.gov.in/pages/copyright/learn/basics-of-copyright

---

## 16. Final policy position

STF will not use one blanket license for every project asset. It will select licenses and permissions according to the nature of each asset, the rights actually held, the intended use and the obligations that must be preserved.

**Open software, open documentation, open scientific data, user-contributed media and AI training assets are separate rights questions.** The ecosystem should make those distinctions explicit, traceable and enforceable from acquisition through publication and reuse.
