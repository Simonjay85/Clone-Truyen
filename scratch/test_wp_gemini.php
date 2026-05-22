<?php
require_once('wp-load.php');

$sys = "You are a helpful assistant.";
$user = "Say 'Gemini on doctieuthuyet works!' and nothing else.";

$res = temply_call_gemini($sys, $user);
if (is_wp_error($res)) {
    echo "ERROR: " . $res->get_error_message();
} else {
    echo "SUCCESS: " . $res;
}
?>
