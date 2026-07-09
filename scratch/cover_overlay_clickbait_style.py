#!/usr/bin/env python3
import argparse
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

SIZE = 2000
FONT_PATHS = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Black.ttf",
    "/System/Library/Fonts/HelveticaNeue.ttc",
    "/System/Library/Fonts/SFNS.ttf",
]
COLORS = [
    (84, 231, 255, 255),
    (255, 62, 74, 255),
    (255, 195, 32, 255),
]


def font(size):
    for path in FONT_PATHS:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size=size)
            except OSError:
                pass
    return ImageFont.load_default()


def text_box(draw, text, font_obj, stroke_width):
    return draw.textbbox((0, 0), text, font=font_obj, stroke_width=stroke_width)


def fit_font(lines, max_width, start=154, minimum=82):
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    for size in range(start, minimum - 1, -4):
        f = font(size)
        if all(text_box(probe, line.upper(), f, 12)[2] <= max_width for line in lines):
            return f, size
    return font(minimum), minimum


def add_top_shadow(img):
    overlay = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for y in range(0, 850):
        t = y / 850
        alpha = int(245 * (1 - t) + 35 * t)
        draw.line([(0, y), (SIZE, y)], fill=(0, 0, 0, alpha))
    return Image.alpha_composite(img, overlay)


def add_title(img, title):
    lines = [line.strip().upper() for line in title.replace("\\n", "\n").split("\n") if line.strip()]
    lines = lines[:3]
    draw = ImageDraw.Draw(img)
    title_font, size = fit_font(lines, max_width=1780)
    line_h = int(size * 1.14)
    start_y = 115

    shadow = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    for idx, line in enumerate(lines):
        bbox = text_box(draw, line, title_font, 14)
        x = (SIZE - (bbox[2] - bbox[0])) // 2
        y = start_y + idx * line_h
        sd.text((x + 8, y + 12), line, font=title_font, fill=(0, 0, 0, 230),
                stroke_width=20, stroke_fill=(0, 0, 0, 230))
    shadow = shadow.filter(ImageFilter.GaussianBlur(7))
    img = Image.alpha_composite(img, shadow)

    draw = ImageDraw.Draw(img)
    for idx, line in enumerate(lines):
        bbox = text_box(draw, line, title_font, 12)
        x = (SIZE - (bbox[2] - bbox[0])) // 2
        y = start_y + idx * line_h
        draw.text((x, y), line, font=title_font, fill=COLORS[idx % len(COLORS)],
                  stroke_width=12, stroke_fill=(0, 0, 0, 255))
    return img


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()

    img = Image.open(args.input).convert("RGBA")
    img = img.resize((SIZE, SIZE), Image.Resampling.LANCZOS)
    img = add_top_shadow(img)
    img = add_title(img, args.title)
    img.convert("RGB").save(args.output, "PNG", quality=95)
    print(args.output)


if __name__ == "__main__":
    main()
