<?php
if (!defined('ABSPATH')) exit;

function temply_ai_render_mobile_page() {
    if (!current_user_can('manage_options')) {
        return '<div class="p-6 bg-red-50 text-red-600 rounded-xl font-bold">Khu vực mật! Vui lòng truy cập bằng tài khoản Admin.</div>';
    }
    
    ob_start();
    ?>
    <style>
    .temply-mobile-app { font-family: 'Inter', system-ui, -apple-system, sans-serif; }
    .temply-input-glass { background: rgba(255,255,255,0.9); backdrop-filter: blur(10px); border: 1px solid rgba(0,0,0,0.05); box-shadow: inset 0 2px 4px rgba(0,0,0,0.02); }
    .temply-btn-magic { background: linear-gradient(135deg, #1e293b, #0f172a); box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.5); }
    .temply-header-bg { background: linear-gradient(135deg, #2563eb, #4f46e5); position: relative; overflow: hidden; }
    .temply-header-bg::after { content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%); transform: rotate(30deg); pointer-events: none; }
    </style>
    
    <div class="temply-mobile-app w-full max-w-md mx-auto bg-slate-50 shadow-2xl rounded-[2rem] overflow-hidden flex flex-col relative mt-6 mb-12 border border-slate-200" style="min-h: 80vh;">
        <!-- App Header -->
        <div class="temply-header-bg p-8 text-white shrink-0 shadow-md z-10">
            <h2 class="text-3xl font-extrabold tracking-tight mb-2 drop-shadow-md flex items-center justify-center gap-2">
                <span class="text-3xl">✨</span> Magic Creator
            </h2>
            <p class="text-blue-100 text-sm opacity-95 text-center font-medium leading-relaxed">
                Biến drama, cốt truyện thô thành tiểu thuyết hoàn chỉnh tự động.
            </p>
        </div>

        <!-- App Body -->
        <div class="p-6 flex flex-col gap-5 overflow-y-auto bg-slate-50 flex-1 z-0 relative">
            <!-- decorative background circle -->
            <div class="absolute top-0 right-0 w-64 h-64 bg-blue-100 rounded-full blur-3xl opacity-50 -z-10 -translate-y-1/2 translate-x-1/2"></div>
            
            <div class="flex flex-col gap-2">
                <label class="text-sm font-bold text-slate-700 flex items-center gap-2"><span class="bg-indigo-100 text-indigo-600 p-1.5 rounded-lg text-xs leading-none">🧠</span> Mô Hình Trí Tuệ (AI)</label>
                <select id="mobile-ai-model" class="temply-input-glass w-full px-4 py-3.5 rounded-xl focus:ring-2 focus:ring-blue-500 font-semibold text-slate-800 outline-none transition-all cursor-pointer">
                    <option value="gemini" selected>⚡️ Google Gemini (2.5 Flash) - Tốc độ cao</option>
                    <option value="claude">🧠 Anthropic Claude (3.5 Sonnet) - Cân Tác Phẩm</option>
                    <option value="openai">🦅 OpenAI (GPT-4o) - Hành văn sắc bén</option>
                </select>
            </div>

            <div class="flex-1 flex flex-col gap-2 min-h-[35vh]">
                <label class="text-sm font-bold text-slate-700 flex items-center gap-2"><span class="bg-rose-100 text-rose-600 p-1.5 rounded-lg text-xs leading-none">🎭</span> Cốt truyện / Nội dung thô</label>
                <textarea id="mobile-source-text" class="temply-input-glass w-full flex-1 p-4 rounded-xl focus:ring-2 focus:ring-blue-500 resize-none text-sm text-slate-800 outline-none transition-all leading-relaxed" placeholder="Dán nội dung drama, bài phốt hoặc tóm tắt vào đây. Ví dụ: Sáng nay đang đánh răng thì anh người yêu đá mỏ khoét gõ cửa đòi chia tay..."></textarea>
            </div>
            
            <div id="mobile-source-comments-group" class="hidden flex-col gap-2 mt-2">
                <label class="text-sm font-bold text-rose-700">💬 Comment Gốc Bóc Được</label>
                <textarea id="mobile-source-comments" class="w-full bg-rose-50 border border-rose-200 text-[12px] p-3 rounded-xl text-rose-900" rows="3"></textarea>
            </div>
            
            <div id="mobile-status-box" class="hidden flex-col items-center justify-center py-8 bg-white/80 backdrop-blur-md rounded-2xl border border-blue-100 shadow-lg mt-2">
                <div class="animate-spin mb-4">
                    <svg class="w-10 h-10 text-blue-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                </div>
                <div id="mobile-status-text" class="text-sm font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600 animate-pulse text-center px-6">Hệ thống đang khởi động...</div>
            </div>
            
            <div id="mobile-result-box" class="hidden p-5 bg-gradient-to-br from-green-50 to-emerald-50 border border-green-200 rounded-2xl flex flex-col items-center gap-3 mt-2 shadow-sm text-center">
                <div id="temply-magic-result" class="hidden mt-6 bg-green-50 border border-green-200 rounded-xl p-4 flex-col items-center justify-center text-center">
                    <span class="material-symbols-outlined text-green-500 text-4xl mb-2">check_circle</span>
                    <p class="text-green-800 font-bold mb-2">Truyện đã hóa thần thành công!</p>
                    <a id="temply-result-link" href="#" target="_blank" class="px-6 py-2 bg-green-600 text-white rounded-full font-bold shadow-md hover:bg-green-700 transition">Mở Trang Quản Trị Truyện</a>
                </div>
                
                <!-- Trạm Kiểm Duyệt Dàn Ý -->
                <div id="temply-mobile-outline-reviewer" class="hidden fixed inset-0 bg-slate-900/90 z-[999] flex-col h-[100dvh] w-screen">
                    <div class="px-4 py-4 bg-white flex justify-between items-center shadow-sm">
                        <div>
                            <h3 class="font-bold text-slate-800 text-lg flex items-center gap-1">
                                <span class="material-symbols-outlined text-blue-600">edit_note</span> Duyệt Dàn Ý
                            </h3>
                        </div>
                    </div>
                    <div id="temply-mobile-outline-list" class="flex-grow overflow-y-auto p-4 space-y-4 bg-slate-50 pb-24">
                        <!-- JS render -->
                    </div>
                    <div class="absolute bottom-0 w-full p-4 bg-white border-t border-slate-200">
                        <button id="temply-mobile-resume-btn" class="w-full bg-blue-600 text-white font-bold py-3 rounded-xl shadow-lg flex items-center justify-center gap-2">
                            <span class="material-symbols-outlined">play_circle</span> CHỐT & VIẾT TRUYỆN
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- App Footer (Sticky Button) -->
        <div class="p-5 bg-white border-t border-slate-200 shrink-0 z-10 shadow-[0_-10px_20px_rgba(0,0,0,0.02)] relative">
            <button id="mobile-start-btn" type="button" class="temply-btn-magic w-full text-white font-extrabold text-lg py-4 px-6 rounded-2xl active:scale-[0.98] transition-all outline-none flex items-center justify-center gap-2 cursor-pointer">
                <span class="text-xl relative -top-[1px]">🚀</span> KÍCH HOẠT MAGIC!
            </button>
        </div>
    </div>

    <script>
        const temply_mobile_ajax = {
            url: "<?php echo admin_url('admin-ajax.php'); ?>",
            nonce: "<?php echo wp_create_nonce('temply_ai_nonce'); ?>"
        };
    </script>
    <script>
    (function() {
        let aiModel, state = {};
        const MAX_CHAPTERS = 4; // Render 4 chapters max to avoid hanging phone too long
        
        const btn = document.getElementById('mobile-start-btn');
        const statusBox = document.getElementById('mobile-status-box');
        const statusText = document.getElementById('mobile-status-text');
        const resultBox = document.getElementById('mobile-result-box');
        const resultLink = document.getElementById('mobile-result-link');
        const sourceTextEl = document.getElementById('mobile-source-text');
        const aiModelEl = document.getElementById('mobile-ai-model');
        
        if (!btn) return; // Prevent errors if DOM is incomplete

        function updateStatus(msg) { statusText.textContent = msg; }
        
        function failWorkflow(msg) {
            statusBox.classList.add('hidden');
            statusBox.classList.remove('flex');
            btn.disabled = false;
            btn.classList.remove('opacity-50', 'cursor-not-allowed');
            btn.textContent = '❌ LỖI - THỬ LẠI KẾT NỐI';
            alert("Lỗi: " + msg);
        }

        async function doPost(data) {
            const params = new URLSearchParams();
            for (const key in data) {
                params.append(key, data[key]);
            }
            
            try {
                const response = await fetch(temply_mobile_ajax.url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                    },
                    body: params.toString()
                });
                if (!response.ok) throw new Error('Network response was not ok');
                return await response.json();
            } catch (error) {
                throw new Error("Network đứt ở " + data.action);
            }
        }

        btn.addEventListener('click', async function(e) {
            e.preventDefault();
            const sourceText = sourceTextEl.value.trim();
            if (!sourceText) {
                alert("Anh chưa dán drama vào!!");
                return;
            }
            
            aiModel = aiModelEl.value;
            btn.disabled = true;
            btn.classList.add('opacity-50', 'cursor-not-allowed');
            btn.textContent = 'Vui lòng đợi 2-3 phút...';
            
            statusBox.classList.remove('hidden');
            statusBox.classList.add('flex');
            resultBox.classList.add('hidden');
            resultBox.classList.remove('flex');
            
            updateStatus("Bước 1/6: Đang dùng AI phân tích thể loại & keywords...");

            try {
                // 1. Analyze
                let res = await doPost({
                    action: 'temply_step_analyze_source',
                    nonce: temply_mobile_ajax.nonce, 
                    ai_model: aiModel,
                    source_text: sourceText
                });
                
                if (!res.success) return failWorkflow(res.data.message);
                state.genre = res.data.result.genre || 'Ngôn tình đô thị';
                state.tone = res.data.result.tone || 'Lãng mạn';
                state.keywords = res.data.result.keywords || sourceText.substring(0, 50);
                
                if (res.data.result.extracted_comments && res.data.result.extracted_comments.trim() !== '') {
                    document.getElementById('mobile-source-comments').value = res.data.result.extracted_comments;
                    document.getElementById('mobile-source-comments-group').classList.remove('hidden');
                    document.getElementById('mobile-source-comments-group').classList.add('flex');
                } else {
                    document.getElementById('mobile-source-comments').value = '';
                    document.getElementById('mobile-source-comments-group').classList.add('hidden');
                    document.getElementById('mobile-source-comments-group').classList.remove('flex');
                }
                
                // 2. Oracle
                updateStatus("Bước 2/6: Bơm thế giới ảo & luân hồi...");
                res = await doPost({
                    action: 'temply_step_oracle',
                    nonce: temply_mobile_ajax.nonce, 
                    ai_model: aiModel,
                    genre: state.genre, tone: state.tone, keywords: state.keywords
                });
                if (!res.success) return failWorkflow(res.data.message);
                state.world = res.data.result || res.data.world; // handle potential mismatch
                
                // 3. Puppet Master
                updateStatus("Bước 3/6: Đúc nhân vật cặn bã và tổng tài...");
                res = await doPost({
                    action: 'temply_step_puppet',
                    nonce: temply_mobile_ajax.nonce, 
                    ai_model: aiModel,
                    genre: state.genre, keywords: state.keywords, world: state.world
                });
                if (!res.success) return failWorkflow(res.data.message);
                state.characters = res.data.result || res.data.characters;
                
                // 4. Architect
                updateStatus(`Bước 4/6: Dựng rạp ${MAX_CHAPTERS} chương siêu bánh cuốn...`);
                res = await doPost({
                    action: 'temply_step_architect',
                    nonce: temply_mobile_ajax.nonce, 
                    ai_model: aiModel,
                    genre: state.genre, keywords: state.keywords, world: state.world, characters: state.characters, num_chapters: MAX_CHAPTERS
                });
                if (!res.success) return failWorkflow(res.data.message);
                state.chapters = res.data.result || res.data.chapters; 
                if (!Array.isArray(state.chapters)) return failWorkflow("Outline rỗng.");

                // Render Reviewer and Pause
                let listDiv = document.getElementById('temply-mobile-outline-list');
                listDiv.innerHTML = '';
                state.chapters.forEach((chap, idx) => {
                    listDiv.innerHTML += `
                        <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm outline-card" data-idx="${idx}">
                            <h4 class="font-bold text-slate-700 mb-2">Chương ${chap.chap_num}</h4>
                            <input type="text" class="w-full px-3 py-2 border border-slate-300 rounded mb-2 font-semibold text-blue-700 outline-title" value="${chap.title}">
                            <textarea class="w-full px-3 py-2 border border-slate-300 rounded text-sm text-slate-600 outline-summary" rows="3">${chap.summary}</textarea>
                        </div>
                    `;
                });
                
                document.getElementById('temply-mobile-outline-reviewer').classList.remove('hidden');
                document.getElementById('temply-mobile-outline-reviewer').classList.add('flex');
                
                document.getElementById('temply-mobile-resume-btn').onclick = async function() {
                    // Gather text
                    const cards = document.querySelectorAll('#temply-mobile-outline-reviewer .outline-card');
                    cards.forEach(card => {
                        const idx = card.getAttribute('data-idx');
                        state.chapters[idx].title = card.querySelector('.outline-title').value;
                        state.chapters[idx].summary = card.querySelector('.outline-summary').value;
                    });
                    
                    document.getElementById('temply-mobile-outline-reviewer').classList.add('hidden');
                    document.getElementById('temply-mobile-outline-reviewer').classList.remove('flex');
                    
                    await resumeWorkflowFromStep5();
                };

            } catch (error) {
                failWorkflow(error.message);
            }
            
            // --- HÀM CONTINUED ---
            async function resumeWorkflowFromStep5() {
                try {
                // 5. Create Story
                updateStatus("Bước 5/6: Làm giấy khai sinh truyện lên Web...");
                let res = await doPost({
                    action: 'temply_step_create_story',
                    nonce: temply_mobile_ajax.nonce, 
                    ai_model: aiModel,
                    genre: state.genre, keywords: state.keywords, world: state.world, characters: state.characters, art: 'Manga'
                });
                if (!res.success) return failWorkflow(res.data.message);
                state.truyen_id = res.data.truyen_id;
                
                // 6. Ghostwriter Loop
                for (let i = 0; i < state.chapters.length; i++) {
                    let chapMeta = state.chapters[i];
                    updateStatus(`Bước 6/6: Đang cày phím viết Chương ${chapMeta.chap_num}/${state.chapters.length}...`);
                    
                    try {
                        await doPost({
                            action: 'temply_step_write_chapter', 
                            nonce: temply_mobile_ajax.nonce, 
                            ai_model: aiModel,
                            mode: 'text', art: 'Manga', seed: 1234, 
                            truyen_id: state.truyen_id, 
                            chap_num: chapMeta.chap_num, 
                            chap_title: chapMeta.title,
                            summary: chapMeta.summary,
                            custom_comments: document.getElementById('mobile-source-comments').value,
                            world: state.world, characters: state.characters,
                            genre: state.genre, tone: state.tone, keywords: state.keywords,
                            is_final_chapter: (i === state.chapters.length - 1 ? 1 : 0)
                        });
                    } catch (e) {
                         // ignore and continue
                    }
                }
                
                // Complete
                statusBox.classList.add('hidden');
                statusBox.classList.remove('flex');
                btn.disabled = false;
                btn.classList.remove('opacity-50', 'cursor-not-allowed');
                btn.textContent = 'HOÀN TẤT! LÀM BỘ MỚI';
                resultBox.classList.remove('hidden');
                resultBox.classList.add('flex');
                resultLink.href = `/wp-admin/post.php?post=${state.truyen_id}&action=edit`;

                } catch (error) {
                    failWorkflow(error.message);
                }
            }
        });
    })();
    </script>
    <?php
    return ob_get_clean();
}

