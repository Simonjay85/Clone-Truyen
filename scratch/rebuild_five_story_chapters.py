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
HELPER = "rebuild_five_story_chapters_20260522.php"
PAYLOADS = [
    ROOT / "scratch" / "story_2089_v2_payload.json",
    ROOT / "scratch" / "story_2067_v2_payload.json",
    ROOT / "scratch" / "story_2052_v2_payload.json",
    ROOT / "scratch" / "story_2044_v2_payload.json",
    ROOT / "scratch" / "story_2035_v2_payload.json",
]


HELPER_PHP = """<?php
ini_set('display_errors', 0);
header('Content-Type: application/json; charset=utf-8');

$input = json_decode(file_get_contents('php://input'), true);
if (($input['secret_token'] ?? '') !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401);
    echo json_encode(['success' => false, 'error' => 'bad token'], JSON_UNESCAPED_UNICODE);
    exit;
}

require_once('wp-load.php');

$admins = get_users(['role' => 'administrator', 'number' => 1]);
if (!empty($admins)) {
    wp_set_current_user($admins[0]->ID);
    $admin_id = $admins[0]->ID;
} else {
    $admin_id = 1;
}

$results = [];
foreach (($input['stories'] ?? []) as $story_data) {
    $story_id = intval($story_data['story_id'] ?? 0);
    $story = get_post($story_id);
    if (!$story || $story->post_type !== 'truyen') {
        $results[] = ['story_id' => $story_id, 'success' => false, 'error' => 'story not found'];
        continue;
    }

    $title = sanitize_text_field($story_data['title'] ?? $story->post_title);
    $intro = wp_kses_post($story_data['intro'] ?? $story->post_content);
    $excerpt = sanitize_textarea_field(wp_trim_words(wp_strip_all_tags($intro), 58, '...'));

    wp_update_post([
        'ID' => $story_id,
        'post_title' => $title,
        'post_content' => $intro,
        'post_excerpt' => $excerpt,
        'post_status' => 'publish',
    ]);

    $existing_chaps = get_posts([
        'post_type' => 'chuong',
        'post_status' => 'any',
        'meta_key' => '_truyen_id',
        'meta_value' => $story_id,
        'posts_per_page' => -1,
        'fields' => 'ids',
    ]);

    $deleted = 0;
    foreach ($existing_chaps as $cid) {
        wp_delete_post($cid, true);
        $deleted++;
    }

    $inserted = [];
    foreach (($story_data['chapters'] ?? []) as $index => $chap) {
        $chap_title = sanitize_text_field($chap['title'] ?? ('Chương ' . ($index + 1)));
        $chap_content = wp_kses_post($chap['content'] ?? '');
        $chap_id = wp_insert_post([
            'post_title' => $chap_title,
            'post_content' => $chap_content,
            'post_status' => 'publish',
            'post_type' => 'chuong',
            'post_author' => $admin_id,
        ], true);
        if (!is_wp_error($chap_id)) {
            update_post_meta($chap_id, '_truyen_id', $story_id);
            $inserted[] = ['id' => $chap_id, 'title' => $chap_title];
        }
    }

    $results[] = [
        'story_id' => $story_id,
        'success' => true,
        'title' => get_the_title($story_id),
        'permalink' => get_permalink($story_id),
        'deleted_chapters' => $deleted,
        'inserted_chapters' => count($inserted),
        'cover_url' => get_the_post_thumbnail_url($story_id, 'full'),
    ];
}

if (class_exists('LiteSpeed\\Purge')) {
    \\LiteSpeed\\Purge::purge_all();
}
wp_cache_flush();

echo json_encode(['success' => true, 'results' => $results], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>"""


def main():
    helper_path = ROOT / "scratch" / HELPER
    helper_path.write_text(HELPER_PHP, encoding="utf-8")
    stories = [json.loads(path.read_text(encoding="utf-8")) for path in PAYLOADS]

    ftp = ftplib.FTP(FTP_HOST, timeout=45)
    ftp.login(FTP_USER, FTP_PASS)
    with helper_path.open("rb") as f:
        ftp.storbinary(f"STOR {HELPER}", f)
    ftp.quit()

    res = requests.post(
        f"{WP_URL}/{HELPER}",
        json={"secret_token": SECRET, "stories": stories},
        timeout=240,
    )
    print(res.status_code)
    print(res.text)
    res.raise_for_status()

    ftp = ftplib.FTP(FTP_HOST, timeout=45)
    ftp.login(FTP_USER, FTP_PASS)
    try:
        ftp.delete(HELPER)
        print(f"deleted {HELPER}")
    finally:
        ftp.quit()


if __name__ == "__main__":
    main()
