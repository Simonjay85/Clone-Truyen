<?php
require_once('../../../wp-load.php');
$args = array('post_type' => 'chuong', 'posts_per_page' => -1);
$posts = get_posts($args);
$fixed = 0;
foreach($posts as $p) {
    if (strpos($p->post_name, '-title-') !== false || strpos($p->post_name, 'title-') === 0 || strpos($p->post_name, 'tieu-de-') === 0 || strpos($p->post_name, '-tieu-de-') !== false) {
        $new_slug = str_replace(array('-title-', 'title-', 'tieu-de-', '-tieu-de-'), array('-', '', '', '-'), $p->post_name);
        $new_slug = preg_replace('/-+/', '-', $new_slug);
        $new_slug = trim($new_slug, '-');
        
        wp_update_post(array(
            'ID' => $p->ID,
            'post_name' => $new_slug
        ));
        $fixed++;
    }
}
echo "Fixed $fixed slugs.";
@unlink(__FILE__);
