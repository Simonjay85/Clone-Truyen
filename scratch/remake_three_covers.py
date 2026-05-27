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

# Configuration for the three novels
NOVELS_CFG = {
    3920: {
        "title": "Nghệ Nhân Sơn Mài Bị Khinh Rẻ Đuổi Khỏi Xưởng Tìm Ra Màu Sơn Thất Truyền Đè Bẹp Tập Đoàn Tranh Giả",
        "subtitle": "Bản hùng ca sảng văn của Trịnh Hoàng Yến & Trần Hoài Nam",
        "base_url": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-3920-215.jpg",
        "output_filename": "cover_card_3920.png"
    },
    3930: {
        "title": "Nghệ Nhân Cacao Bị Vị Hôn Thê Đuổi Đi, Socola Trăm Tỷ Vả Sập Tập Đoàn Hóa Chất Ngày Hội Chợ",
        "subtitle": "Bản hùng ca sảng văn của Nguyễn Minh Thư & Trịnh Gia Bách",
        "base_url": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-3930-486.jpg",
        "output_filename": "cover_card_3930.png"
    },
    3940: {
        "title": "Bác Sĩ Đông Y Bị Đuổi Khỏi Viện Phổi, Mũi Kim Thần Đông Tây Kết Hợp Vả Sập Tập Đoàn Phản Bội",
        "subtitle": "Bản hùng ca sảng văn của Trịnh Khánh Vy & Nguyễn Lâm Phong",
        "base_url": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-3940-620.jpg",
        "output_filename": "cover_card_3940.png"
    }
}

def download_file(url, local_path):
    print(f"📥 Downloading: {url} -> {local_path}...")
    res = requests.get(url, timeout=30)
    res.raise_for_status()
    with open(local_path, "wb") as f:
        f.write(res.content)
    print("✓ Download complete.")

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
    print("=" * 70)
    print("🚀 STARTING AUTOMATED REMAKE OF 3 STORY COVERS (SON MAI, CACAO, BAC SI)")
    print("=" * 70)

    # 1. Process each cover image locally
    for post_id, cfg in NOVELS_CFG.items():
        print("\n" + "-" * 50)
        print(f"📦 Processing Post ID {post_id}: {cfg['title'][:40]}...")
        
        local_base = f"scratch/base_{post_id}.jpg"
        local_overlaid = f"scratch/overlaid_{post_id}.png"
        
        # Download base cover
        try:
            download_file(cfg["base_url"], local_base)
        except Exception as e:
            print(f"❌ Failed to download base cover for post {post_id}: {e}")
            continue
            
        # Run cover overlay standard engine
        print("🎨 Generating overlay using standard layout...")
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

    # 2. Write temp_update_cover.php helper content
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

    # 3. Upload helper script via FTP
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

    # 4. Trigger cover update on WordPress for each novel
    for post_id, cfg in NOVELS_CFG.items():
        print("\n" + "=" * 50)
        print(f"🔗 Triggering WordPress cover update for Post ID {post_id}...")
        try:
            url = f"{WP_URL}/{php_filename}?token=zen_cover_update_2026&post_id={post_id}&filename={cfg['output_filename']}"
            res = requests.get(url, timeout=60)
            print(f"Response Status: {res.status_code}")
            try:
                print("Response JSON:", res.json())
            except:
                print("Raw Response:", res.text)
        except Exception as e:
            print(f"❌ Failed to trigger WordPress update for post {post_id}: {e}")

    # 5. Remote and Local Cleanups
    print("\n" + "=" * 50)
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

    # Clean up local base/overlaid files
    print("🧹 Cleaning up local temporary cover files...")
    for post_id in NOVELS_CFG.keys():
        local_base = f"scratch/base_{post_id}.jpg"
        local_overlaid = f"scratch/overlaid_{post_id}.png"
        if os.path.exists(local_base):
            os.remove(local_base)
        if os.path.exists(local_overlaid):
            os.remove(local_overlaid)
    print("✓ Local cleanup complete.")

    print("\n" + "=" * 70)
    print("🎉 COVERS AUTOMATED REMAKE PROCESS FINISHED SUCCESSFULLY!")
    print("=" * 70)

if __name__ == "__main__":
    main()
