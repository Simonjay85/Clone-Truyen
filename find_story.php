<?php
require_once('wp-load.php');
$q = new WP_Query(['post_type' => 'truyen', 's' => 'Người Đưa Thư', 'posts_per_page' => 5]);
$results = [];
while ($q->have_posts()) {
    $q->the_post();
    $id = get_the_ID();
    $results[] = [
        'id' => $id,
        'title' => get_the_title(),
        'has_thumb' => has_post_thumbnail($id),
        'thumb_url' => get_the_post_thumbnail_url($id, 'medium_large'),
        'thumb_url_full' => get_the_post_thumbnail_url($id, 'full'),
    ];
}
wp_reset_postdata();
header('Content-Type: application/json');
echo json_encode($results, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
