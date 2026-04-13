<?php
if (!defined('ABSPATH')) {
    exit;
}

function temply_ai_render_batch_audit_page() {
    $truyen_id = isset($_GET['truyen_id']) ? intval($_GET['truyen_id']) : 0;
    
    // Thu thập danh sách truyện để chọn
    $args = ['post_type' => 'truyen', 'posts_per_page' => -1, 'post_status' => 'publish', 'orderby' => 'title', 'order' => 'ASC'];
    $truyen_list = get_posts($args);

    ?>
    <div class="wrap" style="max-width:1400px; margin-top:30px;">
        <h1 style="font-size:26px; font-weight:800; color:#1e1e2f; margin-bottom:5px;">📊 Bệnh Viện Truyện - Tổng Khám & Đại Tu</h1>
        <p style="font-size:14px; color:#555; margin-bottom:20px;">Giao diện chuyên quét lỗi logic, nhịp điệu hàng loạt và tự động viết lại. Chọn truyện → xem hồ sơ → ra lệnh AI.</p>

        <!-- ── STORY PICKER ── -->
        <div style="background:#fff; border:1px solid #e2e8f0; padding:20px; border-radius:16px; margin-bottom:16px;">
            <div style="display:flex; gap:12px; align-items:center; flex-wrap:wrap;">
                <strong style="white-space:nowrap; color:#1e293b;">Chọn Tác Phẩm Khám:</strong>

                <!-- Live Search Input -->
                <div style="flex:1; min-width:260px; position:relative;">
                    <input type="text" id="story-search-input" placeholder="🔍 Tìm truyện theo tên..." autocomplete="off"
                        style="width:100%; padding:8px 14px; border:1.5px solid #c7d2fe; border-radius:10px; font-size:14px; outline:none; box-sizing:border-box;"
                        onfocus="document.getElementById('story-dropdown').style.display='block'"
                        oninput="filterStories(this.value)">
                    <div id="story-dropdown" style="display:none; position:absolute; top:110%; left:0; right:0; background:#fff; border:1.5px solid #c7d2fe; border-radius:10px; box-shadow:0 8px 24px rgba(79,70,229,.12); max-height:280px; overflow-y:auto; z-index:999;">
                        <?php foreach($truyen_list as $t): ?>
                        <div class="story-opt" data-id="<?php echo $t->ID; ?>" data-title="<?php echo esc_attr($t->post_title); ?>"
                            style="padding:9px 14px; cursor:pointer; font-size:13px; border-bottom:1px solid #f1f5f9; transition:background .15s;"
                            onmouseover="this.style.background='#eef2ff'" onmouseout="this.style.background=''"
                            onclick="selectStory(<?php echo $t->ID; ?>, '<?php echo esc_js($t->post_title); ?>')">
                            <?php echo esc_html($t->post_title); ?>
                        </div>
                        <?php endforeach; ?>
                    </div>
                </div>

                <!-- Hidden form to submit selected story -->
                <form method="get" action="admin.php" id="story-select-form" style="display:flex; gap:8px; align-items:center;">
                    <input type="hidden" name="page" value="temply-ai-batch-audit">
                    <input type="hidden" name="truyen_id" id="story-select-hidden" value="<?php echo $truyen_id; ?>">
                    <button type="submit" class="button button-primary" style="background:#4f46e5; border-color:#4338ca; border-radius:8px; height:36px;">Mời Bác Sĩ →</button>
                </form>
            </div>
        </div>

        <?php if ($truyen_id):
            $story_post = get_post($truyen_id);
            $genre   = get_post_meta($truyen_id, '_temply_ai_genre', true) ?: get_post_meta($truyen_id, 'truyen_theloai', true) ?: '—';
            $tone    = get_post_meta($truyen_id, '_temply_ai_tone', true) ?: '—';
            $world   = get_post_meta($truyen_id, '_temply_ai_world', true) ?: get_post_meta($truyen_id, 'truyen_boi_canh', true) ?: '';
            $chars   = get_post_meta($truyen_id, '_temply_ai_characters', true) ?: '';
            $script  = get_post_meta($truyen_id, '_temply_ai_script', true) ?: '';
            $hook    = get_post_meta($truyen_id, '_temply_ai_hook', true) ?: '';
            $cover   = get_the_post_thumbnail_url($truyen_id, 'thumbnail') ?: '';
            $excerpt = wp_trim_words($story_post->post_excerpt ?: wp_strip_all_tags($story_post->post_content), 40, '…');

            $chapters = get_posts([
                'post_type'      => 'chuong',
                'posts_per_page' => -1,
                'meta_key'       => '_truyen_id',
                'meta_value'     => $truyen_id,
                'orderby'        => 'menu_order',
                'order'          => 'ASC',
            ]);
            $total_chap = count($chapters);
        ?>

        <!-- ── STORY METADATA EDITOR ── -->
        <div style="background:#fff; border:1px solid #e2e8f0; border-radius:16px; padding:20px; margin-bottom:16px; display:flex; gap:20px; align-items:flex-start;">
            <?php if($cover): ?>
            <div style="flex-shrink:0; text-align:center;">
                <img id="bv-cover-img" src="<?php echo esc_url($cover); ?>" style="width:80px; height:110px; object-fit:cover; border-radius:12px; box-shadow:0 2px 8px rgba(0,0,0,.1); display:block; margin-bottom:8px;">
                <button type="button" onclick="bvMetaAction('aiCover')" id="btn-bv-aicover" style="font-size:11px; padding:4px 8px; border-radius:6px; background:#f43f5e; color:#fff; border:none; cursor:pointer; width:100%;">Tạo Bìa AI</button>
            </div>
            <?php else: ?>
            <div style="flex-shrink:0; text-align:center; width:80px;">
                <div style="width:80px; height:110px; background:#f1f5f9; border-radius:12px; margin-bottom:8px;"></div>
                <button type="button" onclick="bvMetaAction('aiCover')" id="btn-bv-aicover" style="font-size:11px; padding:4px 8px; border-radius:6px; background:#f43f5e; color:#fff; border:none; cursor:pointer; width:100%;">Tạo Bìa AI</button>
            </div>
            <?php endif; ?>

            <div style="flex:1; min-width:0;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                    <h2 style="margin:0 0 6px; font-size:20px; color:#1e1e2f;"><?php echo get_the_title($truyen_id); ?></h2>
                    <div style="display:flex; gap:6px;">
                        <button type="button" onclick="bvMetaAction('saveM')" id="btn-bv-save" style="font-size:12px; font-weight:700; padding:6px 12px; border-radius:8px; background:#10b981; color:#fff; border:none; cursor:pointer;">💾 Lưu Thông Tin</button>
                        <button type="button" onclick="bvMetaAction('seo')" id="btn-bv-seo" style="font-size:12px; font-weight:700; padding:6px 12px; border-radius:8px; background:#f59e0b; color:#fff; border:none; cursor:pointer;">⚡ Tối ưu SEO (Rank Math)</button>
                    </div>
                </div>

                <form id="bv-meta-form" style="margin-top:10px;">
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:12px;">
                        <div>
                            <label style="font-size:12px; font-weight:700; color:#475569; display:block; margin-bottom:4px;">Thể loại</label>
                            <select name="genre" style="width:100%; font-size:13px; padding:6px; border:1px solid #cbd5e1; border-radius:6px; background:#fff;">
                                <option value="Drama (Cẩu huyết, Gia đấu, Vả mặt)" <?php selected($genre, 'Drama (Cẩu huyết, Gia đấu, Vả mặt)'); ?>>Drama (Cẩu huyết, Gia đấu, Vả mặt)</option>
                                <option value="Tâm Lý Xã Hội" <?php selected($genre, 'Tâm Lý Xã Hội'); ?>>Tâm Lý Xã Hội</option>
                                <option value="Trọng sinh" <?php selected($genre, 'Trọng sinh'); ?>>Trọng sinh</option>
                                <option value="Xuyên không" <?php selected($genre, 'Xuyên không'); ?>>Xuyên không</option>
                                <option value="Tu tiên" <?php selected($genre, 'Tu tiên'); ?>>Tu tiên</option>
                                <option value="Tổng tài" <?php selected($genre, 'Tổng tài'); ?>>Tổng tài</option>
                                <option value="Ngôn tình đô thị" <?php selected($genre, 'Ngôn tình đô thị'); ?>>Ngôn tình đô thị</option>
                                <option value="Sảng Văn" <?php selected($genre, 'Sảng Văn'); ?>>Sảng Văn</option>
                                <option value="Giả Heo Ăn Thịt Hổ" <?php selected($genre, 'Giả Heo Ăn Thịt Hổ'); ?>>Giả Heo Ăn Thịt Hổ</option>
                                <option value="Đô Thị Ẩn Thân" <?php selected($genre, 'Đô Thị Ẩn Thân'); ?>>Đô Thị Ẩn Thân</option>
                                <option value="Kinh dị Việt Nam" <?php selected($genre, 'Kinh dị Việt Nam'); ?>>Kinh dị Việt Nam</option>
                            </select>
                        </div>
                        <div>
                            <label style="font-size:12px; font-weight:700; color:#475569; display:block; margin-bottom:4px;">Văn phong (Truyện chữ)</label>
                            <select name="tone" style="width:100%; font-size:13px; padding:6px; border:1px solid #cbd5e1; border-radius:6px; background:#fff;">
                                <option value="Lãng mạn, miêu tả chi tiết cảm xúc" <?php selected($tone, 'Lãng mạn, miêu tả chi tiết cảm xúc'); ?>>Lãng mạn, miêu tả chi tiết cảm xúc</option>
                                <option value="Kịch tính, cắt cảnh nhanh, nhiều twist" <?php selected($tone, 'Kịch tính, cắt cảnh nhanh, nhiều twist'); ?>>Kịch tính, cắt cảnh nhanh, nhiều twist</option>
                                <option value="Hài hước, nhẹ nhàng, dễ đọc" <?php selected($tone, 'Hài hước, nhẹ nhàng, dễ đọc'); ?>>Hài hước, nhẹ nhàng, dễ đọc</option>
                                <option value="U tối, tâm lý sâu, hành động căng thẳng" <?php selected($tone, 'U tối, tâm lý sâu, hành động căng thẳng'); ?>>U tối, tâm lý sâu, hành động căng thẳng</option>
                            </select>
                        </div>
                    </div>

                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
                        <div>
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                                <label style="font-size:12px; font-weight:700; color:#475569;">Từ Khóa / Yếu tố / Hook</label>
                            </div>
                            <textarea id="bv_hook" name="hook" rows="3" placeholder="Ví dụ: Nữ chính bị phản bội, hệ thống báo thù 100 ngày..." style="width:100%; font-size:13px; padding:8px; border:1px solid #cbd5e1; border-radius:6px;"><?php echo esc_textarea($hook); ?></textarea>
                            
                            <div style="margin-top:6px; font-size:12px;">
                                <span style="font-weight:700; color:#ef4444;">🔥 Gợi ý Hook (Bấm để thêm):</span><br>
                                <div style="display:flex; flex-wrap:wrap; gap:6px; margin-top:4px;">
                                    <span onclick="bvAddMetaTag('bv_hook', this.innerText)" style="padding:2px 8px; border-radius:20px; background:#fef3c7; color:#b45309; border:1px solid #fde68a; cursor:pointer;">Giả nghèo thử lòng</span>
                                    <span onclick="bvAddMetaTag('bv_hook', this.innerText)" style="padding:2px 8px; border-radius:20px; background:#fce7f3; color:#be185d; border:1px solid #fbcfe8; cursor:pointer;">Trùng sinh phản diện</span>
                                    <span onclick="bvAddMetaTag('bv_hook', this.innerText)" style="padding:2px 8px; border-radius:20px; background:#e0e7ff; color:#4338ca; border:1px solid #c7d2fe; cursor:pointer;">Hệ thống vô lý</span>
                                    <span onclick="bvAddMetaTag('bv_hook', this.innerText)" style="padding:2px 8px; border-radius:20px; background:#dcfce7; color:#15803d; border:1px solid #bbf7d0; cursor:pointer;">Vả mặt trà xanh</span>
                                </div>
                            </div>
                        </div>
                        <div>
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                                <label style="font-size:12px; font-weight:700; color:#475569;">Bối cảnh & Thế giới (World Building)</label>
                            </div>
                            <textarea id="bv_world" name="world" rows="3" placeholder="Quy luật, tông màu, triều đại..." style="width:100%; font-size:13px; padding:8px; border:1px solid #cbd5e1; border-radius:6px;"><?php echo esc_textarea(wp_strip_all_tags($world)); ?></textarea>
                            
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:6px; margin-bottom:4px;">
                                <label style="font-size:12px; font-weight:700; color:#475569;">👥 Tuyến Nhân vật</label>
                            </div>
                            <textarea name="chars" rows="3" placeholder="Động cơ, tính cách..." style="width:100%; font-size:13px; padding:8px; border:1px solid #cbd5e1; border-radius:6px;"><?php echo esc_textarea(wp_strip_all_tags($chars)); ?></textarea>
                            
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:6px; margin-bottom:4px;">
                                <label style="font-size:12px; font-weight:700; color:#475569;">📋 Kịch bản (Root)</label>
                            </div>
                            <textarea name="script" rows="2" style="width:100%; font-size:13px; padding:8px; border:1px solid #cbd5e1; border-radius:6px;"><?php echo esc_textarea(wp_strip_all_tags($script)); ?></textarea>
                        </div>
                    </div>
                </form>
                <div id="bv-meta-result" style="display:none; font-size:13px; color:#166534; background:#dcfce7; padding:8px; border-radius:6px; margin-top:10px;"></div>
            </div>
        </div>

        <!-- ── AI COMMANDS DOCK ── -->
        <div style="background:#fff; border:1px solid #e2e8f0; border-radius:16px; padding:16px 20px; margin-bottom:16px;">
            <div style="font-size:13px; font-weight:700; color:#374151; margin-bottom:12px;">⚡ Lệnh AI Phân Tích:</div>
            <div style="display:flex; flex-wrap:wrap; gap:8px;">
                <button class="bv-ai-btn" onclick="bvAiAction('add_chapters')" style="background:#4f46e5; color:#fff; border:none; padding:8px 16px; border-radius:10px; font-size:13px; font-weight:700; cursor:pointer;">➕ Thêm chương tiếp</button>
                <button class="bv-ai-btn" onclick="bvAiAction('suggest_prune')" style="background:#f59e0b; color:#fff; border:none; padding:8px 16px; border-radius:10px; font-size:13px; font-weight:700; cursor:pointer;">✂️ Gợi ý bỏ/gộp chương</button>
                <button class="bv-ai-btn" onclick="bvAiAction('improve_plot')" style="background:#10b981; color:#fff; border:none; padding:8px 16px; border-radius:10px; font-size:13px; font-weight:700; cursor:pointer;">🧠 Gợi ý cải thiện mạch truyện</button>
                <button class="bv-ai-btn" onclick="bvAiAction('replan_outline')" style="background:#8b5cf6; color:#fff; border:none; padding:8px 16px; border-radius:10px; font-size:13px; font-weight:700; cursor:pointer;">🗒 Lập lại dàn ý toàn bộ</button>
                <button class="bv-ai-btn" onclick="bvAiAction('hook_check')" style="background:#ef4444; color:#fff; border:none; padding:8px 16px; border-radius:10px; font-size:13px; font-weight:700; cursor:pointer;">🎣 Kiểm tra Hook & Twist</button>
            </div>
            <!-- Lời khuyên & Nhập Master Prompt -->
            <div style="margin-top:14px; background:#f0fdf4; border:1px solid #bbf7d0; border-radius:10px; padding:12px;">
                <p style="margin:0 0 8px; font-size:13px; color:#166534; font-weight:600;">💡 Gọi ý: Sau khi AI Phân Tích tư vấn xong, bạn có thể copy những "Chỉ đạo mạch truyện" quan trọng dán vào ô bên dưới. Khi tiến hành Đại Tu, AI sẽ kết hợp nhược điểm của từng chương + Chỉ đạo này để sửa lại cẩn thận nhất.</p>
                <textarea id="bvGlobalPrompt" rows="2" placeholder="Dán chỉ đạo của bạn/AI Phân tích vào đây (Tuỳ chọn). Ví dụ: Nhớ giữ nhịp độ chậm lại, thêm hint về kẻ thù giấu mặt..." style="width:100%; font-size:12px; padding:8px; border:1px solid #86efac; border-radius:6px;"></textarea>
            </div>
            <!-- Result box -->
            <div id="bv-ai-result" style="display:none; margin-top:14px; background:#f8fafc; border:1.5px solid #e2e8f0; border-radius:12px; padding:16px; font-size:13px; color:#334155; line-height:1.7; white-space:pre-wrap; max-height:400px; overflow-y:auto;"></div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:10px;">
            <div>
                <h2 style="margin:0; font-size:18px; color:#1e293b;">📋 Hồ Sơ Chương — <?php echo get_the_title($truyen_id); ?></h2>
                <p style="margin:4px 0 0; color:#64748b; font-size:13px;">Tổng: <?php echo $total_chap; ?> chương</p>
            </div>
            <div style="display:flex; gap:8px; align-items:center; flex-wrap:wrap;">
                <select id="batchAiModel" style="border-radius:8px; padding:6px 10px; border:1px solid #e2e8f0; font-size:13px;">
                    <option value="gemini" selected>Google Gemini Flash (Miễn Phí)</option>
                    <option value="claude">Claude Sonnet (Tốn Tiền)</option>
                </select>
                <button id="btnMassScan" class="button button-primary" style="background:#5b21b6; border-color:#4c1d95; border-radius:8px;">🔍 Scan Toàn Bộ Chương</button>
                <button id="btnMassFix" class="button button-primary" style="background:#b91c1c; border-color:#991b1b; border-radius:8px; display:inline-block;">🚑 Đại Tu Chương Đã Chọn</button>
            </div>
        </div>

        <script>
        // ── LIVE SEARCH ──
        document.addEventListener('click', function(e) {
            if (!e.target.closest('#story-search-input') && !e.target.closest('#story-dropdown')) {
                document.getElementById('story-dropdown').style.display = 'none';
            }
        });
        function filterStories(q) {
            q = q.toLowerCase();
            document.querySelectorAll('.story-opt').forEach(function(el) {
                el.style.display = el.dataset.title.toLowerCase().includes(q) ? '' : 'none';
            });
            document.getElementById('story-dropdown').style.display = 'block';
        }
        function selectStory(id, title) {
            document.getElementById('story-search-input').value = title;
            document.getElementById('story-select-hidden').value = id;
            document.getElementById('story-dropdown').style.display = 'none';
        }
        // Pre-fill search if already selected
        <?php if($truyen_id): ?>
        document.getElementById('story-search-input').value = '<?php echo esc_js(get_the_title($truyen_id)); ?>';
        <?php endif; ?>

        // ── AI ACTIONS ──
        var bvChapList = <?php echo json_encode(array_map(function($c){ return ['id'=>$c->ID, 'title'=>$c->post_title]; }, $chapters)); ?>;
        var bvMeta = {
            title: <?php echo json_encode(get_the_title($truyen_id)); ?>,
            genre: <?php echo json_encode($genre); ?>,
            tone:  <?php echo json_encode($tone); ?>,
            world: <?php echo json_encode(mb_substr(wp_strip_all_tags($world),0,800)); ?>,
            chars: <?php echo json_encode(mb_substr(wp_strip_all_tags($chars),0,400)); ?>,
            script:<?php echo json_encode(mb_substr(wp_strip_all_tags($script),0,600)); ?>,
            totalChap: <?php echo $total_chap; ?>
        };
        var bvNonce = '<?php echo wp_create_nonce("temply_ai_nonce"); ?>';

        var bvPrompts = {
            add_chapters:   'Dựa vào toàn bộ meta truyện và số chương hiện tại ('+bvMeta.totalChap+' chương), hãy gợi ý viết thêm 5 chương tiếp theo. Mỗi chương cần: STT, Tên chương ấn tượng, Sự kiện chính trong chương (2-3 câu). Đảm bảo mạch truyện liền mạch và giữ đúng giọng văn.',
            suggest_prune:  'Hãy đọc danh sách '+bvMeta.totalChap+' chương. Phân tích xem có chương nào: (1) Trùng lặp nội dung, (2) Đuối nhịp không cần thiết, (3) Có thể gộp với chương khác. Liệt kê rõ số chương và lý do cần cắt/gộp.',
            improve_plot:   'Phân tích bố cục tổng thể của bộ truyện '+bvMeta.totalChap+' chương. Hãy chỉ ra: (1) Điểm mạnh cần giữ, (2) Điểm yếu trong arc nhân vật / nhịp điệu / logic, (3) Gợi ý cải thiện mạch truyện cụ thể.',
            replan_outline: 'Dựa vào bối cảnh và nhân vật hiện tại, hãy viết lại DÀN Ý mới từ đầu cho toàn bộ truyện. Định dạng: Chương N: [Tên] — [Sự kiện chính] (1-2 câu). Ghi đủ '+Math.max(bvMeta.totalChap, 20)+' chương.',
            hook_check:     'Hãy kiểm tra xem bộ truyện này có đủ HOOK và TWIST không. Cụ thể: (1) Mỗi 5 chương có một điểm bùng nổ không?, (2) Hook mở đầu có đủ kéo người đọc không?, (3) Gợi ý thêm 3 twist có thể chèn vào truyện để tăng độ cuốn.'
        };

        function bvAiAction(type) {
            var box = document.getElementById('bv-ai-result');
            box.style.display = 'block';
            box.innerHTML = '<span>⚙️ AI đang phân tích, xin chờ...</span>';

            var chapNames = bvChapList.map(function(c, i){ return (i+1)+'. '+c.title; }).join('\n');
            var context = 'TÊN TRUYỆN: '+bvMeta.title+'\nTHỂ LOẠI: '+bvMeta.genre+'\nGIỌNG VĂN: '+bvMeta.tone+'\nBỐI CẢNH: '+bvMeta.world+'\nNHÂN VẬT: '+bvMeta.chars+'\nKỊCH BẢN: '+bvMeta.script+'\n\nDANH SÁCH CHƯƠNG:\n'+chapNames;

            jQuery.post(ajaxurl, {
                action: 'temply_bv_ai_action',
                nonce:  bvNonce,
                prompt_type: type,
                context: context,
                custom_prompt: bvPrompts[type]
            }, function(res) {
                if (res.success) {
                    box.textContent = res.data.result;
                } else {
                    box.textContent = '❌ Lỗi: ' + (res.data?.message || 'Không rõ');
                }
            }).fail(function() {
                box.textContent = '❌ Lỗi kết nối server';
            });
        }

        // Handle Save Meta, SEO format, and AI Cover
        function bvMetaAction(type) {
            var resBox = document.getElementById('bv-meta-result');
            resBox.style.display = 'block';
            resBox.className = '';
            
            if (type === 'aiCover') {
                var btn = document.getElementById('btn-bv-aicover');
                var origText = btn.innerHTML;
                btn.innerHTML = '🎨 Đang vẽ...';
                btn.disabled = true;
                resBox.innerHTML = '⏳ Đang chờ AI vẽ bìa (khoảng 15-30s)...';
                jQuery.post(ajaxurl, {
                    action: 'temply_step_regenerate_story_cover',
                    nonce: bvNonce,
                    truyen_id: <?php echo $truyen_id; ?>
                }, function(res) {
                    btn.innerHTML = origText;
                    btn.disabled = false;
                    if (res.success) {
                        resBox.innerHTML = '✅ ' + res.data.message;
                        if(res.data.url) {
                            var img = document.getElementById('bv-cover-img');
                            if(img) img.src = res.data.url;
                            else location.reload();
                        }
                    } else {
                        resBox.innerHTML = '❌ ' + (res.data?.message || 'Lỗi tạo bìa');
                    }
                }).fail(function() { btn.innerHTML=origText; btn.disabled=false; resBox.innerHTML='❌ Lỗi kết nối'; });
                return;
            }

            var formData = jQuery('#bv-meta-form').serialize();
            formData += '&action=' + (type === 'saveM' ? 'temply_bv_save_meta' : 'temply_bv_optimize_seo_rm');
            formData += '&nonce=' + bvNonce;
            formData += '&truyen_id=<?php echo $truyen_id; ?>';

            var btnId = type === 'saveM' ? '#btn-bv-save' : '#btn-bv-seo';
            var origBtnHTML = jQuery(btnId).html();
            jQuery(btnId).html('⏳ Đang xử lý...').prop('disabled', true);
            resBox.innerHTML = '⏳ Vui lòng chờ...';

            jQuery.post(ajaxurl, formData, function(res) {
                jQuery(btnId).html(origBtnHTML).prop('disabled', false);
                if (res.success) {
                    resBox.innerHTML = '✅ ' + res.data.message;
                } else {
                    resBox.innerHTML = '❌ Lỗi: ' + (res.data?.message || 'Không rõ');
                }
            }).fail(function() {
                jQuery(btnId).html(origBtnHTML).prop('disabled', false);
                resBox.innerHTML = '❌ Lỗi kết nối server';
            });
        }
        
        function bvAddMetaTag(fieldId, tagText) {
            var el = document.getElementById(fieldId);
            if(el) {
                if(el.value.length > 0 && !el.value.endsWith(' ')) el.value += ', ';
                el.value += tagText;
            }
        }
        </script>

        <?php if(empty($chapters)): ?>
        <div class="notice notice-warning"><p>Truyện này chưa có chương nào!</p></div>
        <?php else: ?>

            <!-- Dashboard Các Chương -->
            <div id="batchProcessBoard" style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; overflow:hidden;">
                <table class="wp-list-table widefat fixed striped table-view-list" style="border:none;">
                    <thead>
                        <tr>
                            <th style="width: 50px;">STT</th>
                            <th style="width: 25%;">Tên Chương</th>
                            <th style="width: 15%;">Trạng Thái</th>
                            <th>Kết Quả Bắt Mạch (AI Nhận Xét)</th>
                            <th style="width: 80px; text-align:center;">
                                Sửa lại<br>
                                <input type="checkbox" id="selectAllChaps" title="Chọn tất cả">
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php foreach($chapters as $idx => $chap): ?>
                            <tr class="chap-row" data-id="<?php echo $chap->ID; ?>" id="row-<?php echo $chap->ID; ?>">
                                <td><?php echo $idx + 1; ?></td>
                                <td>
                                    <strong><a href="<?php echo get_edit_post_link($chap->ID); ?>" target="_blank"><?php echo esc_html($chap->post_title); ?></a></strong>
                                </td>
                                <td>
                                    <span class="status-badge" style="display:inline-block; padding:3px 8px; border-radius:12px; font-size:11px; font-weight:bold; background:#e2e8f0; color:#475569;">Chưa Scan</span>
                                </td>
                                <td class="diagnostic-result" style="font-size:13px; color:#334155; line-height:1.5;">
                                    <em style="color:#94a3b8;">Chưa có dữ liệu...</em>
                                </td>
                                <td>
                                    <input type="checkbox" class="fix-checkbox" value="<?php echo $chap->ID; ?>">
                                </td>
                            </tr>
                        <?php endforeach; ?>
                    </tbody>
                </table>
            </div>
            
            <script>
            var bvAjaxUrl = '<?php echo admin_url("admin-ajax.php"); ?>';
        var bvStoryCtx = {
            genre: <?php echo json_encode($genre); ?>,
            tone:  <?php echo json_encode($tone); ?>,
            world: <?php echo json_encode(mb_substr(wp_strip_all_tags($world), 0, 500)); ?>,
            chars: <?php echo json_encode(mb_substr(wp_strip_all_tags($chars), 0, 300)); ?>
        };
        document.addEventListener('DOMContentLoaded', function() {
                // Checkbox "Chọn tất cả" Logic
                const selectAllCheck = document.getElementById('selectAllChaps');
                if(selectAllCheck) {
                    selectAllCheck.addEventListener('change', function() {
                        const cboxes = document.querySelectorAll('.fix-checkbox'); // Allow checking even if disabled initially
                        cboxes.forEach(cb => {
                            cb.disabled = false; // Always allow manual select after clicking select all
                            cb.checked = this.checked;
                        });
                    });
                }
                
                const btnMassScan = document.getElementById('btnMassScan');
                const btnMassFix = document.getElementById('btnMassFix');
                const rows = document.querySelectorAll('.chap-row');
                const aiModel = document.getElementById('batchAiModel');
                
                async function processQueue(items, processFunc, concurrency = 2) {
                    let index = 0;
                    async function worker() {
                        while (index < items.length) {
                            const cur = index++;
                            await processFunc(items[cur]);
                        }
                    }
                    const workers = [];
                    for(let i=0; i<concurrency; i++) {
                        workers.push(worker());
                    }
                    await Promise.all(workers);
                }

                // KHÂU 1: SCAN HÀNG LOẠT
                btnMassScan.addEventListener('click', async () => {
                    if(!confirm('Quá trình này sẽ gọi API để đọc MỌI CHƯƠNG. Có thể mất 1-3 phút. Bạn đã sẵn sàng?')) return;
                    
                    btnMassScan.disabled = true;
                    btnMassScan.textContent = 'Đang Scan...';
                    
                    const chapters = Array.from(rows).map(r => r.dataset.id);
                    
                    await processQueue(chapters, async (chapId) => {
                        const tr = document.getElementById('row-' + chapId);
                        const badge = tr.querySelector('.status-badge');
                        const resultTd = tr.querySelector('.diagnostic-result');
                        const cbox = tr.querySelector('.fix-checkbox');
                        
                        badge.style.background = '#fef08a'; badge.style.color = '#854d0e'; badge.textContent = 'Đang khám...';
                        resultTd.innerHTML = '<span class="spinner is-active" style="float:none; margin:0"></span> Đang chờ AI phán...';
                        
                        const fd = new FormData();
                        fd.append('action', 'temply_auto_review_chapter');
                        fd.append('nonce', '<?php echo wp_create_nonce("temply_ai_nonce"); ?>');
                        fd.append('chuong_id', chapId);
                        fd.append('ai_model', aiModel.value);
                        fd.append('story_genre', bvStoryCtx.genre);
                        fd.append('story_tone',  bvStoryCtx.tone);
                        fd.append('story_world', bvStoryCtx.world);
                        fd.append('story_chars', bvStoryCtx.chars);
                        
                        try {
                            const r = await fetch(bvAjaxUrl, {method: 'POST', body: fd});
                            const res = await r.json();
                            
                            if(res.success) {
                                // Simple heuristic: if review has lots of negative words, auto-tick. Else safe.
                                const text = res.data.review.toLowerCase();
                                const isBad = text.includes('kém') || text.includes('nhạt') || text.includes('thiếu logic') || text.includes('chưa đủ') || text.includes('lan man');
                                
                                resultTd.innerHTML = res.data.review.replace(/\n/g, '<br>');
                                cbox.disabled = false;
                                
                                if(isBad) {
                                    badge.style.background = '#fee2e2'; badge.style.color = '#991b1b'; badge.textContent = 'Bệnh nặng';
                                    resultTd.style.color = '#991b1b';
                                    cbox.checked = true; // Suggest fixing
                                } else {
                                    badge.style.background = '#dcfce7'; badge.style.color = '#166534'; badge.textContent = 'Đạt chuẩn';
                                    cbox.checked = false;
                                }
                            } else {
                                badge.style.background = '#f1f5f9'; badge.style.color = '#ef4444'; badge.textContent = 'Lỗi';
                                resultTd.textContent = res.data.message || 'Lỗi mạng';
                            }
                        } catch(e) {
                            badge.style.background = '#f1f5f9'; badge.style.color = '#ef4444'; badge.textContent = 'Lỗi API';
                            resultTd.textContent = e.message;
                        }
                    }, 1); // 1 at a time to prevent timeout
                    
                    btnMassScan.textContent = 'ĐÃ QUÉT XONG';
                    btnMassFix.style.display = 'inline-block';
                });
                
                // KHÂU 2: ĐẠI TU HÀNG LOẠT CÁC CHECKBOX ĐƯỢC CHỌN
                btnMassFix.addEventListener('click', async () => {
                    const toFixBoxes = document.querySelectorAll('.fix-checkbox:checked');
                    if(toFixBoxes.length === 0) return alert('Không có chương nào được đánh dấu để đại tu!');
                    if(!confirm(`Xác nhận GỌI HỘI LÊN CHÍCH THUỐC VÀ CẢI TẠO LẠI ${toFixBoxes.length} CHƯƠNG NÀY? Toàn bộ nội dung cũ sẽ bị Ghi Đè.`)) return;
                    
                    btnMassFix.disabled = true;
                    btnMassFix.textContent = 'Đang phẫu thuật...';
                    
                    const toFixIds = Array.from(toFixBoxes).map(cb => cb.value);
                    
                    await processQueue(toFixIds, async (chapId) => {
                        const tr = document.getElementById('row-' + chapId);
                        const badge = tr.querySelector('.status-badge');
                        const reviewText = tr.querySelector('.diagnostic-result').innerText;
                        
                        badge.style.background = '#fef08a'; badge.style.color = '#854d0e'; badge.textContent = 'Đang Viết Lại...';
                        
                        const fd = new FormData();
                        fd.append('action', 'temply_step_regenerate_chapter');
                        fd.append('nonce', '<?php echo wp_create_nonce("temply_ai_nonce"); ?>');
                        fd.append('chuong_id', chapId);
                        fd.append('ai_model', aiModel.value);
                        const globalPrompt = document.getElementById('bvGlobalPrompt').value.trim();
                        let finalPrompt = 'HÃY CHÚA TỂ BIÊN TẬP: \n' + reviewText + '\n\nYêu cầu: Viết lại Chương này sao cho xoá sổ mọi nhược điểm nói trên. Phải hay, cuốn, mặn mòi.';
                        if (globalPrompt !== '') {
                            finalPrompt += '\n\nCHỈ ĐẠO TỔNG QUÁT TỪ TÁC GIẢ (ÁP DỤNG CHUNG): \n' + globalPrompt;
                        }
                        fd.append('custom_summary', finalPrompt);
                        
                        try {
                            const r = await fetch(bvAjaxUrl, {method: 'POST', body: fd});
                            const res = await r.json();
                            if(res.success) {
                                badge.style.background = '#dcfce7'; badge.style.color = '#166534'; badge.textContent = 'Đã Hồi Sinh';
                            } else {
                                badge.style.background = '#fee2e2'; badge.style.color = '#b91c1c'; badge.textContent = 'Mổ Xịt';
                            }
                        } catch(e) {
                            badge.style.background = '#fee2e2'; badge.style.color = '#b91c1c'; badge.textContent = 'Lỗi Băng Ca';
                        }
                    }, 1); // Only rewrite 1 at a time to prevent API timeout.
                    
                    btnMassFix.textContent = 'ĐẠI TU HOÀN TẤT';
                    alert('Quy trình phẫu thuật hàng loạt đã hoàn tất!');
                });
            });
            </script>
        <?php endif; // End of empty($chapters) ?>
        <?php endif; // End of if($truyen_id) ?>
    </div>
    <?php
}
