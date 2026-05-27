#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cover_overlay_modern_card.py — Modern Card Overlay Engine for doctieuthuyet.com
=================================================================================
Tạo ảnh bìa theo phong cách Card Hiện Đại giống Fanqie/TikTok:
- Không viền, tràn viền hoàn toàn (Full-bleed).
- Gradient tối mờ ở đỉnh và đáy để hiển thị text rõ nét.
- 3 dòng tiêu đề cực lớn, căn giữa ở nửa trên, màu sắc tương phản cao (Cyan, Red, Yellow, White).
- Đổ bóng chữ (Drop Shadow) và stroke đen cực dày để tạo độ nổi bật.
- Không có số chương (Ch.5 pill badge) như yêu cầu của khách hàng.
- Góc dưới bên trái: Biểu tượng con mắt + Lượt xem (ví dụ: 👁 53.4K)
- Góc dưới bên phải: Biểu tượng đồng hồ + Thời gian cập nhật (ví dụ: 🕒 2 giờ trước)
"""

import os
import sys
import argparse
from PIL import Image, ImageDraw, ImageFont, ImageFilter

CANVAS_SIZE = 2000

# ─── COLOR PALETTE ────────────────────────────────────────────────────────────
COLORS = {
    "white": (255, 255, 255, 255),
    "cyan": (0, 210, 255, 255),
    "red": (255, 40, 60, 255),
    "yellow": (255, 210, 0, 255),
    "black": (0, 0, 0, 255),
    "light_gray": (220, 220, 220, 255)
}

FONT_PATHS_BOLD = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "/System/Library/Fonts/HelveticaNeue.ttc",
    "/System/Library/Fonts/SFNS.ttf",
]

def load_bold_font(size):
    for p in FONT_PATHS_BOLD:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size=size)
            except Exception:
                continue
    return ImageFont.load_default()

def text_width(font, text):
    bbox = font.getbbox(text)
    return bbox[2] - bbox[0]

def text_height(font, text):
    bbox = font.getbbox(text)
    return bbox[3] - bbox[1]

# ─── GRADIENT OVERLAYS ────────────────────────────────────────────────────────
def apply_vertical_gradient(img: Image.Image, start_y: int, end_y: int, start_alpha: int, end_alpha: int) -> Image.Image:
    """Áp dụng lớp phủ gradient đen từ mờ sang trong suốt (hoặc ngược lại)"""
    gradient = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(gradient)
    
    y_min = min(start_y, end_y)
    y_max = max(start_y, end_y)
    height = y_max - y_min
    
    for y in range(y_min, y_max):
        # Tính tỷ lệ phần trăm
        if start_y < end_y:
            t = (y - y_min) / height
        else:
            t = (y_max - y) / height
            
        alpha = int(start_alpha + (end_alpha - start_alpha) * t)
        draw.rectangle([(0, y), (CANVAS_SIZE, y + 1)], fill=(0, 0, 0, alpha))
        
    return Image.alpha_composite(img, gradient)

# ─── RENDER TEXT WITH ADVANCED DROP SHADOW & CRISP STROKE ─────────────────────
def draw_text_line(img: Image.Image, text: str, font, y: int, color, stroke_width=12) -> Image.Image:
    # 1. Tạo lớp bóng đổ nhòe (Blurred Drop Shadow) để chữ cực kỳ nổi
    shadow_layer = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)
    
    w = text_width(font, text)
    x = (CANVAS_SIZE - w) // 2
    
    # Vẽ stroke đen bóng dày
    for off in range(stroke_width * 2, 0, -2):
        a = int(220 * (1 - off / (stroke_width * 2)))
        sd.text((x + 6, y + 10), text, font=font, fill=(0, 0, 0, a),
                stroke_width=off, stroke_fill=(0, 0, 0, a))
                
    # Làm nhòe lớp bóng đổ
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=8))
    img = Image.alpha_composite(img, shadow_layer)
    
    # 2. Vẽ chữ thật kèm viền sắc nét đè lên trên
    d = ImageDraw.Draw(img)
    d.text((x, y), text, font=font, fill=color, stroke_width=stroke_width, stroke_fill=(0, 0, 0, 255))
    
    return img

def main():
    parser = argparse.ArgumentParser(description="Create modern TikTok/Fanqie style book cover overlay")
    parser.add_argument("--input", required=True, help="Input base image path")
    parser.add_argument("--output", required=True, help="Output image path")
    
    parser.add_argument("--line1", required=True, help="Line 1 text")
    parser.add_argument("--color1", default="white", choices=COLORS.keys(), help="Color of line 1")
    
    parser.add_argument("--line2", required=True, help="Line 2 text")
    parser.add_argument("--color2", default="red", choices=COLORS.keys(), help="Color of line 2")
    
    parser.add_argument("--line3", required=True, help="Line 3 text")
    parser.add_argument("--color3", default="yellow", choices=COLORS.keys(), help="Color of line 3")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"❌ Input file not found: {args.input}")
        sys.exit(1)
        
    print(f"🎨 Processing modern card cover from: {args.input}")
    
    # Mở ảnh gốc và chỉnh cỡ chuẩn
    img = Image.open(args.input).convert("RGBA")
    img = img.resize((CANVAS_SIZE, CANVAS_SIZE), Image.Resampling.LANCZOS)
    
    # 1. Áp dụng Gradient mờ tối ở Đỉnh (Top) và Đáy (Bottom)
    print("🌑 Applying premium gradient shadows...")
    img = apply_vertical_gradient(img, start_y=0, end_y=750, start_alpha=200, end_alpha=0)
    img = apply_vertical_gradient(img, start_y=2000, end_y=1700, start_alpha=80, end_alpha=0) # Rất dịu để giữ độ sáng bottom
    
    # 2. Chuẩn bị font tiêu đề cực lớn
    font_size = 145
    title_font = load_bold_font(font_size)
    
    # Điều chỉnh cỡ chữ tự động nếu quá dài để không bị tràn lề
    max_w = 1850
    for line in [args.line1, args.line2, args.line3]:
        while text_width(title_font, line.upper()) > max_w and font_size > 100:
            font_size -= 5
            title_font = load_bold_font(font_size)
            
    print(f"📐 Chosen Title Font Size: {font_size}px")
    
    # 3. Vẽ 3 dòng tiêu đề
    y_start = 120
    y_spacing = int(font_size * 1.15)
    
    img = draw_text_line(img, args.line1.upper(), title_font, y_start, COLORS[args.color1])
    img = draw_text_line(img, args.line2.upper(), title_font, y_start + y_spacing, COLORS[args.color2])
    img = draw_text_line(img, args.line3.upper(), title_font, y_start + y_spacing * 2, COLORS[args.color3])
    
    # 4. Lưu ảnh dạng chất lượng cao (Không vẽ con mắt hay đồng hồ ở dưới)
    out = img.convert("RGB")
    out.save(args.output, "PNG", quality=95)
    print(f"✅ Premium Card Cover Saved successfully: {args.output}")

if __name__ == "__main__":
    main()
