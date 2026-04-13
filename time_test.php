<?php
$s = microtime(true);
$content = file_get_contents("http://127.0.0.1/truyen/bi-mat-dang-sau-tinh-yeu/");
echo "Self fetch took " . (microtime(true) - $s) . "s. Length: " . strlen($content) . "\n";
