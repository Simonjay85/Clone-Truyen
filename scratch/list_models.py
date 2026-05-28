#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
list_models.py — List all available models in Google AI Studio to check if Imagen is listed.
"""

import requests
import json

API_KEY = "AIzaSyAsrcElDDSGl6jYHL8_1LGeVIvlTB7gl-c"

def main():
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"
    print(f"Requesting URL: {url}")
    try:
        response = requests.get(url, timeout=30)
        print("Response Code:", response.status_code)
        print("Response Data:")
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
