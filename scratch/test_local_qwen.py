import requests

url = "http://127.0.0.1:8000/v1/chat/completions"
payload = {
    "model": "default",
    "messages": [
        {"role": "user", "content": "Say hello in Vietnamese in one sentence."}
    ],
    "temperature": 0.2,
    "max_tokens": 50
}
try:
    res = requests.post(url, json=payload, timeout=10)
    print("Local API Status:", res.status_code)
    print("Local API Response:", res.json())
except Exception as e:
    print("Local API Error:", e)
