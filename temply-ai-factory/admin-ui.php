<?php
if (!defined('ABSPATH')) exit;

function temply_ai_render_admin_page() {
    // Get existing key
    $openai_key = get_option('temply_openai_api_key', '');
    $gemini_key = get_option('temply_gemini_api_key', '');
    $claude_key = get_option('temply_claude_api_key', '');
    
    // Save key if submitted
    if (isset($_POST['temply_submit_key']) && check_admin_referer('temply_save_key')) {
        $openai_key = sanitize_text_field($_POST['temply_openai_api_key']);
        $gemini_key = sanitize_text_field($_POST['temply_gemini_api_key']);
        $claude_key = sanitize_text_field($_POST['temply_claude_api_key']);
        update_option('temply_openai_api_key', $openai_key);
        update_option('temply_gemini_api_key', $gemini_key);
        update_option('temply_claude_api_key', $claude_key);
        echo '<div class="notice notice-success is-dismissible"><p>Đã lưu cấu hình API Key thiên hà!</p></div>';
    }
    ?>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet" />
    <script defer src="https://cdn.tailwindcss.com"></script>
    <div class="wrap" style="margin: 0; padding: 20px; background: #f3f4f6; min-height: 100vh;">
        <div class="max-w-[1600px] w-full mx-auto">
            
            <div class="flex items-center gap-4 mb-8">
                <div class="w-12 h-12 bg-blue-600 rounded-xl flex items-center justify-center shadow-lg text-white font-bold text-2xl">
                    T
                </div>
                <div>
                    <h1 class="text-3xl font-extrabold text-slate-800 tracking-tight" style="margin:0">Temply AI Story Factory</h1>
                    <p class="text-slate-500 font-medium">Multi-step Agentic Workflow powered by GPT-4o-mini</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                
                <!-- Left: Control Panel -->
                <div class="md:col-span-1 space-y-6">
                    
                    <!-- API Key Settings -->
                    <details class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 group mb-6">
                        <summary class="text-lg font-bold text-slate-800 cursor-pointer flex items-center justify-between list-none outline-none">
                            Cấu hình Hệ thống (API Key)
                            <span class="transform transition-transform group-open:-rotate-180">
                                <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </span>
                        </summary>
                        <div class="mt-4 pt-4 border-t border-slate-100">
                            <form method="POST">
                                <?php wp_nonce_field('temply_save_key'); ?>
                                <label class="block text-sm font-semibold text-slate-700 mb-2">OpenAI API Key (GPT-4o-mini)</label>
                                <input type="password" name="temply_openai_api_key" value="<?php echo esc_attr($openai_key); ?>" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all mb-4 text-sm" placeholder="sk-proj-...">
                                
                                <label class="block text-sm font-semibold text-slate-700 mb-2">Google Gemini API Key (2.5 Flash)</label>
                                <input type="password" name="temply_gemini_api_key" value="<?php echo esc_attr($gemini_key); ?>" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-all mb-4 text-sm" placeholder="AIzaSy...">
                                
                                <label class="block text-sm font-semibold text-slate-700 mb-2">Anthropic Claude API Key (3.5 Sonnet)</label>
                                <input type="password" name="temply_claude_api_key" value="<?php echo esc_attr($claude_key); ?>" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 outline-none transition-all mb-4 text-sm" placeholder="sk-ant-...">
                                
                                <button type="submit" name="temply_submit_key" class="w-full bg-slate-800 hover:bg-slate-900 text-white font-semibold py-2 px-4 rounded-lg transition-colors text-sm">💾 Lưu Trữ Chìa Khoá</button>
                            </form>
                        </div>
                    </details>

                    <!-- Creation Form -->
                    <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 relative overflow-hidden">
                        <?php if(empty($openai_key) && empty($gemini_key)): ?>
                            <div class="absolute inset-0 bg-white/80 backdrop-blur-sm z-10 flex flex-col items-center justify-center p-6 text-center">
                                <p class="text-red-500 font-bold mb-2">Hết Nguyên Liệu Mở Cửa (Chưa Cài Key)</p>
                                <p class="text-sm text-slate-500">Vui lòng nhập ít nhất 1 Key (OpenAI hoặc Gemini) ở cột bên trái để khai mở lò luyện linh đen.</p>
                            </div>
                        <?php endif; ?>
                        
                        <h2 class="text-lg font-bold text-slate-800 mb-4 pb-2 border-b border-slate-100 flex items-center justify-between">
                            Cỗ Máy Tạo Truyện
                        </h2>
                        
                        <div class="mb-6 p-4 bg-teal-50 border border-teal-100 rounded-xl">
                            <div class="flex items-center justify-between mb-2">
                                <label class="block text-sm font-bold text-teal-800">🪄 Phóng Tác (Clone) Truyện</label>
                                <button id="temply-analyze-source-btn" type="button" class="text-xs flex items-center gap-1 bg-teal-600 text-white px-3 py-1.5 rounded-md hover:bg-teal-700 transition-colors font-medium border border-teal-700 shadow-sm">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path></svg>
                                    Phân tích & Tự điền Form
                                </button>
                            </div>
                            <p class="text-xs text-teal-600 mb-3">Copy toàn bộ nội dung (tóm tắt, hoặc rải rác vài chương) của truyện khác vào đây để AI tự động cấu hình lại thể loại, văn phong và bối cảnh cho bạn.</p>
                            <textarea id="temply-source-text" rows="4" class="w-full px-4 py-2 border border-teal-200 rounded-lg focus:ring-2 focus:ring-teal-500 outline-none text-sm bg-white placeholder-teal-300" placeholder="Trích đoạn truyện nguồn..."></textarea>
                        </div>
                        
                        <div class="space-y-4" id="temply-form">
                            <div>
                                <label class="block text-sm font-bold text-indigo-700 mb-2">Bộ Não Sinh Trưởng (Mô Hình AI)</label>
                                <select id="temply-ai-model" class="w-full px-4 py-2 border border-indigo-200 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none text-sm bg-indigo-50 font-semibold shadow-sm">
                                    <option value="gemini" selected>🌌 Google Gemini (2.5 Flash) - Siêu Tốc & Bay Bổng</option>
                                    <option value="claude">🧠 Anthropic Claude (Sonnet 4.6) - Đỉnh Cao Văn Học</option>
                                    <option value="openai">🦅 OpenAI (GPT-4o-mini) - Hành văn sắc gọn</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-sm font-semibold text-slate-700 mb-2">Thể loại</label>
                                <select id="temply-genre" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none text-sm bg-slate-50">
                                    <option value="Drama">Drama (Cẩu huyết, Gia đấu, Vả mặt)</option>
                                    <option value="Tâm Lý Xã Hội">Tâm Lý Xã Hội (Mâu thuẫn gia đình, bóc phốt)</option>
                                    <option value="Đô Thị Thực Tế">Đô Thị Thực Tế (Bình dân, không hệ thống/tổng tài)</option>
                                    <option value="Trọng sinh">Trọng sinh</option>
                                    <option value="Tổng tài">Tổng tài</option>
                                    <option value="Xuyên không">Xuyên không</option>
                                    <option value="Tu tiên">Tu tiên</option>
                                    <option value="Ngôn tình đô thị">Ngôn tình đô thị</option>
                                    <option value="Kinh dị Việt Nam">Kinh dị Việt Nam</option>
                                    <option value="Sảng Văn">Sảng Văn (Nhịp siêu tốc, cực thỏa mãn)</option>
                                    <option value="Vả Mặt">Vả Mặt (Giấu thân phận, kẻ thù quỳ lạy)</option>
                                    <option value="Giả Heo Ăn Thịt Hổ">Giả Heo Ăn Thịt Hổ (Giả ngốc lừa thù)</option>
                                    <option value="Đô Thị Ẩn Thân">Đô Thị Ẩn Thân / Hào Môn Thế Gia</option>
                                </select>
                            </div>
                            
                            
                            <div class="grid grid-cols-3 gap-3 mb-4">
                                <div class="col-span-3 lg:col-span-1">
                                    <label class="block text-sm font-semibold text-slate-700 mb-2">Định dạng</label>
                                    <select id="temply-mode" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none text-sm bg-slate-50 font-bold text-blue-700">
                                        <option value="text">📖 Truyện Chữ</option>
                                        <option value="comic">🎨 Truyện Tranh</option>
                                    </select>
                                </div>
                                <div>
                                    <label class="block text-sm font-semibold text-slate-700 mb-2" title="Số chương của 1 bộ truyện (Để Auto để AI tự co giãn)">Số Chương</label>
                                    <input type="text" id="temply-num-chapters" value="Auto" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none text-sm bg-slate-50 text-center font-bold text-blue-600" title="Gõ số (VD: 12) hoặc để 'Auto' cho AI tự cân đối">
                                </div>
                                <div>
                                    <label class="block text-sm font-semibold text-slate-700 mb-2 text-rose-600" title="Số bộ truyện liên tiếp đúc tự động">🔥 Auto-Pilot</label>
                                    <input type="number" id="temply-batch-size" min="1" max="20" value="1" class="w-full px-4 py-2 border border-rose-200 rounded-lg focus:ring-2 focus:ring-rose-500 outline-none text-sm bg-rose-50 text-rose-700 text-center font-bold">
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

                            <div>
                                <div class="flex items-center justify-between mb-2">
                                    <label class="block text-sm font-semibold text-slate-700">Từ khóa / Yếu tố / Hook</label>
                                    <button id="temply-brainstorm-btn" type="button" class="text-xs flex items-center gap-1 bg-purple-100 text-purple-700 px-2 py-1 rounded hover:bg-purple-200 transition-colors font-medium border border-purple-200">
                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                                        Brainstorm AI
                                    </button>
                                </div>
                                <textarea id="temply-keywords" rows="3" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none text-sm bg-slate-50" placeholder="Ví dụ: Nữ chính bị phản bội, hệ thống báo thù 100 ngày..."></textarea>
                                
                                <!-- Thêm Box World Building -->
                                <div class="mt-4">
                                    <div class="flex items-center justify-between mb-2">
                                        <label class="block text-sm font-semibold text-slate-700">Bối Cảnh & Thế Giới (World Building)</label>
                                        <button id="temply-brainstorm-world-btn" type="button" class="text-xs flex items-center gap-1 bg-purple-100 text-purple-700 px-2 py-1 rounded hover:bg-purple-200 transition-colors font-medium border border-purple-200">
                                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                                            Brainstorm AI
                                        </button>
                                    </div>
                                    <textarea id="temply-world-building" rows="4" class="w-full px-4 py-2 border border-purple-200 rounded-lg focus:ring-2 focus:ring-purple-500 outline-none text-sm bg-purple-50/30" placeholder="Copy và Paste quy luật hệ thống, tông màu văn hoá, thiết lập triều đại hoặc phong cách Á Đông... vào đây. AI sẽ dùng nó làm core rules để viết truyện."></textarea>
                                </div>
                                
                                <div id="brainstorm-world-results" class="hidden mt-2 border border-purple-200 bg-purple-50 rounded-lg p-3">
                                    <div class="text-xs font-semibold text-purple-800 mb-2 flex items-center justify-between">
                                        <span>✨ Bấm vào 1 Ý Tưởng Thế Giới dưới đây để nạp:</span>
                                    </div>
                                    <div id="brainstorm-world-list" class="space-y-2"></div>
                                </div>
                                
                                <div id="brainstorm-results" class="hidden mt-2 border border-purple-200 bg-purple-50 rounded-lg p-3">
                                    <div class="text-xs font-semibold text-purple-800 mb-2 flex items-center justify-between">
                                        <span>✨ Bấm vào Ý Tưởng bạn thích để nạp vào Từ Khoá gốc:</span>
                                    </div>
                                    <div id="brainstorm-list" class="space-y-2"></div>
                                </div>
                                <div class="mt-3">
                                    <label class="block text-xs font-medium text-slate-500 mb-2">🔥 Gợi ý Yếu tố Hot (Bấm để thêm):</label>
                                    <div class="flex flex-wrap gap-2" id="hook-suggestions">
                                        <span class="px-2 py-1 bg-amber-50 text-amber-700 border border-amber-200 rounded text-[11px] font-semibold cursor-pointer hover:bg-amber-600 hover:text-white transition-colors" onclick="addHook(this)">Giả nghèo thử lòng bị khinh</span>
                                        <span class="px-2 py-1 bg-rose-50 text-rose-700 border border-rose-200 rounded text-[11px] font-semibold cursor-pointer hover:bg-rose-600 hover:text-white transition-colors" onclick="addHook(this)">Trùng sinh vào vai phản diện</span>
                                        <span class="px-2 py-1 bg-blue-50 text-blue-700 border border-blue-200 rounded text-[11px] font-semibold cursor-pointer hover:bg-blue-600 hover:text-white transition-colors" onclick="addHook(this)">Hệ thống phát tiền cực vô lý</span>
                                        <span class="px-2 py-1 bg-emerald-50 text-emerald-700 border border-emerald-200 rounded text-[11px] font-semibold cursor-pointer hover:bg-emerald-600 hover:text-white transition-colors" onclick="addHook(this)">Vả mặt tiểu tam trà xanh</span>
                                        <span class="px-2 py-1 bg-purple-50 text-purple-700 border border-purple-200 rounded text-[11px] font-semibold cursor-pointer hover:bg-purple-600 hover:text-white transition-colors" onclick="addHook(this)">Game hàng phủ thành hiện thực</span>
                                        <span class="px-2 py-1 bg-slate-100 text-slate-700 border border-slate-200 rounded text-[11px] font-semibold cursor-pointer hover:bg-slate-800 hover:text-white transition-colors" onclick="addHook(this)">Bị đuổi khỏi nhà sau đó lột xác</span>
                                    </div>
                                </div>
                                <script>
                                    function addHook(el) {
                                        let ta = document.getElementById('temply-keywords');
                                        ta.value = ta.value ? ta.value + ', ' + el.innerText : el.innerText;
                                    }
                                    function addWorld(el) {
                                        let ta = document.getElementById('temply-world-building');
                                        ta.value = el.innerText;
                                    }
                                </script>
                                
                                <div class="mt-4 hidden" id="source-comments-group">
                                    <label class="block text-sm font-semibold text-rose-700 mb-2">💬 Danh sách Comment Gốc (Tự động cào được):</label>
                                    <p class="text-xs text-rose-500 mb-2">Hệ thống phát hiện có User chửi lộn / hóng hớt trong Text của bạn. Vua Ma Mì sẽ nạp đạn y xì đúc đống này vào đáy bài viết.</p>
                                    <textarea id="temply-source-comments" rows="3" class="w-full px-4 py-2 border border-rose-300 rounded-lg focus:ring-2 focus:ring-rose-500 outline-none text-[12px] bg-rose-50 text-rose-900" placeholder="Danh sách bình luận gốc của mạng xã hội..."></textarea>
                                </div>
                            </div>

                            <div class="mt-4 bg-yellow-50 border border-yellow-200 p-3 rounded-lg mb-4 flex items-start gap-3">
                                <input type="checkbox" id="temply-pause-outline" class="mt-1 flex-shrink-0" checked>
                                <div>
                                    <label for="temply-pause-outline" class="font-bold text-yellow-800 text-sm cursor-pointer">Trạm Kiểm Duyệt Dàn Ý (Human-in-the-loop)</label>
                                    <p class="text-[11px] text-yellow-700 leading-snug mt-1">Hệ thống sẽ TẠM DỪNG sau bước "Sáng tác Dàn ý" và chờ bạn chỉnh sửa, thêm bớt diễn biến cho từng chương trước khi chính thức Viết Text và Xuất ảnh.</p>
                                </div>
                            </div>

                            <button id="temply-start-btn" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded-xl transition-all shadow-lg hover:shadow-blue-600/30 flex items-center justify-center gap-2 mt-2">
                                <span class="material-symbols-outlined">rocket_launch</span>
                                Bắt Đầu Đúc Truyện
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Outline Review Box (Hidden by default) -->
                <div id="temply-outline-reviewer" class="hidden fixed inset-0 bg-slate-900/80 backdrop-blur-sm z-[99] flex items-center justify-center p-4">
                    <div class="bg-white rounded-2xl shadow-2xl w-full max-w-4xl max-h-[90vh] flex flex-col overflow-hidden border border-slate-200">
                        <div class="px-6 py-4 border-b border-slate-100 bg-slate-50 flex justify-between items-center bg-gradient-to-r from-blue-50 to-indigo-50">
                            <div>
                                <h3 class="text-xl font-bold text-slate-800 flex items-center gap-2"><span class="material-symbols-outlined text-blue-600">edit_note</span> Trạm Kiểm Duyệt Dàn Ý</h3>
                                <p class="text-sm text-slate-500">Mô hình AI đã thiết kế xong kịch bản cho các chương. Hãy xem lại và chỉnh sửa nội dung bên dưới.</p>
                            </div>
                            <button id="close-outline-reviewer" class="text-slate-400 hover:text-slate-700 flex items-center justify-center p-2 rounded-full hover:bg-slate-200 transition-colors">
                                <span class="material-symbols-outlined">close</span>
                            </button>
                        </div>
                        
                        <div id="temply-outline-list" class="p-6 overflow-y-auto flex-grow space-y-6 bg-slate-50 relative">
                            <!-- JS Will Render Outline Cards Here -->
                        </div>
                        
                        <div class="px-6 py-4 border-t border-slate-100 bg-white flex justify-between items-center gap-3 shadow-[0_-10px_20px_-10px_rgba(0,0,0,0.05)] relative z-10">
                            <button id="add-chapter-btn" class="bg-white border border-slate-300 hover:bg-slate-50 text-slate-700 font-semibold px-6 py-3 rounded-xl shadow-sm transition-all flex items-center gap-2">
                                <span class="material-symbols-outlined text-slate-500">add_circle</span>
                                THÊM CHƯƠNG MỚI
                            </button>
                            <button id="temply-resume-btn" class="bg-gradient-to-r from-blue-600 to-indigo-600 hover:to-indigo-500 text-white font-bold px-8 py-3 rounded-xl shadow-lg shadow-blue-500/30 hover:shadow-blue-500/50 transition-all flex items-center gap-2 transform hover:-translate-y-0.5">
                                <span class="material-symbols-outlined">play_circle</span>
                                CHỐT DÀN Ý & BẮT ĐẦU VIẾT TRUYỆN
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Right: Terminal Console -->
                <div class="md:col-span-2">
                    <div class="bg-slate-900 rounded-2xl shadow-xl border border-slate-800 overflow-hidden flex flex-col h-full min-h-[500px]">
                        <!-- Terminal Header -->
                        <div class="bg-slate-800 px-4 py-3 flex items-center gap-2 border-b border-slate-700">
                            <div class="w-3 h-3 rounded-full bg-red-500"></div>
                            <div class="w-3 h-3 rounded-full bg-yellow-500"></div>
                            <div class="w-3 h-3 rounded-full bg-green-500"></div>
                            <span class="ml-4 text-xs font-mono text-slate-400">Agentic Action Terminal</span>
                            
                            <div id="temply-loader" class="ml-auto hidden">
                                <svg class="animate-spin h-4 w-4 text-blue-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                </svg>
                            </div>
                        </div>
                        
                        <!-- Terminal Context -->
                        <div id="temply-console" class="p-6 font-mono text-sm flex-grow overflow-y-auto space-y-3" style="max-height: 600px;">
                            <div class="text-green-400">> System Ready. Waiting for Oracle init...</div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Magic Text-to-Comic Converter Card -->
            <div class="mt-8 bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                <h2 class="text-xl font-bold text-slate-800 mb-2 flex items-center gap-2">
                    🪄 Pháp Bảo: Hóa Phàm Thành Tiên (Text to Comic)
                </h2>
                <p class="text-sm text-slate-500 mb-6">Chọn một bộ truyện chữ có sẵn trên hệ thống của bạn để siêu máy tính AI phân rã nội dung, tự đạo diễn kịch bản Manga và sinh ra ảnh ghép thành 1 bộ truyện tranh Comic hoàn toàn mới.</p>
                
                <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
                    <div class="col-span-2">
                        <label class="block text-sm font-semibold text-slate-700 mb-2">Chọn truyện chữ làm Gốc rễ:</label>
                        <select id="temply-magic-source-truyen" class="w-full px-4 py-3 border border-indigo-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none text-sm bg-indigo-50 font-semibold shadow-sm">
                            <?php
                            $truyens = get_posts(['post_type'=>'truyen', 'posts_per_page'=>50, 'post_status'=>'publish']);
                            foreach($truyens as $t) {
                                echo '<option value="'.esc_attr($t->ID).'">'.esc_html($t->post_title).'</option>';
                            }
                            ?>
                        </select>
                    </div>
                    
                    <div class="col-span-1">
                        <label class="block text-sm font-semibold text-slate-700 mb-2">Độ dài Panel ảnh:</label>
                        <select id="temply-magic-num-panels" class="w-full px-4 py-3 border border-orange-200 rounded-xl focus:ring-2 focus:ring-orange-500 outline-none text-sm bg-orange-50 font-semibold shadow-sm">
                            <option value="6-10">Tóm gọn (6-10 ảnh)</option>
                            <option value="12-18" selected>Vừa phải (12-18 ảnh)</option>
                            <option value="20-25">Chi tiết (20-25 ảnh)</option>
                        </select>
                    </div>
                    
                    <div class="col-span-1 flex items-end">
                        <button id="temply-magic-convert-btn" type="button" class="w-full bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white font-bold h-[46px] rounded-xl shadow-lg transition-all flex items-center justify-center gap-2">
                            <svg class="w-5 h-5 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path></svg>
                            Manga Hóa!
                        </button>
                    </div>
                </div>
            </div>

        </div>
    </div>
    <?php
}
