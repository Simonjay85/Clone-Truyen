import os

# 1. Update temply-ai-factory.php
with open("temply-ai-factory/temply-ai-factory.php", "r", encoding="utf-8") as f:
    core = f.read()
core = core.replace("gemini-api.php", "openai-api.php")
core = core.replace("API Gemini 1.5", "API OpenAI (GPT-4o-mini)")
with open("temply-ai-factory/temply-ai-factory.php", "w", encoding="utf-8") as f:
    f.write(core)

# 2. Update admin-ui.php
with open("temply-ai-factory/admin-ui.php", "r", encoding="utf-8") as f:
    ui = f.read()
ui = ui.replace("temply_gemini_api_key", "temply_openai_api_key")
ui = ui.replace("Gemini API Key", "OpenAI API Key")
ui = ui.replace("AIzaSy...", "sk-proj-...")
ui = ui.replace("Gemini 1.5", "GPT-4o-mini")
with open("temply-ai-factory/admin-ui.php", "w", encoding="utf-8") as f:
    f.write(ui)

# 3. Create openai-api.php
openai_php = """<?php
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
        'timeout' => 60
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
 * STEP 3: The Architect - Dàn ý móc nối (Hooks)
 */
add_action('wp_ajax_temply_step_architect', 'temply_ajax_architect');
function temply_ajax_architect() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $world = sanitize_textarea_field($_POST['world'] ?? '');
    $characters = sanitize_textarea_field($_POST['characters'] ?? '');

    $system_prompt = "Bạn là THE ARCHITECT - Chuyên gia dựng kịch bản với nhịp độ dồn dập. Mỗi chương phải gieo một nút thắt (HOOK) ở cuối để ép độc giả đọc tiếp.";
    $user_prompt = "Dựa vào Thế giới:\\n$world\\n\\nVà Nhân vật:\\n$characters\\n\\nHãy lập dàn ý chi tiết cho 5 chương đầu tiên. Với mỗi chương, mô tả Diễn biến chính và Nút thắt/Hook ở cuối chương.";

    $response = temply_call_openai($system_prompt, $user_prompt, 0.8);
    
    if(is_wp_error($response)) {
        wp_send_json_error(['message' => $response->get_error_message()]);
    }
    wp_send_json_success(['result' => $response]);
}

/**
 * STEP 4: The Ghostwriter - Viết Chương 1 & Đăng Nháp
 */
add_action('wp_ajax_temply_step_ghostwriter', 'temply_ajax_ghostwriter');
function temply_ajax_ghostwriter() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $world = sanitize_textarea_field($_POST['world'] ?? '');
    $characters = sanitize_textarea_field($_POST['characters'] ?? '');
    $outline = sanitize_textarea_field($_POST['outline'] ?? '');
    $genre = sanitize_text_field($_POST['genre'] ?? '');
    $tone = sanitize_text_field($_POST['tone'] ?? '');

    $system_prompt = "Bạn là THE GHOSTWRITER - Nhà văn truyện mạng số 1 thế giới. 
    QUY TẮC CỐT LÕI MÀ BẠN PHẢI TUÂN THỦ:
    1. VĂN HỌC, KHÔNG LIỆT KÊ: Tuyệt đối không viết theo gạch đầu dòng hay kiểu báo cáo. Phải miêu tả cảnh vật, nội tâm nhân vật sinh động.
    2. SHOW, DON'T TELL: Thay vì nói 'anh ấy tức giận', hãy miêu tả 'Móng tay anh găm chặt vào nệm ghế tới rỉ máu'.
    3. HỘI THOẠI CHÂN THỰC: Sử dụng nhiều câu thoại sắc bén, mang đặc trưng của thể loại $genre và văn phong $tone.
    4. Chiều dài: Cố gắng viết dài, ít nhất 1000 chữ.";

    $user_prompt = "Dựa vào toàn bộ tài liệu sau:\\n[Thế Giới]\\n$world\\n\\n[Nhân vật]\\n$characters\\n\\n[Dàn Ý]\\n$outline\\n\\nHãy VIẾT CHI TIẾT CHƯƠNG 1 dựa theo dàn ý của chương 1.
    Sử dụng cú pháp định dạng HTML cơ bản (như <p>, <strong>, <em>) cho bài viết.
    Đầu ra bắt buộc theo định dạng JSON như sau, không xuất hiện text dư thừa:
    {
      \"title\": \"Tên chương truyện / Tiêu đề cực kỳ giật gân, thu hút\",
      \"content\": \"Nội dung chi tiết chương 1 dạng HTML\"
    }";

    $response = temply_call_openai($system_prompt, $user_prompt, 0.9);
    
    if(is_wp_error($response)) {
        wp_send_json_error(['message' => $response->get_error_message()]);
    }

    $clean_json = preg_replace('/```json|```/', '', $response);
    $data = json_decode(trim($clean_json), true);

    if(!$data || !isset($data['title'])) {
        wp_send_json_error(['message' => 'Lỗi Parse JSON từ AI. Hãy thử lại.', 'raw' => $response]);
    }

    $post_id = wp_insert_post([
        'post_title'   => sanitize_text_field($data['title']),
        'post_content' => wp_kses_post($data['content']),
        'post_status'  => 'draft',
        'post_author'  => get_current_user_id()
    ]);

    if(is_wp_error($post_id)) {
        wp_send_json_error(['message' => 'Lỗi khi tạo nháp trong Database.']);
    }

    wp_send_json_success([
        'post_id' => $post_id,
        'title' => $data['title'],
        'content' => $data['content']
    ]);
}
"""
with open("temply-ai-factory/includes/openai-api.php", "w", encoding="utf-8") as f:
    f.write(openai_php)

if os.path.exists("temply-ai-factory/includes/gemini-api.php"):
    os.remove("temply-ai-factory/includes/gemini-api.php")
    
print("Switched to OpenAI!")
