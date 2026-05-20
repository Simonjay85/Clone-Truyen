from PIL import Image
import os

paths = [
    "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f/truyen_phe_vat_cover_1779244267478.png",
    "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f/phe_vat_cover_1200x800_1779245473411.png"
]

for p in paths:
    if os.path.exists(p):
        with Image.open(p) as img:
            print(f"Path: {p} -> Size: {img.size}, Format: {img.format}")
    else:
        print(f"Path: {p} -> Does not exist")
