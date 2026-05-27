#!/usr/bin/env python3
import json
import glob
import os
import re

def analyze():
    # Load all json drafts in scratch/
    draft_files = glob.glob("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/rewrite_*_v13.json")
    # Add the dumped 3940 story
    dump_3940 = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/story_3940_dump.json"
    if os.path.exists(dump_3940):
        draft_files.append(dump_3940)
        
    print(f"Found {len(draft_files)} draft files to analyze.")
    
    cliches = {
        "Vietcombank": [r"Vietcombank", r"phong tỏa tài khoản"],
        "C03 Bộ Công an": [r"C03", r"Bộ Công an", r"cảnh sát kinh tế"],
        "Bẻ gãy thẻ hành nghề/nhân viên": [r"bẻ gãy", r"bẻ làm đôi", r"giật phăng"],
        "Maybach/Rolls-Royce": [r"Maybach", r"Rolls-Royce"],
        "Chiếc nhẫn nảy lên": [r"nhẫn", r"nảy lên", r"góc tối"],
        "Vận An / Quỹ Vạn An": [r"Vạn An", r"Trịnh Vạn An"],
        "Mỹ Hạnh / Mỹ Linh phản bội": [r"Mỹ Hạnh", r"Mỹ Linh"],
        "Khẩy môi cười nham hiểm": [r"khẩy môi", r"nham hiểm", r"đắc ý"],
        "Đông y / châm cứu rác rưởi": [r"châm cứu rác", r"bốc lá cây"],
        "Thử thách Landmark 81": [r"Landmark 81", r"sính lễ 5 tỷ"],
        "Commit Git / Bằng chứng IT": [r"commit Git", r"mã băm", r"SHA-256"]
    }
    
    statistics = {k: 0 for k in cliches}
    occurrences = {k: [] for k in cliches}
    
    for fpath in draft_files:
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # Combine all text content from the draft
            full_text = ""
            title = ""
            if "chapters" in data: # story_3940_dump style
                title = data.get("story", {}).get("title", "")
                for ch in data["chapters"]:
                    full_text += " " + ch.get("content", "")
            else: # rewrite_* style (which might have title and sections or chapters)
                title = data.get("title", "")
                if "chapters" in data:
                    for ch in data["chapters"]:
                        full_text += " " + ch.get("content", "")
                elif "sections" in data:
                    for s in data["sections"]:
                        full_text += " " + s.get("content", "")
                else:
                    full_text += " " + json.dumps(data, ensure_ascii=False)
            
            full_text = re.sub(r'<[^>]+>', ' ', full_text)
            
            # Check patterns
            for key, patterns in cliches.items():
                found = False
                for pat in patterns:
                    if re.search(pat, full_text, re.IGNORECASE) or re.search(pat, title, re.IGNORECASE):
                        found = True
                        break
                if found:
                    statistics[key] += 1
                    occurrences[key].append(f"{os.path.basename(fpath)}: {title[:40]}...")
        except Exception as e:
            print(f"Error reading {fpath}: {e}")
            
    print("\n=== CLICHE AND PROSE ANALYSIS RESULTS ===")
    for key, count in statistics.items():
        percentage = (count / len(draft_files)) * 100 if draft_files else 0
        print(f"\n* {key}: {count} stories ({percentage:.1f}%)")
        print("  Examples:")
        for occ in occurrences[key][:3]:
            print(f"    - {occ}")

if __name__ == "__main__":
    analyze()
