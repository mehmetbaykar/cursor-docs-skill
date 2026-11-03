"""Offline tests for the Cursor product settings in fetch_docs.py."""

from __future__ import annotations

import pytest

import docs_mirror as dm
import fetch_docs


PRODUCT = fetch_docs.PRODUCT
BASE = fetch_docs.BASE_URL


def page_for(path: str) -> dm.Page:
    return dm.pages_from_paths(PRODUCT, {path})[0]


@pytest.mark.parametrize(
    "url",
    [
        f"{BASE}/docs/hooks",
        f"{BASE}/docs/agent/overview",
        f"{BASE}/docs/models/claude-opus-5",
        f"{BASE}/docs/hooks.md",
        f"{BASE}/docs/hooks/",
        f"{BASE}/docs/account/teams/sso",
        f"{BASE}/workflows/autonomous-agents/ci-autofix",
        f"{BASE}/guides/model-routing",
        f"{BASE}/guides",
    ],
)
def test_keeps_cursor_pages(url: str) -> None:
    assert dm.page_path(PRODUCT, url) is not None


@pytest.mark.parametrize(
    "url",
    [
        f"{BASE}/learn/agents",
        f"{BASE}/help/account-and-billing/billing",
        f"{BASE}/blog/whatever",
        f"{BASE}/docs/api/origin/openapi.yaml",
        "https://example.com/docs/hooks",
        "ftp://cursor.com/docs/hooks",
        f"{BASE}/docs/enterprise",
        f"{BASE}/docs/enterprise/security-hardening",
        f"{BASE}/docs/account/enterprise/billing-groups",
    ],
)
def test_drops_out_of_scope_urls(url: str) -> None:
    assert dm.page_path(PRODUCT, url) is None


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("/docs/hooks", "hooks.md"),
        ("/docs/agent/overview", "agent__overview.md"),
        ("/docs/models/claude-opus-5", "models__claude-opus-5.md"),
        ("/docs", "cursor.md"),
        ("/workflows/autonomous-agents/ci-autofix", "workflows__autonomous-agents__ci-autofix.md"),
        ("/guides", "guides.md"),
        ("/guides/model-routing", "guides__model-routing.md"),
    ],
)
def test_filenames(path: str, expected: str) -> None:
    assert page_for(path).filename == expected


def test_title_fallback_is_readable() -> None:
    assert page_for("/docs/agent/plan-mode").title == "Agent Plan Mode"


def test_clean_strips_media_and_sitemap_footer() -> None:
    raw = (
        "# Hooks\n\nIntro paragraph.\n\n[Media](/docs-static/images/agent/hooks.mp4)\n\nBody text.\n\n"
        "---\n\n## Sitemap\n\n[Overview of all docs pages](/llms.txt)\n"
    )
    cleaned = fetch_docs.clean(page_for("/docs/hooks"), raw)
    assert "[Media]" not in cleaned
    assert "## Sitemap" not in cleaned
    assert cleaned.startswith("# Hooks")
    assert cleaned.rstrip().endswith("Body text.")


def test_clean_keeps_media_markers_inside_code() -> None:
    raw = "# Hooks\n\n```bash\ncurl /docs/hooks\n[Media](/x.mp4)\n```\n"
    assert "[Media](/x.mp4)" in fetch_docs.clean(page_for("/docs/hooks"), raw)
