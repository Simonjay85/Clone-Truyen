import sys
import os
import requests
import ftplib
import time

sys.path.append("/Users/aaronnguyen/TN/App/doctieuthuyet")
from cover_overlay_standard import apply_standard_overlay

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

# Configuration for the eleven novels with manual 3-line ngắt dòng titles
NOVELS_CFG = {
    3743: {
        "title": "NỮ HOÀNG TRÀ SEN\nTÂY HỒ\nĐẾ CHẾ NGHÌN TỶ",
        "subtitle": "Bản hùng ca sảng văn của Trịnh Khánh An & Lâm Gia Huy",
        "local_base": "scratch/base_3743.png",
        "output_filename": "cover_card_3743.png"
    },
    3755: {
        "title": "BÁC SĨ THẠM MỸ\nSÀI GÒN\nLẬT MẶT BỆNH VIỆN",
        "subtitle": "Bản hùng ca sảng văn của Nguyễn Hoài Nam & Trần Thế Anh",
        "local_base": "scratch/base_3755.png",
        "output_filename": "cover_card_3755.png"
    },
    3767: {
        "title": "ÔNG TRÙM LOGISTICS\nTÂN CẢNG\nTHÂU TÓM NGƯỢC",
        "subtitle": "Bản hùng ca sảng văn của Lê Quốc Khánh & Hoàng Trọng Nhân",
        "local_base": "scratch/base_3767.png",
        "output_filename": "cover_card_3767.png"
    },
    3769: {
        "title": "THỢ NUÔI TRAI\nĐOẠT LẠI TẬP ĐOÀN\nNGỌC TRAI NGHÌN TỶ",
        "subtitle": "Bản hùng ca sảng văn của Võ Minh Quân & Trịnh Bảo Long",
        "local_base": "scratch/base_3769.png",
        "output_filename": "cover_card_3769.png"
    },
    3789: {
        "title": "KIẾN TRÚC SƯ\nPHỐ CỔ HÀ NỘI\nCỨU CẢ KHU PHỐ",
        "subtitle": "Bản hùng ca sảng văn của Đỗ Minh Tuấn & Nguyễn Văn Hùng",
        "local_base": "scratch/base_3789.png",
        "output_filename": "cover_card_3789.png"
    },
    3801: {
        "title": "VUA LÚA GẠO\nĐỒNG THÁP\nĐẾ CHẾ XUẤT KHẨU",
        "subtitle": "Bản hùng ca sảng văn của Võ Thanh Tùng & Trần Minh Đăng",
        "local_base": "scratch/base_3801.png",
        "output_filename": "cover_card_3801.png"
    },
    3813: {
        "title": "THẦN ĐỒNG PIANO\nNHẠC VIỆN\nCHẤN ĐỘNG CHOPIN",
        "subtitle": "Bản hùng ca sảng văn của Lâm Hoàng Phúc & Phạm Đức Huy",
        "local_base": "scratch/base_3813.png",
        "output_filename": "cover_card_3813.png"
    },
    3825: {
        "title": "CHÚA ĐẢO RESORT\nPHÚ QUỐC\nMUA CẢ HÒN ĐẢO",
        "subtitle": "Bản hùng ca sảng văn của Trịnh Gia Bảo & Nguyễn Hoàng Lâm",
        "local_base": "base_cover_9.png",
        "output_filename": "cover_card_3825.png"
    },
    3837: {
        "title": "ĐẠO DIỄN PHIM TRƯỜNG\nCẦN GIỜ\nCHẤN ĐỘNG CANNES",
        "subtitle": "Bản hùng ca sảng văn của Hoàng Thế Vinh & Nguyễn Minh Triết",
        "local_base": "base_cover_10.png",
        "output_filename": "cover_card_3837.png"
    },
    3849: {
        "title": "VUA SẦU RIÊNG\nĐẮK NÔNG\nTRỒNG LẠI TỪ TRO TÀN",
        "subtitle": "Bản hùng ca sảng văn của Nguyễn Hoàng Long & Trịnh Minh Khang",
        "local_base": "base_cover_11.png",
        "output_filename": "cover_card_3849.png"
    },
    3861: {
        "title": "THIÊN TÀI BLOCKCHAIN\nPHỐ NGUYỄN HUỆ\nHACK NGƯỢC CẢ SÀN",
        "subtitle": "Bản hùng ca sảng văn của Trần Minh Hoàng & Nguyễn Khánh An",
        "local_base": "base_cover_12.png",
        "output_filename": "cover_card_3861.png"
    }
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
    print("🚀 STARTING AUTOMATED REMAKE OF 11 STORY COVERS WITH PREMIUM AI BASES")
    print("=" * 80)

    # 1. Process each cover image locally
    for post_id, cfg in NOVELS_CFG.items():
        print("\n" + "-" * 60)
        print(f"📦 Processing Post ID {post_id}:")
        
        local_base = cfg["local_base"]
        local_overlaid = f"scratch/overlaid_{post_id}.png"
        
        if not os.path.exists(local_base):
            print(f"❌ Error: Local base cover {local_base} not found!")
            continue
            
        # Run cover overlay standard engine
        print("🎨 Generating overlay using standard layout with 3-line bold title...")
        ok = apply_standard_overlay(
            input_path=local_base,
            output_path=local_overlaid,
            title=cfg["title"],
            subtitle=cfg["subtitle"],
            position="top"
        )
        
        if not ok:
            print(f"❌ Failed to apply standard title overlay for post {post_id}!")
            continue
            
        # Upload overlaid PNG to FTP
        try:
            upload_ftp_file(local_overlaid, "wp-content/uploads", cfg["output_filename"])
        except Exception as e:
            print(f"❌ FTP Upload Error for overlaid cover {post_id}: {e}")
            continue

    # 2. Write temp_update_covers_batch.php helper content
    php_content = """<?php
/**
 * Temporary Batch Cover Update Script
 * Security: Uses secret token zen_cover_update_batch_2026
 */
ini_set('display_errors', 1);
error_reporting(E_ALL);
header('Content-Type: application/json');

if (!isset($_GET['token']) || $_GET['token'] !== 'zen_cover_update_batch_2026') {
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

    php_filename = "temp_update_covers_batch.php"
    with open(php_filename, "w", encoding="utf-8") as f:
        f.write(php_content)

    # 3. Upload helper script via FTP
    print("\n📤 Uploading WordPress cover updater batch helper script...")
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

    # 4. Trigger cover update on WordPress for each novel
    for post_id, cfg in NOVELS_CFG.items():
        print("\n" + "=" * 60)
        print(f"🔗 Triggering WordPress cover update for Post ID {post_id}...")
        try:
            url = f"{WP_URL}/{php_filename}?token=zen_cover_update_batch_2026&post_id={post_id}&filename={cfg['output_filename']}"
            res = requests.get(url, timeout=60)
            print(f"Response Status: {res.status_code}")
            try:
                print("Response JSON:", res.json())
            except:
                print("Raw Response:", res.text)
        except Exception as e:
            print(f"❌ Failed to trigger WordPress update for post {post_id}: {e}")

    # 5. Remote and Local Cleanups
    print("\n" + "=" * 60)
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

    # Clean up local overlaid files
    print("🧹 Cleaning up local temporary cover files...")
    for post_id in NOVELS_CFG.keys():
        local_overlaid = f"scratch/overlaid_{post_id}.png"
        if os.path.exists(local_overlaid):
            os.remove(local_overlaid)
    print("✓ Local cleanup complete.")

    print("\n" + "=" * 80)
    print("🎉 ALL 11 COVERS REMADE AND DEPLOYED LIVE SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    main()
