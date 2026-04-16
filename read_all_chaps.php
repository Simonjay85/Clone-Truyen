<?php
require_once('wp-load.php');

$story = get_page_by_path('de-vuong-so-an-minh-ong-lao-an-bam-va-mat-toan-cau', OBJECT, 'truyen');
if ($story) {
    $chapters = get_posts([
        'post_type' => 'chuong',
        'meta_key' => '_truyen_id',
        'meta_value' => $story->ID,
        'posts_per_page' => -1,
        'orderby' => 'date',
        'order' => 'ASC'
    ]);
    
    foreach($chapters as $c) {
        echo "=== " . $c->post_title . " ===\n";
        echo mb_substr(wp_strip_all_tags($c->post_content), 0, 500) . "...\n\n";
    }
} else {
    echo "Không tìm thấy truyện.";
}
