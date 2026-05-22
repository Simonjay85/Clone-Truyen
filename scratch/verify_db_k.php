<?php
require_once('wp-load.php');
header('Content-Type: application/json; charset=utf-8');

$ids = [2238, 2249, 2259, 2269, 2279];
$result = [];
foreach ($ids as $id) {
    $post = get_post($id);
    if ($post) {
        $chaps = get_posts([
            'post_type' => 'chuong',
            'meta_key' => '_truyen_id',
            'meta_value' => $id,
            'posts_per_page' => 100,
            'post_status' => 'any',
            'orderby' => 'menu_order',
            'order' => 'ASC'
        ]);
        $result[$id] = [
            'title' => $post->post_title,
            'focus_keyword' => get_post_meta($id, 'rank_math_focus_keyword', true),
            'seo_title' => get_post_meta($id, 'rank_math_title', true),
            'seo_desc' => get_post_meta($id, 'rank_math_description', true),
            'chapter_count' => count($chaps),
            'chapters' => array_map(function($c) { return $c->post_title; }, $chaps)
        ];
    } else {
        $result[$id] = 'not_found';
    }
}
echo json_encode($result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
