#!/usr/bin/env python3
"""
Add premium title text overlay to novel cover images.
Creates eye-catching covers with gradient overlay + glowing title text.
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os

ARTIFACT_DIR = "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f"
OUTPUT_DIR = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/covers_with_title"
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"

COVERS = [
    {
        "id": 2120,
        "file": f"{ARTIFACT_DIR}/cover_bep_truong_1779287633925.png",
        "title": "MẸ VỢ BẮT RỬA BÁT\nTÔI NẤU TIỆC MICHELIN\nCHẤN ĐỘNG PHÚ QUỐC",
        "subtitle": "Phú Quốc • Michelin • Siêu Sảng",
        "color_accent": (255, 180, 50),  # golden
    },
    {
        "id": 2137,
        "file": f"{ARTIFACT_DIR}/cover_thua_ke_1779287651453.png",
        "title": "MẸ VỢ ĐÒI SÍNH LỄ 5 TỶ\nKHINH TÔI NGHÈO\nLANDMARK 81 LÀ CỦA TÔI",
        "subtitle": "Landmark 81 • Hào Môn Lật Kèo",
        "color_accent": (255, 215, 0),  # gold
    },
    {
        "id": 2145,
        "file": f"{ARTIFACT_DIR}/cover_duoc_pham_1779287668090.png",
        "title": "SẾP CƯỚP CÔNG THỨC THUỐC\nĐUỔI TÔI KHỎI LAB\nTÔI PHÁ SẬP IPO NGHÌN TỶ",
        "subtitle": "Đà Lạt • HoSE • Đại Đông Dược",
        "color_accent": (0, 230, 180),  # teal/emerald
    },
    {
        "id": 2156,
        "file": f"{ARTIFACT_DIR}/cover_vo_than_1779287684148.png",
        "title": "TIỂU THƯ KHINH BẢO VỆ\nKHÔNG NGỜ TÔI LÀ\nĐẶC NHIỆM HẠNG NHẤT",
        "subtitle": "Hải Phòng • Đình Vũ • Siêu Đặc Nhiệm",
        "color_accent": (255, 60, 60),  # red
    },
    {
        "id": 2165,
        "file": f"{ARTIFACT_DIR}/cover_fintech_1779287702263.png",
        "title": "BẠN THÂN CƯỚP STARTUP\nĐUỔI TÔI RA ĐƯỜNG\nTÔI BANK RUN SẬP ĐẾ CHẾ HẮN",
        "subtitle": "Blockchain • Duy Tân • Fintech",
        "color_accent": (100, 140, 255),  # electric blue
    },
]


def add_title_to_cover(cover_info):
    """Add a premium title overlay to a cover image."""
    img = Image.open(cover_info["file"]).convert("RGBA")
    
    # Resize to standard cover size (2000x2000 square)
    img = img.resize((2000, 2000), Image.LANCZOS)
    
    # --- 1. Add dramatic bottom gradient overlay ---
    gradient = Image.new("RGBA", (2000, 2000), (0, 0, 0, 0))
    grad_draw = ImageDraw.Draw(gradient)
    
    # Bottom gradient: transparent -> dark (covers bottom 55%)
    gradient_start = 900  # start y (since height is 2000 now)
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
    accent = cover_info["color_accent"]
    
    # Title font size - dynamically adjust to prevent overflow on 2000px wide canvas
    lines = cover_info["title"].split("\n")
    title_size = 135
    max_allowed_width = 1800  # leaves 100px padding on each side
    
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
    font_subtitle = ImageFont.truetype(FONT_REGULAR, 45)
    
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
    subtitle = cover_info["subtitle"]
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
    output_path = os.path.join(OUTPUT_DIR, f"cover_{cover_info['id']}_titled.png")
    output.save(output_path, "PNG", quality=95)
    
    print(f"✓ Story {cover_info['id']}: {output_path}")
    return output_path


def main():
    print("=" * 60)
    print("🎨 ADDING PREMIUM TITLES TO COVER IMAGES")
    print("=" * 60)
    
    results = {}
    for cover in COVERS:
        if not os.path.exists(cover["file"]):
            print(f"❌ Missing: {cover['file']}")
            continue
        path = add_title_to_cover(cover)
        results[cover["id"]] = path
    
    print(f"\n✓ Generated {len(results)} titled covers in {OUTPUT_DIR}")
    return results


if __name__ == "__main__":
    main()
