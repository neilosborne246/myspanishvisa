#!/usr/bin/env python3
import re
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip_script = False
        self.skip_style = False
    
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            setattr(self, f'skip_{tag}', True)
    
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            setattr(self, f'skip_{tag}', False)
    
    def handle_data(self, data):
        if not self.skip_script and not self.skip_style:
            self.text.append(data)
    
    def get_text(self):
        return ' '.join(self.text).strip()

files = [
    'student-visa-pillar-page.html',
    'student-visa-spain-requirements.html',
    'student-visa-spain-documents.html',
    'student-visa-spain-financial-requirements.html',
    'student-visa-spain-health-insurance.html',
    'student-visa-spain-cost.html',
    'student-visa-spain-processing-time.html',
    'student-visa-spain-work-rights.html',
    'student-visa-spain-extension.html',
    'student-visa-spain-renewal.html',
    'student-visa-to-work-permit-spain.html',
    'student-visa-to-residency-spain.html',
    'job-seeker-visa-spain-after-studies.html',
    'study-in-spain.html',
    'study-spanish-in-spain.html',
    'student-visa-spain-language-school.html',
    'student-visa-spain-university.html',
    'student-visa-spain-tie-card.html',
    'student-visa-spain-nie.html',
    'student-visa-spain-vs-other-visas.html',
    'student-visa-spain-by-nationality.html',
    'student-visa-spain-uk.html',
    'student-visa-spain-usa.html',
    'student-visa-spain-india.html',
    'student-visa-spain-family-dependants.html',
    'student-visa-spain-rejection.html',
]

for fname in files:
    try:
        with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
        
        # Extract visible text
        parser = TextExtractor()
        parser.feed(html)
        text = parser.get_text()
        words = len(text.split())
        
        # Check for FAQ section
        has_faq = bool(re.search(r'class=["\'].*?faq', html, re.I))
        
        # Count FAQ items - look for msv__faq-item or similar
        faq_items = len(re.findall(r'class=["\'][^"\']*faq[_-]item', html, re.I))
        
        # Check for JSON-LD
        has_jsonld = bool(re.search(r'application/ld\+json', html))
        
        # Count internal links
        internal_links = len(re.findall(r'href=["\']([^"\']*(?:/student-visa|/study-|/job-seeker)[^"\']*)["\']', html, re.I))
        
        # Check for broker/insurance section
        has_broker = bool(re.search(r'class=["\'][^"\']*broker', html, re.I))
        
        # Check for CTA sections
        has_cta = bool(re.search(r'class=["\'][^"\']*cta', html, re.I))
        
        print(f"{fname}|{words}|{has_faq}|{faq_items}|{has_jsonld}|{internal_links}|{has_broker}|{has_cta}")
    except Exception as e:
        print(f"{fname}|ERROR: {e}")
