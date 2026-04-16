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
                'chapters' => count($chapters)
            );
        }
    }
    wp_reset_postdata();
}

$output = "Danh sách Truyện bị lỗi tìm thấy:\n";
foreach ($buggy_stories as $story) {
    $output .= "- [ID: {$story['id']}] {$story['title']} (Slug: {$story['slug']}) | Chương: {$story['chapters']} | Lý do: {$story['reason']}\n";
}

echo $output;
