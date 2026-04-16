<?php
require_once('/Users/aaronnguyen/TN/App/Clone Truyen/wp-load.php');
$config = get_option('temply_auto_pilot_queue_config', false);
if ($config) {
    $config['queue'] = [];
    $config['status'] = 'completed';
    update_option('temply_auto_pilot_queue_config', $config);
    wp_clear_scheduled_hook('temply_auto_pilot_cron_hook');
    echo "Queue cleared and cron stopped.";
} else {
    echo "No queue config found.";
}
