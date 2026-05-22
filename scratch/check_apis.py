import requests
import json

OPENAI_KEY = "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"

def check_openai():
    url = "https://api.openai.com/v1/chat/completions"
    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": "Hello"}],
        "max_tokens": 10
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_KEY}"
    }
    try:
        res = requests.post(url, json=payload, headers=headers)
        print("OpenAI Status:", res.status_code)
        print("OpenAI Response:", res.json())
    except Exception as e:
        print("OpenAI Error:", e)

def check_wp():
    url = "https://doctieuthuyet.com/wp-json/wp/v2/truyen/2668"
    try:
        res = requests.get(url, verify=False)
        print("WP API Status:", res.status_code)
        if res.status_code == 200:
            data = res.json()
            print("Title:", data.get('title', {}).get('rendered'))
            print("Intro Preview:", data.get('content', {}).get('rendered')[:200])
    except Exception as e:
        print("WP API Error:", e)

if __name__ == "__main__":
    check_openai()
    check_wp()
