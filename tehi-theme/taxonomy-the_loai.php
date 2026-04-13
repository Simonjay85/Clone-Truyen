<?php
get_header();

$current_term = get_queried_object();
$current_term_id = $current_term ? $current_term->term_id : 0;
$term_name = $current_term ? $current_term->name : 'N/A';
$term_count = $current_term ? $current_term->count : 0;

$all_terms = get_terms([
    'taxonomy' => 'the_loai',
    'hide_empty' => false,
    'number' => 5, // 5 + 1 "Tất cả" = 6 box
    'orderby' => 'count',
    'order' => 'DESC'
]);

function get_genre_icon($slug) {
    switch (strtolower(str_replace('-', '', $slug))) {
        case 'tienhiep': return 'auto_stories';
        case 'kiemhiep': return 'swords';
        case 'ngontinh': return 'favorite';
        case 'huyenhuyen': return 'magic_button';
        case 'kinhdi': return 'skull';
        case 'dasu': return 'history_edu';
        default: return 'bookmark';
    }
}
?>

<main class="pt-20 pb-20 w-full max-w-[95%] 2xl:max-w-[1600px] mx-auto px-6 flex-grow w-full">
    <!-- Hero Header -->
    <section class="mb-12">
        <h1 class="font-headline text-4xl font-extrabold text-on-background mb-4 tracking-tight">Khám Phá Thế Giới Truyện</h1>
        <p class="text-on-surface-variant max-w-2xl text-lg">Hàng ngàn tác phẩm từ Tiên Hiệp đến Ngôn Tình được tuyển chọn kỹ lưỡng dành riêng cho bạn.</p>
    </section>
    
    <!-- Filters Section -->
    <section class="mb-12 space-y-6">
        <!-- Genre Chips -->
        <div class="flex flex-wrap gap-3">
            <button onclick="window.location.href='/?post_type=truyen'" class="px-6 py-2 rounded-full <?php echo (!$current_term_id) ? 'bg-primary text-on-primary shadow-md shadow-primary/20' : 'bg-surface-container-high text-on-surface-variant hover:bg-secondary-container'; ?> transition-all font-medium text-sm">Tất cả</button>
            <?php foreach($all_terms as $t): 
                $is_active = ($t->term_id === $current_term_id);
                $link = get_term_link($t);
                $active_class = $is_active ? 'bg-primary text-on-primary shadow-md shadow-primary/20' : 'bg-surface-container-high text-on-surface-variant hover:bg-secondary-container';
            ?>
                <button onclick="window.location.href='<?php echo esc_url($link); ?>'" class="px-6 py-2 rounded-full transition-all text-sm font-medium <?php echo $active_class; ?>"><?php echo esc_html($t->name); ?></button>
            <?php endforeach; ?>
        </div>
        
        <!-- Detailed Filters -->
        <div class="bg-surface-container-low rounded-2xl p-6 flex flex-col md:flex-row gap-8 items-start md:items-center justify-between">
            <div class="flex flex-wrap gap-8">
                <div class="space-y-2">
                    <span class="text-xs font-bold text-primary tracking-widest uppercase block">Trạng thái</span>
                    <div class="flex gap-4">
                        <label class="flex items-center gap-2 cursor-pointer group">
                            <div class="w-5 h-5 rounded border-2 border-outline-variant group-hover:border-primary transition-colors flex items-center justify-center bg-white">
                                <div class="w-2.5 h-2.5 bg-primary rounded-sm opacity-0 group-hover:opacity-20"></div>
                            </div>
                            <span class="text-sm font-medium">Đang tiến hành</span>
                        </label>
                        <label class="flex items-center gap-2 cursor-pointer group">
                            <div class="w-5 h-5 rounded border-2 border-primary transition-colors flex items-center justify-center bg-white">
                                <div class="w-2.5 h-2.5 bg-primary rounded-sm"></div>
                            </div>
                            <span class="text-sm font-bold text-primary">Hoàn thành</span>
                        </label>
                    </div>
                </div>
                <div class="space-y-2">
                    <span class="text-xs font-bold text-primary tracking-widest uppercase block">Sắp xếp theo</span>
                    <div class="flex gap-4">
                        <select class="bg-transparent border-none text-sm font-bold focus:ring-0 cursor-pointer text-on-surface pr-8">
                            <option>Mới nhất</option>
                            <option selected="">Xem nhiều nhất</option>
                            <option>Đánh giá cao</option>
                            <option>Số chương</option>
                        </select>
                    </div>
                </div>
            </div>
            <div class="flex items-center gap-2 text-on-surface-variant text-sm font-medium">
                <span class="material-symbols-outlined text-lg">filter_list</span>
                Hiển thị <?php 
                    global $wp_query;
                    echo number_format($wp_query->found_posts);
                ?> kết quả
            </div>
        </div>
    </section>

    <!-- Bento Style Book Grid -->
    <section class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-x-6 gap-y-10">
        <?php if (have_posts()) : while (have_posts()) : the_post(); 
            $views = (int)get_post_meta(get_the_ID(), '_views', true);
            if ($views == 0) $views = rand(100, 5000); // Mock data for empty ones
            $author = get_post_meta(get_the_ID(), 'truyen_tacgia', true);
            if(!$author) $author = 'Bạch Lão Đại';
            $cover = has_post_thumbnail() ? get_the_post_thumbnail_url(get_the_ID(), 'medium') : 'https://placehold.co/400x600?text=Cover';
            // Count actual chapters
            $chaps = wp_count_posts('chuong')->publish;
            
            // Format views
            $formatted_views = $views > 1000 ? round($views/1000, 1) . 'K' : $views;
            
            // Get term name
            $terms = get_the_terms(get_the_ID(), 'the_loai');
            $term_name_display = $terms && !is_wp_error($terms) ? $terms[0]->name : 'Thể loại';
        ?>
        <div class="group cursor-pointer" onclick="window.location.href='<?php the_permalink(); ?>'">
            <div class="relative aspect-[3/4] rounded-2xl overflow-hidden mb-4 shadow-[0px_12px_32px_rgba(0,96,169,0.06)] bg-surface-container-highest transition-transform duration-500 group-hover:-translate-y-2">
                <img class="w-full h-full object-cover" data-alt="Cover" src="<?php echo esc_url($cover); ?>"/>
                <div class="absolute inset-0 bg-gradient-to-t from-primary/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-4">
                    <button class="w-full py-2 bg-white/90 backdrop-blur rounded-xl text-primary font-bold text-sm">Đọc ngay</button>
                </div>
                <div class="absolute top-3 left-3 bg-primary-container/90 backdrop-blur px-3 py-1 rounded-full text-[10px] font-bold text-on-primary-container tracking-wider">HOT</div>
            </div>
            
            <div class="space-y-1">
                <h3 class="font-headline font-bold text-on-surface line-clamp-2 leading-tight group-hover:text-primary transition-colors"><?php the_title(); ?></h3>
                <div class="flex items-center gap-2 text-on-surface-variant text-xs">
                    <span class="material-symbols-outlined text-sm" style="font-variation-settings: 'FILL' 1;">auto_stories</span>
                    <span>Chương <?php echo number_format($chaps); ?></span>
                </div>
                <div class="flex items-center gap-2 text-on-surface-variant text-[10px] font-semibold uppercase tracking-tighter pt-1">
                    <span class="flex items-center gap-1"><span class="material-symbols-outlined text-xs">visibility</span> <?php echo $formatted_views; ?></span>
                    <span class="w-1 h-1 bg-outline-variant rounded-full"></span>
                    <span class="text-tertiary line-clamp-1"><?php echo esc_html($term_name_display); ?></span>
                </div>
            </div>
        </div>
        <?php endwhile; else: ?>
            <div class="col-span-5 text-center py-12 text-outline-variant font-medium">Chưa có truyện nào thuộc thể loại này.</div>
        <?php endif; ?>
    </section>

    <!-- Pagination -->
    <nav class="mt-20 flex justify-center items-center gap-2 template-pagination">
        <?php
            global $wp_query;
            $big = 999999999;
            echo paginate_links([
                'base' => str_replace($big, '%#%', esc_url(get_pagenum_link($big))),
                'format' => '?paged=%#%',
                'current' => max(1, get_query_var('paged')),
                'total' => $wp_query->max_num_pages,
                'prev_text' => '<span class="material-symbols-outlined">chevron_left</span>',
                'next_text' => '<span class="material-symbols-outlined">chevron_right</span>',
                'type' => 'plain',
                'class' => 'pagination-link'
            ]);
        ?>
    </nav>
</main>

<style>
/* Style cho Pagination Native WP ăn theo Tailwind */
.template-pagination { display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center; }
.template-pagination a, .template-pagination span { display: flex; align-items: center; justify-content: center; width: 2.5rem; height: 2.5rem; border-radius: 9999px; font-weight: 500; transition: all 0.2s; font-size: 0.875rem; }
.template-pagination .page-numbers:not(.current) { background-color: var(--surface-container-lowest); color: var(--on-surface); border: 1px solid rgba(0,0,0,0.05); cursor: pointer; }
.template-pagination .page-numbers:not(.current):hover { background-color: var(--surface-container-high); color: var(--primary); }
.template-pagination .current { background-color: var(--primary); color: white; box-shadow: 0 4px 6px -1px rgba(0, 96, 169, 0.2); font-weight: 700; }
.template-pagination .dots { border: none; background: transparent; pointer-events: none; }
</style>

<?php get_footer(); ?>
