import requests
import json

ids = [2780, 2787, 2794, 2801, 2808]
results = {}

for truyen_id in ids:
    url = f"https://doctieuthuyet.com/wp-json/wp/v2/truyen/{truyen_id}"
    try:
        res = requests.get(url, timeout=15)
        if res.status_code == 200:
            data = res.json()
            results[truyen_id] = {
                "title": data.get("title", {}).get("rendered", ""),
                "content": data.get("content", {}).get("rendered", ""),
                "slug": data.get("slug", "")
            }
            print(f"✓ Fetched ID {truyen_id}: {results[truyen_id]['title']}")
        else:
            print(f"❌ Failed to fetch ID {truyen_id}: Status {res.status_code}")
    except Exception as e:
        print(f"❌ Error fetching ID {truyen_id}: {e}")

with open("scratch/fetched_novels.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("✓ Saved fetched novels to scratch/fetched_novels.json")
