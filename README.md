# Cursor Docs Skill

Local Agent Skill mirror of the Cursor documentation from
[https://cursor.com/docs](https://cursor.com/docs).

The installable skill lives in `skills/cursor-docs/`: `SKILL.md` is the entry
point, cleaned Markdown copies of every mirrored Cursor page live under
`skills/cursor-docs/references/`, and a 3-hour GitHub Action keeps them in sync
with upstream.

## Install

```bash
npx skills add mehmetbaykar/cursor-docs-skill
```

The `npx skills` CLI discovers the nested skill automatically. Installing the
repo exposes only the skill directory (`SKILL.md`, provider metadata in
`agents/`, and `references/`) to the target agent while repository maintenance
files stay at the repo root.

## Usage

Once installed, invoke the skill with a topic from your agent
(`/cursor-docs hooks` in Cursor or Claude Code, `$cursor-docs hooks` in Codex)
or with no argument to list topics. The full agent-facing usage contract lives
in [skills/cursor-docs/SKILL.md](skills/cursor-docs/SKILL.md).

## What's mirrored

The fetcher discovers pages from the Cursor sitemap at
`https://cursor.com/docs/sitemap.xml` and the machine-readable index at
`https://cursor.com/llms.txt`, then merges both sets. It keeps every page under
`/docs` and excludes:

- `/docs/enterprise` and `/docs/enterprise/*`
- `/docs/account/enterprise/*`
- non-documentation site sections such as `/learn/*`
- cross-domain URLs

Cursor serves Markdown for a documentation path when the request prefers
Markdown or plain text, so pages are fetched from the canonical path rather
than a `.md` twin. Pages that return HTML instead of Markdown — currently the
`/docs` landing page — are recorded under `skipped` in
`skills/cursor-docs/references/docs_manifest.json`. The generated topic list
lives in `skills/cursor-docs/references/INDEX.md`.

## Update

```bash
npx skills update cursor-docs   # update an installed local copy
```

Upstream refreshes happen automatically every 3 hours; there is nothing to
configure on the consumer side.

## Refresh locally (maintainers only)

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements-dev.txt
.venv/bin/python -m pytest tests -q
.venv/bin/python scripts/fetch_cursor_docs.py
```

The fetcher discovers pages, downloads each page's Markdown, cleans upstream
artifacts, and rewrites `skills/cursor-docs/references/INDEX.md` and
`skills/cursor-docs/references/docs_manifest.json`. Files whose content hash is
unchanged are not rewritten.

## Freshness guarantees

The mirror fails loudly rather than serving frozen content. A run aborts
without committing when:

- discovery returns no pages
- no page could be fetched live
- discovery drops below 80% of the previously mirrored page count
- more than 20% of pages served stale content or returned no usable Markdown
- any page failed outright

Every entry in `docs_manifest.json` records a `status` of `live` or `stale`,
and `fetch_metadata` reports live, stale, skipped, and failed counts for the
run.

## Repository layout

```text
.
├── skills/
│   └── cursor-docs/
│       ├── agents/
│       │   └── openai.yaml          # Agent UI metadata + invocation policy
│       ├── SKILL.md                 # installed skill instructions and routing
│       └── references/              # mirrored docs + INDEX + manifest
├── scripts/
│   ├── fetch_cursor_docs.py         # discover -> fetch -> clean -> write
│   ├── requirements.txt
│   └── requirements-dev.txt
├── tests/
│   └── test_fetch_cursor_docs.py    # offline tests for the fetcher
└── .github/workflows/
    └── update-docs.yml              # tests on PRs, cron refresh every 3 hours
```

## Troubleshooting

- If docs look stale, check the latest run of
  [Update Cursor Documentation](../../actions/workflows/update-docs.yml) on this
  repository and reproduce locally with the steps in "Refresh locally" above.
- If the scheduled fetch fails, the workflow opens or updates a failure issue
  automatically and closes it after the next successful run.
- If a page reports `stale` in `docs_manifest.json`, the previous content is
  still served but upstream could not be reached on the last run.

## Notes

This repository is an unofficial local mirror packaged as an Agent Skill. It is
not affiliated with, endorsed by, or sponsored by Cursor.

Documentation content belongs to Cursor and is subject to Cursor's applicable
terms and policies. The MIT license in this repository applies only to the
mirroring tool, scripts, skill metadata, and repository-specific code.
