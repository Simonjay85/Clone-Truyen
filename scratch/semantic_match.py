import json

with open("existing_novels.json", "r", encoding="utf-8") as f:
    existing = json.load(f)

with open("scratch/pipeline_50.json", "r", encoding="utf-8") as f:
    pipeline = json.load(f)

print(f"Loaded {len(existing)} existing novels and {len(pipeline)} pipeline novels.")

matched_pipeline_ids = []
matches = []

for ext in existing:
    ext_title = ext["title"].lower()
    ext_intro = ext.get("intro", "").lower()
    
    # Try to find a match in the pipeline
    best_match = None
    best_score = 0
    
    for p in pipeline:
        if p["id"] in matched_pipeline_ids:
            continue
            
        # Score based on title keyword overlap
        title_words = set(p["title"].lower().replace(",", "").replace(":", "").split())
        ext_title_words = set(ext_title.replace(",", "").replace(":", "").split())
        common_words = title_words.intersection(ext_title_words)
        
        # Filter out common stop words in Vietnamese
        stop_words = {"và", "của", "tôi", "là", "bị", "vì", "để", "ra", "ngày", "trước", "mặt", "họ", "anh", "cô", "ta", "người", "được", "bằng", "lộ", "thân", "phận", "thật"}
        common_words = {w for w in common_words if w not in stop_words}
        
        score = len(common_words)
        
        # Check protagonist name match
        proto_name = p["protagonist"].split(",")[0].strip()
        proto_words = proto_name.lower().split()
        proto_last = proto_words[-1] if proto_words else ""
        
        if proto_last and (proto_last in ext_title or proto_last in ext_intro):
            score += 3
        if proto_name.lower() in ext_intro:
            score += 5
            
        # Check setting match
        setting_city = p["setting"].split(",")[0].strip().lower()
        if setting_city and (setting_city in ext_title or setting_city in ext_intro):
            score += 2
            
        if score > best_score and score >= 2:
            best_score = score
            best_match = p
            
    if best_match:
        matched_pipeline_ids.append(best_match["id"])
        matches.append({
            "pipeline_id": best_match["id"],
            "pipeline_title": best_match["title"],
            "existing_id": ext["id"],
            "existing_title": ext["title"],
            "match_score": best_score
        })

print(f"\nSuccessfully matched {len(matches)} novels between existing and pipeline:")
matches = sorted(matches, key=lambda x: x["pipeline_id"])
for m in matches:
    print(f"  Pipeline ID {m['pipeline_id']} -> Existing ID {m['existing_id']}: '{m['pipeline_title'][:30]}...' matched with '{m['existing_title'][:30]}...' (Score: {m['match_score']})")

missing_ids = [p["id"] for p in pipeline if p["id"] not in matched_pipeline_ids]
print(f"\nMissing Pipeline IDs ({len(missing_ids)}): {missing_ids}")
print("Details of first few missing pipeline novels:")
for pid in missing_ids[:5]:
    p = next(x for x in pipeline if x["id"] == pid)
    print(f"  ID {p['id']}: {p['title']}")
