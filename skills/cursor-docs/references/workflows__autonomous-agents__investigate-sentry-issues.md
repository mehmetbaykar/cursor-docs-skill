---
title: "Investigate Sentry issues"
source: https://cursor.com/workflows/autonomous-agents/investigate-sentry-issues
path: /workflows/autonomous-agents/investigate-sentry-issues
---

# Investigate Sentry issues

Investigate errors from Sentry, identify root causes, and propose fixes

[Try Automation↗](https://cursor.com/automations/new?templateId=investigate-sentry-issues)

New error signatures pile up faster than teams can triage them. An agent can take each one, map the stack trace to the code, and tell you whether it is a real regression worth fixing now.

## How to investigate Sentry issues with Cursor

- **Watches.** Fires when a new Sentry issue is created.
- **Investigates.** Reads the Sentry event and stack trace, inspects the repository, and opens a PR or comment with a root-cause explanation.
- **Reports back.** A root-cause summary linked to the offending code, escalating to a fix PR when contained.

## Prerequisites & integrations

Connect these in your [Cursor integrations settings](https://cursor.com/dashboard/integrations) before you enable the automation:

- [Sentry](https://cursor.com/dashboard/integrations)

Trigger: Webhook

## The prompt

This is the prompt that ships with the template on the [Marketplace](https://cursor.com/marketplace/automations/investigate-sentry-issues). Open the template in Automations to load it, then adapt it to your team.

```
You are an incident-investigation automation focused on Sentry errors.

## Goal

Continuously reduce production errors by investigating high-impact Sentry issues and landing safe fixes.

## Investigation process

1. Use Sentry tools to fetch full error details — stack traces, exception types, affected endpoints, frequency, and user impact.
2. Group duplicate symptoms into root-cause clusters.
3. Correlate stack frames, request context, release timing, and relevant code changes.
4. Form a root-cause hypothesis and validate with code evidence.

## Fix policy

- Only implement fixes with high confidence in root cause.
- Prefer minimal, robust changes with low regression risk.
- Add tests where feasible for the failure mode.
- If a safe fix is not possible, provide a concrete follow-up plan.

## Output

If fixed, open a PR and report to Slack:
- Error signature(s) addressed
- Root cause
- Fix summary and validation
- Any remaining risk
- Link to the Sentry issue

If not fixable with high confidence, post the investigation analysis to Slack with a concrete follow-up plan instead.
```

## How to set up automatic Sentry issue investigation

1. [Open the template in Automations](https://cursor.com/automations/new?templateId=investigate-sentry-issues) to start from it.
2. Connect the repository the agent should work in.
3. Choose the trigger and connect the tools it uses — Sentry, Webhook.
4. Tune the prompt to your quality bar, then activate the automation.

## Tips for tuning error investigation to your codebase

- **Tighten the quality bar.** Tell the agent to comment with its findings instead of opening a pull request when it is not confident, so humans stay in the loop on risky changes.
- **Send updates where the team works.** Add a Slack channel so results land in the flow of work instead of waiting to be noticed.
- **Start narrow, then widen.** Scope the trigger to one repository, branch, or label first, and expand once you trust the results.
- **Make it Team Owned.** Set billing to a team-owned automation so runs are shared and visible across the team.

## Additional automations

### PagerDuty incident investigation

Start investigating the moment PagerDuty pages, and post findings to Slack.

[View template →](https://cursor.com/workflows/autonomous-agents/pagerduty-incident-investigation)

### Investigate production errors from Datadog

Investigate Datadog errors, find root causes, and propose fixes in a PR.

[View template →](https://cursor.com/workflows/autonomous-agents/investigate-datadog-errors)

### Fix bugs reported in Slack

Watch Slack for bug reports, investigate, and return PRs for simple fixes.

[View template →](https://cursor.com/workflows/autonomous-agents/fix-slack-bugs)
