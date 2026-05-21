#!/usr/bin/env python3
"""
Extract actual page content from corrupted files.
Saves content as separate files for reuse.
"""

import os
import re
from pathlib import Path

BLOG_DIR = "/sessions/sharp-determined-cannon/mnt/My Spanish NLV/blog"
CONSULATE_DIR = "/sessions/sharp-determined-cannon/mnt/My Spanish NLV/consulates"
OUTPUT_DIR = "/sessions/sharp-determined-cannon/mnt/My Spanish NLV/content-recovery"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_page_content(html_file):
    """Extract the actual page content from HTML."""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title
        title_match = re.search(r'<title>([^<]+)</title>', content)
        title = title_match.group(1) if title_match else "Untitled"
        
        # Extract page hero content
        hero_match = re.search(r'<section class="page-hero">.*?</section>', content, re.DOTALL)
        hero_content = hero_match.group(0) if hero_match else ""
        
        # Extract main content - from <main> or after hero to first footer
        main_start = content.find('<main>')
        if main_start == -1:
            # Try finding after page-hero section
            hero_end = content.find('</section>', content.find('class="page-hero"'))
            main_start = hero_end + 10 if hero_end != -1 else 0
        
        # Find first footer
        footer_pos = content.find('<footer>')
        if footer_pos == -1:
            main_content = content[main_start:]
        else:
            main_content = content[main_start:footer_pos]
        
        # Clean up - remove closing main tag if present
        main_content = main_content.replace('</main>', '')
        
        return {
            'title': title,
            'hero': hero_content.strip(),
            'main': main_content.strip()
        }
    except Exception as e:
        print(f"Error reading {os.path.basename(html_file)}: {e}")
        return None

def process_directory(directory, dir_name):
    """Process all HTML files in directory."""
    print(f"\n{dir_name}:")
    
    if not os.path.isdir(directory):
        print(f"  Directory not found: {directory}")
        return
    
    html_files = sorted([f for f in os.listdir(directory) if f.endswith('.html')])
    
    for filename in html_files:
        if 'TEMPLATE' in filename or 'index.html' in filename:
            continue
        
        filepath = os.path.join(directory, filename)
        data = extract_page_content(filepath)
        
        if not data:
            continue
        
        # Save extracted content
        base_name = filename.replace('.html', '')
        output_file = os.path.join(OUTPUT_DIR, f"{base_name}.txt")
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"TITLE: {data['title']}\n")
                f.write(f"FILE: {filename}\n")
                f.write("=" * 60 + "\n\n")
                f.write("HERO SECTION:\n")
                f.write(data['hero'] + "\n\n")
                f.write("MAIN CONTENT:\n")
                f.write(data['main'] + "\n")
            
            print(f"  ✓ {filename}")
        except Exception as e:
            print(f"  ✗ {filename} - {e}")

# Process both directories
process_directory(BLOG_DIR, "Blog Posts")
process_directory(CONSULATE_DIR, "Consulate Pages")

print(f"\n✓ Content extracted to: {OUTPUT_DIR}")
