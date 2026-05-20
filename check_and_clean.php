<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);
header('Content-Type: application/json; charset=utf-8');

require_once('wp-load.php');
global $wpdb;

$truyen_id = 2023;

// Query all chapters for the story
$results = $wpdb->get_results($wpdb->prepare("
    SELECT p.ID, p.post_title, p.post_name, p.post_date, p.post_status 
    FROM {$wpdb->posts} p
    INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
    WHERE pm.meta_key = '_truyen_id' AND pm.meta_value = %d AND p.post_type = 'chuong'
    ORDER BY p.post_date ASC
", $truyen_id));

$response = [
    'count' => count($results),
    'chapters' => []
];

foreach ($results as $row) {
    $response['chapters'][] = [
        'id' => (int)$row->ID,
        'title' => $row->post_title,
        'slug' => $row->post_name,
        'date' => $row->post_date,
        'status' => $row->post_status
    ];
}

echo json_encode($response, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
