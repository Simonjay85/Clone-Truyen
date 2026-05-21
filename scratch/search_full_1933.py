import json

log_path = "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f/.system_generated/logs/transcript.jsonl"
out_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/found_1933.txt"

with open(log_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        try:
            data = json.loads(line)
            content = data.get('content', '')
            if "Tôi là Tô Khanh Khanh" in content:
                with open(out_path, 'w', encoding='utf-8') as out:
                    out.write(f"Line {i} Index {data.get('step_index')}\n")
                    out.write(content)
                print(f"Written match to {out_path} from line {i} step_index {data.get('step_index')}")
        except Exception as e:
            pass
