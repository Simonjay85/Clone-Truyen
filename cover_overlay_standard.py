#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cover_overlay_standard.py — Standard Cover Overlay Engine for doctieuthuyet.com
=================================================================================
Áp dụng text overlay chuẩn lên ảnh bìa đã được AI generate.
Phong cách: Gold title on dark gradient + gold double border + TIỂU THUYẾT VIỆT NAM label.

FIXED v2: Smart title auto-wrap (2-3 dòng), font tối thiểu 100px, không bị shrink.

Usage:
    python3 cover_overlay_standard.py \
        --input base_image.png \
        --output final_cover.png \
        --title "CHÊ ANH THỢ HỒ NGHÈO GIÂY SAU PHÁT HIỆN THÂN PHẬN" \
        --subtitle "Tổng Giám Đốc Hùng Phát - Bá Chủ Bình Dương"
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import argparse
import os
import sys
import textwrap

# ─── CONSTANTS ────────────────────────────────────────────────────────────────
CANVAS_SIZE   = 2000
GOLD          = (235, 195, 80, 255)
GOLD_RGB      = (235, 195, 80)
WHITE         = (255, 255, 255, 255)
BLACK         = (0, 0, 0, 255)
SHADOW        = (0, 0, 0, 180)
LABEL_BG      = (10, 8, 5, 215)

FONT_PATHS_BOLD = [
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "/System/Library/Fonts/HelveticaNeue.ttc",
    "/System/Library/Fonts/SFNS.ttf",
]
FONT_PATHS_REGULAR = [
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/Library/Fonts/Arial.ttf",
    "/System/Library/Fonts/HelveticaNeue.ttc",
    "/System/Library/Fonts/SFNS.ttf",
]

def _load_font(paths, size):
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size=size)
            except Exception:
                continue
    return ImageFont.load_default()

def bold(size):
    return _load_font(FONT_PATHS_BOLD, size)

def regular(size):
    return _load_font(FONT_PATHS_REGULAR, size)

# ─── SMART TITLE WRAP ────────────────────────────────────────────────────────
def smart_wrap_title(title: str) -> list:
    """
    Tự động xuống dòng thông minh dựa trên chiều dài tiêu đề.
    Mục tiêu: 2-3 dòng, mỗi dòng cân bằng nhau để font to nhất có thể.
    """
    words = title.split()
    total_chars = len(title)

    # Ngưỡng phân loại
    if total_chars <= 20:
        # Tiêu đề ngắn: 1 dòng
        return [title]
    elif total_chars <= 40:
        # Tiêu đề vừa: 2 dòng cân bằng
        return _wrap_n_lines(words, 2)
    else:
        # Tiêu đề dài: 3 dòng
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

    # Đảm bảo không có quá n_lines dòng
    while len(lines) > n_lines:
        # Gộp 2 dòng cuối
        lines[-2] = lines[-2] + " " + lines[-1]
        lines.pop()

    return lines

# ─── STEP 1: TOP DARK GRADIENT ────────────────────────────────────────────────
def apply_top_gradient(img: Image.Image, fade_end_y: int = 800) -> Image.Image:
    """Apply a strong black-to-transparent gradient from top, for text readability."""
    gradient = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(gradient)
    for y in range(fade_end_y):
        t = 1.0 - (y / fade_end_y)
        alpha = int(230 * t * t)
        draw.rectangle([(0, y), (CANVAS_SIZE, y + 1)], fill=(0, 0, 0, alpha))
    return Image.alpha_composite(img, gradient)

# ─── STEP 2: GOLD DOUBLE BORDER ───────────────────────────────────────────────
def draw_gold_border(draw: ImageDraw.Draw):
    """Draw the premium gold double-border frame with corner ornaments."""
    draw.rectangle([(40, 40), (1960, 1960)], outline=GOLD, width=8)
    draw.rectangle([(80, 80), (1920, 1920)], outline=GOLD, width=3)
    corners = [(80, 80), (1920, 80), (80, 1920), (1920, 1920)]
    for (cx, cy) in corners:
        dx = 1 if cx == 80 else -1
        dy = 1 if cy == 80 else -1
        x0, y0 = min(cx, cx + dx*120), min(cy, cy + dy*120)
        x1, y1 = max(cx, cx + dx*120), max(cy, cy + dy*120)
        draw.rectangle([(x0, y0), (x1, y1)], outline=GOLD, width=3)
        x0s, y0s = min(cx, cx + dx*60), min(cy, cy + dy*60)
        x1s, y1s = max(cx, cx + dx*60), max(cy, cy + dy*60)
        draw.rectangle([(x0s, y0s), (x1s, y1s)], outline=GOLD, width=2)
        draw.ellipse([(cx - 8, cy - 8), (cx + 8, cy + 8)], fill=GOLD)

# ─── STEP 3: TEXT RENDERING ───────────────────────────────────────────────────
def _text_width(font, text):
    bbox = font.getbbox(text)
    return bbox[2] - bbox[0]

def _text_height(font, text):
    bbox = font.getbbox(text)
    return bbox[3] - bbox[1]

def _autofit_font_multiline(text_lines, start_size, max_width, min_size=100, is_bold=True):
    """Return (font_obj, chosen_size) that fits all lines within max_width. Min size = 100px."""
    size = start_size
    while size >= min_size:
        f = bold(size) if is_bold else regular(size)
        fits = all(_text_width(f, ln.upper() if is_bold else ln) <= max_width
                   for ln in text_lines)
        if fits:
            return f, size
        size -= 4
    # Return at minimum size
    f = bold(min_size) if is_bold else regular(min_size)
    return f, min_size

def draw_text_with_shadow(img: Image.Image, lines, font_obj, start_y,
                           line_spacing, text_color, stroke_width=10,
                           to_upper=True) -> Image.Image:
    """Render text with blurred drop-shadow + crisp stroke on top."""
    shadow_layer = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)

    for i, line in enumerate(lines):
        txt = line.upper() if to_upper else line
        w = _text_width(font_obj, txt)
        x = (CANVAS_SIZE - w) // 2
        y = start_y + i * line_spacing
        for off in range(stroke_width * 2, 0, -2):
            a = int(180 * (1 - off / (stroke_width * 2)))
            sd.text((x + 4, y + 7), txt, font=font_obj,
                    fill=(0, 0, 0, a), stroke_width=off, stroke_fill=(0, 0, 0, a))

    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=12))
    img = Image.alpha_composite(img, shadow_layer)

    d = ImageDraw.Draw(img)
    for i, line in enumerate(lines):
        txt = line.upper() if to_upper else line
        w = _text_width(font_obj, txt)
        x = (CANVAS_SIZE - w) // 2
        y = start_y + i * line_spacing
        d.text((x, y), txt, font=font_obj, fill=text_color,
               stroke_width=stroke_width, stroke_fill=BLACK)
    return img

# ─── STEP 4: BOTTOM LABEL ─────────────────────────────────────────────────────
def draw_bottom_label(img: Image.Image, text="TIỂU THUYẾT VIỆT NAM") -> Image.Image:
    """Draw the brand label at the bottom center."""
    label_font = bold(48)
    w = _text_width(label_font, text)
    pad_x, pad_y = 50, 16
    label_w = w + pad_x * 2
    label_h = 90
    x1 = (CANVAS_SIZE - label_w) // 2
    y1 = 1848
    x2 = x1 + label_w
    y2 = y1 + label_h

    overlay = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle([(x1, y1), (x2, y2)], fill=LABEL_BG, outline=GOLD, width=3)

    text_x = x1 + pad_x
    text_y = y1 + (label_h - 48) // 2
    od.text((text_x, text_y), text, font=label_font, fill=WHITE)

    return Image.alpha_composite(img, overlay)

# ─── MAIN FUNCTION ────────────────────────────────────────────────────────────
def apply_standard_overlay(
    input_path: str,
    output_path: str,
    title: str,
    subtitle: str = "",
    bottom_label: str = "TIỂU THUYẾT VIỆT NAM",
) -> bool:
    if not os.path.exists(input_path):
        print(f"❌ Input not found: {input_path}")
        return False

    print(f"🎨 Loading base image: {input_path}")
    img = Image.open(input_path).convert("RGBA")
    img = img.resize((CANVAS_SIZE, CANVAS_SIZE), Image.LANCZOS)

    # Step 1 — Top dark gradient (mạnh hơn để title rõ)
    print("🌑 Applying top dark gradient...")
    img = apply_top_gradient(img, fade_end_y=800)

    # Step 2 — Gold border
    print("⚜️  Drawing gold double border...")
    border_overlay = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    draw_gold_border(ImageDraw.Draw(border_overlay))
    img = Image.alpha_composite(img, border_overlay)

    # Step 3a — Title text (smart wrap trước khi fit)
    # Parse manual newlines first
    if "\\n" in title:
        title_lines = title.split("\\n")
    elif "\n" in title:
        title_lines = title.split("\n")
    else:
        # Auto-wrap thông minh
        title_lines = smart_wrap_title(title)

    print(f"📐 Title wrapped to {len(title_lines)} lines: {title_lines}")

    # Fit font — tối thiểu 100px, bắt đầu 200px
    title_max_w = 1760
    font_title, title_size = _autofit_font_multiline(
        title_lines, start_size=200, max_width=title_max_w, min_size=100, is_bold=True
    )
    title_line_h = int(title_size * 1.25)
    print(f"✍️  Title font size: {title_size}px, lines: {len(title_lines)}")

    img = draw_text_with_shadow(
        img, title_lines, font_title,
        start_y=120, line_spacing=title_line_h,
        text_color=GOLD, stroke_width=10, to_upper=True
    )

    # Step 3b — Subtitle text
    if subtitle:
        sub_lines = subtitle.split("\\n") if "\\n" in subtitle else subtitle.split("\n")
        if len(sub_lines) == 1:
            sub_lines = smart_wrap_title(subtitle) if len(subtitle) > 30 else [subtitle]
        font_sub, sub_size = _autofit_font_multiline(
            sub_lines, start_size=70, max_width=1750, min_size=50, is_bold=False
        )
        sub_start_y = 120 + len(title_lines) * title_line_h + 30
        print(f"📝 Subtitle font size: {sub_size}px")
        img = draw_text_with_shadow(
            img, sub_lines, font_sub,
            start_y=sub_start_y, line_spacing=sub_size + 20,
            text_color=(255, 255, 200, 230), stroke_width=5, to_upper=False
        )

    # Step 4 — Bottom label
    print(f"🏷️  Drawing bottom label: '{bottom_label}'")
    img = draw_bottom_label(img, text=bottom_label)

    out = img.convert("RGB")
    out.save(output_path, "PNG", quality=95)
    print(f"✅ Cover saved: {output_path}")
    return True


# ─── CLI ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Apply standard cover overlay (gold title + border + label)"
    )
    parser.add_argument("--input",    required=True, help="Path to base AI image")
    parser.add_argument("--output",   required=True, help="Path to output PNG")
    parser.add_argument("--title",    required=True, help="Title text (auto-wrapped)")
    parser.add_argument("--subtitle", default="",    help="Optional subtitle/tagline")
    parser.add_argument("--label",    default="TIỂU THUYẾT VIỆT NAM",
                        help="Bottom brand label text")
    args = parser.parse_args()

    ok = apply_standard_overlay(
        input_path=args.input,
        output_path=args.output,
        title=args.title,
        subtitle=args.subtitle,
        bottom_label=args.label,
    )
    sys.exit(0 if ok else 1)
