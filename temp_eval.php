<?php
require('./wp-load.php');
$truyens = get_posts([
    'post_type' => 'truyen',
    'posts_per_page' => 2,
    'post_status' => 'publish',
    'orderby' => 'date',
    'order' => 'DESC'
]);

$results = [];
foreach($truyens as $t) {
    $results[] = [
        'title' => $t->post_title,
        'synopsis' => wp_strip_all_tags($t->post_excerpt),
        'world' => get_post_meta($t->ID, '_temply_ai_world', true),
        'chars' => get_post_meta($t->ID, '_temply_ai_characters', true),
        'script' => get_post_meta($t->ID, '_temply_ai_script', true)
    ];
}

header('Content-Type: application/json; charset=utf-8');
echo json_encode($results, JSON_UNESCAPED_UNICODE);
?>