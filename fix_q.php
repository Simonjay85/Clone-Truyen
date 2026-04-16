<?php
require_once('../../../wp-load.php');
$config = get_option('temply_auto_pilot_queue_config', false);
if($config && isset($config['queue'])) {
    $last = array_pop($config['queue']); // Keep the last one which is my test
    $config['queue'] = [$last];
    $config['status'] = 'running';
    update_option('temply_auto_pilot_queue_config', $config);
    echo "Queue cleared to 1 single element. Processing now...";
    if (function_exists('temply_process_auto_pilot')) {
        temply_process_auto_pilot();
    }
}
