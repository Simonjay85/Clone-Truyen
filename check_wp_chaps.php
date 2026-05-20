<?php
require_once('wp-load.php');
header('Content-Type: application/json; charset=utf-8');

$truyen_id = 2023;

$chapters = get_posts([
    'post_type'      => 'chuong',
    'posts_per_page' => -1,
    'meta_key'       => '_truyen_id',
    'meta_value'     => $truyen_id,
    'orderby'        => 'ID', 
    'order'          => 'ASC'
]);

$response = [
    'count' => count($chapters),
    'chapters' => []
];

foreach ($chapters as $c) {
    $response['chapters'][] = [
        'id' => $c->ID,
        'title' => $c->post_title,
        'slug' => $c->post_name,
        'date' => $c->post_date,
        'status' => $c->post_status
    ];
}

echo json_encode($response, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
