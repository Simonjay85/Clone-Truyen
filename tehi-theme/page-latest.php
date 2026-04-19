<?php
/*
Template Name: Truyện Mới Cập Nhật
*/
get_header();

$paged = (get_query_var('paged')) ? get_query_var('paged') : 1;
$latest_query = new WP_Query([
    'post_type' => 'truyen',
    'posts_per_page' => 15,
    'paged' => $paged,
    'orderby' => 'modified', // Sort by last modified
    'order' => 'DESC'
]);

// Prepare hot query
$hot_query = new WP_Query([
    'post_type' => 'truyen',
    'posts_per_page' => 3,
    'meta_key' => '_views',
    'orderby' => 'meta_value_num',
    'order' => 'DESC'
]);
?>

<main class="w-full max-w-[95%] 2xl:max-w-[1600px] mx-auto px-6 py-12 flex-grow w-full min-h-screen">
    <div class="flex flex-col lg:flex-row gap-12">
        
        <!-- Main Content: New Updates -->
        <div class="flex-1">
            <div class="mb-10">
                <h1 class="text-4xl font-extrabold font-headline text-on-background tracking-tight mb-2">Truyện Mới Cập Nhật</h1>
                <p class="text-on-surface-variant font-medium">Khám phá những chương truyện mới nhất vừa được hệ thống cập nhật.</p>
            </div>

            <div class="grid grid-cols-1 gap-6">
                <?php 
                $current_date = '';
                if ($latest_query->have_posts()) :
                    while ($latest_query->have_posts()) : $latest_query->the_post();
                        $post_date = get_the_modified_date('Y-m-d');
                        $display_date = '';
                        
                        if ($post_date == current_time('Y-m-d')) {
                            $display_date = "Hôm nay";
                        } elseif ($post_date == date('Y-m-d', strtotime('-1 day', current_time('timestamp')))) {
                            $display_date = "Hôm qua";
                        } else {
                            $display_date = get_the_modified_date('d/m/Y');
                        }

                        // Print Date Divider if changed
                        if ($current_date != $display_date):
                            $current_date = $display_date;
                ?>
                            <div class="flex items-center gap-4 mb-2 mt-4">
                                <div class="h-px flex-1 bg-gradient-to-r from-transparent to-outline-variant/30"></div>
                                <span class="px-3 py-1 rounded-full <?php echo ($display_date == 'Hôm nay') ? 'bg-primary-container/20 text-primary' : 'bg-surface-container-high text-on-surface-variant'; ?> font-bold text-[10px] uppercase tracking-widest font-headline">
                                    <?php echo esc_html($display_date); ?>
                                </span>
                                <div class="h-px flex-1 bg-gradient-to-l from-transparent to-outline-variant/30"></div>
                            </div>
                <?php   endif; ?>

                <?php 
                    $cover = has_post_thumbnail() ? get_the_post_thumbnail_url(get_the_ID(), 'large') : 'https://placehold.co/400x600?text=Cover';
                    $genres = wp_get_post_terms(get_the_ID(), 'the_loai');
                    $chapters_arr = get_posts(['post_type' => 'chuong', 'meta_key' => '_truyen_id', 'meta_value' => get_the_ID(), 'posts_per_page' => -1, 'fields' => 'ids']); $chaps = count($chapters_arr);
                    $time_diff = human_time_diff(get_the_modified_time('U'), current_time('timestamp')) . ' trước';
                    if($display_date != 'Hôm nay' && $display_date != 'Hôm qua') $time_diff = get_the_modified_time('H:i');
                ?>
                <!-- Update Item -->
                <div class="group flex gap-4 md:gap-6 p-4 rounded-2xl bg-surface-container-lowest hover:bg-surface-container-lowest transition-all duration-300 border border-transparent hover:border-primary/20 shadow-sm hover:shadow-[0px_4px_24px_rgba(0,96,169,0.08)] cursor-pointer" onclick="window.location.href='<?php the_permalink(); ?>'">
                    <div class="relative w-20 md:w-24 h-28 md:h-32 flex-shrink-0 overflow-hidden rounded-xl shadow-md border border-outline-variant/10">
                        <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="<?php echo esc_url($cover); ?>"/>
                        <?php if ($display_date == "Hôm nay"): ?>
                        <div class="absolute top-2 left-2 px-1.5 py-0.5 bg-primary-container text-on-primary-container text-[8px] font-black tracking-widest rounded uppercase">NEW</div>
                        <?php endif; ?>
                    </div>
                    
                    <div class="flex flex-col justify-between py-1 flex-1">
                        <div>
                            <div class="flex flex-wrap gap-1 mb-1.5">
                                <?php 
                                if(!is_wp_error($genres) && !empty($genres)){
                                    $c = 0;
                                    foreach($genres as $g){
                                        if($c > 1) break;
                                        echo '<span class="text-[9px] font-black tracking-wider text-primary bg-primary/5 border border-primary/10 px-1.5 py-0.5 rounded shadow-sm uppercase">'.esc_html($g->name).'</span> ';
                                        $c++;
                                    }
                                }
                                ?>
                            </div>
                            <h3 class="text-base md:text-lg font-bold text-on-background font-headline leading-tight group-hover:text-primary transition-colors line-clamp-1 md:line-clamp-2"><?php the_title(); ?></h3>
                            <p class="text-[13px] text-on-surface-variant mt-1 line-clamp-1 opacity-80"><?php echo wp_trim_words(get_the_excerpt(), 10); ?></p>
                        </div>
                        
                        <div class="flex items-center justify-between mt-auto pt-2 border-t border-outline-variant/10">
                            <div class="flex items-center gap-3">
                                <span class="text-[11px] font-bold text-primary bg-primary/5 px-2 py-0.5 rounded shadow-sm border border-primary/10">CHƯƠNG <?php echo number_format($chaps); ?></span>
                                <span class="text-[11px] font-semibold text-outline tracking-wide flex items-center gap-1">
                                    <span class="material-symbols-outlined text-[12px]">schedule</span> <?php echo $time_diff; ?>
                                </span>
                            </div>
                            <button class="material-symbols-outlined text-[18px] text-outline hover:text-primary transition-colors" title="Đánh dấu">bookmark_add</button>
                        </div>
                    </div>
                </div>
                
                <?php 
                    endwhile; 
                else: 
                ?>
                    <div class="text-center py-10 opacity-50">Không có truyện nào.</div>
                <?php endif; ?>
            </div>

            <!-- Pagination -->
            <div class="mt-16 flex justify-center template-pagination">
                <?php
                    $big = 999999999;
                    echo paginate_links([
                        'base' => str_replace($big, '%#%', esc_url(get_pagenum_link($big))),
                        'format' => '?paged=%#%',
                        'current' => max(1, get_query_var('paged')),
                        'total' => $latest_query->max_num_pages,
                        'prev_text' => '<span class="material-symbols-outlined">chevron_left</span>',
                        'next_text' => '<span class="material-symbols-outlined">chevron_right</span>',
                        'type' => 'plain',
                        'class' => 'pagination-link'
                    ]);
                ?>
            </div>
        </div>

        <!-- Sidebar: Trending/Top -->
        <aside class="w-full lg:w-80 space-y-8 sticky lg:top-24 self-start">
            
            <div class="bg-gradient-to-b from-surface-container-low to-surface-container-lowest p-6 rounded-[2rem] border border-outline-variant/20 shadow-sm relative overflow-hidden">
                <div class="absolute top-0 right-0 w-32 h-32 bg-primary/5 rounded-full blur-xl pointer-events-none"></div>
                <div class="flex items-center justify-between mb-8 relative z-10">
                    <h2 class="text-xl font-extrabold font-headline text-on-background tracking-tight">Truyện Đang Hot</h2>
                    <div class="w-8 h-8 rounded-full bg-red-100 text-red-500 flex items-center justify-center">
                        <span class="material-symbols-outlined text-[16px]" style="font-variation-settings: 'FILL' 1;">local_fire_department</span>
                    </div>
                </div>
                
                <div class="space-y-6 relative z-10">
                    <?php 
                    $count = 1;
                    if ($hot_query->have_posts()) :
                        while ($hot_query->have_posts()) : $hot_query->the_post();
                            $views = (int)get_post_meta(get_the_ID(), '_views', true);
                            $v_txt = ($views >= 1000000) ? round($views/1000000,1).'M' : (($views >= 1000) ? round($views/1000,1).'K' : $views);
                    ?>
                    <div class="flex gap-4 items-center group cursor-pointer" onclick="window.location.href='<?php the_permalink(); ?>'">
                        <span class="text-3xl font-black text-on-surface-variant/20 font-headline group-hover:text-primary transition-colors italic w-8 text-center shrink-0">
                            0<?php echo $count; ?>
                        </span>
                        <div class="flex-1">
                            <h4 class="font-bold text-[14px] text-on-background leading-snug group-hover:text-primary transition-colors line-clamp-2"><?php the_title(); ?></h4>
                            <div class="flex items-center gap-3 mt-1.5 border-t border-outline-variant/10 pt-1">
                                <span class="text-[10px] text-outline font-bold flex items-center gap-1 uppercase tracking-widest">
                                    <span class="material-symbols-outlined text-[12px]">visibility</span> <?php echo $v_txt; ?>
                                </span>
                            </div>
                        </div>
                    </div>
                    <?php 
                        $count++;
                        endwhile; wp_reset_postdata(); 
                    endif; 
                    ?>
                </div>
                
                <a href="/bang-xep-hang/" class="relative z-10 block text-center w-full mt-8 py-2.5 bg-surface-container text-primary text-[12px] font-black uppercase tracking-widest rounded-xl hover:bg-surface-container-high transition-colors shadow-inner">Khám phá Bảng Xếp Hạng</a>
            </div>

            <!-- Genre Cloud -->
            <div class="bg-surface-container-lowest p-6 rounded-[2rem] border border-outline-variant/20 shadow-sm">
                <h2 class="text-lg font-bold font-headline text-on-background mb-6 flex items-center gap-2">
                    <span class="material-symbols-outlined text-primary">category</span>
                    Thế giới thể loại
                </h2>
                <div class="flex flex-wrap gap-2">
                    <?php 
                    $terms = get_terms(['taxonomy' => 'the_loai', 'number' => 10, 'orderby' => 'count', 'order' => 'DESC']);
                    foreach($terms as $term):
                    ?>
                    <a class="px-3.5 py-1.5 bg-surface-container-low rounded-lg text-xs font-bold text-on-surface-variant hover:bg-primary-container/20 hover:text-primary transition-colors border border-outline-variant/10" href="<?php echo get_term_link($term); ?>">
                        <?php echo esc_html($term->name); ?>
                    </a>
                    <?php endforeach; ?>
                </div>
            </div>

        </aside>
    </div>
</main>

<style>
/* Reset pagination Tailwind alignment */
.template-pagination { display: flex; flex-wrap: wrap; gap: 0.25rem; justify-content: center; align-items: center; }
.template-pagination a, .template-pagination span { display: flex; align-items: center; justify-content: center; width: 2.25rem; height: 2.25rem; border-radius: 9999px; font-weight: 700; transition: all 0.2s; font-size: 0.75rem; color: var(--on-surface-variant); }
.template-pagination .page-numbers:not(.current):not(.dots) { background-color: var(--surface-container-low); border: 1px solid rgba(0,0,0,0.05); cursor: pointer; }
.template-pagination .page-numbers:not(.current):not(.dots):hover { background-color: var(--primary); color: white; border-color: transparent; }
.template-pagination .current { background-color: var(--primary); color: white; box-shadow: 0 4px 14px rgba(0, 96, 169, 0.35); }
.template-pagination .dots { border: none; background: transparent; pointer-events: none; opacity: 0.5; }
</style>

<?php get_footer(); ?>
