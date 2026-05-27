<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);
header('Content-Type: application/json; charset=utf-8');

require_once('wp-load.php');

$ids = isset($_GET['ids']) ? array_map('intval', explode(',', sanitize_text_field($_GET['ids']))) : [];
if (empty($ids)) {
    echo json_encode(['error' => 'Missing ids']);
    exit;
}

$results = [];
foreach ($ids as $story_id) {
    $story_post = get_post($story_id);
    if (!$story_post || $story_post->post_type !== 'truyen') {
        $results[] = ['id' => $story_id, 'error' => 'Story not found'];
        continue;
    }

    $chapter_posts = get_posts([
        'post_type' => 'chuong',
        'posts_per_page' => -1,
        'meta_key' => '_truyen_id',
        'meta_value' => $story_id,
        'orderby' => 'date',
        'order' => 'ASC',
    ]);

    $chapters = [];
    foreach ($chapter_posts as $chapter_post) {
        $chapters[] = [
            'id' => $chapter_post->ID,
            'title' => $chapter_post->post_title,
            'slug' => $chapter_post->post_name,
            'content' => $chapter_post->post_content,
            'date' => $chapter_post->post_date,
            'menu_order' => $chapter_post->menu_order,
        ];
    }

    $results[] = [
        'story' => [
            'id' => $story_post->ID,
            'title' => $story_post->post_title,
            'slug' => $story_post->post_name,
            'excerpt' => $story_post->post_excerpt,
            'content' => $story_post->post_content,
            'thumbnail_id' => get_post_thumbnail_id($story_id),
            'thumbnail_url' => get_the_post_thumbnail_url($story_id, 'full'),
            'rank_math_title' => get_post_meta($story_id, 'rank_math_title', true),
            'rank_math_description' => get_post_meta($story_id, 'rank_math_description', true),
        ],
        'chapters' => $chapters,
    ];
}

echo json_encode($results, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
?>
