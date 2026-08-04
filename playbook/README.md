# Cold Outreach Pipeline for B2B SaaS — Playbook / SOP

**Author:** Bayu Poetra Ramadhan
**Repository:** 100hires-portfolio-project
**Stage:** 3 — Playbook / SOP
**Date:** August 2026
**Source base:** 10 practitioners documented in [`/research/sources.md`](../research/sources.md)

---

## How to read the citations in this document

Two kinds of citation appear here, and the difference matters:

| Marker | Meaning |
|---|---|
| **`[source: …]`** | The claim comes from material I collected in Step 2. It lives in this repo and you can open the file. It is **what the practitioner asserts**, not established fact. |
| **`[verified: …]`** | I independently checked the claim against a public, third-party or primary source in August 2026. Link included. |
| **`[disputed: …]`** | I checked the claim and found it contradicted or materially misstated by the underlying source. I explain the discrepancy. |

If a recommendation carries only a `[source: …]` marker, treat it as a practitioner's opinion that I found credible enough to include — not as evidence.

---

## Source reliability note — read this first

I want to be straightforward about the limits of my own research base before I start making recommendations from it.

**1. My collected LinkedIn posts do not carry permalinks.** The files in [`/research/linkedin-posts/`](../research/linkedin-posts/) contain post text, author, date and engagement count, but no per-post URL. The collection was done via the Apify `harvestapi/linkedin-profile-posts` actor, and several profiles returned sparse or unstructured results (documented in the [root README](../README.md)). This means **a reader cannot independently open and verify most individual posts I cite.** That is a real weakness in a document whose whole premise is "every recommendation cites its source." Where a claim mattered enough to build a recommendation on, I went and found a public source for it — those are the `[verified: …]` markers.

**2. Every number in my source base is self-reported by someone selling the method that produced it.** Nine of the ten are agency owners, course sellers, authors or trainers. None of the reply rates, close rates or lift percentages in this playbook have been independently audited. I have not treated any of them as evidence. I have treated them as claims made by interested parties.

**3. I found one factual error in my own Step 2 submission.** In [`/research/sources.md`](../research/sources.md) I described Vincent Fourcade as the founder of ColdIQ. That is wrong — **Michel Lieben is Founder & CEO of ColdIQ** ([verified: coldiq.com](https://coldiq.com/blog/how-coldiq-grew-from-an-affiliate-side-project-to-a-65m-arr-agency)). ColdIQ's status as one of four Elite Clay Studio partners globally does check out. I am correcting it here rather than quietly fixing it, because the correction is more useful to you than a clean record.

**4. I found one collected post that contradicts the data it cites.** See [Disagreement 3](#disagreement-3--the-cold-call-opener) below. This is the single most important finding in my research and it changed how I weight my own source material.

---

# Part I — The Pipeline

Six stages. Each stage states the recommendation, the source, and the condition under which I would not do it.

---

## Stage 0 — Decide whether cold outreach is the right motion at all

**Recommendation: do not start a cold outreach pipeline unless your ACV can absorb the cost of research-led targeting.**

The entire consensus of my source base is that volume-led outbound is dead. The disagreement is only about what replaces it — and every replacement is more expensive per contact than the thing it replaces.

> "Old outbound: 1,000 emails/day, 0.5% reply rate = 5 replies. New outbound: 100 emails/day, 8% reply rate = 8 replies. Less volume. Better targeting. More results."
> `[source: Vincent Fourcade / ColdIQ, LinkedIn 05.08.2024 — /research/linkedin-posts/vincent-fourcade/vincent-fourcade-posts.md, post 3]`

The market data supports the direction of that claim even if not the specific numbers. **Average B2B cold email reply rates have fallen from roughly 8.5% in 2019 to ~5% in 2025 to ~3.43% in 2026, and SaaS sits at the bottom of the industry table, frequently under 2%** ([verified: Instantly Cold Email Benchmark Report 2026](https://instantly.ai/cold-email-benchmark-report-2026); [Cleanlist 2026 response-rate statistics](https://www.cleanlist.ai/blog/2026-02-18-cold-email-response-rate-statistics)).

**The arithmetic gate.** If deep research costs ~20 minutes per account fully loaded, and your pipeline needs 30 accounts researched per meeting booked, that is 10 hours of SDR time per meeting. At any realistic loaded SDR cost, **cold outreach stops making sense below roughly $8–12K ACV** unless you have a product-led motion feeding it. None of my ten sources state this gate. All ten implicitly assume you have already passed it.

**Do not do this if:** your ACV is under ~$5K and you have no self-serve funnel. Every framework below will lose you money faster than doing nothing.

---

## Stage 1 — ICP and signal identification

### 1.1 Define the account list before you define the message

> "We spend more time deciding WHO to contact than HOW. That is the entire secret."
> `[source: Jack Reamer / SalesBread, LinkedIn 22.07.2024 — /research/linkedin-posts/jack-reamer/jack-reamer-posts.md, post 3]`

This is the one point on which all ten sources agree without qualification, which is itself weak evidence — universal agreement in a commercial content ecosystem usually means the claim is unfalsifiable. It is still the right starting point, because the cost of a wrong list compounds through every later stage.

### 1.2 Run a disqualification pass, not a qualification pass

Filter accounts **out** before you filter them in. Four filters; drop any account failing two or more:

1. Budget authority present at your target persona level
2. A trigger event inside the last 90 days
3. Currently using a competitor or a visible DIY workaround
4. Company in a growth phase

`[source: Jason Bay / Outbound Squad, LinkedIn 22.09.2024 — /research/linkedin-posts/jason-bay/jason-bay-posts.md, post 3]`

Why disqualification-first rather than scoring: a scoring model lets a weak account survive on the strength of one good attribute. A drop-rule does not. This is a structural difference, not a stylistic one.

### 1.3 The four signal families

Both Jason Bay and ColdIQ independently converge on nearly the same signal taxonomy, collected from separate sources:

| Signal | Threshold | What it implies |
|---|---|---|
| **Hiring** | 3+ revenue roles posted in 30 days | Active GTM investment, playbook about to break |
| **Technology** | New CRM / core system in last 6 months | Migration pain, budget already unlocked |
| **Content** | Exec published about the problem you solve | Problem is validated publicly, not inferred |
| **News / funding** | Funding inside 90 days | Budget exists, growth pressure applied |

`[source: Jason Bay, LinkedIn 19.07.2024 — jason-bay-posts.md, post 5]` and `[source: Vincent Fourcade / ColdIQ, LinkedIn 10.09.2024 — vincent-fourcade-posts.md, post 2]`

Two practitioners with different business models and different toolchains arriving at the same four families is the strongest signal in my source base. I weight this higher than any single claimed reply rate.

### 1.4 Account tiering — my addition to the source material

None of my ten sources tier the account list before choosing a motion, yet almost every disagreement between them dissolves once you do. I use three tiers, and the rest of this playbook branches on them:

| Tier | Definition | Accounts/month/rep | Motion |
|---|---|---|---|
| **A** | Top 5% by ACV × fit, named accounts | 20–30 | Deep research, warm-up, multi-thread |
| **B** | Strong fit, standard ACV | 150–250 | Signal-triggered sequence, single-thread first |
| **C** | Fits ICP on paper, no active signal | Nurture only | No outbound. Content + retargeting until a signal fires |

I return to this table repeatedly below.

---

## Stage 2 — Message construction

### 2.1 Email structure (Tier B default)

**Alex Berman's 3C framework** is the most reproducible email skeleton in my source base:

- **C1 — Compliment:** a specific, verifiable observation about their work
- **C2 — Case study:** a comparable company and a number
- **C3 — Call to action:** one question, one ask

`[source: Alex Berman, LinkedIn 31.10.2024 — /research/linkedin-posts/alex-berman/alex-berman-posts.md, post 1]`

I use the **structure** and discard Berman's supporting claims. See [Part V](#part-v--who-i-would-not-recommend-following) for why.

### 2.2 Message length and CTA form

- Emails **under 75 words** carry the highest reply rates; over 200 words, reply rates fall sharply
- **Yes/No CTAs** outperform open-ended ones
- **One CTA per email**, never a menu

`[source: Jeremy Chatelaine / QuickMail, LinkedIn 08.10.2024 — /research/linkedin-posts/jeremy-chatelaine/jeremy-chatelaine-posts.md, post 1]`

Chatelaine is the only source in my set whose numbers come from platform-level aggregate data rather than from his own campaigns, which makes him structurally less prone to survivorship bias than the agency owners. I weight him accordingly.

### 2.3 Anchor every message to one of four buying motives

Make money / save money / save time / avoid risk. If the first sentence maps to none of them, the email is decoration.

`[source: Belal Batrawy, LinkedIn 25.08.2024 — /research/linkedin-posts/belal-batrawy/belal-batrawy-posts.md, post 4]`

### 2.4 Write business cases, not introductions

> "Cold email: *We help companies like yours increase revenue.* Business case: *Companies in your segment with 50–200 reps typically leave $400K in pipeline annually from poor follow-up sequencing.* One is about you. One is about them."
> `[source: Jason Bay, LinkedIn 08.08.2024 — jason-bay-posts.md, post 4]`

### 2.5 What "personalized" actually means

The distinction that matters is **company-level** vs **person-level** research:

> Weak: *"I noticed you are the VP of Sales at Acme Corp."* Strong: *"Your comment on the SaaStr thread about SDR-to-AE handoff ratios was the most practical take I have seen on that problem."*
> `[source: Jack Reamer, LinkedIn 08.09.2024 — jack-reamer-posts.md, post 2]`

Reamer attaches a 6% vs 34% reply-rate delta to this comparison. **I am not carrying that number forward** — see [Rejection 1](#rejection-1--jack-reamers-1-lead-per-day-arithmetic). The qualitative distinction stands on its own and does not need the number.

### 2.6 The buyer-side filter

Before sending, run the message against what a recipient actually deletes on sight: anything over ~150 words, anything with 3+ bullets, and any variant of "I help companies like yours achieve their goals."

`[source: Vin Matano, LinkedIn 01.11.2024 — /research/linkedin-posts/vin-matano/vin-matano-posts.md, post 1]`

This is a useful checklist and a weak evidence base — it is one person describing his own inbox. Use it as a smell test, not a rule.

---

## Stage 3 — Sequencing and channel

### 3.1 Tier B sequence (default)

| Day | Channel | Action |
|---|---|---|
| 1 | Email | Signal-anchored opener, 3C structure, <75 words |
| 3 | LinkedIn | Connection request, no note |
| 5 | Email | New angle — not "just following up." Different buying motive |
| 8 | LinkedIn | Engage with their content, no ask |
| 10 | Phone | Cold call, honest opener (§3.3) |
| 14 | Email | Breakup with a low-friction interest question |

Structure adapted from Reamer's multi-channel cadence `[source: Jack Reamer, LinkedIn 15.10.2024 — jack-reamer-posts.md, post 1]`, with the ask moved earlier for reasons in [Disagreement 4](#disagreement-4--how-long-to-warm-before-you-ask).

### 3.2 Tier A sequence

Everything in Tier B, plus: 30-day content engagement before first contact, multi-threading from day 1 (§3.4), and a named-account research doc per account.

### 3.3 The cold call opener

**Recommendation: open by naming the call for what it is.**

> "Hey Tom, I will be straight with you — this is a cold call. Do you have 27 seconds?"
> `[source: Nick Cegelski / 30MPC, LinkedIn 10.11.2024 — /research/linkedin-posts/nick-cegelski/nick-cegelski-posts.md, post 1]`

The underlying mechanism — a permission-based opener that acknowledges the interruption — is supported by Gong's analysis of 300M+ recorded calls, where permission-based openers show roughly an **11.18% success rate against a ~1.5% baseline** ([verified: Gong Labs, *The best and worst cold call openers*](https://www.gong.io/blog/the-best-and-worst-cold-call-openers-backed-by-data-from-300m-calls)).

Critically, **"Did I catch you at a bad time?" is not the same thing and performs terribly** — around 0.9% success, roughly 40% *less* likely to book ([verified: same source](https://www.gong.io/blog/the-best-and-worst-cold-call-openers-backed-by-data-from-300m-calls)). Asking permission works. Offering an exit does not. Many reps conflate these.

### 3.4 Multi-threading (Tier A / enterprise only)

At companies over 500 employees, 6–10 people participate in a buying decision. Map four roles from day one: Champion, Economic Buyer, Blocker (legal/IT/security), Coach.

`[source: Jen Allen-Knuth / DemandJen, LinkedIn 25.10.2024 — /research/linkedin-posts/jen-allen-knuth/jen-allen-knuth-posts.md, post 1]`

> "One champion = deal at risk. A coalition = deal in motion."
> `[source: Jen Allen-Knuth, LinkedIn 15.07.2024 — jen-allen-knuth-posts.md, post 3]`

**Do not do this for Tier B.** In an SMB deal with a two-person buying committee, parallel outreach to both reads as a swarm and burns the account.

---

## Stage 4 — Deliverability (non-negotiable, do this before Stage 1)

If the mail does not arrive, nothing above matters.

**Technical:** SPF, DKIM and DMARC configured; custom tracking domain; domain aged 90+ days before any cold sending; 4+ weeks of warmup at 20–30/day.
**Behavioural:** 30–50 emails/day/inbox maximum; randomised send intervals; unsubscribe link in every message.

`[source: Jeremy Chatelaine / QuickMail, LinkedIn 20.08.2024 — jeremy-chatelaine-posts.md, post 2]`

**Time cost this implies:** ~4 months from domain purchase to full-rate sending. Plan the hire and the domain purchase together, not sequentially.

---

## Stage 5 — Measurement

### 5.1 Measure replies, not opens

**Do not optimise subject lines for open rate.** Apple Mail Privacy Protection auto-loads tracking pixels, which materially inflates reported opens and makes open rate unreliable as a decision metric ([verified: Instantly Cold Email Benchmark Report 2026](https://instantly.ai/cold-email-benchmark-report-2026)). This is why I reject one of Berman's recommendations outright — see [Rejection 2](#rejection-2--optimising-subject-lines-for-open-rate).

### 5.2 Benchmarks to hold yourself to

| Metric | Realistic target | Basis |
|---|---|---|
| Reply rate (all) | 3–6% | [verified: Apollo 2026 benchmarks](https://www.apollo.io/insights/what-is-a-good-benchmark-for-reply-rates-in-cold-outreach) — 3.43% is the 2026 average; >6% is strong execution |
| Reply rate (SaaS) | 2–4% | [verified: SaaS sits at the bottom of the industry table](https://www.cleanlist.ai/blog/2026-02-18-cold-email-response-rate-statistics) |
| Positive replies as share of all replies | 15–25% | Conservative reading of SalesBread's 48.14% — see [Rejection 1](#rejection-1--jack-reamers-1-lead-per-day-arithmetic) |
| Meetings per connected cold call | ~1 in 3 (top decile) | [verified: 30MPC / *Cold Calling Sucks*, backed by Gong 300M+ call data](https://www.30mpc.com/the-book-on-cold-calling) |

### 5.3 Define the outcome unit before you start

A meeting-ready lead has four properties: budget authority, an active (not theoretical) problem, a need inside 90 days, and awareness that their current approach is failing.

> "Most outreach tries to create all 4. The best outreach finds accounts where all 4 already exist."
> `[source: Nick Abraham / Leadbird, LinkedIn 14.08.2024 — /research/linkedin-posts/nick-abraham/nick-abraham-posts.md, post 3]`

Abraham's agency is paid only for meetings booked `[source: Nick Abraham, LinkedIn 02.11.2024 — nick-abraham-posts.md, post 1]`. That commercial model makes his definition of a qualified meeting stricter than a sender-paid agency's, and it is the definition I would adopt — not because he is more honest, but because his incentives are better aligned with mine than most of this list.

---

# Part II — Where experts disagree

---

## Disagreement 1 — Volume vs. depth

**Alex Berman:** templated, reproducible copy at scale. The 3C framework "tested across 1M+ cold emails," five buying signals tracked with BuiltWith + Sales Navigator + Google Alerts, "takes 10 minutes to set up." `[source: alex-berman-posts.md, posts 1–2]`

**Jason Bay:** the opposite. Martini Glass targeting — wide ICP, narrow to highest intent, then go extremely deep on **20–30 accounts per month**. "20 deeply researched prospects beats 200 generic ones. Every time." `[source: jason-bay-posts.md, post 1]`

**Where I land: neither, because both are answering a question they have not asked — what is the deal worth?**

Berman's economics come from an agency-services model where a single close pays for thousands of sends. Bay's come from training enterprise sales teams where a single account is worth six figures. Both are correct inside their own ACV band and wrong outside it. Neither says so, because saying so would narrow their addressable market.

This is why I introduced tiering in §1.4. Tier A gets Bay's depth (20–30 accounts/month is almost exactly Bay's own number). Tier B gets Berman's structure with signal-gating that Berman does not require. Tier C gets nothing.

The market trend independently favours Bay's direction: falling reply rates across the board `[verified: 8.5% (2019) → 3.43% (2026)](https://www.cleanlist.ai/blog/2026-02-18-cold-email-response-rate-statistics)` mean the marginal generic email is worth less every year, while a researched one holds value. But Bay's approach does not scale to a 50-rep SDR floor, and he does not pretend otherwise.

---

## Disagreement 2 — Should AI write the copy?

**Vincent Fourcade / ColdIQ — yes, at scale.** Step 3 of their standard workflow is "AI waterfall — Claude writes personalized first line based on enrichment," claiming an 8.3% average reply rate against a 1–2% industry average. `[source: vincent-fourcade-posts.md, post 1]`

**Belal Batrawy — no, categorically.** "ChatGPT cold emails are destroying reply rates… The solution is not a better prompt. It is writing like a human who did research." `[source: belal-batrawy-posts.md, post 3]`

**Jason Bay — split the task.** "AI did not kill cold outreach. AI killed lazy cold outreach. Reps struggling right now replaced thinking with prompts. Reps crushing quota use AI to research faster, then write the message themselves." `[source: jason-bay-posts.md, post 1]`

**Where I land: Bay's split, with one refinement.**

Bay resolves the contradiction rather than restating it. Fourcade and Batrawy are both right about different halves: AI is genuinely superior at *retrieval and synthesis across many accounts*, and genuinely worse at *the judgment call about which single fact is worth leading with*. That judgment is the entire value of the first line.

My refinement: **let AI write the first line only where the enrichment data is structured and factual** (funding amount, job posting count, tech stack change). Where the signal is interpretive — someone's argument in a post, a strategic shift implied by a hire — a human writes it. Structured signal → AI is fine. Interpretive signal → AI produces the exact fluent-but-hollow output Batrawy is describing.

**On the ColdIQ 8.3% claim — and a contradiction worth knowing about.** The "1–2% industry average" being compared against is roughly fair for SaaS specifically ([verified: SaaS often under 2%](https://www.cleanlist.ai/blog/2026-02-18-cold-email-response-rate-statistics)), though below the 3.43% cross-industry figure. The 8.3% itself is self-reported by an agency selling this exact service.

More usefully: **ColdIQ's own published account of how the agency grew recommends the opposite of the low-volume position in my collected post.** Their $6.5M ARR retrospective advises "sending at least 500 cold emails per day. At scale, knowing that even a 1% reply rate produces enough conversations to sign clients, that volume becomes predictable pipeline" ([verified: Michel Lieben, ColdIQ, March 2026](https://coldiq.com/blog/how-coldiq-grew-from-an-affiliate-side-project-to-a-65m-arr-agency)).

So the same agency publicly argues both "100 emails/day at 8.3%" and "500 emails/day at 1%." I do not think this is dishonesty — I think it is the difference between what an agency does for its *own* customer acquisition (volume, because their ICP is broad and their ACV is a $3K/month retainer) and what it sells to clients (precision, because that is the differentiated product). That gap is worth noticing generally: **practitioners frequently run a different motion than the one they teach**, and the one they run is usually the more honest signal about what works for their economics.

---

## Disagreement 3 — The cold call opener

This is the disagreement that mattered most to my research, because resolving it revealed a factual error inside my own source material.

**Armand Farrokh's collected post states:** *"Gong data shows reps who open with How are you have 10% lower connect-to-meeting rate."* `[source: armand-farrokh-posts.md, post 1]`

**Nick Cegelski's collected posts recommend:** radical honesty — "I will be straight with you, this is a cold call" — on the grounds that it disarms the sales guard and creates a micro pattern-interrupt. `[source: nick-cegelski-posts.md, posts 1–2]`

**What Gong's published research actually says:** opening with a version of *"How are you?"* correlates with a **5.2% success rate against a 1.5% baseline — a 3.4x improvement**, across a dataset of 90,380 cold calls. *"How have you been?"* is Gong's single best-performing opener at **10.01%, or 6.6x baseline**. By contrast, *"Did I catch you at a bad time?"* sits at **0.9% — 40% worse than baseline** ([verified: Gong Labs, *Proven cold call opening lines that work*](https://www.gong.io/blog/cold-call-opening-lines)).

**Caveat I am applying to my own verification:** that Gong analysis was first published in April 2018 (last updated March 2026), and Gong's own article makes the point that openers "have a shelf life." I am using it to establish that the *direction* of the collected claim is wrong, not to argue that 5.2% is today's number.

**`[disputed: armand-farrokh-posts.md, post 1]` — the claim as collected is the inverse of what the cited source reports.**

**Where I land, and what I concluded from it.**

On the tactic: I recommend Cegelski's honest opener, because it is a permission-based opener, and permission-based openers verify independently at ~11.18% against a ~1.5% baseline ([verified: Gong](https://www.gong.io/blog/the-best-and-worst-cold-call-openers-backed-by-data-from-300m-calls)). That is the highest-performing family in Gong's data and it does not depend on the disputed claim. The 30MPC book itself is explicitly built on Gong's 300M+ call dataset ([verified](https://www.30mpc.com/the-book-on-cold-calling)), which makes the discrepancy more likely to be an artifact of the post or of my collection than a considered position by Farrokh.

On the research: **I cannot fully rule out that the discrepancy originates in my own collection pipeline rather than in the original post.** My Apify collection returned no permalinks, so I cannot open the original post and check. That is the concrete cost of the sourcing weakness I flagged at the top of this document, and it is the single change I would make if I ran Step 2 again — capture the post URL as a required field, or discard the post.

The practical lesson I am taking forward: **when a practitioner cites a dataset, go read the dataset.** In this case it took one search and it inverted the recommendation.

---

## Disagreement 4 — How long to warm before you ask

**Vin Matano — 30 days of warming, minimum.** Identify 50 dream accounts, follow every decision-maker, comment thoughtfully for 30 days with no pitch, share relevant content, then DM referencing a specific interaction. "Warm outreach converts 5x better than cold outreach… The best SDRs do warm outreach that looks cold to everyone else." `[source: vin-matano-posts.md, post 2]`

**Jack Reamer — 12 days, five touches, then ask.** Connection request → voice note → text referencing their post → share content → soft ask on day 12. "5 touches before you ask for anything. That is the rule." `[source: jack-reamer-posts.md, post 1]`

**Nick Abraham — implicitly, as short as the economics allow.** Leadbird is paid per meeting booked, which makes a 30-day unpaid warming period commercially impossible at any volume. `[source: nick-abraham-posts.md, post 1]`

**Where I land: Matano for Tier A, Reamer for Tier B, and I think Matano's 5x figure is doing unearned work.**

Matano's advice is good and his evidence is thin — he is a content creator describing an approach that suits a content creator's existing audience and distribution. His "5x" has no stated basis. More importantly, his method has a hard ceiling: 30 days of genuine engagement across 50 accounts is roughly a full day per week of one person's time, which caps a rep at ~50 accounts per quarter. That is a Tier A motion by definition, and Matano does not say so.

Reamer's 12-day cadence is the right default because it is the shortest sequence in my source base that still front-loads value before the ask. I moved the ask one step earlier than Reamer in §3.1 — Reamer's own economics rest on a 48% *positive reply ratio* that, as [Rejection 1](#rejection-1--jack-reamers-1-lead-per-day-arithmetic) shows, does not mean what his post implies it means. Without that cushion, a 12-day patience budget is expensive.

---

## Disagreement 5 — Multi-thread immediately, or earn the right first?

**Jen Allen-Knuth — day one.** "Starting multi-thread outreach on day 1 is not aggressive. It is the minimum to be taken seriously." `[source: jen-allen-knuth-posts.md, post 1]`

**Jack Reamer — earn it.** Five value-first touches to a single contact before any ask; approaching several people simultaneously is the opposite of that patience. `[source: jack-reamer-posts.md, post 1]`

**Where I land: Allen-Knuth above ~500 employees, Reamer below it — and the threshold is the buying committee size, not the headcount.**

The two are not really disagreeing; they are describing different buyers. In a 6–10 person enterprise committee, single-threading is a single point of failure, and Allen-Knuth's coalition argument `[source: jen-allen-knuth-posts.md, post 3]` is a risk argument, not an aggression argument. In an SMB where the buyer and the economic buyer are the same person, "multi-threading" means emailing that person's colleague, which reads as going around them.

Allen-Knuth's background is Challenger and enterprise training at G2, GE and IBM; Reamer's SalesBread client base skews SMB and mid-market. Each is generalising from a valid sample to an invalid range. Tiering resolves it.

---

# Part III — What I rejected and why

---

## Rejection 1 — Jack Reamer's "1 lead per day" arithmetic

**What the source says:**

> "50 targeted LinkedIn outreaches per day × 48% positive reply rate = 24 replies × 20% book calls = 4–5 calls per week × 20% become qualified opportunities = 1 per day"
> `[source: jack-reamer-posts.md, post 3]`

**Why I reject it: the 48.14% figure is a positive reply *ratio*, not a reply *rate*, and the calculation uses it as the latter.**

SalesBread's own published numbers are: **45% connection acceptance rate, 19.98% reply rate, and 48.14% positive reply ratio** — where "positive reply ratio" means the share *of the replies received* that were meeting requests or qualified inquiries ([verified: SalesBread LinkedIn outreach stats](https://salesbread.com/linkedin-outreach-stats/)).

So the correct chain from 50 outreaches is approximately:

- 50 × 19.98% ≈ **10 replies** (not 24)
- 10 × 48.14% ≈ **5 positive replies**

The post's version overstates replies by roughly **2.4x**. The output number happens to survive because the later conversion steps absorb the error, which is exactly what makes this kind of mistake hard to catch and worth catching.

**What I kept:** the principle — extreme targeting at low volume, more time on *who* than on *how* — is sound and is corroborated across my source base. **What I discarded:** the funnel math, and by extension every downstream capacity plan built on a 48% reply rate. A rep planning headcount off the post's version would under-resource by more than half.

I have also stopped carrying Reamer's "6% vs 34%" personalization figure (§2.5) forward, on the same basis: this source states rates with a precision his own published methodology does not support.

---

## Rejection 2 — Optimising subject lines for open rate

**What the source says:** subject lines ranked by open rate from 1M+ sends — worst: "Quick question," "Following up," "Introduction"; best: "[Their company] + [Your company]," "[Specific metric] for [Their company]," and single words like "Churn?" or "Pipeline?" `[source: alex-berman-posts.md, post 3]`. Chatelaine offers a supporting data point: subject lines under 5 words at 28% open rate vs over 10 words at 14% `[source: jeremy-chatelaine-posts.md, post 1]`.

**Why I reject the framing, not the tactics.**

**Open rate is a broken metric.** Apple Mail Privacy Protection pre-fetches tracking pixels regardless of whether a human opened the message, which systematically inflates reported opens; the industry consensus in 2026 is that reply rate is the only reliable performance signal ([verified: Instantly Cold Email Benchmark Report 2026](https://instantly.ai/cold-email-benchmark-report-2026)). A subject-line test optimised against open rate in 2026 is measuring Apple's servers as much as your prospects.

There is also a second-order cost the sources ignore. Bare single-word subject lines ("Churn?") and bracket-formula subjects ("[Company] + [Company]") are now heavily pattern-matched by both spam filters and experienced buyers — the exact "template smell" that Batrawy argues destroys reply rates `[source: belal-batrawy-posts.md, post 3]`. Berman's own list is internally inconsistent with Batrawy's thesis, and Berman does not engage with it.

**What I do instead:** write the subject as a compressed version of the email's single specific observation, keep it under 5 words per Chatelaine's length finding, and **A/B test against reply rate only**, accepting the slower test cycles that implies.

---

## Rejection 3 — Competitor-threat pattern interrupts as a default opener

**What the source says:**

> "[Their competitor] just raised $50M. Your team has 6 months before they outspend you on [category]. Now they are reading. Because it is about them, not you."
> `[source: belal-batrawy-posts.md, post 1]`

**Why I reject it as a default** (while keeping the broader pattern-interrupt principle):

1. **It is frequently wrong on the facts.** The sender rarely knows the recipient's competitive position well enough to assert a six-month window. If the recipient already has a plan — or does not consider that company a competitor — the message discredits itself in one sentence, and you have spent your only impression proving you did not do the research you are implicitly claiming.
2. **It optimises for attention, not for the conversation you want.** It succeeds by triggering a threat response. That reliably produces a reply and unreliably produces a buyer, because the emotion it creates points at the competitor, not at your product.
3. **It travels badly.** In the markets I work in — Indonesia and broader Southeast Asia — an unsolicited message from a stranger telling a senior leader their company is losing reads as a status challenge, not as insight. Every source in my set writes from a US/EU context and none of them flags this. I would not send this message in Jakarta.

**What I kept:** Batrawy's underlying and much stronger point — lead with the problem, not with yourself; delete "I hope this email finds you," "My name is X," and "We help companies like yours" `[source: belal-batrawy-posts.md, post 1]`. A pattern interrupt can be a specific observation rather than a threat, and it performs the same disarming function without the failure modes.

---

## Rejection 4 — "How are you" as a banned opener

Covered in full in [Disagreement 3](#disagreement-3--the-cold-call-opener). Rejected on evidence: Gong's published data shows it performing at 3.4x baseline, not below it ([verified](https://www.gong.io/blog/cold-call-opening-lines)).

---

# Part IV — My original ideas

Two ideas I did not find in any of my ten sources, plus one smaller operational change.

---

## Original idea 1 — Signal half-life scoring

**The gap.** All ten of my sources treat trigger events as binary: the signal is either present or absent, and if present, the account enters the sequence. Both Jason Bay and ColdIQ publish signal taxonomies `[source: jason-bay-posts.md, post 5; vincent-fourcade-posts.md, post 2]`, and Bay includes a "last 90 days" window in his disqualification filter `[source: jason-bay-posts.md, post 3]`, but nobody in my set treats a signal as a **decaying asset with a channel-specific expiry**. A 90-day window is applied uniformly to signals that do not behave uniformly at all.

**The idea.** Assign every signal a half-life, and route it to a different sequence depending on where in that half-life it is caught.

| Signal | Half-life | Why | Optimal contact window |
|---|---|---|---|
| Job posting for a role you affect | ~21 days | The role gets filled or the req gets pulled. The pain is acute and short. | Days 1–14 |
| New VP/Director in seat | ~45 days | New executives select their stack in the first quarter. After that they defend the choice they made. | Days 14–60 (not week 1 — they have no context yet) |
| Funding announced | ~90 days | Budget unlocks slowly; every vendor emails in week one. | Days 30–90 — deliberately after the inbound wave |
| Tech/CRM migration | ~180 days | Pain grows through implementation and peaks after go-live, not at announcement. | Days 60–180 |
| Exec published about the problem | ~14 days | Attention is at its peak the week they wrote it. | Days 1–7 |

**Why it could work.** Three mechanisms, all independently plausible:

1. **Competitive timing arbitrage.** Every vendor with an Apollo seat sends within 72 hours of a funding announcement. Arriving at day 45 means arriving in a materially emptier inbox with the same signal. The signal has not decayed; the *competition* for it has.
2. **It matches the buyer's internal timeline rather than the trigger's press-release timeline.** A new VP cannot buy in week one — they have no budget authority and no diagnosis yet. Reaching them in week one wastes the signal and, worse, spends it: you have now been categorised as a vendor who emails on arrival.
3. **It makes the list self-cleaning.** A `signal_expiry` date field in Clay lets accounts fall out of sequence automatically when the reason for contacting them has lapsed — which addresses a failure mode none of my sources discuss: sequences that keep running long after their justification has evaporated, producing exactly the generic outreach every one of them warns against.

**Implementation:** one date field per enriched account (`signal_captured_at`), one computed field (`signal_expiry`), and a routing rule in the sequencing tool. This is roughly an afternoon of Clay work, which is part of why I suspect nobody has bothered to formalise it — it is too small to sell as a methodology.

**How I would test it:** hold-out test on funding signals specifically, since that is where the inbox-crowding effect should be largest. Two cohorts, same ICP, same copy, same sender — one contacted at days 1–7, one at days 30–45. Compare positive reply rate. n≈200 per cohort for a usable read. **I have not run this test. It is a hypothesis with a plausible mechanism, not a finding.**

---

## Original idea 2 — A local trigger library for non-US markets

**The gap.** All ten sources write for US/EU B2B SaaS, and the signal taxonomies they publish are downstream of that: funding rounds, Salesforce migrations, SDR job postings, G2 intent. These are artifacts of a specific market structure — venture-funded, high-headcount-churn, publicly-instrumented. Applied unchanged in Southeast Asia, most of them fire rarely or never.

**The idea.** Build a parallel trigger library from locally-observable events, and treat the imported one as the supplement rather than the base.

Candidate triggers for the Indonesian / SEA market:

| Local trigger | Signal it carries |
|---|---|
| **Fiscal year alignment** — most Indonesian corporates run Jan–Dec, unlike the Feb–Jan of many US SaaS vendors | Budget conversations belong in Sept–Nov, not in the vendor's Q4. Outreach timed to the vendor's calendar arrives at the wrong end of the buyer's. |
| **Ramadan / Lebaran** | A ~3-week effective freeze on decisions, plus a pre-period rush. A sequence that lands in that window is not slow, it is dead — and re-engaging in week 4 with "just following up" wastes the account. |
| **Regulatory change** (OJK, Kominfo, sector ministries) | Compliance deadlines create hard, dated, non-discretionary budget — the strongest buying signal in the market and entirely absent from Western intent databases. |
| **Commodity price moves / harvest cycles** | In agri-adjacent and resource-linked sectors, capex timing follows commodity cycles far more closely than it follows funding events. |
| **Expansion into a new province / new licence granted** | The local analogue of a funding round — operational expansion with committed budget, announced locally and rarely captured by international data vendors. |

**Why it could work.** Two arguments, one general and one specific.

The general one: the value of a signal is a function of how many competitors can also see it. G2 intent and funding data are purchasable, which means every well-funded competitor sees them simultaneously and the advantage compresses to zero. Locally-observed signals require someone to be reading the local trade press and the regulator's announcements — a labour cost, not a licence cost, and therefore a defensible one.

The specific one: **this generalises from something I have actually run rather than something I read.** At SawitPRO, standard SaaS triggers were near-useless for supplier and mill acquisition — the signals that predicted a buying window were harvest timing, weather anomalies and CPO price movements. Building acquisition around those, rather than around imported playbooks, contributed to expanding the supplier base 180% year on year. That is adjacent-industry evidence, not B2B SaaS evidence, and I flag it as such in [Part VI](#part-vi--weaknesses-of-this-playbook).

**What would falsify it:** if a matched test shows locally-sourced triggers producing no better positive-reply rate than the imported taxonomy on the same account list, the extra labour is not justified and the imported list wins on cost.

---

## Original idea 3 (minor) — Grade replies, do not count them

Every metric in my source base terminates at "reply rate" or "positive reply rate," where "positive" is a binary. I would grade every reply 1–5 (1 = unsubscribe/hostile, 3 = polite deflection, 5 = meeting booked or qualified inquiry) and optimise campaigns on the **share of 4s and 5s**, not on total replies.

The reason is that the tactics that maximise reply volume and the tactics that maximise reply quality diverge — provocation, curiosity gaps and threat framing all lift replies while lowering the share that convert. A team optimising a single blended number will drift toward provocation without noticing, because the dashboard rewards it. Grading makes the tradeoff visible. It costs about ten seconds per reply.

---

# Part V — Who I would NOT recommend following

---

## Primary: Alex Berman

**I would not recommend Alex Berman as a source, and I have used his framework anyway. Both of those are deliberate.**

The 3C structure (§2.1) is genuinely useful — it is a clean, teachable skeleton and I kept it. My objection is not to the framework; it is to using him as an *evidentiary* source, which is a different thing.

**1. The claims are large, round, and not independently auditable.** "$20M in B2B SaaS leads in one year," "1M+ cold emails," "14,000+ agencies," "500,000+ sales meetings." These figures appear in his own content and are repeated in interviews where he is the source ([SaaS Club interview](https://saasclub.io/podcast/alex-berman-inspirebeats/)) — that is restatement, not corroboration. I could not find a single one of these numbers verified by a third party. No source in my set matches this ratio of claim size to evidence.

**2. There is a documented, undisclosed conflict of interest in his tool recommendations.** A reviewer who paid for and completed two months of Berman's $247/month Email10K program reports that Berman is an affiliate or partner in nearly all the software he recommends to students and on YouTube — LeadShark, Taplio, Mailshake, Lemlist and Zopto are named — and does not disclose those relationships ([verified: independent paid-member review, Nov 2022](https://scottleventon.com/blog/alex-berman-cold-email-program-review)). The same review notes that Berman today sends far fewer cold emails than he once did and derives most revenue from promoting software to his audience.

That is the specific reason I will not cite him as evidence. Undisclosed affiliate incentives on tool recommendations tell you how a source treats the reader's interests when they conflict with his own, and that judgment transfers directly to how much weight his numbers deserve.

**3. The commercial incentive runs the wrong way.** Berman's business is selling cold email training. His revenue depends on cold email appearing accessible and scalable. That is precisely the claim a reader most needs tested, and it is the claim he is least free to test honestly. Compare Jeremy Chatelaine, whose numbers come from platform aggregates across other people's campaigns — Chatelaine's incentives do not require any individual tactic to work.

**4. The advice is from the previous era.** Berman's edge was built when volume worked. Reply rates have fallen from ~8.5% in 2019 to ~3.43% in 2026 ([verified](https://www.cleanlist.ai/blog/2026-02-18-cold-email-response-rate-statistics)), and his own posts still frame buying signals as a "10 minutes to set up" Google Alerts exercise `[source: alex-berman-posts.md, post 2]`. That was true in 2019.

**How I would tell a junior to use him:** take the 3C skeleton, ignore every number, and never cite him as evidence for anything.

---

## Secondary: Vin Matano — a scope objection, not a credibility one

I would not recommend Vin Matano **as a source of cold outreach method**, though I would keep reading him.

Matano's value in my set is real but narrow: he is the only source who describes the receiving end. His delete-on-sight list `[source: vin-matano-posts.md, post 1]` is a good final check before you hit send.

The problem is the evidence base. His buyer-side post generalises from one inbox — his own, which receives 50+ messages a week precisely because he is a well-known B2B creator. That is not a representative buyer. And his primary recommendation, 30 days of engagement across 50 dream accounts before contact `[source: vin-matano-posts.md, post 2]`, works particularly well for someone who already has audience and distribution, which is the thing an SDR at a Series A company does not have. The "5x better" figure carries no stated basis.

He is a useful sanity check and a poor template. I would not build a pipeline from his content, and I would not have ranked him among my ten if I were choosing again — I would replace him with a second data-source practitioner in Chatelaine's mould, since aggregate-data sources were the most reliable category in my whole set.

---

## A note on my own error

I attributed ColdIQ's founding to Vincent Fourcade in Step 2. Michel Lieben is Founder & CEO ([verified](https://coldiq.com/blog/how-coldiq-grew-from-an-affiliate-side-project-to-a-65m-arr-agency)). The ColdIQ *content* I collected remains among the most technically substantive in my set and I have kept it; the attribution was mine to get right and I did not. I would rather correct it in the deliverable than leave it in the repository history unmarked.

---

# Part VI — Weaknesses of this playbook

An honest accounting of what is wrong with this document.

## Weaknesses in the evidence

**1. Nine of ten sources sell the method they advocate.** Agency owners, course sellers, trainers, authors. Not one number in my source base has been independently audited. I have applied consistent skepticism, but skepticism is not a substitute for data I do not have.

**2. Severe survivorship bias.** Every case study in my set is a campaign that worked. Nobody publishes the campaign that burned a domain and produced zero meetings, so the base rate is invisible to me. My benchmarks in §5.2 are drawn from third-party aggregate data rather than from my sources specifically, precisely for this reason — but the *tactics* still come from a sample of winners.

**3. My own source files are not independently verifiable.** No permalinks on the collected LinkedIn posts (see the reliability note at the top). A reader cannot check most of my `[source: …]` citations against the original. This is a genuine defect and it is mine, not the practitioners'.

**4. At least one collected post contradicts its own cited data,** and I cannot determine whether the error originated with the practitioner or with my collection ([Disagreement 3](#disagreement-3--the-cold-call-opener)). If one post has this problem, others may. I checked the claims I built recommendations on. I did not check every claim in every file.

**5. All ten sources are US/EU.** No APAC practitioner, no non-English-language market, no source writing about markets where relationship-first business norms change what a cold approach even means. This is the largest blind spot in my source base and the reason for [Original idea 2](#original-idea-2--a-local-trigger-library-for-non-us-markets).

## Weaknesses in the recommendations

**6. My tiering thresholds are asserted, not derived.** The Tier A/B/C cutoffs in §1.4, the ~$8–12K ACV gate in Stage 0, and the ~500-employee multi-threading threshold in Disagreement 5 are reasoned estimates from the shape of the source material. They are not fitted to data. They are the right *kind* of parameter; the specific values need calibration against a real business.

**7. Both original ideas are untested.** Signal half-life has a plausible mechanism and no evidence. The local trigger library generalises from agritech supplier acquisition in Indonesia to B2B SaaS — an adjacent-industry transfer across a real gap, from a market with different buyers, different cycle lengths and different digital instrumentation. I believe the underlying principle (locally-observed signals are less contested than purchasable ones) transfers. I have not demonstrated that the specific triggers do.

**8. Deliverability advice has the shortest shelf life in this document.** §Stage 4 reflects current sender requirements. Mailbox providers have changed bulk-sender rules materially in the last two years and will again. Treat that section as expiring and re-verify before implementation.

**9. The playbook assumes an ICP already exists.** Everything from Stage 1 onward presumes you know who you sell to and why they buy. If that is not true, none of this helps, and no source in my set addresses it — they all sell to teams who have already done that work.

**10. Cold calling is under-developed relative to email.** My richest sources on calling are 30MPC, and my collected material on them is the material I found an error in. A reader should go to *Cold Calling Sucks (And That's Why It Works)* and to Gong's published research directly rather than relying on my summary.

## What is missing entirely

- **A cost model.** No fully-loaded cost per meeting, no tooling budget beyond Abraham's $2,400/month stack figure `[source: nick-abraham-posts.md, post 2]`, no break-even analysis. Stage 0 gestures at this and does not do the work.
- **Time to first meeting.** Nowhere in this document does a reader learn how long it takes from a standing start to a booked meeting. Given Stage 4's ~4-month domain warm-up, this is a significant omission for anyone planning a hire.
- **Compliance.** GDPR, CAN-SPAM, PDPA (Singapore), and Indonesia's PDP Law all constrain cold outreach and vary sharply by jurisdiction. Zero coverage here, and zero coverage in my source base.
- **The handoff.** This playbook ends at "meeting booked." The SDR-to-AE transition is where a meaningful share of booked meetings die, and I have not addressed it.
- **Anything about what happens after a "no."** Reamer, Batrawy and Cegelski all touch on objections; I did not build a nurture or re-engagement motion. A rejected account with a live signal is a better prospect than a cold account without one, and this playbook has nothing to say about it.

---

## Sources

**Collected material (this repository)**

- [`/research/sources.md`](../research/sources.md) — the 10 practitioners, with annotations
- [`/research/linkedin-posts/`](../research/linkedin-posts/) — posts by author, collected 17 June 2026 via Apify
- [`/research/youtube-transcripts/`](../research/youtube-transcripts/) — video metadata and research notes
- [`/research/other/playbook-outline.md`](../research/other/playbook-outline.md) — Step 2 synthesis

**Independently verified (checked August 2026)**

- Gong Labs — [Proven cold call opening lines that work](https://www.gong.io/blog/cold-call-opening-lines) — "How are you" 5.2% vs 1.5% baseline; "How have you been" 10.01%; "bad time?" 0.9%; 90,380-call dataset, pub. 2018, updated Mar 2026
- Gong Labs — [Best and worst cold call openers, 300M+ calls](https://www.gong.io/blog/the-best-and-worst-cold-call-openers-backed-by-data-from-300m-calls) — permission-based opener ~11.18%
- ColdIQ — [How ColdIQ grew to $6.5M ARR](https://coldiq.com/blog/how-coldiq-grew-from-an-affiliate-side-project-to-a-65m-arr-agency) — Michel Lieben, Founder & CEO; "500 cold emails per day… even a 1% reply rate"
- SalesBread — [LinkedIn outreach stats](https://salesbread.com/linkedin-outreach-stats/) — 45% acceptance, 19.98% reply rate, 48.14% positive reply ratio
- 30 Minutes to President's Club — [*Cold Calling Sucks (And That's Why It Works)*](https://www.30mpc.com/the-book-on-cold-calling) — 2024, built on Gong's 300M+ call dataset
- Instantly — [Cold Email Benchmark Report 2026](https://instantly.ai/cold-email-benchmark-report-2026) — 3.43% average reply rate; Apple MPP and open-rate inflation
- Cleanlist — [Cold email response rate statistics 2026](https://www.cleanlist.ai/blog/2026-02-18-cold-email-response-rate-statistics) — 8.5% (2019) → 3.43% (2026); SaaS under 2%
- Apollo — [Reply rate benchmarks 2026](https://www.apollo.io/insights/what-is-a-good-benchmark-for-reply-rates-in-cold-outreach) — 3–6% good, >8% exceptional
- SaaS Club — [Alex Berman interview](https://saasclub.io/podcast/alex-berman-inspirebeats/) — self-reported volume and background claims
- Scott Leventon — [Email10K program review, Nov 2022](https://scottleventon.com/blog/alex-berman-cold-email-program-review) — paid member; undisclosed affiliate relationships (LeadShark, Taplio, Mailshake, Lemlist, Zopto)

---

*Bayu Poetra Ramadhan — Growth & Demand Generation — Jakarta, Indonesia*
