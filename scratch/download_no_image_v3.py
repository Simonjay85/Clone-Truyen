import urllib.request
import os
from PIL import Image
import collections

url = "https://doctieuthuyet.com/wp-content/themes/tehi-theme/img_data/images/no-image-cover.png?v=3"
dst_dir = "/Users/aaronnguyen/.gemini/antigravity-ide/brain/12ea8d69-8883-4c0b-9ecb-fc7822e46167"
dst_path = os.path.join(dst_dir, "no-image-v3-check.png")

headers = {'User-Agent': 'Mozilla/5.0'}
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        with open(dst_path, 'wb') as f:
            f.write(response.read())
    print(f"Successfully downloaded {url} to {dst_path}")
    
    # Analyze colors
    with Image.open(dst_path) as img:
        img = img.convert("RGB")
        img_small = img.resize((100, 100))
        pixels = list(img_small.getdata())
        counter = collections.Counter(pixels)
        print("Most common colors of no-image-cover.png?v=3:")
        for color, count in counter.most_common(10):
            print(f"Color: {color}, Count: {count}")
            
except Exception as e:
    print("Error:", e)
