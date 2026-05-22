<?php
/**
 * Tệp PHP Helper dùng để cập nhật truyện cũ chuẩn V13 và SEO RankMath
 * Chỉ chạy khi có secret_token hợp lệ.
 */

ini_set('display_errors', 0);
ini_set('max_execution_time', 300); // 5 phút để xử lý lượng lớn dữ liệu
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
    echo json_encode(['error' => 'Từ chối truy cập: Sai Secret Token!']);
    exit;
}

require_once('wp-load.php');

$story_id = isset($input['story_id']) ? intval($input['story_id']) : 0;
$title = isset($input['title']) ? sanitize_text_field($input['title']) : '';
$intro = isset($input['intro']) ? wp_kses_post($input['intro']) : '';
$author = isset($input['author']) ? sanitize_text_field($input['author']) : 'Đang cập nhật';
$chapters = isset($input['chapters']) ? $input['chapters'] : [];
$seo = isset($input['seo']) ? $input['seo'] : [];

if ($story_id <= 0 || empty($title) || empty($intro) || empty($chapters)) {
    http_response_code(400);
    echo json_encode(['error' => 'Thiếu ID truyện, tiêu đề, mô tả hoặc danh sách chương!']);
    exit;
}

// 1. Cập nhật bài viết truyện chính
$story_post = get_post($story_id);
if (!$story_post || $story_post->post_type !== 'truyen') {
    http_response_code(404);
    echo json_encode(['error' => 'Không tìm thấy truyện với ID: ' . $story_id]);
    exit;
}

$update_res = wp_update_post([
    'ID'           => $story_id,
    'post_title'   => $title,
    'post_content' => $intro,
    'post_status'  => 'publish'
]);

if (is_wp_error($update_res)) {
    http_response_code(500);
    echo json_encode(['error' => 'Lỗi khi cập nhật thông tin truyện: ' . $update_res->get_error_message()]);
    exit;
}

// Cập nhật tác giả và các meta khác
update_post_meta($story_id, 'truyen_tacgia', $author);

// Cập nhật RankMath SEO meta fields
if (!empty($seo)) {
    $focus_kw = isset($seo['focus_keyword']) ? sanitize_text_field($seo['focus_keyword']) : '';
    $seo_title = isset($seo['seo_title']) ? sanitize_text_field($seo['seo_title']) : '';
    $seo_desc = isset($seo['seo_description']) ? sanitize_text_field($seo['seo_description']) : '';
    
    if ($focus_kw) {
        update_post_meta($story_id, 'rank_math_focus_keyword', $focus_kw);
        update_post_meta($story_id, '_rank_math_focus_keyword', $focus_kw);
    }
    if ($seo_title) {
        update_post_meta($story_id, 'rank_math_title', $seo_title);
        update_post_meta($story_id, '_rank_math_title', $seo_title);
    }
    if ($seo_desc) {
        update_post_meta($story_id, 'rank_math_description', $seo_desc);
        update_post_meta($story_id, '_rank_math_description', $seo_desc);
    }
    update_post_meta($story_id, 'rank_math_rich_snippet', 'article');
}

// 2. Xóa toàn bộ chương cũ của truyện này
$old_chaps = get_posts([
    'post_type'      => 'chuong',
    'posts_per_page' => -1,
    'meta_query'     => [
        [
            'key'     => '_truyen_id',
            'value'   => $story_id,
            'compare' => '='
        ]
    ]
]);

$deleted_count = 0;
foreach ($old_chaps as $c) {
    wp_delete_post($c->ID, true); // true: force delete bypass trash
    $deleted_count++;
}

// 3. Đăng các chương mới
$published_chapters = [];
$admins = get_users(['role' => 'administrator', 'number' => 1]);
$admin_id = !empty($admins) ? $admins[0]->ID : 1;

foreach ($chapters as $index => $chap) {
    $chap_title = isset($chap['title']) ? sanitize_text_field($chap['title']) : ('Chương ' . ($index + 1));
    $chap_content = isset($chap['content']) ? wp_kses_post($chap['content']) : '';
    
    $new_chap_id = wp_insert_post([
        'post_title'   => $chap_title,
        'post_content' => $chap_content,
        'post_status'  => 'publish',
        'post_type'    => 'chuong',
        'post_author'  => $admin_id,
        'menu_order'   => $index + 1 // Đảm bảo thứ tự chương chuẩn
    ]);
    
    if (!is_wp_error($new_chap_id)) {
        update_post_meta($new_chap_id, '_truyen_id', $story_id);
        $published_chapters[] = [
            'id' => $new_chap_id,
            'title' => $chap_title
        ];
    }
}

// 4. Clear LiteSpeed Cache
if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

echo json_encode([
    'success' => true,
    'story_id' => $story_id,
    'title' => $title,
    'author' => $author,
    'deleted_old_chapters' => $deleted_count,
    'chapters_count' => count($published_chapters),
    'seo_updated' => !empty($seo)
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
