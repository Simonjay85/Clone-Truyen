<?php
require_once('wp-load.php');

$posts_to_delete = array(580);

// Get post IDs by slugs
$slugs = ['kiem-do-huyen-luc-nu-phan-dien-phuc-han', 'ngoc-hoang-giang-tran'];
foreach ($slugs as $slug) {
    $args = array(
        'name'        => $slug,
        'post_type'   => 'truyen',
        'post_status' => 'any',
        'numberposts' => 1
    );
    $my_posts = get_posts($args);
    if($my_posts) {
        $posts_to_delete[] = $my_posts[0]->ID;
    } else {
        echo "Could not find slug: $slug<br>";
    }
}

foreach($posts_to_delete as $id) {
    $post = get_post($id);
    if ($post) {
        echo "Found ID: $id - Deleting...<br>";
        
        $chapters = get_posts(array(
            'post_type' => 'chuong',
            'meta_key' => '_truyen_id',
            'meta_value' => $id,
            'posts_per_page' => -1,
            'fields' => 'ids'
        ));
        
        foreach($chapters as $cid) {
            wp_delete_post($cid, true);
        }
        wp_delete_post($id, true);
        echo "Deleted ID $id and " . count($chapters) . " chapters.<br>";
    } else {
        echo "Could not find ID $id<br>";
    }
}
