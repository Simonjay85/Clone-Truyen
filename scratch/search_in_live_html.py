import re

with open("scratch/live_homepage.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's find all style blocks
style_blocks = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
print(f"Analyzing {len(style_blocks)} style blocks...")

for idx, block in enumerate(style_blocks, 1):
    # Find any rule that targets .mkm-wrap or has display: none / visibility: hidden
    lines = block.split("\n")
    found = []
    for line in lines:
        if "mkm-wrap" in line or "mkm-body" in line or "mkm-footer-top" in line or "display" in line or "visibility" in line:
            found.append(line.strip())
            
    if found:
        print(f"\n--- Style Block {idx} ---")
        for f_line in found[:15]:
            print(f"  {f_line}")
        if len(found) > 15:
            print("  ...")
