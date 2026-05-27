# -*- coding: utf-8 -*-
import urllib.parse
import requests
import os

def download_image():
    prompt = (
        "A premium anime-style webnovel book cover, 1:1 aspect ratio, highly detailed, without any text. "
        "A young, determined, and handsome Vietnamese man in a simple but elegant traditional linen shirt stands on a "
        "high-tech organic Aquilaria crassna (agarwood) research farm near the beautiful ocean bay of Nha Trang. "
        "Next to him is a highly sophisticated, beautiful Vietnamese businesswoman with long dark hair, wearing a sleek "
        "luxury business suit. In the background, majestic green mountains, ocean sunset golden hour rays reflecting on "
        "pristine seawater, crystal-clear glass containers showing glowing amber Ky Nam resin, hyper-realistic, "
        "dynamic lighting, cinematic composition."
    )
    
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true"
    
    print(f"Downloading cover from: {url}")
    try:
        response = requests.get(url, timeout=60)
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
