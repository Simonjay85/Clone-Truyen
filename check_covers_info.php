<?php
/**
 * Query detailed cover thumbnail information for the three specific post IDs.
 */
ini_set('display_errors', 1);
error_reporting(E_ALL);
header('Content-Type: application/json');

require_once('wp-load.php');

$post_ids = [3920, 3930, 3940];
$results = [];

foreach ($post_ids as $id) {
    $results[$id] = [
        'title' => get_the_title($id),
        'has_thumb' => has_post_thumbnail($id),
        'thumb_url' => get_the_post_thumbnail_url($id, 'medium_large'),
        'thumb_url_full' => get_the_post_thumbnail_url($id, 'full'),
        'custom_fields' => get_post_custom($id)
    ];
}

echo json_encode($results, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
