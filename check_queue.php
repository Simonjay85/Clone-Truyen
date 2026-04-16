<?php
require_once('wp-load.php');
$config = get_option('temply_auto_pilot_queue_config', false);
if (!$config) {
    echo "No config found.\n";
} else {
    echo "Status: " . $config['status'] . "\n\n";
    if (!empty($config['queue'])) {
        foreach($config['queue'] as $i => $item) {
            echo "Item $i:\n";
            echo "  Title: " . $item['title'] . "\n";
            echo "  Status: " . $item['status'] . "\n";
            echo "  UUID: " . ($item['uuid'] ?? 'none') . "\n";
            $lock_key = 'temply_ap_lock_' . ($item['uuid'] ?? md5($item['prompt']));
            $locked = get_transient($lock_key);
            echo "  Locked: " . ($locked ? "YES ($locked)" : "NO") . "\n";
        }
    } else {
        echo "Queue is empty.\n";
    }
}
