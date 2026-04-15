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
                    global $wp_query, $tehi_tailwind_page;
                    $tehi_tailwind_page = true;
                    $wp_query->is_404 = false;
                    status_header(200);
                    return $mapped_file;
                }
            }
        }
    }

    // Nếu không phải custom URL nhưng là file giao diện mới (Tailwind)
    $filename = basename($template);
    if (strpos($filename, 'taxonomy-the_loai.php') === 0 || strpos($filename, 'page-') === 0) {
        global $tehi_tailwind_page;
        $tehi_tailwind_page = true;
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

// AJAX for Lượt thích
add_action('wp_ajax_temply_like_chapter', 'temply_handle_like_chapter');
add_action('wp_ajax_nopriv_temply_like_chapter', 'temply_handle_like_chapter');
function temply_handle_like_chapter() {
    $post_id = isset($_POST['post_id']) ? intval($_POST['post_id']) : 0;
    if($post_id > 0) {
        $likes = (int)get_post_meta($post_id, 'truyen_yeu_thich', true);
        $likes++;
        update_post_meta($post_id, 'truyen_yeu_thich', $likes);
        wp_send_json_success(['likes' => $likes]);
    }
    wp_send_json_error();
}
// Custom WP Admin Style injected for modern clean UI
function dtt_custom_wp_admin_style() {
    echo '<style>
        #adminmenu { background-color: #1e1e2d; }
        #adminmenu .menu-top { border-bottom: 2px solid transparent; }
        #adminmenu a { color: #a4a6b3; }
        #adminmenu li.menu-top:hover, #adminmenu li.opensub>a.menu-top, #adminmenu li>a.menu-top:focus { background-color: #2b2b40; color: #fff; }
        #adminmenu .wp-has-current-submenu .wp-submenu, #adminmenu .wp-has-current-submenu .wp-submenu.sub-open, #adminmenu .wp-has-current-submenu.opensub .wp-submenu, #adminmenu a.wp-has-current-submenu:focus+.wp-submenu { background-color: #1c1c2a; }
        #adminmenu .wp-has-current-submenu a.wp-has-current-submenu { background-color: #6366f1; color: #fff; }
        #adminmenu .wp-has-current-submenu .wp-submenu a:hover { color: #fff; }
        #wpadminbar { background-color: #1e1e2d; }
        body.wp-admin { font-family: "Be Vietnam Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f3f6f9; }
        #wpcontent, #wpbody-content { background: #f3f6f9; }
        .postbox { border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); border: none; }
        .button-primary { background: #6366f1 !important; border-color: #6366f1 !important; box-shadow: 0 4px 6px rgba(99, 102, 241, 0.2) !important; border-radius: 6px !important; text-shadow: none !important; }
        .button-primary:hover { background: #4f46e5 !important; border-color: #4f46e5 !important; }
        div.updated, div.error, div.notice { border-left-width: 4px; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); }
        h1, h2, h3, h4, h5, h6 { font-family: "Be Vietnam Pro", sans-serif; font-weight: 700; color: #111827; }
        #wpwrap { font-size: 14px; }
        /* Clean up table rows */
        .wp-list-table th { background: #fff; padding: 12px 10px; font-weight: 600; color: #374151; }
        .wp-list-table tr { border-bottom: 1px solid #f3f4f6; }
        .wp-list-table td { padding: 12px 10px; }
    </style>';
}
add_action('admin_head', 'dtt_custom_wp_admin_style');
add_action('login_enqueue_scripts', 'dtt_custom_wp_admin_style'); // also style login
// ==========================================
// TEMPLY AI ASSISTANT INTEGRATION
// ==========================================

function temply_enqueue_ai_assistant_assets() {
    // Only load on post/page editing screen
    $current_screen = get_current_screen();
    if ( ! $current_screen || ! method_exists( $current_screen, 'is_block_editor' ) || ! $current_screen->is_block_editor() ) {
        return;
    }

    $theme_uri = get_template_directory_uri();
    
    // Enqueue the assistant JS
    wp_enqueue_script(
        'temply-ai-assistant',
        $theme_uri . '/assets/js/temply-ai-assistant.js',
        array('wp-blocks', 'wp-i18n', 'wp-element', 'wp-editor', 'wp-data', 'wp-core-data', 'jquery'),
        filemtime( __DIR__ . '/assets/js/temply-ai-assistant.js' ),
        true
    );

    // Pass AJAX details locally to JS
    wp_localize_script( 'temply-ai-assistant', 'templyAIParams', array(
        'ajaxurl' => admin_url( 'admin-ajax.php' ),
        'nonce'   => wp_create_nonce( 'temply_ai_nonce' ),
        'postId'  => get_the_ID()
    ) );
}
add_action( 'enqueue_block_editor_assets', 'temply_enqueue_ai_assistant_assets' );

// AJAX Handler: Rewrite Content
add_action('wp_ajax_temply_ai_rewrite', 'temply_handle_ai_rewrite');
function temply_handle_ai_rewrite() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');
    
    $content = isset($_POST['content']) ? wp_unslash($_POST['content']) : '';
    $mode = isset($_POST['mode']) ? $_POST['mode'] : 'paragraph'; // 'paragraph' or 'all'
    
    if (empty($content)) {
        wp_send_json_error(array('message' => 'Không có nội dung để AI xử lý.'));
    }

    // MOCK AI ENGINE PROCESSING
    // In production, you would curl OpenAI or Anthropic API here.
    sleep(2); // Simulate network latency
    
    $rewritten = '';
    
    // Intelligent Mock Response based on input length
    if ($mode === 'all') {
        $rewritten = "Đây là phiên bản đã được AI xào bài và viết lại mượt mà hơn cho toàn bộ truyện. Các chi tiết thừa được cắt bỏ, lời thoại trở nên sắc sảo hơn và tình tiết được đẩy lên cao trào. \n\n" . $content;
    } else {
        // Rewrite just the block
        $rewritten = "✨ (Đã được AI tái tạo phong cách Điện Ảnh) ✨ " . $content;
    }

    wp_send_json_success(array('rewritten_content' => $rewritten));
}

// ========== AI HELPER CONFIGURATION ==========
// Lấy thẻ API Key từ DB của Plugin Temply AI Factory
// Fallback key nếu DB rỗng
define('TEMPLY_GEMINI_FALLBACK_KEY', 'AIzaSyDD7JDTkTp9872jQkKGT2A6PPOhfp5M4Q4');

function tehi_get_gemini_key() {
    $key = get_option('temply_gemini_api_key', '');
    return !empty($key) ? $key : TEMPLY_GEMINI_FALLBACK_KEY;
}
function tehi_call_ai_api($prompt, $jsonMode = false, $timeout = 60, $ai_model = 'gemini-2.5-flash') {
    $gemini_key = get_option('temply_gemini_api_key', '');
    
    if ($ai_model !== 'openai' && !empty($gemini_key)) {
        // Connect to Google Gemini API
        $url = 'https://generativelanguage.googleapis.com/v1beta/models/' . $ai_model . ':generateContent?key=' . $gemini_key;
        
        if ($jsonMode) {
            $prompt .= "\n\nPlease respond in pure JSON format only, without Markdown formatting. Start with { and end with }";
        }

        $body = json_encode([
            'contents' => [
                ['parts' => [['text' => $prompt]]]
            ]
        ]);

        $response = wp_remote_post($url, [
            'body'    => $body,
            'headers' => ['Content-Type' => 'application/json'],
            'timeout' => $timeout,
            'sslverify' => false
        ]);

        if (is_wp_error($response)) { return 'CURL_ERROR|' . $response->get_error_message(); }
        
        $res_body = wp_remote_retrieve_body($response);
        $data = json_decode($res_body, true);
        
        if (isset($data['error'])) {
            // Return API error string for debugging
            return 'API_ERROR|' . $data['error']['message'];
        }
        
        return isset($data['candidates'][0]['content']['parts'][0]['text']) ? $data['candidates'][0]['content']['parts'][0]['text'] : '';
    } else {
        // Fallback to Pollinations API
        $args = array(
            'body' => json_encode(array(
                'messages' => array(array('role' => 'user', 'content' => $prompt)),
                'model' => 'openai',
                'jsonMode' => $jsonMode,
                'seed' => wp_rand(1000, 9999)
            )),
            'headers' => array('Content-Type' => 'application/json'),
            'timeout' => $timeout
        );
        $response = wp_remote_post('https://text.pollinations.ai/openai', $args);
        
        if (is_wp_error($response)) return 'CURL_ERROR|' . $response->get_error_message();
        
        $body = wp_remote_retrieve_body($response);
        $json_res = json_decode($body, true);
        return isset($json_res['choices'][0]['message']['content']) ? $json_res['choices'][0]['message']['content'] : $body;
    }
}

// AJAX Handler: Generate SEO
add_action('wp_ajax_temply_ai_generate_seo', 'temply_handle_ai_generate_seo');
function temply_handle_ai_generate_seo() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');
    
    $title = isset($_POST['title']) ? $_POST['title'] : '';
    $content = isset($_POST['content']) ? wp_unslash($_POST['content']) : '';
    
    // Simulate AI generation Latency
    sleep(1);
    $prompt = "Bạn là chuyên gia SEO xuất sắc. Hãy tối ưu hoá cho bài viết có Tiêu đề: '" . $title . "' và nội dung: '" . mb_substr($content, 0, 1000) . "'.\n";
    $prompt .= "Yêu cầu trả về CHỈ MỘT cục JSON hợp lệ với 3 trường (không giải thích thêm):\n";
    $prompt .= '{"title": "Viết lại 1 tiêu đề SEO hấp dẫn dưới 60 ký tự", "slug": "tao-duong-dan-khong-dau-duoi-75-ky-tu", "description": "Viết 1 đoạn tóm tắt SEO thu hút dưới 160 ký tự"}';

    $gpt_text = tehi_call_ai_api($prompt, true, 15);

    if ($gpt_text === false) {
        wp_send_json_error(array('message' => 'Lỗi kết nối tới AI.'));
    }
    if (is_string($gpt_text) && strpos($gpt_text, 'CURL_ERROR|') === 0) {
        wp_send_json_error(array('message' => 'Lỗi kết nối tới AI: ' . str_replace('CURL_ERROR|', '', $gpt_text)));
    }
    if (is_string($gpt_text) && strpos($gpt_text, 'API_ERROR|') === 0) {
        wp_send_json_error(array('message' => 'API Error: ' . str_replace('API_ERROR|', '', $gpt_text)));
    }
    
    // Extract JSON from response text if it contains markdown ticks
    preg_match('/\{.*\}/s', $gpt_text, $matches);
    $clean_json = !empty($matches) ? $matches[0] : '';
    
    $seo_data = json_decode($clean_json, true);

    if (!$seo_data || !isset($seo_data['title'])) {
         // Fallback if AI didn't return valid JSON
         $seo_data = array(
             'title' => mb_substr($title, 0, 60),
             'slug'  => sanitize_title($title),
             'description' => mb_substr($content, 0, 150) . '...'
         );
    }
    
    wp_send_json_success($seo_data);
}

// AJAX Handler: Generate Thumbnail
add_action('wp_ajax_temply_ai_generate_thumbnail', 'temply_handle_ai_thumbnail');
function temply_handle_ai_thumbnail() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');
    
    $post_id = isset($_POST['post_id']) ? intval($_POST['post_id']) : 0;
    $title = isset($_POST['title']) ? sanitize_text_field($_POST['title']) : 'Fantasy Novel';
    $keyword = isset($_POST['keyword']) ? sanitize_text_field($_POST['keyword']) : '';
    
    if (!$post_id) {
        wp_send_json_error(array('message' => 'Lỗi ID truyện.'));
    }

    // Include required WP files for media sideloading
    require_once(ABSPATH . 'wp-admin/includes/media.php');
    require_once(ABSPATH . 'wp-admin/includes/file.php');
    require_once(ABSPATH . 'wp-admin/includes/image.php');

    // Mở rộng prompt để render Chibi/Anime dễ thương hoặc theo keyword của user.
    if (!empty($keyword)) {
        $prompt = $title . " " . $keyword . " , ultra detailed, masterpiece, vibrant high quality";
    } else {
        $prompt = $title . " comic book style cover, fantasy novel art, highly detailed, vivid colors";
    }
    
    // Nếu keyword có chữ chibi, nhồi thêm từ khóa cute để đảm bảo nét vẽ dễ thương
    if (stripos($keyword, 'chibi') !== false) {
        $prompt .= ", incredibly cute adorable chibi character, kawaii anime style, soft lighting, pastel colors";
    }
    
    // Use Pollinations AI (Free, no API key needed). Append random seed to ensure unique generation every time.
    $seed = wp_rand(10000, 99999);
    $image_url = 'https://image.pollinations.ai/prompt/' . urlencode($prompt) . '.jpg?width=1200&height=800&nologo=true&seed=' . $seed;
    
    // Download and attach the image to the post
    $attachment_id = media_sideload_image($image_url, $post_id, 'Cover for ' . $title, 'id');
    
    if (is_wp_error($attachment_id)) {
        wp_send_json_error(array('message' => 'Lỗi tải ảnh từ AI: ' . $attachment_id->get_error_message()));
    }

    // Also forcefully set the featured image of the post in backend
    set_post_thumbnail($post_id, $attachment_id);
    
    $attachment_url = wp_get_attachment_url($attachment_id);

    wp_send_json_success(array(
        'message' => 'Đã tạo và gắn ảnh bìa AI thành công!',
        'attachment_id' => $attachment_id,
        'image_url' => $attachment_url
    ));
}

// ==========================================
// Authentication System: Login & Register
// ==========================================

add_action('wp_ajax_nopriv_tehi_ajax_login', 'tehi_ajax_login');
function tehi_ajax_login() {
    $email = isset($_POST['user_email']) ? sanitize_email($_POST['user_email']) : '';
    $pass = isset($_POST['user_pass']) ? $_POST['user_pass'] : '';

    if (empty($email) || empty($pass)) {
        wp_send_json_error(['message' => 'Vui lòng nhập đầy đủ thông tin.']);
    }

    $login_data = array();
    $login_data['user_login'] = $email;
    $login_data['user_password'] = $pass;
    $login_data['remember'] = true;

    $user_verify = wp_signon($login_data, false);

    if (is_wp_error($user_verify)) {
        wp_send_json_error(['message' => 'Email hoặc Mật khẩu không chính xác.']);
    }

    wp_send_json_success(['message' => 'Đăng nhập thành công! Đang tải lại...']);
}

add_action('wp_ajax_nopriv_tehi_ajax_register', 'tehi_ajax_register');
function tehi_ajax_register() {
    $email = isset($_POST['user_email']) ? sanitize_email($_POST['user_email']) : '';
    $pass = isset($_POST['user_pass']) ? $_POST['user_pass'] : '';
    $display_map = isset($_POST['user_display']) ? sanitize_text_field($_POST['user_display']) : '';

    if (empty($email) || empty($pass) || empty($display_map)) {
        wp_send_json_error(['message' => 'Vui lòng nhập đầy đủ thông tin.']);
    }
    
    if (strlen($pass) < 6) {
        wp_send_json_error(['message' => 'Mật khẩu phải có tối thiểu 6 ký tự.']);
    }

    if (email_exists($email) || username_exists($email)) {
        wp_send_json_error(['message' => 'Email này đã được sử dụng.']);
    }

    $user_id = wp_create_user($email, $pass, $email);

    if (is_wp_error($user_id)) {
        wp_send_json_error(['message' => $user_id->get_error_message()]);
    }

    // Update display name
    wp_update_user(array('ID' => $user_id, 'display_name' => $display_map, 'nickname' => $display_map));

    // Send WordPress default welcome email to the user, and notify admin
    wp_new_user_notification($user_id, null, 'both');

    // Auto login
    $login_data = array(
        'user_login' => $email,
        'user_password' => $pass,
        'remember' => true
    );
    wp_signon($login_data, false);

    wp_send_json_success(['message' => 'Tạo tài khoản thành công! Đang tải lại...']);
}

// ==========================================
// AI Story Splitter Handler
// ==========================================
add_action('wp_ajax_temply_ai_split_chapters', 'temply_handle_ai_split_chapters');
function temply_handle_ai_split_chapters() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');

    $truyen_id = isset($_POST['post_id']) ? intval($_POST['post_id']) : 0;
    $content = isset($_POST['content']) ? wp_unslash($_POST['content']) : '';

    if (!$truyen_id || empty($content)) {
        wp_send_json_error(array('message' => 'Lỗi kết nối hoặc nội dung trống.'));
    }

    // ── Strategy 1: split by <h2>/<h3> tags ─────────────────────────────────
    $parts = preg_split('/(<h[1-6][^>]*>.*?<\/h[1-6]>)/is', $content, -1, PREG_SPLIT_DELIM_CAPTURE | PREG_SPLIT_NO_EMPTY);

    $chapters = [];
    $current_chapter_title   = '';
    $current_chapter_content = '';
    $count = 1;

    foreach ($parts as $part) {
        if (preg_match('/<h[1-6][^>]*>(.*?)<\/h[1-6]>/is', $part, $matches)) {
            $text_title = trim(strip_tags($matches[1]));
            if (preg_match('/(?:Chương|Chapter|Hồi)\s*\d+/iu', $text_title)) {
                if (!empty(trim($current_chapter_content)) || !empty($current_chapter_title)) {
                    $chapters[] = array(
                        'title'   => $current_chapter_title ?: ('Chương ' . $count),
                        'content' => $current_chapter_content
                    );
                    $count++;
                }
                $current_chapter_title   = $text_title;
                $current_chapter_content = '';
                continue;
            }
        }
        $current_chapter_content .= $part . "\n";
    }
    if (!empty(trim($current_chapter_content)) || !empty($current_chapter_title)) {
        $chapters[] = array(
            'title'   => $current_chapter_title ?: ('Chương ' . $count),
            'content' => $current_chapter_content
        );
    }

    // ── Strategy 2 (fallback): scan plain text for "Chương N" (even with markdown #) ─
    if (count($chapters) <= 1) {
        $chapters = [];
        $count    = 1;
        $current_chapter_title   = '';
        $current_chapter_content = '';

        // Strip tags and markdown
        $plain_text = wp_strip_all_tags($content);
        $plain_text = str_replace(["\r\n", "\r"], "\n", $plain_text);
        // Strip markdown heading markers
        $plain_text = preg_replace('/^#{1,6}\s+/m', '', $plain_text);
        $lines = explode("\n", $plain_text);

        foreach ($lines as $line) {
            $line = trim($line);
            if (empty($line)) continue;

            // Match: optional markdown # then "Chương N" with optional title
            if (preg_match('/^#*\s*((?:Chương|Chapter|Hồi)\s*\d+[^\r\n]*)/iu', $line, $hm)) {
                if (!empty(trim($current_chapter_content)) || !empty($current_chapter_title)) {
                    $chapters[] = ['title' => $current_chapter_title ?: ('Chương ' . $count), 'content' => $current_chapter_content];
                    $count++;
                }
                $current_chapter_title   = trim($hm[1]);
                $current_chapter_content = '';
            } else {
                $current_chapter_content .= '<p>' . esc_html($line) . '</p>' . "\n";
            }
        }
        if (!empty(trim($current_chapter_content)) || !empty($current_chapter_title)) {
            $chapters[] = ['title' => $current_chapter_title ?: ('Chương ' . $count), 'content' => $current_chapter_content];
        }
    }

    if (count($chapters) === 0) {
        wp_send_json_error(array('message' => 'Không tìm thấy tiêu đề "Chương N" nào để tách. Hãy kiểm tra lại nội dung.'));
    }

    $created = 0;
    foreach ($chapters as $ch) {
        $post_data = array(
            'post_title'    => wp_strip_all_tags($ch['title']),
            'post_content'  => trim($ch['content']),
            'post_status'   => 'publish',
            'post_type'     => 'chuong'
        );
        $chuong_id = wp_insert_post($post_data);
        if ($chuong_id && !is_wp_error($chuong_id)) {
            update_post_meta($chuong_id, '_truyen_id', $truyen_id);
            $created++;
        }
    }

    wp_send_json_success(array(
        'count' => $created,
        'message' => 'Thành công'
    ));
}

// ==========================================
// STORY STUDIO: Create Draft Post
// ==========================================
add_action('wp_ajax_temply_studio_create_draft', 'temply_studio_create_draft');
function temply_studio_create_draft() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');
    
    $title = isset($_POST['title']) ? sanitize_text_field($_POST['title']) : 'Truyện chưa đặt tên';

    $post_id = wp_insert_post(array(
        'post_title'  => $title,
        'post_status' => 'draft',
        'post_type'   => 'truyen',
        'post_author' => get_current_user_id()
    ));

    if (is_wp_error($post_id)) {
        wp_send_json_error(array('message' => 'Không tạo được bài viết: ' . $post_id->get_error_message()));
    }

    wp_send_json_success(array('post_id' => $post_id));
}

// ==========================================
// STORY STUDIO: Get Prompt + Key (JS will call Gemini directly)
// ==========================================
add_action('wp_ajax_temply_studio_get_prompt', 'temply_studio_get_prompt');
function temply_studio_get_prompt() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');

    $title    = isset($_POST['title']) ? sanitize_text_field($_POST['title']) : '';
    $prompt   = isset($_POST['prompt']) ? sanitize_textarea_field($_POST['prompt']) : '';
    $genre    = isset($_POST['genre']) ? sanitize_text_field($_POST['genre']) : 'Phổ thông';
    $chapters = isset($_POST['chapters']) ? intval($_POST['chapters']) : 10;
    $tone     = isset($_POST['tone']) ? sanitize_text_field($_POST['tone']) : 'Hài hước, sảng văn';

    if (!$title || !$prompt) {
        wp_send_json_error(array('message' => 'Thiếu thông tin.'));
    }

    $chapters = max(3, min(20, $chapters));

    $ai_prompt  = "Bạn là một nhà văn sáng tác truyện chuyên nghiệp người Việt.\n";
    $ai_prompt .= "Hãy viết một bộ truyện hoàn chỉnh với tiêu đề: \"$title\".\n";
    $ai_prompt .= "Thể loại: $genre. Giọng văn: $tone.\n";
    $ai_prompt .= "Ý tưởng cốt lõi: $prompt\n\n";
    $ai_prompt .= "YÊU CẦU BẮT BUỘC:\n";
    $ai_prompt .= "1. Viết đúng $chapters chương, mỗi chương khoảng 1500-2500 từ tiếng Việt (đủ nội dung, hấp dẫn, không tóm tắt sơ sài).\n";
    $ai_prompt .= "2. Mỗi chương BẮT BUỘC phải bắt đầu bằng TIÊU ĐỀ theo format CHÍNH XÁC: \"Chương [số]: [tên chương]\" trên một dòng riêng biệt.\n";
    $ai_prompt .= "3. Các chương phải liên kết mạch lạc, cốt truyện nhất quán, không mâu thuẫn.\n";
    $ai_prompt .= "4. Phong cách viết hấp dẫn, có đối thoại, mô tả cảm xúc sinh động.\n";
    $ai_prompt .= "5. Kết thúc chương cuối phải hoàn chỉnh, có hậu (Happy ending hoặc Open ending).\n";
    $ai_prompt .= "6. KHÔNG viết thêm bất kỳ ghi chú nào ngoài nội dung truyện.\n";
    $ai_prompt .= "Hãy bắt đầu viết ngay bây giờ:";

    $gemini_key = tehi_get_gemini_key();

    wp_send_json_success(array(
        'prompt'      => $ai_prompt,
        'gemini_key'  => $gemini_key,
        'has_key'     => true
    ));
}


add_action('wp_ajax_temply_studio_generate_story', 'temply_studio_generate_story');
function temply_studio_generate_story() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');

    $post_id  = isset($_POST['post_id']) ? intval($_POST['post_id']) : 0;
    $title    = isset($_POST['title']) ? sanitize_text_field($_POST['title']) : '';
    $prompt   = isset($_POST['prompt']) ? sanitize_textarea_field($_POST['prompt']) : '';
    $genre    = isset($_POST['genre']) ? sanitize_text_field($_POST['genre']) : 'Phổ thông';
    $chapters = isset($_POST['chapters']) ? intval($_POST['chapters']) : 10;
    $tone     = isset($_POST['tone']) ? sanitize_text_field($_POST['tone']) : 'Hài hước, sảng văn';
    $ai_model = isset($_POST['ai_model']) ? sanitize_text_field($_POST['ai_model']) : 'gemini-2.5-flash';

    if (!$post_id || !$title || !$prompt) {
        wp_send_json_error(array('message' => 'Thiếu thông tin đầu vào.'));
    }

    // Clamp chapters to valid range
    $chapters = max(3, min(20, $chapters));

    // Build AI prompt
    $ai_prompt  = "Bạn là một nhà văn sáng tác truyện chuyên nghiệp người Việt.\n";
    $ai_prompt .= "Hãy viết một bộ truyện hoàn chỉnh với tiêu đề: \"$title\".\n";
    $ai_prompt .= "Thể loại: $genre. Giọng văn: $tone.\n";
    $ai_prompt .= "Ý tưởng cốt lõi: $prompt\n\n";
    $ai_prompt .= "YÊU CẦU BẮT BUỘC:\n";
    $ai_prompt .= "1. Viết đúng $chapters chương, mỗi chương khoảng 1500-2500 từ tiếng Việt (đủ nội dung, hấp dẫn, không tóm tắt sơ sài).\n";
    $ai_prompt .= "2. Mỗi chương BẮT BUỘC phải bắt đầu bằng TIÊU ĐỀ theo format CHÍNH XÁC: \"Chương [số]: [tên chương]\" trên một dòng riêng biệt.\n";
    $ai_prompt .= "3. Các chương phải liên kết mạch lạc, cốt truyện nhất quán, không mâu thuẫn.\n";
    $ai_prompt .= "4. Phong cách viết hấp dẫn, có đối thoại, mô tả cảm xúc sinh động.\n";
    $ai_prompt .= "5. Kết thúc chương cuối phải hoàn chỉnh, có hậu (Happy ending hoặc Open ending).\n";
    $ai_prompt .= "6. KHÔNG viết thêm bất kỳ ghi chú nào ngoài nội dung truyện.\n";
    $ai_prompt .= "Hãy bắt đầu viết ngay bây giờ:";

    $raw_text = tehi_call_ai_api($ai_prompt, false, 90, $ai_model);

    if ($raw_text === false) {
        wp_send_json_error(array('message' => 'Lỗi mạng nội bộ không xác định.'));
    }
    if (strpos($raw_text, 'CURL_ERROR|') === 0) {
        wp_send_json_error(array('message' => 'Lỗi hệ thống: ' . str_replace('CURL_ERROR|', '', $raw_text)));
    }
    if (strpos($raw_text, 'API_ERROR|') === 0) {
        wp_send_json_error(array('message' => 'Google Gemini báo lỗi: ' . str_replace('API_ERROR|', '', $raw_text)));
    }

    if (empty(trim($raw_text))) {
        wp_send_json_error(array('message' => 'AI không trả về nội dung. Thử lại sau giây lát.'));
    }

    // Convert plain-text story to clean HTML for the editor
    // Split by chapter headings
    $lines    = explode("\n", $raw_text);
    $html     = '';
    foreach ($lines as $line) {
        $line = trim($line);
        if (empty($line)) continue;

        if (preg_match('/^(Chương\s+\d+[:\-–.]\s*.+)$/iu', $line)) {
            $html .= '<h2>' . esc_html($line) . '</h2>' . "\n";
        } else {
            $html .= '<p>' . esc_html($line) . '</p>' . "\n";
        }
    }

    // Save content to the draft post
    wp_update_post(array(
        'ID'           => $post_id,
        'post_content' => $html,
        'post_status'  => 'draft'
    ));

    wp_send_json_success(array(
        'content' => $html,
        'post_id' => $post_id
    ));
}

// ==========================================
// STORY STUDIO: Save Content sent from Browser
// ==========================================
add_action('wp_ajax_temply_studio_save_content', 'temply_studio_save_content');
function temply_studio_save_content() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');

    $post_id  = isset($_POST['post_id']) ? intval($_POST['post_id']) : 0;
    $raw_text = isset($_POST['raw_text']) ? wp_unslash($_POST['raw_text']) : '';

    if (!$post_id || empty($raw_text)) {
        wp_send_json_error(array('message' => 'Thiếu dữ liệu.'));
    }

    // 1. Normalize Windows/Mac line endings
    $raw_text = str_replace(["\r\n", "\r"], "\n", $raw_text);

    // 2. Strip any HTML tags (browser contenteditable may send HTML)
    $raw_text = wp_strip_all_tags($raw_text);

    // 3. Strip markdown heading markers (# ## ### at line start)
    $raw_text = preg_replace('/^#{1,6}\s+/m', '', $raw_text);

    // 4. Convert plain text to clean HTML
    $lines = explode("\n", $raw_text);
    $html  = '';
    foreach ($lines as $line) {
        $line = trim($line);
        if (empty($line)) continue;
        // Match "Chương N" with optional separator and optional title
        if (preg_match('/^(Chương\s+\d+(?:[:\-–.].*)?)\s*$/iu', $line)) {
            $html .= '<h2>' . esc_html($line) . '</h2>' . "\n";
        } else {
            $html .= '<p>' . esc_html($line) . '</p>' . "\n";
        }
    }

    wp_update_post(array(
        'ID'           => $post_id,
        'post_content' => $html,
        'post_status'  => 'draft'
    ));

    wp_send_json_success(array(
        'content' => $html,
        'post_id' => $post_id
    ));
}

// ==========================================
// STORY STUDIO: Get Autodetect Prompt (Browser-side AI)
// ==========================================
add_action('wp_ajax_temply_studio_autodetect_prompt', 'temply_studio_autodetect_prompt');
function temply_studio_autodetect_prompt() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');

    $prompt = isset($_POST['prompt']) ? sanitize_textarea_field($_POST['prompt']) : '';
    if (empty($prompt)) {
        wp_send_json_error(array('message' => 'Prompt rỗng.'));
    }

    $genre_list = 'Ngôn Tình, Tiên Hiệp, Hài Hước, Trinh Thám, Kiếm Hiệp, Huyền Huyễn, Trọng Sinh, Đô Thị, Dị Giới, Võ Hiệp, Xuyên Không, Gia Đấu, Học Đường, Cung Đấu, Mạt Thế, Zombie, Quân Sự, Khoa Huyễn, Kinh Dị, Game, Điền Văn, Đam Mỹ, Nữ Cường, Lịch Sử, Thể Thao, Vả Mặt, Hệ Thống, Không Gian';
    $tone_list  = 'lãng mạn, huyền bí, hài hước, hùng tráng, kinh dị, trinh thám, hồi hộp, nhẹ nhàng, cuồng nhiệt, triết lý';

    $ai_prompt  = "Phân tích ý tưởng truyện sau và gợi ý phù hợp nhất:\n";
    $ai_prompt .= "\"$prompt\"\n\n";
    $ai_prompt .= "Danh sách thể loại có thể chọn: $genre_list\n";
    $ai_prompt .= "Danh sách giọng văn có thể chọn: $tone_list\n\n";
    $ai_prompt .= "Trả về CHỈ MỘT JSON hợp lệ (không giải thích thêm):\n";
    $ai_prompt .= '{"genres": ["Thể loại 1", "Thể loại 2"], "tone": "giọng văn phù hợp nhất"}';

    $gemini_key = tehi_get_gemini_key();

    wp_send_json_success(array(
        'ai_prompt'  => $ai_prompt,
        'gemini_key' => $gemini_key,
        'has_key'    => true
    ));
}

// ==========================================
// STORY STUDIO: Server-side URL Scraper
// (Works for tehitruyen.com + non-Cloudflare sites)
// ==========================================
add_action('wp_ajax_temply_studio_scrape_url', 'temply_studio_scrape_url');
function temply_studio_scrape_url() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');

    $url         = isset($_POST['url']) ? esc_url_raw($_POST['url']) : '';
    $multi_count = isset($_POST['chapters']) ? intval($_POST['chapters']) : 1;

    if (empty($url)) {
        wp_send_json_error(array('message' => 'Thiếu URL.'));
    }

    // Security: Only allow whitelisted Vietnamese story sites
    $allowed_hosts = array('tehitruyen.com', 'truyenfull.vn', 'metruyenchu.com', 'truyencv.com', 'tangthuvien.vn', 'metruyenhot.com');
    $host = parse_url($url, PHP_URL_HOST);
    $host = preg_replace('/^www\./', '', $host);
    if (!in_array($host, $allowed_hosts)) {
        wp_send_json_error(array('message' => "Site '$host' chưa được hỗ trợ cào server-side. Dùng Bookmarklet để cào."));
    }

    $multi_count = max(1, min(10, $multi_count)); // max 10 chapters at once

    // Selectors per domain (priority order)
    $selectors = array(
        'tehitruyen.com'   => array('#noi_dung_truyen', '.chapter-content', '#box_doc'),
        'truyenfull.vn'    => array('#chapter-c', '.chapter-c', '#box_doc'),
        'default'          => array('#chapter-c', '.chapter-c', '#box_doc', '.content', 'article'),
    );
    $domain_selectors = isset($selectors[$host]) ? $selectors[$host] : $selectors['default'];

    // Chapter URL pattern for tehitruyen: ?chuong=N
    $all_text  = '';
    $title     = '';
    $errors    = 0;

    for ($i = 0; $i < $multi_count; $i++) {
        // Build chapter URL
        if ($i === 0) {
            $chapter_url = $url;
        } else {
            // Try to increment chapter number in URL
            if (strpos($url, '?chuong=') !== false) {
                $base   = preg_replace('/\?chuong=\d+/', '', $url);
                $cur_ch = intval(preg_replace('/.*\?chuong=/', '', $url));
                $chapter_url = $base . '?chuong=' . ($cur_ch + $i);
            } elseif (preg_match('/chuong-(\d+)/', $url, $m)) {
                $chapter_url = str_replace('chuong-' . $m[1], 'chuong-' . ($m[1] + $i), $url);
            } else {
                break; // Can't determine next chapter URL
            }
        }

        $response = wp_remote_get($chapter_url, array(
            'timeout'    => 20,
            'sslverify'  => false,
            'user-agent' => 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'headers'    => array('Accept-Language' => 'vi-VN,vi;q=0.9'),
        ));

        if (is_wp_error($response)) { $errors++; continue; }

        $html = wp_remote_retrieve_body($response);
        if (empty($html)) { $errors++; continue; }

        // Extract title from first chapter
        if ($i === 0 && preg_match('/<h1[^>]*>(.*?)<\/h1>/is', $html, $tm)) {
            $title = trim(strip_tags($tm[1]));
        }
        if ($i === 0 && empty($title) && preg_match('/<title>(.*?)<\/title>/is', $html, $tm)) {
            $title = trim(strip_tags($tm[1]));
        }

        // Extract content using domain selectors (supports both #id and .class)
        $text = '';
        foreach ($domain_selectors as $selector) {
            if (strpos($selector, '#') === 0) {
                // ID selector: <div id="...">
                $id = preg_quote(substr($selector, 1), '/');
                if (preg_match('/<[^>]+id=["\']' . $id . '["\'][^>]*>(.*?)<\/(?:div|section|article)>/is', $html, $m)) {
                    $text = strip_tags($m[1], '');
                } elseif (preg_match('/id=["\']' . $id . '["\'][^>]*>([\s\S]{200,}?)(?=<div(?:\s[^>]*)?\s+id="|<footer|<\/main|<\/body)/i', $html, $m)) {
                    $text = strip_tags($m[1], '');
                }
            } elseif (strpos($selector, '.') === 0) {
                // Class selector: <div class="...">
                $cls = preg_quote(substr($selector, 1), '/');
                if (preg_match('/<[^>]+class=["\'][^"\']*' . $cls . '[^"\']*["\'][^>]*>([\s\S]{200,}?)(?=<div(?:\s[^>]*)?\s+(?:id|class)="|<footer|<\/main|<\/body)/i', $html, $m)) {
                    $text = strip_tags($m[1], '');
                }
            }

            if (!empty($text)) {
                $text = html_entity_decode($text, ENT_QUOTES | ENT_HTML5, 'UTF-8');
                $text = preg_replace('/[ \t]+/', ' ', $text);
                $text = preg_replace('/\n{3,}/', "\n\n", $text);
                $text = trim($text);
            }

            if (strlen($text) > 200) break;
        }

        if (strlen($text) > 200) {
            $all_text .= "\n\n" . $text;
        }

        usleep(300000); // 0.3s delay between requests
    }

    $all_text = trim($all_text);
    if (empty($all_text)) {
        wp_send_json_error(array('message' => 'Không trích xuất được nội dung. Hãy thử Bookmarklet hoặc paste thủ công.'));
    }

    $words = str_word_count($all_text);

    wp_send_json_success(array(
        'text'      => $all_text,
        'title'     => $title,
        'source'    => $host,
        'wordCount' => $words,
        'chapters'  => $multi_count - $errors,
    ));
}

// ==========================================
// STORY STUDIO: Schedule Post Publishing
// ==========================================
add_action('wp_ajax_temply_studio_schedule', 'temply_studio_schedule');
function temply_studio_schedule() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');

    $post_id      = isset($_POST['post_id']) ? intval($_POST['post_id']) : 0;
    $publish_date = isset($_POST['publish_date']) ? sanitize_text_field($_POST['publish_date']) : '';
    $status       = isset($_POST['status']) ? sanitize_text_field($_POST['status']) : 'publish';

    if (!$post_id) {
        wp_send_json_error(array('message' => 'Không có ID bài viết.'));
    }

    $update_data = array('ID' => $post_id);

    if (!empty($publish_date)) {
        // Schedule for specific date/time
        $date_gmt = get_gmt_from_date($publish_date);
        $update_data['post_date']     = $publish_date;
        $update_data['post_date_gmt'] = $date_gmt;
        $update_data['post_status']   = 'future'; // WordPress scheduled
        $msg = 'Lịch đăng đã được cài vào: ' . $publish_date;
    } else {
        // Publish now
        $update_data['post_status'] = 'publish';
        $msg = 'Đã đăng bài ngay!';
    }

    $result = wp_update_post($update_data);

    if (is_wp_error($result)) {
        wp_send_json_error(array('message' => 'Lỗi: ' . $result->get_error_message()));
    }

    wp_send_json_success(array('message' => $msg, 'post_id' => $post_id));
}

// ==========================================
// STORY STUDIO: Auto-detect Genre & Tone
// ==========================================
add_action('wp_ajax_temply_studio_autodetect', 'temply_studio_autodetect');
function temply_studio_autodetect() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');

    $prompt   = isset($_POST['prompt']) ? sanitize_textarea_field($_POST['prompt']) : '';
    $ai_model = isset($_POST['ai_model']) ? sanitize_text_field($_POST['ai_model']) : 'gemini-2.5-flash';

    if (empty($prompt)) {
        wp_send_json_error(array('message' => 'Prompt rỗng.'));
    }

    $genre_list = 'Ngôn Tình, Tiên Hiệp, Hài Hước, Trinh Thám, Kiếm Hiệp, Huyền Huyễn, Trọng Sinh, Đô Thị, Dị Giới, Võ Hiệp, Xuyên Không, Gia Đấu, Học Đường, Cung Đấu, Mạt Thế, Zombie, Quân Sự, Khoa Huyễn, Kinh Dị, Game, Điền Văn, Đam Mỹ, Nữ Cường, Lịch Sử, Thể Thao, Vả Mặt, Hệ Thống, Không Gian';
    $tone_list  = 'lãng mạn, huyền bí, hài hước, hùng tráng, kinh dị, trinh thám, hồi hộp, nhẹ nhàng, cuồng nhiệt, triết lý';

    $ai_prompt = "Phân tích ý tưởng truyện sau và gợi ý phù hợp nhất:\n";
    $ai_prompt .= "\"$prompt\"\n\n";
    $ai_prompt .= "Danh sách thể loại có thể chọn: $genre_list\n";
    $ai_prompt .= "Trọng tâm là 30 ký tự cuối. Hãy suy luận.\n";
    $ai_prompt .= "Trả về CHỈ MỘT JSON hợp lệ (không giải thích thêm):\n";
    $ai_prompt .= '{"genres": ["Thể loại 1", "Thể loại 2"], "tone": "giọng văn phù hợp nhất"}';

    $raw = tehi_call_ai_api($ai_prompt, true, 25, $ai_model);

    if ($raw === false) {
        wp_send_json_error(array('message' => 'Lỗi kết nối AI.'));
    }
    if (is_string($raw) && strpos($raw, 'CURL_ERROR|') === 0) {
        wp_send_json_error(array('message' => 'Lỗi kết nối AI: ' . str_replace('CURL_ERROR|', '', $raw)));
    }
    if (is_string($raw) && strpos($raw, 'API_ERROR|') === 0) {
        wp_send_json_error(array('message' => 'API Error: ' . str_replace('API_ERROR|', '', $raw)));
    }

    preg_match('/\{.*\}/s', $raw, $matches);
    $data = json_decode(!empty($matches) ? $matches[0] : $raw, true);

    if (!$data || !isset($data['genres'])) {
        wp_send_json_error(array('message' => 'AI không gợi ý được. Thử lại.'));
    }

    wp_send_json_success(array(
        'genres' => array_slice((array)$data['genres'], 0, 3),
        'tone'   => isset($data['tone']) ? $data['tone'] : 'lãng mạn'
    ));
}
