<?php
require_once('wp-load.php');

$config = get_option('temply_auto_pilot_queue_config', false);
if ($config) {
    $config['interval'] = 'every_minute';
    update_option('temply_auto_pilot_queue_config', $config);
    
    wp_clear_scheduled_hook('temply_auto_pilot_cron_hook');
    wp_schedule_event(time(), 'every_minute', 'temply_auto_pilot_cron_hook');
    
    echo "Rescheduled cron to every_minute successfully.";
} else {
    echo "No config found.";
}
?>
