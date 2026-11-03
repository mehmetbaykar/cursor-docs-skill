---
title: "PagerDuty incident investigation"
source: https://cursor.com/workflows/autonomous-agents/pagerduty-incident-investigation
path: /workflows/autonomous-agents/pagerduty-incident-investigation
---

# PagerDuty incident investigation

Investigate incidents using Datadog and code context

[Try Automation↗](https://cursor.com/automations/new?templateId=pagerduty-incident-investigation)

The first ten minutes of an incident are spent gathering context. Let an agent do that gathering the instant a page fires, so responders arrive to a head start instead of a blank page.

## How to investigate PagerDuty incidents with Cursor

- **Watches.** Fires when a PagerDuty incident is triggered.
- **Investigates.** Pulls metrics and traces via the Datadog MCP, correlates with recent deploys, and posts a running summary to Slack.
- **Reports back.** A Slack thread with a timeline, likely causes, and suggested next steps — plus a PR when a code cause is clear.

## Prerequisites & integrations

Connect these in your [Cursor integrations settings](https://cursor.com/dashboard/integrations) before you enable the automation:

- [PagerDuty](https://cursor.com/dashboard/integrations)
- [Slack](https://cursor.com/dashboard/integrations)
- [Datadog](https://cursor.com/dashboard/integrations)

## The prompt

This is the prompt that ships with the template on the [Marketplace](https://cursor.com/marketplace/automations/pagerduty-incident-investigation). Open the template in Automations to load it, then adapt it to your team.

```
You are an incident investigation automation for PagerDuty incidents.

## Goal

Investigate the triggering PagerDuty incident, use Datadog MCP to gather evidence, and analyze the codebase (especially recent commits) to identify likely causes and suggest fixes.

## Investigation process

1. Start from the PagerDuty incident context provided by the trigger payload (incident title, service, urgency, timestamps, links, and any included details).
2. Use Datadog MCP tools to investigate the affected service:
   - Look for correlated errors, logs, traces, and monitors around the incident window.
   - Identify what changed around the time the incident began (deployments, traffic shifts, dependency failures, infrastructure issues).
   - Gather concrete evidence (error signatures, endpoints, stack traces, services, hosts, tags).
3. Investigate the codebase for likely sources of the incident:
   - Search the relevant code paths and services implicated by Datadog evidence.
   - Review recent commits and diffs that may have introduced the regression.
   - Correlate commit timing and code changes with the observed symptoms.
4. Form and validate hypotheses:
   - Prefer evidence-backed hypotheses over speculation.
   - If multiple plausible causes exist, rank them by likelihood and explain why.

## Fix guidance

- If there is a safe, high-confidence fix, implement it and open a PR.
- If a fix is not yet safe to implement, propose the smallest next steps to confirm the root cause and reduce impact.
- Prefer minimal, low-risk changes and include tests when feasible.

## Output

Report:
- Incident summary (what failed and impact)
- Datadog evidence used
- Most likely root cause(s)
- Relevant recent commit(s) or code changes
- Proposed fix (or implemented fix + validation)
- Remaining risks / follow-up work
```

## How to set up automatic incident investigation

1. [Open the template in Automations](https://cursor.com/automations/new?templateId=pagerduty-incident-investigation) to start from it.
2. Connect a repository if you want the agent to read or change code.
3. Choose the trigger and connect the tools it uses — PagerDuty, Slack, Datadog.
4. Tune the prompt to your quality bar, then activate the automation.

## Tips for customizing incident investigation for your stack

- **Tighten the quality bar.** Tell the agent to comment with its findings instead of opening a pull request when it is not confident, so humans stay in the loop on risky changes.
- **Send updates where the team works.** Add a Slack channel so results land in the flow of work instead of waiting to be noticed.
- **Start narrow, then widen.** Scope the trigger to one repository, branch, or label first, and expand once you trust the results.
- **Make it Team Owned.** Set billing to a team-owned automation so runs are shared and visible across the team.

## Additional automations

### Investigate Sentry issues

Turn new Sentry issues into root-cause summaries and candidate fixes.

[View template →](https://cursor.com/workflows/autonomous-agents/investigate-sentry-issues)

### Investigate production errors from Datadog

Investigate Datadog errors, find root causes, and propose fixes in a PR.

[View template →](https://cursor.com/workflows/autonomous-agents/investigate-datadog-errors)

### Fix bugs reported in Slack

Watch Slack for bug reports, investigate, and return PRs for simple fixes.

[View template →](https://cursor.com/workflows/autonomous-agents/fix-slack-bugs)
