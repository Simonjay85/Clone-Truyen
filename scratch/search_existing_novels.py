import json

fpath = "/Users/aaronnguyen/TN/App/doctieuthuyet/existing_novels.json"
with open(fpath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for novel in data:
    if novel.get('id') == 2227 or "Đà Lạt" in novel.get('title', '') or "Đà Lạt" in novel.get('intro', '') or "2227" in str(novel.get('id', '')):
        print("--- MATCH FOUND ---")
        print(json.dumps(novel, ensure_ascii=False, indent=2))
        print("-------------------")
