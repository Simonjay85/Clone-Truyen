import requests
import json

GEMINI_KEY = "AIzaSyAsrcElDDSGl6jYHL8_1LGeVIvlTB7gl-c"

def call_gemini_header(system_prompt, user_prompt, model="gemini-2.5-flash"):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    payload = {
        "system_instruction": {"parts": [{"text": system_prompt}]},
        "contents": [{"role": "user", "parts": [{"text": user_prompt}]}],
        "generationConfig": {"temperature": 0.7}
    }
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_KEY
    }
    
    res = requests.post(url, json=payload, headers=headers, timeout=60)
    print("Header call HTTP Code:", res.status_code)
    try:
        data = res.json()
        if "error" in data:
            print("Error details:", data["error"])
        else:
            text = data['candidates'][0]['content']['parts'][0]['text']
            print("Response:", text[:500])
    except Exception as e:
        print("Raw response:", res.text)
        print("Exception:", e)

def call_gemini_param(system_prompt, user_prompt, model="gemini-2.5-flash"):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GEMINI_KEY}"
    payload = {
        "system_instruction": {"parts": [{"text": system_prompt}]},
        "contents": [{"role": "user", "parts": [{"text": user_prompt}]}],
        "generationConfig": {"temperature": 0.7}
    }
    headers = {"Content-Type": "application/json"}
    
    res = requests.post(url, json=payload, headers=headers, timeout=60)
    print("Param call HTTP Code:", res.status_code)
    try:
        data = res.json()
        if "error" in data:
            print("Error details:", data["error"])
        else:
            text = data['candidates'][0]['content']['parts'][0]['text']
            print("Response:", text[:500])
    except Exception as e:
        print("Raw response:", res.text)
        print("Exception:", e)

print("--- Header Call ---")
call_gemini_header("You are a helpful assistant.", "Hello, how are you?")

print("\n--- Param Call ---")
call_gemini_param("You are a helpful assistant.", "Hello, how are you?")
