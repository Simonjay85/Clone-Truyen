<?php
require_once('wp-load.php');
global $wpdb;
$res = $wpdb->get_results("SELECT option_name, option_value FROM {$wpdb->options} WHERE option_name LIKE '_transient_timeout_temply_ap_lock%'");
print_r($res);
