import re

with open("scratch/live_homepage.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's clean up script and style tags to avoid counting divs inside scripts or styles
html_clean = re.sub(r'<script.*?>.*?</script>', '', html, flags=re.DOTALL)
html_clean = re.sub(r'<style.*?>.*?</style>', '', html_clean, flags=re.DOTALL)
html_clean = re.sub(r'<!--.*?-->', '', html_clean, flags=re.DOTALL)

# Let's find all HTML tags (only div, main, header, footer)
tags = re.findall(r'<(/?(?:div|main|header|footer)(?:\s+[^>]*)?)>', html_clean, re.IGNORECASE)

stack = []
mismatches = []

for idx, full_tag in enumerate(tags):
    # Parse tag name and type
    tag_clean = full_tag.strip().split()[0].lower()
    is_closing = tag_clean.startswith('/')
    tag_name = tag_clean.replace('/', '')
    
    if not is_closing:
        stack.append((tag_name, idx, full_tag))
    else:
        if not stack:
            print(f"⚠️ EXTRA CLOSING TAG: </{tag_name}> at tag index {idx} ({full_tag})")
            mismatches.append((None, tag_name, full_tag))
        else:
            last_open, last_idx, last_full = stack.pop()
            if last_open != tag_name:
                print(f"⚠️ MISMATCH: Opened <{last_open}> ({last_full}) closed by </{tag_name}> ({full_tag})")
                mismatches.append((last_open, tag_name, full_tag))

print(f"\nParsing complete. Remaining unclosed tags in stack: {len(stack)}")
for item in stack[:20]:
    print(f"  Unclosed <{item[0]}> opened at tag index {item[1]} ({item[2]})")
