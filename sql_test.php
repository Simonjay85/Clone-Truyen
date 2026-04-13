<?php
require_once('wp-load.php');
$args = array(
    'post_type' => 'chuong',
    'posts_per_page' => 1
);
$query = new WP_Query($args);
if ($query->have_posts()) {
    while ($query->have_posts()) {
        $query->the_post();
        echo "ID: " . get_the_ID() . "\n";
        echo "Title: " . get_the_title() . "\n";
        echo "Content Length: " . strlen($post->post_content) . "\n";
        echo "Content Prefix: " . substr($post->post_content, 0, 100) . "\n";
    }
} else {
    echo "No posts found.";
}
