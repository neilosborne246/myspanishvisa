#!/bin/bash

# Script to apply NLV master template to blog and consulate pages
# Usage: ./apply-template.sh

TEMPLATE="/Users/neil/Documents/Claude/Projects/My Spanish NLV/template-master-nlv.html"
BLOG_DIR="/Users/neil/Documents/Claude/Projects/My Spanish NLV/blog"
CONSULATE_DIR="/Users/neil/Documents/Claude/Projects/My Spanish NLV/consulates"

# Function to extract page content
extract_content() {
    local file="$1"
    # Extract from first <section class="page-hero"> to before </footer>
    # This preserves all page content while removing nav/footer

    # Use awk to extract the content section
    awk '/<section class="page-hero">/,/<\/footer>/' "$file" | \
    sed '/<\/footer>/,$d' | \
    sed '$d'  # Remove the last closing tag
}

# Function to apply template to a file
apply_template_to_file() {
    local input_file="$1"
    local temp_file="${input_file}.tmp"

    # Extract page content
    local content=$(extract_content "$input_file")

    if [ -z "$content" ]; then
        echo "  SKIPPED: Could not extract content from $(basename "$input_file")"
        return 1
    fi

    # Create new file by replacing placeholder in template
    cp "$TEMPLATE" "$temp_file"

    # Replace the placeholder with actual content
    # Using a temporary marker to handle multi-line content
    perl -i -pe "s|<!-- PAGE CONTENT GOES HERE -->|$content|" "$temp_file" 2>/dev/null

    if [ $? -eq 0 ]; then
        mv "$temp_file" "$input_file"
        echo "  ✓ Updated: $(basename "$input_file")"
        return 0
    else
        rm "$temp_file"
        echo "  ✗ Failed: $(basename "$input_file")"
        return 1
    fi
}

# Function to safely apply template using sed
apply_template_safe() {
    local input_file="$1"
    local output_file="${input_file}"
    local content_file="${input_file}.content"

    # Extract content to temporary file
    awk '/<section class="page-hero">/,/<\/footer>/' "$input_file" | \
    sed '/<\/footer>/,$d' > "$content_file"

    if [ ! -s "$content_file" ]; then
        echo "  SKIPPED: Could not extract content from $(basename "$input_file")"
        rm "$content_file"
        return 1
    fi

    # Build the output file: template + content + closing footer/scripts
    {
        # Add template up to the placeholder
        head -n $(grep -n "<!-- PAGE CONTENT GOES HERE -->" "$TEMPLATE" | cut -d: -f1 | head -1) "$TEMPLATE" | sed '$ d'

        # Add extracted content
        cat "$content_file"

        # Add closing sections (footer, mobile bar, scripts)
        tail -n +$(grep -n "<!-- Footer -->" "$TEMPLATE" | cut -d: -f1) "$TEMPLATE"
    } > "${output_file}.new"

    if [ -s "${output_file}.new" ]; then
        mv "${output_file}.new" "$output_file"
        rm "$content_file"
        echo "  ✓ Updated: $(basename "$input_file")"
        return 0
    else
        echo "  ✗ Failed: $(basename "$input_file")"
        rm "$content_file" "${output_file}.new" 2>/dev/null
        return 1
    fi
}

echo "Applying NLV Master Template..."
echo ""

# Process blog posts
echo "Blog Posts:"
count=0
for file in "$BLOG_DIR"/*.html; do
    # Skip template files and index
    if [[ "$(basename "$file")" == *"TEMPLATE"* ]] || [[ "$(basename "$file")" == "index.html" ]]; then
        echo "  SKIPPED: $(basename "$file") (template/index file)"
        continue
    fi

    apply_template_safe "$file"
    count=$((count + 1))

    # Show progress every 10 files
    if [ $((count % 10)) -eq 0 ]; then
        echo "  ... processed $count files"
    fi
done

echo ""
echo "Consulate Pages:"
# Process consulate pages (skip index)
for file in "$CONSULATE_DIR"/*.html; do
    if [[ "$(basename "$file")" == "index.html" ]]; then
        echo "  SKIPPED: $(basename "$file") (index file)"
        continue
    fi

    apply_template_safe "$file"
done

echo ""
echo "Template application complete!"
