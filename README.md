# Cursor Docs Skill

An unofficial mirror of the [Cursor documentation](https://cursor.com/docs), workflows, and guides, packaged as an [Agent Skill](https://agentskills.io) so coding agents read the docs locally instead of searching the web. A GitHub Action refreshes the mirror every 3 hours.

The skill lives in `skills/cursor-docs/`. The repository is also a plugin, `cursor-docs`, for Claude Code, Codex, and Cursor.

## Install

| Agent | Install |
| --- | --- |
| Any agent that reads Agent Skills | `npx skills add mehmetbaykar/cursor-docs-skill` |
| Claude Code | `/plugin marketplace add mehmetbaykar/cursor-docs-skill`, then `/plugin install cursor-docs@cursor-docs-skill` |
| Codex | `codex plugin marketplace add mehmetbaykar/cursor-docs-skill`, then `codex plugin add cursor-docs@cursor-docs-skill` |
| Cursor | In **Customize**, choose **From GitHub Repository** and enter `https://github.com/mehmetbaykar/cursor-docs-skill`, then install `cursor-docs` |

## Use

Ask a Cursor question and the agent picks up the skill on its own, or call it with a topic:

- Cursor and Claude Code: `/cursor-docs hooks` (as a Claude Code plugin, also `/cursor-docs:cursor-docs hooks`)
- Codex: `$cursor-docs hooks`

With no topic, the skill shows what the mirror covers. [`skills/cursor-docs/SKILL.md`](skills/cursor-docs/SKILL.md) holds the instructions the agent follows.

## Update

| Installed with | Update |
| --- | --- |
| `npx skills` | `npx skills update cursor-docs` |
| Claude Code plugin | `claude plugin marketplace update cursor-docs-skill`, then `claude plugin update cursor-docs@cursor-docs-skill` |
| Codex plugin | `codex plugin marketplace upgrade` |
| Cursor plugin | Import the repository again from **Customize**; team marketplaces can turn on **Enable Auto Refresh** |

Every refresh sets the plugin version to the time of the mirror's last change (`2026.1103.1534` is November 3, 15:34 UTC), so plugin managers see each update.

## What's mirrored

The fetcher reads https://cursor.com/docs/sitemap.xml, https://cursor.com/sitemap.xml, and https://cursor.com/llms.txt and merges the lists, because none is complete on its own. It mirrors three sections:

- **Documentation** under `/docs`. cursor.com serves Markdown for a docs page when the request prefers it, so pages are fetched from their canonical path.
- **Workflows** under `/workflows`, converted from HTML.
- **Guides** under `/guides`, converted from HTML.

Enterprise administration (`/docs/enterprise`, `/docs/enterprise/*`, `/docs/account/enterprise/*`), other parts of cursor.com such as `/help`, `/learn`, and `/blog`, links to files such as `llms.txt` or `openapi.yaml`, and other sites are left out.

[`references/INDEX.md`](skills/cursor-docs/references/INDEX.md) lists every page by section. [`references/docs_manifest.json`](skills/cursor-docs/references/docs_manifest.json) records each page's upstream URL, content hash, and `live` or `stale` status.

## Freshness guarantees

A refresh builds the whole mirror in memory and publishes it only when every check passes, so a failed run never leaves a half-written mirror. The run fails without publishing when:

- discovery finds no pages, or fewer than 80% of the pages already mirrored
- no page could be fetched live
- more than 20% of pages are stale, have no usable Markdown, or fail cleaning
- a page fails and has no earlier copy to fall back on

A page that fails while an earlier copy exists keeps that copy and is marked `stale`. Converted HTML pages must keep a heading and real text, so a cursor.com redesign fails the run instead of publishing empty pages.

## For maintainers

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements-dev.txt
.venv/bin/python -m pytest -q
.venv/bin/python scripts/fetch_docs.py
```

[`scripts/fetch_docs.py`](scripts/fetch_docs.py) holds the Cursor settings. Everything else in `scripts/`, `tests/`, and `.github/` is shared, byte for byte, with [claude-code-docs-skill](https://github.com/mehmetbaykar/claude-code-docs-skill) and [codex-docs-skill](https://github.com/mehmetbaykar/codex-docs-skill); `SHARED_FILES` in [`scripts/docs_mirror.py`](scripts/docs_mirror.py) lists the files. Change shared files in all three repositories on branches with the same name: CI's drift check (`python scripts/fetch_docs.py --check-drift`) compares against that branch in the other repositories, or their `main`, and fails while the files differ.

```text
.
├── plugin.json                          # Agent Plugins manifest (Codex, Cursor)
├── .claude-plugin/                      # Claude Code plugin and marketplace (Codex and npx skills read these too)
├── .cursor-plugin/                      # Cursor plugin and marketplace
├── skills/cursor-docs/
│   ├── SKILL.md                         # instructions the agent follows
│   ├── agents/openai.yaml               # Codex and ChatGPT app metadata
│   └── references/                      # mirrored pages, INDEX.md, docs_manifest.json
├── scripts/
│   ├── fetch_docs.py                    # Cursor settings
│   └── docs_mirror.py                   # shared engine
├── tests/                               # offline tests
└── .github/workflows/update-docs.yml    # tests, refresh every 3 hours, drift check, failure alerts
```

## Troubleshooting

- **Docs look stale:** check the latest run of [Update docs mirror](../../actions/workflows/update-docs.yml).
- **A scheduled refresh failed:** the workflow opens or updates an issue titled "Docs mirror update failures" and closes it after the next successful run.
- **A page shows `stale`:** upstream could not be reached on the last run, so the previous copy is still served.

## Legal notice

- **Unofficial.** This is an unofficial community project. It is not affiliated with, endorsed by, or sponsored by Anysphere, Inc., the maker of Cursor.
- **Documentation.** The mirrored pages belong to Anysphere and are subject to Anysphere's terms. Every page names its source, and https://cursor.com/docs is the authoritative version.
- **Trademarks.** Cursor is a trademark of Anysphere, Inc. It is used here only to name the product the documentation describes.
- **License.** The MIT license covers only this repository's own code: the scripts, tests, workflow, and skill instructions. It does not cover the mirrored documentation.
- **Removal requests.** If you represent Anysphere and want this mirror changed or removed, [open an issue](../../issues) and it will be handled promptly.
