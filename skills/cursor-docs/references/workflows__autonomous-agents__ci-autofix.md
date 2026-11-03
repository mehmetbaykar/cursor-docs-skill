---
title: "CI autofix"
source: https://cursor.com/workflows/autonomous-agents/ci-autofix
path: /workflows/autonomous-agents/ci-autofix
---

# CI autofix

Detect CI failures on main and automatically open PRs

[Try Automation↗](https://cursor.com/automations/new?templateId=ci-autofix)

Flaky formatting, lint, and simple test breaks stall PRs and pull engineers out of flow. An agent can take the first pass at green — fixing the obvious cases and escalating the rest.

## How to autofix CI failures with Cursor

- **Watches.** Fires on a failing CI run for an open pull request.
- **Investigates.** Reads the failing job output and repository, reproduces the failure, and commits a fix to the PR branch.
- **Reports back.** A commit that turns CI green, or a comment explaining why a human is needed.

## Prerequisites & integrations

Connect these in your [Cursor integrations settings](https://cursor.com/dashboard/integrations) before you enable the automation:

- [Git provider](https://cursor.com/dashboard/integrations) (GitHub, GitLab, or Bitbucket)

Trigger: Webhook

## The prompt

This is the prompt that ships with the template on the [Marketplace](https://cursor.com/marketplace/automations/ci-autofix). Open the template in Automations to load it, then adapt it to your team.

```
Your task is to fix CI failures on a branch.

# Deduplication

To avoid racing against other agents, before any investigation:
1. Collect the names of ALL failing CI jobs/checks from the CI Status Report above.
2. Calculate your memory filename: sort the failing jobs alphabetically, join with "_", then remove any characters that are not letters, digits, hyphens, underscores, or dots. Prepend "ci-fail-" and truncate to 64 characters total. This is the filename.
3. Read the memory file with this filename.
  - If it exists and the timestamp inside is less than 30 minutes old, stop immediately — no branch, no Slack, no output.
4. Else, write the memory file with the current unix timestamp.
  - If the write SUCCEEDS: you claimed this failure. Proceed with the investigation below.
  - If the write FAILS (version conflict): another agent claimed it first. Stop immediately — no branch, no Slack, no output.

# Investigation

Root cause the CI failure. Look at the logs for the CI failure.
- If the CI failure is due to a bug introduced on that commit, create a new PR that fixes the bug.
- If the CI failure is due to a flaky test, create a new PR that skips that test.
- If you are not confident in either of these outcomes, then do nothing.

# Output

Output your results in the following format:
**CI Autofix Automation**

**Failure logs**: <link to failing CI job>
**Broken by**: <link to PR> (cc @prAuthor)
**Reason**: <1-2 sentence explanation of why CI broke>
**Fixed by**: <1-2 sentence explanation of what fixed it>

Make sure to push the PR but don't include a PR link in your output — the system will generate that for you.
```

## How to set up automatic CI fixes

1. [Open the template in Automations](https://cursor.com/automations/new?templateId=ci-autofix) to start from it.
2. Connect the repository the agent should work in.
3. Choose the trigger and connect the tools it uses — GitHub, Webhook.
4. Tune the prompt to your quality bar, then activate the automation.

## Tips for customizing CI autofix for your repo

- **Tighten the quality bar.** Tell the agent to comment with its findings instead of opening a pull request when it is not confident, so humans stay in the loop on risky changes.
- **Send updates where the team works.** Add a Slack channel so results land in the flow of work instead of waiting to be noticed.
- **Start narrow, then widen.** Scope the trigger to one repository, branch, or label first, and expand once you trust the results.
- **Make it Team Owned.** Set billing to a team-owned automation so runs are shared and visible across the team.

## Additional automations

### Triage failed GitHub Actions

Investigate failed GitHub Actions runs, find the root cause, and report back.

[View template →](https://cursor.com/workflows/autonomous-agents/triage-github-workflow-failures)

### Autofix PR review comments

Respond to review comments with fixes so PRs move without a round trip.

[View template →](https://cursor.com/workflows/autonomous-agents/autofix-pr-review-comments)

### Add test coverage

Review new commits and add tests for high-risk logic automatically.

[View template →](https://cursor.com/workflows/autonomous-agents/add-test-coverage)
