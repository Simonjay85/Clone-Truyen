<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);
header('Content-Type: application/json');

require_once('wp-load.php');

$ids = isset($_GET['ids']) ? array_map('intval', explode(',', sanitize_text_field($_GET['ids']))) : [];
if (empty($ids)) {
    echo json_encode(['error' => 'Missing ids']);
    exit;
}

$results = [];
foreach ($ids as $post_id) {
    $post = get_post($post_id);
    if (!$post) {
        $results[] = ['id' => $post_id, 'error' => 'Story not found'];
        continue;
    }

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

    $results[] = [
        'story' => [
            'id' => $post->ID,
            'title' => $post->post_title,
            'slug' => $post->post_name,
            'excerpt' => $post->post_excerpt,
            'content' => $post->post_content,
            'thumbnail_id' => get_post_thumbnail_id($post_id),
            'thumbnail_url' => get_the_post_thumbnail_url($post_id, 'full'),
        ],
        'chapters' => $chapters,
    ];
}

echo json_encode($results, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
?>
