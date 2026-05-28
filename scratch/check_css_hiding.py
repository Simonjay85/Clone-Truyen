import re

css_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/tehi-theme/assets/css/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Let's search for any class names that could hide the main content
# such as .index, .home, #main-content, main, etc. followed by display: none
patterns = [
    r"\.index\s*\{[^}]*display\s*:\s*none",
    r"\.home\s*\{[^}]*display\s*:\s*none",
    r"main\s*\{[^}]*display\s*:\s*none",
    r"#main-content\s*\{[^}]*display\s*:\s*none",
    r"\.mkm-wrap\s*\{[^}]*display\s*:\s*none"
]

print("Searching style.css for display: none patterns:")
found_pattern = False
for p in patterns:
    matches = re.findall(p, css, re.IGNORECASE)
    if matches:
        print(f"  ⚠️ Match found: {matches}")
        found_pattern = True

if not found_pattern:
    print("  No direct display: none found for these classes in style.css.")
    
# Let's list all display: none rules in style.css to see if any are suspicious
print("\nSuspicious display: none rules in style.css:")
matches = re.finditer(r"([^{}\n]+)\{[^}]*display\s*:\s*none[^}]*\}", css, re.IGNORECASE)
for m in list(matches)[:40]:
    selector = m.group(1).strip()
    # Filter for class or id selectors that might affect our layout
    if any(kwd in selector for kwd in ["main", "body", "content", "wrapper", "container", "wrap", "footer", "home", "index"]):
        print(f"  {selector} {{ ... display: none; ... }}")
