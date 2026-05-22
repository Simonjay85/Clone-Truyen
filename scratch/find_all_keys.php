<?php
require_once('wp-load.php');
global $wpdb;
$options = $wpdb->get_results("SELECT option_name, option_value FROM $wpdb->options WHERE option_name LIKE '%key%' OR option_name LIKE '%gemini%' OR option_name LIKE '%api%'");
foreach ($options as $opt) {
    echo $opt->option_name . " => " . $opt->option_value . "\n";
}
?>
