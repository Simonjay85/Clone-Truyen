import requests
import json
import os

ids = [2089, 2099, 2106, 2112, 2120]
results = {}

for idx in ids:
    url = f"https://doctieuthuyet.com/wp-json/wp/v2/truyen/{idx}"
    try:
        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            data = r.json()
            results[idx] = {
                "title": data.get("title", {}).get("rendered", ""),
                "slug": data.get("slug", ""),
                "content": data.get("content", {}).get("rendered", ""),
                "meta": data.get("meta", {})
            }
            print(f"Successfully fetched details for ID: {idx}")
        else:
            print(f"Failed to fetch ID: {idx}, status: {r.status_code}")
    except Exception as e:
        print(f"Error fetching ID {idx}: {e}")

os.makedirs("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch", exist_ok=True)
with open("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/story_details.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("Saved to scratch/story_details.json")
