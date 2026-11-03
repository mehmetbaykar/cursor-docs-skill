---
title: "Remediate dependency vulnerabilities"
source: https://cursor.com/workflows/autonomous-agents/remediate-dependency-vulnerabilities
path: /workflows/autonomous-agents/remediate-dependency-vulnerabilities
---

# Remediate dependency vulnerabilities

Triage dependency-vulnerability tickets from Linear and open upgrade PRs when the fix is safe

[Try Automation↗](https://cursor.com/automations/new?templateId=remediate-dependency-vulnerabilities)

Vulnerable dependencies are easy to flag and tedious to fix safely. An agent can upgrade them, run the tests, and open a pull request once everything passes.

## How to remediate dependency vulnerabilities with Cursor

- **Watches.** Runs on a schedule or when a vulnerable dependency is detected.
- **Investigates.** Identifies impacted dependencies, upgrades them, runs tests to check for breakage, and opens a pull request.
- **Reports back.** A pull request upgrading vulnerable dependencies with tests passing.

## Prerequisites & integrations

Connect these in your [Cursor integrations settings](https://cursor.com/dashboard/integrations) before you enable the automation:

- [Git provider](https://cursor.com/dashboard/integrations) (GitHub, GitLab, or Bitbucket)

Trigger: Schedule

## The prompt

This is the prompt that ships with the template on the [Marketplace](https://cursor.com/marketplace/automations/remediate-dependency-vulnerabilities). Open the template in Automations to load it, then adapt it to your team.

```
You are a dependency-vulnerability remediation automation.

## Goal

When a new Linear issue describes a vulnerable dependency, determine whether it can be upgraded safely and open a PR only when confidence is high.

If the issue is not a dependency-vulnerability report, do nothing.

## Expected issue content

The issue may include some or all of the following:
- vulnerable package name
- current version
- proposed fixed version
- affected dependency file paths
- reachable paths or impacted call sites
- advisory notes or remediation guidance

## Investigation workflow

1. Extract the advisory, package name, current version, and candidate fix versions.
2. Exhaustively identify all callers of the affected package across the repository.
3. Classify callers by production-critical, tooling, tests, or isolated usage.
4. Prefer the lowest version that fixes the vulnerability and minimizes change risk.
5. Review changelogs and breaking changes for the selected upgrade.
6. Prefer direct upgrades over overrides. Use an override only when you can clearly justify the risk.
7. Run focused validation on affected code paths, including targeted tests when available.

## Decision rule

Create a PR only when the upgrade is clearly safe. Otherwise, do not make code changes.

## Output

Post a concise Slack summary that includes:
- advisory and package
- chosen target version, if any
- key callers and risks
- whether a PR was created or manual review is still needed
```

## How to set up automatic dependency remediation

1. [Open the template in Automations](https://cursor.com/automations/new?templateId=remediate-dependency-vulnerabilities) to start from it.
2. Connect the repository the agent should work in.
3. Choose the trigger and connect the tools it uses — Schedule, GitHub.
4. Tune the prompt to your quality bar, then activate the automation.

## Tips for customizing dependency upgrades for your stack

- **Tighten the quality bar.** Tell the agent to comment with its findings instead of opening a pull request when it is not confident, so humans stay in the loop on risky changes.
- **Send updates where the team works.** Add a Slack channel so results land in the flow of work instead of waiting to be noticed.
- **Start narrow, then widen.** Scope the trigger to one repository, branch, or label first, and expand once you trust the results.
- **Make it Team Owned.** Set billing to a team-owned automation so runs are shared and visible across the team.

## Additional automations

### Scan codebase for vulnerabilities

Run a scheduled security sweep across the whole codebase.

[View template →](https://cursor.com/workflows/autonomous-agents/scan-codebase-vulnerabilities)

### Find vulnerabilities

Review new changes for security vulnerabilities and flag them as inline PR comments.

[View template →](https://cursor.com/workflows/autonomous-agents/find-vulnerabilities)

### CI autofix

Automatically diagnose and fix failing CI so pull requests keep moving.

[View template →](https://cursor.com/workflows/autonomous-agents/ci-autofix)
