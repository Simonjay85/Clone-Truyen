<?php
define('WP_USE_THEMES', false);
require_once('../../../wp-load.php');

header('Content-Type: text/plain; charset=UTF-8');

echo "=== INSPECTING TRUYEN POSTS ===\n\n";

$q = new WP_Query([
    'post_type' => 'truyen',
    'posts_per_page' => 15,
    'orderby' => 'comment_count'
]);

if (!$q->have_posts()) {
    echo "No posts found.\n";
    exit;
}

while ($q->have_posts()) {
    $q->the_post();
    $id = get_the_ID();
    $title = get_the_title();
    $thumb_id = get_post_thumbnail_id($id);
    $thumb_url_ml = get_the_post_thumbnail_url($id, 'medium_large');
    $thumb_url_full = get_the_post_thumbnail_url($id, 'full');
    
    echo "ID: $id\n";
    echo "Title: $title\n";
    echo "Thumbnail ID: $thumb_id\n";
    echo "Thumbnail (medium_large): " . ($thumb_url_ml ?: 'NONE') . "\n";
    echo "Thumbnail (full): " . ($thumb_url_full ?: 'NONE') . "\n";
    
    if ($thumb_id) {
        $meta = wp_get_attachment_metadata($thumb_id);
        echo "Attachment Meta: " . json_encode($meta) . "\n";
        $attached_file = get_post_meta($thumb_id, '_wp_attached_file', true);
        echo "Attached File Path: " . ($attached_file ?: 'NONE') . "\n";
        
        $upload_dir = wp_upload_dir();
        $full_path = $upload_dir['basedir'] . '/' . $attached_file;
        echo "File Exists locally on server: " . (file_exists($full_path) ? 'YES' : 'NO') . "\n";
        echo "File Size: " . (file_exists($full_path) ? filesize($full_path) . " bytes" : 'N/A') . "\n";
    }
    echo "---------------------------------\n";
}
wp_reset_postdata();
