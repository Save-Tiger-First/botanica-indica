# ODR-03 — GitHub Copilot Free-Only Project Usage

**Decision ID:** ODR-03  
**Decision type:** Owner Decision Record (not an Architecture Decision Record)  
**Status:** Owner-authorized project constraint — 26 November 2026  
**Decision authority:** Save Tiger First project owner  
**Project:** Save Tiger First / Botanica Indica  
**Repository:** Save-Tiger-First/botanica-indica  
**Recorded in:** PR #20 workstream, branch docs/full-system-architecture-and-repo-engineering-plan

## 1. Owner instruction

On 26 November 2026, the project owner instructed that GitHub Copilot be checked and restricted to free-only use.

## 2. Decision

For Save Tiger First / Botanica Indica project work:

- Use GitHub Copilot only under the **Copilot Free** plan.
- Do not purchase, renew, assign or rely on Copilot Pro, Pro+, Business, Enterprise, paid seats, premium paid features or paid AI-credit usage for this project without a new explicit owner decision.
- Do not enable additional paid usage, usage-based billing or additional usage budgets for Copilot.
- Do not configure automatic Copilot code review or cloud-agent workflows for this repository.
- When the Copilot Free allowance is exhausted, stop using Copilot until the allowance resets; do not upgrade to continue.
- Do not treat Copilot output as authoritative. All generated code, scientific assertions, citations, security changes and repository modifications require ordinary project review and validation.

This is a cost-control policy. It does not prohibit use of other tools already available to the project owner or ChatGPT, and it does not change the AI Project Operating Prompt.

## 3. Repository-level inspection on 26 November 2026

The active repository ruleset Protect main branch (ID 23822734) was inspected. It targets the default branch and contains only:

- deletion protection;
- non-fast-forward protection.

It does **not** contain the GitHub rule “Automatically request Copilot code review.” No repository-level automatic Copilot code-review rule was found in the inspected ruleset.

No repository ruleset or protection setting was changed.

## 4. Account and organization billing boundary

The connected GitHub repository tools do not expose the user's personal Copilot subscription, organization Copilot seats, AI-credit budget or billing settings. Those account/organization settings were not inspected and cannot be changed through this repository connection.

Therefore this record establishes the project policy, but **does not claim that a personal or organization subscription has been downgraded or cancelled**. The account holder or organization owner must verify the active license and billing settings directly in GitHub.

## 5. Free-plan facts checked

GitHub's official Copilot plan page currently lists Copilot Free at USD $0, with 2,000 completions per month and no credit card required. GitHub lists Copilot code review as a Pro feature. Plan allowances and features can change; verify the live official plan page before any future change.

Sources checked 26 November 2026:
- GitHub Copilot plans and pricing: https://github.com/features/copilot/plans
- Viewing, changing and cancelling a Copilot plan: https://docs.github.com/en/copilot/how-tos/manage-your-account/view-and-change-your-copilot-plan
- Configuring Copilot code review: https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-code-review

## 6. Required account-holder verification

To ensure the account is Free-only:

1. Open GitHub profile menu → **Settings**.
2. Open **Billing & licensing** → **Licensing** (or **Plans and usage** in the original billing interface).
3. In the GitHub Copilot section, verify the current plan.
4. If a paid individual plan is active, choose **Manage subscription** → **Cancel subscription** / downgrade to Copilot Free and complete GitHub's confirmation flow. GitHub states that access to the paid plan continues until the current billing cycle ends; Free takes effect afterward.
5. Check that no organization-assigned Copilot seat or paid organization usage budget is being used for this project. Organization/enterprise licenses are managed by their owner.

## 7. Verification status

- Repository automatic Copilot code review: **not configured in the inspected active repository ruleset**.
- Repository settings changed: **no**.
- Personal Copilot plan inspected: **no — account billing endpoint is not available through this connection**.
- Personal or organization plan downgraded/cancelled: **not performed**.
- Free-only project policy: **recorded by owner authorization**.

**Decision:** Free-only use; no paid Copilot use or automatic repository Copilot reviews for STF/Botanica Indica without a new explicit owner decision.
