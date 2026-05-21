#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helper script to apply a premium title text overlay to cover images using PIL.
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import sys

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"

def add_title_to_cover(input_path, output_path, title, subtitle, color_accent_rgb):
    """Add a premium title overlay to a cover image."""
    if not os.path.exists(input_path):
        print(f"❌ Input file not found: {input_path}")
        return False
        
    img = Image.open(input_path).convert("RGBA")
    
    # Resize to standard cover size (2000x2000 square)
    img = img.resize((2000, 2000), Image.LANCZOS)
    
    # --- 1. Add dramatic bottom gradient overlay ---
    gradient = Image.new("RGBA", (2000, 2000), (0, 0, 0, 0))
    grad_draw = ImageDraw.Draw(gradient)
    
    # Bottom gradient: transparent -> dark (covers bottom 55%)
    gradient_start = 900
    for y in range(gradient_start, 2000):
        progress = (y - gradient_start) / (2000 - gradient_start)
        alpha = int(progress * progress * 230)  # quadratic ease-in for dramatic effect
        grad_draw.rectangle([(0, y), (2000, y + 1)], fill=(0, 0, 0, alpha))
    
    # Top gradient: slight vignette
    for y in range(0, 200):
        progress = 1 - (y / 200)
        alpha = int(progress * progress * 100)
        grad_draw.rectangle([(0, y), (2000, y + 1)], fill=(0, 0, 0, alpha))
    
    img = Image.alpha_composite(img, gradient)
    
    # --- 2. Add title text with glow effect ---
    draw = ImageDraw.Draw(img)
    accent = color_accent_rgb
    
    # Title font size - dynamically adjust to prevent overflow on 2000px wide canvas
    lines = title.split("\n")
    title_size = 200  # Increased from 135 to make letters much larger
    max_allowed_width = 1920  # Increased from 1800 to make the title stretch wider (leaves 40px padding on each side)
    
    while title_size > 40:
        font_title = ImageFont.truetype(FONT_BOLD, title_size)
        fits = True
        for line in lines:
            bbox = font_title.getbbox(line)
            width = bbox[2] - bbox[0]
            if width > max_allowed_width:
                fits = False
                break
        if fits:
            break
        title_size -= 4
        
    font_title = ImageFont.truetype(FONT_BOLD, title_size)
    font_subtitle = ImageFont.truetype(FONT_REGULAR, 55)  # Increased subtitle font size from 45 to 55
    
    # Calculate title block position (bottom area)
    line_height = title_size + 24
    total_title_height = len(lines) * line_height
    title_y_start = 2000 - total_title_height - 250  # 250px from bottom
    
    # --- 2a. Draw glow/shadow behind text ---
    glow_layer = Image.new("RGBA", (2000, 2000), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_layer)
    
    for i, line in enumerate(lines):
        y = title_y_start + i * line_height
        bbox = font_title.getbbox(line)
        text_width = bbox[2] - bbox[0]
        x = (2000 - text_width) // 2
        
        # Draw glow (accent color, semi-transparent)
        for offset in range(12, 0, -1):
            glow_alpha = int(40 * (1 - offset / 12))
            glow_color = (accent[0], accent[1], accent[2], glow_alpha)
            glow_draw.text((x, y), line, font=font_title, fill=glow_color,
                          stroke_width=offset * 2, stroke_fill=glow_color)
    
    # Blur the glow
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(radius=8))
    img = Image.alpha_composite(img, glow_layer)
    
    # --- 2b. Draw crisp title text ---
    draw = ImageDraw.Draw(img)
    for i, line in enumerate(lines):
        y = title_y_start + i * line_height
        bbox = font_title.getbbox(line)
        text_width = bbox[2] - bbox[0]
        x = (2000 - text_width) // 2
        
        # Black outline for readability
        draw.text((x, y), line, font=font_title, fill=(255, 255, 255, 255),
                 stroke_width=6, stroke_fill=(0, 0, 0, 200))
    
    # --- 3. Draw accent line ---
    line_y = title_y_start + total_title_height + 30
    accent_rgba = (accent[0], accent[1], accent[2], 220)
    draw.rectangle([(600, line_y), (1400, line_y + 6)], fill=accent_rgba)
    
    # --- 4. Draw subtitle ---
    sub_bbox = font_subtitle.getbbox(subtitle)
    sub_width = sub_bbox[2] - sub_bbox[0]
    sub_x = (2000 - sub_width) // 2
    sub_y = line_y + 36
    draw.text((sub_x, sub_y), subtitle, font=font_subtitle,
             fill=(accent[0], accent[1], accent[2], 230),
             stroke_width=2, stroke_fill=(0, 0, 0, 150))
    
    # --- 5. Add "HOT" badge in top-right ---
    badge_font = ImageFont.truetype(FONT_BOLD, 36)
    badge_x, badge_y = 1750, 60
    draw.rounded_rectangle([(badge_x, badge_y), (badge_x + 180, badge_y + 70)],
                          radius=35, fill=(255, 40, 40, 230))
    draw.text((badge_x + 30, badge_y + 10), "🔥 HOT", font=badge_font,
             fill=(255, 255, 255, 255))
    
    # Convert to RGB for saving as PNG
    output = img.convert("RGB")
    output.save(output_path, "PNG", quality=95)
    print(f"✓ Created titled cover at: {output_path}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: python3 apply_text_overlay.py <input> <output> <title> <subtitle> <accent_r,g,b>")
        sys.exit(1)
        
    in_p = sys.argv[1]
    out_p = sys.argv[2]
    title_str = sys.argv[3].replace("\\n", "\n")
    sub_str = sys.argv[4]
    rgb_str = sys.argv[5]
    
    r, g, b = map(int, rgb_str.split(","))
    add_title_to_cover(in_p, out_p, title_str, sub_str, (r, g, b))
