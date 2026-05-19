# Cursor Docs Skill

Local Agent Skill mirror of selected Cursor agent-extension docs from
[https://cursor.com/docs/](https://cursor.com/docs/) — Skills, Rules, Hooks,
MCP, Subagents, Plugins. A scheduled GitHub Action keeps the mirror in sync
with upstream every three hours.

## Install

```bash
npx skills add mehmetbaykar/cursor-docs-skill
```

## Usage

Once installed, invoke the skill with a topic from your agent:

```
/cursor-docs hooks
```

Invoke with no topic to list available topics. The full agent-facing usage
contract lives in [skills/cursor-docs/SKILL.md](skills/cursor-docs/SKILL.md).

## Repository layout

```text
.
├── skills/
│   └── cursor-docs/                # installable skill
│       ├── SKILL.md                # entry point + routing
│       ├── agents/openai.yaml      # provider metadata
│       └── references/             # mirrored docs + INDEX + manifest
├── scripts/
│   └── update_cursor_docs.py       # live fetch → clean → write
└── .github/workflows/
    └── update-cursor-docs.yml      # cron every 3 hours
```

## Notes

Unofficial mirror packaged as an Agent Skill. Not affiliated with, endorsed by,
or sponsored by Cursor. Documentation content belongs to Cursor and is subject
to Cursor's applicable terms. The MIT LICENSE applies only to the mirroring
tool, scripts, and skill metadata in this repository.
