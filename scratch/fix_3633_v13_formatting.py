import json
import re

path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/rewrite_3633_v13.json"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

print("Fixing formatting in rewrite_3633_v13.json...")

for ch_idx, chap in enumerate(data.get("chapters", [])):
    content = chap.get("content", "")
    lines = content.strip().split('\n')
    fixed_lines = []
    
    for line_idx, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        has_p_start = line.startswith("<p>")
        has_p_end = line.endswith("</p>")
        
        if has_p_start and has_p_end:
            fixed_lines.append(line)
        elif has_p_start and not has_p_end:
            print(f"  [FIX] Chap {ch_idx+1} Line {line_idx+1}: Appending </p>")
            fixed_lines.append(line + "</p>")
        elif not has_p_start and has_p_end:
            print(f"  [FIX] Chap {ch_idx+1} Line {line_idx+1}: Prepended <p>")
            fixed_lines.append("<p>" + line)
        else:
            print(f"  [FIX] Chap {ch_idx+1} Line {line_idx+1}: Wrapping with <p>...</p>")
            fixed_lines.append("<p>" + line + "</p>")
            
    chap["content"] = "\n".join(fixed_lines)

# Save back
with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Fixing complete!")
