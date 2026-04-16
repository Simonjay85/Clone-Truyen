<?php
require_once('../../../wp-load.php');

$truyen_slugs = [
    'bong-hoa-thep-huyen-thoai-bien-cuong'
];

foreach ($truyen_slugs as $slug) {
    // TÌm truyện
    $args = array(
      'name'        => $slug,
      'post_type'   => 'truyen',
      'post_status' => 'publish',
      'numberposts' => 1
    );
    $my_posts = get_posts($args);
    if( $my_posts ) {
        $t_id = $my_posts[0]->ID;
        $name = $my_posts[0]->post_title;
        echo "Found Truyen ID: $t_id for '$name'. Trashing its chapters...<br>";
        
        $args_chaps = [
            'post_type' => 'chuong',
            'meta_key' => '_truyen_id',
            'meta_value' => $t_id,
            'posts_per_page' => -1
        ];
        $chaps = get_posts($args_chaps);
        foreach ($chaps as $c) {
            wp_delete_post($c->ID, true); // Force delete
        }
        echo "Deleted " . count($chaps) . " chapters for '$name'.<br>";
    } else {
        echo "Not found: $slug<br>";
    }
}
