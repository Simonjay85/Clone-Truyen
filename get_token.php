<?php
require_once('wp-load.php');
$token = defined('TEHI_BACKFILL_TOKEN') ? TEHI_BACKFILL_TOKEN : get_option('tehi_backfill_token', '');
echo "TOKEN:" . $token;
?>
