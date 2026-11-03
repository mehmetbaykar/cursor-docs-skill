---
title: "Daily digest of repo changes"
source: https://cursor.com/workflows/autonomous-agents/daily-digest
path: /workflows/autonomous-agents/daily-digest
---

# Daily digest of repo changes

Post a daily Slack digest summarizing notable repository changes and risks from the previous day

[Try Automation↗](https://cursor.com/automations/new?templateId=daily-digest)

Keeping up with a busy repository is a job in itself. A scheduled agent can read the day's changes and produce a digest that keeps the team oriented without anyone doing the reading.

## How to get a daily digest of repo changes with Cursor

- **Watches.** Runs on a schedule — for example every weekday morning.
- **Investigates.** Reads recent commits and PRs, summarizes what changed and what looks risky, and posts to Slack.
- **Reports back.** A Slack digest of notable changes, new risks, and follow-ups worth attention.

## Prerequisites & integrations

Trigger: Schedule

## The prompt

This is the prompt that ships with the template on the [Marketplace](https://cursor.com/marketplace/automations/daily-digest). Open the template in Automations to load it, then adapt it to your team.

```
You create a daily engineering digest for this repository.

## Goal

Produce a concise, high-signal summary of what changed in the last 24 hours.

## What to include

- Major merged PRs and their user or system impact.
- Notable bug fixes, incidents, and risky areas touched.
- Security or dependency-related changes.
- Follow-ups worth attention (tests missing, rollout risk, possible regressions).

## Quality bar

- Prioritize signal over completeness.
- Cluster related changes into themes.
- Do not invent details; cite concrete evidence from commits/PRs.
- Keep the digest easy to skim.

## Output format

Post one Slack message with:
- Date range covered
- 3-7 key bullets of meaningful changes
- "Watchlist" section with 1-3 risks or pending follow-ups
```

## How to set up a daily repo digest

1. [Open the template in Automations](https://cursor.com/automations/new?templateId=daily-digest) to start from it.
2. Connect the repository the agent should work in.
3. Choose the trigger and connect the tools it uses — Schedule.
4. Tune the prompt to your quality bar, then activate the automation.

## Tips for tailoring the daily digest to your team

- **Tighten the quality bar.** Tell the agent to comment with its findings instead of opening a pull request when it is not confident, so humans stay in the loop on risky changes.
- **Send updates where the team works.** Add a Slack channel so results land in the flow of work instead of waiting to be noticed.
- **Start narrow, then widen.** Scope the trigger to one repository, branch, or label first, and expand once you trust the results.
- **Make it Team Owned.** Set billing to a team-owned automation so runs are shared and visible across the team.

## Additional automations

### Generate and update docs

Keep documentation in sync with the code as it changes.

[View template →](https://cursor.com/workflows/autonomous-agents/generate-docs)

### Slack digest agent

Summarize activity across channels into a single readable digest. No repo required.

[View on Marketplace ↗](https://cursor.com/marketplace/automations/slack-digest-agent)

### Scan codebase for vulnerabilities

Run a scheduled security sweep across the whole codebase.

[View template →](https://cursor.com/workflows/autonomous-agents/scan-codebase-vulnerabilities)
