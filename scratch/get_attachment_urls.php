<?php
require_once('wp-load.php');
header('Content-Type: application/json');

$post_ids = [7389, 7492, 7480];
$results = [];

foreach ($post_ids as $pid) {
    $title = get_the_title($pid);
    $thumb_id = get_post_thumbnail_id($pid);
    $thumb_url = wp_get_attachment_url($thumb_id);
    $results[$pid] = [
        'title' => $title,
        'thumb_id' => $thumb_id,
        'thumb_url' => $thumb_url
    ];
}

echo json_encode($results, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>
