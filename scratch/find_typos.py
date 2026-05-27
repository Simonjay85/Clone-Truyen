import json

with open("scratch/story_3940_dump.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("=" * 80)
print("🔍 SEARCHING FOR TYPOS IN CHAPTERS CONTENT:")
print("=" * 80)

# Check titles
for idx, ch in enumerate(data["chapters"]):
    title = ch["title"]
    print(f"Chapter {idx + 1} Title: {title}")
    
    # Check duplicate adjacent words
    words = title.split()
    for i in range(len(words) - 1):
        if words[i].lower() == words[i+1].lower() and len(words[i]) > 1:
            print(f"   ⚠️ Duplicate word in title: '{words[i]} {words[i+1]}'")
            
    # Check specific typos
    if "tiêm" in title.lower():
        print(f"   ⚠️ Possible typo in title: 'tiêm' (did you mean 'tim'?)")

print("\n" + "-" * 50 + "\n")

# Check contents
for idx, ch in enumerate(data["chapters"]):
    content = ch["content"]
    # Check duplicate adjacent words in content
    import re
    # Strip HTML tags
    clean_text = re.sub(r'<[^>]*>', ' ', content)
    words = clean_text.split()
    for i in range(len(words) - 1):
        if words[i].lower() == words[i+1].lower() and len(words[i]) > 1:
            # Skip common duplicates if any are standard Vietnamese (like "đi đi", "lần lần", etc.) but print others
            skip = ["đi", "đại", "lại", "ngày", "đêm", "bay", "đang"]
            if words[i].lower() not in skip:
                print(f"Ch {idx + 1} Content duplicate: '{words[i]} {words[i+1]}' near ...{' '.join(words[max(0, i-4):i+5])}...")
