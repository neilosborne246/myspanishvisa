#!/usr/bin/env python3
"""
Rebuild all My Spanish NLV blog pages with clean, consistent formatting.
Based on the My Spanish Student Visa blog template, adapted for NLV.

Usage:
    python3 rebuild_blogs.py [--test] [--file filename.html]

Options:
    --test      Process only a handful of files for verification
    --file X    Process a single specific file
"""

import os, re, glob, sys, html as html_module
from bs4 import BeautifulSoup

BLOG_DIR = "/sessions/cool-loving-galileo/mnt/My Spanish NLV/blog"

SKIP_FILES = {
    'BLOG-TEMPLATE-NLV.html', 'MASTER-TEMPLATE-V2.html', 'MASTER-TEMPLATE.html',
    'TEMPLATE-NLV-BLOG-POST.html', 'index.html'
}

COOKIEYES = '<script id="cookieyes" type="text/javascript" src="https://cdn-cookieyes.com/client_data/78271008c96df6c735efd415cdea6100/script.js"></script>'

CSS = """:root{--navy:#0c1930;--navy-mid:#1a3a5c;--red:#be0011;--yellow:#facf39;--cream:#f8f7f4;--white:#ffffff;--grey-100:#f0eff0;--grey-300:#c8c8cc;--grey-600:#6b6b72;--ff-display:'Bricolage Grotesque',sans-serif;--ff-body:'Inter',sans-serif;--r-sm:6px;--r-md:12px;--r-lg:20px;--r-pill:40px;--shadow-sm:0 2px 8px rgba(0,0,0,.08);--max-w:1140px;--nav-h:130px;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:var(--ff-body);background:var(--white);color:var(--navy);line-height:1.6;-webkit-font-smoothing:antialiased;padding-top:var(--nav-h);}
img{display:block;max-width:100%;}
a{color:inherit;text-decoration:none;}
/* NAV */
nav.site-nav{position:fixed;top:0;left:0;right:0;z-index:900;height:var(--nav-h);background:rgba(12,25,48,.95);backdrop-filter:blur(12px);border-bottom:1px solid rgba(255,255,255,.08);display:flex;align-items:center;justify-content:space-between;padding:1.25rem 4rem;}
.nav-logo{display:flex;align-items:center;text-decoration:none;flex-shrink:0;}
.nav-logo-img{height:108px;width:auto;display:block;}
.nav-links{display:flex;gap:2rem;list-style:none;align-items:center;}
.nav-links a{color:rgba(255,255,255,.82);text-decoration:none;font-size:.82rem;font-weight:400;letter-spacing:.06em;text-transform:uppercase;transition:color .2s;}
.nav-links a:hover{color:var(--yellow);}
.nav-cta{background:var(--red)!important;color:#fff!important;padding:.5rem 1.3rem!important;border-radius:var(--r-pill)!important;font-weight:600!important;letter-spacing:.04em!important;}
.nav-toggle{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:4px;background:none;border:none;}
.nav-toggle span{display:block;width:24px;height:2px;background:#fff;border-radius:2px;}
/* MOBILE MENU */
.mobile-menu{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:#0c1930;z-index:10000;flex-direction:column;align-items:center;padding-top:4.5rem;overflow-y:auto;}
.mobile-menu.open{display:flex;}
.mobile-menu-close{position:absolute;top:1.1rem;right:1.5rem;background:none;border:1px solid rgba(255,255,255,.3);color:#fff;font-size:1.3rem;width:44px;height:44px;display:flex;align-items:center;justify-content:center;border-radius:6px;cursor:pointer;}
.mobile-menu>a{display:block;width:100%;text-align:center;padding:1.3rem 2rem;color:#fff;text-decoration:none;font-size:1.15rem;font-weight:400;letter-spacing:.08em;text-transform:uppercase;border-bottom:1px solid rgba(255,255,255,.1);}
.mobile-menu>a:first-of-type{border-top:1px solid rgba(255,255,255,.1);}
.mobile-menu>a:hover{background:rgba(255,255,255,.05);}
.mobile-menu-bottom{width:100%;padding:1.5rem 2rem 2rem;display:flex;flex-direction:column;gap:.75rem;margin-top:auto;}
.mm-label{font-size:.65rem;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.45);text-align:center;margin-top:.5rem;}
.mobile-menu-pill{display:block;width:100%;text-align:center;padding:.85rem 1.5rem;border-radius:var(--r-pill);font-size:.9rem;font-weight:600;text-decoration:none;letter-spacing:.04em;border:none;transition:background .2s;}
.pill-red{background:var(--red);color:#fff;}
.pill-outline{background:transparent;color:#fff;border:1px solid rgba(255,255,255,.25);}
.pill-outline:hover{border-color:var(--yellow);color:var(--yellow);}
.pill-yellow{background:var(--yellow);color:var(--navy);}
/* MOBILE BAR */
.mobile-bar{display:none;position:fixed;bottom:0;left:0;right:0;z-index:100;background:var(--navy);border-top:1px solid rgba(255,255,255,.1);padding:.75rem 1rem;gap:.5rem;}
.mobile-bar a{flex:1;text-align:center;padding:.75rem .5rem;border-radius:var(--r-pill);font-size:.85rem;font-weight:600;text-decoration:none;}
.bar-apply{background:var(--red);color:#fff;}
.bar-contact{background:transparent;border:1px solid var(--cream);color:var(--cream);}
/* HERO */
.page-hero{background:var(--navy);padding:3.5rem 4rem 5rem;position:relative;overflow:hidden;display:flex;flex-direction:column;justify-content:flex-start;}
.page-hero::before{content:'';position:absolute;top:-200px;right:-200px;width:700px;height:700px;background:radial-gradient(circle,rgba(250,207,57,.07) 0%,transparent 70%);pointer-events:none;}
.page-hero-inner{max-width:800px;position:relative;}
.page-hero-badge{display:flex;align-items:center;gap:.75rem;background:transparent;border:none;padding:0;color:var(--yellow);font-size:.75rem;letter-spacing:.2em;text-transform:uppercase;font-weight:500;margin-bottom:1.5rem;}
.page-hero-badge::before{content:'';display:block;width:2rem;height:1px;background:var(--yellow);flex-shrink:0;}
.page-hero h1{font-family:var(--ff-display);font-size:clamp(2.2rem,5vw,3.8rem);font-weight:500;color:var(--white);line-height:1.15;margin-bottom:1.5rem;}
.page-hero h1 em{color:var(--yellow);font-style:normal;}
.page-hero p{font-size:1.1rem;color:rgba(255,255,255,.78);max-width:640px;margin:0 0 2.5rem;font-weight:300;}
.hero-actions{display:flex;gap:1rem;justify-content:flex-start;flex-wrap:wrap;}
.btn-primary{background:var(--red);color:#fff;padding:.85rem 2rem;border-radius:var(--r-pill);font-weight:700;font-size:1rem;transition:background .2s,transform .15s;display:inline-block;}
.btn-primary:hover{background:#9a000e;transform:translateY(-2px);}
.btn-outline{border:2px solid rgba(255,255,255,.35);color:#fff;padding:.85rem 2rem;border-radius:var(--r-pill);font-weight:600;font-size:1rem;display:inline-block;transition:border-color .2s;}
.btn-outline:hover{border-color:var(--yellow);}
/* BREADCRUMB (hidden) */
.breadcrumb{display:none;}
/* SECTIONS */
.section{padding:5rem 2rem;}
.section-inner{max-width:var(--max-w);margin:0 auto;}
.section--cream{background:var(--cream);}
.section--dark{background:var(--navy);color:#fff;}
/* BLOG GRID */
.blog-grid{display:grid;grid-template-columns:minmax(0,2fr) minmax(0,1fr);gap:3rem;align-items:start;}
.blog-body{max-width:760px;}
.blog-body h2{font-family:var(--ff-display);font-size:1.5rem;font-weight:700;margin:2.5rem 0 .75rem;color:var(--navy);}
.blog-body h3{font-family:var(--ff-display);font-size:1.1rem;font-weight:700;margin:1.75rem 0 .5rem;color:var(--navy);}
.blog-body h4{font-family:var(--ff-display);font-size:1rem;font-weight:700;margin:1.5rem 0 .4rem;color:var(--navy);}
.blog-body p{font-size:1rem;color:var(--grey-600);line-height:1.85;margin-bottom:1.1rem;}
.blog-body ul,.blog-body ol{margin-bottom:1.1rem;padding-left:1.6rem;}
.blog-body li{font-size:1rem;color:var(--grey-600);line-height:1.75;margin-bottom:.4rem;}
.blog-body strong{color:var(--navy);font-weight:600;}
.blog-body a{color:var(--red);text-decoration:underline;text-underline-offset:3px;}
.highlight{background:rgba(250,207,57,.12);border-left:4px solid var(--yellow);border-radius:0 8px 8px 0;padding:1rem 1.3rem;margin:1.8rem 0;font-size:.97rem;color:var(--navy);}
/* SIDEBAR */
.sidebar{position:sticky;top:calc(var(--nav-h) + 2rem);}
.sidebar-card{background:var(--cream);border-radius:var(--r-md);padding:1.5rem;margin-bottom:1.2rem;}
.sidebar-card h4{font-family:var(--ff-display);font-size:.95rem;font-weight:700;margin-bottom:.9rem;}
.sidebar-card ul{list-style:none;padding:0;display:flex;flex-direction:column;gap:.5rem;}
.sidebar-card ul li a{font-size:.88rem;color:var(--navy-mid);display:flex;align-items:center;gap:.4rem;}
.sidebar-card ul li a::before{content:"\\2192";color:var(--red);flex-shrink:0;}
.sidebar-cta{background:var(--red);border-radius:var(--r-md);padding:1.5rem;text-align:center;}
.sidebar-cta h4{font-family:var(--ff-display);font-size:1rem;font-weight:700;color:#fff;margin-bottom:.6rem;}
.sidebar-cta p{font-size:.85rem;color:rgba(255,255,255,.82);margin-bottom:1rem;line-height:1.6;}
.sidebar-cta a{display:block;background:#fff;color:var(--red);padding:.7rem 1.2rem;border-radius:var(--r-pill);font-weight:700;font-size:.9rem;}
/* FAQ */
.faq-list{display:flex;flex-direction:column;gap:1rem;margin-top:1.5rem;}
.faq-item{border:1px solid var(--grey-300);border-radius:var(--r-md);overflow:hidden;}
.faq-q{width:100%;background:#fff;border:none;cursor:pointer;padding:1.2rem 1.4rem;display:flex;justify-content:space-between;align-items:center;gap:1rem;text-align:left;}
.faq-q span{font-family:var(--ff-display);font-weight:600;font-size:.97rem;color:var(--navy);}
.faq-q svg{flex-shrink:0;transition:transform .3s;color:var(--red);}
.faq-item.open .faq-q svg{transform:rotate(45deg);}
.faq-a{display:none;padding:0 1.4rem 1.2rem;font-size:.93rem;color:var(--grey-600);line-height:1.7;}
.faq-item.open .faq-a{display:block;}
/* CTA BANNER */
.cta-banner{background:var(--red);border-radius:var(--r-lg);padding:3rem 2.5rem;text-align:center;}
.cta-banner h2{font-family:var(--ff-display);font-size:1.8rem;font-weight:700;color:#fff;margin-bottom:.75rem;}
.cta-banner p{color:rgba(255,255,255,.85);margin-bottom:1.8rem;font-size:1.05rem;}
.btn-white{background:#fff;color:var(--red);padding:.85rem 2.2rem;border-radius:var(--r-pill);font-weight:700;font-size:1rem;display:inline-block;transition:transform .15s;}
.btn-white:hover{transform:translateY(-2px);}
/* FOOTER */
footer{background:var(--navy);border-top:1px solid rgba(255,255,255,.08);padding:4rem 2rem 2rem;}
.footer-grid{max-width:var(--max-w);margin:0 auto;display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:3rem;}
.footer-col .footer-logo{margin-bottom:.75rem;}
.footer-logo-img{height:108px;width:auto;}
.footer-tagline{font-size:.88rem;color:#8a9bb0;line-height:1.6;margin-bottom:1.25rem;}
.footer-email a{color:var(--yellow);text-decoration:none;font-size:.9rem;font-weight:500;transition:color .2s;}
.footer-email a:hover{color:#fff;}
.footer-heading{font-size:.7rem;letter-spacing:.15em;text-transform:uppercase;color:var(--yellow);margin-bottom:1rem;font-weight:600;}
.footer-list{list-style:none;}
.footer-list li{margin-bottom:.6rem;}
.footer-list a{color:#8a9bb0;text-decoration:none;font-size:.85rem;transition:color .2s;}
.footer-list a:hover{color:#fff;}
.footer-visa-pills{display:flex;flex-direction:column;gap:.5rem;margin-bottom:1.5rem;}
.footer-pill{display:inline-block;background:var(--yellow);color:var(--navy);padding:.4rem 1rem;border-radius:var(--r-pill);font-size:.78rem;font-weight:600;text-decoration:none;transition:opacity .2s;white-space:nowrap;}
.footer-pill:hover{opacity:.82;}
.footer-pill--outline{background:transparent;color:var(--yellow);border:1px solid var(--yellow);}
.footer-pill--outline:hover{background:var(--yellow);color:var(--navy);}
.footer-bottom{max-width:var(--max-w);margin:2.5rem auto 0;padding-top:1.5rem;border-top:1px solid rgba(255,255,255,.08);display:flex;justify-content:space-between;align-items:center;gap:1.5rem;flex-wrap:wrap;}
.footer-copy{font-size:.78rem;color:#8a9bb0;}
.footer-legal{display:flex;gap:1.5rem;flex-wrap:wrap;}
.footer-legal a{color:#8a9bb0;text-decoration:none;font-size:.78rem;transition:color .2s;}
.footer-legal a:hover{color:#fff;}
/* RESPONSIVE */
@media(max-width:900px){
  nav.site-nav{padding:1rem 1.5rem;}
  .nav-logo-img{height:72px;}
  .nav-links{display:none!important;}
  .nav-toggle{display:flex!important;}
  .mobile-bar{display:flex!important;}
  .page-hero{padding:2.5rem 1.5rem 3.5rem;}
  .blog-grid{grid-template-columns:1fr;}
  .sidebar{position:static;}
  .footer-grid{grid-template-columns:1fr 1fr;gap:2rem;}
  .section{padding:3.5rem 1.5rem;}
  body{padding-top:100px;}
}
@media(max-width:700px){
  .footer-grid{grid-template-columns:1fr;}
  .footer-bottom{flex-direction:column;text-align:center;}
  .hero-actions{flex-direction:column;align-items:stretch;}
  .btn-primary,.btn-outline{width:100%;text-align:center;}
}"""

NAV_HTML = """<nav class="site-nav" aria-label="Site navigation">
  <a href="/" class="nav-logo" aria-label="My Spanish NLV — Home">
    <img src="/assets/logo-horizontal-light.png" alt="My Spanish NLV" class="nav-logo-img" />
  </a>
  <button class="nav-toggle" aria-label="Open menu" aria-expanded="false">
    <span></span><span></span><span></span>
  </button>
  <ul class="nav-links">
    <li><a href="/what-is-nlv/">What Is It</a></li>
    <li><a href="/requirements/">Requirements</a></li>
    <li><a href="/pricing/">Pricing</a></li>
    <li><a href="/application-process/">Process</a></li>
    <li><a href="/faq/">FAQ</a></li>
    <li><a href="/blog/">Guides</a></li>
    <li><a href="https://dashboard.platinumlegalspain.com/nlv" class="nav-cta" rel="noopener">Start Application</a></li>
  </ul>
</nav>"""

MOBILE_MENU_HTML = """<div class="mobile-menu" id="mobileMenu" aria-label="Navigation menu">
  <button class="mobile-menu-close" id="mobileMenuClose" aria-label="Close menu">&#x2715;</button>
  <a href="/what-is-nlv/">What Is It</a>
  <a href="/requirements/">Requirements</a>
  <a href="/pricing/">Pricing</a>
  <a href="/application-process/">Process</a>
  <a href="/faq/">FAQ</a>
  <a href="/blog/">Guides</a>
  <a href="/contact/">Contact</a>
  <div class="mobile-menu-bottom">
    <a href="https://dashboard.platinumlegalspain.com/nlv" class="mobile-menu-pill pill-red" rel="noopener">Start Application &#x2192;</a>
    <a href="mailto:hola@myspanishvisa.com" class="mobile-menu-pill pill-outline">Email Us</a>
    <p class="mm-label">Other Visa Types</p>
    <a href="https://myspanishstudentvisa.com" class="mobile-menu-pill pill-yellow" rel="noopener">Student Visa</a>
    <a href="https://myspanishdnv.com" class="mobile-menu-pill pill-yellow" rel="noopener">Digital Nomad Visa</a>
    <a href="https://www.myspanishvisa.com" class="mobile-menu-pill pill-yellow" rel="noopener">All Spanish Visas</a>
  </div>
</div>"""

FOOTER_HTML = """<footer>
  <div class="footer-grid">
    <div class="footer-col">
      <div class="footer-logo">
        <img src="/assets/logo-horizontal-light.png" alt="My Spanish NLV" class="footer-logo-img" />
      </div>
      <p class="footer-tagline">Spain&#x27;s Non-Lucrative Visa &mdash; apply online with our immigration specialists at Platinum Legal Spain.</p>
      <p class="footer-email"><a href="mailto:hola@myspanishvisa.com">hola@myspanishvisa.com</a></p>
    </div>
    <div class="footer-col">
      <p class="footer-heading">NLV Guide</p>
      <ul class="footer-list">
        <li><a href="/what-is-nlv/">What Is the NLV</a></li>
        <li><a href="/requirements/">Requirements</a></li>
        <li><a href="/pricing/">Pricing</a></li>
        <li><a href="/application-process/">Process</a></li>
        <li><a href="/faq/">FAQ</a></li>
        <li><a href="/renewal/">Renew Your NLV</a></li>
        <li><a href="/contact/">Contact Us</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <p class="footer-heading">Other Visa Types</p>
      <div class="footer-visa-pills">
        <a href="https://myspanishstudentvisa.com" class="footer-pill" rel="noopener">Student Visa &middot; My Spanish</a>
        <a href="https://myspanishdnv.com" class="footer-pill" rel="noopener">Digital Nomad Visa &middot; My Spanish DNV</a>
        <a href="https://www.myspanishvisa.com" class="footer-pill footer-pill--outline" rel="noopener">All other visas &middot; My Spanish Visa</a>
      </div>
      <p class="footer-heading" style="margin-top:1.5rem;">Services</p>
      <ul class="footer-list">
        <li><a href="https://spanish-healthinsurance.com" rel="noopener">Spanish Health Insurance</a></li>
        <li><a href="https://247expatinsurance.com" rel="noopener">247 Expat Insurance</a></li>
        <li><a href="https://dashboard.platinumlegalspain.com/nlv" rel="noopener">Start Application</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <p class="footer-heading">Company</p>
      <ul class="footer-list">
        <li><a href="https://platinumlegalspain.com" rel="noopener">Platinum Legal Spain</a></li>
        <li><a href="/about/">About Us</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p class="footer-copy">&#x00A9; 2026 My Spanish. Operated by Retail Consulting UK Ltd (Company No. 06711242). Legal services delivered in partnership with Platinum Legal Spain.</p>
    <div class="footer-legal">
      <a href="/legal/legal-statement/">Legal Statement</a>
      <a href="/legal/terms-and-conditions/">Terms and Conditions</a>
      <a href="/legal/privacy-policy/">Privacy Policy</a>
      <a href="/legal/cookies-policy/">Cookies Policy</a>
      <a href="/legal/refund-policy/">Refund Policy</a>
    </div>
  </div>
</footer>"""

MOBILE_BAR_HTML = """<div class="mobile-bar">
  <a href="https://dashboard.platinumlegalspain.com/nlv" class="bar-apply">Start Application &#x2192;</a>
  <a href="mailto:hola@myspanishvisa.com" class="bar-contact">Contact Us</a>
</div>"""

JS_HTML = """<script>
const _toggle = document.querySelector('.nav-toggle');
const _menu = document.getElementById('mobileMenu');
const _close = document.getElementById('mobileMenuClose');
function _openMenu(){_menu.classList.add('open');_toggle.setAttribute('aria-expanded','true');document.body.style.overflow='hidden';}
function _closeMenu(){_menu.classList.remove('open');_toggle.setAttribute('aria-expanded','false');document.body.style.overflow='';}
if(_toggle&&_menu&&_close){
  _toggle.addEventListener('click',()=>_menu.classList.contains('open')?_closeMenu():_openMenu());
  _close.addEventListener('click',_closeMenu);
  _menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',_closeMenu));
}
document.querySelectorAll('.faq-q').forEach(q=>{
  q.addEventListener('click',()=>{
    const item=q.closest('.faq-item');
    const open=item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(i=>{i.classList.remove('open');i.querySelector('.faq-q').setAttribute('aria-expanded','false');});
    if(!open){item.classList.add('open');q.setAttribute('aria-expanded','true');}
  });
});
</script>"""

SIDEBAR_HTML = """<aside class="sidebar">
  <div class="sidebar-card">
    <h4>NLV Guides</h4>
    <ul>
      <li><a href="/requirements/income-requirements/">Income Requirements</a></li>
      <li><a href="/requirements/health-insurance-requirement/">Health Insurance</a></li>
      <li><a href="/application-process/step-by-step-guide/">Step-by-Step Guide</a></li>
      <li><a href="/renewal/how-to-renew-nlv/">How to Renew Your NLV</a></li>
      <li><a href="/blog/">All NLV Guides</a></li>
    </ul>
  </div>
  <div class="sidebar-card">
    <h4>Quick Links</h4>
    <ul>
      <li><a href="/requirements/">Requirements</a></li>
      <li><a href="/pricing/">Pricing &amp; Services</a></li>
      <li><a href="/faq/">FAQ</a></li>
      <li><a href="/renewal/">Renewal Guide</a></li>
    </ul>
  </div>
  <div class="sidebar-cta">
    <h4>Ready to Apply?</h4>
    <p>Our immigration specialists handle your full NLV application end to end.</p>
    <a href="https://dashboard.platinumlegalspain.com/nlv">Start Your Application</a>
  </div>
</aside>"""

FAQ_SVG = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>'


def extract_faq_items(soup):
    """Find all .faq-item elements in the document and rebuild them cleanly."""
    faq_items = soup.find_all(class_='faq-item')
    if not faq_items:
        return ""
    seen_questions = set()
    result = []
    for item in faq_items:
        q_btn = item.find(class_='faq-q')
        a_div = item.find(class_='faq-a')
        if not (q_btn and a_div):
            continue
        q_span = q_btn.find('span')
        q_text = (q_span.get_text(strip=True) if q_span else q_btn.get_text(strip=True))
        if q_text in seen_questions:
            continue
        seen_questions.add(q_text)
        a_inner = a_div.decode_contents().strip()
        result.append(
            f'<div class="faq-item">'
            f'<button class="faq-q" aria-expanded="false">'
            f'<span>{html_module.escape(q_text)}</span>{FAQ_SVG}'
            f'</button>'
            f'<div class="faq-a">{a_inner}</div>'
            f'</div>'
        )
    return '\n'.join(result)


def clean_article(article_el):
    """
    Extract and clean the article content:
    1. Unwrap <section class="content-section*"> wrappers
    2. Unwrap <div class="section-body"> wrappers
    3. Remove <div class="internal-links"> blocks
    4. Remove section-title CSS class from headings
    5. Convert raw markdown ## / ### headings in text nodes
    6. Deduplicate repeated paragraphs/headings
    7. Remove FAQ list (rendered separately)
    8. Remove duplicate "Frequently Asked Questions" headings
    """
    if not article_el:
        return ""

    # Work on a string copy so we don't mutate original
    raw = str(article_el)

    # Convert markdown headings that appear as bare text
    # Match lines starting with ## or ### (may be in TextNode or inside <p>)
    raw = re.sub(r'(?m)^####\s+(.+?)$', r'<h4>\1</h4>', raw)
    raw = re.sub(r'(?m)^###\s+(.+?)$',  r'<h3>\1</h3>', raw)
    raw = re.sub(r'(?m)^##\s+(.+?)$',   r'<h2>\1</h2>', raw)
    raw = re.sub(r'(?m)^#\s+(.+?)$',    r'<h2>\1</h2>', raw)  # lone # becomes h2

    soup = BeautifulSoup(raw, 'html.parser')

    # Remove internal-links divs
    for div in soup.find_all('div', class_='internal-links'):
        div.decompose()

    # Remove FAQ list blocks from article body
    for fl in soup.find_all(class_='faq-list'):
        fl.decompose()
    for fi in soup.find_all(class_='faq-item'):
        fi.decompose()

    # Unwrap content-section sections
    for section in soup.find_all('section'):
        section.unwrap()

    # Unwrap section-body divs
    for div in soup.find_all('div', class_='section-body'):
        div.unwrap()

    # Strip section-title class from headings (keep heading, remove class)
    for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5']):
        classes = h.get('class', [])
        if 'section-title' in classes:
            h.attrs.pop('class', None)

    # Remove H1 from article body (already in hero)
    for h1 in soup.find_all('h1'):
        h1.decompose()

    # Remove "Frequently Asked Questions" headings from article body
    for heading in soup.find_all(['h2', 'h3']):
        if re.search(r'frequently asked', heading.get_text(), re.I):
            heading.decompose()

    # Deduplicate: remove second+ occurrences of identical paragraphs/headings
    seen_texts = {}
    for el in soup.find_all(['p', 'h2', 'h3', 'h4', 'li']):
        text = el.get_text(strip=True)
        if len(text) < 40:
            continue  # too short to bother deduplicating
        if text in seen_texts:
            el.decompose()
        else:
            seen_texts[text] = True

    # Get content from inside <article> tag (the soup wraps in <article>)
    article_out = soup.find('article')
    if article_out:
        return article_out.decode_contents().strip()
    return soup.decode_contents().strip()


def build_page(title, description, badge, h1_text, slug, article_content, faq_html):
    canonical = f"https://myspanishnlv.com/blog/{slug}/"

    # Clean title — strip ALL trailing "| My Spanish NLV" occurrences (handles doubled-up titles)
    clean_title = re.sub(r'(\s*\|\s*My Spanish NLV)+\s*$', '', title, flags=re.I).strip()
    if not clean_title or clean_title.lower() in ('my spanish nlv', ''):
        clean_title = re.sub(r'(\s*\|\s*My Spanish NLV)+\s*$', '', h1_text, flags=re.I).strip()
    page_title = f"{clean_title} | My Spanish NLV"

    # Clean H1 — strip all trailing "| My Spanish NLV" occurrences
    clean_h1 = re.sub(r'(\s*\|\s*My Spanish NLV)+\s*$', '', h1_text, flags=re.I).strip()

    faq_section = ""
    if faq_html:
        faq_section = f'<h2>Frequently Asked Questions</h2>\n<div class="faq-list">\n{faq_html}\n</div>'

    esc_title  = html_module.escape(page_title)
    esc_clean  = html_module.escape(clean_title)
    esc_desc   = html_module.escape(description)
    esc_badge  = html_module.escape(badge)
    # JSON-safe versions (escape backslashes and double-quotes for inline JSON)
    clean_title_js = clean_title.replace('\\', '\\\\').replace('"', '\\"')
    desc_js        = description.replace('\\', '\\\\').replace('"', '\\"')

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{esc_title}</title>
<meta name="description" content="{esc_desc}" />
<meta name="author" content="My Spanish NLV / Platinum Legal Spain" />
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1" />
<link rel="canonical" href="{canonical}" />
<link rel="alternate" hreflang="en" href="{canonical}" />
<link rel="alternate" hreflang="x-default" href="{canonical}" />
<meta property="og:type" content="article" />
<meta property="og:site_name" content="My Spanish NLV" />
<meta property="og:url" content="{canonical}" />
<meta property="og:title" content="{esc_clean}" />
<meta property="og:description" content="{esc_desc}" />
<meta property="og:image" content="https://myspanishnlv.com/assets/og-home.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:locale" content="en_GB" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{esc_clean}" />
<meta name="twitter:description" content="{esc_desc}" />
<meta name="twitter:image" content="https://myspanishnlv.com/assets/og-home.jpg" />
<link rel="icon" type="image/png" sizes="32x32" href="/assets/logo-square-dark.png" />
<link rel="apple-touch-icon" sizes="180x180" href="/assets/logo-square-dark.png" />
<link rel="manifest" href="/site.webmanifest" />
<meta name="theme-color" content="#0c1930" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,500;12..96,600;12..96,700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
<script type="application/ld+json">
{{"@context":"https://schema.org","@graph":[
  {{"@type":"Organization","@id":"https://myspanishnlv.com/#organization","name":"My Spanish NLV","url":"https://myspanishnlv.com/","logo":{{"@type":"ImageObject","url":"https://myspanishnlv.com/assets/logo.png","width":512,"height":512}},"parentOrganization":{{"@type":"LegalService","name":"Platinum Legal Spain","url":"https://platinumlegalspain.com"}}}},
  {{"@type":"BlogPosting","headline":"{clean_title_js}","description":"{desc_js}","url":"{canonical}","datePublished":"2026-04-27","dateModified":"2026-04-27","author":{{"@type":"Organization","name":"My Spanish NLV"}},"publisher":{{"@id":"https://myspanishnlv.com/#organization"}}}},
  {{"@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://myspanishnlv.com/"}},{{"@type":"ListItem","position":2,"name":"Blog","item":"https://myspanishnlv.com/blog/"}},{{"@type":"ListItem","position":3,"name":"{clean_title_js}","item":"{canonical}"}}]}}
]}}
</script>
<style>{CSS}</style>
{COOKIEYES}
</head>
<body>
{NAV_HTML}
{MOBILE_MENU_HTML}
<main>
<section class="page-hero">
  <div class="page-hero-inner">
    <span class="page-hero-badge">{esc_badge}</span>
    <h1>{clean_h1}</h1>
    <div class="hero-actions">
      <a class="btn-primary" href="https://dashboard.platinumlegalspain.com/nlv" rel="noopener">Start Your Application</a>
      <a class="btn-outline" href="/blog/">&#x2190; All Guides</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-inner">
    <div class="blog-grid">
      <article class="blog-body">
        {article_content}
        {faq_section}
        <div style="margin-top:2.5rem;padding:1.5rem;background:var(--cream);border-radius:var(--r-md);">
          <p style="font-size:.9rem;color:var(--grey-600);"><strong>Need expert help with your Spain NLV?</strong> Our immigration specialists at <a href="https://dashboard.platinumlegalspain.com/nlv">My Spanish NLV</a> handle your full application end to end. <a href="/pricing/">See our pricing</a> or <a href="https://dashboard.platinumlegalspain.com/nlv">start your application today</a>.</p>
        </div>
      </article>
      {SIDEBAR_HTML}
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="section-inner">
    <div class="cta-banner">
      <h2>Ready to get started?</h2>
      <p>Take our free eligibility quiz, book a free call, or dive straight in. Our qualified immigration specialists handle your full NLV application end to end.</p>
      <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-top:0.5rem;">
        <a class="btn-white" href="https://dashboard.platinumlegalspain.com/nlv" rel="noopener">Free Eligibility Quiz &#x2192;</a>
        <a style="display:inline-flex;align-items:center;background:transparent;color:#fff;padding:.85rem 2rem;border-radius:40px;font-weight:600;font-size:1rem;text-decoration:none;border:2px solid rgba(255,255,255,.5);" href="https://dashboard.platinumlegalspain.com/nlv" rel="noopener">Book a Free Call</a>
      </div>
      <p style="margin-top:1.25rem;font-size:.88rem;opacity:.75;">Already have an account? <a href="https://dashboard.platinumlegalspain.com" style="color:#fff;font-weight:600;text-decoration:underline;" rel="noopener">Log in to your dashboard 24/7 &#x2192;</a></p>
    </div>
  </div>
</section>
</main>
{FOOTER_HTML}
{MOBILE_BAR_HTML}
{JS_HTML}
</body>
</html>"""


def process_file(filepath):
    slug = os.path.splitext(os.path.basename(filepath))[0]

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        raw = f.read()

    soup = BeautifulSoup(raw, 'html.parser')

    # ── TITLE ──────────────────────────────────────────────────────────────
    title_tag = soup.find('title')
    title = title_tag.get_text(strip=True) if title_tag else ''

    # ── META DESCRIPTION ───────────────────────────────────────────────────
    meta = soup.find('meta', attrs={'name': 'description'})
    description = meta.get('content', '').strip() if meta else ''
    if not description or description == "Spain's Non-Lucrative Visa guide and application support.":
        # Derive something from the slug
        readable = slug.replace('-', ' ').capitalize()
        description = f"Complete guide to {readable} — Spain Non-Lucrative Visa information and advice from My Spanish NLV."

    # ── BADGE ──────────────────────────────────────────────────────────────
    badge_el = soup.find(class_='page-hero-badge')
    badge = badge_el.get_text(strip=True) if badge_el else 'NLV Guide'
    if not badge or badge.strip() == '':
        badge = 'NLV Guide'

    # ── H1 ─────────────────────────────────────────────────────────────────
    h1_el = soup.find('h1')
    h1 = h1_el.get_text(strip=True) if h1_el else title

    # ── ARTICLE CONTENT ────────────────────────────────────────────────────
    article_el = soup.find('article', class_='blog-body')

    # ── FAQ ITEMS (extract from whole soup before cleaning article) ─────────
    faq_html = extract_faq_items(soup)

    if article_el:
        article_content = clean_article(article_el)
    else:
        # Fallback: try to find any main content section
        section = soup.find('section', class_='section')
        if section:
            inner = section.find(class_='section-inner') or section
            article_content = clean_article(inner)
        else:
            article_content = '<p>Guide content coming soon.</p>'

    return build_page(title, description, badge, h1, slug, article_content, faq_html)


def main():
    args = sys.argv[1:]
    test_mode = '--test' in args
    single_file = None
    if '--file' in args:
        idx = args.index('--file')
        if idx + 1 < len(args):
            single_file = args[idx + 1]

    if single_file:
        files = [os.path.join(BLOG_DIR, single_file)]
    else:
        files = sorted(glob.glob(os.path.join(BLOG_DIR, '*.html')))
        files = [f for f in files if os.path.basename(f) not in SKIP_FILES]

    if test_mode:
        files = files[:5]
        print(f"TEST MODE — processing {len(files)} files")
    else:
        print(f"Processing {len(files)} blog files...")

    ok, errors = 0, []
    for i, filepath in enumerate(files, 1):
        basename = os.path.basename(filepath)
        try:
            result = process_file(filepath)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"  [{i}/{len(files)}] ✓  {basename}")
            ok += 1
        except Exception as e:
            print(f"  [{i}/{len(files)}] ✗  {basename}: {e}")
            errors.append((basename, str(e)))

    print(f"\nDone. {ok} rebuilt successfully, {len(errors)} failed.")
    if errors:
        for name, err in errors:
            print(f"  FAILED: {name}: {err}")


if __name__ == '__main__':
    main()
