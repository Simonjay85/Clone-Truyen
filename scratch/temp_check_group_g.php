<?php
require_once('wp-load.php');
header('Content-Type: application/json; charset=utf-8');

$ids = [2023, 2035, 2044, 2052, 2067];
$list = [];

foreach ($ids as $id) {
    $post = get_post($id);
    if ($post) {
        $chapters = get_posts([
            'post_type' => 'chuong',
            'posts_per_page' => -1,
            'meta_key' => '_truyen_id',
            'meta_value' => $id,
            'orderby' => 'ID',
            'order' => 'ASC',
            'post_status' => 'any'
        ]);
        
        $chaps_list = [];
        foreach ($chapters as $c) {
            $chaps_list[] = [
                'id' => $c->ID,
                'title' => $c->post_title,
                'status' => $c->post_status
            ];
        }
        
        $list[$id] = [
            'id' => $post->ID,
            'title' => $post->post_title,
            'status' => $post->post_status,
            'intro' => $post->post_content,
            'focus_keyword' => get_post_meta($id, 'rank_math_focus_keyword', true),
            'seo_title' => get_post_meta($id, 'rank_math_title', true),
            'seo_description' => get_post_meta($id, 'rank_math_description', true),
            'chapter_count' => count($chapters),
            'chapters' => $chaps_list
        ];
    } else {
        $list[$id] = null;
    }
}

echo json_encode($list, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>