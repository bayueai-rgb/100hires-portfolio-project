import subprocess
import os
import json
import re
from datetime import date

TARGETS = [
    {'author': 'armand-farrokh-30mpc', 'videos': [
        {'url': 'https://www.youtube.com/watch?v=lIZ_RMm4dQ0', 'title': '30mpc-cold-calling-framework'},
        {'url': 'https://www.youtube.com/watch?v=Q1n359bBnys', 'title': '30mpc-cold-email-reply-method'},
    ]},
    {'author': 'jason-bay-outbound-squad', 'videos': [
        {'url': 'https://www.youtube.com/watch?v=Xm5YHJGc3X4', 'title': 'signal-based-personalization'},
    ]},
    {'author': 'alex-berman', 'videos': [
        {'url': 'https://www.youtube.com/watch?v=Z9Rl_QUTPLA', 'title': '3c-framework-cold-email'},
        {'url': 'https://www.youtube.com/watch?v=j53CjFCXnkU', 'title': 'buying-signals-b2b-leads'},
    ]},
    {'author': 'coldiq-vincent-fourcade', 'videos': [
        {'url': 'https://www.youtube.com/watch?v=3hVlMFqtBsQ', 'title': 'clay-ai-cold-outreach'},
    ]},
]

OUTPUT_DIR = 'research/youtube-transcripts'

def slugify(text):
    return re.sub(r'[\s_-]+', '-', re.sub(r'[^\w\s-]', '', text.lower().strip()))[:80]

def fetch_transcript(url, outpath, title):
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    
    print("  Trying:", title)
    
    # Try subtitles
    cmd = ['yt-dlp', '--no-check-certificate', '--skip-download',
           '--write-auto-subs', '--sub-lang', 'en',
           '--convert-subs', 'srt', '--output', outpath.replace('.txt',''),
           '--no-playlist', '--ignore-errors', url]
    
    subprocess.run(cmd, capture_output=True)
    
    # Check if SRT exists
    base = outpath.replace('.txt', '')
    srt_path = base + '.srt'
    if os.path.exists(srt_path):
        lines = []
        for line in open(srt_path, encoding='utf-8').read().splitlines():
            line = line.strip()
            if line and not re.match(r'^\d+$', line) and not re.match(r'^\d{2}:\d{2}', line):
                clean = re.sub(r'<[^>]+>', '', line)
                if clean:
                    lines.append(clean)
        content = "# Transcript: " + title + "\nSource: " + url + "\nFetched: " + str(date.today()) + "\n\n---\n\n" + "\n".join(lines)
        with open(outpath, 'w', encoding='utf-8') as f:
            f.write(content)
        os.remove(srt_path)
        print("  ✅ SUCCESS transcript:", title)
        return True
    else:
        # Metadata fallback
        cmd2 = ['yt-dlp', '--no-check-certificate', '--skip-download', '--dump-json', url]
        r = subprocess.run(cmd2, capture_output=True, text=True)
        if r.returncode == 0:
            try:
                m = json.loads(r.stdout)
                content = "# Metadata: " + str(m.get('title', title)) + "\n"
                content += "Source: " + url + "\n"
                content += "Uploader: " + str(m.get('uploader', '')) + "\n"
                content += "Date: " + str(m.get('upload_de', '')) + "\n"
                content += "Note: No transcript - using metadata\n\n---\n\n"
                content += str(m.get('description', ''))[:2500]
                with open(outpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print("  📄 Metadata saved for:", title)
                return True
            except:
                pass
        print("  ❌ FAILED:", title)
        return False

print("=== YouTube Transcript Fetcher - FINAL CLEAN VERSION ===")
ok = fail = 0
for expert in TARGETS:
    adir = os.path.join(OUTPUT_DIR, expert['author'])
    os.makedirs(adir, exist_ok=True)
    print("\n=== " + expert['author'] + " ===")
    for v in expert['videos']:
        out = os.path.join(adir, slugify(v['title']) + '.txt')
        if fetch_transcript(v['url'], out, v['title']):
            ok += 1
        else:
            fail += 1

print("\n=== DONE === OK =", ok, "FAIL =", fail)
