#!/usr/bin/env python3
import argparse
import ftplib
import io
import os
import sys

import requests

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
TOKEN = "zen_cover_update_2026"


PHP_HELPER = """<?php
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

$tmp_copy = ABSPATH . 'wp-content/uploads/tmp_' . $filename;
if (!copy($filepath, $tmp_copy)) {
    echo json_encode(['error' => 'Failed to copy file to temp path']);
    exit;
}

$admins = get_users(['role' => 'administrator', 'number' => 1]);
if (!empty($admins)) {
    wp_set_current_user($admins[0]->ID);
}

$file_array = [
    'name' => 'cover-' . $post_id . '-' . rand(100, 999) . '.png',
    'tmp_name' => $tmp_copy
];

$attach_id = media_handle_sideload($file_array, $post_id);

if (!is_wp_error($attach_id)) {
    $old_thumb_id = get_post_thumbnail_id($post_id);
    if ($old_thumb_id) {
        wp_delete_attachment($old_thumb_id, true);
    }
    set_post_thumbnail($post_id, $attach_id);
    if (function_exists('litespeed_purge_all')) {
        litespeed_purge_all();
    }
    @unlink($filepath);
    echo json_encode(['success' => true, 'post_id' => $post_id, 'attach_id' => $attach_id]);
} else {
    if (file_exists($tmp_copy)) @unlink($tmp_copy);
    echo json_encode(['success' => false, 'error' => $attach_id->get_error_message()]);
}
?>"""


def ftp_store(local_path, remote_name):
    with ftplib.FTP(FTP_HOST, timeout=30) as ftp:
        ftp.login(FTP_USER, FTP_PASS)
        ftp.cwd("wp-content/uploads")
        with open(local_path, "rb") as f:
            ftp.storbinary(f"STOR {remote_name}", f)


def upload_helper():
    with ftplib.FTP(FTP_HOST, timeout=30) as ftp:
        ftp.login(FTP_USER, FTP_PASS)
        ftp.storbinary("STOR temp_update_cover.php", io.BytesIO(PHP_HELPER.encode("utf-8")))


def delete_helper():
    try:
        with ftplib.FTP(FTP_HOST, timeout=30) as ftp:
            ftp.login(FTP_USER, FTP_PASS)
            ftp.delete("temp_update_cover.php")
    except Exception as exc:
        print(f"cleanup warning: {exc}")


def main():
    parser = argparse.ArgumentParser(description="Upload a finished, already-titled cover image.")
    parser.add_argument("--image", required=True)
    parser.add_argument("--post-id", required=True, type=int)
    args = parser.parse_args()

    if not os.path.exists(args.image):
        print(f"missing image: {args.image}")
        sys.exit(1)

    remote_name = f"cover_finished_{args.post_id}.png"
    ftp_store(args.image, remote_name)
    upload_helper()
    try:
        url = f"{WP_URL}/temp_update_cover.php?token={TOKEN}&post_id={args.post_id}&filename={remote_name}"
        res = requests.get(url, timeout=60)
        print(res.status_code)
        print(res.text)
        data = res.json()
    finally:
        delete_helper()

    sys.exit(0 if data.get("success") else 1)


if __name__ == "__main__":
    main()
