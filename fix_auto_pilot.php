<?php
require_once('/Users/aaronnguyen/TN/App/Clone Truyen/wp-load.php');

$truyen_names = [
    'Hợp Đồng Vàng Từ Nét Vẽ Bí Mật',
    'Cú Lật Ngược Của Kẻ Bán Sticker',
    'Nữ Chủ Của Thời Khắc'
];

foreach ($truyen_names as $name) {
    // TÌm truyện
    $post = get_page_by_title($name, OBJECT, 'truyen');
    if ($post) {
        $t_id = $post->ID;
        echo "Found Truyen ID: $t_id for '$name'. Trashing its chapters...\n";
        
        $args = [
            'post_type' => 'chuong',
            'meta_key' => '_truyen_id',
            'meta_value' => $t_id,
            'posts_per_page' => -1
        ];
        $chaps = get_posts($args);
        foreach ($chaps as $c) {
            wp_delete_post($c->ID, true); // Force delete
        }
        echo "Deleted " . count($chaps) . " chapters for '$name'.\n";
    } else {
        echo "Not found: $name\n";
    }
}
