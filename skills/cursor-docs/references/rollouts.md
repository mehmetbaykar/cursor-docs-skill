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

When Rollouts detects a regression, it names the change it suspects, opens an issue, and notifies the author. It does the same when a change causes no regression but doesn't work as intended: the new code path ran, but its effect is missing, it errors, or its behavior is wrong. On the issue's page, select **Fix issue** to start a cloud agent on it, or **Close** it with a reason. The agent opens in a panel on the issue's page. After a fix starts, **View fix** takes the place of **Fix issue** and reopens that agent. Rollouts doesn't merge, revert, or roll back changes on its own.

### Track changes

The [Rollouts page](https://cursor.com/automations/rollouts) lists merged pull requests and groups them into **Attention**, **Monitoring**, **Pending**, and **Verified**. Each environment a change deploys to shows its own status, such as **Deploying**, **Monitoring**, **Verified**, **Deploy failed**, or **Issues found**.

A change sits in **Attention** while it has an open issue or a failed deploy. Once every issue on the change is closed, it counts as **Verified**. Reopening an issue moves it back to **Attention**.

### Services

Select **Services** at the top of the Rollouts page to see each service your deployment pipeline reports. To hide a service from that list, open it and select **Archive**. Its deployments stay in history. The service moves under **Archived**, where **Restore** brings it back.

## Set up Rollouts

In [Automations](https://cursor.com/automations), open the **Team** tab and select **Enable** on the Rollouts card under **From Cursor**. Setup has four steps:

### Access to monitored repositories

Choose the repositories to watch. Every pull request that ships from these repositories gets its own watch, tied to its author. Rollouts watches repositories on Origin, GitHub, GitLab.com, and Bitbucket Cloud.

### Send deployment events to Rollouts

Tell Rollouts when each production deploy starts and finishes. [Create an API key](https://cursor.com/docs/api.md#creating-api-keys) and store it as the `CURSOR_API_KEY` CI secret. Use a user API key, a service account API key, or a team Admin API key with the `admin:*` scope. You can either do this [manually](https://cursor.com/docs/rollouts.md#send-deployment-events) or with an agent. With an agent, a setup agent opens a pull request that adds the calls, then you merge it to finish setup.

### Telemetry

Connect your observability tools, such as Datadog, so each change is verified against what production is doing. Rollouts needs at least one connected tool. Without one, changes stay pending and Rollouts can't detect issues.

### Notifications

Choose how pull request authors get notified about their rollouts.

## Send deployment events

### Exchange the API key for a token

At the top of the deploy job, exchange the `CURSOR_API_KEY` secret for a token. Every call below sends this token.

```bash
TOKEN=$(curl -s -X POST https://api2.cursor.sh/auth/exchange_user_api_key \
  -H "Authorization: Bearer $CURSOR_API_KEY" -H "Content-Type: application/json" -d '{}' \
  | jq -r .accessToken)
```

### Create each environment and service once

Run this by hand, or as a bootstrap step before the deploy job. It creates the rows the calls below name, so run it before the first report.

```bash
curl -s -X POST https://api.cursor.com/factory.v1.DeploymentsService/CreateEnvironment -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -H "Connect-Protocol-Version: 1" \
  -d '{"environmentId":"{env}","environment":{"displayName":"{env}"}}'
curl -s -X POST https://api.cursor.com/factory.v1.DeploymentsService/CreateService -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -H "Connect-Protocol-Version: 1" \
  -d '{"serviceId":"{service}","service":{"displayName":"{service}"}}'
```

### Create the deployment

Run this right before you ship. `deployVersion` is the commit SHA being shipped.

```bash
DEPLOYMENT=$(curl -s -X POST https://api.cursor.com/factory.v1.DeploymentsService/CreateDeployment -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -H "Connect-Protocol-Version: 1" \
  -d '{"deployment":{"deploySourceUri":"https://github.com/{owner}/{repo}","environment":"environments/{env}","service":"services/{service}","deployVersion":"'"$GIT_SHA"'"},"event":{"started":{},"actor":"'"$CI_JOB_URL"'"}}' \
  | jq -r .deployment.name)
```

### Append the finished event

Run this right after the outcome is known. A failed report must never fail the deploy.

```bash
curl -s -X POST https://api.cursor.com/factory.v1.DeploymentsService/AppendDeploymentEvent -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -H "Connect-Protocol-Version: 1" \
  -d '{"name":"'"$DEPLOYMENT"'","event":{"completed":{"succeeded":{}},"actor":"'"$CI_JOB_URL"'"}}'
# On failure:   "event":{"completed":{"failed":{"message":"<why>"}},"actor":...}
# If cancelled: "event":{"aborted":{},"actor":...}
```

## Settings

Rollouts settings have four sections:

- **Code access.** The repositories Rollouts watches, up to 200, and which changes to monitor.
- **Deployment events.** How your pipeline reports what gets deployed and where.
- **Data sources.** The MCP connections Rollouts queries to verify deployed changes and detect regressions.
- **Notifications.** How you hear about deployments and regressions on your changes.

The switch at the top of Settings turns Rollouts on or off for your team. Its label reads **Enabled** or **Disabled**.

### Choose which changes to monitor

Under **Which changes to monitor**, describe in plain English the pull requests Rollouts should skip. By default, Rollouts skips changes that can't affect what runs in a deployed environment: documentation-only changes, formatting, lint, or typo fixes with no behavior change, and test-only changes. Clear the text to monitor every change in the watched repositories.

A pull request is skipped only when it clearly matches. When Rollouts skips a pull request, it says why in a comment. To monitor it anyway, mention the handle the comment names.

### Notifications

Turn on **Personal Slack Notifications** to hear about your changes in Slack. It starts with **Issues found** messages only. To also hear when a deployment succeeds or fails, or when a check finds no issues, turn on **Deployment succeeded**, **Deployment failed**, or **Check clear**. Under **Deliver to**, choose **Direct message** or **Channel**. For a channel, enter a public channel name or its ID, invite each app named under the field, then save. Slack Connect channels aren't supported.

A team admin must add Rollouts to Slack first. Only team admins can change the team's notification defaults. Turning on the team default sends members a Slack message when a check finds issues with their pull request, until they change their own settings. Slack notifications aren't available in Privacy Mode.

## Related pages

- [Automations](https://cursor.com/docs/cloud-agent/automations.md)
- [Security Agents](https://cursor.com/docs/security-agents.md)
- [Bugbot](https://cursor.com/docs/bugbot.md)
