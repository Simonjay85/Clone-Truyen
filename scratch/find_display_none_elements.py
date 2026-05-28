import re

with open("scratch/live_homepage.html", "r", encoding="utf-8") as f:
    html = f.read()

# Search for style="display:none" or display: none in style attribute
matches = re.finditer(r'<[^>]*style="[^"]*display\s*:\s*none[^"]*"[^>]*>', html, re.IGNORECASE)

for idx, m in enumerate(matches, 1):
    start = max(0, m.start() - 150)
    end = min(len(html), m.end() + 150)
    print(f"\n--- ELEMENT {idx} ---")
    print(html[start:end])
