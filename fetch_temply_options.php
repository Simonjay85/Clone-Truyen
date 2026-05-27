<?php
require_once('wp-load.php');
global $wpdb;
$rows = $wpdb->get_results("SELECT option_name, option_value FROM {$wpdb->options} WHERE option_name LIKE 'temply_%'");
foreach ($rows as $row) {
    echo $row->option_name . ": " . $row->option_value . "\n";
}
unlink(__FILE__);
