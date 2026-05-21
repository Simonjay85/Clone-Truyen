#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helper script to apply the classic "old style" gold-framed plaque cover overlay to cover images.
Features:
- Dark semi-transparent plaque background in the upper section.
- Double-border gold frame around the title/subtitle.
- Classic serif bold gold title and white subtitle for absolute legibility.
- Green chapter pill badge in the top-left corner.
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import sys

# Define standard fonts on macOS supplemental folder
FONT_BOLD_SERIF = "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"
FONT_REGULAR_SERIF = "/System/Library/Fonts/Supplemental/Times New Roman.ttf"
FONT_BOLD_SANS = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REGULAR_SANS = "/System/Library/Fonts/Supplemental/Arial.ttf"

def select_fonts():
    """Fallback utility to ensure fonts exist."""
    bold_font = FONT_BOLD_SERIF if os.path.exists(FONT_BOLD_SERIF) else FONT_BOLD_SANS
    regular_font = FONT_REGULAR_SERIF if os.path.exists(FONT_REGULAR_SERIF) else FONT_REGULAR_SANS
    return bold_font, regular_font

def apply_old_style_overlay(input_path, output_path, title, subtitle, chapter_text="Ch.12"):
    if not os.path.exists(input_path):
        print(f"❌ Input file not found: {input_path}")
        return False
        
    img = Image.open(input_path).convert("RGBA")
    
    # Ensure standard high-res size (2000x2000 square)
    img = img.resize((2000, 2000), Image.LANCZOS)
    
    # Create an overlay layer for semi-transparent drawings
    overlay = Image.new("RGBA", (2000, 2000), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # 1. --- DRAW GREEN CHAPTER BADGE (Top-Left) ---
    # Draw pill badge
    badge_x1, badge_y1 = 60, 60
    badge_x2, badge_y2 = 280, 150
    badge_color = (0, 168, 104, 255) # Classic green from the screenshot
    
    draw.rounded_rectangle([(badge_x1, badge_y1), (badge_x2, badge_y2)], radius=45, fill=badge_color)
    
    # Badge text
    bold_font_path, regular_font_path = select_fonts()
    badge_font = ImageFont.truetype(FONT_BOLD_SANS if os.path.exists(FONT_BOLD_SANS) else bold_font_path, 46)
    
    # Center text in pill
    badge_bbox = badge_font.getbbox(chapter_text)
    badge_w = badge_bbox[2] - badge_bbox[0]
    badge_h = badge_bbox[3] - badge_bbox[2] # standard approx
    text_x = badge_x1 + (badge_x2 - badge_x1 - badge_w) // 2
    text_y = badge_y1 + (badge_y2 - badge_y1 - 50) // 2 # offset adjustment
    
    draw.text((text_x, text_y), chapter_text, font=badge_font, fill=(255, 255, 255, 255))
    
    # 2. --- DRAW THE PREMIUM CLASSIC GOLD PLAQUE (Upper-Center) ---
    # Dimensions
    plaque_w = 1680
    plaque_h = 420
    plaque_x1 = (2000 - plaque_w) // 2 # 160
    plaque_y1 = 200
    plaque_x2 = plaque_x1 + plaque_w  # 1840
    plaque_y2 = plaque_y1 + plaque_h  # 620
    
    # Dark semi-transparent backing plate
    backing_color = (12, 12, 12, 215) # Very dark gray/black with high opacity for readability
    draw.rectangle([(plaque_x1, plaque_y1), (plaque_x2, plaque_y2)], fill=backing_color)
    
    # Gold frame borders
    gold_color = (235, 195, 80, 255) # Classic premium gold color
    
    # Outer gold border rectangle (thicker)
    draw.rectangle([(plaque_x1, plaque_y1), (plaque_x2, plaque_y2)], outline=gold_color, width=6)
    
    # Inner gold border rectangle (thinner)
    inset = 14
    inner_x1 = plaque_x1 + inset
    inner_y1 = plaque_y1 + inset
    inner_x2 = plaque_x2 - inset
    inner_y2 = plaque_y2 - inset
    draw.rectangle([(inner_x1, inner_y1), (inner_x2, inner_y2)], outline=gold_color, width=2)
    
    # Decorative Corner Accents (Draw small gold squares at the corners of the inner border)
    corner_size = 12
    # Top-left corner box
    draw.rectangle([(inner_x1 - 2, inner_y1 - 2), (inner_x1 + corner_size, inner_y1 + corner_size)], fill=gold_color)
    # Top-right corner box
    draw.rectangle([(inner_x2 - corner_size, inner_y1 - 2), (inner_x2 + 2, inner_y1 + corner_size)], fill=gold_color)
    # Bottom-left corner box
    draw.rectangle([(inner_x1 - 2, inner_y2 - corner_size), (inner_x1 + corner_size, inner_y2 + 2)], fill=gold_color)
    # Bottom-right corner box
    draw.rectangle([(inner_x2 - corner_size, inner_y2 - corner_size), (inner_x2 + 2, inner_y2 + 2)], fill=gold_color)
    
    # 3. --- DRAW TITLE TEXT INSIDE PLAQUE ---
    # Find fitting font size for Title
    title_size = 125
    title_lines = title.split("\n")
    
    while title_size > 40:
        font_title = ImageFont.truetype(bold_font_path, title_size)
        fits = True
        for line in title_lines:
            bbox = font_title.getbbox(line)
            w = bbox[2] - bbox[0]
            if w > (plaque_w - 100):
                fits = False
                break
        if fits:
            break
        title_size -= 4
        
    font_title = ImageFont.truetype(bold_font_path, title_size)
    
    # Title placement y-coord inside plaque
    # Plaque center-y is (plaque_y1 + plaque_y2) // 2
    plaque_center_y = (plaque_y1 + plaque_y2) // 2
    
    # If single line vs double line
    line_h = title_size + 15
    total_title_h = len(title_lines) * line_h
    
    title_y_start = plaque_center_y - (total_title_h // 2) - 30 # offset up to leave space for line and subtitle
    
    # Draw Title Lines
    for i, line in enumerate(title_lines):
        y = title_y_start + i * line_h
        bbox = font_title.getbbox(line)
        w = bbox[2] - bbox[0]
        x = (2000 - w) // 2
        
        # Dark shadow outline for title text
        draw.text((x, y), line, font=font_title, fill=gold_color,
                  stroke_width=6, stroke_fill=(0, 0, 0, 255))
                  
    # 4. --- DRAW CLASSIC ACCENT LINE INSIDE PLAQUE ---
    line_y = title_y_start + total_title_h + 10
    line_w = 900
    line_x1 = (2000 - line_w) // 2
    line_x2 = line_x1 + line_w
    draw.rectangle([(line_x1, line_y), (line_x2, line_y + 3)], fill=gold_color)
    
    # 5. --- DRAW TAGLINE/SUBTITLE INSIDE PLAQUE ---
    subtitle_size = 46
    font_sub = ImageFont.truetype(regular_font_path, subtitle_size)
    
    # Wrap subtitle if too long
    sub_bbox = font_sub.getbbox(subtitle)
    sub_w = sub_bbox[2] - sub_bbox[0]
    
    sub_x = (2000 - sub_w) // 2
    sub_y = line_y + 20
    
    # Draw Subtitle with crisp black shadow outline
    draw.text((sub_x, sub_y), subtitle, font=font_sub, fill=(255, 255, 255, 255),
              stroke_width=3, stroke_fill=(0, 0, 0, 255))
              
    # Composite the overlay onto the original image
    img = Image.alpha_composite(img, overlay)
    
    # Convert to RGB for clean PNG compression and save
    final_img = img.convert("RGB")
    final_img.save(output_path, "PNG", quality=95)
    print(f"✅ Successfully created classic plaque cover image at: {output_path}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python3 apply_old_style_overlay.py <input> <output> <title> <subtitle> [chapter]")
        print("Example: python3 apply_old_style_overlay.py base.png out.png \"THỢ HỒ NGHÌN TỶ\" \"Bá Chủ Bình Dương - Vả Mặt Tổng Tài!\" \"Ch.12\"")
        sys.exit(1)
        
    in_p = sys.argv[1]
    out_p = sys.argv[2]
    title_str = sys.argv[3].replace("\\n", "\n")
    sub_str = sys.argv[4]
    chapter_str = sys.argv[5] if len(sys.argv) > 5 else "Ch.12"
    
    apply_old_style_overlay(in_p, out_p, title_str, sub_str, chapter_str)
