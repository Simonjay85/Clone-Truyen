<?php
/**
 * Tệp Update Story V13 - Dành cho việc viết lại truyện và cập nhật SEO RankMath
 * Chức năng: Cập nhật mô tả truyện, xóa chương cũ, đăng chương mới, cập nhật RankMath SEO
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

// Tự động lấy admin đầu tiên
$admins = get_users(['role' => 'administrator', 'number' => 1]);
if (empty($admins)) {
    http_response_code(500);
    echo json_encode(['error' => 'Không tìm thấy tài khoản Administrator nào']);
    exit;
}
$admin_id = $admins[0]->ID;
wp_set_current_user($admin_id);

$story_id = isset($input['story_id']) ? intval($input['story_id']) : 0;
$intro = isset($input['intro']) ? wp_kses_post($input['intro']) : '';
$focus_keyword = isset($input['focus_keyword']) ? sanitize_text_field($input['focus_keyword']) : '';
$seo_title = isset($input['seo_title']) ? sanitize_text_field($input['seo_title']) : '';
$seo_description = isset($input['seo_description']) ? sanitize_text_field($input['seo_description']) : '';
$chapters = isset($input['chapters']) ? $input['chapters'] : [];

if ($story_id <= 0 || empty($intro) || empty($chapters)) {
    http_response_code(400);
    echo json_encode(['error' => 'Thiếu thông tin ID truyện, giới thiệu hoặc danh sách chương!']);
    exit;
}

// Kiểm tra truyện có tồn tại không
$story = get_post($story_id);
if (!$story || $story->post_type !== 'truyen') {
    http_response_code(404);
    echo json_encode(['error' => 'Không tìm thấy truyện với ID: ' . $story_id]);
    exit;
}

// 1. Cập nhật nội dung truyện (Intro mới)
$update_post = wp_update_post([
    'ID'           => $story_id,
    'post_content' => $intro,
]);

if (is_wp_error($update_post)) {
    http_response_code(500);
    echo json_encode(['error' => 'Lỗi khi cập nhật truyện: ' . $update_post->get_error_message()]);
    exit;
}

// 2. Cập nhật RankMath SEO Metadata
update_post_meta($story_id, 'rank_math_focus_keyword', $focus_keyword);
update_post_meta($story_id, 'rank_math_title', $seo_title);
update_post_meta($story_id, 'rank_math_description', $seo_description);

// 3. Xóa toàn bộ chương cũ của truyện này
$old_chapters = get_posts([
    'post_type' => 'chuong',
    'meta_key' => '_truyen_id',
    'meta_value' => $story_id,
    'posts_per_page' => -1,
    'fields' => 'ids'
]);

$deleted_count = 0;
if (!empty($old_chapters)) {
    foreach ($old_chapters as $chap_id) {
        wp_delete_post($chap_id, true); // Xóa vĩnh viễn (bypass trash)
        $deleted_count++;
    }
}

// 4. Đăng 8 chương mới V13
$published_chapters = [];
foreach ($chapters as $index => $chap) {
    $chap_title = isset($chap['title']) ? sanitize_text_field($chap['title']) : ('Chương ' . ($index + 1));
    $chap_content = isset($chap['content']) ? wp_kses_post($chap['content']) : '';
    
    // Tạo chương mới
    $chap_id = wp_insert_post([
        'post_title'   => $chap_title,
        'post_content' => $chap_content,
        'post_status'  => 'publish',
        'post_type'    => 'chuong',
        'post_author'  => $admin_id,
        'menu_order'   => $index + 1 // Sắp xếp theo đúng thứ tự chương 1-8
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
    'title' => get_the_title($story_id),
    'deleted_chapters_count' => $deleted_count,
    'inserted_chapters_count' => count($published_chapters),
    'seo' => [
        'focus_keyword' => $focus_keyword,
        'seo_title' => $seo_title,
        'seo_description' => $seo_description
    ],
    'chapters' => $published_chapters
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
