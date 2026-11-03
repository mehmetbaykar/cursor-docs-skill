---
title: "Linear issue triage"
source: https://cursor.com/workflows/autonomous-agents/linear-issue-triage
path: /workflows/autonomous-agents/linear-issue-triage
---

# Linear issue triage

Triage new issues by investigating bugs, planning feature requests, and opening PRs for easy fixes

[Try Automation↗](https://cursor.com/automations/new?templateId=linear-issue-triage)

Untriaged issues rot: duplicates accumulate, priorities drift, and reporters never hear back. An agent can do the first pass on every new issue so the backlog stays trustworthy.

## How to triage Linear issues with Cursor

- **Watches.** Fires when a new Linear issue is created.
- **Investigates.** Reads the issue and related code, applies labels and priority, and adds a comment with repro or context.
- **Reports back.** A labeled, prioritized issue with a context comment — flagged for a human when ambiguous.

## Prerequisites & integrations

Connect these in your [Cursor integrations settings](https://cursor.com/dashboard/integrations) before you enable the automation:

- [Linear](https://cursor.com/dashboard/integrations)

Trigger: Webhook

## The prompt

This is the prompt that ships with the template on the [Marketplace](https://cursor.com/marketplace/automations/linear-issue-triage). Open the template in Automations to load it, then adapt it to your team.

```
You are an issue triage automation for Linear.

Examine the issue. Add an eyes emoji reaction when you start looking at it. When opening PRs, include a line like "Resolves BUG-123" or "Fixes BUG-123" (where BUG-123 is the issue ID) so that the PR gets properly linked to the issue.

If the issue is neither a bug report nor a feature request, do nothing. Do not comment, do not create noise.

## Bug report

- If it's a bug report, investigate the bug and report your findings. This can be either refuting the bug or explaining the likely root cause.
- Use Datadog logs to assist, if applicable.
- If it's an easy fix, open a PR.
- If status is Triage, change status to Backlog if it's a real bug.

## Feature request

- If it's a feature request, plan out the high level approach and comment with the approach.
- If it's an easy change, make the change and open a PR.
```

## How to set up automatic issue triage

1. [Open the template in Automations](https://cursor.com/automations/new?templateId=linear-issue-triage) to start from it.
2. Connect a repository if you want the agent to read or change code.
3. Choose the trigger and connect the tools it uses — Linear, Webhook.
4. Tune the prompt to your quality bar, then activate the automation.

## Tips for customizing issue triage for your backlog

- **Tighten the quality bar.** Tell the agent to comment with its findings instead of opening a pull request when it is not confident, so humans stay in the loop on risky changes.
- **Send updates where the team works.** Add a Slack channel so results land in the flow of work instead of waiting to be noticed.
- **Start narrow, then widen.** Scope the trigger to one repository, branch, or label first, and expand once you trust the results.
- **Make it Team Owned.** Set billing to a team-owned automation so runs are shared and visible across the team.

## Additional automations

### Fix bugs reported in Slack

Watch Slack for bug reports, investigate, and return PRs for simple fixes.

[View template →](https://cursor.com/workflows/autonomous-agents/fix-slack-bugs)

### Daily digest of repo changes

Post a daily summary of notable repository changes and new risks.

[View template →](https://cursor.com/workflows/autonomous-agents/daily-digest)

### Product FAQ agent

Answer recurring product questions from a trusted source of truth. No repo required.

[View on Marketplace ↗](https://cursor.com/marketplace/automations/product-faq-agent)
