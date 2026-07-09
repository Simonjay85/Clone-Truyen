#!/usr/bin/env python3
import os
import requests
from PIL import Image

local_bases = {}

# 1. Standard base covers in root
for i in range(1, 65):
    path = f"base_cover_{i}.png"
    if os.path.exists(path):
        local_bases[path] = path

# 2. Other base covers
other_bases = [
    "lan_ong_base_cover.png",
    "than_y_base.png",
    "tu_nu_base_cover.png",
    "vua_tom_hum_v2.png",
    "de_che_gom_su_v2.png"
]
for ob in other_bases:
    if os.path.exists(ob):
        local_bases[ob] = ob
    if os.path.exists(os.path.join("scratch", ob)):
        local_bases[ob] = os.path.join("scratch", ob)

def mse_pure_pil(img1, img2):
    im1 = img1.convert("L").resize((32, 32), Image.Resampling.LANCZOS)
    im2 = img2.convert("L").resize((32, 32), Image.Resampling.LANCZOS)
    p1 = list(im1.getdata())
    p2 = list(im2.getdata())
    diff_sq = [(a - b) ** 2 for a, b in zip(p1, p2)]
    return sum(diff_sq) / len(diff_sq)

def identify_cover(url, pid):
    temp_path = f"scratch/temp_download/identify_{pid}.png"
    os.makedirs(os.path.dirname(temp_path), exist_ok=True)
    
    # Download
    print(f"Downloading cover from {url}...")
    r = requests.get(url, timeout=15)
    with open(temp_path, "wb") as f:
        f.write(r.content)
        
    live_img = Image.open(temp_path)
    
    best_match = None
    min_mse = float('inf')
    
    for name, path in local_bases.items():
        try:
            base_img = Image.open(path)
            score = mse_pure_pil(live_img, base_img)
            if score < min_mse:
                min_mse = score
                best_match = path
        except Exception as e:
            pass
            
    print(f"⭐ BEST MATCH FOR ID {pid}: {best_match} (MSE: {min_mse:.2f})")
    return best_match

if __name__ == "__main__":
    identify_cover("https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-7480-updated-587.png", 7480)
