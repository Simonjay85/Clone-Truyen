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
 * Inject Tailwind CDN + Material Symbols để các template cũ render đúng
 */
add_action('wp_head', function() {
    // Chỉ tải trên các trang KHÔNG phải front-page (vì front-page dùng CSS riêng)
    if (!is_front_page()) {
        echo '<script src="https://cdn.tailwindcss.com"></script>' . "\n";
        echo '<script>tailwind.config={corePlugins:{preflight:false},theme:{extend:{colors:{"surface-container-lowest":"#ffffff","surface-container-low":"#f6f3f2","surface-container":"#f0eded","surface-container-high":"#eae8e7","surface-container-highest":"#e4e2e1","surface-bright":"#fbf9f8","surface":"#fbf9f8","on-surface":"#1b1c1c","on-surface-variant":"#404752","outline":"#707783","outline-variant":"#c0c7d4","primary":"#0060a9","primary-container":"#3f9cfb","on-primary":"#ffffff","on-primary-container":"#00325c","secondary":"#536068","secondary-container":"#d4e2eb","on-secondary-container":"#57656c","background":"#fbf9f8","on-background":"#1b1c1c"}}}}</script>' . "\n";
    }
    echo '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&display=swap">' . "\n";
}, 1);

/**
 * Bật Hỗ Trợ Elementor Header & Footer Builder
 */
function tehi_elementor_hf_support() {
    add_theme_support( 'header-footer-elementor' );
    add_theme_support( 'elementor' );
}
add_action( 'after_setup_theme', 'tehi_elementor_hf_support' );

/**
 * Điều hướng sửa lỗi 404 cho các link .html cũ (như bang-xep-hang.html, hoan-thanh.html)
 */
add_filter('template_include', function($template) {
    if (!is_admin()) {
        $uri = $_SERVER['REQUEST_URI'];
        if (strpos($uri, '.html') !== false) {
            $path = parse_url($uri, PHP_URL_PATH);
            $basename = basename($path);
            
            $template_map = [
                'dang-nhap.html'           => '/page-profile.php',
                'the-loai.html'            => '/page-directory.php',
                'danh-muc.html'            => '/page-directory.php',
                'theo-doi.html'            => '/page-library.php',
                'bang-xep-hang.html'       => '/page-bxh.php',
                'hoan-thanh.html'          => '/page-completed.php',
                'truyen-moi-cap-nhat.html' => '/page-latest.php',
                'nhom-dich.html'           => '/page-teams.php'
            ];
            
            if (isset($template_map[$basename])) {
                $mapped_file = get_template_directory() . $template_map[$basename];
                
                // Fallback nếu Bảng xếp hạng bị rỗng (0 bytes)
                if ($basename == 'bang-xep-hang.html' && (!file_exists($mapped_file) || filesize($mapped_file) < 50)) {
                    $mapped_file = get_template_directory() . '/page-latest.php';
                }
                
                if (file_exists($mapped_file) && filesize($mapped_file) > 0) {
                    global $wp_query;
                    $wp_query->is_404 = false;
                    status_header(200);
                    return $mapped_file;
                }
            }
        }
    }
    return $template;
}, 99);

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
