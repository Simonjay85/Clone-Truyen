<?php
require('./wp-load.php');
$truyens = get_posts(['post_type' => 'truyen', 'posts_per_page' => -1]);
$count = 0;
foreach($truyens as $t) {
    if(empty($t->post_excerpt) || strpos($t->post_excerpt, '1. Bối cảnh') !== false || strlen($t->post_excerpt) < 60) {
        // broken
        $count++;
    }
}
echo "Found $count broken stories.";
?>