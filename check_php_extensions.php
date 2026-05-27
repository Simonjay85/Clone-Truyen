<?php
header('Content-Type: application/json');

$res = [
    'gd' => extension_loaded('gd'),
    'imagick' => extension_loaded('imagick'),
    'loaded_extensions' => get_loaded_extensions()
];
echo json_encode($res, JSON_PRETTY_PRINT);
?>
