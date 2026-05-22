<?php
require_once('./wp-load.php');
$post_id = 3633;
$t = get_post($post_id);
if(empty($t)) die("Not found");

$chaps = get_posts([
    'post_type' => 'chuong',
    'meta_key' => '_truyen_id',
    'meta_value' => $post_id,
    'posts_per_page' => -1,
    'orderby' => 'meta_value_num',
    'meta_key' => '_chap_order',
    'order' => 'ASC'
]);

// If order is empty, fallback to ID order
if (empty($chaps)) {
    $chaps = get_posts([
        'post_type' => 'chuong',
        'meta_key' => '_truyen_id',
        'meta_value' => $post_id,
        'posts_per_page' => -1,
        'orderby' => 'ID',
        'order' => 'ASC'
    ]);
}

$genre_names = [];
$terms = wp_get_post_terms($post_id, 'the_loai');
foreach($terms as $term) {
    $genre_names[] = $term->name;
}

$rm_title = get_post_meta($post_id, 'rank_math_title', true);
$rm_desc = get_post_meta($post_id, 'rank_math_description', true);
$rm_keyword = get_post_meta($post_id, 'rank_math_focus_keyword', true);
$rm_title_u = get_post_meta($post_id, '_rank_math_title', true);
$rm_desc_u = get_post_meta($post_id, '_rank_math_description', true);
$rm_keyword_u = get_post_meta($post_id, '_rank_math_focus_keyword', true);

$thumb_id = get_post_thumbnail_id($post_id);
$alt_text = get_post_meta($thumb_id, '_wp_attachment_image_alt', true);

$output = [
    'id' => $t->ID,
    'title' => $t->post_title,
    'slug' => $t->post_name,
    'excerpt' => $t->post_excerpt,
    'genres' => $genre_names,
    'thumb_id' => $thumb_id,
    'thumb_alt' => $alt_text,
    'rank_math_title' => $rm_title ? $rm_title : $rm_title_u,
    'rank_math_description' => $rm_desc ? $rm_desc : $rm_desc_u,
    'rank_math_focus_keyword' => $rm_keyword ? $rm_keyword : $rm_keyword_u,
    'chapters' => []
];

foreach($chaps as $c) {
    $output['chapters'][] = [
        'id' => $c->ID,
        'title' => $c->post_title,
        'content' => wp_strip_all_tags($c->post_content)
    ];
}

header('Content-Type: application/json; charset=utf-8');
echo json_encode($output, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>