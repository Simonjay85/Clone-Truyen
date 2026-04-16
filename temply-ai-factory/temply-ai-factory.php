<?php
/*
Plugin Name: Temply AI Story Factory
Description: Tự động sinh nội dung truyện gốc đa thể loại, tích hợp API OpenAI (GPT-4o-mini) với Multi-step Agent Workflow.
Version: 1.0
Author: Full-stack AI Expert
*/

if (!defined('ABSPATH')) {
    exit;
}

// Khởi tạo Menu Admin
function temply_ai_add_admin_menu() {
    add_menu_page(
        'Temply AI Factory',
        'AI Story Factory',
        'manage_options',
        'temply-ai-factory',
        'temply_ai_render_admin_page',
        'dashicons-edit-page',
        25
    );
    
    add_submenu_page(
        'temply-ai-factory',
        'Cỗ Máy Rặn Tự Động',
        '🤖 Auto-Pilot',
        'manage_options',
        'temply-ai-auto-pilot',
        'temply_ai_render_auto_pilot_page'
    );
    
    add_submenu_page(
        'temply-ai-factory',
        'Đại Tu Sửa Chữa',
        '📊 Tổng Phẫu Thuật',
        'manage_options',
        'temply-ai-batch-audit',
        'temply_ai_render_batch_audit_page'
    );
}
// add_action('admin_menu', 'temply_ai_add_admin_menu'); // Đã chuyển sang Frontend Studio

// Enqueue Scripts & CSS cho Admin UI
function temply_ai_admin_assets($hook) {
    if ($hook != 'toplevel_page_temply-ai-factory') {
        return;
    }
    wp_enqueue_script('temply-agent-js', plugin_dir_url(__FILE__) . 'assets/agentic-workflow.js', ['jquery'], filemtime(plugin_dir_path(__FILE__) . 'assets/agentic-workflow.js'), true);
    wp_localize_script('temply-agent-js', 'temply_ai_ajax', [
        'ajax_url' => admin_url('admin-ajax.php'),
        'nonce'    => wp_create_nonce('temply_ai_nonce')
    ]);
}
add_action('admin_enqueue_scripts', 'temply_ai_admin_assets');

// Enqueue JS cho giao diện truyện bên ngoài (Frontend - Tải ảnh Comic tuần tự)
function temply_ai_frontend_assets() {
    wp_enqueue_script('temply-frontend-js', plugin_dir_url(__FILE__) . 'assets/frontend-comic.js', [], filemtime(plugin_dir_path(__FILE__) . 'assets/frontend-comic.js'), true);
}
add_action('wp_enqueue_scripts', 'temply_ai_frontend_assets');

// Enqueue JS cho Gutenberg Sidebar (Admin Edit Post)
function temply_ai_gutenberg_assets() {
    // Chỉ nhúng vào bài viết/trang (ở đây có thể check get_post_type)
    wp_enqueue_script(
        'temply-gutenberg-sidebar',
        plugin_dir_url(__FILE__) . 'assets/gutenberg-sidebar.js',
        ['wp-plugins', 'wp-edit-post', 'wp-element', 'wp-components', 'wp-data', 'wp-api-fetch', 'wp-notices'],
        filemtime(plugin_dir_path(__FILE__) . 'assets/gutenberg-sidebar.js'),
        true
    );
    
    wp_localize_script('temply-gutenberg-sidebar', 'temply_ai_ajax', [
        'ajax_url' => admin_url('admin-ajax.php'),
        'nonce'    => wp_create_nonce('temply_ai_nonce')
    ]);
}
add_action('enqueue_block_editor_assets', 'temply_ai_gutenberg_assets');

require_once plugin_dir_path(__FILE__) . 'admin-ui.php';
require_once plugin_dir_path(__FILE__) . 'admin/auto-pilot.php';
require_once plugin_dir_path(__FILE__) . 'admin/batch-audit.php';
require_once plugin_dir_path(__FILE__) . 'includes/openai-api.php';
require_once plugin_dir_path(__FILE__) . 'includes/convert_comic.php';
require_once plugin_dir_path(__FILE__) . 'includes/backfill.php';
require_once plugin_dir_path(__FILE__) . 'includes/paragraph-comments.php';
require_once plugin_dir_path(__FILE__) . 'mobile-ui.php';
require_once plugin_dir_path(__FILE__) . 'includes/blueprint-meta.php';

// Đăng ký Cron Schedules
add_filter('cron_schedules', 'temply_ai_cron_schedules');
function temply_ai_cron_schedules($schedules) {
    if(!isset($schedules['every_five_minutes'])) {
        $schedules['every_five_minutes'] = array(
            'interval' => 300,
            'display'  => __('Mỗi 5 phút')
        );
    }
    return $schedules;
}

// Đăng ký Shortcode Mobile Creator
add_shortcode('temply_mobile_creator', 'temply_ai_render_mobile_page');


// Custom Column cho Danh sách Chương (CPT Chuong) để dễ dàng quản lý
add_filter('manage_chuong_posts_columns', function($columns) {
    $new_columns = [];
    foreach($columns as $key => $title) {
        if ($key === 'date') {
            $new_columns['truyen_thuoc_ve'] = 'Thuộc Truyện Gốc';
        }
        $new_columns[$key] = $title;
    }
    return $new_columns;
});

add_action('manage_chuong_posts_custom_column', function($column, $post_id) {
    if ($column === 'truyen_thuoc_ve') {
        $truyen_id = get_post_meta($post_id, '_truyen_id', true);
        if ($truyen_id) {
            $truyen_title = get_the_title($truyen_id);
            echo '<strong><a href="' . admin_url('post.php?post=' . $truyen_id . '&action=edit') . '" style="color: #2271b1; text-decoration: none;">' . esc_html($truyen_title) . '</a></strong>';
        } else {
            echo '<em style="color: #999;">Trống</em>';
        }
    }
}, 10, 2);

// API Backfill Auto Covers
add_action('rest_api_init', function () {
    register_rest_route('temply/v1', '/backfill-covers', array(
        'methods' => 'POST',
        'callback' => 'temply_api_backfill_covers',
        'permission_callback' => '__return_true'
    ));
    register_rest_route('temply/v1', '/backfill-cover', array(
        'methods' => 'GET',
        'callback' => 'temply_api_backfill_cover',
        'permission_callback' => '__return_true'
    ));
});

// API Phân tích mồi Kịch bản Auto Pilot
add_action('wp_ajax_temply_ajax_pilot_analyze', function() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $keyword = trim(sanitize_textarea_field($_POST['keyword'] ?? ''));
    if(empty($keyword)) wp_send_json_error(['message' => 'Keyword rỗng']);
    
    $model = 'gemini';
    $sys = "Phân tích 1 kịch bản truyện dựa trên keyword.
Chỉ trả về JSON có cấu trúc chính xác (Không kèm giải thích hay bọc trong markdown):
{
  \"title\": \"Đề xuất Tên truyện (dưới 15 chữ, cực thu hút)\",
  \"genre\": \"Chỉ được chọn 1 thể loại khớp nhất trong danh sách sau: Drama, Tâm Lý Xã Hội, Đô Thị Thực Tế, Trọng sinh, Tổng tài, Xuyên không, Tu tiên, Ngôn tình đô thị, Kinh dị Việt Nam, Sảng Văn, Vả Mặt, Giả Heo Ăn Thịt Hổ, Đô Thị Ẩn Thân\",
  \"tone\": \"Chỉ được chọn 1 văn phong khớp nhất trong danh sách sau: Lãng mạn, Kịch tính, Hài hước, U tối\",
  \"chapters\": [Số nguyên đại diện số chương đề xuất, VD: 20],
  \"world\": \"Đoạn mô tả bối cảnh thế giới độc đáo\",
  \"chars\": \"Hệ thống nhân vật chính/phụ thiết yếu\",
  \"hook\": \"Điểm thu hút (Giả nghèo, Vả mặt tiểu tam...)\"
}";
    
    // Call AI in openai-api.php (assuming it exists there)
    require_once plugin_dir_path(__FILE__) . 'includes/openai-api.php';
    $res = temply_call_ai($sys, $keyword, 0.7, $model);
    if(is_wp_error($res)) {
        wp_send_json_error(['message' => $res->get_error_message()]);
    }
    
    $clean_json = trim(preg_replace('/```(?:json)?|```/', '', $res));
    $data = json_decode($clean_json, true);
    if(!$data) {
        wp_send_json_error(['message' => 'Lỗi Parse JSON: ' . $clean_json]);
    }
    
    wp_send_json_success($data);
});

// AJAX: Generate Chapter-by-Chapter Outline (Step 3 of Wizard)
add_action('wp_ajax_temply_ajax_pilot_generate_outline', function() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $keyword  = sanitize_textarea_field($_POST['keyword']  ?? '');
    $title    = sanitize_text_field($_POST['title']    ?? '');
    $genre    = sanitize_text_field($_POST['genre']    ?? '');
    $tone     = sanitize_text_field($_POST['tone']     ?? '');
    $chars    = sanitize_textarea_field($_POST['chars']    ?? '');
    $world    = sanitize_textarea_field($_POST['world']    ?? '');
    $chapters = max(1, intval($_POST['chapters'] ?? 20));

    if (empty($keyword) && empty($title)) {
        wp_send_json_error(['message' => 'Thiếu nội dung ý tưởng']);
    }

    require_once plugin_dir_path(__FILE__) . 'includes/openai-api.php';

    $sys = "Bạn là THE PLOT ARCHITECT. Nhiệm vụ: Lập dàn ý chi tiết từng chương cho một bộ truyện.
Trả về DANH SÁCH có đánh số từng chương, mỗi chương 1-2 câu tóm tắt ngắn gọn sự kiện chính.
Định dạng: Chương N: [Tên chương] — [Sự kiện chính]
Viết đủ $chapters chương. KHÔNG giải thích thêm.";

    $user = "ĐỀ TÀI / Ý TƯỞNG GỐC:\n$keyword\n\n" .
            "TÊN TRUYỆN: $title\n" .
            "THỂ LOẠI: $genre\n" .
            "GIỌNG VĂN: $tone\n" .
            "NHÂN VẬT:\n$chars\n\n" .
            "BỐI CẢNH:\n$world\n\n" .
            "Hãy lập dàn ý chi tiết $chapters chương. Mỗi chương phải có sự kiện sự vụ rõ ràng, twist đủ để giữ chân đọc giả.";

    $res = temply_call_ai($sys, $user, 0.9);
    if (is_wp_error($res)) {
        wp_send_json_error(['message' => $res->get_error_message()]);
    }

    wp_send_json_success(['outline' => trim($res)]);
});

// AJAX: Bệnh Viện AI Actions (add chapters, prune, improve plot, replan, hook check)
add_action('wp_ajax_temply_bv_ai_action', function() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $context       = sanitize_textarea_field($_POST['context']       ?? '');
    $custom_prompt = sanitize_textarea_field($_POST['custom_prompt'] ?? '');

    if (empty($custom_prompt)) {
        wp_send_json_error(['message' => 'Thiếu prompt']);
    }

    require_once plugin_dir_path(__FILE__) . 'includes/openai-api.php';

    $sys  = "Bạn là CHIEF STORY EDITOR. Nhiệm vụ: Phân tích và tư vấn chiến lược sáng tác cho một bộ truyện web. Trả lời bằng Tiếng Việt, rõ ràng, có đánh số mục, và cực kỳ cụ thể với tên chương / nhân vật thực tế trong truyện.";
    $user = "CONTEXT BỘ TRUYỆN:\n$context\n\n---\nNHIỆM VỤ:\n$custom_prompt";

    $res = temply_call_ai($sys, $user, 0.9);
    if (is_wp_error($res)) {
        wp_send_json_error(['message' => $res->get_error_message()]);
    }

    wp_send_json_success(['result' => trim($res)]);
});

// AJAX: Bệnh Viện Save Meta
add_action('wp_ajax_temply_bv_save_meta', function() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $truyen_id = intval($_POST['truyen_id']);
    if(!$truyen_id) wp_send_json_error(['message' => 'Lỗi ID truyện.']);

    update_post_meta($truyen_id, '_temply_ai_genre', sanitize_text_field($_POST['genre']));
    update_post_meta($truyen_id, 'truyen_theloai', sanitize_text_field($_POST['genre'])); // Legacy key
    update_post_meta($truyen_id, '_temply_ai_tone', sanitize_text_field($_POST['tone']));
    update_post_meta($truyen_id, '_temply_ai_hook', sanitize_textarea_field($_POST['hook']));
    update_post_meta($truyen_id, '_temply_ai_world', sanitize_textarea_field($_POST['world']));
    update_post_meta($truyen_id, 'truyen_boi_canh', sanitize_textarea_field($_POST['world'])); // Legacy key
    update_post_meta($truyen_id, '_temply_ai_characters', sanitize_textarea_field($_POST['chars']));
    update_post_meta($truyen_id, '_temply_ai_script', sanitize_textarea_field($_POST['script']));

    wp_send_json_success(['message' => 'Đã lưu thông tin truyện thành công!']);
});

// AJAX: Bệnh Viện Tối Ưu SEO Rank Math
add_action('wp_ajax_temply_bv_optimize_seo_rm', function() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $truyen_id = intval($_POST['truyen_id']);
    if(!$truyen_id) wp_send_json_error(['message' => 'Lỗi ID truyện.']);

    require_once plugin_dir_path(__FILE__) . 'includes/openai-api.php';

    $title = get_the_title($truyen_id);
    $genre = sanitize_text_field($_POST['genre'] ?? '');
    $hook = sanitize_textarea_field($_POST['hook'] ?? '');
    $world = sanitize_textarea_field($_POST['world'] ?? '');

    $sys = "Bạn là CHUYÊN GIA SEO. Nhiệm vụ: Viết tiêu đề và mô tả SEO chuẩn click-bait cho truyện web. Output CHỈ LÀ JSON: {\"title\": \"Đọc Truyện [Tên Truyện] (Mới Cập Nhật) - Cực Cuốn\", \"desc\": \"150 ký tự mô tả giật gân, chứa từ khóa Tên Truyện để tăng tỷ lệ click\", \"keyword\": \"Truyện [Tên Truyện]\"}";
    $user = "Tên Truyện: $title\nThể loại: $genre\nHook/Bối cảnh: $hook\nViết SEO JSON ngay.";

    $res = temply_call_ai($sys, $user, 0.7);
    if(is_wp_error($res)) wp_send_json_error(['message' => $res->get_error_message()]);
    
    // Clean JSON markdown
    $res = preg_replace('/```(?:json)?|```/i', '', $res);
    $data = json_decode(trim($res), true);
    
    if(!$data) wp_send_json_error(['message' => 'Lỗi parse JSON từ AI.']);

    update_post_meta($truyen_id, 'rank_math_title', sanitize_text_field($data['title']));
    update_post_meta($truyen_id, 'rank_math_description', sanitize_text_field($data['desc']));
    update_post_meta($truyen_id, 'rank_math_focus_keyword', sanitize_text_field($data['keyword']));
    
    // For yoast compatibility
    update_post_meta($truyen_id, '_yoast_wpseo_title', sanitize_text_field($data['title']));
    update_post_meta($truyen_id, '_yoast_wpseo_metadesc', sanitize_text_field($data['desc']));
    update_post_meta($truyen_id, '_yoast_wpseo_focuskw', sanitize_text_field($data['keyword']));

    wp_send_json_success(['message' => 'Đã tối ưu SEO xong! Title: ' . esc_html($data['title'])]);
});

// FEATURE: Tự động Xoá / Xoá Tạm / Phục hồi các Chương liên quan khi thao tác trên Bài Truyện
add_action('wp_trash_post', function($post_id) {
    if (get_post_type($post_id) === 'truyen') {
        $chaps = get_posts(['post_type' => 'chuong', 'meta_key' => '_truyen_id', 'meta_value' => $post_id, 'posts_per_page' => -1, 'post_status' => 'any']);
        foreach($chaps as $c) wp_trash_post($c->ID);
    }
});
add_action('untrash_post', function($post_id) {
    if (get_post_type($post_id) === 'truyen') {
        $chaps = get_posts(['post_type' => 'chuong', 'meta_key' => '_truyen_id', 'meta_value' => $post_id, 'posts_per_page' => -1, 'post_status' => 'any']);
        foreach($chaps as $c) wp_untrash_post($c->ID);
    }
});
add_action('before_delete_post', function($post_id) {
    if (get_post_type($post_id) === 'truyen') {
        $chaps = get_posts(['post_type' => 'chuong', 'meta_key' => '_truyen_id', 'meta_value' => $post_id, 'posts_per_page' => -1, 'post_status' => 'any']);
        foreach($chaps as $c) wp_delete_post($c->ID, true);
    }
});

function temply_api_backfill_covers() {
    $args = ['post_type' => 'truyen', 'posts_per_page' => 5, 'meta_query' => [['key' => '_thumbnail_id', 'compare' => 'NOT EXISTS']]];
    $posts = get_posts($args);
    foreach($posts as $p) {
        wp_remote_get(home_url('/wp-json/temply/v1/backfill-cover?id=' . $p->ID), ['blocking' => false]);
    }
    return ['success' => true, 'count' => count($posts)];
}

function temply_api_backfill_cover() {
    $q = new WP_Query([
        'post_type' => ['post', 'page', 'truyen'],
        'posts_per_page' => 1,
        'post_status' => 'publish',
        'meta_query' => [
            [
                'key' => '_thumbnail_id',
                'compare' => 'NOT EXISTS'
            ]
        ]
    ]);
    if(!$q->have_posts()) return rest_ensure_response(['status'=>'done']);
    
    $post = $q->posts[0];
    
    $title = $post->post_title;
    $prompt = "A simple, clean, minimalist flat vector illustration representing: " . $title . " web design, corporate aesthetics, 8k";
    if($post->post_type === 'truyen') {
        $prompt = "Vietnamese web novel book cover art, illustration, fantasy anime style, professional digital painting, title concept: " . $title . " masterpiece";
    }
    
    $img_url = "https://image.pollinations.ai/prompt/" . rawurlencode($prompt) . "?width=800&height=600&seed=" . wp_rand(1, 99999) . "&nologo=true";
    
    require_once(ABSPATH . 'wp-admin/includes/media.php');
    require_once(ABSPATH . 'wp-admin/includes/file.php');
    require_once(ABSPATH . 'wp-admin/includes/image.php');
    
    $tmp = download_url($img_url, 30);
    if(is_wp_error($tmp)) return rest_ensure_response(['status'=>'error_download', 'msg' => $tmp->get_error_message()]);
    
    $file_array = [
        'name' => 'cover-' . $post->ID . '-' . wp_rand(100,999) . '.jpg',
        'tmp_name' => $tmp
    ];
    
    $att_id = media_handle_sideload($file_array, $post->ID);
    if(is_wp_error($att_id)) {
        @unlink($tmp);
        return rest_ensure_response(['status'=>'error_sideload', 'msg' => $att_id->get_error_message()]);
    }
    
    set_post_thumbnail($post->ID, $att_id);
    return rest_ensure_response(['status'=>'success', 'post_id'=>$post->ID, 'title'=>$title]);
}
