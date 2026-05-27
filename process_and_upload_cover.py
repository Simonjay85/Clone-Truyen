#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
process_and_upload_cover.py — Process titled overlay and upload to doctieuthuyet.com
"""

import os
import sys
import argparse
import subprocess
import ftplib
import requests

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

def main():
    parser = argparse.ArgumentParser(description="Process titled cover overlay and deploy to doctieuthuyet.com")
    parser.add_argument("--base-image", required=True, help="Path to raw AI base image")
    parser.add_argument("--post-id", required=True, type=int, help="WordPress Post ID")
    parser.add_argument("--title", required=True, help="Title of the novel")
    parser.add_argument("--subtitle", default="", help="Subtitle/Author tag")
    parser.add_argument("--position", default="top", choices=["top", "bottom"], help="Text position")
    args = parser.parse_args()

    if not os.path.exists(args.base_image):
        print(f"❌ Base image not found: {args.base_image}")
        sys.exit(1)

    brain_dir = os.path.dirname(args.base_image)
    titled_cover_path = os.path.join(brain_dir, f"titled_cover_{args.post_id}.png")
    
    print("=" * 60)
    print(f"🚀 PROCESSING COVER FOR POST ID: {args.post_id} ({args.title})")
    print("=" * 60)

    # 1. Run cover_overlay_standard.py
    print(f"🎨 Running cover_overlay_standard.py --position {args.position}...")
    overlay_cmd = [
        "python3", "cover_overlay_standard.py",
        "--input", args.base_image,
        "--output", titled_cover_path,
        "--title", args.title,
        "--subtitle", args.subtitle,
        "--position", args.position
    ]
    try:
        res = subprocess.run(overlay_cmd, check=True, capture_output=True, text=True)
        print(res.stdout)
        print("✓ Successfully generated titled cover.")
    except subprocess.CalledProcessError as e:
        print("❌ Error running cover_overlay_standard.py:")
        print(e.stderr)
        sys.exit(1)

    if not os.path.exists(titled_cover_path):
        print(f"❌ Titled cover file was not created: {titled_cover_path}")
        sys.exit(1)

    # 2. Upload Titled Cover Image to FTP
    remote_filename = f"cover_update_card_{args.post_id}.png"
    print(f"📤 Uploading titled cover image to FTP /wp-content/uploads/{remote_filename}...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.cwd("wp-content/uploads")
        with open(titled_cover_path, "rb") as f:
            ftp.storbinary(f"STOR {remote_filename}", f)
        print("✓ Uploaded titled cover image via FTP.")
        ftp.quit()
    except Exception as e:
        print("❌ FTP Upload Error for titled cover image:", e)
        sys.exit(1)

    # 3. Create temp_update_cover.php helper content and upload
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

if (empty($post_id) || empty($filename)) {
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

// Set current user to administrator
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
        
    print("📤 Uploading temp_update_cover.php helper script via FTP...")
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
        sys.exit(1)

    # 4. Trigger WordPress endpoint
    print(f"🔗 Triggering cover update via endpoint...")
    success = False
    try:
        url = f"{WP_URL}/temp_update_cover.php?token=zen_cover_update_2026&post_id={args.post_id}&filename={remote_filename}"
        res = requests.get(url, timeout=60)
        print("Response Code:", res.status_code)
        try:
            res_data = res.json()
            print("Response Data:", res_data)
            if res_data.get("success"):
                success = True
        except Exception:
            print("Raw Response:", res.text)
    except Exception as e:
        print("❌ HTTP Request Error:", e)

    # 5. Clean up remote and local temp files
    print("🧹 Cleaning up helper script...")
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

    # Clean up local titled cover to save space
    if os.path.exists(titled_cover_path):
        os.remove(titled_cover_path)
        print("✓ Deleted temporary local titled cover.")

    print("=" * 60)
    if success:
        print(f"🎉 SUCCESS: COVER FOR POST {args.post_id} UPDATED LIVE!")
    else:
        print(f"❌ FAILURE: COULD NOT UPDATE COVER FOR POST {args.post_id}")
    print("=" * 60)
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
