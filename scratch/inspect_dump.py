import json

with open("scratch/story_3940_dump.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("=" * 80)
print("📖 INSPECTING DUMP DATA FOR ID 3940:")
print("=" * 80)
print("Story ID:", data["story"]["id"])
print("Story Title:", data["story"]["title"])
print("Story Excerpt:", data["story"]["excerpt"])
print("Number of Chapters:", len(data["chapters"]))
print("-" * 50)

for idx, ch in enumerate(data["chapters"]):
    print(f"Chapter {idx + 1}: {ch['title']} (ID: {ch['id']})")
    print(f"Content length: {len(ch['content'])} characters")
    print(f"Content preview: {ch['content'][:200]}...")
    print("-" * 50)
