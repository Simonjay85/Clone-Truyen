<?php
if (!defined('ABSPATH')) {
    exit;
}

function temply_ai_render_auto_pilot_page() {
    // Thêm kịch bản đã qua chỉnh sửa vào Queue
    if (isset($_POST['temply_add_to_queue']) && check_admin_referer('temply_auto_pilot_action')) {
        $keyword = sanitize_textarea_field($_POST['pilot_keyword']);
        $title = sanitize_text_field($_POST['pilot_title'] ?? '');
        if (empty($title)) {
            $title = wp_trim_words($keyword, 8, '...');
        }
        $genre = sanitize_text_field($_POST['pilot_genre']);
        $tone = sanitize_text_field($_POST['pilot_tone']);
        
        $chapters_val = sanitize_text_field($_POST['pilot_chapters']);
        $chapters = ($chapters_val === 'Auto' || empty($chapters_val) || !is_numeric($chapters_val)) ? 50 : intval($chapters_val);
        
        $world = sanitize_textarea_field($_POST['pilot_world']);
        $chars = '';
        $hook = '';
        
        $cron_interval = sanitize_text_field($_POST['pilot_interval']);
        $enable_audit = isset($_POST['pilot_enable_audit']) ? 1 : 0;
        
        $current_config = get_option('temply_auto_pilot_queue_config', false);
        if (!$current_config) {
            $current_config = [
                'interval' => $cron_interval,
                'queue' => [],
                'status' => 'running',
                'last_run' => time()
            ];
        }
        
        $current_config['interval'] = $cron_interval;
        $current_config['status'] = 'running'; // Đảm bảo luôn bật
        
        $pause_outline = isset($_POST['pilot_pause_outline']) ? 1 : 0;
        $initial_status = $pause_outline ? 'draft_outline' : 'pending';

        $current_config['queue'][] = [
            'status' => $initial_status, // draft_outline, pending, writing, completed
            'prompt' => $keyword,
            'title' => $title,
            'genre' => $genre,
            'tone' => $tone,
            'world' => $world,
            'chars' => $chars,
            'hook' => $hook,
            'truyen_id' => 0,
            'target_chapters' => $chapters,
            'chapters_left' => $chapters,
            'enable_audit' => $enable_audit,
            'pause_outline' => $pause_outline
        ];
        
        update_option('temply_auto_pilot_queue_config', $current_config);
        
        // Khởi động cron nếu nó đang ngủ
        if (!wp_next_scheduled('temply_auto_pilot_cron_hook')) {
            wp_schedule_event(time(), $cron_interval, 'temply_auto_pilot_cron_hook');
        }
        
        echo '<div class="notice notice-success is-dismissible"><p>Đã ném thành công bộ truyện "<b>'.esc_html($title).'</b>" vào Lò Bát Quái!</p></div>';
    }
    
    // Nút huỷ cron
    if (isset($_POST['temply_stop_auto_pilot']) && check_admin_referer('temply_auto_pilot_action')) {
        delete_option('temply_auto_pilot_queue_config');
        wp_clear_scheduled_hook('temply_auto_pilot_cron_hook');
        echo '<div class="notice notice-warning is-dismissible"><p>Đã DỌN SẠCH hàng chờ và tắt trạm phát sóng.</p></div>';
    }

    $current_config = get_option('temply_auto_pilot_queue_config', false);
    
    $total_queue = 0;
    $done_queue = 0;
    $active_item = null;
    if ($current_config && !empty($current_config['queue'])) {
        foreach ($current_config['queue'] as $item) {
            $total_queue++;
            if ($item['status'] === 'completed') $done_queue++;
            if (($item['status'] === 'pending' || $item['status'] === 'writing' || $item['status'] === 'draft_outline') && !$active_item) {
                $active_item = $item;
            }
        }
    }
    ?>
    <div class="wrap" style="max-w: 1200px; margin-top:20px;">
        <h1 style="font-size:28px; font-weight:800; color:#1e1e2f; margin-bottom: 20px;">🤖 Trạm Tiền Phương: Xây Kịch Bản & Xếp Hàng</h1>
        <p style="font-size:15px; color:#555;">Khu vực cấm địa: Bạn quăng Ý tưởng mồi, AI sẽ nặn thành Khuôn. Chỉnh sửa vừa ý rồi Quăng vào Lò đúc để máy tự đẻ truyện, tự kiểm duyệt cả ngày đêm.</p>

        <div style="display: flex; gap: 30px; margin-top:20px; flex-wrap: wrap;">
            
            <!-- Cột Trái: Bếp Nấu Kịch Bản -->
            <div style="flex: 2; min-width: 500px;">
                <script src="https://cdn.tailwindcss.com"></script>
                <div class="bg-white border border-slate-200 rounded-xl p-6 shadow-sm">
                    <div class="mb-6 pb-4 border-b border-slate-100 flex items-center justify-between">
                        <h2 class="text-xl font-extrabold text-slate-800 m-0">Gieo Hạt Giống (Đẩy Vào Hàng Chờ)</h2>
                        <span class="bg-rose-100 text-rose-700 text-xs px-2 py-1 rounded font-bold uppercase tracking-wider">Hạt Giống Auto-Pilot</span>
                    </div>

                    <form method="post" id="auto-pilot-form">
                        <?php wp_nonce_field('temply_auto_pilot_action'); ?>
                        
                        <!-- Thể loại & Tone -->
                        <div class="grid grid-cols-2 gap-4 mb-4">
                            <div>
                                <label class="block text-sm font-semibold text-slate-700 mb-2">Thể loại</label>
                                <select name="pilot_genre" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none text-sm bg-slate-50">
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
                            <div>
                                <label class="block text-sm font-semibold text-slate-700 mb-2">Văn phong</label>
                                <select name="pilot_tone" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none text-sm bg-slate-50">
                                    <option value="Lãng mạn">Lãng mạn, miêu tả chi tiết cảm xúc</option>
                                    <option value="Kịch tính">Kịch tính, dồn dập, giật gân</option>
                                    <option value="Hài hước">Hài hước, sảng văn, nhẹ nhàng</option>
                                    <option value="U tối">U tối, bí hiểm, nặng nề tâm lý</option>
                                </select>
                            </div>
                        </div>
                        
                        <div class="grid grid-cols-2 gap-4 mb-4">
                            <div>
                                <label class="block text-sm font-semibold text-slate-700 mb-2">Tên Truyện</label>
                                <input type="text" name="pilot_title" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none text-sm bg-slate-50 font-bold text-blue-700" placeholder="Để trống AI tự đặt dựa theo Từ khoá...">
                            </div>
                            <div>
                                <label class="block text-sm font-semibold text-slate-700 mb-2">Số Chương (dự kiến)</label>
                                <input type="text" name="pilot_chapters" value="Auto" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none text-sm bg-slate-50 text-center font-bold text-rose-600">
                            </div>
                        </div>

                        <!-- Keywords / Hook -->
                        <div class="mb-4">
                            <div class="flex items-center justify-between mb-2">
                                <label class="block text-sm font-semibold text-slate-700">Từ khóa / Yếu tố / Hook</label>
                                <button id="temply-brainstorm-btn" type="button" class="text-xs flex items-center gap-1 bg-purple-100 text-purple-700 px-2 py-1 rounded hover:bg-purple-200 transition-colors font-medium border border-purple-200">
                                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                                    Brainstorm AI
                                </button>
                            </div>
                            <textarea name="pilot_keyword" id="temply-keywords" rows="3" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none text-sm bg-slate-50" placeholder="Ví dụ: Nữ chính bị phản bội, hệ thống báo thù 100 ngày..."></textarea>
                            
                            <div id="brainstorm-results" class="hidden mt-2 border border-purple-200 bg-purple-50 rounded-lg p-3">
                                <div class="text-xs font-semibold text-purple-800 mb-2">✨ Bấm vào Ý Tưởng bạn thích để nạp vào Từ Khoá gốc:</div>
                                <div id="brainstorm-list" class="space-y-2"></div>
                            </div>
                            
                            <div class="mt-3">
                                <label class="block text-xs font-medium text-slate-500 mb-2">🔥 Gợi ý Yếu tố Hot (Bấm để thêm):</label>
                                <div class="flex flex-wrap gap-2">
                                    <span class="px-2 py-1 bg-amber-50 text-amber-700 border border-amber-200 rounded text-[11px] font-semibold cursor-pointer hover:bg-amber-600 hover:text-white" onclick="addHook(this)">Giả nghèo thử lòng bị khinh</span>
                                    <span class="px-2 py-1 bg-rose-50 text-rose-700 border border-rose-200 rounded text-[11px] font-semibold cursor-pointer hover:bg-rose-600 hover:text-white" onclick="addHook(this)">Trùng sinh vào vai phản diện</span>
                                    <span class="px-2 py-1 bg-emerald-50 text-emerald-700 border border-emerald-200 rounded text-[11px] font-semibold cursor-pointer hover:bg-emerald-600 hover:text-white" onclick="addHook(this)">Vả mặt tiểu tam trà xanh</span>
                                    <span class="px-2 py-1 bg-blue-50 text-blue-700 border border-blue-200 rounded text-[11px] font-semibold cursor-pointer hover:bg-blue-600 hover:text-white" onclick="addHook(this)">Hệ thống phát tiền cực vô lý</span>
                                </div>
                            </div>
                        </div>

                        <!-- World Building -->
                        <div class="mb-4 mt-6">
                            <div class="flex items-center justify-between mb-2">
                                <label class="block text-sm font-semibold text-slate-700">Bối Cảnh & Thế Giới (World Building)</label>
                                <button id="temply-brainstorm-world-btn" type="button" class="text-xs flex items-center gap-1 bg-purple-100 text-purple-700 px-2 py-1 rounded hover:bg-purple-200 transition-colors font-medium border border-purple-200">
                                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                                    Brainstorm AI
                                </button>
                            </div>
                            <textarea name="pilot_world" id="temply-world-building" rows="3" class="w-full px-4 py-2 border border-purple-200 rounded-lg focus:ring-2 focus:ring-purple-500 outline-none text-sm bg-purple-50/30" placeholder="Copy và Paste quy luật hệ thống, tông màu văn hoá, thiết lập triều đại... AI sẽ dùng nó làm core rules để viết truyện."></textarea>
                            <div id="brainstorm-world-results" class="hidden mt-2 border border-purple-200 bg-purple-50 rounded-lg p-3">
                                <div class="text-xs font-semibold text-purple-800 mb-2">✨ Bấm vào 1 Ý Tưởng Thế Giới dưới đây để nạp:</div>
                                <div id="brainstorm-world-list" class="space-y-2"></div>
                            </div>
                        </div>

                        <!-- Trạm kiểm duyệt -->
                        <div class="mt-4 bg-yellow-50 border border-yellow-200 p-3 rounded-lg mb-4 flex items-start gap-3">
                            <input type="checkbox" name="pilot_pause_outline" value="1" id="temply-pause-outline" class="mt-1 flex-shrink-0" checked>
                            <div>
                                <label for="temply-pause-outline" class="font-bold text-yellow-800 text-sm cursor-pointer">Trạm Kiểm Duyệt Dàn Ý (Human-in-the-loop)</label>
                                <p class="text-[11px] text-yellow-700 leading-snug mt-1">Hệ thống sẽ TẠM DỪNG sau bước "Sáng tác Dàn ý" và chờ bạn phê duyệt trong hàng chờ (Tính năng đang làm).</p>
                            </div>
                        </div>
                        
                        <!-- Tốc độ -->
                        <div class="bg-slate-50 border border-slate-200 p-4 rounded-lg mb-6">
                            <label class="block text-sm font-semibold text-slate-700 mb-2">Chu kỳ rặn (Tốc độ lò ấp):</label>
                            <select name="pilot_interval" class="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none text-sm bg-white">
                                <option value="every_five_minutes">Chế độ Thác Đổ (Mỗi 5 phút 1 Chương)</option>
                                <option value="hourly">Nhỏ Giọt (Mỗi tiếng 1 Chương)</option>
                                <option value="twicedaily">Tà Tà (Ngày 2 Chương)</option>
                            </select>
                        </div>

                        <button type="submit" name="temply_add_to_queue" class="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-3 px-4 rounded-xl transition-all shadow-lg hover:shadow-emerald-600/30 flex items-center justify-center gap-2">
                            <span class="dashicons dashicons-plus-alt2" style="margin-top:2px;"></span> Đẩy Vào Hàng Chờ Chạy Ngầm
                        </button>
                    </form>

                    <script>
                    jQuery(document).ready(function($) {
                        function addHook(el) {
                            let ta = document.getElementById('temply-keywords');
                            ta.value = ta.value ? ta.value + ', ' + el.innerText : el.innerText;
                        }
                        window.addHook = addHook;

                        function addWorld(el) {
                            let ta = document.getElementById('temply-world-building');
                            ta.value = el.innerText;
                        }
                        window.addWorld = addWorld;

                        // Brainstorm Hook
                        $('#temply-brainstorm-btn').click(function() {
                            const btn = $(this);
                            const keyword = $('#temply-keywords').val();
                            const genre = $('select[name="pilot_genre"]').val();
                            btn.prop('disabled', true).html('<span class="dashicons dashicons-update spin"></span> Đang nặn ý tưởng...');
                            
                            $.post(ajaxurl, {
                                action: 'temply_ajax_brainstorm_hook',
                                nonce: '<?php echo wp_create_nonce('temply_ai_nonce'); ?>',
                                keyword: keyword,
                                genre: genre
                            }, function(res) {
                                btn.prop('disabled', false).html('<svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg> Brainstorm AI');
                                if(res.success && res.data.hooks) {
                                    let html = '';
                                    res.data.hooks.forEach(h => {
                                        html += `<div class="bg-white border border-purple-100 p-2 rounded cursor-pointer hover:bg-purple-100 text-[13px] text-slate-800 transition-colors shadow-sm" onclick="addHook(this)">${h}</div>`;
                                    });
                                    $('#brainstorm-list').html(html);
                                    $('#brainstorm-results').removeClass('hidden');
                                } else {
                                    alert('Có lỗi khi Brainstorm: ' + (res.data.message || 'Server error.'));
                                }
                            }).fail(function() {
                                btn.prop('disabled', false).html('<svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg> Brainstorm AI');
                                alert('Không kết nối được server.');
                            });
                        });
                        
                        // Brainstorm World
                        $('#temply-brainstorm-world-btn').click(function() {
                            const btn = $(this);
                            const keyword = $('#temply-keywords').val();
                            const genre = $('select[name="pilot_genre"]').val();
                            btn.prop('disabled', true).html('<span class="dashicons dashicons-update spin"></span> Đang nặn thế giới...');
                            
                            $.post(ajaxurl, {
                                action: 'temply_ajax_brainstorm_world',
                                nonce: '<?php echo wp_create_nonce('temply_ai_nonce'); ?>',
                                keyword: keyword,
                                genre: genre
                            }, function(res) {
                                btn.prop('disabled', false).html('<svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg> Brainstorm AI');
                                if(res.success && res.data.worlds) {
                                    let html = '';
                                    res.data.worlds.forEach(w => {
                                        html += `<div class="bg-white border border-purple-100 p-2 rounded cursor-pointer hover:bg-purple-100 text-[13px] text-slate-800 transition-colors shadow-sm" onclick="addWorld(this)">${w}</div>`;
                                    });
                                    $('#brainstorm-world-list').html(html);
                                    $('#brainstorm-world-results').removeClass('hidden');
                                } else {
                                    alert('Có lỗi khi Brainstorm World: ' + (res.data.message || 'Server error.'));
                                }
                            }).fail(function() {
                                btn.prop('disabled', false).html('<svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg> Brainstorm AI');
                                alert('Không kết nối được server.');
                            });
                        });
                    });
                    </script>
                </div>
            </div>
            
            <!-- Cột Phải: Bảng Theo Dõi Queue -->
            <div style="flex: 1; min-width: 350px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 20px; border-radius: 12px;">
                    <h2 style="margin-top:0; color:#334155;">📺 Trạm Tín Hiệu (Tiến độ Lò)</h2>
                    
                    <?php if (!$current_config || empty($current_config['queue'])): ?>
                        <div style="background:#fff; border:1px dashed #cbd5e1; padding:20px; text-align:center; color:#94a3b8; border-radius:8px;">
                            Hàng chờ trống rỗng. Hãy ném thêm củi vào lò!
                        </div>
                    <?php else: ?>
                        <div style="margin-bottom:15px; font-size:13px; font-weight:bold; color:#059669;">
                            Tổng tiến độ Kho: <?php echo $done_queue; ?> / <?php echo $total_queue; ?> Truyện.
                        </div>
                        <ul style="list-style:none; padding:0; margin:0; max-height: 500px; overflow-y:auto;">
                            <?php foreach($current_config['queue'] as $idx => $q): ?>
                                <li style="background:#fff; border-left: 4px solid <?php echo ($q['status']==='completed') ? '#94a3b8' : (($q['status']==='writing') ? '#10b981' : '#f59e0b'); ?>; padding: 12px; margin-bottom:10px; border-radius:4px; box-shadow:0 1px 2px rgba(0,0,0,0.05);">
                                    <div style="font-weight:bold; font-size:14px; margin-bottom:5px; <?php if($q['status']==='completed') echo 'text-decoration:line-through;color:#94a3b8;'; ?>">
                                        <?php echo isset($q['title']) ? esc_html($q['title']) : esc_html($q['prompt']); ?>
                                    </div>
                                    <div style="font-size:11px; color:#64748b; margin-bottom:5px;">
                                        (<?php echo isset($q['genre']) ? esc_html($q['genre']) : 'Chưa phân tích'; ?> - 🎯 Target: <?php echo $q['target_chapters']; ?>/c)
                                    </div>
                                    
                                    <?php if($q['status'] === 'writing'): ?>
                                        <div style="background:#d1fae5; color:#065f46; display:inline-block; padding:2px 8px; border-radius:12px; font-size:11px; font-weight:bold;">
                                            ▶ Đang mài mực (Còn <?php echo $q['chapters_left']; ?> Chương)
                                        </div>
                                    <?php elseif($q['status'] === 'draft_outline'): ?>
                                        <div style="background:#fef08a; color:#854d0e; display:inline-block; padding:2px 8px; border-radius:12px; font-size:11px; font-weight:bold;">
                                            📝 Đang dừng ở Dàn ý (Cần duyệt)
                                        </div>
                                    <?php elseif($q['status'] === 'pending'): ?>
                                        <div style="background:#fef3c7; color:#92400e; display:inline-block; padding:2px 8px; border-radius:12px; font-size:11px; font-weight:bold;">
                                            ⏱ Đợi lên dĩa
                                        </div>
                                    <?php else: ?>
                                        <div style="background:#f1f5f9; color:#475569; display:inline-block; padding:2px 8px; border-radius:12px; font-size:11px; font-weight:bold;">
                                            ✓ Đã Xong
                                        </div>
                                    <?php endif; ?>
                                </li>
                            <?php endforeach; ?>
                        </ul>
                        
                        <form method="post" style="margin-top:20px; border-top:1px solid #e2e8f0; padding-top:15px; text-align:center;">
                            <?php wp_nonce_field('temply_auto_pilot_action'); ?>
                            <button type="submit" name="temply_stop_auto_pilot" class="button" style="color:#ef4444; border-color:#fca5a5;" onclick="return confirm('Anh có chắc muốn xoá sạch hàng chờ và huỷ toàn bộ tiến trình không?');">Huỷ Toàn Bộ Lò Ấp</button>
                        </form>
                    <?php endif; ?>
                </div>
            </div>
            
        </div>
    </div>
    <?php
}
