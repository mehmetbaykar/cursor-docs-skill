---
title: "Cloud Agents settings"
source: https://cursor.com/docs/cloud-agent/settings
path: /docs/cloud-agent/settings
---

# Cloud Agents settings

Workspace admins can configure Cloud Agents from the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents).

## Environment management

The **Environments** view lists the saved environments available to your team. Environments can be scoped to one repo or to a group of repos.

Open an environment to review:

- The repositories it applies to
- Whether it uses a snapshot or `.cursor/environment.json`
- The install script that runs during [Builds](https://cursor.com/docs/cloud-agent/builds.md)
- Runtime secrets and build secrets
- Network access settings
- Version history, Builds, and setup runs

Use **Update with Agent** when you want Cursor to inspect the current environment and propose a new setup. Use **New Setup Run** when you want Cursor to start setting up the environment fresh. Use **Restore** from version history to make a prior environment version active again.

To manage environments from a script, use the [environment endpoints](https://cursor.com/docs/cloud-agent/api/endpoints.md#environments) in the Cloud Agents API.

The **Builds** tab shows the prepared environment versions available to Cloud Agents. You can inspect logs, trigger a Build, choose or pin the active Build, and start an agent from a specific Build. See [Cloud Agent Builds](https://cursor.com/docs/cloud-agent/builds.md) for details.

## Default settings

- **Default model** – the model used when a run does not specify one. Pick any model available for cloud agents.
- **Default repository** – when empty, agents ask the user to choose a repo. Supplying a repo here lets users skip that step.
- **Base branch** – the branch agents fork from when creating pull requests. Leave blank to use the repository’s default branch.

## Network access settings

Control which network resources Cloud Agents can reach. User and team settings support three modes:

- **Allow all network access** – no domain restrictions.
- **Default + allowlist** – the [default domains](https://cursor.com/docs/agent/security/run-modes.md#network-access) plus any domains you add.
- **Allowlist only** – only domains you explicitly add.

Users, team admins, and environment owners can configure network access. Environment-level settings can inherit user or team policy, add an environment allowlist, or define their own access mode. See [Network Access](https://cursor.com/docs/cloud-agent/security-network.md) for full details.

## Security settings

All security options require admin privileges.

- **Display agent summary** – controls whether Cursor shows the agent's file-diff images and code snippets. Disable this if you prefer not to expose file paths or code in the sidebar.
- **Display agent summary in external channels** – extends the previous toggle to Slack or any external channel you've connected.
- **Team follow-ups** – controls whether team members can send follow-up messages to cloud agents created by other users on the team. See [team follow-ups](https://cursor.com/docs/cloud-agent/settings.md#team-follow-ups) below.
- **Automatically allow agents to use self-hosted machines** – lets agents in a [Project](https://cursor.com/docs/agent/projects.md) start work on any [self-hosted](https://cursor.com/docs/cloud-agent/self-hosted.md) machine or pool the Project owner can reach, without asking first. When it's off, the agent asks for approval in the Project's chat before it uses a new machine or pool. It's off by default for every team. Cloud Agents and Projects get other repos and environments without asking you to approve each one; see [Access Other Repositories](https://cursor.com/docs/cloud-agent/repo-access.md#how-it-works).

## Team feature settings

Team admins can enable or disable these features for their team:

- **Computer use** – controls whether agents can use computer interaction capabilities (available to enterprise teams only).

Changes save instantly and affect new agents immediately.

For long-running work, use [`/goal`](https://cursor.com/docs/agent/overview.md#goals-with-goal) in the composer. In the Cursor app, `/goal` needs a recent version.

### Team follow-ups

Team members can send follow-up messages to cloud agents started on the same team. This helps when a teammate kicks off work and you want to course-correct, add context, or pick up where they left off.

Follow-ups build on agent visibility. A teammate must be able to view the agent before they can follow up: they must belong to the same Cursor team, and they need their own access to the agent's repository. See [Share agents with your team](https://cursor.com/docs/cloud-agent.md#share-agents-with-your-team).

Agents started from multiplayer surfaces run under a team-owned service account by default so no personal secrets enter the machine, while each message still uses the sender's own MCP connections, approvals, PR and commit credit, and billing.

Team admins control this behavior with **Team Followups** in the [Cloud Agents security settings](https://cursor.com/dashboard/cloud-agents). It has three options:

| Setting                       | Behavior                                                                                                                                                                                                                                                                                                                          |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Disabled**                  | Only the person who started an agent can send it follow-ups.                                                                                                                                                                                                                                                                      |
| **On Service Account Agents** | Team members can send follow-ups to agents running under a [service account](https://cursor.com/docs/account/enterprise/service-accounts.md), including multiplayer surface agents (such as Slack, Microsoft Teams, or Jira) and automation or API service accounts. Personal agents stay private to the person who started them. |
| **On All Team Member Agents** | Any team member can send follow-ups to any agent on the team, whether owned by a service account or a teammate.                                                                                                                                                                                                                   |

If no admin has picked an option, Enterprise teams default to **On Service Account Agents** and all other teams default to **On All Team Member Agents**. Whatever the setting, the person who started an agent can always follow up on it.

#### How service account agents differ

Two kinds of cloud agents run under a service account, and they handle credentials differently:

- **Multiplayer surface agents:** The agent runs on a team-owned service account machine, so no person's personal secrets, personal agent store, or personal tokens enter the machine. When any teammate sends a message or follows up on the agent, that turn uses the sender's own MCP connections, opens pull requests and credits commits under their name, routes approval prompts to them, and bills usage to them.
- **Automation and API service accounts:** When the agent runs on its own, it uses the team credentials, MCP connections, and usage pool configured for that service account. When a teammate sends a follow-up message, pull requests, commit credit, and usage follow the person who sent the message.

### Secret exposure on personal agents

The personal-secret exposure risk applies when you select **On All Team Member Agents**. A personal agent runs on a machine that holds its creator's personal secrets, personal agent store, and creator tokens. Letting teammates follow up on personal agents means another user can instruct the agent to read those environment variables, print secrets to logs, send credentials to an external endpoint, or act with the creator's tokens.

With **On Service Account Agents**, no person's personal secrets or personal tokens are on the machine. Teammates only share the repository workspace and any team or environment secrets that admins have approved for the team. Treat **On All Team Member Agents** with the same care you would give shared SSH keys or privileged credentials.
