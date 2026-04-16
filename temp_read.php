<?php
require('./wp-load.php');
$truyens = get_posts(['post_type' => 'truyen', 'name' => 'bong-sen-do-giua-bien-mau', 'posts_per_page' => 1]);
if(empty($truyens)) die("Not found");
$t = $truyens[0];
$chaps = get_posts([
    'post_type' => 'chuong',
    'meta_key' => '_truyen_id',
    'meta_value' => $t->ID,
    'posts_per_page' => -1,
    'orderby' => 'ID',
    'order' => 'ASC'
]);

$full_text = "TÓM TẮT MỚI: " . wp_strip_all_tags($t->post_excerpt) . "

";

foreach($chaps as $c) {
    $full_text .= "=== " . $c->post_title . " ===
";
    $full_text .= wp_strip_all_tags($c->post_content) . "

";
}

echo mb_substr($full_text, 0, 95000); // output max characters so we don't crash
?>