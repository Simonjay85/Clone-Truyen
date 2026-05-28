#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_gemini_text.py — Test if the Gemini API key in the database is valid for text generation.
"""

import requests
import json

API_KEY = "AIzaSyAsrcElDDSGl6jYHL8_1LGeVIvlTB7gl-c"

def main():
    model_id = "gemini-2.5-flash"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_id}:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": "Hello, respond with exactly one word: Success"}]}
        ]
    }
    print(f"Requesting URL: {url}")
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        print("Response Code:", response.status_code)
        print("Response Body:", response.text)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
