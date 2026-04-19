<?php
/*
Template Name: Danh Mục
*/
global $tehi_tailwind_page;
$tehi_tailwind_page = true;
get_header();

$paged = (get_query_var('paged')) ? get_query_var('paged') : 1;
$query_args = [
    'post_type' => 'truyen',
    'posts_per_page' => 24,
    'paged' => $paged,
    'orderby' => 'date',
    'order' => 'DESC'
];
$directory_query = new WP_Query($query_args);
$total_posts = $directory_query->found_posts;

$all_terms = get_terms([
    'taxonomy' => 'the_loai',
    'hide_empty' => false,
    'number' => 20,
    'orderby' => 'count',
    'order' => 'DESC'
]);
?>

<main class="pt-24 pb-20 px-4 w-full max-w-[95%] 2xl:max-w-[1400px] mx-auto flex-grow">
    <!-- Hero / Header Section -->
    <header class="mb-10 relative overflow-hidden flex flex-col md:flex-row items-center justify-between rounded-[2rem] bg-gradient-to-r from-surface-container-low to-surface-container-highest p-8 md:p-12 border border-gray-200 shadow-sm text-left">
        
        <!-- Background decorative blob -->
        <div class="absolute -top-40 -right-40 w-96 h-96 bg-blue-600/10 rounded-full blur-[80px] pointer-events-none"></div>

        <div class="relative z-10 md:w-3/5">
            <nav class="flex items-center gap-2 text-xs font-bold text-gray-500 mb-6 uppercase tracking-widest">
                <a href="<?php echo home_url(); ?>" class="hover:text-blue-600 transition-colors" style="text-decoration:none;">Trang chủ</a>
                <span class="material-symbols-outlined text-[14px]">chevron_right</span>
                <span class="text-blue-600 border-b border-blue-600/30">Danh Mục</span>
            </nav>
            <h1 class="font-headline text-5xl md:text-6xl font-black tracking-tighter text-gray-900 mb-6" style="margin:0 0 24px 0;line-height:1.2;">
                Thế Giới <span class="bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-blue-400">Truyện</span>
            </h1>
            <p class="text-gray-700 text-lg font-medium leading-relaxed max-w-prose border-l-4 border-blue-600/30 pl-4" style="margin:0;">
                Tuyển chọn hàng ngàn tác phẩm đặc sắc nhất dành riêng cho bạn.
            </p>
        </div>

        <div class="relative z-10 hidden md:block" style="margin-left: auto;">
            <div class="w-56 h-56 rounded-full overflow-hidden border-4 border-white shadow-xl shadow-blue-600/20 transform rotate-3 hover:rotate-0 transition-transform duration-500">
                <img class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBV_SP1Lo5K64DTSZmS8kWMxUUBd-Vbi2TEetTZaMs5X_QwTAja1I0K-yM2KMObZYiWz3ohHAgh0g00e9Om8UE-x3H_0iCihRdoy25RvXkpgjZuvIDQLkB2nJ-Pj6Loo4dJkr1avsg80s9n676nonOdgYCusDVhpBK0U50krmKpNGn0GBFFb1b3OFe2vaWgE_Oui4rW9m2cuyirydWRJh79PHWKIcPjm6WKnIcF9FlQ6CyrvwSe_XDrKwhVV5jGfqbVXFXVariiVeo" alt="Directory Banner"/>
            </div>
        </div>
    </header>
    
    <!-- Filters Section -->
    <div class="mb-12 flex flex-col gap-6 bg-white p-6 rounded-3xl border border-gray-200 shadow-sm">
        <!-- Genre Chips -->
        <div class="flex flex-wrap gap-2 md:gap-3">
            <a href="<?php echo get_site_url(); ?>/?post_type=truyen" class="px-5 py-2 rounded-xl font-bold text-sm transition-all duration-300 bg-blue-600 shadow-md shadow-blue-600/20 text-white">Tất cả</a>
            <?php foreach($all_terms as $t): 
                $link = get_term_link($t);
            ?>
                <a href="<?php echo esc_url($link); ?>" class="px-5 py-2 rounded-xl font-bold text-sm transition-all duration-300 bg-gray-100 text-red-500 hover:text-red-600 hover:bg-red-50"><?php echo esc_html($t->name); ?></a>
            <?php endforeach; ?>
        </div>
        
        <!-- Detailed Filters -->
        <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 pt-4 border-t border-gray-100">
            <div class="flex flex-col sm:flex-row gap-6">
                <div class="flex items-center gap-4">
                    <span class="text-xs font-bold text-red-500 uppercase tracking-widest">Trạng thái</span>
                    <div class="flex gap-3">
                        <label class="flex items-center gap-2 cursor-pointer text-red-500 font-semibold text-sm">
                            <input type="checkbox" disabled class="rounded text-red-500 border-gray-300 focus:ring-red-500"> Đang ra
                        </label>
                        <label class="flex items-center gap-2 cursor-pointer text-red-500 font-semibold text-sm">
                            <input type="checkbox" disabled class="rounded text-red-500 border-gray-300 focus:ring-red-500"> Hoàn Thành
                        </label>
                    </div>
                </div>
                <div class="h-6 w-px bg-gray-200 hidden sm:block"></div>
                <div class="flex items-center gap-4">
                    <span class="text-xs font-bold text-red-500 uppercase tracking-widest">Sắp xếp</span>
                    <select class="mkm-native-select bg-gray-50 border-none text-gray-900 text-sm rounded-lg focus:ring-blue-500 block w-full py-2 px-3 font-semibold ring-1 ring-gray-200" style="appearance: auto; -webkit-appearance: auto;">
                        <option>Mới cập nhật</option>
                        <option>Xem nhiều</option>
                    </select>
                    <style>.mkm-native-select { display: block !important; } .mkm-native-select + .nice-select, .mkm-native-select + .select2-container { display: none !important; }</style>
                </div>
            </div>
            
            <div class="inline-flex items-center gap-2 bg-blue-50 text-blue-600 px-4 py-2 rounded-xl text-sm font-bold shadow-sm">
                <span class="material-symbols-outlined text-[18px]">library_books</span>
                Hiển thị <?php echo number_format($total_posts); ?> truyện
            </div>
        </div>
    </div>

    <!-- Book Grid (Using mkm styles) -->
    <section class="mkm-grid">
        <?php 
        if ($directory_query->have_posts()) :
            while ($directory_query->have_posts()) : $directory_query->the_post();
            $views = (int)get_post_meta(get_the_ID(), '_views', true);
            if ($views == 0) $views = rand(100, 5000);
            $cover = has_post_thumbnail() ? get_the_post_thumbnail_url(get_the_ID(), 'large') : 'https://placehold.co/400x600?text=Cover';
            $chapters_arr = get_posts(['post_type' => 'chuong', 'meta_key' => '_truyen_id', 'meta_value' => get_the_ID(), 'posts_per_page' => -1, 'fields' => 'ids']); $chaps = count($chapters_arr);
            
            // Format views
            $formatted_views = $views > 1000 ? round($views/1000, 1) . 'K' : $views;
            
            // Get term name
            $terms = get_the_terms(get_the_ID(), 'the_loai');
            $term_name_display = $terms && !is_wp_error($terms) ? $terms[0]->name : 'Thể loại';
        ?>
        
        <a href="<?php the_permalink(); ?>" class="mkm-card group" style="background:#fff; border-radius:12px; overflow:hidden; box-shadow:0 1px 4px rgba(0,0,0,0.06); display:block; transition:transform 0.2s, box-shadow 0.2s; border: 1px solid #f3f4f6;">
            <div class="mkm-card-img" style="position:relative; aspect-ratio:3/2; overflow:hidden; background:#f9fafb;">
                <span style="position:absolute; top:8px; left:8px; background:#10b981; color:#fff; font-size:10px; font-weight:700; padding:2px 7px; border-radius:6px; z-index:2; box-shadow:0 2px 4px rgba(0,0,0,0.1);">Ch.<?php echo $chaps; ?></span>
                <img src="<?php echo esc_url($cover); ?>" style="width:100%; height:100%; object-fit:cover; display:block; transition:transform 0.4s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'"/>
                <div style="position:absolute; bottom:0; left:0; right:0; padding:20px 10px 8px 10px; background:linear-gradient(transparent, rgba(0,0,0,.7)); display:flex; justify-content:space-between; align-items:center; color:#fff; font-size:11px; font-weight:600; z-index:1;">
                    <span style="display:flex;align-items:center;gap:3px;"><svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg> <?php echo $formatted_views; ?></span>
                    <span style="display:flex;align-items:center;gap:3px;color:#fbbf24;"><svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> 2 giờ trước</span>
                </div>
            </div>
            <div style="padding:12px;">
                <p style="font-size:14px; font-weight:700; color:#111827; margin:0 0 8px 0; line-height:1.4; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; font-family: ui-sans-serif, sans-serif;"><?php the_title(); ?></p>
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="background:#f3f4f6; color:#6b7280; font-size:10px; font-weight:600; padding:4px 8px; border-radius:6px;"><?php echo esc_html($term_name_display); ?></span>
                    <span style="background:rgba(217, 119, 6, 0.1); color:#d97706; font-size:10px; font-weight:700; padding:4px 8px; border-radius:6px;">Chi tiết</span>
                </div>
            </div>
        </a>
        <?php 
            endwhile; 
            wp_reset_postdata();
        else: ?>
            <div style="grid-column: 1 / -1; text-align: center; padding: 40px; color: #6b7280; font-weight: 500;">Chưa có truyện nào trong danh mục.</div>
        <?php endif; ?>
    </section>

    <!-- Pagination -->
    <nav class="mkm-pagination" style="margin-top: 40px; display: flex; justify-content: center;">
        <?php
            $big = 999999999;
            echo paginate_links([
                'base' => str_replace($big, '%#%', esc_url(get_pagenum_link($big))),
                'format' => '?paged=%#%',
                'current' => max(1, get_query_var('paged')),
                'total' => $directory_query->max_num_pages,
                'prev_text' => '&laquo; Trước',
                'next_text' => 'Sau &raquo;',
                'type' => 'plain',
            ]);
        ?>
    </nav>
</main>

<style>
.mkm-grid { display: grid !important; grid-template-columns: repeat(3, 1fr) !important; gap: 24px !important; margin-bottom: 0 !important; }
@media (max-width: 1024px) { .mkm-grid { grid-template-columns: repeat(3, 1fr) !important; gap: 16px !important; } }
@media (max-width: 640px) { .mkm-grid { grid-template-columns: repeat(2, 1fr) !important; gap: 12px !important; } }
.mkm-card { background: #fff !important; border-radius: 16px !important; overflow: hidden !important; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -2px rgba(0,0,0,0.05) !important; transition: box-shadow 0.3s, transform 0.3s !important; text-decoration: none !important; display: block !important; border: 1px solid rgba(0,0,0,0.05) !important; }
.mkm-card:hover { box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1) !important; transform: translateY(-4px) !important; border-color: rgba(37,99,235,0.2) !important; }
.mkm-card-img { position: relative !important; aspect-ratio: 3/4 !important; overflow: hidden !important; }
.mkm-card-img img { width: 100% !important; height: 100% !important; object-fit: cover !important; display: block !important; transition: transform 0.5s !important; }
.mkm-card:hover .mkm-card-img img { transform: scale(1.08) !important; }
.mkm-badge-tl { position: absolute !important; top: 10px !important; left: 10px !important; background: linear-gradient(135deg, #3b82f6, #2563eb) !important; color: #fff !important; font-size: 10px !important; font-weight: 800 !important; padding: 4px 8px !important; border-radius: 8px !important; z-index: 2 !important; letter-spacing: 0.05em; box-shadow: 0 2px 4px rgba(37,99,235,0.3); }
.mkm-card-overlay { position: absolute !important; bottom: 0 !important; left: 0 !important; right: 0 !important; background: linear-gradient(0deg, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 50%, transparent 100%) !important; padding: 24px 12px 12px 12px !important; display: flex !important; flex-direction: column !important; justify-content: flex-end !important; z-index: 2 !important; }
.mkm-card-title { color: #fff !important; font-size: 15px !important; font-weight: 800 !important; line-height: 1.4 !important; margin-bottom: 8px !important; display: -webkit-box !important; -webkit-line-clamp: 2 !important; -webkit-box-orient: vertical !important; overflow: hidden !important; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }
.mkm-card-meta { display: flex !important; justify-content: space-between !important; align-items: center !important; color: #d1d5db !important; font-size: 12px !important; font-weight: 600 !important; }

.mkm-pagination a, .mkm-pagination span { display: inline-flex; align-items: center; justify-content: center; width: 44px; height: 44px; margin: 0 4px; border-radius: 12px; background: #fff; color: #4b5563; font-weight: 700; text-decoration: none; font-size: 15px; border: 1px solid #e5e7eb; transition: all 0.3s; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
.mkm-pagination a:hover { background: #f8fafc; border-color: #2563eb; color: #2563eb; transform: translateY(-2px); box-shadow: 0 4px 6px -1px rgba(37,99,235,0.1); }
.mkm-pagination .current { background: #2563eb; color: #fff; border-color: #2563eb; box-shadow: 0 4px 12px rgba(37,99,235,0.3); }
</style>

<?php get_footer(); ?>
