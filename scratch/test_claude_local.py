import requests
import json

CLAUDE_KEY = "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"

def test_claude_sonnet():
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "content-type": "application/json",
        "x-api-key": CLAUDE_KEY,
        "anthropic-version": "2023-06-01"
    }
    payload = {
        "model": "claude-sonnet-4-6",
        "max_tokens": 100,
        "messages": [
            {"role": "user", "content": "Say 'Claude Sonnet 4.6 works!'"}
        ]
    }
    res = requests.post(url, json=payload, headers=headers, timeout=20)
    print("HTTP Code:", res.status_code)
    try:
        data = res.json()
        if "error" in data:
            print("Error details:", data["error"])
        else:
            print("Response:", data['content'][0]['text'])
    except Exception as e:
        print("Raw response:", res.text)
        print("Exception:", e)

if __name__ == "__main__":
    test_claude_sonnet()
