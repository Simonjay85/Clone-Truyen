<?php
require_once('wp-load.php');
header('Content-Type: application/json; charset=utf-8');

global $wpdb;

$results = $wpdb->get_results("
    SELECT p.ID, p.post_title, p.post_name, p.post_status, pm.meta_value as truyen_id
    FROM {$wpdb->posts} p
    LEFT JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id AND pm.meta_key = '_truyen_id'
    WHERE p.post_type = 'chuong'
    ORDER BY p.ID DESC
    LIMIT 100
");

echo json_encode($results, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
