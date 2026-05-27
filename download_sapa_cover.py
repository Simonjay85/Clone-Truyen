# -*- coding: utf-8 -*-
import urllib.parse
import requests
import os

def download_image():
    prompt = (
        "A premium, highly detailed anime-style book cover, a confident and handsome young Vietnamese pharmacologist "
        "with short black hair, wearing a white clinical lab coat over a dark blue turtleneck, holding a glowing green "
        "botanical gel vial. In the background, the majestic mist-covered Fansipan mountain peaks of Sapa, blended "
        "with the high-tech glowing chemical equipment of a modern laboratory. Elegant and dramatic lighting, vibrant "
        "harmonious colors, HSL tailored palette, 1:1 ratio, clean premium art, no text."
    )
    
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true"
    
    print(f"Downloading cover from Pollinations AI...")
    try:
        response = requests.get(url, timeout=90)
        if response.status_code == 200:
            output_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_cover.png"
            with open(output_path, "wb") as f:
                f.write(response.content)
            print(f"✓ SUCCESSFULLY DOWNLOADED COVER AND SAVED TO: {output_path}")
        else:
            print(f"❌ Failed to download cover. Status code: {response.status_code}")
    except Exception as e:
        print("❌ Error downloading cover:", e)

if __name__ == "__main__":
    download_image()
