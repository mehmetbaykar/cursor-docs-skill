#!/usr/bin/env python3
"""Generate the cursor-docs skill references from Cursor documentation pages."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html as html_lib
import json
import logging
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from email import policy
from email.parser import BytesParser
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURES_DIR = ROOT / "pages"
REFERENCES_DIR = ROOT / "skills" / "cursor-docs" / "references"
BASE_URL = "https://cursor.com"
FETCH_TOOL_VERSION = "1.0"
USER_AGENT = "Mozilla/5.0"
NEXT_FLIGHT_PUSH_RE = re.compile(
    r"<script[^>]*>\s*self\.__next_f\.push\((.*?)\)\s*</script>", re.DOTALL
)
NEXT_FLIGHT_REFERENCE_RE = re.compile(r"^\$L([0-9a-fA-F]+)$")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("cursor-docs")


@dataclass(frozen=True)
class PageSpec:
    slug: str
    url: str
    fixture: str

    @property
    def path(self) -> str:
        return urllib.parse.urlparse(self.url).path


SELECTED_PAGES: tuple[PageSpec, ...] = (
    PageSpec(
        "skills", "https://cursor.com/docs/skills", "Agent Skills _ Cursor Docs.mhtml"
    ),
    PageSpec("rules", "https://cursor.com/docs/rules", "Rules _ Cursor Docs.mhtml"),
    PageSpec("hooks", "https://cursor.com/docs/hooks", "Hooks _ Cursor Docs.mhtml"),
    PageSpec(
        "mcp",
        "https://cursor.com/docs/mcp",
        "Model Context Protocol (MCP) _ Cursor Docs.mhtml",
    ),
    PageSpec(
        "subagents",
        "https://cursor.com/docs/subagents",
        "Subagents _ Cursor Docs.mhtml",
    ),
    PageSpec(
        "plugins", "https://cursor.com/docs/plugins", "Plugins _ Cursor Docs.mhtml"
    ),
)

INCLUDED_SLUGS = {page.slug for page in SELECTED_PAGES}
SKIP_TAGS = {"script", "style", "svg", "form", "iframe", "video", "canvas", "noscript"}
VOID_TAGS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "source",
    "track",
    "wbr",
}


def normalize_slug(value: str) -> str:
    """Normalize a Cursor docs path, URL, or topic into a reference slug."""

    value = value.strip().lower()
    if not value:
        return ""

    parsed = urllib.parse.urlparse(value)
    if parsed.netloc == "cursor.com" and parsed.path.startswith("/docs/"):
        value = parsed.path[len("/docs/") :]
    elif value.startswith("https://cursor.com/docs/"):
        value = value[len("https://cursor.com/docs/") :]
    elif value.startswith("/docs/"):
        value = value[len("/docs/") :]

    value = value.split("#", 1)[0].split("?", 1)[0]
    value = value.strip("/")
    value = value.removesuffix(".md")
    value = re.sub(r"\s+", "-", value)
    return "__".join(part for part in value.split("/") if part)


def rewrite_link(href: str) -> str:
    """Rewrite mirrored Cursor docs links to local reference files."""

    href = href.strip()
    if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
        return href

    parsed = urllib.parse.urlparse(href)
    fragment = f"#{parsed.fragment}" if parsed.fragment else ""

    path = parsed.path.removesuffix(".md")

    if not parsed.netloc and path.startswith("/docs/"):
        slug = normalize_slug(path)
        if slug in INCLUDED_SLUGS:
            return f"{slug}.md{fragment}"
        return urllib.parse.urljoin(BASE_URL, parsed.path) + fragment

    if parsed.netloc == "cursor.com" and path.startswith("/docs/"):
        slug = normalize_slug(path)
        if slug in INCLUDED_SLUGS:
            return f"{slug}.md{fragment}"
        return urllib.parse.urlunparse(
            ("https", "cursor.com", parsed.path, "", parsed.query, parsed.fragment)
        )

    return href


class ProseMarkdownConverter(HTMLParser):
    """Small HTML-to-Markdown converter for Cursor's docs prose subtree."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.active = False
        self.found_prose = False
        self.depth = 0
        self.skip_depth = 0
        self.in_pre = False
        self.pre_parts: list[str] = []
        self.list_stack: list[dict[str, int | str]] = []
        self.link_stack: list[dict[str, str | list[str]]] = []
        self.in_table = False
        self.table_rows: list[list[str]] = []
        self.current_row: list[str] | None = None
        self.current_cell_parts: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {name: value or "" for name, value in attrs}

        if not self.active:
            if tag == "div" and self._is_prose_container(attrs_dict):
                self.active = True
                self.found_prose = True
                self.depth = 1
            return

        if tag not in VOID_TAGS:
            self.depth += 1

        if self.skip_depth:
            if tag not in VOID_TAGS:
                self.skip_depth += 1
            return

        if tag in SKIP_TAGS:
            self.skip_depth = 1 if tag not in VOID_TAGS else 0
            return

        if self.in_pre and tag != "pre":
            if tag == "br":
                self.pre_parts.append("\n")
            return

        if tag == "pre":
            self._append("\n\n")
            self.in_pre = True
            self.pre_parts = []
            return

        if tag == "table":
            self.in_table = True
            self.table_rows = []
            return

        if self.in_table:
            self._handle_table_start(tag)
            return

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(tag[1])
            self._append(f"\n\n{'#' * level} ")
        elif tag == "p":
            self._append("\n\n")
        elif tag == "br":
            self._append("\n")
        elif tag in {"ul", "ol"}:
            self.list_stack.append({"type": tag, "index": 0})
            self._append("\n")
        elif tag == "li":
            self._start_list_item()
        elif tag == "blockquote":
            self._append("\n\n> ")
        elif tag == "code":
            self._append("`")
        elif tag == "strong" or tag == "b":
            self._append("**")
        elif tag == "em" or tag == "i":
            self._append("*")
        elif tag == "a":
            href = rewrite_link(attrs_dict.get("href", ""))
            self.link_stack.append({"href": href, "parts": []})
        elif tag == "hr":
            self._append("\n\n---\n\n")
        elif tag == "img":
            alt = attrs_dict.get("alt", "").strip()
            if alt:
                self._append(f"\n\n{alt}\n\n")

    def handle_endtag(self, tag: str) -> None:
        if not self.active:
            return

        if self.skip_depth:
            self.skip_depth -= 1
            if tag not in VOID_TAGS:
                self._leave_tag()
            return

        if self.in_pre and tag != "pre":
            self._leave_tag()
            return

        if tag == "pre":
            code = "".join(self.pre_parts).strip("\n")
            self._append(f"```\n{code}\n```\n\n")
            self.in_pre = False
            self.pre_parts = []
            self._leave_tag()
            return

        if self.in_table:
            self._handle_table_end(tag)
            self._leave_tag()
            return

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6", "p", "blockquote"}:
            self._append("\n\n")
        elif tag in {"ul", "ol"}:
            if self.list_stack:
                self.list_stack.pop()
            self._append("\n")
        elif tag == "li":
            self._append("\n")
        elif tag == "code":
            self._append("`")
        elif tag == "strong" or tag == "b":
            self._append("**")
        elif tag == "em" or tag == "i":
            self._append("*")
        elif tag == "a" and self.link_stack:
            link = self.link_stack.pop()
            text = "".join(link["parts"]).strip()
            href = str(link["href"])
            if text and href:
                self._append(f"[{text}]({href})")
            elif text:
                self._append(text)

        self._leave_tag()

    def handle_data(self, data: str) -> None:
        if not self.active or self.skip_depth:
            return
        if self.in_pre:
            self.pre_parts.append(data)
        else:
            self._append_text(data)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in VOID_TAGS:
            self.handle_endtag(tag)

    def markdown(self) -> str:
        if not self.found_prose:
            raise ValueError("Could not find Cursor docs prose container")
        return clean_markdown("".join(self.parts))

    def _is_prose_container(self, attrs: dict[str, str]) -> bool:
        classes = set(attrs.get("class", "").split())
        if {"prose", "prose-lg", "max-w-none"}.issubset(classes):
            return True
        return "prose" in classes

    def _append_text(self, text: str) -> None:
        text = re.sub(r"\s+", " ", text.replace("\xa0", " "))
        if not text:
            return
        if text == " " and self._last_char_is_space():
            return
        self._append(text)

    def _append(self, text: str) -> None:
        if self.link_stack:
            self.link_stack[-1]["parts"].append(text)
        elif self.current_cell_parts is not None:
            self.current_cell_parts.append(text)
        else:
            self.parts.append(text)

    def _last_char_is_space(self) -> bool:
        target: list[str]
        if self.link_stack:
            target = self.link_stack[-1]["parts"]  # type: ignore[assignment]
        elif self.current_cell_parts is not None:
            target = self.current_cell_parts
        else:
            target = self.parts
        return bool(target and target[-1] and target[-1][-1].isspace())

    def _start_list_item(self) -> None:
        if not self.list_stack:
            self._append("\n- ")
            return
        current = self.list_stack[-1]
        current["index"] = int(current["index"]) + 1
        indent = "  " * (len(self.list_stack) - 1)
        marker = f"{current['index']}. " if current["type"] == "ol" else "- "
        self._append(f"\n{indent}{marker}")

    def _handle_table_start(self, tag: str) -> None:
        if tag == "tr":
            self.current_row = []
        elif tag in {"th", "td"}:
            self.current_cell_parts = []
        elif tag == "br":
            self._append(" ")
        elif tag == "code":
            self._append("`")
        elif tag == "strong" or tag == "b":
            self._append("**")
        elif tag == "em" or tag == "i":
            self._append("*")
        elif tag == "a":
            self.link_stack.append({"href": "", "parts": []})

    def _handle_table_end(self, tag: str) -> None:
        if (
            tag in {"th", "td"}
            and self.current_row is not None
            and self.current_cell_parts is not None
        ):
            cell = " ".join("".join(self.current_cell_parts).split())
            self.current_row.append(cell)
            self.current_cell_parts = None
        elif tag == "tr" and self.current_row:
            self.table_rows.append(self.current_row)
            self.current_row = None
        elif tag == "table":
            self._append(render_table(self.table_rows))
            self.in_table = False
        elif tag == "code":
            self._append("`")
        elif tag == "strong" or tag == "b":
            self._append("**")
        elif tag == "em" or tag == "i":
            self._append("*")
        elif tag == "a" and self.link_stack:
            link = self.link_stack.pop()
            self._append("".join(link["parts"]).strip())

    def _leave_tag(self) -> None:
        if self.depth:
            self.depth -= 1
        if self.depth == 0:
            self.active = False


def prose_html_to_markdown(html_text: str) -> str:
    converter = ProseMarkdownConverter()
    converter.feed(html_text)
    converter.close()
    return converter.markdown()


def clean_markdown(text: str) -> str:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    cleaned: list[str] = []
    in_fence = False
    blank = 0

    for line in lines:
        if line.startswith("```"):
            if cleaned and cleaned[-1] != "":
                cleaned.append("")
            cleaned.append(line.rstrip())
            in_fence = not in_fence
            blank = 0
            continue

        if in_fence:
            cleaned.append(line.rstrip())
            continue

        line = re.sub(r"[ \t]+", " ", line).rstrip()
        if not re.match(r"^\s+(-|\d+\.) ", line):
            line = line.strip()

        if not line:
            blank += 1
            if blank <= 1:
                cleaned.append("")
            continue

        blank = 0
        cleaned.append(line)

    return "\n".join(cleaned).strip() + "\n"


def render_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""

    width = max(len(cells) for cells in rows)
    normalized = [cells + [""] * (width - len(cells)) for cells in rows]
    header = normalized[0]
    body = normalized[1:]

    def cell(value: str) -> str:
        return value.replace("|", "\\|").strip()

    lines = ["", "| " + " | ".join(cell(value) for value in header) + " |"]
    lines.append("| " + " | ".join("---" for _ in header) + " |")
    lines.extend("| " + " | ".join(cell(value) for value in row) + " |" for row in body)
    return "\n".join(lines) + "\n\n"


def extract_next_flight_records(html_text: str) -> dict[str, object]:
    """Extract parseable React Flight records embedded in Next.js HTML."""

    stream_parts: list[str] = []
    for match in NEXT_FLIGHT_PUSH_RE.finditer(html_text):
        try:
            payload = json.loads(match.group(1))
        except json.JSONDecodeError:
            continue

        if (
            isinstance(payload, list)
            and len(payload) > 1
            and isinstance(payload[1], str)
        ):
            stream_parts.append(payload[1])

    records: dict[str, object] = {}
    for line in "".join(stream_parts).splitlines():
        record_id, separator, payload = line.partition(":")
        if not separator:
            continue

        payload = payload.strip()
        if not payload or payload[0] not in '[{"ntf-0123456789':
            continue

        try:
            records[record_id] = json.loads(payload)
        except json.JSONDecodeError:
            continue

    return records


def next_flight_to_html(html_text: str) -> str:
    records = extract_next_flight_records(html_text)
    if not records:
        return ""

    for node in records.values():
        prose_node = find_next_flight_prose_node(node, records, set())
        if prose_node is not None:
            return render_next_flight_node(prose_node, records, set())

    return ""


def find_next_flight_prose_node(
    node: object,
    records: dict[str, object],
    seen: set[str],
) -> object | None:
    resolved = resolve_next_flight_reference(node, records, seen)
    if resolved is None:
        return None

    if is_next_flight_element(resolved):
        props = next_flight_props(resolved)
        if has_prose_classes(props.get("className", "")):
            return resolved

        found = find_next_flight_prose_node(props.get("children"), records, seen)
        if found is not None:
            return found

    if isinstance(resolved, list):
        for item in resolved:
            found = find_next_flight_prose_node(item, records, seen)
            if found is not None:
                return found
    elif isinstance(resolved, dict):
        for value in resolved.values():
            found = find_next_flight_prose_node(value, records, seen)
            if found is not None:
                return found

    return None


def has_prose_classes(class_name: object) -> bool:
    if not isinstance(class_name, str):
        return False
    parts = set(class_name.split())
    if {"prose", "prose-lg", "max-w-none"}.issubset(parts):
        return True
    return "prose" in parts


def render_next_flight_node(
    node: object,
    records: dict[str, object],
    seen: set[str],
) -> str:
    resolved = resolve_next_flight_reference(node, records, seen)
    if resolved is None or resolved == "$undefined":
        return ""

    if isinstance(resolved, str):
        if resolved.startswith("$$"):
            resolved = resolved[1:]
        return html_lib.escape(resolved)

    if isinstance(resolved, (int, float)):
        return html_lib.escape(str(resolved))

    if isinstance(resolved, list):
        if is_next_flight_element(resolved):
            return render_next_flight_element(resolved, records, seen)
        return "".join(
            render_next_flight_node(item, records, seen) for item in resolved
        )

    if isinstance(resolved, dict):
        return render_next_flight_node(resolved.get("children"), records, seen)

    return ""


def render_next_flight_element(
    element: list[object],
    records: dict[str, object],
    seen: set[str],
) -> str:
    tag = element[1]
    props = next_flight_props(element)

    if not isinstance(tag, str) or tag.startswith("$"):
        return render_next_flight_component(props, records, seen)

    if tag in SKIP_TAGS:
        return ""

    if tag == "br":
        return "<br>"

    attrs = render_next_flight_attrs(tag, props)
    if tag in VOID_TAGS:
        return f"<{tag}{attrs}>"

    children = render_next_flight_node(props.get("children"), records, seen)
    return f"<{tag}{attrs}>{children}</{tag}>"


def render_next_flight_component(
    props: dict[str, object],
    records: dict[str, object],
    seen: set[str],
) -> str:
    code = props.get("code")
    if isinstance(code, str):
        return f"<pre><code>{html_lib.escape(code)}</code></pre>"

    children = render_next_flight_node(props.get("children"), records, seen)
    if props.get("baseId") and children:
        level = 2 if "mt-12" in str(props.get("className", "")) else 3
        return f"<h{level}>{children}</h{level}>"

    if children.strip():
        return children

    fallback_parts: list[str] = []
    for key in ("title", "description", "label"):
        value = props.get(key)
        if isinstance(value, str) and value and not value.startswith("$"):
            fallback_parts.append(f"<p>{html_lib.escape(value)}</p>")
    return "".join(fallback_parts)


def render_next_flight_attrs(tag: str, props: dict[str, object]) -> str:
    attrs: list[str] = []

    class_name = props.get("className")
    if isinstance(class_name, str) and class_name and class_name != "$undefined":
        attrs.append(f' class="{html_lib.escape(class_name, quote=True)}"')

    if tag == "a":
        href = props.get("href") or props.get("data-card-href")
        if isinstance(href, str) and href and href != "$undefined":
            attrs.append(f' href="{html_lib.escape(href, quote=True)}"')

    if tag == "img":
        alt = props.get("alt")
        if isinstance(alt, str) and alt:
            attrs.append(f' alt="{html_lib.escape(alt, quote=True)}"')

    return "".join(attrs)


def resolve_next_flight_reference(
    node: object,
    records: dict[str, object],
    seen: set[str],
) -> object | None:
    if not isinstance(node, str):
        return node

    match = NEXT_FLIGHT_REFERENCE_RE.match(node)
    if not match:
        return node

    record_id = match.group(1)
    if record_id in seen or record_id not in records:
        return None

    return resolve_next_flight_reference(
        records[record_id], records, seen | {record_id}
    )


def is_next_flight_element(node: object) -> bool:
    return isinstance(node, list) and len(node) >= 4 and node[0] == "$"


def next_flight_props(element: list[object]) -> dict[str, object]:
    props = element[3]
    return props if isinstance(props, dict) else {}


def html_to_markdown(html_text: str) -> str:
    try:
        return prose_html_to_markdown(html_text)
    except ValueError as error:
        flight_html = next_flight_to_html(html_text)
        if flight_html:
            return prose_html_to_markdown(flight_html)
        raise error


def rewrite_markdown_links(markdown: str) -> str:
    def replace(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2).strip()
        if target.startswith("<") and target.endswith(">"):
            rewritten = rewrite_link(target[1:-1])
            return f"[{label}](<{rewritten}>)"
        return f"[{label}]({rewrite_link(target)})"

    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", replace, markdown)


def clean_live_markdown(markdown: str) -> str:
    markdown = rewrite_markdown_links(markdown)
    markdown = re.sub(r"\n?\[Media\]\([^)]+\)\n?", "\n", markdown)
    return clean_markdown(markdown)


def read_mhtml(path: Path) -> tuple[str, str]:
    with path.open("rb") as file:
        message = BytesParser(policy=policy.default).parse(file)

    source_url = message.get("Snapshot-Content-Location") or ""
    for part in message.walk():
        if part.get_content_type() != "text/html":
            continue
        payload = part.get_payload(decode=True)
        if payload is None:
            continue
        charset = part.get_content_charset() or "utf-8"
        content_url = part.get("Content-Location") or source_url
        return payload.decode(charset, errors="replace"), content_url

    raise ValueError(f"No HTML part found in {path}")


def _fetch(
    request: urllib.request.Request, attempts: int = 6
) -> tuple[bytes, str, str]:
    """Open the request with retry on 5xx and transient connection errors."""

    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                charset = response.headers.get_content_charset() or "utf-8"
                final_url = response.geturl() or request.full_url
                return response.read(), charset, final_url
        except urllib.error.HTTPError as error:
            transient = error.code >= 500 or error.code == 404
            if not transient or attempt == attempts - 1:
                raise
        except (urllib.error.URLError, TimeoutError):
            if attempt == attempts - 1:
                raise
        time.sleep(2**attempt)
    raise RuntimeError("unreachable: retries exhausted without raising")


def fetch_live(url: str) -> tuple[str, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    body, charset, final_url = _fetch(request)
    return body.decode(charset, errors="replace"), final_url


def fetch_live_markdown(url: str) -> tuple[str, str]:
    markdown_url = url.rstrip("/") + ".md"
    request = urllib.request.Request(
        markdown_url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/markdown,text/plain,*/*",
        },
    )
    body, charset, final_url = _fetch(request)
    return body.decode(charset, errors="replace"), final_url


def build_reference(
    html_text: str, source_url: str, page: PageSpec
) -> tuple[str, dict[str, str]]:
    markdown = html_to_markdown(html_text)
    return build_reference_from_markdown(markdown, source_url, page)


def build_reference_from_markdown(
    markdown: str,
    source_url: str,
    page: PageSpec,
) -> tuple[str, dict[str, str]]:
    markdown = clean_live_markdown(markdown)
    title = first_heading(markdown)
    if not title:
        raise ValueError(f"{page.url} did not produce an H1 heading")

    content = (
        f"---\ntitle: {title}\nsource: {page.url}\npath: {page.path}\n---\n\n{markdown}"
    )
    if len(markdown.strip()) < 100:
        raise ValueError(f"{page.url} produced suspiciously short Markdown")
    if "Skip to main content" in markdown:
        raise ValueError(f"{page.url} includes docs chrome")

    metadata = {
        "hash": hashlib.sha256(content.encode("utf-8")).hexdigest(),
        "original_url": page.url,
        "path": page.path,
        "source_url": source_url,
        "title": title,
    }
    return content, metadata


def first_heading(markdown: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def build_index(files: dict[str, dict[str, str]]) -> str:
    lines = [
        "# Cursor Docs Index",
        "",
        "Local mirror of selected Cursor documentation from https://cursor.com/docs/.",
        "",
        "Invoke this skill with a topic, for example `/cursor-docs hooks`.",
        "",
        "## Topics",
        "",
    ]
    for filename, metadata in sorted(files.items()):
        slug = filename.removesuffix(".md")
        lines.append(f"- `{slug}` - [{metadata['title']}]({metadata['original_url']})")
    return "\n".join(lines).rstrip() + "\n"


def load_existing_manifest(references_dir: Path = REFERENCES_DIR) -> dict[str, object]:
    manifest_path = references_dir / "docs_manifest.json"
    if not manifest_path.exists():
        return {}
    try:
        return json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def preserve_last_updated(
    filename: str,
    metadata: dict[str, str],
    previous_manifest: dict[str, object],
    run_timestamp: str,
) -> dict[str, str]:
    previous_files = previous_manifest.get("files")
    if isinstance(previous_files, dict):
        previous_metadata = previous_files.get(filename)
        if (
            isinstance(previous_metadata, dict)
            and previous_metadata.get("hash") == metadata["hash"]
            and isinstance(previous_metadata.get("last_updated"), str)
        ):
            metadata["last_updated"] = previous_metadata["last_updated"]
            return metadata

    metadata["last_updated"] = run_timestamp
    return metadata


def manifest_last_updated(
    files: dict[str, dict[str, str]],
    previous_manifest: dict[str, object],
    run_timestamp: str,
) -> str:
    previous_files = previous_manifest.get("files")
    if isinstance(previous_files, dict) and set(previous_files) == set(files):
        hashes_match = all(
            isinstance(previous_files[name], dict)
            and previous_files[name].get("hash") == metadata["hash"]
            for name, metadata in files.items()
        )
        previous_timestamp = previous_manifest.get("last_updated")
        if hashes_match and isinstance(previous_timestamp, str):
            return previous_timestamp
    return run_timestamp


def build_manifest(
    files: dict[str, dict[str, str]],
    fixture_mode: bool,
    last_updated: str,
) -> dict[str, object]:
    return {
        "description": "Cursor documentation mirror manifest. Files live beside this manifest in references/.",
        "source": "https://cursor.com/docs/",
        "include": [page.url for page in SELECTED_PAGES],
        "last_updated": last_updated,
        "fetch_metadata": {
            "failed_pages": [],
            "fetch_tool_version": FETCH_TOOL_VERSION,
            "fixture_mode": fixture_mode,
            "pages_failed": 0,
            "pages_fetched_successfully": len(files),
            "pages_skipped": 0,
            "raw_fallback_pages": 0,
            "total_pages_discovered": len(SELECTED_PAGES),
        },
        "files": files,
        "skipped": [],
    }


def generate_references(
    fixtures_dir: Path | None = None,
) -> tuple[dict[str, str], dict[str, object]]:
    run_timestamp = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    previous_manifest = load_existing_manifest()
    contents: dict[str, str] = {}
    files: dict[str, dict[str, str]] = {}

    previous_files = previous_manifest.get("files")
    previous_files = previous_files if isinstance(previous_files, dict) else {}
    failed: list[tuple[str, Exception]] = []
    updated = 0
    unchanged = 0

    for index, page in enumerate(SELECTED_PAGES, start=1):
        logger.info("Fetching %d/%d: %s", index, len(SELECTED_PAGES), page.slug)
        filename = f"{page.slug}.md"
        try:
            if fixtures_dir is None:
                markdown, source_url = fetch_live_markdown(page.url)
                content, metadata = build_reference_from_markdown(
                    markdown, source_url, page
                )
            else:
                html_text, source_url = read_mhtml(fixtures_dir / page.fixture)
                content, metadata = build_reference(html_text, source_url, page)
        except urllib.error.HTTPError as error:
            if (
                error.code == 404
                and fixtures_dir is None
                and isinstance(previous_files.get(filename), dict)
                and (REFERENCES_DIR / filename).exists()
            ):
                logger.warning(
                    "Stale (404 after retries): %s; keeping previous content", page.slug
                )
                content = (REFERENCES_DIR / filename).read_text(encoding="utf-8")
                metadata = dict(previous_files[filename])
                contents[filename] = content
                files[filename] = metadata
                unchanged += 1
                continue
            logger.error("Failed: %s (%s)", page.slug, error)
            failed.append((page.slug, error))
            continue
        except Exception as error:  # noqa: BLE001
            logger.error("Failed: %s (%s)", page.slug, error)
            failed.append((page.slug, error))
            continue

        metadata = preserve_last_updated(
            filename, metadata, previous_manifest, run_timestamp
        )
        previous_hash = (
            previous_files.get(filename, {}).get("hash")
            if isinstance(previous_files.get(filename), dict)
            else None
        )
        if previous_hash == metadata["hash"]:
            logger.info("Unchanged: %s", filename)
            unchanged += 1
        else:
            logger.info("Updated: %s", filename)
            updated += 1
        contents[filename] = content
        files[filename] = metadata

    if failed:
        raise RuntimeError(
            "failed to fetch or parse "
            + ", ".join(f"{slug} ({error})" for slug, error in failed)
        )

    logger.info(
        "Fetch complete: %d updated, %d unchanged",
        updated,
        unchanged,
    )

    contents["INDEX.md"] = build_index(files)
    manifest = build_manifest(
        files,
        fixture_mode=fixtures_dir is not None,
        last_updated=manifest_last_updated(files, previous_manifest, run_timestamp),
    )
    contents["docs_manifest.json"] = (
        json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    )
    return contents, manifest


def write_references(
    contents: dict[str, str], references_dir: Path = REFERENCES_DIR
) -> None:
    references_dir.mkdir(parents=True, exist_ok=True)
    generated_names = set(contents)
    for path in references_dir.iterdir():
        if (
            path.is_file()
            and (path.suffix == ".md" or path.name == "docs_manifest.json")
            and path.name not in generated_names
        ):
            path.unlink()
    for filename, content in contents.items():
        (references_dir / filename).write_text(content, encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fixtures",
        nargs="?",
        const=str(DEFAULT_FIXTURES_DIR),
        help="Generate from local MHTML fixtures instead of live Cursor docs.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Generate references in memory only and report success without writing files.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    fixtures_dir = Path(args.fixtures).resolve() if args.fixtures else None

    try:
        contents, _ = generate_references(fixtures_dir)
    except Exception as error:  # noqa: BLE001 - CLI should surface any fetch or parse failure clearly.
        logger.error("cursor-docs update failed: %s", error)
        return 1

    if args.check:
        logger.info(
            "Generated %d cursor-docs reference artifacts successfully.", len(contents)
        )
        return 0

    write_references(contents)
    mode = "fixtures" if fixtures_dir else "live Cursor docs"
    logger.info("Updated cursor-docs references from %s.", mode)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
