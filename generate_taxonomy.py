import re

php_code = """<?php
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

<main class="max-w-7xl mx-auto px-6 py-12 flex-grow w-full">
    <!-- Hero Section Title -->
    <section class="mb-16 text-center">
        <h1 class="font-headline text-5xl md:text-6xl font-extrabold text-on-background tracking-tight mb-4">
            Khám Phá Theo <span class="text-primary">Thể Loại</span>
        </h1>
        <p class="text-on-surface-variant max-w-2xl mx-auto text-lg text-center md:text-justify max-w-prose">
            Hành trình tìm kiếm những chương truyện tuyệt vời nhất bắt đầu từ đây. Chọn một thể loại để bắt đầu khám phá.
        </p>
    </section>

    <!-- Bento Grid Genres -->
    <section class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4 mb-20">
        <?php foreach($all_terms as $index => $t): 
            $icon = get_genre_icon($t->slug);
            $is_active = ($t->term_id === $current_term_id);
            $link = get_term_link($t);
            $count = number_format($t->count);
        ?>
            <?php if ($is_active || ($index === 0 && !$current_term_id)): ?>
            <!-- Active/Featured Genre Item -->
            <div onclick="window.location.href='<?php echo esc_url($link); ?>'" class="col-span-2 row-span-1 border-2 border-primary/20 bg-surface-container-lowest p-6 rounded-xl shadow-[0px_12px_32px_rgba(0,96,169,0.06)] relative overflow-hidden group cursor-pointer">
                <div class="absolute top-0 right-0 w-32 h-32 bg-primary/5 rounded-full -mr-16 -mt-16 transition-transform group-hover:scale-110"></div>
                <div class="relative z-10">
                    <span class="material-symbols-outlined text-primary text-4xl mb-4" style="font-variation-settings: 'FILL' 1;"><?php echo $icon; ?></span>
                    <h3 class="font-headline font-bold text-xl text-on-background"><?php echo esc_html($t->name); ?></h3>
                    <p class="text-sm text-on-surface-variant mt-1"><?php echo $count; ?> truyện</p>
                </div>
                <div class="absolute bottom-4 right-4">
                    <span class="material-symbols-outlined text-primary/30">chevron_right</span>
                </div>
            </div>
            <?php else: ?>
            <!-- Standard Genre Item -->
            <div onclick="window.location.href='<?php echo esc_url($link); ?>'" class="bg-surface-container-low p-6 rounded-xl hover:bg-surface-container-lowest hover:shadow-lg transition-all group cursor-pointer border border-transparent hover:border-outline-variant/30">
                <span class="material-symbols-outlined text-primary-container text-3xl mb-4" style="font-variation-settings: 'FILL' 1;"><?php echo $icon; ?></span>
                <h3 class="font-headline font-bold text-lg text-on-background"><?php echo esc_html($t->name); ?></h3>
                <p class="text-sm text-on-surface-variant mt-1"><?php echo $count; ?> truyện</p>
            </div>
            <?php endif; ?>
        <?php endforeach; ?>
        
        <!-- More Genres Button -->
        <div class="bg-surface-container-high/50 p-6 rounded-xl flex items-center justify-center border-2 border-dashed border-outline-variant hover:border-primary/50 transition-all cursor-pointer">
            <div class="text-center">
                <span class="material-symbols-outlined text-outline mb-1">more_horiz</span>
                <p class="text-sm font-bold text-on-surface-variant">Tất cả</p>
            </div>
        </div>
    </section>

    <!-- Filter and Content Section -->
    <section class="flex flex-col md:flex-row gap-8 items-start">
        <!-- Sticky Filters (Static UI currently) -->
        <aside class="w-full md:w-64 sticky xl:top-28 space-y-8">
            <div>
                <h4 class="font-headline font-bold text-on-background mb-4 flex items-center gap-2">
                    <span class="material-symbols-outlined text-primary">filter_list</span> Lọc Trạng Thái
                </h4>
                <div class="space-y-2">
                    <label class="flex items-center justify-between p-3 rounded-lg bg-surface-container-lowest shadow-sm cursor-pointer group border border-outline-variant/10 hover:border-primary/30">
                        <span class="flex items-center gap-3">
                            <input checked class="text-primary focus:ring-primary w-4 h-4 border-outline-variant" name="status" type="radio"/>
                            <span class="text-sm font-medium">Đang ra</span>
                        </span>
                        <span class="text-[10px] text-on-surface-variant bg-surface-container-high px-2 py-0.5 rounded-full font-bold">ALL</span>
                    </label>
                    <label class="flex items-center justify-between p-3 rounded-lg bg-surface-container-low hover:bg-surface-container-lowest transition-all cursor-pointer group border border-transparent hover:border-outline-variant/30">
                        <span class="flex items-center gap-3">
                            <input class="text-primary focus:ring-primary w-4 h-4 border-outline-variant" name="status" type="radio" disabled/>
                            <span class="text-sm font-medium text-slate-400">Hoàn thành</span>
                        </span>
                    </label>
                </div>
            </div>
            <div>
                <h4 class="font-headline font-bold text-on-background mb-4">Sắp xếp theo</h4>
                <select class="w-full bg-surface-container-low border border-outline-variant/20 rounded-xl text-sm py-3 px-4 focus:ring-2 ring-primary/20 outline-none">
                    <option>Mới cập nhật</option>
                    <option disabled>Lượt xem nhiều nhất</option>
                </select>
            </div>
        </aside>

        <!-- Book List Grid -->
        <div class="flex-1">
            <div class="flex flex-wrap items-center justify-between mb-8">
                <h2 class="font-headline text-2xl font-bold text-on-background">Truyện <?php echo esc_html($term_name); ?> <span class="text-primary text-base font-normal ml-2">(<?php echo number_format($term_count); ?>+)</span></h2>
            </div>

            <div class="grid grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                <?php if (have_posts()) : while (have_posts()) : the_post(); 
                    $views = (int)get_post_meta(get_the_ID(), '_views', true);
                    $author = get_post_meta(get_the_ID(), 'truyen_tacgia', true);
                    if(!$author) $author = 'Đang cập nhật';
                    $cover = has_post_thumbnail() ? get_the_post_thumbnail_url(get_the_ID(), 'medium') : 'https://placehold.co/400x600?text=Cover';
                    $chaps = wp_count_posts('chuong')->publish; // mock chap count
                ?>
                <!-- Book Card -->
                <div class="bg-surface-container-lowest rounded-xl overflow-hidden group shadow-[0px_4px_16px_rgba(0,0,0,0.02)] hover:shadow-[0px_12px_32px_rgba(0,96,169,0.06)] border border-outline-variant/10 hover:border-primary/30 transition-all flex flex-col h-full cursor-pointer" onclick="window.location.href='<?php the_permalink(); ?>'">
                    <div class="aspect-[3/4] relative overflow-hidden">
                        <img class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" src="<?php echo esc_url($cover); ?>"/>
                        
                        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex items-end p-4">
                            <button class="w-full py-2 bg-white text-primary rounded-full font-bold text-sm shadow-xl active:bg-surface-container transition-colors">Đọc ngay</button>
                        </div>
                    </div>
                    
                    <div class="p-4 flex flex-col flex-grow">
                        <h3 class="font-headline font-bold text-on-background text-[15px] mb-1 line-clamp-2 leading-snug group-hover:text-primary transition-colors"><?php the_title(); ?></h3>
                        <p class="text-xs text-on-surface-variant mb-3 flex items-center gap-1 opacity-80">
                            <span class="material-symbols-outlined text-[13px]">person</span> <?php echo esc_html($author); ?>
                        </p>
                        
                        <div class="mt-auto pt-3 flex items-center justify-between border-t border-surface-variant/50">
                            <div class="flex items-center gap-1 text-[10px] font-bold text-outline">
                                <span class="material-symbols-outlined text-[13px]">format_list_bulleted</span> CHƯƠNG <?php echo number_format($chaps); ?>
                            </div>
                            <div class="flex items-center gap-1 text-[10px] font-bold text-tertiary-container">
                                <span class="material-symbols-outlined text-[14px]" style="font-variation-settings: 'FILL' 1;">star</span> 4.9
                            </div>
                        </div>
                    </div>
                </div>
                <?php endwhile; else: ?>
                    <div class="col-span-4 text-center py-12 text-outline-variant font-medium">Chưa có truyện nào thuộc thể loại này.</div>
                <?php endif; ?>
            </div>

            <!-- Pagination -->
            <div class="mt-16 flex items-center justify-center gap-2 template-pagination">
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
            </div>
        </div>
    </section>
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
"""

with open("tehi-theme/taxonomy-the_loai.php", "w", encoding="utf-8") as f:
    f.write(php_code)

# Ensure the header category link is properly set or unhashed
def fix_header_category_link(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    # Find "Thể loại"
    content = content.replace('href="#">Danh mục', 'href="/the-loai/tien-hiep">Thể loại')
    content = content.replace('href="#">Thể loại', 'href="/the-loai/tien-hiep">Thể loại')
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

fix_header_category_link("tehi-theme/header.php")
fix_header_category_link("tehi-theme/header-home.php")
fix_header_category_link("tehi-theme/page-profile.php")
fix_header_category_link("tehi-theme/page-bangxephang.php") 

print("Created taxonomy-the_loai.php")
