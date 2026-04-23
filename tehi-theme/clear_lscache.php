<?php
require_once('../../../wp-load.php');
if (class_exists('LiteSpeed\Purge')) {
    \LiteSpeed\Purge::purge_all();
    echo "LSCache Purged successfully!";
} else {
    echo "LSCache class not found.";
}
if (function_exists('wp_cache_clear_cache')) {
    wp_cache_clear_cache();
    echo " WP Super Cache Purged!";
}
if (function_exists('w3tc_flush_all')) {
    w3tc_flush_all();
    echo " W3TC Purged!";
}
?>
