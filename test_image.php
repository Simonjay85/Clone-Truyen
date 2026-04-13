<?php
require_once 'wp-load.php';
$url = "https://image.pollinations.ai/prompt/anime%20boy?nologo=true";
$tmp = download_url($url);
if(is_wp_error($tmp)) {
    echo "Error: " . $tmp->get_error_message();
} else {
    echo "Success: " . $tmp;
    @unlink($tmp);
}
