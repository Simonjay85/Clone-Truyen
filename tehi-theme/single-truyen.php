<?php get_header(); ?>
<?php if (have_posts()) : while (have_posts()) : the_post(); ?>
<?php
$cover = get_the_post_thumbnail_url(null, 'medium_large') ?: get_template_directory_uri().'/templates/images/no-image-cover.png';
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
    'orderby'        => 'name',
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
/* Scoped CSS to override preflight issues on this specific wrapper */
.mkm-single-wrap {
    max-width: 1100px; /* Matched to Meo Xam Map UI */
    margin: 30px auto;
    padding: 0 15px;
    font-family: 'Inter', ui-sans-serif, system-ui, -apple-system, sans-serif;
    color: #374151;
}
.mkm-detail-box { background: #fff; border-radius: 12px; border: 1px solid #e5e7eb; padding: 20px; margin-bottom: 24px; display:flex; gap: 30px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); }
.mkm-cover-col { width: 240px; flex-shrink: 0; }
.mkm-cover-col img { width: 100%; border-radius: 12px; display:block; aspect-ratio: 3/4; object-fit: cover; }
.mkm-info-col { flex: 1; min-width: 0; }
.mkm-book-title { font-size: 24px; font-weight: 800; color: #111827; margin: 0 0 16px 0; line-height: 1.3; }
.mkm-meta-row { display: flex; align-items: flex-start; margin-bottom: 12px; font-size: 13px; }
.mkm-meta-label { width: 100px; color: #6b7280; display:flex; align-items:center; gap:6px; flex-shrink:0; }
.mkm-tags { display: flex; flex-wrap: wrap; gap: 8px; }
.mkm-meta-tag { padding: 4px 12px; border-radius: 20px; border: 1px solid #e5e7eb; font-size: 12px; color: #4b5563; background: #f9fafb; font-weight: 500; }
.mkm-action-btns { display: flex; gap: 16px; margin-top: 24px; margin-bottom: 24px; }
.mkm-btn-prim { flex: 1; text-align:center; background: #f97316; color: #fff; padding: 12px 0; border-radius: 8px; font-weight: 600; text-decoration: none; transition: background .2s; }
.mkm-btn-prim:hover { background: #ea580c; color: #fff; }
.mkm-btn-sec { flex: 1; text-align:center; background: #10b981; color: #fff; padding: 12px 0; border-radius: 8px; font-weight: 600; text-decoration: none; transition: background .2s; }
.mkm-btn-sec:hover { background: #059669; color: #fff; }
.mkm-stat-icons { display: flex; gap: 24px; border-top: 1px solid #f3f4f6; padding-top: 16px; margin-bottom: 16px; font-size: 13px; color: #6b7280; }
.mkm-stat-icons span { display:flex; align-items:center; gap:6px; cursor:pointer; }
.mkm-synopsis { font-size: 14px; color: #4b5563; line-height: 1.6; }

/* Chapters Grid */
.mkm-chaps-box { background: #fff; border-radius: 12px; border: 1px solid #e5e7eb; padding: 20px; margin-bottom: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); }
.mkm-chaps-hdr { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 12px; }
.mkm-chaps-hdr select { padding: 8px 12px; border-radius: 8px; border: 1px solid #e5e7eb; font-size: 13px; color: #374151; background:#fff; outline:none;}
.mkm-chaps-hdr input { padding: 8px 12px; border-radius: 8px; border: 1px solid #e5e7eb; font-size: 13px; width: 220px; outline:none; }
.mkm-chaps-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 20px; }
@media (max-width: 768px) {
    .mkm-detail-box { flex-direction: column; gap:16px;}
    .mkm-cover-col { width: 140px; margin: 0 auto; }
    .mkm-book-title { text-align: center; }
    .mkm-chaps-grid { grid-template-columns: 1fr; }
    .mkm-action-btns { flex-direction: column; }
}
.mkm-chap-card { border: 1px solid #e5e7eb; border-radius: 10px; padding: 12px; display: flex; align-items: center; gap: 12px; text-decoration: none; color: inherit; transition: border-color .2s; }
.mkm-chap-card:hover { border-color: #6366f1; }
.mkm-chap-icon { width: 40px; height: 40px; background: #6366f1; border-radius: 10px; color: #fff; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.mkm-chap-txt { flex: 1; min-width: 0; }
.mkm-chap-t { font-size: 12px; color: #9ca3af; margin: 0 0 4px 0; display:flex; justify-content:space-between; align-items:center;}
.mkm-chap-n { font-size: 14px; font-weight: 700; color: #111827; margin: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

/* Rel stories */
.mkm-rel-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; }
.mkm-rel-card { border: 1px solid #e5e7eb; border-radius: 10px; padding: 16px; transition: box-shadow .2s;}
.mkm-rel-card:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
.mkm-rel-title { font-weight: 700; color: #111827; margin: 0 0 8px 0; font-size:14px; }
.mkm-rel-desc { font-size: 13px; color: #6b7280; margin: 0; }
@media (max-width: 768px) { .mkm-rel-grid { grid-template-columns: 1fr; } }
</style>

<div class="mkm-single-wrap">
    <!-- Block 1: Info -->
    <div class="mkm-detail-box">
        <div class="mkm-cover-col">
            <img src="<?php echo esc_url($cover); ?>" alt="<?php the_title_attribute(); ?>">
        </div>
        <div class="mkm-info-col">
            <h1 class="mkm-book-title"><?php the_title(); ?></h1>
            
            <div class="mkm-meta-row">
                <div class="mkm-meta-label">🏷 Loại</div>
                <div class="mkm-tags"><span class="mkm-meta-tag">Truyện Chữ</span></div>
            </div>
            
            <div class="mkm-meta-row">
                <div class="mkm-meta-label">📚 Thể loại</div>
                <div class="mkm-tags">
                    <?php if(!empty($terms_tl) && !is_wp_error($terms_tl)): foreach($terms_tl as $t): ?>
                    <a href="<?php echo get_term_link($t); ?>" class="mkm-meta-tag"><?php echo esc_html($t->name); ?></a>
                    <?php endforeach; else: ?><span class="mkm-meta-tag">Truyện Hay</span><?php endif; ?>
                </div>
            </div>
            
            <div class="mkm-meta-row">
                <div class="mkm-meta-label">👥 Nhóm dịch</div>
                <div class="mkm-tags">
                    <span class="mkm-meta-tag" style="color:#6366f1; font-weight:600; border-color:#e0e7ff; background:#e0e7ff; cursor:pointer;">Mỗi Ngày Chỉ Muốn Quạc...</span>
                </div>
            </div>
            
            <div class="mkm-meta-row" style="gap:24px;">
                <div style="display:flex; gap:6px;"><span class="mkm-meta-label" style="width:auto;">✍️ Tác giả:</span> <strong style="color:#111827;"><?php echo esc_html($author_name); ?></strong></div>
                <div style="display:flex; gap:6px; color:#9ca3af;"><span class="mkm-meta-label" style="width:auto;">🕒</span> <?php echo get_the_date('d/m/Y'); ?> trước</div>
            </div>
            
            <div class="mkm-meta-row" style="gap:24px; margin-top:20px;">
                <div style="display:flex; gap:6px;"><span class="mkm-meta-label" style="width:auto;">👁 Lượt xem:</span> <strong style="color:#111827;"><?php echo number_format((int)$views); ?></strong></div>
                <div style="display:flex; gap:6px;"><span class="mkm-meta-label" style="width:auto;">👍 Yêu thích:</span> <strong style="color:#111827;"><?php echo number_format((int)$likes); ?></strong></div>
                <div style="display:flex; gap:6px;"><span class="mkm-meta-label" style="width:auto;">✅ Trạng thái:</span> <strong style="color:#10b981;"><?php echo esc_html($status); ?></strong></div>
            </div>
            
            <div class="mkm-action-btns">
                <a href="<?php echo esc_url($first_chapter_url); ?>" class="mkm-btn-prim">📖 Đọc từ đầu</a>
                <a href="<?php echo esc_url($latest_chapter_url); ?>" class="mkm-btn-sec">★ Đọc tập mới</a>
            </div>
            
            <div class="mkm-stat-icons">
                <span>♡ Yêu thích</span>
                <span>➦ Chia sẻ</span>
                <span>⚑ Báo lỗi</span>
            </div>
            
            <div class="mkm-synopsis">
                <?php echo nl2br(esc_html(wp_trim_words(wp_strip_all_tags(get_the_content()), 70, '... '))); ?>
                <a href="#doc-them" style="color:#6366f1; text-decoration:none;">Xem thêm</a>
            </div>
        </div>
    </div>

    <!-- Block 2: Chapters -->
    <div class="mkm-chaps-box">
        <div class="mkm-chaps-hdr">
            <div style="display:flex; gap:10px;">
                <select><option>↑↓ Giảm dần</option><option>↑↓ Tăng dần</option></select>
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
            <p style="grid-column: span 3; text-align:center; color:#9ca3af; font-size:14px; padding: 20px 0;">Đang cập nhật chương mới.</p>
            <?php endif; ?>
        </div>
        
        <!-- Pagination Mock -->
        <div style="display:flex; justify-content:center; gap:10px; margin-top:30px;">
            <button style="padding:8px 20px; border:1px solid #e5e7eb; border-radius:24px; background:#fff; color:#9ca3af; font-size:13px;" disabled>&lsaquo; Trước</button>
            <span style="font-size:14px; align-self:center; margin: 0 10px; color:#374151;">Trang 1 / 1</span>
            <button style="padding:8px 20px; border:1px solid #e5e7eb; border-radius:24px; background:#fff; color:#9ca3af; font-size:13px;" disabled>Sau &rsaquo;</button>
        </div>
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
            ?>
            <a href="<?php the_permalink(); ?>" class="mkm-rel-card" style="text-decoration:none; display:block; background:#fff;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px;">
                    <h4 class="mkm-rel-title"><?php echo wp_trim_words(get_the_title(), 12, '...'); ?></h4>
                    <span style="background:#f1f5f9; padding:4px 10px; border-radius:6px; font-size:11px; font-weight:600; color:#475569;">Xem</span>
                </div>
                <p class="mkm-rel-desc"><?php echo wp_trim_words(get_the_excerpt() ?: wp_strip_all_tags(get_the_content()), 16, '...'); ?></p>
            </a>
            <?php endwhile; wp_reset_postdata(); endif; ?>
        </div>
    </div>
</div>

<?php endwhile; endif; ?>
<?php get_footer(); ?>