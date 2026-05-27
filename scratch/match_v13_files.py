import os
import glob
import json

def main():
    scratch_dir = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch"
    registry_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/existing_novels.json"
    
    with open(registry_path, "r", encoding="utf-8") as f:
        novels = json.load(f)
        
    novel_ids = [n.get("id") for n in novels]
    print(f"Total novels in registry: {len(novel_ids)}")
    
    v13_files = glob.glob(os.path.join(scratch_dir, "rewrite_*_v13.json"))
    v13_ids = []
    for fpath in v13_files:
        fname = os.path.basename(fpath)
        try:
            nid = int(fname.split("_")[1])
            v13_ids.append(nid)
        except Exception:
            pass
            
    print(f"Total rewrite_*_v13.json files: {len(v13_ids)}")
    
    matched = set(novel_ids).intersection(set(v13_ids))
    missing = set(novel_ids) - set(v13_ids)
    
    print(f"Matched stories: {len(matched)}")
    print(f"Missing stories: {len(missing)} (IDs: {sorted(list(missing))})")

if __name__ == "__main__":
    main()
