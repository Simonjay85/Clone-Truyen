import json

log_path = "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f/.system_generated/logs/transcript.jsonl"
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            content = data.get('content', '')
            if "Đà Lạt" in content or "mã hóa" in content or "2227" in content:
                print(f"Step {data.get('step_index')} (type: {data.get('type')}):")
                print(content[:500])
                print("=" * 50)
        except Exception as e:
            pass
