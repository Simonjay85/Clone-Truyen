<?php
require_once('wp-load.php');
$q2 = new WP_Query(['post_type' => 'truyen', 'posts_per_page' => 4, 'orderby' => 'comment_count', 'no_found_rows' => true]);
$results = [];
while ($q2->have_posts()) {
    $q2->the_post();
    $id = get_the_ID();
    $thumb_id = get_post_thumbnail_id($id);
    $meta = wp_get_attachment_metadata($thumb_id);
    $file = get_attached_file($thumb_id);
    $results[] = [
        'id' => $id,
        'title' => get_the_title(),
        'thumb_id' => $thumb_id,
        'attached_file' => $file,
        'file_exists' => $file ? file_exists($file) : false,
        'filesize' => ($file && file_exists($file)) ? filesize($file) : 0,
        'meta' => $meta,
    ];
}
wp_reset_postdata();
header('Content-Type: application/json');
echo json_encode($results, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
