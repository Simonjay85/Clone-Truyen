from PIL import Image

img_paths = {
    "cover-2573.png": "/Users/aaronnguyen/.gemini/antigravity-ide/brain/12ea8d69-8883-4c0b-9ecb-fc7822e46167/cover-2573.png",
    "cover-1927.jpg": "/Users/aaronnguyen/.gemini/antigravity-ide/brain/12ea8d69-8883-4c0b-9ecb-fc7822e46167/cover-1927.jpg",
    "icon": "/Users/aaronnguyen/TN/App/doctieuthuyet/tehi-theme/img_data/images/icon_tehi_truyen_2025.png"
}

for name, path in img_paths.items():
    img = Image.open(path)
    # Get average color by resizing to 1x1
    small = img.resize((1, 1))
    print(f"Image {name}: format={img.format}, size={img.size}, avg color={small.getpixel((0,0))}")
