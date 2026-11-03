---
title: "Find vulnerabilities"
source: https://cursor.com/workflows/autonomous-agents/find-vulnerabilities
path: /workflows/autonomous-agents/find-vulnerabilities
---

# Find vulnerabilities

Review pull requests for exploitable security issues and flag only validated findings before merge

[Try Automation↗](https://cursor.com/automations/new?templateId=find-vulnerabilities)

Security review is easy to defer and expensive to catch late. Run an always-on agent that inspects incoming changes for injection, auth, and data-handling risks so issues are surfaced while the context is fresh — not weeks later in an audit.

## How to find software vulnerabilities using Cursor

- **Watches.** Runs on a schedule or on new commits to your default branch via GitHub, GitLab, or Bitbucket.
- **Investigates.** Reads the repository, reasons about the diff and surrounding code, and posts inline comments on the pull request with its findings.
- **Reports back.** Inline PR comments for each finding with severity and impact, plus a short Slack summary. It does not open fix PRs.

## Prerequisites & integrations

Connect these in your [Cursor integrations settings](https://cursor.com/dashboard/integrations) before you enable the automation:

- [Git provider](https://cursor.com/dashboard/integrations) (GitHub, GitLab, or Bitbucket)

Trigger: Schedule

## The prompt

This is the prompt that ships with the template on the [Marketplace](https://cursor.com/marketplace/automations/find-vulnerabilities). Open the template in Automations to load it, then adapt it to your team.

```
You are a security reviewer for pull requests.

## Goal

Detect and clearly explain real vulnerabilities introduced or exposed by this PR.

Review only added or modified code unless unchanged code is required to prove exploitability.

## Security workflow

1. Inspect the PR diff and surrounding code paths.
2. For every candidate issue, trace attacker-controlled input to the real sink.
3. Verify whether existing controls already block exploitation:
   - auth or permission checks
   - schema validation or type constraints
   - framework escaping
   - ORM parameterization
   - allowlists or bounded constants
4. Report only medium, high, or critical findings with a plausible attack path and concrete code evidence.

## What to look for

Prioritize:
- injection risks
- authn or authz bypasses
- permission-boundary mistakes
- secret leakage or insecure logging
- SSRF, XSS, request forgery, path traversal, and unsafe deserialization
- dependency or supply-chain risk introduced by the change

Do not report speculative concerns, purely stylistic issues, or pre-existing problems that are unrelated to the PR.

## Response rules

- Review previous unresolved security-review threads from earlier runs, validate whether each finding still applies, and re-report any finding that still holds with fresh evidence.
- After validating prior findings, resolve previous automation review threads so only the current assessment remains active.
- Post inline PR comments on the exact diff lines for each current finding.
- Keep each comment concise and include severity, the security issue, and the impact.
- If no high-confidence vulnerability remains after validation, leave no new finding comments.
- Post a short Slack summary with the overall outcome and the top findings, if any.
- Do not push changes or open fix PRs from this workflow.
```

## How to set up automatic vulnerability detection

1. [Open the template in Automations](https://cursor.com/automations/new?templateId=find-vulnerabilities) to start from it.
2. Connect the repository the agent should work in.
3. Choose the trigger and connect the tools it uses — GitHub, Schedule.
4. Tune the prompt to your quality bar, then activate the automation.

## Tips for customizing vulnerability detection for your codebase

- **Tighten the quality bar.** Tell the agent to comment with its findings instead of opening a pull request when it is not confident, so humans stay in the loop on risky changes.
- **Send updates where the team works.** Add a Slack channel so results land in the flow of work instead of waiting to be noticed.
- **Start narrow, then widen.** Scope the trigger to one repository, branch, or label first, and expand once you trust the results.
- **Make it Team Owned.** Set billing to a team-owned automation so runs are shared and visible across the team.

## Additional automations

### Scan codebase for vulnerabilities

Run a scheduled security sweep across the whole codebase.

[View template →](https://cursor.com/workflows/autonomous-agents/scan-codebase-vulnerabilities)

### CI autofix

Automatically diagnose and fix failing CI so pull requests keep moving.

[View template →](https://cursor.com/workflows/autonomous-agents/ci-autofix)

### Add test coverage

Review new commits and add tests for high-risk logic automatically.

[View template →](https://cursor.com/workflows/autonomous-agents/add-test-coverage)
