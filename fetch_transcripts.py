#!/usr/bin/env python3
"""
YouTube Transcript Fetcher via yt-dlp
Updated with validated video links (June 2026)
"""

import subprocess, os, re, json
from datetime import date

TARGETS = [
    {"author": "30mpc-armand-nick", "videos": [
        {"url": "https://www.youtube.com/watch?v=6UiOAGvZYd8", "title": "top-15-sales-tactics"},
    ]},
    {"author": "alex-berman", "videos": [
        {"url": "https://www.youtube.com/watch?v=AApSKUGVw0E", "title": "cold-email-tech-stack"},
    ]},
    {"author": "jason-bay", "videos": [
        {"url": "https://www.youtube.com/watch?v=4TuHuaZe0bU", "title": "cold-calling-2025"},
    ]},
    {"author": "belal-batrawy", "videos": [
        {"url": "https://www.youtube.com/watch?v=2aK8YyUR4Rw", "title": "no-fluff-cold-calling"},
    ]},
    {"author": "nick-abraham", "videos": [
        {"url": "https://www.youtube.com/watch?v=l_yhQ7tAKCw", "title": "7-figure-cold-email"},
    ]},
    {"author": "jen-allen-knuth", "videos": [
        {"url": "https://www.youtube.com/watch?v=RaffMnUapLc", "title": "cost-of-inaction"},
    ]},
]

OUTPUT_DIR = "research/youtube-transcripts"

def slugify(t):
    return re.sub(r'[\s_-]+', '-', re.sub(r'[^\w\s-]', '', t.lower().strip()))[:80]

def fetch_transcript(url, outpath, title):
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    tmp = outpath.replace(".txt", "")
    cmd = ["yt-dlp", "--skip-download", "--write-auto-subs", "--sub-lang", "en", "--convert-subs", "srt", "--output", tmp, url]
    subprocess.run(cmd, capture_output=True)
    
    srt = tmp + ".srt"
    if os.path.exists(srt):
        lines, seen = [], set()
        for line in open(srt).read().splitlines():
            line = line.strip()
            if not line or re.match(r"^\d+$", line) or re.match(r"^\d{2}:\d{2}", line):
                continue
            line = re.sub(r"<[^>]+>", "", line)
            if line and line not in seen:
                lines.append(line)
                seen.add(line)
        with open(outpath, "w") as f:
            f.write(f"# Transcript: {title}\nSource: {url}\nFetched: {date.today()}\n\n---\n\n" + "\n".join(lines))
        os.remove(srt)
        print(f"  OK: {outpath}")
        return True
    else:
        cmd2 = ["yt-dlp", "--skip-download", "--dump-json", url]
        r = subprocess.run(cmd2, capture_output=True, text=True)
        if r.returncode == 0:
            try:
                m = json.loads(r.stdout)
                with open(outpath, "w") as f:
                    f.write(f"# Metadata: {m.get('title', title)}\nSource: {url}\nUploader: {m.get('uploader','')}\nDate: {m.get('upload_date','')}\nNote: No auto-transcript available\n\n---\n\n{m.get('description','')[:2500]}")
                print(f"  META: {outpath}")
                return True
            except:
                pass
        print(f"  FAIL: {url}")
        return False

def main():
    print("YouTube Transcript Fetcher — Updated June 2026")
    ok = fail = 0
    for expert in TARGETS:
        adir = os.path.join(OUUT_DIR, expert["author"])
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
