import json
import requests
import os

ids = [2549, 2561, 2573, 2587, 2606, 2658]
results = {}

print("Fetching metadata for Group N...")
for story_id in ids:
    url = f"https://doctieuthuyet.com/wp-json/wp/v2/truyen/{story_id}"
    try:
        r = requests.get(url, verify=False, timeout=15)
        if r.status_code == 200:
            data = r.json()
            results[str(story_id)] = {
                "id": story_id,
                "title": data.get("title", {}).get("rendered", ""),
                "content": data.get("content", {}).get("rendered", "")
            }
            print(f"✓ Fetched story {story_id}: {results[str(story_id)]['title']}")
        else:
            print(f"❌ Failed to fetch story {story_id}: Status {r.status_code}")
    except Exception as e:
        print(f"❌ Error fetching story {story_id}: {e}")

os.makedirs("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch", exist_ok=True)
out_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/group_n_metadata.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Saved metadata to {out_path}")
