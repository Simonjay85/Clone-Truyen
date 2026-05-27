#!/usr/bin/env python3
import ftplib
import json
from pathlib import Path

import requests


FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
SECRET = "ZEN_TRUYEN_2026_BYPASS"
OUT_DIR = Path("scratch/chatgpt_covers_3743_3755_3767_20260525")

COVERS = [
    {"id": 3767, "local_file": OUT_DIR / "3767_cover.png", "remote_name": "chatgpt-cover-3767-20260525.png"},
    {"id": 3755, "local_file": OUT_DIR / "3755_cover.png", "remote_name": "chatgpt-cover-3755-20260525.png"},
    {"id": 3743, "local_file": OUT_DIR / "3743_cover.png", "remote_name": "chatgpt-cover-3743-20260525.png"},
]

PHP_HELPER = """<?php
require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

header('Content-Type: application/json');

$secret = "ZEN_TRUYEN_2026_BYPASS";
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret']) || $input['secret'] !== $secret) {
    echo json_encode(['error' => 'Unauthorized']);
    exit;
}

$post_id = intval($input['post_id']);
$filename = sanitize_file_name($input['filename']);
$local_path = ABSPATH . 'wp-content/uploads/' . $filename;
if (!file_exists($local_path)) {
    echo json_encode(['error' => 'File not found: ' . $local_path]);
    exit;
}

$tmp = tempnam(get_temp_dir(), 'cover');
if (!copy($local_path, $tmp)) {
    echo json_encode(['error' => 'Failed to copy file']);
    exit;
}

$file_array = [
    'name' => 'cover-' . $post_id . '-chatgpt-image-20260525-' . rand(100, 999) . '.png',
    'tmp_name' => $tmp,
];

$attach_id = media_handle_sideload($file_array, $post_id);
if (is_wp_error($attach_id)) {
    @unlink($tmp);
    echo json_encode(['error' => $attach_id->get_error_message()]);
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
    'attachment_id' => $attach_id,
    'thumbnail' => get_the_post_thumbnail_url($post_id, 'full'),
], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
?>"""


def main():
    helper_path = OUT_DIR / "update_cover_local.php"
    helper_path.write_text(PHP_HELPER, encoding="utf-8")
    results = []
    ftp = ftplib.FTP(FTP_HOST, timeout=60)
    ftp.login(FTP_USER, FTP_PASS)
    try:
        with helper_path.open("rb") as handle:
            ftp.storbinary("STOR update_cover_local.php", handle)
        print("Uploaded helper.")

        for cover in COVERS:
            with cover["local_file"].open("rb") as handle:
                ftp.storbinary(f"STOR wp-content/uploads/{cover['remote_name']}", handle)
            print(f"[{cover['id']}] Uploaded cover.")
            payload = {"secret": SECRET, "post_id": cover["id"], "filename": cover["remote_name"]}
            res = requests.post(f"{WP_URL}/update_cover_local.php", json=payload, timeout=90)
            try:
                data = res.json()
            except json.JSONDecodeError:
                data = {"error": res.text[:500]}
            print(f"[{cover['id']}] {data}")
            results.append({**cover, "local_file": str(cover["local_file"]), "server": data})
    finally:
        try:
            ftp.delete("update_cover_local.php")
            print("Deleted helper.")
        except Exception as exc:
            print("cleanup warning", exc)
        ftp.quit()
        try:
            helper_path.unlink()
        except FileNotFoundError:
            pass

    (OUT_DIR / "upload_results.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
