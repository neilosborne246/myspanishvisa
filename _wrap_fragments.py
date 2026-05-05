#!/usr/bin/env python3
"""
MSV Part 2 — Wrap HTML fragments in the site shell template.

Finds every .html file in the target folder that does NOT start with <!DOCTYPE html>,
reads _template.html, injects the fragment between FRAGMENT_START / FRAGMENT_END
markers, and overwrites the original file.

Skips:
  - _template.html itself
  - Any file already starting with <!DOCTYPE
"""

import os
import re
import sys

# ── Config ────────────────────────────────────────────────────────────────────
FOLDER       = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_FILE = os.path.join(FOLDER, "_template.html")
LOG_FILE      = os.path.join(FOLDER, "_wrap_log.txt")
MARKER_START  = "<!-- FRAGMENT_START -->"
MARKER_END    = "<!-- FRAGMENT_END -->"

# ── Load template ─────────────────────────────────────────────────────────────
with open(TEMPLATE_FILE, "r", encoding="utf-8") as fh:
    template = fh.read()

if MARKER_START not in template or MARKER_END not in template:
    print("ERROR: Template is missing FRAGMENT_START / FRAGMENT_END markers.")
    sys.exit(1)

# ── Helpers ───────────────────────────────────────────────────────────────────

def is_fragment(path: str) -> bool:
    """Return True if file does NOT begin with <!DOCTYPE (case-insensitive)."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            head = fh.read(100)
        return not head.lstrip().upper().startswith("<!DOCTYPE")
    except Exception:
        return False


def extract_title(content: str, filename: str) -> str:
    """
    Try to extract a page title from the fragment:
      1. │ Title: … │  pattern in HTML comments
      2. <title>…</title>  tag
      3. Fall back to prettified filename
    """
    # Pattern 1 — box-comment metadata
    m = re.search(r"[│|]\s*Title:\s*(.+?)\s*[│|]", content)
    if m:
        return m.group(1).strip()

    # Pattern 2 — existing <title> tag
    m = re.search(r"<title>([^<]+)</title>", content, re.IGNORECASE)
    if m:
        return m.group(1).strip()

    # Pattern 3 — derive from filename
    stem = os.path.splitext(os.path.basename(filename))[0]
    return stem.replace("-", " ").replace("_", " ").title() + " | My Spanish Visa"


def extract_meta_description(content: str) -> str:
    """Pull meta description from fragment if present."""
    m = re.search(
        r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']',
        content,
        re.IGNORECASE,
    )
    if m:
        return m.group(1).strip()
    # Also check box-comment style
    m = re.search(r"[│|]\s*Description:\s*(.+?)\s*[│|]", content)
    if m:
        return m.group(1).strip()
    return ""


def inject_fragment(template_html: str, fragment: str, title: str, desc: str) -> str:
    """
    Replace the fragment markers in the template and patch the <title> placeholder.
    """
    # Patch title
    result = re.sub(
        r"<title>[^<]*</title>",
        f"<title>{title}</title>",
        template_html,
        count=1,
        flags=re.IGNORECASE,
    )
    # Patch meta description
    if desc:
        result = re.sub(
            r'(<meta\s+name=["\']description["\']\s+content=["\'])[^"\']*(["\'])',
            lambda m_: m_.group(1) + desc + m_.group(2),
            result,
            count=1,
            flags=re.IGNORECASE,
        )

    # Inject fragment content
    result = result.replace(
        f"{MARKER_START}\n{MARKER_END}",
        f"{MARKER_START}\n{fragment}\n{MARKER_END}",
    )
    # Fallback if markers are on same line
    result = result.replace(
        f"{MARKER_START}{MARKER_END}",
        f"{MARKER_START}\n{fragment}\n{MARKER_END}",
    )
    return result


# ── Main ──────────────────────────────────────────────────────────────────────
html_files = sorted(
    f for f in os.listdir(FOLDER) if f.lower().endswith(".html")
)

processed = []
skipped   = []

for fname in html_files:
    fpath = os.path.join(FOLDER, fname)

    # Skip the template itself
    if fname.startswith("_"):
        skipped.append(f"SKIP (underscore): {fname}")
        continue

    if not is_fragment(fpath):
        skipped.append(f"SKIP (has DOCTYPE): {fname}")
        continue

    # Read fragment
    with open(fpath, "r", encoding="utf-8", errors="replace") as fh:
        fragment_content = fh.read()

    title = extract_title(fragment_content, fname)
    desc  = extract_meta_description(fragment_content)

    wrapped = inject_fragment(template, fragment_content, title, desc)

    # Write back
    with open(fpath, "w", encoding="utf-8") as fh:
        fh.write(wrapped)

    msg = f"WRAPPED: {fname}  |  title='{title}'"
    print(msg)
    processed.append(msg)

# ── Write log ─────────────────────────────────────────────────────────────────
with open(LOG_FILE, "w", encoding="utf-8") as fh:
    fh.write(f"MSV Wrap Log — {len(processed)} files wrapped, {len(skipped)} skipped\n")
    fh.write("=" * 70 + "\n\n")
    fh.write("── WRAPPED ─────────────────────────────────────────────────────\n")
    fh.write("\n".join(processed))
    fh.write("\n\n── SKIPPED ─────────────────────────────────────────────────────\n")
    fh.write("\n".join(skipped))
    fh.write("\n")

print(f"\n✓ Done — {len(processed)} wrapped, {len(skipped)} skipped.")
print(f"  Log: {LOG_FILE}")
