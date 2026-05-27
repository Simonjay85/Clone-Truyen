<?php
/**
 * fix_dup_chapters.php
 * Cập nhật nội dung các chương bị trùng lặp
 * Tìm chương theo slug rồi update content
 */
ini_set('display_errors', 0);
ini_set('max_execution_time', 300);
header('Content-Type: application/json');

$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401); echo json_encode(['error'=>'Unauthorized']); exit;
}
require_once('wp-load.php');

$updates = $input['updates'] ?? [];
$results = [];

foreach ($updates as $u) {
    $slug    = $u['slug'] ?? '';
    $content = $u['content'] ?? '';
    $title   = $u['title'] ?? '';

    if (!$slug || !$content) {
        $results[] = ['slug' => $slug, 'status' => 'skip_missing'];
        continue;
    }

    $post = get_page_by_path($slug, OBJECT, 'chuong');
    if (!$post) {
        $results[] = ['slug' => $slug, 'status' => 'not_found'];
        continue;
    }

    $data = ['ID' => $post->ID, 'post_content' => wp_kses_post($content)];
    if ($title) $data['post_title'] = sanitize_text_field($title);

    $r = wp_update_post($data);
    if (is_wp_error($r)) {
        $results[] = ['slug' => $slug, 'id' => $post->ID, 'status' => 'error', 'msg' => $r->get_error_message()];
    } else {
        $results[] = ['slug' => $slug, 'id' => $post->ID, 'status' => 'ok', 'title' => $post->post_title, 'len' => strlen($content)];
    }
}

if (function_exists('litespeed_purge_all')) litespeed_purge_all();

echo json_encode(['success' => true, 'total' => count($results), 'results' => $results], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
