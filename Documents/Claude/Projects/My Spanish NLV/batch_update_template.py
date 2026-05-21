#!/usr/bin/env python3
"""
Batch apply NLV master template to all blog and consulate pages.
Extracts page content and wraps with master template.
"""

import os
import re
from pathlib import Path

# Use mounted paths for bash environment
import os
if os.path.exists("/sessions/sharp-determined-cannon/mnt/My Spanish NLV"):
    TEMPLATE_FILE = "/sessions/sharp-determined-cannon/mnt/My Spanish NLV/template-master-nlv.html"
    BLOG_DIR = "/sessions/sharp-determined-cannon/mnt/My Spanish NLV/blog"
    CONSULATE_DIR = "/sessions/sharp-determined-cannon/mnt/My Spanish NLV/consulates"
else:
    TEMPLATE_FILE = "/Users/neil/Documents/Claude/Projects/My Spanish NLV/template-master-nlv.html"
    BLOG_DIR = "/Users/neil/Documents/Claude/Projects/My Spanish NLV/blog"
    CONSULATE_DIR = "/Users/neil/Documents/Claude/Projects/My Spanish NLV/consulates"

def read_file(filepath):
    """Read file content safely."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"  ERROR reading {os.path.basename(filepath)}: {e}")
        return None

def write_file(filepath, content):
    """Write file content safely."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"  ERROR writing {os.path.basename(filepath)}: {e}")
        return False

def extract_page_content(html_content):
    """
    Extract the main page content from an HTML file.
    Looks for content between first page element and </footer>
    """
    try:
        # Find the start of page content - looking for multiple patterns
        start_pattern = r'(<section class="page-hero".*?>|<header[^>]*>|<main[^>]*>)'
        start_match = re.search(start_pattern, html_content, re.DOTALL)

        if not start_match:
            # Try to find any section tag
            start_pattern = r'<(section|header|main)[^>]*>'
            start_match = re.search(start_pattern, html_content)
            if not start_match:
                return None
            start_pos = start_match.start()
        else:
            start_pos = start_match.start()

        # Find end - before footer
        footer_pos = html_content.find('</footer>')
        if footer_pos == -1:
            footer_pos = html_content.find('<footer')

        if footer_pos == -1:
            # Try to find closing script tags as fallback
            footer_pos = html_content.rfind('</script>')
            if footer_pos == -1:
                return None

        # Get content section
        content_section = html_content[start_pos:footer_pos]

        # Return the extracted content
        return content_section.strip()

    except Exception as e:
        print(f"    Error extracting content: {e}")
        return None

def apply_template(input_file):
    """Apply master template to a single file."""
    filename = os.path.basename(input_file)

    # Skip certain files
    if 'TEMPLATE' in filename or 'MASTER' in filename or filename == 'index.html':
        print(f"  SKIP {filename} (template/index file)")
        return False

    # Read input file
    input_html = read_file(input_file)
    if not input_html:
        return False

    # Extract page content
    page_content = extract_page_content(input_html)
    if not page_content:
        print(f"  SKIP {filename} (could not extract content)")
        return False

    # Read template
    template_html = read_file(TEMPLATE_FILE)
    if not template_html:
        return False

    # Replace placeholder in template with page content
    output_html = template_html.replace('    <!-- PAGE CONTENT GOES HERE -->', page_content)

    # Write back to input file
    if write_file(input_file, output_html):
        print(f"  ✓ {filename}")
        return True
    else:
        return False

def process_directory(directory, dir_name):
    """Process all HTML files in a directory."""
    print(f"\n{dir_name}:")

    if not os.path.isdir(directory):
        print(f"  Directory not found: {directory}")
        return 0

    html_files = sorted([f for f in os.listdir(directory) if f.endswith('.html')])
    success_count = 0
    skip_count = 0

    for filename in html_files:
        filepath = os.path.join(directory, filename)
        if apply_template(filepath):
            success_count += 1
        else:
            skip_count += 1

        # Show progress
        if (success_count + skip_count) % 10 == 0:
            print(f"    ... processed {success_count + skip_count} files")

    print(f"  Summary: {success_count} updated, {skip_count} skipped")
    return success_count

def main():
    """Main function."""
    print("=" * 60)
    print("Applying NLV Master Template to All Pages")
    print("=" * 60)

    # Verify template exists
    if not os.path.exists(TEMPLATE_FILE):
        print(f"ERROR: Template not found at {TEMPLATE_FILE}")
        return

    total = 0

    # Process blog posts
    blog_count = process_directory(BLOG_DIR, "Blog Posts")
    total += blog_count

    # Process consulate pages
    consulate_count = process_directory(CONSULATE_DIR, "Consulate Pages")
    total += consulate_count

    print("\n" + "=" * 60)
    print(f"Template application complete!")
    print(f"Total files updated: {total}")
    print("=" * 60)

if __name__ == '__main__':
    main()
