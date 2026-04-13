<?php
$s = microtime(true);
require_once('../wp-load.php');
global $wpdb;
$wpdb->get_results("SELECT ID FROM {$wpdb->posts} WHERE post_type='post' LIMIT 5");
echo "DB took " . (microtime(true) - $s) . "s\n";
