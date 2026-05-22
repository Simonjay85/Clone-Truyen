<?php
/**
 * Custom Update Story API for Sen Tea Story V13
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

// Authenticate as Administrator
$admins = get_users(['role' => 'administrator', 'number' => 1]);
if (empty($admins)) {
    http_response_code(500);
    echo json_encode(['error' => 'Không tìm thấy tài khoản Administrator nào']);
    exit;
}
$admin_id = $admins[0]->ID;
wp_set_current_user($admin_id);

$story_id = isset($input['story_id']) ? intval($input['story_id']) : 0;
$title = isset($input['title']) ? sanitize_text_field($input['title']) : '';
$intro = isset($input['intro']) ? wp_kses_post($input['intro']) : '';
$chapters = isset($input['chapters']) ? $input['chapters'] : [];
$seo = isset($input['seo']) ? $input['seo'] : [];
$genres = isset($input['genres']) ? $input['genres'] : [];
$comments = isset($input['comments']) ? $input['comments'] : [];
$alt_text = isset($input['alt_text']) ? sanitize_text_field($input['alt_text']) : '';

if (empty($story_id) || empty($title) || empty($intro) || empty($chapters)) {
    http_response_code(400);
    echo json_encode(['error' => 'Thiếu thông tin ID truyện, tiêu đề, mô tả hoặc danh sách chương!']);
    exit;
}

// 1. Check if post exists and is of type 'truyen'
$post = get_post($story_id);
if (!$post || $post->post_type !== 'truyen') {
    http_response_code(404);
    echo json_encode(['error' => 'Không tìm thấy truyện với ID: ' . $story_id]);
    exit;
}

// 2. Delete all existing chapters for this story
$chaps = get_posts([
    'post_type' => 'chuong',
    'meta_key' => '_truyen_id',
    'meta_value' => $story_id,
    'posts_per_page' => -1
]);
$deleted_count = 0;
foreach ($chaps as $c) {
    wp_delete_post($c->ID, true);
    $deleted_count++;
}

// 3. Update the main story title and content (Intro)
wp_update_post([
    'ID'           => $story_id,
    'post_title'   => $title,
    'post_content' => $intro,
    'post_status'  => 'publish'
]);

// 4. Update SEO RankMath and other metadata
if (!empty($seo)) {
    $focus_keyword = isset($seo['focus_keyword']) ? sanitize_text_field($seo['focus_keyword']) : '';
    $seo_title = isset($seo['seo_title']) ? sanitize_text_field($seo['seo_title']) : '';
    $seo_description = isset($seo['seo_description']) ? sanitize_text_field($seo['seo_description']) : '';
    
    if (!empty($focus_keyword)) {
        update_post_meta($story_id, '_rank_math_focus_keyword', $focus_keyword);
        update_post_meta($story_id, 'rank_math_focus_keyword', $focus_keyword);
    }
    if (!empty($seo_title)) {
        update_post_meta($story_id, '_rank_math_title', $seo_title);
        update_post_meta($story_id, 'rank_math_title', $seo_title);
    }
    if (!empty($seo_description)) {
        update_post_meta($story_id, '_rank_math_description', $seo_description);
        update_post_meta($story_id, 'rank_math_description', $seo_description);
    }
    update_post_meta($story_id, 'rank_math_rich_snippet', 'article');
}

// 5. Update Taxonomy ('the_loai')
if (!empty($genres)) {
    wp_set_post_terms($story_id, $genres, 'the_loai');
}

// 6. Update Featured Image Alt Text
$thumb_id = get_post_thumbnail_id($story_id);
if ($thumb_id && !empty($alt_text)) {
    update_post_meta($thumb_id, '_wp_attachment_image_alt', $alt_text);
}

// 7. Insert new chapters
$published_chapters = [];
foreach ($chapters as $index => $chap) {
    $chap_title = isset($chap['title']) ? sanitize_text_field($chap['title']) : ('Chương ' . ($index + 1));
    $chap_content = isset($chap['content']) ? wp_kses_post($chap['content']) : '';
    
    $chap_id = wp_insert_post([
        'post_title'   => $chap_title,
        'post_content' => $chap_content,
        'post_status'  => 'publish',
        'post_type'    => 'chuong',
        'post_author'  => $admin_id,
        'menu_order'   => $index + 1
    ]);
    
    if (!is_wp_error($chap_id)) {
        update_post_meta($chap_id, '_truyen_id', $story_id);
        update_post_meta($chap_id, '_chap_order', $index + 1);
        $published_chapters[] = [
            'id' => $chap_id,
            'title' => $chap_title
        ];
    }
}

// 8. Seed comments
$inserted_comments_count = 0;
if (!empty($comments)) {
    foreach ($comments as $comment) {
        $c_author = isset($comment['comment_author']) ? sanitize_text_field($comment['comment_author']) : 'Ẩn danh';
        $c_content = isset($comment['comment_content']) ? wp_strip_all_tags($comment['comment_content']) : '';
        
        if (empty($c_content)) continue;
        
        // Avoid duplicate comments
        $existing = get_comments([
            'post_id' => $story_id,
            'search'  => $c_content
        ]);
        
        if (empty($existing)) {
            $commentdata = [
                'comment_post_ID'      => $story_id,
                'comment_author'       => $c_author,
                'comment_content'      => $c_content,
                'comment_approved'     => 1,
                'comment_type'         => 'comment',
                'comment_date'         => current_time('mysql'),
                'comment_date_gmt'     => current_time('mysql', 1)
            ];
            wp_insert_comment($commentdata);
            $inserted_comments_count++;
        }
    }
}

// 9. Purge cache (LSCache)
if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

echo json_encode([
    'success' => true,
    'story_id' => $story_id,
    'title' => $title,
    'deleted_chapters_count' => $deleted_count,
    'chapters_count' => count($published_chapters),
    'comments_seeded' => $inserted_comments_count,
    'thumb_id' => $thumb_id,
    'thumb_alt_updated' => !empty($alt_text) && $thumb_id ? true : false,
    'chapters' => $published_chapters
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
