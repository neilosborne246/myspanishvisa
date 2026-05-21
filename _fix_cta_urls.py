#!/usr/bin/env python3
"""
MSV Part 3 — Fix CTA button and link URLs across all .html files.

Rules:
  Visa-type is determined by filename first, then page content.
  All placeholder action CTAs on a visa-specific page point to the
  relevant dashboard URL. Generic / contact CTAs → /contact-us.html.

Dashboard URLs:
  NLV (new)         → https://dashboard.platinumlegalspain.com/nlv
  DNV (new)         → https://dashboard.platinumlegalspain.com/dnv
  Student (new)     → https://dashboard.platinumlegalspain.com/student-visa
  NLV Renewal       → https://dashboard.platinumlegalspain.com/nlv-renewal
  DNV Renewal       → https://dashboard.platinumlegalspain.com/dnv-renewal
  General contact   → /contact-us.html

Placeholder URLs replaced:
  /book-consultation/  /book-a-consultation/  /book-consultation
  /eligibility-check/  /eligibility-check
  /get-help/           /get-help
  /contact/            /contact
  /start-application/  /apply/
  href="#" on action CTAs  (context-matched only)
  dashboard.platinumlegalspain.com/* generic placeholders

CTA action text triggers (these strings in the SAME <a> tag body mark
a link as an action CTA that should be replaced):
  Start My Application, Check My Eligibility, Book a Free Call,
  Book an Appointment, Speak to a Specialist, Get Started,
  Start Free Eligibility, Book Consultation, Book a Consultation,
  Get Expert Help, Apply Now, Start Application, Check Eligibility,
  Book Your Consultation, Start My NLV, Start My DNV, Start My Student,
  Get Started with, Take Free Eligibility
"""

import os
import re
import sys

# ── Config ────────────────────────────────────────────────────────────────────
FOLDER   = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(FOLDER, "_cta_fix_log.txt")

# ── Dashboard URLs ─────────────────────────────────────────────────────────────
DASH = {
    "nlv":             "https://dashboard.platinumlegalspain.com/nlv",
    "dnv":             "https://dashboard.platinumlegalspain.com/dnv",
    "student":         "https://dashboard.platinumlegalspain.com/student-visa",
    "nlv-renewal":     "https://dashboard.platinumlegalspain.com/nlv-renewal",
    "dnv-renewal":     "https://dashboard.platinumlegalspain.com/dnv-renewal",
    "general":         "/contact-us.html",
}

# ── Placeholder URL patterns (matched inside href="…") ────────────────────────
PLACEHOLDER_HREFS = [
    r"/book-a?-?consultation/?",
    r"/eligibility-check/?",
    r"/get-help/?",
    r"/contact/?",
    r"/start-application/?",
    r"/apply/?",
    r"#",   # bare hash — only replaced when anchor text is CTA-like
]

# Compile into a single alternation for href matching
PLACEHOLDER_RE = re.compile(
    r'href=["\'](' + "|".join(PLACEHOLDER_HREFS) + r')["\']',
    re.IGNORECASE,
)

# Also match dashboard placeholder paths that aren't real visa paths
DASH_PLACEHOLDER_RE = re.compile(
    r'href=["\']https?://dashboard\.platinumlegalspain\.com(?!/(?:nlv|dnv|student-visa|nlv-renewal|dnv-renewal))[^"\']*["\']',
    re.IGNORECASE,
)

# ── CTA action-text detection ─────────────────────────────────────────────────
CTA_TEXT_RE = re.compile(
    r"(Start\s+My\s+Application|Check\s+My\s+Eligibility|Book\s+a?\s*Free\s+Call|"
    r"Book\s+an?\s+Appointment|Speak\s+to\s+a\s+Specialist|Get\s+Started|"
    r"Start\s+Free\s+Eligibility|Book\s+Consultation|Book\s+a\s+Consultation|"
    r"Get\s+Expert\s+Help|Apply\s+Now|Start\s+Application|Check\s+Eligibility|"
    r"Book\s+Your\s+Consultation|Start\s+My\s+NLV|Start\s+My\s+DNV|"
    r"Start\s+My\s+Student|Get\s+Started\s+with|Take\s+Free\s+Eligibility|"
    r"Start\s+My\s+Application|Free\s+Consultation|Free\s+Eligibility\s+Check)",
    re.IGNORECASE,
)

# ── Visa-type classification ───────────────────────────────────────────────────

def classify_file(fname: str, content: str) -> str:
    """
    Return one of: nlv-renewal, dnv-renewal, nlv, dnv, student, general.
    Priority: filename → content signals.
    """
    stem = fname.lower().replace("-", " ").replace("_", " ")

    # Renewal first (more specific)
    if any(x in stem for x in ["nlv renewal", "nlv-renewal", "renew nlv",
                                 "nlv renew", "non lucrative renewal",
                                 "non-lucrative renewal"]):
        return "nlv-renewal"
    if any(x in stem for x in ["dnv renewal", "dnv-renewal", "renew dnv",
                                 "dnv renew", "digital nomad renewal",
                                 "nomad renewal"]):
        return "dnv-renewal"
    # Student renewal → still student (new application URL)
    if "student" in stem and ("renewal" in stem or "renew" in stem):
        return "student"

    # Specific visa types
    if any(x in stem for x in ["nlv", "non lucrative", "non-lucrative",
                                 "retire to spain", "retirement visa",
                                 "nlv pillar"]):
        return "nlv"
    if any(x in stem for x in ["dnv", "digital nomad", "nomad visa",
                                 "dnv pillar", "beckham law"]):
        return "dnv"
    if any(x in stem for x in ["student visa", "student-visa",
                                 "student pillar", "study in spain",
                                 "study spanish"]):
        return "student"

    # Fallback: scan content for strong signals
    content_lower = content.lower()
    nlv_hits = content_lower.count("non-lucrative") + content_lower.count("non lucrative")
    dnv_hits  = content_lower.count("digital nomad")
    stu_hits  = content_lower.count("student visa")

    if nlv_hits == 0 and dnv_hits == 0 and stu_hits == 0:
        return "general"

    best = max(
        ("nlv", nlv_hits), ("dnv", dnv_hits), ("student", stu_hits),
        key=lambda x: x[1],
    )
    return best[0]


# ── Per-anchor replacement ─────────────────────────────────────────────────────

def replace_anchor_hrefs(html: str, visa_type: str) -> tuple[str, list]:
    """
    Find all <a …> … </a> blocks. For each:
      - If href is a placeholder AND anchor text is CTA-like → replace href.
      - If href is a generic dashboard URL → replace with visa_type dashboard URL.
    Returns (updated_html, list_of_replacement_messages).
    """
    replacements = []
    target_url = DASH.get(visa_type, DASH["general"])

    # Match entire anchor tags (non-greedy, handles multiline)
    ANCHOR_RE = re.compile(r'<a\b([^>]*)>(.*?)</a>', re.IGNORECASE | re.DOTALL)

    def replace_anchor(m):
        attrs   = m.group(1)
        body    = m.group(2)
        original = m.group(0)

        # Check if href is a placeholder
        href_m = re.search(r'href=["\']([^"\']*)["\']', attrs, re.IGNORECASE)
        if not href_m:
            return original

        href_val = href_m.group(1).strip()

        # Is it a bare '#' or placeholder path?
        is_placeholder = bool(re.fullmatch(
            r'#|/book-a?-?consultation/?|/eligibility-check/?|/get-help/?|'
            r'/contact/?|/start-application/?|/apply/?',
            href_val, re.IGNORECASE,
        ))

        # Is it a generic/broken dashboard URL?
        is_dash_placeholder = bool(re.match(
            r'https?://dashboard\.platinumlegalspain\.com(?!/(?:nlv|dnv|student-visa|nlv-renewal|dnv-renewal))',
            href_val, re.IGNORECASE,
        ))

        if not (is_placeholder or is_dash_placeholder):
            return original

        # For bare '#', only replace if anchor text looks like a CTA
        if href_val == "#" and not CTA_TEXT_RE.search(body):
            return original

        # Perform replacement
        new_attrs = re.sub(
            r'href=["\'][^"\']*["\']',
            f'href="{target_url}"',
            attrs,
            count=1,
            flags=re.IGNORECASE,
        )
        new_tag = f'<a{new_attrs}>{body}</a>'
        replacements.append(
            f'  [{href_val}] → [{target_url}]  (text: {body[:60].strip()!r})'
        )
        return new_tag

    updated = ANCHOR_RE.sub(replace_anchor, html)
    return updated, replacements


# ── Main ──────────────────────────────────────────────────────────────────────
html_files = sorted(f for f in os.listdir(FOLDER) if f.lower().endswith(".html"))

all_logs = []
total_replacements = 0
files_changed = 0

for fname in html_files:
    # Skip utility/script files
    if fname.startswith("_"):
        continue

    fpath = os.path.join(FOLDER, fname)
    with open(fpath, "r", encoding="utf-8", errors="replace") as fh:
        original = fh.read()

    visa_type = classify_file(fname, original)
    updated, replacements = replace_anchor_hrefs(original, visa_type)

    if replacements:
        with open(fpath, "w", encoding="utf-8") as fh:
            fh.write(updated)
        n = len(replacements)
        total_replacements += n
        files_changed += 1
        log_entry = (
            f"\nFILE: {fname}  [visa_type={visa_type}, {n} replacement(s)]\n"
            + "\n".join(replacements)
        )
        print(log_entry)
        all_logs.append(log_entry)
    else:
        all_logs.append(f"NO CHANGE: {fname}  [visa_type={visa_type}]")

# ── Write log ─────────────────────────────────────────────────────────────────
with open(LOG_FILE, "w", encoding="utf-8") as fh:
    fh.write(
        f"MSV CTA Fix Log — {total_replacements} URL replacements "
        f"across {files_changed} files\n"
        + "=" * 70 + "\n"
    )
    fh.write("\n".join(all_logs))
    fh.write("\n")

print(
    f"\n✓ Done — {total_replacements} CTA URLs fixed across "
    f"{files_changed} files.\n  Log: {LOG_FILE}"
)
