"""Regression tests for repository governance routing and Markdown checks."""
from pathlib import Path
import io
import json
import os
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_repository_governance import (  # noqa: E402
    ALLOWED_PREFIXES,
    KNOWN_REPOSITORY_BRANCHES,
    LEGACY_MAIN_PR_HEADS,
    LONG_LIVED_BRANCHES,
    MAX_BRANCHES,
    STACKED_PR_ROUTES,
    check_branch_inventory,
    check_fences,
    check_relative_links,
    check_routing,
    fetch_repository_branches,
    is_grandfathered_main_pr,
)


class RoutingTests(unittest.TestCase):
    def test_approved_prefixes_are_accepted_into_develop(self):
        for prefix in ALLOWED_PREFIXES:
            with self.subTest(prefix=prefix):
                self.assertEqual(check_routing("develop", prefix + "example", 100), [])

    def test_exact_legacy_main_pairs_are_grandfathered(self):
        for number, head in LEGACY_MAIN_PR_HEADS.items():
            with self.subTest(number=number):
                self.assertTrue(is_grandfathered_main_pr(number, head))
                self.assertEqual(check_routing("main", head, number), [])

    def test_legacy_allowlist_requires_exact_number_and_head(self):
        self.assertTrue(check_routing("main", "docs/asset-specific-licensing-policy", 999))
        self.assertTrue(check_routing("main", "docs/other-branch", 1))

    def test_new_direct_main_pr_is_rejected(self):
        self.assertTrue(check_routing("main", "docs/new-work", 100))

    def test_pr_body_text_is_not_an_authorization_input(self):
        with self.assertRaises(TypeError):
            check_routing(
                "main", "fix/urgent", 100,
                "Emergency hotfix exception: approved by owner",
            )
        self.assertTrue(check_routing("main", "fix/urgent", 100))

    def test_staging_promotion_and_hotfix_rules(self):
        self.assertEqual(check_routing("main", "staging", 100), [])
        self.assertTrue(check_routing("main", "fix/urgent", 100))

    def test_only_develop_promotes_to_staging(self):
        self.assertEqual(check_routing("staging", "develop", 100), [])
        self.assertTrue(check_routing("staging", "docs/change", 100))

    def test_long_lived_branches_cannot_target_develop(self):
        for head in LONG_LIVED_BRANCHES:
            self.assertTrue(check_routing("develop", head, 100))

    def test_unknown_base_is_default_denied(self):
        self.assertTrue(check_routing("temporary/base", "docs/task", 100))
        self.assertTrue(check_routing("release-candidate", "develop", 100))

    def test_exact_stacked_pr_routes_are_allowed(self):
        for number, (base, head) in STACKED_PR_ROUTES.items():
            with self.subTest(number=number):
                self.assertEqual(check_routing(base, head, number), [])

    def test_stacked_route_requires_exact_pr_base_and_head(self):
        base, head = STACKED_PR_ROUTES[11]
        self.assertTrue(check_routing(base, head, 999))
        self.assertTrue(check_routing(base, "docs/other-head", 11))
        self.assertTrue(check_routing("other/base", head, 11))


class BranchInventoryTests(unittest.TestCase):
    def test_current_baseline_has_23_branches(self):
        self.assertEqual(len(KNOWN_REPOSITORY_BRANCHES), 23)

    def test_current_baseline_reports_ceiling_as_warning(self):
        errors, warnings = check_branch_inventory(sorted(KNOWN_REPOSITORY_BRANCHES))
        self.assertEqual(errors, [])
        self.assertEqual(len(warnings), 1)
        self.assertIn(str(MAX_BRANCHES), warnings[0])

    def test_unknown_branch_is_rejected(self):
        errors, _ = check_branch_inventory(
            sorted(KNOWN_REPOSITORY_BRANCHES | {"feature/unapproved-new-branch"})
        )
        self.assertEqual(len(errors), 1)
        self.assertIn("feature/unapproved-new-branch", errors[0])

    def test_retired_branch_may_be_absent(self):
        branches = sorted(KNOWN_REPOSITORY_BRANCHES - {"docs/asset-specific-licensing-policy"})
        errors, _ = check_branch_inventory(branches)
        self.assertEqual(errors, [])

    def test_required_long_lived_branches_must_remain(self):
        branches = sorted(KNOWN_REPOSITORY_BRANCHES - {"staging"})
        errors, _ = check_branch_inventory(branches)
        self.assertTrue(any("staging" in error for error in errors))

    def test_seven_or_fewer_branches_has_no_ceiling_warning(self):
        branches = sorted(LONG_LIVED_BRANCHES | {
            "docs/repository-audit-and-ai-operating-standard",
            "docs/full-system-architecture-and-repo-engineering-plan",
            "review/scientific-data-model-review-pack",
            "strategy/naturetech-biodiversity-conservation-impact",
        })
        errors, warnings = check_branch_inventory(branches)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])


class MarkdownFenceTests(unittest.TestCase):
    def test_unclosed_fence_reports_opening_line(self):
        fence = chr(96) * 3
        errors = check_fences(Path("sample.md"), "before\n" + fence + "python\nprint('x')\n")
        self.assertEqual(len(errors), 1)
        self.assertIn("sample.md:2", errors[0])

    def test_backtick_and_tilde_fences_close(self):
        ticks = chr(96) * 3
        self.assertEqual(check_fences(Path("a.md"), ticks + "py\nx\n" + ticks * 2 + "\n~~~\ny\n~~~\n"), [])

    def test_mismatched_fence_does_not_close(self):
        ticks = chr(96) * 3
        errors = check_fences(Path("a.md"), "~~~\nx\n" + ticks + "\n")
        self.assertEqual(len(errors), 1)

    def test_closing_fence_must_have_only_trailing_whitespace(self):
        ticks = chr(96) * 3
        errors = check_fences(Path("a.md"), ticks + "\nx\n" + ticks + " not-closed\n")
        self.assertEqual(len(errors), 1)

    def test_four_space_indentation_is_not_a_fence(self):
        self.assertEqual(check_fences(Path("a.md"), "    " + chr(96) * 3 + "\n"), [])

    def test_backtick_info_string_cannot_contain_backticks(self):
        ticks = chr(96) * 3
        self.assertEqual(check_fences(Path("a.md"), ticks + "bad" + chr(96) + "info\ntext\n"), [])


class RelativeLinkTests(unittest.TestCase):
    def test_missing_relative_link_is_a_warning(self):
        warnings = check_relative_links(Path("docs/guide.md"), "[missing](not-here.md)")
        self.assertEqual(len(warnings), 1)
        self.assertIn("not-here.md", warnings[0])

    def test_existing_relative_link_is_not_a_warning(self):
        warnings = check_relative_links(
            Path("README.md"), "[script](scripts/check_repository_governance.py)"
        )
        self.assertEqual(warnings, [])

    def test_external_and_fragment_links_are_ignored(self):
        text = "[web](https://example.org) [mail](mailto:a@example.org) [anchor](#heading)"
        self.assertEqual(check_relative_links(Path("README.md"), text), [])

    def test_angle_bracket_link_with_spaces_is_supported(self):
        warnings = check_relative_links(
            Path("docs/guide.md"), "[file](<folder name/file.md>)"
        )
        self.assertEqual(len(warnings), 1)
        self.assertIn("folder name/file.md", warnings[0])


class BranchApiTests(unittest.TestCase):
    @patch("check_repository_governance.urlopen")
    def test_fetch_branches_paginates_without_authorization_header(self, mocked_urlopen):
        first_page = [{"name": f"branch-{i}"} for i in range(100)]
        second_page = [{"name": "last-branch"}]
        mocked_urlopen.side_effect = [
            io.BytesIO(json.dumps(first_page).encode("utf-8")),
            io.BytesIO(json.dumps(second_page).encode("utf-8")),
        ]

        result = fetch_repository_branches("owner/repo")

        self.assertEqual(len(result), 101)
        self.assertEqual(result[-1], "last-branch")
        self.assertEqual(mocked_urlopen.call_count, 2)
        first_request = mocked_urlopen.call_args_list[0].args[0]
        second_request = mocked_urlopen.call_args_list[1].args[0]
        self.assertIn("page=1", first_request.full_url)
        self.assertIn("page=2", second_request.full_url)
        self.assertIsNone(first_request.get_header("Authorization"))
        self.assertIsNone(second_request.get_header("Authorization"))

    @patch("check_repository_governance.urlopen")
    def test_fetch_rejects_non_list_api_response(self, mocked_urlopen):
        mocked_urlopen.return_value = io.BytesIO(
            json.dumps({"message": "rate limited"}).encode("utf-8")
        )
        with self.assertRaisesRegex(RuntimeError, "unexpected response"):
            fetch_repository_branches("owner/repo")

    @patch("check_repository_governance.urlopen")
    def test_fetch_rejects_malformed_branch_entry(self, mocked_urlopen):
        mocked_urlopen.return_value = io.BytesIO(
            json.dumps([{"name": "valid"}, {"name": 42}]).encode("utf-8")
        )
        with self.assertRaisesRegex(RuntimeError, "malformed branch entry"):
            fetch_repository_branches("owner/repo")

    @patch("check_repository_governance.urlopen", side_effect=OSError("network unavailable"))
    def test_fetch_propagates_api_failure(self, mocked_urlopen):
        with self.assertRaisesRegex(OSError, "network unavailable"):
            fetch_repository_branches("owner/repo")

    @patch.dict(os.environ, {"GITHUB_REPOSITORY": "owner/repo"}, clear=True)
    @patch("check_repository_governance.tracked_markdown", return_value=[])
    @patch("check_repository_governance.fetch_repository_branches", side_effect=OSError("network unavailable"))
    @patch("sys.argv", ["check_repository_governance.py", "--check-branch-inventory"])
    def test_main_fails_closed_when_live_inventory_cannot_be_fetched(
        self, mocked_fetch, mocked_markdown
    ):
        import check_repository_governance
        self.assertEqual(check_repository_governance.main(), 1)


if __name__ == "__main__":
    unittest.main()
