<?php
/**
 * fix_endings.php - Viết lại ch8 cho 3 truyện có kết thúc dang dở
 * ID 2227 (WP ch 4277), ID 2217 (WP ch 4285), ID 2675 (WP ch 4541)
 */
ini_set('display_errors', 0);
ini_set('max_execution_time', 120);
header('Content-Type: application/json');

$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401); echo json_encode(['error'=>'Unauthorized']); exit;
}
require_once('wp-load.php');

$updates = $input['updates'] ?? [];
$results = [];

foreach ($updates as $u) {
    $wp_id = intval($u['wp_id']);
    $post = get_post($wp_id);
    if (!$post) {
        $results[] = ['wp_id' => $wp_id, 'status' => 'not_found'];
        continue;
    }
    $data = [
        'ID'           => $wp_id,
        'post_title'   => $u['title'],
        'post_content' => wp_kses_post($u['content']),
    ];
    $ret = wp_update_post($data, true);
    if (is_wp_error($ret)) {
        $results[] = ['wp_id' => $wp_id, 'status' => 'error', 'msg' => $ret->get_error_message()];
    } else {
        if (function_exists('litespeed_purge_post')) litespeed_purge_post($wp_id);
        $results[] = [
            'wp_id'  => $wp_id,
            'slug'   => $post->post_name,
            'status' => 'updated',
            'len'    => strlen($u['content']),
        ];
    }
}

if (function_exists('litespeed_purge_all')) litespeed_purge_all();
echo json_encode(['results' => $results], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
