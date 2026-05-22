import json
import os
import glob

print("============================================================")
print("🔍 BATCH 4 DRAFT VERIFICATION TOOL")
print("============================================================")

batch_ids = [20, 21, 22, 23, 24]
for nid in batch_ids:
    path = f"scratch/draft_novel_{nid}.json"
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            chaps = data.get("chapters", [])
            print(f"\n✅ Novel ID {nid} (FOUND)")
            print(f"   Title:  {data.get('title')}")
            print(f"   Author: {data.get('author')}")
            print(f"   Intro:  {len(data.get('intro', ''))} chars")
            print(f"   Chapters count: {len(chaps)}")
            all_chaps_ok = True
            for i, c in enumerate(chaps):
                content = c.get("content", "")
                words = len(content.split())
                paragraphs = content.count("<p>")
                starts_p = content.strip().startswith("<p>")
                ends_p = content.strip().endswith("</p>")
                print(f"     • Chap {i+1}: '{c.get('title')}' -> {words} words, {paragraphs} paragraphs | Starts <p>: {starts_p}, Ends </p>: {ends_p}")
                if words < 1100 or not starts_p or not ends_p:
                    all_chaps_ok = False
            if all_chaps_ok:
                print(f"   👉 COMPLIANCE: 100% V12 PASSED")
            else:
                print(f"   👉 COMPLIANCE: FAILED V12 (check word count or paragraph wrappers)")
        except Exception as e:
            print(f"\n❌ Novel ID {nid} (READ ERROR): {e}")
    else:
        print(f"\n⏳ Novel ID {nid} (PENDING/NOT CREATED YET)")
print("============================================================")
