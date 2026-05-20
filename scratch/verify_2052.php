<?php
/**
 * Verification Script for Story 2052 - Doctieuthuyet.com
 */
require_once('wp-load.php');
header('Content-Type: application/json; charset=utf-8');

$truyen_id = 2052;

// Check parent story
$story = get_post($truyen_id);
if (!$story) {
    echo json_encode(['error' => 'Story not found'], JSON_PRETTY_PRINT);
    exit;
}

$chapters = get_posts([
    'post_type'      => 'chuong',
    'posts_per_page' => -1,
    'meta_key'       => '_truyen_id',
    'meta_value'     => $truyen_id,
    'orderby'        => 'ID', 
    'order'          => 'ASC'
]);

$response = [
    'story' => [
        'id' => $story->ID,
        'title' => $story->post_title,
        'status' => get_post_meta($truyen_id, 'truyen_status', true),
    ],
    'count' => count($chapters),
    'chapters' => []
];

foreach ($chapters as $index => $c) {
    $response['chapters'][] = [
        'index' => $index + 1,
        'id' => $c->ID,
        'title' => $c->post_title,
        'slug' => $c->post_name,
        'word_count' => str_word_count(strip_tags($c->post_content))
    ];
}

echo json_encode($response, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
