import requests
import json

GEMINI_KEY = "AIzaSyDD7JDTkTp9872jQkKGT2A6PPOhfp5M4Q4"

def test_model(model_name):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={GEMINI_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": "Say 'hello world' in Vietnamese"}
                ]
            }
        ]
    }
    try:
        res = requests.post(url, json=payload, headers=headers, timeout=15)
        print(f"Model: {model_name} -> HTTP {res.status_code}")
        if res.status_code == 200:
            res_json = res.json()
            text = res_json['candidates'][0]['content']['parts'][0]['text'].strip()
            print("Response:", text)
            return True
        else:
            print("Error Response:", res.text)
            return False
    except Exception as e:
        print(f"Exception for {model_name}: {e}")
        return False

def main():
    models = ["gemini-1.5-flash", "gemini-2.5-flash", "gemini-1.5-pro", "gemini-2.5-pro"]
    for m in models:
        test_model(m)

if __name__ == "__main__":
    main()
