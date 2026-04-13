<?php
require_once('wp-load.php');
$slugs = ['bang-xep-hang', 'tai-khoan', 'truyen-hoan-thanh'];
foreach ($slugs as $slug) {
    $page = get_page_by_path($slug);
    if ($page) {
        $template = get_post_meta($page->ID, '_wp_page_template', true);
        echo "Page $slug exists ID: {$page->ID}, Template: $template\\n";
    } else {
        echo "Page $slug NOT FOUND\\n";
    }
}
?>
