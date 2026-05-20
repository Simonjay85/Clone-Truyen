<?php
require_once('wp-load.php');
header('Content-Type: text/plain; charset=utf-8');

$truyen_id = 2023;

$chapters = get_posts([
    'post_type'      => 'chuong',
    'posts_per_page' => -1,
    'meta_key'       => '_truyen_id',
    'meta_value'     => $truyen_id,
    'orderby'        => 'ID', 
    'order'          => 'ASC'
]);

echo "Story ID: " . $truyen_id . "\n";
echo "Total chapters: " . count($chapters) . "\n\n";

foreach ($chapters as $c) {
    echo "==========================================\n";
    echo "ID: " . $c->ID . "\n";
    echo "Title: " . $c->post_title . "\n";
    echo "Slug: " . $c->post_name . "\n";
    echo "Content Length: " . strlen($c->post_content) . " bytes\n";
    echo "--- Snippet (First 500 chars) ---\n";
    echo mb_substr(wp_strip_all_tags($c->post_content), 0, 500) . "\n";
    echo "--- Snippet (Last 500 chars) ---\n";
    echo mb_substr(wp_strip_all_tags($c->post_content), -500) . "\n\n";
}
?>
