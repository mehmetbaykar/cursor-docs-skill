---
title: "Generate and update docs"
source: https://cursor.com/workflows/autonomous-agents/generate-docs
path: /workflows/autonomous-agents/generate-docs
---

# Generate and update docs

Create and update developer documentation for recently changed or under-documented code

[Try Automation↗](https://cursor.com/automations/new?templateId=generate-docs)

Documentation drifts from the code the moment it is written. An agent can keep docs in sync as the code changes, so they stay trustworthy instead of going stale.

## How to generate and update docs with Cursor

- **Watches.** Runs on merges to the default branch or on a schedule.
- **Investigates.** Reads recent changes and the repository, updates the affected documentation, and opens a pull request.
- **Reports back.** A pull request that brings documentation back in line with the code.

## Prerequisites & integrations

Connect these in your [Cursor integrations settings](https://cursor.com/dashboard/integrations) before you enable the automation:

- [Git provider](https://cursor.com/dashboard/integrations) (GitHub, GitLab, or Bitbucket)

Trigger: Schedule

## The prompt

This is the prompt that ships with the template on the [Marketplace](https://cursor.com/marketplace/automations/generate-docs). Open the template in Automations to load it, then adapt it to your team.

```
You are a documentation automation for engineering teams.

## Goal

Keep technical documentation current and useful as the codebase evolves.

## What to document

- Recently changed subsystems with weak docs.
- Public interfaces, workflows, and operational runbooks.
- Setup, troubleshooting, and common pitfalls for developers.

## Documentation standards

- Explain intent, architecture, and usage.
- Include concrete examples and constraints.
- Keep docs concise and structured for scanning.
- Align with existing docs style and location.

## Guardrails

- Do not fabricate behavior; verify against source code.
- Prefer updating existing docs over creating redundant pages.
- Keep documentation-only PRs clean and focused.

## Output

If you open a PR, summarize:
- Docs added/updated
- Which codepaths they cover
- Key knowledge gaps addressed
```

## How to set up automatic documentation updates

1. [Open the template in Automations](https://cursor.com/automations/new?templateId=generate-docs) to start from it.
2. Connect the repository the agent should work in.
3. Choose the trigger and connect the tools it uses — GitHub, Schedule.
4. Tune the prompt to your quality bar, then activate the automation.

## Tips for keeping generated docs in your team's voice

- **Tighten the quality bar.** Tell the agent to comment with its findings instead of opening a pull request when it is not confident, so humans stay in the loop on risky changes.
- **Send updates where the team works.** Add a Slack channel so results land in the flow of work instead of waiting to be noticed.
- **Start narrow, then widen.** Scope the trigger to one repository, branch, or label first, and expand once you trust the results.
- **Make it Team Owned.** Set billing to a team-owned automation so runs are shared and visible across the team.

## Additional automations

### Daily digest of repo changes

Post a daily summary of notable repository changes and new risks.

[View template →](https://cursor.com/workflows/autonomous-agents/daily-digest)

### Add test coverage

Review new commits and add tests for high-risk logic automatically.

[View template →](https://cursor.com/workflows/autonomous-agents/add-test-coverage)

### Find vulnerabilities

Review new changes for security vulnerabilities and flag them as inline PR comments.

[View template →](https://cursor.com/workflows/autonomous-agents/find-vulnerabilities)
