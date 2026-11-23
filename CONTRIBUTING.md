# Contributing to Botanica Indica

Thank you for your interest in contributing to Botanica Indica.

Botanica Indica is being developed as a scientifically grounded botanical intelligence and biodiversity technology platform focused initially on India.

The project brings together botanical knowledge, taxonomy, geographic information, observations, evidence, artificial intelligence, and human expertise.

Contributions are welcome across software, science, data, documentation, research, design, testing, and community development.

---

## 1. Our Contribution Principles

Contributors should help maintain the following principles:

- Scientific credibility
- Evidence over false certainty
- Data provenance
- Transparent uncertainty
- Human expertise and expert validation
- Privacy and security by design
- Accessibility and inclusion
- Open standards where practical
- Technology independence
- Modular and reusable architecture
- Reproducibility
- Responsible use of artificial intelligence

AI-generated output must not automatically be treated as scientifically validated information.

---

## 2. What You Can Contribute

Contributions may include:

### Software

- Application code
- APIs
- Backend services
- Mobile functionality
- Web functionality
- Infrastructure
- Testing
- Performance improvements
- Security improvements

### Scientific and Botanical Work

- Taxonomic information
- Species records
- Synonym relationships
- Morphological information
- Geographic information
- References
- Scientific corrections
- Expert review

### Data

- Observations
- Photographs
- Local and common names
- Field notes
- Geographic information
- Structured datasets
- Data quality improvements

### Artificial Intelligence and Machine Learning

- Training datasets
- Model development
- Evaluation
- Benchmarking
- Model documentation
- Error analysis
- Human-in-the-loop workflows

### Documentation

- Technical documentation
- Scientific documentation
- User documentation
- Tutorials
- Research notes
- Architecture documentation

### Design and UX

- User-interface design
- Accessibility improvements
- Interaction design
- Information architecture
- Design-system contributions

---

## 3. Scientific Validation

Community contribution does not automatically mean scientific validation.

The platform should distinguish between different states of information, including:

- Submitted
- AI identified
- User confirmed
- Expert reviewed
- Scientifically verified

Contributors should not represent an unverified observation or AI prediction as scientifically established fact.

Where appropriate, corrections should include supporting evidence or references.

---

## 4. Data Provenance

For important scientific and data records, provenance should be maintained wherever practical.

Contributions should identify, where applicable:

- Source
- Contributor
- Date
- License
- Validation status
- Taxonomic version
- Relevant references

Contributors must not add third-party data, photographs, text, or datasets unless their use is permitted by the applicable license or permission.

Do not assume that information available on the internet is freely reusable.

---

## 5. Photographs and Media

Only contribute photographs and other media that you have the right to contribute.

When applicable, provide:

- Creator/photographer
- Source
- License
- Attribution requirements

Do not upload copyrighted material simply because it is publicly accessible online.

---

## 6. Taxonomy and Scientific Information

Taxonomic information can change over time.

When contributing taxonomic information:

- Prefer authoritative sources.
- Preserve accepted names and synonyms where relevant.
- Record the source and version where practical.
- Avoid silently replacing historical information.
- Document significant taxonomic changes.

Conflicting taxonomic treatments should be documented rather than hidden.

---

## 7. Artificial Intelligence

AI is a component of Botanica Indica, not the sole authority.

AI systems may generate:

- Identification candidates
- Similarity results
- Classifications
- Extracted information
- Recommendations for review

These outputs should be treated according to their evidence and validation status.

The platform should support an explicit state where the available evidence is insufficient to identify a species reliably.

An "I don't know" or equivalent result is acceptable when evidence is insufficient.

---

## 8. Geographic and Sensitive Data

Contributors should consider the sensitivity of geographic information.

Some biodiversity observations may require additional protection because publishing precise locations could create conservation risks.

Potential safeguards may include:

- Generalized locations
- Obscured coordinates
- Delayed publication
- Restricted access
- Controlled data sharing

Do not intentionally expose sensitive location information without appropriate authorization or policy.

---

## 9. Privacy and Security

Do not commit:

- Passwords
- API keys
- Access tokens
- Private credentials
- Personal authentication information
- Production secrets

Security vulnerabilities should not be publicly disclosed through ordinary issues when private reporting is available.

Contributors should follow secure development practices and avoid unnecessarily collecting or exposing personal information.

---

## 10. Technology Independence

Botanica Indica is intended to remain independent of any single programming language, framework, cloud provider, database, AI model, or external identification provider.

Technical contributions should therefore:

- Prefer documented interfaces and standards.
- Avoid unnecessary vendor lock-in.
- Keep contracts and interfaces explicit.
- Separate domain logic from infrastructure where practical.
- Consider portability when introducing major dependencies.

Technology choices should be justified by requirements rather than preference alone.

---

## 11. Development Workflow

**Current project-owner directive:** no new branches may be created during the current development period, and the repository must be reduced to no more than seven branches in total. Until the project owner explicitly lifts this directive:

1. Do not create a feature, fix, research, review or other new branch.
2. Use an existing workstream branch only when the work genuinely belongs to that workstream and the project owner has directed or approved its use.
3. Do not place unrelated work on a shared branch merely to avoid creating a branch.
4. If no existing branch is suitable, stop and request explicit project-owner authorization before creating one.
5. Preserve the source branch, PR and commit provenance for any consolidation work.

This current directive takes precedence over the general workflow below. The live branch inventory and approved consolidation destinations are recorded in `docs/governance/BRANCH-INVENTORY-AND-CONSOLIDATION-REGISTER.md`. The project operating instructions are in `docs/governance/AI-PROJECT-OPERATING-PROMPT.md`.

Once the project owner formally lifts the no-new-branches directive, the normal code-contribution workflow is:

1. Create a temporary task branch from `develop`, using an approved prefix and the repository's current branch policy.
2. Make the smallest coherent change possible.
3. Add or update tests where appropriate.
4. Update relevant documentation.
5. Review your own changes.
6. Open a pull request to the approved target branch.
7. Describe the purpose and impact of the change, evidence, tests and known limitations.
8. Address review feedback.
9. Merge only after the required checks and reviews have been completed.
10. Retire the temporary branch safely after verifying that required content and history are preserved.

The branch policy document remains proposed for adoption; this current no-new-branches instruction is an explicit project-owner directive and is already binding for this work.

---

## 12. Pull Requests

A pull request should explain:

- What was changed
- Why it was changed
- How it was implemented
- How it was tested
- Any known limitations
- Any scientific or data implications
- Any licensing implications

For significant architectural changes, contributors should reference the relevant Architecture Decision Record (ADR), when one exists.

---

## 13. Issues and Discussions

Use issues for:

- Bugs
- Feature requests
- Technical problems
- Scientific corrections
- Data-quality problems
- Documentation problems

Use discussions, when enabled, for broader questions, proposals, research topics, and community conversations.

Before opening a new issue, check whether a related issue already exists.

---

## 14. Scientific Corrections

Scientific corrections are especially valuable.

When reporting a correction, provide supporting evidence whenever possible, such as:

- Taxonomic references
- Published literature
- Herbarium records
- Authoritative databases
- Expert references
- Relevant institutional sources

Corrections may require expert review before being incorporated into validated platform data.

---

## 15. Code Quality

Contributors should aim for code that is:

- Readable
- Testable
- Maintainable
- Documented where necessary
- Secure
- Consistent with project architecture

Avoid unnecessary complexity.

New abstractions should have a clear reason to exist.

---

## 16. Documentation

Documentation is considered part of the project.

When a contribution changes:

- Architecture
- APIs
- Data models
- Scientific workflows
- User workflows
- Development setup
- Security practices

the relevant documentation should be updated as part of the same contribution.

---

## 17. Architecture Decisions

Significant architectural decisions should be documented.

Where appropriate, an Architecture Decision Record should capture:

- Decision
- Context
- Alternatives considered
- Advantages
- Disadvantages
- Consequences
- Date
- Decision status

This helps preserve project knowledge as contributors and technologies change.

---

## 18. Reproducibility

Scientific and machine-learning contributions should aim to be reproducible.

Where practical, document:

- Dataset versions
- Source datasets
- Transformation steps
- Model versions
- Training configuration
- Evaluation methodology
- Software dependencies
- Relevant random seeds or reproducibility controls

---

## 19. Code of Conduct

All contributors are expected to interact respectfully and constructively.

Disagreement about technical, scientific, or architectural decisions is expected.

Criticism should focus on ideas, evidence, implementation, and outcomes rather than individuals.

A separate Code of Conduct may be introduced as the community grows.

---

## 20. License and contributor terms

The repository currently contains an Apache License 2.0 file for the repository's software. Its presence must not be interpreted as licensing third-party datasets, photographs, publications, user media, trademarks or other material that STF does not own or have authority to license.

**Formal contributor terms have not yet been adopted.** STF has not selected a Developer Certificate of Origin (DCO), Contributor License Agreement (CLA), or another complete contributor agreement. This guide is informational; it is not itself a copyright assignment, a complete contributor agreement, or a blanket permission for redistribution, commercial use, research use or AI/ML training.

Before submitting material, ensure that you are its creator or are otherwise authorised to submit it, and identify any third-party license, permission, attribution or restriction that applies. A pull request or upload must not be treated as proof that the submitter owns all included rights.

Code, documentation, datasets, photographs, scientific content and other assets may require different terms. Any permission for AI/ML training, fine-tuning or embedding use must be assessed separately and must not be inferred from a general contribution or display permission.

Until formal contributor terms are approved and published, STF may request evidence of rights or defer inclusion of a contribution where the rights basis is unclear. Broad external contribution solicitation should wait for reviewed contributor terms.

---

## 21. Questions

If you are unsure whether a contribution is appropriate, open a discussion or issue describing:

- What you want to contribute
- Where it came from
- What license or permission applies
- How you believe it should be used

When in doubt, preserve provenance and ask before importing external material.

---

Thank you for helping build an open, scientifically responsible, and reusable botanical intelligence platform.
