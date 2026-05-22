#!/usr/bin/env python3
import ftplib
import json
from pathlib import Path

import requests
from PIL import Image, ImageDraw, ImageFilter, ImageFont


FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
SECRET = "ZEN_TRUYEN_2026_BYPASS"

OUT_DIR = Path("scratch/thumbnail_style_covers_20260522")
CANVAS = 1200

FONT_BOLD_PATHS = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "/System/Library/Fonts/HelveticaNeue.ttc",
]

FONT_REGULAR_PATHS = [
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/Library/Fonts/Arial.ttf",
    "/System/Library/Fonts/HelveticaNeue.ttc",
]

STORIES = [
    {
        "id": 2815,
        "chapter": 5,
        "source": "scratch/base_cover_4.png",
        "title_lines": ["HỢP ĐỒNG SINH HỌC", "BỊ CƯỚP", "BẪY IPO TRĂM TỶ"],
        "colors": [(92, 232, 255), (255, 64, 64), (255, 184, 43)],
    },
    {
        "id": 2808,
        "chapter": 5,
        "source": "scratch/base_cover_24.png",
        "title_lines": ["NGƯỜI ĐƯA THƯ", "LÀ CHỦ TÒA NHÀ"],
        "colors": [(92, 232, 255), (255, 184, 43)],
    },
    {
        "id": 2801,
        "chapter": 5,
        "source": "scratch/base_cover_23.png",
        "title_lines": ["TRỌNG TÀI BỊ SỈ NHỤC", "LÀ HUYỀN THOẠI", "QUỐC GIA"],
        "colors": [(255, 255, 255), (255, 184, 43), (92, 232, 255)],
    },
    {
        "id": 2794,
        "chapter": 5,
        "source": "scratch/base_cover_21.png",
        "title_lines": ["NGƯỜI LÀM VƯỜN", "BỊ KHINH", "THIẾT KẾ CẢ ĐÔ THỊ"],
        "colors": [(92, 232, 255), (255, 64, 64), (255, 184, 43)],
    },
    {
        "id": 2787,
        "chapter": 5,
        "source": "scratch/base_cover_20.png",
        "title_lines": ["GIÁO VIÊN LÀNG", "BỊ KHINH", "THANH TRA ĐẶC BIỆT"],
        "colors": [(92, 232, 255), (255, 64, 64), (255, 184, 43)],
    },
    {
        "id": 2780,
        "chapter": 5,
        "source": "scratch/base_cover_11.png",
        "title_lines": ["CÔ GÁI BÁN HOA", "BỊ ĐUỔI", "IPO NGAY HÔM ĐÓ"],
        "colors": [(255, 255, 255), (255, 64, 64), (255, 184, 43)],
    },
]

PHP_HELPER = """<?php
require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

header('Content-Type: application/json');
$secret = "ZEN_TRUYEN_2026_BYPASS";
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret']) || $input['secret'] !== $secret) {
    echo json_encode(['error' => 'Unauthorized']);
    exit;
}

$post_id = intval($input['post_id']);
$filename = sanitize_file_name($input['filename']);
$local_path = ABSPATH . 'wp-content/uploads/' . $filename;
if (!file_exists($local_path)) {
    echo json_encode(['error' => 'File not found: ' . $local_path]);
    exit;
}

$tmp = tempnam(get_temp_dir(), 'cover');
copy($local_path, $tmp);
$file_array = [
    'name' => 'cover-' . $post_id . '-thumbstyle-' . rand(100,999) . '.png',
    'tmp_name' => $tmp,
];
$attach_id = media_handle_sideload($file_array, $post_id);
if (is_wp_error($attach_id)) {
    @unlink($tmp);
    echo json_encode(['error' => $attach_id->get_error_message()]);
    exit;
}

$old_thumb = get_post_thumbnail_id($post_id);
if ($old_thumb) {
    wp_delete_attachment($old_thumb, true);
}
set_post_thumbnail($post_id, $attach_id);
if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}
@unlink($local_path);
echo json_encode([
    'success' => true,
    'post_id' => $post_id,
    'attachment_id' => $attach_id,
    'thumbnail' => get_the_post_thumbnail_url($post_id, 'full'),
], JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
?>"""


def load_font(paths, size):
    for path in paths:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size=size)
            except Exception:
                pass
    return ImageFont.load_default()


def text_size(draw, text, font, stroke_width=0):
    box = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    return box[2] - box[0], box[3] - box[1]


def fit_title_font(draw, lines, max_width, max_height):
    size = 116
    while size >= 58:
        font = load_font(FONT_BOLD_PATHS, size)
        heights = []
        widths = []
        for line in lines:
            w, h = text_size(draw, line, font, stroke_width=5)
            widths.append(w)
            heights.append(h)
        total_height = sum(heights) + (len(lines) - 1) * int(size * 0.16)
        if max(widths) <= max_width and total_height <= max_height:
            return font, size, total_height
        size -= 4
    font = load_font(FONT_BOLD_PATHS, 58)
    return font, 58, max_height


def add_dark_title_gradient(img):
    overlay = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for y in range(0, 520):
        t = 1 - y / 520
        alpha = int(225 * t * t)
        draw.rectangle([(0, y), (CANVAS, y + 1)], fill=(0, 0, 0, alpha))
    for y in range(760, CANVAS):
        t = (y - 760) / (CANVAS - 760)
        alpha = int(110 * t * t)
        draw.rectangle([(0, y), (CANVAS, y + 1)], fill=(0, 0, 0, alpha))
    return Image.alpha_composite(img, overlay)


def draw_text_shadow(base, pos, text, font, fill, stroke_width=5):
    shadow = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    x, y = pos
    sd.text((x + 4, y + 6), text, font=font, fill=(0, 0, 0, 230), stroke_width=stroke_width + 2, stroke_fill=(0, 0, 0, 230))
    shadow = shadow.filter(ImageFilter.GaussianBlur(2))
    base.alpha_composite(shadow)
    draw = ImageDraw.Draw(base)
    draw.text(pos, text, font=font, fill=fill, stroke_width=stroke_width, stroke_fill=(18, 18, 18, 255))


def make_cover(story):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"{story['id']}_cover.png"
    source = Path(story["source"])
    if not source.exists():
        raise FileNotFoundError(source)

    img = Image.open(source).convert("RGBA")
    img = img.resize((CANVAS, CANVAS), Image.Resampling.LANCZOS)
    img = add_dark_title_gradient(img)

    draw = ImageDraw.Draw(img)

    title_font, title_size, total_height = fit_title_font(draw, story["title_lines"], 1080, 350)
    y = 84
    spacing = int(title_size * 0.14)
    for idx, line in enumerate(story["title_lines"]):
        w, h = text_size(draw, line, title_font, stroke_width=5)
        x = (CANVAS - w) // 2
        draw_text_shadow(img, (x, y), line, title_font, story["colors"][idx])
        y += h + spacing

    badge_text = f"Ch.{story['chapter']}"
    badge_font = load_font(FONT_BOLD_PATHS, 38)
    bw, bh = text_size(draw, badge_text, badge_font)
    bx, by = 34, 26
    draw.rounded_rectangle((bx, by, bx + bw + 34, by + 52), radius=18, fill=(35, 190, 127, 255))
    draw.text((bx + 17, by + 7), badge_text, font=badge_font, fill=(255, 255, 255, 255))

    out = img.convert("RGB")
    out.save(out_path, "PNG", optimize=True)
    return out_path


def upload_and_set(covers):
    helper_path = OUT_DIR / "update_cover_local.php"
    helper_path.write_text(PHP_HELPER, encoding="utf-8")
    ftp = ftplib.FTP(FTP_HOST, timeout=60)
    ftp.login(FTP_USER, FTP_PASS)
    results = []
    try:
        with helper_path.open("rb") as handle:
            ftp.storbinary("STOR update_cover_local.php", handle)
        for story, cover_path in covers:
            remote_name = f"thumbstyle_cover_{story['id']}_20260522.png"
            with cover_path.open("rb") as handle:
                ftp.storbinary(f"STOR wp-content/uploads/{remote_name}", handle)
            payload = {"secret": SECRET, "post_id": story["id"], "filename": remote_name}
            res = requests.post(f"{WP_URL}/update_cover_local.php", json=payload, timeout=90)
            try:
                data = res.json()
            except json.JSONDecodeError:
                data = {"error": res.text[:500]}
            print(story["id"], data, flush=True)
            results.append({"id": story["id"], "cover": str(cover_path), "server": data})
    finally:
        try:
            ftp.delete("update_cover_local.php")
        except Exception:
            pass
        ftp.quit()
        try:
            helper_path.unlink()
        except FileNotFoundError:
            pass
    (OUT_DIR / "upload_results.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    return results


def make_contact_sheet(covers):
    sheet = Image.new("RGB", (3 * 360, 2 * 410), "white")
    draw = ImageDraw.Draw(sheet)
    for idx, (story, path) in enumerate(covers):
        img = Image.open(path).convert("RGB")
        img.thumbnail((340, 340))
        x = (idx % 3) * 360 + 10
        y = (idx // 3) * 410 + 10
        sheet.paste(img, (x, y))
        draw.text((x, y + 348), path.name, fill=(0, 0, 0))
    sheet.save(OUT_DIR / "contact_sheet.jpg", quality=92)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--generate-only", action="store_true")
    args = parser.parse_args()

    covers = [(story, make_cover(story)) for story in STORIES]
    make_contact_sheet(covers)
    print(f"Preview: {OUT_DIR / 'contact_sheet.jpg'}", flush=True)
    if not args.generate_only:
        upload_and_set(covers)


if __name__ == "__main__":
    main()
