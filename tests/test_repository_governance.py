"""Regression tests for repository governance routing."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_repository_governance import (  # noqa: E402
    ALLOWED_PREFIXES,
    LEGACY_MAIN_PR_HEADS,
    check_routing,
    is_grandfathered_main_pr,
)


class RoutingTests(unittest.TestCase):
    def test_approved_prefixes_are_accepted_into_develop(self):
        for prefix in ALLOWED_PREFIXES:
            with self.subTest(prefix=prefix):
                self.assertEqual(check_routing("develop", prefix + "example", ""), [])

    def test_exact_legacy_main_pairs_are_grandfathered(self):
        for number, head in LEGACY_MAIN_PR_HEADS.items():
            with self.subTest(number=number):
                self.assertTrue(is_grandfathered_main_pr(number, head))
                self.assertEqual(check_routing("main", head, "", number), [])

    def test_legacy_allowlist_requires_exact_number_and_head(self):
        self.assertTrue(check_routing("main", "docs/asset-specific-licensing-policy", "", 999))
        self.assertTrue(check_routing("main", "docs/other-branch", "", 1))

    def test_new_direct_main_pr_is_rejected(self):
        self.assertTrue(check_routing("main", "docs/new-work", "", 100))

    def test_staging_promotion_and_hotfix_rules(self):
        self.assertEqual(check_routing("main", "staging", "", 100), [])
        self.assertTrue(check_routing("main", "fix/urgent", "", 100))
        self.assertEqual(check_routing("main", "fix/urgent", "Emergency hotfix exception: approved", 100), [])

    def test_only_develop_promotes_to_staging(self):
        self.assertEqual(check_routing("staging", "develop", "", 100), [])
        self.assertTrue(check_routing("staging", "docs/change", "", 100))

    def test_long_lived_branches_cannot_target_develop(self):
        for head in ("main", "develop", "staging"):
            self.assertTrue(check_routing("develop", head, "", 100))


if __name__ == "__main__":
    unittest.main()
