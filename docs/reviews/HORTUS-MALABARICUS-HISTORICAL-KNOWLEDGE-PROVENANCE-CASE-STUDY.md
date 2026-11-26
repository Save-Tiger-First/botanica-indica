# Hortus Malabaricus — Historical Knowledge and Provenance Case Study

- **Project:** Botanica Indica — Save Tiger First
- **Document type:** Historical/scientific research note and proposed model-validation input
- **Version:** 0.1
- **Status:** Proposed; not an approved data-model decision
- **Prepared:** 21 November 2026
- **Review branch:** `review/scientific-data-model-review-pack`
- **Related PR:** [PR #9](https://github.com/Save-Tiger-First/botanica-indica/pull/9)
- **Owner-supplied audiovisual lead:** [YouTube video](https://www.youtube.com/watch?v=FiXo1iHoxgE)

> **Decision boundary:** This note proposes a historical case study and validation questions. It does not amend or supersede any accepted ADR, approve a scientific model, authorize ingestion of historical data or community-held knowledge, authorize reproduction of images/text, or represent any community, knowledge holder, institution or rights holder as having approved Botanica Indica's use of this material.

## 1. Executive assessment

`Hortus Indicus Malabaricus` (commonly `Hortus Malabaricus`) is a high-value historical case study for Botanica Indica. It demonstrates that botanical knowledge production can involve local and community-held plant knowledge; named and unnamed contributors; oral, experiential and manuscript sources; plant names in multiple languages and scripts; translation, transliteration, editorial and visual transformations; historical plant descriptions and illustrations; later taxonomic interpretation; and questions of recognition, colonial power and cultural ownership.

The case matters not because Botanica Indica should reproduce its historical classification, but because it illustrates why a botanical intelligence platform must preserve **who contributed what, from which source, in which language, through which transformations, under which rights and with what uncertainty**.

Treat it as a historical-source and provenance case study—not as a new taxonomic authority or a medicinal-efficacy reference.

## 2. Evidence baseline and careful wording

### 2.1 Publication and scale

The twelve-volume work was published in Amsterdam between **1678 and 1693**; the first volume appeared in 1678. A National Centre for Biological Sciences (NCBS) curated account describes 742 plants and 792 copperplate engravings. Other institutional descriptions round the coverage to over 740 plants. A concise description can say “twelve volumes, published 1678–1693, documenting approximately 742 plants and containing 792 copperplate engravings,” while retaining the cited source and counting convention.

The first volume opens with the coconut palm (`Cocos nucifera`), as described by the Max Planck Institute for the History of Science.

### 2.2 Contributors and knowledge sources

Hendrik Adriaan van Rheede tot Drakenstein was central to the project, but the work was collaborative. Magdalen College, University of Oxford, describes a team of over a hundred people, including local and colonial contributors. NCBS describes a broad committee drawn from different parts of Malabar and identifies local physicians, translators and artists.

Itty Achudan (also rendered as Itti Achudem, Itty Achyuden or Itty Acchudan) was an Ezhava physician and an important contributor. The certificate attributed to him in Volume I records his contribution and refers to knowledge grounded in long experience and practice. NCBS describes his reference to hereditary family palm-leaf manuscripts. Three Konkani scholars/physicians—Appu Bhatt, Ranga Bhatt and Vinayaka Pandit—are also acknowledged.

Do not flatten these contributions into a single-author narrative. Nor should the project assume that every contributor, artist, collector or knowledge lineage has been identified in surviving records.

### 2.3 Languages, scripts and translation

The work contains plant names and knowledge mediated through multiple languages and scripts. Institutional and scholarly accounts identify Malayalam and Konkani, alongside Latin and Arabic-related scripts/representations; they also describe translation through Portuguese and Dutch intermediaries before Latin publication.

The exact language/script path varies by contributor and record. Do not encode one universal translation chain for every entry. Preserve each attested source language, script, transcription, transliteration, translator, intermediary language and editorial intervention separately where the evidence supports it.

Magdalen College cautions that many plant names represent transliterations of spoken Malayalam rather than direct examples of written Malayalam, and that historical engraving/transcription introduced errors. It describes the certificates in Volume I as rare examples of written Malayalam in distinct scripts. Therefore, the claim that this was definitively “the first book ever printed in Malayalam” is not adopted here. Use “an important and rare early printed witness to Malayalam scripts” unless specialist bibliographic evidence establishes a stronger claim.

### 2.4 Botanical and taxonomic influence

The work influenced later European botanical literature, including Linnaeus. A 2003 paper by K. S. Manilal, C. Sathish Kumar and M. Remesh specifically analyses Linnaeus's use of the work and Malayalam plant names in `Species Plantarum`. The Max Planck Institute feature states that Linnaeus described 100 plant species based on the work.

These are different descriptions of influence. Do not collapse them into a claim that Linnaeus simply copied or independently validated every local name or plant identification. Each historical name-to-modern-taxon mapping requires its own bibliographic and taxonomic evidence.

A useful candidate example is the historical vernacular name “Mouringou”. Kew's Medicinal Plant Names Services currently maps this non-scientific name to `Moringa oleifera` Lam. This is a modern reference assertion, not proof that every historical usage of a similar name refers to the same taxon in every context.

### 2.5 K. S. Manilal's translations

K. S. Manilal's decades-long work made the twelve volumes more accessible to contemporary readers. Institutional sources commonly identify 2003 for the English translation and 2008 for the Malayalam translation. Some secondary accounts conflate the publication dates; formal bibliography should verify the title page and edition details of the exact translation cited.

### 2.6 Historical motives and colonial context

Institutional accounts describe practical Dutch colonial motives, including access to local medicinal resources and reducing the expense and delay of importing medicines from Europe. The supplied video summary also mentions political rivalry involving Cochin and Colombo. That specific geopolitical explanation was not corroborated by the sources consulted for this note and should not be repeated as established fact without further historical research.

The project should neither romanticize the colonial compilation nor erase the local expertise and knowledge systems on which it depended. Max Planck's history-of-science research discusses both its colonial knowledge-making context and the continuing cultural and intellectual-property significance attributed to it by Ezhava community members.

## 3. Relevance to existing Botanica Indica decisions

This case tests principles already substantially expressed in accepted:

- **ADR-004 — Data and Scientific Provenance:** source identity, versions, transformations, rights and uncertainty.
- **ADR-005 — Taxonomy Reconciliation:** historical names, source-specific taxonomic treatments and versioned mappings.
- **ADR-007 — Evidence and Expert Validation:** attributable evidence, disagreement and expert review.
- **ADR-010 — Data Ingestion and Source Integration:** source registry, rights-aware ingestion and transformation history.

This note is a proposed application and validation input. It does not reopen or amend those accepted decisions.

The current scientific validation matrix already expects reviewers to consider provenance, rights, historical context, taxonomic uncertainty, sensitive information and community-designated review where community-held knowledge is in scope. It also explicitly states that the review package does not authorize ingestion of external datasets or collection of community-held knowledge.

## 4. Candidate model-validation questions

These are proposed test questions, not approved new entities or schema requirements.

| ID | Case-study challenge | Expected model behaviour to evaluate |
|---|---|---|
| HM-01 | A historical plant entry has an original Malayalam name in a particular script. | Preserve verbatim source form, script, language attribution, page/volume/plate reference and transcription provenance. |
| HM-02 | A name is translated/transliterated through Portuguese, Dutch and Latin. | Preserve each attested transformation and contributor; do not overwrite the original form with the final Latin expression. |
| HM-03 | A vernacular name may refer to different taxa in different historical or regional contexts. | Keep source-specific name usages and candidate mappings distinct; do not resolve by string equality alone. |
| HM-04 | A historical name is mapped to a modern taxon. | Record the mapping as an evidence-backed, versioned reconciliation with source, rationale, reviewer and uncertainty. |
| HM-05 | Some contributors are named while other collectors, artists or knowledge holders are anonymous. | Preserve known attribution, uncertainty and explicit unknowns; never invent identities or infer consent. |
| HM-06 | A historical medicinal use is recorded. | Label it as a historically reported use; do not represent it as clinically validated efficacy or current medical advice. |
| HM-07 | A modern translation, scan, photograph or digitized plate is used. | Evaluate rights separately for the historical work, modern edition/translation, scan, image, annotations and hosting institution. |
| HM-08 | A community asserts cultural ownership or governance interests in historical knowledge. | Support appropriate access restrictions and attributable permissions; do not treat public availability as blanket permission. |
| HM-09 | Experts disagree about the modern identity of a historical illustration or name. | Preserve competing determinations, evidence and taxonomic treatments; do not erase earlier claims. |
| HM-10 | Historical images, text or extracted names are proposed for model training. | Require explicit rights and purpose review; do not infer training permission from display, research access or public availability. |

Reviewers should map HM-01–HM-10 to existing scenarios and identify genuine gaps before proposing any new domain object. In particular, assess whether existing generic provenance, evidence and assertion concepts can represent this case before introducing a dedicated `KnowledgeHolder`, `KnowledgeContribution` or similar entity.

## 5. Rights, community governance and legal caution

### 5.1 Asset-specific rights

The historical age of the original publication does not establish that every modern digital asset is free to reproduce. Distinguish:

- The original seventeenth-century text and engravings;
- A particular physical copy or digitized scan;
- Modern photographs of pages or objects;
- Modern transcriptions and transliterations;
- K. S. Manilal's translations, annotations and editorial material;
- Contemporary scholarly articles and exhibition material;
- The supplied YouTube video's narration, music, footage and graphics.

The proposed repository `LICENSING-AND-IP-POLICY.md` requires rights-before-reuse, asset-specific permissions and no implied rights from public visibility or API availability. Apply that policy conservatively; do not assume a public scan, video or institutional webpage grants redistribution, derivative or AI-training rights.

### 5.2 Traditional knowledge and access/benefit-sharing

The Nagoya Protocol addresses access to traditional knowledge associated with genetic resources, community participation, prior informed consent or approval/involvement as applicable under domestic law, mutually agreed terms and fair and equitable benefit-sharing. Articles 7 and 12 are particularly relevant.

India's Biological Diversity Act, 2002 has been amended. The National Biodiversity Authority reports that the Biological Diversity Rules, 2024 superseded the 2004 Rules and were subsequently amended in 2025. The applicable law and rules depend on the actual activity, parties, resource, knowledge, purpose and statutory exemptions. Qualified legal review is required before collection, access, research use, commercialization or transfer of biological resources or associated traditional knowledge. This note is not a legal opinion.

The WIPO Treaty on Intellectual Property, Genetic Resources and Associated Traditional Knowledge was adopted on 24 May 2024. WIPO's treaty status page currently labels it “not yet in force”; recheck status before relying on it as an operative treaty obligation.

### 5.3 Community authority and representation

Do not assume that one individual, scholar, institution or contributor can grant rights on behalf of an entire community. Do not presume that the historical record exhaustively identifies the holders, custodians or customary governance of the knowledge. Where contemporary community-held knowledge is proposed for collection or use, identify the relevant community's own processes and competent representatives, document applicable permissions and terms, and provide appropriate benefit-sharing and governance. No permission or endorsement is asserted here.

## 6. Recommendations

**A. Include as a historical case study.** Include `Hortus Malabaricus` in historical and scientific context material, with careful attribution and a balanced account of local expertise, multilingual knowledge production, colonial context and modern scholarship.

**B. Use it as a model-validation case, not a new schema mandate.** Map HM-01–HM-10 to existing ADRs and the scientific validation matrix. Ask reviewers whether the proposed model can represent the case with current concepts. Raise a model change only if a reproducible gap is demonstrated.

**C. Separate historical use from current evidence.** Historical medicinal descriptions are source-reported historical claims. They must not become clinical recommendations, safety claims or efficacy evidence without independent contemporary scientific assessment.

**D. Do not ingest or train on source materials yet.** No book scans, translated text, plates, video frames, audio, transcripts or community-held knowledge should be ingested, redistributed, transformed or used for model training until asset-specific rights, source terms and relevant legal/community governance have been assessed.

**E. Preserve contributor credit and uncertainty.** Preserve source-supported attributions. Where contributors are unknown, record that the historical source does not identify them. Do not invent identities or flatten collective knowledge into a single-author narrative.

## 7. Relationship to project decisions and status

| Existing decision/document | Relevance | Treatment proposed here |
|---|---|---|
| ADR-004 — accepted | Provenance and rights | Apply as written; no amendment |
| ADR-005 — accepted | Historical names and taxonomic reconciliation | Apply as written; no amendment |
| ADR-007 — accepted | Evidence, disagreement and expert review | Apply as written; no amendment |
| ADR-010 — accepted | Source-aware ingestion and rights | Apply as written; no amendment |
| `LICENSING-AND-IP-POLICY.md` on PR #16 branch | Asset-specific rights and purpose limitations | Proposed policy; not represented as merged |
| Scientific validation matrix on PR #9 branch | Rights, provenance, historical evidence and community review | Map HM tests to existing scenarios |
| Task 05C / Task 05D | Logical model and validation gate | No status change; Task 05C remains not approved and Task 05E remains not ready |

## 8. Source register

Sources consulted on 21 November 2026:

1. **Max Planck Institute for the History of Science**, Minakshi Menon, “Hortus Indicus Malabaricus: The Eurasian Life of a Seventeenth-Century ‘European’ Botanical Classic” (12 July 2023). Historical context, dates, Linnaeus, Itty Achudan's certificate, local knowledge and contemporary cultural significance.  
   https://www.mpiwg-berlin.mpg.de/feature-story/malabaricus-botanical-seventeenth-century

2. **National Centre for Biological Sciences (NCBS), Tata Institute of Fundamental Research**, “Portuguese and Dutch Records of Indian Medicine” (Google Arts & Culture exhibition). Publication dates, 742 plants, 792 engravings, Itty Achudem's statement, local contributors and artists.  
   https://artsandculture.google.com/story/portuguese-and-dutch-records-of-indian-medicine-national-centre-for-biological-sciences/KwXhWshAlfr6IQ

3. **Magdalen College, University of Oxford**, “Hortus Malabaricus: A Botanical and Linguistic Treasure” (8 November 2024). Team composition, Itty Achudan, translation history, scripts and transliteration caveats.  
   https://www.magd.ox.ac.uk/blog/hortus-malabaricus-a-botanical-and-linguistic-treasure/

4. **Manilal, K. S., Sathish Kumar, C. & Remesh, M.** (2003). “Carl Linnaeus and Hortus Malabaricus: A 250th Anniversary Tribute to Species Plantarum.” `Rheedea`, 13(1–2), 3–18.  
   https://doi.org/10.22244/rheedea.2003.13.1-2.01

5. **Kew, Medicinal Plant Names Services**, entry for “mouringou”; current matched accepted name shown as `Moringa oleifera` Lam.  
   https://mpns.science.kew.org/mpns-portal/drugDetail?drugName=mouringou

6. **Convention on Biological Diversity**, Nagoya Protocol, Article 7 (access to traditional knowledge associated with genetic resources).  
   https://www.cbd.int/abs/text/articles?sec=abs-07

7. **Convention on Biological Diversity**, Nagoya Protocol, Article 12 (traditional knowledge, community protocols and procedures).  
   https://www.cbd.int/abs/text/articles?sec=abs-12

8. **National Biodiversity Authority, India**, FAQs on the Biological Diversity Act and 2024 Rules / 2025 amendments.  
   https://nbaindia.nic.in/about-us/faqs

9. **India Code**, Biological Diversity Act, 2002 (as amended).  
   https://www.indiacode.nic.in/bitstream/123456789/21545/1/the_biological_diversity_act%2C_2002.pdf

10. **World Intellectual Property Organization**, WIPO Treaty on Intellectual Property, Genetic Resources and Associated Traditional Knowledge; adoption date and treaty information.  
    https://www.wipo.int/en/web/treaties/ip/gratk/index

11. **WIPO Lex**, treaty status page, currently labelled “not yet in force”.  
    https://www.wipo.int/wipolex/en/treaties/ShowResults?search_what=N&treaty_id=19830

12. **Owner-supplied audiovisual lead:** YouTube video and summary. The video page itself could not be independently retrieved during this research session; video-specific statements were treated as leads and checked against the institutional and scholarly sources above.  
    https://www.youtube.com/watch?v=FiXo1iHoxgE

## 9. Open questions for reviewers

1. Can the current logical model represent historical name usage, language, script, transcription, transliteration and translation provenance without conflating these with modern TaxonName or TaxonConcept records?
2. Can it preserve named and anonymous contributors, their distinct roles and limits of what is known about their authority?
3. Can source-reported historical medicinal uses be represented without being mistaken for validated contemporary efficacy?
4. Can rights and permitted purposes be represented separately for a historical source, modern edition, scan, plate image, translation, transcript and derived training asset?
5. What governance is required if the project later proposes to collect or use contemporary community-held knowledge?
6. Which HM tests map to existing validation scenarios, and which demonstrate a genuine gap requiring a formal decision?

**Closing status:** Proposed research and validation input only. No accepted ADR, scientific model, product requirement, rights policy or implementation status is changed by this note.
