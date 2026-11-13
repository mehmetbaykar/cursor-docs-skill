---
title: "Security Review"
source: https://cursor.com/docs/security-review
path: /docs/security-review
---

# Security Review

Security Review checks pull requests for security bugs, risky patterns, and vulnerabilities before they merge. Security Reviewer agents run on [Automations](https://cursor.com/docs/cloud-agent/automations.md), and the `/review-security` skill runs the same review from your own agent before you push.

To scan code that's already merged and patch what you find, use [Vulnerability Remediation](https://cursor.com/docs/vulnerability-remediation.md).

## Setup

Open the [Security Review page in Automations](https://cursor.com/automations/from-cursor/security-review) to create and configure Security Reviewer agents. Security Reviewer agents require Cloud Agents.

### Source control support

Security Reviewer supports repositories on Origin, GitHub, GitLab, and Bitbucket Cloud.

| Source control provider                                                          | Security Review | Bugbot                                                                                                  |
| :------------------------------------------------------------------------------- | :-------------- | :------------------------------------------------------------------------------------------------------ |
| [Origin](https://cursor.com/docs/origin.md)                                      | Supported       | Supported                                                                                               |
| [GitHub](https://cursor.com/docs/integrations/github.md)                         | Supported       | Supported                                                                                               |
| [GitLab](https://cursor.com/docs/integrations/gitlab.md)                         | Supported       | Supported                                                                                               |
| [Bitbucket Cloud](https://cursor.com/docs/integrations/bitbucket.md)             | Supported       | Supported                                                                                               |
| [Bitbucket Data Center](https://cursor.com/docs/integrations/bitbucket.md#setup) | Not supported   | Supported on Teams and Enterprise; automatic reviews only; no `bugbot run`, `cursor review`, or Autofix |
| [Azure DevOps Services](https://cursor.com/docs/integrations/azure-devops.md)    | Not supported   | Supported (public beta)                                                                                 |

### Triggers

Security Reviewer agents support Git-based Automations triggers, including pull request and merge request events. Use these triggers to run security checks when code changes.

![Security Reviewer Git-based trigger configuration](https://cursor.com/docs-static/images/security-review/triggers.png)

### Security checks

Security Reviewer includes built-in security checks. Enable or disable individual checks based on what you want each agent to review.

### Custom instructions

Use custom instructions to give each agent more context. You can describe the types of issues to prioritize, explain project-specific security expectations, or define how the agent should behave.

### Tools and MCPs

A Security Reviewer needs at least one tool or MCP before you can save it. Use tools and MCPs to connect it to the systems where your team tracks security work.

- Send vulnerabilities to a Slack channel, issue tracker, or another connected system.
- Add custom instructions that explain when and how the agent should use each MCP.
- Give the agent extra context from tools or MCPs before it reports a finding.

### Environment setup

Both Cursor-managed hosting and Cloud Agents are used in this solution. If a team [requires Self-Hosted Machines](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#triggering-pool-agents) then scans remain on Cloud Agents.

## Run in your agent

Use the `/review-security` or `/review` skills to run Security Review from your agent before you push the code.

**What diff is reviewed:** By default, `/review-security` reviews your branch changes: every change relative to the base branch, including committed and uncommitted changes. Ask it to review only your uncommitted changes when you want narrower feedback.

**Against which branch:** `/review-security` compares against your default base branch. When your base branch isn't the default (such as `main`), tell the agent which branch to compare against or let it infer from the context.

![Running the /review-security skill from the agent input](https://cursor.com/docs-static/images/security-review/review-security-skill.png)

`/review` and `/review-security` are available in Cursor 3.7+, at [cursor.com/agents](https://cursor.com/agents), and in the [Cursor CLI](https://cursor.com/docs/cli/overview.md).

## Billing

Security Reviewer agents are billed at the team usage level:

- Usage is charged to the team's usage pool.
- Agents run under a shared team service account, so they don't affect any individual user's usage.

## Analytics

The [Security Review page in Automations](https://cursor.com/automations/from-cursor/security-review) tracks three key metrics across agent runs:

- **Vulnerabilities found**: the number of security findings reported by agents.
- **Issues fixed**: the number of findings that were resolved after they were reported.
- **Resolution rate**: the percentage of reported findings that were fixed.

To determine whether an issue was fixed, Cursor uses LLMs to review incremental diffs and assess whether the flagged issue was resolved.

## Viewing runs

The Security Review page in Automations lists **Recent Runs** for your Security Reviewer agents. Use the run history to see when an agent ran, which tools it used, its final status, and how long it took.

Open a run to inspect the underlying Cloud Agent for more detail about what the agent did. A review that ran on Cursor-managed hosting has no Cloud Agent; opening it shows a read-only view of the review session.

![Security Reviewer run history in Automations](https://cursor.com/docs-static/images/security-review/recent-runs.png)

## Related pages

- [Vulnerability Remediation](https://cursor.com/docs/vulnerability-remediation.md) scans your codebase at rest and patches confirmed vulnerabilities.
- [Bugbot](https://cursor.com/docs/bugbot.md) reviews pull requests for bugs before they merge.
- [Rollouts](https://cursor.com/docs/rollouts.md) monitors each pull request as it deploys and reports its health in every environment.
