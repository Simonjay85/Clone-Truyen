<?php
/**
 * fix_chapter_content.php
 * Cập nhật nội dung một chương đơn lẻ hoặc lấy danh sách chương của truyện
 * Secret token: ZEN_TRUYEN_2026_BYPASS
 */

ini_set('display_errors', 0);
ini_set('max_execution_time', 120);
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    http_response_code(405);
    echo json_encode(['error' => 'POST only']);
    exit;
}

$raw_input = file_get_contents('php://input');
$input = json_decode($raw_input, true);

if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401);
    echo json_encode(['error' => 'Unauthorized']);
    exit;
}

require_once('wp-load.php');

$action = isset($input['action']) ? $input['action'] : 'get_chapters';

// ─── ACTION: get_chapters — lấy danh sách chương của 1 truyện ───────────────
if ($action === 'get_chapters') {
    $truyen_id = isset($input['truyen_id']) ? intval($input['truyen_id']) : 0;
    if (!$truyen_id) {
        http_response_code(400);
        echo json_encode(['error' => 'Thiếu truyen_id']);
        exit;
    }

    $chapters = get_posts([
        'post_type'      => 'chuong',
        'posts_per_page' => -1,
        'orderby'        => 'ID',
        'order'          => 'ASC',
        'meta_query'     => [[
            'key'     => '_truyen_id',
            'value'   => $truyen_id,
            'compare' => '='
        ]]
    ]);

    $result = [];
    foreach ($chapters as $ch) {
        $content = $ch->post_content;
        $result[] = [
            'id'              => $ch->ID,
            'title'           => $ch->post_title,
            'content_length'  => strlen($content),
            'content_preview' => mb_substr(wp_strip_all_tags($content), 0, 200),
            'content_hash'    => md5(mb_substr(wp_strip_all_tags($content), 0, 300)),
        ];
    }

    echo json_encode([
        'truyen_id' => $truyen_id,
        'count'     => count($result),
        'chapters'  => $result
    ], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
    exit;
}

// ─── ACTION: update_chapter — cập nhật nội dung chương ──────────────────────
if ($action === 'update_chapter') {
    $chapter_id = isset($input['chapter_id']) ? intval($input['chapter_id']) : 0;
    $new_content = isset($input['content']) ? $input['content'] : '';
    $new_title   = isset($input['title']) ? sanitize_text_field($input['title']) : '';

    if (!$chapter_id || empty($new_content)) {
        http_response_code(400);
        echo json_encode(['error' => 'Thiếu chapter_id hoặc content']);
        exit;
    }

    $post = get_post($chapter_id);
    if (!$post || $post->post_type !== 'chuong') {
        http_response_code(404);
        echo json_encode(['error' => 'Không tìm thấy chương ID: ' . $chapter_id]);
        exit;
    }

    $update_data = [
        'ID'           => $chapter_id,
        'post_content' => wp_kses_post($new_content),
    ];
    if ($new_title) {
        $update_data['post_title'] = $new_title;
    }

    $res = wp_update_post($update_data);
    if (is_wp_error($res)) {
        http_response_code(500);
        echo json_encode(['error' => $res->get_error_message()]);
        exit;
    }

    // Clear cache
    if (function_exists('litespeed_purge_post')) {
        litespeed_purge_post($chapter_id);
    } elseif (function_exists('litespeed_purge_all')) {
        litespeed_purge_all();
    }

    echo json_encode([
        'success'    => true,
        'chapter_id' => $chapter_id,
        'title'      => $post->post_title,
        'length'     => strlen($new_content),
    ], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
    exit;
}

http_response_code(400);
echo json_encode(['error' => 'action không hợp lệ. Dùng: get_chapters | update_chapter']);
?>
