#!/bin/bash
# ============================================================
# My Spanish Visa — Publish Script
# Copies website files to live folder and pushes to GitHub
# Usage: ./publish.sh "Your commit message"
# ============================================================

WORKING="/Users/neil/Documents/Claude/Projects/My Spanish Visa"
LIVE="/Users/neil/Claude/myspanishvisa"
MESSAGE="${1:-Update site}"

echo "→ Syncing files to live folder..."
rsync -av --delete \
  --exclude='*.py' \
  --exclude='*.md' \
  --exclude='*.docx' \
  --exclude='.DS_Store' \
  --exclude='Blog Posts/' \
  --exclude='PDF_GENERATION_SUMMARY.txt' \
  --exclude='1.png' \
  --exclude='2.png' \
  --exclude='3.png' \
  --exclude='4.png' \
  --exclude='.git/' \
  --exclude='.github/' \
  --exclude='publish.sh' \
  "$WORKING/" "$LIVE/"

echo "→ Committing and pushing to GitHub..."
cd "$LIVE"
git add -A
git commit -m "$MESSAGE"
git push origin main

echo ""
echo "✓ Done! Changes are live at myspanishvisa.com"
