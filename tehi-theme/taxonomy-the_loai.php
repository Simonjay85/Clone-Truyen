<?php
get_header();

$current_term = get_queried_object();
$current_term_id = $current_term ? $current_term->term_id : 0;
$term_name = $current_term ? $current_term->name : 'N/A';
$term_count = $current_term ? $current_term->count : 0;

$all_terms = get_terms([
    'taxonomy' => 'the_loai',
    'hide_empty' => false,
    'number' => 20, // 20 box
    'orderby' => 'count',
    'order' => 'DESC'
]);
?>

<div class="mkm-taxonomy-page" style="margin-top:20px; margin-bottom:40px; padding:0 15px; max-width:1200px; margin-left:auto; margin-right:auto;">
    <!-- Hero Header -->
    <div class="mkm-tax-hero" style="background: linear-gradient(135deg, #f3f4f6 0%, #e5e7eb 100%); border-radius: 16px; padding: 40px 24px; text-align: center; margin-bottom: 24px;">
        <h1 style="font-size:32px; font-weight:800; color:#1f2937; margin:0 0 10px 0;">Khám Phá Thế Giới Truyện</h1>
        <p style="font-size:16px; color:#4b5563; margin:0;">Tuyển chọn hàng ngàn tác phẩm đặc sắc nhất dành riêng cho bạn.</p>
    </div>
    
    <!-- Filters Section -->
    <div class="mkm-tax-filters" style="margin-bottom: 24px;">
        <!-- Genre Chips -->
        <div class="mkm-genre-chips" style="display:flex; flex-wrap:wrap; gap:10px; margin-bottom:20px;">
            <a href="<?php echo get_site_url(); ?>/?post_type=truyen" class="mkm-chip <?php echo (!$current_term_id) ? 'active' : ''; ?>">Tất cả</a>
            <?php foreach($all_terms as $t): 
                $is_active = ($t->term_id === $current_term_id);
                $link = get_term_link($t);
            ?>
                <a href="<?php echo esc_url($link); ?>" class="mkm-chip <?php echo $is_active ? 'active' : ''; ?>"><?php echo esc_html($t->name); ?></a>
            <?php endforeach; ?>
        </div>
        
        <!-- Detailed Filters -->
        <div class="mkm-sort-panel" style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:16px; display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:16px;">
            <div style="display:flex; gap:24px; flex-wrap:wrap;">
                <div>
                    <span style="font-size:11px; font-weight:700; color:#6b7280; text-transform:uppercase; letter-spacing:1px; display:block; margin-bottom:6px;">Trạng thái</span>
                    <div style="display:flex; gap:16px;">
                        <label style="display:flex; align-items:center; gap:6px; cursor:pointer; opacity:0.5; font-size:14px; font-weight:600;"><input type="checkbox" disabled style="margin:0;"> Đang tiến hành</label>
                        <label style="display:flex; align-items:center; gap:6px; cursor:pointer; opacity:0.5; font-size:14px; font-weight:600;"><input type="checkbox" disabled style="margin:0;"> Hoàn thành</label>
                    </div>
                </div>
                <div>
                    <span style="font-size:11px; font-weight:700; color:#6b7280; text-transform:uppercase; letter-spacing:1px; display:block; margin-bottom:6px;">Sắp xếp theo</span>
                    <select style="border:none; background:transparent; font-size:14px; font-weight:700; color:#111827; outline:none; padding:0; cursor:pointer;">
                        <option>Mới nhất</option>
                        <option disabled>Xem nhiều nhất (BETA)</option>
                    </select>
                </div>
            </div>
            
            <div style="font-size:14px; font-weight:600; color:#4f46e5; background:rgba(79,70,229,0.1); padding:8px 16px; border-radius:8px;">
                <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" style="vertical-align:middle; margin-right:4px;"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
                Hiển thị <?php 
                    global $wp_query;
                    echo number_format($wp_query->found_posts);
                ?> kết quả
            </div>
        </div>
    </section>

    <!-- Book Grid (Using mkm styles) -->
    <section class="mkm-grid">
        <?php if (have_posts()) : while (have_posts()) : the_post(); 
            $views = (int)get_post_meta(get_the_ID(), '_views', true);
            if ($views == 0) $views = rand(100, 5000);
            $cover = has_post_thumbnail() ? get_the_post_thumbnail_url(get_the_ID(), 'medium') : 'https://placehold.co/400x600?text=Cover';
            $chaps = wp_count_posts('chuong')->publish;
            
            // Format views
            $formatted_views = $views > 1000 ? round($views/1000, 1) . 'K' : $views;
            
            // Get term name
            $terms = get_the_terms(get_the_ID(), 'the_loai');
            $term_name_display = $terms && !is_wp_error($terms) ? $terms[0]->name : 'Thể loại';
        ?>
        <a href="<?php the_permalink(); ?>" class="mkm-card">
            <div class="mkm-card-img">
                <img src="<?php echo esc_url($cover); ?>" alt="<?php the_title(); ?>"/>
                <div class="mkm-badge-tl">HOT</div>
                <div class="mkm-card-overlay">
                    <div class="mkm-card-title"><?php the_title(); ?></div>
                    <div class="mkm-card-meta">
                        <span style="display:flex;align-items:center;gap:3px;"><svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg> <?php echo $formatted_views; ?></span>
                        <span style="display:flex;align-items:center;gap:3px;"><svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 10h16M4 14h16M4 18h16"/></svg> <?php echo $chaps; ?> Ch</span>
                    </div>
                </div>
            </div>
        </a>
        <?php endwhile; else: ?>
            <div style="grid-column: 1 / -1; text-align: center; padding: 40px; color: #6b7280; font-weight: 500;">Chưa có truyện nào thuộc thể loại này.</div>
        <?php endif; ?>
    </section>

    <!-- Pagination -->
    <nav class="mkm-pagination" style="margin-top: 40px; display: flex; justify-content: center;">
        <?php
            global $wp_query;
            $big = 999999999;
            echo paginate_links([
                'base' => str_replace($big, '%#%', esc_url(get_pagenum_link($big))),
                'format' => '?paged=%#%',
                'current' => max(1, get_query_var('paged')),
                'total' => $wp_query->max_num_pages,
                'prev_text' => '&laquo; Trước',
                'next_text' => 'Sau &raquo;',
                'type' => 'plain',
            ]);
        ?>
    </nav>
</div>

<style>
/* MKM Taxonomic Styles */
.mkm-chip {
    padding: 8px 16px;
    border-radius: 99px;
    background: #f3f4f6;
    color: #4b5563;
    font-size: 14px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.2s;
}
.mkm-chip:hover {
    background: #e5e7eb;
}
.mkm-chip.active {
    background: #4f46e5;
    color: #fff;
    box-shadow: 0 4px 6px -1px rgba(79,70,229,0.3);
}

.mkm-grid {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 14px !important;
    margin-bottom: 0 !important;
}
@media (max-width: 900px) {
    .mkm-grid { grid-template-columns: repeat(3, 1fr) !important; }
}
@media (max-width: 600px) {
    .mkm-grid { grid-template-columns: repeat(2, 1fr) !important; }
}

.mkm-card {
    background: #fff !important;
    border-radius: 12px !important;
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
.mkm-card-overlay {
    position: absolute !important;
    bottom: 0 !important;
    left: 0 !important;
    right: 0 !important;
    background: linear-gradient(0deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.4) 60%, transparent 100%) !important;
    padding: 20px 10px 10px 10px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-end !important;
    z-index: 2 !important;
}
.mkm-card-title {
    color: #fff !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    line-height: 1.3 !important;
    margin-bottom: 6px !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 2 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
}
.mkm-card-meta {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    color: #f3f4f6 !important;
    font-size: 11px !important;
    font-weight: 600 !important;
}

.mkm-pagination a, .mkm-pagination span {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 8px 16px;
    margin: 0 4px;
    border-radius: 8px;
    background: #f3f4f6;
    color: #374151;
    font-weight: 600;
    text-decoration: none;
    font-size: 14px;
    transition: all 0.2s;
}
.mkm-pagination a:hover {
    background: #e5e7eb;
}
.mkm-pagination .current {
    background: #4f46e5;
    color: #fff;
    box-shadow: 0 4px 6px -1px rgba(79,70,229,0.3);
}
</style>

<?php get_footer(); ?>
