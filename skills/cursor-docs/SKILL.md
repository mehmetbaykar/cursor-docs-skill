---
name: cursor-docs
description: >-
  Answers questions about Cursor from a local mirror of its official
  documentation, workflows, and guides (cursor.com). Use when someone asks how
  Cursor behaves or how to set it up: Agent and its modes, Rules, Skills,
  Hooks, MCP, Subagents, Plugins, the CLI, cloud agents, Bugbot, models and
  pricing, the SDK and APIs, integrations, or account and team settings.
  Read the mirror before searching the web. Not for Claude Code, OpenAI
  Codex, or other editors.
license: MIT for the mirroring tooling; the mirrored documentation belongs to Cursor.
compatibility: Any agent that reads Agent Skills, such as Claude Code, Codex, or Cursor. Needs read access to this skill's files and no network access.
allowed-tools: Read Grep Glob
metadata:
  upstream: https://cursor.com/docs
---

# Cursor Docs

A local mirror of the Cursor documentation, workflows, and guides, refreshed from cursor.com every 3 hours. Start at `references/INDEX.md`. Each page is a file `references/<topic>.md` whose frontmatter holds its `title`, `source` URL, and `path`; `references/docs_manifest.json` records every page's upstream URL and status. Enterprise administration pages are not mirrored.

## Find the page

1. Turn the topic into a slug: lowercase, drop a leading `/docs/`, and join nested segments with `__` (for example `agent overview` becomes `agent__overview`). Workflows are `workflows__<name>` and guides are `guides__<name>`.
2. If `references/<slug>.md` exists, read it.
3. Otherwise read `references/INDEX.md`, pick the closest topics, and read those files. Search the `references/` tree only when the index has no match; the index is faster and keeps context small.
4. With no topic, show the topic groups in `references/INDEX.md`.

## Answer

- Lead with a direct answer grounded in the files you read.
- Quote commands, flags, and settings keys exactly as the page writes them.
- End with `Source: <url>`, using the `source` value from the page's frontmatter.

## When the mirror looks stale or wrong

1. Check the page's `status` in `references/docs_manifest.json`: `stale` means the last refresh could not reach upstream, so the previous copy is still served.
2. Suggest updating the skill with `npx skills update cursor-docs`, or the `cursor-docs` plugin from the agent's plugin manager.
3. Offer the page's `source` URL so the user can check the live page.
4. A page whose cleaning failed keeps its raw upstream source in `references/_raw/<slug>.md`.

## Examples

| Request | Read |
| --- | --- |
| `/cursor-docs hooks` in Cursor or Claude Code, `$cursor-docs hooks` in Codex | `references/hooks.md` |
| "How do Agent Skills work in Cursor?" | `references/skills.md` |
| "How do I connect an MCP server?" | `references/mcp.md` |
| "What can the agent do?" | `references/agent__overview.md` |
| "How do I set up CI autofix with cloud agents?" | `references/workflows__autonomous-agents__ci-autofix.md` |
| No topic, or no matching file | `references/INDEX.md` |
