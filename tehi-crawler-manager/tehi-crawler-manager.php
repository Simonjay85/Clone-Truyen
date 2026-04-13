<?php
/**
 * Plugin Name: TeHi Crawler Manager
 * Description: Plugin kết nối API với Python Worker để crawl truyện tự động, theo dõi tiến độ và xử lý bằng AI.
 * Version: 1.0.0
 * Author: Your Name
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

define( 'TEHI_CRAWLER_VER', '1.0.0' );
define( 'TEHI_CRAWLER_DIR', plugin_dir_path( __FILE__ ) );
define( 'TEHI_CRAWLER_URL', plugin_dir_url( __FILE__ ) );

// 1. Tạo Database Table khi Activate Plugin
function tehi_crawler_activate() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'crawler_jobs';
    $charset_collate = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        novel_url varchar(255) NOT NULL,
        novel_title varchar(255) DEFAULT '' NOT NULL,
        status varchar(50) DEFAULT 'pending' NOT NULL,
        total_chapters int DEFAULT 0 NOT NULL,
        crawled_chapters int DEFAULT 0 NOT NULL,
        ai_rewrite tinyint(1) DEFAULT 0 NOT NULL,
        fake_meta text,
        error_log text,
        created_at datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
        updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL,
        PRIMARY KEY  (id),
        UNIQUE KEY novel_url (novel_url)
    ) $charset_collate;";

    require_once( ABSPATH . 'wp-admin/includes/upgrade.php' );
    dbDelta( $sql );
}
register_activation_hook( __FILE__, 'tehi_crawler_activate' );

// 2. Tạo Menu hiển thị trong Dashboard
function tehi_crawler_admin_menu() {
    add_menu_page(
        'Quản Lý Crawler',
        'Crawler AI',
        'manage_options',
        'tehi-crawler',
        'tehi_crawler_dashboard_page',
        'dashicons-download',
        30
    );
}
add_action( 'admin_menu', 'tehi_crawler_admin_menu' );

// Giao diện Dashboard (Load từ file riêng)
function tehi_crawler_dashboard_page() {
    include TEHI_CRAWLER_DIR . 'admin/dashboard.php';
}

// 3. Tải các file phụ trợ nếu có
require_once TEHI_CRAWLER_DIR . 'api/endpoints.php';
