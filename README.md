# 100Hires Portfolio Project — Bayu Poetra Ramadhan

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

## Repository Structure
/research/
├── sources.md ← 10 curated experts with full annotations
├── linkedin-posts/ ← Posts per author (collected via Apify API)
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
├── youtube-transcripts/ ← Video research notes per author
│   ├── 30mpc-armand-nick/
│   ├── alex-berman/
│   ├── jason-bay/
│   ├── belal-batrawy/
│   ├── nick-abraham/
│   └── jen-allen-knuth/
└── other/
└── playbook-outline.md ← Synthesis of all frameworks into actionable pipeline
fetch_linkedin_posts.py ← Apify API scraper for LinkedIn posts
fetch_transcripts.py ← yt-dlp script for YouTube metadata
SETUP.md ← Step-by-step setup guide
README.md ← This file
plain

---

## The 10 Experts

| # | Expert | Channel | Angle | ICP Tier |
|---|--------|---------|-------|----------|
| 1 | Armand & Nick (30MPC) | Podcast/YouTube | Cold calling + sequencing | Mid-market/Enterprise |
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
