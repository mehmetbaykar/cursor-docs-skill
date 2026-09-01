---
title: "Self-Hosted Agents"
source: https://cursor.com/docs/cloud-agent/self-hosted-guides/pool
path: /docs/cloud-agent/self-hosted-guides/pool
---

# Self-Hosted Agents

Self-Hosted Pool is for Enterprise teams that want Cloud Agents to run inside company-managed infrastructure. Instead of each developer starting a worker on a personal machine, admins operate a pool of workers that can be assigned to agents across the organization.

Self-hosted pools are an infrastructure-ownership choice. They do not move the agent loop out of Cursor's cloud. The worker executes terminal commands, file edits, browser actions, and other tool calls in your infrastructure while Cursor handles orchestration, model access, and the Cloud Agent experience.

Cursor-managed Cloud Agents are the recommended path for most teams, including
teams that need private network access. Use managed environments with network
controls, Tailscale or a similar client, or private connectivity for supported
source control paths before taking on a worker fleet. See [Choose where Cloud
Agents run](https://cursor.com/docs/cloud-agent/self-hosted-guides/choose-runtime.md).

Use a pool when you need:

- Centrally managed workers for a team or organization
- Service account authentication instead of individual browser logins
- Kubernetes, autoscaling, or fleet management
- Labels that route work to the right environment, team, repo, or hardware profile
- Company-owned hosts for tool execution, build outputs, worker logs, and monitoring

For a fast personal setup, see [My Machines](https://cursor.com/docs/cloud-agent/self-hosted-guides/my-machines.md).

## How it works

A worker opens a long-lived outbound HTTPS connection to Cursor's cloud. The agent loop, including inference and planning, runs in Cursor's cloud and sends tool calls over this connection. The worker executes those tool calls in your infrastructure: terminal commands, file edits, browser actions, and access to internal services.

Your repos, build caches, secrets, and tool execution stay in your environment while Cursor handles orchestration, model access, and the Cloud Agent experience. Cloud Agent [artifacts](https://cursor.com/docs/cloud-agent/self-hosted-guides/pool.md#artifacts), like screenshots and videos, are uploaded to Cursor so you can view them in PRs and the dashboard.

Workers only need outbound access. No inbound ports, public IPs, or VPN tunnels are required. See [Networking](https://cursor.com/docs/cloud-agent/self-hosted-guides/pool.md#networking) for the full list of required hosts.

Self-Hosted Cloud Agents support up to 10 workers per user and 50 per team. For larger company-wide deployments, [contact us](https://cursor.com/contact-sales?source=self-hosted-agents) to discuss scaling.

## Prerequisites

- A **Cursor Enterprise plan**
- Self-hosted settings configured by a team admin in the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#self-hosted-agents):
  - **Allow Self-Hosted Agents** lets users opt in to self-hosted runs.
  - **Require Self-Hosted Agents** routes every Cloud Agent run to self-hosted workers.
- A [service account API key](https://cursor.com/docs/account/enterprise/service-accounts.md) for pool worker authentication
- A worker machine or image with:
  - `agent` CLI installed
  - `git` installed and available on `PATH` (required when the worker serves git remotes or uses [`--clone-git-repos`](https://cursor.com/docs/cloud-agent/self-hosted-guides/pool.md#repo-less-pools); optional for [repo-less pools](https://cursor.com/docs/cloud-agent/self-hosted-guides/pool.md#repo-less-pools) if your own scripts handle SCM)
  - A workspace directory (a cloned repository with a configured remote, or a [repo-less](https://cursor.com/docs/cloud-agent/self-hosted-guides/pool.md#repo-less-pools) directory)
  - Access to the build tools, package registries, secrets, and internal services your agents need

## Install the CLI

```bash
# macOS, Linux, and WSL
curl https://cursor.com/install -fsS | bash

# Windows PowerShell
irm 'https://cursor.com/install?win32=true' | iex
```

Confirm the CLI is available:

```bash
agent --version
```

## Authenticate workers

Pool workers must authenticate with a [service account API key](https://cursor.com/docs/account/enterprise/service-accounts.md).

User, personal, team, and organization API keys can't start pool workers. Use personal or user API keys with personal workers on [My Machines](https://cursor.com/docs/cloud-agent/self-hosted-guides/my-machines.md).

```bash
export CURSOR_API_KEY="your-service-account-api-key"
```

You can also pass the key directly:

```bash
agent worker --api-key "your-service-account-api-key" start
```

## Start a pool worker

Run the worker from the workspace it should serve (a git repo root, or a [repo-less](https://cursor.com/docs/cloud-agent/self-hosted-guides/pool.md#repo-less-pools) directory):

```bash
cd /path/to/repo
agent worker --pool start
```

`--pool` registers the worker for pool assignment. Pass an optional name to join a named pool (for example, `--pool gpu`). When the name is omitted, the worker joins `default`. Each Cloud Agent session claims one worker at a time.

For orchestrated environments, combine it with `--idle-release-timeout` so the process exits cleanly after work completes:

```bash
agent worker --pool gpu --idle-release-timeout 600 start
```

`--idle-release-timeout` keeps the worker alive for a window (in seconds) after a session ends to handle follow-up messages. If a follow-up arrives, the timer resets. Once the timeout fires, the CLI exits with code 0. The default is `3600` seconds; pass `0` to disable idle-based release.

## Register multiple repo roots

Self-hosted multi-repo support is configured at worker startup by registering multiple workspace roots. Pass `--worker-dir` once for each local repo root. The first root is the primary repository for assignment identity and dashboard display. All roots are exposed to the agent runtime, and roots with valid git origins register repository routing metadata.

`--worker-dir` is repeatable up to 20 paths. Each path must already exist and be a directory. If you don't pass `--worker-dir`, the CLI uses the current working directory.

Before you start, enable self-hosted workers in **Dashboard** > **Cloud Agents** > **Self-Hosted**. Use writable paths under `$HOME` unless your own machine image guarantees another writable location.

Example setup:

```bash
export WORKER_ROOT="$HOME/cursor-repos/my-org"
mkdir -p "$WORKER_ROOT"

git clone git@github.com:my-org/app.git "$WORKER_ROOT/app"
git clone git@github.com:my-org/infra.git "$WORKER_ROOT/infra"

export CURSOR_API_KEY="<key>"
```

Run a preflight check before starting the worker:

```bash
agent worker \
  --pool app-infra \
  --name app-infra-worker \
  --worker-dir "$WORKER_ROOT/app" \
  --worker-dir "$WORKER_ROOT/infra" \
  debug --json
```

Start the worker with the same roots:

```bash
agent worker \
  --pool app-infra \
  --name app-infra-worker \
  --worker-dir "$WORKER_ROOT/app" \
  --worker-dir "$WORKER_ROOT/infra" \
  start --verbose
```

Place worker options before `start` or `debug`. Leave the process running under a supervisor like `systemd`, `tmux`, `launchd`, Kubernetes, or your own process manager.

Verbose startup logs are the source of truth for registered roots. A successful multi-repo worker shows each derived repo label, the workspace paths, and the repository URLs:

```text
repo=my-org/app
repo=my-org/infra
workspacePaths: [app, infra]
x-repository-urls: ["git@github.com:my-org/app.git","git@github.com:my-org/infra.git"]
```

The dashboard currently displays a self-hosted worker under its primary repo.
There is no named self-hosted multi-repo environment object in the portal yet.
This can look like only the first repo is registered. Check `workspacePaths`
and `x-repository-urls` in verbose logs to confirm all roots. To make another
repo primary, put its `--worker-dir` first.

Use `--name` and `--pool <name>` to make multi-repo workers recognizable in the dashboard and triggers.

In pool mode, one Cloud Agent claims the worker at a time. Without `--pool`, shared assignment is allowed. Add `--management-addr 0.0.0.0:8080` before `start` when you need `/healthz`, `/readyz`, and `/metrics` for an orchestrator.

Non-git directories can be execution roots, but they don't contribute repo routing metadata. All repos needed by the agent must already be cloned and accessible to the worker before the process starts. The worker process also needs filesystem and SCM access to each root.

## Repo-less pools

A pool worker does not require a git remote. Point `--worker-dir` at any existing directory when you want the agent (or your own hooks and scripts) to manage cloning and git state:

```bash
mkdir -p "$HOME/cursor-sandboxes/default"
agent worker --pool sandbox --worker-dir "$HOME/cursor-sandboxes/default" start
```

To have the worker clone the claimed agent's repos on claim, pass `--clone-git-repos`. This is opt-in. Default any-repo behavior does not clone.

```bash
agent worker --pool sandbox --clone-git-repos start
```

`--clone-git-repos` implies `--mint-github-token`. Clone uses that minted short-lived GitHub token. A team admin must enable GitHub token minting for self-hosted pool workers, and `git` must be on `PATH`.

Use this flag only on any-repo pool workers: a named `--pool` other than `default`, with no bound repository (`repo=`) and no bound machine (`name=`). The CLI exits with a clear error on a bound-repo worker, a named machine, the `default` pool, or a personal [My Machines](https://cursor.com/docs/cloud-agent/self-hosted-guides/my-machines.md) worker.

Branch names clone with `--branch`. A full 40-character commit SHA uses a detached checkout after clone. Use HTTPS GitHub remotes so the minted token can authenticate.

If clone fails, the request stays in the queue. Operators see a generic clone failure.

`--clone-git-repos`, `--mint-github-token`, and `--sync-dashboard-secrets` assume one worker per container or OS user. Co-locating multiple credential-enabled workers under the same user is unsupported.

Repo-less pools omit `repo=` routing labels. Start agents against them with `env.type: "pool"` and `env.name` set to the pool name, and omit `repos` (see [Create An Agent](https://cursor.com/docs/cloud-agent/api/endpoints.md#create-an-agent)). In the dashboard, repo-less pools appear under an **Any repo** grouping.

Durable pool records stay registered after the last worker disconnects, so a repo-less (or repo-bound) pool remains selectable at zero capacity. Use [List Pools](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pools) and [pending requests](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pending-pool-requests) to scale workers back up.

## Pool names

Group pool workers under a name when you want sessions to route to a specific subset, like GPU machines, a staging fleet, or a team's dedicated build boxes.

Pass the name to `--pool`:

```bash
agent worker --pool gpu start
```

When the name is omitted, the worker joins the `default` pool. Older CLI versions that only supported a boolean `--pool` plus separate `--pool-name` continue to work; `--pool-name` is a deprecated alias for `--pool <name>`.

Set the pool name from the environment when an orchestrator injects config:

```bash
export CURSOR_WORKER_POOL_NAME=gpu
agent worker --pool start
```

Multi-use workers (started without `--pool`) don't belong to a pool.

From the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents), pick a pool in the worker selector when starting a session or editing an automation. You can also include `pool=<name>` in a Slack, GitHub, or Linear trigger. Sessions route only to workers registered with that pool name.

## Triggering pool agents

Use pool triggers when you want a Cloud Agent to run on your team's shared worker fleet. Pool workers are the right target for centrally managed capacity, autoscaling, CI-like runners, and repo-scoped infrastructure.

Team admins control self-hosted routing from the Self-Hosted section of the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents). **Allow Self-Hosted Agents** lets users opt in per request. Without opt-in, runs use Cursor's managed infrastructure. **Require Self-Hosted Agents** routes Cloud Agent runs to self-hosted workers.

When Cursor starts a pool agent, it matches workers with labels. Every pool request includes a `repo=<owner/repo>` label. Requests for a named pool also include `pool=<name>`.

Pool workers handle:

- Runs covered by **Require Self-Hosted Agents**, unless the request targets a specific My Machines worker with `worker=` or `machine=`
- Requests with `self_hosted=true`, `self_hosted`, or `selfhosted`
- Requests with `pool=<name>`, which also selects that named pool
- Self-hosted requests with repository selection from the trigger surface, such as `repo=<owner/repo>` where supported

`repo=` selects the repository for the run. For self-hosted pool runs, that repository becomes the `repo=<owner/repo>` worker label. It does not target a personal machine.

Use these options from integrations to start pool agents:

- **Slack**: Mention `@Cursor` with `self_hosted=true`, standalone `self_hosted`, `selfhosted`, or `pool=<name>`. Legacy aliases like `private_worker=true`, `useprivateworker`, and `useprivateworkers=false` still work.
- **GitHub**: Comment `@cursoragent self_hosted=true ...` or `@cursoragent pool=<name> ...` on an issue, pull request, or review comment. The legacy `private_worker=true` alias still works.
- **Linear**: Add `pool=<name>` or `[pool=<name>]` to the issue body. You can also use issue or project labels where the parent label is `pool` and the child label is the value. Linear does not parse standalone `self_hosted=true`.

Policy handling depends on where the request starts:

- **Slack** rejects self-hosted opt-in when Allow Self-Hosted Agents is off and replies in Slack. If Require Self-Hosted Agents is on, every Slack mention runs self-hosted.
- **GitHub** lets repo `OWNER` and `COLLABORATOR` users route runs to self-hosted workers. Other commenters run on managed infrastructure when they opt in, or are skipped if Require Self-Hosted Agents is on. This protects public repos where outside contributors can leave comments.
- **Linear** rejects explicit self-hosted requests when Allow Self-Hosted Agents is off. The issue gets an agent activity error that asks an admin to turn on self-hosted workers or remove the hint to run on Cursor's managed infrastructure.

To target one of your own machines by name, use [My Machines](https://cursor.com/docs/cloud-agent/self-hosted-guides/my-machines.md#trigger-this-machine-from-a-chat-surface) with `worker=` or `machine=`.

The Cloud Agent API uses the same resolver with `usePrivateWorker` and `labels` fields. See the [Cloud Agent API docs](https://cursor.com/docs/cloud-agent/api/endpoints.md) for endpoint details.

## Hooks

Self-hosted workers run project hooks committed in your repository through `.cursor/hooks.json`.

If you're on Enterprise, self-hosted workers also support team hooks and enterprise-managed hooks.

See [Hooks](https://cursor.com/docs/hooks.md) for configuration details.

## Labels

Labels are key-value pairs that describe a worker. They control how Cloud Agent sessions route to the right pool.

### CLI flags

Good for quick testing or small pools:

```bash
agent worker \
  --pool \
  --label team=backend \
  --label env=production \
  start
```

### JSON file

Better for production where labels are managed as config:

```json
{
  "team": "backend",
  "env": "production",
  "capabilities": ["docker", "gpu"]
}
```

```bash
agent worker --pool --labels-file labels.json start
```

### TOML file

Same as JSON, different format:

```toml
team = "backend"
env = "production"
capabilities = ["docker", "gpu"]
```

```bash
agent worker --pool --labels-file labels.toml start
```

### Environment variable

Useful when the path is injected by your orchestrator:

```bash
export CURSOR_WORKER_LABELS_FILE=/path/to/labels.json
agent worker --pool start
```

The `repo` and `pool` labels are reserved. `repo` comes from the worker directory's git remote when present. `pool` is set by [`--pool`](https://cursor.com/docs/cloud-agent/self-hosted-guides/pool.md#pool-names). Don't set either manually.

## MCP servers

MCP servers on self-hosted workers are routed by transport type:

| Transport        | Runs on        | Use case                                                                                                               |
| ---------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Command (stdio)  | Worker         | The MCP process starts on the worker and can reach private networks, internal APIs, and services behind your firewall. |
| HTTP / SSE (url) | Cursor backend | Cursor handles OAuth, session caching, and auth for HTTP-based MCP servers.                                            |

If your MCP server needs to access private-network endpoints, use the command (stdio) transport. The process runs directly on the worker and shares its network. For HTTP-based MCP servers, Cursor manages the connection from its backend, handling OAuth and session caching.

## Artifacts

Artifact behavior is identical on self-hosted workers and Cursor-hosted agents. The agent produces the artifact inside the worker and the worker uploads it to Cursor-managed storage over HTTPS. Everything downstream (PR embeds, dashboard previews, notification attachments) is handled by Cursor's backend and doesn't depend on where the worker runs.

Artifacts are on by default. See [Capabilities](https://cursor.com/docs/cloud-agent/capabilities.md#demos-and-artifacts) for what they look like in the UI.

To disable artifact uploads, block outbound traffic to `cloud-agent-artifacts.s3.us-east-1.amazonaws.com`. The agent session keeps working; artifacts produced during the session fail to upload.

## Networking

Workers need outbound HTTPS access to:

- `api2.cursor.sh` and `api2direct.cursor.sh` for the agent session
- `cloud-agent-artifacts.s3.us-east-1.amazonaws.com` for [artifact](https://cursor.com/docs/cloud-agent/self-hosted-guides/pool.md#artifacts) uploads

If your firewall can only match wildcards, `*.s3.us-east-1.amazonaws.com` covers the artifact host, but also opens every other bucket in the region. Prefer an exact-host rule when the firewall supports it.

No inbound ports, public IPs, or VPN tunnels are required. If you use a proxy, set `HTTPS_PROXY` or `https_proxy` in the worker environment.

### Failure modes

| If you block...                                       | Effect                                                                                                                                                                        |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api2.cursor.sh` or `api2direct.cursor.sh`            | The worker can't start or continue an agent session.                                                                                                                          |
| `cloud-agent-artifacts.s3.us-east-1.amazonaws.com`    | Artifact uploads fail. PR embeds, dashboard previews, and notification attachments that depend on artifacts are missing. The agent session and other tool calls keep working. |
| An outbound host a specific tool or integration needs | Only that tool or integration fails. The agent continues.                                                                                                                     |

The [Prerequisites](https://cursor.com/docs/cloud-agent/self-hosted-guides/pool.md#prerequisites) section covers the broader set of hosts a worker needs during agent runs (git hosts, package registries, internal APIs).

## Kubernetes

We provide a Helm chart and Kubernetes operator for managing worker pools at scale. See the [Kubernetes deployment guide](https://cursor.com/docs/cloud-agent/self-hosted-guides/kubernetes.md) for setup instructions.

## Reference deployments

The [self-hosted Cloud Agents cookbook](https://github.com/cursor/cookbook/tree/main/self-hosted-cloud-agent) has Terraform and Helm examples for running worker pools on AWS:

- [EC2 + Docker](https://github.com/cursor/cookbook/tree/main/self-hosted-cloud-agent/ec2): one worker container on a single host. The smallest footprint.
- [ECS/Fargate](https://github.com/cursor/cookbook/tree/main/self-hosted-cloud-agent/ecs): AWS-native service with CloudWatch metrics and ECS Service Auto Scaling.
- [EKS + Helm](https://github.com/cursor/cookbook/tree/main/self-hosted-cloud-agent/eks): Kubernetes path using Cursor's worker-set controller and `WorkerDeployment` resources.

Each guide has an architecture overview and a copy-paste setup README.

## Worker controller

`agent worker controller` starts workers from a `--spawn` hook. It keeps process-forked workers. It does not patch a Kubernetes `WorkerDeployment`. On Kubernetes, keep warm size with `WorkerDeployment.spec.readyReplicas`. See the [Kubernetes deployment guide](https://cursor.com/docs/cloud-agent/self-hosted-guides/kubernetes.md#scaling).

`--spawn <path>` is required. The hook runs once after a successful claim, or once per missing warm worker. Hook environment includes `CURSOR_API_KEY`, `CURSOR_API_URL`, `CURSOR_API_ENDPOINT`, `CURSOR_AGENT_WORKER_ID`, and request fields. Authenticate with a [service account](https://cursor.com/docs/account/enterprise/service-accounts.md) key via `--api-key` or `CURSOR_API_KEY`. The key binds the team. Session login is not used.

| Flag                  | Description                                                                                                                           |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `--spawn <path>`      | Script to run once after a successful claim, or once per missing warm worker. Required.                                               |
| `--api-key <key>`     | Service account API key. Also readable from `CURSOR_API_KEY`. Session login is not used.                                              |
| `--pool <name>`       | Pool to watch (repeatable). Mutually exclusive with `--all-pools`. Warm mode requires `--pool`.                                       |
| `--all-pools`         | Team-wide pending-requests list and stream. Does not register pools. Not allowed in warm mode.                                        |
| `--warm-idle <count>` | Keep `count` idle workers per `--pool` and skip claiming.                                                                             |
| `--repository <url>`  | Filter pending requests by repository. Required for repo-scoped keys. In warm mode, also pins the pool idle-count to that repo's row. |
| `--endpoint <url>`    | Public API base (default `https://api.cursor.com`). Also readable from `CURSOR_API_ENDPOINT`.                                         |

The spawn hook should start a worker with the same worker id:

```bash
#!/usr/bin/env bash
set -euo pipefail
agent worker --pool "$CURSOR_POOL" --worker-id "$CURSOR_AGENT_WORKER_ID" start
```

The worker CLI also reads `CURSOR_AGENT_WORKER_ID` from the environment.

### Claim-then-spawn

Default mode. The controller lists pending requests, watches `GET /v0/private-workers/pending-requests/stream`, claims each request, and execs `--spawn` once per claim.

```bash
agent worker controller --spawn ./spawn.sh --api-key "$CURSOR_API_KEY" --pool gpu --pool default
```

### Warm pool

`--warm-idle <count>` keeps `<count>` idle workers connected in each `--pool` by pre-spawning unclaimed workers. It never calls claim. Cursor assigns queued agents to those warm workers.

The controller reconciles against `GET /v0/private-workers/pools` every 60 seconds. The pending-requests SSE stream only accelerates backfill.

Warm mode requires `--pool`. You cannot combine it with `--all-pools`. Run one warm controller per pool: there is no server-side spawn lease, so concurrent controllers can transiently over-spawn.

```bash
agent worker controller --spawn ./spawn.sh --api-key "$CURSOR_API_KEY" --pool gpu --warm-idle 5
```

To build a custom controller instead, use the [fleet management API](https://cursor.com/docs/cloud-agent/self-hosted-guides/pool.md#fleet-management-api).

## Fleet management API

For non-Kubernetes environments, use the fleet management API to monitor utilization and build autoscaling. See the [Cloud Agents API reference](https://cursor.com/docs/cloud-agent/api/endpoints.md#fleet-management) for the full endpoint list, including durable [pools](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pools), [pending requests](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pending-pool-requests), the [SSE queue watch](https://cursor.com/docs/cloud-agent/api/endpoints.md#watch-pending-pool-requests), [claim](https://cursor.com/docs/cloud-agent/api/endpoints.md#claim-a-pending-request), and [release](https://cursor.com/docs/cloud-agent/api/endpoints.md#release-a-claim).

Authenticate with the pool's service account API key via Basic auth or Bearer token. Other API key types can't manage pool worker fleet capacity.

### List workers

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers?status=idle&scope=team_pool&limit=50" \
  -u "$CURSOR_API_KEY:"
```

| Parameter   | Type                               | Default | Description                                                       |
| ----------- | ---------------------------------- | ------- | ----------------------------------------------------------------- |
| `status`    | `all` \| `in_use` \| `idle`        | `all`   | Filter by worker status                                           |
| `scope`     | `all` \| `team_pool` \| `personal` | `all`   | Filter by worker scope                                            |
| `limit`     | integer (1-100)                    | `50`    | Results per page                                                  |
| `pageToken` | string                             |         | Pagination cursor: the `nextPageToken` from the previous response |

Workers include `name`, `isInUse`, connection metadata, and repo fields (`repoOwner`/`repoName` are empty strings for repo-less workers). See the [API reference](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-workers) for the full response.

### List pools

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/pools?scope=team_pool" \
  -u "$CURSOR_API_KEY:"
```

Returns durable pools with `connectedWorkerCount`, `inUseWorkerCount`, `isStale`, and optional repo fields. Repo-less pools omit repo fields.

### Get summary

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/summary" \
  -u "$CURSOR_API_KEY:"
```

Returns connected and in-use counts for your user and team. Use this to trigger scaling when utilization is high:

```typescript
const summary = await response.json();
const team = summary.teamSummary;
if (team && team.totalConnected > 0) {
  const utilization = team.inUse / team.totalConnected;
  if (utilization >= 0.9) {
    // Scale up: provision additional workers
  }
}
```

### Get worker by ID

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/pw_123" \
  -u "$CURSOR_API_KEY:"
```

### Claim a pending request

Ephemeral controllers can reserve a queued request before starting a worker:

```bash
curl --request POST \
  --url "https://api.cursor.com/v0/private-workers/claim" \
  -u "$CURSOR_API_KEY:" \
  --header 'Content-Type: application/json' \
  --data '{
    "id": "bc-00000000-0000-0000-0000-000000000002",
    "workerId": "pw_123"
  }'
```

Then start the worker with the same id (`CURSOR_AGENT_WORKER_ID=pw_123`). See [Claim A Pending Request](https://cursor.com/docs/cloud-agent/api/endpoints.md#claim-a-pending-request).

### Release a claim

Drop the claim that binds an agent to a self-hosted worker. Cursor then stops preferring that machine for the agent:

```bash
curl --request POST \
  --url "https://api.cursor.com/v0/private-workers/claims/bc-00000000-0000-0000-0000-000000000002/release" \
  -u "$CURSOR_API_KEY:"
```

A second claim while a live claim exists is rejected; release first, then claim a new `workerId`. See [Release A Claim](https://cursor.com/docs/cloud-agent/api/endpoints.md#release-a-claim).

## Monitoring

The management server exposes `GET /metrics`, `GET /healthz`, and `GET /readyz` when you start a worker with `--management-addr`:

```bash
agent worker --pool --management-addr ":8080" start
```

Scrape metrics from your worker:

```bash
curl http://localhost:8080/metrics
```

### Available metrics

**Gauges**

| Metric                                                 | Type  | Description                                                                                |
| ------------------------------------------------------ | ----- | ------------------------------------------------------------------------------------------ |
| `cursor_self_hosted_worker_connected`                  | Gauge | `1` when the outbound connection to Cursor's cloud is active, `0` otherwise.               |
| `cursor_self_hosted_worker_session_active`             | Gauge | `1` when a cloud agent session is running on this worker, `0` when idle.                   |
| `cursor_self_hosted_worker_last_activity_unix_seconds` | Gauge | Unix timestamp of the last frame or heartbeat from Cursor's cloud. `0` if no activity yet. |

**Counters**

| Metric                                             | Type    | Description                                               |
| -------------------------------------------------- | ------- | --------------------------------------------------------- |
| `cursor_self_hosted_worker_connect_attempts_total` | Counter | Outbound connection attempts to Cursor's cloud.           |
| `cursor_self_hosted_worker_connect_retry_total`    | Counter | Connection retries after a failed attempt.                |
| `cursor_self_hosted_worker_session_ends_total`     | Counter | Agent sessions ended on this worker, labeled by `reason`. |

### Session end reasons

The `cursor_self_hosted_worker_session_ends_total` counter includes a `reason` label with one of these values:

| Reason               | Description                                                      |
| -------------------- | ---------------------------------------------------------------- |
| `stream_end`         | Connection closed normally.                                      |
| `stream_error`       | Connection failed with an error.                                 |
| `session_closed`     | HTTP/2 session closed cleanly.                                   |
| `session_error`      | HTTP/2 session entered an error state.                           |
| `connection_timeout` | Initial connection timed out before streaming started.           |
| `session_aborted`    | Session was aborted, for example because the worker was stopped. |

## Security

**Data flow.** Two things leave your network: file chunks the model reads during inference, and Cloud Agent [artifacts](https://cursor.com/docs/cloud-agent/self-hosted-guides/pool.md#artifacts) (screenshots, videos, and log references) the worker uploads to Cursor-managed storage so they can appear in PRs and the dashboard. Your repos, build caches, and secrets stay on your machines.

**Outbound-only.** Workers connect outbound over HTTPS. No inbound ports or firewall changes required.

**Privacy mode.** Self-hosted Cloud Agents respect Cursor's [Privacy Mode settings](https://cursor.com/data-use). When Privacy Mode is enabled, none of your code is used for training.

**Isolation.** Each agent session gets its own dedicated worker. Sessions are not shared across workers.

**Authentication.** Pool workers authenticate with a [service account API key](https://cursor.com/docs/account/enterprise/service-accounts.md). Other API key types are rejected.

**Dashboard visibility.** Team admins can see all connected workers. Team members see only workers assigned to them.

## CLI reference

```bash
agent worker [options] start
```

| Flag                           | Env var                              | Description                                                                                                                                                                                                                                                          |
| ------------------------------ | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--worker-dir <path>`          |                                      | Workspace root to expose to agents. Repeatable up to 20 paths. Each path must exist and be a directory. Git remotes are optional; see [repo-less pools](https://cursor.com/docs/cloud-agent/self-hosted-guides/pool.md#repo-less-pools). Default: current directory. |
| `--management-addr <addr>`     |                                      | Address for `/healthz`, `/readyz`, and `/metrics` endpoints, for example `:8080`.                                                                                                                                                                                    |
| `--label <key=value>`          |                                      | Add a label. Repeatable. Mutually exclusive with `--labels-file`.                                                                                                                                                                                                    |
| `--labels-file <path>`         | `CURSOR_WORKER_LABELS_FILE`          | Path to JSON or TOML labels file. Mutually exclusive with `--label`.                                                                                                                                                                                                 |
| `--idle-release-timeout <sec>` | `CURSOR_WORKER_IDLE_RELEASE_TIMEOUT` | Seconds to stay connected after a session ends. Default: `3600`. Pass `0` to disable idle-based release.                                                                                                                                                             |
| `--pool [name]`                | `CURSOR_WORKER_POOL_NAME`            | Register for pool assignment. Optional pool name; defaults to `default`. Each session claims one worker at a time.                                                                                                                                                   |
| `--single-use`                 |                                      | Legacy alias for `--pool`.                                                                                                                                                                                                                                           |
| `--pool-name <name>`           | `CURSOR_WORKER_POOL_NAME`            | Deprecated alias for `--pool <name>`.                                                                                                                                                                                                                                |
| `--api-key <key>`              | `CURSOR_API_KEY`                     | Service account API key for pool workers.                                                                                                                                                                                                                            |
| `--auth-token <token>`         |                                      | Pre-minted access token. Used by the Kubernetes operator and other automation that exchanges an API key for a short-lived token externally.                                                                                                                          |
| `--auth-token-file <path>`     |                                      | File containing an access token. The CLI re-reads this file when reconnecting after an auth failure or disconnect, which lets a controller rotate the mounted token without restarting the pod.                                                                      |
| `--clone-git-repos`            |                                      | On claim, clone the agent's GitHub repos into the workspace. Any-repo named pools only (not `default`, and not a bound repo or named machine). Implies `--mint-github-token`. Requires `git` on `PATH`. Default: off.                                                |
| `--mint-github-token`          |                                      | Receive short-lived GitHub tokens during claimed runs. Pool workers only. Requires team-admin enablement. At most one credential-enabled worker per OS user or container.                                                                                            |
| `--sync-dashboard-secrets`     |                                      | Receive eligible dashboard Cloud Agent secrets as environment variables during claimed runs. Pool workers only. Same one-worker-per-user rule.                                                                                                                       |
| `--worker-id <id>`             | `CURSOR_AGENT_WORKER_ID`             | Stable worker id used with [claim](https://cursor.com/docs/cloud-agent/api/endpoints.md#claim-a-pending-request). Prefer the env var so older CLI builds ignore an unknown flag.                                                                                     |
| `-e, --endpoint <url>`         |                                      | API endpoint. Default: `https://api2.cursor.sh`.                                                                                                                                                                                                                     |

## FAQ

### How should I size workers?

There is no fixed worker spec. Size each worker the same way you size a CI
runner or devbox for the repo it serves.

Each worker needs enough CPU, memory, disk, and network access to clone the
repo and run the builds, tests, and tools your agents need.

### Can I bake skills into the worker image?

Yes. Project-level skills in `.cursor/skills/` or `.agents/skills/` are
automatically available on self-hosted workers.

To share skills across a team, check them into the repo or bake them into
your custom worker image.

### Do MCP servers work on self-hosted workers?

Yes. Configure MCP servers through the Cloud Agents dashboard. See the
[MCP servers](https://cursor.com/docs/cloud-agent/self-hosted-guides/pool.md#mcp-servers) section for how routing works by transport type.

## Related

- [Choose where Cloud Agents run](https://cursor.com/docs/cloud-agent/self-hosted-guides/choose-runtime.md)
- [My Machines](https://cursor.com/docs/cloud-agent/self-hosted-guides/my-machines.md)
- [Kubernetes deployment guide](https://cursor.com/docs/cloud-agent/self-hosted-guides/kubernetes.md)
- [Self-hosted Cloud Agents cookbook](https://github.com/cursor/cookbook/tree/main/self-hosted-cloud-agent) (EC2, ECS, EKS reference deployments)
- [Cloud Agent security and network](https://cursor.com/docs/cloud-agent/security-network.md)
- [Service accounts](https://cursor.com/docs/account/enterprise/service-accounts.md)
