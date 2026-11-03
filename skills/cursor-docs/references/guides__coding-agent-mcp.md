---
title: "MCP for coding agents: how agents plug into your stack"
source: https://cursor.com/guides/coding-agent-mcp
path: /guides/coding-agent-mcp
---

Aug 12, 2026·integrations

# MCP for coding agents: how agents plug into your stack

8 min read

An agent can already work in your repo: search code, edit files, run commands, and browse the web. But it can't see your error tracker, database, tickets, or docs. Until those are connected, it stalls on anything that lives outside the editor.

The Model Context Protocol (MCP) is an open standard that connects an agent to outside tools and data. Connect an MCP server and the agent queries the database instead of asking you for the schema. It opens the ticket instead of describing what the ticket should say.

That access is what separates an agent your team leans on from one writing code in isolation, and it makes the coding agent MCP strategy one of the first things teams need to solve for. This guide covers what MCP does for coding agents in practice, which servers are worth connecting first, and how to add one in a couple of minutes.

## [#](#why-agents-need-real-tool-access)Why agents need real tool access

The work is moving from writing code to running the loop around it, and coding agents are already reaching for more tools to do that. In our usage, average tool calls per session [rose roughly 30% in a recent two-month window](https://cursor.com/insights/developer-habits), as agents read files, search code, run commands, and browse the web more often inside a single task.

Every one of those tool calls is a spot where an integration either exists or the agent hits a wall. MCP turns each of those calls into a working connection instead of a dead end. The smartest model in the world can't tell you why the staging deploy failed if it can't see your error tracker. Wire that same model into the tracker, the database, and the issue queue and it can often drive the entire problem from symptom to fix. MCP makes those connections portable, so a server you set up once works across the agents and surfaces that your team needs.

## [#](#questions-before-you-connect)Questions before you connect

If you are setting up MCP for a coding agent for the first time, these are the things to settle before you start installing servers.

### [#](#what-is-an-mcp-server)What is an MCP server?

An MCP server is a small adapter that exposes one tool or data source (a database, an API, a SaaS product) through the Model Context Protocol, so any MCP-capable agent can use it. In a coding agent MCP setup, the agent is the client and the server is the connector. [MCP servers expose capabilities](https://cursor.com/docs/mcp) like tools, prompts, and resources through the protocol. In practice you do not write most of them: the vendor ships one, or the community does, and you point your agent at it.

### [#](#how-is-mcp-different-from-a-plugin-or-a-normal-api-integration)How is MCP different from a plugin or a normal API integration?

A plugin is built for one app. A raw API integration is built for one pair of systems, and you build it again for the next agent. MCP is the standard layer in between, so a server written once works with any client that speaks the protocol. Connect Sentry or Postgres through MCP and it works the same in Cursor, and in any other MCP client, without a bespoke integration each time.

### [#](#does-the-agent-run-these-tools-on-its-own)Does the agent run these tools on its own?

It calls them as part of its work, within the access you grant. You choose which servers to install and, for anything sensitive, you authenticate through OAuth so the server only reaches what your account can. Remote servers can authenticate with OAuth when the server requires it, or with headers and API keys; local servers run as a shell command on your machine. The agent gets a defined set of tools, not a blank check on your systems.

### [#](#what-makes-a-good-mcp-server-versus-a-noisy-one)What makes a good MCP server versus a noisy one?

The good ones give the agent a tight set of well-named actions, so it knows when to reach for them. The bad ones dump dozens of low-value tools into every prompt, bloating the context window with unused tool descriptions, which compounds as you add servers. Start with servers for the systems you actually touch mid-task, your database, your error tracker, whatever you keep alt-tabbing to, and add more only when a real workflow asks for it.

## [#](#best-mcp-servers-for-cursor-by-use-case)Best MCP servers for Cursor, by use case

The [Cursor Marketplace](https://cursor.com/marketplace) lists official plugins that install with one click and bundle an MCP server (often with rules and skills). These are the MCP servers worth connecting first, grouped by use case.

**Databases.** Give the agent read (and careful write) access to your schema and data so it stops guessing about your tables.

- [Supabase](https://cursor.com/marketplace/supabase): manage tables, fetch config, and query data across your Supabase projects.
- [MongoDB](https://cursor.com/marketplace/mongodb): connect to databases, explore data, manage collections, and optimize queries.
- [Neon Postgres](https://cursor.com/marketplace/neon-postgres): manage Neon projects and databases through the Neon MCP server.
- [Prisma](https://cursor.com/marketplace/prisma): MCP server, rules, and skills for database development.

**Dev workflows.** Wire the agent into the tools where work is tracked, shipped, and monitored.

- [Linear](https://cursor.com/marketplace/linear): manage issues, projects, and documents across your Linear workspace.
- [Sentry](https://cursor.com/marketplace/sentry): pull in errors and traces so the agent can debug against real production issues.
- [GitLab](https://cursor.com/marketplace/gitlab): plan and manage issues, merge requests, and pipelines from the editor.
- [Datadog](https://cursor.com/marketplace/datadog): query logs, metrics, traces, and dashboards through a preconfigured MCP server (in preview).

Note: GitHub is not featured in the MCP list because it's a native Cursor integration. The [Cursor GitHub app](https://cursor.com/docs/integrations/github) connects your repositories from the dashboard so features like Cloud Agents and Bugbot can act on your pull requests. You connect it once under Integrations rather than adding it through `mcp.json`.

**Browser automation.** Let the agent drive a real browser to test, reproduce bugs, and pull live data.

- [Browserbase Browse](https://cursor.com/marketplace/browse): navigate, click, fill forms, extract data, and take screenshots, controlled via MCP.
- [BrowserStack](https://cursor.com/marketplace/browserstack): test sites and mobile apps on real devices and debug failures.
- [Bright Data](https://cursor.com/marketplace/bright-data): web search, content extraction, and browser automation over a web-data platform.

**Documentation retrieval.** Keep the agent on current, version-specific docs instead of stale training data.

- [Context7](https://cursor.com/marketplace/context7-plugin): pull up-to-date, version-specific documentation and code examples straight into context.
- [Notion](https://cursor.com/marketplace/notion-workspace): bring your team's docs, specs, and requirements into the coding workflow.

The marketplace features many more (Figma, Stripe, Postman, and others), so browse it for your stack. New servers are added regularly.

## [#](#how-to-add-an-mcp-server-in-cursor)How to add an MCP server in Cursor

Two paths: one click from the marketplace, or a small config file for anything custom.

Two ways to add an MCP server in Cursor: one click from the marketplace, or a config file.

**One click.** On a [marketplace](https://cursor.com/marketplace) listing, click Add to Cursor to install the server and authenticate with OAuth. This is the fastest way to connect the named servers above.

**Config file.** For a custom or self-hosted server, add it to `mcp.json`. Use `.cursor/mcp.json` in a project for project-specific tools, or `~/.cursor/mcp.json` in your home directory for tools available everywhere. A local (command-based) server looks like this:

```
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "mcp-server"],
      "env": {
        "API_KEY": "value"
      }
    }
  }
}
```

A remote (HTTP or SSE) server uses a URL instead:

```
{
  "mcpServers": {
    "server-name": {
      "url": "http://localhost:3000/mcp",
      "headers": {
        "API_KEY": "value"
      }
    }
  }
}
```

**For teams.** Admins can configure Team MCP servers once for Cloud Agents from the dashboard, and can link those same servers to a team marketplace for the Agents Window, IDE, and CLI. Teammates may still need to install and authenticate, but they do not each have to hand-edit `mcp.json`.

The docs cover transports, authentication, and the full config reference. Follow along at [cursor.com/docs/mcp](https://cursor.com/docs/mcp).

## [#](#build-your-own-mcp-server)Build your own MCP server

If no server exists for your internal service you can build one. Write it in any language that can print to `stdout` or serve an HTTP endpoint, and have it expose a small set of well-named tools that wrap your API.

The fastest way to start is to let the agent write it. Point Cursor at your service's API reference, OpenAPI spec, or client library and ask it to scaffold an MCP server for the endpoints you care about. It can read the schema, generate each tool's JSON schema and handler, and wire up auth, so you review and refine instead of starting from a blank file. Keep the tool set tight, name each action clearly, and add the server to `mcp.json` the same way you would a third-party one.

## [#](#wire-it-into-the-stack-you-already-use)Wire it into the stack you already use

A model on its own can write code. A coding agent with MCP wired into the systems you work with takes a task from the ticket to the fix and checks its own work on the way. MCP makes those connections portable across the tools you use. Pick the two or three servers that match your stack, connect them, and give the agent direct access to the systems you keep switching to.

Filed under: integrations

## Related guides

[Model routing: right model, right job, right price

Model routing sends each request to the model that fits the job, so routine work stops billing at frontier prices. How it works, what to measure, and how to run it.](https://cursor.com/guides/model-routing)

[AI code review: more context, fewer bugs

AI code review only helps with real codebase context. What changed as agents grew, what to measure, and how to run Bugbot and Agent Review.](https://cursor.com/guides/ai-code-review)

[View all guides →](https://cursor.com/guides)
