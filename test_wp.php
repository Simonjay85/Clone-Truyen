<?php
require_once('wp-load.php');
$slider_q = new WP_Query(['post_type'=>'truyen','posts_per_page'=>6,'orderby'=>'rand','no_found_rows'=>true]);
var_dump($slider_q->request);
var_dump($slider_q->post_count);
