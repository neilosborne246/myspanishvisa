#!/usr/bin/env python3
"""
MSV Insurance Fix — Three-pass cleanup across all HTML files.

PASS 1 — Delete brand-specific insurer review pages (whole page is about one brand).
PASS 2 — Fix broker card tags/descriptions: remove "Exclusive Sanitas Agents" language
          from Spanish Health Insurance cards; ensure both partners appear correctly.
PASS 3 — Scrub inline brand name mentions from body text across all remaining files.
          Replace brand comparisons/recommendations with generic language or partner refs.

Approved partners only:
  Spanish Health Insurance  → https://www.spanish-healthinsurance.com/myspanishvisa
  247 Expat Insurance       → https://www.247expatinsurance.com/myspanishvisa
"""

import os
import re
import sys

FOLDER   = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(FOLDER, "_insurance_fix_log.txt")

# ── Files to delete entirely (brand-specific review pages) ─────────────────────
DELETE_FILES = [
    "blog-axa-spain-health-insurance-visa.html",
    "blog-cigna-allianz-health-insurance-spain.html",
    "blog-sanitas-health-insurance-spain-review.html",
]

# ── Brand name pattern ─────────────────────────────────────────────────────────
BRAND_RE = re.compile(
    r'\b(AXA(?:\s+Salud)?|Sanitas(?:\s+\(backed\s+by\s+Bupa\))?|Cigna(?:\s+Global)?|'
    r'Allianz(?:\s+Care)?|Mapfre|MAPFRE|Asisa|ASISA|DKV|Adeslas|Caser|'
    r'Generali|Zurich|Bupa)\b',
    re.IGNORECASE,
)

# Regex for comma-separated brand lists (e.g. "Sanitas, Adeslas, Mapfre, Asisa, and DKV")
BRAND_LIST_RE = re.compile(
    r'(?:(?:AXA|Sanitas|Cigna|Allianz|Mapfre|Asisa|DKV|Adeslas|Caser|Generali|Zurich|Bupa)'
    r'(?:\s*\([^)]*\))?'
    r'(?:,\s*|\s+and\s+|\s+or\s+|\s*/\s*))+(?:AXA|Sanitas|Cigna|Allianz|Mapfre|Asisa|DKV|Adeslas|Caser|Generali|Zurich|Bupa)(?:\s*\([^)]*\))?',
    re.IGNORECASE,
)

# ── Broker card fix patterns ───────────────────────────────────────────────────
# Fix "Exclusive Sanitas Agents" tag in both dark and light card variants
BROKER_TAG_DARK_BAD  = re.compile(
    r'(<span\s+class="msv__broker-card-tag">)\s*Exclusive Sanitas Agents\s*(</span>)',
    re.IGNORECASE,
)
BROKER_TAG_LIGHT_BAD = re.compile(
    r'(<span\s+class="msv__broker-card-light-tag">)\s*Exclusive Sanitas Agents\s*(</span>)',
    re.IGNORECASE,
)

# Fix the Spanish Health Insurance card description that references Sanitas
# Matches any <p> tag immediately inside the Spanish Health Insurance broker card
# that contains "Sanitas" — replaces the whole paragraph.
BROKER_DESC_BAD = re.compile(
    r'(<h3>Spanish Health Insurance</h3>\s*)'
    r'<p>[^<]*Sanitas[^<]*(?:<[^>]+>[^<]*)*</p>',
    re.IGNORECASE | re.DOTALL,
)

BROKER_DESC_REPLACEMENT_DARK = (
    r'\1'
    r'<p>Health and visa insurance specialists for English-speaking foreigners moving to Spain. '
    r'Their team understand exactly what Spanish consulates require and can match you to '
    r'the right policy — whether you need cover for a new application, a renewal, or a full family plan.</p>'
)

# Same replacement but for light card variant (description is same, context different)
BROKER_DESC_REPLACEMENT_LIGHT = BROKER_DESC_REPLACEMENT_DARK

# ── Inline brand-comparison sections ──────────────────────────────────────────
# These are blocks like "Spain's Top Private Insurers" that list brands one by one.
# We replace the whole section with a clean generic + partner-referral paragraph.

# Match a section header followed by brand-by-brand <p> paragraphs
INSURER_SECTION_RE = re.compile(
    r'<h[23][^>]*>\s*(?:Spain\'?s?\s+)?(?:Top|Best|Major|Popular|Leading)\s+'
    r'(?:Private\s+)?(?:Insurers?|Health\s+Insurers?|Health\s+Insurance\s+(?:Providers?|Options?|Brands?))'
    r'(?:\s+in\s+Spain)?\s*</h[23]>'
    r'(?:\s*<p>[^<]*(?:Sanitas|AXA|Adeslas|Mapfre|Asisa|DKV|Cigna|Allianz)[^<]*</p>\s*)+',
    re.IGNORECASE | re.DOTALL,
)

INSURER_SECTION_REPLACEMENT = (
    '<h3>Finding the Right Health Insurance for Your Visa</h3>\n'
    '<p>There are several established private health insurers in Spain offering policies '
    'that meet consulate requirements. The right choice depends on your age, health history, '
    'family situation, and the specific consulate you are applying to.</p>\n'
    '<p>We recommend working with a specialist broker who understands Spanish visa requirements '
    'and can compare policies across providers on your behalf.</p>'
)

# ── "Our recommendation: [brand]..." paragraph fix ────────────────────────────
OUR_REC_RE = re.compile(
    r'<p[^>]*><strong>Our recommendation:</strong>[^<]*(?:Sanitas|AXA|Adeslas|Mapfre)[^<]*</p>',
    re.IGNORECASE | re.DOTALL,
)

OUR_REC_REPLACEMENT = (
    '<p><strong>Our recommendation:</strong> Work with a specialist insurance broker '
    'who understands Spanish visa requirements and can compare options across providers. '
    'See our recommended partners below.</p>'
)

# ── "Insurer choice: Sanitas, Adeslas..." list item fix ───────────────────────
INSURER_CHOICE_RE = re.compile(
    r'(<li[^>]*><strong>Insurer choice:</strong>\s*)'
    r'(?:Sanitas|AXA|Adeslas|Mapfre|Asisa|DKV)[^<]*(?:Sanitas|AXA|Adeslas|Mapfre|Asisa|DKV)[^<]*'
    r'(</li>)',
    re.IGNORECASE | re.DOTALL,
)

INSURER_CHOICE_REPLACEMENT = (
    r'\1Premiums and network coverage vary between insurers. '
    r'Use a specialist broker to compare policies for your specific profile.\2'
)

# ── Partner referral HTML block (inserted where needed) ───────────────────────
PARTNER_BLOCK_HTML = """
<div class="msv-callout" style="margin-top:32px;">
  <p><strong>Recommended insurance specialists:</strong><br>
  <a href="https://www.spanish-healthinsurance.com/myspanishvisa" target="_blank" rel="noopener"><strong>Spanish Health Insurance</strong></a> — visa-compliant health insurance for English-speaking foreigners in Spain.<br>
  <a href="https://www.247expatinsurance.com/myspanishvisa" target="_blank" rel="noopener"><strong>247 Expat Insurance</strong></a> — health and all types of insurance in Spain, tailored for expats.</p>
</div>"""

# Pages where we should inject the partner referral block if not already present
# (pages that are specifically about health insurance)
INSURANCE_FOCUSED_PAGES = {
    "best-health-insurance-nlv-spain.html",
    "nlv-health-insurance.html",
    "guide-healthcare-spain.html",
    "student-visa-spain-health-insurance.html",
    "no-copay-health-insurance-nlv.html",
    "nlv-renewal-health-insurance.html",
    "blog-nlv-health-insurance-requirements.html",
    "blog-category-health-insurance.html",
    "blog-best-private-health-insurance-spain-expats-2026.html",
    "blog-best-health-insurance-digital-nomad-visa.html",
    "blog-health-insurance-spain-cost-guide.html",
    "blog-health-insurance-spain-for-retirees.html",
    "blog-health-insurance-spain-pre-existing-conditions.html",
    "blog-private-health-insurance-spain-expat.html",
    "blog-no-copay-health-insurance-spain-visa.html",
    "blog-healthcare-spain-expats-guide.html",
    "blog-visa-compliant-health-insurance-spain.html",
    "blog-student-visa-spain-health-insurance.html",
    "blog-family-health-insurance-spain.html",
    "blog-non-lucrative-visa-spain-health-insurance-requirements.html",
    "blog-nlv-health-insurance-requirements.html",
    "dnv-health-insurance.html",
    "nlv-health-insurance-mistakes.html",
    "travel-insurance-nlv-spain.html",
}

# Anchor to insert partner block before (footer CTA section)
INSERT_ANCHOR_RE = re.compile(
    r'(<section[^>]+class="[^"]*msv-footer-cta[^"]*")',
    re.IGNORECASE,
)

# ── Inline brand-list replacement ─────────────────────────────────────────────

def replace_brand_lists(html: str) -> tuple[str, int]:
    """Replace comma-separated brand lists with generic language."""
    count = [0]

    def _repl(m):
        count[0] += 1
        return "established private health insurers in Spain"

    result = BRAND_LIST_RE.sub(_repl, html)
    return result, count[0]


def replace_solo_brands_in_body(html: str) -> tuple[str, int]:
    """
    Replace remaining solo brand mentions in body text (<p>, <li>, <td>).
    Avoids touching <script>, JSON-LD, <style>, or attribute values.
    """
    count = [0]

    # We'll process only text nodes inside body-content tags
    # Strategy: split on tags, replace brand names only in text runs
    parts = re.split(r'(<[^>]+>)', html)
    in_script = False
    in_style  = False
    result_parts = []

    for part in parts:
        if part.startswith('<'):
            low = part.lower()
            if low.startswith('<script'):
                in_script = True
            elif low.startswith('</script'):
                in_script = False
            elif low.startswith('<style'):
                in_style = True
            elif low.startswith('</style'):
                in_style = False
            result_parts.append(part)
        else:
            if in_script or in_style:
                result_parts.append(part)
            else:
                def _brand_repl(m):
                    count[0] += 1
                    return "a leading private insurer"
                replaced = BRAND_RE.sub(_brand_repl, part)
                result_parts.append(replaced)

    return ''.join(result_parts), count[0]


# ── Main processing ────────────────────────────────────────────────────────────

logs = []
total_deleted = 0
total_files_changed = 0
total_replacements = 0


# ── Redirect page template for replaced brand-specific pages ──────────────────
REDIRECT_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="0; url=/blog-healthcare-spain-expats-guide.html">
<link rel="canonical" href="https://www.myspanishvisa.com/guide-healthcare-spain.html">
<title>Health Insurance for Spain Visa | My Spanish Visa</title>
</head>
<body>
<p>Redirecting to our <a href="/guide-healthcare-spain.html">Spain health insurance guide</a>…</p>
</body>
</html>"""

# ── PASS 1: Replace brand-specific pages with redirects ───────────────────────
print("PASS 1 — Replacing brand-specific pages with redirects...")
for fname in DELETE_FILES:
    fpath = os.path.join(FOLDER, fname)
    if os.path.exists(fpath):
        with open(fpath, "w", encoding="utf-8") as fh:
            fh.write(REDIRECT_PAGE)
        msg = f"REDIRECTED: {fname}"
        print(f"  {msg}")
        logs.append(msg)
        total_deleted += 1
    else:
        msg = f"NOT FOUND (already gone?): {fname}"
        print(f"  {msg}")
        logs.append(msg)

print(f"  → {total_deleted} file(s) replaced with redirects.\n")


# ── PASS 2 & 3: Fix remaining files ───────────────────────────────────────────
html_files = sorted(f for f in os.listdir(FOLDER) if f.lower().endswith(".html"))

print("PASS 2+3 — Fixing brand mentions in remaining files...")

for fname in html_files:
    if fname.startswith("_"):
        continue

    fpath = os.path.join(FOLDER, fname)
    with open(fpath, "r", encoding="utf-8", errors="replace") as fh:
        original = html = fh.read()

    file_replacements = 0
    file_log = []

    # ── Broker card tag fixes ──────────────────────────────────────────────────
    new_html, n = BROKER_TAG_DARK_BAD.subn(
        r'\1Health Insurance Specialists\2', html
    )
    if n:
        file_log.append(f"  broker-card-tag (dark) fixed: {n}")
        file_replacements += n
        html = new_html

    new_html, n = BROKER_TAG_LIGHT_BAD.subn(
        r'\1Health Insurance Specialists\2', html
    )
    if n:
        file_log.append(f"  broker-card-light-tag fixed: {n}")
        file_replacements += n
        html = new_html

    # ── Broker card description fix ────────────────────────────────────────────
    new_html, n = BROKER_DESC_BAD.subn(BROKER_DESC_REPLACEMENT_DARK, html)
    if n:
        file_log.append(f"  broker card description (Sanitas ref) fixed: {n}")
        file_replacements += n
        html = new_html

    # ── Insurer section replacement ────────────────────────────────────────────
    new_html, n = INSURER_SECTION_RE.subn(INSURER_SECTION_REPLACEMENT, html)
    if n:
        file_log.append(f"  insurer comparison section replaced: {n}")
        file_replacements += n
        html = new_html

    # ── "Our recommendation: [brand]" fix ─────────────────────────────────────
    new_html, n = OUR_REC_RE.subn(OUR_REC_REPLACEMENT, html)
    if n:
        file_log.append(f"  'Our recommendation' paragraph fixed: {n}")
        file_replacements += n
        html = new_html

    # ── Insurer choice list item fix ───────────────────────────────────────────
    new_html, n = INSURER_CHOICE_RE.subn(INSURER_CHOICE_REPLACEMENT, html)
    if n:
        file_log.append(f"  insurer-choice list item fixed: {n}")
        file_replacements += n
        html = new_html

    # ── Brand list replacement ─────────────────────────────────────────────────
    new_html, n = replace_brand_lists(html)
    if n:
        file_log.append(f"  brand lists replaced: {n}")
        file_replacements += n
        html = new_html

    # ── Solo brand replacement ─────────────────────────────────────────────────
    new_html, n = replace_solo_brands_in_body(html)
    if n:
        file_log.append(f"  solo brand mentions replaced: {n}")
        file_replacements += n
        html = new_html

    # ── Partner block injection (insurance-focused pages only) ─────────────────
    if fname in INSURANCE_FOCUSED_PAGES:
        already_has_partner = (
            "spanish-healthinsurance.com" in html or
            "247expatinsurance.com" in html
        )
        if not already_has_partner:
            new_html, n = INSERT_ANCHOR_RE.subn(
                PARTNER_BLOCK_HTML + r'\n\1', html, count=1
            )
            if n:
                file_log.append(f"  partner referral block injected")
                file_replacements += 1
                html = new_html

    # ── Write if changed ───────────────────────────────────────────────────────
    if html != original:
        with open(fpath, "w", encoding="utf-8") as fh:
            fh.write(html)
        total_files_changed += 1
        total_replacements += file_replacements
        entry = f"\nFILE: {fname}  [{file_replacements} change(s)]\n" + "\n".join(file_log)
        print(entry)
        logs.append(entry)

# ── Write log ─────────────────────────────────────────────────────────────────
with open(LOG_FILE, "w", encoding="utf-8") as fh:
    fh.write(
        f"MSV Insurance Fix Log\n"
        f"  Deleted: {total_deleted} file(s)\n"
        f"  Modified: {total_files_changed} file(s)\n"
        f"  Total replacements: {total_replacements}\n"
        + "=" * 70 + "\n"
    )
    fh.write("\n".join(logs))
    fh.write("\n")

print(
    f"\n✓ Done.\n"
    f"  Deleted: {total_deleted} files\n"
    f"  Modified: {total_files_changed} files ({total_replacements} replacements)\n"
    f"  Log: {LOG_FILE}"
)
