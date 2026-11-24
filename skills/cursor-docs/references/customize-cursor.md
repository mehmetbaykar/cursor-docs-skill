---
title: "Customize Cursor"
source: https://cursor.com/docs/customize-cursor
path: /docs/customize-cursor
---

# Customize Cursor

Plugins, skills, and MCPs let you customize Cursor for your workflows. The **Customize** page brings them into one place.

Open **Customize** from the sidebar in Cursor to add and manage extensions at the user, team, or workspace level. You can install official and community plugins, connect MCP servers (including your own), and control which rules, skills, subagents, commands, and hooks are active for each scope.

## What you can do from Customize

From the Customize page, you can:

- **Browse and install** plugins, skills, and MCPs from the [Cursor Marketplace](https://cursor.com/marketplace) with one click
- **Install Team MCP servers** shared through your team's [Default marketplace](https://cursor.com/docs/plugins.md#default-team-marketplace)
- **See your team leaderboard** of the most popular plugins, skills, and MCPs across your team and the community
- **Add and manage** plugins, skills, MCPs, subagents, rules, commands, and hooks without switching between separate settings pages
- **Filter by scope** to see what is installed for you, your workspace, or your team
- **Open plugin canvases** for shared setup templates your team can reuse

Learn more in the [changelog](https://cursor.com/changelog/customize).

## Extension components

Cursor extensions are built from composable pieces. Plugins often bundle several of these together, but you can also add each component on its own.

| Component     | Description                                                                                                                                                                                                                                                                                                                |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Plugins**   | Distributable bundles that package rules, skills, subagents, commands, MCP servers, and hooks. Install from the [marketplace](https://cursor.com/marketplace) or a [team marketplace](https://cursor.com/docs/plugins.md#team-marketplaces).                                                                                                 |
| **Rules**     | Persistent instructions that shape how Agent works with your code. Use [project rules](https://cursor.com/docs/rules.md#project-rules), [user rules](https://cursor.com/docs/rules.md#user-rules), [team rules](https://cursor.com/docs/rules.md#team-rules), or [`AGENTS.md`](https://cursor.com/docs/rules.md#agentsmd). |
| **Skills**    | Specialized capabilities Agent loads when relevant. Skills package domain knowledge, workflows, and scripts in `SKILL.md` files. See [Agent Skills](https://cursor.com/docs/skills.md).                                                                                                                                    |
| **Subagents** | Specialized assistants Agent delegates to for parallel or isolated work. Each subagent runs in its own context window. See [Subagents](https://cursor.com/docs/subagents.md).                                                                                                                                              |
| **Hooks**     | Scripts that observe, control, or extend the agent loop at specific lifecycle events. See [Hooks](https://cursor.com/docs/hooks.md).                                                                                                                                                                                       |
| **Commands**  | Reusable prompts you invoke with `/` in Agent chat. Commands are markdown files that define a focused workflow or action.                                                                                                                                                                                                  |

For MCP servers that connect Cursor to external tools and data sources, see [Model Context Protocol (MCP)](https://cursor.com/docs/mcp.md).

## What each surface reads from your home folder

Config in your home folder applies only on the machine where it lives. The editor and CLI read your own machine's home folder. A [self-hosted worker](https://cursor.com/docs/cloud-agent/self-hosted.md) reads the home folder of the account it runs as on the worker machine. A hosted Cloud Agent runs on a Cursor VM whose home folder doesn't hold your files, so it uses synced skills, dashboard MCP servers, and plugins installed for your account and team instead.

| Home path                       | Editor                              | CLI                                 | Hosted Cloud Agent                                                                                  | Self-hosted worker                                            |
| :------------------------------ | :---------------------------------- | :---------------------------------- | :-------------------------------------------------------------------------------------------------- | :------------------------------------------------------------ |
| `~/.cursor/skills/`             | Yes                                 | Yes                                 | No. [Sync skills](https://cursor.com/docs/skills.md#use-personal-skills-with-cloud-agents) instead. | Yes, and listed in the `/` menu                               |
| `~/.agents/skills/`             | Yes                                 | Yes                                 | No                                                                                                  | Yes, to the agent. Not listed in the `/` menu.                |
| `~/.cursor/agents/` (subagents) | Yes                                 | No                                  | No                                                                                                  | Yes                                                           |
| `~/.cursor/commands/`           | Yes                                 | Yes                                 | No                                                                                                  | Yes                                                           |
| `~/.cursor/mcp.json`            | Yes                                 | Yes                                 | No                                                                                                  | Command and loopback URL servers, read when the worker starts |
| `~/.cursor/hooks.json`          | Yes                                 | Yes                                 | No                                                                                                  | Yes                                                           |
| `~/.cursor/plugins/local/`      | If local plugin imports are allowed | If local plugin imports are allowed | No                                                                                                  | If local plugin imports are allowed                           |

[Synced personal skills](https://cursor.com/docs/skills.md#use-personal-skills-with-cloud-agents) load in Cloud Agents you start on both hosted VMs and self-hosted workers.

A self-hosted worker also loads the `.mdc` rule files in its own `~/.cursor/rules/`. To set rules for every project in the editor, use [User Rules](https://cursor.com/docs/rules.md#user-rules).

MCP servers for self-hosted workers are configured at [cursor.com/agents](https://cursor.com/agents), the same as for hosted Cloud Agents. A worker also runs command (stdio) servers bundled in its local plugins, and command and loopback URL servers in its own `~/.cursor/mcp.json`. See [MCP servers on self-hosted workers](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#mcp-servers).

## Marketplace leaderboard

Cursor shows a leaderboard of the most popular plugins, skills, and MCPs across your team.

Add any entry to your setup with one click from the Customize page and extend Cursor for your workflow. The leaderboard helps you discover what teammates and the community use most, so you can adopt proven setups quickly.

Browse the full catalog in the [Cursor Marketplace](https://cursor.com/marketplace). For community plugins and MCP servers, see [cursor.directory](https://cursor.directory).

## Learn more

### Plugins

Browse the marketplace, install plugins, and set up team marketplaces

### Rules

Write project, user, and team rules that guide Agent behavior

### Skills

Package specialized workflows in portable SKILL.md files

### MCP

Connect Cursor to external tools, APIs, and data sources

### Subagents

Delegate complex tasks to specialized agents

### Hooks

Run scripts at key points in the agent loop
