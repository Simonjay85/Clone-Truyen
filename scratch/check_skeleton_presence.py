with open("scratch/live_homepage.html", "r", encoding="utf-8") as f:
    html = f.read()

skeleton_count = html.count("vh-skeleton")
print(f"Number of occurrences of 'vh-skeleton' in HTML: {skeleton_count}")

# Print where they occur
import re
matches = re.finditer(r'<[^>]*class="[^"]*vh-skeleton[^"]*"[^>]*>', html, re.IGNORECASE)
for m in list(matches)[:20]:
    print("  -", m.group(0))
