#!/usr/bin/env python3
"""Repository governance checks for Botanica Indica.

The branch inventory is a dated allowlist of branches already present when
this control was introduced. Remove retired branches from the allowlist only
after the required preservation and owner-approval gates have been satisfied.
Adding a branch requires explicit project-owner authorization.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
from urllib.request import Request, urlopen

ALLOWED_PREFIXES = (
    "feature/", "fix/", "docs/", "research/",
    "governance/", "test/", "release/",
    "proposal/", "strategy/", "review/",
)
LONG_LIVED_BRANCHES = frozenset({"main", "develop", "staging"})
MAX_BRANCHES = 7

# Live baseline verified on 21 November 2026. This is an allowlist, not
# authorization to create branches. Remove entries only after safe retirement.
KNOWN_REPOSITORY_BRANCHES = frozenset({
    "main",
    "develop",
    "staging",
    "docs/adr-011-stf-ecosystem-boundaries",
    "docs/asset-specific-licensing-policy",
    "docs/canonical-task-03-04-baselines",
    "docs/full-product-vision-capability-blueprint",
    "docs/full-system-architecture-and-repo-engineering-plan",
    "docs/repository-audit-and-ai-operating-standard",
    "docs/requirements-traceability-register",
    "docs/task-05-data-architecture",
    "docs/task-05-data-dictionary",
    "docs/task-05c-logical-data-model",
    "docs/task-05c-logical-database-model",
    "docs/task-05d-logical-model-validation",
    "docs/task-05d-logical-model-validation-v2",
    "docs/task-05d-logical-model-validation-v3",
    "governance/branch-lifecycle-policy",
    "governance/stf-organisational-readiness-review",
    "proposal/bengaluru-urban-biodiversity-feasibility-pilot",
    "research/bengaluru-pilot-site-selection",
    "review/scientific-data-model-review-pack",
    "strategy/naturetech-biodiversity-conservation-impact",
})

# Exact legacy exceptions: both PR number and head branch must match.
# Remove an entry when its PR is retargeted or closed.
LEGACY_MAIN_PR_HEADS = {
    1: "docs/asset-specific-licensing-policy",
    2: "docs/adr-011-stf-ecosystem-boundaries",
    3: "docs/task-05-data-architecture",
    4: "docs/task-05-data-dictionary",
    5: "docs/task-05c-logical-data-model",
    8: "strategy/naturetech-biodiversity-conservation-impact",
    9: "review/scientific-data-model-review-pack",
    13: "proposal/bengaluru-urban-biodiversity-feasibility-pilot",
    14: "research/bengaluru-pilot-site-selection",
}

# Exact, temporary exceptions for existing stacked PRs. The PR number, base
# and head must all match. Remove entries when the corresponding PR is closed
# or retargeted. This does not authorize new stacked PRs.
STACKED_PR_ROUTES = {
    11: ("docs/task-05c-logical-data-model", "docs/task-05d-logical-model-validation-v3"),
    12: ("strategy/naturetech-biodiversity-conservation-impact", "governance/stf-organisational-readiness-review"),
    21: ("review/scientific-data-model-review-pack", "docs/task-05c-logical-database-model"),
    22: ("review/scientific-data-model-review-pack", "docs/task-05d-logical-model-validation"),
    23: ("review/scientific-data-model-review-pack", "docs/task-05d-logical-model-validation-v2"),
}

# Empty by default. Add an exact PR/head pair only after explicit project-owner
# authorization has been recorded in the repository. PR-body text is not proof.
OWNER_APPROVED_HOTFIX_PR_HEADS: dict[int, str] = {}

BACKTICK = chr(96)
OPEN_FENCE_RE = re.compile(
    r"^( {0,3})(" + re.escape(BACKTICK) + r"{3,}|~{3,})(.*)$"
)
CLOSE_FENCE_RE = re.compile(
    r"^ {0,3}(" + re.escape(BACKTICK) + r"{3,}|~{3,})[ \t]*$"
)
INLINE_LINK_RE = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^)\s]+)(?:\s+[^)]*)?\)")


def is_grandfathered_main_pr(pr_number: int | None, head: str) -> bool:
    return pr_number is not None and LEGACY_MAIN_PR_HEADS.get(pr_number) == head


def is_owner_approved_hotfix(pr_number: int | None, head: str) -> bool:
    return pr_number is not None and OWNER_APPROVED_HOTFIX_PR_HEADS.get(pr_number) == head


def tracked_markdown() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "*.md", "**/*.md"],
        check=True, capture_output=True, text=True,
    )
    paths = sorted({Path(line) for line in result.stdout.splitlines() if line})
    return [p for p in paths if p.is_file()]


def check_fences(path: Path, text: str) -> list[str]:
    """Check CommonMark fenced blocks (not a complete Markdown parser)."""
    errors: list[str] = []
    active_char: str | None = None
    active_length = 0
    active_line = 0

    for number, line in enumerate(text.splitlines(), start=1):
        if active_char is None:
            match = OPEN_FENCE_RE.match(line)
            if not match:
                continue
            marker, info = match.group(2), match.group(3)
            char, length = marker[0], len(marker)
            # CommonMark forbids backticks in a backtick fence's info string.
            if char == BACKTICK and BACKTICK in info:
                continue
            active_char, active_length, active_line = char, length, number
            continue

        closing = CLOSE_FENCE_RE.match(line)
        if closing:
            marker = closing.group(1)
            if marker[0] == active_char and len(marker) >= active_length:
                active_char, active_length, active_line = None, 0, 0

    if active_char is not None:
        errors.append(
            f"{path}:{active_line}: unclosed Markdown fence "
            f"({active_char * active_length})"
        )
    return errors


def check_relative_links(path: Path, text: str) -> list[str]:
    """Warn on missing inline relative links; this is intentionally advisory.

    Reference-style links, heading anchors, and full CommonMark parsing are
    outside this lightweight check's scope.
    """
    warnings: list[str] = []
    for match in INLINE_LINK_RE.finditer(text):
        raw = match.group(1).strip()
        if raw.startswith("<") and raw.endswith(">"):
            raw = raw[1:-1]
        if not raw or raw.startswith("#"):
            continue
        parsed = urlsplit(raw)
        if parsed.scheme or parsed.netloc:
            continue
        target = unquote(parsed.path)
        # Root-relative site paths and fragment-only links are not filesystem
        # relative links and are intentionally not assessed here.
        if not target or target.startswith("/"):
            continue
        if not (path.parent / target).resolve().exists():
            warnings.append(f"{path}: unresolved relative link: {raw}")
    return warnings


def check_routing(
    base: str | None,
    head: str | None,
    pr_number: int | None = None,
) -> list[str]:
    if not base or not head:
        return []

    if base == "develop":
        if head in LONG_LIVED_BRANCHES:
            return ["PRs into develop must come from a temporary task branch."]
        if not head.startswith(ALLOWED_PREFIXES):
            return [
                "PR source branch must use an approved temporary prefix: "
                + ", ".join(ALLOWED_PREFIXES)
            ]
        return []

    if base == "staging":
        if head != "develop":
            return ["Only develop may be promoted directly into staging."]
        return []

    if base == "main":
        if head == "staging":
            return []
        if is_grandfathered_main_pr(pr_number, head):
            return []
        if is_owner_approved_hotfix(pr_number, head) and head.startswith("fix/"):
            return []
        return [
            "Only staging promotion, an exact grandfathered legacy PR/head pair, "
            "or an explicitly owner-authorized hotfix PR/head pair may target main. "
            "PR-description text is not authorization."
        ]

    if STACKED_PR_ROUTES.get(pr_number) == (base, head):
        return []

    return [
        f"Unsupported PR base branch '{base}'. Only main, develop, staging, "
        "or an exact pre-existing stacked-PR exception is permitted."
    ]


def check_branch_inventory(branches: list[str]) -> tuple[list[str], list[str]]:
    """Reject unknown repository branches; report the seven-branch excess.

    The excess is a warning while preservation/retirement PRs are being
    resolved. Making it a hard failure now would deadlock that cleanup work.
    """
    actual = set(branches)
    errors: list[str] = []
    warnings: list[str] = []

    unknown = sorted(actual - KNOWN_REPOSITORY_BRANCHES)
    if unknown:
        errors.append(
            "Unregistered repository branch(es) detected; no-new-branches "
            "directive requires explicit owner authorization before use: "
            + ", ".join(unknown)
        )

    missing_long_lived = sorted(LONG_LIVED_BRANCHES - actual)
    if missing_long_lived:
        errors.append(
            "Required long-lived branch(es) missing: " + ", ".join(missing_long_lived)
        )

    if len(actual) > MAX_BRANCHES:
        warnings.append(
            f"Repository has {len(actual)} branches; immediate ceiling is "
            f"{MAX_BRANCHES}. Preserve, resolve and retire branches safely."
        )
    return errors, warnings


def fetch_repository_branches(repository: str) -> list[str]:
    """Fetch every branch from the public GitHub API without a credential."""
    if not repository or "/" not in repository:
        raise ValueError("GITHUB_REPOSITORY must be in owner/repository form.")

    encoded_repo = quote(repository, safe="/")
    branches: list[str] = []
    page = 1
    while True:
        request = Request(
            f"https://api.github.com/repos/{encoded_repo}/branches"
            f"?per_page=100&page={page}",
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "botanica-indica-repository-governance",
            },
        )
        with urlopen(request, timeout=20) as response:
            payload = json.loads(response.read().decode("utf-8"))
        if not isinstance(payload, list):
            raise RuntimeError("GitHub branches API returned an unexpected response.")
        if any(
            not isinstance(item, dict) or not isinstance(item.get("name"), str) or not item["name"]
            for item in payload
        ):
            raise RuntimeError("GitHub branches API returned a malformed branch entry.")
        branches.extend(item["name"] for item in payload)
        if len(payload) < 100:
            break
        page += 1
    return branches


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="")
    parser.add_argument("--head", default="")
    parser.add_argument("--number", type=int, default=None)
    parser.add_argument(
        "--check-branch-inventory",
        action="store_true",
        help="Fetch live repository branches and check the approved inventory.",
    )
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    files = tracked_markdown()
    for path in files:
        content = path.read_text(encoding="utf-8")
        errors.extend(check_fences(path, content))
        warnings.extend(check_relative_links(path, content))

    errors.extend(check_routing(args.base, args.head, args.number))

    if args.check_branch_inventory:
        repository = os.environ.get("GITHUB_REPOSITORY", "")
        try:
            branches = fetch_repository_branches(repository)
            inventory_errors, inventory_warnings = check_branch_inventory(branches)
            errors.extend(inventory_errors)
            warnings.extend(inventory_warnings)
            print(f"Live GitHub branch inventory: {len(branches)} branches.")
        except Exception as exc:  # fail closed if live inventory cannot be verified
            errors.append(f"Unable to verify live branch inventory: {exc}")

    print(f"Checked {len(files)} tracked Markdown files.")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"Governance checks failed with {len(errors)} error(s).")
        return 1
    print("Markdown fence, PR routing and requested branch-inventory checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
