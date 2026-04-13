<?php
$start = microtime(true);
require_once('../wp-load.php');
echo "Loaded WP in " . (microtime(true) - $start) . " seconds";
