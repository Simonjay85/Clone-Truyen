#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates a highly clickbaity premium cover for Novel 2197.
Wording is extremely dramatic, engaging, and curiosity-inducing.
"""

from PIL import Image, ImageDraw, ImageFont
import os
import ftplib
import requests

# Config paths
BASE_IMAGE = "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f/binh_duong_cover_1779390874003.png"
OUTPUT_IMAGE = "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f/cover_2197_titled_v4.png"

FONT_BOLD_SERIF = "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"
FONT_REGULAR_SERIF = "/System/Library/Fonts/Supplemental/Times New Roman.ttf"
FONT_BOLD_SANS = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

def select_fonts():
    bold = FONT_BOLD_SERIF if os.path.exists(FONT_BOLD_SERIF) else FONT_BOLD_SANS
    regular = FONT_REGULAR_SERIF if os.path.exists(FONT_REGULAR_SERIF) else FONT_BOLD_SANS
    return bold, regular

def generate_cover():
    if not os.path.exists(BASE_IMAGE):
        print(f"❌ Base image not found: {BASE_IMAGE}")
        return False
        
    img = Image.open(BASE_IMAGE).convert("RGBA")
    img = img.resize((2000, 2000), Image.LANCZOS)
    
    # Create overlay
    overlay = Image.new("RGBA", (2000, 2000), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # 1. Chapter Badge
    badge_x1, badge_y1 = 60, 60
    badge_x2, badge_y2 = 280, 150
    badge_color = (0, 168, 104, 255) # Premium green
    draw.rounded_rectangle([(badge_x1, badge_y1), (badge_x2, badge_y2)], radius=45, fill=badge_color)
    
    bold_f, regular_f = select_fonts()
    badge_font = ImageFont.truetype(FONT_BOLD_SANS if os.path.exists(FONT_BOLD_SANS) else bold_f, 46)
    chapter_text = "Ch.12"
    badge_bbox = badge_font.getbbox(chapter_text)
    badge_w = badge_bbox[2] - badge_bbox[0]
    text_x = badge_x1 + (badge_x2 - badge_x1 - badge_w) // 2
    text_y = badge_y1 + (badge_y2 - badge_y1 - 50) // 2
    draw.text((text_x, text_y), chapter_text, font=badge_font, fill=(255, 255, 255, 255))
    
    # 2. Premium Plaque Dimensions (Wider and taller for the long title)
    plaque_w = 1840 # Spans almost the full 2000px width
    plaque_h = 560  # Expanded height for long 2-line title and subtitle
    plaque_x1 = (2000 - plaque_w) // 2 # 80
    plaque_y1 = 200
    plaque_x2 = plaque_x1 + plaque_w  # 1920
    plaque_y2 = plaque_y1 + plaque_h  # 760
    
    # Dark semi-transparent plaque background
    backing_color = (12, 12, 12, 220)
    draw.rectangle([(plaque_x1, plaque_y1), (plaque_x2, plaque_y2)], fill=backing_color)
    
    # Gold double borders
    gold_color = (235, 195, 80, 255)
    draw.rectangle([(plaque_x1, plaque_y1), (plaque_x2, plaque_y2)], outline=gold_color, width=6)
    
    inset = 14
    inner_x1 = plaque_x1 + inset
    inner_y1 = plaque_y1 + inset
    inner_x2 = plaque_x2 - inset
    inner_y2 = plaque_y2 - inset
    draw.rectangle([(inner_x1, inner_y1), (inner_x2, inner_y2)], outline=gold_color, width=2)
    
    # Gold corner accents
    corner_size = 12
    draw.rectangle([(inner_x1 - 2, inner_y1 - 2), (inner_x1 + corner_size, inner_y1 + corner_size)], fill=gold_color)
    draw.rectangle([(inner_x2 - corner_size, inner_y1 - 2), (inner_x2 + 2, inner_y1 + corner_size)], fill=gold_color)
    draw.rectangle([(inner_x1 - 2, inner_y2 - corner_size), (inner_x1 + corner_size, inner_y2 + 2)], fill=gold_color)
    draw.rectangle([(inner_x2 - corner_size, inner_y2 - corner_size), (inner_x2 + 2, inner_y2 + 2)], fill=gold_color)
    
    # 3. Dynamic Title Wording
    title_text = "CHÊ ANH THỢ HỒ NGHÈO BẨN THỈU\nGIÂY SAU CHẾT LẶNG PHÁT HIỆN THÂN PHẬN!"
    subtitle_text = "Tổng Giám Đốc Hùng Phát Construction - Bá Chủ Bình Dương!"
    
    title_lines = title_text.split("\n")
    
    # Auto-fit title text font size
    title_size = 85
    while title_size > 30:
        font_title = ImageFont.truetype(bold_f, title_size)
        fits = True
        for line in title_lines:
            bbox = font_title.getbbox(line)
            w = bbox[2] - bbox[0]
            if w > (plaque_w - 80): # Margin check
                fits = False
                break
        if fits:
            break
        title_size -= 2
        
    font_title = ImageFont.truetype(bold_f, title_size)
    print(f"Chosen title font size: {title_size}")
    
    plaque_center_y = (plaque_y1 + plaque_y2) // 2
    line_h = title_size + 20
    total_title_h = len(title_lines) * line_h
    
    title_y_start = plaque_center_y - (total_title_h // 2) - 40
    
    # Draw Title Lines with stroke outline
    for i, line in enumerate(title_lines):
        y = title_y_start + i * line_h
        bbox = font_title.getbbox(line)
        w = bbox[2] - bbox[0]
        x = (2000 - w) // 2
        draw.text((x, y), line, font=font_title, fill=gold_color,
                  stroke_width=6, stroke_fill=(0, 0, 0, 255))
                  
    # 4. Gold separator accent line
    line_y = title_y_start + total_title_h + 15
    line_w = 1200
    line_x1 = (2000 - line_w) // 2
    line_x2 = line_x1 + line_w
    draw.rectangle([(line_x1, line_y), (line_x2, line_y + 3)], fill=gold_color)
    
    # 5. Dynamic Subtitle (white serif with stroke)
    sub_size = 46
    while sub_size > 20:
        font_sub = ImageFont.truetype(regular_f, sub_size)
        bbox = font_sub.getbbox(subtitle_text)
        w = bbox[2] - bbox[0]
        if w < (plaque_w - 80):
            break
        sub_size -= 2
        
    font_sub = ImageFont.truetype(regular_f, sub_size)
    print(f"Chosen subtitle font size: {sub_size}")
    
    sub_bbox = font_sub.getbbox(subtitle_text)
    sub_w = sub_bbox[2] - sub_bbox[0]
    sub_x = (2000 - sub_w) // 2
    sub_y = line_y + 25
    
    draw.text((sub_x, sub_y), subtitle_text, font=font_sub, fill=(255, 255, 255, 255),
              stroke_width=3, stroke_fill=(0, 0, 0, 255))
              
    # Composite and save
    img = Image.alpha_composite(img, overlay)
    final_img = img.convert("RGB")
    final_img.save(OUTPUT_IMAGE, "PNG", quality=95)
    print(f"✅ Premium cover generated successfully at: {OUTPUT_IMAGE}")
    return True

if __name__ == "__main__":
    generate_cover()
