import glob
import os

for root, dirs, files in os.walk("/Users/aaronnguyen/TN/App/doctieuthuyet"):
    for file in files:
        if file.endswith(".json") and "node_modules" not in root and ".git" not in root:
            fpath = os.path.join(root, file)
            size = os.path.getsize(fpath)
            print(f"Path: {fpath} ({size} bytes)")
