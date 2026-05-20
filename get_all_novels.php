<?php
require_once('wp-load.php');
$truyens = get_posts([
    'post_type' => 'truyen',
    'posts_per_page' => -1,
    'post_status' => 'any'
]);

$list = [];
foreach ($truyens as $t) {
    $list[] = [
        'id' => $t->ID,
        'title' => $t->post_title,
        'slug' => $t->post_name,
        'intro' => wp_strip_all_tags(mb_substr($t->post_content, 0, 200))
    ];
}
echo json_encode($list, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
