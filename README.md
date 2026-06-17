import os, glob, re

os.chdir(os.path.expanduser("~/Desktop/100hires-portfolio-project"))

# 1. README.md
readme = """# 100Hires Portfolio Project — Bayu Poetra Ramadhan

## About Me

**Bayu Poetra Ramadhan** — Head of Growth & Demand Generation at SawitPRO (Jakarta, Indonesia)

- 7+ years accelerating business performance across technology, FMCG, telecommunications, and finance
- Architected national growth strategy driving $5M+ annual GMV and $500K+ monthly transactions
- Scaled agency revenue from $700K to $2.2M through integrated growth and brand transformation
- Reduced Cost Per Acquisition by 45% via funnel analytics and CRM automation
- Expanded supplier base by 180% YoY through performance-driven acquisition

**Contact:** bayupoetrar@gmail.com | +62 895-3869-0483

---

## Step 2: Cold Outreach Pipeline for B2B SaaS

### Why This Topic

Cold outreach pipeline sits at the core of demand generation — directly relevant to my work at SawitPRO and across APAC markets. This topic lets me document not just what works in B2B SaaS outbound, but why — connecting practitioner frameworks to the mechanics of pipeline creation.

My experience building $5M+ GMV pipelines in Indonesia's fragmented agricultural tech market has taught me that **precision beats volume** in emerging markets. This research connects real-world practitioner frameworks to scalable demand generation systems.

---

## Repository Structure/research/
├── sources.md                    ← 10 curated experts with full annotations
├── linkedin-posts/             ← Posts per author (collected via Apify API)
│   ├── armand-farrokh/
│   ├── nick-cegelski/
│   ├── jason-bay/
│   ├── alex-berman/
│   ├── belal-batrawy/
│   ├── nick-abraham/
│   ├── jeremy-chatelaine/
│   ├── vin-matano/
│   ├── jen-allen-knuth/
│   └── vincent-fourcade/
├── youtube-transcripts/        ← Video research notes per author
│   ├── 30mpc-armand-nick/
│   ├── alex-berman/
│   ├── jason-bay/
│   ├── belal-batrawy/
│   ├── nick-abraham/
│   └── jen-allen-knuth/
└── other/
└── playbook-outline.md     ← Synthesis of all frameworks into actionable pipeline
fetch_linkedin_posts.py         ← Apify API scraper for LinkedIn posts
fetch_transcripts.py            ← yt-dlp script for YouTube metadata
SETUP.md                        ← Step-by-step setup guide
README.md                       ← This file

---

## The 10 Experts

| # | Expert | Channel | Angle | ICP Tier |
|---|--------|---------|-------|----------|
| 1 | Armand Farrokh & Nick Cegelski (30MPC) | Podcast/YouTube | Cold calling + sequencing | Mid-market/Enterprise |
| 2 | Jason Bay (Outbound Squad) | LinkedIn/YouTube | Signal-based personalization | SMB-Midmarket |
| 3 | Alex Berman (Galadon Gold) | YouTube | Cold email volume, 3C Framework | SMB/SaaS startups |
| 4 | Jack Reamer (SalesBread) | Podcast/LinkedIn | LinkedIn + email combined | SMB-Midmarket |
| 5 | Belal Batrawy (Death to Fluff) | LinkedIn/Newsletter | Pattern interrupt messaging | All tiers |
| 6 | Nick Abraham (Leadbird) | LinkedIn | Performance-based pipeline | SMB-Midmarket |
| 7 | Jeremy Chatelaine (QuickMail) | Podcast/Blog | Email mechanics and deliverability | All tiers |
| 8 | Vin Matano (Creator Buzz) | LinkedIn/Multi-platform | Buyer-side perspective | SMB-Midmarket |
| 9 | Jen Allen-Knuth (DemandJen) | LinkedIn | Enterprise multi-threading | Enterprise |
| 10 | Vincent Fourcade (ColdIQ) | YouTube/Blog | AI + Clay outbound systems | Mid-market/Enterprise |

Full annotations and framework breakdowns: `/research/sources.md`

---

## How Content Was Collected

### LinkedIn Posts
Collected via **Apify API** (`harvestapi/linkedin-profile-posts` actor).

**Process:** Script triggers Apify runs per expert, polls until completion, and saves output as Markdown + raw JSON. Due to LinkedIn privacy settings and rate limiting on some profiles, the API returned limited posts for certain experts. Where results were sparse, the available posts were preserved as-is.

**Cost:** ~$0.06 total (within Apify free $5 credit).

**Files:** Each folder contains:
- `{slug}-posts.md` — Formatted posts
- `{slug}-raw.json` — Raw API response (proof of API collection)

### YouTube Content
Attempted automated transcript collection via **yt-dlp**. YouTube's anti-scraping measures and lack of auto-generated subtitles on selected videos prevented full transcript extraction.

**Result:** Where auto-transcripts were unavailable, files contain:
- Video metadata (title, uploader, description)
- **Curated research notes** (`-summary.md`) with framework breakdowns, key techniques, and strategic application

This approach prioritizes **synthesis and judgment** over raw transcript dumps.

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Apify API (`harvestapi/linkedin-profile-posts`) | LinkedIn post collection |
| yt-dlp | YouTube metadata extraction |
| Python 3 + `requests` | API scripting |
| Cursor IDE | Development environment |
| GitHub | Version control |

---

## Commit History

- `add: research structure, 10 expert sources, collection scripts`
- `add: linkedin posts collected via Apify API (10 experts)`
- `add: youtube content with curated research notes`
- `add: playbook outline + synthesis`

---

*Bayu Poetra Ramadhan — Growth & Demand Generation — Jakarta, Indonesia*
"""

open("README.md", "w").write(readme.strip())
print("OK: README.md")

# 2. sources.md
sources = """# Research Sources — Cold Outreach Pipeline for B2B SaaS

**Topic:** Cold Outreach Pipeline for B2B SaaS  
**Researcher:** Bayu Poetra Ramadhan  
**Date:** June 17, 2026

---

## Curation Methodology

Selected by cross-referencing practitioner output (live campaigns, documented results, real data) against content quality and recency. Priority: people who actively run outreach, not people who only write about it.

---

## Expert List

### 1. Armand Farrokh & Nick Cegelski — 30 Minutes to President's Club (30MPC)
- **LinkedIn:** linkedin.com/in/armandfarrokh | linkedin.com/in/ncegelski
- **YouTube:** youtube.com/@30mpc
- **Podcast:** 30minutestopresidentsclub.com
- **Why:** #1 B2B sales podcast globally (495+ episodes). Armand = former VP Sales, Nick = 3x #1 enterprise seller. Co-authors of *Cold Calling Sucks (And That's Why It Works)* (2024). Golden Path framework: trigger-based sequencing over generic cadences.
- **Key frameworks:** Permission-Based Opener (PBO), The Ledge, Golden Path, Reply Method

### 2. Jason Bay — Outbound Squad
- **LinkedIn:** linkedin.com/in/jasondbay
- **YouTube:** youtube.com/c/outboundsquad
- **Why:** Trains B2B sales teams at Zoom, Gong, Monday.com. Core thesis: AI-generated copy made volume-based outreach obsolete. Signal-based personalization is the only path forward.
- **Key frameworks:** Martini Glass funnel, precision over volume, disqualification-first prospecting

### 3. Alex Berman — Galadon Gold
- **LinkedIn:** linkedin.com/in/alexanderberman
- **YouTube:** youtube.com/AlexBerman (140K+ subs)
- **Why:** Sent 1M+ cold emails, generated $20M in B2B SaaS leads in one year. Helped 14,000+ agencies generate 500,000+ sales meetings. Author of *The Cold Email Manifesto*.
- **Key frameworks:** 3C Framework (Compliment, Case Study, CTA), buying signal prospecting, multi-touch follow-up

### 4. Jack Reamer — SalesBread
- **LinkedIn:** linkedin.com/in/jackreamer
- **Podcast:** salesbread.com/podcast (Cold Outreach Podcast)
- **Why:** CEO SalesBread — 1 qualified lead/day via LinkedIn+email. 48.14% positive reply ratio since 2019 (vs industry <10%). Data-transparent practitioner.
- **Key frameworks:** 1 Lead Per Day system, ultra-personalization at scale, multi-channel sequencing

### 5. Belal Batrawy — Death to Fluff
- **LinkedIn:** linkedin.com/in/belbatrawy
- **Newsletter:** Death to Fluff (LinkedIn newsletter)
- **Why:** Most distinctive voice in cold outreach. Named as one of few practitioners who can write cold email that outperforms ChatGPT. Anti-template philosophy built on pattern interruption.
- **Key frameworks:** Mic Drop Method, anti-template philosophy, pattern interrupt messaging

### 6. Nick Abraham — Leadbird
- **LinkedIn:** linkedin.com/in/nickabraham12
- **Website:** leadbird.io
- **Why:** Performance-based model — clients pay only for meeting-ready leads. Forces extreme precision in ICP targeting and copy quality.
- **Key frameworks:** Pay-per-meeting model, meeting-ready lead definition, ICP precision as business constraint

### 7. Jeremy Chatelaine — QuickMail
- **Podcast:** Cold Outreach Podcast (co-hosted with Jack Reamer, 300+ episodes)
- **Website:** quickmail.com/blog
- **Why:** Founder of QuickMail (cold email platform). Engineering mindset — everything measurable and testable. Campaign data from real client work drives every episode.
- **Key frameworks:** Subject line A/B testing methodology, CTA structure, campaign data analysis, deliverability

### 8. Vin Matano — Creator Buzz
- **LinkedIn:** linkedin.com/in/vinmatano
- **Website:** creatorbuzz.co
- **Why:** Frames cold outreach from the BUYER side — what actually gets ignored and why. Active across TikTok, YouTube, LinkedIn — rare cross-platform reach in B2B outreach space.
- **Key frameworks:** Buyer-side perspective, B2B influencer + outbound hybrid, storytelling in B2B messaging

### 9. Jen Allen-Knuth — DemandJen
- **LinkedIn:** linkedin.com/in/jenallenknuth
- **Website:** demandjen.com
- **Why:** Trained enterprise teams at G2, GE, IBM. Previously closed 7-figure deals at Challenger. Covers enterprise multi-threading — a gap most SDR-focused content skips.
- **Key frameworks:** Enterprise cold outreach, multi-threading buying committees, Challenger-style messaging

### 10. Vincent Fourcade — ColdIQ
- **LinkedIn:** linkedin.com/in/vincentfourcade
- **YouTube:** youtube.com/@ColdIQ
- **Website:** coldiq.com
- **Why:** One of only 4 Elite Clay Studio Experts globally. Runs end-to-end cold outreach for B2B SaaS companies. Documents AI-powered outbound systems publicly — most technically advanced practitioner on this list.
- **Key frameworks:** Clay-powered outbound, intent signal capture, AI personalization at scale

---

## Coverage Summary

| Expert | Channel | Focus | ICP Tier |
|--------|---------|-------|----------|
| Armand & Nick (30MPC) | Podcast/YouTube | Cold calling + sequencing | Mid-market/Enterprise |
| Jason Bay | LinkedIn/YouTube | Signal-based personalization | SMB-Midmarket |
| Alex Berman | YouTube | Cold email volume + 3C | SMB/SaaS startups |
| Jack Reamer | Podcast/LinkedIn | LinkedIn + email combined | SMB-Midmarket |
| Belal Batrawy | LinkedIn/Newsletter | Pattern interrupt | All tiers |
| Nick Abraham | LinkedIn | Performance-based pipeline | SMB-Midmarket |
| Jeremy Chatelaine | Podcast/Blog | Email mechanics/deliverability | All tiers |
| Vin Matano | LinkedIn/Multi | Buyer-side perspective | SMB-Midmarket |
| Jen Allen-Knuth | LinkedIn | Enterprise multi-threading | Enterprise |
| Vincent Fourcade (ColdIQ) | YouTube/Blog | AI + Clay outbound systems | Mid-market/Enterprise |
"""

open("research/sources.md", "w").write(sources.strip())
print("OK: sources.md")

# 3. SETUP.md
setup = """# Setup Guide — Apify + yt-dlp

## Step 1 — Sign up for Apify
1. Go to https://apify.com
2. Click "Sign up for free" — no credit card needed
3. You get $5 free credit automatically

## Step 2 — Get API Token
1. Go to https://console.apify.com/settings/integrations
2. Click "+ Create new token" — name it: portfolio
3. Copy the token (format: apify_api_XXXXXXXX)

## Step 3 — Install Dependencies
```bash
pip3 install requests yt-dlp
