#!/usr/bin/env python3
"""
fix_image_paths.py
==================
Replaces all wp-content/uploads image references with /assets/images/ equivalents
across every .html file in the target directory.

Handles:
  - https://www.myspanishvisa.com/wp-content/uploads/...  (meta OG tags, JSON-LD)
  - http://myspanishvisa.com/wp-content/uploads/...        (old nav/footer img tags)
  - /wp-content/uploads/...                                (relative paths)

Covers img src, meta content, twitter:image, JSON-LD logo fields.

Usage:
  python3 fix_image_paths.py                  # dry run — shows what would change
  python3 fix_image_paths.py --apply          # writes changes to disk
  python3 fix_image_paths.py --apply --verbose  # verbose output per file

"""

import os
import sys
import glob
import argparse

# ─────────────────────────────────────────────────────────────────────────────
# REPLACEMENT MAP
# Order matters: longer / more-specific patterns must come before shorter ones
# to avoid partial matches (e.g. the dated paths before the bare filename).
# ─────────────────────────────────────────────────────────────────────────────

REPLACEMENTS = [

    # ── Absolute https:// URLs ───────────────────────────────────────────────

    # Logos (various dated upload paths → single canonical logo file)
    (
        "https://www.myspanishvisa.com/wp-content/uploads/2026/04/EMAIL-PLS-LOGO.png",
        "https://www.myspanishvisa.com/assets/images/msv-logo.png",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/msv-logo.png",
        "https://www.myspanishvisa.com/assets/images/msv-logo.png",
    ),

    # OG / social sharing images
    (
        "https://www.myspanishvisa.com/wp-content/uploads/msv-eligibility-og.jpg",
        "https://www.myspanishvisa.com/assets/images/og/msv-eligibility-og.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/msv-get-help-og.jpg",
        "https://www.myspanishvisa.com/assets/images/og/msv-get-help-og.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/msv-services-og.jpg",
        "https://www.myspanishvisa.com/assets/images/og/msv-services-og.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-blog-myspanishvisa.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-blog-myspanishvisa.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-blog.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-blog.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-dnv-pathway.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-dnv-pathway.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-dnv-spain.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-dnv-spain.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-faq.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-faq.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-myspanishvisa-default.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-myspanishvisa-default.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-myspanishvisa.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-myspanishvisa.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-nlv-ireland.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-nlv-ireland.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-nlv-pathway.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-nlv-pathway.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-nlv-spain.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-nlv-spain.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-retire-spain.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-retire-spain.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-spain-retirement-visa-americans.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-spain-retirement-visa-americans.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-spain-retirement-visa-australia.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-spain-retirement-visa-australia.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-spain-retirement-visa-canada.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-spain-retirement-visa-canada.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-spain-retirement-visa-ireland.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-spain-retirement-visa-ireland.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-spain-retirement-visa-south-africa.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-spain-retirement-visa-south-africa.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-spain-retirement-visa-uk.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-spain-retirement-visa-uk.jpg",
    ),
    (
        "https://www.myspanishvisa.com/wp-content/uploads/og-student-visa-spain.jpg",
        "https://www.myspanishvisa.com/assets/images/og/og-student-visa-spain.jpg",
    ),

    # ── Absolute http:// URLs (old nav/footer img tags) ──────────────────────
    # These are in <img src="..."> so replace with a root-relative path

    (
        "http://myspanishvisa.com/wp-content/uploads/2024/04/4-2.png",
        "/assets/images/msv-logo.png",
    ),
    (
        "http://myspanishvisa.com/wp-content/uploads/2024/04/2-1.png",
        "/assets/images/msv-logo.png",
    ),
    (
        "http://myspanishvisa.com/wp-content/uploads/2026/04/EMAIL-PLS-LOGO.png",
        "/assets/images/msv-logo.png",
    ),

    # ── Relative paths (/wp-content/uploads/...) ─────────────────────────────
    # Specific dated paths first, then bare filenames

    (
        "/wp-content/uploads/2024/04/4-2.png",
        "/assets/images/msv-logo.png",
    ),
    (
        "/wp-content/uploads/2024/04/2-1.png",
        "/assets/images/msv-logo.png",
    ),
    (
        "/wp-content/uploads/2026/04/EMAIL-PLS-LOGO.png",
        "/assets/images/msv-logo.png",
    ),
    (
        "/wp-content/uploads/msv-logo.png",
        "/assets/images/msv-logo.png",
    ),
    (
        "/wp-content/uploads/msv-eligibility-og.jpg",
        "/assets/images/og/msv-eligibility-og.jpg",
    ),
    (
        "/wp-content/uploads/msv-get-help-og.jpg",
        "/assets/images/og/msv-get-help-og.jpg",
    ),
    (
        "/wp-content/uploads/msv-services-og.jpg",
        "/assets/images/og/msv-services-og.jpg",
    ),
    (
        "/wp-content/uploads/og-blog-myspanishvisa.jpg",
        "/assets/images/og/og-blog-myspanishvisa.jpg",
    ),
    (
        "/wp-content/uploads/og-blog.jpg",
        "/assets/images/og/og-blog.jpg",
    ),
    (
        "/wp-content/uploads/og-dnv-pathway.jpg",
        "/assets/images/og/og-dnv-pathway.jpg",
    ),
    (
        "/wp-content/uploads/og-dnv-spain.jpg",
        "/assets/images/og/og-dnv-spain.jpg",
    ),
    (
        "/wp-content/uploads/og-faq.jpg",
        "/assets/images/og/og-faq.jpg",
    ),
    (
        "/wp-content/uploads/og-myspanishvisa-default.jpg",
        "/assets/images/og/og-myspanishvisa-default.jpg",
    ),
    (
        "/wp-content/uploads/og-myspanishvisa.jpg",
        "/assets/images/og/og-myspanishvisa.jpg",
    ),
    (
        "/wp-content/uploads/og-nlv-ireland.jpg",
        "/assets/images/og/og-nlv-ireland.jpg",
    ),
    (
        "/wp-content/uploads/og-nlv-pathway.jpg",
        "/assets/images/og/og-nlv-pathway.jpg",
    ),
    (
        "/wp-content/uploads/og-nlv-spain.jpg",
        "/assets/images/og/og-nlv-spain.jpg",
    ),
    (
        "/wp-content/uploads/og-retire-spain.jpg",
        "/assets/images/og/og-retire-spain.jpg",
    ),
    (
        "/wp-content/uploads/og-spain-retirement-visa-americans.jpg",
        "/assets/images/og/og-spain-retirement-visa-americans.jpg",
    ),
    (
        "/wp-content/uploads/og-spain-retirement-visa-australia.jpg",
        "/assets/images/og/og-spain-retirement-visa-australia.jpg",
    ),
    (
        "/wp-content/uploads/og-spain-retirement-visa-canada.jpg",
        "/assets/images/og/og-spain-retirement-visa-canada.jpg",
    ),
    (
        "/wp-content/uploads/og-spain-retirement-visa-ireland.jpg",
        "/assets/images/og/og-spain-retirement-visa-ireland.jpg",
    ),
    (
        "/wp-content/uploads/og-spain-retirement-visa-south-africa.jpg",
        "/assets/images/og/og-spain-retirement-visa-south-africa.jpg",
    ),
    (
        "/wp-content/uploads/og-spain-retirement-visa-uk.jpg",
        "/assets/images/og/og-spain-retirement-visa-uk.jpg",
    ),
    (
        "/wp-content/uploads/og-student-visa-spain.jpg",
        "/assets/images/og/og-student-visa-spain.jpg",
    ),
]


# ─────────────────────────────────────────────────────────────────────────────

def process_file(filepath, apply=False, verbose=False):
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        original = f.read()

    updated = original
    changes = []

    for old, new in REPLACEMENTS:
        if old in updated:
            count = updated.count(old)
            updated = updated.replace(old, new)
            changes.append((old, new, count))

    if changes:
        rel = os.path.relpath(filepath)
        if apply:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(updated)
            status = "FIXED"
        else:
            status = "DRY RUN"

        print(f"\n[{status}] {rel}")
        if verbose or not apply:
            for old, new, count in changes:
                print(f"  {count}x  {old}")
                print(f"      → {new}")
        else:
            total = sum(c for _, _, c in changes)
            print(f"  {len(changes)} pattern(s), {total} replacement(s)")

    return len(changes)


def main():
    parser = argparse.ArgumentParser(description="Fix wp-content image paths in HTML files")
    parser.add_argument(
        "--apply", action="store_true",
        help="Write changes to disk (default is dry run)"
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Print every replacement even when --apply is used"
    )
    parser.add_argument(
        "--dir", default=".",
        help="Root directory to scan (default: current directory)"
    )
    args = parser.parse_args()

    html_files = glob.glob(os.path.join(args.dir, "**", "*.html"), recursive=True)
    html_files.sort()

    if not html_files:
        print(f"No .html files found in: {args.dir}")
        sys.exit(1)

    mode = "APPLYING CHANGES" if args.apply else "DRY RUN (no files will be modified)"
    print(f"{'='*60}")
    print(f"  fix_image_paths.py — {mode}")
    print(f"  Directory : {os.path.abspath(args.dir)}")
    print(f"  HTML files: {len(html_files)}")
    print(f"{'='*60}")

    files_changed = 0
    for fp in html_files:
        n = process_file(fp, apply=args.apply, verbose=args.verbose)
        if n:
            files_changed += 1

    # Final summary
    print(f"\n{'='*60}")
    print(f"  Files scanned : {len(html_files)}")
    print(f"  Files {'changed' if args.apply else 'would change'}: {files_changed}")
    if not args.apply:
        print(f"\n  To apply changes, run:")
        print(f"    python3 fix_image_paths.py --apply")
    print(f"{'='*60}\n")

    # Safety check: confirm no wp-content references remain
    if args.apply:
        remaining = []
        for fp in html_files:
            with open(fp, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
            if "wp-content/uploads" in content:
                remaining.append(fp)

        if remaining:
            print(f"⚠️  WARNING: {len(remaining)} file(s) still contain wp-content/uploads references:")
            for fp in remaining:
                print(f"   {os.path.relpath(fp)}")
        else:
            print("✅  Verified: no wp-content/uploads references remain in any HTML file.")


if __name__ == "__main__":
    main()
