<?php
/**
 * fix_3940.php - Xóa đoạn văn lặp lại trong chương 1 của truyện 3940
 */
ini_set('display_errors', 0);
ini_set('max_execution_time', 60);
header('Content-Type: application/json');

$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401); echo json_encode(['error'=>'Unauthorized']); exit;
}
require_once('wp-load.php');

$slug = 'chuong-1-truc-xuat-khoi-vien-phoi-quoc-te';
$post = get_page_by_path($slug, OBJECT, 'chuong');
if (!$post) {
    echo json_encode(['error' => 'Chapter not found: ' . $slug]); exit;
}

$content = $post->post_content;
$original_len = strlen($content);

// Tách thành các đoạn theo thẻ </p><p> hoặc newline
$paragraphs = preg_split('/<\/p>\s*<p[^>]*>/i', $content);

$seen_normalized = [];
$unique_paragraphs = [];
$removed = 0;

foreach ($paragraphs as $i => $para) {
    // Strip all tags to get plain text for comparison
    $plain = wp_strip_all_tags($para);
    $plain = trim(preg_replace('/\s+/', ' ', $plain));

    if (mb_strlen($plain) < 40) {
        // Đoạn ngắn < 40 ký tự: giữ nguyên
        $unique_paragraphs[] = $para;
        continue;
    }

    // Dùng 120 ký tự đầu làm key so sánh
    $key = mb_strtolower(mb_substr($plain, 0, 120));

    if (!isset($seen_normalized[$key])) {
        $seen_normalized[$key] = true;
        $unique_paragraphs[] = $para;
    } else {
        $removed++;
    }
}

// Ráp lại với thẻ <p>
if (count($unique_paragraphs) > 0) {
    // Đảm bảo đoạn đầu có mở <p> và đoạn cuối có đóng </p>
    $fixed = implode('</p><p>', $unique_paragraphs);

    // Nếu content gốc bắt đầu với <p>, đảm bảo output cũng vậy
    if (preg_match('/^\s*<p/i', $content) && !preg_match('/^\s*<p/i', $fixed)) {
        $fixed = '<p>' . $fixed;
    }
    if (preg_match('/<\/p>\s*$/i', $content) && !preg_match('/<\/p>\s*$/i', $fixed)) {
        $fixed = $fixed . '</p>';
    }
} else {
    $fixed = $content;
}

$new_len = strlen($fixed);
$changed = ($fixed !== $content) && $removed > 0;

if ($changed) {
    wp_update_post(['ID' => $post->ID, 'post_content' => wp_kses_post($fixed)]);
    if (function_exists('litespeed_purge_post')) litespeed_purge_post($post->ID);
    elseif (function_exists('litespeed_purge_all')) litespeed_purge_all();
}

echo json_encode([
    'id'           => $post->ID,
    'slug'         => $slug,
    'changed'      => $changed,
    'removed_dupes'=> $removed,
    'original_len' => $original_len,
    'new_len'      => $new_len,
    'paragraphs_kept' => count($unique_paragraphs),
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
