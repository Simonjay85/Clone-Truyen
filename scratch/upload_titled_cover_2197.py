import ftplib
import requests
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

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
    'name' => 'cover-' . $post_id . '-hq-titled.png',
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

echo json_encode([
    'success' => true,
    'post_id' => $post_id,
    'attachment_id' => $attach_id
]);
?>"""

def main():
    story_id = 2197
    local_titled_path = "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f/cover_2197_titled_v3.png"
    
    print("Uploading PHP helper and titled cover image via FTP...")
    
    # Write temporary helper file
    with open("temp_upload_helper.php", "w") as f:
        f.write(PHP_HELPER)
        
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    
    # Upload helper
    with open("temp_upload_helper.php", "rb") as f:
        ftp.storbinary("STOR temp_upload_helper.php", f)
    print("✓ Helper uploaded")
    
    # Upload image
    remote_filename = "cover_temp_2197_titled.png"
    with open(local_titled_path, "rb") as f:
        ftp.storbinary(f"STOR wp-content/uploads/{remote_filename}", f)
    print("✓ Image uploaded to wp-content/uploads/")
    
    ftp.quit()
    os.remove("temp_upload_helper.php")
    
    # Trigger
    print("Triggering sideload helper...")
    payload = {
        "secret": "ZEN_TRUYEN_2026_BYPASS",
        "post_id": story_id,
        "filename": remote_filename
    }
    res = requests.post(f"{WP_URL}/temp_upload_helper.php", json=payload, timeout=60)
    print("Server Response:", res.json())
    
    # Clean up remote helper
    print("Cleaning up remote helper...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.delete("temp_upload_helper.php")
    ftp.quit()
    print("✓ Sideload process completed cleanly")

if __name__ == "__main__":
    main()
