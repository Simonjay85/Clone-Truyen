import requests
import json

ids = [2238, 2249, 2259, 2269, 2279]
print("=" * 60)
print("🔍 VERIFYING GROUP K STORIES STATUS ON WORDPRESS 🔍")
print("=" * 60)

for story_id in ids:
    url = f"https://doctieuthuyet.com/wp-json/wp/v2/truyen/{story_id}"
    try:
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            data = res.json()
            title = data.get("title", {}).get("rendered", "N/A")
            meta = data.get("meta", {})
            focus_keyword = meta.get("rank_math_focus_keyword", "N/A")
            chapter_count = meta.get("_chapter_count", "N/A")
            print(f"ID: {story_id}")
            print(f"  Title: {title}")
            print(f"  Focus Keyword: {focus_keyword}")
            print(f"  Chapters: {chapter_count}")
        elif res.status_code == 404:
            print(f"ID: {story_id} - NOT FOUND (404)")
        else:
            print(f"ID: {story_id} - HTTP Error {res.status_code}")
    except Exception as e:
        print(f"ID: {story_id} - Exception: {e}")
    print("-" * 60)
