#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_openai_dalle.py — Test if the OpenAI API key in the database is valid for DALL-E 3 image generation.
"""

import os
import requests
import json

API_KEY = "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"

def main():
    url = "https://api.openai.com/v1/images/generations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    prompt = (
        "A highly realistic, cinematic 8k dramatic movie still capturing a powerful psychological confrontation: "
        "an arrogant, wealthy high-society critic in a premium designer suit looking at a young artist with an intense contemptuous sneer, "
        "a mocking, disdainful expression showing deep scorn. Opposite him, a stylish, handsome 29-year-old Vietnamese digital artist "
        "looks back with a proud, extremely confident, slightly smug smirk, holding a brilliant glowing digital tablet showing masterpieces. "
        "High-contrast dramatic cinematic lighting, deep shadows, intense emotional clash on realistic human faces. "
        "Professional studio photography, shot on a 50mm anamorphic lens, photorealistic."
    )
    payload = {
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }

    print("🚀 Querying OpenAI DALL-E 3 API...")
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=90)
        print("Response Code:", response.status_code)
        print("Response Body:", response.text)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
