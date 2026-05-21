import json
import glob

for fpath in glob.glob("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/original_*.json"):
    print(f"File: {fpath}")
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print("Keys:", data.keys())
            if 'chapters' in data and len(data['chapters']) > 0:
                print(f"Num chapters: {len(data['chapters'])}")
                print("First chapter title:", data['chapters'][0].get('title'))
                content = data['chapters'][0].get('content', '')
                print("First chapter content preview:", content[:300])
            else:
                print("No chapters key or empty")
    except Exception as e:
        print("Error reading:", e)
    print("-" * 50)
