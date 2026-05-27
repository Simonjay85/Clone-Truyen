import os
import ftplib
import requests

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

def main():
    local_cover = "/Users/aaronnguyen/TN/App/doctieuthuyet/than_y_overlaid.png"
    remote_filename = "cover_update_than_y.png"
    post_id = 3873
    
    if not os.path.exists(local_cover):
        print(f"❌ Local cover not found: {local_cover}")
        return
        
    print("=" * 60)
    print("🚀 AUTOMATED COVER UPDATER")
    print("=" * 60)
    
    # 1. Upload Cover Image to FTP
    print(f"📤 Uploading final cover image to FTP /wp-content/uploads/{remote_filename}...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.cwd("wp-content/uploads")
        with open(local_cover, "rb") as f:
            ftp.storbinary(f"STOR {remote_filename}", f)
        print("✓ Uploaded cover image via FTP.")
        ftp.quit()
    except Exception as e:
        print("❌ FTP Upload Error for cover image:", e)
        return
        
    # 2. Write temp_update_cover.php content and upload
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

$post_id = isset($_GET['post_id']) ? intval($_GET['post_id']) : 3873;
$filename = isset($_GET['filename']) ? sanitize_file_name($_GET['filename']) : '';

if (empty($filename)) {
    echo json_encode(['error' => 'Missing filename']);
    exit;
}

$filepath = ABSPATH . 'wp-content/uploads/' . $filename;
if (!file_exists($filepath)) {
    echo json_encode(['error' => 'File not found: ' . $filepath]);
    exit;
}

$file_array = [
    'name' => 'cover-' . $post_id . '-new-' . rand(100, 999) . '.png',
    'tmp_name' => $filepath
];

// Copy to a temp file because media_handle_sideload moves/deletes it
$tmp_copy = ABSPATH . 'wp-content/uploads/tmp_' . $filename;
if (!copy($filepath, $tmp_copy)) {
    echo json_encode(['error' => 'Failed to copy file to temp path']);
    exit;
}
$file_array['tmp_name'] = $tmp_copy;

// Tự động lấy admin đầu tiên
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
    
    // Purge LSCache if exists
    if (function_exists('litespeed_purge_all')) {
        litespeed_purge_all();
    }
    
    // Clean up original uploaded file
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
    
    php_local_file = "temp_update_cover.php"
    with open(php_local_file, "w", encoding="utf-8") as f:
        f.write(php_content)
        
    print("\n📤 Uploading temp_update_cover.php helper script via FTP...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        with open(php_local_file, "rb") as f:
            ftp.storbinary("STOR temp_update_cover.php", f)
        print("✓ Uploaded helper script.")
        ftp.quit()
    except Exception as e:
        print("❌ FTP Upload Error for helper script:", e)
        if os.path.exists(php_local_file):
            os.remove(php_local_file)
        return

    # 3. Trigger endpoint
    print(f"\n🔗 Triggering cover update via endpoint: {WP_URL}/temp_update_cover.php...")
    try:
        url = f"{WP_URL}/temp_update_cover.php?token=zen_cover_update_2026&post_id={post_id}&filename={remote_filename}"
        res = requests.get(url, timeout=60)
        print("Response Code:", res.status_code)
        try:
            print("Response Data:", res.json())
        except:
            print("Raw Response:", res.text)
    except Exception as e:
        print("❌ HTTP Request Error:", e)

    # 4. Clean up remote and local temp files
    print("\n🧹 Cleaning up remote helper script...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("temp_update_cover.php")
        print("✓ Deleted temp_update_cover.php from remote server.")
        ftp.quit()
    except Exception as e:
        print("❌ Remote cleanup error:", e)

    if os.path.exists(php_local_file):
        os.remove(php_local_file)
        print("✓ Deleted local temp_update_cover.php.")
        
    print("=" * 60)
    print("🎉 COVER UPDATING PROCESS FINISHED")
    print("=" * 60)

if __name__ == "__main__":
    main()
