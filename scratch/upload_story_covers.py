import os
import ftplib
import requests
import json

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
    'name' => 'cover-' . $post_id . '-hq-' . rand(100,999) . '.png',
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

// Clean up the original uploaded file on disk
@unlink($local_path);

echo json_encode([
    'success' => true,
    'post_id' => $post_id,
    'attachment_id' => $attach_id
]);
?>"""

def main():
    print("🚀 STARTING STORY COVERS UPLOAD & SIDELOAD...")
    
    # 1. Connect to FTP and upload PHP helper
    print("📤 Connecting to FTP to upload helper...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        
        # Write PHP helper locally first to temp_update_helper.php
        temp_helper_path = "scratch/temp_update_helper.php"
        with open(temp_helper_path, "w", encoding="utf-8") as f:
            f.write(PHP_HELPER)
            
        with open(temp_helper_path, "rb") as f:
            ftp.storbinary("STOR update_cover_local.php", f)
            
        os.remove(temp_helper_path)
        print("✓ Uploaded update_cover_local.php helper script.")
        
        # Define updates
        updates = [
            {"story_id": 2587, "local_file": "scratch/cover_2587_titled.png", "remote_name": "cover_2587_titled_final.png"}
        ]
        
        for up in updates:
            story_id = up["story_id"]
            local_file = up["local_file"]
            remote_name = up["remote_name"]
            
            if not os.path.exists(local_file):
                print(f"❌ Local cover file {local_file} not found! Skipping...")
                continue
                
            print(f"\n📤 Uploading {local_file} to /wp-content/uploads/{remote_name} via FTP...")
            with open(local_file, "rb") as f:
                ftp.storbinary(f"STOR wp-content/uploads/{remote_name}", f)
            print(f"✓ Uploaded {remote_name} successfully.")
            
            # Call PHP helper API to register cover in WordPress
            print(f"📡 Triggering API for story ID {story_id}...")
            payload = {
                "secret": "ZEN_TRUYEN_2026_BYPASS",
                "post_id": story_id,
                "filename": remote_name
            }
            try:
                res = requests.post(f"{WP_URL}/update_cover_local.php", json=payload, timeout=60)
                data = res.json()
                if data.get('success'):
                    print(f"🎉 Cover for Story {story_id} updated successfully! Attachment ID: {data['attachment_id']}")
                else:
                    print(f"❌ Server returned error for Story {story_id}: {data}")
            except Exception as e:
                print(f"❌ Server API call error for Story {story_id}: {e}")
                
        # Delete PHP helper from server
        print("\n🧹 Cleaning up PHP helper from remote server...")
        try:
            ftp.delete("update_cover_local.php")
            print("✓ Removed update_cover_local.php from remote server.")
        except Exception as e:
            print(f"⚠️ Could not delete update_cover_local.php: {e}")
            
        ftp.quit()
        print("\n✨ Finished covers upload process successfully.")
    except Exception as e:
        print(f"❌ Critical FTP error during covers update: {e}")

if __name__ == "__main__":
    main()
