import requests

key = "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"
url = "https://api.openai.com/v1/chat/completions"
payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "user", "content": "Hello, is this key active?"}
    ],
    "max_tokens": 10
}
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {key}"
}

try:
    r = requests.post(url, json=payload, headers=headers, timeout=10)
    print(f"Status: {r.status_code}")
    print(r.text)
except Exception as e:
    print(f"Error: {e}")
