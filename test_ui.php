<?php
require_once('../wp-load.php');
$truyen = get_posts(['post_type'=>'truyen', 'posts_per_page'=>20, 'post_status'=>'publish']);
echo count($truyen) . " truyen found.";
