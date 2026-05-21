import json

with open("existing_novels.json", "r", encoding="utf-8") as f:
    existing = json.load(f)

with open("scratch/pipeline_50.json", "r", encoding="utf-8") as f:
    pipeline = json.load(f)

print(f"Loaded {len(existing)} existing novels and {len(pipeline)} pipeline novels.")

existing_titles = [x["title"].lower() for x in existing]
existing_slugs = [x.get("slug", "").lower() for x in existing]
existing_intros = [x.get("intro", "").lower() for x in existing]

missing = []
for p in pipeline:
    title = p["title"]
    # Check if title or similar title is already published
    found = False
    for ext in existing:
        ext_title = ext["title"].lower()
        ext_intro = ext.get("intro", "").lower()
        ext_slug = ext.get("slug", "").lower()
        # check for substring overlap or exact matches
        if p["title"].lower() in ext_title or ext_title in p["title"].lower():
            found = True
            p["existing_id"] = ext["id"]
            p["existing_title"] = ext["title"]
            break
        # Also check based on setting / protagonist keywords
        proto_last = p["protagonist"].split(",")[0].split()[-1].lower() if p["protagonist"] else ""
        if proto_last and proto_last in ext_intro:
            # check if title similarity is also high or setting matches
            if p["setting"].split(",")[0].lower() in ext_intro:
                found = True
                p["existing_id"] = ext["id"]
                p["existing_title"] = ext["title"]
                break
                
    if not found:
        missing.append(p)

print(f"\nFound {len(pipeline) - len(missing)} already published/matched from pipeline.")
print(f"Missing ({len(missing)}):")
for m in missing:
    print(f"  ID {m['id']}: {m['title']} | Protagonist: {m['protagonist']} | Setting: {m['setting']}")

# Let's save matched ones
matched = [p for p in pipeline if "existing_id" in p]
with open("scratch/matched_pipeline.json", "w", encoding="utf-8") as f:
    json.dump(matched, f, ensure_ascii=False, indent=2)

with open("scratch/missing_pipeline.json", "w", encoding="utf-8") as f:
    json.dump(missing, f, ensure_ascii=False, indent=2)
