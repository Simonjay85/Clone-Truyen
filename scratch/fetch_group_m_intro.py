import requests
import json
import os

STORY_IDS = [2482, 2489, 2497, 2508, 2517]
WP_URL = "https://doctieuthuyet.com"

def main():
    metadata = {}
    for story_id in STORY_IDS:
        url = f"{WP_URL}/wp-json/wp/v2/truyen/{story_id}"
        print(f"Fetching metadata for ID {story_id} from {url}...")
        try:
            res = requests.get(url, timeout=30)
            if res.status_code == 200:
                data = res.json()
                title = data.get("title", {}).get("rendered", "")
                content = data.get("content", {}).get("rendered", "")
                metadata[story_id] = {
                    "id": story_id,
                    "title": title,
                    "content": content
                }
                print(f"✓ Success: '{title}'")
            else:
                print(f"❌ Failed: HTTP {res.status_code}")
        except Exception as e:
            print(f"❌ Error fetching {story_id}: {e}")
            
    os.makedirs("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch", exist_ok=True)
    out_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/group_m_metadata.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    print(f"Saved metadata to {out_path}")

if __name__ == "__main__":
    main()
