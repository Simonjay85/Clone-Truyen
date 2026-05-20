<?php
/**
 * Overwrite Story Chapters & Metadata API - Doctieuthuyet.com
 * Chức năng: Xóa sạch các chương cũ và chèn 8 chương mới nguyên bản để tránh trùng lặp hoặc mâu thuẫn.
 */

ini_set('display_errors', 0);
header('Content-Type: application/json; charset=utf-8');

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    http_response_code(405);
    echo json_encode(['error' => 'Chỉ hỗ trợ phương thức POST']);
    exit;
}

$raw_input = file_get_contents('php://input');
$input = json_decode($raw_input, true);

$secret_token = "ZEN_TRUYEN_2026_BYPASS";

if (!isset($input['secret_token']) || $input['secret_token'] !== $secret_token) {
    http_response_code(401);
    echo json_encode(['error' => 'Từ chối truy cập: Sai Secret Token!']);
    exit;
}

require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

$story_id = isset($input['story_id']) ? intval($input['story_id']) : 2052;
$title = isset($input['title']) ? sanitize_text_field($input['title']) : '';
$intro = isset($input['intro']) ? wp_kses_post($input['intro']) : '';
$chapters = isset($input['chapters']) ? $input['chapters'] : [];

if (empty($title) || empty($intro) || empty($chapters)) {
    http_response_code(400);
    echo json_encode(['error' => 'Thiếu thông tin tiêu đề, mô tả hoặc danh sách chương!']);
    exit;
}

// 1. Kiểm tra truyện tồn tại
$story_post = get_post($story_id);
if (!$story_post || $story_post->post_type !== 'truyen') {
    http_response_code(404);
    echo json_encode(['error' => 'Không tìm thấy truyện với ID: ' . $story_id]);
    exit;
}

// Tự động lấy admin đầu tiên
$admins = get_users(['role' => 'administrator', 'number' => 1]);
if (empty($admins)) {
    http_response_code(500);
    echo json_encode(['error' => 'Không tìm thấy tài khoản Administrator nào']);
    exit;
}
$admin_id = $admins[0]->ID;
wp_set_current_user($admin_id);

// 2. Xóa sạch các chương cũ của truyện này
$existing_chaps = get_posts(array(
    'post_type' => 'chuong',
    'meta_key' => '_truyen_id',
    'meta_value' => $story_id,
    'posts_per_page' => -1,
    'fields' => 'ids'
));

$deleted_count = 0;
foreach ($existing_chaps as $cid) {
    wp_delete_post($cid, true);
    $deleted_count++;
}

// 3. Cập nhật tiêu đề và mô tả của truyện gốc
$update_result = wp_update_post([
    'ID'           => $story_id,
    'post_title'   => $title,
    'post_content' => $intro
]);

if (is_wp_error($update_result)) {
    http_response_code(500);
    echo json_encode(['error' => 'Không thể cập nhật truyện gốc: ' . $update_result->get_error_message()]);
    exit;
}

// Cập nhật trạng thái truyện thành ongoing
update_post_meta($story_id, 'truyen_status', 'ongoing');

// 4. Thêm các chương mới một cách tuần tự
$published_chapters = [];
foreach ($chapters as $index => $chap) {
    $chap_title = isset($chap['title']) ? sanitize_text_field($chap['title']) : ('Chương ' . ($index + 1));
    $chap_content = isset($chap['content']) ? wp_kses_post($chap['content']) : '';
    
    $chap_id = wp_insert_post([
        'post_title'   => $chap_title,
        'post_content' => $chap_content,
        'post_status'  => 'publish',
        'post_type'    => 'chuong',
        'post_author'  => $admin_id
    ]);
    
    if (!is_wp_error($chap_id)) {
        update_post_meta($chap_id, '_truyen_id', $story_id);
        $published_chapters[] = [
            'id' => $chap_id,
            'title' => $chap_title
        ];
    }
}

// 5. Xóa bộ nhớ đệm (Purge LSCache)
if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

echo json_encode([
    'success' => true,
    'story_id' => $story_id,
    'title' => $title,
    'deleted_chapters_count' => $deleted_count,
    'inserted_chapters_count' => count($published_chapters),
    'chapters' => $published_chapters
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
