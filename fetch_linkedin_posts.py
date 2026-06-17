import os, sys, json, time, requests
from datetime import datetime, timezone

APIFY_TOKEN = os.environ.get('APIFY_TOKEN', '')
ACTOR_ID = 'harvestapi~linkedin-profile-posts'
APIFY_BASE = 'https://api.apify.com/v2'
OUTPUT_DIR = 'research/linkedin-posts'
MAX_POSTS = 5

EXPERTS = [
    {'slug': 'armand-farrokh', 'name': 'Armand Farrokh', 'url': 'https://www.linkedin.com/in/armandfarrokh/'},
    {'slug': 'nick-cegelski', 'name': 'Nick Cegelski', 'url': 'https://www.linkedin.com/in/ncegelski/'},
    {'slug': 'jason-bay', 'name': 'Jason Bay', 'url': 'https://www.linkedin.com/in/jasondbay/'},
    {'slug': 'alex-berman', 'name': 'Alex Berman', 'url': 'https://www.linkedin.com/in/alexanderberman/'},
    {'slug': 'belal-batrawy', 'name': 'Belal Batrawy', 'url': 'https://www.linkedin.com/in/belbatrawy/'},
    {'slug': 'nick-abraham', 'name': 'Nick Abraham', 'url': 'https://www.linkedin.com/in/nickabraham12/'},
    {'slug': 'jeremy-chatelaine', 'name': 'Jeremy Chatelaine', 'url': 'https://www.linkedin.com/in/jeremychatelaine/'},
    {'slug': 'vin-matano', 'name': 'Vin Matano', 'url': 'https://www.linkedin.com/in/vinmatano/'},
    {'slug': 'jen-allen-knuth', 'name': 'Jen Allen-Knuth', 'url': 'https://www.linkedin.com/in/jenallenknuth/'},
    {'slug': 'vincent-fourcade', 'name': 'Vincent Fourcade', 'url': 'https://www.linkedin.com/in/vincentfourcade/'},
]

def run_actor(url, max_posts):
    params = {'token': APIFY_TOKEN}
    resp = requests.post(
        APIFY_BASE + '/acts/' + ACTOR_ID + '/runs',
        json={'profileUrls': [url], 'maxPosts': max_posts},
        params=params, timeout=30
    )
    resp.raise_for_status()
    run_id = resp.json()['data']['id']
    print('    Run: ' + run_id)
    for i in range(36):
        time.sleep(5)
        r = requests.get(APIFY_BASE + '/actor-runs/' + run_id, params=params, timeout=10)
        status = r.json()['data']['status']
        print('    ' + str(i*5) + 's status=' + status)
        if status in ('SUCCEEDED', 'FAILED', 'ABORTED', 'TIMED-OUT'):
            break
    if status != 'SUCCEEDED':
        return []
    dataset_id = r.json()['data']['defaultDatasetId']
    items = requests.get(APIFY_BASE + '/datasets/' + dataset_id + '/items', params=dict(params, clean=True), timeout=30)
    return items.json()

def save(expert, posts):
    d = os.path.join(OUTPUT_DIR, expert['slug'])
    os.makedirs(d, exist_ok=True)
    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    md = ['# LinkedIn Posts: ' + expert['name'], '', 'URL: ' + expert['url'], 'Date: ' + today, 'Count: ' + str(len(posts)), '', '---', '']
    for i, p in enumerate(posts, 1):
        if isinstance(p, dict):
            text = str(p.get('text') or p.get('content') or p.get('commentary') or '')
            date = str(p.get('postedAt') or p.get('publishedAt') or '')[:10]
            likes = str(p.get('likes') or p.get('numLikes') or 0)
            link = str(p.get('postUrl') or p.get('url') or '')
        else:
            text = str(p)
            date = ''
            likes = '0'
            link = ''
        md += ['### Post ' + str(i), 'Date: ' + date + ' | Likes: ' + likes, 'URL: ' + link, '', text, '', '---', '']
    open(os.path.join(d, expert['slug'] + '-posts.md'), 'w').write('\n'.join(md))
    json.dump(posts, open(os.path.join(d, expert['slug'] + '-raw.json'), 'w'), ensure_ascii=False, indent=2)
    print('    Saved ' + str(len(posts)) + ' posts')

def placeholder(expert, reason):
    d = os.path.join(OUTPUT_DIR, expert['slug'])
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, expert['slug'] + '-posts.md'), 'w').write('# ' + expert['name'] + '\nNo posts: ' + reason + '\n')
    print('    Placeholder saved')

if not APIFY_TOKEN:
    print('ERROR: set APIFY_TOKEN')
    sys.exit(1)

print('Starting | Experts: ' + str(len(EXPERTS)))
ok = fail = 0
for i, e in enumerate(EXPERTS, 1):
    print('[' + str(i) + '/' + str(len(EXPERTS)) + '] ' + e['name'])
    try:
        posts = run_actor(e['url'], MAX_POSTS)
        if posts:
            save(e, posts)
            ok += 1
        else:
            placeholder(e, 'empty')
            fail += 1
    except Exception as ex:
        print('    ERR: ' + str(ex))
        placeholder(e, str(ex))
        fail += 1
    if i < len(EXPERTS):
        time.sleep(2)

print('DONE ok=' + str(ok) + ' fail=' + str(fail))