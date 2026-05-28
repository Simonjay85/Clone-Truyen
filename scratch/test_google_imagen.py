#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_google_imagen.py — Test generating an image using Google AI Studio Imagen 3 API with the live Gemini API Key.
"""

import os
import requests
import json
import base64

API_KEY = "AIzaSyAsrcElDDSGl6jYHL8_1LGeVIvlTB7gl-c"

def main():
    prompt = (
        "A highly realistic, cinematic 8k dramatic movie still capturing a powerful psychological confrontation: "
        "an arrogant, wealthy high-society critic in a premium designer suit looking at a young artist with an intense contemptuous sneer, "
        "a mocking, disdainful expression showing deep scorn. Opposite him, a stylish, handsome 29-year-old Vietnamese digital artist "
        "looks back with a proud, extremely confident, slightly smug smirk, holding a brilliant glowing digital tablet showing masterpieces. "
        "High-contrast dramatic cinematic lighting, deep shadows, intense emotional clash on realistic human faces. "
        "Professional studio photography, shot on a 50mm anamorphic lens, photorealistic, no text."
    )

    url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-002:generateImages?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "prompt": prompt,
        "numberOfImages": 1,
        "outputMimeType": "image/png",
        "aspectRatio": "1:1"
    }

    print("🚀 Querying Google AI Studio Imagen 3 API...")
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=90)
        print("Response Code:", response.status_code)
        
        # If not successful, print error details
        if response.status_code != 200:
            print("Error Text:", response.text)
            return

        res_data = response.json()
        
        # Parse the base64 image data
        # Structure is usually: {"generatedImages": [{"image": {"imageBytes": "BASE64_DATA"}}]}
        images = res_data.get("generatedImages", [])
        if not images:
            print("❌ No images returned in response. Response JSON:", res_data)
            return

        img_b64 = images[0].get("image", {}).get("imageBytes")
        if not img_b64:
            print("❌ imageBytes not found in response.")
            return

        img_data = base64.b64decode(img_b64)
        
        output_path = "scratch/temp_google_imagen_5498.png"
        with open(output_path, "wb") as f:
            f.write(img_data)
        print(f"✓ Success! Saved raw image to: {output_path}")

    except Exception as e:
        print("❌ Exception during Google Imagen request:", e)

if __name__ == "__main__":
    main()
