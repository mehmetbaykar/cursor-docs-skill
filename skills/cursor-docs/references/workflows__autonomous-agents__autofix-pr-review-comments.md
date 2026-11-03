---
title: "Autofix PR review comments"
source: https://cursor.com/workflows/autonomous-agents/autofix-pr-review-comments
path: /workflows/autonomous-agents/autofix-pr-review-comments
---

# Autofix PR review comments

Take a first pass at addressing inline review comments on PR diffs

[Try Automation↗](https://cursor.com/automations/new?templateId=autofix-pr-review-comments)

Review comments pile up, and each round trip costs the author a context switch. An agent can take the first pass at addressing them so pull requests keep moving.

## How to autofix PR review comments with Cursor

- **Watches.** Fires when a reviewer leaves comments on an open pull request.
- **Investigates.** Reads the review thread and repository, applies the requested changes, and pushes them to the pull request branch.
- **Reports back.** A commit that addresses the comments, or a reply explaining why a human is needed.

## Prerequisites & integrations

Connect these in your [Cursor integrations settings](https://cursor.com/dashboard/integrations) before you enable the automation:

- [Git provider](https://cursor.com/dashboard/integrations) (GitHub, GitLab, or Bitbucket)

## The prompt

This is the prompt that ships with the template on the [Marketplace](https://cursor.com/marketplace/automations/autofix-pr-review-comments). Open the template in Automations to load it, then adapt it to your team.

```
You address inline PR review comments with a first-pass fix.

## Goal

When a reviewer leaves an inline comment on the diff, attempt a minimal fix and respond on the thread.

## Process

1. Read the triggering inline comment from the payload (author, comment body, comment URL, PR number).
2. Use the comment URL or `gh` to fetch the file path and line if needed.
3. Understand the requested change — bug, style, missing case, naming, etc.
4. Inspect the surrounding code and make the smallest correct fix.
5. Commit and push to the existing PR branch. Do not open a new PR.
6. Reply on the review thread with what you changed. Resolve the thread if the comment is fully addressed.

## Rules

- Only change code required by the comment. Match existing patterns.
- If the comment is unclear, a design question, or needs human judgment, reply explaining what is ambiguous — do not guess.
- If you cannot fix confidently, say why and what you'd need to proceed.
- Do not approve the PR. Do not address unrelated comments.
```

## How to set up automatic review comment fixes

1. [Open the template in Automations](https://cursor.com/automations/new?templateId=autofix-pr-review-comments) to start from it.
2. Connect the repository the agent should work in.
3. Choose the trigger and connect the tools it uses — GitHub.
4. Tune the prompt to your quality bar, then activate the automation.

## Tips for customizing review comment fixes for your team

- **Tighten the quality bar.** Tell the agent to comment with its findings instead of opening a pull request when it is not confident, so humans stay in the loop on risky changes.
- **Send updates where the team works.** Add a Slack channel so results land in the flow of work instead of waiting to be noticed.
- **Start narrow, then widen.** Scope the trigger to one repository, branch, or label first, and expand once you trust the results.
- **Make it Team Owned.** Set billing to a team-owned automation so runs are shared and visible across the team.

## Additional automations

### CI autofix

Automatically diagnose and fix failing CI so pull requests keep moving.

[View template →](https://cursor.com/workflows/autonomous-agents/ci-autofix)

### Triage failed GitHub Actions

Investigate failed GitHub Actions runs, find the root cause, and report back.

[View template →](https://cursor.com/workflows/autonomous-agents/triage-github-workflow-failures)

### Assess PR risk and assign reviewers

Rate PR risk, assign the right reviewers, and auto-approve low-risk changes.

[View template →](https://cursor.com/workflows/autonomous-agents/assign-pr-reviewers)
