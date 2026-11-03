#!/usr/bin/env python3
"""Mirror the Cursor documentation into the cursor-docs skill.

Product-specific settings only; the shared engine lives in docs_mirror.py.
"""

from __future__ import annotations

import re

from docs_mirror import Page, Product, Section, apply_outside_fences, run


BASE_URL = "https://cursor.com"

SITEMAP_FOOTER = re.compile(r"\n+---\s*\n+##\s*Sitemap\s*\n+\[[^\]]*\]\([^)]*llms\.txt\)\s*$")
MEDIA_PLACEHOLDER = re.compile(r"^[ \t]*\[Media\]\([^)]*\)[ \t]*\n?", re.MULTILINE)


def clean(page: Page, content: str) -> str:
    """Drop the docs-wide sitemap footer and the `[Media](...)` video markers."""

    content = SITEMAP_FOOTER.sub("\n", content)
    return apply_outside_fences(content, lambda text: MEDIA_PLACEHOLDER.sub("", text))


PRODUCT = Product(
    name="Cursor",
    skill="cursor-docs",
    repository="mehmetbaykar/cursor-docs-skill",
    docs_url=f"{BASE_URL}/docs",
    base_url=BASE_URL,
    sitemap_urls=(f"{BASE_URL}/docs/sitemap.xml", f"{BASE_URL}/sitemap.xml"),
    llms_txt_url=f"{BASE_URL}/llms.txt",
    sections=(
        # cursor.com serves Markdown for a docs path only when the request
        # prefers it; the same path returns HTML under `*/*`.
        Section(
            key="docs",
            label="Documentation",
            path_prefix="/docs",
            fetch="negotiate",
            root_filename="cursor",
        ),
        Section(
            key="workflows",
            label="Workflows",
            path_prefix="/workflows",
            fetch="html",
            keep_prefix=True,
            root_filename="workflows",
            html_selector="main#main",
        ),
        Section(
            key="guides",
            label="Guides",
            path_prefix="/guides",
            fetch="html",
            keep_prefix=True,
            root_filename="guides",
            html_selector="main#main",
        ),
    ),
    # Enterprise administration lives under two prefixes and is out of scope.
    excluded_prefixes=("/docs/enterprise/", "/docs/account/enterprise/"),
    excluded_paths=("/docs/enterprise",),
    clean=clean,
)


if __name__ == "__main__":
    raise SystemExit(run(PRODUCT))
