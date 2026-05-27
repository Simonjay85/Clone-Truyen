#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cover_overlay_standard.py — Standard Cover Overlay Engine for doctieuthuyet.com
=================================================================================
Tạo ảnh bìa theo phong cách Card Hiện Đại giống Fanqie/TikTok:
- Không viền, tràn viền hoàn toàn (Full-bleed).
- Gradient tối mờ ở đỉnh và đáy để hiển thị text rõ nét.
- Tiêu đề tự động xuống dòng (2-3 dòng), căn giữa, màu sắc tương phản cao (White, Red, Yellow).
- Đổ bóng chữ (Drop Shadow) và stroke đen cực dày để tạo độ nổi bật.
- Không có số chương hay biểu tượng con mắt/đồng hồ (WordPress theme tự render).
"""

import os
import sys
import argparse
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

CANVAS_SIZE = 2000

# ─── COLOR PALETTE ────────────────────────────────────────────────────────────
LINE_COLORS = [
    (255, 255, 255, 255),  # White
    (255, 40, 60, 255),    # Red
    (255, 210, 0, 255),    # Yellow
]

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

def _text_width(font, text):
    bbox = font.getbbox(text)
    return bbox[2] - bbox[0]

def _text_height(font, text):
    bbox = font.getbbox(text)
    return bbox[3] - bbox[1]

# ─── SMART TITLE WRAP ────────────────────────────────────────────────────────
def smart_wrap_title(title: str) -> list:
    """Tự động xuống dòng thông minh dựa trên chiều dài tiêu đề."""
    words = title.split()
    total_chars = len(title)

    if total_chars <= 20:
        return [title]
    elif total_chars <= 40:
        return _wrap_n_lines(words, 2)
    else:
        return _wrap_n_lines(words, 3)

def _wrap_n_lines(words: list, n_lines: int) -> list:
    """Chia words thành n_lines dòng cân bằng nhất."""
    if len(words) <= n_lines:
        return words

    total = sum(len(w) for w in words) + len(words) - 1
    target_per_line = total / n_lines

    lines = []
    current = []
    current_len = 0

    for word in words:
        if current and current_len + 1 + len(word) > target_per_line * 1.3 and len(lines) < n_lines - 1:
            lines.append(" ".join(current))
            current = [word]
            current_len = len(word)
        else:
            if current:
                current_len += 1 + len(word)
            else:
                current_len = len(word)
            current.append(word)

    if current:
        lines.append(" ".join(current))

    while len(lines) > n_lines:
        lines[-2] = lines[-2] + " " + lines[-1]
        lines.pop()

    return lines

# ─── GRADIENT OVERLAYS ────────────────────────────────────────────────────────
def apply_vertical_gradient(img: Image.Image, start_y: int, end_y: int, start_alpha: int, end_alpha: int) -> Image.Image:
    """Áp dụng lớp phủ gradient đen từ mờ sang trong suốt (hoặc ngược lại)"""
    gradient = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(gradient)
    
    y_min = min(start_y, end_y)
    y_max = max(start_y, end_y)
    height = y_max - y_min
    
    for y in range(y_min, y_max):
        if start_y < end_y:
            t = (y - y_min) / height
        else:
            t = (y_max - y) / height
            
        alpha = int(start_alpha + (end_alpha - start_alpha) * t)
        draw.rectangle([(0, y), (CANVAS_SIZE, y + 1)], fill=(0, 0, 0, alpha))
        
    return Image.alpha_composite(img, gradient)

# ─── TEXT RENDERING WITH SHADOW & COLOR BLOCKS ─────────────────────────────────
def draw_card_titles_with_shadow(img: Image.Image, lines, font_obj, start_y, line_spacing, stroke_width=12) -> Image.Image:
    # Bản đồ màu cho từng dòng:
    if len(lines) == 2:
        colors_map = [LINE_COLORS[0], LINE_COLORS[2]] # Dòng 1: Trắng, Dòng 2: Vàng
    elif len(lines) == 1:
        colors_map = [LINE_COLORS[0]] # Dòng 1: Trắng
    else:
        # 3 dòng hoặc hơn: Trắng, Đỏ, Vàng
        colors_map = [LINE_COLORS[i % len(LINE_COLORS)] for i in range(len(lines))]

    # 1. Vẽ bóng đổ mờ cực đẹp
    shadow_layer = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)

    for i, line in enumerate(lines):
        txt = line.upper()
        w = _text_width(font_obj, txt)
        x = (CANVAS_SIZE - w) // 2
        y = start_y + i * line_spacing
        
        # Stroke đen bóng mờ
        for off in range(stroke_width * 2, 0, -2):
            a = int(220 * (1 - off / (stroke_width * 2)))
            sd.text((x + 6, y + 10), txt, font=font_obj,
                    fill=(0, 0, 0, a), stroke_width=off, stroke_fill=(0, 0, 0, a))

    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=8))
    img = Image.alpha_composite(img, shadow_layer)

    # 2. Vẽ chữ thật có viền sắc nét
    d = ImageDraw.Draw(img)
    for i, line in enumerate(lines):
        txt = line.upper()
        w = _text_width(font_obj, txt)
        x = (CANVAS_SIZE - w) // 2
        y = start_y + i * line_spacing
        color = colors_map[i]
        
        d.text((x, y), txt, font=font_obj, fill=color,
               stroke_width=stroke_width, stroke_fill=(0, 0, 0, 255))
               
    return img

def _autofit_font_multiline(text_lines, start_size, max_width, min_size=100):
    size = start_size
    while size >= min_size:
        f = load_bold_font(size)
        fits = all(_text_width(f, ln.upper()) <= max_width for ln in text_lines)
        if fits:
            return f, size
        size -= 4
    return load_bold_font(min_size), min_size

# ─── MAIN FUNCTION ────────────────────────────────────────────────────────────
def apply_standard_overlay(
    input_path: str,
    output_path: str,
    title: str,
    subtitle: str = "",
    bottom_label: str = "TIỂU THUYẾT VIỆT NAM", # Ignored backward compatibility
    position: str = "top",
) -> bool:
    if not os.path.exists(input_path):
        print(f"❌ Input not found: {input_path}")
        return False

    print(f"🎨 Loading base image: {input_path}")
    img = Image.open(input_path).convert("RGBA")
    img = img.resize((CANVAS_SIZE, CANVAS_SIZE), Image.Resampling.LANCZOS)

    # 1. Gradient mờ tối ở Đỉnh (Top) và Đáy (Bottom) tùy theo vị trí text
    print(f"🌑 Applying premium gradient shadows for position: {position}...")
    if position == "bottom":
        img = apply_vertical_gradient(img, start_y=2000, end_y=1250, start_alpha=220, end_alpha=0)
        img = apply_vertical_gradient(img, start_y=0, end_y=300, start_alpha=80, end_alpha=0)
    else:
        img = apply_vertical_gradient(img, start_y=0, end_y=750, start_alpha=200, end_alpha=0)
        img = apply_vertical_gradient(img, start_y=2000, end_y=1700, start_alpha=80, end_alpha=0)

    # 2. Xuống dòng tự động thông minh
    if "\\n" in title:
        title_lines = title.split("\\n")
    elif "\n" in title:
        title_lines = title.split("\n")
    else:
        title_lines = smart_wrap_title(title)

    print(f"📐 Title wrapped to {len(title_lines)} lines: {title_lines}")

    # 3. Fit cỡ chữ tiêu đề
    title_max_w = 1850
    font_title, title_size = _autofit_font_multiline(
        title_lines, start_size=145, max_width=title_max_w, min_size=100
    )
    title_line_h = int(title_size * 1.15)
    print(f"📐 Chosen Title Font Size: {title_size}px")

    # Tính toán vị trí Y của tiêu đề
    total_height = (len(title_lines) - 1) * title_line_h + title_size
    if position == "bottom":
        start_y = 1800 - total_height
    else:
        start_y = 120

    # 4. Vẽ tiêu đề màu sắc rực rỡ dạng Card
    img = draw_card_titles_with_shadow(
        img, title_lines, font_title,
        start_y=start_y, line_spacing=title_line_h, stroke_width=12
    )

    # 5. Phụ đề phụ (nếu có) vẽ rất nhẹ nhàng ở dưới (hoặc trên nếu ở bottom)
    if subtitle:
        sub_lines = subtitle.split("\\n") if "\\n" in subtitle else subtitle.split("\n")
        font_sub = load_bold_font(42)
        
        if position == "bottom":
            sub_y = start_y - len(sub_lines) * 50 - 20
        else:
            sub_y = start_y + total_height + 20
        
        # Thêm bóng đổ mờ cho phụ đề
        shadow_layer = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
        sd = ImageDraw.Draw(shadow_layer)
        for i, sl in enumerate(sub_lines):
            w = _text_width(font_sub, sl)
            x = (CANVAS_SIZE - w) // 2
            y = sub_y + i * 50
            sd.text((x + 3, y + 4), sl, font=font_sub, fill=(0, 0, 0, 180), stroke_width=3, stroke_fill=(0, 0, 0, 180))
        shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=4))
        img = Image.alpha_composite(img, shadow_layer)
        
        d = ImageDraw.Draw(img)
        for i, sl in enumerate(sub_lines):
            w = _text_width(font_sub, sl)
            x = (CANVAS_SIZE - w) // 2
            y = sub_y + i * 50
            d.text((x, y), sl, font=font_sub, fill=(255, 255, 255, 220), stroke_width=3, stroke_fill=(0, 0, 0, 255))

    # Lưu ảnh dạng chất lượng cao
    out = img.convert("RGB")
    out.save(output_path, "PNG", quality=95)
    print(f"✅ Premium Standard Cover Saved successfully: {output_path}")
    return True

# ─── CLI ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Apply premium standard cover overlay (TikTok/Fanqie Card style)"
    )
    parser.add_argument("--input",    required=True, help="Path to base AI image")
    parser.add_argument("--output",   required=True, help="Path to output PNG")
    parser.add_argument("--title",    required=True, help="Title text (auto-wrapped)")
    parser.add_argument("--subtitle", default="",    help="Optional subtitle/tagline")
    parser.add_argument("--label",    default="TIỂU THUYẾT VIỆT NAM",
                        help="Bottom brand label text (ignored, kept for compatibility)")
    parser.add_argument("--position", default="top", choices=["top", "bottom"],
                        help="Vertical position of the title text (top or bottom)")
    args = parser.parse_args()

    ok = apply_standard_overlay(
        input_path=args.input,
        output_path=args.output,
        title=args.title,
        subtitle=args.subtitle,
        position=args.position,
    )
    sys.exit(0 if ok else 1)
