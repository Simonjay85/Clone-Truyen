import urllib.request
import os
from PIL import Image
import collections

url = "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-2808-hq-383-768x768.png"
dst_dir = "/Users/aaronnguyen/.gemini/antigravity-ide/brain/12ea8d69-8883-4c0b-9ecb-fc7822e46167"
dst_path = os.path.join(dst_dir, "cover-2808-check.png")

headers = {'User-Agent': 'Mozilla/5.0'}
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        with open(dst_path, 'wb') as f:
            f.write(response.read())
    print(f"Successfully downloaded {url} to {dst_path}")
    
    # Analyze colors of downloaded cover
    with Image.open(dst_path) as img:
        img = img.convert("RGB")
        img_small = img.resize((100, 100))
        pixels = list(img_small.getdata())
        counter = collections.Counter(pixels)
        print("Most common colors of cover-2808:")
        for color, count in counter.most_common(10):
            print(f"Color: {color}, Count: {count}")
            
except Exception as e:
    print("Error downloading or analyzing:", e)
