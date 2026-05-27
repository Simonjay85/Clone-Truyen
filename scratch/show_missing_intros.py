import json

def main():
    missing_ids = [2710, 3724, 3743, 3755, 3767, 3769, 3789, 3801, 3813, 3825, 3837, 3849, 3861, 3873, 3920, 3930, 3940, 3954, 3998, 4036]
    
    with open("existing_novels.json", "r", encoding="utf-8") as f:
        novels = json.load(f)
        
    for novel in novels:
        nid = novel.get("id")
        if nid in missing_ids:
            title = novel.get("title")
            intro = novel.get("intro", "")
            print("="*60)
            print(f"ID: {nid} | Title: {title}")
            print(f"Intro: {intro}")
            print("="*60)

if __name__ == "__main__":
    main()
