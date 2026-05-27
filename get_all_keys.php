<?php
require_once('wp-load.php');
echo "OPENAI_KEY:" . get_option('temply_openai_api_key', '') . "\n";
echo "GEMINI_KEY:" . get_option('temply_gemini_api_key', '') . "\n";
echo "GEMINI_FREE_KEY:" . get_option('temply_gemini_api_key_free', '') . "\n";
?>
