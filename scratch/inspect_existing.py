import json
import os

existing_path = "existing_novels.json"
pipeline_path = "scratch/pipeline_50.json"

if os.path.exists(existing_path):
    with open(existing_path, "r", encoding="utf-8") as f:
        existing = json.load(f)
else:
    existing = []

if os.path.exists(pipeline_path):
    with open(pipeline_path, "r", encoding="utf-8") as f:
        pipeline = json.load(f)
else:
    pipeline = []

print(f"Total existing novels in registry: {len(existing)}")
print(f"Total pipeline planned novels: {len(pipeline)}")

existing_titles = {e['title'].strip().lower() for e in existing}
pipeline_map = {p['id']: p for p in pipeline}

print("\nExisting novels list:")
for e in existing:
    print(f"- ID {e.get('id')}: {e['title']} (slug: {e.get('slug')})")

print("\nChecking matching in pipeline:")
for p in pipeline:
    p_title = p['title'].strip().lower()
    matched = False
    for e in existing:
        if e['title'].strip().lower() == p_title or e.get('slug', '').endswith(p.get('title', '').lower().replace(" ", "-")):
            matched = True
            break
    if matched:
        print(f"✓ Pipeline ID {p['id']} is PUBLISHED: {p['title']}")
    else:
        print(f"❌ Pipeline ID {p['id']} is PENDING: {p['title']}")
