import os
import json
import re

def clean_html(text):
    if not text:
        return ""
    # Standardize curly quotes and amp; entities if any
    text = text.replace("&ldquo;", "“").replace("&rdquo;", "”")
    text = text.replace("&quot;", "\"").replace("&apos;", "'")
    text = text.replace("&amp;", "&")
    # Clean up double spacing
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def main():
    scratch_dir = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch"
    registry_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/existing_novels.json"
    
    with open(registry_path, "r", encoding="utf-8") as f:
        novels = json.load(f)
        
    print(f"Loaded {len(novels)} novels from registry.")
    
    payload = {}
    
    for i, novel in enumerate(novels):
        nid = novel.get("id")
        title_reg = novel.get("title")
        intro_reg = novel.get("intro", "")
        
        # Check if v13 rewrite file exists
        v13_path = os.path.join(scratch_dir, f"rewrite_{nid}_v13.json")
        title_to_use = title_reg
        intro_to_use = intro_reg
        
        source = "registry"
        if os.path.exists(v13_path):
            try:
                with open(v13_path, "r", encoding="utf-8") as vf:
                    v13_data = json.load(vf)
                title_to_use = v13_data.get("title", title_reg)
                intro_to_use = v13_data.get("intro", intro_reg)
                source = "v13_file"
            except Exception as e:
                print(f"Error reading v13 file for ID {nid}: {e}")
                
        # Minor fallback checks: make sure it is not truncated
        intro_cleaned = clean_html(intro_to_use)
        if len(intro_cleaned) < 50:
            print(f"⚠️ Warning: ID {nid} has an extremely short introduction ({len(intro_cleaned)} chars)!")
            
        payload[str(nid)] = {
            "title": title_to_use,
            "intro": intro_to_use
        }
        
        print(f"[{i+1}/{len(novels)}] Matched ID {nid} -> Title: '{title_to_use[:40]}...' | Source: {source} | Length: {len(intro_to_use)} chars")
        
    out_path = os.path.join(scratch_dir, "all_descriptions_update.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=4)
        
    print(f"🎉 Payload prepared successfully! Saved to {out_path}")

if __name__ == "__main__":
    main()
