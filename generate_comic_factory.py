import re

# 1. Update admin-ui.php
with open("temply-ai-factory/admin-ui.php", "r", encoding="utf-8") as f:
    admin_ui = f.read()

replacement_html = """
                            <div class="grid grid-cols-2 gap-4 mb-4">
                                <div>
                                    <label class="block text-sm font-semibold text-slate-700 mb-2">Định dạng</label>
                                    <select id="temply-mode" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none text-sm bg-slate-50 font-bold text-blue-700">
                                        <option value="text">📖 Truyện Chữ</option>
                                        <option value="comic">🎨 Truyện Tranh</option>
                                    </select>
                                </div>
                                <div>
                                    <label class="block text-sm font-semibold text-slate-700 mb-2">Số lượng Chương</label>
                                    <input type="number" id="temply-num-chapters" min="1" max="20" value="3" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none text-sm bg-slate-50">
                                </div>
                            </div>
                            
                            <div id="tone-group">
                                <label class="block text-sm font-semibold text-slate-700 mb-2">Văn phong (Truyện chữ)</label>
                                <select id="temply-tone" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none text-sm bg-slate-50">
                                    <option value="Lãng mạn">Lãng mạn, miêu tả chi tiết cảm xúc</option>
                                    <option value="Kịch tính">Kịch tính, dồn dập, giật gân</option>
                                    <option value="Hài hước">Hài hước, sảng văn, nhẹ nhàng</option>
                                    <option value="U tối">U tối, bí hiểm, nặng nề tâm lý</option>
                                </select>
                            </div>
                            
                            <div id="art-group" class="hidden">
                                <label class="block text-sm font-semibold text-slate-700 mb-2">Nét Vẽ (Truyện tranh)</label>
                                <select id="temply-art" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none text-sm bg-slate-50">
                                    <option value="Manga">Manga Đen trắng Nhật Bản</option>
                                    <option value="Anime">Anime 90s Cổ Điển</option>
                                    <option value="Webtoon">Digital Webtoon full màu siêu đẹp</option>
                                    <option value="Chibi">Chibi dễ thương hài hước</option>
                                    <option value="Dark Fantasy">Dark Fantasy u ám, đáng sợ</option>
                                </select>
                            </div>
                            
                            <script>
                                document.getElementById("temply-mode").addEventListener("change", function(e) {
                                    if(e.target.value === "comic") {
                                        document.getElementById("tone-group").classList.add("hidden");
                                        document.getElementById("art-group").classList.remove("hidden");
                                    } else {
                                        document.getElementById("tone-group").classList.remove("hidden");
                                        document.getElementById("art-group").classList.add("hidden");
                                    }
                                });
                            </script>
"""
# We replace the old tone select and the num chapters with this new block.
# Actually, I'll regex replace the whole section from `<label class="block text-sm font-semibold text-slate-700 mb-2">Văn phong</label>` to before `<label class="block text-sm font-semibold text-slate-700 mb-2">Từ khóa / Yếu tố / Hook</label>`
pattern = re.compile(r'<div>\s*<label class="block text-sm font-semibold text-slate-700 mb-2">Văn phong</label>.*?</div>\s*<div>\s*<label class="block text-sm font-semibold text-slate-700 mb-2">Số lượng Chương</label>.*?</select>\s*</div>', re.DOTALL)
# Wait, I already added num-chapters in a separate `<div>`. Let's just find exactly what to replace.
admin_ui = re.sub(
    r'(<label class="block text-sm font-semibold text-slate-700 mb-2">Văn phong</label>.*?</select>\s*</div>\s*<div>\s*<label class="block text-sm font-semibold text-slate-700 mb-2">Số lượng Chương</label>.*?</input>\s*</div>)', 
    replacement_html, 
    admin_ui, flags=re.DOTALL
)

# Oh wait, the layout in admin-ui.php currently is:
# <div>
#     <label class="block text-sm font-semibold text-slate-700 mb-2">Văn phong</label>
#     <select id="temply-tone"...>...</select>
# </div>
# <div>
#     <label class="block text-sm font-semibold text-slate-700 mb-2">Số lượng Chương</label>
#     <input id="temply-num-chapters"... />
# </div>

# A simpler approach: use split and replace!
parts = admin_ui.split("<div>\n                                <label class=\"block text-sm font-semibold text-slate-700 mb-2\">Văn phong</label>")
if len(parts) == 2:
    part2 = parts[1].split("<div>\n                                <label class=\"block text-sm font-semibold text-slate-700 mb-2\">Từ khóa", 1)
    admin_ui = parts[0] + replacement_html + "\n                            <div>\n                                <label class=\"block text-sm font-semibold text-slate-700 mb-2\">Từ khóa" + part2[1]

with open("temply-ai-factory/admin-ui.php", "w", encoding="utf-8") as f:
    f.write(admin_ui)


# 2. Update agentic-workflow.js
with open("temply-ai-factory/assets/agentic-workflow.js", "r", encoding="utf-8") as f:
    js = f.read()

# Add mode and art extraction
js = js.replace("const tone = $('#temply-tone').val();", "const tone = $('#temply-tone').val();\n        const mode = $('#temply-mode').val();\n        const art = $('#temply-art').val();\n        const comicSeed = Math.floor(Math.random() * 1000000);")

# Change write_chapter AJAX router logic based on mode
js = js.replace("action: 'temply_step_write_chapter', nonce: temply_ai_ajax.nonce,", 
"""action: mode === 'comic' ? 'temply_step_write_comic_chapter' : 'temply_step_write_chapter', 
nonce: temply_ai_ajax.nonce,
mode: mode, art: art, seed: comicSeed,""")

with open("temply-ai-factory/assets/agentic-workflow.js", "w", encoding="utf-8") as f:
    f.write(js)

# 3. Update openai-api.php
with open("temply-ai-factory/includes/openai-api.php", "r", encoding="utf-8") as f:
    php = f.read()

# Inject Step 4b (Comic Storyboarder & Artist)
comic_php = """

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

    if(!$truyen_id) wp_send_json_error(['message' => 'Mất ID Truyện.']);

    $system_prompt = "Bạn là THE COMIC STORYBOARDER (Đạo diễn truyện tranh Webtoon cực đỉnh). Hãy chia tóm tắt truyền vào thành 4 đến 6 Panel (khung hình). Mỗi panel yêu cầu 1 câu tiếng Anh Prompt mô tả hình ảnh cực kỳ chi tiết chuẩn xác nhân vật và hành động để vẽ ảnh, và mảng Text Tiếng Việt là Lời Thoại của các nhân vật.
    KHÔNG THÊM BẤT KỲ TEXT THỪA NÀO. BẮT BUỘC TRẢ VỀ CHUỖI MẢNG JSON NHƯ SAU:
    [
      {
         \"prompt\": \"A young man in black suit laughing wickedly, luxury office background...\",
         \"dialogues\": [\"Chủ tịch, tiểu thư đã tới!\", \"Để cô ta đợi ở ngoài!\"]
      },
      ...
    ]";

    $user_prompt = "Hãy rã chi tiết Chương $chap_num dành cho Thể loại $genre, nét vẽ $art, dựa theo tóm tắt:\n$summary\n\nTạo 6 panels JSON. Lời thoại (dialogues) phải sắc bén, mang đặc trưng thể loại.";

    $response = temply_call_openai($system_prompt, $user_prompt, 0.8);
    $clean_json = preg_replace('/```json|```/', '', $response);
    $panels = json_decode(trim($clean_json), true);

    if(!is_array($panels)) wp_send_json_error(['message' => 'Lỗi Parse JSON Webtoon.']);

    $html_content = '<style>
    .comic-container { max-width: 600px; margin: 0 auto; background: #fff; border-left: 2px solid #000; border-right: 2px solid #000; padding: 20px 0; }
    .comic-panel { position: relative; width: 100%; border-bottom: 5px solid #fff; border-top: 5px solid #fff; background: #eee; overflow: hidden; }
    .comic-panel img { width: 100%; height: auto; display: block; object-fit: cover; }
    .bubbles-layer { position: absolute; inset: 0; padding: 15px; display: flex; flex-direction: column; justify-content: space-between; pointer-events: none; }
    .bubble { background: rgba(255,255,255,0.96); border: 2px solid #111; border-radius: 12px; padding: 8px 12px; font-weight: 700; font-size: 15px; color: #111; font-family: sans-serif; max-width: 75%; align-self: flex-start; margin-bottom: 15px; box-shadow: 3px 3px 0 #111; position: relative; line-height: 1.4; pointer-events: auto; }
    .bubble.right { align-self: flex-end; }
    .bubble::after { content: ""; position: absolute; bottom: -8px; left: 15px; border-width: 8px 8px 0; border-style: solid; border-color: #111 transparent transparent transparent; }
    .bubble.right::after { left: auto; right: 15px; }
    </style>
    <div class="comic-container">';

    foreach($panels as $idx => $p) {
        $prmpt = $p['prompt'] ?? '';
        if(empty($prmpt)) continue;
        
        $escaped_prompt = urlencode($prmpt . ", style of " . $art . ", highly detailed, expressive manga illustration art, masterpiece");
        $img_url = "https://image.pollinations.ai/prompt/" . $escaped_prompt . "?width=600&height=500&seed=" . $seed . "&nologo=true";

        // Tải ảnh về host để lưu vĩnh viễn (nếu muốn) hoặc dùng link trực tiếp để tiết kiệm host
        // Ở đây dùng thẻ img trực tiếp (Hotlink API) để tốc độ tạo truyện nhanh như điện xẹt
        
        $html_content .= '<div class="comic-panel">';
        $html_content .= '<img src="' . esc_attr($img_url) . '" alt="Cảnh truyện ' . $chap_num . ' panel ' . $idx . '" loading="lazy" />';
        
        if(!empty($p['dialogues']) && is_array($p['dialogues'])) {
            $html_content .= '<div class="bubbles-layer">';
            foreach($p['dialogues'] as $d_idx => $dialogue) {
                // Đảo trái phải ảo diệu
                $pos = ($d_idx % 2 == 0) ? '' : ' right';
                // Đẩy vị trí lên đầu hoặc cuối ngẫu nhiên bằng Flex
                $align = ($d_idx == 0) ? 'margin-top: 5px;' : 'margin-top: auto; margin-bottom: 5px;';
                $html_content .= '<div class="bubble' . $pos . '" style="' . $align . '">' . esc_html($dialogue) . '</div>';
            }
            $html_content .= '</div>';
        }
        
        $html_content .= '</div>';
    }

    $html_content .= '</div>';

    $post_id = wp_insert_post([
        'post_title'   => "Chương $chap_num",
        'post_content' => $html_content,
        'post_status'  => 'draft',
        'post_type'    => 'chuong',
        'post_author'  => get_current_user_id()
    ]);

    if(is_wp_error($post_id)) wp_send_json_error(['message' => 'Lỗi tạo Chương Comic.']);
    update_post_meta($post_id, '_truyen_id', $truyen_id);

    wp_send_json_success([
        'chuong_id' => $post_id,
        'title' => "Chương $chap_num"
    ]);
}
"""

php = php + comic_php

with open("temply-ai-factory/includes/openai-api.php", "w", encoding="utf-8") as f:
    f.write(php)

print("Created Comic Mode!")
