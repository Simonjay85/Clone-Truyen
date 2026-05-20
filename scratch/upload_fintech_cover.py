import os
import ftplib
import requests

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

STORY_ID = 2165
LOCAL_PATH = "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f/cover_fintech_1779287702263.png"

php_code = """<?php
require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');
header('Content-Type: application/json');
$raw = file_get_contents('php://input');
$input = json_decode($raw, true);
if (!isset($input['secret']) || $input['secret'] !== "ZEN_TRUYEN_2026_BYPASS") { echo json_encode(['error'=>'Unauthorized']); exit; }
$post_id = intval($input['post_id']);
$image_url = esc_url_raw($input['image_url']);
$old = get_post_thumbnail_id($post_id);
if ($old) wp_delete_attachment($old, true);
$tmp = download_url($image_url, 60);
if (is_wp_error($tmp)) { echo json_encode(['error'=>$tmp->get_error_message()]); exit; }
$f = array('name'=>'cover-'.$post_id.'-hq.png','tmp_name'=>$tmp);
$a = media_handle_sideload($f, $post_id);
if (is_wp_error($a)) { @unlink($tmp); echo json_encode(['error'=>$a->get_error_message()]); exit; }
set_post_thumbnail($post_id, $a);
if (function_exists('litespeed_purge_all')) litespeed_purge_all();
echo json_encode(['success'=>true,'post_id'=>$post_id,'attachment_id'=>$a]);
?>"""

with open("update_cover_hq.php", "w") as f:
    f.write(php_code)

ftp = ftplib.FTP(FTP_HOST, timeout=30)
ftp.login(FTP_USER, FTP_PASS)
with open("update_cover_hq.php", "rb") as f:
    ftp.storbinary("STOR update_cover_hq.php", f)

filename = f"cover_hq_{STORY_ID}.png"
with open(LOCAL_PATH, "rb") as f:
    ftp.storbinary(f"STOR wp-content/uploads/{filename}", f)
print(f"✓ Uploaded {filename}")

res = requests.post(f"{WP_URL}/update_cover_hq.php", json={
    "secret": "ZEN_TRUYEN_2026_BYPASS",
    "post_id": STORY_ID,
    "image_url": f"{WP_URL}/wp-content/uploads/{filename}"
}, timeout=60)
print(res.json())

try:
    ftp.delete("update_cover_hq.php")
except: pass
ftp.quit()
os.remove("update_cover_hq.php")
print("✓ Done!")
