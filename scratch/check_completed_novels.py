import os
import json

target_indices = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
base_dir = "/Users/aaronnguyen/TN/App/doctieuthuyet"

print("Pregenerated files check:")
print("-------------------------")
for idx in target_indices:
    completed_file = os.path.join(base_dir, f"pending_novel_{idx}.json")
    temp_file = os.path.join(base_dir, f"pending_novel_{idx}_temp.json")
    
    if os.path.exists(completed_file):
        try:
            with open(completed_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            chapters = data.get("chapters", [])
            print(f"Index {idx}: COMPLETE -> Title: '{data.get('title')}', Chapters: {len(chapters)}")
            for c_idx, chap in enumerate(chapters):
                words = len(chap.get("content", "").split())
                print(f"  -> Chap {c_idx+1}: {chap.get('title')} ({words} words)")
        except Exception as e:
            print(f"Index {idx}: Error reading complete file: {e}")
    elif os.path.exists(temp_file):
        try:
            with open(temp_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            chapters = data.get("chapters", [])
            print(f"Index {idx}: TEMP -> Chapters: {len(chapters)}")
        except Exception as e:
            print(f"Index {idx}: Error reading temp file: {e}")
    else:
        print(f"Index {idx}: NOT FOUND")
