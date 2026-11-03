---
title: "Triage failed GitHub Actions"
source: https://cursor.com/workflows/autonomous-agents/triage-github-workflow-failures
path: /workflows/autonomous-agents/triage-github-workflow-failures
---

# Triage failed GitHub Actions

Investigate failed or cancelled workflow runs and report findings in Slack

[Try Automation↗](https://cursor.com/automations/new?templateId=triage-github-workflow-failures)

Red CI blocks everyone downstream, and the person best placed to fix it is rarely the person watching the run. Hand failed workflows to an agent that reads the logs, reproduces the failure path, and reports what broke and why.

## How to triage failed GitHub Actions with Cursor

- **Watches.** Fires when a GitHub Actions workflow fails, via the GitHub trigger or a webhook.
- **Investigates.** Reads the workflow logs and repository, correlates the failure with recent changes, and comments on the PR or run.
- **Reports back.** A root-cause summary on the failing run or PR, escalating to a fix PR when the fix is contained.

## Prerequisites & integrations

Connect these in your [Cursor integrations settings](https://cursor.com/dashboard/integrations) before you enable the automation:

- [Git provider](https://cursor.com/dashboard/integrations) (GitHub, GitLab, or Bitbucket)

Trigger: Webhook

## The prompt

This is the prompt that ships with the template on the [Marketplace](https://cursor.com/marketplace/automations/triage-github-workflow-failures). Open the template in Automations to load it, then adapt it to your team.

```
You triage failed or cancelled GitHub Actions workflow runs.

## Goal

Investigate the triggering workflow run and post a concise Slack summary.

## Investigation

1. Start from the workflow run context in the trigger payload (repository, conclusion, status, head SHA).
2. Use `gh run list --commit <headSha>` (or equivalent) to find the run, then fetch logs. Identify the failing or cancelled job and step.
3. Determine root cause: code regression, config issue, infra flake, dependency problem, or intentional cancellation.
4. If the commit is on a PR, check whether the failure was introduced by recent changes.

## Output

Post to Slack:
- Workflow conclusion (failure or cancelled)
- Failing job(s) and key error excerpt
- Likely root cause (1-2 sentences)
- Recommended next step (fix, rerun, escalate, or no action)

Do not open PRs unless you have high confidence in a minimal fix. Default to triage only.
```

## How to set up automated CI failure triage

1. [Open the template in Automations](https://cursor.com/automations/new?templateId=triage-github-workflow-failures) to start from it.
2. Connect the repository the agent should work in.
3. Choose the trigger and connect the tools it uses — GitHub, Webhook.
4. Tune the prompt to your quality bar, then activate the automation.

## Tips for tuning CI failure triage to your workflows

- **Tighten the quality bar.** Tell the agent to comment with its findings instead of opening a pull request when it is not confident, so humans stay in the loop on risky changes.
- **Send updates where the team works.** Add a Slack channel so results land in the flow of work instead of waiting to be noticed.
- **Start narrow, then widen.** Scope the trigger to one repository, branch, or label first, and expand once you trust the results.
- **Make it Team Owned.** Set billing to a team-owned automation so runs are shared and visible across the team.

## Additional automations

### CI autofix

Automatically diagnose and fix failing CI so pull requests keep moving.

[View template →](https://cursor.com/workflows/autonomous-agents/ci-autofix)

### Autofix PR review comments

Respond to review comments with fixes so PRs move without a round trip.

[View template →](https://cursor.com/workflows/autonomous-agents/autofix-pr-review-comments)

### Investigate production errors from Datadog

Investigate Datadog errors, find root causes, and propose fixes in a PR.

[View template →](https://cursor.com/workflows/autonomous-agents/investigate-datadog-errors)
