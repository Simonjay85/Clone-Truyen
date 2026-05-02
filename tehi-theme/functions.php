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
    // Most theme CSS is emitted in header.php with async hints. Keep WP hooks alive
    // for plugin compatibility and scripts that depend on wp_head/wp_footer.
    wp_enqueue_style( 'tehi-clone-style', get_stylesheet_uri(), array(), wp_get_theme()->get('Version') );
    wp_enqueue_script( 'bootstrap-js', 'https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.3/js/bootstrap.bundle.min.js', array(), null, true );
}
add_action( 'wp_enqueue_scripts', 'tehi_clone_scripts' );

function tehi_get_meta_description() {
    if (is_singular()) {
        $excerpt = get_the_excerpt();
        if (!$excerpt) {
            $excerpt = get_post_field('post_content', get_the_ID());
        }
        $excerpt = trim(wp_strip_all_tags(strip_shortcodes((string) $excerpt)));
        if ($excerpt !== '') {
            return wp_trim_words($excerpt, 28, '...');
        }
    }

    if (is_search()) {
        return sprintf('Kết quả tìm kiếm truyện cho "%s" tại %s.', get_search_query(), get_bloginfo('name'));
    }

    if (is_tax()) {
        $term = get_queried_object();
        if ($term && !is_wp_error($term)) {
            return sprintf('Đọc truyện thể loại %s mới nhất, cập nhật nhanh tại %s.', $term->name, get_bloginfo('name'));
        }
    }

    $description = get_bloginfo('description');
    if (!$description) {
        $description = get_bloginfo('name') . ' - Đọc Truyện Online, truyện ngôn tình, truyện full và chương mới cập nhật mỗi ngày.';
    }

    return $description;
}

function tehi_get_canonical_url() {
    $request_uri = isset($_SERVER['REQUEST_URI']) ? wp_unslash($_SERVER['REQUEST_URI']) : '/';
    $path = parse_url($request_uri, PHP_URL_PATH);

    $legacy_map = array(
        '/the-loai.html'            => '/the-loai/',
        '/danh-muc.html'            => '/the-loai/',
        '/theo-doi.html'            => '/theo-doi/',
        '/bang-xep-hang.html'       => '/bang-xep-hang/',
        '/hoan-thanh.html'          => '/truyen-hoan-thanh/',
        '/truyen-moi-cap-nhat.html' => '/truyen-moi-cap-nhat/',
        '/nhom-dich.html'           => '/nhom-dich/',
    );

    if ($path && isset($legacy_map[$path])) {
        return home_url($legacy_map[$path]);
    }

    if (is_singular() || is_page() || is_home() || is_front_page()) {
        return get_permalink();
    }

    if (is_search()) {
        return home_url('/?s=' . rawurlencode(get_search_query()));
    }

    if (is_tax() || is_category() || is_tag()) {
        $link = get_term_link(get_queried_object());
        if (!is_wp_error($link)) {
            return $link;
        }
    }

    return home_url($path ?: '/');
}

function tehi_current_legacy_page_title() {
    $request_uri = isset($_SERVER['REQUEST_URI']) ? wp_unslash($_SERVER['REQUEST_URI']) : '';
    $path = parse_url($request_uri, PHP_URL_PATH);
    $titles = array(
        '/the-loai.html'            => 'Thể loại',
        '/danh-muc.html'            => 'Thể loại',
        '/theo-doi.html'            => 'Theo dõi',
        '/bang-xep-hang.html'       => 'Bảng xếp hạng',
        '/hoan-thanh.html'          => 'Truyện full',
        '/truyen-moi-cap-nhat.html' => 'Truyện mới cập nhật',
        '/nhom-dich.html'           => 'Nhóm dịch',
    );

    return ($path && isset($titles[$path])) ? $titles[$path] : '';
}

add_filter('pre_get_document_title', function($title) {
    $site_name = get_bloginfo('name') ?: 'DTT';

    if (is_front_page() || is_home()) {
        return $site_name . ' - Đọc Truyện Online';
    }

    $legacy_title = tehi_current_legacy_page_title();
    if ($legacy_title) {
        return $legacy_title . ' - ' . $site_name;
    }

    if (is_search()) {
        return get_search_query() . ' - ' . $site_name;
    }

    if (is_singular() || is_page()) {
        return single_post_title('', false) . ' - ' . $site_name;
    }

    if (is_tax() || is_category() || is_tag()) {
        return single_term_title('', false) . ' - ' . $site_name;
    }

    return trim((string) $title) ?: $site_name;
}, 20);

add_filter('document_title_separator', function() {
    return '-';
});

/**
 * Inject Tailwind CDN + Material Symbols để các template cũ render đúng
 */
add_action('wp_head', function() {
    if (!is_front_page()) {
        echo '<script>window.tailwind=window.tailwind||{};window.tailwind.config={corePlugins:{preflight:false},theme:{extend:{colors:{"surface-container-lowest":"#ffffff","surface-container-low":"#f6f3f2","surface-container":"#f0eded","surface-container-high":"#eae8e7","surface-container-highest":"#e4e2e1","surface-bright":"#fbf9f8","surface":"#fbf9f8","on-surface":"#1b1c1c","on-surface-variant":"#404752","outline":"#707783","outline-variant":"#c0c7d4","primary":"#0060a9","primary-container":"#3f9cfb","on-primary":"#ffffff","on-primary-container":"#00325c","secondary":"#536068","secondary-container":"#d4e2eb","on-secondary-container":"#57656c","background":"#fbf9f8","on-background":"#1b1c1c"}}}};</script>' . "\n";
        echo '<script src="https://cdn.tailwindcss.com"></script>' . "\n";
    }
    echo '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&display=swap">' . "\n";
}, 1);

add_action('template_redirect', function() {
    $request_uri = isset($_SERVER['REQUEST_URI']) ? wp_unslash($_SERVER['REQUEST_URI']) : '';
    $path = parse_url($request_uri, PHP_URL_PATH);

    if ($path === '/sitemap_index.xml') {
        status_header(200);
        header('Content-Type: application/xml; charset=UTF-8');
        echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n";
        echo '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' . "\n";
        echo '  <sitemap><loc>' . esc_url(home_url('/wp-sitemap.xml')) . '</loc></sitemap>' . "\n";
        echo '</sitemapindex>';
        exit;
    }
}, 0);

add_filter('robots_txt', function($output, $public) {
    if (strpos($output, 'sitemap_index.xml') === false) {
        $output = rtrim($output) . "\nSitemap: " . home_url('/sitemap_index.xml') . "\n";
    }
    return $output;
}, 10, 2);

add_action('admin_init', function() {
    register_setting('general', 'tehi_facebook_group_url', array(
        'type' => 'string',
        'sanitize_callback' => 'esc_url_raw',
        'default' => '',
    ));
    register_setting('general', 'tehi_unlock_guide_url', array(
        'type' => 'string',
        'sanitize_callback' => 'esc_url_raw',
        'default' => '',
    ));
    register_setting('general', 'tehi_backfill_token', array(
        'type' => 'string',
        'sanitize_callback' => 'sanitize_text_field',
        'default' => '',
    ));

    add_settings_section('tehi_social_settings', 'DTT Reading Settings', '__return_false', 'general');

    add_settings_field('tehi_facebook_group_url', 'Facebook group URL', function() {
        printf(
            '<input type="url" class="regular-text" name="tehi_facebook_group_url" value="%s" placeholder="https://facebook.com/groups/..." />',
            esc_attr(get_option('tehi_facebook_group_url', ''))
        );
    }, 'general', 'tehi_social_settings');

    add_settings_field('tehi_unlock_guide_url', 'Unlock guide URL', function() {
        printf(
            '<input type="url" class="regular-text" name="tehi_unlock_guide_url" value="%s" placeholder="%s" />',
            esc_attr(get_option('tehi_unlock_guide_url', '')),
            esc_attr(home_url('/huong-dan-mo-khoa/'))
        );
    }, 'general', 'tehi_social_settings');

    add_settings_field('tehi_backfill_token', 'Cover backfill token', function() {
        printf(
            '<input type="text" class="regular-text" name="tehi_backfill_token" value="%s" autocomplete="off" /> <p class="description">Optional token for auto_cover.py when not using an admin session.</p>',
            esc_attr(get_option('tehi_backfill_token', ''))
        );
    }, 'general', 'tehi_social_settings');
});

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
 * Đăng ký cron schedule mới: 1 Phút / Lần để ép xung Auto Pilot cực hạn
 */
add_filter('cron_schedules', function($schedules) {
    if (!isset($schedules['every_minute'])) {
        $schedules['every_minute'] = array(
            'interval' => 60,
            'display'  => __('Mỗi 1 Phút (Tốc biến)')
        );
    }
    return $schedules;
});

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

// ==========================================
// MINIMALIST ADMIN UI
// ==========================================

/**
 * 1. Dọn dẹp Dashboard & Ẩn các menu không cần thiết
 */
add_action('wp_dashboard_setup', 'minimalist_clean_dashboard');
function minimalist_clean_dashboard() {
    global $wp_meta_boxes;
    unset($wp_meta_boxes['dashboard']['normal']['core']['dashboard_right_now']);
    unset($wp_meta_boxes['dashboard']['normal']['core']['dashboard_activity']);
    unset($wp_meta_boxes['dashboard']['side']['core']['dashboard_quick_press']);
    unset($wp_meta_boxes['dashboard']['side']['core']['dashboard_primary']);
}

// Ẩn bớt thông báo rác (Admin Notices)
add_action('admin_head', 'minimalist_hide_notices');
function minimalist_hide_notices() {
    echo '<style>.notice, .update-nag { display: none !important; }</style>';
}

// ───────────────────────────────────────────
// 4. BỘ GIAO DIỆN QUẢN TRỊ (ADMIN) - VINTAGE MODE
// ───────────────────────────────────────────
function tehi_vintage_admin_styles() {
    // Gọi file CSS đổi màu hoài cổ (giữ nguyên cấu trúc HTML gốc để max tốc độ)
    wp_enqueue_style(
        'tehi-vintage-admin-css',
        get_template_directory_uri() . '/assets/css/vintage-admin.css',
        array(),
        '1.0.0'
    );
}
add_action('admin_enqueue_scripts', 'tehi_vintage_admin_styles');

// Apply the same admin bar style to the frontend if the admin bar is showing
add_action('wp_enqueue_scripts', function() {
    if ( is_admin_bar_showing() ) {
        tehi_vintage_admin_styles();
    }
});

/**
 * 2.1. Nạp Giao diện màn hình Đăng nhập (Login screen)
 */
function blue_horizon_login_enqueue() {
    wp_enqueue_style( 'blue-horizon-login-css', get_template_directory_uri() . '/assets/css/blue-horizon-login.css', array(), '1.0', 'all' );
}
add_action( 'login_enqueue_scripts', 'blue_horizon_login_enqueue' );
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

    $chapters = [];
    $count = 1;
    $current_chapter_title = '';
    $current_chapter_content = '';
    $story_title = '';
    $story_desc = '';
    $parsing_state = 'init';

    // Strip tags and markdown
    $plain_text = wp_strip_all_tags($content);
    $plain_text = str_replace(["\r\n", "\r"], "\n", $plain_text);
    // Strip markdown heading markers
    $plain_text = preg_replace('/^#{1,6}\s+/m', '', $plain_text);
    $lines = explode("\n", $plain_text);

    foreach ($lines as $line) {
        $trim_line = trim($line);
        if (empty($trim_line)) continue;

        if (preg_match('/^(?:Tiêu đề|Title|Tên truyện):\s*(.+)/iu', $trim_line, $m)) {
            $story_title = trim($m[1]);
            $story_title = preg_replace('/^["\']|["\']$/', '', $story_title);
            continue;
        }

        if (preg_match('/^(?:Mô tả|Synopsis|Description|Tóm tắt):\s*(.*)/iu', $trim_line, $m)) {
            $story_desc = '';
            if (!empty(trim($m[1]))) {
                $story_desc .= '<p>' . esc_html(trim($m[1])) . '</p>' . "\n";
            }
            $parsing_state = 'desc';
            continue;
        }

        // Match: "Chương N" with optional title
        if (preg_match('/^(?:#|\*)*\s*((?:Chương|Chapter|Hồi)\s*\d+[^\r\n]*)/iu', $trim_line, $hm)) {
            if ($parsing_state === 'chapter') {
                if (!empty(trim($current_chapter_content)) || !empty($current_chapter_title)) {
                    $chapters[] = ['title' => $current_chapter_title ?: ('Chương ' . $count), 'content' => $current_chapter_content];
                    $count++;
                }
            }
            $current_chapter_title   = trim($hm[1]);
            $current_chapter_title   = preg_replace('/^[*_]+|[*_]+$/', '', $current_chapter_title); // remove markdown bolds in title
            // Clean up literal "Title:" outputs from AI
            $current_chapter_title   = preg_replace('/(?i)(Chương\s+\d+[\s:\-]*)(?:Title|Tiêu đề):\s*/u', '$1', $current_chapter_title);
            // Clean up duplicated "Chương X: Chương X"
            $current_chapter_title   = preg_replace('/(?i)(Chương\s+\d+[\s:\-]+)(?:Chương\s+\d+[\s:\-]+)+/u', '$1', $current_chapter_title);
            $current_chapter_content = '';
            $parsing_state = 'chapter';
            continue;
        }

        // Append text based on current state
        if ($parsing_state === 'desc') {
            $story_desc .= '<p>' . esc_html($trim_line) . '</p>' . "\n";
        } elseif ($parsing_state === 'chapter') {
            $current_chapter_content .= '<p>' . esc_html($trim_line) . '</p>' . "\n";
        }
    }

    if ($parsing_state === 'chapter' && (!empty(trim($current_chapter_content)) || !empty($current_chapter_title))) {
        $chapters[] = ['title' => $current_chapter_title ?: ('Chương ' . $count), 'content' => $current_chapter_content];
    }

    if (count($chapters) === 0) {
        wp_send_json_error(array('message' => 'Không tìm thấy tiêu đề "Chương N" nào để tách. Hãy kiểm tra lại nội dung.'));
    }

    $created = 0;
    $first_chapter_excerpt = '';
    foreach ($chapters as $idx => $ch) {
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
            // Grab first few words from chapter 1 to use as story synopsis
            if ($idx === 0 && empty($first_chapter_excerpt)) {
                $plain = wp_strip_all_tags(trim($ch['content']));
                $first_chapter_excerpt = wp_trim_words($plain, 120, '...');
            }
        }
    }

    // ── Clear the parent truyen post_content (replace with short synopsis) ──
    // This prevents the story page from showing 10,000+ words in the intro box
    if ($created > 0) {
        $final_desc = !empty($story_desc) ? $story_desc : $first_chapter_excerpt;
        $update_payload = array(
            'ID'           => $truyen_id,
            'post_content' => $final_desc,
            'post_excerpt' => wp_trim_words(wp_strip_all_tags($final_desc), 50, '...'),
        );
        if (!empty($story_title)) {
            $update_payload['post_title'] = $story_title;
        }
        wp_update_post($update_payload);
    }

    wp_send_json_success(array(
        'count'   => $created,
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

    // ── Update Categories/Genres ──
    $genre_str = isset($_POST['genre']) ? sanitize_text_field($_POST['genre']) : '';
    if (!empty($genre_str)) {
        // Split comma-separated string, trim whitespace
        $selected_terms = array_map('trim', explode(',', $genre_str));
        $selected_terms = array_filter($selected_terms);
    } else {
        // Fallback random genres
        $categories = array('Đô Thị Ẩn Thân', 'Drama', 'Ngôn tình đô thị', 'Sảng Văn');
        shuffle($categories);
        $selected_terms = array_slice($categories, 0, rand(2, 3));
    }
    
    // Assign to taxonomy 'the_loai' (append = false to set them exactly)
    wp_set_object_terms($post_id, $selected_terms, 'the_loai', false);

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
    $ai_prompt .= "Nhiệm vụ của bạn là sáng tác một bộ truyện mạch lạc, lôi cuốn.\n";
    $ai_prompt .= "Cố định Tiêu đề truyện: \"$title\". TUYỆT ĐỐI GIỮ NGUYÊN tiêu đề này, KHÔNG tự ý đổi tên.\n";
    $ai_prompt .= "Thể loại: $genre. Giọng văn: $tone.\n";
    $ai_prompt .= "Ý tưởng cốt lõi: $prompt\n\n";
    $ai_prompt .= "YÊU CẦU BẮT BUỘC:\n";
    $ai_prompt .= "1. BẮT BUỘC bắt đầu bằng dòng: \"Tiêu đề: $title\"\n";
    $ai_prompt .= "2. BẮT BUỘC dòng thứ hai là: \"Mô tả: [Đoạn tóm tắt giới thiệu truyện ngắn gọn, hấp dẫn]\"\n";
    $ai_prompt .= "3. Viết đúng $chapters chương, mỗi chương khoảng 1500-2500 từ tiếng Việt (đủ nội dung, hấp dẫn, không tóm tắt sơ sài).\n";
    $ai_prompt .= "4. Mỗi chương BẮT BUỘC phải bắt đầu bằng dòng ĐÚNG FORMAT: \"Chương [số]: [tên chương]\" trên một dòng riêng biệt.\n";
    $ai_prompt .= "5. Các chương phải liên kết mạch lạc, cốt truyện nhất quán, không mâu thuẫn.\n";
    $ai_prompt .= "6. Kết thúc chương cuối phải hoàn chỉnh, có hậu (Happy ending hoặc Open ending).\n";
    $ai_prompt .= "7. KHÔNG viết thêm bất kỳ ghi chú nào ngoài nội dung truyện.\n";
    $ai_prompt .= "8. SHOW, DON'T TELL (Quan trọng): Tuyệt đối KHÔNG viết một đoạn văn dài dòng chỉ để kể lể tóm tắt lại quá khứ của nhân vật. Hãy để nhân vật tự bộc bạch qua lời thoại ngập ngừng, rưng rưng nước mắt, hoặc qua hành động, những mảnh hồi ức chớp nhoáng đan xen với hiện tại để câu chuyện chân thực và 'điện ảnh' hơn.\n";
    $ai_prompt .= "9. NGHỆ THUẬT XỬ LÝ CAO TRÀO: Nếu truyện theo hướng tâm lý hoặc chữa lành (Healing/Dark Healing), hồi kết và cao trào phải thiên về sự giằng xé nội tâm sâu sắc, ảo giác tâm lý hoặc sự tự thức tỉnh. TUYỆT ĐỐI KHÔNG biến cao trào thành các trận đánh nhau phép thuật kiểu 'siêu anh hùng' hay 'shounen manga' với quái vật hiện hình gầm rú phá hoại vật lý.\n";
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
    $ai_prompt .= "Nhiệm vụ của bạn là sáng tác một bộ truyện mạch lạc, lôi cuốn.\n";
    if ($title && $title !== 'Truyện chưa đặt tên') {
        $ai_prompt .= "Gợi ý tiêu đề: \"$title\" (Bạn có thể tinh chỉnh cho hay hơn).\n";
    }
    $ai_prompt .= "Thể loại: $genre. Giọng văn: $tone.\n";
    $ai_prompt .= "Ý tưởng cốt lõi: $prompt\n\n";
    $ai_prompt .= "YÊU CẦU BẮT BUỘC:\n";
    $ai_prompt .= "1. BẮT BUỘC bắt đầu bằng dòng: \"Tiêu đề: [Tên truyện ấn tượng do bạn nghĩ ra]\"\n";
    $ai_prompt .= "2. BẮT BUỘC dòng thứ hai là: \"Mô tả: [Đoạn tóm tắt giới thiệu truyện ngắn gọn, hấp dẫn]\"\n";
    $ai_prompt .= "3. Viết đúng $chapters chương, mỗi chương khoảng 1500-2500 từ tiếng Việt (đủ nội dung, hấp dẫn, không tóm tắt sơ sài).\n";
    $ai_prompt .= "4. Mỗi chương BẮT BUỘC phải bắt đầu bằng TIÊU ĐỀ theo format CHÍNH XÁC: \"Chương [số]: [tên chương]\" trên một dòng riêng biệt.\n";
    $ai_prompt .= "5. Các chương phải liên kết mạch lạc, cốt truyện nhất quán, không mâu thuẫn.\n";
    $ai_prompt .= "6. Kết thúc chương cuối phải hoàn chỉnh, có hậu (Happy ending hoặc Open ending).\n";
    $ai_prompt .= "7. KHÔNG viết thêm bất kỳ ghi chú nào ngoài nội dung truyện.\n";
    $ai_prompt .= "8. SHOW, DON'T TELL (Quan trọng): Tuyệt đối KHÔNG viết một đoạn văn dài dòng chỉ để kể lể tóm tắt lại quá khứ của nhân vật. Hãy để nhân vật tự bộc bạch qua lời thoại ngập ngừng, rưng rưng nước mắt, hoặc qua hành động, những mảnh hồi ức chớp nhoáng đan xen với hiện tại để câu chuyện chân thực và 'điện ảnh' hơn.\n";
    $ai_prompt .= "9. NGHỆ THUẬT XỬ LÝ CAO TRÀO: Nếu truyện theo hướng tâm lý hoặc chữa lành (Healing/Dark Healing), hồi kết và cao trào phải thiên về sự giằng xé nội tâm sâu sắc, ảo giác tâm lý hoặc sự tự thức tỉnh. TUYỆT ĐỐI KHÔNG biến cao trào thành các trận đánh nhau phép thuật kiểu 'siêu anh hùng' hay 'shounen manga' với quái vật hiện hình gầm rú phá hoại vật lý.\n";
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
    $title    = isset($_POST['title']) ? sanitize_text_field($_POST['title']) : 'Truyện Sáng Tác Nhanh';
    $genre_str= isset($_POST['genre']) ? sanitize_text_field($_POST['genre']) : '';

    if (empty($raw_text)) {
        wp_send_json_error(array('message' => 'Nội dung truyện rỗng.'));
    }

    if (!$post_id) {
        $post_id = wp_insert_post(array(
            'post_title'   => $title,
            'post_status'  => 'draft',
            'post_type'    => 'truyen',
            'post_author'  => get_current_user_id()
        ));
        
        if (is_wp_error($post_id)) {
            wp_send_json_error(array('message' => 'Lỗi tạo bài viết: ' . $post_id->get_error_message()));
        }

        // Apply Genres
        if (!empty($genre_str)) {
            $selected_terms = array_map('trim', explode(',', $genre_str));
            $selected_terms = array_filter($selected_terms);
        } else {
            $categories = array('Đô Thị Ẩn Thân', 'Drama', 'Ngôn tình đô thị', 'Sảng Văn');
            shuffle($categories);
            $selected_terms = array_slice($categories, 0, rand(2, 3));
        }
        wp_set_object_terms($post_id, $selected_terms, 'the_loai', false);

        // Parse Tiêu đề / Mô tả từ AI content để cấu hình SEO
        $extracted_title = $title;
        $extracted_desc = '';
        foreach (explode("\n", current(array_slice(explode("Chương", $raw_text), 0, 1))) as $line) {
            if (preg_match('/^Tiêu\s*đề:?\s*(.*)$/iu', trim($line), $m)) {
                $extracted_title = trim($m[1]);
            }
            if (preg_match('/^Mô\s*tả:?\s*(.*)$/iu', trim($line), $m)) {
                $extracted_desc = trim($m[1]);
            }
        }

        $seo_keyword = sprintf('Truyện %s', $extracted_title);
        $seo_title = sprintf('Đọc Ngay Truyện %s (Mới Nhất) - Cực Cuốn', $extracted_title);
        
        update_post_meta($post_id, 'rank_math_title', $seo_title);
        update_post_meta($post_id, 'rank_math_focus_keyword', $seo_keyword);
        update_post_meta($post_id, '_yoast_wpseo_title', $seo_title);
        update_post_meta($post_id, '_yoast_wpseo_focuskw', $seo_keyword);
        
        if (!empty($extracted_desc)) {
            $seo_text = $extracted_desc;
            if (mb_strlen($seo_text, 'UTF-8') > 160) {
                $seo_text = mb_substr($seo_text, 0, 157, 'UTF-8') . '...';
            }
            update_post_meta($post_id, 'rank_math_description', $seo_text);
            update_post_meta($post_id, '_yoast_wpseo_metadesc', $seo_text);
        }

        // Bật Schema Article cho Rank Math
        update_post_meta($post_id, 'rank_math_rich_snippet', 'article');
        $schema_data = array(
            '@type' => 'Article',
            'headline' => $seo_title,
            'description' => !empty($seo_text) ? $seo_text : ''
        );
        update_post_meta($post_id, 'rank_math_schema_Article', $schema_data);
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
    $ai_prompt .= "Yêu cầu:\n";
    $ai_prompt .= "- Gợi ý 3 tựa đề truyện: Hấp dẫn, gợi tò mò, sang trọng, mang phong cách văn học mảng web novel chuyên nghiệp. Tiêu đề NÊN dài một chút (thường cấu trúc Nửa chính - Nửa phụ) ví dụ: 'Thương Vụ Sticker Tỷ Đô: Kẻ Ngạo Mạn Phải Cúi Đầu', hoặc 'Sự Trở Lại Của Kẻ Bị Ruồng Bỏ'. KHÔNG ĐƯỢC dùng các từ quá sến, sáo rỗng hoặc quá trẻ con (chuối).\n";
    $ai_prompt .= "- Dựa vào độ dài và độ phức tạp của cốt truyện, hãy đề xuất số lượng chương phù hợp nhất để triển khai (ví dụ: 5, 10, 15, hoặc 20, 30 nếu truyện cần không gian rông).\n";
    $ai_prompt .= "Trả về CHỈ MỘT JSON hợp lệ (không giải thích thêm):\n";
    $ai_prompt .= '{"genres": ["Thể loại 1", "Thể loại 2"], "tone": "giọng văn phù hợp nhất", "titles": ["Tựa đề 1", "Tựa đề 2", "Tựa đề 3"], "chapters": 10}';

    $gemini_key = tehi_get_gemini_key();

    wp_send_json_success(array(
        'ai_prompt'  => $ai_prompt,
        'gemini_key' => $gemini_key,
        'has_key'    => true
    ));
}

// ==========================================
// STORY STUDIO: Brainstorm 10 Idea Kịch Bản
// ==========================================
add_action('wp_ajax_temply_studio_brainstorm_prompts', 'temply_studio_brainstorm_prompts');
function temply_studio_brainstorm_prompts() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');

    $genres = isset($_POST['genres']) ? sanitize_text_field($_POST['genres']) : '';
    $tone   = isset($_POST['tone']) ? sanitize_text_field($_POST['tone']) : '';
    $prompt = isset($_POST['prompt']) ? sanitize_textarea_field($_POST['prompt']) : ''; // Keyword ngắn do user gõ

    $count  = isset($_POST['count']) ? intval($_POST['count']) : 10;
    if ($count < 1) $count = 1;
    if ($count > 30) $count = 30; // Giới hạn toi da 30

    $ai_prompt  = "Bạn là một NHÀ BIÊN KỊCH THIÊN TÀI, chuyên tạo ra những kịch bản truyện mạng (Web Novel) VƯỢT TẦM và gây sốc nhất. Người dùng đang muốn viết một truyện mới dựa trên các thông số sau:\n";
    if (!empty($genres)) $ai_prompt .= "- Thể loại mong muốn: $genres\n";
    if (!empty($tone))   $ai_prompt .= "- Giọng văn/Không khí hướng tới: $tone\n";
    if (!empty($prompt)) $ai_prompt .= "- Ý tưởng Cốt lõi của người dùng: $prompt\n\n";

    $ai_prompt .= "NHIỆM VỤ TỐI THƯỢNG:\n";
    $ai_prompt .= "Nhiệm vụ của bạn là nghiên cứu các THỊ HIẾU VÀ MÔ-TÍP ĐANG THỊNH HÀNH NHẤT ở Châu Á (như: Xuyên không, Hệ thống, Tổng tài, Nữ cường, Võng du...).\n";
    $ai_prompt .= "BẮT BUỘC SÁNG TẠO ĐA DẠNG TUYỆT ĐỐI: Dù chung một Ý tưởng Cốt lõi, nhưng MỖI kịch bản phải là một vũ trụ HOÀN TOÀN KHÁC NHAU. KHÔNG ĐƯỢC lặp lại tên nhân vật (ví dụ: dàn 1 tên Mai, thì dàn 2 tên Lan, dàn 3 bối cảnh Cổ Đại, dàn 4 bối cảnh Đô Thị...). TUYỆT ĐỐI CHỈ SỬ DỤNG TÊN (VIỆT NAM/TRUNG QUỐC) VÀ BỐI CẢNH CHÂU Á (KHÔNG dùng tên phương Tây, KHÔNG dùng bối cảnh Châu Âu). Phải liên tục thay đổi Góc Nhìn, Thời Đại, Tuổi Tác, Tên Gọi, Hoàn Cảnh Xuất Thân để {$count} kịch bản này là {$count} kiệt tác riêng biệt.\n";
    $ai_prompt .= "Mỗi kịch bản dài khoảng 3-5 câu: Mở đầu bằng thiết lập hấp dẫn, xây dựng kịch tính và chốt bằng mâu thuẫn khốc liệt.\n";
    $ai_prompt .= "BẮT BUỘC trả về CHỈ MỘT MẢNG JSON gồm {$count} Object (KHÔNG TEXT THỪA, KHÔNG GIẢI THÍCH).\n";
    $ai_prompt .= "Ví dụ định dạng trả về:\n";
    $ai_prompt .= "[\n";
    $ai_prompt .= "  {\n";
    $ai_prompt .= "    \"title\": \"Tên truyện gợi ý (cấu trúc hấp dẫn)\",\n";
    $ai_prompt .= "    \"genres\": \"Thể loại 1, Thể loại 2...\",\n";
    $ai_prompt .= "    \"prompt\": \"Kịch bản chi tiết...\"\n";
    $ai_prompt .= "  }\n";
    $ai_prompt .= "]";

    $gemini_key = tehi_get_gemini_key();

    wp_send_json_success(array(
        'ai_prompt'  => $ai_prompt,
        'gemini_key' => $gemini_key,
        'has_key'    => true
    ));
}

// ==========================================
// STORY STUDIO: Đẩy Batch Kịch Bản vào Auto-Pilot
// ==========================================
add_action('wp_ajax_temply_studio_batch_autopilot_push', 'temply_studio_batch_autopilot_push');
function temply_studio_batch_autopilot_push() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');

    $raw_payload = isset($_POST['payload']) ? wp_unslash($_POST['payload']) : '';
    if(empty($raw_payload)) wp_send_json_error(['message' => 'Lỗi: Payload trống']);

    $data = json_decode($raw_payload, true);
    if(!$data || !isset($data['prompts']) || !is_array($data['prompts'])) {
        wp_send_json_error(['message' => 'Lỗi Data formats']);
    }

    $prompts      = $data['prompts']; // Array of objects
    $chapters_min = intval($data['chapters_min'] ?? 20);
    $chapters_max = intval($data['chapters_max'] ?? $chapters_min);
    $interval     = sanitize_text_field($data['interval'] ?? 'every_five_minutes');
    if($chapters_min < 1) $chapters_min = 20;
    if($chapters_max < $chapters_min) $chapters_max = $chapters_min;

    $config = get_option('temply_auto_pilot_queue_config', false);
    if (!$config) {
        $config = ['interval' => $interval, 'queue' => [], 'status' => 'running', 'last_run' => time()];
    }
    
    // Ghi đè interval nếu tốc độ mới nhanh hơn/chậm hơn theo quyết định user
    $config['interval'] = $interval;
    $config['status']   = 'running';

    foreach($prompts as $p) {
        if(!is_array($p) || empty(trim($p['prompt'] ?? ''))) continue;

        $p_title  = sanitize_text_field($p['title'] ?? 'Truyện chờ phân tích...');
        $p_genres = sanitize_text_field($p['genres'] ?? '');
        $p_prompt = sanitize_textarea_field(trim($p['prompt']));
        $target_c = rand($chapters_min, $chapters_max);
        if ($target_c > 25) $target_c = 25; // MAX 25 chapters hard limit

        // Trạng thái 'draft_outline' để auto-pilot tự động gọi AI phân tích Dàn ý & Nhân vật ngầm!
        $config['queue'][]  = [
            'uuid'            => wp_generate_uuid4(),
            'status'          => 'draft_outline', 
            'prompt'          => $p_prompt,
            'title'           => $p_title,
            'genre'           => $p_genres,
            'tone'            => '',
            'world'           => '',
            'chars'           => '',
            'script'          => '',
            'hook'            => '',
            'truyen_id'       => 0,
            'target_chapters' => $target_c,
            'chapters_left'   => $target_c,
            'enable_audit'    => 1, // mặc định bật audit
        ];
    }
    
    update_option('temply_auto_pilot_queue_config', $config);

    if (!wp_next_scheduled('temply_auto_pilot_cron_hook')) {
        wp_schedule_event(time(), $interval, 'temply_auto_pilot_cron_hook');
    }

    wp_send_json_success(['message' => 'Đã đưa ' . count($prompts) . ' kịch bản vào hàng chờ!']);
}

// ==========================================
// RESUME AUTO PILOT ERROR
// ==========================================
add_action('wp_ajax_temply_studio_resume_error_queue', 'temply_studio_resume_error_queue');
function temply_studio_resume_error_queue() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');
    if (!current_user_can('edit_posts')) wp_send_json_error(['message' => 'Không đủ quyền.']);

    $index = isset($_POST['index']) ? intval($_POST['index']) : -1;
    $config = get_option('temply_auto_pilot_queue_config', false);
    
    if ($config && isset($config['queue'][$index])) {
        if ($config['queue'][$index]['status'] === 'error') {
            $config['queue'][$index]['status'] = 'writing'; // Quay lại trạm làm việc
            $config['queue'][$index]['error_log'] = ''; // Xóa vết nhơ
            update_option('temply_auto_pilot_queue_config', $config);
            wp_send_json_success(['message' => 'Đã phục hồi tiến trình! AutoPilot sẽ thử lại.']);
        } else {
            wp_send_json_error(['message' => 'Tiến trình này không ở trạng thái Lỗi.']);
        }
    } else {
        wp_send_json_error(['message' => 'Không tìm thấy tiến trình trong Hàng Đợi.']);
    }
}

// ==========================================
// THÔNG TIN TRẠM GIÁM SÁT (UI)
// ==========================================
add_action('wp_ajax_temply_studio_clear_auto_pilot', 'temply_studio_clear_auto_pilot');
function temply_studio_clear_auto_pilot() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');
    if (!current_user_can('edit_posts')) wp_send_json_error(['message' => 'Không đủ quyền.']);

    delete_option('temply_auto_pilot_queue_config');
    wp_clear_scheduled_hook('temply_auto_pilot_cron_hook');
    
    wp_send_json_success(['message' => 'Đã thu dọn sạch sẽ Lò Ấp và giải phóng tiến trình gốc!']);
}

// ==========================================
// STORY STUDIO: Đánh Giá Độ Ăn Khách (AI Evaluation)
// ==========================================
add_action('wp_ajax_temply_studio_evaluate_prompts', 'temply_studio_evaluate_prompts');
function temply_studio_evaluate_prompts() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');

    $raw_payload = isset($_POST['payload']) ? wp_unslash($_POST['payload']) : '';
    if(empty($raw_payload)) wp_send_json_error(['message' => 'Lỗi: Payload trống']);
    
    $prompts = json_decode($raw_payload, true);
    if(!$prompts || !is_array($prompts)) {
        wp_send_json_error(['message' => 'Lỗi Data formats']);
    }

    $str_payload = "";
    foreach($prompts as $idx => $p) {
        $str_payload .= "Kịch bản số {$idx}: " . ($p['title'] ?? '') . "\n" . ($p['prompt'] ?? '') . "\n\n";
    }

    $sys = "Bạn là NỮ BIÊN TẬP VIÊN KIÊU KÌ, KHẮT KHE chuyên phân tích độ 'ĂN KHÁCH' của kịch bản truyện chữ mạng. Hãy đọc danh sách kịch bản dưới đây.\n";
    $sys .= "BẮT BUỘC trả về CHỈ MỘT MẢNG JSON các Object tương ứng với các kịch bản.\n";
    $sys .= "Ví dụ: [\n { \"score\": \"9.0\", \"review\": \"Cốt truyện xuất sắc, twist vả mặt gãy gọn, phù hợp độc giả trẻ.\" },\n { \"score\": \"5.5\", \"review\": \"Mô típ quá cũ, thiếu điểm nhấn, khó cạnh tranh.\" }\n]";
    $usr = $str_payload;

    $gemini_key = tehi_get_gemini_key();
    
    // We send back the system prompt and user prompt to let the browser call AI (save bandwidth/timeouts)
    wp_send_json_success(array(
        'ai_sys_prompt' => $sys,
        'ai_usr_prompt' => $usr,
        'gemini_key'    => $gemini_key
    ));
}

// ==========================================
// STORY STUDIO: Cải Thiện Kịch Bản (AI Enhance)
// ==========================================
add_action('wp_ajax_temply_studio_improve_prompt', 'temply_studio_improve_prompt');
function temply_studio_improve_prompt() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');

    $sys = "Bạn là Bậc Thầy Kịch Bản. Hãy nhận đoạn kịch bản do Lò vớt ra sau đây và tái cấu trúc nó thành phiên bản KỊCH TÍNH, HẤP DẪN, và ĐỈNH CAO hơn gấp 10 lần.
YÊU CẦU:
- Không viết thành truyện chữ, chỉ viết tóm tắt diễn biến (outline).
- Độ dài vừa phải, súc tích. Tôn trọng thể loại và chủ đề ban đầu.
- Trả về ĐÚNG 1 ĐOẠN VĂN THEO TEXT THUẦN TÚY, không sinh JSON, không kèm định dạng Markdown hay lời chào.";
    
    $gemini_key = tehi_get_gemini_key();
    
    wp_send_json_success(array(
        'ai_sys_prompt' => $sys,
        'gemini_key'    => $gemini_key
    ));
}

// ==========================================
// STORY STUDIO: Quản Lý Hàng Đợi Auto-Pilot (Frontend)
// ==========================================
add_action('wp_ajax_temply_studio_get_autopilot_queue', 'temply_studio_get_autopilot_queue');
function temply_studio_get_autopilot_queue() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');
    $config = get_option('temply_auto_pilot_queue_config', false);
    if (!$config) $config = ['queue' => []];
    wp_send_json_success(['config' => $config]);
}

add_action('wp_ajax_temply_studio_remove_autopilot_item', 'temply_studio_remove_autopilot_item');
function temply_studio_remove_autopilot_item() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');
    $index = isset($_POST['index']) ? intval($_POST['index']) : -1;
    if ($index < 0) wp_send_json_error(['message' => 'Lỗi index']);

    $config = get_option('temply_auto_pilot_queue_config', false);
    if ($config && isset($config['queue']) && isset($config['queue'][$index])) {
        unset($config['queue'][$index]);
        $config['queue'] = array_values($config['queue']); // reindex
        update_option('temply_auto_pilot_queue_config', $config);
        wp_send_json_success(['message' => 'Đã xoá truyện khỏi hàng chờ.']);
    }
    wp_send_json_error(['message' => 'Không tìm thấy truyện này.']);
}

add_action('wp_ajax_temply_studio_clear_autopilot_queue', 'temply_studio_clear_autopilot_queue');
function temply_studio_clear_autopilot_queue() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');
    if (!current_user_can('manage_options')) wp_send_json_error(['message' => 'Không có quyền.']);
    
    $config = get_option('temply_auto_pilot_queue_config', false);
    if ($config) {
        $config['queue'] = [];
        $config['status'] = 'completed';
        update_option('temply_auto_pilot_queue_config', $config);
        wp_clear_scheduled_hook('temply_auto_pilot_cron_hook');
        wp_send_json_success(['message' => 'Đã xoá sạch hàng đợi và ngắt hệ thống Auto-Pilot.']);
    }
    wp_send_json_error(['message' => 'Hàng đợi vốn đã trống.']);
}

// Bơm xung hệ thống: Ép WP Cron chạy lập tức khi user đang mở bảng theo dõi
add_action('wp_ajax_temply_studio_trigger_cron', 'temply_studio_trigger_cron');
function temply_studio_trigger_cron() {
    check_ajax_referer('temply_ai_nonce', 'action_nonce');
    if (function_exists('temply_process_auto_pilot')) {
        temply_process_auto_pilot();
    }
    wp_send_json_success(['message' => 'Đã ép xung lò ấp.']);
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

// ==========================================
// AUTO PILOT DASHBOARD WIDGET
// ==========================================
function tehi_register_autopilot_dashboard_widget() {
    wp_add_dashboard_widget(
        'tehi_autopilot_dashboard_widget', 
        '🚀 Trạm Giám Sát Auto-Pilot', 
        'tehi_render_autopilot_dashboard_widget'
    );
}
add_action('wp_dashboard_setup', 'tehi_register_autopilot_dashboard_widget');

function tehi_render_autopilot_dashboard_widget() {
    $config_raw = get_option('temply_auto_pilot_queue_config');
    $config = $config_raw ? maybe_unserialize($config_raw) : null;
    $queue = isset($config['queue']) ? $config['queue'] : [];
    
    $published_count = wp_count_posts('truyen')->publish;

    echo '<div style="background:#1d2327; color:#fff; padding:16px; border-radius:0 0 4px 4px; margin:-12px; max-height: 400px; overflow-y:auto; box-sizing:border-box;">';
    
    echo '<div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:12px; margin-bottom:16px;">';
    echo '<div><strong style="color:#10b981; font-size:12px;">Đã xuất bản:</strong> <span style="font-size:18px; font-weight:800; color:#fff; display:block;">' . intval($published_count) . ' bộ</span></div>';
    echo '<div style="text-align:right;"><strong style="color:#a5b4fc; font-size:12px;">Đang nằm Lò:</strong> <span style="font-size:18px; font-weight:800; color:#fff; display:block;">' . count($queue) . ' truyện</span></div>';
    echo '</div>';

    if (empty($queue)) {
        echo '<div style="padding:40px 0; text-align:center; color:#9ca3af; font-size:13px;">Lò ấp Auto-Pilot đang trống.<br><br>Hãy vào <strong style="color:#a5b4fc;">Story Studio</strong> ở trang chủ để đẩy thêm kịch bản vào chờ cày chữ tự động nhé!</div>';
    } else {
        foreach ($queue as $idx => $q) {
            $target = isset($q['target_chapters']) ? intval($q['target_chapters']) : 20;
            $left = isset($q['chapters_left']) ? intval($q['chapters_left']) : $target;
            $done = max(0, $target - $left);
            $pct = floor(($done / max(1, $target)) * 100);
            
            $statusColor = '#94a3b8';
            $statusText = isset($q['status']) ? $q['status'] : 'Lỗi';
            
            if($statusText === 'draft_outline') { 
                $statusColor = '#f59e0b'; $statusText = 'Đang xếp Dàn Ý'; 
            } else if($statusText === 'writing') { 
                $statusColor = '#10b981'; $statusText = 'Đang Cày Chữ'; 
            } else if($statusText === 'pending') { 
                $statusColor = '#3b82f6'; $statusText = 'Đang chờ'; 
            } else if($statusText === 'error' || $statusText === 'failed') {
                $statusColor = '#ef4444'; 
                $statusText = !empty($q['error_log']) ? substr($q['error_log'], 0, 30).'...' : 'Lỗi không xác định'; 
            }

            $title = !empty($q['title']) ? esc_html($q['title']) : 'Sáng Tác Chờ Tên';
            $genre = !empty($q['genre']) ? esc_html($q['genre']) : 'Chưa định hình';
            $idx_display = $idx + 1;
            
            echo '<div style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:12px; margin-bottom:12px; display:flex; gap:12px; align-items:center;">';
            echo '<div style="width:36px; height:36px; background:rgba(79,70,229,0.2); color:#a5b4fc; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:14px; flex-shrink:0;">#'.$idx_display.'</div>';
            echo '<div style="flex:1; min-width:0;">'; 
            echo '<div style="font-size:14px; font-weight:700; color:#fff; margin-bottom:4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">'.$title.'</div>';
            echo '<div style="display:flex; gap:6px; font-size:11px; margin-bottom:8px; flex-wrap:wrap; align-items:center;">';
            echo '<span style="background:rgba(255,255,255,0.1); color:'.$statusColor.'; padding:2px 6px; border-radius:12px; font-weight:bold;">'.$statusText.'</span>';
            echo '<span style="background:rgba(255,255,255,0.1); color:#cbd5e1; padding:2px 6px; border-radius:12px; white-space:nowrap;">'.$genre.'</span>';
            echo '</div>';
            echo '<div style="background:rgba(0,0,0,0.5); height:6px; border-radius:3px; overflow:hidden; position:relative;">';
            echo '<div style="background:linear-gradient(90deg, #4f46e5, #ec4899); position:absolute; top:0; left:0; bottom:0; width:'.$pct.'%;"></div>';
            echo '</div>';
            echo '<div style="font-size:10px; color:#cbd5e1; margin-top:4px; text-align:right;">Tiến độ: '.$done.'/'.$target.' ('.$pct.'%)</div>';
            echo '</div>';
            echo '</div>';
        }
    }

    echo '</div>'; 
}

/**
 * Auto-create and assign 'the_loai' taxonomy terms from REST API String Input.
 * M-Core sends ["Xuyên Không", "Vả Mặt"], which WP REST API ignores by default.
 * This hook creates the terms and links them!
 */
add_action( 'rest_insert_truyen', function( $post, $request, $creating ) {
    $the_loai = $request->get_param('the_loai');
    if ( !empty($the_loai) && is_array($the_loai) ) {
        $term_ids = array();
        foreach ( $the_loai as $term_name ) {
            $term_name = trim($term_name);
            if (empty($term_name)) continue;
            
            $term = get_term_by('name', $term_name, 'the_loai');
            if ( $term ) {
                $term_ids[] = (int) $term->term_id;
            } else {
                $inserted = wp_insert_term( $term_name, 'the_loai' );
                if ( !is_wp_error($inserted) ) {
                    $term_ids[] = (int) $inserted['term_id'];
                }
            }
        }
        if ( !empty($term_ids) ) {
            wp_set_object_terms( $post->ID, $term_ids, 'the_loai', false );
        }
    }
}, 10, 3 );

/**
 * Thêm Meta Box Chọn Truyện Mẹ cho Chương
 */
add_action('add_meta_boxes', 'tehi_clone_add_truyen_meta_box');
function tehi_clone_add_truyen_meta_box() {
    add_meta_box(
        'tehi_truyen_parent_box',
        '📘 Chọn Truyện Gốc (Truyện Mẹ)',
        'tehi_clone_truyen_meta_box_html',
        'chuong',
        'side',
        'high'
    );
}

function tehi_clone_truyen_meta_box_html($post) {
    $truyen_id = get_post_meta($post->ID, '_truyen_id', true);
    
    // Lấy danh sách Truyện để hiển thị dropdown
    $args = array(
        'post_type' => 'truyen',
        'posts_per_page' => -1,
        'post_status' => array('publish', 'draft'),
        'orderby' => 'date',
        'order' => 'DESC'
    );
    $truyens = get_posts($args);
    
    echo '<label for="tehi_truyen_parent_id" style="display:block; margin-bottom:8px;">Chọn bộ truyện chứa chương này:</label>';
    echo '<select name="tehi_truyen_parent_id" id="tehi_truyen_parent_id" style="width:100%;">';
    echo '<option value="">-- Trống --</option>';
    
    foreach ($truyens as $t) {
        $selected = ($t->ID == $truyen_id) ? 'selected' : '';
        echo '<option value="' . esc_attr($t->ID) . '" ' . $selected . '>' . esc_html($t->post_title) . ' (ID: ' . $t->ID . ')</option>';
    }
    echo '</select>';
    wp_nonce_field('tehi_truyen_parent_nonce_action', 'tehi_truyen_parent_nonce');
}

add_action('save_post_chuong', 'tehi_clone_save_truyen_meta_box');
function tehi_clone_save_truyen_meta_box($post_id) {
    if (!isset($_POST['tehi_truyen_parent_nonce']) || !wp_verify_nonce($_POST['tehi_truyen_parent_nonce'], 'tehi_truyen_parent_nonce_action')) {
        return;
    }
    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) {
        return;
    }
    if (!current_user_can('edit_post', $post_id)) {
        return;
    }
    
    if (isset($_POST['tehi_truyen_parent_id'])) {
        update_post_meta($post_id, '_truyen_id', sanitize_text_field($_POST['tehi_truyen_parent_id']));
    }
}

/**
 * Tự động set mặc định Kích thước đầy đủ (Full Size) khi chèn ảnh vào bài viết
 */
function tehi_clone_force_full_image_size() {
    update_option('image_default_size', 'full'); // Mặc định chèn ảnh Full
    update_option('image_default_link_type', 'none'); // Mặc định không chèn link vào ảnh
}
add_action('after_setup_theme', 'tehi_clone_force_full_image_size');

/**
 * Tắt nén ảnh tự động của WordPress để giữ nguyên chất lượng text của Truyện tranh
 */
add_filter('jpeg_quality', function($arg){ return 100; });
add_filter('wp_editor_set_quality', function($arg){ return 100; });
