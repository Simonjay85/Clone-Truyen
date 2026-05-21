import glob
import json
import os

for fpath in glob.glob("/Users/aaronnguyen/TN/App/doctieuthuyet/*.json"):
    print(f"File: {fpath}")
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            # check size first
            size = os.path.getsize(fpath)
            print(f"  Size: {size} bytes")
            if size < 500000:
                data = json.load(f)
                if isinstance(data, dict):
                    print("  Keys:", list(data.keys()))
                    if 'title' in data:
                        print("  Title:", data['title'])
                    if 'chapters' in data:
                        print("  Num chapters:", len(data['chapters']))
                        if len(data['chapters']) > 0:
                            print("  Chapter 1 title:", data['chapters'][0].get('title'))
                            print("  Chapter 1 content preview:", data['chapters'][0].get('content', '')[:150])
                elif isinstance(data, list):
                    print(f"  List of {len(data)} items")
                    if len(data) > 0:
                        print("  First item keys:", list(data[0].keys()) if isinstance(data[0], dict) else type(data[0]))
    except Exception as e:
        print("  Error:", e)
    print("-" * 50)
