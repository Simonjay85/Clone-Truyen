<?php get_header(); ?>

<!-- ─── MEOKAMMAP CLONE - front-page.php ─── -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>
/* ── RESET cứng để không bị CSS cũ đè ── */
.mkm-wrap, .mkm-wrap * {
    box-sizing: border-box !important;
    font-family: 'Be Vietnam Pro', sans-serif !important;
}

/* ── Layout Container ── */
.mkm-wrap {
    max-width: 1200px !important;
    margin: 20px auto !important;
    padding: 0 16px !important;
    background: transparent !important;
}

/* ── HERO CARD ── */
.mkm-hero {
    display: flex !important;
    gap: 20px !important;
    background: #fff !important;
    border-radius: 24px !important;
    padding: 20px !important;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06) !important;
    margin-bottom: 32px !important;
    align-items: flex-start !important;
}
.mkm-hero-cover {
    width: 160px !important;
    flex-shrink: 0 !important;
    border-radius: 16px !important;
    overflow: hidden !important;
    aspect-ratio: 3/4 !important;
}
.mkm-hero-cover img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    border-radius: 16px !important;
    display: block !important;
}
.mkm-hero-body {
    flex: 1 !important;
    min-width: 0 !important;
}
.mkm-hero-title {
    font-size: 20px !important;
    font-weight: 800 !important;
    color: #111827 !important;
    margin: 0 0 8px 0 !important;
    line-height: 1.35 !important;
}
.mkm-hero-meta {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 6px !important;
    margin-bottom: 10px !important;
    align-items: center !important;
}
.mkm-tag {
    display: inline-block !important;
    padding: 2px 10px !important;
    border-radius: 20px !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    line-height: 1.6 !important;
}
.mkm-tag-hot { background: #fef3f2 !important; color: #e03d2b !important; border: 1px solid #fecaca !important; }
.mkm-tag-full { background: #f0fdf4 !important; color: #16a34a !important; border: 1px solid #bbf7d0 !important; }
.mkm-tag-new { background: #eef2ff !important; color: #4f46e5 !important; border: 1px solid #c7d2fe !important; }
.mkm-hero-desc {
    font-size: 13px !important;
    color: #6b7280 !important;
    line-height: 1.7 !important;
    margin-bottom: 16px !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 3 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
}
.mkm-hero-btns {
    display: flex !important;
    gap: 10px !important;
    flex-wrap: wrap !important;
}
.mkm-btn {
    padding: 8px 20px !important;
    border-radius: 12px !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    text-decoration: none !important;
    border: none !important;
    cursor: pointer !important;
    transition: all .2s !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
}
.mkm-btn-prim {
    background: #4f46e5 !important;
    color: #fff !important;
    box-shadow: 0 2px 8px rgba(79,70,229,.25) !important;
}
.mkm-btn-prim:hover { background: #4338ca !important; color: #fff !important; }
.mkm-btn-sec {
    background: #f4f4f5 !important;
    color: #374151 !important;
}
.mkm-btn-sec:hover { background: #e4e4e7 !important; color: #374151 !important; }

/* ── MAIN LAYOUT ── */
.mkm-body {
    display: flex !important;
    gap: 24px !important;
    align-items: flex-start !important;
}
.mkm-main {
    flex: 1 !important;
    min-width: 0 !important;
}
.mkm-aside {
    width: 280px !important;
    flex-shrink: 0 !important;
}

/* ── SECTION HEADER ── */
.mkm-sec-hdr {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    margin-bottom: 14px !important;
    margin-top: 30px !important;
}
.mkm-sec-hdr:first-child { margin-top: 0 !important; }
.mkm-sec-title {
    font-size: 17px !important;
    font-weight: 800 !important;
    color: #111827 !important;
    display: flex !important;
    align-items: center !important;
    gap: 7px !important;
    margin: 0 !important;
}
.mkm-view-all {
    font-size: 13px !important;
    color: #4f46e5 !important;
    font-weight: 600 !important;
    text-decoration: none !important;
}
.mkm-view-all:hover { text-decoration: underline !important; }

/* ── GRID ── */
.mkm-grid {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 14px !important;
    margin-bottom: 0 !important;
}
@media (max-width: 900px) {
    .mkm-grid { grid-template-columns: repeat(3, 1fr) !important; }
    .mkm-body { flex-direction: column !important; }
    .mkm-aside { width: 100% !important; }
    .mkm-hero { flex-direction: column !important; }
    .mkm-hero-cover { width: 100% !important; max-width: 200px !important; }
}
@media (max-width: 600px) {
    .mkm-grid { grid-template-columns: repeat(2, 1fr) !important; }
}

/* ── BOOK CARD ── */
.mkm-card {
    background: #fff !important;
    border-radius: 16px !important;
    overflow: hidden !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06) !important;
    transition: box-shadow .2s, transform .2s !important;
    text-decoration: none !important;
    display: block !important;
}
.mkm-card:hover {
    box-shadow: 0 6px 20px rgba(0,0,0,0.12) !important;
    transform: translateY(-2px) !important;
}
.mkm-card-img {
    position: relative !important;
    aspect-ratio: 3/4 !important;
    overflow: hidden !important;
}
.mkm-card-img img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    display: block !important;
    transition: transform .3s !important;
}
.mkm-card:hover .mkm-card-img img { transform: scale(1.05) !important; }
.mkm-badge-tl {
    position: absolute !important;
    top: 8px !important;
    left: 8px !important;
    background: #10b981 !important;
    color: #fff !important;
    font-size: 10px !important;
    font-weight: 700 !important;
    padding: 2px 7px !important;
    border-radius: 6px !important;
    z-index: 2 !important;
}
.mkm-badge-tr {
    position: absolute !important;
    top: 8px !important;
    right: 8px !important;
    background: #ef4444 !important;
    color: #fff !important;
    font-size: 10px !important;
    font-weight: 700 !important;
    padding: 2px 7px !important;
    border-radius: 6px !important;
    z-index: 2 !important;
}
.mkm-badge-full-pos {
    position: absolute !important;
    top: 8px !important;
    right: 8px !important;
    background: #e11d48 !important;
    color: #fff !important;
    font-size: 10px !important;
    font-weight: 700 !important;
    padding: 2px 7px !important;
    border-radius: 6px !important;
    z-index: 2 !important;
}
.mkm-card-overlay {
    position: absolute !important;
    bottom: 0 !important;
    left: 0 !important;
    right: 0 !important;
    padding: 20px 8px 8px 8px !important;
    background: linear-gradient(transparent, rgba(0,0,0,.7)) !important;
    color: #fff !important;
    font-size: 11px !important;
    display: flex !important;
    justify-content: space-between !important;
}
.mkm-card-info {
    padding: 10px 10px 12px 10px !important;
}
.mkm-card-name {
    font-size: 13px !important;
    font-weight: 700 !important;
    color: #111827 !important;
    line-height: 1.4 !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 2 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
    margin: 0 0 4px 0 !important;
}
.mkm-card-chap {
    font-size: 12px !important;
    color: #9ca3af !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}

/* ── SIDEBAR ── */
.mkm-widget {
    background: #fff !important;
    border-radius: 20px !important;
    padding: 16px !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06) !important;
    margin-bottom: 20px !important;
}
.mkm-widget-title {
    font-size: 16px !important;
    font-weight: 800 !important;
    color: #111827 !important;
    margin: 0 0 14px 0 !important;
    display: flex !important;
    align-items: center !important;
    gap: 7px !important;
}
.mkm-tabs {
    display: flex !important;
    gap: 4px !important;
    background: #f4f4f5 !important;
    border-radius: 10px !important;
    padding: 3px !important;
    margin-bottom: 14px !important;
}
.mkm-tab {
    flex: 1 !important;
    text-align: center !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    padding: 5px 0 !important;
    border-radius: 8px !important;
    color: #6b7280 !important;
    cursor: pointer !important;
}
.mkm-tab.active {
    background: #fff !important;
    color: #4f46e5 !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1) !important;
}
.mkm-rank-list {
    list-style: none !important;
    padding: 0 !important;
    margin: 0 !important;
}
.mkm-rank-item {
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    padding: 8px 6px !important;
    border-radius: 12px !important;
    margin-bottom: 4px !important;
    transition: background .15s !important;
    text-decoration: none !important;
}
.mkm-rank-item.top1 {
    background: #fffbeb !important;
    border: 1px solid #fde68a !important;
}
.mkm-rank-item:hover { background: #f9fafb !important; }
.mkm-rank-num {
    width: 22px !important;
    height: 22px !important;
    border-radius: 50% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    flex-shrink: 0 !important;
}
.rn1 { background: #f59e0b !important; color: #fff !important; }
.rn2 { background: #9ca3af !important; color: #fff !important; }
.rn3 { background: #b45309 !important; color: #fff !important; }
.rn-other { background: #f4f4f5 !important; color: #6b7280 !important; }
.mkm-rank-thumb {
    width: 38px !important;
    height: 50px !important;
    border-radius: 8px !important;
    object-fit: cover !important;
    flex-shrink: 0 !important;
}
.mkm-rank-info {
    flex: 1 !important;
    min-width: 0 !important;
}
.mkm-rank-name {
    font-size: 12px !important;
    font-weight: 700 !important;
    color: #111827 !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}
.mkm-rank-views {
    font-size: 11px !important;
    color: #9ca3af !important;
    margin-top: 2px !important;
}
</style>

<div class="mkm-wrap">

    <!-- ══ HERO CARD ══ -->
    <?php
    $hero_q = new WP_Query(['post_type' => 'truyen', 'posts_per_page' => 1, 'orderby' => 'rand', 'no_found_rows' => true]);
    if ($hero_q->have_posts()) : while ($hero_q->have_posts()) : $hero_q->the_post();
        $cover = get_the_post_thumbnail_url(null, 'medium') ?: get_template_directory_uri().'/templates/images/no-image-cover.png';
        $excerpt = wp_trim_words(get_the_excerpt(), 35, '...');
    ?>
    <div class="mkm-hero">
        <div class="mkm-hero-cover">
            <img src="<?php echo esc_url($cover); ?>" alt="<?php the_title_attribute(); ?>" loading="eager">
        </div>
        <div class="mkm-hero-body">
            <h2 class="mkm-hero-title"><?php the_title(); ?></h2>
            <div class="mkm-hero-meta">
                <span class="mkm-tag mkm-tag-hot">🔥 Nổi Bật</span>
                <span class="mkm-tag mkm-tag-full">✅ Hoàn Thành</span>
                <span class="mkm-tag mkm-tag-new">⚡ Mới nhất</span>
            </div>
            <p class="mkm-hero-desc"><?php echo esc_html($excerpt ?: 'Đang cập nhật nội dung...'); ?></p>
            <div class="mkm-hero-btns">
                <a href="<?php the_permalink(); ?>" class="mkm-btn mkm-btn-prim">
                    <svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path d="M9 4.804A7.968 7.968 0 005.5 4c-1.255 0-2.443.29-3.5.804v10A7.969 7.969 0 015.5 14c1.669 0 3.218.51 4.5 1.385A7.962 7.962 0 0114.5 14c1.255 0 2.443.29 3.5.804v-10A7.968 7.968 0 0014.5 4 7.962 7.962 0 0010 5.389 7.962 7.962 0 009 4.804z"/></svg>
                    Đọc ngay
                </a>
                <a href="<?php the_permalink(); ?>" class="mkm-btn mkm-btn-sec">
                    Danh sách chương
                </a>
            </div>
        </div>
    </div>
    <?php endwhile; wp_reset_postdata(); endif; ?>

    <div class="mkm-body">
        <!-- ══ MAIN COLUMN ══ -->
        <div class="mkm-main">

            <!-- MỚI CẬP NHẬT -->
            <div class="mkm-sec-hdr">
                <h2 class="mkm-sec-title">
                    <svg width="18" height="18" fill="none" stroke="#4f46e5" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    Mới cập nhật
                </h2>
                <a href="<?php echo get_site_url(); ?>/truyen-moi-cap-nhat.html" class="mkm-view-all">Xem tất cả →</a>
            </div>
            <div class="mkm-grid">
                <?php
                $q = new WP_Query(['post_type' => 'truyen', 'posts_per_page' => 8, 'no_found_rows' => true]);
                while ($q->have_posts()) : $q->the_post();
                    $img = get_the_post_thumbnail_url(null, 'medium') ?: get_template_directory_uri().'/templates/images/no-image-cover.png';
                ?>
                <a href="<?php the_permalink(); ?>" class="mkm-card">
                    <div class="mkm-card-img">
                        <span class="mkm-badge-tl">MỚI</span>
                        <img src="<?php echo esc_url($img); ?>" alt="<?php the_title_attribute(); ?>" loading="lazy">
                        <div class="mkm-card-overlay">
                            <span>👁 <?php echo number_format(rand(1000,9999)); ?></span>
                            <span>📖 <?php echo rand(50,500); ?></span>
                        </div>
                    </div>
                    <div class="mkm-card-info">
                        <p class="mkm-card-name"><?php the_title(); ?></p>
                        <p class="mkm-card-chap">Chương mới nhất</p>
                    </div>
                </a>
                <?php endwhile; wp_reset_postdata(); ?>
            </div>

            <!-- TRUYỆN HOT -->
            <div class="mkm-sec-hdr">
                <h2 class="mkm-sec-title">
                    <svg width="18" height="18" fill="#ef4444" viewBox="0 0 24 24"><path d="M17.657 9.343a1 1 0 00-1.414 0l-.707.707A8 8 0 006.5 20H18a1 1 0 000-2h-1.343A8.004 8.004 0 0018 12.5V11a1 1 0 00-.343-.657z"/></svg>
                    Truyện hot
                </h2>
                <a href="#" class="mkm-view-all">Xem tất cả →</a>
            </div>
            <div class="mkm-grid">
                <?php
                $q2 = new WP_Query(['post_type' => 'truyen', 'posts_per_page' => 4, 'orderby' => 'comment_count', 'no_found_rows' => true]);
                while ($q2->have_posts()) : $q2->the_post();
                    $img2 = get_the_post_thumbnail_url(null, 'medium') ?: get_template_directory_uri().'/templates/images/no-image-cover.png';
                ?>
                <a href="<?php the_permalink(); ?>" class="mkm-card">
                    <div class="mkm-card-img">
                        <span class="mkm-badge-tr">HOT 🔥</span>
                        <img src="<?php echo esc_url($img2); ?>" alt="<?php the_title_attribute(); ?>" loading="lazy">
                        <div class="mkm-card-overlay">
                            <span>👁 <?php echo number_format(rand(10000, 50000)); ?></span>
                        </div>
                    </div>
                    <div class="mkm-card-info">
                        <p class="mkm-card-name"><?php the_title(); ?></p>
                        <p class="mkm-card-chap">Đang hot</p>
                    </div>
                </a>
                <?php endwhile; wp_reset_postdata(); ?>
            </div>

            <!-- TRUYỆN FULL -->
            <div class="mkm-sec-hdr">
                <h2 class="mkm-sec-title">
                    <svg width="18" height="18" fill="#10b981" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                    Truyện full
                </h2>
                <a href="<?php echo get_site_url(); ?>/hoan-thanh.html" class="mkm-view-all">Xem tất cả →</a>
            </div>
            <div class="mkm-grid">
                <?php
                $q3 = new WP_Query(['post_type' => 'truyen', 'posts_per_page' => 4, 'offset' => 12, 'no_found_rows' => true]);
                while ($q3->have_posts()) : $q3->the_post();
                    $img3 = get_the_post_thumbnail_url(null, 'medium') ?: get_template_directory_uri().'/templates/images/no-image-cover.png';
                ?>
                <a href="<?php the_permalink(); ?>" class="mkm-card">
                    <div class="mkm-card-img">
                        <span class="mkm-badge-full-pos">FULL</span>
                        <img src="<?php echo esc_url($img3); ?>" alt="<?php the_title_attribute(); ?>" loading="lazy">
                    </div>
                    <div class="mkm-card-info">
                        <p class="mkm-card-name"><?php the_title(); ?></p>
                        <p class="mkm-card-chap">Hoàn thành</p>
                    </div>
                </a>
                <?php endwhile; wp_reset_postdata(); ?>
            </div>

        </div>

        <!-- ══ SIDEBAR ══ -->
        <div class="mkm-aside">
            <div class="mkm-widget">
                <h3 class="mkm-widget-title">
                    <svg width="18" height="18" fill="#f59e0b" viewBox="0 0 24 24"><path d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/></svg>
                    Bảng xếp hạng
                </h3>
                <div class="mkm-tabs">
                    <div class="mkm-tab active">Ngày</div>
                    <div class="mkm-tab">Tuần</div>
                    <div class="mkm-tab">Tháng</div>
                </div>
                <ul class="mkm-rank-list">
                    <?php
                    $bxh = new WP_Query(['post_type' => 'truyen', 'posts_per_page' => 10, 'no_found_rows' => true]);
                    $ri = 1;
                    while ($bxh->have_posts()) : $bxh->the_post();
                        $rthumb = get_the_post_thumbnail_url(null, 'thumbnail') ?: get_template_directory_uri().'/templates/images/no-image-cover.png';
                        $rclass = ($ri === 1) ? 'rn1' : (($ri === 2) ? 'rn2' : (($ri === 3) ? 'rn3' : 'rn-other'));
                    ?>
                    <li>
                        <a href="<?php the_permalink(); ?>" class="mkm-rank-item<?php if($ri===1) echo ' top1'; ?>">
                            <span class="mkm-rank-num <?php echo $rclass; ?>"><?php echo $ri <= 3 ? ['🥇','🥈','🥉'][$ri-1] : $ri; ?></span>
                            <img src="<?php echo esc_url($rthumb); ?>" class="mkm-rank-thumb" alt="" loading="lazy">
                            <div class="mkm-rank-info">
                                <div class="mkm-rank-name"><?php the_title(); ?></div>
                                <div class="mkm-rank-views">👁 <?php echo number_format(rand(1000,99999)); ?> lượt đọc</div>
                            </div>
                        </a>
                    </li>
                    <?php $ri++; endwhile; wp_reset_postdata(); ?>
                </ul>
            </div>
        </div>
    </div>
</div>

<?php get_footer(); ?>
