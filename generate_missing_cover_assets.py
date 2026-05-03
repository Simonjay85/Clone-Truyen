import argparse
import html
import json
import math
import os
import random
import re
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


W, H = 1200, 800


PALETTES = {
    "fire": ("#2b0b0b", "#b91c1c", "#f97316", "#fde68a"),
    "crime": ("#07111f", "#1e293b", "#7f1d1d", "#f8fafc"),
    "wealth": ("#111827", "#0f766e", "#f59e0b", "#ecfeff"),
    "romance": ("#3b1027", "#be185d", "#fb7185", "#fff1f2"),
    "palace": ("#1f1537", "#7c2d12", "#d97706", "#fef3c7"),
    "sea": ("#06283d", "#0e7490", "#38bdf8", "#ecfeff"),
    "school": ("#172554", "#2563eb", "#facc15", "#eff6ff"),
    "medical": ("#083344", "#0f766e", "#14b8a6", "#ecfeff"),
    "default": ("#111827", "#4338ca", "#22c55e", "#f8fafc"),
}


def clean_title(value):
    value = html.unescape(value or "")
    value = re.sub(r"\s+", " ", value).strip()
    return value


def classify(title):
    t = title.lower()
    rules = [
        ("fire", ["cứu hỏa", "cháy", "lửa"]),
        ("crime", ["sát nhân", "ma túy", "án mạng", "hung thủ", "dao", "đen tối"]),
        ("wealth", ["100 tỷ", "10 tỷ", "công ty", "chủ tịch", "tổng giám đốc", "siêu giàu", "thừa kế", "hào môn"]),
        ("romance", ["bạn trai", "chồng", "hôn nhân", "cưới", "người tình", "mẹ chồng", "con dâu"]),
        ("palace", ["phi tần", "triều đình", "đích nữ", "gia tộc", "kiếp trước"]),
        ("sea", ["làng chài", "biển", "mưa"]),
        ("school", ["học sinh", "trường học", "họp lớp"]),
        ("medical", ["bác sĩ", "bệnh viện"]),
    ]
    for key, words in rules:
        if any(word in t for word in words):
            return key
    return "default"


def font(size, bold=False):
    candidates = [
        "/System/Library/Fonts/SFNS.ttf",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size=size, index=0)
    return ImageFont.load_default()


def wrap_text(draw, text, font_obj, max_width, max_lines):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        probe = (current + " " + word).strip()
        if draw.textbbox((0, 0), probe, font=font_obj)[2] <= max_width:
            current = probe
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(".,;:") + "..."
    return lines


def gradient(bg, c1, c2):
    base = Image.new("RGB", (W, H), c1)
    top = Image.new("RGB", (W, H), c2)
    mask = Image.new("L", (W, H))
    md = ImageDraw.Draw(mask)
    for y in range(H):
        md.line((0, y, W, y), fill=int(255 * y / H))
    return Image.composite(top, base, mask)


def add_scene(draw, kind, colors, rng):
    dark, mid, accent, light = colors
    for _ in range(34):
        x = rng.randint(-80, W)
        y = rng.randint(-80, H)
        r = rng.randint(30, 170)
        fill = accent if rng.random() > 0.45 else mid
        draw.ellipse((x, y, x + r, y + r), fill=fill + "28")

    horizon = 560
    draw.rectangle((0, horizon, W, H), fill="#050816aa")

    if kind == "fire":
        draw.rectangle((760, 220, 1010, horizon), fill="#1f2937")
        draw.rectangle((810, 280, 855, 360), fill="#f59e0b")
        for x in range(140, 620, 90):
            draw.polygon([(x, 610), (x + 40, 420), (x + 90, 610)], fill="#f97316cc")
            draw.polygon([(x + 25, 610), (x + 50, 500), (x + 78, 610)], fill="#fde68acc")
    elif kind == "sea":
        for i in range(7):
            y = 520 + i * 35
            draw.arc((80, y, 1120, y + 90), 180, 360, fill="#bae6fd99", width=5)
        draw.polygon([(760, 500), (930, 320), (1080, 500)], fill="#e0f2fe88")
    elif kind == "palace":
        draw.rectangle((720, 300, 1020, horizon), fill="#3b0764")
        for x in (760, 860, 960):
            draw.polygon([(x - 45, 300), (x, 200), (x + 45, 300)], fill="#f59e0b")
            draw.rectangle((x - 32, 300, x + 32, horizon), fill="#581c87")
    elif kind == "medical":
        draw.rounded_rectangle((760, 250, 1040, 560), radius=24, fill="#ecfeffcc")
        draw.rectangle((875, 315, 925, 495), fill="#ef4444")
        draw.rectangle((810, 380, 990, 430), fill="#ef4444")
    elif kind == "school":
        draw.rectangle((710, 250, 1060, horizon), fill="#1e3a8a")
        for x in range(750, 1030, 70):
            draw.rectangle((x, 310, x + 36, 360), fill="#dbeafe")
        draw.polygon([(700, 250), (885, 150), (1070, 250)], fill="#facc15")
    elif kind == "wealth":
        draw.rectangle((760, 240, 1040, horizon), fill="#042f2e")
        for y in range(300, 520, 54):
            draw.line((800, y, 1000, y), fill="#fbbf24", width=6)
        draw.ellipse((885, 160, 955, 230), fill="#fbbf24")
    else:
        draw.rectangle((760, 260, 1030, horizon), fill="#111827")
        draw.polygon([(735, 260), (895, 150), (1055, 260)], fill="#22c55e")

    draw.ellipse((220, 250, 430, 460), fill="#0f172a")
    draw.rounded_rectangle((170, 430, 480, 690), radius=120, fill="#111827")
    draw.line((290, 462, 235, 650), fill=accent, width=9)
    draw.line((360, 462, 420, 650), fill=accent, width=9)


def render(item, out_dir):
    title = clean_title(item["title"])
    kind = classify(title)
    colors = PALETTES[kind]
    rng = random.Random(int(item["id"]))
    img = gradient(Image.new("RGB", (W, H)), colors[0], colors[1])
    draw = ImageDraw.Draw(img, "RGBA")
    add_scene(draw, kind, colors, rng)

    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay, "RGBA")
    od.rectangle((0, 0, 690, H), fill=(5, 8, 22, 185))
    od.rectangle((0, 0, 690, H), fill=(255, 255, 255, 18))
    img = Image.alpha_composite(img.convert("RGBA"), overlay)
    draw = ImageDraw.Draw(img, "RGBA")

    title_font = font(58, bold=True)
    small_font = font(24)
    badge_font = font(28)
    lines = wrap_text(draw, title.upper(), title_font, 560, 5)
    y = 210
    for line in lines:
        draw.text((72, y), line, font=title_font, fill="#ffffff")
        y += 68

    draw.rounded_rectangle((72, 92, 330, 142), radius=25, fill=colors[2])
    draw.text((96, 101), "DOC TIEU THUYET", font=small_font, fill="#ffffff")
    draw.line((74, y + 16, 430, y + 16), fill=colors[3], width=4)
    draw.text((72, 690), "Anh dai dien 1200x800", font=badge_font, fill="#e5e7eb")

    img = img.convert("RGB").filter(ImageFilter.UnsharpMask(radius=1, percent=120, threshold=3))
    out_path = out_dir / f"{item['id']}.jpg"
    img.save(out_path, "JPEG", quality=92, optimize=True)
    return out_path


def render_team_assets(out_dir):
    teams = [
        ("team1.jpeg", "Meo Kam Map", "fire"),
        ("team2.jpeg", "Lac Gioi Tinh Thu", "palace"),
        ("team3.jpeg", "Moi Ngay Chi Muon", "romance"),
        ("team4.jpeg", "Ca Chep Ngam Mua", "sea"),
        ("team5.jpeg", "Trong Tim Co Cau", "romance"),
        ("team6.jpeg", "O Mat Mat", "wealth"),
        ("team7.jpeg", "Nguyet Sat Tinh", "crime"),
        ("team8.jpeg", "Meo Bung Beo", "default"),
    ]
    out_dir.mkdir(parents=True, exist_ok=True)
    title_font = font(72, bold=True)
    small_font = font(30)
    for idx, (name, label, kind) in enumerate(teams, start=1):
        colors = PALETTES[kind]
        rng = random.Random(9000 + idx)
        img = gradient(Image.new("RGB", (W, H)), colors[0], colors[1])
        draw = ImageDraw.Draw(img, "RGBA")
        add_scene(draw, kind, colors, rng)
        draw.rounded_rectangle((78, 78, 690, 310), radius=44, fill=(5, 8, 22, 170))
        draw.text((120, 120), label.upper(), font=title_font, fill="#ffffff")
        draw.text((124, 226), "Team Doc Tieu Thuyet", font=small_font, fill="#e5e7eb")
        draw.ellipse((880, 150, 1090, 360), fill=colors[2])
        draw.text((945, 206), str(idx), font=font(104, bold=True), fill="#ffffff")
        img.convert("RGB").save(out_dir / name, "JPEG", quality=92, optimize=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="/tmp/missing-covers.json")
    parser.add_argument("--out", default="generated_covers")
    parser.add_argument("--team-out", default="tehi-theme/templates/images")
    args = parser.parse_args()
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(args.input, "r", encoding="utf-8") as f:
        items = json.load(f)
    for item in items:
        path = render(item, out_dir)
        print(path)
    render_team_assets(Path(args.team_out))


if __name__ == "__main__":
    main()
