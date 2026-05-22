import json

def main():
    with open("scratch/full_site_audit.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
    stories = data["stories"]
    print(f"Total stories loaded: {len(stories)}")
    
    # 1. Analyze genres (the_loai)
    genre_counts = {}
    no_genre_stories = []
    for s in stories:
        genres = s["genres"]
        if not genres:
            no_genre_stories.append(s)
        for g in genres:
            name = g["name"]
            genre_counts[name] = genre_counts.get(name, 0) + 1
            
    print("\n--- GENRE DISTRIBUTION ---")
    for name, count in sorted(genre_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  * {name}: {count} stories")
        
    print(f"\nStories with NO genre: {len(no_genre_stories)}")
    for s in no_genre_stories[:10]:
        print(f"  - ID {s['id']}: {s['title']}")
        
    # 2. Analyze alt text
    alt_counts = {"empty": 0, "filled": 0}
    empty_alt_stories = []
    for s in stories:
        alt = s["alt_text"]
        if not alt or alt.strip() == "":
            alt_counts["empty"] += 1
            empty_alt_stories.append(s)
        else:
            alt_counts["filled"] += 1
            
    print("\n--- ALT TEXT STATUS ---")
    print(f"  * Empty Alt: {alt_counts['empty']}")
    print(f"  * Filled Alt: {alt_counts['filled']}")
    print("Some stories with empty Alt:")
    for s in empty_alt_stories[:10]:
         print(f"  - ID {s['id']}: {s['title']}")
         
    # 3. Analyze comments
    comments_stats = {"total_comments": 0, "stories_with_comments": 0, "stories_without_comments": 0}
    no_comments_stories = []
    for s in stories:
        count = s["comments_count"]
        comments_stats["total_comments"] += count
        if count > 0:
            comments_stats["stories_with_comments"] += 1
        else:
            comments_stats["stories_without_comments"] += 1
            no_comments_stories.append(s)
            
    print("\n--- COMMENTS STATUS ---")
    print(f"  * Total comments: {comments_stats['total_comments']}")
    print(f"  * Stories with comments: {comments_stats['stories_with_comments']}")
    print(f"  * Stories without comments: {comments_stats['stories_without_comments']}")
    print("Some stories with no comments:")
    for s in no_comments_stories[:10]:
        print(f"  - ID {s['id']}: {s['title']}")
        
    # 4. Analyze RankMath
    rm_stats = {"empty_title": 0, "empty_desc": 0, "empty_key": 0, "completed": 0}
    incomplete_rm = []
    for s in stories:
        rm = s["rank_math"]
        title_empty = not rm.get("title")
        desc_empty = not rm.get("description")
        key_empty = not rm.get("keyword")
        
        if title_empty: rm_stats["empty_title"] += 1
        if desc_empty: rm_stats["empty_desc"] += 1
        if key_empty: rm_stats["empty_key"] += 1
        
        if not title_empty and not desc_empty and not key_empty:
            rm_stats["completed"] += 1
        else:
            incomplete_rm.append(s)
            
    print("\n--- RANKMATH SEO STATUS ---")
    print(f"  * Empty Title: {rm_stats['empty_title']}")
    print(f"  * Empty Description: {rm_stats['empty_desc']}")
    print(f"  * Empty Focus Keyword: {rm_stats['empty_key']}")
    print(f"  * Fully Completed SEO: {rm_stats['completed']}")
    print("Some stories with incomplete SEO:")
    for s in incomplete_rm[:10]:
        print(f"  - ID {s['id']}: {s['title']} (Title: {'OK' if s['rank_math']['title'] else 'EMPTY'}, Desc: {'OK' if s['rank_math']['description'] else 'EMPTY'}, Keyword: {'OK' if s['rank_math']['keyword'] else 'EMPTY'})")

if __name__ == "__main__":
    main()
