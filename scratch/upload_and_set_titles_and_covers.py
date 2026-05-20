#!/usr/bin/env python3
import os
import ftplib
import requests
import json

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
SECRET = "ZEN_TRUYEN_2026_BYPASS"

DATA = [
    {
        "id": 2120,
        "title": "Mẹ Vợ Bắt Rửa Bát, Tôi Nấu Tiệc Michelin Chấn Động Phú Quốc",
        "cover": "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/covers_with_title/cover_2120_titled.png"
    },
    {
        "id": 2137,
        "title": "Mẹ Vợ Đòi Sính Lễ 5 Tỷ Khinh Tôi Nghèo, Landmark 81 Là Của Tôi",
        "cover": "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/covers_with_title/cover_2137_titled.png"
    },
    {
        "id": 2145,
        "title": "Sếp Cướp Công Thức Thuốc Đuổi Tôi Khỏi Lab, Tôi Phá Sập IPO Nghìn Tỷ",
        "cover": "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/covers_with_title/cover_2145_titled.png"
    },
    {
        "id": 2156,
        "title": "Tiểu Thư Khinh Tôi Là Bảo Vệ 8 Triệu, Tôi Là Đặc Nhiệm Hạng Nhất",
        "cover": "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/covers_with_title/cover_2156_titled.png"
    },
    {
        "id": 2165,
        "title": "Bạn Thân Cướp Startup Đuổi Tôi Ra Đường, Tôi Bank Run Sập Đế Chế Hắn",
        "cover": "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/covers_with_title/cover_2165_titled.png"
    }
]

def main():
    print("=" * 60)
    print("🚀 SEN-SATIONALIZING TITLES AND COVER IMAGES ON SERVER")
    print("=" * 60)

    # Connect to FTP
    print("Connecting to FTP...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    print("✓ Connected to FTP!")

    # 1. Upload update_titles.php
    local_update_titles = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/update_titles.php"
    if os.path.exists(local_update_titles):
        print("\nUploading update_titles.php to server root...")
        with open(local_update_titles, "rb") as f:
            ftp.storbinary("STOR update_titles.php", f)
        print("✓ Uploaded update_titles.php")

        # 2. Call update_titles.php to update titles in database
        print("\nCalling update_titles.php API...")
        updates = [{"id": item["id"], "title": item["title"]} for item in DATA]
        payload = {
            "secret": SECRET,
            "updates": updates
        }
        try:
            res = requests.post(f"{WP_URL}/update_titles.php", json=payload, timeout=60)
            data = res.json()
            if data.get('success'):
                print("✓ Successfully updated titles in WordPress DB:")
                for result in data.get('results', []):
                    print(f"  - Story {result['id']}: '{result['title']}' (Success: {result.get('success')})")
            else:
                print(f"⚠️ Title update API error: {data}")
        except Exception as e:
            print(f"❌ Title update API error: {e}")

        # Delete update_titles.php from server for security
        try:
            ftp.delete("update_titles.php")
            print("✓ Deleted update_titles.php from server for security.")
        except Exception as e:
            print(f"⚠️ Failed to delete update_titles.php from server: {e}")
    else:
        print("❌ update_titles.php not found locally.")

    # 3. Create update_cover_hq.php dynamically and upload it
    print("\nCreating update_cover_hq.php dynamically...")
    php_cover_helper = """<?php
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
$image_url = esc_url_raw($input['image_url']);

// Delete old thumbnail if exists
$old_thumb = get_post_thumbnail_id($post_id);
if ($old_thumb) {
    wp_delete_attachment($old_thumb, true);
}

$tmp = download_url($image_url, 60);
if (is_wp_error($tmp)) {
    echo json_encode(['error' => 'Download failed: ' . $tmp->get_error_message()]);
    exit;
}

$file_array = array(
    'name' => 'cover-' . $post_id . '-hq-' . rand(100,999) . '.png',
    'tmp_name' => $tmp
);

$attach_id = media_handle_sideload($file_array, $post_id);
if (is_wp_error($attach_id)) {
    @unlink($tmp);
    echo json_encode(['error' => 'Sideload failed: ' . $attach_id->get_error_message()]);
    exit;
}

set_post_thumbnail($post_id, $attach_id);

if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

echo json_encode([
    'success' => true,
    'post_id' => $post_id,
    'attachment_id' => $attach_id,
    'message' => 'Cover updated successfully!'
], JSON_UNESCAPED_UNICODE);
?>"""

    with open("update_cover_hq.php", "w") as f:
        f.write(php_cover_helper)

    print("Uploading update_cover_hq.php to FTP root...")
    with open("update_cover_hq.php", "rb") as f:
        ftp.storbinary("STOR update_cover_hq.php", f)
    print("✓ Uploaded update_cover_hq.php")

    # 4. Upload each titled cover and set it as featured image
    for item in DATA:
        story_id = item["id"]
        local_cover = item["cover"]

        if not os.path.exists(local_cover):
            print(f"❌ Cover not found for story {story_id}: {local_cover}")
            continue

        filename = f"cover_hq_{story_id}_sensational.png"
        remote_path = f"wp-content/uploads/{filename}"

        print(f"\nUploading sensational cover for story {story_id} ({item['title']})...")
        with open(local_cover, "rb") as f:
            ftp.storbinary(f"STOR {remote_path}", f)
        print(f"✓ Uploaded {filename} to server uploads")

        # Call PHP helper to sideload image as post thumbnail
        image_url = f"{WP_URL}/wp-content/uploads/{filename}"
        payload = {
            "secret": SECRET,
            "post_id": story_id,
            "image_url": image_url
        }
        try:
            res = requests.post(f"{WP_URL}/update_cover_hq.php", json=payload, timeout=60)
            data = res.json()
            if data.get('success'):
                print(f"✓ Story {story_id}: Cover updated successfully! (Attachment ID: {data['attachment_id']})")
            else:
                print(f"⚠️ Story {story_id}: Cover update warning: {data}")
        except Exception as e:
            print(f"❌ Story {story_id}: Cover update API error: {e}")

    # 5. Clean up helper script from remote server
    try:
        ftp.delete("update_cover_hq.php")
        print("\n✓ Deleted update_cover_hq.php from server for security.")
    except Exception as e:
        print(f"⚠️ Failed to delete update_cover_hq.php from server: {e}")

    ftp.quit()
    if os.path.exists("update_cover_hq.php"):
        os.remove("update_cover_hq.php")
    print("✓ Done! Titles and sensational covers are updated and deployed.")

if __name__ == "__main__":
    main()
