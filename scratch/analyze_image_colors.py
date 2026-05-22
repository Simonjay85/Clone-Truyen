from PIL import Image
import collections

img_path = "/Users/aaronnguyen/.gemini/antigravity-ide/brain/12ea8d69-8883-4c0b-9ecb-fc7822e46167/no-image-cover-check.png"

with Image.open(img_path) as img:
    img = img.convert("RGB")
    img_small = img.resize((100, 100))
    pixels = list(img_small.getdata())
    counter = collections.Counter(pixels)
    print("Most common colors:")
    for color, count in counter.most_common(10):
        print(f"Color: {color}, Count: {count}")
