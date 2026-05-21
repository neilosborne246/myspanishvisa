#!/usr/bin/env python3
"""
Rebuild corrupted files by removing duplicate footers and keeping content intact.
Restores files to readable state while preserving all text.
"""

import os
import re
from pathlib import Path

BLOG_DIR = "/sessions/sharp-determined-cannon/mnt/My Spanish NLV/blog"
CONSULATE_DIR = "/sessions/sharp-determined-cannon/mnt/My Spanish NLV/consulates"

# Read the clean template once
TEMPLATE_FILE = "/sessions/sharp-determined-cannon/mnt/My Spanish NLV/template-master-nlv.html"
with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
    TEMPLATE = f.read()

def rebuild_file(html_file):
    """Rebuild corrupted file by extracting content and removing duplicate footers."""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find page-hero section
        hero_start = content.find('<section class="page-hero">')
        if hero_start == -1:
            return False
        
        # Find the FIRST footer position
        footer_first = content.find('<footer>', hero_start)
        if footer_first == -1:
            return False
        
        # Extract everything from hero to first footer
        page_content = content[hero_start:footer_first]
        
        # Find the placeholder in template
        placeholder = '    <!-- PAGE CONTENT GOES HERE -->'
        if placeholder not in TEMPLATE:
            return False
        
        # Build new file: template with content replacing placeholder
        new_html = TEMPLATE.replace(placeholder, page_content)
        
        # Write back
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_html)
        
        return True
    except Exception as e:
        print(f"    Error: {e}")
        return False

def process_directory(directory, dir_name):
    """Process all HTML files in directory."""
    print(f"\n{dir_name}:")
    
    if not os.path.isdir(directory):
        print(f"  Directory not found: {directory}")
        return
    
    html_files = sorted([f for f in os.listdir(directory) if f.endswith('.html')])
    success = 0
    failed = 0
    
    for filename in html_files:
        if 'TEMPLATE' in filename or 'index.html' in filename:
            continue
        
        filepath = os.path.join(directory, filename)
        
        if rebuild_file(filepath):
            print(f"  ✓ {filename}")
            success += 1
        else:
            print(f"  ✗ {filename}")
            failed += 1
    
    print(f"  Summary: {success} restored, {failed} failed")
    return success

# Process both directories
blog_count = process_directory(BLOG_DIR, "Blog Posts")
consulate_count = process_directory(CONSULATE_DIR, "Consulate Pages")

total = (blog_count or 0) + (consulate_count or 0)
print(f"\n{'='*60}")
print(f"✓ Restoration complete: {total} files cleaned")
print(f"{'='*60}")
