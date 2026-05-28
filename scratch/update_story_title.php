<?php
require_once('wp-load.php');

$story_id = 5056;
$new_title = 'Sếp Cũ Cướp Code Gọi Vốn 5 Triệu Đô, Tôi Trùng Sinh Dùng Git Log Vả Sập Sân Khấu';

$story = get_post($story_id);
if ($story && $story->post_type === 'truyen') {
    wp_update_post([
        'ID'         => $story_id,
        'post_title' => $new_title,
        'post_name'  => sanitize_title($new_title)
    ]);
    
    // Also, clear rewrite rules just in case
    flush_rewrite_rules();
    
    echo "TITLE_UPDATE_SUCCESS: Updated ID $story_id to title '$new_title'\n";
} else {
    echo "ERROR: Story ID $story_id not found or not post_type=truyen\n";
}
?>
