<?php
/**
 * Update Novel API - Cập nhật nội dung truyện đã tồn tại
 * Chức năng: Cập nhật intro + xóa chapters cũ + tạo chapters mới
 */

ini_set('display_errors', 0);
header('Content-Type: application/json');

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
    echo json_encode(['error' => 'Sai Secret Token']);
    exit;
}

$story_id = isset($input['story_id']) ? intval($input['story_id']) : 0;
$intro = isset($input['intro']) ? $input['intro'] : '';
$chapters = isset($input['chapters']) ? $input['chapters'] : [];

if (empty($story_id) || empty($chapters)) {
    http_response_code(400);
    echo json_encode(['error' => 'Thiếu story_id hoặc chapters']);
    exit;
}

require_once('wp-load.php');

// Verify story exists
$story = get_post($story_id);
if (!$story || $story->post_type !== 'truyen') {
    http_response_code(404);
    echo json_encode(['error' => "Story ID $story_id không tồn tại hoặc không phải post_type=truyen"]);
    exit;
}

$admins = get_users(['role' => 'administrator', 'number' => 1]);
$admin_id = $admins[0]->ID;
wp_set_current_user($admin_id);

// 1. Update intro if provided
$intro_status = 'Không thay đổi';
if (!empty($intro)) {
    wp_update_post([
        'ID' => $story_id,
        'post_content' => wp_kses_post($intro)
    ]);
    $intro_status = 'Đã cập nhật intro';
}

// 2. Delete old chapters
$old_chapters = get_posts([
    'post_type' => 'chuong',
    'meta_key' => '_truyen_id',
    'meta_value' => $story_id,
    'numberposts' => -1,
    'post_status' => 'any',
    'fields' => 'ids'
]);

$deleted_count = 0;
foreach ($old_chapters as $old_id) {
    wp_delete_post($old_id, true); // force delete, bypass trash
    $deleted_count++;
}

// 3. Create new chapters
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

// 4. Purge cache
if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

echo json_encode([
    'success' => true,
    'story_id' => $story_id,
    'story_title' => $story->post_title,
    'intro_status' => $intro_status,
    'old_chapters_deleted' => $deleted_count,
    'new_chapters_count' => count($published_chapters),
    'chapters' => $published_chapters
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
