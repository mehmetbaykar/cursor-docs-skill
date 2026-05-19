---
name: cursor-docs
description: >-
  Local mirror of Cursor product documentation for agent-extension features:
  Agent Skills, Rules, Hooks, MCP, Subagents, Plugins, and closely related
  Cursor customization docs. Use whenever the user asks how Cursor agent
  extension features behave, how to configure them, or what a Cursor docs page
  says. Read this skill's references/ before generic web search for Cursor
  product documentation questions. Do NOT use for Claude Code, OpenAI Codex,
  Anthropic API docs, or general coding-agent questions.
---

# Cursor Docs

Local mirror of selected Cursor documentation, checked for freshness by scheduled CI. The cleaned Markdown lives in `references/`; the generated topic list lives in `references/INDEX.md`; the per-file manifest with upstream URLs lives in `references/docs_manifest.json`.

## Scope

Use this skill for Cursor-specific product and configuration questions about Agent Skills, Rules, Hooks, Model Context Protocol (MCP), Subagents, Plugins, and related Cursor agent-extension features. If the question is about Claude Code, OpenAI Codex, Anthropic API docs, or another non-Cursor coding agent, this skill does not apply.

## Workflow

1. If the user supplied a topic, normalize it to a slug:
   - lowercase the requested topic
   - strip leading `https://cursor.com/docs/`, `/docs/`, and surrounding slashes
   - join nested path segments with `__` (for example, `foo/bar` becomes `foo__bar`)
2. If `references/<slug>.md` exists, read that file directly. Do not search the whole `references/` tree first.
3. If no exact match exists, read `references/INDEX.md` and choose the closest topic. If multiple topics could match, list the candidates and ask the user to choose.
4. If the user supplied no topic, read `references/INDEX.md`, present the available mirrored topics, and ask what they want to inspect.

## Answer Format

- Lead with a direct answer grounded in the local reference file.
- Quote short commands, config keys, schema snippets, and exact constraints when useful.
- End with `Source: <upstream Cursor docs URL>` using the URL from the file frontmatter or `references/docs_manifest.json`.

## Freshness

Scheduled CI runs the updater and fails if checked-in references drift from live Cursor docs. If the local content looks stale, contradicted by the user, empty, or incomplete, tell the user to run or inspect the updater workflow rather than guessing from memory.

## Examples

| Invocation | Reads |
| --- | --- |
| `/cursor-docs hooks` | `references/hooks.md` |
| `/cursor-docs mcp` | `references/mcp.md` |
| `/cursor-docs skills` | `references/skills.md` |
| `/cursor-docs` | `references/INDEX.md` |
