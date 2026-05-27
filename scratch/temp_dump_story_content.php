<?php
/**
 * Temporary Story Content Dump Script
 */
ini_set('display_errors', 1);
error_reporting(E_ALL);
header('Content-Type: application/json');

require_once('wp-load.php');

$post_id = 3940; // Target story ID

$post = get_post($post_id);
if (!$post) {
    echo json_encode(['error' => 'Story not found']);
    exit;
}

// Get all chapters
$chaps_query = new WP_Query([
    'post_type' => 'chuong',
    'posts_per_page' => -1,
    'meta_query' => [
        [
            'key' => '_truyen_id',
            'value' => $post_id,
            'compare' => '='
        ]
    ],
    'orderby' => 'date',
    'order' => 'ASC'
]);

$chapters = [];
if ($chaps_query->have_posts()) {
    while ($chaps_query->have_posts()) {
        $chaps_query->the_post();
        $chapters[] = [
            'id' => get_the_ID(),
            'title' => get_the_title(),
            'content' => get_the_content(),
            'date' => get_the_date('Y-m-d H:i:s')
        ];
    }
}
wp_reset_postdata();

$result = [
    'story' => [
        'id' => $post->ID,
        'title' => $post->post_title,
        'excerpt' => $post->post_excerpt,
        'content' => $post->post_content
    ],
    'chapters' => $chapters
];

echo json_encode($result, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
?>
