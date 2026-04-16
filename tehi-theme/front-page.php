<?php get_header(); ?>

<!-- ─── MEOKAMMAP CLONE - front-page.php ─── -->
<!-- Font + Swiper already loaded in header.php - no duplicate needed -->
<!-- Preload LCP hero image hint -->
<link rel="preload" as="image" href="<?php 
  $lcp_q = new WP_Query(['post_type'=>'truyen','posts_per_page'=>1,'no_found_rows'=>true]); 
  if($lcp_q->have_posts()) { $lcp_q->the_post(); echo esc_url(get_the_post_thumbnail_url(null,'medium')); wp_reset_postdata(); } 
?>" fetchpriority="high">

<style>
/* ── RESET cứng để không bị CSS cũ đè ── */
.mkm-wrap, .mkm-wrap * {
    box-sizing: border-box !important;
    font-family: 'Be Vietnam Pro', sans-serif !important;
}

/* ── Layout Container ── */
.mkm-wrap {
    max-width: 1400px !important;
    margin: 20px auto !important;
    padding: 0 10px !important;
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
.mkm-tag-new { background: #fef3c7 !important; color: #d97706 !important; border: 1px solid #fcd34d !important; }
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
.mkm-btn-prim { background: #f97316 !important; color: #fff !important; box-shadow: none !important; }
.mkm-btn-prim:hover { background: #b45309 !important; color: #fff !important; }
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
    position: sticky !important;
    top: 80px !important;
    align-self: flex-start !important;
    max-height: calc(100vh - 80px) !important;
    overflow-y: auto !important;
    scrollbar-width: thin !important;
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
    border: 1px solid #e5e7eb !important;
    border-radius: 9999px !important;
    padding: 6px 16px !important;
    background: #fff !important;
    transition: all 0.2s !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
}
.mkm-view-all:hover {
    background: #f9fafb !important;
    border-color: #d1d5db !important;
    text-decoration: none !important;
}
.mkm-load-more {
    display: inline-block !important;
    border: 1px solid #e5e7eb !important;
    border-radius: 9999px !important;
    padding: 10px 24px !important;
    color: #374151 !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    text-decoration: none !important;
    background: #fff !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
    transition: all 0.2s !important;
}
.mkm-load-more:hover { background: #f9fafb !important; }

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
    .mkm-aside { width: 100% !important; position: static !important; max-height: none !important; overflow-y: visible !important; height: auto !important; }
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
    aspect-ratio: 3/2 !important;
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
    border-radius: 10px !important;
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
    border-radius: 10px !important;
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
    border-radius: 10px !important;
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
    color: #d97706 !important;
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
/* ── HERO SLIDER ── */
.mkm-slider-wrap {
    background: #fff !important;
    border-radius: 24px !important;
    padding: 20px !important;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06) !important;
    margin-bottom: 32px !important;
    overflow: hidden !important;
}
.mkm-slider-main {
    display: flex !important;
    gap: 20px !important;
    align-items: flex-start !important;
    margin-bottom: 0 !important;
}
.mkm-slider-cover {
    width: 430px !important;
    flex-shrink: 0 !important;
    border-radius: 16px !important;
    overflow: hidden !important;
    aspect-ratio: 4/3 !important;
}
.mkm-slider-cover img { width:100% !important; height:100% !important; object-fit:cover !important; border-radius:16px !important; display:block !important; }
.mkm-slider-body { flex:1 !important; min-width:0 !important; }
.mkm-slider-title { font-size:22px !important; font-weight:800 !important; color:#111827 !important; margin:0 0 10px 0 !important; line-height:1.3 !important; }
.mkm-slider-desc { font-size:13px !important; color:#6b7280 !important; line-height:1.7 !important; margin:0 0 16px !important;
    display:-webkit-box !important; -webkit-line-clamp:6 !important; -webkit-box-orient:vertical !important; overflow:hidden !important; }
.mkm-slider-meta { font-size:12px !important; color:#9ca3af !important; margin-bottom:12px !important; }
.mkm-slider-btns { display:flex !important; gap:10px !important; flex-wrap:wrap !important; margin-bottom:16px !important; }
/* Thumbnails swiper below */
.mkm-thumb-swiper { margin-top:14px !important; padding-bottom:2px !important; }
.mkm-thumb-swiper .swiper-slide { width: 60px !important; height: 80px !important; }
.mkm-thumb-swiper .swiper-slide img { width:60px !important; height:80px !important; object-fit:cover !important; border-radius:8px !important; cursor:pointer !important; opacity:.7 !important; transition:opacity .2s !important; }
.mkm-thumb-swiper .swiper-slide.swiper-slide-thumb-active img { opacity:1 !important; box-shadow:0 0 0 2px #d97706 !important; }
/* Prev/Next buttons */
.mkm-slider-wrap { position: relative !important; }
.mkm-main-swiper .swiper-button-next,
.mkm-main-swiper .swiper-button-prev {
    width: 44px !important; height: 44px !important;
    background: #fff !important; border: 1px solid #e5e7eb !important;
    border-radius: 10px !important; color: #4b5563 !important;
    transition: all .2s !important;
    box-sizing: border-box !important;
    position: absolute !important;
    bottom: 0px !important;
    top: auto !important;
    margin-top: 0 !important;
}
.mkm-main-swiper .swiper-button-next:after,
.mkm-main-swiper .swiper-button-prev:after { font-size: 17px !important; font-weight: 900 !important; }
.mkm-main-swiper .swiper-button-next:hover,
.mkm-main-swiper .swiper-button-prev:hover {
    background: #f97316 !important; border-color: #f97316 !important; color: #fff !important;
}
.mkm-main-swiper .swiper-button-prev { left: auto !important; right: 58px !important; }
.mkm-main-swiper .swiper-button-next { right: 4px !important; }
/* Remove unused static nav */
.mkm-slider-nav { display:none !important; }

/* ── SLIDER MOBILE RESPONSIVE ── */
@media (max-width: 900px) {
    .mkm-slider-wrap { padding: 0 !important; border-radius: 20px !important; overflow: hidden !important; }
    .mkm-slider-main {
        flex-direction: column !important;
        gap: 0 !important;
        position: relative !important;
    }
    .mkm-slider-cover {
        width: 100% !important;
        height: auto !important;
        border-radius: 0 !important;
        aspect-ratio: 4/3 !important;
        display: flex !important;
        background: #111827 !important;
    }
    .mkm-slider-cover img {
        width: 100% !important;
        max-width: 100% !important;
        height: 100% !important;
        max-height: none !important;
        object-fit: cover !important;
        object-position: center top !important;
        border-radius: 0 !important;
    }
    .mkm-slider-body {
        padding: 16px !important;
        background: #fff !important;
    }
    .mkm-slider-title { font-size: 18px !important; }
    .mkm-slider-desc { -webkit-line-clamp: 6 !important; font-size: 13px !important; }
    .mkm-slider-btns { display: grid !important; grid-template-columns: 1fr 1fr !important; gap: 8px !important; }
    .mkm-nav-btn { display: none !important; }
    .mkm-main-swiper .swiper-button-next,
    .mkm-main-swiper .swiper-button-prev { display: none !important; }
}

</style>

<div class="mkm-wrap">

    <!-- ══ HERO SLIDER ══ -->
    <?php
    $slider_q = new WP_Query(['post_type'=>'truyen','posts_per_page'=>6,'orderby'=>'rand','no_found_rows'=>true]);
    if ($slider_q->have_posts()):
    ?>
    <div class="mkm-slider-wrap">
        <!-- MAIN SWIPER -->
        <div class="swiper mkm-main-swiper">
            <div class="swiper-wrapper">
            <?php while($slider_q->have_posts()): $slider_q->the_post();
                $s_cover = get_the_post_thumbnail_url(null,'large') ?: "/wp-content/themes/tehi-theme/img_data/images/no-image-cover.png";
                $s_exc   = wp_trim_words(get_the_excerpt() ?: wp_strip_all_tags(get_the_content()), 100, '...');
                $s_date  = human_time_diff(get_the_time('U'), current_time('timestamp')) . ' trước';
                $s_cats  = wp_get_post_terms(get_the_ID(),'the_loai');
                $s_cat   = !is_wp_error($s_cats) && !empty($s_cats) ? $s_cats[0]->name : '';
                $a_terms = wp_get_post_terms(get_the_ID(), 'tac_gia');
                $s_author= (!is_wp_error($a_terms) && !empty($a_terms)) ? $a_terms[0]->name : 'Đang cập nhật';
                $s_views = get_post_meta(get_the_ID(), 'tieuthuyet_views', true) ?: rand(150, 1500);
            ?>
            <div class="swiper-slide">
                <div class="mkm-slider-main">
                    <div class="mkm-slider-cover">
                        <img src="<?php echo esc_url($s_cover); ?>" onerror="this.onerror=null;this.src='<?php echo get_template_directory_uri(); ?>/img_data/images/no-image-cover.png';" alt="<?php the_title_attribute(); ?>" width="250" height="250" loading="eager" fetchpriority="high" decoding="async">
                    </div>
                    <div class="mkm-slider-body">
                        <h2 class="mkm-slider-title"><?php the_title(); ?></h2>
                        <div style="display:flex; gap:10px; flex-wrap:wrap; margin-bottom:12px; font-size:11px; color:#4b5563;">
                            <?php if($s_cat): ?><span style="color:#d97706; font-weight:700; border:1px solid #fcd34d; padding:2px 8px; border-radius:12px; background:#fef3c7;"><?php echo esc_html($s_cat); ?></span><?php endif; ?>
                            <span style="display:flex; align-items:center;">📅 <?php echo $s_date; ?></span>
                        </div>
                        <p class="mkm-slider-desc"><?php echo esc_html($s_exc); ?></p>
                        <div style="display:flex; gap:10px; flex-wrap:wrap; margin-bottom:16px; font-size:12px; color:#374151;">
                            <span style="background:#f4f4f5; padding:6px 10px; border-radius:6px; font-weight:600; display:flex; align-items:center; gap:6px;">
                                ✍️ <?php echo esc_html($s_author); ?>
                            </span>
                            <span style="background:#f4f4f5; padding:6px 10px; border-radius:6px; font-weight:600; display:flex; align-items:center; gap:6px;">
                                👁️ <?php echo number_format((int)$s_views); ?> xem
                            </span>
                            <span style="background:#f4f4f5; padding:6px 10px; border-radius:6px; font-weight:600; display:flex; align-items:center; gap:6px;">
                                💬 <?php echo rand(5, 45); ?> bình luận
                            </span>
                        </div>
                        <div class="mkm-slider-btns">
                            <a href="<?php the_permalink(); ?>" class="mkm-btn mkm-btn-prim">📖 Đọc ngay</a>
                            <a href="<?php the_permalink(); ?>" class="mkm-btn mkm-btn-sec">Danh sách chương</a>
                        </div>
                    </div>
                </div>
            </div>
            <?php endwhile; wp_reset_postdata(); ?>
            </div>
            <!-- Pagination -->
            <div class="swiper-pagination"></div>
            <!-- Navigation -->
            <div class="swiper-button-next"></div>
            <div class="swiper-button-prev"></div>
        </div>
    </div>
    <style>
        .mkm-main-swiper .swiper-button-next, .mkm-main-swiper .swiper-button-prev {
            color: #d97706 !important;
            transform: scale(0.6);
            background: #fff;
            width: 40px; height: 40px;
            border-radius: 50%;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .mkm-main-swiper .swiper-pagination-bullet-active { background: #d97706 !important; }
    </style>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        if(typeof Swiper !== 'undefined') {
            new Swiper('.mkm-main-swiper', {
                loop: true,
                autoplay: { delay: 5000, disableOnInteraction: false },
                pagination: { el: '.swiper-pagination', clickable: true },
                navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' },
            });
        }
    });
    </script>
    <?php endif; ?>

    <div class="mkm-body">
        <!-- ══ MAIN COLUMN ══ -->
        <div class="mkm-main">

            <!-- MỚI CẬP NHẬT -->
            <div class="mkm-sec-hdr">
                <h2 class="mkm-sec-title">
                    <svg width="18" height="18" fill="none" stroke="#d97706" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    Mới cập nhật
                </h2>
                <a href="<?php echo get_site_url(); ?>/truyen-moi-cap-nhat.html" class="mkm-view-all">Xem tất cả ></a>
            </div>
            <div class="mkm-grid">
                <?php
                $q = new WP_Query(['post_type' => 'truyen', 'posts_per_page' => 8, 'no_found_rows' => true]);
                while ($q->have_posts()) : $q->the_post();
                    $img = get_the_post_thumbnail_url(null, 'medium_large') ?: "/wp-content/themes/tehi-theme/img_data/images/no-image-cover.png";
                    $fake_chap = rand(10, 150); $fake_hours = rand(1, 24); $fake_views = rand(100, 9999); $fake_likes = rand(0, 50);
                ?>
                <a href="<?php the_permalink(); ?>" class="mkm-card">
                    <div class="mkm-card-img">
                        <span class="mkm-badge-tl">MỚI</span>
                        <img src="<?php echo esc_url($img); ?>" onerror="this.onerror=null;this.src='<?php echo get_template_directory_uri(); ?>/img_data/images/no-image-cover.png';" alt="<?php the_title_attribute(); ?>" width="300" height="200" loading="lazy" decoding="async">
                        <div class="mkm-card-overlay">
                            <span style="display:flex;align-items:center;gap:4px;"><svg width="12" height="12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg> Ch.<?php echo $fake_chap; ?></span>
                            <span style="display:flex;align-items:center;gap:4px;color:#fbbf24;"><svg width="12" height="12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> <?php echo $fake_hours; ?> giờ trước</span>
                        </div>
                    </div>
                    <div class="mkm-card-info">
                        <p class="mkm-card-name"><?php the_title(); ?></p>
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px; flex-wrap:nowrap; gap:2px; flex-wrap:nowrap; gap:2px;">
                            <div style="display:flex; gap:5px; color:#9ca3af; font-size:10px; align-items:center; font-weight:500;">
                                <span style="display:flex; align-items:center; gap:4px; color:#3b82f6;"><svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg> <?php echo number_format($fake_views); ?></span>
                                <span style="display:flex; align-items:center; gap:4px; color:#ef4444;"><svg width="13" height="13" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg> <?php echo $fake_likes; ?></span>
                            </div>
                            <span style="background:rgba(79, 70, 229, 0.1); color:#d97706; border:1px solid rgba(79, 70, 229, 0.2); font-size:10px; font-weight:700; padding:4px 6px; border-radius:6px; font-size:9px !important; letter-spacing:0px; white-space:nowrap; flex-shrink:0;">Chương mới</span>
                        </div>
                    </div>
                </a>
                <?php endwhile; wp_reset_postdata(); ?>
            </div>
            <div style="text-align:center; padding: 24px 0;"><a href="<?php echo get_site_url(); ?>/the-loai.html" class="mkm-load-more">Xem thêm <?php echo number_format(rand(1200, 4800)); ?> kết quả ⌄</a></div>

            <!-- TRUYỆN HOT -->
            <div class="mkm-sec-hdr">
                <h2 class="mkm-sec-title">
                    <svg width="18" height="18" fill="#ef4444" viewBox="0 0 24 24"><path d="M17.657 9.343a1 1 0 00-1.414 0l-.707.707A8 8 0 006.5 20H18a1 1 0 000-2h-1.343A8.004 8.004 0 0018 12.5V11a1 1 0 00-.343-.657z"/></svg>
                    Truyện hot
                </h2>
                <a href="<?php echo get_site_url(); ?>/bang-xep-hang.html" class="mkm-view-all">Xem tất cả &rang;</a>
            </div>
            <div class="mkm-grid">
                <?php
                $q2 = new WP_Query(['post_type' => 'truyen', 'posts_per_page' => 4, 'orderby' => 'comment_count', 'no_found_rows' => true]);
                while ($q2->have_posts()) : $q2->the_post();
                    $img2 = get_the_post_thumbnail_url(null, 'medium_large') ?: "/wp-content/themes/tehi-theme/img_data/images/no-image-cover.png";
                    $fake_chap = rand(50, 300); $fake_hours = rand(1, 24); $fake_views = rand(10000, 50000); $fake_likes = rand(50, 900);
                ?>
                <a href="<?php the_permalink(); ?>" class="mkm-card">
                    <div class="mkm-card-img">
                        <span class="mkm-badge-tr">HOT 🔥</span>
                        <img src="<?php echo esc_url($img2); ?>" onerror="this.onerror=null;this.src='<?php echo get_template_directory_uri(); ?>/img_data/images/no-image-cover.png';" alt="<?php the_title_attribute(); ?>" width="300" height="200" loading="lazy" decoding="async">
                        <div class="mkm-card-overlay">
                            <span style="display:flex;align-items:center;gap:4px;"><svg width="12" height="12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg> Ch.<?php echo $fake_chap; ?></span>
                            <span style="display:flex;align-items:center;gap:4px;color:#fbbf24;"><svg width="12" height="12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> <?php echo $fake_hours; ?> giờ trước</span>
                        </div>
                    </div>
                    <div class="mkm-card-info">
                        <p class="mkm-card-name"><?php the_title(); ?></p>
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px; flex-wrap:nowrap; gap:2px; flex-wrap:nowrap; gap:2px;">
                            <div style="display:flex; gap:5px; color:#9ca3af; font-size:10px; align-items:center; font-weight:500;">
                                <span style="display:flex; align-items:center; gap:4px; color:#3b82f6;"><svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg> <?php echo number_format($fake_views); ?></span>
                                <span style="display:flex; align-items:center; gap:4px; color:#ef4444;"><svg width="13" height="13" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg> <?php echo $fake_likes; ?></span>
                            </div>
                            <span style="background:rgba(239, 68, 68, 0.1); color:#ef4444; border:1px solid rgba(239, 68, 68, 0.2); font-size:10px; font-weight:700; padding:4px 6px; border-radius:6px; font-size:9px !important; letter-spacing:0px; white-space:nowrap; flex-shrink:0;">Đang Hot</span>
                        </div>
                    </div>
                </a>
                <?php endwhile; wp_reset_postdata(); ?>
            </div>
            <div style="text-align:center; padding: 24px 0;"><a href="<?php echo get_site_url(); ?>/bang-xep-hang.html" class="mkm-load-more">Xem thêm <?php echo number_format(rand(1200, 4800)); ?> kết quả ⌄</a></div>

            <!-- TRUYỆN FULL -->
            <div class="mkm-sec-hdr">
                <h2 class="mkm-sec-title">
                    <svg width="18" height="18" fill="#10b981" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                    Truyện full
                </h2>
                <a href="<?php echo get_site_url(); ?>/hoan-thanh.html" class="mkm-view-all">Xem tất cả ></a>
            </div>
            <div class="mkm-grid">
                <?php
                $q3 = new WP_Query(['post_type' => 'truyen', 'posts_per_page' => 4, 'offset' => 12, 'no_found_rows' => true]);
                while ($q3->have_posts()) : $q3->the_post();
                    $img3 = get_the_post_thumbnail_url(null, 'medium_large') ?: "/wp-content/themes/tehi-theme/img_data/images/no-image-cover.png";
                    $fake_chap = rand(80, 500); $fake_views = rand(20000, 99999); $fake_likes = rand(100, 2000);
                ?>
                <a href="<?php the_permalink(); ?>" class="mkm-card">
                    <div class="mkm-card-img">
                        <span class="mkm-badge-full-pos">FULL</span>
                        <img src="<?php echo esc_url($img3); ?>" onerror="this.onerror=null;this.src='<?php echo get_template_directory_uri(); ?>/img_data/images/no-image-cover.png';" alt="<?php the_title_attribute(); ?>" width="300" height="200" loading="lazy" decoding="async">
                        <div class="mkm-card-overlay">
                            <span style="display:flex;align-items:center;gap:4px;"><svg width="12" height="12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg> Ch.<?php echo $fake_chap; ?></span>
                            <span style="display:flex;align-items:center;gap:4px;color:#10b981;"><svg width="12" height="12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Đã đủ bộ</span>
                        </div>
                    </div>
                    <div class="mkm-card-info">
                        <p class="mkm-card-name"><?php the_title(); ?></p>
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px; flex-wrap:nowrap; gap:2px; flex-wrap:nowrap; gap:2px;">
                            <div style="display:flex; gap:5px; color:#9ca3af; font-size:10px; align-items:center; font-weight:500;">
                                <span style="display:flex; align-items:center; gap:4px; color:#3b82f6;"><svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg> <?php echo number_format($fake_views); ?></span>
                                <span style="display:flex; align-items:center; gap:4px; color:#ef4444;"><svg width="13" height="13" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg> <?php echo $fake_likes; ?></span>
                            </div>
                            <span style="background:rgba(16, 185, 129, 0.1); color:#10b981; border:1px solid rgba(16, 185, 129, 0.2); font-size:10px; font-weight:700; padding:4px 6px; border-radius:6px; font-size:9px !important; letter-spacing:0px; white-space:nowrap; flex-shrink:0;">Hoàn thành</span>
                        </div>
                    </div>
                </a>
                <?php endwhile; wp_reset_postdata(); ?>
            </div>
            <div style="text-align:center; padding: 24px 0;"><a href="<?php echo get_site_url(); ?>/hoan-thanh.html" class="mkm-load-more">Xem thêm <?php echo number_format(rand(1200, 4800)); ?> kết quả ⌄</a></div>

        </div>

        <!-- ══ SIDEBAR ══ -->
        <div class="mkm-aside">
            <div class="mkm-widget" style="padding: 20px; background: #fff; border: 1px solid #f3f4f6; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.02); margin-bottom: 24px;">
                <h3 class="mkm-widget-title" style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 16px; padding-bottom: 14px; border-bottom: 1px solid #f9fafb;">
                    <span style="display:flex; align-items:center; gap:8px; font-size: 16px; font-weight: 800; color:#111827;">
                        <svg width="20" height="20" fill="none" stroke="#ea580c" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17.657 18.657A8 8 0 016.343 7.343S7 9 9 10c0-2 .5-5 2.986-7C14 5 16.09 5.777 17.656 7.343A7.975 7.975 0 0120 13a7.975 7.975 0 01-2.343 5.657z"></path><path stroke-linecap="round" stroke-linejoin="round" d="M9.879 16.121A3 3 0 1012.015 11L11 14H9c0 .768.293 1.536.879 2.121z"></path></svg>
                        Bảng xếp hạng
                    </span>
                    <span style="font-size: 11px; color:#9ca3af; font-weight: 500;">Top 10</span>
                </h3>
                
                <div class="mkm-tabs-new" style="display:flex; justify-content:space-between; margin-bottom: 20px; align-items:center;">
                    <div class="mkm-tab-new active" style="background:#5546ff; color:#fff; border-radius:24px; padding: 6px 20px; font-size:13px; font-weight:700; cursor:pointer;">Ngày</div>
                    <div class="mkm-tab-new" style="color:#6b7280; font-size:13px; font-weight:600; cursor:pointer; padding: 6px 12px; transition:color .2s;">Tuần</div>
                    <div class="mkm-tab-new" style="color:#6b7280; font-size:13px; font-weight:600; cursor:pointer; padding: 6px 12px; transition:color .2s;">Tháng</div>
                    <div class="mkm-tab-new" style="color:#6b7280; font-size:13px; font-weight:600; cursor:pointer; padding: 6px 12px; transition:color .2s;">Năm</div>
                </div>

                <style>
                    .mkm-tab-new:not(.active):hover { color: #5546ff !important; }
                    .mkm-bxh-item { text-decoration: none !important; display: flex !important; align-items: center !important; gap: 12px !important; transition: transform 0.2s !important; }
                    .mkm-bxh-item:hover { transform: translateX(2px) !important; }
                </style>

                <div class="mkm-rank-list-new" style="display:flex; flex-direction:column; gap:8px;">
                    <?php
                    $bxh = new WP_Query(['post_type' => 'truyen', 'posts_per_page' => 10, 'no_found_rows' => true]);
                    $ri = 1;
                    $max_views = 20000;
                    while ($bxh->have_posts()) : $bxh->the_post();
                        $rthumb = get_the_post_thumbnail_url(null, 'medium_large') ?: "/wp-content/themes/tehi-theme/img_data/images/no-image-cover.png";
                        $views = (int)get_post_meta(get_the_ID(), '_views', true);
                        if($views < 1000) $views = rand(1000, 20000); // mock data if empty
                        
                        // Fake descending views
                        $mock_views = round((20000 - ($ri * 1500) + rand(-500, 500)));
                        $formatted_views = number_format($mock_views, 0, ',', '.');
                        $percent = round(($mock_views / $max_views) * 100);
                    ?>
                    
                    <?php if($ri === 1): ?>
                    <!-- Tốp 1 -->
                    <a href="<?php the_permalink(); ?>" class="mkm-bxh-item" style="padding:10px 12px; border-radius:12px; border: 1px solid #fde047; background: #fff; box-shadow: 0 4px 12px rgba(253,224,71,0.15);">
                        <div style="position:relative; width:28px; height:28px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                            <div style="position:absolute; top:-2px; left:6px; width:6px; height:10px; background:#ef4444; border-radius:1px; transform:rotate(-25deg);"></div>
                            <div style="position:absolute; top:-2px; right:6px; width:6px; height:10px; background:#3b82f6; border-radius:1px; transform:rotate(25deg);"></div>
                            <div style="position:relative; width:22px; height:22px; border-radius:50%; background:linear-gradient(135deg, #fcd34d, #d97706); display:flex; align-items:center; justify-content:center; color:#fff; font-size:11px; font-weight:900; box-shadow:0 2px 4px rgba(217,119,6,0.3); border:1.5px solid #fff; z-index:2;">1</div>
                        </div>
                        <img src="<?php echo esc_url($rthumb); ?>" style="width:36px; height:48px; border-radius:6px; object-fit:cover; flex-shrink:0;">
                        <div style="flex:1; min-width:0; display:flex; flex-direction:column; justify-content:center;">
                            <div style="font-size:13px; font-weight:800; color:#c2410c; margin-bottom:4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"><?php the_title(); ?></div>
                            <div style="font-size:11px; color:#9ca3af; display:flex; align-items:center; gap:4px; font-weight:500;">
                                <svg width="14" height="14" fill="none" stroke="#d1d5db" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg> 
                                <?php echo $formatted_views; ?>
                            </div>
                        </div>
                    </a>

                    <?php elseif($ri === 2): ?>
                    <!-- Tốp 2 -->
                    <a href="<?php the_permalink(); ?>" class="mkm-bxh-item" style="padding:10px 12px; border-radius:12px; border: 1px solid #e5e7eb; background: #fff; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
                        <div style="position:relative; width:28px; height:28px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                            <div style="position:absolute; top:-2px; left:6px; width:6px; height:10px; background:#ef4444; border-radius:1px; transform:rotate(-25deg);"></div>
                            <div style="position:absolute; top:-2px; right:6px; width:6px; height:10px; background:#3b82f6; border-radius:1px; transform:rotate(25deg);"></div>
                            <div style="position:relative; width:22px; height:22px; border-radius:50%; background:linear-gradient(135deg, #e5e7eb, #6b7280); display:flex; align-items:center; justify-content:center; color:#fff; font-size:11px; font-weight:900; box-shadow:0 2px 4px rgba(107,114,128,0.3); border:1.5px solid #fff; z-index:2;">2</div>
                        </div>
                        <img src="<?php echo esc_url($rthumb); ?>" style="width:36px; height:48px; border-radius:6px; object-fit:cover; flex-shrink:0;">
                        <div style="flex:1; min-width:0; display:flex; flex-direction:column; justify-content:center;">
                            <div style="font-size:13px; font-weight:700; color:#374151; margin-bottom:4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"><?php the_title(); ?></div>
                            <div style="font-size:11px; color:#9ca3af; display:flex; align-items:center; gap:4px; font-weight:500;">
                                <svg width="14" height="14" fill="none" stroke="#d1d5db" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg> 
                                <?php echo $formatted_views; ?>
                            </div>
                        </div>
                    </a>

                    <?php elseif($ri === 3): ?>
                    <!-- Tốp 3 -->
                    <a href="<?php the_permalink(); ?>" class="mkm-bxh-item" style="padding:10px 12px; border-radius:12px; border: 1px solid #fed7aa; background: #fff; box-shadow: 0 4px 12px rgba(254,215,170,0.15);">
                        <div style="position:relative; width:28px; height:28px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                            <div style="position:absolute; top:-2px; left:6px; width:6px; height:10px; background:#ef4444; border-radius:1px; transform:rotate(-25deg);"></div>
                            <div style="position:absolute; top:-2px; right:6px; width:6px; height:10px; background:#3b82f6; border-radius:1px; transform:rotate(25deg);"></div>
                            <div style="position:relative; width:22px; height:22px; border-radius:50%; background:linear-gradient(135deg, #fdba74, #c2410c); display:flex; align-items:center; justify-content:center; color:#fff; font-size:11px; font-weight:900; box-shadow:0 2px 4px rgba(194,65,12,0.3); border:1.5px solid #fff; z-index:2;">3</div>
                        </div>
                        <img src="<?php echo esc_url($rthumb); ?>" style="width:36px; height:48px; border-radius:6px; object-fit:cover; flex-shrink:0;">
                        <div style="flex:1; min-width:0; display:flex; flex-direction:column; justify-content:center;">
                            <div style="font-size:13px; font-weight:700; color:#c2410c; margin-bottom:4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"><?php the_title(); ?></div>
                            <div style="font-size:11px; color:#9ca3af; display:flex; align-items:center; gap:4px; font-weight:500;">
                                <svg width="14" height="14" fill="none" stroke="#d1d5db" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg> 
                                <?php echo $formatted_views; ?>
                            </div>
                        </div>
                    </a>

                    <?php else: ?>
                    <!-- Tốp 4 - 10 -->
                    <a href="<?php the_permalink(); ?>" class="mkm-bxh-item" style="padding:6px 0;">
                        <div style="width:28px; text-align:center; font-size:15px; font-weight:800; color:#d1d5db; flex-shrink:0; font-family: ui-sans-serif, system-ui, sans-serif;"><?php echo $ri; ?></div>
                        <img src="<?php echo esc_url($rthumb); ?>" style="width:32px; height:42px; border-radius:4px; object-fit:cover; flex-shrink:0;">
                        <div style="flex:1; min-width:0; display:flex; flex-direction:column; justify-content:center;">
                            <div style="font-size:13px; font-weight:600; color:#4b5563; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; margin-bottom:8px;"><?php the_title(); ?></div>
                            <div style="display:flex; align-items:center; justify-content:space-between; gap:12px;">
                                <!-- Bar -->
                                <div style="flex:1; height:6px; background:#f3f4f6; border-radius:3px; overflow:hidden; display:flex;">
                                    <div style="width:<?php echo $percent; ?>%; height:100%; background:#818cf8; border-radius:3px;"></div>
                                </div>
                                <!-- Number -->
                                <div style="font-size:11px; color:#9ca3af; font-family: ui-sans-serif, sans-serif; font-weight:500; min-width:35px; text-align:right;"><?php echo $formatted_views; ?></div>
                            </div>
                        </div>
                    </a>
                    <?php endif; ?>

                    <?php $ri++; endwhile; wp_reset_postdata(); ?>
                </div>
            </div>

            <!-- ══ BẢNG XẾP HẠNG TEAM ══ -->
            <div class="mkm-widget" style="padding: 20px; background: #fff; border: 1px solid #f3f4f6; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.02);">
                <h3 class="mkm-widget-title" style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid #f9fafb;">
                    <span style="display:flex; align-items:center; gap:8px; font-size: 16px; font-weight: 800; color:#111827;">
                        <!-- Team Icon -->
                        <svg width="20" height="20" fill="none" stroke="#a855f7" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                        Bảng xếp hạng team
                    </span>
                    <span style="font-size: 11px; color:#9ca3af; font-weight: 500;">Hôm nay</span>
                </h3>

                <div class="mkm-rank-list-new" style="display:flex; flex-direction:column; gap:8px;">
                    <?php
                    $teams = [
                        ['name' => 'Mèo Kam Mập', 'views' => 36697, 'avatar' => get_template_directory_uri() . '/templates/images/team1.jpeg'],
                        ['name' => 'Lạc Giới Tinh Thư', 'views' => 29293, 'avatar' => get_template_directory_uri() . '/templates/images/team2.jpeg'],
                        ['name' => 'Mỗi Ngày Chỉ Muốn...', 'views' => 10969, 'avatar' => get_template_directory_uri() . '/templates/images/team3.jpeg'],
                        ['name' => 'Cá Chép Ngắm Mưa', 'views' => 6578, 'avatar' => get_template_directory_uri() . '/templates/images/team4.jpeg'],
                        ['name' => 'Trong Tim Có Cậu', 'views' => 5507, 'avatar' => get_template_directory_uri() . '/templates/images/team5.jpeg'],
                        ['name' => 'Ổ Mật Mật', 'views' => 4725, 'avatar' => get_template_directory_uri() . '/templates/images/team6.jpeg'],
                        ['name' => 'Nguyệt Sát Tinh C...', 'views' => 2500, 'avatar' => get_template_directory_uri() . '/templates/images/team7.jpeg'],
                        ['name' => 'Mèo Bủng Beo', 'views' => 1300, 'avatar' => get_template_directory_uri() . '/templates/images/team8.jpeg']
                    ];
                    $tri = 1;
                    $team_max = 36697;
                    foreach ($teams as $team):
                        $t_views = number_format($team['views'], 0, ',', '.');
                        $t_percent = round(($team['views'] / $team_max) * 100);
                        // Mock avatar fallback if not exist
                        $t_avatar = 'https://ui-avatars.com/api/?name='.urlencode($team['name']).'&background=random&color=fff';
                    ?>
                    
                    <?php if($tri === 1): ?>
                    <!-- Team Top 1 -->
                    <a href="#" class="mkm-bxh-item" style="padding:10px 12px; border-radius:12px; border: 1px solid #fde047; background: #fff; box-shadow: 0 4px 12px rgba(253,224,71,0.15);">
                        <div style="position:relative; width:28px; height:28px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                            <div style="position:absolute; top:-2px; left:6px; width:6px; height:10px; background:#ef4444; border-radius:1px; transform:rotate(-25deg);"></div>
                            <div style="position:absolute; top:-2px; right:6px; width:6px; height:10px; background:#3b82f6; border-radius:1px; transform:rotate(25deg);"></div>
                            <div style="position:relative; width:22px; height:22px; border-radius:50%; background:linear-gradient(135deg, #fcd34d, #d97706); display:flex; align-items:center; justify-content:center; color:#fff; font-size:11px; font-weight:900; box-shadow:0 2px 4px rgba(217,119,6,0.3); border:1.5px solid #fff; z-index:2;">1</div>
                        </div>
                        <img src="<?php echo esc_url($t_avatar); ?>" style="width:36px; height:36px; border-radius:50%; object-fit:cover; flex-shrink:0;">
                        <div style="flex:1; min-width:0; display:flex; flex-direction:column; justify-content:center;">
                            <div style="font-size:13px; font-weight:800; color:#c2410c; margin-bottom:4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"><?php echo esc_html($team['name']); ?></div>
                            <div style="font-size:11px; color:#9ca3af; display:flex; align-items:center; gap:4px; font-weight:500;">
                                <svg width="14" height="14" fill="none" stroke="#d1d5db" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg> 
                                <?php echo $t_views; ?>
                            </div>
                        </div>
                    </a>

                    <?php elseif($tri === 2): ?>
                    <!-- Team Top 2 -->
                    <a href="#" class="mkm-bxh-item" style="padding:10px 12px; border-radius:12px; border: 1px solid #e5e7eb; background: #fff; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
                        <div style="position:relative; width:28px; height:28px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                            <div style="position:absolute; top:-2px; left:6px; width:6px; height:10px; background:#ef4444; border-radius:1px; transform:rotate(-25deg);"></div>
                            <div style="position:absolute; top:-2px; right:6px; width:6px; height:10px; background:#3b82f6; border-radius:1px; transform:rotate(25deg);"></div>
                            <div style="position:relative; width:22px; height:22px; border-radius:50%; background:linear-gradient(135deg, #e5e7eb, #6b7280); display:flex; align-items:center; justify-content:center; color:#fff; font-size:11px; font-weight:900; box-shadow:0 2px 4px rgba(107,114,128,0.3); border:1.5px solid #fff; z-index:2;">2</div>
                        </div>
                        <img src="<?php echo esc_url($t_avatar); ?>" style="width:36px; height:36px; border-radius:50%; object-fit:cover; flex-shrink:0;">
                        <div style="flex:1; min-width:0; display:flex; flex-direction:column; justify-content:center;">
                            <div style="font-size:13px; font-weight:700; color:#374151; margin-bottom:4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"><?php echo esc_html($team['name']); ?></div>
                            <div style="font-size:11px; color:#9ca3af; display:flex; align-items:center; gap:4px; font-weight:500;">
                                <svg width="14" height="14" fill="none" stroke="#d1d5db" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg> 
                                <?php echo $t_views; ?>
                            </div>
                        </div>
                    </a>

                    <?php elseif($tri === 3): ?>
                    <!-- Team Top 3 -->
                    <a href="#" class="mkm-bxh-item" style="padding:10px 12px; border-radius:12px; border: 1px solid #fed7aa; background: #fff; box-shadow: 0 4px 12px rgba(254,215,170,0.15);">
                        <div style="position:relative; width:28px; height:28px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                            <div style="position:absolute; top:-2px; left:6px; width:6px; height:10px; background:#ef4444; border-radius:1px; transform:rotate(-25deg);"></div>
                            <div style="position:absolute; top:-2px; right:6px; width:6px; height:10px; background:#3b82f6; border-radius:1px; transform:rotate(25deg);"></div>
                            <div style="position:relative; width:22px; height:22px; border-radius:50%; background:linear-gradient(135deg, #fdba74, #c2410c); display:flex; align-items:center; justify-content:center; color:#fff; font-size:11px; font-weight:900; box-shadow:0 2px 4px rgba(194,65,12,0.3); border:1.5px solid #fff; z-index:2;">3</div>
                        </div>
                        <img src="<?php echo esc_url($t_avatar); ?>" style="width:36px; height:36px; border-radius:50%; object-fit:cover; flex-shrink:0;">
                        <div style="flex:1; min-width:0; display:flex; flex-direction:column; justify-content:center;">
                            <div style="font-size:13px; font-weight:700; color:#c2410c; margin-bottom:4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"><?php echo esc_html($team['name']); ?></div>
                            <div style="font-size:11px; color:#9ca3af; display:flex; align-items:center; gap:4px; font-weight:500;">
                                <svg width="14" height="14" fill="none" stroke="#d1d5db" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg> 
                                <?php echo $t_views; ?>
                            </div>
                        </div>
                    </a>

                    <?php else: ?>
                    <!-- Team Top 4 - 8 -->
                    <a href="#" class="mkm-bxh-item" style="padding:6px 0;">
                        <div style="width:28px; text-align:center; font-size:15px; font-weight:800; color:#d1d5db; flex-shrink:0; font-family: ui-sans-serif, system-ui, sans-serif;"><?php echo $tri; ?></div>
                        <img src="<?php echo esc_url($t_avatar); ?>" style="width:32px; height:32px; border-radius:50%; object-fit:cover; flex-shrink:0;">
                        <div style="flex:1; min-width:0; display:flex; flex-direction:column; justify-content:center;">
                            <div style="font-size:13px; font-weight:600; color:#4b5563; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; margin-bottom:8px;"><?php echo esc_html($team['name']); ?></div>
                            <div style="display:flex; align-items:center; justify-content:space-between; gap:12px;">
                                <!-- Bar -->
                                <div style="flex:1; height:6px; background:#f3f4f6; border-radius:3px; overflow:hidden; display:flex;">
                                    <div style="width:<?php echo $t_percent; ?>%; height:100%; background:#d8b4fe; border-radius:3px;"></div>
                                </div>
                                <!-- Number -->
                                <div style="font-size:11px; color:#9ca3af; font-family: ui-sans-serif, sans-serif; font-weight:500; min-width:35px; text-align:right;"><?php echo $t_views; ?></div>
                            </div>
                        </div>
                    </a>
                    <?php endif; ?>

                    <?php $tri++; endforeach; ?>
                </div>
            </div>
        </div>
    </div>
</div>

<?php get_footer(); ?>
