<?php
require_once('wp-load.php');
$posts = get_posts([
    'post_type' => 'truyen',
    'numberposts' => 2,
    'post_status' => 'publish'
]);
foreach ($posts as $p) {
    echo "================================\n";
    echo "TITLE: " . $p->post_title . "\n";
    echo "SYNOPSIS:\n" . strip_tags($p->post_excerpt) . "\n";
    echo "\n\n";
}
