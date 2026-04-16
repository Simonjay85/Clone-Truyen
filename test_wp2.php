<?php
require_once('wp-load.php');
$q1 = new WP_Query(['post_type'=>'truyen','posts_per_page'=>6,'no_found_rows'=>true]);
var_dump($q1->post_count);
$q2 = new WP_Query(['post_type'=>'truyen','posts_per_page'=>6,'orderby'=>'rand','no_found_rows'=>true]);
var_dump($q2->post_count);
$q3 = new WP_Query(['post_type'=>'truyen','posts_per_page'=>6,'orderby'=>'date','no_found_rows'=>true]);
var_dump($q3->post_count);
