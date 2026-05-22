import urllib.request
import ssl
from PIL import Image
import os

ctx = ssl._create_unverified_context()

urls = {
    "cover_2587": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-2587-hq-859-768x768.png",
    "cover_1927": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-1927-upd-414.jpg",
    "cover_1933": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-1933-hq-295.jpg",
    "cover_1948": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-1948-hq-733.jpg"
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
