<?php
require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

$temp_dir = ABSPATH . 'wp-content/uploads/temp_covers/';
if (!is_dir($temp_dir)) {
    echo "Temp directory not found.";
    exit;
}

$files = glob($temp_dir . '*.png');
$results = [];

foreach ($files as $file) {
    $post_id = basename($file, '.png');
    if (is_numeric($post_id)) {
        // Check if post exists
        if (get_post_status($post_id)) {
            // Sideload image
            $file_array = [
                'name' => basename($file),
                'tmp_name' => $file
            ];
            
            // We need to copy the file because media_handle_sideload might move it
            $copy_path = $temp_dir . 'copy_' . basename($file);
            copy($file, $copy_path);
            $file_array['tmp_name'] = $copy_path;

            $thumb_id = media_handle_sideload($file_array, $post_id);
            
            if (!is_wp_error($thumb_id)) {
                set_post_thumbnail($post_id, $thumb_id);
                $results[] = "Success for ID $post_id";
                // Delete original temp file
                unlink($file);
            } else {
                $results[] = "Error for ID $post_id: " . $thumb_id->get_error_message();
                if (file_exists($copy_path)) unlink($copy_path);
            }
        } else {
            $results[] = "Post ID $post_id not found.";
        }
    }
}

echo implode("\n", $results);
?>
