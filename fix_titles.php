<?php
require_once('../../../wp-load.php');
$args = array('post_type' => 'chuong', 'posts_per_page' => -1);
$posts = get_posts($args);
$fixed = 0;
foreach($posts as $p) {
    $orig = $p->post_title;
    $new = preg_replace('/(?i)(Chương\s+\d+[\s:\-]*)(?:Title|Tiêu đề):\s*/u', '$1', $orig);
    $new = preg_replace('/(?i)(Chương\s+\d+[\s:\-]+)(?:Chương\s+\d+[\s:\-]+)+/u', '$1', $new);
    if ($orig !== $new) {
        wp_update_post(array('ID' => $p->ID, 'post_title' => $new));
        $fixed++;
    }
}
echo "Fixed $fixed chapters.";
@unlink(__FILE__);
