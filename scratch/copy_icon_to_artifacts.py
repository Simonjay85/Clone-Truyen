import shutil
import os
from PIL import Image

src = "/Users/aaronnguyen/TN/App/doctieuthuyet/tehi-theme/img_data/images/icon_tehi_truyen_2025.png"
dst_dir = "/Users/aaronnguyen/.gemini/antigravity-ide/brain/12ea8d69-8883-4c0b-9ecb-fc7822e46167"
dst = os.path.join(dst_dir, "icon-check.png")

if os.path.exists(src):
    shutil.copy2(src, dst)
    print(f"Copied icon to {dst}")
    with Image.open(dst) as img:
        print(f"Icon format: {img.format}, size: {img.size}, mode: {img.mode}")
        # Print top 5 colors
        img_rgb = img.convert("RGB")
        img_small = img_rgb.resize((10, 10))
        pixels = list(img_small.getdata())
        print("Pixels of small resized icon:")
        print(pixels[:20])
else:
    print("Icon does not exist!")
