<?php
require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

$covers_data = [
    1736 => 'https://files.manuscdn.com/user_upload_by_module/session_file/310519663588147362/AGVxbjHqtPVutueI.png',
    1648 => 'https://files.manuscdn.com/user_upload_by_module/session_file/310519663588147362/BJMuZEZXWiTLdKUE.png',
    1649 => 'https://files.manuscdn.com/user_upload_by_module/session_file/310519663588147362/BAdUCpZSBUBxyVAn.png',
    1650 => 'https://files.manuscdn.com/user_upload_by_module/session_file/310519663588147362/aeTEhwURNYHypLNK.png',
    1651 => 'https://files.manuscdn.com/user_upload_by_module/session_file/310519663588147362/JLdtGIGxnceyjxDe.png',
    1653 => 'https://files.manuscdn.com/user_upload_by_module/session_file/310519663588147362/nvghkuGTYcqpWjtW.png',
    1595 => 'https://files.manuscdn.com/user_upload_by_module/session_file/310519663588147362/dSojQDSngfJGUgJc.png',
    1593 => 'https://files.manuscdn.com/user_upload_by_module/session_file/310519663588147362/QMaXbFjkuFeKKWtZ.png',
    1591 => 'https://files.manuscdn.com/user_upload_by_module/session_file/310519663588147362/SXwvwYmDtXHbyuUw.png',
    1592 => 'https://files.manuscdn.com/user_upload_by_module/session_file/310519663588147362/aqgNLnLIiLPSKQCq.png',
];

$results = [];
foreach ($covers_data as $post_id => $url) {
    $tmp = download_url($url, 60);
    if (is_wp_error($tmp)) {
        $results[] = "Error downloading for ID $post_id: " . $tmp->get_error_message();
        continue;
    }

    $file_array = [
        'name' => 'cover-' . $post_id . '.png',
        'tmp_name' => $tmp
    ];

    $attach_id = media_handle_sideload($file_array, $post_id);
    
    if (!is_wp_error($attach_id)) {
        set_post_thumbnail($post_id, $attach_id);
        $results[] = "Success for ID $post_id";
    } else {
        @unlink($tmp);
        $results[] = "Error setting thumbnail for ID $post_id: " . $attach_id->get_error_message();
    }
}

echo implode("\n", $results);
?>
