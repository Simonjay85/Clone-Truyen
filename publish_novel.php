<?php
/**
 * Tệp Publish Novel API - Dành cho Clone Truyện App
 * Chức năng: Đăng tải trọn vẹn cả câu chuyện (Novel + Cover + All Chapters + Genre) một cách nguyên tử.
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
    echo json_encode(['error' => 'Từ chối truy cập: Sai Secret Token!']);
    exit;
}

require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

// Tự động lấy admin đầu tiên
$admins = get_users(['role' => 'administrator', 'number' => 1]);
if (empty($admins)) {
    http_response_code(500);
    echo json_encode(['error' => 'Không tìm thấy tài khoản Administrator nào']);
    exit;
}
$admin_id = $admins[0]->ID;
wp_set_current_user($admin_id);

$title = isset($input['title']) ? sanitize_text_field($input['title']) : '';
$intro = isset($input['intro']) ? wp_kses_post($input['intro']) : '';
$author = isset($input['author']) ? sanitize_text_field($input['author']) : 'Đang cập nhật';
$genre_name = isset($input['genre']) ? sanitize_text_field($input['genre']) : 'Sảng Văn';
$views = isset($input['views']) ? intval($input['views']) : rand(20000, 80000);
$cover_url = isset($input['cover_url']) ? esc_url_raw($input['cover_url']) : '';
$chapters = isset($input['chapters']) ? $input['chapters'] : [];

if (empty($title) || empty($intro) || empty($chapters)) {
    http_response_code(400);
    echo json_encode(['error' => 'Thiếu thông tin tiêu đề, mô tả hoặc danh sách chương!']);
    exit;
}

// 1. Tạo Truyện (post_type = truyen)
$story_id = wp_insert_post([
    'post_title'   => $title,
    'post_content' => $intro,
    'post_status'  => 'publish',
    'post_type'    => 'truyen',
    'post_author'  => $admin_id
]);

if (is_wp_error($story_id)) {
    http_response_code(500);
    echo json_encode(['error' => 'Lỗi khi tạo truyện: ' . $story_id->get_error_message()]);
    exit;
}

// Cập nhật meta cho Truyện
update_post_meta($story_id, 'truyen_tacgia', $author);
update_post_meta($story_id, '_views', $views);
update_post_meta($story_id, '_is_hot', 1);

// Thiết lập thể loại (taxonomy = the_loai)
$term = get_term_by('name', $genre_name, 'the_loai');
if (!$term && !is_wp_error($term)) {
    $new_term = wp_insert_term($genre_name, 'the_loai');
    if (!is_wp_error($new_term)) {
        wp_set_object_terms($story_id, intval($new_term['term_id']), 'the_loai');
    }
} else if ($term) {
    wp_set_object_terms($story_id, intval($term->term_id), 'the_loai');
}

// 2. Tải và cài đặt Ảnh bìa (Cover Image)
$cover_status = 'Không có ảnh bìa';
if (!empty($cover_url)) {
    $tmp = download_url($cover_url, 45);
    if (!is_wp_error($tmp)) {
        $file_array = array(
            'name' => 'cover-' . $story_id . '-' . rand(100, 999) . '.jpg',
            'tmp_name' => $tmp
        );
        $attach_id = media_handle_sideload($file_array, $story_id);
        if (!is_wp_error($attach_id)) {
            set_post_thumbnail($story_id, $attach_id);
            $cover_status = 'Tải ảnh bìa thành công!';
        } else {
            $cover_status = 'Lỗi media_handle_sideload: ' . $attach_id->get_error_message();
            @unlink($tmp);
        }
    } else {
        $cover_status = 'Lỗi tải ảnh bìa từ URL: ' . $tmp->get_error_message();
    }
}

// 3. Đăng các chương (post_type = chuong)
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

// 4. Xóa bộ nhớ đệm (Purge LSCache)
if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

echo json_encode([
    'success' => true,
    'story_id' => $story_id,
    'title' => $title,
    'author' => $author,
    'genre' => $genre_name,
    'cover_status' => $cover_status,
    'chapters_count' => count($published_chapters),
    'chapters' => $published_chapters
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
