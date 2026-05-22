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

OUT_DIR = Path("scratch/group_f_chatgpt_covers_20260522")
CANVAS = 1200

FONT_BOLD_PATHS = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "/System/Library/Fonts/HelveticaNeue.ttc",
]

STORIES = [
    {
        "id": 2013,
        "chapter": 8,
        "source": OUT_DIR / "base/2013_base.png",
        "title_lines": ["KỸ SƯ BỊ KHINH", "LÁ THƯ CỦA BIỂN", "CỨU CẢ CÁT HẢI"],
        "colors": [(92, 232, 255), (255, 184, 43), (255, 64, 64)],
    },
    {
        "id": 2007,
        "chapter": 8,
        "source": OUT_DIR / "base/2007_base.png",
        "title_lines": ["SẾP CƯỚP CÔNG", "LOG LAB LẬT KÈO", "IPO NGHÌN TỶ"],
        "colors": [(255, 64, 64), (92, 232, 255), (255, 184, 43)],
    },
    {
        "id": 2001,
        "chapter": 8,
        "source": OUT_DIR / "base/2001_base.png",
        "title_lines": ["HỌA SĨ MÙ", "BỊ CƯỚP TRANH", "ĐẤU GIÁ CÂM LẶNG"],
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


def fit_title_font(draw, lines, max_width, max_height):
    size = 112
    while size >= 56:
        font = load_font(size)
        heights = []
        widths = []
        for line in lines:
            w, h = text_size(draw, line, font, stroke_width=5)
            widths.append(w)
            heights.append(h)
        total_height = sum(heights) + (len(lines) - 1) * int(size * 0.16)
        if max(widths) <= max_width and total_height <= max_height:
            return font, size
        size -= 4
    return load_font(56), 56


def add_gradients(img):
    overlay = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for y in range(0, 530):
        t = 1 - y / 530
        draw.rectangle([(0, y), (CANVAS, y + 1)], fill=(0, 0, 0, int(228 * t * t)))
    for y in range(770, CANVAS):
        t = (y - 770) / (CANVAS - 770)
        draw.rectangle([(0, y), (CANVAS, y + 1)], fill=(0, 0, 0, int(120 * t * t)))
    return Image.alpha_composite(img, overlay)


def draw_text_shadow(base, pos, text, font, fill):
    shadow = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    x, y = pos
    sd.text((x + 4, y + 6), text, font=font, fill=(0, 0, 0, 230), stroke_width=7, stroke_fill=(0, 0, 0, 230))
    shadow = shadow.filter(ImageFilter.GaussianBlur(2))
    base.alpha_composite(shadow)
    draw = ImageDraw.Draw(base)
    draw.text(pos, text, font=font, fill=fill, stroke_width=5, stroke_fill=(18, 18, 18, 255))


def make_cover(story):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    img = Image.open(story["source"]).convert("RGBA").resize((CANVAS, CANVAS), Image.Resampling.LANCZOS)
    img = add_gradients(img)
    draw = ImageDraw.Draw(img)
    title_font, title_size = fit_title_font(draw, story["title_lines"], 1080, 350)
    y = 84
    spacing = int(title_size * 0.14)
    for idx, line in enumerate(story["title_lines"]):
        w, h = text_size(draw, line, title_font, stroke_width=5)
        draw_text_shadow(img, ((CANVAS - w) // 2, y), line, title_font, story["colors"][idx])
        y += h + spacing

    badge_text = f"Ch.{story['chapter']}"
    badge_font = load_font(38)
    bw, _ = text_size(draw, badge_text, badge_font)
    draw.rounded_rectangle((34, 26, 34 + bw + 34, 78), radius=18, fill=(35, 190, 127, 255))
    draw.text((51, 33), badge_text, font=badge_font, fill=(255, 255, 255, 255))

    out_path = OUT_DIR / f"{story['id']}_cover.png"
    img.convert("RGB").save(out_path, "PNG", optimize=True)
    return out_path


def make_contact_sheet(covers):
    sheet = Image.new("RGB", (3 * 380, 430), "#eef7ff")
    for idx, (_, cover_path) in enumerate(covers):
        thumb = Image.open(cover_path).convert("RGB").resize((360, 360), Image.Resampling.LANCZOS)
        sheet.paste(thumb, (idx * 380 + 10, 10))
    sheet.save(OUT_DIR / "contact_sheet.jpg", "JPEG", quality=92)


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
            remote_name = f"chatgpt_group_f_cover_{story['id']}_20260522.png"
            with cover_path.open("rb") as handle:
                ftp.storbinary(f"STOR wp-content/uploads/{remote_name}", handle)
            payload = {"secret": SECRET, "post_id": story["id"], "filename": remote_name}
            res = requests.post(f"{WP_URL}/update_cover_local.php", json=payload, timeout=90)
            data = res.json()
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


def main():
    covers = [(story, make_cover(story)) for story in STORIES]
    make_contact_sheet(covers)
    upload_and_set(covers)


if __name__ == "__main__":
    main()
