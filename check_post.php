<?php
require_once('wp-load.php');
$args = array('post_type' => 'chuong', 'posts_per_page' => 1);
$q = new WP_Query($args);
if ($q->have_posts()) {
    while ($q->have_posts()) {
        $q->the_post();
        echo "ID: " . get_the_ID() . "\n";
        echo "Title: " . get_the_title() . "\n";
        echo "Meta: " . json_encode(get_post_custom(get_the_ID())) . "\n";
    }
} else {
    echo "No chapters found.";
}
