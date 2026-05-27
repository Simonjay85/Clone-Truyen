import os
import glob
import json

def main():
    scratch_dir = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch"
    missing_ids = [2710, 3724, 3743, 3755, 3767, 3769, 3789, 3801, 3813, 3825, 3837, 3849, 3861, 3873, 3920, 3930, 3940, 3954, 3998, 4036]
    
    print("Scanning for alternative JSON files for missing stories...")
    for nid in missing_ids:
        patterns = [
            f"story_{nid}_*.json",
            f"story_{nid}.json",
            f"pending_novel_{nid}_*.json",
            f"pending_novel_{nid}.json",
            f"*_{nid}_*.json",
            f"*_{nid}.json"
        ]
        found_files = []
        for p in patterns:
            matches = glob.glob(os.path.join(scratch_dir, p))
            found_files.extend(matches)
        
        # Also check root directory
        for p in patterns:
            matches = glob.glob(os.path.join("/Users/aaronnguyen/TN/App/doctieuthuyet", p))
            found_files.extend(matches)
            
        if found_files:
            print(f"ID {nid}: Found files -> {[os.path.basename(f) for f in set(found_files)]}")
        else:
            print(f"ID {nid}: No alternative JSON files found.")

if __name__ == "__main__":
    main()
