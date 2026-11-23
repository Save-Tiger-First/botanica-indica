# Graphify — Repository Intelligence Tooling Adoption Assessment

- **Document ID:** STF-BI-ENG-TOOL-002
- **Version:** 0.1 — Proposed evaluation and adoption plan
- **Prepared:** 23 November 2026
- **Status:** Proposed for project-owner review; not an approved architecture decision or implementation authorization
- **Repository:** Save-Tiger-First/botanica-indica
- **Working branch:** docs/full-system-architecture-and-repo-engineering-plan (existing branch; PR #20)
- **Decision authority:** Save Tiger First project owner
- **Scope:** Use of Graphify for repository understanding, engineering analysis and developer workflow
- **Out of scope:** Botanica Indica production runtime, scientific authority, taxonomic validation, biodiversity data ingestion and authorization to upload restricted data

---

## 1. Executive recommendation

Evaluate and adopt Graphify initially as an **optional, local-first engineering and repository-intelligence tool**. Do not make it a runtime dependency of Botanica Indica, a scientific system of record, a taxonomic authority or a substitute for human review.

The most suitable initial use cases are:

1. Build a navigable map of the repository's architecture, ADRs, requirements, scientific-model documents, tests and source code as implementation develops.
2. Trace links between requirements, design decisions, modules, APIs and tests.
3. Help developers understand unfamiliar code and bounded change impact.
4. Support PR triage and dependency review after meaningful application code exists.
5. Produce reviewable architecture maps and a controlled Markdown knowledge index.

**Preferred starting route:** open-source Graphify CLI on a separate local clone or Git worktree, with a local Ollama model for semantic extraction of Markdown and other non-code material. Start with one existing workstream branch, not all branches at once.

The available Graphify workspace currently indexes Botanica Indica at main commit 6f2f51da093caf8183fde386dbec707cc6046d27. Its graph reports 17 nodes and 29 edges, and the ranked source-file result contains only README.md. This is a small README-level graph, not a repository-wide map of ADRs, PRD, architecture and scientific review material. It must not be represented as comprehensive.

## 2. The three supplied repositories

The supplied URLs have different purposes and should not be treated as three software dependencies.

| Repository | Verified purpose | Current inspected revision | Recommended use |
|---|---|---|---|
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Open-source Python package/CLI and agent skill that builds and queries a knowledge graph | Default branch v8; branch commit a3db62f680cde2cf516642bbfef1e3ab33fd30d8; repository metadata reports Apache-2.0 | Install as optional developer tooling; do not copy its implementation into Botanica Indica |
| [Graphify-Labs/docs](https://github.com/Graphify-Labs/docs) | Source for the official Graphify documentation site | main commit 1b5c264c6447d6b0d20199221e8e13391650401a; repository metadata reports MIT | Use as the operational reference for installation, CLI, ignore rules, local model providers and MCP |
| [Graphify-Labs/.github](https://github.com/Graphify-Labs/.github) | Organization profile repository | main commit c5e95a8edd645d44f44be7421fa433db8e05b08a | No integration required; inspected tree contains the profile README and image assets, not reusable workflows or project tooling |

The Graphify source repository's default branch is v8, not main. Pin and record the installed CLI version during evaluation. The official Python package name is graphifyy (two trailing y characters); the installed command is graphify. Avoid similarly named packages that are not published by Graphify Labs.

The Graphify docs repository is documentation source, not a package Botanica Indica needs to install. The special .github repository is not an organization-wide GitHub Actions library in the inspected state.

## 3. What Graphify can and cannot do for Botanica Indica

### Suitable uses

- Map code symbols and source relationships using local tree-sitter parsing.
- Represent documented concepts, ADR/RFC references and selected Markdown/PDF material through semantic extraction.
- Show extracted versus inferred/ambiguous relationships.
- Query a graph, explain a node, trace a path and inspect affected dependencies.
- Generate HTML, JSON, Markdown reports and optional wiki-style exports.
- Expose a local graph through an MCP server to compatible coding agents.
- Potentially support PR impact review when the repository contains real code and graph-linked tests.

### Not a substitute for

- Taxonomist or botanical expert review.
- Validation of scientific claims, plant identifications, taxonomic nomenclature or source authority.
- Rights, licensing, consent, privacy or community-governance assessment.
- Formal requirements traceability or accepted ADRs.
- Reproducible automated tests, static analysis, security scanning or CI status checks.
- A canonical data model, database, provenance registry or scientific system of record.

Graph edges labelled INFERRED are useful navigation hypotheses, not verified project facts. Even an EXTRACTED edge only confirms that a relationship was found in a source; it does not prove that the source itself is correct or approved.

## 4. Fit with accepted Botanica Indica architecture

This proposal is consistent with the current direction in accepted ADR-001: technology independence, modularity, documented contracts and replaceable tooling. Graphify should remain outside the product runtime.

| Existing project principle | Safe Graphify role |
|---|---|
| Modular, contract-driven architecture | Map module and contract relationships once implementation exists |
| TypeScript platform/API direction | Analyse TypeScript dependencies and call relationships |
| Python AI/ML direction | Analyse Python packages, pipelines and tests |
| Dart/Flutter mobile direction | Map Dart/Flutter source and client dependencies when present |
| PostgreSQL/PostGIS candidate | Optionally inspect schema files or a deliberately sanitized schema export; never connect it to production by default |
| Provenance and taxonomic integrity | Navigate references to authoritative records; do not infer taxonomic truth |
| Sensitive-location and privacy safeguards | Exclude restricted datasets and metadata from all graph and model processing |
| Full-product requirements traceability | Help discover links; preserve the formal requirements register as the authority |

No change to ADR-001 through ADR-010 is proposed. No Graphify dependency should be added to the application package manifests or production deployment.

## 5. Data protection and processing modes

Graphify's own documentation distinguishes its local open-source CLI from its hosted service.

### 5.1 Local CLI

- Source-code parsing with tree-sitter is performed locally and does not require an LLM.
- Semantic extraction of Markdown, PDFs, images, transcripts and other non-code content uses a configured model backend.
- The documented Ollama backend can run locally without an API key.
- The local MCP server serves an existing graph; it does not need to make model calls.
- Graphify documents built-in sensitive-file filters and supports .graphifyignore and command-line exclusions.

For Botanica Indica, prefer local processing. If semantic extraction is enabled, explicitly select the local Ollama backend; do not rely on automatic provider detection because configured hosted API credentials may take precedence.

### 5.2 Hosted Graphify service

Graphify's current hosted-service security documentation states that repository graphs and content are stored by the service, and that code/content is sent to LLM subprocessors for results. It reports encryption in transit and at rest, no model training on customer code, AWS hosting in the United States, deletion/retention periods, and a SOC 2 Type II engagement that is in progress. These are vendor statements, not an independent compliance certification.

Do not connect non-public, personal, sensitive biodiversity or community-held material to the hosted service until STF has reviewed the current privacy policy, terms, subprocessors, DPA, retention/deletion process, data location and applicable Indian legal requirements. No conclusion about legal compliance is made by this desk assessment.

### 5.3 Minimum exclusion policy

Before scanning, exclude or quarantine:

- Credentials, API keys, tokens, private keys, .env files and local configuration secrets.
- Personal data, private correspondence, unpublished contributor information and account identifiers.
- Sensitive species coordinates, restricted locality data and exact nesting/collection sites.
- Community-held or traditional knowledge unless the relevant authority, rights, purpose and processing permissions have been established.
- Raw scans, photographs, manuscripts, audio/video or third-party source material whose rights and permitted processing purposes have not been assessed.
- Local caches, build outputs, generated data and unrelated archives.

A public GitHub repository is not a blanket authorization to process every file for every purpose.

## 6. Proposed pilot — no repository changes required

### Stage 0 — preparation

1. Use a separate local clone or detached Git worktree so the user's normal checkout is not disturbed.
2. Record the selected branch name, exact commit SHA, Graphify version, Python version, model/backend and scan configuration.
3. Review .gitignore, create a project-specific .graphifyignore locally, and verify exclusions before extraction.
4. Start with the existing PR #20 architecture workstream because it contains the architecture plan, roadmap, accepted ADR copies and architecture audit material. It is an existing branch; do not create a new branch.

### Stage 1 — local installation on Windows

Install uv if it is not already available:

    winget install astral-sh.uv

Install the official package in an isolated tool environment:

    uv tool install --python 3.12 graphifyy
    graphify --version

Install Ollama separately, obtain a suitable local model, and verify that Ollama is running. Graphify's documentation currently gives this example:

    ollama pull qwen2.5-coder:7b

From the local Botanica Indica checkout, run a bounded semantic extraction with the local backend:

    graphify extract . --backend ollama

For code-only extraction (no model calls), use:

    graphify extract . --code-only

The current main branch is predominantly documentation and has no verified application source tree. A code-only run on that branch will therefore be of limited value. The documentation-rich PR #20 workstream is the better first evaluation corpus.

Do not run a broad scan until the ignore rules and data classification have been checked. Do not commit generated graph outputs during the pilot.

### Stage 2 — inspect and validate output

Review:

- graphify-out/GRAPH_REPORT.md
- graphify-out/graph.html
- graphify-out/graph.json

Check whether the graph correctly connects:
- ADR-001 and other accepted ADRs to relevant architecture statements.
- Product requirements to proposed modules and contracts.
- Scientific-model decisions to their validation documents.
- Rights, privacy and sensitive-location controls to affected components.
- Each inferred edge against the cited source text.

Record false links, missing links, conflated document versions, duplicate concepts and misleading inferences. Graphify output is a navigation aid; the source documents remain authoritative.

### Stage 3 — expand by workstream, not by blindly merging branches

The repository has many open, divergent workstream branches. Build separate graph snapshots for the existing workstreams that are relevant to a review (for example PR #16, PR #20 and PR #9), each labelled with its exact commit SHA.

Do not combine graphs from divergent branches until node identity, duplicate file paths, source-version collisions and provenance are understood. In particular, successive Task 05C/05D versions must not be collapsed into a false single source of truth.

### Stage 4 — optional MCP access

If a local coding agent supports MCP, the local Graphify package can expose the generated graph through graphify-mcp over stdio. HTTP sharing is optional and requires deliberate authentication/network configuration.

The available ChatGPT Graphify workspace can also be queried, but its current Botanica Indica index is only README-level. Do not confuse this connected index with a completed local CLI pilot or a fully indexed repository.

### Stage 5 — later PR workflow

Once application code and tests exist, evaluate Graphify's PR-impact and dependency analysis on a small number of code PRs. Treat it as an additional reviewer signal, not a required status check or merge authority. Validate its findings against actual code, tests and human review before considering CI integration.

## 7. Suggested local ignore rules

Use a project-specific .graphifyignore and adapt it after reviewing the repository tree. Example starting rules:

    # Secrets and local credentials
    .env
    .env.*
    *.pem
    *.key
    *.p12
    *.pfx
    *.crt
    secrets/
    private/

    # Generated outputs and local data
    graphify-out/
    .cache/
    cache/
    tmp/
    temp/
    build/
    dist/

    # Restricted or sensitive material — refine to actual project paths
    data/restricted/
    data/sensitive-locations/
    data/community-restricted/
    data/unlicensed/

These patterns are illustrative. Confirm actual repository paths and ensure that no negation rule re-includes excluded files. The built-in secret filter is a secondary safeguard, not a substitute for explicit exclusions and review.

## 8. Acceptance criteria for the pilot

The pilot is successful only if:

1. The exact source branch and commit are recorded.
2. The installed Graphify version and model/backend are recorded.
3. No excluded or restricted material appears in the graph, cache, report or logs.
4. The graph identifies relevant architecture and governance concepts without merging conflicting document versions.
5. Extracted, inferred and ambiguous relationships remain distinguishable.
6. A human reviewer can trace every material graph claim to its source file and section.
7. The report identifies known omissions and limitations.
8. Re-running the same version/configuration on the same corpus produces a reviewable result.
9. The generated output is kept local until rights, security and usefulness are reviewed.
10. No accepted ADR, scientific model, product requirement, branch, PR or repository setting is changed by the pilot.

## 9. Risks and mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| Only a small subset of the repository is indexed | Major | Verify file inventory and graph source coverage before relying on it |
| Conflicting branch versions are conflated | Critical | Separate graph snapshots by exact branch/commit; do not merge blindly |
| Semantic extraction invents or overstates links | Major | Preserve confidence labels and require source-level human verification |
| Restricted data or secrets enter graph/model processing | Critical | Local-only processing, explicit ignore rules, secret review and output inspection |
| Graph output is mistaken for accepted architecture/science | Critical | Label it as derived tooling output; source documents and ADRs remain authoritative |
| Hosted-service retention/data location is unsuitable | Major | Prefer local CLI; conduct legal/security review before cloud use |
| Tool version changes alter graph output | Major | Record and pin versions/configuration for comparable reviews |
| CI integration creates false confidence or noisy gates | Major | Pilot as advisory only; do not make it a required check until validated |

## 10. Decision requested

**Recommendation:** approve a time-bounded, local-only evaluation of Graphify CLI on one existing workstream branch, beginning with PR #20. This approval would authorize only a local tooling experiment and report; it would not authorize:

- adding Graphify to the Botanica Indica production runtime;
- connecting the repository to Graphify Cloud;
- sending non-public or restricted material to any hosted model;
- committing generated graph output;
- adding CI gates or automated PR review requirements;
- changing accepted ADRs, the scientific model, product requirements or repository governance.

No Graphify installation, local extraction, MCP configuration, CI integration, hosted-service connection or repository code change is claimed as completed by this proposal.

## 11. Sources checked

**Graphify project sources (checked 23 November 2026):**

- Graphify source repository, default branch v8, commit a3db62f680cde2cf516642bbfef1e3ab33fd30d8: https://github.com/Graphify-Labs/graphify
- Graphify documentation repository, main, commit 1b5c264c6447d6b0d20199221e8e13391650401a: https://github.com/Graphify-Labs/docs
- Graphify Labs profile repository, main, commit c5e95a8edd645d44f44be7421fa433dbb8e05b08a: https://github.com/Graphify-Labs/.github
- Local CLI quickstart: https://docs.graphify.com/open-source/quickstart
- CLI configuration and commands: https://docs.graphify.com/open-source/configuration/cli
- Ignoring files and limits: https://docs.graphify.com/open-source/configuration/ignoring-files
- LLM providers and local Ollama: https://docs.graphify.com/open-source/configuration/llm-providers
- Local MCP server: https://docs.graphify.com/open-source/mcp-server
- Hosted-service security and data handling: https://docs.graphify.com/platform/support/security
- Graphify source architecture: https://github.com/Graphify-Labs/graphify/blob/v8/ARCHITECTURE.md
- Graphify source security threat model: https://github.com/Graphify-Labs/graphify/blob/v8/SECURITY.md

**Botanica Indica sources checked:**

- Accepted ADR-001, main, blob a7d3b5c6ec55278c8af70d2e25521153f7f766ad.
- Full System Architecture and Repository Engineering Plan, PR #20 branch, blob 91fb02be87b42df51f92106f90fd536a01a5b902.
- Master Project Roadmap and Status, PR #20 branch, blob 60fba1bdb5d2b3fe299847225d21aee18641ad48.
- Product and Architecture Baseline Audit, PR #20 branch, blob 0405e8e4ab331c4987f6b28c3cb4ccb57c733adf.
- Current Graphify-connected Botanica Indica graph, indexed at main commit 6f2f51da093caf8183fde386dbec707cc6046d27, 17 nodes / 29 edges / one source file (README.md).

---

**Status summary:** This is a tooling adoption proposal. The local pilot is recommended but not yet executed. No product architecture, scientific decision, repository setting or branch lifecycle decision is changed.


## 12. Connected Graphify workspace capability check — 23 November 2026

This addendum distinguishes the hosted/connected Graphify workspace from the separately installed open-source Graphify CLI.

### 12.1 Verified workspace constraints

The connected Graphify workspace reports:

- Repository: `Save-Tiger-First/botanica-indica`
- Default branch: `main`
- Workspace repository status: ready and queryable
- Indexed nodes: **17**
- Indexed source coverage: `README.md` only
- Workspace plan note: on the Free plan, only `README.md` is indexed from a repository's documents; a documentation-only repository is therefore indexed from its README alone.

This explains why querying the connected Graphify workspace cannot yet provide a meaningful graph of the ADRs, PRD, architecture, scientific-model review pack or requirements register. The limitation is workspace-plan coverage, not evidence that those repository documents are absent.

### 12.2 Automated pull-request review status

The Graphify review-status query returned no review record for PR #16 or PR #20. Therefore:

- No Graphify automated review of either PR is verified.
- Do not claim Graphify has reviewed, approved, rejected or commented on either PR.
- The connected Graphify workspace's code-context tools and its optional automated PR-review feature are distinct capabilities; availability of the former does not prove the latter is enabled or active.

### 12.3 Revised operational recommendation

1. Continue to use the connected Graphify workspace only for limited README-level exploration while this plan limitation applies.
2. If broader repository-document analysis is required, evaluate the open-source CLI locally against a precisely pinned PR #20 branch commit and an explicit exclusion policy.
3. Keep local graph snapshots separate by branch and commit; do not merge graph data from divergent Task 05C/05D branches.
4. Treat Graphify output as a navigation aid and candidate relationship map, not as source-of-truth, formal traceability, scientific review or approval evidence.
5. Do not add Graphify to the product runtime, CI gates or hosted repository connections as part of this evaluation.

This addendum does not represent that Graphify CLI has been installed or run on a project-owner device. No local extraction, MCP setup, hosted-service connection, CI integration or product dependency was created.


## 13. Graphify release, security-policy and source-provenance recheck — 23 November 2026

**Status:** External-source recheck and proposal refinement only. No Graphify installation or execution is claimed.

### 13.1 Pin the published package to its source provenance

The latest PyPI release page checked on 23 November 2026 reports:

- Package: `graphifyy` (the CLI command is `graphify`)
- Latest release shown: **0.9.115**, uploaded 21 November 2026
- License expression: Apache-2.0
- Python requirement shown by PyPI: `>=3.11.5, <3.15`
- PyPI publishing attestation identifies source repository `Graphify-Labs/graphify` and source commit `3671f31124fdb1de4ec4e485b1bcd7059726a5f3`.
- Source distribution SHA-256 reported by PyPI: `1b8f1f8ffd246792ce5d8e9097611fa42c1f55a39e1283e799d37e26667d09a7`.

The repository default branch is `v8`, whose head was independently fetched as `a3db62f680cde2cf516642bbfef1e3ab33fd30d8`. A Git comparison showed that the PyPI-attested source commit `3671f31124fdb1de4ec4e485b1bcd7059726a5f3` is four commits ahead of that fetched branch head. Consequently, the previous statement that the inspected v8 branch head and latest package source were the same revision would be inaccurate. For a reproducible pilot, pin the package version and record the PyPI attested source commit and artifact checksum; do not rely on the moving branch name alone.

### 13.2 Security-policy version discrepancy resolved by source pinning

The `SECURITY.md` at the fetched v8 branch head `a3db62f680cde2cf516642bbfef1e3ab33fd30d8` still lists `0.3.x` as supported. This is stale relative to the latest package line.

The `SECURITY.md` fetched at the PyPI-attested 0.9.115 source commit `3671f31124fdb1de4ec4e485b1bcd7059726a5f3` lists **Latest 0.9.x** as supported and versions below 0.9 as unsupported. Its threat model also documents additional controls, including source-content prompt-injection handling, credential-shaped text redaction before graph persistence, symlink-safe ingestion and guarded destructive uninstall.

The source discrepancy is material. For the proposed pilot:
- use only the exact PyPI release whose provenance was checked;
- retain the artifact checksum and source commit in the local experiment record;
- review the security policy at that exact source commit, not a stale branch snapshot;
- recheck the package, provenance and security policy before any later upgrade.

These are upstream maintainer/project statements, not an independent security audit or guarantee that all attacks are prevented.

### 13.3 Processing and logging implications for Botanica Indica

The current v8 README and the attested 0.9.115 source documentation describe distinct processing paths:

- Tree-sitter source-code extraction is local and does not require a model API.
- Semantic extraction of Markdown, PDFs and images uses the configured assistant/model backend. A local Ollama backend is available when deliberately configured.
- Graphify query/path/explain and MCP graph-query calls write query metadata to a local JSONL log by default. The documented log includes timestamps, questions, corpus, returned-node counts and duration; full subgraph responses are not stored by default.
- `GRAPHIFY_QUERY_LOG_DISABLE=1` opts out of query logging, or `GRAPHIFY_QUERY_LOG=/dev/null` silences the log path.

For this project, local-only processing remains preferred. Before any scan, explicitly set the backend, verify that no hosted provider is selected by automatic environment detection, and decide whether query logging should be disabled. The graph, reports, cache, logs and any exported graph must all be treated as derived project artifacts and inspected for secrets, personal data, sensitive biodiversity locations and restricted knowledge.

### 13.4 Current status of the three supplied repositories

| Repository | Freshly verified revision | Finding |
|---|---|---|
| `Graphify-Labs/graphify` | Default branch `v8`: `a3db62f680cde2cf516642bbfef1e3ab33fd30d8`; PyPI 0.9.115 source commit: `3671f31124fdb1de4ec4e485b1bcd7059726a5f3` | CLI/tooling source; use the versioned package and attested source, not a moving branch |
| `Graphify-Labs/docs` | `main`: `1b5c264c6447d6b0d20199221e8e13391650401a` | Documentation source; useful reference, not a Botanica runtime dependency |
| `Graphify-Labs/.github` | `main`: `c5e95a8edd645d44f44be7421fa433db8e05b08a` | Inspected tree contains profile README and image assets only; no reusable workflow or project tooling was found |

### 13.5 Revised recommendation and pilot gate

Retain the local CLI pilot proposal, but make reproducibility and source-provenance checks explicit acceptance conditions:

1. Pin `graphifyy==0.9.115` for the first experiment, subject to confirming Python compatibility on the machine that will run it.
2. Record the PyPI provenance commit and SHA-256 checksum above.
3. Use an isolated local clone/worktree at the exact PR #20 commit; do not scan a moving branch.
4. Keep a local `.graphifyignore` that excludes secrets, personal information, sensitive species coordinates, restricted community-held knowledge, unlicensed media, local caches and generated outputs.
5. Explicitly select local Ollama for semantic extraction if available; otherwise use code-only extraction and acknowledge that the documentation graph will be incomplete. Do not let ambient API keys silently select a hosted provider.
6. Disable or explicitly govern query logging and inspect generated graph/report/cache/log artifacts before retention or sharing.
7. Keep the graph local and uncommitted for the first pilot. The upstream recommendation to commit `graphify-out/` is not adopted automatically because Botanica Indica has stricter source-version and sensitive-data controls.
8. Evaluate graph usefulness against a small human-labelled set of known relationships across ADRs, PRD, architecture, traceability and scientific decision records. Measure both false links and missed links; do not treat graph coverage or edge confidence as truth.
9. Do not combine branch snapshots or use Graphify's inferred links to close requirements, approve an ADR, resolve a scientific dispute or authorize a merge.
10. Stop the pilot if excluded material appears in any generated artifact or if the backend, version, provenance or processing path cannot be established.

**Decision status:** local Graphify evaluation remains a proposal and has not been executed. No Graphify software has been installed on the project owner's device; no repository graph, MCP server, CI integration, cloud connection or production dependency has been created.

### 13.6 External sources checked

- PyPI `graphifyy` 0.9.115, release/provenance details (uploaded 21 November 2026): https://pypi.org/project/graphifyy/
- Attested source commit: https://github.com/Graphify-Labs/graphify/tree/3671f31124fdb1de4ec4e485b1bcd7059726a5f3
- Security policy at attested source commit: https://github.com/Graphify-Labs/graphify/blob/3671f31124fdb1de4ec4e485b1bcd7059726a5f3/SECURITY.md
- README at v8 branch: https://github.com/Graphify-Labs/graphify/blob/v8/README.md
- Graphify documentation repository: https://github.com/Graphify-Labs/docs/tree/main
- Graphify Labs profile repository: https://github.com/Graphify-Labs/.github/tree/main
