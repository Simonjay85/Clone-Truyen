php_code_directory = """<?php
/*
Template Name: Danh Mục
*/
get_header();

$paged = (get_query_var('paged')) ? get_query_var('paged') : 1;
$query_args = [
    'post_type' => 'truyen',
    'posts_per_page' => 20,
    'paged' => $paged,
    'orderby' => 'date',
    'order' => 'DESC'
];
$directory_query = new WP_Query($query_args);
$total_posts = $directory_query->found_posts;

$all_terms = get_terms([
    'taxonomy' => 'the_loai',
    'hide_empty' => false,
    'number' => 15,
    'orderby' => 'count',
    'order' => 'DESC'
]);
?>

<main class="pt-24 pb-20 max-w-7xl mx-auto px-6 w-full flex-grow">
    <!-- Hero Header -->
    <section class="mb-12 text-center md:text-left">
        <h1 class="font-headline text-4xl mt-4 font-extrabold text-on-background mb-4 tracking-tight">Khám Phá <span class="bg-clip-text text-transparent bg-gradient-to-r from-primary to-primary-container">Thế Giới Truyện</span></h1>
        <p class="text-on-surface-variant max-w-2xl text-lg mx-auto md:mx-0">Hàng ngàn tác phẩm từ Tiên Hiệp đến Ngôn Tình được tuyển chọn kỹ lưỡng dành riêng cho bạn.</p>
    </section>

    <!-- Filters Section -->
    <section class="mb-12 space-y-6">
        <!-- Genre Chips -->
        <div class="flex flex-wrap gap-3">
            <a href="?genre=all" class="px-6 py-2 rounded-full bg-primary text-on-primary font-medium text-sm shadow-md shadow-primary/20 transition-all cursor-pointer">Tất cả</a>
            <?php foreach($all_terms as $t): ?>
                <a href="<?php echo esc_url(get_term_link($t)); ?>" class="px-6 py-2 rounded-full bg-surface-container-high text-on-surface-variant hover:bg-secondary-container hover:text-on-secondary-container transition-all text-sm font-medium cursor-pointer">
                    <?php echo esc_html($t->name); ?>
                </a>
            <?php endforeach; ?>
        </div>

        <!-- Detailed Filters -->
        <div class="bg-surface-container-low rounded-2xl p-6 flex flex-col md:flex-row gap-8 items-start md:items-center justify-between border border-outline-variant/10 shadow-sm">
            <div class="flex flex-wrap gap-8">
                <div class="space-y-2" title="Tính năng Lọc Trạng thái (BETA) sẽ sớm hoạt động">
                    <span class="text-[10px] font-bold text-primary tracking-widest uppercase block">Trạng thái</span>
                    <div class="flex gap-4">
                        <label class="flex items-center gap-2 cursor-pointer group opacity-50">
                            <div class="w-5 h-5 rounded border-2 border-outline-variant flex items-center justify-center bg-white"><div class="w-2.5 h-2.5 bg-primary rounded-sm opacity-0 group-hover:opacity-20"></div></div>
                            <span class="text-sm font-medium">Đang tiến hành</span>
                        </label>
                        <label class="flex items-center gap-2 cursor-pointer group opacity-50">
                            <div class="w-5 h-5 rounded border-2 border-outline-variant flex items-center justify-center bg-white"><div class="w-2.5 h-2.5 bg-primary rounded-sm opacity-0"></div></div>
                            <span class="text-sm font-bold text-on-surface-variant">Hoàn thành</span>
                        </label>
                    </div>
                </div>
                <div class="space-y-2">
                    <span class="text-[10px] font-bold text-primary tracking-widest uppercase block">Sắp xếp theo</span>
                    <div class="flex gap-4">
                        <select class="bg-transparent border-none text-sm font-bold focus:ring-0 cursor-pointer text-on-surface outline-none pl-0">
                            <option>Mới nhất</option>
                            <option disabled>Xem nhiều nhất</option>
                            <option disabled>Đánh giá cao</option>
                        </select>
                    </div>
                </div>
            </div>
            <div class="flex items-center gap-2 text-primary text-sm font-bold bg-primary/5 px-4 py-2 rounded-lg border border-primary/10">
                <span class="material-symbols-outlined text-[18px]">menu_book</span>
                Hiển thị <?php echo number_format($total_posts); ?> truyện
            </div>
        </div>
    </section>

    <!-- Bento Style Book Grid -->
    <section class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-x-6 gap-y-10">
        <?php 
        if ($directory_query->have_posts()) :
            while ($directory_query->have_posts()) : $directory_query->the_post();
                $views = (int)get_post_meta(get_the_ID(), '_views', true);
                $is_hot = ($views > 5000) ? true : false;
                $cover = has_post_thumbnail() ? get_the_post_thumbnail_url(get_the_ID(), 'medium') : 'https://placehold.co/400x600?text=Cover';
                $chaps = wp_count_posts('chuong')->publish;
                
                // Fetch first genre for small tag
                $genres = wp_get_post_terms(get_the_ID(), 'the_loai');
                $main_genre = !is_wp_error($genres) && !empty($genres) ? $genres[0]->name : 'Truyện chữ';

                // Simplified View Formatter
                $view_fmt = $views;
                if ($views >= 1000000) $view_fmt = round($views / 1000000, 1) . 'M';
                else if ($views >= 1000) $view_fmt = round($views / 1000, 1) . 'K';
        ?>
        <!-- Book Card -->
        <div class="group cursor-pointer flex flex-col h-full" onclick="window.location.href='<?php the_permalink(); ?>'">
            <div class="relative aspect-[3/4] rounded-2xl overflow-hidden mb-4 shadow-[0px_4px_16px_rgba(0,0,0,0.06)] group-hover:shadow-[0px_16px_40px_rgba(0,96,169,0.15)] bg-surface-container-highest transition-all duration-300 group-hover:-translate-y-2 border border-outline-variant/10">
                <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" src="<?php echo esc_url($cover); ?>"/>
                
                <div class="absolute inset-0 bg-gradient-to-t from-primary/80 via-primary/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-4">
                    <button class="w-full py-2 bg-white/95 backdrop-blur-md rounded-xl text-primary font-black text-[13px] shadow-lg active:scale-95 transition-transform">Đọc Ngay</button>
                </div>

                <?php if ($is_hot): ?>
                <div class="absolute top-3 left-3 bg-secondary-container/90 backdrop-blur px-3 py-1 rounded-full text-[10px] font-black text-on-secondary-container tracking-wider shadow-sm uppercase border border-secondary-container/50">HOT</div>
                <?php else: ?>
                <div class="absolute top-3 left-3 bg-primary-container/90 backdrop-blur px-3 py-1 rounded-full text-[10px] font-black text-on-primary-container tracking-wider shadow-sm uppercase border border-primary-container/50">MỚI</div>
                <?php endif; ?>
                
                <!-- Bookmark quick action -->
                <div class="absolute top-3 right-3 bg-white/80 hover:bg-white backdrop-blur p-2 rounded-full text-outline hover:text-primary shadow-sm transition-colors opacity-0 group-hover:opacity-100" title="Đánh dấu truyện">
                    <span class="material-symbols-outlined text-[18px]" style="font-variation-settings: 'FILL' 0;">bookmark_add</span>
                </div>
            </div>
            
            <div class="space-y-1.5 flex-grow flex flex-col px-1">
                <h3 class="font-headline font-bold text-on-surface line-clamp-2 leading-snug group-hover:text-primary transition-colors text-[15px]"><?php the_title(); ?></h3>
                
                <div class="flex items-center gap-1.5 text-on-surface-variant text-[11px] font-semibold mt-auto">
                    <span class="material-symbols-outlined text-[14px] text-outline">format_list_bulleted</span>
                    <span>Chương <?php echo number_format($chaps); ?></span>
                </div>
                
                <div class="flex items-center gap-2 text-on-surface-variant text-[10px] font-bold uppercase tracking-wide pt-1 opacity-80">
                    <span class="flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">visibility</span> <?php echo $view_fmt; ?></span>
                    <span class="w-1 h-1 bg-outline-variant rounded-full"></span>
                    <span class="text-tertiary line-clamp-1"><?php echo esc_html($main_genre); ?></span>
                </div>
            </div>
        </div>
        <?php 
            endwhile; 
            wp_reset_postdata();
        else:
        ?>
            <div class="col-span-full py-20 text-center text-outline-variant font-medium">Chưa có truyện nào trong danh mục.</div>
        <?php endif; ?>
    </section>

    <!-- Pagination -->
    <div class="mt-20 flex justify-center template-pagination">
        <?php
            $big = 999999999;
            echo paginate_links([
                'base' => str_replace($big, '%#%', esc_url(get_pagenum_link($big))),
                'format' => '?paged=%#%',
                'current' => max(1, get_query_var('paged')),
                'total' => $directory_query->max_num_pages,
                'prev_text' => '<span class="material-symbols-outlined">chevron_left</span>',
                'next_text' => '<span class="material-symbols-outlined">chevron_right</span>',
                'type' => 'plain',
                'class' => 'pagination-link'
            ]);
        ?>
    </div>
</main>

<style>
/* Reset pagination Tailwind alignment */
.template-pagination { display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center; align-items: center; }
.template-pagination a, .template-pagination span { display: flex; align-items: center; justify-content: center; width: 2.75rem; height: 2.75rem; border-radius: 9999px; font-weight: 600; transition: all 0.2s; font-size: 0.875rem; color: var(--on-surface-variant); }
.template-pagination .page-numbers:not(.current):not(.dots) { background-color: var(--surface-container-low); border: 1px solid rgba(0,0,0,0.05); cursor: pointer; }
.template-pagination .page-numbers:not(.current):not(.dots):hover { background-color: var(--surface-container-high); color: var(--primary); border-color: transparent; }
.template-pagination .current { background-color: var(--primary); color: white; box-shadow: 0 4px 14px rgba(0, 96, 169, 0.35); }
.template-pagination .dots { border: none; background: transparent; pointer-events: none; opacity: 0.5; }
</style>

<?php get_footer(); ?>
"""

with open("tehi-theme/page-directory.php", "w", encoding="utf-8") as f:
    f.write(php_code_directory)

print("Created page-directory.php")
