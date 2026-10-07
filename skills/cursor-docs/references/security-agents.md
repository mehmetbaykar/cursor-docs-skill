---
title: "Security Agents"
source: https://cursor.com/docs/security-agents
path: /docs/security-agents
---

# Security Agents

Security Agents scan your code for security bugs, risky patterns, and vulnerabilities.

Configure Security Agents in Automations. Each agent type has its own page: [Security Reviewer](https://cursor.com/automations/from-cursor/security-reviewer) and [Vulnerability Scanner](https://cursor.com/automations/from-cursor/vulnerability-scanner).

## How it works

Security Agents include two Cursor-managed agent types:

- **Security Reviewer** checks pull requests before they merge. Use it to catch vulnerabilities during code review.
- **Vulnerability Scanner** scans your codebase at rest. Use it to find pre-existing vulnerabilities, long-standing issues, and problems missed during PR review.

Both agent types run on the Automations platform and require Cloud Agents.

## Setup

Open the [Security Reviewer](https://cursor.com/automations/from-cursor/security-reviewer) or [Vulnerability Scanner](https://cursor.com/automations/from-cursor/vulnerability-scanner) page in Automations to configure that agent type.

### Source control support

Security Reviewer supports pull requests on Origin, GitHub, and GitLab. For pull request reviews on Bitbucket or Azure DevOps repositories, use [Bugbot](https://cursor.com/docs/bugbot.md).

| Source control provider                                                          | Security Reviewer | Bugbot                                                                                                  |
| :------------------------------------------------------------------------------- | :---------------- | :------------------------------------------------------------------------------------------------------ |
| [Origin](https://cursor.com/docs/origin.md)                                      | Supported         | Supported                                                                                               |
| [GitHub](https://cursor.com/docs/integrations/github.md)                         | Supported         | Supported                                                                                               |
| [GitLab](https://cursor.com/docs/integrations/gitlab.md)                         | Supported         | Supported                                                                                               |
| [Bitbucket Cloud](https://cursor.com/docs/integrations/bitbucket.md)             | Not supported     | Supported (public beta)                                                                                 |
| [Bitbucket Data Center](https://cursor.com/docs/integrations/bitbucket.md#setup) | Not supported     | Supported on Teams and Enterprise; automatic reviews only; no `bugbot run`, `cursor review`, or Autofix |
| [Azure DevOps Services](https://cursor.com/docs/integrations/azure-devops.md)    | Not supported     | Supported (public beta)                                                                                 |

Vulnerability Scanner also does not support Bitbucket Cloud or Bitbucket Data Center repositories.

### Triggers

**Security Reviewer agents** support Git-based Automations triggers, including pull request and merge request events. Use these triggers to run security checks when code changes.

![Security Reviewer Git-based trigger configuration](https://cursor.com/docs-static/images/security-review/triggers.png)

**Vulnerability Scanner agents** support cron-based triggers. Use these triggers to scan your codebase on a recurring schedule, independent of pull request activity.

![Vulnerability Scanner cron trigger configuration](https://cursor.com/docs-static/images/security-review/vulnerability-scanner-triggers.png)

Each Vulnerability Scanner has one schedule. To change when it runs, edit its existing trigger. To scan on another schedule, create a separate Vulnerability Scanner. A scan across more than 1,000 repositories can hit provider rate limits, so split large scopes into separate Vulnerability Scanners with smaller repository scopes.

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

Security Agents run on Cloud Agents. The exception is a team's Security Reviewer: when a pull request event triggers it, the review runs on Cursor-managed hosting instead of a Cloud Agent.

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

Vulnerability Scanner findings appear in the **Flagged Vulnerabilities** list on the [Vulnerability Scanner page in Automations](https://cursor.com/automations/from-cursor/vulnerability-scanner) and on each scanner's detail page. The list groups findings by repository. Filter them by scanner, status, feedback, and severity.

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

Every agent run is tracked in Automations. Each agent type's page lists **Recent Runs** for its own agents. Use the run history to see when an agent ran, which tools it used, its final status, and how long it took.

Open a run to inspect the underlying Cloud Agent for more detail about what the agent did. A review that ran on Cursor-managed hosting has no Cloud Agent. Find it under **Recent Runs** on the Security Reviewer page, where it opens a read-only view of the review session.

![Security Agents run history in Automations](https://cursor.com/docs-static/images/security-review/recent-runs.png)

## Related pages

- [Rollouts](https://cursor.com/docs/rollouts.md) monitors each pull request as it deploys and reports its health in every environment.
