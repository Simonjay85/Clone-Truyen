<?php
require_once('wp-load.php');
$args = array(
    'post_type'      => 'truyen',
    'post_status'    => 'publish',
    'posts_per_page' => -1,
);
$query = new WP_Query($args);
$missing_covers = array();
if ($query->have_posts()) {
    while ($query->have_posts()) {
        $query->the_post();
        $id = get_the_ID();
        if (!has_post_thumbnail($id)) {
            $missing_covers[] = array(
                'id' => $id,
                'title' => get_the_title(),
                'excerpt' => get_the_excerpt()
            );
        }
    }
    wp_reset_postdata();
}

header('Content-Type: application/json');
echo json_encode($missing_covers, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
