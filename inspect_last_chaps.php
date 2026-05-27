<?php
require_once('wp-load.php');
header('Content-Type: application/json; charset=utf-8');

// Lấy 5 truyện mới nhất
$truyens = get_posts([
    'post_type'      => 'truyen',
    'posts_per_page' => 5,
    'orderby'        => 'ID',
    'order'          => 'DESC'
]);

$response = [];

foreach ($truyens as $t) {
    $tid = $t->ID;
    
    // Query direct chapters ordered by ID ASC
    $chaps_id_asc = get_posts([
        'post_type'      => 'chuong',
        'posts_per_page' => -1,
        'meta_key'       => '_truyen_id',
        'meta_value'     => $tid,
        'orderby'        => 'ID',
        'order'          => 'ASC',
        'post_status'    => 'any'
    ]);
    
    // Query direct chapters ordered by ID DESC
    $chaps_id_desc = get_posts([
        'post_type'      => 'chuong',
        'posts_per_page' => 1,
        'meta_key'       => '_truyen_id',
        'meta_value'     => $tid,
        'orderby'        => 'ID',
        'order'          => 'DESC',
        'post_status'    => 'any'
    ]);
    
    // Query direct chapters ordered by menu_order ASC
    $chaps_menu_asc = get_posts([
        'post_type'      => 'chuong',
        'posts_per_page' => -1,
        'meta_key'       => '_truyen_id',
        'meta_value'     => $tid,
        'orderby'        => 'menu_order',
        'order'          => 'ASC',
        'post_status'    => 'any'
    ]);
    
    $last_chap_by_query = !empty($chaps_id_desc) ? $chaps_id_desc[0]->post_title : 'N/A';
    $last_chap_in_asc_list = !empty($chaps_id_asc) ? $chaps_id_asc[count($chaps_id_asc) - 1]->post_title : 'N/A';
    
    // Get display name function outputs
    $helper_display_name = function_exists('tehi_get_last_chapter_display_name') ? tehi_get_last_chapter_display_name($tid) : 'not defined';
    $helper_url = function_exists('tehi_get_last_chapter_url') ? tehi_get_last_chapter_url($tid) : 'not defined';
    $helper_count = function_exists('tehi_get_chapter_count') ? tehi_get_chapter_count($tid) : 'not defined';
    
    // Check transients directly
    $transient_name = get_transient('tehi_last_chap_display_name_' . $tid);
    $transient_url = get_transient('tehi_last_chap_url_' . $tid);
    
    $c_list = [];
    foreach ($chaps_id_asc as $c) {
        $c_list[] = [
            'id' => $c->ID,
            'title' => $c->post_title,
            'menu_order' => $c->menu_order,
            'date' => $c->post_date,
            'status' => $c->post_status
        ];
    }
    
    $response[] = [
        'truyen_id' => $tid,
        'truyen_title' => $t->post_title,
        'total_chaps_count' => count($chaps_id_asc),
        'helper_count' => $helper_count,
        'last_chap_by_desc_query' => $last_chap_by_query,
        'last_chap_in_asc_list' => $last_chap_in_asc_list,
        'helper_display_name' => $helper_display_name,
        'helper_url' => $helper_url,
        'transient_display_name_cache' => $transient_name,
        'transient_url_cache' => $transient_url,
        'chapters' => $c_list
    ];
}

echo json_encode($response, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
