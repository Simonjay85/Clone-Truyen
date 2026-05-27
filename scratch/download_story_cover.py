# -*- coding: utf-8 -*-
import urllib.parse
import requests

def download_image():
    prompt = (
        "A highly luxurious anime-style book cover, featuring a determined handsome young Vietnamese biochemist "
        "in a clean white lab coat, standing inside a state-of-the-art laboratory in Kon Tum. He is holding a glowing "
        "golden glass vial with a pure golden Sâm Ngọc Linh extract. In the background, futuristic automated glass "
        "chromatography columns are glowing with soft golden and amber light. Hyper-detailed, cinematic soft lighting, "
        "premium webnovel art, 1:1 aspect ratio, absolutely no text or words on screen."
    )
    
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true"
    
    print(f"Downloading cover from Pollinations AI...")
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
