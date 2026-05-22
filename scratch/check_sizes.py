import os

p1 = "/Users/aaronnguyen/.gemini/antigravity-ide/brain/12ea8d69-8883-4c0b-9ecb-fc7822e46167/cover-2808-check.png"
p2 = "/Users/aaronnguyen/.gemini/antigravity-ide/brain/12ea8d69-8883-4c0b-9ecb-fc7822e46167/no-image-web-check.png"

for p in [p1, p2]:
    if os.path.exists(p):
        size_mb = os.path.getsize(p) / (1024 * 1024)
        print(f"Path: {p} -> Size: {size_mb:.2f} MB")
    else:
        print(f"Path: {p} -> Does not exist")
