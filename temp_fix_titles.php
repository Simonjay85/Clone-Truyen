<?php
require('./wp-load.php');
$chaps = get_posts(['post_type' => 'chuong', 'posts_per_page' => -1, 'post_status' => 'any']);
$count = 0;
foreach($chaps as $c) {
   $title = $c->post_title;
   $new_title = str_replace(array('*', '#', '[', ']', 'TITLE:', 'TITLE :', 'Title:', 'title:'), '', $title);
   // remove multiple spaces if any
   $new_title = trim(preg_replace('/\s+/', ' ', $new_title));
   if($new_title !== $title) {
       wp_update_post(['ID' => $c->ID, 'post_title' => $new_title]);
       $count++;
   }
}
echo "Fixed $count chapters.";
?>