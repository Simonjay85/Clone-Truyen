import json

try:
    with open("existing_novels.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for idx, item in enumerate(data):
            title = item.get("title", "")
            if "đông y" in title.lower() or "bác sĩ" in title.lower():
                print(f"Index: {idx} | ID: {item.get('id')} | Title: {title}")
except Exception as e:
    print("Error:", e)
