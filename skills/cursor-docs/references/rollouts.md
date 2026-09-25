---
title: "Rollouts"
source: https://cursor.com/docs/rollouts
path: /docs/rollouts
---

# Rollouts

Rollouts monitors each pull request from review to production. It writes a rollout plan when the pull request opens, checks the change against your telemetry after it deploys, and reports its health in every environment.

Configure Rollouts in [Automations](https://cursor.com/automations/rollouts).

Rollouts is available on Teams and Enterprise plans.

## How it works

### Rollout plans

When a pull request opens, Rollouts reads the diff and the systems it touches, then writes a rollout plan. The plan lists the risks Rollouts found, the effect the change should have, the signals it will check, and any gaps in instrumentation that would make the change hard to verify. On GitHub, GitLab.com, and Bitbucket Cloud, Rollouts posts the plan as a comment on the pull request. On Origin, the plan appears on the pull request page.

To change the plan, mention the handle the Rollouts comment names in a pull request comment and say what to watch or ignore. Rollouts revises the plan and replies. Only people with write access to the repository can change the plan.

### Deploy tracking

Rollouts wakes on deploy events for the change's commit and runs the plan against your logs, metrics, and traces. It tracks each environment separately, so a change can be verified in staging and still flagged in production.

Rollouts checks a deploy when it happens, then again after 20 minutes, 1 hour, 1 day, and 3 days.

### Regressions

When Rollouts detects a regression, it names the change it suspects, opens an issue, and notifies the author. On the issue's page, select **Fix** to start a cloud agent on it, or **Close** it with a reason. Rollouts doesn't merge, revert, or roll back changes on its own.

### Track changes

The [Rollouts page](https://cursor.com/automations/rollouts) groups changes into **Attention**, **Monitoring**, **Pending**, and **Verified**. Each environment a change deploys to shows its own status, such as **Deploying**, **Monitoring**, **Verified**, **Deploy failed**, or **Issues found**.

A change sits in **Attention** while it has an open issue or a failed deploy. Once every issue on the change is closed, it counts as **Verified**. Reopening an issue moves it back to **Attention**.

## Set up Rollouts

In [Automations](https://cursor.com/automations), select **Enable** on the Rollouts card under **From Cursor**. Setup has four steps:

### Access to monitored repositories

Choose the repositories to watch. Every pull request that ships from these repositories gets its own watch, tied to its author. Rollouts watches repositories on Origin, GitHub, GitLab.com, and Bitbucket Cloud.

### Send deployment events to Rollouts

Tell Rollouts when each production deploy starts and finishes, using a Cursor API key stored in your CI secrets. Choose **Manually** to add the calls to your pipeline yourself. Choose **With an agent** to have a setup agent open a pull request that adds them, then merge it to finish setup.

### Telemetry

Connect your observability tools, such as Datadog, so each change is verified against what production is doing. Rollouts needs at least one connected tool. Without one, changes stay pending and Rollouts can't detect issues.

### Notifications

Choose how pull request authors get notified about their rollouts.

## Settings

Rollouts settings have four sections:

- **Code access.** The repositories Rollouts watches, up to 200, and which changes to monitor.
- **Deployment events.** How your pipeline reports what gets deployed and where.
- **Data sources.** The MCP connections Rollouts queries to verify deployed changes and detect regressions.
- **Notifications.** How you hear about deployments and regressions on your changes.

### Choose which changes to monitor

Under **Which changes to monitor**, describe in plain English the pull requests Rollouts should skip. By default, Rollouts skips changes that can't affect what runs in a deployed environment: documentation-only changes, formatting, lint, or typo fixes with no behavior change, and test-only changes. Clear the text to monitor every change in the watched repositories.

A pull request is skipped only when it clearly matches. When Rollouts skips a pull request, it says why in a comment. To monitor it anyway, mention the handle the comment names.

### Notifications

Turn on **Send Slack notifications to me** to hear about your changes in Slack. Under **Deliver to**, choose **Direct message** or **Channel**. For a channel, enter a public channel name or its ID, invite each app named under the field, then save. Slack Connect channels aren't supported.

A team admin must add Rollouts to Slack first. Only team admins can change the team's notification defaults. Slack notifications aren't available in Privacy Mode.

## Related pages

- [Automations](https://cursor.com/docs/cloud-agent/automations.md)
- [Security Agents](https://cursor.com/docs/security-agents.md)
- [Bugbot](https://cursor.com/docs/bugbot.md)
