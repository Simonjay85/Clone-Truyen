<?php
/**
 * TeHi Clone Theme Functions and Definitions
 */

if ( ! function_exists( 'tehi_clone_setup' ) ) {
    function tehi_clone_setup() {
        // Thêm các tính năng cơ bản của theme
        add_theme_support( 'title-tag' );
        add_theme_support( 'post-thumbnails' );
        
        // Đăng ký Menu
        register_nav_menus( array(
            'primary' => esc_html__( 'Primary Menu', 'tehiclone' ),
            'mobile'  => esc_html__( 'Mobile Menu', 'tehiclone' )
        ) );
    }
}
add_action( 'after_setup_theme', 'tehi_clone_setup' );

/**
 * Gọi CSS/JS của theme
 */
function tehi_clone_scripts() {
    // Gọi tệp style.css chính
    wp_enqueue_style( 'tehi-clone-style', get_stylesheet_uri(), array(), wp_get_theme()->get('Version') );

    wp_enqueue_style( 'bootstrap-css', get_template_directory_uri() . '/assets/css/bootstrap.min.css' );
    wp_enqueue_style( 'tehi-media', get_template_directory_uri() . '/assets/css/media.css' );
    wp_enqueue_style( 'tehi-mongdaovien', get_template_directory_uri() . '/assets/css/style-mongdaovien.css' );
    wp_enqueue_style( 'tehi-truyen-moi', get_template_directory_uri() . '/assets/css/style-truyen-moi-v1.css' );
    wp_enqueue_style( 'tehi-style-base', get_template_directory_uri() . '/assets/css/style.css' );
    
    wp_enqueue_style( 'fontawesome', 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css' );
    
    wp_enqueue_script( 'bootstrap-js', 'https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.3/js/bootstrap.bundle.min.js', array(), null, true );
}
add_action( 'wp_enqueue_scripts', 'tehi_clone_scripts' );

/**
 * Đăng ký Custom Post Types: Truyện và Chương
 */
function tehi_clone_cpt_init() {
    // 1. CPT Truyện
    $labels_truyen = array(
        'name'               => 'Truyện',
        'singular_name'      => 'Truyện',
        'menu_name'          => 'Kho Truyện',
        'add_new'            => 'Thêm Truyện Mới',
        'add_new_item'       => 'Thêm Truyện Mới',
        'edit_item'          => 'Sửa Truyện',
        'all_items'          => 'Tất cả Truyện'
    );
    $args_truyen = array(
        'labels'             => $labels_truyen,
        'public'             => true,
        'has_archive'        => true,
        'show_in_rest'       => true,
        'rewrite'            => array('slug' => 'truyen'),
        'supports'           => array( 'title', 'editor', 'thumbnail', 'excerpt', 'comments' ),
        'menu_icon'          => 'dashicons-book-alt'
    );
    register_post_type( 'truyen', $args_truyen );

    // 2. CPT Chương
    $labels_chuong = array(
        'name'               => 'Chương',
        'singular_name'      => 'Chương',
        'menu_name'          => 'Danh sách Chương',
        'add_new'            => 'Thêm Chương Mới',
        'add_new_item'       => 'Thêm Chương Mới',
        'edit_item'          => 'Sửa Chương',
        'all_items'          => 'Tất cả Chương'
    );
    $args_chuong = array(
        'labels'             => $labels_chuong,
        'public'             => true,
        'has_archive'        => false,
        'show_in_rest'       => true,
        'rewrite'            => array('slug' => 'chuong'),
        'supports'           => array( 'title', 'editor', 'custom-fields' ),
        'menu_icon'          => 'dashicons-media-document'
    );
    register_post_type( 'chuong', $args_chuong );

    // Đăng ký trường Meta để lưu ID của Truyện
    register_post_meta( 'chuong', '_truyen_id', array(
        'show_in_rest' => true,
        'single'       => true,
        'type'         => 'integer',
        'auth_callback'=> '__return_true'
    ) );


    // 3. Taxonomy: Thể loại
    register_taxonomy(
        'the_loai',
        'truyen',
        array(
            'label' => 'Thể loại',
            'hierarchical' => true,
            'show_in_rest' => true,
            'rewrite' => array('slug' => 'the-loai')
        )
    );
}
add_action( 'init', 'tehi_clone_cpt_init' );
