import re

php_code_completed = """<?php
/*
Template Name: Truyện Hoàn Thành
*/
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

<main class="pt-24 pb-16 px-6 max-w-7xl mx-auto flex-grow w-full">
    <!-- Hero / Header Section -->
    <header class="mb-12 relative overflow-hidden rounded-3xl bg-surface-container-low p-8 md:p-12 border border-outline-variant/10">
        <div class="absolute top-0 right-0 w-1/3 h-full opacity-10 pointer-events-none">
            <img class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBV_SP1Lo5K64DTSZmS8kWMxUUBd-Vbi2TEetTZaMs5X_QwTAja1I0K-yM2KMObZYiWz3ohHAgh0g00e9Om8UE-x3H_0iCihRdoy25RvXkpgjZuvIDQLkB2nJ-Pj6Loo4dJkr1avsg80s9n676nonOdgYCusDVhpBK0U50krmKpNGn0GBFFb1b3OFe2vaWgE_Oui4rW9m2cuyirydWRJh79PHWKIcPjm6WKnIcF9FlQ6CyrvwSe_XDrKwhVV5jGfqbVXFXVariiVeo"/>
        </div>
        <div class="relative z-10 max-w-2xl">
            <nav class="flex items-center gap-2 text-xs font-medium text-on-surface-variant mb-4">
                <a href="<?php echo home_url(); ?>" class="hover:text-primary transition-colors">Trang chủ</a>
                <span class="material-symbols-outlined text-xs">chevron_right</span>
                <span class="text-primary font-bold">Truyện Hoàn Thành</span>
            </nav>
            <h1 class="font-headline text-4xl md:text-5xl font-extrabold tracking-tight text-on-surface mb-4">
                Hành Trình <span class="bg-clip-text text-transparent bg-gradient-to-r from-primary to-primary-container">Trọn Vẹn</span>
            </h1>
            <p class="text-on-surface-variant text-lg leading-relaxed max-w-prose">
                Khám phá những bộ truyện đã đi đến hồi kết. Không còn phải chờ đợi từng chương, hãy tận hưởng trọn vẹn cảm xúc từ đầu đến cuối ngay hôm nay.
            </p>
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
                    <select class="bg-transparent border-none focus:ring-0 text-primary cursor-pointer font-bold outline-none -ml-1">
                        <option>Mới cập nhật</option>
                        <option disabled>Lượt xem nhiều</option>
                    </select>
                </div>
            </div>

            <!-- Story Grid -->
            <div class="grid grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-6">
                <?php 
                if ($completed_query->have_posts()) :
                    while ($completed_query->have_posts()) : $completed_query->the_post();
                        $views = (int)get_post_meta(get_the_ID(), '_views', true);
                        $author = get_post_meta(get_the_ID(), 'truyen_tacgia', true);
                        if(!$author) $author = 'Đang cập nhật';
                        $cover = has_post_thumbnail() ? get_the_post_thumbnail_url(get_the_ID(), 'medium') : 'https://placehold.co/400x600?text=Cover';
                        $chaps = wp_count_posts('chuong')->publish;
                ?>
                <!-- Card -->
                <div class="group cursor-pointer flex flex-col h-full bg-surface-container-lowest rounded-2xl p-2 hover:shadow-[0px_12px_32px_rgba(0,96,169,0.06)] border border-transparent hover:border-primary/10 transition-all duration-300" onclick="window.location.href='<?php the_permalink(); ?>'">
                    <div class="relative aspect-[3/4] rounded-xl overflow-hidden mb-3 bg-surface-container-high shadow-inner">
                        <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" src="<?php echo esc_url($cover); ?>"/>
                        
                        <!-- Badges -->
                        <div class="absolute top-2 left-2 flex gap-1 flex-col items-start">
                            <span class="bg-primary/90 backdrop-blur-md text-white px-2.5 py-1 rounded-md text-[9px] shadow-sm font-black uppercase tracking-widest border border-white/10 shrink-0">FULL TẬP</span>
                            <span class="bg-black/60 backdrop-blur-md text-white px-2 py-0.5 rounded text-[10px] font-bold shrink-0"><?php echo number_format($chaps); ?> Chương</span>
                        </div>
                        
                        <!-- Rating Overlay -->
                        <div class="absolute bottom-0 left-0 right-0 p-3 pt-8 bg-gradient-to-t from-black/80 via-black/40 to-transparent flex items-end">
                            <div class="flex items-center gap-1 bg-amber-400/20 backdrop-blur-sm border border-amber-400/30 px-2 py-0.5 rounded-full text-amber-300 text-[10px]">
                                <span class="material-symbols-outlined text-[12px]" style="font-variation-settings: 'FILL' 1;">star</span>
                                <span class="font-bold">4.9</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex flex-col flex-grow px-1">
                        <h3 class="font-headline font-bold text-on-surface text-[15px] group-hover:text-primary transition-colors line-clamp-2 leading-snug mb-1"><?php the_title(); ?></h3>
                        <p class="text-xs text-outline font-medium mt-auto flex items-center gap-1">
                            <span class="material-symbols-outlined text-[12px]">edit</span> <?php echo esc_html($author); ?>
                        </p>
                    </div>
                </div>
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
"""

with open("tehi-theme/page-completed.php", "w", encoding="utf-8") as f:
    f.write(php_code_completed)

# Update headers again 
def fix_header_link(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    # Find "Truyện Hoàn Thành"
    content = content.replace('href="#">Truyện Hoàn Thành', 'href="/truyen-hoan-thanh">Truyện Hoàn Thành')
    content = content.replace('href="#">Hoàn thành', 'href="/truyen-hoan-thanh">Hoàn thành')
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

for tpl in ["tehi-theme/header.php", "tehi-theme/header-home.php"]:
    fix_header_link(tpl)

print("Created page-completed.php")
