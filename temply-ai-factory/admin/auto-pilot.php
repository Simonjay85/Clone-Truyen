<?php
if (!defined('ABSPATH')) exit;

function temply_ai_render_auto_pilot_page() {
    // ── Xử lý nút HUỶ CRON ──
    if (isset($_POST['temply_stop_auto_pilot']) && check_admin_referer('temply_auto_pilot_action')) {
        delete_option('temply_auto_pilot_queue_config');
        wp_clear_scheduled_hook('temply_auto_pilot_cron_hook');
        echo '<div class="notice notice-warning is-dismissible"><p>Đã DỌN SẠCH hàng chờ và tắt trạm phát sóng.</p></div>';
    }

    // ── Xử lý Lên Lịch (từ Wizard Step 3) ──
    if (isset($_POST['temply_schedule_approved']) && check_admin_referer('temply_auto_pilot_action')) {
        $title       = sanitize_text_field($_POST['approved_title'] ?? '');
        $genre       = sanitize_text_field($_POST['approved_genre'] ?? '');
        $tone        = sanitize_text_field($_POST['approved_tone'] ?? '');
        $world       = sanitize_textarea_field($_POST['approved_world'] ?? '');
        $chars       = sanitize_textarea_field($_POST['approved_chars'] ?? '');
        $script      = sanitize_textarea_field($_POST['approved_script'] ?? '');
        $outline     = sanitize_textarea_field($_POST['approved_outline'] ?? '');
        $keyword     = sanitize_textarea_field($_POST['approved_keyword'] ?? '');
        $chapters    = max(1, intval($_POST['approved_chapters'] ?? 20));
        $interval    = sanitize_text_field($_POST['approved_interval'] ?? 'hourly');
        $enable_audit= isset($_POST['approved_enable_audit']) ? 1 : 0;

        if (empty($title)) $title = wp_trim_words($keyword ?: $outline, 8, '...');

        $config = get_option('temply_auto_pilot_queue_config', false);
        if (!$config) {
            $config = ['interval' => $interval, 'queue' => [], 'status' => 'running', 'last_run' => time()];
        }
        $config['interval'] = $interval;
        $config['status']   = 'running';
        $config['queue'][]  = [
            'status'          => 'pending',
            'prompt'          => $keyword,
            'title'           => $title,
            'genre'           => $genre,
            'tone'            => $tone,
            'world'           => $world,
            'chars'           => $chars,
            'script'          => $outline . "\n\n" . $script,
            'hook'            => '',
            'truyen_id'       => 0,
            'target_chapters' => $chapters,
            'chapters_left'   => $chapters,
            'enable_audit'    => $enable_audit,
        ];
        update_option('temply_auto_pilot_queue_config', $config);

        if (!wp_next_scheduled('temply_auto_pilot_cron_hook')) {
            wp_schedule_event(time(), $interval, 'temply_auto_pilot_cron_hook');
        }

        echo '<div class="notice notice-success is-dismissible"><p>✅ Đã đưa <b>' . esc_html($title) . '</b> vào hàng chờ thành công!</p></div>';
    }

    $config     = get_option('temply_auto_pilot_queue_config', false);
    $total_q    = 0;
    $done_q     = 0;
    $active_item= null;
    if ($config && !empty($config['queue'])) {
        foreach ($config['queue'] as $item) {
            $total_q++;
            if ($item['status'] === 'completed') $done_q++;
            if (in_array($item['status'], ['pending','writing']) && !$active_item) $active_item = $item;
        }
    }
    ?>
    <style>
    .apw-wrap { max-width: 960px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }
    .apw-header { margin-bottom: 24px; }
    .apw-header h1 { font-size: 24px; font-weight: 800; color: #1e1e2f; margin: 0 0 6px 0; }
    .apw-header p { color: #666; margin: 0; font-size: 14px; }

    /* ── WIZARD STEPS ── */
    .wizard-steps { display: flex; align-items: center; gap: 0; margin-bottom: 32px; }
    .wizard-step { display: flex; align-items: center; gap: 10px; flex: 1; }
    .wizard-step:not(:last-child)::after { content: ''; flex: 1; height: 2px; background: #e5e7eb; margin: 0 8px; }
    .step-circle { width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700; flex-shrink: 0; transition: all .3s; }
    .step-circle.done  { background: #10b981; color: #fff; }
    .step-circle.active{ background: #4f46e5; color: #fff; box-shadow: 0 0 0 4px rgba(79,70,229,.15); }
    .step-circle.idle  { background: #e5e7eb; color: #9ca3af; }
    .step-label { font-size: 13px; font-weight: 600; color: #374151; white-space: nowrap; }
    .step-label.idle { color: #9ca3af; }

    /* ── PANELS ── */
    .wizard-panel { background: #fff; border-radius: 16px; padding: 24px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); margin-bottom: 20px; display: none; }
    .wizard-panel.visible { display: block; }
    .panel-title { font-size: 16px; font-weight: 800; color: #1e1e2f; margin: 0 0 16px 0; display: flex; align-items: center; gap: 8px; }

    /* ── INPUTS ── */
    .apw-textarea, .apw-input, .apw-select {
        width: 100%; border: 1.5px solid #e5e7eb; border-radius: 10px;
        padding: 10px 14px; font-size: 14px; outline: none;
        transition: border-color .2s, box-shadow .2s; background: #fafafa;
        font-family: inherit; resize: vertical;
    }
    .apw-textarea:focus, .apw-input:focus, .apw-select:focus {
        border-color: #4f46e5; box-shadow: 0 0 0 3px rgba(79,70,229,.12); background: #fff;
    }
    .apw-label { font-size: 13px; font-weight: 700; color: #374151; margin-bottom: 6px; display: block; }
    .apw-field { margin-bottom: 16px; }
    .apw-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }

    /* ── BUTTONS ── */
    .apw-btn { display: inline-flex; align-items: center; gap: 7px; padding: 10px 22px; border-radius: 10px; font-size: 14px; font-weight: 700; cursor: pointer; border: none; transition: all .2s; }
    .apw-btn-primary { background: #4f46e5; color: #fff; box-shadow: 0 2px 8px rgba(79,70,229,.25); }
    .apw-btn-primary:hover { background: #4338ca; }
    .apw-btn-primary:disabled { background: #a5b4fc; cursor: not-allowed; }
    .apw-btn-success { background: #10b981; color: #fff; box-shadow: 0 2px 8px rgba(16,185,129,.25); }
    .apw-btn-success:hover { background: #059669; }
    .apw-btn-danger { background: #ef4444; color: #fff; }
    .apw-btn-danger:hover { background: #dc2626; }
    .apw-btn-ghost { background: #f4f4f5; color: #374151; }
    .apw-btn-ghost:hover { background: #e4e4e7; }

    /* ── AI RESULT BOX ── */
    .ai-result-box { background: linear-gradient(135deg, #f0f4ff, #faf5ff); border: 1px solid #c7d2fe; border-radius: 12px; padding: 16px; margin-top: 16px; display: none; }
    .ai-result-box.visible { display: block; }
    .ai-badge { display: inline-flex; align-items: center; gap: 5px; font-size: 11px; font-weight: 700; color: #4f46e5; background: #ede9fe; padding: 3px 10px; border-radius: 20px; margin-bottom: 12px; }

    /* ── OUTLINE BOX ── */
    .outline-box { background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 12px; font-size: 13px; color: #374151; line-height: 1.7; }

    /* ── QUEUE STATUS ── */
    .queue-card { background: #fff; border-radius: 16px; padding: 20px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); margin-bottom: 20px; border-left: 4px solid #4f46e5; }
    .queue-title { font-size: 15px; font-weight: 700; color: #1e1e2f; margin: 0 0 4px 0; }
    .queue-meta { font-size: 13px; color: #6b7280; }
    .progress-bar { height: 6px; background: #f0f0f0; border-radius: 99px; overflow: hidden; margin-top: 10px; }
    .progress-fill { height: 100%; background: linear-gradient(90deg, #4f46e5, #818cf8); border-radius: 99px; transition: width .5s; }
    .spin { animation: spin 1s linear infinite; display: inline-block; }
    @keyframes spin { to { transform: rotate(360deg); } }
    </style>

    <div class="wrap apw-wrap">
        <div class="apw-header">
            <h1>🤖 Trạm Tiền Phương: Xây Kịch Bản & Xếp Hàng</h1>
            <p>Nhập ý tưởng xô bồ → AI phân tích → Lập dàn ý → Anh duyệt → Máy tự viết cả ngày đêm.</p>
        </div>

        <!-- ── WIZARD STEPS ── -->
        <div class="wizard-steps">
            <div class="wizard-step">
                <div class="step-circle active" id="circle-1">1</div>
                <span class="step-label" id="label-1">Nhập Ý Tưởng</span>
            </div>
            <div class="wizard-step">
                <div class="step-circle idle" id="circle-2">2</div>
                <span class="step-label idle" id="label-2">AI Phân Tích</span>
            </div>
            <div class="wizard-step">
                <div class="step-circle idle" id="circle-3">3</div>
                <span class="step-label idle" id="label-3">Lập Dàn Ý</span>
            </div>
            <div class="wizard-step">
                <div class="step-circle idle" id="circle-4">4</div>
                <span class="step-label idle" id="label-4">Duyệt & Lên Lịch</span>
            </div>
        </div>

        <!-- ══════════════════════════════════════════════ -->
        <!-- STEP 1: NHẬP Ý TƯỞNG -->
        <!-- ══════════════════════════════════════════════ -->
        <div class="wizard-panel visible" id="panel-1">
            <div class="panel-title">💡 Bước 1: Nhập Ý Tưởng / Keyword / Kịch Bản Thô</div>
            <div class="apw-field">
                <label class="apw-label">Ý tưởng của bạn (keyword, tóm tắt hoặc cả kịch bản thô đều OK)</label>
                <textarea id="apw-raw-idea" class="apw-textarea" rows="6" placeholder="Ví dụ: 'Nữ chính giả vờ nghèo khó, bị chồng cũ khinh thường, bỗng được thừa kế tập đoàn nghìn tỷ. Hành trình vả mặt tiểu tam và khẳng định bản thân...'

Hoặc dán thẳng kịch bản chi tiết vào đây. AI sẽ tự phân loại và lập dàn ý."></textarea>
            </div>
            <div style="display:flex; gap:10px; align-items:center;">
                <button type="button" class="apw-btn apw-btn-primary" id="btn-analyze" onclick="apwRunAnalyze()">
                    <svg width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                    AI Phân Tích Ngay
                </button>
                <span id="analyze-status" style="font-size:13px;color:#6b7280;"></span>
            </div>
        </div>

        <!-- ══════════════════════════════════════════════ -->
        <!-- STEP 2: KẾT QUẢ PHÂN TÍCH + CHỈNH SỬA -->
        <!-- ══════════════════════════════════════════════ -->
        <div class="wizard-panel" id="panel-2">
            <div class="panel-title">🧬 Bước 2: AI Gợi Ý — Kiểm Tra & Chỉnh Sửa Nếu Muốn</div>
            <div class="ai-badge visible">✨ Kết quả phân tích bởi Gemini AI</div>
            <div class="apw-row">
                <div class="apw-field">
                    <label class="apw-label">Tên truyện gợi ý</label>
                    <input type="text" id="apw-title" class="apw-input" placeholder="AI sẽ điền vào...">
                </div>
                <div class="apw-field">
                    <label class="apw-label">Số chương (dự kiến)</label>
                    <input type="number" id="apw-chapters" class="apw-input" value="20" min="1" max="500">
                </div>
            </div>
            <div class="apw-row">
                <div class="apw-field">
                    <label class="apw-label">Thể loại</label>
                    <select id="apw-genre" class="apw-select">
                        <option>Drama (Cẩu huyết, Gia đấu, Vả mặt)</option>
                        <option>Tâm Lý Xã Hội</option>
                        <option>Trọng sinh</option>
                        <option>Xuyên không</option>
                        <option>Tu tiên</option>
                        <option>Tổng tài</option>
                        <option>Ngôn tình đô thị</option>
                        <option>Sảng Văn</option>
                        <option>Giả Heo Ăn Thịt Hổ</option>
                        <option>Đô Thị Ẩn Thân</option>
                        <option>Kinh dị Việt Nam</option>
                    </select>
                </div>
                <div class="apw-field">
                    <label class="apw-label">Giọng văn</label>
                    <select id="apw-tone" class="apw-select">
                        <option>Lãng mạn, miêu tả chi tiết cảm xúc</option>
                        <option>Kịch tính, cắt cảnh nhanh, nhiều twist</option>
                        <option>Hài hước, nhẹ nhàng, dễ đọc</option>
                        <option>U tối, tâm lý sâu, hành động căng thẳng</option>
                    </select>
                </div>
            </div>
            <div class="apw-field">
                <label class="apw-label">Tuyến nhân vật</label>
                <textarea id="apw-chars" class="apw-textarea" rows="3" placeholder="AI sẽ gợi ý..."></textarea>
            </div>
            <div class="apw-field">
                <label class="apw-label">Bối cảnh & Thế giới</label>
                <textarea id="apw-world" class="apw-textarea" rows="3" placeholder="AI sẽ gợi ý..."></textarea>
            </div>
            <div style="display:flex; gap:10px; flex-wrap:wrap;">
                <button type="button" class="apw-btn apw-btn-ghost" onclick="apwGoStep(1)">← Nhập lại</button>
                <button type="button" class="apw-btn apw-btn-primary" id="btn-outline" onclick="apwRunOutline()">
                    <svg width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
                    AI Lập Dàn Ý Ngay
                </button>
                <span id="outline-status" style="font-size:13px;color:#6b7280;align-self:center;"></span>
            </div>
        </div>

        <!-- ══════════════════════════════════════════════ -->
        <!-- STEP 3: DÀN Ý + DUYỆT -->
        <!-- ══════════════════════════════════════════════ -->
        <div class="wizard-panel" id="panel-3">
            <div class="panel-title">📋 Bước 3: Kiểm Tra Dàn Ý — Chỉnh Sửa Nếu Muốn</div>
            <div class="apw-field">
                <label class="apw-label">Dàn ý AI gợi ý (Có thể chỉnh thoải mái)</label>
                <textarea id="apw-outline" class="apw-textarea outline-box" rows="18" placeholder="AI đang soạn dàn ý..."></textarea>
            </div>
            <div style="display:flex; gap:10px; flex-wrap:wrap;">
                <button type="button" class="apw-btn apw-btn-ghost" onclick="apwGoStep(2)">← Chỉnh lại</button>
                <button type="button" class="apw-btn apw-btn-success" onclick="apwGoStep(4)">
                    ✅ Dàn ý ổn — Lên Lịch Ngay →
                </button>
            </div>
        </div>

        <!-- ══════════════════════════════════════════════ -->
        <!-- STEP 4: LÊN LỊCH -->
        <!-- ══════════════════════════════════════════════ -->
        <div class="wizard-panel" id="panel-4">
            <div class="panel-title">🚀 Bước 4: Cài Đặt Lịch Chạy & Lên Lò</div>
            <div class="apw-row">
                <div class="apw-field">
                    <label class="apw-label">Số chương cần viết</label>
                    <input type="number" id="apw-chapters-final" class="apw-input" value="20" min="1" max="500">
                </div>
                <div class="apw-field">
                    <label class="apw-label">Tốc độ lò ấp</label>
                    <select id="apw-interval" class="apw-select">
                        <option value="every_five_minutes">Thác Đổ (Mỗi 5 phút 1 Chương)</option>
                        <option value="hourly">Nhỏ Giọt (Mỗi tiếng 1 Chương)</option>
                        <option value="twicedaily">Tà Tà (Ngày 2 Chương)</option>
                    </select>
                </div>
            </div>
            <div class="apw-field" style="display:flex;align-items:center;gap:10px;background:#fefce8;border:1px solid #fde68a;padding:12px;border-radius:10px;">
                <input type="checkbox" id="apw-audit" style="width:18px;height:18px;" checked>
                <label for="apw-audit" style="font-size:13px;font-weight:600;color:#92400e;cursor:pointer;">Bật Auto-Review: AI tự chấm điểm và viết lại chương kém chất lượng</label>
            </div>

            <!-- FORM ẨN GỬI LÊN SERVER -->
            <form method="post" id="apw-schedule-form">
                <?php wp_nonce_field('temply_auto_pilot_action'); ?>
                <input type="hidden" name="temply_schedule_approved" value="1">
                <input type="hidden" name="approved_title" id="f-title">
                <input type="hidden" name="approved_genre" id="f-genre">
                <input type="hidden" name="approved_tone" id="f-tone">
                <input type="hidden" name="approved_world" id="f-world">
                <input type="hidden" name="approved_chars" id="f-chars">
                <input type="hidden" name="approved_keyword" id="f-keyword">
                <input type="hidden" name="approved_outline" id="f-outline">
                <input type="hidden" name="approved_script" id="f-script">
                <input type="hidden" name="approved_chapters" id="f-chapters">
                <input type="hidden" name="approved_interval" id="f-interval">
                <input type="hidden" name="approved_enable_audit" id="f-audit" value="1">
            </form>

            <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 8px;">
                <button type="button" class="apw-btn apw-btn-ghost" onclick="apwGoStep(3)">← Sửa lại dàn ý</button>
                <button type="button" class="apw-btn apw-btn-success" style="font-size:15px;padding:12px 32px;" onclick="apwSubmitSchedule()">
                    🚀 Đẩy Vào Lò Chạy Ngầm
                </button>
            </div>
        </div>

        <!-- ══════════════════════════════════════════════ -->
        <!-- QUEUE STATUS -->
        <!-- ══════════════════════════════════════════════ -->
        <?php if ($config && $total_q > 0): ?>
        <div class="queue-card">
            <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;">
                <div>
                    <div class="queue-title">🏭 Trạm Tin Hiệu (Tiến độ Lò)</div>
                    <div class="queue-meta">Tổng tiến độ Kho: <?php echo $done_q; ?> / <?php echo $total_q; ?> Truyện<?php if ($active_item): ?> · Đang viết: <b><?php echo esc_html($active_item['title'] ?? 'Chưa rõ'); ?></b><?php endif; ?></div>
                </div>
                <form method="post">
                    <?php wp_nonce_field('temply_auto_pilot_action'); ?>
                    <button type="submit" name="temply_stop_auto_pilot" class="apw-btn apw-btn-danger" onclick="return confirm('Dọn sạch toàn bộ hàng chờ?')">
                        🗑 Huỷ Toàn Bộ Lò Áp
                    </button>
                </form>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: <?php echo $total_q > 0 ? round(($done_q/$total_q)*100) : 0; ?>%"></div>
            </div>
            <?php if (!empty($config['queue'])): ?>
            <div style="margin-top:16px; display:flex; flex-direction:column; gap:8px;">
                <?php foreach ($config['queue'] as $qi => $item): ?>
                <?php
                    $scolor = ['pending'=>'#4f46e5','writing'=>'#f59e0b','completed'=>'#10b981','draft_outline'=>'#8b5cf6'][$item['status']] ?? '#aaa';
                    $slabel = ['pending'=>'Đang chờ','writing'=>'Đang viết ✍️','completed'=>'✅ Hoàn thành','draft_outline'=>'Chờ dàn ý'][$item['status']] ?? $item['status'];
                    $done_ch = ($item['target_chapters'] ?? 0) - ($item['chapters_left'] ?? 0);
                ?>
                <div style="background:#fafafa;padding:10px 14px;border-radius:10px;display:flex;align-items:center;gap:12px;border:1px solid #e5e7eb;">
                    <div style="width:8px;height:8px;border-radius:50%;background:<?php echo $scolor; ?>;flex-shrink:0;"></div>
                    <div style="flex:1;">
                        <div style="font-weight:700;font-size:13px;"><?php echo esc_html($item['title'] ?? 'Không rõ'); ?></div>
                        <div style="font-size:12px;color:#6b7280;"><?php echo esc_html($item['genre'] ?? ''); ?> · Chương <?php echo $done_ch; ?>/<?php echo $item['target_chapters'] ?? 0; ?></div>
                    </div>
                    <span style="font-size:12px;font-weight:700;color:<?php echo $scolor; ?>"><?php echo $slabel; ?></span>
                </div>
                <?php endforeach; ?>
            </div>
            <?php endif; ?>
        </div>
        <?php endif; ?>

    </div><!-- /.wrap -->

    <script>
    var apwStep = 1;
    var apwNonce = '<?php echo wp_create_nonce('temply_ai_nonce'); ?>';
    var ajaxUrl  = '<?php echo admin_url('admin-ajax.php'); ?>';

    function apwGoStep(n) {
        // Update circles
        [1,2,3,4].forEach(function(i) {
            var c = document.getElementById('circle-' + i);
            var l = document.getElementById('label-' + i);
            c.className = 'step-circle ' + (i < n ? 'done' : (i === n ? 'active' : 'idle'));
            l.className = 'step-label' + (i > n ? ' idle' : '');
        });
        [1,2,3,4].forEach(function(i) {
            var p = document.getElementById('panel-' + i);
            if (p) p.className = 'wizard-panel' + (i === n ? ' visible' : '');
        });
        apwStep = n;
        // Sync chapters field
        if (n === 4) {
            document.getElementById('apw-chapters-final').value = document.getElementById('apw-chapters').value;
        }
        window.scrollTo({top: 0, behavior: 'smooth'});
    }

    function apwRunAnalyze() {
        var idea = document.getElementById('apw-raw-idea').value.trim();
        if (!idea) { alert('Gõ ý tưởng vào trước đã anh ơi!'); return; }

        var btn = document.getElementById('btn-analyze');
        var st  = document.getElementById('analyze-status');
        btn.disabled = true;
        btn.innerHTML = '<span class="spin">⚙</span> AI đang phân tích...';
        st.textContent = '';

        jQuery.post(ajaxUrl, {
            action: 'temply_ajax_pilot_analyze',
            nonce:  apwNonce,
            keyword: idea
        }, function(res) {
            btn.disabled = false;
            btn.innerHTML = '<svg width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg> AI Phân Tích Ngay';

            if (res.success && res.data) {
                var d = res.data;
                document.getElementById('apw-title').value   = d.title   || '';
                document.getElementById('apw-chapters').value= d.chapters || 20;
                setSelectByText('apw-genre', d.genre);
                setSelectByText('apw-tone',  d.tone);
                document.getElementById('apw-chars').value   = d.chars   || '';
                document.getElementById('apw-world').value   = d.world   || '';
                apwGoStep(2);
            } else {
                st.textContent = '❌ Lỗi: ' + (res.data?.message || 'Không rõ');
            }
        }).fail(function() {
            btn.disabled = false;
            btn.innerHTML = 'AI Phân Tích Ngay';
            st.textContent = '❌ Lỗi kết nối server';
        });
    }

    function apwRunOutline() {
        var btn = document.getElementById('btn-outline');
        var st  = document.getElementById('outline-status');
        btn.disabled = true;
        btn.innerHTML = '<span class="spin">⚙</span> Đang lập dàn ý...';
        st.textContent = '';

        var payload = {
            action:   'temply_ajax_pilot_generate_outline',
            nonce:    apwNonce,
            keyword:  document.getElementById('apw-raw-idea').value,
            title:    document.getElementById('apw-title').value,
            genre:    document.getElementById('apw-genre').value,
            tone:     document.getElementById('apw-tone').value,
            chars:    document.getElementById('apw-chars').value,
            world:    document.getElementById('apw-world').value,
            chapters: document.getElementById('apw-chapters').value
        };

        jQuery.post(ajaxUrl, payload, function(res) {
            btn.disabled = false;
            btn.innerHTML = '<svg width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg> AI Lập Dàn Ý Ngay';

            if (res.success && res.data) {
                document.getElementById('apw-outline').value = res.data.outline || '';
                apwGoStep(3);
            } else {
                st.textContent = '❌ Lỗi: ' + (res.data?.message || 'Không rõ');
            }
        }).fail(function() {
            btn.disabled = false;
            btn.innerHTML = 'AI Lập Dàn Ý Ngay';
            st.textContent = '❌ Lỗi kết nối';
        });
    }

    function apwSubmitSchedule() {
        document.getElementById('f-title').value   = document.getElementById('apw-title').value;
        document.getElementById('f-genre').value   = document.getElementById('apw-genre').value;
        document.getElementById('f-tone').value    = document.getElementById('apw-tone').value;
        document.getElementById('f-world').value   = document.getElementById('apw-world').value;
        document.getElementById('f-chars').value   = document.getElementById('apw-chars').value;
        document.getElementById('f-keyword').value = document.getElementById('apw-raw-idea').value;
        document.getElementById('f-outline').value = document.getElementById('apw-outline').value;
        document.getElementById('f-script').value  = '';
        document.getElementById('f-chapters').value= document.getElementById('apw-chapters-final').value;
        document.getElementById('f-interval').value= document.getElementById('apw-interval').value;
        document.getElementById('f-audit').value   = document.getElementById('apw-audit').checked ? '1' : '0';
        document.getElementById('apw-schedule-form').submit();
    }

    function setSelectByText(id, text) {
        if (!text) return;
        var sel = document.getElementById(id);
        for (var i = 0; i < sel.options.length; i++) {
            if (sel.options[i].text.toLowerCase().indexOf(text.toLowerCase().split(' ')[0]) >= 0) {
                sel.selectedIndex = i; return;
            }
        }
    }
    </script>
    <?php
}
