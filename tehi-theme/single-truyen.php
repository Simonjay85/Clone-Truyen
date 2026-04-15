<?php get_header(); ?>
<?php if (have_posts()) : while (have_posts()) : the_post(); ?>
<?php
$cover = get_the_post_thumbnail_url(null, 'medium_large') ?: get_template_directory_uri().'/img_data/images/no-image-cover.png';
$terms_loai = wp_get_post_terms(get_the_ID(), 'loai_truyen'); // Might not exist, fallback to "Truyện Chữ"
$terms_tl = wp_get_post_terms(get_the_ID(), 'the_loai');
$terms_nhom = wp_get_post_terms(get_the_ID(), 'nhom_dich');
$author_name = get_post_meta(get_the_ID(), 'truyen_tac_gia', true) ?: 'Đang cập nhật';
$status = 'Đã đủ bộ';
$views = get_post_meta(get_the_ID(), 'truyen_luot_xem', true) ?: rand(1000, 9999);
$likes = get_post_meta(get_the_ID(), 'truyen_yeu_thich', true) ?: rand(100, 500);
$shares = 0;

// Fetch chapters (ensure no orderby cache issues)
$chapters = get_posts([
    'post_type'      => 'chuong',
    'posts_per_page' => -1,
    'meta_key'       => '_truyen_id',
    'meta_value'     => get_the_ID(),
    'orderby'        => 'ID',
    'order'          => 'ASC' // we can reverse it for display
]);

$first_chapter_url = $chapters ? get_permalink($chapters[0]->ID) : '#';
$latest_chapter_url = $chapters ? get_permalink($chapters[count($chapters)-1]->ID) : '#';
?>

<!-- CẤU TRÚC SEO SCHEMA BẮT ĐẦU -->
<script type="application/ld+json">
{
  "@context": "https://schema.org/",
  "@type": "CreativeWorkSeries",
  "name": "<?php echo esc_js(get_the_title()); ?>",
  "author": {
    "@type": "Person",
    "name": "<?php echo esc_js($author_name); ?>"
  },
  "url": "<?php echo esc_url(get_permalink()); ?>",
  "image": "<?php echo esc_url($cover); ?>",
  "description": "<?php echo esc_js(wp_trim_words(wp_strip_all_tags(get_the_content()), 30, '...')); ?>"
}
</script>
<!-- CẤU TRÚC SEO SCHEMA KẾT THÚC -->

<style>
/* ===== SINGLE TRUYEN - PREMIUM REDESIGN ===== */
.mkm-single-wrap {
    width: 100% !important; display: block !important; clear: both !important;
    box-sizing: border-box !important; max-width: 1100px;
    margin: 30px auto; padding: 0 15px; font-family: 'Be Vietnam Pro', ui-sans-serif, system-ui, sans-serif;
    color: #374151;
}
.mkm-single-wrap * { box-sizing: border-box; }

/* ===== HERO CARD ===== */
.mkm-hero {
    position: relative;
    border-radius: 16px;
    overflow: hidden;
    margin-bottom: 24px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.08);
}
.mkm-hero-bg {
    position: absolute; inset: 0;
    background-size: cover; background-position: center;
    filter: blur(24px) saturate(1.5) brightness(0.4);
    transform: scale(1.1);
    z-index: 0;
}
.mkm-hero-inner {
    position: relative; z-index: 1;
    display: grid;
    grid-template-columns: 360px 1fr 180px;
    gap: 28px;
    padding: 28px;
    align-items: start;
}

/* Cover */
.mkm-cover-col { flex-shrink: 0; }
.mkm-cover-col img {
    width: 100%; border-radius: 12px; display: block;
    aspect-ratio: 3/2; object-fit: cover; object-position: center;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
}
.mkm-cover-badge {
    display: flex; gap: 8px; margin-top: 10px; justify-content: center; flex-wrap: wrap;
}
.mkm-cover-badge span {
    background: rgba(255,255,255,0.12); backdrop-filter: blur(8px);
    border: 1px solid rgba(255,255,255,0.2);
    color: #fff; padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: 600;
}

/* Info col */
.mkm-info-col { color: #fff; min-width: 0; }
.mkm-book-title {
    font-size: 26px; font-weight: 800; color: #fff;
    margin: 0 0 8px 0; line-height: 1.3;
    text-shadow: 0 2px 8px rgba(0,0,0,0.4);
}
.mkm-genre-chips { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 16px; }
.mkm-genre-chip {
    padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: 700;
    backdrop-filter: blur(8px); cursor: pointer; text-decoration: none;
    background: rgba(99,102,241,0.35); border: 1px solid rgba(99,102,241,0.5); color: #e0e7ff;
    transition: background .2s;
}
.mkm-genre-chip:hover { background: rgba(99,102,241,0.6); color: #fff; }

.mkm-info-grid {
    display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 16px;
}
.mkm-info-item {
    background: rgba(255,255,255,0.08); backdrop-filter: blur(8px);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 10px; padding: 10px 14px;
    display: flex; flex-direction: column; gap: 3px;
}
.mkm-info-item .lbl { font-size: 10px; color: rgba(255,255,255,0.55); text-transform: uppercase; letter-spacing: .8px; font-weight: 600; }
.mkm-info-item .val { font-size: 14px; font-weight: 700; color: #fff; }

.mkm-synopsis-box {
    background: rgba(0,0,0,0.25); backdrop-filter: blur(8px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 10px; padding: 14px 16px;
    font-size: 13px; line-height: 1.7; color: rgba(255,255,255,0.82);
    margin-bottom: 16px;
}
.mkm-synopsis-box a { color: #a78bfa; text-decoration: none; font-weight: 600; }

.mkm-action-btns { display: flex; gap: 12px; }
.mkm-btn-prim {
    flex: 1; text-align: center; background: #f97316; color: #fff;
    padding: 12px 0; border-radius: 10px; font-weight: 700; text-decoration: none;
    transition: all .2s; font-size: 14px; display: flex; align-items: center; justify-content: center; gap: 6px;
}
.mkm-btn-prim:hover { background: #ea580c; color: #fff; transform: translateY(-1px); }
.mkm-btn-sec {
    flex: 1; text-align: center; background: #10b981; color: #fff;
    padding: 12px 0; border-radius: 10px; font-weight: 700; text-decoration: none;
    transition: all .2s; font-size: 14px; display: flex; align-items: center; justify-content: center; gap: 6px;
}
.mkm-btn-sec:hover { background: #059669; color: #fff; transform: translateY(-1px); }

/* Stats col */
.mkm-stats-col {
    display: flex; flex-direction: column; gap: 10px;
}
.mkm-stat-card {
    background: rgba(255,255,255,0.09); backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 12px; padding: 14px 16px;
    text-align: center; color: #fff;
}
.mkm-stat-card .sv { font-size: 22px; font-weight: 800; color: #fff; line-height: 1; }
.mkm-stat-card .sl { font-size: 11px; color: rgba(255,255,255,0.5); margin-top: 4px; font-weight: 600; text-transform: uppercase; letter-spacing: .8px; }
.mkm-stat-card .si { font-size: 20px; margin-bottom: 4px; }

.mkm-status-badge {
    background: rgba(16,185,129,0.2); border: 1px solid rgba(16,185,129,0.4);
    border-radius: 10px; padding: 10px 12px; text-align: center;
    color: #6ee7b7; font-size: 12px; font-weight: 700;
}

.mkm-social-btns {
    display: flex; flex-direction: column; gap: 8px; margin-top: 4px;
}
.mkm-social-btn {
    background: rgba(255,255,255,0.07); border: 1px solid rgba(255,255,255,0.12);
    border-radius: 8px; padding: 8px; color: rgba(255,255,255,0.7); font-size: 12px;
    font-weight: 600; text-align: center; cursor: pointer; transition: all .2s;
    display: flex; align-items: center; justify-content: center; gap: 6px;
}
.mkm-social-btn:hover { background: rgba(255,255,255,0.14); color: #fff; }

/* Chapters Grid */
.mkm-chaps-box { width: 100% !important; clear: both !important; display: block !important; background: #fff; border-radius: 12px; border: 1px solid #e5e7eb; padding: 20px; margin-bottom: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); }
.mkm-chaps-hdr { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 12px; }
.mkm-chaps-hdr select { padding: 8px 12px; border-radius: 8px; border: 1px solid #e5e7eb; font-size: 13px; color: #374151; background:#fff; outline:none;}
.mkm-chaps-hdr input { padding: 8px 12px; border-radius: 8px; border: 1px solid #e5e7eb; font-size: 13px; width: 220px; outline:none; }
.mkm-chaps-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; margin-bottom: 20px; box-sizing: border-box; width: 100%; }

.mkm-chap-card { border: 1px solid #e5e7eb; border-radius: 10px; padding: 12px; display: flex; align-items: center; gap: 12px; text-decoration: none; color: inherit; transition: all .2s; min-width: 0; overflow: hidden; }
.mkm-chap-card:hover { border-color: #6366f1; box-shadow: 0 2px 8px rgba(99,102,241,0.1); }
.mkm-chap-icon { width: 40px; height: 40px; background: #6366f1; border-radius: 10px; color: #fff; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.mkm-chap-txt { flex: 1; min-width: 0; overflow: hidden; }
.mkm-chap-t { font-size: 12px; color: #9ca3af; margin: 0 0 4px 0; display:flex; justify-content:space-between; align-items:center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.mkm-chap-n { font-size: 14px; font-weight: 700; color: #111827; margin: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

/* Rel stories */
.mkm-rel-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }
.mkm-rel-card { border-radius: 10px; overflow: hidden; transition: box-shadow .2s; text-decoration: none; display: block; background: #fff; border: 1px solid #e5e7eb; }
.mkm-rel-card:hover { box-shadow: 0 4px 16px rgba(0,0,0,0.08); transform: translateY(-2px); }
.mkm-rel-img { width: 100%; aspect-ratio: 3/2; object-fit: cover; display: block; }
.mkm-rel-body { padding: 10px 12px; }
.mkm-rel-title { font-weight: 700; color: #111827; margin: 0 0 4px 0; font-size: 13px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.mkm-rel-desc { font-size: 12px; color: #6b7280; margin: 0; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }

/* Responsive */
@media (max-width: 900px) {
    .mkm-hero-inner { grid-template-columns: 200px 1fr; }
    .mkm-stats-col { display: none; }
    .mkm-rel-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
    .mkm-hero { padding: 20px 0; }
    .mkm-hero-inner { grid-template-columns: 1fr; gap: 20px; }
    .mkm-cover-col { max-width: 100%; margin: 0 auto; width: 100%; }
    .mkm-cover-col img { aspect-ratio: 3/2; width: 100%; }
    .mkm-action-btns { flex-direction: row; }
    .mkm-info-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; }
    .mkm-chaps-grid { grid-template-columns: 1fr !important; }
    .mkm-rel-grid { grid-template-columns: repeat(2, 1fr); }
    .mkm-extra-stats { display: none !important; }
}
</style>

<div class="mkm-single-wrap">
    <!-- HERO BLOCK -->
    <div class="mkm-hero">
        <!-- Blurred background from cover -->
        <div class="mkm-hero-bg" style="background-image: url('<?php echo esc_url($cover); ?>')"></div>

        <div class="mkm-hero-inner">
            <!-- Cover Column -->
            <div class="mkm-cover-col">
                <img src="<?php echo esc_url($cover); ?>" alt="<?php the_title_attribute(); ?>" loading="eager" fetchpriority="high">
                <div class="mkm-cover-badge">
                    <span>📖 Truyện Chữ</span>
                    <?php if($status === 'Đã đủ bộ'): ?><span style="background:rgba(16,185,129,0.3); border-color:rgba(16,185,129,0.5);">✅ Đã đủ bộ</span><?php endif; ?>
                </div>

                <!-- Read Buttons (Moved to fill gap) -->
                <div class="mkm-action-btns" style="margin-top: 20px;">
                    <a href="<?php echo esc_url($first_chapter_url); ?>" class="mkm-btn-prim">📖 Đọc từ đầu</a>
                    <a href="<?php echo esc_url($latest_chapter_url); ?>" class="mkm-btn-sec">★ Đọc tập mới</a>
                </div>

                <!-- Extra Quick Stats to fill left column vertically -->
                <div class="mkm-extra-stats" style="margin-top: 20px; background: rgba(0,0,0,0.25); backdrop-filter: blur(10px); border-radius:12px; padding: 16px; border:1px solid rgba(255,255,255,0.08); color:#fff; font-size:13px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                    <div style="display:flex; justify-content:space-between; margin-bottom:12px; align-items:center;">
                        <span style="color:rgba(255,255,255,0.65); display:flex; align-items:center; gap:6px;"><span style="font-size:16px;">⏱️</span> Thời gian đọc</span>
                        <strong style="font-weight:700; color:#e2e8f0; font-family:monospace; font-size:14px;">~<?php echo max(1, round(count($chapters) * 0.5)); ?> giờ</strong>
                    </div>
                    <div style="display:flex; justify-content:space-between; margin-bottom:12px; align-items:center;">
                        <span style="color:rgba(255,255,255,0.65); display:flex; align-items:center; gap:6px;"><span style="font-size:16px;">💬</span> Thảo luận</span>
                        <strong style="font-weight:700; color:#e2e8f0; font-family:monospace; font-size:14px;"><?php echo get_comments_number(); ?> lượt</strong>
                    </div>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="color:rgba(255,255,255,0.65); display:flex; align-items:center; gap:6px;"><span style="font-size:16px;">⭐</span> Đánh giá</span>
                        <strong style="color:#fbbf24; font-weight:800; font-family:monospace; font-size:14px;">4.9/5 <span style="font-size:11px; font-weight:500; font-family:'Be Vietnam Pro',sans-serif; color:rgba(255,255,255,0.5);">(<?php echo rand(120, 999); ?>)</span></strong>
                    </div>
                </div>
            </div>

            <!-- Info Column -->
            <div class="mkm-info-col">
                <h1 class="mkm-book-title"><?php the_title(); ?></h1>

                <!-- Genre chips -->
                <div class="mkm-genre-chips">
                    <?php if(!empty($terms_tl) && !is_wp_error($terms_tl)): foreach($terms_tl as $t): ?>
                    <a href="<?php echo get_term_link($t); ?>" class="mkm-genre-chip"><?php echo esc_html($t->name); ?></a>
                    <?php endforeach; else: ?><span class="mkm-genre-chip">Truyện Hay</span><?php endif; ?>
                </div>

                <!-- Info grid -->
                <div class="mkm-info-grid">
                    <div class="mkm-info-item">
                        <span class="lbl">✍️ Tác giả</span>
                        <span class="val"><?php echo esc_html($author_name); ?></span>
                    </div>
                    <div class="mkm-info-item">
                        <span class="lbl">🕒 Cập nhật</span>
                        <span class="val"><?php echo get_the_date('d/m/Y'); ?></span>
                    </div>
                    <div class="mkm-info-item">
                        <span class="lbl">📚 Số chương</span>
                        <span class="val"><?php echo count($chapters); ?> chương</span>
                    </div>
                    <div class="mkm-info-item">
                        <span class="lbl">🏷️ Nhóm dịch</span>
                        <span class="val"><?php echo !empty($terms_nhom) && !is_wp_error($terms_nhom) ? esc_html($terms_nhom[0]->name) : 'ST'; ?></span>
                    </div>
                </div>

                <!-- Synopsis -->
                <?php
                // Clean content: decode HTML entities first (fix double-escaped <p> tags), then strip
                $raw_synopsis = get_the_content();
                $raw_synopsis = html_entity_decode($raw_synopsis, ENT_QUOTES, 'UTF-8');
                $raw_synopsis = wp_strip_all_tags($raw_synopsis);
                $raw_synopsis = preg_replace('/^#{1,6}\s+/m', '', $raw_synopsis);
                $raw_synopsis = trim($raw_synopsis);
                $synopsis_short = wp_trim_words($raw_synopsis, 50, '...');
                $synopsis_full  = wp_trim_words($raw_synopsis, 500, '...');
                ?>
                <div class="mkm-synopsis-box">
                    <div id="synopFull" style="display:none;"><?php echo nl2br(esc_html($synopsis_full)); ?></div>
                    <div id="synopShort"><?php echo nl2br(esc_html($synopsis_short)); ?></div>
                    <a href="#" onclick="event.preventDefault(); var s=document.getElementById('synopShort'),f=document.getElementById('synopFull'),b=this.closest('.mkm-synopsis-box'); if(f.style.display==='none'){f.style.display='block';s.style.display='none';b.style.maxHeight='400px';this.textContent='▲ Thu gọn';}else{f.style.display='none';s.style.display='block';b.style.maxHeight='200px';this.textContent='▼ Xem toàn bộ';}">▼ Xem toàn bộ</a>
                </div>

                <!-- Action buttons moved to left column -->
            </div>

            <!-- Stats Column -->
            <div class="mkm-stats-col">
                <div class="mkm-stat-card">
                    <div class="si">👁</div>
                    <div class="sv"><?php echo number_format((int)$views); ?></div>
                    <div class="sl">Lượt xem</div>
                </div>
                <div class="mkm-stat-card">
                    <div class="si">👍</div>
                    <div class="sv"><?php echo number_format((int)$likes); ?></div>
                    <div class="sl">Yêu thích</div>
                </div>
                <div class="mkm-stat-card">
                    <div class="si">📚</div>
                    <div class="sv"><?php echo count($chapters); ?></div>
                    <div class="sl">Chương</div>
                </div>

                <div class="mkm-status-badge">✅ <?php echo esc_html($status); ?></div>

                <div class="mkm-social-btns">
                    <button class="mkm-social-btn">♡ Yêu thích</button>
                    <button class="mkm-social-btn">➦ Chia sẻ</button>
                    <button class="mkm-social-btn">⚑ Báo lỗi</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Block 2: Chapters -->
    <div class="mkm-chaps-box">
        <div class="mkm-chaps-hdr">
            <div style="display:flex; gap:10px;">
                <select id="sortChap"><option value="desc">↑↓ Giảm dần</option><option value="asc">↑↓ Tăng dần</option></select>
                <input id="qChap" type="text" placeholder="🔍 Tìm chương">
            </div>
            <div style="font-size:13px; color:#6b7280;">Tổng: <strong><?php echo count($chapters); ?></strong> chương • Trang 1 / 1</div>
        </div>
        
        <script>
        document.getElementById('qChap').addEventListener('keyup', function() {
            var val = this.value.toLowerCase();
            document.querySelectorAll('.mkm-chap-card').forEach(function(el) {
                if(el.innerText.toLowerCase().includes(val)) el.style.display = 'flex';
                else el.style.display = 'none';
            });
        });
        document.getElementById('sortChap').addEventListener('change', function() {
            var order = this.value;
            var numBlocks = document.querySelectorAll('.mkm-chap-card').length;
            document.querySelectorAll('.mkm-chap-card').forEach(function(el, idx) {
                el.style.order = (order === 'asc') ? (numBlocks - idx) : idx;
            });
        });
        </script>
        
        <div class="mkm-chaps-grid">
            <?php 
            if($chapters): 
                // reverse to show newest first similar to screenshot
                $display_chapters = array_reverse($chapters); 
                foreach($display_chapters as $idx => $chap):
                    $chap_num = count($chapters) - $idx;
            ?>
            <a href="<?php echo get_permalink($chap->ID); ?>" class="mkm-chap-card">
                <div class="mkm-chap-icon"><svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg></div>
                <div class="mkm-chap-txt">
                    <p class="mkm-chap-t"><span>Ch. <?php echo $chap_num; ?> &bull; 🕒 <?php echo human_time_diff(get_the_time('U', $chap->ID), current_time('timestamp')); ?> trước</span> <span>👁 <?php echo rand(100,999); ?></span></p>
                    <p class="mkm-chap-n"><?php echo esc_html($chap->post_title); ?></p>
                </div>
            </a>
            <?php endforeach; else: ?>
            <p style="grid-column: span 2; text-align:center; color:#9ca3af; font-size:14px; padding: 20px 0;">Đang cập nhật chương mới.</p>
            <?php endif; ?>
        </div>
        
        <script>
        // Chapter search filter
        document.getElementById('qChap').addEventListener('keyup', function() {
            var val = this.value.toLowerCase();
            var all = document.querySelectorAll('.mkm-chap-card');
            all.forEach(function(el) {
                var match = el.innerText.toLowerCase().includes(val);
                el.style.display = match ? 'flex' : 'none';
            });
        });
        </script>
    </div>
    
    <!-- Block 3: Comments -->
    <div class="mkm-chaps-box">
        <h3 style="font-size:18px; font-weight:800; margin: 0 0 20px 0; color:#111827; display:flex; align-items:center; gap:10px;">
            <div style="width:30px; height:30px; background:#6366f1; border-radius:8px; color:#fff; display:flex; justify-content:center; align-items:center; font-size:16px;">💬</div>
            Bình luận 
            <span style="font-size:13px; font-weight:normal; color:#9ca3af; margin-left:auto;">Chưa có bình luận</span>
        </h3>
        <div style="display:flex; gap:16px;">
            <div style="width:48px; height:48px; border-radius:50%; background:#fcd34d; display:flex; align-items:center; justify-content:center; font-size:24px; flex-shrink:0;">😋</div>
            <div style="flex:1;">
                <textarea rows="2" placeholder="Viết bình luận của bạn..." style="width:100%; border:1px solid #e5e7eb; border-radius:12px; padding:12px 16px; font-size:14px; outline:none; transition:border-color .2s;"></textarea>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-top:10px;">
                    <span style="font-size:12px; color:#9ca3af;">0/300</span>
                    <button style="background:#8b5cf6; color:#fff; border:none; padding:8px 20px; border-radius:24px; font-size:13px; font-weight:600; cursor:pointer;">Đăng bình luận</button>
                </div>
            </div>
        </div>
        <div style="text-align:center; padding:40px 0 20px 0; color:#9ca3af; font-size:14px;">Hãy là người đầu tiên bình luận!</div>
    </div>

    <!-- Block 4: Related Stories -->
    <div class="mkm-chaps-box" style="background:transparent; border:none; padding:0; box-shadow:none;">
        <h3 style="font-size:16px; font-weight:700; margin: 0 0 16px 0; color:#111827;">Gợi ý danh sách truyện liên quan</h3>
        <div class="mkm-rel-grid">
            <?php
            // random 4 stories
            $rel_q = new WP_Query(['post_type'=>'truyen','posts_per_page'=>4,'orderby'=>'rand','no_found_rows'=>true,'post__not_in'=>[get_the_ID()]]);
            if($rel_q->have_posts()): while($rel_q->have_posts()): $rel_q->the_post();
            $rel_cover = get_the_post_thumbnail_url(null, 'medium') ?: get_template_directory_uri().'/img_data/images/no-image-cover.png';
            ?>
            <a href="<?php the_permalink(); ?>" class="mkm-rel-card">
                <img src="<?php echo esc_url($rel_cover); ?>" alt="<?php the_title_attribute(); ?>" class="mkm-rel-img" loading="lazy">
                <div class="mkm-rel-body">
                    <h4 class="mkm-rel-title"><?php echo wp_trim_words(get_the_title(), 10, '...'); ?></h4>
                    <p class="mkm-rel-desc"><?php echo wp_trim_words(get_the_excerpt() ?: wp_strip_all_tags(get_the_content()), 14, '...'); ?></p>
                </div>
            </a>
            <?php endwhile; wp_reset_postdata(); endif; ?>
        </div>
    </div>
</div>

<?php endwhile; endif; ?>
<?php get_footer(); ?>