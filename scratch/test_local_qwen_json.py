import requests
import json

url = "http://127.0.0.1:8000/v1/chat/completions"
payload = {
    "model": "default",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant. Output JSON only."},
        {"role": "user", "content": "Return a JSON with keys 'test' and 'reply'."}
    ],
    "temperature": 0.2,
    "max_tokens": 1000,
    "response_format": {"type": "json_object"}
}

try:
    res = requests.post(url, json=payload, timeout=20)
    print("Status:", res.status_code)
    print("Response JSON:")
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
except Exception as e:
    print("Local Qwen JSON test failed:", e)
