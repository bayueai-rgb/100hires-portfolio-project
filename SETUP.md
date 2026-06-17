# Setup Guide - 100Hires Portfolio Project

## Prerequisites
- Python 3.8+
- Git
- macOS (tested on Sonoma)

## Step 1 - Clone Repository
    git clone https://github.com/bayueai-rgb/100hires-portfolio-project.git
    cd 100hires-portfolio-project

## Step 2 - Sign up for Apify
1. Go to https://apify.com
2. Click "Sign up for free" - no credit card needed
3. You get $5 free credit automatically

## Step 3 - Get Apify API Token
1. Go to https://console.apify.com/settings/integrations
2. Click "+ Create new token" - name it: portfolio
3. Copy the token (format: apify_api_XXXXXXXX)

## Step 4 - Install yt-dlp (macOS)
    brew install yt-dlp

Verify:
    which yt-dlp

## Step 5 - Run LinkedIn Collection Script
    APIFY_TOKEN=apify_api_XXXXXXXX python3 fetch_linkedin_posts.py

What it does:
- Triggers Apify harvestapi/linkedin-profile-posts actor per expert
- Polls until completion
- Saves output as:
  - {slug}-posts.md - Formatted Markdown
  - {slug}-raw.json - Raw API response

## Step 6 - Run YouTube Collection Script
    python3 fetch_transcripts.py

What it does:
- Attempts to fetch auto-generated English subtitles via yt-dlp
- If subtitles unavailable: falls back to video metadata
- Curated research notes (-summary.md) are the primary deliverable

## Step 7 - Verify Output
    ls research/linkedin-posts/       # 10 expert folders
    ls research/youtube-transcripts/  # 6 video folders
    ls research/other/                # playbook-outline.md

## Step 8 - Commit & Push
    git add research/
    git commit -m "add: collected research data"
    git push origin main

## Cost Breakdown

Item | Cost
-----|-----
Apify API (50 posts) | ~$0.06
yt-dlp (free) | $0
Total | ~$0.06

## Troubleshooting

Error | Cause | Fix
------|-------|-----
APIFY_TOKEN not set | Environment variable missing | export APIFY_TOKEN=...
HTTP 401 | Token expired | Create new token at Apify Console
0 posts returned | Profile private | Retry later
yt-dlp not found | Not installed | brew install yt-dlp
pip3 blocked | macOS protection | Use brew install instead

## File Structure

    100hires-portfolio-project/
    ├── research/
    │   ├── sources.md
    │   ├── linkedin-posts/
    │   ├── youtube-transcripts/
    │   └── other/
    │       └── playbook-outline.md
    ├── fetch_linkedin_posts.py
    ├── fetch_transcripts.py
    ├── SETUP.md
    └── README.md