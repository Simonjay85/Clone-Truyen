import requests
import json

GEMINI_KEY = "AIzaSyAsrcElDDSGl6jYHL8_1LGeVIvlTB7gl-c"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"

headers = {
    "Content-Type": "application/json"
}

payload = {
    "contents": [
        {"parts": [{"text": "Say hello in 5 words."}]}
    ]
}

try:
    res = requests.post(url, headers=headers, json=payload, timeout=10)
    print("Status:", res.status_code)
    print("Response:", res.json())
except Exception as e:
    print("Gemini API direct test failed:", e)
