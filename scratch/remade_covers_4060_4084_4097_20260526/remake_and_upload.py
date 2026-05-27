#!/usr/bin/env python3
import ftplib
import json
import sys
from pathlib import Path

import requests
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from remake_chatgpt_batch2_covers import FTP_HOST, FTP_PASS, FTP_USER, SECRET, WP_URL


ROOT = Path(__file__).resolve().parent
CANVAS = 1200

FONT_BOLD_PATHS = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "/System/Library/Fonts/HelveticaNeue.ttc",
]

STORIES = [
    {
        "id": 4097,
        "source": ROOT / "base/4097_base.png",
        "title_lines": ["VUA ĐÁ QUÝ", "LỤC YÊN", "THÂU TÓM RUBY GIẢ"],
        "colors": [(255, 255, 255), (255, 184, 43), (92, 232, 255)],
    },
    {
        "id": 4084,
        "source": ROOT / "base/4084_base.png",
        "title_lines": ["CƯỚP CÔNG THỨC", "SÂM NGỌC LINH", "LẬT KÈO TẬP ĐOÀN DƯỢC"],
        "colors": [(255, 255, 255), (255, 184, 43), (92, 232, 255)],
    },
    {
        "id": 4060,
        "source": ROOT / "base/4060_base.png",
        "title_lines": ["BỊ HÔN THÊ", "VU OAN CÁ TRA", "THÂU TÓM NGHÌN TỶ"],
        "colors": [(255, 255, 255), (92, 232, 255), (255, 184, 43)],
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
    'name' => 'cover-' . $post_id . '-remade-20260526-' . rand(100,999) . '.png',
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


def load_font(size):
    for path in FONT_BOLD_PATHS:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size=size)
            except Exception:
                pass
    return ImageFont.load_default()


def text_size(draw, text, font, stroke_width=0):
    box = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    return box[2] - box[0], box[3] - box[1]


def fit_font(draw, lines, max_width, max_height):
    size = 108
    while size >= 52:
        font = load_font(size)
        widths, heights = [], []
        for line in lines:
            width, height = text_size(draw, line, font, stroke_width=5)
            widths.append(width)
            heights.append(height)
        total_height = sum(heights) + (len(lines) - 1) * int(size * 0.15)
        if max(widths) <= max_width and total_height <= max_height:
            return font, size
        size -= 3
    return load_font(52), 52


def add_gradients(img):
    overlay = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for y in range(0, 540):
        t = 1 - y / 540
        draw.rectangle((0, y, CANVAS, y + 1), fill=(0, 0, 0, int(238 * t * t)))
    for y in range(810, CANVAS):
        t = (y - 810) / (CANVAS - 810)
        draw.rectangle((0, y, CANVAS, y + 1), fill=(0, 0, 0, int(85 * t * t)))
    return Image.alpha_composite(img, overlay)


def draw_shadowed_text(img, xy, text, font, fill):
    x, y = xy
    shadow = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.text((x + 5, y + 7), text, font=font, fill=(0, 0, 0, 235), stroke_width=7, stroke_fill=(0, 0, 0, 235))
    img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(2)))
    draw = ImageDraw.Draw(img)
    draw.text((x, y), text, font=font, fill=fill, stroke_width=5, stroke_fill=(14, 14, 14, 255))


def make_cover(story):
    img = Image.open(story["source"]).convert("RGBA")
    img = img.resize((CANVAS, CANVAS), Image.Resampling.LANCZOS)
    img = add_gradients(img)
    draw = ImageDraw.Draw(img)
    font, size = fit_font(draw, story["title_lines"], 1080, 335)
    y = 84
    spacing = int(size * 0.15)
    for idx, line in enumerate(story["title_lines"]):
        width, height = text_size(draw, line, font, stroke_width=5)
        draw_shadowed_text(img, ((CANVAS - width) // 2, y), line, font, story["colors"][idx])
        y += height + spacing
    out_path = ROOT / f"{story['id']}_cover.png"
    img.convert("RGB").save(out_path, "PNG", optimize=True)
    return out_path


def make_preview(covers):
    sheet = Image.new("RGB", (3 * 370, 410), "white")
    draw = ImageDraw.Draw(sheet)
    for idx, (story, path) in enumerate(covers):
        thumb = Image.open(path).convert("RGB")
        thumb.thumbnail((350, 350))
        x = idx * 370 + 10
        y = 10
        sheet.paste(thumb, (x, y))
        draw.text((x, y + 360), f"{story['id']} - {path.name}", fill=(0, 0, 0))
    sheet.save(ROOT / "preview_grid.png", quality=94)


def upload(covers):
    helper_path = ROOT / "update_cover_local.php"
    helper_path.write_text(PHP_HELPER, encoding="utf-8")
    ftp = ftplib.FTP(FTP_HOST, timeout=60)
    ftp.login(FTP_USER, FTP_PASS)
    results = []
    try:
        with helper_path.open("rb") as handle:
            ftp.storbinary("STOR update_cover_local.php", handle)
        for story, cover_path in covers:
            remote_name = f"remade_cover_{story['id']}_20260526.png"
            with cover_path.open("rb") as handle:
                ftp.storbinary(f"STOR wp-content/uploads/{remote_name}", handle)
            response = requests.post(
                f"{WP_URL}/update_cover_local.php",
                json={"secret": SECRET, "post_id": story["id"], "filename": remote_name},
                timeout=90,
            )
            try:
                data = response.json()
            except json.JSONDecodeError:
                data = {"error": response.text[:500]}
            print(story["id"], data, flush=True)
            results.append({"id": story["id"], "cover": str(cover_path), "server": data})
    finally:
        try:
            ftp.delete("update_cover_local.php")
        except Exception:
            pass
        ftp.quit()
        helper_path.unlink(missing_ok=True)
    (ROOT / "upload_results.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--generate-only", action="store_true")
    args = parser.parse_args()

    covers = [(story, make_cover(story)) for story in STORIES]
    make_preview(covers)
    print(ROOT / "preview_grid.png", flush=True)
    if not args.generate_only:
        upload(covers)


if __name__ == "__main__":
    main()
