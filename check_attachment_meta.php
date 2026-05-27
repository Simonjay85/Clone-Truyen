<?php
require_once('wp-load.php');
header('Content-Type: application/json');

// Find attachment by filename
global $wpdb;
$attachment = $wpdb->get_row("SELECT * FROM {$wpdb->posts} WHERE post_type = 'attachment' AND guid LIKE '%vo-than-bao-ve%' LIMIT 1");

if ($attachment) {
    $meta = wp_get_attachment_metadata($attachment->ID);
    $res = [
        'found' => true,
        'id' => $attachment->ID,
        'title' => $attachment->post_title,
        'guid' => $attachment->guid,
        'metadata' => $meta,
        'medium_url' => wp_get_attachment_image_url($attachment->ID, 'medium'),
        'medium_src' => wp_get_attachment_image_src($attachment->ID, 'medium')
    ];
} else {
    $res = [
        'found' => false,
        'message' => 'No attachment found with name containing vo-than-bao-ve'
    ];
}

echo json_encode($res, JSON_PRETTY_PRINT);
?>
