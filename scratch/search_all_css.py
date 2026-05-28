import os
import re

css_dirs = [
    "/Users/aaronnguyen/TN/App/doctieuthuyet/tehi-theme/",
    "/Users/aaronnguyen/TN/App/doctieuthuyet/tehi-theme/assets/css/"
]

keywords = [r"display\s*:\s*none", r"visibility\s*:\s*hidden", r"opacity\s*:\s*0"]

for d in css_dirs:
    if not os.path.exists(d):
        continue
    for f in os.listdir(d):
        if f.endswith(".css"):
            path = os.path.join(d, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            # Search for mkm-wrap, mkm-body, main, etc.
            matches_hiding = []
            for kw in keywords:
                for match in re.finditer(r'([^{}\n]+)\{[^}]*' + kw + r'[^}]*\}', content, re.IGNORECASE):
                    selector = match.group(1).strip()
                    if any(x in selector for x in ["mkm", "main", "body", "content", "wrap", "container", "footer", "home"]):
                        matches_hiding.append((kw, selector))
            
            if matches_hiding:
                print(f"\n--- File: {f} ---")
                for kw, sel in matches_hiding:
                    print(f"  [{kw}] {sel}")
