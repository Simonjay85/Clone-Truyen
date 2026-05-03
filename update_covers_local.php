<?php
require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

$covers_data = [
    1736 => '1736_1200x800.png',
    1648 => '1648_1200x800.png',
    1649 => '1649_1200x800.png',
    1650 => '1650_1200x800.png',
    1651 => '1651_1200x800.png',
    1653 => '1653_1200x800.png',
    1595 => '1595_1200x800.png',
    1593 => '1593_1200x800.png',
    1591 => '1591_1200x800.png',
    1592 => '1592_1200x800.png',
];

$results = [];
foreach ($covers_data as $post_id => $filename) {
    $filepath = ABSPATH . $filename;
    if (file_exists($filepath)) {
        $file_array = [
            'name' => $filename,
            'tmp_name' => $filepath
        ];
        
        // Copy to a temp file because media_handle_sideload moves it
        $tmp_copy = ABSPATH . 'tmp_' . $filename;
        copy($filepath, $tmp_copy);
        $file_array['tmp_name'] = $tmp_copy;

        $attach_id = media_handle_sideload($file_array, $post_id);
        
        if (!is_wp_error($attach_id)) {
            set_post_thumbnail($post_id, $attach_id);
            $results[] = "Success for ID $post_id";
            unlink($filepath); // Delete the original uploaded file
        } else {
            $results[] = "Error for ID $post_id: " . $attach_id->get_error_message();
            if (file_exists($tmp_copy)) unlink($tmp_copy);
        }
    } else {
        $results[] = "File not found for ID $post_id: $filename";
    }
}

echo implode("\n", $results);
?>
