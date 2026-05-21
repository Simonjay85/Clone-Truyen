#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V5 Standardized Cover Generator for Novel 2197.
Generates an elegant gold double-border framed cover with premium modern Sans-Serif Bold typography,
matching the layout of popular covers like "Triều Đại Cà Phê Bazan Đắk Lắk".
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import sys

BASE_IMAGE = "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f/binh_duong_cover_1779390874003.png"
OUTPUT_IMAGE = "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f/cover_2197_standard_v5.png"

GOLD_COLOR = (235, 195, 80, 255) # Classic premium metallic gold
DARK_GOLD_BG = (15, 10, 5, 220)  # Dark translucent background for bottom compartment
WHITE_COLOR = (255, 255, 255, 255)

def get_bold_font(size):
    paths = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/System/Library/Fonts/SFNS.ttf"
    ]
    for path in paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size=size)
            except Exception:
                continue
    return ImageFont.load_default()

def get_regular_font(size):
    paths = [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/System/Library/Fonts/SFNS.ttf"
    ]
    for path in paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size=size)
            except Exception:
                continue
    return ImageFont.load_default()

def draw_corner_ornament(draw, x_center, y_center, is_left, is_top):
    """Draws elegant interlocking gold nested squares and anchoring lines in the corner."""
    d = 1 if is_left else -1
    dy = 1 if is_top else -1
    
    # 1. Outer to Inner frame anchoring connection lines (length 35px)
    draw.line([(x_center, y_center - dy * 35), (x_center, y_center)], fill=GOLD_COLOR, width=2)
    draw.line([(x_center - d * 35, y_center), (x_center, y_center)], fill=GOLD_COLOR, width=2)
    
    # 2. Large nested square (side length = 120px)
    x0, y0 = x_center, y_center
    x1, y1 = x_center + d * 120, y_center + dy * 120
    draw.rectangle([
        (min(x0, x1), min(y0, y1)), 
        (max(x0, x1), max(y0, y1))
    ], outline=GOLD_COLOR, width=2)
    
    # 3. Small nested square (side length = 60px)
    x2, y2 = x_center + d * 60, y_center + dy * 60
    draw.rectangle([
        (min(x0, x2), min(y0, y2)), 
        (max(x0, x2), max(y0, y2))
    ], outline=GOLD_COLOR, width=2)
    
    # 4. Small filled gold square accents (10x10px) at the square corners for depth
    accent_w = 10
    cx1, cy1 = x_center + d * 120, y_center + dy * 120
    draw.rectangle([
        (min(cx1 - accent_w//2, cx1 + accent_w//2), min(cy1 - accent_w//2, cy1 + accent_w//2)),
        (max(cx1 - accent_w//2, cx1 + accent_w//2), max(cy1 - accent_w//2, cy1 + accent_w//2))
    ], fill=GOLD_COLOR)
    
    cx2, cy2 = x_center + d * 60, y_center + dy * 60
    draw.rectangle([
        (min(cx2 - accent_w//2, cx2 + accent_w//2), min(cy2 - accent_w//2, cy2 + accent_w//2)),
        (max(cx2 - accent_w//2, cx2 + accent_w//2), max(cy2 - accent_w//2, cy2 + accent_w//2))
    ], fill=GOLD_COLOR)

def draw_text_with_glow(img, lines, font_obj, start_y, line_height, text_color, is_caps=True):
    """Renders text with a heavy, professional blurred black drop shadow glow for maximum legibility."""
    glow_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_layer)
    
    # Draw drop shadow layers offset by 2px on all sides for soft volume
    for i, line in enumerate(lines):
        if is_caps:
            line = line.upper()
        bbox = font_obj.getbbox(line)
        w = bbox[2] - bbox[0]
        x = (2000 - w) // 2
        y = start_y + i * line_height
        
        # Overlay thick shadow lines offset downward-right slightly
        for offset in range(12, 0, -1):
            alpha = int(45 * (1 - offset / 12))
            glow_draw.text((x + 2, y + 4), line, font=font_obj, fill=(0, 0, 0, alpha),
                           stroke_width=offset * 2, stroke_fill=(0, 0, 0, alpha))
            
    # Apply elegant Gaussian blur to the shadow layer
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(radius=6))
    
    # Merge shadow back to source image
    img = Image.alpha_composite(img, glow_layer)
    
    # Draw crisp gold text directly on top with fine black outline for ultra readability
    draw = ImageDraw.Draw(img)
    for i, line in enumerate(lines):
        if is_caps:
            line = line.upper()
        bbox = font_obj.getbbox(line)
        w = bbox[2] - bbox[0]
        x = (2000 - w) // 2
        y = start_y + i * line_height
        
        draw.text((x, y), line, font=font_obj, fill=text_color,
                  stroke_width=5, stroke_fill=(0, 0, 0, 255))
                  
    return img

def main():
    if not os.path.exists(BASE_IMAGE):
        print(f"❌ Base image not found: {BASE_IMAGE}")
        sys.exit(1)
        
    print("🎨 Initializing base image (2000x2000 format)...")
    img = Image.open(BASE_IMAGE).convert("RGBA")
    img = img.resize((2000, 2000), Image.LANCZOS)
    
    # Create overlay drawing context
    overlay = Image.new("RGBA", (2000, 2000), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # --- 1. DRAW ELABORATE GOLD DOUBLE FRAME ---
    print("⚜️ Drawing premium double gold border frame...")
    
    # Outer frame: (75, 75) to (1925, 1925), width = 6px
    draw.rectangle([(75, 75), (1925, 1925)], outline=GOLD_COLOR, width=6)
    
    # Inner frame: (110, 110) to (1890, 1890), width = 2px
    draw.rectangle([(110, 110), (1890, 1890)], outline=GOLD_COLOR, width=2)
    
    # Draw interlocking corner designs
    draw_corner_ornament(draw, 110, 110, is_left=True, is_top=True)     # Top-Left
    draw_corner_ornament(draw, 1890, 110, is_left=False, is_top=True)   # Top-Right
    draw_corner_ornament(draw, 110, 1890, is_left=True, is_top=False)   # Bottom-Left
    draw_corner_ornament(draw, 1890, 1890, is_left=False, is_top=False) # Bottom-Right
    
    # --- 2. DRAW BOTTOM compartment FOR "TIỂU THUYẾT VIỆT NAM" ---
    print("🇻🇳 Drawing bottom banner label...")
    
    comp_x1, comp_y1 = 670, 1855
    comp_x2, comp_y2 = 1330, 1925
    
    # Translucent gold backing compartment
    draw.rectangle([(comp_x1, comp_y1), (comp_x2, comp_y2)], fill=DARK_GOLD_BG)
    draw.rectangle([(comp_x1, comp_y1), (comp_x2, comp_y2)], outline=GOLD_COLOR, width=2)
    
    # Draw bottom text inside compartment
    bottom_font = get_bold_font(34)
    bottom_text = "TIỂU THUYẾT VIỆT NAM"
    bot_bbox = bottom_font.getbbox(bottom_text)
    bot_w = bot_bbox[2] - bot_bbox[0]
    bot_h = bot_bbox[3] - bot_bbox[1]
    
    bot_x = comp_x1 + (660 - bot_w) // 2
    bot_y = comp_y1 + (70 - bot_h) // 2 - 2  # centering adjust
    
    draw.text((bot_x, bot_y), bottom_text, font=bottom_font, fill=WHITE_COLOR)
    
    # Composite the border layer onto the image
    img = Image.alpha_composite(img, overlay)
    
    # --- 3. DYNAMIC TITLE WRITING ---
    print("✍️ Drawing modern Sans-Serif titles at the top...")
    
    title_text = "CHÊ ANH THỢ HỒ NGHÈO BẨN THỈU\nGIÂY SAU CHẾT LẶNG PHÁT HIỆN THÂN PHẬN!"
    title_lines = title_text.split("\n")
    
    # Auto-fit title text font size
    max_w = 1750  # maximum allowed text width inside borders
    title_size = 90
    
    while title_size > 30:
        test_font = get_bold_font(title_size)
        fits = True
        for line in title_lines:
            bbox = test_font.getbbox(line.upper())
            w = bbox[2] - bbox[0]
            if w > max_w:
                fits = False
                break
        if fits:
            break
        title_size -= 2
        
    font_title = get_bold_font(title_size)
    print(f"✓ Selected title size: {title_size}px")
    
    # Line height & positioning
    line_h = title_size + 20
    start_y = 200  # starting position at top center
    
    # Render title text with drop shadow glow
    img = draw_text_with_glow(img, title_lines, font_title, start_y, line_h, GOLD_COLOR, is_caps=True)
    
    # --- 4. SUBTITLE WRITING ---
    subtitle_text = "Tổng Giám Đốc Hùng Phát Construction - Bá Chủ Bình Dương!"
    sub_size = 46
    
    while sub_size > 20:
        test_font = get_bold_font(sub_size)
        bbox = test_font.getbbox(subtitle_text)
        w = bbox[2] - bbox[0]
        if w < max_w:
            break
        sub_size -= 2
        
    font_sub = get_bold_font(sub_size)
    print(f"✓ Selected subtitle size: {sub_size}px")
    
    sub_y = start_y + len(title_lines) * line_h + 30
    
    # Render subtitle with drop shadow glow
    img = draw_text_with_glow(img, [subtitle_text], font_sub, sub_y, sub_size + 10, WHITE_COLOR, is_caps=False)
    
    # Convert and Save final image
    final_img = img.convert("RGB")
    final_img.save(OUTPUT_IMAGE, "PNG", quality=95)
    print(f"✅ V5 Standardized Cover saved successfully to: {OUTPUT_IMAGE}")

if __name__ == "__main__":
    main()
