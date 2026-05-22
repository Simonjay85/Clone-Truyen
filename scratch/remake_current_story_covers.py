#!/usr/bin/env python3
import ftplib
import json
import random
import time
import urllib.parse
from pathlib import Path

import requests
from PIL import Image

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from cover_overlay_standard import apply_standard_overlay


FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
SECRET = "ZEN_TRUYEN_2026_BYPASS"

OUT_DIR = Path("scratch/remade_covers_20260522")

STORIES = [
    {
        "id": 2815,
        "title": "Kỹ Sư Sơn Mài Bị Đuổi Khỏi Lab, Hợp Đồng Sinh Học Trăm Tỷ Lật Kèo Phút Chót Ngày IPO",
        "display_title": "Kỹ Sư Sơn Mài\nLật Kèo IPO",
        "subtitle": "Hợp đồng sinh học trăm tỷ",
        "source": "scratch/base_cover_4.png",
        "visual": "Vietnamese biotech laboratory fused with lacquer art, brilliant gold resin panels, young engineer in lab coat holding contract, IPO countdown board, dramatic corporate betrayal, luxury cinematic lighting",
    },
    {
        "id": 2808,
        "title": "Người Đưa Thư Bị Cả Tòa Nhà Cao Cấp Coi Thường, Anh Là Chủ Sở Hữu Tòa Nhà Đó",
        "display_title": "Người Đưa Thư\nChủ Tòa Nhà",
        "subtitle": "Cả cao ốc cúi đầu",
        "source": "scratch/base_cover_24.png",
        "visual": "humble Vietnamese mailman standing in front of a luxury high-rise lobby, security guards shocked, property deed glowing in hand, modern city drama, gold and teal cinematic light",
    },
    {
        "id": 2801,
        "title": "Trọng Tài Bóng Đá Bị Cầu Thủ Ngôi Sao Xúc Phạm, Hóa Ra Là Cựu Danh Thủ Số 1 Quốc Gia",
        "display_title": "Trọng Tài Bị Sỉ Nhục\nLà Huyền Thoại",
        "subtitle": "Cựu danh thủ số 1 quốc gia",
        "source": "scratch/base_cover_23.png",
        "visual": "Vietnamese football stadium at night, stern referee holding whistle, arrogant star player frozen in shock, championship trophy silhouette, roaring crowd, cinematic sports drama poster",
    },
    {
        "id": 2794,
        "title": "Người Làm Vườn Bị Gia Đình Chủ Biệt Thự Khinh, Lộ Ra Là Kiến Trúc Sư Thiết Kế Cả Khu Đô Thị Đó",
        "display_title": "Người Làm Vườn\nThiết Kế Đô Thị",
        "subtitle": "Cả biệt thự phải im lặng",
        "source": "scratch/base_cover_21.png",
        "visual": "quiet Vietnamese gardener in elegant villa garden, luxury masterplan blueprint glowing behind him, wealthy family shocked on marble steps, modern urban skyline, cinematic revenge reveal",
    },
    {
        "id": 2787,
        "title": "Giáo Viên Làng Bị Hiệu Trưởng Khinh Thường, Bộ Giáo Dục Bổ Nhiệm Anh Làm Thanh Tra Đặc Biệt",
        "display_title": "Giáo Viên Làng\nThanh Tra Đặc Biệt",
        "subtitle": "Bộ Giáo Dục bổ nhiệm",
        "source": "scratch/base_cover_20.png",
        "visual": "rural Vietnamese teacher standing calmly in a school courtyard, official education ministry inspectors arriving, principal stunned, warm sunrise and authoritative cinematic drama",
    },
    {
        "id": 2780,
        "title": "Cô Gái Bán Hoa Bị Đám Cưới Nhà Giàu Đuổi Ra, Tập Đoàn Hoa Tươi Của Cô Niêm Yết Ngay Hôm Đó",
        "display_title": "Cô Gái Bán Hoa\nNiêm Yết Tập Đoàn",
        "subtitle": "Đám cưới nhà giàu chết lặng",
        "source": "scratch/base_cover_11.png",
        "visual": "Vietnamese flower seller woman outside a luxury wedding ballroom, elegant floral corporation IPO screen behind her, wealthy guests shocked, roses and gold confetti, cinematic corporate revenge poster",
    },
]

PHP_HELPER = """<?php
require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

header('Content-Type: application/json');

$secret = "ZEN_TRUYEN_2026_BYPASS";
$raw = file_get_contents('php://input');
$input = json_decode($raw, true);

if (!isset($input['secret']) || $input['secret'] !== $secret) {
    echo json_encode(['error' => 'Unauthorized']);
    exit;
}

$post_id = intval($input['post_id']);
$filename = sanitize_file_name($input['filename']);
$local_path = ABSPATH . 'wp-content/uploads/' . $filename;

if (!file_exists($local_path)) {
    echo json_encode(['error' => 'File not found on server disk: ' . $local_path]);
    exit;
}

$tmp = tempnam(get_temp_dir(), 'cover');
if (!copy($local_path, $tmp)) {
    echo json_encode(['error' => 'Failed to copy to temp directory']);
    exit;
}

$file_array = array(
    'name' => 'cover-' . $post_id . '-remade-' . rand(100,999) . '.png',
    'tmp_name' => $tmp
);

$attach_id = media_handle_sideload($file_array, $post_id);
if (is_wp_error($attach_id)) {
    @unlink($tmp);
    echo json_encode(['error' => 'Sideload failed: ' . $attach_id->get_error_message()]);
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

echo json_encode(array(
    'success' => true,
    'post_id' => $post_id,
    'attachment_id' => $attach_id,
    'thumbnail' => get_the_post_thumbnail_url($post_id, 'full')
), JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
?>"""


def pollinations_prompt(story):
    return (
        "Premium square Vietnamese web novel cover illustration, no typography, no letters, "
        "no watermark, no logo, no UI. Clear central character, readable at small thumbnail, "
        "high-end streaming drama poster quality, rich depth, polished digital painting. "
        f"Scene: {story['visual']}."
    )


def download_base(story, force=False):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    base_path = OUT_DIR / f"{story['id']}_base.png"
    source = story.get("source")
    if source:
        source_path = Path(source)
        if not source_path.exists():
            raise FileNotFoundError(f"Local source not found for {story['id']}: {source}")
        with Image.open(source_path) as img:
            img.convert("RGB").resize((1200, 1200), Image.Resampling.LANCZOS).save(base_path)
        print(f"[{story['id']}] Using local source: {source}")
        return base_path

    if base_path.exists() and not force:
        return base_path

    seed = story["id"] + 20260522 + random.randint(1, 999)
    prompt = pollinations_prompt(story)
    params = urllib.parse.urlencode({
        "width": 1200,
        "height": 1200,
        "seed": seed,
        "nologo": "true",
        "private": "true",
        "enhance": "true",
        "model": "flux",
    })
    url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote(prompt)}?{params}"

    for attempt in range(1, 4):
        try:
            print(f"[{story['id']}] Downloading base image, attempt {attempt}...")
            res = requests.get(url, timeout=150)
            if res.status_code == 429:
                time.sleep(30 * attempt)
                continue
            res.raise_for_status()
            base_path.write_bytes(res.content)
            with Image.open(base_path) as img:
                img.convert("RGB").resize((1200, 1200), Image.Resampling.LANCZOS).save(base_path)
            return base_path
        except Exception as exc:
            print(f"[{story['id']}] Download failed: {exc}")
            time.sleep(8 * attempt)

    raise RuntimeError(f"Could not generate base cover for {story['id']}")


def make_cover(story, force=False):
    cover_path = OUT_DIR / f"{story['id']}_cover.png"
    if cover_path.exists() and not force:
        return cover_path
    base_path = download_base(story, force=force)
    ok = apply_standard_overlay(
        input_path=str(base_path),
        output_path=str(cover_path),
        title=story["display_title"],
        subtitle=story["subtitle"],
        bottom_label="ĐỌC TIỂU THUYẾT",
    )
    if not ok:
        raise RuntimeError(f"Overlay failed for {story['id']}")
    return cover_path


def upload_and_set(covers):
    helper_path = OUT_DIR / "update_cover_local.php"
    helper_path.write_text(PHP_HELPER, encoding="utf-8")

    ftp = ftplib.FTP(FTP_HOST, timeout=60)
    ftp.login(FTP_USER, FTP_PASS)
    try:
        with helper_path.open("rb") as handle:
            ftp.storbinary("STOR update_cover_local.php", handle)
        print("Uploaded helper.")

        results = []
        for story, cover_path in covers:
            remote_name = f"remade_cover_{story['id']}_20260522.png"
            with cover_path.open("rb") as handle:
                ftp.storbinary(f"STOR wp-content/uploads/{remote_name}", handle)
            print(f"[{story['id']}] Uploaded image.")

            payload = {"secret": SECRET, "post_id": story["id"], "filename": remote_name}
            res = requests.post(f"{WP_URL}/update_cover_local.php", json=payload, timeout=90)
            try:
                data = res.json()
            except json.JSONDecodeError:
                data = {"error": res.text[:500]}
            print(f"[{story['id']}] {data}")
            results.append({"id": story["id"], "title": story["title"], "cover": str(cover_path), "server": data})
        return results
    finally:
        try:
            ftp.delete("update_cover_local.php")
            print("Deleted helper.")
        except Exception as exc:
            print(f"Helper cleanup warning: {exc}")
        ftp.quit()
        try:
            helper_path.unlink()
        except FileNotFoundError:
            pass


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--generate-only", action="store_true")
    args = parser.parse_args()

    covers = []
    for story in STORIES:
        covers.append((story, make_cover(story, force=args.force)))

    if args.generate_only:
        print("Generated only:")
        for story, cover in covers:
            print(f"{story['id']}: {cover}")
        return

    results = upload_and_set(covers)
    result_path = OUT_DIR / "upload_results.json"
    result_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {result_path}")


if __name__ == "__main__":
    main()
