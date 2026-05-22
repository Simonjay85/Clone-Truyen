<?php
require_once('wp-load.php');
$truyens = get_posts([
    'post_type' => 'truyen',
    'posts_per_page' => -1,
    'post_status' => 'any',
    'orderby' => 'date',
    'order' => 'DESC'
]);

$list = [];
foreach ($truyens as $t) {
    $chapters = get_posts([
        'post_type' => 'chuong',
        'meta_key' => '_truyen_id',
        'meta_value' => $t->ID,
        'posts_per_page' => -1,
        'fields' => 'ids'
    ]);
    
    $list[] = [
        'id' => $t->ID,
        'title' => $t->post_title,
        'status' => $t->post_status,
        'date' => $t->post_date,
        'slug' => $t->post_name,
        'chapters_count' => count($chapters)
    ];
}
echo json_encode($list, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>