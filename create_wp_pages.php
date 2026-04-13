<?php
require_once('wp-load.php');

$pages = [
    [
        'title' => 'Bảng xếp hạng',
        'slug' => 'bang-xep-hang',
        'template' => 'page-bangxephang.php'
    ],
    [
        'title' => 'Tài khoản',
        'slug' => 'tai-khoan',
        'template' => 'page-profile.php'
    ],
    [
        'title' => 'Truyện Hoàn Thành',
        'slug' => 'truyen-hoan-thanh',
        'template' => 'page-completed.php'
    ]
];

foreach ($pages as $p) {
    $page = get_page_by_path($p['slug']);
    if (!$page) {
        $post_id = wp_insert_post([
            'post_title'    => $p['title'],
            'post_name'     => $p['slug'],
            'post_status'   => 'publish',
            'post_type'     => 'page',
        ]);
        if (!is_wp_error($post_id)) {
            update_post_meta($post_id, '_wp_page_template', $p['template']);
            echo "Created page: " . $p['title'] . "\n";
        }
    } else {
        update_post_meta($page->ID, '_wp_page_template', $p['template']);
        echo "Updated template for page: " . $p['title'] . "\n";
    }
}
?>
