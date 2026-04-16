<?php
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
/**
 * Gọi API Google Gemini với auto-fallback và usage tracking.
 * Thứ tự fallback: gemini-2.5-flash → gemini-2.0-flash-lite → gemini-1.5-pro
 */
function temply_call_gemini($system_prompt, $user_prompt, $temperature = 0.7, $force_model = '') {
    $paid_key = get_option('temply_gemini_api_key', '');
    $free_key = get_option('temply_gemini_api_key_free', '');
    
    if(empty($paid_key) && empty($free_key)) return new WP_Error('no_api_key', 'Chưa cấu hình Gemini API Key');

    // Danh sách model theo ưu tiên fallback ngâm cứu:
    $model_chain = [
        ['tier' => 'free', 'model' => 'gemini-2.5-flash', 'id' => 'free_gemini-2.5-flash', 'key' => $free_key],
        ['tier' => 'free', 'model' => 'gemini-2.0-flash', 'id' => 'free_gemini-2.0-flash', 'key' => $free_key],
        ['tier' => 'paid', 'model' => 'gemini-2.5-flash', 'id' => 'paid_gemini-2.5-flash', 'key' => $paid_key],
        ['tier' => 'paid', 'model' => 'gemini-1.5-pro',   'id' => 'paid_gemini-1.5-pro',   'key' => $paid_key],
    ];

    if (!empty($force_model)) {
        $model_chain = [
            ['tier' => 'paid', 'model' => $force_model, 'id' => 'paid_' . $force_model, 'key' => $paid_key]
        ];
    }

    $last_error = null;
    foreach ($model_chain as $node) {
        $api_key = $node['key'];
        if(empty($api_key)) continue;

        $model_id  = $node['model'];
        $record_id = $node['id'];

        $url = "https://generativelanguage.googleapis.com/v1beta/models/{$model_id}:generateContent?key=" . $api_key;

        $payload = [
            "system_instruction" => ["parts" => [["text" => $system_prompt]]],
            "contents"           => [["role" => "user", "parts" => [["text" => $user_prompt]]]],
            "generationConfig"   => ["temperature" => $temperature]
        ];

        $response = wp_remote_post($url, [
            'headers' => ['Content-Type' => 'application/json'],
            'body'    => json_encode($payload),
            'timeout' => 120
        ]);

        if (is_wp_error($response)) {
            $last_error = $response;
            continue; // Thử model tiếp theo
        }

        $http_code = wp_remote_retrieve_response_code($response);
        $body      = wp_remote_retrieve_body($response);
        $data      = json_decode($body, true);

        // 429 hoặc RESOURCE_EXHAUSTED = hết quota Flash → fallback
        $is_quota_error = ($http_code === 429)
            || (isset($data['error']['status']) && in_array($data['error']['status'], ['RESOURCE_EXHAUSTED', 'QUOTA_EXCEEDED']))
            || (isset($data['error']['code'])   && $data['error']['code'] === 429);

        if ($is_quota_error) {
            // Ghi flag ”Flash đã hết quota hôm nay”
            temply_gemini_mark_model_exhausted($record_id);
            $last_error = new WP_Error('quota_exceeded', "[{$record_id}] Hết quota - tự chuyển model...");
            continue;
        }

        if (isset($data['error'])) {
            $last_error = new WP_Error('api_error', $data['error']['message'] ?? json_encode($data['error']));
            // Lỗi khác (không phải quota) → không fallback
            return $last_error;
        }

        if (isset($data['candidates'][0]['content']['parts'][0]['text'])) {
            // ✅ Thành công - ghi usage
            temply_gemini_log_usage($record_id);
            return $data['candidates'][0]['content']['parts'][0]['text'];
        }

        $last_error = new WP_Error('parse_error', "Không đọc được phản hồi từ Gemini [{$record_id}]");
    }

    return $last_error ?? new WP_Error('all_models_failed', 'Tất cả Gemini models đều thất bại');
}

/**
 * Ghi lại lượt gọi thành công theo model và ngày
 */
function temply_gemini_log_usage($model_id) {
    $today = gmdate('Y-m-d');
    $key   = '_temply_gemini_usage_' . $today;
    $usage = get_option($key, []);
    if (!is_array($usage)) $usage = [];
    $usage[$model_id] = ($usage[$model_id] ?? 0) + 1;
    $usage['_updated'] = time();
    update_option($key, $usage, false);
}

/**
 * Đánh dấu model đã bị giới hạn quota hôm nay (reset lúc 0h)
 */
function temply_gemini_mark_model_exhausted($model_id) {
    $today = gmdate('Y-m-d');
    $key   = '_temply_gemini_exhausted_' . $today;
    $list  = get_option($key, []);
    if (!is_array($list)) $list = [];
    if (!in_array($model_id, $list)) $list[] = $model_id;
    update_option($key, $list, false);
}

/**
 * Endpoint AJAX: Lấy thống kê usage Gemini 7 ngày gần nhất
 */
add_action('wp_ajax_temply_gemini_usage_stats', function() {
    check_ajax_referer('temply_ai_nonce', 'nonce');

    // Gemini free-tier limits (per day)
    $limits = [
        'free_gemini-2.5-flash' => 500,  
        'free_gemini-2.0-flash' => 1500,
        'paid_gemini-2.5-flash' => 99999999, // Vô cực cho paid
        'paid_gemini-1.5-pro'   => 99999999,
    ];

    $days = [];
    for ($i = 6; $i >= 0; $i--) {
        $d     = gmdate('Y-m-d', strtotime("-{$i} days"));
        $key   = '_temply_gemini_usage_' . $d;
        $ex_key= '_temply_gemini_exhausted_' . $d;
        $usage = get_option($key, []);
        $exhausted = get_option($ex_key, []);
        if (!is_array($usage)) $usage = [];
        unset($usage['_updated']);
        $days[$d] = [
            'usage'     => $usage,
            'exhausted' => is_array($exhausted) ? $exhausted : [],
        ];
    }

    wp_send_json_success([
        'days'   => $days,
        'limits' => $limits,
        'today'  => gmdate('Y-m-d'),
    ]);
});

/**
 * Endpoint AJAX: Bắn trigger từ trình duyệt Browser để ghi nhận lượt xài hoặc báo cháy (quota)
 */
add_action('wp_ajax_temply_track_gemini_usage_browser', function() {
    // Không dùng check_ajax_referer vì trình duyệt gửi POST kèm nonce nhưng có thể key tên khác tuỳ theo JS
    // chỉ cần log lại là được.
    $model = isset($_POST['model']) ? sanitize_text_field($_POST['model']) : '';
    if ($model) {
        $status = sanitize_text_field($_POST['status'] ?? 'success');
        if ($status === 'success') {
            temply_gemini_log_usage($model);
        } else if ($status === 'exhausted') {
            temply_gemini_mark_model_exhausted($model);
        }
    }
    wp_send_json_success();
});


/**
 * Gọi API Anthropic Claude.
 * $model_override: 'haiku' (mặc định, rẻ+nhanh) hoặc 'sonnet' (chất lượng cao, tốn tiền hơn)
 */
function temply_call_claude($system_prompt, $user_prompt, $temperature = 0.7, $model_override = 'haiku') {
    $api_key = get_option('temply_claude_api_key', '');
    if(empty($api_key)) return new WP_Error('no_api_key', 'Chưa cấu hình Claude API Key');

    $url = 'https://api.anthropic.com/v1/messages';

    // Haiku 4.5: ~$0.008/1K tokens — dùng cho các bước trung gian (brainstorm, outline, review)
    // Sonnet 4.6: ~$0.03/1K tokens — chỉ dùng cho viết chương cuối nếu cần
    if ($model_override === 'sonnet') {
        $model     = 'claude-sonnet-4-6';
        $max_tok   = 8000;
    } else {
        $model     = 'claude-haiku-4-5-20251001'; // Mặc định: nhanh, rẻ
        $max_tok   = 4096;
    }

    $payload = [
        'model'       => $model,
        'max_tokens'  => $max_tok,
        'system'      => $system_prompt,
        'messages'    => [
            ['role' => 'user', 'content' => $user_prompt]
        ]
    ];
    if($temperature > 0) {
        $payload['temperature'] = (float)$temperature;
    }

    $body_json = json_encode($payload, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);

    // Timeout động: Haiku sinh rất nhanh nên 90s, nhưng Sonnet viết 3000 chữ thì cần tới 300-400s
    $timeout = ($model_override === 'sonnet') ? 400 : 120;

    $response = wp_remote_post($url, [
        'headers' => [
            'content-type'      => 'application/json',
            'x-api-key'         => trim($api_key),
            'anthropic-version' => '2023-06-01',
        ],
        'body'      => $body_json,
        'timeout'   => $timeout,
        'sslverify' => false,
    ]);

    if(is_wp_error($response)) {
        return new WP_Error('network_error', 'Lỗi kết nối Anthropic: ' . $response->get_error_message());
    }

    $http_code = wp_remote_retrieve_response_code($response);
    $body      = wp_remote_retrieve_body($response);
    $data      = json_decode($body, true);

    error_log("[Temply Claude $model] HTTP $http_code | " . substr($body, 0, 300));

    if(isset($data['error'])) {
        $err_type = $data['error']['type'] ?? 'unknown';
        $err_msg  = $data['error']['message'] ?? json_encode($data['error']);
        return new WP_Error('api_error', "[Claude $err_type] $err_msg");
    }

    if(isset($data['content'][0]['text'])) {
        return $data['content'][0]['text'];
    }

    return new WP_Error('parse_error', 'Không đọc được phản hồi từ Claude. Raw: ' . substr($body, 0, 300));
}

/**
 * Điều hướng API (OpenAI, Gemini hoặc Claude)
 * Dùng cho các bước trung gian: Haiku (nhanh + rẻ)
 */
function temply_call_ai($system_prompt, $user_prompt, $temperature = 0.7) {
    if(isset($_POST['ai_model'])) {
        if($_POST['ai_model'] === 'gemini') {
            return temply_call_gemini($system_prompt, $user_prompt, $temperature);
        }
        if($_POST['ai_model'] === 'claude') {
            // Mặc định: Haiku cho tất cả các bước trung gian — rẻ hơn 15x Sonnet
            return temply_call_claude($system_prompt, $user_prompt, $temperature, 'haiku');
        }
    }
    return temply_call_openai($system_prompt, $user_prompt, $temperature);
}

/**
 * Gọi Claude Sonnet 4.6 cho bước VIẾT CHƯƠNG (chất lượng cao).
 * Chỉ dùng khi user thực sự muốn Claude viết nội dung chương cuối.
 */
function temply_call_ai_quality($system_prompt, $user_prompt, $temperature = 0.9) {
    if(isset($_POST['ai_model'])) {
        if($_POST['ai_model'] === 'gemini') {
            return temply_call_gemini($system_prompt, $user_prompt, $temperature);
        }
        if($_POST['ai_model'] === 'claude') {
            // Bước viết chính: dùng Sonnet 4.6 cho chất lượng văn cao nhất
            return temply_call_claude($system_prompt, $user_prompt, $temperature, 'sonnet');
        }
    }
    return temply_call_openai($system_prompt, $user_prompt, $temperature);
}

/**
 * Hàm hỗ trợ Tải Ảnh Từ URL làm Thumbnail
 */
function temply_upload_external_image($image_url, $post_id, $alt_text) {
    require_once(ABSPATH . 'wp-admin/includes/media.php');
    require_once(ABSPATH . 'wp-admin/includes/file.php');
    require_once(ABSPATH . 'wp-admin/includes/image.php');

    $response = wp_remote_get($image_url, [
        'timeout' => 45,
        'headers' => [
            'User-Agent' => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        ]
    ]);
    
    if (is_wp_error($response)) {
        error_log('Temply Upload Lỗi: ' . $response->get_error_message());
        return false;
    }

    $image_data = wp_remote_retrieve_body($response);
    if (empty($image_data)) {
        error_log('Temply Upload Lỗi: Body rỗng');
        return false;
    }

    $filename = 'cover-' . $post_id . '-' . wp_rand(100, 999) . '.jpg';
    $upload = wp_upload_bits($filename, null, $image_data);

    if (!empty($upload['error'])) {
        error_log('Temply Upload Bits Lỗi: ' . $upload['error']);
        return false;
    }
    
    $file_path = $upload['file'];
    $file_name = basename($file_path);
    $file_type = wp_check_filetype($file_name, null);

    $attachment = [
        'post_mime_type' => $file_type['type'],
        'post_title'     => sanitize_file_name($file_name),
        'post_content'   => '',
        'post_status'    => 'inherit'
    ];

    $attach_id = wp_insert_attachment($attachment, $file_path, $post_id);
    if(is_wp_error($attach_id)) return false;
    
    $attach_data = wp_generate_attachment_metadata($attach_id, $file_path);
    wp_update_attachment_metadata($attach_id, $attach_data);
    update_post_meta($attach_id, '_wp_attachment_image_alt', sanitize_text_field($alt_text));
    set_post_thumbnail($post_id, $attach_id);
    
    return $attach_id;
}

/**
 * Hàm hỗ trợ Bóc tách bình luận ảo (AI Seeding) và đẩy trực tiếp vào db
 */
function temply_parse_and_insert_ai_comments($post_id, $raw_ai_text) {
    $parts = explode('---COMMENTS---', $raw_ai_text);
    $main_content = trim($parts[0]);
    
    if (count($parts) > 1 && !empty(trim($parts[1]))) {
        $comments_text = trim($parts[1]);
        $lines = explode("\n", $comments_text);
        
        $inserted = 0;
        foreach ($lines as $line) {
            $line = trim(preg_replace('/^[-*\d\.\s]+/', '', $line)); // Remove bullets/numbers
            if (empty($line)) continue;
            
            // Expected format: Name|Comment
            $split = explode('|', $line, 2);
            if (count($split) === 2) {
                $author = trim(wp_strip_all_tags($split[0]));
                $content = trim(wp_strip_all_tags($split[1]));
                
                if (!empty($author) && !empty($content)) {
                    $time = current_time('mysql');
                    $commentdata = [
                        'comment_post_ID'      => $post_id,
                        'comment_author'       => $author,
                        'comment_author_email' => sanitize_title($author) . mt_rand(10, 99) . '@gmail.com',
                        'comment_content'      => $content,
                        'comment_type'         => 'comment',
                        'comment_parent'       => 0,
                        'comment_approved'     => 1,
                        'comment_date'         => wp_date('Y-m-d H:i:s', strtotime('-' . mt_rand(1, 60) . ' minutes', current_time('timestamp')))
                    ];
                    
                    wp_insert_comment($commentdata);
                    $inserted++;
                }
            }
        }
    }
    
    return $main_content;
}
/**
 * STEP 0: The Analyst (Ngửi Nội Dung Nguồn)
 */
add_action('wp_ajax_temply_step_analyze_source', 'temply_ajax_analyze_source');
function temply_ajax_analyze_source() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $source_text = sanitize_textarea_field($_POST['source_text'] ?? '');
    if(empty($source_text)) wp_send_json_error(['message' => 'Nội dung nguồn trống.']);

    // NẾU LÀ ĐƯỜNG LINK, HÚT NỘI DUNG TỪ OG:DESCRIPTION HOẶC TITLE
    if (preg_match('/^https?:\/\/[^\s]+$/', trim($source_text))) {
        $url = trim($source_text);
        $response = wp_remote_get($url, [
            'timeout' => 15,
            'headers' => [
                'User-Agent' => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
            ]
        ]);
        if (!is_wp_error($response)) {
            $body = wp_remote_retrieve_body($response);
            $extracted_content = '';
            if (preg_match('/<meta[^>]*property=[\'"]og:description[\'"][^>]*content=[\'"]([^\'"]+)[\'"][^>]*>/i', $body, $matches) || 
                preg_match('/<meta[^>]*content=[\'"]([^\'"]+)[\'"][^>]*property=[\'"]og:description[\'"][^>]*>/i', $body, $matches)) {
                $extracted_content .= html_entity_decode($matches[1]) . " \n";
            }
            if (preg_match('/<meta[^>]*property=[\'"]og:title[\'"][^>]*content=[\'"]([^\'"]+)[\'"][^>]*>/i', $body, $matches)) {
                $extracted_content .= html_entity_decode($matches[1]) . " \n";
            }
            if(empty(trim($extracted_content))) {
                // Thử bóc text thô
                $body_no_script = preg_replace('#<script(.*?)>(.*?)</script>#is', '', $body);
                $body_no_style = preg_replace('#<style(.*?)>(.*?)</style>#is', '', $body_no_script);
                $extracted_content .= wp_trim_words(wp_strip_all_tags($body_no_style), 1000);
            }
            $source_text = "Nội dung trích xuất từ link ($url):\n" . $extracted_content;
        }
    }

    $system_prompt = "Bạn là THE ANALYST - Chuyên gia bóc tách kịch bản truyện mạng.
Nhiệm vụ: Phân tích đoạn text nguồn của user (có thể là tóm tắt, trích đoạn truyện, có dính cả bình luận của người lạ) và trích xuất ra các yếu tố CỐT LÕI để viết lại (remake) thành truyện.
Trả về ĐÚNG MỘT đoạn JSON duy nhất, không có markdown block (không có ```json), với cấu trúc sau:
{
  \"genre\": \"[Chọn đúng 1 trong các thể loại: Drama, Trọng sinh, Tổng tài, Xuyên không, Tu tiên, Ngôn tình đô thị, Kinh dị Việt Nam, Sảng Văn, Vả Mặt, Giả Heo Ăn Thịt Hổ, Đô Thị Ẩn Thân]\",
  \"tone\": \"[Chọn đúng 1: Lãng mạn, Kịch tính, Hài hước, U tối]\",
  \"keywords\": \"[Tóm tắt siêu ngắn gọn cốt truyện chính, mâu thuẫn, hook]\",
  \"extracted_comments\": \"[NẾU TRONG TEXT CÓ CHỨA BÌNH LUẬN XÔN XAO CỦA CƯ DÂN MẠNG BÊN DƯỚI BÀI ĐĂNG GỐC, HÃY CÚP NHẶT VÀ GIỮ NGUYÊN VĂN 3-5 BÌNH LUẬN HAY NHẤT THEO ĐỊNH DẠNG 'Tên|Nội dung bình luận'. Cách nhau bởi dấu xuống dòng (\\n). NẾU KHÔNG CÓ BÌNH LUẬN NÀO THÌ TRẢ VỀ RỖNG.]\"
}";
    
    $user_prompt = "Đọc và bóc tách đoạn text sau:\n" . $source_text;

    $response = temply_call_ai($system_prompt, $user_prompt, 0.7);
    if(is_wp_error($response)) wp_send_json_error(['message' => 'Lỗi kết nối AI: ' . $response->get_error_message()]);
    
    $clean_json = preg_replace('/```json|```/', '', $response);
    $data = json_decode(trim($clean_json), true);
    
    if(!$data || !isset($data['genre'])) {
        wp_send_json_error(['message' => 'Lỗi Parse JSON Phân Tích.', 'raw' => $response]);
    }

    wp_send_json_success(['result' => $data]);
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
    $world_building = sanitize_textarea_field(wp_unslash($_POST['world_building'] ?? ''));

    $system_prompt = "Bạn là THE ORACLE - Chuyên gia thiết lập thế giới quan (World-building) cho tiểu thuyết mạng. Hãy phản hồi thật súc tích, ngắn gọn.";
    if(!empty($world_building)) {
        $system_prompt .= "\n\n*** BỐI CẢNH / QUY TẮC THẾ GIỚI BẮT BUỘC PHẢI TUÂN THỦ (KHÔNG ĐƯỢC LÀM TRÁI) ***\n" . $world_building;
    }
    if($genre == "Drama") $system_prompt .= "\nTập trung vào mâu thuẫn gia đình gay gắt, ngoại tình, trà xanh, tiểu tam, mẹ chồng nàng dâu, vả mặt lật kèo, sự ức chế và giải tỏa tột độ mang đậm chất cẩu huyết đời thường.";
    if($genre == "Tổng tài") $system_prompt .= "\nTập trung vào sự giàu sang tột đỉnh, bá đạo, các tập đoàn đa quốc gia và những mâu thuẫn giai cấp tinh tế nhưng tàn nhẫn.";
    if($genre == "Trọng sinh") $system_prompt .= "\nTập trung vào sự hối tiếc ở kiếp trước, sự phản bội, và hành trình trả thù máu lạnh, sửa chữa sai lầm ở kiếp này.";
    if($genre == "Xuyên không") $system_prompt .= "\nTập trung vào sự khác biệt văn hóa, lợi thế từ kỹ năng/kiến thức tương lai áp dụng vào thế giới cũ.";
    if($genre == "Tu tiên") $system_prompt .= "\nTập trung vào luật rừng, thực lực vi tôn, pháp bảo, kỳ ngộ, hệ thống phân cấp tu vi rõ ràng.";
    if($genre == "Sảng Văn") $system_prompt .= "\nTập trung vào nhịp truyện siêu tốc độ cao, nhân vật chính cực kỳ giỏi hoặc có tài sản khủng nhưng bị khinh thường, để rồi lật tẩy thân phận và đáp trả một cách bùng nổ, gieo sự dồn dập thỏa mãn tối đa cho người đọc.";
    if($genre == "Vả Mặt") $system_prompt .= "\nTập trung vào cốt truyện giấu diếm thân phận (ví dụ Chủ Tịch giả nghèo). Rất nhiều nhân vật phụ nông cạn khinh thường nhân vật chính, sau đó thân phận thật bị lộ tẩy khiến kẻ thù quỳ gối hối hận tột cùng, tạo hiệu ứng Cực Kỳ Tức Giận rồi Cực Kỳ Thỏa Mãn.";
    if($genre == "Giả Heo Ăn Thịt Hổ") $system_prompt .= "\nTập trung vào việc nhân vật chính cố tình tỏ ra ngốc nghếch, yếu kém, cam chịu để che giấu mưu đồ thực sự và đánh lừa cả kẻ địch lẫn người quen cường hào, sau đó chốt hạ và tiêu diệt kẻ địch một cách bất ngờ, lạnh lùng.";
    if($genre == "Đô Thị Ẩn Thân") $system_prompt .= "\nTập trung bối cảnh thành phố hiện đại siêu sang. Nhân vật chính là truyền nhân gia tộc hàng đầu hoặc thế lực siêu cường (Hào Môn Thế Gia) nhưng chọn cách sống tự lập, bình dị. Nhạc điệu truyện xoay quanh việc ứng phó với tầng lớp tinh hoa, mâu thuẫn xã hội.";

    $user_prompt = "Hãy thiết lập bối cảnh thế giới độc đáo cho một câu chuyện thuộc thể loại $genre, với văn phong $tone. Các yếu tố bắt buộc: $keywords.\nTrình bày dưới dạng các gạch đầu dòng rõ ràng về Bối cảnh chung, Quy luật cốt lõi, và Xung đột chính.";

    $response = temply_call_ai_quality($system_prompt, $user_prompt, 0.9);
    if(is_wp_error($response)) wp_send_json_error(['message' => 'Lỗi kết nối AI: ' . $response->get_error_message()]);
    
    if(is_wp_error($response)) {
        wp_send_json_error(['message' => $response->get_error_message()]);
    }
    wp_send_json_success(['result' => $response]);
}

/**
 * STEP 2: The Puppet Master - Characters
 * Trả về JSON 2 lớp:
 *   - character_bible_json: object key-value TÊN CỐ ĐỊNH để Ghostwriter lock cứng
 *   - character_full_text: văn xuôi miêu tả đầy đủ để làm context phong phú
 */
add_action('wp_ajax_temply_step_puppet', 'temply_ajax_puppet');
function temply_ajax_puppet() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $world    = sanitize_textarea_field($_POST['world']    ?? '');
    $keywords = sanitize_textarea_field($_POST['keywords'] ?? '');

    // --- BƯỚC 2a: Sinh hồ sơ nhân vật có cấu trúc JSON ---
    $system_json = "Bạn là THE PUPPET MASTER. Nhiệm vụ: Thiết kế bộ nhân vật CỐT LÕI cho truyện web Việt Nam.

QUY TẮC BẮT BUỘC:
- TÊN: Thuần Việt hoặc Hán Việt đậm chất Châu Á. NGHIÊM CẤM tên Tiếng Anh/Phương Tây.
- HỌ: Thành viên cùng gia tộc PHẢI cùng họ.
- TÊN TẬP ĐOÀN: Chọn 1 tên duy nhất, nhất quán xuyên suốt. KHÔNG phải tên nước ngoài.
- Phản diện hoặc tình địch phải có động cơ thực tế, không ác một màu.

TRẢ VỀ ĐÚNG JSON SAU (không có markdown block, không có text thừa):
{
  \"protagonist_name\": \"Họ và Tên đầy đủ của Nam/Nữ Chính (VD: Lâm Tuấn Kiệt)\",
  \"antagonist_name\": \"Họ và Tên đầy đủ của Phản Diện Chính (VD: Khải Minh)\",
  \"love_interest_name\": \"Họ và Tên đầy đủ của Nhân Vật Tình Yêu/Ex (VD: Hạ Vy) hoặc để trống nếu không có\",
  \"support_name\": \"Họ và Tên của Nhân Vật Phụ Hỗ Trợ (VD: Đỗ Quân - trợ lý) hoặc để trống\",
  \"company_name\": \"Tên TẬP ĐOÀN/CÔNG TY của Nhân Vật Chính (VD: V-Tech, Thiên Anh Corp...) - 1 tên DUY NHẤT\",
  \"rival_company\": \"Tên tập đoàn đối thủ nếu có, để trống nếu không\",
  \"character_profiles\": \"Mô tả đầy đủ TẤT CẢ nhân vật: ngoại hình, tính cách, tổn thương, động cơ. Viết văn xuôi, tối thiểu 200 chữ.\"
}";

    $user_json = "[BỐI CẢNH THẾ GIỚI]\n$world\n\n[CỐT TRUYỆN YÊU CẦU]\n$keywords\n\nHãy thiết kế bộ nhân vật và trả về JSON ngay.";

    $response = temply_call_ai($system_json, $user_json, 0.75);
    if (is_wp_error($response)) wp_send_json_error(['message' => 'Lỗi AI Puppet Master: ' . $response->get_error_message()]);

    // Parse JSON
    $clean = trim(preg_replace('/```(?:json)?|```/', '', $response));
    $parsed = json_decode($clean, true);

    if (!$parsed || !isset($parsed['protagonist_name'])) {
        // Fallback: trả về text thô nếu parse lỗi
        wp_send_json_success([
            'result'               => $response,
            'character_bible_json' => null,
        ]);
        return;
    }

    // Tách character_profiles ra thành full_text, giữ JSON key-value sạch
    $bible_json = [
        'protagonist_name'  => sanitize_text_field($parsed['protagonist_name']  ?? ''),
        'antagonist_name'   => sanitize_text_field($parsed['antagonist_name']   ?? ''),
        'love_interest_name'=> sanitize_text_field($parsed['love_interest_name']?? ''),
        'support_name'      => sanitize_text_field($parsed['support_name']       ?? ''),
        'company_name'      => sanitize_text_field($parsed['company_name']       ?? ''),
        'rival_company'     => sanitize_text_field($parsed['rival_company']      ?? ''),
    ];
    $full_text = sanitize_textarea_field($parsed['character_profiles'] ?? $response);

    wp_send_json_success([
        'result'               => $full_text,          // Text mô tả đầy đủ (dùng trên UI)
        'character_bible_json' => $bible_json,          // JSON tên khoá cứng
    ]);
}

/**
 * STEP 3: The Architect - Outline
 */
add_action('wp_ajax_temply_step_architect', 'temply_ajax_architect');
function temply_ajax_architect() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $world = sanitize_textarea_field($_POST['world'] ?? '');
    $characters = sanitize_textarea_field($_POST['characters'] ?? '');
    $keywords = sanitize_textarea_field($_POST['keywords'] ?? '');

    $num_chapters_raw = strtolower(sanitize_text_field($_POST['num_chapters'] ?? 'auto'));
    $is_auto = ($num_chapters_raw === 'auto' || empty($num_chapters_raw) || intval($num_chapters_raw) == 0);

    $system_prompt = "Bạn là THE ARCHITECT - Chuyên gia dựng kịch bản tài ba bậc nhất mạng lưới. TỐI THƯỢNG: TRONG MỖI CHƯƠNG, BẮT BUỘC PHẢI THIẾT KẾ RÕ 1 NÚT THẮT THEO LUẬT KILLER HOOK Ở CUỐI CHƯƠNG: Một tình huống sinh tử, một lời lật lọng, hoặc một bí mật vừa hé nửa chừng (Cliffhanger) để bắt buộc độc giả phải ấn đọc tiếp lập tức. Đặt một tiêu đề thật giật gân, khơi gợi tò tự cho mỗi chương.";
    
    $user_prompt = "Dựa vào Thế giới:\n$world\n\nVà Nhân vật:\n$characters\n\nVÀ YÊU CẦU CỐT TRUYỆN MONG MUỐN BẮT BUỘC ĐƯA VÀO Outline:\n$keywords\n\n";
    $user_prompt .= "❌ QUY TẮC ĐẶT TÊN CHƯƠNG TỐI THƯỢNG:\n- Tuyệt đối KHÔNG lặp lại các từ vựng nghèo nàn sáo rỗng như: 'Hành trình', 'Hồi sinh', 'Bí mật', 'Sự thật', 'Khám phá', 'Quá khứ', 'Bóng ma'.\n- Tên chương phải dùng từ vựng phong phú, sắc sảo, gợi sự tò mò. KHÔNG ĐƯỢC phép có 2 chương nào trùng lặp quá 2 từ khóa chính với nhau.\n\n";

    if ($is_auto) {
        $user_prompt .= "Hãy phân tích độ phức tạp của cốt truyện và TỰ ĐỘNG QUYẾT ĐỊNH số lượng chương phù hợp nhất để kể vẹn toàn câu chuyện này (Từ 3 đến tối đa 15 chương, chia đều cao trào, không lê thê). BẠN BẮT BUỘC TRẢ VỀ CHÍNH XÁC ĐỊNH DẠNG JSON MẢNG CHỨA: Object cấu trúc { \"synopsis\": \"Tóm tắt/Văn án cực kỳ giật gân, khơi gợi tò mò tột độ (Dưới 100 chữ)\", \"script\": [ Các chương... ] }.\nVí dụ cấu trúc:\n{\n  \"synopsis\": \"...\",\n  \"script\": [\n    { \"chap_num\": 1, \"title\": \"Tên chương dựa theo cốt truyện...\", \"summary\": \"Nội dung...\" },\n    { \"chap_num\": 2, \"title\": \"Tên chương tiếp...\", \"summary\": \"Nội dung...\" }\n  ]\n}";
    } else {
        $num_chapters = intval($num_chapters_raw);
        if($num_chapters < 1) $num_chapters = 1;
        if($num_chapters > 50) $num_chapters = 50;
        
        $user_prompt .= "Hãy lập dàn ý chi tiết cho exactly $num_chapters chương. BẠN BẮT BUỘC TRẢ VỀ CHÍNH XÁC ĐỊNH DẠNG JSON MẢNG CHỨA: Object cấu trúc { \"synopsis\": \"Tóm tắt/Văn án cực kỳ giật gân, khơi gợi tò mò tột độ (Dưới 100 chữ)\", \"script\": [ Các chương... ] }.\nVí dụ cấu trúc:\n{\n  \"synopsis\": \"...\",\n  \"script\": [\n    { \"chap_num\": 1, \"title\": \"Tên chương...\", \"summary\": \"Nội dung...\" },\n    { \"chap_num\": $num_chapters, \"title\": \"Tên chương cuối...\", \"summary\": \"Nội dung...\" }\n  ]\n}";
    }

    $response = temply_call_ai($system_prompt, $user_prompt, 0.8);
    if(is_wp_error($response)) wp_send_json_error(['message' => 'Lỗi kết nối AI: ' . $response->get_error_message()]);
    
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
    $tone = sanitize_text_field($_POST['tone'] ?? '');
    $art = sanitize_text_field($_POST['art'] ?? '');
    $keywords = sanitize_textarea_field($_POST['keywords'] ?? '');

    // Map art style label → Pollinations quality style keywords
    $art_style_map = [
        'Manga Đen trắng Nhật Bản' => 'manga black and white, monochrome, japanese manga style, ink drawing, no color',
        'Manhwa màu Hàn Quốc'      => 'manhwa full color, korean webtoon style, vibrant colors, detailed digital art',
        'Manhua màu Trung Quốc'    => 'manhua full color, chinese comic style, vivid colors, wuxia art style',
        'Anime Style'              => 'anime art style, cel shading, vibrant colors, detailed anime illustration',
        'Realistic'                => 'realistic digital painting, photorealistic, cinematic lighting, highly detailed',
    ];
    $style_suffix = $art_style_map[$art] ?? 'high quality manga illustration, detailed';

    
    $system_prompt = "Bạn là The Publisher. Dựa vào Bối Cảnh, Nhân Vật và Ý Tưởng, sinh ra đúng 1 chuỗi JSON chứa Tựa Đề Truyện (vô cùng hấp dẫn, bắt mắt kiểu web novel) và Tiếng Anh Prompt để tạo ảnh bìa. KHÔNG TEXT THỪA.";
    $user_prompt = "[World]\n$world\n\n[Char]\n$characters\n\n[Hook/Ý tưởng]\n$keywords\n\nTrả về JSON:
    {
      \"title\": \"Tên truyện giật gân thuần Việt hoặc Hán Việt, ví dụ: Sự Thật Phía Sau, Thiên Tôn... Hành văn chuẩn Á Đông.\",
      \"desc\": \"VIẾT TÓM TẮT TRUYỆN (Phần Giới Thiệu) SIÊU SÚC TÍCH, CHUẨN UX CHO ĐIỆN THOẠI (Áp dụng 'Công thức 3 lớp'):\n- Lớp 1 (Đoạn 1): Cú Hook 'Chạm Đáy Ức Chế'. Mở đầu bằng 1 câu thoại gây sốc hoặc tóm tắt trực diện vào mâu thuẫn khốc liệt nhất để giữ chân người đọc trong 3 giây đầu.\n- Lớp 2: Dàn ý cốt lõi. Trình bày bằng danh sách gạch đầu dòng (bullet points) tóm tắt nhanh gọn về: Nhân vật chính, Phản diện, Kịch tính cốt lõi.\n- Lớp 3 (Đoạn cuối): Câu hỏi mở (Cliffhanger) kịch tính để kích thích người xem bấm Đọc Tiếp.\nSử dụng HTML <p>, <ul>, <li>, <strong> để trình bày rõ ràng, dễ đọc. Văn phong sắc bén, giật gân nhưng NGẮN GỌN, KHÔNG DÀI DÒNG.\",
      \"seo_desc\": \"1 câu Meta Description chuẩn SEO (chính xác 140 - 150 ký tự). BẮT BUỘC chứa tên truyện. Văn phong giật gân, tò mò và phải có Call-to-action (Ví dụ: Click đọc ngay cái kết tởm lợm...) để tăng tối đa tỷ lệ Click (CTR).\",
      \"cover_prompt\": \"1 câu tiếng anh mô tả ngắn gọn cảnh tựng hoặc nhân vật anime/fantasy để vẽ ảnh bìa. Ghi nhớ bằng tiếng Anh. Ví dụ: A handsome CEO in a dark suit standing...\"
    }";

    $response = temply_call_ai_quality($system_prompt, $user_prompt, 0.9);
    if(is_wp_error($response)) wp_send_json_error(['message' => 'Lỗi kết nối AI: ' . $response->get_error_message()]);
    $clean_json = preg_replace('/```json|```/', '', $response);
    $data = json_decode(trim($clean_json), true);

    if(!$data || !isset($data['title'])) wp_send_json_error(['message' => 'Lỗi Parse Tên truyện']);

    // Chuẩn bị biến SEO Keyword trước để chèn vào nội dung
    $seo_keyword = sprintf('Truyện %s', sanitize_text_field($data['title']));
    $seo_title = sprintf('Đọc Ngay Truyện %s (Mới Nhất) - Cực Cuốn', sanitize_text_field($data['title']));

    // Tối ưu hóa Nội dung để pass 100/100 RankMath (Chèn Keyword vào H2, dòng đầu và Internal Link)
    $optimized_content = '<h2 style="display:none;">Giới thiệu ' . $seo_keyword . '</h2>';
    $optimized_content .= '<p style="display:none;">Chào mừng bạn đến với góc đọc <strong>' . $seo_keyword . '</strong>.</p>';
    $optimized_content .= wp_kses_post($data['desc']);
    $optimized_content .= '<p style="margin-top:20px; font-style:italic;">Mời bạn khám phá thêm các bộ <a href="' . home_url() . '" title="Truyện hay">truyện hay</a> khác tại Hệ thống.</p>';

    // 1. Tạo post_type=truyen
    $post_id = wp_insert_post([
        'post_title'   => sanitize_text_field($data['title']),
        'post_content' => $optimized_content, // Dùng nội dung đã nhúng SEO tàng hình
        'post_status'  => 'publish',
        'post_type'    => 'truyen',
        'post_author'  => get_current_user_id()
    ]);
    
    if(is_wp_error($post_id)) {
        wp_send_json_error(['message' => 'Không thể tạo bài Đăng.']);
    }

    // Thêm lưu Dấu Ấn Prompt (Blueprint) để Reference sau này
    update_post_meta($post_id, '_temply_blueprint_world', $world);
    update_post_meta($post_id, '_temply_blueprint_characters', $characters);
    update_post_meta($post_id, '_temply_blueprint_genre', $genre);
    update_post_meta($post_id, '_temply_blueprint_tone', $tone);
    update_post_meta($post_id, '_temply_blueprint_keywords', $keywords);
    update_post_meta($post_id, '_temply_blueprint_art', $art);

    // Rank Math
    update_post_meta($post_id, 'rank_math_title', $seo_title);
    update_post_meta($post_id, 'rank_math_focus_keyword', $seo_keyword);
    
    // Yoast SEO
    update_post_meta($post_id, '_yoast_wpseo_title', $seo_title);
    update_post_meta($post_id, '_yoast_wpseo_focuskw', $seo_keyword);

    if(!empty($data['seo_desc'])) {
        $seo_text = sanitize_text_field($data['seo_desc']);
        if (stripos($seo_text, $seo_keyword) === false) {
            $seo_text = 'Đọc ' . $seo_keyword . ': ' . $seo_text;
            if (mb_strlen($seo_text, 'UTF-8') > 160) {
                $seo_text = mb_substr($seo_text, 0, 157, 'UTF-8') . '...';
            }
        }
        update_post_meta($post_id, '_yoast_wpseo_metadesc', $seo_text);
        update_post_meta($post_id, 'rank_math_description', $seo_text);
    }
    
    // Bật Schema Article cho Rank Math
    update_post_meta($post_id, 'rank_math_rich_snippet', 'article');
    $schema_data = array(
        '@type' => 'Article',
        'headline' => $seo_title,
        'description' => isset($seo_text) ? $seo_text : ''
    );
    update_post_meta($post_id, 'rank_math_schema_Article', $schema_data);
    // Lưu Context AI để dùng cho tính năng Đẻ chương mới
    update_post_meta($post_id, '_temply_ai_world', $world);
    update_post_meta($post_id, '_temply_ai_characters', $characters);
    update_post_meta($post_id, '_temply_ai_genre', $genre);
    update_post_meta($post_id, '_temply_ai_keywords', $keywords);

    // ── Lưu Character Bible JSON (khoá cứng tên nhân vật) ──
    $bible_json_raw = sanitize_textarea_field(wp_unslash($_POST['character_bible_json'] ?? ''));
    if (!empty($bible_json_raw)) {
        $bible_decoded = json_decode($bible_json_raw, true);
        if ($bible_decoded) {
            update_post_meta($post_id, '_temply_character_bible_json', $bible_decoded);
        }
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

    // 3. Cover Image — Dùng cùng art style với nội dung truyện
    $cover_full_prompt = $data['cover_prompt'] . ', ' . $style_suffix . ', masterpiece, best quality, highly detailed cover art';
    $escaped_prompt = rawurlencode($cover_full_prompt);
    $image_url = "https://image.pollinations.ai/prompt/" . $escaped_prompt . "?width=600&height=900&nologo=true";
    
    $thumb_id = temply_upload_external_image($image_url, $post_id, $seo_keyword);
    
    wp_send_json_success([
        'truyen_id' => $post_id,
        'title' => $data['title'],
        'thumb' => $thumb_id ? 'Đã cài Cover Ảnh AI' : 'Lỗi cài Cover'
    ]);
}

/**
 * ============================================================
 * HELPER: Xây dựng CHARACTER BIBLE nhúng vào system prompt
 * Ưu tiên dùng JSON khoá cứng từ Puppet Master nếu có.
 * ============================================================
 */
function temply_extract_character_bible($characters_text, $world_text, $bible_json = null) {
    // ── Nếu có JSON khoá cứng từ Puppet Master ──

    if (!empty($bible_json) && is_array($bible_json)) {
        $pname  = $bible_json['protagonist_name']   ?? '';
        $aname  = $bible_json['antagonist_name']    ?? '';
        $lname  = $bible_json['love_interest_name'] ?? '';
        $sname  = $bible_json['support_name']       ?? '';
        $cname  = $bible_json['company_name']       ?? '';
        $rname  = $bible_json['rival_company']      ?? '';

        $locked_names = "\n\n╔" . str_repeat("═", 50) . "╗\n";
        $locked_names .= "║   CHARACTER BIBLE - BẢNG TÊN KHOÁ CỨNG (BUỘC PHẢI TUÂN THỦ)   ║\n";
        $locked_names .= "╚" . str_repeat("═", 50) . "╝\n";
        $locked_names .= "❌ LUẬT TỐI THƯỢNG - QUAN TRỌNG HƠN MỌI THỨ KHÁC:\n\n";
        $locked_names .= "► TÊN NHÂN VẬT CHÍNH THỨC (NGHIÊM CẤM ĐỔI TÊN):\n";
        if ($pname) $locked_names .= "- NAM/NỮ CHÍNH: {$pname}\n";
        if ($aname) $locked_names .= "- PHẢN DIỆN CHÍNH: {$aname}\n";
        if ($lname) $locked_names .= "- TÌNH YÊU / EX: {$lname}\n";
        if ($sname) $locked_names .= "- TRỢ LÝ / NHÂN VẬT PHỤ: {$sname}\n";
        if ($cname) $locked_names .= "\n► TẬP ĐOÀN CHÍNH THỨC (KHÔNG ĐỔI TÊN): {$cname}\n";
        if ($rname) $locked_names .= "► TẬP ĐOÀN ĐỐI THỦ: {$rname}\n";
        $locked_names .= "\n❌ NGHIÊM CẤM TUYỆT ĐỐI:\n";
        $locked_names .= "  - Dùng bất kỳ tên nào khác ngoài danh sách trên\n";
        $locked_names .= "  - Dùng tên Tiếng Anh/nước ngoài cho nhân vật Việt/Á Đông\n";
        $locked_names .= "  - Tạo cảnh 'CEO ngoại quốc cúi đầu 50 triệu USD' nếu dàn ý không yêu cầu\n";
        $locked_names .= "  - Đổi tên tập đoàn giữa các chương\n";
        $locked_names .= "\n[HỒ SƠ NHÂN VẬT ĐẦY ĐỦ]\n{$characters_text}\n";
        return $locked_names;
    }

    // ── Fallback (chưa có JSON) ──
    $company_lock = '';
    if (!empty($world_text)) {
        $company_lock = "\n[TÊN CÔNG TY/TẬP ĐOÀN CHÍNH THỨC - BẤT BIẾN]\nLấy từ bối cảnh thế giới đã được xây dựng ở trên. TUYỆT ĐỐI không tự ý thêm tên công ty/tổ chức mới nào.";
    }
    $out  = "\n\n╔" . str_repeat("═", 38) . "╗\n";
    $out .= "║   CHARACTER BIBLE - DANH SÁCH TÊN BẤT BIẾN   ║\n";
    $out .= "╚" . str_repeat("═", 38) . "╝\n";
    $out .= "✅ CHỈ ĐƯỢC PHÉP dùng đúng tên/họ nhân vật trong danh sách này.\n";
    $out .= "❌ NGHIÊM CẤM: đổi tên, dùng tên nước ngoài, đổi tên tập đoàn giữa chương.\n";
    $out .= "$company_lock\n[HỒ SƠ NHÂN VẬT ĐẦY ĐỦ]\n$characters_text\n";
    return $out;
}


/**
 * STEP 5: The Ghostwriter - Viết các Chương nội dung
 */
add_action('wp_ajax_temply_step_write_chapter', 'temply_ajax_write_chapter');
function temply_ajax_write_chapter() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    // Chống timeout 502
    set_time_limit(600);
    ignore_user_abort(true);

    $truyen_id = intval($_POST['truyen_id'] ?? 0);
    $chap_num = intval($_POST['chap_num'] ?? 1);
    $summary = sanitize_textarea_field($_POST['summary'] ?? '');
    $genre = sanitize_text_field($_POST['genre'] ?? '');
    $tone = sanitize_text_field($_POST['tone'] ?? '');
    $keywords = sanitize_textarea_field($_POST['keywords'] ?? '');
    $world = sanitize_textarea_field($_POST['world'] ?? '');
    $characters = sanitize_textarea_field($_POST['characters'] ?? '');
    $is_final = intval($_POST['is_final_chapter'] ?? 0);
    $custom_comments = sanitize_textarea_field($_POST['custom_comments'] ?? '');

    if(!$truyen_id) wp_send_json_error(['message' => 'Mất ID Truyện.']);

    // ── BUILD CHARACTER BIBLE: Ưu tiên JSON khoá cứng từ DB ──
    $bible_json = get_post_meta($truyen_id, '_temply_character_bible_json', true);
    if (!is_array($bible_json)) $bible_json = null;
    $character_bible = temply_extract_character_bible($characters, $world, $bible_json);


    // Thiết lập luật định dạng Comments
    if (!empty($custom_comments)) {
        $comment_rules = "SỬ DỤNG CHÍNH XÁC Y XÌ ĐÚC Danh sách Comment sau, KHÔNG ĐƯỢC THÊM BỚT HAY CHẾ CHÁO GÌ THÊM:\n" . $custom_comments;
    } else {
        $comment_rules = "Luật Bình Luận: KHÔNG ĐƯỢC màu mè sến súa. AI phải nhập vai Hội bà tám mạng xã hội, mẹ bỉm sữa hoặc thanh niên Gen Z. Dùng văn phong chửi đổng, viết tắt (vcl, đm, má ơi, khứa, trời ơi, đọc mà tức), bực dọc vì nhân vật ác, hoặc hóng chờ bẻ lái. Ví dụ: 'Má nó đọc đoạn con tiểu tam mà sôi máu, nam chính bị mù hả?'.\nNamdeptrai|Má nó con tiểu tam trơ trẽn vđ, nam chính bị mù hả trời?\nHoinangdau|Tr ơi đọc mà nước mắt lưng tròng, thương nữ chính quá.\nBinhlunx|Khứa tác giả bẻ lái khét lẹt... hóng chương sau!";
    }


    // ── ANTI-REPETITION: Lấy lịch sử cảnh đã viết ──
    $previous_summaries = get_post_meta($truyen_id, '_temply_written_chapter_summaries', true);
    if (!is_array($previous_summaries)) $previous_summaries = [];
    
    // Lấy riêng danh sách "cấu trúc kịch tính" đã dùng (lưu suốt truyện)
    $used_plot_structures = get_post_meta($truyen_id, '_temply_used_plot_structures', true);
    if (!is_array($used_plot_structures)) $used_plot_structures = [];

    $anti_repeat_block = '';
    // Block 1: Tóm tắt đại cương để AI hiểu tiến trình truyện (Tránh lặp vô thức)
    if (!empty($previous_summaries)) {
        $anti_repeat_block .= "\n\n[TÓM TẮT DIỄN BIẾN CÁC CHƯƠNG ĐÃ QUA - TUYỆT ĐỐI KHÔNG TÁI DIỄN LẠI TÌNH TIẾT ĐÃ CÓ]:\n";
        foreach ($previous_summaries as $prev) {
            $anti_repeat_block .= "- " . $prev . "\n";
        }
    }
    
    // Block 2: Cấu trúc kịch tính đã dùng (cấm suốt cả truyện)
    if (!empty($used_plot_structures)) {
        $anti_repeat_block .= "\n\n[CẤU TRÚC KỊCH TÍNH ĐÃ KHAI THÁC - TỨYT ĐỐI KHÔNG TÁI SọNG DỤNG ĐUỦI BẤT KỲ HÌNH THỨC NÀO]\n";
        foreach ($used_plot_structures as $idx => $ps) {
            $anti_repeat_block .= ($idx + 1) . ". " . $ps . "\n";
        }
        $anti_repeat_block .= "\n➤ BẮt buộc tạo cắt KHAI THÁC MỚI HOÀN TOÀN \u2014 dùng sự kiện khác, yếu tố bất ngờ khác, cách phùng phất khác.\n";
    }
    
    // Block 3: Cấm cứng cấu trúc lặp phiếu nhất
    $hard_forbidden = [
        "ceo / lãnh đạo nước ngoài bước vào tiệc, cúi đầu trước nam chính, công bố hợp đồng 50 triệu usd",
        "phản diện bị sa thải ngay tại chỗ trước mặt đám đông",
        "nam chính ngồi vẽ sticker ở góc khuất, bị chế giễu, sau đó lất kèo bằng cách tiết lộ danh tính",
    ];
    
    // Chỉ thêm forbidden nếu đã xuất hiện trong used_plot_structures
    $active_forbidden = array_intersect($hard_forbidden, $used_plot_structures);
    if (!empty($active_forbidden)) {
        $anti_repeat_block .= "\n[CẤM TỨYT ĐỐI - ĐÃ KHAI THÁC OUỞ ỚT]\n";
        foreach ($active_forbidden as $f) {
            $anti_repeat_block .= "\u274c " . $f . "\n";
        }
        $anti_repeat_block .= "\u27a4 Thay vào đó: Dùng các cách lật kèo KHÁC: tiết lộ qua phương tiện truyền thông, qua cuộc gọi bộc phát, qua tài liệu bí mật lộ ra, qua đối thủ đỏnh chính, qua cách xử lý khủng hoảng của công ty...\n";
    }


    $system_prompt = "Bạn là THE GHOSTWRITER. Bậc thầy văn học mạng, có khả năng viết cực kỳ lôi cuốn, mượt mà và tôn trọng sát thể loại được yêu cầu. HÃY MÔ TẢ ĐỦ ĐẦY, CẢ VỀ KHÔNG GIAN LẪN NỘI TÂM. Viết thật dài (tối thiểu 800 chữ).
    Mục tiêu 1: MỞ ĐẦU CHƯƠNG BẰNG 1 CÂU HOOK GÂY TÒ MÒ ĐỂ LÔI KÉO ĐỘC GIẢ.
    Mục tiêu 2: TUYỆT ĐỐI TUÂN THỦ DANH SÁCH TÊN NHÂN VẬT TRONG CHARACTER BIBLE VÀ KẾT THÚC BẰNG MỘT CÚ TWIST/CLIFFHANGER ĐỂ LƯU GIỮ SỰ TÒ MÒ.
    LUẬT VĂN HOÁ: BẮT BUỘC đặt bối cảnh Việt Nam hoặc Á Đông. Lời thoại, cách hành xử thuần Việt 100%. NGUYÊM CẤM dùng từ tiếng Anh (như hello, murmured...).
    LUẬT ĐỊNH DẠNG PHẢN HỒI:
    - Dòng 1: TITLE: [Tên chương ấn tượng không có số chương]
    - Dòng 2 trở đi: Toàn bộ nội dung HTML (<p>, <strong>, <em>). Không cần JSON. Không markdown code block.
    - SUY NGHĨ NHƯ MỘT HỌA SĨ: BẮT BUỘC chèn ĐÚNG 1 ĐẾN 2 BỨC ẢNH minh họa nằm rải rác ở những phân đoạn đắt giá (Cao trào, mô tả nhân vật, bối cảnh ngộp thở). Cú pháp bắt buộc ĐỂ CHÈN ẢNH: [IMAGE: Mô_tả_chi_tiết_cảnh_vật_hoặc_nhân_vật_bằng_Tiếng_Anh]. Ví dụ: [IMAGE: A highly detailed illustration of a handsome CEO crying in the rain, cinematic lighting, masterpiece] (phải tự đứng trên 1 dòng riêng biệt).
    - Cuối cùng là khối sau:
---COMMENTS---
$comment_rules
$character_bible$anti_repeat_block";

    if (stripos($genre, 'drama') !== false || stripos($genre, 'cẩu huyết') !== false || stripos($genre, 'vả mặt') !== false) {
        $system_prompt = "VAI TRÒ: Bạn là THE GHOSTWRITER - Đại sư biên kịch chuyên về Webnovel thể loại \"Cẩu Huyết\", \"Gia Đấu\" và \"Đô Thị Vả Mặt\" hàng đầu Việt Nam.

MỤC TIÊU NỘI DUNG:
1. Tập trung vào Xung đột: Mọi đoạn văn phải phục vụ mục tiêu đẩy mâu thuẫn lên đỉnh điểm. Không mô tả thiên nhiên, không tả cảnh lan man.
2. Kỹ thuật 'Vả Mặt Liên Hoàn' (Yo-yo Face-slapping): Khi nhân vật chính tiết lộ thân phận/sức mạnh, KHÔNG cho kẻ ác tin ngay! Lần 1: Kẻ ác tìm được cớ lấp liếm, sỉ nhục thêm. Lần 2: Viện binh của ác nhân tới đông hơn/mạnh hơn. Lần 3-4: Lật kèo liên tục cho đến khi viện binh mạnh nhất của kẻ ác hoảng loạn quỳ lạy nhân vật chính. Đây là nghệ thuật dồn nén ức chế cực đại rồi kết liễu tàn khốc khiến kẻ thù sụp đổ thảm hại não nề.
3. Hành văn Sắc Lạnh: Sử dụng câu văn ngắn, gãy gọn. Viết thật dài, chi tiết (tối thiểu 800 chữ).
4. Chiều sau Tâm lý (Đa chiều): Kẻ ác không được ác một màu vô lý. Phải lồng ghép động cơ thực tế, sự đố kỵ, sự tổn thương hoặc sợ hãi của chúng. Mô tả sự hoảng loạn tột cùng khi chúng từ từ mất đi chỗ dựa.
5. Nghệ thuật Foreshadowing (Gài cắm sức mạnh ngầm): Ngay cả ở những chương đầu khi nhân vật chính đang đóng giả kẻ yếu thế, HÃY GÀI CẮM NHỮNG CHI TIẾT NHỎ THỂ HIỆN QUYỀN NĂNG (Ví dụ: một cái gõ tay làm sập hệ thống, 1 cuộc điện thoại bí ẩn thao túng thị trường, sát khí áp đảo trong nháy mắt khiến kẻ thù rùng mình).

QUY TẮC CẤM (TỐI QUAN TRỌNG): 
- KHÔNG viết lời chào/kết. KHÔNG triết lý sáo rỗng. BẮT BUỘC bối cảnh Việt Nam. TUYỆT ĐỐI KHÔNG dùng từ Tiếng Anh trong nội dung truyện (Trừ cú pháp chèn ảnh).

LUẬT ĐỊNH DẠNG PHẢN HỒI BẮT BUỘC TRẢ VỀ DƯỚI ĐÂY (Không Markdown Code Block):
TITLE: [Tên chương siêu ấn tượng không có số]
<p>Nội dung HTML bọc trong thẻ p</p>
[IMAGE: Bản mô tả cảnh hoặc nhân vật bằng TIẾNG ANH để Máy AI vẽ minh họa]
<p>Tiếp tục nội dung...</p>
---COMMENTS---
$comment_rules

Chú ý: Mục ---COMMENTS--- phải nằm ở DƯỚI CÙNG.
$character_bible$anti_repeat_block";
    }

    if ($is_final == 1) {
        $system_prompt .= "\n\n[CẢNH BÁO TỪ HỆ THỐNG]: ĐÂY LÀ CHƯƠNG CUỐI CÙNG (EPILOGUE - VĨ THANH)!! NGHIÊM CẤM TẠO CLIFFHANGER (Kết thúc lửng). Bạn PHẢI giải quyết dứt điểm mâu thuẫn lớn nhất. ĐẶC BIỆT: Nửa sau của chương BẮT BUỘC phải là phần Vĩ Thanh, mô tả rõ thế giới xung quanh/công ty/gia tộc đã biến chuyển và thay đổi cục diện ra sao sau sự kiện cao trào, hậu quả mà kẻ ác phải gánh chịu trong phần đời còn lại. Chốt lại toàn bộ câu chuyện một cách viên mãn, triệt để và sâu sắc nhất.";
        $ending_phrase = "KẾT THÚC TRỌN VẸN BẰNG MỘT VĨ THANH (EPILOGUE) THỎA MÃN LÂU DÀI.";
    } else {
        $ending_phrase = "KẾT THÚC BẰNG MỘT KILLER HOOK HOẶC CLIFFHANGER GÂY SỐC.";
    }

    $user_prompt = "[CHARACTER BIBLE - BẮT BUỘC XEM TRƯỚC KHI VIẾT]\n(Xem trong System Prompt)\n\n[BỐI CẢNH THẾ GIỚI]\n$world\n\n[Ý TƯỞNG CỐT LÕI (BẮT BUỘC BÁM SÁT)]\n$keywords\n\nVIẾT CHI TIẾT Chương $chap_num dành cho Thể loại $genre, văn phong $tone, dựa theo Dàn Ý sau:\n$summary\n\nSử dụng thẻ HTML (<p>, <strong>, <em>). $ending_phrase Định dạng bắt buộc:\nTITLE: [tên chương]\n[nội dung HTML]";

    $response = temply_call_ai_quality($system_prompt, $user_prompt, 0.9);
    if(is_wp_error($response)) wp_send_json_error(['message' => 'Lỗi kết nối AI: ' . $response->get_error_message()]);

    // Bền vững parse: Hỗ trợ mọi định dạng TITLE: hoặc không có TITLE:
    $chap_title_from_ai = '';
    $chap_content = '';
    $response_trimmed = trim($response);
    
    // Xóa block code markdown nếu có
    $response_trimmed = preg_replace('/```(?:html|json)?/', '', $response_trimmed);
    $response_trimmed = trim(preg_replace('/```/', '', $response_trimmed));

    if(preg_match('/(?:^|\n)\s*(?:\*\*|#)?\s*TITLE\s*:\s*(?:\*\*)?\s*(.*)/i', $response_trimmed, $title_match)) {
        $chap_title_from_ai = trim($title_match[1]);
        $parts = preg_split('/(?:^|\n)\s*(?:\*\*|#)?\s*TITLE\s*:\s*(?:\*\*)?\s*.*\n/i', $response_trimmed, 2);
        $chap_content = trim($parts[1] ?? '');
        if(empty($chap_content)) {
            $chap_content = trim(preg_replace('/(?:^|\n)\s*(?:\*\*|#)?\s*TITLE\s*:\s*(?:\*\*)?\s*.*/i', '', $response_trimmed, 1));
        }
    } else {
        // Kịch bản AI quên viết TITLE:, lấy luôn dòng đầu tiên làm Title
        $lines = explode("\n", $response_trimmed);
        if(count($lines) > 2) {
            $first_line = trim(array_shift($lines));
            $chap_title_from_ai = preg_replace('/^[#\*]+\s*(.*)[#\*]*$/', '$1', $first_line);
            $chap_content = trim(implode("\n", $lines));
        } else {
            // Nếu quá ngắn, có thể là lỗi nhưng vẫn lưu
            $chap_content = $response_trimmed;
        }
    }

    if(empty($chap_content)) wp_send_json_error(['message' => 'Lỗi Parse Nội dung. Hãy thử lại.']);
    
    $chap_title_posted = sanitize_text_field($_POST['chap_title'] ?? '');
    $final_title = !empty($chap_title_posted)
        ? "Chương $chap_num: $chap_title_posted"
        : (!empty($chap_title_from_ai) ? "Chương $chap_num: $chap_title_from_ai" : "Chương $chap_num");

    $post_id = wp_insert_post([
        'post_title'   => $final_title,
        'post_content' => wp_kses_post('Đang phân tích và gieo cấy bình luận...'),
        'post_status'  => 'publish',
        'post_type'    => 'chuong',
        'menu_order'   => $chap_num,
        'post_author'  => get_current_user_id()
    ]);

    if(is_wp_error($post_id)) wp_send_json_error(['message' => 'Lỗi tạo Chương.']);

    // Tách bóc Comment ảo ra và Update Nội dung lõi
    $clean_content = temply_parse_and_insert_ai_comments($post_id, $chap_content);
    
    // Biến thẻ [IMAGE: ...] thành thẻ <img> gọi tới AI Họa Sĩ Pollinations
    $clean_content = preg_replace_callback('/\[IMAGE:\s*(.+?)\]/i', function($m) {
        $prompt = trim($m[1]) . ', masterpiece, best quality, highly detailed cover art';
        $escaped_prompt = rawurlencode($prompt);
        // Tạo ảnh khổ ngang (800x500) phù hợp chèn vào giữa bài viết chữ
        $url = 'https://image.pollinations.ai/prompt/' . $escaped_prompt . '?width=800&height=500&nologo=true';
        return '<figure style="margin: 30px 0; text-align: center;"><img src="' . esc_url($url) . '" alt="' . esc_attr($m[1]) . '" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);" /></figure>';
    }, $clean_content);

    wp_update_post([
        'ID' => $post_id,
        'post_content' => wp_kses_post($clean_content)
    ]);

    update_post_meta($post_id, '_truyen_id', $truyen_id); // Liên kết chương với truyện
    update_post_meta($post_id, '_temply_ai_summary', $summary);

    // ── GHI NHỚ CẢNH ĐÃ DÙNG (Anti-Repeat cho chương tiếp theo) ──
    $existing_summaries = get_post_meta($truyen_id, '_temply_written_chapter_summaries', true);
    if (!is_array($existing_summaries)) $existing_summaries = [];
    $existing_summaries[] = "Chương $chap_num: " . mb_substr(strip_tags($summary), 0, 100, 'UTF-8');
    if (count($existing_summaries) > 15) {
        $existing_summaries = array_slice($existing_summaries, -15);
    }
    update_post_meta($truyen_id, '_temply_written_chapter_summaries', $existing_summaries);

    // ── GHI NHỚ CẤU TRÚC KỊCH TÍNH ĐÃ DÙNG (Lưu suốt cả truyện) ──
    $summary_lower = mb_strtolower(strip_tags($summary), 'UTF-8');
    $patterns_to_check = [
        'ceo / lãnh đạo nước ngoài bước vào tiệc, cúi đầu trước nam chính, công bố hợp đồng 50 triệu usd'
            => ['cúi đầu', 'tiệc', '50 triệu', 'hợp đồng'],
        'phản diện bị sa thải ngay tại chỗ trước mặt đám đông'
            => ['sa thải', 'đám đông', 'buổi tiệc'],
        'nam chính ngồi vẽ sticker ở góc khuất, bị chế giễu, sau đó lất kèo bằng cách tiết lộ danh tính'
            => ['sticker', 'chế giễu', 'góc khuất', 'danh tính'],
    ];
    $used_plot_structures = get_post_meta($truyen_id, '_temply_used_plot_structures', true);
    if (!is_array($used_plot_structures)) $used_plot_structures = [];
    foreach ($patterns_to_check as $label => $keywords) {
        $match_count = 0;
        foreach ($keywords as $kw) {
            if (mb_strpos($summary_lower, $kw) !== false) $match_count++;
        }
        if ($match_count >= 2 && !in_array($label, $used_plot_structures)) {
            $used_plot_structures[] = $label;
        }
    }
    update_post_meta($truyen_id, '_temply_used_plot_structures', $used_plot_structures);



    wp_send_json_success([
        'chuong_id' => $post_id,
        'title' => $final_title
    ]);
}


/**
 * STEP 4b: The Comic Artist - Sinh Băng Truyện Tranh Cực Chí (Webtoon Mode)
 */
add_action('wp_ajax_temply_step_write_comic_chapter', 'temply_ajax_write_comic_chapter');
function temply_ajax_write_comic_chapter() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $truyen_id = intval($_POST['truyen_id'] ?? 0);
    $chap_num = intval($_POST['chap_num'] ?? 1);
    $summary = sanitize_textarea_field($_POST['summary'] ?? '');
    $genre = sanitize_text_field($_POST['genre'] ?? '');
    $art = sanitize_text_field($_POST['art'] ?? '');
    $seed = sanitize_text_field($_POST['seed'] ?? '12345');
    $custom_comments = sanitize_textarea_field($_POST['custom_comments'] ?? '');

    if(!$truyen_id) wp_send_json_error(['message' => 'Mất ID Truyện.']);

    $system_prompt = "Bạn là THE COMIC STORYBOARDER (Đạo diễn Webtoon cực đỉnh). Hãy rã tóm tắt thành ÍT NHẤT 20 ĐẾN 25 Panel (khung hình) liên tục để chương thật dài. Tách nhỏ hành động, biểu cảm, ngoại cảnh. Mỗi panel yêu cầu 1 câu tiếng Anh Prompt tả cảnh chi tiết để vẽ minh họa, và 1 Array các câu thoại Tiếng Việt ngắn gọn, vả mặt cường độ cao.
    CẢNH BÁO TỐI QUAN TRỌNG: Để truyện không bị rối mắt, MỖI PANEL CHỈ ĐƯỢC PHÉP CÓ TỐI ĐA TỪ 0 ĐẾN 2 CÂU THOẠI NGẮN (Độ dài mảng dialogues <= 2). Không nhồi nhét chữ vào ảnh!
    CHỈ TRẢ VỀ JSON MẢNG (ARRAY) CHỨA 20-25 OBJECT. KHÔNG CẦN CHUÔNG HAY BAO BÌ.
    [
      {
         \"prompt\": \"A young man in black suit laughing wickedly, luxury office background...\",
         \"dialogues\": [\"Chủ tịch, tiểu thư đã tới!\", \"Để cô ta đợi ở ngoài!\"]
      }
    ]";

    $user_prompt = "Hãy rã chi tiết Chương $chap_num dành cho Thể loại $genre, nét vẽ $art, dựa theo tóm tắt:\n$summary\n\nBẮT BUỘC TẠO 20 - 25 PANELS JSON. Cắt cảnh thật mượt, hội thoại cực cuốn.";

    $response = temply_call_ai($system_prompt, $user_prompt, 0.8);
    if(is_wp_error($response)) wp_send_json_error(['message' => 'Lỗi kết nối AI: ' . $response->get_error_message()]);
    $clean_json = preg_replace('/```json|```/', '', $response);
    $panels = json_decode(trim($clean_json), true);

    if(!is_array($panels)) wp_send_json_error(['message' => 'Lỗi Parse JSON Webtoon. Hãy thử lại.']);

    $html_content = '<style>
    .comic-container { max-width: 600px; margin: 0 auto; background: #111; padding: 0; }
    .comic-panel { position: relative; width: 100%; border-bottom: 3px solid #0a0a0a; background: #111; overflow: hidden; display: flex; flex-direction: column; }
    .comic-panel img { width: 100%; height: auto; min-height: 400px; display: block; object-fit: cover; }
    .bubbles-layer { position: absolute; inset: 0; padding: 25px 20px; display: flex; flex-direction: column; justify-content: space-evenly; pointer-events: none; z-index: 10; }
    .bubble { background: rgba(255,255,255,0.96); border: 2.5px solid #111; border-radius: 16px; padding: 12px 18px; font-weight: 700; font-size: 16px; color: #111; font-family: Tahoma, sans-serif; max-width: 85%; align-self: flex-start; box-shadow: 4px 4px 0 rgba(0,0,0,0.85); position: relative; line-height: 1.45; pointer-events: auto; }
    .bubble.right { align-self: flex-end; }
    .bubble::after { content: ""; position: absolute; bottom: -10px; left: 24px; border-width: 10px 10px 0; border-style: solid; border-color: #111 transparent transparent transparent; }
    .bubble.right::after { left: auto; right: 24px; }
    @media (max-width: 600px) {
        .comic-container { width: 100%; max-width: 100%; }
        .bubbles-layer { padding: 20px 15px; }
        .bubble { font-size: 15px; padding: 10px 14px; max-width: 90%; border-radius: 14px; border-width: 2px; box-shadow: 3px 3px 0 rgba(0,0,0,0.85); }
        .bubble::after { border-width: 8px 8px 0; bottom: -8px; left: 18px; }
        .bubble.right::after { left: auto; right: 18px; }
    }
    </style>
    <div class="comic-container" id="comic-main-container">';

    $warmup_urls = [];

    // Tải ảnh về Server → lưu WordPress Media (không còn phụ thuộc browser rate-limit)
    set_time_limit(300); // 5 phút - đủ thời gian tải 25 ảnh
    require_once(ABSPATH . 'wp-admin/includes/media.php');
    require_once(ABSPATH . 'wp-admin/includes/file.php');
    require_once(ABSPATH . 'wp-admin/includes/image.php');

    foreach($panels as $idx => $p) {
        $prmpt = $p['prompt'] ?? '';
        if(empty($prmpt)) continue;
        
        // Build style map inside comic handler too
        $art_style_map_c = [
            'Manga Đen trắng Nhật Bản' => 'manga black and white, monochrome, japanese manga style, ink drawing, no color',
            'Manhwa màu Hàn Quốc'      => 'manhwa full color, korean webtoon style, vibrant colors, detailed digital art',
            'Manhua màu Trung Quốc'    => 'manhua full color, chinese comic style, vivid colors, wuxia art style',
            'Anime Style'              => 'anime art style, cel shading, vibrant colors, detailed anime illustration',
            'Realistic'                => 'realistic digital painting, photorealistic, cinematic lighting, highly detailed',
        ];
        $panel_style = $art_style_map_c[$art] ?? $art . ', highly detailed expressive manga illustration masterpiece';
        $full_panel_prompt = $prmpt . ', ' . $panel_style . ', masterpiece';
        $escaped_prompt = rawurlencode($full_panel_prompt);
        $img_url = "https://image.pollinations.ai/prompt/" . $escaped_prompt . "?width=512&height=768&seed=" . $seed . "&nologo=true";
        $warmup_urls[] = $img_url;

        // Thử tải ảnh về Server với retry
        $final_img_src = $img_url; // Fallback về hotlink nếu download thất bại
        $max_tries = 3;
        for($try = 0; $try < $max_tries; $try++) {
            $tmp = download_url($img_url, 25);
            if(!is_wp_error($tmp)) {
                $file_array = [
                    'name'     => 'comic-' . $chap_num . '-panel-' . ($idx+1) . '-' . wp_rand(10,99) . '.jpg',
                    'tmp_name' => $tmp
                ];
                // Sideload vào Media Library, đính vào Chương (post_id = $truyen_id tạm)
                $att_id = media_handle_sideload($file_array, $truyen_id);
                if(!is_wp_error($att_id)) {
                    $final_img_src = wp_get_attachment_url($att_id);
                    break;
                }
                @unlink($tmp);
            }
            sleep(2); // Chờ 2 giây trước khi retry
        }

        $html_content .= '<div class="comic-panel">';
        $html_content .= '<img src="' . esc_attr($final_img_src) . '" alt="Cảnh truyện ' . $chap_num . ' panel ' . ($idx+1) . '" loading="lazy" />';
        
        if(!empty($p['dialogues']) && is_array($p['dialogues'])) {
            $html_content .= '<div class="bubbles-layer">';
            foreach($p['dialogues'] as $d_idx => $dialogue) {
                // Đảo hướng trái/phải ngẫu nhiên nhưng tuần tự
                $pos = ($d_idx % 2 == 0) ? '' : ' right';
                // Không cần manual margin vì đã có justify-content: space-evenly chặn rồi
                $html_content .= '<div class="bubble' . $pos . '">' . esc_html($dialogue) . '</div>';
            }
            $html_content .= '</div>';
        }
        
        $html_content .= '</div>';
        
        usleep(800000); // Delay 0.8 giây giữa các ảnh để tránh 429
    }

    $html_content .= '</div>';

    $chap_title = sanitize_text_field($_POST['chap_title'] ?? '');
    $final_title = !empty($chap_title) ? "Chương $chap_num: $chap_title" : "Chương $chap_num";

    $post_id = wp_insert_post([
        'post_title'   => $final_title,
        'post_content' => $html_content,
        'post_status'  => 'publish',
        'post_type'    => 'chuong',
        'menu_order'   => $chap_num,
        'post_author'  => get_current_user_id()
    ]);

    if(is_wp_error($post_id)) wp_send_json_error(['message' => 'Lỗi tạo Chương Comic.']);
    update_post_meta($post_id, '_truyen_id', $truyen_id);

    // Gieo mầm Comment gốc trực tiếp cho Webtoon (Không cần AI chế)
    if (!empty($custom_comments)) {
        $dummy_text = "---COMMENTS---\n" . $custom_comments;
        temply_parse_and_insert_ai_comments($post_id, $dummy_text);
    }

    wp_send_json_success([
        'chuong_id' => $post_id,
        'title' => $final_title,
        'warmup_urls' => $warmup_urls
    ]);
}

/**
 * FEATURE: KÍCH PHÓNG AI HOOK (BRAINSTORMING)
 */
add_action('wp_ajax_temply_step_brainstorm', 'temply_ajax_brainstorm');
function temply_ajax_brainstorm() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $genre = sanitize_text_field($_POST['genre'] ?? '');
    $keywords = sanitize_textarea_field($_POST['keywords'] ?? '');

    if(empty($keywords)) wp_send_json_error(['message' => 'Vui lòng nhập ít nhất 1-2 từ khoá để AI suy nghĩ.']);

    $system_prompt = "Bạn là AI Cố Vấn Cốt Truyện chuyên nghiệp. Dựa vào Thể loại và Vài từ khoá ngắn của người dùng, hãy sáng tạo ra đúng 3 ý tưởng/hook (mỗi ý tưởng dài 2-3 câu) thật giật gân, độc đáo, và câu khách.\nBạn PHẢI trả về đúng định dạng JSON Array chứa 3 chuỗi. KHÔNG giải thích gì thêm.\nVí dụ chuẩn: [\"[Hệ thống]: Bạn xuyên không thành nhân vật phụ...\", \"[Phản diện]: Cố tình đóng vai ác...\", \"[Vả mặt]: Giấu tài phiệt để thử lòng...\"]";
    $user_prompt = "Thể loại: $genre\nTừ khoá gốc: $keywords\nHãy cho tôi 3 options cốt truyện siêu cuốn.";

    $response = temply_call_ai_quality($system_prompt, $user_prompt, 0.9);
    if(is_wp_error($response)) wp_send_json_error(['message' => 'Lỗi kết nối AI: ' . $response->get_error_message()]);
    if(is_wp_error($response)) wp_send_json_error(['message' => $response->get_error_message()]);

    $json_str = preg_replace('/```(?:json)?|```/', '', $response);
    $arr = json_decode(trim($json_str), true);
    
    if(!is_array($arr) || empty($arr)) wp_send_json_error(['message' => 'Lỗi Parse JSON. AI trả về: ' . $response]);

    wp_send_json_success(['options' => $arr]);
}

/**
 * FEATURE: KÍCH PHÓNG AI HOOK (BRAINSTORMING WORLD BUILDING)
 */
add_action('wp_ajax_temply_step_brainstorm_world', 'temply_ajax_brainstorm_world');
function temply_ajax_brainstorm_world() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    $genre = sanitize_text_field($_POST['genre'] ?? '');
    $keywords = sanitize_textarea_field($_POST['keywords'] ?? '');

    $system_prompt = "Bạn là AI Cố Vấn Thế Giới Quan (World Building) cho Tiểu thuyết mạng. Dựa vào Thể loại và Từ khoá cốt truyện của người dùng, hãy sáng tạo ra đúng 3 tuỳ chọn Bối Cảnh & Thế Giới thật chi tiết, có chiều sâu (mỗi ý tưởng dài 3-4 câu).
QUY TẮC QUAN TRỌNG: 
1. Bối cảnh PHẢI TUYỆT ĐỐI TƯƠNG THÍCH với Thể loại và Cốt truyện. Nếu là truyện Đô Thị/Hiện Đại, bối cảnh phải là thành phố xa hoa, tập đoàn tài phiệt, quyền lực gia tộc mờ ám. Nếu là Tiên Hiệp/Cổ Đại, bối cảnh mới là môn phái, triều đại. Nếu là Kinh Dị, bối cảnh phải u ám, nguyền rủa.
2. BẮT BUỘC SỬ DỤNG BỐI CẢNH CHÂU Á (Việt Nam, Trung Quốc, Châu Á giả tưởng...). TUYỆT ĐỐI KHÔNG dùng bối cảnh hoặc tên gọi văn hóa Phương Tây/Âu Mỹ.
Bạn PHẢI trả về đúng định dạng JSON Array chứa 3 chuỗi. KHÔNG giải thích gì thêm.";
    $user_prompt = "Thể loại: $genre\nTừ khoá cốt truyện: $keywords\nHãy cho tôi 3 options Bối cảnh Thế giới (World building).";

    $response = temply_call_ai_quality($system_prompt, $user_prompt, 0.9);
    if(is_wp_error($response)) wp_send_json_error(['message' => 'Lỗi kết nối AI: ' . $response->get_error_message()]);

    $json_str = preg_replace('/```(?:json)?|```/', '', $response);
    $arr = json_decode(trim($json_str), true);
    
    if(!is_array($arr) || empty($arr)) wp_send_json_error(['message' => 'Lỗi Parse JSON. AI trả về: ' . $response]);

    wp_send_json_success(['options' => $arr]);
}

/**
 * FEATURE: AI TOOLKIT - REGENERATE CHAPTER (VIẾT LẠI CHƯƠNG)
 */
add_action('wp_ajax_temply_step_regenerate_chapter', 'temply_ajax_regenerate_chapter');
function temply_ajax_regenerate_chapter() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    set_time_limit(600);
    ignore_user_abort(true);

    $chuong_id = intval($_POST['chuong_id'] ?? 0);
    if(!$chuong_id) wp_send_json_error(['message' => 'Mất ID Chương.']);

    // Trích xuất dữ liệu móng từ Truyện mẹ
    $truyen_id = get_post_meta($chuong_id, '_truyen_id', true);
    if(!$truyen_id) wp_send_json_error(['message' => 'Không tìm thấy Truyện gốc.']);

    // Cho phép Override bằng Post Data nếu User có gõ vào Modal
    $world = isset($_POST['custom_world']) ? sanitize_textarea_field($_POST['custom_world']) : (get_post_meta($truyen_id, '_temply_ai_world', true) ?: '');
    $characters = isset($_POST['custom_characters']) ? sanitize_textarea_field($_POST['custom_characters']) : (get_post_meta($truyen_id, '_temply_ai_characters', true) ?: '');
    $summary = isset($_POST['custom_summary']) ? sanitize_textarea_field($_POST['custom_summary']) : (get_post_meta($chuong_id, '_temply_ai_summary', true) ?: '');
    $genre = get_post_meta($truyen_id, '_temply_ai_genre', true) ?: '';

    $old_post = get_post($chuong_id);
    $old_content = wp_strip_all_tags($old_post->post_content);

    // Nếu không có dàn ý, lấy chính nội dung text cũ làm nguồn
    if(empty($summary)) {
        $summary = "Biên tập viên không để lại lời nhắn.";
    }

    $system_prompt = "VAI TRÒ: Bạn là THE GHOSTWRITER. Nhiệm vụ: VIẾT LẠI (Regenerate) chương truyện này sao cho mượt mà, sâu sắc và kịch tính hơn dựa trên chuyên môn biên tập. BẮT BUỘC giữ nguyên toàn bộ cốt truyện, bối cảnh và hành động của CHƯƠNG CŨ, nhưng hành văn phải xuất sắc hơn và KHẮC PHỤC TRIỆT ĐỂ CÁC LỖI mà Biên Tập Viên đã nhắc nhở. Viết độ dài tối thiểu 800 chữ.\n\nLUẬT ĐỊNH DẠNG BẮT BUỘC TRẢ VỀ DƯỚI ĐÂY (Và KHÔNG ĐƯỢC sinh markdown code block):\n<p>Nội dung HTML của truyện với các thẻ p, strong</p>\n---COMMENTS---\nLuật Đẻ Bình Luận: Nhập vai cư dân mạng Việt Nam, Gen Z, hội mẹ tám (viết tắt, từ lóng, phẫn nộ, chửi thẳng). KHÔNG sến súa văn mẫu. Ví dụ: 'Đọc mà tức á', 'Má cái lão tác giả', 'đm con phò'.\nTên người 1|Bình luận cực mặn, nhập tâm chửi bới thật đời thường.\nTên người 2|Bình luận hóng hớt, viết tắt kiểu mạng xã hội.\n\nChú ý: Mục ---COMMENTS--- phải nằm ở DƯỚI CÙNG, tạo ra khoảng 3 bình luận giả lập sự xôn xao mạng xã hội.";

    if (stripos($genre, 'drama') !== false || stripos($genre, 'cẩu huyết') !== false || stripos($genre, 'vả mặt') !== false) {
        $system_prompt .= "\n\nHƯỚNG DẪN DRAMA CẨU HUYẾT: Đẩy mạnh tính cẩu huyết, mâu thuẫn gia đình gay gắt, khắc họa cực đoan những câu nói sỉ nhục, vả mặt hoặc sự uất ức. Hành văn gãy gọn sắc bén.";
    }

    $user_prompt = "[HỒ SƠ NHÂN VẬT]\n$characters\n\n[BỐI CẢNH THẾ GIỚI]\n$world\n\n============= NỘI DUNG CHƯƠNG CŨ (CỐT TRUYỆN GỐC TỪ TÁC GIẢ) =============\n$old_content\n=========================================================================\n\nVIẾT LẠI TOÀN BỘ CHƯƠNG TRÊN DỰA TRÊN LỜI NHẬN XÉT CỦA BIÊN TẬP VIÊN SAU ĐÂY:\n$summary\n\nSử dụng thẻ HTML (<p>, <strong>, <em>). Mở đầu bằng Hook hấp dẫn. Kết thúc bằng Cliffhanger kịch tính.";

    $response = temply_call_ai_quality($system_prompt, $user_prompt, 0.9);
    if(is_wp_error($response)) wp_send_json_error(['message' => 'Lỗi AI: ' . $response->get_error_message()]);

    $response = trim(preg_replace('/```(?:html)?|```/', '', trim($response)));
    $chap_content = trim(preg_replace('/^(?:\*\*|#)?\s*TITLE\s*:\s*(?:\*\*)?\s*.*\n?/i', '', $response)); // Lọc bỏ Title nếu AI lỡ sinh ra

    $chap_content = temply_parse_and_insert_ai_comments($chuong_id, $chap_content);

    if(empty($chap_content)) wp_send_json_error(['message' => 'Lỗi Parse Nội dung Rewrite.']);

    // Đè nội dung cũ
    wp_update_post([
        'ID' => $chuong_id,
        'post_content' => wp_kses_post($chap_content)
    ]);
    
    // Nếu có override từ Frontend Modal, lưu trữ giá trị mới luôn vào post_meta để lần sau tái sử dụng
    if(isset($_POST['custom_summary']) && !empty($_POST['custom_summary'])) {
        update_post_meta($chuong_id, '_temply_ai_summary', $_POST['custom_summary']);
    }

    wp_send_json_success(['message' => 'Regenerate thành công!', 'chuong_id' => $chuong_id]);
}

/**
 * FEATURE: AI TOOLKIT - GET CHAPTER CONTEXT
 */
add_action('wp_ajax_temply_step_get_chapter_context', 'temply_ajax_get_chapter_context');
add_action('wp_ajax_nopriv_temply_step_get_chapter_context', 'temply_ajax_get_chapter_context');
function temply_ajax_get_chapter_context() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    if (!current_user_can('manage_options')) wp_send_json_error(['message' => 'Không có quyền truy cập.']);

    $chuong_id = intval($_POST['chuong_id'] ?? 0);
    if(!$chuong_id) wp_send_json_error(['message' => 'Mất ID Chương.']);

    $truyen_id = get_post_meta($chuong_id, '_truyen_id', true);
    
    $world = ''; $characters = ''; $summary = ''; $genre = '';
    if ($truyen_id) {
        $world = get_post_meta($truyen_id, '_temply_ai_world', true) ?: '';
        $characters = get_post_meta($truyen_id, '_temply_ai_characters', true) ?: '';
        $genre = get_post_meta($truyen_id, '_temply_ai_genre', true) ?: '';
    }
    
    $summary = get_post_meta($chuong_id, '_temply_ai_summary', true) ?: '';
    
    if(empty($summary)) {
        $old_post = get_post($chuong_id);
        $summary = "Chương này thuộc thế hệ truyện Cũ chưa lưu Vết Dàn Ý. Vui lòng nhập ý tưởng/sườn diễn biến mới vào đây để AI viết lại thay thế cho Nội dung Hiện tại:\n" . wp_trim_words(wp_strip_all_tags($old_post->post_content), 50, '...');
    }

    $chapter_list = [];
    if ($truyen_id) {
        $args = [
            'post_type' => 'chuong',
            'meta_key' => '_truyen_id',
            'meta_value' => $truyen_id,
            'posts_per_page' => -1,
            'orderby' => 'menu_order date',
            'order' => 'ASC'
        ];
        $all_chaps = get_posts($args);
        foreach ($all_chaps as $c) {
            $chapter_list[] = [
                'id' => $c->ID,
                'title' => $c->post_title,
                'edit_url' => admin_url('post.php?post=' . $c->ID . '&action=edit')
            ];
        }
    }

    wp_send_json_success([
        'truyen_id' => $truyen_id,
        'world' => $world,
        'characters' => $characters,
        'summary' => $summary,
        'genre' => $genre,
        'chapter_list' => $chapter_list
    ]);
}

/**
 * FEATURE: AI TOOLKIT - GENERATE NEXT CHAPTER (SINH THÊM CHƯƠNG KẾ TIẾP)
 */
add_action('wp_ajax_temply_step_generate_next_chapter', 'temply_ajax_generate_next_chapter');
function temply_ajax_generate_next_chapter() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    set_time_limit(600);
    ignore_user_abort(true);

    $truyen_id = intval($_POST['truyen_id'] ?? 0);
    if(!$truyen_id) wp_send_json_error(['message' => 'Mất ID Truyện.']);

    // Đếm tổng chuơng
    $args = ['post_type' => 'chuong', 'meta_key' => '_truyen_id', 'meta_value' => $truyen_id, 'posts_per_page' => -1, 'fields' => 'ids'];
    $all_chap_ids = get_posts($args);
    if(empty($all_chap_ids)) wp_send_json_error(['message' => 'Truyện chưa có chương nào để viết tiếp.']);
    
    $next_chap_num = count($all_chap_ids) + 1;
    $last_chap = get_posts(['post_type' => 'chuong', 'meta_key' => '_truyen_id', 'meta_value' => $truyen_id, 'posts_per_page' => 1, 'orderby' => 'date', 'order' => 'DESC'])[0];
    
    $last_content = wp_strip_all_tags($last_chap->post_content);
    // Cắt gọt text cũ nếu quá dài
    if(mb_strlen($last_content) > 3000) {
        $last_content = mb_substr($last_content, -3000) . '... (Cắt bớt phần đầu)';
    }

    $world = get_post_meta($truyen_id, '_temply_ai_world', true) ?: '';
    $characters = get_post_meta($truyen_id, '_temply_ai_characters', true) ?: '';
    $genre = get_post_meta($truyen_id, '_temply_ai_genre', true) ?: '';

    $custom_next = isset($_POST['custom_next_outline']) ? sanitize_textarea_field($_POST['custom_next_outline']) : '';

    if (!empty($custom_next)) {
        // Nếu user MỚM dàn ý, bỏ qua bước tự brainstorm, dùng luôn dàn ý do user feed.
        $next_summary = $custom_next;
    } else {
        // BƯỚC 1: BRAINSTORM THE NEXT OUTLINE
        $br_sys = "Bạn là THE ARCHITECT. Nhiệm vụ: Đọc diễn biến từ cuối chương trước, sau đó Nghĩ ra Dàn Ý tóm tắt cho Chương Số $next_chap_num tiếp theo.\nBắt buộc trả về đúng 1 đoạn Text tóm tắt dài tầm 50-100 chữ chứa diễn biến chính của chương mới. KHÔNG FORMAT JSON.";
        $br_user = "[Bối Cảnh]\n$world\n\n[Nhân vật]\n$characters\n\n[Nội dung diễn biến ở cuối Chương trước]\n$last_content\n\nHãy tóm tắt diễn biến của NGAY CHƯƠNG KẾ TIẾP (Chương $next_chap_num).";
        
        $next_summary = temply_call_ai($br_sys, $br_user, 0.9);
        if(is_wp_error($next_summary)) wp_send_json_error(['message' => 'Lỗi Brainstorm AI: ' . $next_summary->get_error_message()]);
    }

    // BƯỚC 2: VIẾT CHƯƠNG MỚI THEO OUTLINE KIA
    $system_prompt = "VAI TRÒ: Bạn là THE GHOSTWRITER. Viết tiếp Chương $next_chap_num dựa trên tóm tắt diễn biến tiếp theo. Viết thật dài, chi tiết (tối thiểu 800 chữ).\n\nLUẬT ĐỊNH DẠNG BẮT BUỘC TRẢ VỀ DƯỚI ĐÂY (Và KHÔNG ĐƯỢC sinh markdown code block):\nTITLE: [Tên chương ấn tượng bằng tiếng Việt]\n<p>Nội dung HTML của truyện với các thẻ p, strong</p>\n---COMMENTS---\nLuật Bình Luận: Nhập vai mxh Việt Nam bực tức, cục súc hoặc xót xa (viết tắt vcl, tr ơi, bó tay, má nó). KHÔNG văn mẫu, chỉ nói ngôn ngữ mạng đời thường.\nTên người 1|chửi mắng ác liệt hoặc hóng chương mới.\nTên người 2|Bình luận cực gắt về một twist trong chương.\n\nChú ý: Mục ---COMMENTS--- phải nằm ở DƯỚI CÙNG, tạo ra khoảng 3 bình luận giả lập sự xôn xao mạng xã hội.";
    if (stripos($genre, 'drama') !== false || stripos($genre, 'cẩu huyết') !== false || stripos($genre, 'vả mặt') !== false) {
        $system_prompt .= "\n\nHƯỚNG DẪN DRAMA CẨU HUYẾT: Đẩy mạnh tính cẩu huyết, mâu thuẫn gia đình, vả mặt hoặc sự uất ức. Hành văn gãy gọn sắc bén. Nếu không phải là hồi kết, luôn chốt chương bằng Cliffhanger.";
    }

    $user_prompt = "[HỒ SƠ NHÂN VẬT]\n$characters\n\n[BỐI CẢNH]\n$world\n\nVIẾT CHI TIẾT Chương $next_chap_num dựa theo Dàn Ý bám sát này:\n$next_summary";
    $response = temply_call_ai_quality($system_prompt, $user_prompt, 0.9);
    if(is_wp_error($response)) wp_send_json_error(['message' => 'Lỗi Viết AI: ' . $response->get_error_message()]);

    $response_trimmed = trim(preg_replace('/```(?:html|json)?|```/', '', $response));
    $chap_title = "Kì Tiếp Theo";
    if(preg_match('/(?:^|\n)\s*(?:\*\*|#)?\s*TITLE\s*:\s*(?:\*\*)?\s*(.*)/i', $response_trimmed, $m)) {
        $chap_title = trim($m[1]);
        $parts = preg_split('/(?:^|\n)\s*(?:\*\*|#)?\s*TITLE\s*:\s*(?:\*\*)?\s*.*\n/i', $response_trimmed, 2);
        $chap_content = trim($parts[1] ?? '');
        if(empty($chap_content)) $chap_content = trim(preg_replace('/(?:^|\n)\s*(?:\*\*|#)?\s*TITLE\s*:\s*(?:\*\*)?\s*.*/i', '', $response_trimmed, 1));
    } else {
        $lines = explode("\n", $response_trimmed);
        if(count($lines)>2) { $chap_title = trim(array_shift($lines)); $chap_content = trim(implode("\n", $lines)); } 
        else { $chap_content = $response_trimmed; }
    }

    $post_id = wp_insert_post([
        'post_title'   => "Chương $next_chap_num: $chap_title",
        'post_content' => wp_kses_post('Đang tạo nội dung...'),
        'post_status'  => 'publish',
        'post_type'    => 'chuong',
        'menu_order'   => $next_chap_num,
        'post_author'  => get_current_user_id()
    ]);

    if(is_wp_error($post_id)) wp_send_json_error(['message' => 'Lỗi tạo Chương.']);
    
    // Parse comments and update true content
    $clean_content = temply_parse_and_insert_ai_comments($post_id, $chap_content);
    wp_update_post([
        'ID' => $post_id,
        'post_content' => wp_kses_post($clean_content)
    ]);

    update_post_meta($post_id, '_truyen_id', $truyen_id);
    update_post_meta($post_id, '_temply_ai_summary', $next_summary);

    wp_send_json_success(['message' => 'Tự đẻ chương N+1 thành công!', 'chuong_id' => $post_id, 'redirect_url' => get_permalink($post_id)]);
}

/**
 * FEATURE: AUTO PILOT CRON PROCESSOR (BULK PIPELINE)
 * Lập lịch đẻ truyện + Review tự động. Xử lý theo Hàng Đợi (Queue).
 */
add_action('temply_auto_pilot_cron_hook', 'temply_process_auto_pilot');
function temply_process_auto_pilot() {
    $config = get_option('temply_auto_pilot_queue_config', false);
    if (!$config || $config['status'] !== 'running' || empty($config['queue'])) {
        wp_clear_scheduled_hook('temply_auto_pilot_cron_hook');
        return;
    }

    // Tìm Truyện đang làm dở (writing) hoặc chờ mổ (pending)
    $active_idx = -1;
    foreach($config['queue'] as $i => $item) {
        if ($item['status'] === 'draft_outline' || $item['status'] === 'pending' || $item['status'] === 'writing') {
            $active_idx = $i;
            break; // Tìm thấy thì dừng
        }
    }

    // Nếu xong hết cmnr
    if ($active_idx === -1) {
        $config['status'] = 'completed';
        update_option('temply_auto_pilot_queue_config', $config);
        wp_clear_scheduled_hook('temply_auto_pilot_cron_hook');
        return;
    }

    // Tham chiếu để thay đổi update lưu lại
    $curr_item = &$config['queue'][$active_idx];
    $model = 'gemini'; 

    // ===============================================
    // STAGE 0: DRAFT OUTLINE (Sinh Tự Động Metadata từ Kịch Bản Raw)
    // ===============================================
    if ($curr_item['status'] === 'draft_outline') {
        $raw_prompt = $curr_item['prompt'] ?? '';
        $hint_genre = $curr_item['genre'] ?? '';
        $hint_tone  = $curr_item['tone'] ?? '';

        $sys = "Bạn là NHÀ THIẾT KẾ KỊCH BẢN TRUYỆN MẠNG. Dựa trên Ý TƯỞNG CỐT LÕI (Prompt) dưới đây, hãy phát triển thành một hệ thống thông tin đầy đủ để viết một tác phẩm dài kỳ. TRẢ VỀ CHỈ 1 MẢNG JSON duy nhất, KHÔNG giải thích thêm.
QUY TẮC:
- Nhân vật & Bối cảnh BẮT BUỘC phải mang đậm nét văn hóa Châu Á (Việt Nam, Trung Quốc...). 
- Nghiêm cấm dùng tên Phương Tây/Tiếng Anh. Tên nhân vật, tổ chức, bản đồ phải thuần Việt hoặc Hán Việt.";
        $usr = "Ý TƯỞNG CỐT LÕI:\n$raw_prompt\n\nThể loại: $hint_genre\nGiọng văn: $hint_tone\n\nYÊU CẦU JSON ĐẦU RA:\n{\n  \"title\": \"Tên truyện (Giật gân, hấp dẫn, độ dài vừa phải)\",\n  \"synopsis\": \"Tóm tắt/Văn án truyện CỤC KỲ GIẬT GÂN, gây sốc và khơi gợi tò mò tột độ để người đọc lao vào ngay. Ngắn gọn dưới 100 chữ.\",\n  \"world\": \"Bối cảnh thế giới chi tiết (Luật lệ, quy tắc, gia tộc, bản đồ mang đậm nét Châu Á...)\",\n  \"chars\": \"Tuyến nhân vật chính (Ngoại hình, tính cách, vũ khí/khả năng). Tên nhân vật thuần Châu Á.\",\n  \"script\": \"Dàn ý sự kiện chính của toàn bộ tác phẩm (Outline)\"\n}";
        
        $ai_data = temply_call_ai($sys, $usr, 0.7, $model);
        if(!is_wp_error($ai_data)) {
            // Trim and extract json 
            $ai_data = preg_replace('/```(?:json)?|```/', '', $ai_data);
            $parsed = json_decode(trim($ai_data), true);
            if($parsed && isset($parsed['title'])) {
                $curr_item['title']  = sanitize_text_field($parsed['title']);
                $curr_item['synopsis'] = sanitize_textarea_field($parsed['synopsis'] ?? '');
                $curr_item['world']  = sanitize_textarea_field($parsed['world'] ?? '');
                $curr_item['chars']  = sanitize_textarea_field($parsed['chars'] ?? '');
                $curr_item['script'] = sanitize_textarea_field($parsed['script'] ?? '');
                $curr_item['status'] = 'pending'; // Nâng lên pending để chờ sinh truyện
                update_option('temply_auto_pilot_queue_config', $config);
            } else {
                error_log('TEMPLY AUTO PILOT ERROR: Lỗi parse JSON ' . $ai_data);
                $curr_item['status'] = 'failed';
                $curr_item['error_log'] = 'Lỗi Parse JSON (Tắt cẩu huyết/văn mẫu quá mức).';
                update_option('temply_auto_pilot_queue_config', $config);
            }
        } else {
            error_log('TEMPLY AUTO PILOT ERROR: Lỗi tạo Dàn Ý Tự động ' . $ai_data->get_error_message());
            $curr_item['status'] = 'failed';
            update_option('temply_auto_pilot_queue_config', $config);
        }
        return; // Dừng cron lần này, chờ cron sau tạo post
    }

    // ===============================================
    // STAGE 1: INITIATION (Khởi Tạo Truyện Mới Từ Data Staging Đã Duyệt)
    // ===============================================
    if ($curr_item['status'] === 'pending') {
        $prompt = $curr_item['prompt'] ?? '';
        $title = $curr_item['title'] ?? 'Truyện Mới';
        $genre = $curr_item['genre'] ?? 'Hỗn hợp';
        $tone = $curr_item['tone'] ?? 'Lôi cuốn';
        $world = $curr_item['world'] ?? '';
        $script = $curr_item['script'] ?? '';
        $chars = $curr_item['chars'] ?? '';
        
        // Tất cả Data bối cảnh đã có sẵn từ lưới Staging, không cần gọi AI rặn nữa! Đỡ được 20s.
        $truyen_id = wp_insert_post([
            'post_type' => 'truyen',
            'post_title' => $title,
            'post_excerpt' => $curr_item['synopsis'] ?? mb_substr(wp_strip_all_tags($script), 0, 300),
            'post_content' => wp_kses_post("<h3>1. Bối cảnh Thế Giới</h3><p>" . nl2br(esc_html($world)) . "</p><br><h3>2. Nhân Vật</h3><p>" . nl2br(esc_html($chars)) . "</p><br><h3>3. Kịch Bản</h3><p>" . nl2br(esc_html($script)) . "</p>"),
            'post_status' => 'publish',
            'post_author' => 1
        ]);
        
        if (is_wp_error($truyen_id)) return;

        update_post_meta($truyen_id, '_temply_ai_genre', $genre);
        update_post_meta($truyen_id, '_temply_ai_tone', $tone);
        update_post_meta($truyen_id, '_temply_ai_world', $world);
        update_post_meta($truyen_id, '_temply_ai_script', $script);
        update_post_meta($truyen_id, '_temply_ai_characters', $chars);

        // Đổi trang thái Hàng Đợi -> Writing (Sẽ viết ở nhịp sau)
        $curr_item['status'] = 'writing';
        $curr_item['truyen_id'] = $truyen_id;
        
        // Lưu Config cẩn thận!
        update_option('temply_auto_pilot_queue_config', $config);
        
        // Bắn Lệnh Đẻ Ảnh Bìa Bối Cảnh (Chạy ngầm không đợi)
        wp_remote_post(home_url('/wp-json/temply/v1/backfill-covers'), ['blocking' => false]);
        
        return; // XONG NHỊP 1
    }

    // ===============================================
    // STAGE 2: WRITING (Đẻ Chương Dần Từng Chút)
    // ===============================================
    $truyen_id = intval($curr_item['truyen_id']);
    $enable_audit = intval($curr_item['enable_audit']);
    
    // Tự động đếm tổng số chương hiện có để tính số chương tiếp theo (Bền bỉ hơn menu_order)
    $args = ['post_type' => 'chuong', 'meta_key' => '_truyen_id', 'meta_value' => $truyen_id, 'posts_per_page' => -1, 'fields' => 'ids'];
    $all_chap_ids = get_posts($args);
    $next_chap_num = count($all_chap_ids) + 1;
    $last_content = '';
    
    // Lấy nội dung chương gần nhất (nếu có)
    if (!empty($all_chap_ids)) {
        $last_chap = get_posts(['post_type' => 'chuong', 'meta_key' => '_truyen_id', 'meta_value' => $truyen_id, 'posts_per_page' => 1, 'orderby' => 'date', 'order' => 'DESC'])[0];
        $last_content = wp_strip_all_tags($last_chap->post_content);
        if(mb_strlen($last_content) > 3000) {
            $last_content = mb_substr($last_content, -3000) . '... (Cắt bớt phần đầu)';
        }
    } else {
        $last_content = "Đây là chương mở đầu. Hãy viết một cách hoành tráng.";
    }

    $world = get_post_meta($truyen_id, '_temply_ai_world', true) ?: '';
    $characters = get_post_meta($truyen_id, '_temply_ai_characters', true) ?: '';
    $script = get_post_meta($truyen_id, '_temply_ai_script', true) ?: '';
    $genre = get_post_meta($truyen_id, '_temply_ai_genre', true) ?: '';

    // A. BRAINSTORM (Haiku / Gemini)
    $br_sys = "Bạn là THE ARCHITECT - Bậc thầy xây dựng cốt truyện kịch tính nảy lửa. 
Nhiệm vụ: Nghĩ ra Dàn Ý cho Chương $next_chap_num.
YÊU CẦU BẮT BUỘC: 
- Phải có RỦI RO (Stakes) và XUNG ĐỘT (Conflict). Tuyệt đối không để nhân vật ngồi im tâm sự nhẹ nhàng, không viết kiểu tản văn hay trị liệu tâm lý. 
- Phải có biến cố, hành động hoặc bí mật được hé lộ gây rúng động, bám sát sát điệu thể loại.
Chỉ trả về 1 đoạn 100 chữ tóm tắt diễn biến. KHÔNG JSON.";
    $br_user = "[THỂ LOẠI TÁC PHẨM]\n$genre\n\n[Bối Cảnh]\n$world\n\n[Kịch bản gốc / Cốt truyện]\n$script\n\n[Nhân vật]\n$characters\n\n[Diễn biến cũ/Ghi chú]\n$last_content\n\nViết tóm tắt mạch truyện ĐẬM ĐẶC KỊCH TÍNH cho trương $next_chap_num.";
    $next_summary = temply_call_ai($br_sys, $br_user, 0.9, $model);
    if(is_wp_error($next_summary)) {
        error_log('TEMPLY AUTO PILOT ERROR: Lỗi Brainstorm ' . $next_summary->get_error_message());
        return; // Dừng cron lần này, chờ lần sau
    }

    // B. RẶN CHỮ
    $system_prompt = "VAI TRÒ: THE GHOSTWRITER. Bạn là Tiểu Thuyết Gia Hàng Đầu. Viết tiếp Chương $next_chap_num dựa trên tóm tắt. Viết dài tối thiểu 800 chữ.
LUẬT BẮT BUỘC VỀ VĂN PHONG:
- Cốt truyện phải logic, liên kết chặt chẽ với tên truyện và thể loại. Hành động dứt khoát, âm mưu sâu sắc, tuyệt đối không loanh quanh tự kỷ.
- Nếu là trinh thám/hành động, phải có máu, sự đen tối và rượt đuổi. Nếu là gia đấu/cẩu huyết, phải có đấu trí và lật lọng. 
- CHÓT VÓT CAO TRÀO: Không bao giờ để mọi thứ trôi qua êm đềm. Giải quyết 1 khó khăn thì phải nảy sinh tiểu xảo, bẫy rập mới.
FORMAT BẮT BUỘC:
TITLE: [Tên chương ấn tượng, đầy bí ẩn]
<p>Nội dung HTML</p>
---COMMENTS---
User1|chửi
User2|hóng";
    if (stripos($genre, 'drama') !== false || stripos($genre, 'cẩu huyết') !== false || stripos($genre, 'hành động') !== false || stripos($genre, 'trinh thám') !== false) {
        $system_prompt .= "\n\nHARDCORE MODE: Đẩy mạnh cẩu huyết, mâu thuẫn, máu me, đổ vỡ, hoặc đấu trí rùng rợn. Phản diện phải tàn ác và thông minh.";
    }
    $user_prompt = "[CHỈ ĐẠO KỊCH BẢN CHUNG]\n$script\n\n[NHÂN VẬT]\n$characters\n\n[BỐI CẢNH]\n$world\n\nViết Chương $next_chap_num bám theo:\n$next_summary";
    
    $response = temply_call_ai_quality($system_prompt, $user_prompt, 0.9, $model);
    if(is_wp_error($response)) {
        error_log('TEMPLY AUTO PILOT ERROR: Lỗi Viết nội dung ' . $response->get_error_message());
        $curr_item['status'] = 'failed';
        update_option('temply_auto_pilot_queue_config', $config);
        return;
    }

    $response_trimmed = trim(preg_replace('/```(?:html|json)?|```/', '', $response));
    $chap_title = "Kì Tiếp Theo";
    if(preg_match('/(?:^|\n)\s*(?:\*\*|#)?\s*TITLE\s*:\s*(?:\*\*)?\s*(.*)/i', $response_trimmed, $m)) {
        $chap_title = trim($m[1]);
        $parts = preg_split('/(?:^|\n)\s*(?:\*\*|#)?\s*TITLE\s*:\s*(?:\*\*)?\s*.*\n/i', $response_trimmed, 2);
        $chap_content = trim($parts[1] ?? '');
        if(empty($chap_content)) $chap_content = trim(preg_replace('/(?:^|\n)\s*(?:\*\*|#)?\s*TITLE\s*:\s*(?:\*\*)?\s*.*/i', '', $response_trimmed, 1));
    } else {
        $lines = explode("\n", $response_trimmed);
        if(count($lines)>2) { $chap_title = trim(array_shift($lines)); $chap_content = trim(implode("\n", $lines)); } 
        else { $chap_content = $response_trimmed; }
    }

    // C. KIỂM DUYỆT KHẮT KHE (Tự Khen Tự Chê)
    if ($enable_audit && !empty($chap_content)) {
        $eval_sys = "Bạn là THE RUTHLESS EDITOR. Một nhà phê bình siêu khắc nghiệt. Hãy đọc nội dung chương truyện sau.
Nhiệm vụ: Chỉ trích các lỗi về Logic, Mức độ cẩu huyết, Nhịp điệu.
KHÔNG khen ngợi. Chỉ tìm điểm yếu để yêu cầu viết lại.
Trả về bài review lỗi chi tiết.";
        $eval_user = "TÓM TẮT DÀN Ý ĐÃ DUYỆT:\n" . $next_summary . "\n\nNỘI DUNG VỪA VIẾT:\n" . wp_strip_all_tags($chap_content);
        
        $review_feedback = temply_call_ai($eval_sys, $eval_user, 0.7, $model);
        
        if(!is_wp_error($review_feedback)) {
            // Tự sửa lại dựa trên lỗi
            $rewrite_user = "BỐI CẢNH:\n$world\n\nNHẬN XÉT CỦA BIÊN TẬP:\n$review_feedback\n\nHãy VIẾT LẠI HOÀN TOÀN TỪ ĐẦU nội dung chương truyện này. Sửa sạch các lỗi trên, viết sâu sắc, bùng nổ hơn.\nGiữ nguyên định dạng TITLE: [Tên] \n <p>...</p>\n---COMMENTS---...";
            $rewritten_response = temply_call_ai_quality($system_prompt, $rewrite_user, 0.9, $model);
            
            if(!is_wp_error($rewritten_response)) {
                $rewritten_trimmed = trim(preg_replace('/```(?:html|json)?|```/', '', $rewritten_response));
                if(preg_match('/(?:^|\n)\s*(?:\*\*|#)?\s*TITLE\s*:\s*(?:\*\*)?\s*(.*)/i', $rewritten_trimmed, $m2)) {
                    $chap_title = trim($m2[1]);
                    $parts2 = preg_split('/(?:^|\n)\s*(?:\*\*|#)?\s*TITLE\s*:\s*(?:\*\*)?\s*.*\n/i', $rewritten_trimmed, 2);
                    $chap_content = trim($parts2[1] ?? '');
                } else {
                    $lines2 = explode("\n", $rewritten_trimmed);
                    if(count($lines2)>2) { $chap_title = trim(array_shift($lines2)); $chap_content = trim(implode("\n", $lines2)); } 
                    else { $chap_content = $rewritten_trimmed; }
                }
            }
        }
    }

    // D. Lên Sóng Publish
    $chap_title = trim(preg_replace('/\s+/', ' ', str_replace(['*', '#', '[', ']', 'TITLE:', 'TITLE :', 'Title:', 'title:'], '', $chap_title)));
    $post_id = wp_insert_post([
        'post_title'   => "Chương $next_chap_num: $chap_title",
        'post_content' => wp_kses_post('Đang tạo...'),
        'post_status'  => 'publish',
        'post_type'    => 'chuong',
        'menu_order'   => $next_chap_num,
        'post_author'  => 1
    ]);

    if(!is_wp_error($post_id)) {
        $clean_content = temply_parse_and_insert_ai_comments($post_id, $chap_content);
        wp_update_post([
            'ID' => $post_id,
            'post_content' => wp_kses_post($clean_content)
        ]);

        update_post_meta($post_id, '_truyen_id', $truyen_id);
        update_post_meta($post_id, '_temply_ai_summary', $next_summary);
        
        // Trừ đi 1 chương trong hợp đồng của Item hiện tại
        $curr_item['chapters_left'] = $curr_item['chapters_left'] - 1;
        $config['last_run'] = time();
        
        if ($curr_item['chapters_left'] <= 0) {
            $curr_item['status'] = 'completed';
        }
        
        update_option('temply_auto_pilot_queue_config', $config);
    }
}

/**
 * FEATURE: AI TOOLKIT - GET STORY MASTER CONTEXT (STORY MANAGER)
 */
add_action('wp_ajax_temply_step_get_story_master_context', 'temply_ajax_get_story_master_context');
function temply_ajax_get_story_master_context() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    if (!current_user_can('manage_options')) wp_send_json_error(['message' => 'Không có quyền truy cập.']);

    $truyen_id = intval($_POST['truyen_id'] ?? 0);
    if(!$truyen_id) wp_send_json_error(['message' => 'Mất ID Truyện.']);

    $world = get_post_meta($truyen_id, '_temply_ai_world', true) ?: '';
    $characters = get_post_meta($truyen_id, '_temply_ai_characters', true) ?: '';
    $genre = get_post_meta($truyen_id, '_temply_ai_genre', true) ?: '';

    $chapter_list = [];
    $args = [
        'post_type' => 'chuong',
        'meta_key' => '_truyen_id',
        'meta_value' => $truyen_id,
        'posts_per_page' => -1,
        'orderby' => 'menu_order date',
        'order' => 'ASC'
    ];
    $all_chaps = get_posts($args);
    foreach ($all_chaps as $c) {
        $ch_summary = get_post_meta($c->ID, '_temply_ai_summary', true) ?: '';
        if(empty($ch_summary)) {
            $ch_summary = "Chưa có Dàn Ý lưu nháp. Đây là truyện cũ.\nNội dung vắn tắt:\n" . wp_trim_words(wp_strip_all_tags($c->post_content), 30, '...');
        }
        $chapter_list[] = [
            'id' => $c->ID,
            'title' => $c->post_title,
            'summary' => $ch_summary
        ];
    }

    wp_send_json_success([
        'truyen_id' => $truyen_id,
        'world' => $world,
        'characters' => $characters,
        'genre' => $genre,
        'chapter_list' => $chapter_list
    ]);
}

/**
 * FEATURE: AI TOOLKIT - SAVE STORY MASTER CONTEXT
 */
add_action('wp_ajax_temply_step_save_story_master_context', 'temply_ajax_save_story_master_context');
function temply_ajax_save_story_master_context() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    if (!current_user_can('manage_options')) wp_send_json_error(['message' => 'Không có quyền truy cập.']);

    $truyen_id = intval($_POST['truyen_id'] ?? 0);
    if(!$truyen_id) wp_send_json_error(['message' => 'Mất ID Truyện.']);

    if (isset($_POST['world'])) update_post_meta($truyen_id, '_temply_ai_world', wp_unslash($_POST['world']));
    if (isset($_POST['characters'])) update_post_meta($truyen_id, '_temply_ai_characters', wp_unslash($_POST['characters']));
    if (isset($_POST['genre'])) update_post_meta($truyen_id, '_temply_ai_genre', wp_unslash($_POST['genre']));

    if (isset($_POST['chapter_summaries'])) {
        $summaries = json_decode(wp_unslash($_POST['chapter_summaries']), true);
        if (is_array($summaries)) {
            foreach($summaries as $chap_id => $sum) {
                update_post_meta(intval($chap_id), '_temply_ai_summary', $sum);
            }
        }
    }

    wp_send_json_success(['message' => 'Lưu Tổng Trạm Thành Công!']);
}

/**
 * FEATURE: AI TOOLKIT - REGENERATE STORY COVER
 */
add_action('wp_ajax_temply_step_regenerate_story_cover', 'temply_ajax_regenerate_story_cover');
function temply_ajax_regenerate_story_cover() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    if (!current_user_can('manage_options')) wp_send_json_error(['message' => 'Không có quyền truy cập.']);

    $truyen_id = intval($_POST['truyen_id'] ?? 0);
    if(!$truyen_id) wp_send_json_error(['message' => 'Mất ID Truyện.']);

    $world = get_post_meta($truyen_id, '_temply_ai_world', true) ?: '';
    $title = get_the_title($truyen_id);

    $system_prompt = "You are an expert anime/manga illustrator prompt engineer. Read the story context and output ONLY ONE English sentence to be used as an image generation prompt. No quotes, no markdown.";
    $user_prompt = "Title: $title\nWorld Context: $world\nCreate a prompt for a book cover. Example: A handsome CEO standing in front of a skyscraper, dark cinematic lighting...";
    
    $cover_prompt = temply_call_ai_quality($system_prompt, $user_prompt, 0.9);
    if(is_wp_error($cover_prompt)) wp_send_json_error(['message' => 'Lỗi AI: ' . $cover_prompt->get_error_message()]);

    $cover_full_prompt = trim($cover_prompt) . ', high quality manga illustration, masterpiece, best quality, highly detailed cover art';
    $escaped_prompt = rawurlencode($cover_full_prompt);
    $image_url = "https://image.pollinations.ai/prompt/" . $escaped_prompt . "?width=600&height=900&nologo=true";
    
    $thumb_id = temply_upload_external_image($image_url, $truyen_id, $title);

    if ($thumb_id) {
        wp_send_json_success(['message' => 'Đã vẽ xong ảnh bìa (Thumbnail)! Vui lòng refresh trang để thấy.', 'url' => wp_get_attachment_url($thumb_id)]);
    } else {
        wp_send_json_error(['message' => 'AI Cứng đầu vẽ nháp đen xì hoặc API quá tải. Hãy thử lại!']);
    }
}

/**
 * AUTO-REVIEW: AI tự đọc chương và sinh nhận xét biên tập chi tiết.
 */
add_action('wp_ajax_temply_auto_review_chapter', 'temply_ajax_auto_review_chapter');
function temply_ajax_auto_review_chapter() {
    check_ajax_referer('temply_ai_nonce', 'nonce');
    set_time_limit(120);

    $chuong_id = intval($_POST['chuong_id'] ?? 0);
    if (!$chuong_id) wp_send_json_error(['message' => 'Thi\u1ebfu ID ch\u01b0\u01a1ng.']);

    $post = get_post($chuong_id);
    if (!$post) wp_send_json_error(['message' => 'Kh\u00f4ng t\u00ecm th\u1ea5y ch\u01b0\u01a1ng.']);

    $content_text = wp_strip_all_tags($post->post_content);
    $truyen_id    = get_post_meta($chuong_id, '_truyen_id', true);
    $genre        = get_post_meta($truyen_id, '_temply_ai_genre', true) ?: 'Ch\u01b0a r\u00f5 th\u1ec3 lo\u1ea1i';

    $excerpt = mb_substr($content_text, 0, 5000);

    $system_prompt = "Bạn là BIÊN TẬP VIÊN TIỂU THUYẾT chuyên nghiệp, chuyên đọc và đánh giá văn chương web Việt Nam.\nNhiệm vụ: Đọc đoạn truyện thể loại [{$genre}] dưới đây và đưa ra NHẬN XÉT.\n\nNẾU CHƯƠNG ĐÃ RẤT HAY, LOGIC MƯỢT MÀ, HÀNH VĂN CUỐN HÚT: Chỉ cần trả về duy nhất cụm từ 'ĐẠT CHUẨN - Không cần sửa thêm'.\n\nNẾU CHƯƠNG KÉM HAY CẦN SỬA, MỚI LIỆT KÊ:\n1. Điểm yếu lớn nhất (hành văn, logic)\n2. Cụ thể cần sửa gì\n\nQUAN TRỌNG: Nhận xét NGẮN GỌN (dưới 300 từ), TRỰC TIẾP. Viết bằng tiếng Việt.";

    $user_prompt = "Nội dung chương truyện cần đánh giá:\n\n" . $excerpt;

    $response = temply_call_ai($system_prompt, $user_prompt, 0.7);
    if (is_wp_error($response)) {
        wp_send_json_error(['message' => 'AI l\u1ed7i: ' . $response->get_error_message()]);
    }

    wp_send_json_success(['review' => trim($response)]);
}
