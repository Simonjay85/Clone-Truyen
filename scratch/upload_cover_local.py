import os
import ftplib
import requests
import urllib.parse
import random

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

def set_cover_via_local_upload(story_id, prompt):
    print(f"Generating and downloading cover locally for story {story_id}...")
    escaped_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{escaped_prompt}?width=1200&height=1200&seed={random.randint(1, 99999)}&nologo=true"
    
    # Download locally
    local_img_path = f"scratch/temp_cover_{story_id}.png"
    try:
        r = requests.get(url, timeout=90)
        r.raise_for_status()
        with open(local_img_path, "wb") as f:
            f.write(r.content)
        print(f"✓ Downloaded locally to {local_img_path}")
    except Exception as e:
        print(f"❌ Failed to download from Pollinations: {e}")
        return False

    # Upload update_cover_local.php and the cover image via FTP
    print("Uploading helper and image to FTP...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        
        # Upload PHP helper
        temp_helper_path = "scratch/temp_helper.php"
        with open(temp_helper_path, "w", encoding="utf-8") as f:
            f.write(PHP_HELPER)
        with open(temp_helper_path, "rb") as f:
            ftp.storbinary("STOR update_cover_local.php", f)
        os.remove(temp_helper_path)
        print("✓ Uploaded update_cover_local.php")
        
        # Upload cover image to wp-content/uploads/
        remote_filename = f"cover_temp_{story_id}.png"
        remote_path = f"wp-content/uploads/{remote_filename}"
        with open(local_img_path, "rb") as f:
            ftp.storbinary(f"STOR {remote_path}", f)
        print(f"✓ Uploaded {remote_filename} to server")
        
        ftp.quit()
    except Exception as e:
        print(f"❌ FTP Error: {e}")
        if os.path.exists(local_img_path):
            os.remove(local_img_path)
        return False

    # Call PHP helper
    print("Triggering PHP helper on server...")
    payload = {
        "secret": "ZEN_TRUYEN_2026_BYPASS",
        "post_id": story_id,
        "filename": remote_filename
    }
    try:
        res = requests.post(f"{WP_URL}/update_cover_local.php", json=payload, timeout=60)
        data = res.json()
        if data.get('success'):
            print(f"✓ Cover for Story {story_id} updated successfully! Attachment ID: {data['attachment_id']}")
            success = True
        else:
            print(f"⚠️ Error from server: {data}")
            success = False
    except Exception as e:
        print(f"❌ Server trigger error: {e}")
        success = False

    # Clean up local image and remote PHP helper
    if os.path.exists(local_img_path):
        os.remove(local_img_path)
        
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("update_cover_local.php")
        ftp.quit()
        print("✓ Deleted update_cover_local.php from server")
    except:
        pass
        
    return success

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        story_id = int(sys.argv[1])
        prompt = sys.argv[2]
        set_cover_via_local_upload(story_id, prompt)
