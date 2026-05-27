# -*- coding: utf-8 -*-
import json
import os
import requests

def main():
    print("Downloading premium cover from Pollinations AI for the rice novel...")
    cover_prompt = (
        "A highly premium anime style, 1:1, luxurious illustration. A handsome 29-year-old Vietnamese agricultural scientist with sharp eyes and determined expression, wearing a stylish modern field researcher outfit, holding a glowing golden rice stalk with green grains inside a modern high-tech laboratory. Beside him stands a beautiful, elegant, and highly sophisticated 27-year-old Vietnamese female CEO in a premium dark blue business blazer. In the background, beautiful golden sunset over misty Mekong Delta rice fields visible through large glass windows, advanced bio-analysis screens displaying molecular structures. Beautiful cinematic warm lighting, detailed accents, no text."
    )
    
    try:
        encoded_prompt = requests.utils.quote(cover_prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
        print(f"Requesting URL: {url[:100]}...")
        response = requests.get(url, timeout=60)
        if response.status_code == 200:
            output_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_cover.png"
            with open(output_path, "wb") as img_f:
                img_f.write(response.content)
            print(f"✓ Successfully downloaded and saved premium cover to {output_path}!")
        else:
            print(f"✗ Failed to download cover from Pollinations AI: status code {response.status_code}")
    except Exception as e:
        print(f"✗ Error downloading cover: {e}")

if __name__ == "__main__":
    main()
