#!/usr/bin/env python3
"""Fetch and clean Cursor documentation for the cursor-docs skill."""

from __future__ import annotations

import hashlib
import json
import logging
import random
import re
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests


ROOT_DIR = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT_DIR / "skills" / "cursor-docs"
REFERENCES_DIR = SKILL_DIR / "references"
MANIFEST_FILE = "docs_manifest.json"

CURSOR_BASE_URL = "https://cursor.com"
DOCS_PATH_PREFIX = "/docs"
SITEMAP_URLS = [
    f"{CURSOR_BASE_URL}/docs/sitemap.xml",
    f"{CURSOR_BASE_URL}/sitemap.xml",
]
LLMS_TXT_URL = f"{CURSOR_BASE_URL}/llms.txt"

# Enterprise administration lives under two prefixes on cursor.com and is out of
# scope for this skill, matching the codex-docs-skill enterprise exclusion.
EXCLUDED_PREFIXES = (
    f"{DOCS_PATH_PREFIX}/enterprise/",
    f"{DOCS_PATH_PREFIX}/account/enterprise/",
)
EXCLUDED_EXACT_PATHS = {f"{DOCS_PATH_PREFIX}/enterprise"}

HEADERS = {
    "User-Agent": "cursor-docs-skill-fetcher/2.0 (+https://cursor.com/docs)",
    "Accept": "application/xml, text/xml, text/plain, */*",
    "Cache-Control": "no-cache",
}
# cursor.com serves Markdown for a documentation path only when the request
# prefers Markdown or plain text; the same path returns HTML under `*/*`, and
# the `.md` twin advertised by llms.txt returns 404 under this Accept header.
MARKDOWN_HEADERS = {
    "User-Agent": HEADERS["User-Agent"],
    "Accept": "text/markdown,text/plain,*/*",
    "Cache-Control": "no-cache",
}

MAX_RETRIES = 3
REQUEST_TIMEOUT = 30
RATE_LIMIT_SECONDS = 0.2
RETRY_BASE_DELAY_SECONDS = 1
RETRY_MAX_DELAY_SECONDS = 10
MAX_THROTTLE_RETRIES = 5

# Coverage guards. A documentation mirror that silently keeps serving old
# content is worse than one that fails loudly, so the run fails when live
# coverage collapses.
MAX_STALE_RATIO = 0.2
MAX_SKIPPED_RATIO = 0.2
MIN_DISCOVERY_RATIO = 0.8
FETCH_TOOL_VERSION = "2.0"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("cursor-docs")


@dataclass(frozen=True)
class CursorPage:
    """A Cursor documentation page discovered from the sitemap or llms.txt."""

    url: str
    path: str
    filename: str
    title: str


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sanitize_error(error: Exception) -> str:
    """Render an exception without leaking local paths or credentials.

    Error text is recorded in the committed manifest, so a maintainer running
    the fetcher locally must not publish their home directory, their operating
    system username, or credentials embedded in a proxy URL.
    """

    message = f"{type(error).__name__}: {error}"
    message = re.sub(r"//[^/@\s]+:[^/@\s]+@", "//<redacted>@", message)
    message = message.replace(str(ROOT_DIR), "<repo>")
    message = message.replace(str(Path.home()), "<home>")
    message = re.sub(r"/(Users|home)/[^/\s'\"]+", r"/\1/<user>", message)
    return message[:300]


def sha256(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def load_manifest() -> dict:
    manifest_path = REFERENCES_DIR / MANIFEST_FILE
    if not manifest_path.exists():
        return {"files": {}}

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        logger.warning("Ignoring invalid manifest JSON: %s", error)
        return {"files": {}}

    if "files" not in manifest or not isinstance(manifest["files"], dict):
        manifest["files"] = {}
    return manifest


def write_text_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def _sleep_backoff(url: str, attempt: int, error: Exception) -> None:
    delay = min(
        RETRY_BASE_DELAY_SECONDS * (2 ** (attempt - 1)), RETRY_MAX_DELAY_SECONDS
    )
    delay *= random.uniform(0.5, 1.0)
    logger.warning(
        "Fetch failed for %s (%s/%s): %s; retrying in %.1fs",
        url,
        attempt,
        MAX_RETRIES,
        error,
        delay,
    )
    time.sleep(delay)


def request_with_retries(
    session: requests.Session,
    url: str,
    *,
    headers: dict[str, str],
    allow_404: bool = False,
) -> requests.Response | None:
    """Fetch a URL, retrying transient failures with jittered backoff.

    Returns None only when ``allow_404`` is set and the server replied 404.
    Other 4xx responses raise immediately because they are not transient. 5xx,
    connection, and timeout errors retry; 429 honors ``Retry-After`` (or 30s)
    and does not consume an attempt.
    """

    last_error: Exception | None = None
    attempt = 0
    throttle_count = 0
    while attempt < MAX_RETRIES:
        attempt += 1
        try:
            response = session.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        except (
            requests.ConnectionError,
            requests.Timeout,
            requests.exceptions.ChunkedEncodingError,
        ) as error:
            last_error = error
            _sleep_backoff(url, attempt, error)
            continue

        if response.status_code == 404 and allow_404:
            return None
        if response.status_code == 429:
            if throttle_count >= MAX_THROTTLE_RETRIES:
                raise RuntimeError(
                    f"Rate limited fetching {url} after "
                    f"{MAX_THROTTLE_RETRIES} cooperative retries"
                )
            throttle_count += 1
            wait_seconds = int(response.headers.get("Retry-After", "30"))
            logger.warning(
                "Rate limited fetching %s; waiting %ss (cooperative retry %s/%s)",
                url,
                wait_seconds,
                throttle_count,
                MAX_THROTTLE_RETRIES,
            )
            time.sleep(wait_seconds)
            attempt -= 1
            continue
        if 500 <= response.status_code < 600:
            error = requests.HTTPError(
                f"{response.status_code} {response.reason}", response=response
            )
            last_error = error
            _sleep_backoff(url, attempt, error)
            continue

        response.raise_for_status()
        return response

    raise RuntimeError(
        f"Failed to fetch {url} after {MAX_RETRIES} attempts: {last_error}"
    )


def fetch_text(
    session: requests.Session, url: str, *, allow_404: bool = False
) -> str | None:
    response = request_with_retries(
        session, url, headers=HEADERS, allow_404=allow_404
    )
    return None if response is None else response.text


def fetch_markdown_page(
    session: requests.Session, url: str
) -> tuple[str | None, str | None]:
    """Return ``(markdown, skip_reason)`` for a documentation page."""

    response = request_with_retries(
        session, url, headers=MARKDOWN_HEADERS, allow_404=True
    )
    if response is None:
        return None, "No markdown endpoint"

    content_type = response.headers.get("Content-Type", "").split(";")[0].strip()
    if content_type not in {"text/markdown", "text/plain", ""}:
        return None, f"Non-markdown response ({content_type})"
    return response.text, None


def _parse_xml(xml_text: str) -> ET.Element:
    """Parse XML defensively against XXE / external-entity attacks."""

    try:
        parser = ET.XMLParser(
            forbid_dtd=True, forbid_entities=True, forbid_external=True
        )
        return ET.fromstring(xml_text, parser=parser)
    except TypeError:
        logger.warning("XMLParser safety parameters unavailable; using default parser")
        return ET.fromstring(xml_text)


def xml_locs(xml_text: str) -> list[str]:
    try:
        root = _parse_xml(xml_text)
    except ET.ParseError as error:
        raise RuntimeError(f"Failed to parse XML: {error}") from error

    locs: list[str] = []
    for element in root.iter():
        if element.tag.endswith("loc") and element.text:
            locs.append(element.text.strip())
    return locs


def normalize_path(path: str) -> str:
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    if path.endswith(".md"):
        path = path.removesuffix(".md")
    return path


def is_cursor_doc_url(url: str) -> bool:
    """Return True for mirrored Cursor documentation pages."""

    parsed = urlparse(url)
    path = normalize_path(parsed.path)

    if parsed.scheme not in {"http", "https"}:
        return False
    if parsed.netloc != urlparse(CURSOR_BASE_URL).netloc:
        return False
    if not (path == DOCS_PATH_PREFIX or path.startswith(f"{DOCS_PATH_PREFIX}/")):
        return False
    if path in EXCLUDED_EXACT_PATHS:
        return False
    if any(path.startswith(prefix) for prefix in EXCLUDED_PREFIXES):
        return False
    return True


def path_to_filename(path: str) -> str:
    slug = path.removeprefix(DOCS_PATH_PREFIX).strip("/")
    if not slug:
        # Keep the overview filename stable for installed skill consumers.
        slug = "cursor"

    slug = slug.replace("/", "__")
    slug = re.sub(r"[^a-zA-Z0-9_.-]+", "-", slug)
    slug = slug.strip("-._").lower() or "cursor"
    return f"{slug}.md"


def title_from_path(path: str) -> str:
    slug = path.removeprefix(DOCS_PATH_PREFIX).strip("/") or "cursor"
    return " ".join(part.capitalize() for part in re.split(r"[/_-]+", slug) if part)


def paths_from_sitemaps(session: requests.Session) -> set[str]:
    """Collect documentation paths from the first sitemap that yields URLs."""

    for sitemap_url in SITEMAP_URLS:
        logger.info("Trying sitemap: %s", sitemap_url)
        try:
            sitemap_text = fetch_text(session, sitemap_url, allow_404=True)
        except (RuntimeError, requests.RequestException) as error:
            logger.warning("Failed to fetch sitemap %s: %s", sitemap_url, error)
            continue
        if not sitemap_text:
            continue

        locs = xml_locs(sitemap_text)
        nested = [url for url in locs if url.endswith(".xml")]
        for nested_url in nested:
            logger.info("Fetching nested sitemap: %s", nested_url)
            try:
                nested_text = fetch_text(session, nested_url, allow_404=True)
            except (RuntimeError, requests.RequestException) as error:
                logger.warning("Failed to fetch %s: %s", nested_url, error)
                continue
            if nested_text:
                locs.extend(xml_locs(nested_text))

        paths = {
            normalize_path(urlparse(url).path)
            for url in locs
            if is_cursor_doc_url(url)
        }
        if paths:
            logger.info("Discovered %s documentation paths from %s", len(paths), sitemap_url)
            return paths

    logger.warning("No documentation paths discovered from any sitemap")
    return set()


def paths_from_llms_txt(session: requests.Session) -> set[str]:
    """Collect documentation paths from the llms.txt index."""

    logger.info("Fetching llms.txt: %s", LLMS_TXT_URL)
    try:
        llms_text = fetch_text(session, LLMS_TXT_URL, allow_404=True)
    except (RuntimeError, requests.RequestException) as error:
        logger.warning("Failed to fetch %s: %s", LLMS_TXT_URL, error)
        return set()
    if not llms_text:
        return set()

    paths: set[str] = set()
    for match in re.finditer(r"https://cursor\.com(/docs[A-Za-z0-9_./-]*)", llms_text):
        candidate = f"{CURSOR_BASE_URL}{normalize_path(match.group(1))}"
        if is_cursor_doc_url(candidate):
            paths.add(normalize_path(urlparse(candidate).path))

    logger.info("Discovered %s documentation paths from llms.txt", len(paths))
    return paths


def pages_from_paths(paths: set[str]) -> list[CursorPage]:
    pages: list[CursorPage] = []
    filename_to_path: dict[str, str] = {}
    for path in sorted(paths):
        filename = path_to_filename(path)
        prior_path = filename_to_path.get(filename)
        if prior_path is not None and prior_path != path:
            raise RuntimeError(
                f"Slug collision: {prior_path!r} and {path!r} both map to "
                f"{filename!r}; adjust path_to_filename"
            )
        filename_to_path[filename] = path
        pages.append(
            CursorPage(
                url=f"{CURSOR_BASE_URL}{path}",
                path=path,
                filename=filename,
                title=title_from_path(path),
            )
        )
    return pages


def discover_cursor_pages(session: requests.Session) -> list[CursorPage]:
    """Discover pages from the sitemap and llms.txt, then merge both sets."""

    paths = paths_from_sitemaps(session) | paths_from_llms_txt(session)
    pages = pages_from_paths(paths)
    logger.info("Discovered %s Cursor documentation URLs after filtering", len(pages))
    return pages


def _split_by_fences(text: str) -> list[tuple[bool, str]]:
    segments: list[tuple[bool, str]] = []
    buffer: list[str] = []
    in_fence = False

    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith("```"):
            if buffer:
                segments.append((in_fence, "".join(buffer)))
                buffer = []
            segments.append((False, line))
            in_fence = not in_fence
            continue
        buffer.append(line)

    if buffer:
        segments.append((in_fence, "".join(buffer)))

    return segments


def _apply_outside_fences(text: str, transform) -> str:
    return "".join(
        chunk if in_fence else transform(chunk)
        for in_fence, chunk in _split_by_fences(text)
    )


def absolutize_links(content: str) -> str:
    """Rewrite root-relative Markdown links to absolute cursor.com URLs."""

    def replace(match: re.Match[str]) -> str:
        return f"]({CURSOR_BASE_URL}{match.group('target')})"

    # Anchored on the link target rather than the label, because labels can
    # themselves contain brackets (for example `` `[auto_review].policy` ``).
    return re.sub(r"\]\((?P<target>/(?!/)[^)\s]*)\)", replace, content)


def strip_media_placeholders(content: str) -> str:
    """Drop the `[Media](...)` markers Cursor emits for inline video assets."""

    return re.sub(r"^[ \t]*\[Media\]\([^)]*\)[ \t]*\n?", "", content, flags=re.MULTILINE)


def strip_sitemap_footer(content: str) -> str:
    """Drop the docs-wide sitemap footer appended to every Cursor page."""

    return re.sub(
        r"\n+---\s*\n+##\s*Sitemap\s*\n+\[[^\]]*\]\([^)]*llms\.txt\)\s*$",
        "\n",
        content,
    )


def clean_markdown(raw_content: str) -> str:
    content = raw_content.replace("\r\n", "\n")
    content = strip_sitemap_footer(content)
    content = _apply_outside_fences(content, strip_media_placeholders)
    content = _apply_outside_fences(content, absolutize_links)

    content = re.sub(r"\n{3,}", "\n\n", content)
    content = re.sub(r"[ \t]+\n", "\n", content)
    return content.strip() + "\n"


def content_looks_like_markdown(content: str) -> bool:
    stripped = content.strip()
    if len(stripped) < 50:
        return False
    if "<!DOCTYPE html" in stripped[:200] or "<html" in stripped[:200]:
        return False
    return True


def extract_title(content: str, fallback: str) -> str:
    for line in content.splitlines():
        if line.startswith("# "):
            return line.removeprefix("# ").strip()
    return fallback


def yaml_quoted(value: str) -> str:
    """Quote a YAML scalar without escaping non-ASCII characters."""

    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def frontmatter_for(page: CursorPage, *, source_url: str) -> str:
    return (
        "---\n"
        f"title: {yaml_quoted(page.title)}\n"
        f"source: {source_url}\n"
        f"path: {page.path}\n"
        "---\n\n"
    )


def build_index(entries: dict[str, dict], skipped: list[dict]) -> str:
    lines = [
        "# Cursor Docs Index",
        "",
        "Local mirror of Cursor documentation from https://cursor.com/docs.",
        "",
        "Invoke this skill with a topic, for example `/cursor-docs hooks`.",
        "",
        "## Topics",
        "",
    ]

    for filename, metadata in sorted(entries.items(), key=lambda item: item[0]):
        title = metadata.get("title") or filename.removesuffix(".md")
        source = metadata.get("original_url", "")
        lines.append(f"- `{filename.removesuffix('.md')}` - [{title}]({source})")

    if skipped:
        lines.extend(["", "## Skipped Pages", ""])
        for item in skipped:
            lines.append(f"- `{item['path']}` - {item['reason']}")

    return "\n".join(lines).strip() + "\n"


def cleanup_old_files(manifest: dict, current_files: set[str]) -> None:
    previous_files = set(manifest.get("files", {}).keys())
    for filename in sorted(previous_files - current_files):
        if filename == MANIFEST_FILE:
            continue
        path = REFERENCES_DIR / filename
        if path.exists():
            logger.info("Removing obsolete file: %s", filename)
            path.unlink()


def save_page(
    page: CursorPage,
    content: str,
    source_url: str,
    manifest: dict,
    new_files: dict[str, dict],
    current_files: set[str],
    *,
    status: str = "live",
) -> None:
    content_hash = sha256(content)
    old_entry = manifest.get("files", {}).get(page.filename, {})
    old_hash = old_entry.get("hash")
    last_updated = old_entry.get("last_updated", now_iso())

    if old_hash != content_hash:
        last_updated = now_iso()
        write_text_if_changed(REFERENCES_DIR / page.filename, content)
        logger.info("Updated: %s", page.filename)
    else:
        logger.info("Unchanged: %s", page.filename)

    new_files[page.filename] = {
        "title": extract_title(content, page.title),
        "path": page.path,
        "original_url": page.url,
        "source_url": source_url,
        "hash": content_hash,
        "last_updated": last_updated,
        "status": status,
    }
    current_files.add(page.filename)


def load_previous_reference(
    page: CursorPage, manifest: dict
) -> tuple[str, str] | None:
    """Return ``(content, source_url)`` for a previously mirrored page."""

    entry = manifest.get("files", {}).get(page.filename)
    reference_path = REFERENCES_DIR / page.filename
    if not isinstance(entry, dict) or not reference_path.exists():
        return None
    return reference_path.read_text(encoding="utf-8"), entry.get("source_url", page.url)


def check_coverage_guards(
    *,
    discovered: int,
    live: int,
    stale: int,
    skipped: int,
    previous_file_count: int,
) -> list[str]:
    """Return the reasons this run must fail instead of committing."""

    problems: list[str] = []
    if discovered == 0:
        problems.append("Discovery returned no documentation pages")
        return problems

    if live == 0:
        problems.append("No page was fetched live; the mirror would be frozen")

    if previous_file_count and discovered < previous_file_count * MIN_DISCOVERY_RATIO:
        problems.append(
            f"Discovered {discovered} pages, below {MIN_DISCOVERY_RATIO:.0%} of the "
            f"previous {previous_file_count}; refusing to delete references"
        )

    if stale > discovered * MAX_STALE_RATIO:
        problems.append(
            f"{stale}/{discovered} pages served stale content, above the "
            f"{MAX_STALE_RATIO:.0%} threshold"
        )

    if skipped > discovered * MAX_SKIPPED_RATIO:
        problems.append(
            f"{skipped}/{discovered} pages had no usable Markdown, above the "
            f"{MAX_SKIPPED_RATIO:.0%} threshold"
        )

    return problems


def fetch_and_save_pages(
    session: requests.Session, pages: list[CursorPage], manifest: dict
) -> dict:
    new_files: dict[str, dict] = {}
    current_files: set[str] = set()
    skipped: list[dict] = []
    failed: list[dict] = []
    stale: list[dict] = []
    live = 0

    for index, page in enumerate(pages, start=1):
        logger.info("Processing %s/%s: %s", index, len(pages), page.path)
        try:
            raw_content, skip_reason = fetch_markdown_page(session, page.url)
            if raw_content is None:
                skipped.append(
                    {"path": page.path, "url": page.url, "reason": skip_reason}
                )
                logger.info("Skipped (%s): %s", skip_reason, page.path)
                continue

            cleaned_content = clean_markdown(raw_content)
            if not content_looks_like_markdown(cleaned_content):
                raise RuntimeError("Response did not look like documentation Markdown")

            page_with_title = CursorPage(
                page.url,
                page.path,
                page.filename,
                extract_title(cleaned_content, page.title),
            )
            content = (
                frontmatter_for(page_with_title, source_url=page.url) + cleaned_content
            )
            save_page(
                page_with_title,
                content,
                page.url,
                manifest,
                new_files,
                current_files,
            )
            live += 1
            time.sleep(RATE_LIMIT_SECONDS)
        except (RuntimeError, requests.RequestException, OSError) as error:
            previous = load_previous_reference(page, manifest)
            if previous is None:
                logger.error("Failed to process %s: %s", page.path, error)
                failed.append(
                    {"path": page.path, "url": page.url, "error": sanitize_error(error)}
                )
                continue

            previous_content, previous_source = previous
            logger.warning(
                "Serving stale content for %s after fetch failure: %s",
                page.path,
                error,
            )
            stale.append({"path": page.path, "url": page.url, "error": sanitize_error(error)})
            save_page(
                page,
                previous_content,
                previous_source,
                manifest,
                new_files,
                current_files,
                status="stale",
            )

    cleanup_old_files(manifest, current_files)

    index_content = build_index(new_files, skipped)
    write_text_if_changed(REFERENCES_DIR / "INDEX.md", index_content)

    new_manifest = {
        "description": (
            "Cursor documentation mirror manifest. Files live beside this "
            "manifest in references/."
        ),
        "source": {
            "base_url": CURSOR_BASE_URL,
            "sitemap_urls": SITEMAP_URLS,
            "llms_txt_url": LLMS_TXT_URL,
        },
        "filters": {
            "include": [f"{DOCS_PATH_PREFIX}/*"],
            "exclude_prefixes": list(EXCLUDED_PREFIXES),
            "exclude_exact_paths": sorted(EXCLUDED_EXACT_PATHS),
            "exclude_cross_domain": True,
        },
        "files": new_files,
        "skipped": skipped,
        "fetch_metadata": {
            "total_pages_discovered": len(pages),
            "pages_fetched_successfully": live,
            "pages_stale": len(stale),
            "pages_skipped": len(skipped),
            "pages_failed": len(failed),
            "failed_pages": failed,
            "stale_pages": stale,
            "fetch_tool_version": FETCH_TOOL_VERSION,
        },
    }
    if _manifest_projection(manifest) == _manifest_projection(new_manifest):
        new_manifest["last_updated"] = manifest.get("last_updated", now_iso())
    else:
        new_manifest["last_updated"] = now_iso()
    write_text_if_changed(
        REFERENCES_DIR / MANIFEST_FILE,
        json.dumps(new_manifest, indent=2, sort_keys=True) + "\n",
    )

    problems = check_coverage_guards(
        discovered=len(pages),
        live=live,
        stale=len(stale),
        skipped=len(skipped),
        previous_file_count=len(manifest.get("files", {})),
    )
    if failed:
        problems.append(f"{len(failed)} page(s) failed; see {MANIFEST_FILE}")
    if problems:
        raise RuntimeError("; ".join(problems))

    return new_manifest


def _manifest_projection(manifest: dict) -> dict:
    projection = dict(manifest)
    projection.pop("last_updated", None)
    projection.pop("fetch_metadata", None)
    return projection


def main() -> int:
    start = time.monotonic()
    REFERENCES_DIR.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest()
    with requests.Session() as session:
        pages = discover_cursor_pages(session)
        if not pages:
            raise RuntimeError("No Cursor pages discovered")
        new_manifest = fetch_and_save_pages(session, pages, manifest)

    elapsed = time.monotonic() - start
    metadata = new_manifest["fetch_metadata"]
    logger.info(
        "Fetch complete in %.1fs: %s live, %s stale, %s skipped, %s failed",
        elapsed,
        metadata["pages_fetched_successfully"],
        metadata["pages_stale"],
        metadata["pages_skipped"],
        metadata["pages_failed"],
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        logger.error("%s", error)
        raise SystemExit(1) from error
