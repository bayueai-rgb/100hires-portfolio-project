#!/usr/bin/env python3
"""
YouTube Transcript Fetcher via yt-dlp
100Hires Portfolio — Cold Outreach B2B SaaS
Author: Bayu Poetra Ramadhan

Usage:
    pip3 install yt-dlp
    python3 fetch_transcripts.py
"""

import subprocess, os, json, re, sys
from datetime import date

TARGETS = [
    {"author": "armand-farrokh-30mpc", "videos": [
        {"url": "https://www.youtube.com/watch?v=lIZ_RMm4dQ0", "title": "30mpc-cold-calling-framework"},
        {"url": "https://www.youtube.com/watch?v=Q1n359bBnys", "title": "30mpc-cold-email-reply-method"},
    ]},
    {"author": "jason-bay-outbound-squad", "videos": [
        {"url": "https://www.youtube.com/watch?v=Xm5YHJGc3X4", "title": "signal-based-personalization"},
    ]},
    author": "alex-berman", "videos": [
        {"url": "https://www.youtube.com/watch?v=Z9Rl_QUTPLA", "title": "3c-framework-cold-email"},
        {"url": "https://www.youtube.com/watch?v=j53CjFCXnkU", "title": "buying-signals-b2b-leads"},
    ]},
    {"author": "coldiq-vincent-fourcade", "videos": [
        {"url": "https://www.youtube.com/watch?v=3hVlMFqtBsQ", "title": "clay-ai-cold-outreach"},
    ]},
]

OUTPUT_DIR = "research/youtube-transcripts"

def slugify(t):
    return re.sub(r'[\s_-]+', '-', re.sub(r'[^\w\s-]', '', t.lower().strip()))[:80]

def fetch_transcript(url, outpath, title):
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    tmp = outpath.replace(".txt", "")
    cmd = ["yt-dlp", "--no-check-certificate", "--skip-download",
           "--write-auto-subs", "--sub-lang", "en", "--sub-format", "vtt",
           "--convert-subs", "srt", "--output", tmp, "--no-playlist", url]
    subprocess.run(cmd, capture_output=True, text=True)
    srt = None
    dname = os.path.dirname(outpath) or "."
    for f in os.listdir(dname):
        if f.startswith(os.path.basename(tmp)) and f.endswith(".srt"):
            srt = os.path.join(dname, f)
            break
    if srt and os.path.exists(srt):
        lines, seen = [], set()
        for line in open(srt).read().split("\n"):
            line = line.strip()
            if not line or re.match(r'^\d+$', line) or re.match(r'\d{2}:\d{2}:\d{2}', line):
                continue
            line = re.sub(r'<[^>]+>', '', line)
            if line and line not in seen:
                lines.append(line)
                seen.add(line)
        with open(outpath, "w") as f:
            f.write(f"# Transcript: {title}\nSource: {url}\nFetched: {date.today()}\n\n---\n\n" + "\n".join(lines))
        os.remove(srt)
        print(f"  Saved: {outpath}")
        return True
    cmd2 = ["yt-dlp", "--no-check-certificate", "--skip-download", "--dump-json", "--no-playlist", url]
    r = subprocess.run(cmd2, capture_output=True, text=True)
    if r.returncode == 0:
        try:
            m = json.loads(r.stdout)
            with open(outpath, "w") as f:
                f.write(f"# Metadata: {m.get('title', title)}\nSource: {url}\nUploader: {m.get('uploader','')}\nDate: {m.get('upload_date','')}\nNote: No transcript available\n\n---\n\n{m.get('description','')[:2000]}")
            print(f"  Metadata saved: {outpath}")
            return True
        except:
            pass
    print(f"  FAILED: {url}")
    return False

def main():
    print("=" * 50)
    print("YouTube Transcript Fetcher")
    print("=" * 50)
    try:
        r = subprocess.run(["yt-dlp", "--version"], capture_output=True, text=True)
        print(f"yt-dlp: {r.stdout.strip()}")
    except FileNotFoundError:
        print("ERROR: yt-dlp not found. Run: pip3 install yt-dlp")
        sys.exit(1)
    ok = fail = 0
    for expert in TARGETS:
        adir = os.path.join(OUTPUT_DIR, expert["author"])
        os.makedirs(adir, exist_ok=True)
        print(f"\n-- {expert['author']} --")
        for v in expert["videos"]:
            out = os.path.join(adir, slugify(v["title"]) + ".txt")
            if fetch_transcript(v["url"], out, v["title"]):
                ok += 1
            else:
                fail += 1
    print(f"\nDone. OK={ok} FAIL={fail}")

if __name__ == "__main__":
    main()