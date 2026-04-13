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
    <div class="wrap" style="max-w: 1200px; margin-top:30px;">
        <h1 style="font-size:28px; font-weight:800; color:#1e1e2f; margin-bottom: 5px;">📊 Bệnh Viện Truyện - Tổng Khám & Đại Tu</h1>
        <p style="font-size:15px; color:#555; margin-bottom: 25px;">Giao diện chuyên quét lỗi logic, nhịp điệu trên diện rộng (10-50 chương cùng lúc) và Tự động viết lại hàng loạt.</p>

        <!-- Khâu chọn Truyện -->
        <div style="background: #fff; border: 1px solid #ddd; padding: 20px; border-radius: 12px; margin-bottom: 20px;">
            <form method="get" action="admin.php">
                <input type="hidden" name="page" value="temply-ai-batch-audit">
                <div style="display:flex; gap: 10px; align-items:center;">
                    <strong style="white-space:nowrap;">Chọn Tác Phẩm Khám:</strong>
                    <select name="truyen_id" style="flex:1; border-radius:6px; max-width:400px;">
                        <option value="">-- Chọn 1 Đầu Truyện --</option>
                        <?php foreach($truyen_list as $t): ?>
                            <option value="<?php echo $t->ID; ?>" <?php echo $truyen_id === $t->ID ? 'selected' : ''; ?>><?php echo esc_html($t->post_title); ?></option>
                        <?php endforeach; ?>
                    </select>
                    <button type="submit" class="button button-primary" style="background:#0369a1; border-color:#0284c7;">Mời Bác Sĩ</button>
                </div>
            </form>
        </div>

        <?php if ($truyen_id): 
            $chapters = get_posts([
                'post_type' => 'chuong',
                'posts_per_page' => -1,
                'meta_key' => '_truyen_id',
                'meta_value' => $truyen_id,
                'orderby' => 'menu_order',
                'order' => 'ASC'
            ]);
            
            if(empty($chapters)):
                echo '<div class="notice notice-warning"><p>Truyện này chưa có chương nào!</p></div>';
            else:
        ?>
            <!-- Tổng Quan Story -->
            <div style="display:flex; justify-content:space-between; align-items:flex-end; margin-bottom: 15px;">
                <div>
                    <h2 style="margin:0; font-size: 20px; color: #1e293b;">Hồ Sơ Bệnh Án: <?php echo get_the_title($truyen_id); ?></h2>
                    <p style="margin:5px 0 0 0; color:#64748b;">Tổng số lượng: <?php echo count($chapters); ?> chương</p>
                </div>
                <div style="display:flex; gap:10px;">
                    <select id="batchAiModel" style="border-radius:6px;">
                        <option value="gemini" selected>Google Gemini Flash (Miễn Phí)</option>
                        <option value="claude">Claude Sonnet (Tốn Tiền)</option>
                    </select>
                    <button id="btnMassScan" class="button button-primary button-hero" style="background:#5b21b6; border-color:#4c1d95; text-shadow:none;">🔍 SCAN TOÀN BỘ CHƯƠNG</button>
                    <button id="btnMassFix" class="button button-primary button-hero" style="background:#b91c1c; border-color:#991b1b; text-shadow:none; display:none;">🚑 ĐẠI TU CÁC CHƯƠNG BỆNH</button>
                </div>
            </div>

            <!-- Dashboard Các Chương -->
            <div id="batchProcessBoard" style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; overflow:hidden;">
                <table class="wp-list-table widefat fixed striped table-view-list" style="border:none;">
                    <thead>
                        <tr>
                            <th style="width: 50px;">STT</th>
                            <th style="width: 25%;">Tên Chương</th>
                            <th style="width: 15%;">Trạng Thái</th>
                            <th>Kết Quả Bắt Mạch (AI Nhận Xét)</th>
                            <th style="width: 80px;">Sửa lại</th>
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
                                    <input type="checkbox" class="fix-checkbox" value="<?php echo $chap->ID; ?>" disabled>
                                </td>
                            </tr>
                        <?php endforeach; ?>
                    </tbody>
                </table>
            </div>
            
            <script>
            document.addEventListener('DOMContentLoaded', function() {
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
                        
                        try {
                            const r = await fetch('/wp-admin/admin-ajax.php', {method: 'POST', body: fd});
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
                    }, 3); // 3 requests at a time
                    
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
                        fd.append('custom_summary', 'HÃY CHÚA TỂ BIÊN TẬP: \n' + reviewText + '\n\nYêu cầu: Viết lại Chương này sao cho xoá sổ mọi nhược điểm nói trên. Phải hay, cuốn, mặn mòi.');
                        
                        try {
                            const r = await fetch('/wp-admin/admin-ajax.php', {method: 'POST', body: fd});
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
