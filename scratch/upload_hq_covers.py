import os
import ftplib
import requests
import json
import sys

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

# Map of story_id -> local cover image path
COVERS = {
    2120: "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f/cover_bep_truong_1779287633925.png",
    2137: "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f/cover_thua_ke_1779287651453.png",
    2145: "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f/cover_duoc_pham_1779287668090.png",
    2156: "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f/cover_vo_than_1779287684148.png",
}

def main():
    print("=" * 60)
    print("🎨 UPLOADING HIGH-QUALITY COVERS TO SERVER")
    print("=" * 60)

    # 1. Create a PHP helper that downloads an image from URL and sets it as post thumbnail
    php_code = """<?php
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

    # Write the PHP helper locally
    with open("update_cover_hq.php", "w") as f:
        f.write(php_code)

    # 2. Upload PHP helper to server
    print("\nUploading update_cover_hq.php to FTP...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open("update_cover_hq.php", "rb") as f:
        ftp.storbinary("STOR update_cover_hq.php", f)
    print("✓ Uploaded update_cover_hq.php")

    # 3. Upload each cover image to the uploads directory on FTP
    for story_id, local_path in COVERS.items():
        if not os.path.exists(local_path):
            print(f"❌ Cover not found for story {story_id}: {local_path}")
            continue

        filename = f"cover_hq_{story_id}.png"
        remote_path = f"wp-content/uploads/{filename}"
        
        print(f"\nUploading cover for story {story_id}...")
        with open(local_path, "rb") as f:
            ftp.storbinary(f"STOR {remote_path}", f)
        print(f"✓ Uploaded {filename} to server")

        # 4. Call PHP helper to set as featured image
        image_url = f"{WP_URL}/wp-content/uploads/{filename}"
        payload = {
            "secret": "ZEN_TRUYEN_2026_BYPASS",
            "post_id": story_id,
            "image_url": image_url
        }
        try:
            res = requests.post(f"{WP_URL}/update_cover_hq.php", json=payload, timeout=60)
            data = res.json()
            if data.get('success'):
                print(f"✓ Story {story_id}: Cover set successfully! (Attachment ID: {data['attachment_id']})")
            else:
                print(f"⚠️ Story {story_id}: {data}")
        except Exception as e:
            print(f"❌ Story {story_id} API error: {e}")

    # 5. Clean up
    try:
        ftp.delete("update_cover_hq.php")
        print("\n✓ Deleted update_cover_hq.php from server for security.")
    except:
        pass
    ftp.quit()
    os.remove("update_cover_hq.php")
    print("✓ Done! All high-quality covers uploaded.")

if __name__ == "__main__":
    main()
