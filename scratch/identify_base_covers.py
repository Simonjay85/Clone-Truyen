#!/usr/bin/env python3
import os
import requests
import json
from PIL import Image, ImageChops

# Target stories
targets = {
    "7466": {
        "title": "Hồn Sơn Mài: HỒN SƠN MÀI",
        "url": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-7466-hq-461.png"
    },
    "7448": {
        "title": "Vua Tôm Hùm Phú Yên: Chàng Ngư Dân Bị Vu Oan Buôn Lậu Thâu Tóm Vùng Biển Nghìn Tỷ",
        "url": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-7448-hq-596.png"
    },
    "7437": {
        "title": "Đế Chế Gốm Sứ Bát Tràng: Nghệ Nhân Bị Phản Bội Thiêu Đốt Cả Làng Nghề",
        "url": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-7437-hq-658.png"
    },
    "1933": {
        "title": "Bị Gọi Là Con Bé Bên Máy In, Ngày Tôi Tung Báo Cáo Kiểm Toán Nghìn Tỷ Cả Tập Đoàn Quỳ Lạy",
        "url": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-1933-426.png"
    },
    "7379": {
        "title": "Thần Y Châm Cứu Phố Lãn Ông: Bị Vu Oan Giết Bệnh Nhân, Tôi Dùng Kim Cứu Cả Làng Thuốc",
        "url": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-7379-hq-590.png"
    },
    "7369": {
        "title": "Kẻ Bị Đuổi Khỏi Công Trường Hôm Nay Là Ông Chủ Của Cả Thành Phố Ngày Mai",
        "url": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-7369-hq-138.png"
    },
    "5046": {
        "title": "SÁNG KÝ ĐƠN LY HÔN, CHIỀU TÔI GẶP VỢ TRÊN GHẾ CEO HỢP ĐỒNG 500 TỶ",
        "url": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-5046-hq-276.png"
    },
    "5180": {
        "title": "Bị Cấm Bến Ở Nha Trang, Tôi Xây Đội Tàu Cứu Hộ Biển Lớn Nhất Miền Trung",
        "url": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-5180-hq-544.png"
    },
    "5294": {
        "title": "Bị Gạt Khỏi HĐQT Công Ty Mình Sáng Lập, Tôi Xây PayChain Và Thâu Tóm Lại VietPay",
        "url": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-5294-hq-321.png"
    }
}

# Collect all local base covers
local_bases = {}

# 1. Standard base covers
for i in range(4, 64):
    path = f"base_cover_{i}.png"
    if os.path.exists(path):
        local_bases[path] = path

# 2. Other base covers in root
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

# Also check for base_1933.png in scratch/remade_related_three_20260525
base_1933 = "scratch/remade_related_three_20260525/base_1933.png"
if os.path.exists(base_1933):
    local_bases["base_1933.png"] = base_1933

print(f"Loaded {len(local_bases)} local base images for comparison.")

def mse_pure_pil(img1, img2):
    # Resize both to 32x32 and convert to grayscale for direct pixel difference
    im1 = img1.convert("L").resize((32, 32), Image.Resampling.LANCZOS)
    im2 = img2.convert("L").resize((32, 32), Image.Resampling.LANCZOS)
    p1 = list(im1.getdata())
    p2 = list(im2.getdata())
    diff_sq = [(a - b) ** 2 for a, b in zip(p1, p2)]
    return sum(diff_sq) / len(diff_sq)

# Directory to download temp covers
os.makedirs("scratch/temp_download", exist_ok=True)

results = {}

for pid, info in targets.items():
    print(f"\n🔍 Identifying base image for ID {pid}: {info['title']}")
    temp_path = f"scratch/temp_download/{pid}.png"
    
    # Download if not exists
    if not os.path.exists(temp_path):
        try:
            r = requests.get(info['url'], timeout=15)
            with open(temp_path, "wb") as f:
                f.write(r.content)
            print("  ✓ Downloaded current cover.")
        except Exception as e:
            print(f"  ❌ Download failed: {e}")
            continue
            
    # Load downloaded cover
    try:
        live_img = Image.open(temp_path)
    except Exception as e:
        print(f"  ❌ Failed to open downloaded cover: {e}")
        continue
        
    best_match = None
    min_mse = float('inf')
    
    # Compare with all local bases
    for name, path in local_bases.items():
        try:
            base_img = Image.open(path)
            score = mse_pure_pil(live_img, base_img)
            if score < min_mse:
                min_mse = score
                best_match = path
        except Exception as e:
            pass
            
    print(f"  ⭐ Best Match: {best_match} (MSE: {min_mse:.2f})")
    results[pid] = {
        "title": info["title"],
        "post_id": int(pid),
        "base_image": best_match,
        "mse": min_mse
    }

# Save results
with open("scratch/identified_bases.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\n🎉 Done! Mappings saved to scratch/identified_bases.json")
