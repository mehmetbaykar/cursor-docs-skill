---
name: cursor-docs
description: >-
  Local mirror of Cursor product documentation (cursor.com/docs): Agent,
  Agent Skills, Rules, Hooks, MCP, Subagents, Plugins, CLI, cloud agents,
  models and pricing, SDK, integrations, account and team settings, and
  Cursor configuration reference. Use whenever the user asks how Cursor
  behaves, how to install or configure Cursor, or what a Cursor feature,
  flag, model, or settings key does. Read this skill's references/ before
  generic web search for Cursor product questions. Do NOT use for Claude
  Code, OpenAI Codex, Anthropic API docs, or general coding-agent questions.
---

# Cursor Docs

Local mirror of Cursor documentation, kept fresh by a 3-hour GitHub Action. The cleaned Markdown lives in `references/`; the auto-generated topic list lives in `references/INDEX.md`; the per-file manifest with upstream URLs lives in `references/docs_manifest.json`.

## Scope

Use this skill for Cursor-specific product and configuration questions, including the agent and its tools, Agent Skills, Rules, Hooks, Model Context Protocol (MCP), Subagents, Plugins, the Cursor CLI, cloud agents, models and pricing, the SDK, integrations, and account, team, and reference documentation. If the question is about Claude Code, OpenAI Codex, the Anthropic API, or another non-Cursor product, this skill does not apply. Cursor enterprise administration docs are intentionally not mirrored.

## Workflow

1. If the user supplied a topic, normalize it to a slug:
   - lowercase, strip leading `https://cursor.com/docs/` or `/docs/`, strip surrounding slashes
   - join nested segments with `__` (e.g. `agent overview` -> `agent__overview`, `reference permissions` -> `reference__permissions`)
2. If `references/<slug>.md` exists, read that file directly. Do NOT grep the whole `references/` tree first - the index plus targeted reads is faster and uses less context.
3. If no exact match, read `references/INDEX.md` and pick the closest topic. If still ambiguous, list the candidates and ask.
4. If the user supplied no topic, read `references/INDEX.md` and present the available topics.

## Answer format

- Lead with a direct answer to the user's question grounded in the file you read.
- Quote short snippets (commands, config keys) when they appear verbatim in the doc.
- End with `Source: <upstream URL>` using the `source` value from the file frontmatter or `original_url` from `references/docs_manifest.json`.

## Freshness and fallback

The mirror is refreshed every 3 hours by upstream CI, which fails rather than committing frozen content. If the local content looks stale, contradicted by the user, or empty:

1. Suggest the user run `npx skills update cursor-docs`.
2. Check the file's entry in `references/docs_manifest.json`: a `status` of `stale` means upstream could not be reached on the last run.
3. Cross-check the canonical URL via `original_url` in `references/docs_manifest.json` and offer it as a follow-up source.

## Examples

| Invocation | Reads |
| --- | --- |
| `/cursor-docs hooks` | `references/hooks.md` |
| `/cursor-docs mcp` | `references/mcp.md` |
| `/cursor-docs skills` | `references/skills.md` |
| `/cursor-docs agent overview` | `references/agent__overview.md` |
| `/cursor-docs reference permissions` | `references/reference__permissions.md` |
| `/cursor-docs` (no argument) | `references/INDEX.md` |
