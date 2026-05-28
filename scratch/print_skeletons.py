import re

with open("scratch/live_homepage.html", "r", encoding="utf-8") as f:
    html = f.read()

# Search for vh-skeleton occurrences with 100 characters of context
for m in re.finditer(r'vh-skeleton', html):
    start = max(0, m.start() - 100)
    end = min(len(html), m.end() + 100)
    print("\n--- OCCURRENCE ---")
    print(html[start:end])
