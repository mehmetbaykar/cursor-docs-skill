"""Offline tests for the cursor-docs fetcher."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import fetch_cursor_docs as fetcher  # noqa: E402


@pytest.mark.parametrize(
    "url",
    [
        "https://cursor.com/docs/hooks",
        "https://cursor.com/docs/agent/overview",
        "https://cursor.com/docs/models/claude-opus-5",
        "https://cursor.com/docs/hooks.md",
        "https://cursor.com/docs/hooks/",
    ],
)
def test_keeps_documentation_urls(url: str) -> None:
    assert fetcher.is_cursor_doc_url(url) is True


@pytest.mark.parametrize(
    "url",
    [
        "https://cursor.com/learn/agents",
        "https://cursor.com/blog/whatever",
        "https://example.com/docs/hooks",
        "ftp://cursor.com/docs/hooks",
        "https://cursor.com/docs/enterprise",
        "https://cursor.com/docs/enterprise/security-hardening",
        "https://cursor.com/docs/account/enterprise/billing-groups",
    ],
)
def test_drops_out_of_scope_urls(url: str) -> None:
    assert fetcher.is_cursor_doc_url(url) is False


def test_account_pages_outside_enterprise_are_kept() -> None:
    assert fetcher.is_cursor_doc_url("https://cursor.com/docs/account/teams/sso") is True


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("/docs/hooks", "hooks.md"),
        ("/docs/agent/overview", "agent__overview.md"),
        ("/docs/models/claude-opus-5", "models__claude-opus-5.md"),
        ("/docs", "cursor.md"),
    ],
)
def test_path_to_filename(path: str, expected: str) -> None:
    assert fetcher.path_to_filename(path) == expected


def test_title_from_path_builds_readable_fallback() -> None:
    assert fetcher.title_from_path("/docs/agent/plan-mode") == "Agent Plan Mode"


def test_pages_from_paths_detects_slug_collisions() -> None:
    with pytest.raises(RuntimeError, match="Slug collision"):
        fetcher.pages_from_paths({"/docs/agent/overview", "/docs/agent__overview"})


def test_pages_from_paths_is_sorted_and_absolute() -> None:
    pages = fetcher.pages_from_paths({"/docs/rules", "/docs/hooks"})
    assert [page.path for page in pages] == ["/docs/hooks", "/docs/rules"]
    assert pages[0].url == "https://cursor.com/docs/hooks"


def test_clean_markdown_strips_media_and_sitemap_footer() -> None:
    raw = (
        "# Hooks\n\n"
        "Intro paragraph.\n\n"
        "[Media](/docs-static/images/agent/hooks.mp4)\n\n"
        "Body text.\n\n"
        "---\n\n"
        "## Sitemap\n\n"
        "[Overview of all docs pages](/llms.txt)\n"
    )
    cleaned = fetcher.clean_markdown(raw)

    assert "[Media]" not in cleaned
    assert "## Sitemap" not in cleaned
    assert "llms.txt" not in cleaned
    assert cleaned.startswith("# Hooks")
    assert cleaned.endswith("Body text.\n")


def test_clean_markdown_absolutizes_root_relative_links() -> None:
    raw = "# Rules\n\nSee [subagents](/docs/subagents) and ![shot](/img/a.png).\n"
    cleaned = fetcher.clean_markdown(raw)

    assert "(https://cursor.com/docs/subagents)" in cleaned
    assert "(https://cursor.com/img/a.png)" in cleaned


def test_clean_markdown_leaves_absolute_and_anchor_links_alone() -> None:
    raw = "# MCP\n\n[docs](https://cursor.com/docs/mcp) and [top](#overview).\n"
    cleaned = fetcher.clean_markdown(raw)

    assert "[docs](https://cursor.com/docs/mcp)" in cleaned
    assert "[top](#overview)" in cleaned


def test_clean_markdown_handles_labels_containing_brackets() -> None:
    raw = "# Rules\n\nSee [`[rules].policy`](/docs/reference/permissions) for details.\n"
    cleaned = fetcher.clean_markdown(raw)

    assert "(https://cursor.com/docs/reference/permissions)" in cleaned


def test_clean_markdown_leaves_protocol_relative_urls_alone() -> None:
    raw = "# Rules\n\n[cdn](//cdn.example.com/a.png) stays put in this documentation.\n"
    cleaned = fetcher.clean_markdown(raw)

    assert "(//cdn.example.com/a.png)" in cleaned


def test_clean_markdown_preserves_code_fences() -> None:
    raw = "# Hooks\n\n```bash\ncurl /docs/hooks\n[Media](/x.mp4)\n```\n"
    cleaned = fetcher.clean_markdown(raw)

    assert "curl /docs/hooks" in cleaned
    assert "[Media](/x.mp4)" in cleaned


def test_content_looks_like_markdown_rejects_html() -> None:
    assert fetcher.content_looks_like_markdown("<!DOCTYPE html><html>...</html>") is False
    assert (
        fetcher.content_looks_like_markdown(
            "# Title\n\nA real documentation paragraph that is long enough to keep.\n"
        )
        is True
    )


def test_content_looks_like_markdown_rejects_short_bodies() -> None:
    assert fetcher.content_looks_like_markdown("# Hi\n") is False


def test_extract_title_falls_back_when_page_has_no_h1() -> None:
    body = "Claude Opus 5 is Anthropic's latest Opus model.\n\n## Strengths\n"
    assert fetcher.extract_title(body, "Models Claude Opus 5") == "Models Claude Opus 5"


def test_extract_title_prefers_h1() -> None:
    assert fetcher.extract_title("# Hooks\n\nBody\n", "Hooks Fallback") == "Hooks"


def test_yaml_quoted_preserves_non_ascii_and_escapes_quotes() -> None:
    assert fetcher.yaml_quoted("Week 26 · June 22–26") == '"Week 26 · June 22–26"'
    assert fetcher.yaml_quoted('He said "hi"') == '"He said \\"hi\\""'


def test_frontmatter_quotes_titles_with_colons() -> None:
    page = fetcher.CursorPage(
        url="https://cursor.com/docs/hooks",
        path="/docs/hooks",
        filename="hooks.md",
        title="Hooks: the agent loop",
    )
    frontmatter = fetcher.frontmatter_for(page, source_url=page.url)

    assert 'title: "Hooks: the agent loop"' in frontmatter
    assert "path: /docs/hooks" in frontmatter


def test_guards_pass_on_a_healthy_run() -> None:
    problems = fetcher.check_coverage_guards(
        discovered=150, live=149, stale=0, skipped=1, previous_file_count=149
    )
    assert problems == []


def test_guards_fail_when_nothing_is_live() -> None:
    problems = fetcher.check_coverage_guards(
        discovered=150, live=0, stale=150, skipped=0, previous_file_count=150
    )
    assert any("No page was fetched live" in problem for problem in problems)


def test_guards_fail_when_every_page_lost_its_markdown_endpoint() -> None:
    """The 404-on-every-page regression must fail the run, not freeze the mirror."""

    problems = fetcher.check_coverage_guards(
        discovered=150, live=0, stale=0, skipped=150, previous_file_count=150
    )
    assert any("No usable Markdown" in problem or "no usable Markdown" in problem for problem in problems)


def test_guards_fail_when_discovery_collapses() -> None:
    problems = fetcher.check_coverage_guards(
        discovered=10, live=10, stale=0, skipped=0, previous_file_count=150
    )
    assert any("refusing to delete references" in problem for problem in problems)


def test_guards_fail_on_empty_discovery() -> None:
    problems = fetcher.check_coverage_guards(
        discovered=0, live=0, stale=0, skipped=0, previous_file_count=150
    )
    assert problems == ["Discovery returned no documentation pages"]


def test_guards_tolerate_a_single_stale_page() -> None:
    problems = fetcher.check_coverage_guards(
        discovered=150, live=149, stale=1, skipped=0, previous_file_count=150
    )
    assert problems == []


def test_sanitize_error_strips_local_paths() -> None:
    """Error text is committed to the manifest, so it must not carry a home path."""

    error = OSError(
        "[Errno 2] No such file or directory: '/Users/someone/Desktop/repo/x.md'"
    )
    message = fetcher.sanitize_error(error)

    assert "/Users/someone" not in message
    assert "/Users/<user>" in message
    assert message.startswith("OSError: ")


def test_sanitize_error_redacts_proxy_credentials() -> None:
    error = fetcher.requests.ConnectionError(
        "Failed to connect to https://alice:hunter2@proxy.corp.example/"
    )
    message = fetcher.sanitize_error(error)

    assert "hunter2" not in message
    assert "<redacted>@proxy.corp.example" in message


def test_sanitize_error_replaces_the_repository_root() -> None:
    error = OSError(f"cannot write {fetcher.ROOT_DIR}/skills/x/references/y.md")
    message = fetcher.sanitize_error(error)

    assert str(fetcher.ROOT_DIR) not in message
    assert "<repo>" in message


def test_sanitize_error_is_bounded() -> None:
    assert len(fetcher.sanitize_error(RuntimeError("x" * 5000))) == 300
