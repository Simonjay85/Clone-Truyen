#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
remake_thirty_covers.py — Remake all 30 covers using highly realistic photo prompts and 2-line shortened titles.
"""

import sys
import os
import requests
import ftplib
import time
import json

sys.path.append("/Users/aaronnguyen/TN/App/doctieuthuyet")
from cover_overlay_standard import apply_standard_overlay

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

# The 30 novel IDs and their photorealistic prompts
ID_TO_PROMPT = {
    5498: "A highly realistic, cinematic 8k real photo of a young, handsome, stylish 29-year-old Vietnamese digital artist in his cozy penthouse studio in Saigon at night, drawing on a modern glowing tablet with a stylus. The Saigon city skyline with neon lights is visible through a large glass window in the background. Warm desk lamp lighting, moody cinematic atmosphere, extremely detailed, professional photography, shot on 35mm lens, no text, realistic human face.",
    5510: "A highly realistic, cinematic 8k real photo of an elegant, intelligent 28-year-old Vietnamese female architect standing in front of a giant modern architectural model of a futuristic museum in her bright sunlit design studio. She is holding blueprints, smiling confidently. Beautiful volumetric lighting, blueprints on table, architectural drawings, shot on 50mm lens, extremely detailed, real photo, photorealistic.",
    5522: "A highly realistic, cinematic 8k real photo of a sharp-looking 29-year-old Vietnamese male software engineer sitting in a dimly lit high-tech room, coding on multiple large computer screens displaying clean code. Neon ambient glowing lights, cozy developer setup, shot on 35mm lens, highly detailed, real photo, photorealistic.",
    5534: "A highly realistic, cinematic 8k real photo of a beautiful, sophisticated 27-year-old Vietnamese female dermatologist in a clean modern laboratory, holding a premium glass serum bottle containing clear liquid. Green botanical elements and a elegant white lotus flower in the background. Soft studio lighting, highly detailed, real photo, photorealistic.",
    5546: "A highly realistic, cinematic 8k real photo of a thoughtful, handsome 26-year-old Vietnamese male writer sitting at a wooden desk in his cozy vintage library at sunset. He is typing on a classic keyboard, surrounded by rows of beautiful books, warm soft lighting through window, highly detailed, real photo, photorealistic.",
    5558: "A highly realistic, cinematic 8k real photo of a charismatic, intelligent 32-year-old Vietnamese male university economics professor standing in front of a modern whiteboard with charts, lecturing confidently. Bright modern classroom background, natural soft lighting, highly detailed, real photo, photorealistic.",
    5569: "A highly realistic, cinematic 8k real photo of an experienced, focused 35-year-old Vietnamese male watchmaker in his cozy traditional workshop, wearing magnifying loupe glasses and carefully assembling a luxurious mechanical wristwatch movement with tiny tools under a warm desk lamp. Highly detailed gears, real photo.",
    5582: "A highly realistic, cinematic 8k real photo of a determined, professional 28-year-old Vietnamese female journalist holding a professional camera and a notepad, standing on a bustling city street under rain at night. Street lights reflecting, moody journalistic atmosphere, shot on 50mm, real photo.",
    5592: "A highly realistic, cinematic 8k real photo of a brave, strong 38-year-old Vietnamese ship captain standing on the bridge of a large cargo vessel, looking out at the deep blue ocean. Advanced navigation screens glowing, determined expression, real photo.",
    5604: "A highly realistic, cinematic 8k real photo of a young, artistic 27-year-old Vietnamese male ceramic artisan in his sun-drenched pottery workshop, shaping a beautiful ceramic vase on a spinning pottery wheel. Clay on hands, shelves of beautiful pottery in the background, warm natural lighting, real photo.",
    5618: "A highly realistic, cinematic 8k real photo of a highly elegant, powerful 30-year-old Vietnamese female CEO in a premium business suit standing in her high-rise modern office overlooking the city skyline, looking out confidently. Luxurious corporate background, real photo.",
    5630: "A highly realistic, cinematic 8k real photo of a kind, professional 33-year-old Vietnamese male child psychologist sitting in a cozy, warm, and colorful playroom, talking gently and smiling at a happy child playing with wooden blocks. Bright natural lighting, real photo.",
    5641: "A highly realistic, cinematic 8k real photo of a talented young Vietnamese male pianist playing a grand piano on a beautifully lit concert stage. Warm spotlights, elegant posture, dramatic atmosphere, highly detailed, real photo.",
    5654: "A highly realistic, cinematic 8k real photo of a beautiful, strong-willed Vietnamese female fashion model with a light artistic facial scar, posing confidently in a premium fashion studio under professional studio lighting. High fashion editorial shot, real photo.",
    5664: "A highly realistic, cinematic 8k real photo of a successful 32-year-old Vietnamese male real estate developer standing in front of a modern, beautifully designed community housing project at sunset, smiling warmly. Volumetric sunset lighting, real photo.",
    5676: "A highly realistic, cinematic 8k real photo of a cozy, beautiful hidden coffee shop in a narrow alley in Saigon. Small wooden tables, warm glowing hanging lights, green plants, peaceful and moody coffee shop atmosphere, shot on 35mm, real photo.",
    5687: "A highly realistic, cinematic 8k real photo of a dedicated young Vietnamese teacher walking on a misty mountain trail in northwestern Vietnam, carrying a wooden box full of books on his back. Beautiful green rice terraces in the background, soft morning mist, real photo.",
    5699: "A highly realistic, cinematic 8k real photo of a warm, cozy traditional Vietnamese bakery kitchen. An elegant young woman and an old grandmother smiling and preparing delicious fresh caramel flan on a wooden table. Warm soft lighting, real photo.",
    5709: "A highly realistic, cinematic 8k real photo of a kind, professional 35-year-old Vietnamese male doctor wearing a white coat and stethoscope, smiling warmly at a patient in a simple countryside clinic. Warm natural lighting, real photo.",
    5722: "A highly realistic, cinematic 8k real photo of a beautiful, gentle Vietnamese female florist arranging a gorgeous bouquet of fresh colorful flowers in a sunlit wooden flower shop in Da Lat. Volumetric dust motes in light beams, real photo.",
    5734: "A highly realistic, cinematic 8k real photo of a powerful, elegant 29-year-old Vietnamese female hotel executive standing in the grand, luxurious lobby of a five-star hotel. Marble floors, glowing chandeliers, looking extremely confident, real photo.",
    5746: "A highly realistic, cinematic 8k real photo of an intelligent, professional 28-year-old Vietnamese female corporate secretary holding a tablet, standing in a modern glass office boardroom, smiling confidently. Sleek business setup, real photo.",
    5757: "A highly realistic, cinematic 8k real photo of a strong-willed, smart 32-year-old Vietnamese female logistics corporate leader in a business suit standing in a modern automated cargo shipping terminal. High-tech container port background at sunset, real photo.",
    5770: "A highly realistic, cinematic 8k real photo of a brilliant 26-year-old Vietnamese female financial analyst sitting in a modern high-rise office at night, looking at multiple screens displaying glowing green and red stock market charts. Professional atmosphere, real photo.",
    5780: "A highly realistic, cinematic 8k real photo of a determined, professional 40-year-old Vietnamese male doctor standing in the modern clean hallway of a state-of-the-art private hospital. Bright clean lighting, confident posture, real photo.",
    5792: "A highly realistic, cinematic 8k real photo of a stylish 27-year-old Vietnamese male barber cutting hair in a rustic vỉa hè open-air street-side barber shop in Saigon. Retro mirror, plastic chairs, vibrant street background with soft bokeh, real photo.",
    5803: "A highly realistic, cinematic 8k real photo of a professional, dignified 30-year-old Vietnamese female lawyer wearing a modern black blazer, standing in front of a bookshelf in her law office, holding a folder. Confident and warm expression, real photo.",
    5815: "A highly realistic, cinematic 8k real photo of a small traditional Vietnamese street-side sweet dessert cart (xe chè) glowing under warm light bulbs at night in Saigon. An old kind vendor smiling, steaming pots, moody cozy night street atmosphere, real photo.",
    5825: "A highly realistic, cinematic 8k real photo of an energetic, creative 29-year-old Vietnamese female marketing agency director presenting ideas in a modern loft agency office. Colorful creative mood board and glass window background, real photo.",
    5838: "A highly realistic, cinematic 8k real photo of a proud, strong 30-year-old Vietnamese male self-taught builder in a hard hat, standing in front of a modern, exceptionally beautiful architectural residence under construction. Golden hour sun rays, real photo.",
}

ID_TO_SHORT_TITLE = {
    5498: "BỊ CƯỚP BST NFT\nVẼ LẠI TỪ SỐ 0",
    5510: "BỊ ĐẠO THIẾT KẾ\nXÂY SIÊU CÔNG TRÌNH",
    5522: "BỊ COPY CODE APP\nVIẾT LẠI TỪ ĐẦU",
    5534: "BỊ CƯỚP CÔNG THỨC\nLẬP HÃNG MỸ PHẨM SẠCH",
    5546: "BỊ ĐẠO TIỂU THUYẾT\nVIẾT PHẦN TIẾP THEO",
    5558: "BỊ ÉP NGHỈ DẠY\nMỞ HỌC VIỆN ONLINE",
    5569: "THỢ ĐỒNG HỒ VỈA HÈ\nCHẾ TẠO KIỆT TÁC",
    5582: "BỊ SA THẢI PHÓNG VIÊN\nLẬP TÒA SOẠN ĐỘC LẬP",
    5592: "BỊ VU OAN CHÌM TÀU\nTỰ TRỤC VỚT BẰNG CHỨNG",
    5604: "BỊ ĐUỔI KHỎI LÀNG\nTẠO DÒNG GỐM MỚI",
    5618: "TRẺ MỒ CÔI CỔNG CHÙA\nCEO THỜI TRANG ĐÔNG NAM Á",
    5630: "NỖI ĐAU MỒ CÔI\nCHỮA LÀNH HÀNG NGHÌN EM NHỎ",
    5641: "MẤT 3 NGÓN TAY\nĐẠT THẦN ĐỒNG PIANO",
    5654: "BỊ TẠT AXIT VÌ TỪ CHỐI\nNGƯỜI MẪU ĐỘC BẢN",
    5664: "BỐ MẸ PHÁ SẢN\nVƯƠN LÊN ÔNG TRÙM MIỀN TÂY",
    5676: "QUÁN CÀ PHÊ NHỎ\nHẺM SÂU SÀI GÒN",
    5687: "MANG SÁCH LÊN NÚI\nHÀNH TRÌNH THẦY GIÁO TRẺ",
    5699: "TIỆM BÁNH BÀ NGOẠI\nCHỮA LÀNH TUỔI THƠ",
    5709: "BS GIỎI VỀ QUÊ\nPHÒNG KHÁM MIỄN PHÍ",
    5722: "CÔ GÁI CÂM\nMỞ TIỆM HOA ĐÀ LẠT",
    5734: "CON DÂU PHÒNG TRÀ\nNẮM ĐẾ CHẾ KHÁCH SẠN",
    5746: "BỊ VU OAN 10 TỶ\nTHƯ KÝ LẬT KÈO",
    5757: "TRANH GIÀNH THỪA KẾ\nCON GÁI ÚT THÂU TÓM",
    5770: "CHA NUÔI PHẢN BỘI\nĐẠI CHIẾN SÀN CHỨNG KHOÁN",
    5780: "TỪ CHỐI NHẬN PHONG BÌ\nBÁC SĨ LẬP VIỆN RIÊNG",
    5792: "BỊ ĐUỔI VÌ CẮT RẺ\nTIỆM TÓC VỈA HÈ ĐÔNG NGHỊT",
    5803: "BỊ BÁN QUA BIÊN GIỚI\nTRỞ THÀNH LUẬT SƯ",
    5815: "XE CHÈ ĐÊM\nẤM LÒNG SÀI GÒN",
    5825: "BỊ ĐẠO CHIẾN DỊCH\nLẬP AGENCY ĐÈ SẾP CŨ",
    5838: "BỊ KHINH LÀ THỢ XÂY\nXÂY SIÊU DINH THỰ",
}

def upload_ftp_file(local_path, remote_dir, remote_filename):
    print(f"📤 Uploading: {local_path} -> FTP://{remote_dir}/{remote_filename}...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd(remote_dir)
    with open(local_path, "rb") as f:
        ftp.storbinary(f"STOR {remote_filename}", f)
    ftp.quit()
    print("✓ Upload complete.")

def main():
    print("=" * 80)
    print("🚀 STARTING AUTOMATED REMAKE OF ALL 30 STORY COVERS WITH PHOTOREALISTIC IMAGES")
    print("=" * 80)

    # Helper script content
    php_content = """<?php
/**
 * Temporary Cover Update Script
 * Security: Uses secret token zen_cover_update_2026
 */
ini_set('display_errors', 1);
error_reporting(E_ALL);
header('Content-Type: application/json');

if (!isset($_GET['token']) || $_GET['token'] !== 'zen_cover_update_2026') {
    http_response_code(403);
    echo json_encode(['error' => 'Unauthorized']);
    exit;
}

require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

$post_id = isset($_GET['post_id']) ? intval($_GET['post_id']) : 0;
$filename = isset($_GET['filename']) ? sanitize_file_name($_GET['filename']) : '';

if (!$post_id || empty($filename)) {
    echo json_encode(['error' => 'Missing parameter post_id or filename']);
    exit;
}

$filepath = ABSPATH . 'wp-content/uploads/' . $filename;
if (!file_exists($filepath)) {
    echo json_encode(['error' => 'File not found: ' . $filepath]);
    exit;
}

$file_array = [
    'name' => 'cover-' . $post_id . '-' . rand(100, 999) . '.png',
    'tmp_name' => $filepath
];

// Copy to a temp file because media_handle_sideload moves/deletes it
$tmp_copy = ABSPATH . 'wp-content/uploads/tmp_' . $filename;
if (!copy($filepath, $tmp_copy)) {
    echo json_encode(['error' => 'Failed to copy file to temp path']);
    exit;
}
$file_array['tmp_name'] = $tmp_copy;

// Set admin context
$admins = get_users(['role' => 'administrator', 'number' => 1]);
if (!empty($admins)) {
    wp_set_current_user($admins[0]->ID);
}

$attach_id = media_handle_sideload($file_array, $post_id);

if (!is_wp_error($attach_id)) {
    // Delete old thumbnail if exists
    $old_thumb_id = get_post_thumbnail_id($post_id);
    if ($old_thumb_id) {
        wp_delete_attachment($old_thumb_id, true);
    }
    
    set_post_thumbnail($post_id, $attach_id);
    
    if (function_exists('litespeed_purge_all')) {
        litespeed_purge_all();
    }
    
    @unlink($filepath);
    
    echo json_encode([
        'success' => true,
        'post_id' => $post_id,
        'attach_id' => $attach_id,
        'message' => 'Cover updated successfully!'
    ]);
} else {
    if (file_exists($tmp_copy)) @unlink($tmp_copy);
    echo json_encode([
        'success' => false,
        'error' => $attach_id->get_error_message()
    ]);
}
?>"""

    php_filename = "temp_update_cover.php"
    with open(php_filename, "w", encoding="utf-8") as f:
        f.write(php_content)

    # Upload helper script via FTP
    print("\n📤 Uploading WordPress cover updater helper script...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        with open(php_filename, "rb") as f:
            ftp.storbinary(f"STOR {php_filename}", f)
        ftp.quit()
        print("✓ Upload helper complete.")
    except Exception as e:
        print("❌ Failed to upload helper script via FTP:", e)
        if os.path.exists(php_filename):
            os.remove(php_filename)
        return

    # Process all 30 covers
    for post_id, prompt in ID_TO_PROMPT.items():
        title = ID_TO_SHORT_TITLE.get(post_id)
        if not title:
            print(f"⚠️ Post ID {post_id} not found in title dictionary! Skipping.")
            continue

        print("\n" + "-" * 70)
        print(f"📦 Processing Cover for Post ID {post_id}: {title.replace(chr(10), ' ')}...")

        local_base = f"scratch/temp_base_{post_id}.png"
        local_overlaid = f"scratch/overlaid_{post_id}.png"
        remote_filename = f"cover_card_{post_id}.png"

        # 1. Verify pre-saved Gemini-generated base cover exists locally
        if not os.path.exists(local_base):
            print(f"❌ Error: Gemini-generated base image not found for post {post_id} at '{local_base}'! Skipping.")
            continue
        print(f"✓ Found base image at: {local_base}")

        # 2. Run the overlay standard layout (No subtitle)
        ok = apply_standard_overlay(
            input_path=local_base,
            output_path=local_overlaid,
            title=title,
            subtitle="", # Empty string completely skips subtitle!
            position="top"
        )
        
        if not ok:
            print(f"❌ Failed to apply standard title overlay for post {post_id}!")
            if os.path.exists(local_base):
                os.remove(local_base)
            continue

        # 3. Upload overlaid PNG to FTP
        try:
            upload_ftp_file(local_overlaid, "wp-content/uploads", remote_filename)
        except Exception as e:
            print(f"❌ FTP Upload Error for overlaid cover {post_id}: {e}")
            if os.path.exists(local_base):
                os.remove(local_base)
            if os.path.exists(local_overlaid):
                os.remove(local_overlaid)
            continue

        # 4. Trigger update on WordPress
        try:
            url = f"{WP_URL}/{php_filename}?token=zen_cover_update_2026&post_id={post_id}&filename={remote_filename}"
            res = requests.get(url, timeout=60)
            print(f"Response Status: {res.status_code}")
            try:
                print("Response JSON:", res.json())
            except:
                print("Raw Response:", res.text)
        except Exception as e:
            print(f"❌ Failed to trigger WordPress update for post {post_id}: {e}")

        # Clean up temporary local files
        if os.path.exists(local_base):
            os.remove(local_base)
        if os.path.exists(local_overlaid):
            os.remove(local_overlaid)

    # Remote and Local Cleanups of the helper PHP
    print("\n" + "=" * 80)
    print("🧹 Cleaning up remote helper script...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete(php_filename)
        ftp.quit()
        print("✓ Remote helper script deleted.")
    except Exception as e:
        print("❌ Remote cleanup failed:", e)

    if os.path.exists(php_filename):
        os.remove(php_filename)
        print("✓ Local helper script deleted.")

    print("\n" + "=" * 80)
    print("🎉 ALL 30 STORIES GENERATED WITH REALISTIC PHOTOS & INSTANTLY SYNCED TO THE LIVE SITE!")
    print("=" * 80)

if __name__ == "__main__":
    main()
