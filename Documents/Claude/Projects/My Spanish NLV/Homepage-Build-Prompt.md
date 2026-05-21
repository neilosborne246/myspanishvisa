# Homepage Build Prompt — Reusable Template

Copy and paste everything below into a new conversation to build a homepage for a different brand in the same ecosystem.

---

## PROMPT STARTS HERE

I need you to build a single-page homepage (index.html) for a new website. I'll give you the brand details below. Use the same architecture, structure, and approach as the myspanishnlv.com homepage we built previously. Here's exactly what that means:

### Page structure (follow this order exactly)

1. **Fixed glass nav** — logo left, links right (What Is It, Requirements, Pricing, Process, FAQ, CTA button). On mobile: hamburger that opens a full-screen overlay menu (the overlay must be a separate div OUTSIDE the nav element to avoid stacking context issues from backdrop-filter). Include a visible ✕ close button inside the overlay itself.

2. **Mobile sticky bottom bar** — two buttons fixed to bottom of screen: primary CTA (red) + "Contact Us" (outlined, mailto link). Only visible on mobile.

3. **Hero section** — label line (e.g. "Spain Digital Nomad Visa · 2026"), big H1 headline with an italic emphasis line, sub-paragraph explaining the visa/product and target audience, two buttons (primary CTA + "See pricing"), and a stats row (4 key numbers). Giant watermark text behind (e.g. "DNV" or "NLV").

4. **Nationality strip** — horizontal bar listing target nationalities (USA, UK, Canada, Australia, etc.)

5. **"What Is It" section** (dark background) — section label, H2 title, body paragraph explaining the visa, plus a "Quick Facts" info card with key data points in a grid.

6. **Requirements grid** (light background) — 6 cards, each with an emoji icon, title, and description.

7. **Step-by-step process** (dark background) — numbered steps (typically 5), each with a title and description.

8. **Pricing section** (light background) — cards showing staged payment structure. One card can be "featured" with a badge.

9. **Highlight section** — a big visual callout for the most important thing the audience needs to know (e.g. health insurance for NLV, Beckham Law for DNV). Big number or stat, explanation, and CTA.

10. **FAQ** — details/summary accordion pattern, typically 7 questions.

11. **Red CTA banner** — full-width red background, headline + CTA button.

12. **Cross-sell links** — "You May Also Need" section with cards linking to sibling sites.

13. **Footer** — logo, nav links, email address (yellow), copyright with "Legal services provided by Platinum Legal Spain."

### Technical requirements

- **Single self-contained HTML file** — all CSS inline in `<style>`, JS inline in `<script>`.
- **CSS custom properties** for brand tokens (colors, fonts, radii, spacing).
- **Brand palette**: navy (#0c1930), navy-mid (#1a3a5c), red (#be0011), red-deep (#8c000d), cream (#f8f7f4), yellow (#facf39). Adjust if the new brand needs different colors.
- **Fonts**: Bricolage Grotesque (display) + Inter (body), loaded from Google Fonts.
- **JSON-LD structured data** @graph including: Organization, WebSite, WebPage, Service with Offer(s), BreadcrumbList, FAQPage. Link the parent organization to Platinum Legal Spain.
- **Full SEO meta**: title, description, keywords, canonical, hreflang, Open Graph, Twitter Card.
- **Accessibility**: skip link, aria-labelledby on sections, role="list" where appropriate, prefers-reduced-motion media query.
- **Responsive**: mobile-first grid collapses, nav becomes hamburger at 900px.
- Dashboard links go to: `dashboard.platinumlegalspain.com/[product-slug]`
- Contact email: `hola@myspanishvisa.com`

### What I need to provide you

Fill in these details for the new brand:

```
BRAND NAME: [e.g. My Spanish DNV]
DOMAIN: [e.g. myspanishdnv.com]
PRODUCT: [e.g. Spain Digital Nomad Visa]
PRODUCT SLUG: [e.g. /dnv for dashboard links]
RENEWAL SLUG: [e.g. /dnv-renewal]
WATERMARK TEXT: [e.g. DNV]

TARGET AUDIENCE: [who is this for?]

HERO HEADLINE: [line 1]
HERO EMPHASIS: [italic line 2]
HERO SUB-TEXT: [1-2 sentence description]

STATS (4 items):
- [number] — [label]
- [number] — [label]
- [number] — [label]
- [number] — [label]

PRICING:
- Main product: [name, total price, payment stages]
- Renewal (if applicable): [name, total price, payment stages]

QUICK FACTS (8-10 key data points):
- [fact]: [value]

REQUIREMENTS (6 items):
- [emoji] [title]: [description]

PROCESS STEPS (5 items):
1. [title]: [description]

HIGHLIGHT SECTION:
- Big stat/number: [e.g. "#1" or "24%" or "€0"]
- Caption: [what it means]
- Explanation: [paragraph]
- CTA link: [url and text]

FAQ (7 questions):
1. Q: ... A: ...

CROSS-SELL SITES (2-3):
- [label], [title], [description], [url]

NATIONALITIES: [list target countries]

Any color changes from the default navy/red/cream/yellow palette? [yes/no, details]
```

Once you have all that, build the full index.html following the structure above. Make it production-ready.

---

## PROMPT ENDS HERE
