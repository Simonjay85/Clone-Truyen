import requests

OPENAI_KEY = "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"

def test_openai():
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_KEY}"
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": "Say 'OpenAI works!'"}],
        "temperature": 0.7
    }
    res = requests.post(url, json=payload, headers=headers, timeout=20)
    print("HTTP Code:", res.status_code)
    try:
        data = res.json()
        if "error" in data:
            print("Error details:", data["error"])
        else:
            print("Response:", data['choices'][0]['message']['content'])
    except Exception as e:
        print("Raw response:", res.text)
        print("Exception:", e)

test_openai()
