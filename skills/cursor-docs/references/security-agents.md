---
title: "Security Agents"
source: https://cursor.com/docs/security-agents
path: /docs/security-agents
---

# Security Agents

Security Agents scan your code for security bugs, risky patterns, and vulnerabilities.

Configure Security Agents in [Automations](https://cursor.com/automations/from-cursor/security).

## How it works

Security Agents include two Cursor-managed agent types:

- **Security Reviewer** checks pull requests before they merge. Use it to catch vulnerabilities during code review.
- **Vulnerability Scanner** scans your codebase at rest. Use it to find pre-existing vulnerabilities, long-standing issues, and problems missed during PR review.

Both agent types run on the Automations platform and require Cloud Agents.

## Setup

Open [Security Agents in Automations](https://cursor.com/automations/from-cursor/security) to configure an agent.

### Triggers

**Security Reviewer agents** support Git-based Automations triggers, including pull request and merge request events. Use these triggers to run security checks when code changes.

![Security Reviewer Git-based trigger configuration](https://cursor.com/docs-static/images/security-review/triggers.png)

**Vulnerability Scanner agents** support cron-based triggers. Use these triggers to scan your codebase on a recurring schedule, independent of pull request activity.

![Vulnerability Scanner cron trigger configuration](https://cursor.com/docs-static/images/security-review/vulnerability-scanner-triggers.png)

### Security Checks

Both agent types include built-in security checks. Enable or disable individual checks based on what you want each agent to review.

### Custom instructions

Use custom instructions to give each agent more context. You can describe the types of issues to prioritize, explain project-specific security expectations, or define how the agent should behave.

### Tools and MCPs

Both agent types support tools and MCPs. A Security Reviewer needs at least one tool or MCP before you can save it. A Vulnerability Scanner saves without one and reports its findings to the [Flagged vulnerabilities](https://cursor.com/docs/security-agents.md#flagged-vulnerabilities) list.

Use tools and MCPs to connect Security Agents to the systems where your team tracks security work.

- Send vulnerabilities to a Slack channel, issue tracker, or another connected system.
- Add custom instructions that explain when and how the agent should use each MCP.
- Give the agent extra context from tools or MCPs before it reports a finding.

### Environment Setup

Security Agents run on Cloud Agents.

You can use Cursor's cloud with no additional setup.

## Run in your agent

Use the `/review-security` or `/review` skills to run the Security Agent from your agent before you push the code.

**What diff is reviewed:** By default, `/review-security` reviews your branch changes: every change relative to the base branch, including committed and uncommitted changes. Ask it to review only your uncommitted changes when you want narrower feedback.

**Against which branch:** `/review-security` compares against your default base branch. When your base branch isn't the default (such as `main`), tell the agent which branch to compare against or let it infer from the context.

![Running the /review-security skill from the agent input](https://cursor.com/docs-static/images/security-review/review-security-skill.png)

`/review` and `/review-security` are available in Cursor 3.7+, at [cursor.com/agents](https://cursor.com/agents), and in the [Cursor CLI](https://cursor.com/docs/cli/overview.md).

## Billing

Security Agents are billed at the team usage level:

- Usage is charged to the team's usage pool.
- Agents run under a shared team service account, so they don't affect any individual user's usage.

## Analytics

Security Agents track three key metrics across agent runs:

- **Vulnerabilities found**: the number of security findings reported by agents.
- **Issues fixed**: the number of findings that were resolved after they were reported.
- **Resolution rate**: the percentage of reported findings that were fixed.

To determine whether an issue was fixed, Cursor uses LLMs to review incremental diffs and assess whether the flagged issue was resolved.

## Flagged vulnerabilities

Vulnerability Scanner findings appear in the **Flagged Vulnerabilities** list on the [Security Agents page in Automations](https://cursor.com/automations/from-cursor/security) and on each scanner's detail page. The list groups findings by repository. Filter them by scanner, status, feedback, and severity.

| Field           | Description                                                                                                                 |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| **Status**      | **Active** or **Dismissed**. Change it from the list to dismiss or restore a finding.                                       |
| **Feedback**    | **Useful**, **False Positive**, or **Unimportant**. Set it from the list to record whether the finding was worth reporting. |
| **Severity**    | Severity reported by the scanner. Filter by **Critical**, **High**, or **Medium**.                                          |
| **Location**    | File the finding points to.                                                                                                 |
| **Detected On** | Date the scanner found the issue.                                                                                           |
| **Commit**      | Commit the scan ran against.                                                                                                |
| **Reported**    | Link to where the finding was reported, when the scanner recorded one.                                                      |

Each finding has two actions:

- **Fix in Cursor** starts a [Cloud Agent](https://cursor.com/docs/cloud-agent.md) to fix the vulnerability in that repository.
- **View in codebase** opens the scan run in [Origin](https://cursor.com/docs/origin.md). This appears only when Origin is enabled for your team.

## Viewing Runs

Every agent run is tracked in Automations. Use the run history to see when an agent ran, which tools it used, its final status, and how long it took.

Open a run to inspect the underlying Cloud Agent for more detail about what the agent did.

![Security Agents run history in Automations](https://cursor.com/docs-static/images/security-review/recent-runs.png)

## Related pages

- [Rollouts](https://cursor.com/docs/rollouts.md) monitors each pull request as it deploys and reports its health in every environment.
