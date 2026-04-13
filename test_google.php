<?php
require_once('../wp-load.php');
$s = microtime(true);
$res = wp_remote_post("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=invalid_key", [
    'timeout' => 15,
    'body' => json_encode(['contents'=>[['parts'=>[['text'=>'Hi']]]]])
]);
echo "Took " . (microtime(true) - $s) . "s. ";
if(is_wp_error($res)) {
    echo "Error: " . $res->get_error_message();
} else {
    echo "Code: " . wp_remote_retrieve_response_code($res);
}
