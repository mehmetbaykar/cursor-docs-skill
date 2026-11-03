---
title: "Add test coverage"
source: https://cursor.com/workflows/autonomous-agents/add-test-coverage
path: /workflows/autonomous-agents/add-test-coverage
---

# Add test coverage

Review recent changes and add tests for high-risk logic that lacks adequate coverage

[Try Automation↗](https://cursor.com/automations/new?templateId=add-test-coverage)

High-risk logic often ships without tests, and backfilling coverage never reaches the top of the backlog. An agent can review new changes and add tests where they matter most.

## How to add test coverage with Cursor

- **Watches.** Runs on new commits or on a schedule.
- **Investigates.** Reads the diff and repository, identifies under-tested high-risk paths, and opens a pull request that adds tests.
- **Reports back.** A pull request adding targeted tests for high-risk logic.

## Prerequisites & integrations

Connect these in your [Cursor integrations settings](https://cursor.com/dashboard/integrations) before you enable the automation:

- [Git provider](https://cursor.com/dashboard/integrations) (GitHub, GitLab, or Bitbucket)

Trigger: Schedule

## The prompt

This is the prompt that ships with the template on the [Marketplace](https://cursor.com/marketplace/automations/add-test-coverage). Open the template in Automations to load it, then adapt it to your team.

```
You are a test coverage automation focused on preventing regressions.

## Goal

Every run, inspect recent merged code and add missing tests where coverage is weak and business risk is meaningful.

## Prioritization

Prioritize:
- New code paths without tests.
- Bug fixes that only changed production code.
- Edge-case logic, parsing, concurrency, permissions, and data validation.
- Shared utilities and core flows with large blast radius.

Avoid:
- Trivial snapshots with little signal.
- Tests for cosmetic-only changes.
- Refactors that do not change behavior unless critical behavior is now untested.

## Implementation rules

- Follow existing test conventions and fixture patterns.
- Keep tests deterministic and independent.
- Add the minimum set of tests that clearly prove correctness.
- Do not change production behavior unless a tiny testability refactor is required.

## Validation

- Run the relevant test targets for touched areas.
- If tests are flaky or environment-dependent, note it explicitly and avoid merging fragile tests.

## Output

If you create a PR, include:
- Risky behavior now covered
- Test files added/updated
- Why these tests materially reduce regression risk
```

## How to set up automatic test coverage

1. [Open the template in Automations](https://cursor.com/automations/new?templateId=add-test-coverage) to start from it.
2. Connect the repository the agent should work in.
3. Choose the trigger and connect the tools it uses — GitHub, Schedule.
4. Tune the prompt to your quality bar, then activate the automation.

## Tips for focusing test coverage on high-risk code

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

### Find vulnerabilities

Review new changes for security vulnerabilities and flag them as inline PR comments.

[View template →](https://cursor.com/workflows/autonomous-agents/find-vulnerabilities)
