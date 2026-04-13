import re

with open("temply-ai-factory/includes/openai-api.php", "r") as f:
    content = f.read()

gemini_code = """
/**
 * Gọi API Google Gemini (1.5 Flash).
 */
function temply_call_gemini($system_prompt, $user_prompt, $temperature = 0.7) {
    $api_key = get_option('temply_gemini_api_key', '');
    if(empty($api_key)) return new WP_Error('no_api_key', 'Chưa cấu hình Gemini API Key');

    $url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" . $api_key;
    
    $payload = [
        "system_instruction" => [
            "parts" => [
                ["text" => $system_prompt]
            ]
        ],
        "contents" => [
            [
                "role" => "user",
                "parts" => [
                    ["text" => $user_prompt]
                ]
            ]
        ],
        "generationConfig" => [
            "temperature" => $temperature
        ]
    ];

    $response = wp_remote_post($url, [
        'headers' => [
            'Content-Type' => 'application/json'
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

    if(isset($data['candidates'][0]['content']['parts'][0]['text'])) {
        return $data['candidates'][0]['content']['parts'][0]['text'];
    }

    return new WP_Error('parse_error', 'Không đọc được phản hồi từ Gemini AI');
}

/**
 * Điều hướng API (OpenAI hoặc Gemini)
 */
function temply_call_ai($system_prompt, $user_prompt, $temperature = 0.7) {
    if(isset($_POST['ai_model']) && $_POST['ai_model'] === 'gemini') {
        return temply_call_gemini($system_prompt, $user_prompt, $temperature);
    }
    return temply_call_openai($system_prompt, $user_prompt, $temperature);
}
"""

content = content.replace("/**\n * Hàm hỗ trợ Tải Ảnh Từ URL làm Thumbnail", gemini_code + "\n/**\n * Hàm hỗ trợ Tải Ảnh Từ URL làm Thumbnail")
content = re.sub(r'temply_call_openai\(', 'temply_call_ai(', content)
content = re.sub(r'function temply_call_ai\(\$system_prompt, \$user_prompt, \$temperature = 0.7\) \{', 'function temply_call_openai_REPLACE_ME($system_prompt, $user_prompt, $temperature = 0.7) {', content)
content = content.replace('temply_call_openai_REPLACE_ME', 'temply_call_ai')

with open("temply-ai-factory/includes/openai-api.php", "w") as f:
    f.write(content)
