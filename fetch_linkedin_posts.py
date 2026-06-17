#!/usr/bin/env python3
"""
LinkedIn Posts Scraper via Apify API
100Hires Portfolio — Cold Outreach B2B SaaS
Author: Bayu Poetra Ramadhan

Usage (Mac/Linux):
    APIFY_TOKEN=apify_api_xxx python3 fetch_linkedin_posts.py
"""

import os, sys, json, time, re, requests
from datetime import datetime, timezone

APIFY_TOKEN = os.environ.get("APIFY_TOKEN", "")
ACTOR_ID    = "harvestapi~linkedin-profile-posts"
APIFY_BASE  = "https://api.apify.com/v2"
OUTPUT_DIR  = "research/linkedin-posts"
MAX_POSTS   = 5

EXPERTS = [
    {"slug": "armand-farrokh",    "name": "Armand Farrokh",    "url": "https://www.linkedin.com/in/armandfarrokh/"},
    {"slug": "nick-cegelski",     "name": "Nick Cegelski",     "url": "https://www.linkedin.com/in/ncegelski/"},
    {"slug": "jason-bay",         "name": "Jason Bay",         "url": "https://www.linkedin.com/in/jasondbay/"},
    {"slug": "alex-berman",       "name": "Alex Berman",       "url": "https://w.linkedin.com/in/alexanderberman/"},
    {"slug": "belal-batrawy",     "name": "Belal Batrawy",     "url": "https://www.linkedin.com/in/belbatrawy/"},
    {"slug": "nick-abraham",      "name": "Nick Abraham",      "url": "https://www.linkedin.com/in/nickabraham12/"},
    {"slug": "jeremy-chatelaine", "name": "Jeremy Chatelaine", "url": "https://www.linkedin.com/in/jeremychatelaine/"},
    {"slug": "vin-matano",        "name": "Vin Matano",        "url": "https://www.linkedin.com/in/vinmatano/"},
    {"slug": "jen-allen-knuth",   "name": "Jen Allen-Knuth",   "url": "https://www.linkedin.com/in/jenallenknuth/"},
    {"slug": "vincent-fourcade",  "name": "Vincent Fourcade",  "url": "https://www.linkedin.com/in/vincentfourcade/"},
]

def run_actor(linkedin_url, max_posts):
    run_url = f"{APIFY_BASE}/acts/{ACTOR_ID}/runs"
    payload = {"profileUrls": [linkedin_url], "maxPosts": max_posts, "scrapeReactions": False, "scrapeComments": False}
    params  = {"token": APIFY_TOKEN}
    resp = requests.post(run_url, json=payload, headers={"Content-Type": "application/json"}, params=params, timeout=30)
    resp.raise_for_status()
    run_id = resp.json()["data"]["id"]
    print(f"    Run started: {run_id}")

    status_url = f"{APIFY_BASE}/actor-runs/{run_id}"
    for i in range(36):
        time.sleep(5)
        r = requests.get(status_url, params=params, timeout=10)
        status = r.json()["data"]["status"]
        if status in ("SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT"):
            break
        print(f"    Waiting... ({i*5}s)")

    if status != "SUCCEEDED":
        print(f"    Run ended: {status}")
        return []

    dataset_id = r.json()["data"]["defaultDatasetId"]
    items = requests.get(f"{APIFY_BASE}/datasets/{dataset_id}/items", params={**params, "clean": True}, timeout=30)
    items.raise_for_status()
    return items.json()

def save_posts(expert, posts):
    out_dir = os.path.join(OUTPUT_DIR, expert["slug"])
    os.makedirs(out_dir, exist_ok=True)
    header = f"# LinkedIn Posts — {expert['nam]}\n\n**LinkedIn:** {expert['url']}\n**Collected:** {datetime.now(timezone.utc).strftime('%Y-%m-%d')}\n**Posts:** {len(posts)}\n\n---\n\n"
    blocks = []
    for i, p in enumerate(posts, 1):
        text = (p.get("text") or p.get("content") or p.get("postContent") or "").strip()
        ts   = str(p.get("postedAt") or p.get("publishedAt") or "")[:10]
        likes = p.get("likes") or p.get("numLikes") or 0
        url  = p.get("postUrl") or p.get("url") or ""
        blocks.append(f"### Post {i}\n**Date:** {ts}  \n**Likes:** {likes}  \n**URL:** {url}\n\n{text}")
    with open(os.path.join(out_dir, f"{expert['slug']}-posts.md"), "w") as f:
        f.write(header + "\n\n---\n\n".join(blocks))
    with open(os.path.join(out_dir, f"{expert['slug']}-raw.json"), "w") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    print(f"    Saved {len(posts)} posts")

def save_placeholder(expert, reason):
    out_dir = os.path.join(OUTPUT_DIR, expert["slug"])
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, f"{expert['slug']}-posts.md"), "w") as f:
        f.write(f"# LinkedIn Posts — {expert['name']}\n\nStatus: No posts collected\nReason: {reason}\nProfile: {expert['url']}\n")
    print(f"    Placeholder saved")

def main():
    print("=" * 50)
    print("LinkedIn Scraper — Apify")
    print("=" * 50)
    if not APIFY_TOKEN:
        print("ERROR: APIFY_TOKEN not set")
        print("Run: APIFY_TOKEN=apify_api_xxx python3 fetch_linkedin_posts.py")
        sys.exit(1)
    print(f"Token: {APIFY_TOKEN[:12]}... | Experts: {len(EXPERTS)} | Posts: max {MAX_POSTS} each")
    ok, fail = 0, 0
    for i, expert in enumerate(EXPERTS, 1):
        print(f"\n[{i}/{len(EXPERTS)}] {expert['name']}")
        try:
            posts = run_actor(expert["url"], MAX_POSTS)
            if posts:
                save_posts(expert, posts)
                ok += 1
            else:
                save_placeholder(expert, "Actor returned 0 posts")
                fail += 1
        et Exception as e:
            print(f"    Error: {e}")
            save_placeholder(expert, str(e))
            fail += 1
        if i < len(EXPERTS):
            time.sleep(3)
    print(f"\nDone. OK={ok} FAIL={fail}")

if __name__ == "__main__":
    main()