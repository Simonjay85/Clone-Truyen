<?php
/**
 * update_cover_3724.php
 * Sets the newly generated and framed image as the featured image for post 3724.
 */

// Load WordPress context. We place this file in the theme folder: wp-content/themes/tehi-theme/
require_once('../../../wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

$post_id = 3724;
$local_file_name = 'temp_cover_3724.png';
$file_path = __DIR__ . '/' . $local_file_name;

if (!file_exists($file_path)) {
    die("Error: File not found at " . $file_path);
}

// Prepare file array for media_handle_sideload
$file_array = array(
    'name' => 'cover-3724-premium.png',
    'tmp_name' => $file_path
);

// Copy file because sideload will move it
$copy_path = __DIR__ . '/copy_' . $local_file_name;
if (!copy($file_path, $copy_path)) {
    die("Error: Failed to create a copy of the cover file.");
}
$file_array['tmp_name'] = $copy_path;

// Sideload the image and attach it to post 3724
$attach_id = media_handle_sideload($file_array, $post_id);

if (is_wp_error($attach_id)) {
    @unlink($copy_path);
    die("Error sideloading media: " . $attach_id->get_error_message());
}

// Set it as post featured image
$success = set_post_thumbnail($post_id, $attach_id);

if ($success) {
    echo "SUCCESS: Featured image set to Attachment ID " . $attach_id . " for Post 3724!\n";
} else {
    echo "FAILED: sideloaded successfully as ID " . $attach_id . " but failed to set as thumbnail for Post 3724.\n";
}

// Cleanup copy just in case
if (file_exists($copy_path)) {
    @unlink($copy_path);
}
?>
