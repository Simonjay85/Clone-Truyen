import sys
import os
import json

sys.path.insert(0, '.')
from scratch.novel_editor import *

def main():
    upload_helper()
    try:
        for story_id in [1948, 1933, 1927, 2227]:
            print(f"Fetching story {story_id}...")
            res = get_story_chapters(story_id)
            if res.get('success'):
                with open(f"scratch/original_{story_id}.json", "w", encoding="utf-8") as f:
                    json.dump(res, f, ensure_ascii=False, indent=2)
                print(f"  Saved scratch/original_{story_id}.json")
            else:
                print(f"  Error: {res}")
    finally:
        remove_helper()

if __name__ == "__main__":
    main()
