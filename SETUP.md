# Setn up Apify
Go to https://apify.com — free, no credit card, get $5 credit

## Step 2 — Get API Token
console.apify.com/settings/integrations — Create new token — copy it

## Step 3 — Install deps
pip3 install requests yt-dlp

## Step 4 — Run LinkedIn script (Mac)
APIFY_TOKEN=apify_api_XXXXXXXX python3 fetch_linkedin_posts.py

## Step 5 — Run YouTube script
python3 fetch_transcripts.py

## Step 6 — Commit
git add research/
git commit -m "add: linkedin posts and youtube transcripts collected"
git push origin main

## Cost: ~0.06 USD for 10 experts x 5 posts (within $5 free credit)