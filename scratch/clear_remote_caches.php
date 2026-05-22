<?php
require_once('wp-load.php');
header('Content-Type: text/plain');

echo "Purging LSCache...\n";
if (class_exists('LiteSpeed\Purge')) {
    \LiteSpeed\Purge::purge_all();
    echo "LiteSpeed Cache Purged!\n";
} else {
    echo "LiteSpeed Cache is not active.\n";
}

if (function_exists('wp_cache_clear_cache')) {
    wp_cache_clear_cache();
    echo "WP Super Cache Purged!\n";
}

if (function_exists('w3tc_flush_all')) {
    w3tc_flush_all();
    echo "W3 Total Cache Purged!\n";
}

echo "Flushing rewrite rules...\n";
flush_rewrite_rules(true);
echo "Rewrite rules flushed!\n";

echo "All caches cleared successfully!\n";
?>
