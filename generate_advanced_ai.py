import re

openai_api = """<?php
if (!defined('ABSPATH')) exit;

/**
 * Gọi API OpenAI (GPT-4o-mini).
 */
function temply_call_openai($system_prompt, $user_prompt, $temperature = 0.7) {
    $api_key = get_option('temply_openai_api_key', '');
    if(empty($api_key)) return new WP_Error('no_api_key', 'Chưa cấu hình API Key');

    $url = "https://api.openai.com/v1/chat/completions";
    
    $payload = [
        "model" => "gpt-4o-mini",
        "messages" => [
            ["role" => "system", "content" => $system_prompt],
            ["role" => "user", "content" => $user_prompt]
        ],
        "temperature" => $temperature
    ];

    $response = wp_remote_post($url, [
        'headers' => [
            'Content-Type' => 'application/json',
            'Authorization' => 'Bearer ' . $api_key
        ],
        'body'    => json_encode($payload),
        'timeout' => 90
    ]);

    if(is_wp_error($response)) {
        return $response;
    }

    $body = wp_remote_retrieve_body($response);
    $data = json_decode($body, true);

    if(isset($data['error'])) {
        return new WP_Error('api_error', $data['error']['message']);
    }

    if(isset($data['choices'][0]['message']['content'])) {
        return $data['choices'][0]['message']['content'];
    }

    return new WP_Error('parse_error', 'Không đọc được phản hồi từ AI');
}

/**
 * Hàm hỗ trợ Tải Ảnh Từ URL làm Thumbnail
 */
function temply_upload_external_image($image_url, $post_id, $alt_text) {
    require_once(ABSPATH . 'wp-admin/includes/media.php');
    require_once(ABSPATH . 'wp-admin/includes/file.php');
    require_once(ABSPATH . 'wp-admin/includes/image.php');

    $tmp = download_url($image_url);
    if(is_wp_error($tmp)) return false;

    $file_array = [
        'name' => basename(parse_url($image_url, PHP_URL_PATH)) . '.jpg',
        'tmp_name' => $tmp
    ];

    $id = media_handle_sideload($file_array, $post_id);
    if(is_wp_error($id)) {
        @unlink($file_array['tmp_name']);
        return false;
    }

    update_post_meta($id, '_wp_attachment_image_alt', $alt_text);
    set_post_thumbnail($post_id, $id);
    return $id;
}


/**
 * STEP 1: The Oracle - World Building
 */
add_action('wp_ajax_temply_step_oracle', 'temply_ajax_oracle');
function temply_ajax_oracle() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $genre = sanitize_text_field($_POST['genre'] ?? '');
    $tone = sanitize_text_field($_POST['tone'] ?? '');
    $keywords = sanitize_textarea_field($_POST['keywords'] ?? '');

    $system_prompt = "Bạn là THE ORACLE - Chuyên gia thiết lập thế giới quan (World-building) cho tiểu thuyết mạng. Hãy phản hồi thật súc tích, ngắn gọn.";
    if($genre == "Tổng tài") $system_prompt .= "\\nTập trung vào sự giàu sang tột đỉnh, bá đạo, các tập đoàn đa quốc gia và những mâu thuẫn giai cấp tinh tế nhưng tàn nhẫn.";
    if($genre == "Trọng sinh") $system_prompt .= "\\nTập trung vào sự hối tiếc ở kiếp trước, sự phản bội, và hành trình trả thù máu lạnh, sửa chữa sai lầm ở kiếp này.";
    if($genre == "Xuyên không") $system_prompt .= "\\nTập trung vào sự khác biệt văn hóa, lợi thế từ kỹ năng/kiến thức tương lai áp dụng vào thế giới cũ.";
    if($genre == "Tu tiên") $system_prompt .= "\\nTập trung vào luật rừng, thực lực vi tôn, pháp bảo, kỳ ngộ, hệ thống phân cấp tu vi rõ ràng.";

    $user_prompt = "Hãy thiết lập bối cảnh thế giới độc đáo cho một câu chuyện thuộc thể loại $genre, với văn phong $tone. Các yếu tố bắt buộc: $keywords.\\nTrình bày dưới dạng các gạch đầu dòng rõ ràng về Bối cảnh chung, Quy luật cốt lõi, và Xung đột chính.";

    $response = temply_call_openai($system_prompt, $user_prompt, 0.9);
    
    if(is_wp_error($response)) {
        wp_send_json_error(['message' => $response->get_error_message()]);
    }
    wp_send_json_success(['result' => $response]);
}

/**
 * STEP 2: The Puppet Master - Characters
 */
add_action('wp_ajax_temply_step_puppet', 'temply_ajax_puppet');
function temply_ajax_puppet() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $world = sanitize_textarea_field($_POST['world'] ?? '');
    
    $system_prompt = "Bạn là THE PUPPET MASTER - Bậc thầy tâm lý học và sáng tạo nhân vật. Bạn tạo ra những nhân vật có chiều sâu, góc khuất và động cơ rõ ràng.";
    $user_prompt = "Dựa vào bối cảnh thế giới sau:\\n$world\\n\\nHãy tạo ra 2 nhân vật: Nhân vật chính và Nhân vật phản diện (hoặc cản trở lớn nhất). Chỉ định tên, ngoại hình, tính cách bề ngoài, tổn thương sâu kín bên trong, và mục tiêu tối thượng của họ.";

    $response = temply_call_openai($system_prompt, $user_prompt, 0.8);
    
    if(is_wp_error($response)) {
        wp_send_json_error(['message' => $response->get_error_message()]);
    }
    wp_send_json_success(['result' => $response]);
}

/**
 * STEP 3: The Architect - Outline
 */
add_action('wp_ajax_temply_step_architect', 'temply_ajax_architect');
function temply_ajax_architect() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $world = sanitize_textarea_field($_POST['world'] ?? '');
    $characters = sanitize_textarea_field($_POST['characters'] ?? '');

    $system_prompt = "Bạn là THE ARCHITECT - Chuyên gia dựng kịch bản. Mỗi chương gieo một nút thắt (HOOK) ở cuối.";
    $user_prompt = "Dựa vào Thế giới:\\n$world\\n\\nVà Nhân vật:\\n$characters\\n\\nHãy lập dàn ý chi tiết cho 5 chương đầu tiên. 
    BẠN BẮT BUỘC TRẢ VỀ CHÍNH XÁC ĐỊNH DẠNG JSON MẢNG, KHÔNG THÊM BẤT KỲ TEXT NÀO KHÁC BÊN NGOÀI:
    [
      { \"chap_num\": 1, \"summary\": \"Nội dung...\" },
      { \"chap_num\": 2, \"summary\": \"Nội dung...\" },
      { \"chap_num\": 3, \"summary\": \"Nội dung...\" },
      { \"chap_num\": 4, \"summary\": \"Nội dung...\" },
      { \"chap_num\": 5, \"summary\": \"Nội dung...\" }
    ]";

    $response = temply_call_openai($system_prompt, $user_prompt, 0.8);
    
    if(is_wp_error($response)) {
        wp_send_json_error(['message' => $response->get_error_message()]);
    }
    
    $clean_json = preg_replace('/```json|```/', '', $response);
    $data = json_decode(trim($clean_json), true);
    
    if(!$data) {
        wp_send_json_error(['message' => 'Lỗi Parse JSON Dàn Ý. Thử lại.', 'raw' => $response]);
    }

    wp_send_json_success(['result' => $data]);
}

/**
 * STEP 4: The Publisher - Tạo Đầu Truyện & Đẻ Ảnh Cover
 */
add_action('wp_ajax_temply_step_create_story', 'temply_ajax_create_story');
function temply_ajax_create_story() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $world = sanitize_textarea_field($_POST['world'] ?? '');
    $characters = sanitize_textarea_field($_POST['characters'] ?? '');
    $genre = sanitize_text_field($_POST['genre'] ?? '');
    
    $system_prompt = "Bạn là The Publisher. Dựa vào Bối Cảnh và Nhân Vật, sinh ra đúng 1 chuỗi JSON chứa Tựa Đề Truyện (vô cùng hấp dẫn, bắt mắt kiểu web novel) và Tiếng Anh Prompt để tạo ảnh bìa. KHÔNG TEXT THỪA.";
    $user_prompt = "[World]\\n$world\\n\\n[Char]\\n$characters\\n\\nTrả về JSON:
    {
      \"title\": \"Tên truyện giật gân, ví dụ: Thiên Tôn Trùng Sinh...\",
      \"desc\": \"Tóm tắt hấp dẫn 300 chữ\",
      \"cover_prompt\": \"1 câu tiếng anh mô tả ngắn gọn cảnh tượng hoặc nhân vật anime/fantasy để vẽ ảnh bìa. Ví dụ: A handsome CEO in a dark suit standing...\"
    }";

    $response = temply_call_openai($system_prompt, $user_prompt, 0.9);
    $clean_json = preg_replace('/```json|```/', '', $response);
    $data = json_decode(trim($clean_json), true);

    if(!$data || !isset($data['title'])) wp_send_json_error(['message' => 'Lỗi Parse Tên truyện']);

    // 1. Tạo post_type=truyen
    $post_id = wp_insert_post([
        'post_title'   => sanitize_text_field($data['title']),
        'post_content' => wp_kses_post($data['desc']), // Có thể coi đây là phần Giới thiệu
        'post_status'  => 'draft',
        'post_type'    => 'truyen',
        'post_author'  => get_current_user_id()
    ]);
    
    if(is_wp_error($post_id)) {
        wp_send_json_error(['message' => 'Không thể tạo bài Đăng.']);
    }

    // 2. Set Taxonomy (Thể loại)
    $term = get_term_by('name', $genre, 'the_loai');
    if(!$term && !is_wp_error($term)) {
        $new_term = wp_insert_term($genre, 'the_loai');
        if(!is_wp_error($new_term)) {
            wp_set_object_terms($post_id, intval($new_term['term_id']), 'the_loai');
        }
    } else if($term) {
        wp_set_object_terms($post_id, intval($term->term_id), 'the_loai');
    }

    // 3. Automated Image Generation via Pollinations.ai 
    // Stable Diffusion - No API Key Needed!
    $escaped_prompt = urlencode($data['cover_prompt'] . ", masterpiece, best quality, highly detailed cover art");
    $image_url = "https://image.pollinations.ai/prompt/" . $escaped_prompt . "?width=600&height=900&nologo=true";
    
    $thumb_id = temply_upload_external_image($image_url, $post_id, $data['title']);
    
    wp_send_json_success([
        'truyen_id' => $post_id,
        'title' => $data['title'],
        'thumb' => $thumb_id ? 'Đã cài Cover Ảnh AI' : 'Lỗi cài Cover'
    ]);
}

/**
 * STEP 5: The Ghostwriter - Viết các Chương nội dung
 */
add_action('wp_ajax_temply_step_write_chapter', 'temply_ajax_write_chapter');
function temply_ajax_write_chapter() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $truyen_id = intval($_POST['truyen_id'] ?? 0);
    $chap_num = intval($_POST['chap_num'] ?? 1);
    $summary = sanitize_textarea_field($_POST['summary'] ?? '');
    $genre = sanitize_text_field($_POST['genre'] ?? '');
    $tone = sanitize_text_field($_POST['tone'] ?? '');

    if(!$truyen_id) wp_send_json_error(['message' => 'Mất ID Truyện.']);

    $system_prompt = "Bạn là THE GHOSTWRITER. VĂN HỌC, SHOW DON'T TELL. Cố gắng viết thật dài, chi tiết, hội thoại chân thực.";
    $user_prompt = "Hãy VIẾT CHI TIẾT Chương $chap_num dành cho Thể loại $genre, văn phong $tone, dựa theo tóm tắt:\\n$summary\\n
    Sử dụng định dạng HTML (<p>, <strong>).\\nTrả về JSON:
    {
      \"title\": \"Chương $chap_num: Tên chương ấn tượng\",
      \"content\": \"Nội dung HTML...\"
    }";

    $response = temply_call_openai($system_prompt, $user_prompt, 0.9);
    $clean_json = preg_replace('/```json|```/', '', $response);
    $data = json_decode(trim($clean_json), true);

    if(!$data || !isset($data['title'])) wp_send_json_error(['message' => 'Lỗi Parse JSON Nội dung.']);

    $post_id = wp_insert_post([
        'post_title'   => sanitize_text_field($data['title']),
        'post_content' => wp_kses_post($data['content']),
        'post_status'  => 'draft',
        'post_type'    => 'chuong',
        'post_author'  => get_current_user_id()
    ]);

    if(is_wp_error($post_id)) wp_send_json_error(['message' => 'Lỗi tạo Chương.']);

    update_post_meta($post_id, '_truyen_id', $truyen_id); // Liên kết chương với truyện

    wp_send_json_success([
        'chuong_id' => $post_id,
        'title' => $data['title']
    ]);
}
"""

with open("temply-ai-factory/includes/openai-api.php", "w", encoding="utf-8") as f:
    f.write(openai_api)

print("Updated openai_api.php")
