import json

PATH = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_7.json"

with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# 1. Check top-level keys
required_keys = ["idx", "title", "author", "genre", "intro", "chapters"]
for key in required_keys:
    if key not in data:
        raise ValueError(f"Missing key: {key}")

# 2. Check intro V13 format
intro = data["intro"]
intro_paragraphs = intro.strip().split("\n")
for p in intro_paragraphs:
    if not p.startswith("<p>") or not p.endswith("</p>"):
        raise ValueError(f"Intro paragraph format error: {p}")

# 3. Check chapters
if len(data["chapters"]) != 10:
    raise ValueError(f"Expected 10 chapters, got {len(data['chapters'])}")

for idx, chap in enumerate(data["chapters"]):
    title = chap["title"]
    content = chap["content"]
    
    # Verify title
    if not title.startswith(f"Chương {idx+1}:"):
        raise ValueError(f"Chapter title format error: {title}")
    
    # Verify content lines (V13)
    paragraphs = content.strip().split("\n")
    for p_idx, p in enumerate(paragraphs):
        p = p.strip()
        if not p:
            continue
        if not p.startswith("<p>") or not p.endswith("</p>"):
            raise ValueError(f"Chapter {idx+1} paragraph {p_idx+1} format error: '{p}'")

print("All HTML and JSON structural validations passed successfully!")
