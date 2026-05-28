import re

with open("scratch/live_homepage.html", "r", encoding="utf-8") as f:
    html = f.read()

links = re.findall(r'<link\s+[^>]*rel=["\']stylesheet["\'][^>]*>', html, re.IGNORECASE)
print(f"Found {len(links)} stylesheet links:")
for l in links:
    href_match = re.search(r'href=["\'](.*?)["\']', l)
    if href_match:
        print(f"  - {href_match.group(1)}")
