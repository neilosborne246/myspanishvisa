# Full Website Project Prompt — Reusable Template

Copy everything below into a new conversation to build a complete website project for a different brand from scratch.

---

## PROMPT STARTS HERE

I'm building a single-topic website focused on one specific Spanish visa/immigration product. The site is part of a network of whitelabel sites all powered by Platinum Legal Spain. The dashboard for applications is at dashboard.platinumlegalspain.com.

I need you to do everything we'd need to launch this site, in this order:

---

### PHASE 1: Master Keyword List (save as .docx)

Take all the keyword data I give you and organise it into a single master keyword list document (.docx). Cluster the keywords into logical groups such as:

- Core / head terms
- High-intent / commercial
- Platform / branded
- Requirements
- Health insurance
- Process / how-to
- Cost / pricing
- Renewal
- Conversion / application
- Family / dependents
- By nationality / consulate
- Questions (who/what/when/how)
- Problems / rejection / refused
- Demographics (retirees, families, digital nomads, etc.)
- Tax / financial
- Comparison (vs other visas)

For each keyword include the cluster name, the keyword itself, and a brief note on intent (informational, commercial, navigational, transactional). Don't invent search volumes — just organise what I give you.

---

### PHASE 2: SEO Site Strategy & Sitemap (save as .docx)

Create a full site strategy document following this exact structure:

1. **Positioning** — what the site is, who it's for, how it fits in the Platinum Legal Spain ecosystem, what makes it different from competitors (Balcells, Lexidy, Immigration Spain, etc.)

2. **Sitemap with silo architecture** — full URL map organised into cluster hubs. Each hub gets a pillar page and supporting pages. Example structure:
   - / (homepage)
   - /requirements/ (hub) → /requirements/income/, /requirements/health-insurance/, /requirements/criminal-record/, etc.
   - /application-process/ (hub) → /application-process/documents/, /application-process/consulate-appointment/, etc.
   - /health-insurance/ (hub)
   - /renewal/ (hub)
   - /pricing/ and /services/
   - /by-country/ (hub) → /by-country/usa/, /by-country/uk/, etc.
   - /tax/ (hub if relevant)
   - /compare/ → vs other visa types
   - /for/ → /for/retirees/, /for/families/, etc.
   - /blog/
   - /about/, /legal/

3. **Internal linking strategy** — hub-and-spoke model, how pillar pages link to clusters and back, cross-linking between related hubs.

4. **Yoast / Rank Math SEO setup** — recommended settings for each page type.

5. **JSON-LD schema strategy** — which schema types go on which pages (Organization, WebSite, WebPage, Service, Offer, BreadcrumbList, FAQPage, LegalService, etc.)

6. **90-day build roadmap** — priority table for every page, scored by:
   - T (Traffic potential, 1-5)
   - C (Commercial intent, 1-5)
   - D (Difficulty, 1-5)
   - Score = (T × C) / D
   
   Phased into:
   - Weeks 1-2: Foundation (homepage, pricing, services, core pillar pages)
   - Weeks 3-6: Backbone (requirements cluster, process cluster, insurance cluster)
   - Weeks 7-10: Country pages + demographic pages
   - Weeks 11-12: Niche / comparison / rejection pages
   - Weeks 9-12+: Blog content

7. **Search volume notes** — honest assessment of keyword competitiveness and what's needed to rank.

8. **Technical checklist** — Core Web Vitals, canonical URLs, hreflang, OG/Twitter meta, sitemap.xml, robots.txt.

9. **Next actions** — what to build first, what to ask next.

---

### PHASE 3: Homepage (index.html)

Build a single self-contained HTML file (all CSS in `<style>`, JS in `<script>`) with this exact structure:

1. **Fixed glass nav** — logo left, links right. Mobile: hamburger opens a full-screen overlay menu. The overlay MUST be a separate `<div>` outside the `<nav>` element (backdrop-filter on nav creates a stacking context that traps child z-index). Include a visible ✕ close button inside the overlay. Also lock body scroll when menu is open.

2. **Mobile sticky bottom bar** — fixed to bottom, two buttons: primary CTA (red) + "Contact Us" (outlined, mailto). Only visible at ≤900px.

3. **Hero** — label line, big H1 with italic emphasis line, descriptive sub-paragraph covering all target audiences, two buttons (CTA + "See pricing"), 4-stat row, giant watermark text behind.

4. **Nationality strip** — horizontal bar listing target nationalities.

5. **"What Is It" dark section** — explanation + Quick Facts info card with key data points.

6. **Requirements grid** (light) — 6 cards with emoji, title, description.

7. **Process steps** (dark) — 5 numbered steps.

8. **Pricing** (light) — cards showing staged payment breakdown. Featured card gets a badge.

9. **Highlight section** — big visual callout for the single most important thing the audience needs to know. Big number/stat, explanation, CTA.

10. **FAQ** — 7 questions, details/summary accordion.

11. **Red CTA banner** — full-width, headline + button.

12. **Cross-sell links** — "You May Also Need" cards linking to sibling sites in the network.

13. **Footer** — logo, nav links, contact email in yellow, copyright line crediting Platinum Legal Spain.

**Technical spec:**
- CSS custom properties for brand tokens
- Default palette: navy (#0c1930), navy-mid (#1a3a5c), red (#be0011), red-deep (#8c000d), cream (#f8f7f4), yellow (#facf39)
- Fonts: Bricolage Grotesque (display) + Inter (body) from Google Fonts
- JSON-LD @graph: Organization, WebSite, WebPage, Service with Offer(s), BreadcrumbList, FAQPage
- Full SEO meta: title, description, keywords, canonical, hreflang, OG, Twitter Card
- Accessibility: skip link, aria-labelledby, prefers-reduced-motion
- Responsive at 900px breakpoint

---

### FILL IN FOR YOUR BRAND

```
BRAND NAME: [e.g. My Spanish NIE]
DOMAIN: [e.g. myspanishnie.com]
PRODUCT: [e.g. Spain NIE Number]
PRODUCT SLUG: [e.g. /nie — used for dashboard.platinumlegalspain.com/nie]
RENEWAL SLUG: [if applicable]
WATERMARK TEXT: [e.g. NIE]
CONTACT EMAIL: [e.g. hola@myspanishvisa.com]

TARGET AUDIENCE: [who is this product for — be specific about demographics, life situations, motivations]

PRICING:
- Main product: [name] — [total] — [staged payments breakdown]
- Second product (if any): [name] — [total] — [staged payments breakdown]
- Family discount? [yes/no]
- What's included? [e.g. translations, dashboard access, lawyer support]

COMPETITORS: [who are the main organic competitors for this topic]

CROSS-SELL SITES (sibling brands in the network):
- [url] — [label] — [one-line description]
- [url] — [label] — [one-line description]
- [url] — [label] — [one-line description]

NATIONALITIES: [target countries, e.g. USA, UK, Canada, Australia, Ireland, South Africa, New Zealand]

HERO HEADLINE: [line 1, e.g. "Get Your NIE Number."]
HERO EMPHASIS: [italic line 2, e.g. "Sorted from home."]
HERO SUB-TEXT: [1-2 sentences explaining who it's for and what you do]

STATS (4 key numbers for the hero):
- [number] — [label]
- [number] — [label]
- [number] — [label]
- [number] — [label]

QUICK FACTS (8-10 data points):
- [label]: [value]

REQUIREMENTS (6 items):
- [emoji] [title]: [description]

PROCESS STEPS (5 items):
1. [title]: [description]

HIGHLIGHT SECTION (the single most important thing):
- Big stat: [e.g. "#1", "24%", "€0"]
- Caption: [what it means]
- Body: [1-2 sentence explanation]
- CTA: [link url + button text]

FAQ (7 questions and answers):
1. Q: ... A: ...

COLOR CHANGES: [any changes from the default navy/red/cream/yellow palette? or keep the same]
```

---

### IMPORTANT NOTES

- The site is a whitelabel. Legal services are provided by Platinum Legal Spain but the branding is the domain name (e.g. "My Spanish NIE"). PLS is credited in the footer and schema, not plastered in headers.
- Dashboard links always go to dashboard.platinumlegalspain.com/[slug]
- All pricing uses staged payments (e.g. €X to start + €X before submission + €X on approval). Get the exact breakdown right — don't miss a payment stage.
- The keyword list and strategy docs should be saved as .docx files.
- The homepage is saved as index.html.
- Focus only on the one domain/product I specify. Don't expand scope to other domains unless I ask.

---

### KEYWORD DATA

[PASTE YOUR KEYWORD LISTS HERE — I'll organise them into clusters]

---

## PROMPT ENDS HERE
