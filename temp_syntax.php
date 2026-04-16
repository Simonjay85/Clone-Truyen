<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
register_shutdown_function(function() {
    $e = error_get_last();
    if($e !== null) {
        echo "\n--- FATAL ERROR DETECTED ---\n";
        print_r($e);
    }
});
require('./wp-load.php');
?>