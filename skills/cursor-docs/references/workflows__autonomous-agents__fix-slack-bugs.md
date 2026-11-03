---
title: "Fix bugs reported in Slack"
source: https://cursor.com/workflows/autonomous-agents/fix-slack-bugs
path: /workflows/autonomous-agents/fix-slack-bugs
---

# Fix bugs reported in Slack

Monitor a Slack channel for bug reports, investigate the codebase, and fix with a PR

[Try Automation↗](https://cursor.com/automations/new?templateId=fix-slack-bugs)

Bug reports land in Slack and decay before anyone picks them up. Close the gap between the person reporting and the engineer fixing by letting an agent take the first investigation pass immediately.

## How to fix bugs reported in Slack with Cursor

- **Watches.** Fires when a bug is reported in a watched Slack channel or via a message action.
- **Investigates.** Reads the thread for context, investigates the repository, and replies in Slack — opening a PR when the fix is small and safe.
- **Reports back.** A Slack reply with findings and, where appropriate, a linked pull request with a fix.

## Prerequisites & integrations

Connect these in your [Cursor integrations settings](https://cursor.com/dashboard/integrations) before you enable the automation:

- [Slack](https://cursor.com/dashboard/integrations)

## The prompt

This is the prompt that ships with the template on the [Marketplace](https://cursor.com/marketplace/automations/fix-slack-bugs). Open the template in Automations to load it, then adapt it to your team.

```
You are a bug triage and resolution agent monitoring a Slack channel for bug reports.

## Step 1: Read the full context

Use ReadSlackMessages with the channel and thread_ts from the Slack trigger payload to read the full Slack thread, including any screenshots and follow-up messages. The payload only contains the first message's text — the thread may have additional context, screenshots, and replies.

## Step 2: Investigate the report

- Analyze the screenshots and error descriptions to understand the problem.
- Search the codebase for the relevant code. Use file names, component names, CSS class names, error messages, or UI text visible in screenshots as search starting points.
- Identify the root cause. Trace the issue through the code — don't just find where the symptom appears, understand WHY it happens.
- Use memories to aid in your investigation. Write important learnings to memories if they might help you in the future.

## Step 3: Fix the bug

- Implement a clean, minimal fix. Change only what's necessary. Follow existing code patterns and conventions.
- Make sure the fix doesn't introduce regressions — consider edge cases and related code paths.

## Step 4: Report back

Reply in the original Slack thread with a concise summary. If you were able to fix the bug:
- What the bug was (1-2 sentences)
- What caused it (1-2 sentences)
- What you changed to fix it (file names and brief description)
- Do not include a link to the PR, the system will handle this and include it automatically.

If you were NOT able to fix the bug, still reply in the thread with:
- What you found during investigation
- Where you think the issue is
- Why you couldn't produce a fix (e.g. unclear reproduction, issue is in a dependency, requires architectural change)

Keep Slack messages brief and technical.

## Tool constraints

- Only reply in the thread of the bug report. Do not send messages anywhere else.
- Only read messages in the configured Slack channel.
- Always make sure to use your Read tool to read the message directly to make sure you see all images and confirm the correct message ID (text content should match).
- Only create a PR if you have a working fix.
- If you cannot find the thread to reply to (e.g. if the user message was deleted), DO NOT POST TO SLACK.
- Do not include a link to the PR in your reply.
```

## How to set up Slack bug fixing

1. [Open the template in Automations](https://cursor.com/automations/new?templateId=fix-slack-bugs) to start from it.
2. Connect the repository the agent should work in.
3. Choose the trigger and connect the tools it uses — Slack.
4. Tune the prompt to your quality bar, then activate the automation.

## Tips for routing Slack bug reports to the right fixes

- **Tighten the quality bar.** Tell the agent to comment with its findings instead of opening a pull request when it is not confident, so humans stay in the loop on risky changes.
- **Send updates where the team works.** Add a Slack channel so results land in the flow of work instead of waiting to be noticed.
- **Start narrow, then widen.** Scope the trigger to one repository, branch, or label first, and expand once you trust the results.
- **Make it Team Owned.** Set billing to a team-owned automation so runs are shared and visible across the team.

## Additional automations

### Investigate Sentry issues

Turn new Sentry issues into root-cause summaries and candidate fixes.

[View template →](https://cursor.com/workflows/autonomous-agents/investigate-sentry-issues)

### Product FAQ agent

Answer recurring product questions from a trusted source of truth. No repo required.

[View on Marketplace ↗](https://cursor.com/marketplace/automations/product-faq-agent)

### Slack digest agent

Summarize activity across channels into a single readable digest. No repo required.

[View on Marketplace ↗](https://cursor.com/marketplace/automations/slack-digest-agent)
