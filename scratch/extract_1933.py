import json

log_path = "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f/.system_generated/logs/transcript.jsonl"
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('step_index') == 2876:
                content = data.get('content', '')
                print("--- START ---")
                print(content)
                print("--- END ---")
                break
        except Exception as e:
            pass
