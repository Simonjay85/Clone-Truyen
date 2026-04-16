<?php
require_once('../../../wp-load.php');
$config = get_option('temply_auto_pilot_queue_config', false);
print_r($config);
