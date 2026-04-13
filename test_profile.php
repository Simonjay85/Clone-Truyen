<?php
$s = microtime(true);
require_once('../wp-load.php');
error_log("WP loaded in " . (microtime(true) - $s));

$s = microtime(true);
ob_start();
get_header();
$html = ob_get_clean();
error_log("get_header() took " . (microtime(true) - $s));

echo "OK";
