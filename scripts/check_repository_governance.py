#!/usr/bin/env python3
"""Repository governance checks for Botanica Indica."""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ALLOWED_PREFIXES = (
    "feature/", "fix/", "docs/", "research/",
    "governance/", "test/", "release/",
    "proposal/", "strategy/", "review/",
)

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


def is_grandfathered_main_pr(pr_number: int | None, head: str) -> bool:
    return pr_number is not None and LEGACY_MAIN_PR_HEADS.get(pr_number) == head


def tracked_markdown() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "*.md", "**/*.md"],
        check=True, capture_output=True, text=True,
    )
    paths = sorted({Path(line) for line in result.stdout.splitlines() if line})
    return [p for p in paths if p.is_file()]


def check_fences(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    active_char: str | None = None
    active_length = 0
    active_line = 0
    backtick = chr(96)
    pattern = re.compile(r"^\s{0,3}(" + re.escape(backtick) + r"{3,}|~{3,})(.*)$")
    for number, line in enumerate(text.splitlines(), start=1):
        match = pattern.match(line)
        if not match:
            continue
        marker = match.group(1)
        char, length = marker[0], len(marker)
        if active_char is None:
            active_char, active_length, active_line = char, length, number
        elif char == active_char and length >= active_length:
            active_char, active_length, active_line = None, 0, 0
    if active_char is not None:
        errors.append(
            f"{path}:{active_line}: unclosed Markdown fence "
            f"({active_char * active_length})"
        )
    return errors


def check_relative_links(path: Path, text: str) -> list[str]:
    warnings: list[str] = []
    pattern = re.compile(r"!?\\[[^\\]]*\\]\\(([^)]+)\\)")
    for match in pattern.finditer(text):
        raw = match.group(1).strip().split()[0].strip("<>")
        if not raw or raw.startswith(("#", "http://", "https://", "mailto:", "data:")):
            continue
        parsed = urlsplit(raw)
        if parsed.scheme or parsed.netloc:
            continue
        target = unquote(parsed.path)
        if target and not (path.parent / target).resolve().exists():
            warnings.append(f"{path}: unresolved relative link: {raw}")
    return warnings


def check_routing(
    base: str | None,
    head: str | None,
    body: str | None,
    pr_number: int | None = None,
) -> list[str]:
    if not base or not head:
        return []
    errors: list[str] = []
    if base == "develop":
        if head in {"main", "develop", "staging"}:
            errors.append("PRs into develop must come from a temporary task branch.")
        elif not head.startswith(ALLOWED_PREFIXES):
            errors.append(
                "PR source branch must use an approved temporary prefix: "
                + ", ".join(ALLOWED_PREFIXES)
            )
    elif base == "staging":
        if head != "develop":
            errors.append("Only develop may be promoted directly into staging.")
    elif base == "main":
        if head == "staging":
            pass
        elif head.startswith("fix/"):
            if "Emergency hotfix exception:" not in (body or ""):
                errors.append(
                    "A fix/* PR directly into main must document "
                    "'Emergency hotfix exception:' in its PR description."
                )
        elif not is_grandfathered_main_pr(pr_number, head):
            errors.append(
                "Only staging promotion or a documented fix/* emergency hotfix "
                "may target main. Exact pre-existing PR/head pairs are temporarily "
                "grandfathered; new direct-to-main PRs are rejected."
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="")
    parser.add_argument("--head", default="")
    parser.add_argument("--body", default="")
    parser.add_argument("--number", type=int, default=None)
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    files = tracked_markdown()
    for path in files:
        content = path.read_text(encoding="utf-8")
        errors.extend(check_fences(path, content))
        warnings.extend(check_relative_links(path, content))
    errors.extend(check_routing(args.base, args.head, args.body, args.number))

    if args.base == "main" and is_grandfathered_main_pr(args.number, args.head):
        warnings.append(
            f"PR #{args.number} is grandfathered for routing only; this is not merge approval."
        )
    print(f"Checked {len(files)} tracked Markdown files.")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"Governance checks failed with {len(errors)} error(s).")
        return 1
    print("Markdown fence and PR routing checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
