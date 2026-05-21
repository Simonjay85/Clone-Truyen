import urllib.request
import ssl
from PIL import Image
import os

ctx = ssl._create_unverified_context()

urls = {
    "cover_2573": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-2573-hq-397.png",
    "cover_2573_thumb": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-2573-hq-397-768x768.png",
    "icon": "https://doctieuthuyet.com/wp-content/themes/tehi-theme/img_data/images/icon_tehi_truyen_2025.png"
}

for name, url in urls.items():
    print(f"Downloading {url}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        out_path = f"scratch/{name}.png"
        with urllib.request.urlopen(req, context=ctx) as response:
            with open(out_path, "wb") as f:
                f.write(response.read())
        
        img = Image.open(out_path)
        print(f"  Downloaded: format={img.format}, size={img.size}")
        small = img.resize((1, 1))
        print(f"  Average color: {small.getpixel((0,0))}")
    except Exception as e:
        print(f"  Failed: {e}")
    print("-" * 50)
