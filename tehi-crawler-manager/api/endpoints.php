<?php
if ( ! defined( 'ABSPATH' ) ) exit;

// Đăng ký API Route
add_action( 'rest_api_init', function () {
    // 1. Endpoint lấy Job
    register_rest_route( 'crawler/v1', '/get-task', array(
        'methods' => 'GET',
        'callback' => 'tehi_crawler_api_get_task',
        'permission_callback' => '__return_true' // Thiết lập auth Basic/JWT trong môi trường thực
    ) );

    // 2. Endpoint cập nhật tiến độ
    register_rest_route( 'crawler/v1', '/update-status', array(
        'methods' => 'POST',
        'callback' => 'tehi_crawler_api_update_status',
        'permission_callback' => '__return_true'
    ) );
    
    // 3. Lấy cấu hình (OpenAI Key) cho Bot
    register_rest_route( 'crawler/v1', '/settings', array(
        'methods' => 'GET',
        'callback' => function() {
            return array('openai_key' => get_option('tehi_openai_key', ''));
        },
        'permission_callback' => '__return_true'
    ) );
} );

function tehi_crawler_api_get_task( WP_REST_Request $request ) {
    global $wpdb;
    $table_name = $wpdb->prefix . 'crawler_jobs';

    // Tìm 1 job đang pending
    $job = $wpdb->get_row( "SELECT * FROM $table_name WHERE status = 'pending' ORDER BY id ASC LIMIT 1" );

    if ( $job ) {
        // Đổi trạng thái sang processing
        $wpdb->update( 
            $table_name, 
            array( 'status' => 'processing' ), 
            array( 'id' => $job->id ) 
        );
        return rest_ensure_response( array(
            'success' => true,
            'task'    => $job
        ) );
    }

    return rest_ensure_response( array('success' => false, 'message' => 'No pending tasks') );
}

function tehi_crawler_api_update_status( WP_REST_Request $request ) {
    global $wpdb;
    $table_name = $wpdb->prefix . 'crawler_jobs';
    
    $job_id           = sanitize_text_field( $request->get_param( 'job_id' ) );
    $status           = sanitize_text_field( $request->get_param( 'status' ) );
    $novel_title      = sanitize_text_field( $request->get_param( 'novel_title' ) );
    $total_chapters   = intval( $request->get_param( 'total_chapters' ) );
    $crawled_chapters = intval( $request->get_param( 'crawled_chapters' ) );
    $error_log        = sanitize_text_field( $request->get_param( 'error_log' ) );

    if ( ! $job_id ) {
        return new WP_Error( 'missing_id', 'Missing job_id', array('status' => 400) );
    }

    $update_data = array();
    if ( $status ) $update_data['status'] = $status;
    if ( $novel_title ) $update_data['novel_title'] = $novel_title;
    if ( $total_chapters !== null ) $update_data['total_chapters'] = $total_chapters;
    if ( $crawled_chapters !== null ) $update_data['crawled_chapters'] = $crawled_chapters;
    if ( $error_log ) $update_data['error_log'] = $error_log;

    $wpdb->update( $table_name, $update_data, array( 'id' => $job_id ) );

    return rest_ensure_response( array( 'success' => true ) );
}
