<?php
require_once('wp-load.php');

function print_story_info($slug) {
    echo "====================================\n";
    echo "Story Slug: $slug\n";
    
    $story = get_page_by_path($slug, OBJECT, 'truyen');
    if (!$story) {
        echo "Story not found.\n";
        return;
    }
    
    echo "Title: " . $story->post_title . "\n";
    echo "Created: " . $story->post_date . "\n\n";
    
    $chapters = get_posts([
        'post_type' => 'chuong',
        'meta_key' => '_truyen_id',
        'meta_value' => $story->ID,
        'posts_per_page' => -1,
        'orderby' => 'date',
        'order' => 'ASC'
    ]);
    
    echo "Total chapters: " . count($chapters) . "\n";
    
    $i = 1;
    foreach($chapters as $c) {
        echo "[$i] " . $c->post_title . " (Date: " . $c->post_date . ")\n";
        if ($i <= 2) {
            echo "Excerpt: " . mb_substr(wp_strip_all_tags($c->post_content), 0, 150) . "...\n";
        }
        $i++;
    }
}

print_story_info('lua-vang-giua-doi-thuong');
print_story_info('di-chuc-vo-hinh-tran-chien-tai-san');
