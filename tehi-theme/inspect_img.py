import os
from PIL import Image

def analyze_image(path):
    if not os.path.exists(path):
        print(f"{path} does not exist")
        return
    try:
        img = Image.open(path)
        print(f"File: {path}")
        print(f"  Format: {img.format}")
        print(f"  Size: {img.size}")
        print(f"  Mode: {img.mode}")
        
        # Get dominant color or average color
        img_resized = img.resize((1, 1))
        color = img_resized.getpixel((0, 0))
        print(f"  Average Color: {color}")
        
        # Let's count unique colors
        img_small = img.resize((50, 50))
        colors = img_small.getcolors(50*50)
        if colors:
            print(f"  Unique colors in 50x50 resize: {len(colors)}")
    except Exception as e:
        print(f"Error reading {path}: {e}")

if __name__ == "__main__":
    analyze_image("live_cover_1927.jpg")
    analyze_image("live_no_image_cover.png")
    analyze_image("live_no_image_cover_v5.png")
    analyze_image("img_data/images/no-image-cover.png")
