import requests

key = "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"

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}
payload = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "say hello"}],
    "max_tokens": 10
}

try:
    res = requests.post(url, json=payload, headers=headers, timeout=10)
    print("Status code:", res.status_code)
    print("Response:", res.text)
except Exception as e:
    print("Exception:", e)
