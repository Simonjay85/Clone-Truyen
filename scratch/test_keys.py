import requests
import json

GEMINI_KEY = "AIzaSyAsrcElDDSGl6jYHL8_1LGeVIvlTB7gl-c"
CLAUDE_KEY = "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"

def test_gemini():
    print("Testing Gemini...")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": "Say 'Gemini OK' and nothing else."}]}]
    }
    try:
        res = requests.post(url, json=payload, headers=headers)
        print("Gemini status:", res.status_code)
        if res.status_code == 200:
            print("Gemini response:", res.json()['candidates'][0]['content']['parts'][0]['text'].strip())
        else:
            print("Gemini error:", res.text)
    except Exception as e:
        print("Gemini exception:", e)

def test_claude():
    print("Testing Claude...")
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": CLAUDE_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    payload = {
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 20,
        "messages": [{"role": "user", "content": "Say 'Claude OK' and nothing else."}]
    }
    try:
        res = requests.post(url, json=payload, headers=headers)
        print("Claude status:", res.status_code)
        if res.status_code == 200:
            print("Claude response:", res.json()['content'][0]['text'].strip())
        else:
            print("Claude error:", res.text)
    except Exception as e:
        print("Claude exception:", e)

if __name__ == "__main__":
    test_gemini()
    test_claude()
