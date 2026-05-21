#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cover_overlay_standard.py — Standard Cover Overlay Engine for doctieuthuyet.com
=================================================================================
Áp dụng text overlay chuẩn lên ảnh bìa đã được AI generate.
Phong cách: Gold title on dark gradient + gold double border + TIỂU THUYẾT VIỆT NAM label.
Không vẽ chapter badge (do WordPress theme tự render).

Usage:
    python3 cover_overlay_standard.py \
        --input base_image.png \
        --output final_cover.png \
        --title "CHÊ ANH THỢ HỒ NGHÈO\nGIÂY SAU PHÁT HIỆN THÂN PHẬN" \
        --subtitle "Tổng Giám Đốc Hùng Phát - Bá Chủ Bình Dương"

Or import and call apply_standard_overlay() directly.
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import argparse
import os
import sys

# ─── CONSTANTS ────────────────────────────────────────────────────────────────
CANVAS_SIZE   = 2000
GOLD          = (235, 195, 80, 255)
GOLD_RGB      = (235, 195, 80)
WHITE         = (255, 255, 255, 255)
BLACK         = (0, 0, 0, 255)
SHADOW        = (0, 0, 0, 180)
LABEL_BG      = (10, 8, 5, 215)

FONT_PATHS_BOLD = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "/System/Library/Fonts/HelveticaNeue.ttc",
    "/System/Library/Fonts/SFNS.ttf",
]
FONT_PATHS_REGULAR = [
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

# ─── STEP 1: TOP DARK GRADIENT ────────────────────────────────────────────────
def apply_top_gradient(img: Image.Image, fade_end_y: int = 620) -> Image.Image:
    """Apply a strong black-to-transparent gradient from top, for text readability."""
    gradient = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(gradient)
    for y in range(fade_end_y):
        # Quadratic ease-out: strongest at top, fades quickly
        t = 1.0 - (y / fade_end_y)
        alpha = int(210 * t * t)
        draw.rectangle([(0, y), (CANVAS_SIZE, y + 1)], fill=(0, 0, 0, alpha))
    return Image.alpha_composite(img, gradient)

# ─── STEP 2: GOLD DOUBLE BORDER ───────────────────────────────────────────────
def draw_gold_border(draw: ImageDraw.Draw):
    """Draw the premium gold double-border frame with corner ornaments."""
    # Outer border
    draw.rectangle([(60, 60), (1940, 1940)], outline=GOLD, width=6)
    # Inner border
    draw.rectangle([(100, 100), (1900, 1900)], outline=GOLD, width=2)
    # Corner ornaments at each corner of inner border
    corners = [(100, 100), (1900, 100), (100, 1900), (1900, 1900)]
    for (cx, cy) in corners:
        dx = 1 if cx == 100 else -1
        dy = 1 if cy == 100 else -1
        # Large square 100x100
        x0, y0 = min(cx, cx + dx*100), min(cy, cy + dy*100)
        x1, y1 = max(cx, cx + dx*100), max(cy, cy + dy*100)
        draw.rectangle([(x0, y0), (x1, y1)], outline=GOLD, width=2)
        # Small square 50x50
        x0s, y0s = min(cx, cx + dx*50), min(cy, cy + dy*50)
        x1s, y1s = max(cx, cx + dx*50), max(cy, cy + dy*50)
        draw.rectangle([(x0s, y0s), (x1s, y1s)], outline=GOLD, width=1)
        # Solid dot 8x8 at corner
        draw.rectangle([(cx - 4, cy - 4), (cx + 4, cy + 4)], fill=GOLD)

# ─── STEP 3: TEXT RENDERING ───────────────────────────────────────────────────
def _text_width(font, text):
    bbox = font.getbbox(text)
    return bbox[2] - bbox[0]

def _autofit_font(text_lines, start_size, step, max_width, is_bold=True):
    """Return (font_obj, chosen_size) that fits all lines within max_width."""
    size = start_size
    while size > 30:
        f = bold(size) if is_bold else regular(size)
        fits = all(_text_width(f, ln.upper() if is_bold else ln) <= max_width
                   for ln in text_lines)
        if fits:
            return f, size
        size -= step
    f = bold(30) if is_bold else regular(30)
    return f, 30

def draw_text_with_shadow(img: Image.Image, lines, font_obj, start_y,
                           line_spacing, text_color, stroke_width=8,
                           to_upper=True) -> Image.Image:
    """Render text with blurred drop-shadow + crisp stroke on top."""
    shadow_layer = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)

    for i, line in enumerate(lines):
        txt = line.upper() if to_upper else line
        w = _text_width(font_obj, txt)
        x = (CANVAS_SIZE - w) // 2
        y = start_y + i * line_spacing
        # Draw thick shadow
        for off in range(stroke_width * 2, 0, -2):
            a = int(160 * (1 - off / (stroke_width * 2)))
            sd.text((x + 3, y + 5), txt, font=font_obj,
                    fill=(0, 0, 0, a), stroke_width=off, stroke_fill=(0, 0, 0, a))

    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=10))
    img = Image.alpha_composite(img, shadow_layer)

    # Crisp text on top
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
    label_font = bold(36)
    w = _text_width(label_font, text)
    pad_x, pad_y = 40, 14
    label_w = w + pad_x * 2
    label_h = 76
    x1 = (CANVAS_SIZE - label_w) // 2
    y1 = 1862
    x2 = x1 + label_w
    y2 = y1 + label_h

    overlay = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle([(x1, y1), (x2, y2)], fill=LABEL_BG, outline=GOLD, width=2)

    text_x = x1 + pad_x
    text_y = y1 + (label_h - 36) // 2
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
    """
    Apply the full standard cover overlay.

    Args:
        input_path: Path to the AI-generated base image.
        output_path: Path to save the final cover PNG.
        title: Main title text. Use \\n to split into multiple lines.
               Will be rendered in UPPERCASE gold.
        subtitle: Optional subtitle/tagline. Rendered in white below title.
        bottom_label: Text for the bottom brand label.

    Returns:
        True if successful, False otherwise.
    """
    if not os.path.exists(input_path):
        print(f"❌ Input not found: {input_path}")
        return False

    print(f"🎨 Loading base image: {input_path}")
    img = Image.open(input_path).convert("RGBA")
    img = img.resize((CANVAS_SIZE, CANVAS_SIZE), Image.LANCZOS)

    # Step 1 — Top dark gradient
    print("🌑 Applying top dark gradient...")
    img = apply_top_gradient(img, fade_end_y=620)

    # Step 2 — Gold border
    print("⚜️  Drawing gold double border...")
    border_overlay = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    draw_gold_border(ImageDraw.Draw(border_overlay))
    img = Image.alpha_composite(img, border_overlay)

    # Step 3a — Title text
    title_lines = title.split("\\n") if "\\n" in title else title.split("\n")
    title_max_w = 1800
    font_title, title_size = _autofit_font(title_lines, start_size=120, step=4,
                                           max_width=title_max_w, is_bold=True)
    title_line_h = title_size + 28
    print(f"✍️  Title font size: {title_size}px, lines: {len(title_lines)}")

    img = draw_text_with_shadow(
        img, title_lines, font_title,
        start_y=140, line_spacing=title_line_h,
        text_color=GOLD, stroke_width=8, to_upper=True
    )

    # Step 3b — Subtitle text
    if subtitle:
        sub_lines = subtitle.split("\\n") if "\\n" in subtitle else subtitle.split("\n")
        font_sub, sub_size = _autofit_font(sub_lines, start_size=52, step=2,
                                           max_width=1750, is_bold=True)
        sub_start_y = 140 + len(title_lines) * title_line_h + 20
        print(f"📝 Subtitle font size: {sub_size}px")
        img = draw_text_with_shadow(
            img, sub_lines, font_sub,
            start_y=sub_start_y, line_spacing=sub_size + 18,
            text_color=(255, 255, 255, 225), stroke_width=4, to_upper=False
        )

    # Step 4 — Bottom label
    print(f"🏷️  Drawing bottom label: '{bottom_label}'")
    img = draw_bottom_label(img, text=bottom_label)

    # Save
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
    parser.add_argument("--title",    required=True, help="Title text (use \\n for newlines)")
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
