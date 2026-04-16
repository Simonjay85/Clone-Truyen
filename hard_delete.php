<?php
require_once('wp-load.php');
wp_cache_flush();
delete_option('temply_auto_pilot_queue_config');
wp_clear_scheduled_hook('temply_auto_pilot_cron_hook');
echo "Deleted successfully";
