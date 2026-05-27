import json
import re
import os

def main():
    json_path = "recent_50_stories_detailed.json"
    if not os.path.exists(json_path):
        print("Error: detailed JSON not found")
        return
        
    with open(json_path, "r", encoding="utf-8") as f:
        stories = json.load(f)
        
    print(f"Loaded {len(stories)} stories.")
    
    # Let's search inside the titles and excerpts for key names
    names_count = {}
    story_details = []
    
    for s in stories:
        text = (s.get("title", "") + " " + s.get("first_chap_excerpt", "") + " " + s.get("last_chap_excerpt", "")).lower()
        
        # Look for standard protagonist names, female leads, and company names
        found_protagonists = []
        found_helpers = []
        found_antagonists = []
        found_companies = []
        
        # Protagonists
        protos = ["hữu nam", "hoài nam", "hải phong", "quốc bảo", "gia bách", "tuấn anh", "văn dũng", "gia huy", "lâm phong", "thế khải", "tấn đạt", "quân", "huy", "đức minh"]
        for p in protos:
            if p in text:
                found_protagonists.append(p)
                
        # Helpers
        helpers = ["hoàng yến", "minh thư", "khánh vy", "mai chi", "thanh mai", "an", "tuyền"]
        for h in helpers:
            if h in text:
                found_helpers.append(h)
                
        # Antagonists
        antags = ["mỹ hạnh", "mỹ linh", "hữu phước", "đại nghĩa", "lý bách", "vinh thịnh", "gia bảo"]
        for a in antags:
            if a in text:
                found_antagonists.append(a)
                
        # Companies
        comps = ["vạn an", "thịnh phát", "đông hải", "cybershield", "southernbank"]
        for c in comps:
            if c in text:
                found_companies.append(c)
                
        story_details.append({
            "id": s["id"],
            "title": s["title"],
            "date": s["date"],
            "protagonists": found_protagonists,
            "helpers": found_helpers,
            "antagonists": found_antagonists,
            "companies": found_companies
        })
        
        # Add to global counts
        for x in found_protagonists + found_helpers + found_antagonists + found_companies:
            names_count[x] = names_count.get(x, 0) + 1
            
    print("\nName distribution across 50 novels:")
    for name, cnt in sorted(names_count.items(), key=lambda item: item[1], reverse=True):
        print(f"  - {name}: {cnt} matches")
        
    print("\nExamples of duplicates:")
    # Find stories that share the same protagonist name
    for p in protos:
        matches = [s for s in story_details if p in s["protagonists"]]
        if len(matches) > 1:
            print(f"\nProtagonist: '{p.upper()}' is repeated in {len(matches)} novels:")
            for m in matches[:5]:
                print(f"  * ID {m['id']}: {m['title']} ({m['date']})")
                
    # Find stories that share 'hoàng yến'
    matches_yeen = [s for s in story_details if "hoàng yến" in s["helpers"]]
    if len(matches_yeen) > 1:
        print(f"\nHelper: 'hoàng yến' (usually CFO of Quỹ Vạn An) is repeated in {len(matches_yeen)} novels:")
        for m in matches_yeen[:5]:
            print(f"  * ID {m['id']}: {m['title']} ({m['date']})")
            
    # Find stories that share 'vạn an'
    matches_van_an = [s for s in story_details if "vạn an" in s["companies"]]
    if len(matches_van_an) > 1:
        print(f"\nCompany: 'vạn an' is repeated in {len(matches_van_an)} novels:")
        for m in matches_van_an[:5]:
            print(f"  * ID {m['id']}: {m['title']} ({m['date']})")

if __name__ == "__main__":
    main()
