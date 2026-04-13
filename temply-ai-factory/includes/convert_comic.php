<?php
if (!defined('ABSPATH')) exit;

add_action('wp_ajax_temply_step_convert_comic_init', 'temply_step_convert_comic_init');
function temply_step_convert_comic_init() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $source_id = intval($_POST['source_id'] ?? 0);
    if (!$source_id) wp_send_json_error(['message' => 'Lỗi ID.']);
    
    $source_post = get_post($source_id);
    if (!$source_post) wp_send_json_error(['message' => 'Không tìm thấy truyện gốc.']);
    
    // Create new comic truyen
    $new_title = $source_post->post_title . ' [Bản Comic]';
    
    // Check if exists
    $existing = get_page_by_title($new_title, OBJECT, 'truyen');
    if ($existing) {
        $truyen_id = $existing->ID;
    } else {
        $truyen_id = wp_insert_post([
            'post_title' => $new_title,
            'post_content' => $source_post->post_content,
            'post_status' => 'publish',
            'post_type' => 'truyen',
            'post_author' => get_current_user_id()
        ]);
        
        if (is_wp_error($truyen_id)) wp_send_json_error(['message' => 'Lỗi tạo rễ.']);
        
        // Add meta format
        update_post_meta($truyen_id, '_format', 'comic');
        
        // SEO rank math
        update_post_meta($truyen_id, 'rank_math_title', "Đọc truyện tranh $new_title");
        update_post_meta($truyen_id, 'rank_math_focus_keyword', "Truyện tranh $new_title");
    }
    
    // Fetch chapters list
    $q = new WP_Query([
        'post_type' => 'chuong',
        'meta_query'=>[['key'=>'_truyen_id','value'=>$source_id,'compare'=>'=']],
        'orderby' => 'menu_order date',
        'order' => 'ASC',
        'posts_per_page' => -1
    ]);
    
    $chapters = [];
    foreach($q->posts as $p) {
        $chapters[] = [
            'id' => $p->ID,
            'title' => str_replace($source_post->post_title, '', $p->post_title) // keep mostly the chapter numb
        ];
    }
    
    wp_send_json_success([
        'truyen_id' => $truyen_id,
        'title' => $new_title,
        'chapters' => $chapters
    ]);
}

add_action('wp_ajax_temply_step_convert_comic_chapter', 'temply_step_convert_comic_chapter');
function temply_step_convert_comic_chapter() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $truyen_id = intval($_POST['truyen_id'] ?? 0);
    $chap_source_id = intval($_POST['chap_source_id'] ?? 0);
    $ai_model = sanitize_text_field($_POST['ai_model'] ?? 'gemini');
    $art = sanitize_text_field($_POST['art'] ?? 'Manga Đen trắng Nhật Bản');
    $chap_num = intval($_POST['chap_num'] ?? 1);
    $num_panels = sanitize_text_field($_POST['num_panels'] ?? '8-15');
    
    if (!$truyen_id || !$chap_source_id) wp_send_json_error(['message' => 'Thiếu dữ liệu.']);
    
    $source_chap = get_post($chap_source_id);
    $content_text = strip_tags($source_chap->post_content);
    
    $system_prompt = "Bạn là Kịch bản gia Manga chuyên nghiệp. 
Nhiệm vụ: Phân tích 1 đoạn truyện chữ, chia nhỏ nó thành MẠNG LƯỚI $num_panels PHÂN CẢNH (Panels).
Trả về MỘT mảng JSON duy nhất chứa đoạn:
[
  {
    \"dialogue\": \"Lời thoại chắt lọc từ text gốc\",
    \"prompt\": \"Mô tả TRỰC QUAN bối cảnh/nhân vật BẰNG TIẾNG ANH chuyên nghiệp (ví dụ: 1 boy looking far away, emotional, dynamic lighting...)\"
  }
]
Không được bôi markdown hay giải thích thêm.";
    
    $user_prompt = "Nội dung truyện chữ gốc:\n" . mb_substr($content_text, 0, 4500);
    
    $response = temply_call_ai($system_prompt, $user_prompt, 0.7);
    
    if(is_wp_error($response)) wp_send_json_error(['message' => 'AI đứt: ' . $response->get_error_message()]);
    
    $clean_json = preg_replace('/```json|```/', '', $response);
    $scenes = json_decode(trim($clean_json), true);
    if (!is_array($scenes)) wp_send_json_error(['message' => 'AI Parse JSON lỗi.']);
    
    $art_style_map = [
        'Manga Đen trắng Nhật Bản' => 'manga black and white, monochrome, japanese manga style, ink drawing, no color',
        'Manhwa màu Hàn Quốc'      => 'manhwa full color, korean webtoon style, vibrant colors, detailed digital art'
    ];
    $style_suffix = $art_style_map[$art] ?? 'manga black and white';
    
    $html_content = '<div class="comic-container" style="max-width: 800px; margin: 0 auto;">';
    $warmup_urls = [];
    
    foreach($scenes as $idx => $sc) {
        $full_prompt = $sc['prompt'] . ', ' . $style_suffix;
        $escaped_prompt = urlencode($full_prompt);
        $seed = wp_rand(1000, 99999);
        $img_url = "https://image.pollinations.ai/prompt/" . $escaped_prompt . "?width=600&height=500&seed=" . $seed . "&nologo=true";
        $warmup_urls[] = $img_url;
        
        $html_content .= '
        <div class="comic-panel relative mb-6 rounded-lg overflow-hidden border-2 border-gray-800 shadow-xl bg-black">
            <img class="w-full h-auto min-h-[300px] object-cover pollination-lazy" 
                 src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" 
                 data-src="'.esc_url($img_url).'" />
            <div class="absolute bottom-0 left-0 w-full bg-gradient-to-t from-black/80 to-transparent p-4">
                <div class="bg-white text-black p-3 rounded-2xl rounded-bl-none font-bold text-sm shadow-md italic">
                    "'.esc_html($sc['dialogue']).'"
                </div>
            </div>
        </div>';
    }
    $html_content .= '</div>';
    
    $final_title = "Chương $chap_num: Bắt đầu";
    
    $post_id = wp_insert_post([
        'post_title'   => $source_chap->post_title,
        'post_content' => $html_content,
        'post_status'  => 'publish',
        'post_type'    => 'chuong',
        'menu_order'   => $chap_num,
        'post_author'  => get_current_user_id()
    ]);
    
    if(is_wp_error($post_id)) wp_send_json_error(['message' => 'Lỗi tạo Chương.']);
    
    update_post_meta($post_id, '_truyen_id', $truyen_id);
    
    wp_send_json_success([
        'chuong_id' => $post_id,
        'title' => $source_chap->post_title,
        'warmup_urls' => $warmup_urls
    ]);
}
