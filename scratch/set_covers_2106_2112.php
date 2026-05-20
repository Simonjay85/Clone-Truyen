<?php
ini_set('display_errors', 0);
header('Content-Type: application/json; charset=utf-8');

if ($_SERVER['REQUEST_METHOD'] === 'GET' && (!isset($_GET['secret_token']) || $_GET['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS')) {
    http_response_code(401);
    echo json_encode(['error' => 'Unauthorized']);
    exit;
}

require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

$covers = [
    2106 => 'https://picsum.photos/seed/milktea-doctieuthuyet-2106/800/1200',
    2112 => 'https://picsum.photos/seed/garage-doctieuthuyet-2112/800/1200',
];

$results = [];
foreach ($covers as $post_id => $url) {
    $tmp = download_url($url, 60);
    if (is_wp_error($tmp)) {
        $results[] = ['id' => $post_id, 'success' => false, 'error' => $tmp->get_error_message()];
        continue;
    }

    $file_array = [
        'name' => 'cover-' . $post_id . '.jpg',
        'tmp_name' => $tmp,
    ];

    $attach_id = media_handle_sideload($file_array, $post_id);
    if (is_wp_error($attach_id)) {
        @unlink($tmp);
        $results[] = ['id' => $post_id, 'success' => false, 'error' => $attach_id->get_error_message()];
        continue;
    }

    set_post_thumbnail($post_id, $attach_id);
    $results[] = ['id' => $post_id, 'success' => true, 'attachment_id' => $attach_id];
}

if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

echo json_encode(['success' => true, 'results' => $results], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
