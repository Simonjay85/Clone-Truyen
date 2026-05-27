<?php
/**
 * Bulk Update Story Descriptions and Titles - Doctieuthuyet
 */

ini_set('display_errors', 0);
header('Content-Type: application/json; charset=utf-8');

$secret_token = "ZEN_TRUYEN_2026_BYPASS";

if (!isset($_GET['token']) || $_GET['token'] !== $secret_token) {
    http_response_code(401);
    echo json_encode(['error' => 'Từ chối truy cập: Sai Secret Token!']);
    exit;
}

require_once('wp-load.php');

// Authenticate as Admin
$admins = get_users(['role' => 'administrator', 'number' => 1]);
if (empty($admins)) {
    http_response_code(500);
    echo json_encode(['error' => 'Không tìm thấy tài khoản Administrator nào']);
    exit;
}
$admin_id = $admins[0]->ID;
wp_set_current_user($admin_id);

$json_file = 'all_descriptions_update.json';
if (!file_exists($json_file)) {
    http_response_code(404);
    echo json_encode(['error' => 'Không tìm thấy tệp JSON payload: ' . $json_file]);
    exit;
}

$raw_json = file_get_contents($json_file);
$stories_data = json_decode($raw_json, true);

if (empty($stories_data)) {
    http_response_code(400);
    echo json_encode(['error' => 'Dữ liệu JSON rỗng hoặc lỗi cú pháp']);
    exit;
}

$updated_count = 0;
$errors = [];
$results = [];

foreach ($stories_data as $story_id => $data) {
    $story_id = intval($story_id);
    $title = isset($data['title']) ? sanitize_text_field($data['title']) : '';
    $intro = isset($data['intro']) ? wp_kses_post($data['intro']) : '';
    
    if (empty($story_id) || empty($title) || empty($intro)) {
        $errors[] = "ID $story_id: Thiếu tiêu đề hoặc mô tả";
        continue;
    }
    
    // Check if post exists and is of type 'truyen'
    $post = get_post($story_id);
    if (!$post || $post->post_type !== 'truyen') {
        $errors[] = "ID $story_id: Không tìm thấy truyện hoặc sai post type";
        continue;
    }
    
    // Update the story title and description
    $res = wp_update_post([
        'ID'           => $story_id,
        'post_title'   => $title,
        'post_content' => $intro,
        'post_status'  => 'publish'
    ]);
    
    if (is_wp_error($res)) {
        $errors[] = "ID $story_id: Cập nhật thất bại - " . $res->get_error_message();
    } else {
        $updated_count++;
        $results[] = "ID $story_id: Cập nhật thành công";
    }
}

// Purge LiteSpeed Cache
if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
    $cache_purged = true;
} else {
    $cache_purged = false;
}

echo json_encode([
    'success' => true,
    'total_payload' => count($stories_data),
    'updated_count' => $updated_count,
    'errors_count' => count($errors),
    'errors' => $errors,
    'cache_purged' => $cache_purged,
    'details' => $results
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
