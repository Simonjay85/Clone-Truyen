<?php
require_once('wp-load.php');
$key = get_option('temply_openai_api_key', '');
echo "OPENAI_KEY:" . $key;
?>
