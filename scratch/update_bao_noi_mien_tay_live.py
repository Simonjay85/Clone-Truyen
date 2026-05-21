import ftplib
import json
from pathlib import Path

import requests


FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
SECRET = "ZEN_TRUYEN_2026_BYPASS"

ROOT = Path(__file__).resolve().parents[1]
PAYLOAD_PATH = ROOT / "scratch" / "bao_noi_mien_tay_v2.json"
COVER_PATH = ROOT / "assets" / "covers" / "bao-noi-mien-tay-cover-v2.png"
REMOTE_HELPER = "update_bao_noi_mien_tay_2457.php"
REMOTE_COVER = "bao-noi-mien-tay-cover-v2.png"


HELPER_PHP = """<?php
ini_set('display_errors', 0);
header('Content-Type: application/json; charset=utf-8');

$raw = file_get_contents('php://input');
$input = json_decode($raw, true);
$secret_token = 'ZEN_TRUYEN_2026_BYPASS';

if (!isset($input['secret_token']) || $input['secret_token'] !== $secret_token) {
    http_response_code(401);
    echo json_encode(['success' => false, 'error' => 'bad token'], JSON_UNESCAPED_UNICODE);
    exit;
}

require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

$admins = get_users(['role' => 'administrator', 'number' => 1]);
if (empty($admins)) {
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'no admin'], JSON_UNESCAPED_UNICODE);
    exit;
}
wp_set_current_user($admins[0]->ID);

$story_id = intval($input['story_id'] ?? 0);
$story = get_post($story_id);
if (!$story || $story->post_type !== 'truyen') {
    http_response_code(404);
    echo json_encode(['success' => false, 'error' => 'story not found'], JSON_UNESCAPED_UNICODE);
    exit;
}

$title = sanitize_text_field($input['title'] ?? $story->post_title);
$intro = wp_kses_post($input['intro'] ?? $story->post_content);
$chapters = $input['chapters'] ?? [];

$story_update = wp_update_post([
    'ID' => $story_id,
    'post_title' => $title,
    'post_content' => $intro,
    'post_status' => 'publish',
], true);

if (is_wp_error($story_update)) {
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => $story_update->get_error_message()], JSON_UNESCAPED_UNICODE);
    exit;
}

$chapter_posts = get_posts([
    'post_type' => 'chuong',
    'post_status' => 'any',
    'meta_key' => '_truyen_id',
    'meta_value' => $story_id,
    'posts_per_page' => -1,
    'orderby' => 'ID',
    'order' => 'ASC',
]);

$updated_chapters = [];
foreach ($chapters as $index => $chap) {
    if (!isset($chapter_posts[$index])) {
        continue;
    }
    $chap_id = $chapter_posts[$index]->ID;
    $chap_title = sanitize_text_field($chap['title'] ?? ('Chương ' . ($index + 1)));
    $chap_content = wp_kses_post($chap['content'] ?? '');
    $res = wp_update_post([
        'ID' => $chap_id,
        'post_title' => $chap_title,
        'post_content' => $chap_content,
        'post_status' => 'publish',
    ], true);
    if (!is_wp_error($res)) {
        $updated_chapters[] = ['id' => $chap_id, 'title' => $chap_title];
    }
}

$cover_status = 'not updated';
$cover_filename = sanitize_file_name($input['cover_local_filename'] ?? '');
if (!empty($cover_filename)) {
    $local_path = ABSPATH . $cover_filename;
    if (file_exists($local_path)) {
        $tmp = tempnam(get_temp_dir(), 'cover2457');
        if (copy($local_path, $tmp)) {
            $file_array = [
                'name' => 'bao-noi-mien-tay-cover-v2-' . time() . '.png',
                'tmp_name' => $tmp,
            ];
            $attach_id = media_handle_sideload($file_array, $story_id);
            if (!is_wp_error($attach_id)) {
                set_post_thumbnail($story_id, $attach_id);
                $cover_status = 'updated';
            } else {
                $cover_status = 'media error: ' . $attach_id->get_error_message();
                @unlink($tmp);
            }
        } else {
            $cover_status = 'copy failed';
        }
        @unlink($local_path);
    } else {
        $cover_status = 'cover file not found';
    }
}

if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

echo json_encode([
    'success' => true,
    'story_id' => $story_id,
    'story_title' => get_the_title($story_id),
    'chapters_found' => count($chapter_posts),
    'chapters_updated' => count($updated_chapters),
    'cover_status' => $cover_status,
    'cover_url' => get_the_post_thumbnail_url($story_id, 'full'),
    'updated_chapters' => $updated_chapters,
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>"""


def main():
    data = json.loads(PAYLOAD_PATH.read_text(encoding="utf-8"))
    data.update(
        {
            "secret_token": SECRET,
            "story_id": 2457,
            "cover_local_filename": REMOTE_COVER,
        }
    )

    helper_path = ROOT / "scratch" / REMOTE_HELPER
    helper_path.write_text(HELPER_PHP, encoding="utf-8")

    ftp = ftplib.FTP(FTP_HOST, timeout=45)
    ftp.login(FTP_USER, FTP_PASS)
    with helper_path.open("rb") as f:
        ftp.storbinary(f"STOR {REMOTE_HELPER}", f)
    with COVER_PATH.open("rb") as f:
        ftp.storbinary(f"STOR {REMOTE_COVER}", f)
    ftp.quit()

    res = requests.post(f"{WP_URL}/{REMOTE_HELPER}", json=data, timeout=180)
    print(res.status_code)
    print(res.text)
    res.raise_for_status()

    ftp = ftplib.FTP(FTP_HOST, timeout=45)
    ftp.login(FTP_USER, FTP_PASS)
    for remote in [REMOTE_HELPER]:
        try:
            ftp.delete(remote)
            print(f"deleted {remote}")
        except Exception as exc:
            print(f"cleanup warning {remote}: {exc}")
    ftp.quit()


if __name__ == "__main__":
    main()
