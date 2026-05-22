import requests
import json

ids = [1921, 1927, 1933, 1948, 1968]
for story_id in ids:
    url = f"https://doctieuthuyet.com/wp-json/wp/v2/truyen/{story_id}"
    try:
        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            data = r.json()
            print(f"ID: {story_id}")
            print(f"Title: {data.get('title', {}).get('rendered', '')}")
            # print link
            print(f"Link: {data.get('link', '')}")
            print(f"Intro (truncated): {data.get('content', {}).get('rendered', '')[:500]}...")
            print("-" * 40)
        else:
            print(f"ID: {story_id} failed with status {r.status_code}")
    except Exception as e:
        print(f"ID: {story_id} error: {e}")
