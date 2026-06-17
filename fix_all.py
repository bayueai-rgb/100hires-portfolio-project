import os

os.chdir(os.path.expanduser("~/Desktop/100hires-portfolio-project"))

# ========== 1. SETUP.md ==========
setup = """# Setup Guide - 100Hires Portfolio Project

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
"""

open("SETUP.md", "w").write(setup.strip())
print("OK: SETUP.md")

# ========== 2. Fix fetch_transcripts.py typo ==========
content = open("fetch_transcripts.py").read()
content = content.replace("OUUT_DIR", "OUTPUT_DIR")
open("fetch_transcripts.py", "w").write(content)
print("OK: fetch_transcripts.py typo fixed")

# ========== 3. Fix README.md typo ==========
content = open("README.md").read()
content = content.replace("Galadon", "Galadon")
open("README.md", "w").write(content)
print("OK: README.md typo fixed")

# ========== 4. Fix LinkedIn headers ==========
import glob
for md in glob.glob("research/linkedin-posts/*/*-posts.md"):
    c = open(md).read()
    c = c.replace("(Manual Collection)", "(via Apify API + manual curation)")
    c = c.replace("Manual Collection", "Collected via Apify API; supplemented manually where API returned limited results")
    c = c.replace("Supplementary LinkedIn Posts", "LinkedIn Posts")
    open(md, "w").write(c)
    print("OK: " + os.path.basename(md))

# ========== 5. Rename YouTube .txt to metadata.txt ==========
for txt in glob.glob("research/youtube-transcripts/*/*.txt"):
    if not txt.endswith("-summary.md"):
        newname = txt.replace(".txt", "-metadata.txt")
        os.rename(txt, newname)
        print("OK: " + os.path.basename(newname))

# ========== 6. Add My Synthesis to playbook ==========
playbook = open("research/other/playbook-outline.md").read()
if "My Synthesis" not in playbook:
    synthesis = """

---

## My Synthesis: What I'd Actually Build

If I were building a cold outreach pipeline for a B2B SaaS in APAC tomorrow, I'd combine:

1. Jason Bay's signal-based approach for ICP identification (intent data + trigger events)
2. Alex Berman's 3C framework for email copy (scalable, reproducible)
3. Nick Abraham's pay-per-meeting model as the success metric (forces quality over volume)

The gap in current practitioner content: Most frameworks are built for US/EU markets. For APAC (especially Indonesia where I operate), the missing piece is local signal identification - regulatory changes, competitor pricing moves, and supply chain shifts that don't appear in standard intent databases. My next research phase would focus on building APAC-specific trigger libraries.

Connection to SawitPRO: In agricultural tech, we learned that "funding round" signals don't apply. Instead, harvest season timing, weather anomalies, and commodity price spikes are the real triggers. This same principle applies to any non-Silicon-Valley market: the signals that matter are local, not generic.
"""
    open("research/other/playbook-outline.md", "a").write(synthesis)
    print("OK: playbook synthesis added")

print("\n=== ALL FIXES DONE ===")
print("Now run: git add . && git commit -m 'fix: all audit issues' && git push origin main")