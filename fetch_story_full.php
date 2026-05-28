<?php
/**
 * fetch_story_full.php
 * Fetches complete story with all chapter content for evaluation and editing.
 */
ini_set('display_errors', 0);
ini_set('max_execution_time', 120);
header('Content-Type: application/json; charset=utf-8');

$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401);
    echo json_encode(['error' => 'Unauthorized']);
    exit;
}

require_once('wp-load.php');
global $wpdb;

$story_id = intval($input['story_id'] ?? 0);
if ($story_id <= 0) {
    http_response_code(400);
    echo json_encode(['error' => 'Missing story_id']);
    exit;
}

$story = get_post($story_id);
if (!$story || $story->post_type !== 'truyen') {
    http_response_code(404);
    echo json_encode(['error' => 'Story not found']);
    exit;
}

// Get chapters
$chapters = $wpdb->get_results($wpdb->prepare(
    "SELECT p.ID, p.post_title, p.post_content, p.post_date, p.menu_order
     FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
     WHERE p.post_type = 'chuong' AND p.post_status = 'publish'
     AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
     ORDER BY p.menu_order ASC, p.post_date ASC",
    (string)$story_id
));

$chapter_list = [];
foreach ($chapters as $ch) {
    $plain_text = wp_strip_all_tags($ch->post_content);
    $word_count = mb_strlen(preg_replace('/\s+/', ' ', $plain_text), 'UTF-8');
    $chapter_list[] = [
        'wp_id' => $ch->ID,
        'title' => $ch->post_title,
        'content' => $ch->post_content,
        'plain_text' => $plain_text,
        'word_count' => $word_count,
        'menu_order' => intval($ch->menu_order),
        'date' => $ch->post_date
    ];
}

// Get author
$author = get_post_meta($story_id, 'truyen_tacgia', true);
if (empty($author)) $author = 'Đang cập nhật';

// Get genre
$terms = wp_get_post_terms($story_id, 'the_loai');
$genre = '';
if (!is_wp_error($terms) && !empty($terms)) {
    $genre = $terms[0]->name;
}

echo json_encode([
    'story_id' => $story_id,
    'title' => $story->post_title,
    'slug' => $story->post_name,
    'intro' => $story->post_content,
    'author' => $author,
    'genre' => $genre,
    'status' => $story->post_status,
    'total_chapters' => count($chapter_list),
    'chapters' => $chapter_list
], JSON_UNESCAPED_UNICODE);
?>
