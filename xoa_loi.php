<?php
require_once('wp-load.php');

$args = array(
    'post_type'      => 'truyen',
    'post_status'    => 'any',
    'posts_per_page' => -1,
);
$query = new WP_Query($args);
$buggy_stories = array();

if ($query->have_posts()) {
    while ($query->have_posts()) {
        $query->the_post();
        $id = get_the_ID();
        $title = get_the_title();
        $excerpt = get_the_excerpt();
        $slug = get_post_field('post_name', $id);
        
        $is_buggy = false;
        $reason = "";
        
        // Condition 1: Empty title or very generic wait titles
        if (trim($title) === "" || $title === "DTT" || str_contains($title, "Truyện Chờ Tên") || str_contains($title, "Truyện chờ phân tích")) {
            $is_buggy = true;
            $reason = "Lỗi Tiêu đề trống/tạm";
        }
        
        // Condition 2: Title exactly mathces post ID string (e.g. 580)
        global $post;
        if (trim($title) === "" && trim($slug) === (string)$id) {
            $is_buggy = true;
            $reason = "Lỗi không có Title (slug trùng ID)";
        }

        // Condition 3: Excerpt is the HTML fallback
        if (str_contains($excerpt, "1. Bối cảnh Thế Giới 2. Nhân Vật") || trim($excerpt) === "1. Bối cảnh Thế Giới 2. Nhân Vật 3. Kịch Bản") {
            $is_buggy = true;
            $reason = "Lỗi Văn án rỗng (Fallback HTML)";
        }
        
        // Action: Delete if '?delete=1'
        if ($is_buggy) {
            // Count chapters
            $chapters = get_posts(array(
                'post_type' => 'chuong',
                'meta_key' => '_truyen_id',
                'meta_value' => $id,
                'posts_per_page' => -1,
                'fields' => 'ids'
            ));
            
            $buggy_stories[] = array(
                'id' => $id,
                'title' => $title,
                'slug' => $slug,
                'reason' => $reason,
                'chapters_count' => count($chapters),
                'chapter_ids' => $chapters
            );
        }
    }
    wp_reset_postdata();
}

$output = "Danh sách Truyện bị lỗi tìm thấy:\n";
foreach ($buggy_stories as $story) {
    if (isset($_GET['delete']) && $_GET['delete'] == '1') {
        // Delete all chapters
        foreach($story['chapter_ids'] as $cid) {
            wp_delete_post($cid, true);
        }
        // Delete story
        wp_delete_post($story['id'], true);
        $output .= "- ĐÃ XÓA VĨNH VIỄN: [ID: {$story['id']}] {$story['title']} (Slug: {$story['slug']}) | Xóa {$story['chapters_count']} chương | Lý do: {$story['reason']}\n";
    } else {
        $output .= "- PHÁT HIỆN LỖI: [ID: {$story['id']}] {$story['title']} (Slug: {$story['slug']}) | Chương: {$story['chapters_count']} | Lý do: {$story['reason']}\n";
    }
}

// Clean up the queue from buggy entries
if (isset($_GET['delete']) && $_GET['delete'] == '1') {
    $config = get_option('temply_auto_pilot_queue_config', false);
    if ($config && isset($config['queue'])) {
        foreach($config['queue'] as $i => $item) {
            if(isset($item['truyen_id'])) {
                foreach($buggy_stories as $story) {
                    if ($item['truyen_id'] == $story['id']) {
                        unset($config['queue'][$i]);
                    }
                }
            }
        }
        $config['queue'] = array_values($config['queue']); // re-index
        update_option('temply_auto_pilot_queue_config', $config);
        $output .= "\nĐã dọn dẹp Hàng đợi Auto Pilot!\n";
    }
}

echo nl2br($output);
