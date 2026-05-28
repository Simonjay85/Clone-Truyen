<?php
require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

$token = $_POST['secret_token'] ?? '';
if ($token !== 'ZEN_TRUYEN_2026_BYPASS') {
    wp_send_json_error(['message' => 'Invalid token'], 403);
}

$post_id = intval($_POST['post_id'] ?? 0);
$cover_local_filename = sanitize_file_name($_POST['cover_local_filename'] ?? '');

if (!$post_id || !$cover_local_filename) {
    wp_send_json_error(['message' => 'Missing post_id or cover_local_filename'], 400);
}

$local_path = ABSPATH . 'wp-content/uploads/' . $cover_local_filename;
if (!file_exists($local_path)) {
    wp_send_json_error(['message' => 'Cover file not found', 'path' => $local_path], 404);
}

$tmp = tempnam(get_temp_dir(), 'cover');
if (!copy($local_path, $tmp)) {
    wp_send_json_error(['message' => 'Could not copy cover to temp'], 500);
}

$file_array = [
    'name' => 'cover-' . $post_id . '-short-title-' . rand(100, 999) . '.png',
    'tmp_name' => $tmp,
];

$attach_id = media_handle_sideload($file_array, $post_id);
if (is_wp_error($attach_id)) {
    @unlink($tmp);
    wp_send_json_error(['message' => $attach_id->get_error_message()], 500);
}

set_post_thumbnail($post_id, $attach_id);
update_post_meta($attach_id, '_wp_attachment_image_alt', get_the_title($post_id));
@unlink($local_path);

wp_send_json_success([
    'post_id' => $post_id,
    'attachment_id' => $attach_id,
    'thumbnail' => get_the_post_thumbnail_url($post_id, 'large'),
]);
