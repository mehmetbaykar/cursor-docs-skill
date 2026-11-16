---
title: "Access Other Repositories"
source: https://cursor.com/docs/cloud-agent/repo-access
path: /docs/cloud-agent/repo-access
---

# Access Other Repositories

Work often spans more than one repo. Some cloud agents can get access to the repos and environments they need while they work, so a change to your web app and the API it calls can happen in one piece of work, without you setting up a new environment first.

Every cloud agent starts with the repos in its environment: one repo, [several repos](https://cursor.com/docs/cloud-agent/setup.md#multi-repo-environments), or [repository dependencies](https://cursor.com/docs/cloud-agent/setup.md#repository-dependencies). Today, agents in a [Project](https://cursor.com/docs/agent/projects.md) can get access beyond that.

## In a Project

When a Project needs another repo or environment, it asks for access first.

- **Repos** are allowed automatically when you can push to them.
- **Environments** are allowed automatically when you can use them and they have a name in the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#environments).
- **[Self-hosted](https://cursor.com/docs/cloud-agent/self-hosted.md) machines and pools** need your approval in the Project's chat, unless your team turns on **Automatically allow agents to use self-hosted machines** in [settings](https://cursor.com/docs/cloud-agent/settings.md#security-settings).

Access covers the whole Project, including agents it starts later, and lasts until you remove it. With access, the Project can start agents on that repo, in that environment with its secrets and network settings, or on that machine.

To see or remove access, open the **Run on** menu next to the Project's chat input in the [Agents Window](https://cursor.com/docs/agent/agents-window.md).

**Example.** A Project in `acme/web` needs a new endpoint in `acme/api`. It gets access to `acme/api`, then starts one agent there and another in `acme/web`.

## Security

- **Access is consent.** Repos and environments are allowed automatically, so a Project can reach any repo you can push to. Give Projects tasks from sources you trust.
- **Repos run their own hooks.** An agent started on another repo runs that repo's [hooks](https://cursor.com/docs/hooks.md#cloud-agent-support), with the machine's git credentials and the environment's secrets.

## Related pages

- [Cloud Environment Setup](https://cursor.com/docs/cloud-agent/setup.md)
- [Projects](https://cursor.com/docs/agent/projects.md)
- [Self-Hosted Machines](https://cursor.com/docs/cloud-agent/self-hosted.md)
