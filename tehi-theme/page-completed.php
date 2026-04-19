<?php
/*
Template Name: Truyện Hoàn Thành
*/
global $tehi_tailwind_page;
$tehi_tailwind_page = true;
get_header();

$paged = (get_query_var('paged')) ? get_query_var('paged') : 1;
// Currently no _trang_thai complete flag, so we query all.
$query_args = [
    'post_type' => 'truyen',
    'posts_per_page' => 12,
    'paged' => $paged,
    'orderby' => 'date',
    'order' => 'DESC'
];
$completed_query = new WP_Query($query_args);
$total_posts = $completed_query->found_posts;

$all_terms = get_terms([
    'taxonomy' => 'the_loai',
    'hide_empty' => false,
    'number' => 10, 
    'orderby' => 'count',
    'order' => 'DESC'
]);
?>

<main class="pt-20 pb-16 px-6 w-full max-w-[95%] 2xl:max-w-[1600px] mx-auto flex-grow w-full">
    <!-- Hero / Header Section -->
    <header class="mb-10 relative overflow-hidden flex flex-col md:flex-row items-center justify-between rounded-[2rem] bg-gradient-to-r from-surface-container-low to-surface-container-highest p-8 md:p-12 border border-gray-200 shadow-sm">
        
        <!-- Background decorative blob -->
        <div class="absolute -top-40 -right-40 w-96 h-96 bg-blue-600/10 rounded-full blur-[80px] pointer-events-none"></div>

        <div class="relative z-10 md:w-3/5">
            <nav class="flex items-center gap-2 text-xs font-bold text-gray-500 mb-6 uppercase tracking-widest">
                <a href="<?php echo home_url(); ?>" class="hover:text-blue-600 transition-colors">Trang chủ</a>
                <span class="material-symbols-outlined text-[14px]">chevron_right</span>
                <span class="text-blue-600 border-b border-blue-600/30">Truyện Hoàn Thành</span>
            </nav>
            <h1 class="font-headline text-5xl md:text-6xl font-black tracking-tighter text-gray-900 mb-6" style="line-height:1.2;">
                Hành Trình <span class="bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-blue-400">Trọn Vẹn</span>
            </h1>
            <p class="text-gray-700 text-lg font-medium leading-relaxed max-w-prose border-l-4 border-blue-600/30 pl-4">
                Khám phá những bộ truyện đã đi đến hồi kết. Không còn phải chờ đợi từng chương, hãy tận hưởng trọn vẹn cảm xúc từ đầu đến cuối ngay hôm nay.
            </p>
        </div>

        <div class="relative z-10 hidden md:block">
            <div class="w-56 h-56 rounded-full overflow-hidden border-4 border-white shadow-xl shadow-blue-600/20 transform rotate-3 hover:rotate-0 transition-transform duration-500">
                <img class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBV_SP1Lo5K64DTSZmS8kWMxUUBd-Vbi2TEetTZaMs5X_QwTAja1I0K-yM2KMObZYiWz3ohHAgh0g00e9Om8UE-x3H_0iCihRdoy25RvXkpgjZuvIDQLkB2nJ-Pj6Loo4dJkr1avsg80s9n676nonOdgYCusDVhpBK0U50krmKpNGn0GBFFb1b3OFe2vaWgE_Oui4rW9m2cuyirydWRJh79PHWKIcPjm6WKnIcF9FlQ6CyrvwSe_XDrKwhVV5jGfqbVXFXVariiVeo" alt="Completed Banner"/>
            </div>
        </div>
    </header>

    <div class="flex flex-col lg:flex-row gap-8">
        <!-- Sidebar Filters -->
        <aside class="w-full lg:w-64 space-y-8 sticky lg:top-28 self-start">
            <div>
                <h3 class="font-headline font-bold text-on-surface mb-4 flex items-center gap-2">
                    <span class="material-symbols-outlined text-primary" style="font-variation-settings: 'FILL' 1;">filter_list</span> Bộ lọc
                </h3>
                
                <div class="space-y-6">
                    <!-- Genre Chips Dynamic -->
                    <div class="space-y-3">
                        <label class="text-xs font-bold uppercase tracking-wider text-outline">Thể loại</label>
                        <div class="flex flex-wrap gap-2">
                            <span class="px-3 py-1.5 rounded-md bg-primary text-white text-sm font-medium cursor-pointer shadow-md shadow-primary/20">Tất cả</span>
                            <?php foreach($all_terms as $t): ?>
                                <a href="<?php echo get_term_link($t); ?>" class="px-3 py-1.5 rounded-md bg-surface-container-high text-on-surface-variant text-sm font-medium hover:bg-secondary-container hover:text-on-secondary-container transition-colors cursor-pointer border border-transparent hover:border-outline-variant/30">
                                    <?php echo esc_html($t->name); ?>
                                </a>
                            <?php endforeach; ?>
                        </div>
                    </div>

                    <!-- Rating Static -->
                    <div class="space-y-3 opacity-60 pointer-events-none" title="Chức năng đang cập nhật">
                        <label class="text-xs font-bold uppercase tracking-wider text-outline flex justify-between items-center">
                            Đánh giá <span class="text-[9px] bg-surface-container-highest px-1 rounded text-outline">BETA</span>
                        </label>
                        <div class="space-y-2">
                            <label class="flex items-center gap-3 cursor-pointer group">
                                <div class="w-5 h-5 rounded border-2 border-outline-variant flex items-center justify-center bg-primary border-primary">
                                    <span class="material-symbols-outlined text-xs text-white" style="font-variation-settings: 'FILL' 1;">check</span>
                                </div>
                                <div class="flex text-amber-400">
                                    <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                    <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                    <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                    <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                    <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                </div>
                                <span class="text-sm font-bold text-on-surface">5 Sao</span>
                            </label>
                            <label class="flex items-center gap-3 cursor-pointer group">
                                <div class="w-5 h-5 rounded border-2 border-outline-variant"></div>
                                <div class="flex text-amber-400">
                                    <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                    <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                    <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                    <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                                    <span class="material-symbols-outlined text-sm">star</span>
                                </div>
                                <span class="text-sm text-on-surface-variant">Từ 4 Sao</span>
                            </label>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Recommendation Widget -->
            <div class="p-6 rounded-2xl bg-gradient-to-br from-primary/10 to-primary-container/10 border border-primary/10 shadow-sm relative overflow-hidden group">
                <div class="absolute top-0 right-0 w-16 h-16 bg-primary/10 rounded-full blur-xl transform group-hover:scale-150 transition-transform"></div>
                <h4 class="font-headline font-black text-primary mb-2 flex items-center gap-2 relative z-10"><span class="material-symbols-outlined text-lg">hotel_class</span> Đề cử hôm nay</h4>
                <p class="text-xs text-on-surface-variant text-justify mb-4 leading-relaxed relative z-10">Những tuyệt phẩm đã hoàn thành được cộng đồng đánh giá cao nhất trong tháng.</p>
                <!-- Kéo 1 truyện ngẫu nhiên -->
                <?php
                $random_post = get_posts([
                    'post_type' => 'truyen',
                    'posts_per_page' => 1,
                    'orderby' => 'rand'
                ]);
                if ($random_post):
                    $rp = $random_post[0];
                ?>
                <button onclick="window.location.href='<?php echo get_permalink($rp->ID); ?>'" class="relative z-10 w-full py-2.5 bg-white text-primary text-[13px] font-bold rounded-xl shadow-[0px_4px_12px_rgba(0,96,169,0.1)] hover:shadow-[0px_8px_16px_rgba(0,96,169,0.15)] hover:-translate-y-0.5 active:translate-y-0 active:shadow-sm transition-all flex items-center justify-center gap-2">
                    Xem ngẫu nhiên <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
                </button>
                <?php endif; ?>
            </div>
        </aside>

        <!-- Main Content -->
        <section class="flex-1">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-8 gap-4 border-b border-surface-variant/30 pb-4">
                <h2 class="font-headline text-xl md:text-2xl font-bold text-on-surface flex items-baseline gap-2">
                    <span class="text-primary"><?php echo number_format($total_posts); ?></span> <span class="text-lg">truyện xuất sắc</span>
                </h2>
                
                <div class="flex items-center gap-2 bg-surface-container-low px-4 py-2 rounded-xl text-sm font-medium text-on-surface-variant border border-outline-variant/10 shadow-sm">
                    <span class="material-symbols-outlined text-[16px]">sort</span>
                    <span class="hidden sm:inline">Sắp xếp:</span>
                    <select class="mkm-native-select bg-transparent border-none focus:ring-0 text-primary cursor-pointer font-bold outline-none -ml-1" style="appearance: auto; -webkit-appearance: auto;">
                        <option>Mới cập nhật</option>
                        <option>Lượt xem nhiều</option>
                    </select>
                    <style>.mkm-native-select { display: inline-block !important; } .mkm-native-select + .nice-select, .mkm-native-select + .select2-container { display: none !important; }</style>
                </div>
            </div>

            <!-- Story Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                <?php 
                if ($completed_query->have_posts()) :
                    while ($completed_query->have_posts()) : $completed_query->the_post();
                        $views = (int)get_post_meta(get_the_ID(), '_views', true);
                        $author = get_post_meta(get_the_ID(), 'truyen_tacgia', true);
                        if(!$author) $author = 'Đang cập nhật';
                        $cover = has_post_thumbnail() ? get_the_post_thumbnail_url(get_the_ID(), 'large') : 'https://placehold.co/400x600?text=Cover';
                        $chapters_arr = get_posts(['post_type' => 'chuong', 'meta_key' => '_truyen_id', 'meta_value' => get_the_ID(), 'posts_per_page' => -1, 'fields' => 'ids']); $chaps = count($chapters_arr);
                ?>
                <!-- Card -->
                
        <a href="<?php the_permalink(); ?>" class="mkm-card group" style="background:#fff; border-radius:12px; overflow:hidden; box-shadow:0 1px 4px rgba(0,0,0,0.06); display:block; transition:transform 0.2s, box-shadow 0.2s; border: 1px solid #f3f4f6;">
            <div class="mkm-card-img" style="position:relative; aspect-ratio:3/2; overflow:hidden; background:#f9fafb;">
                <span style="position:absolute; top:8px; left:8px; background:#10b981; color:#fff; font-size:10px; font-weight:700; padding:2px 7px; border-radius:6px; z-index:2; box-shadow:0 2px 4px rgba(0,0,0,0.1);">FULL TẬP</span>
                <span style="position:absolute; top:32px; left:8px; background:#111827; color:#fff; font-size:9px; font-weight:700; padding:2px 7px; border-radius:6px; z-index:2;"><?php echo $chaps; ?> Chương</span>
                <img src="<?php echo esc_url($cover); ?>" style="width:100%; height:100%; object-fit:cover; display:block; transition:transform 0.4s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'"/>
                <div style="position:absolute; bottom:0; left:0; right:0; padding:20px 10px 8px 10px; background:linear-gradient(transparent, rgba(0,0,0,.7)); display:flex; justify-content:space-between; align-items:center; color:#fff; font-size:11px; font-weight:600; z-index:1;">
                    <span style="display:flex;align-items:center;gap:3px;"><svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg> <?php echo number_format($views); ?></span>
                    <span style="display:flex;align-items:center;gap:3px;color:#fbbf24;"><svg width="12" height="12" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg> 4.9</span>
                </div>
            </div>
            <div style="padding:12px;">
                <p style="font-size:14px; font-weight:700; color:#111827; margin:0 0 8px 0; line-height:1.4; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; font-family: ui-sans-serif, sans-serif;"><?php the_title(); ?></p>
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="background:#f3f4f6; color:#6b7280; font-size:10px; font-weight:600; padding:4px 8px; border-radius:6px;"><?php 
                        $cats = wp_get_post_terms(get_the_ID(), 'the_loai');
                        echo (!is_wp_error($cats) && !empty($cats)) ? esc_html($cats[0]->name) : 'Micro Drama';
                    ?></span>
                    <span style="background:rgba(217, 119, 6, 0.1); color:#d97706; font-size:10px; font-weight:700; padding:4px 8px; border-radius:6px;">Hoàn thành</span>
                </div>
            </div>
        </a>
                <?php 
                    endwhile; 
                    wp_reset_postdata();
                else: 
                ?>
                    <div class="col-span-full text-center py-12 text-outline-variant">
                        <span class="material-symbols-outlined text-4xl mb-2 opacity-50">menu_book</span>
                        <p>Danh sách đang được cập nhật thêm.</p>
                    </div>
                <?php endif; ?>
            </div>

            <!-- Pagination -->
            <div class="mt-16 flex items-center justify-center gap-2 template-pagination">
                <?php
                    $big = 999999999;
                    echo paginate_links([
                        'base' => str_replace($big, '%#%', esc_url(get_pagenum_link($big))),
                        'format' => '?paged=%#%',
                        'current' => max(1, get_query_var('paged')),
                        'total' => $completed_query->max_num_pages,
                        'prev_text' => '<span class="material-symbols-outlined">chevron_left</span>',
                        'next_text' => '<span class="material-symbols-outlined">chevron_right</span>',
                        'type' => 'plain',
                        'class' => 'pagination-link'
                    ]);
                ?>
            </div>
        </section>
    </div>
</main>

<style>
/* CSS cho Phân trang WP Native tích hợp Tailwind */
.template-pagination { display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center; }
.template-pagination a, .template-pagination span { display: flex; align-items: center; justify-content: center; width: 2.75rem; height: 2.75rem; border-radius: 9999px; font-weight: 600; transition: all 0.2s; font-size: 0.875rem; color: var(--on-surface-variant); }
.template-pagination .page-numbers:not(.current):not(.dots) { background-color: transparent; border: 1px solid rgba(0,0,0,0.05); cursor: pointer; }
.template-pagination .page-numbers:not(.current):not(.dots):hover { background-color: var(--surface-container-high); color: var(--primary); border-color: transparent; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }
.template-pagination .current { background-color: var(--primary); color: white; box-shadow: 0 4px 12px rgba(0, 96, 169, 0.3); }
.template-pagination .dots { border: none; background: transparent; pointer-events: none; opacity: 0.5; }
</style>

<?php get_footer(); ?>
