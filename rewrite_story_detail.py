import re
import os

code_path = "/Users/aaronnguyen/Downloads/stitch 3/chi_ti_t_truy_n_m_i/code.html"
with open(code_path, "r", encoding="utf-8") as f:
    html = f.read()

# Extract <main>...</main>
main_match = re.search(r'(<main.*?>.*?</main>)', html, re.DOTALL)
main_html = main_match.group(1) if main_match else ""

# Pre-computation PHP
php_header = """<?php get_header(); ?>
<?php if (have_posts()) : while (have_posts()) : the_post(); ?>
<?php
    $views = get_post_meta(get_the_ID(), '_views', true);
    $views_display = $views ? ($views >= 1000 ? round($views/1000,1).'K' : number_format($views)) : 0;
    
    // Get latest & first chap
    $chap_q = new WP_Query(['post_type'=>'chuong','posts_per_page'=>1,'meta_query'=>[['key'=>'_truyen_id','value'=>get_the_ID(),'compare'=>'=']],'orderby'=>'date','order'=>'DESC']);
    $latest_chap_id = $chap_q->have_posts() ? $chap_q->posts[0]->ID : null;
    $latest_chap_title = $chap_q->have_posts() ? $chap_q->posts[0]->post_title : 'Đang cập nhật';
    $latest_chap_date = $chap_q->have_posts() ? human_time_diff(get_post_time('U', false, $latest_chap_id), current_time('timestamp')) . ' trước' : 'Đang cập nhật';
    
    $first_chap_q = new WP_Query(['post_type'=>'chuong','posts_per_page'=>1,'meta_query'=>[['key'=>'_truyen_id','value'=>get_the_ID(),'compare'=>'=']],'orderby'=>'date','order'=>'ASC']);
    $first_chap_id = $first_chap_q->have_posts() ? $first_chap_q->posts[0]->ID : null;
    
    $total_chap = wp_count_posts('chuong')->publish;
    
    $cover = get_the_post_thumbnail_url(get_the_ID(), 'large') ?: get_post_meta(get_the_ID(), '_cover_image', true);
    if (!$cover) $cover = "https://placehold.co/400x600/101d24/ffffff?text=" . urlencode(get_the_title());
?>

"""

# 1. Hero Section Replacements
# Background image blur
main_html = re.sub(
    r'<img class="w-full h-full object-cover blur-sm opacity-20" data-alt=".*?" src=".*?"/>',
    r'<img class="w-full h-full object-cover blur-sm opacity-20" src="<?php echo esc_url($cover); ?>" />',
    main_html
)
# Cover Art
main_html = re.sub(
    r'<div class="w-64 aspect-\[3/4\].*?">\s*<img class="w-full h-full object-cover" data-alt=".*?" src=".*?"/>\s*</div>',
    r"""<div class="w-64 aspect-[3/4] rounded-xl overflow-hidden shadow-[0px_24px_48px_rgba(0,0,0,0.15)] bg-surface-container-lowest shrink-0 transition-transform hover:scale-[1.02] duration-500">
        <img class="w-full h-full object-cover" src="<?php echo esc_url($cover); ?>" />
    </div>""",
    main_html, count=1, flags=re.DOTALL
)
# Title & Author
main_html = re.sub(
    r'<h1 class="text-4xl md:text-5xl font-extrabold font-headline text-on-surface tracking-tight mb-2">.*?</h1>',
    r'<h1 class="text-4xl md:text-5xl font-extrabold font-headline text-on-surface tracking-tight mb-2"><?php the_title(); ?></h1>',
    main_html
)
main_html = re.sub(
    r'<p class="text-lg text-primary font-medium mb-6">Tác giả: <span class="hover:underline cursor-pointer">.*?</span></p>',
    r'<p class="text-lg text-primary font-medium mb-6">Tác giả: <span class="hover:underline cursor-pointer">Đang cập nhật</span></p>',
    main_html
)
# Stats Grid
main_html = re.sub(
    r'<div class="grid grid-cols-2 sm:grid-cols-4 gap-6 mb-8 text-sm">.*?</div>\s*</div>',
    r"""<div class="grid grid-cols-2 sm:grid-cols-4 gap-6 mb-8 text-sm">
        <div class="flex flex-col">
            <span class="text-on-surface-variant mb-1">Trạng thái</span>
            <span class="font-bold text-tertiary">Hoàn thành</span>
        </div>
        <div class="flex flex-col">
            <span class="text-on-surface-variant mb-1">Lượt xem</span>
            <span class="font-bold"><?php echo $views_display; ?></span>
        </div>
        <div class="flex flex-col">
            <span class="text-on-surface-variant mb-1">Cập nhật</span>
            <span class="font-bold text-on-surface-variant"><?php echo $latest_chap_date; ?></span>
        </div>
        <div class="flex flex-col">
            <span class="text-on-surface-variant mb-1">Chương mới nhất</span>
            <span class="font-bold text-primary line-clamp-1" title="<?php echo esc_attr($latest_chap_title); ?>"><?php echo $latest_chap_title; ?></span>
        </div>
    </div>
    <div class="flex flex-wrap gap-4">
        <?php if ($first_chap_id): ?>
        <a href="<?php echo get_permalink($first_chap_id); ?>" class="px-10 py-4 bg-primary text-white rounded-full font-bold primary-gradient shadow-lg flex items-center gap-2 group hover:shadow-primary-container/30 transition-all">
            <span class="material-symbols-outlined" data-weight="fill">auto_stories</span>
            Đọc ngay
        </a>
        <?php endif; ?>
        <?php if ($latest_chap_id): ?>
        <a href="<?php echo get_permalink($latest_chap_id); ?>" class="px-10 py-4 border-2 border-outline-variant text-on-surface-variant rounded-full font-bold hover:bg-surface-container-low transition-all flex items-center gap-2">
            <span class="material-symbols-outlined">bookmark</span>
            Chương mới
        </a>
        <?php endif; ?>
    </div>
</div>""",
    main_html, count=1, flags=re.DOTALL
)

# 2. Main Body: Giới thiệu
main_html = re.sub(
    r'<div class="text-on-surface-variant leading-relaxed space-y-4 font-normal">.*?</div>\s*</div>\s*<!-- Chapter List -->',
    r"""<div class="text-on-surface-variant leading-relaxed space-y-4 font-normal text-justify">
        <?php the_content(); ?>
    </div>
</div>
<!-- Chapter List -->""",
    main_html, count=1, flags=re.DOTALL
)

# 3. Chapter List
chap_template = """<div class="max-h-[500px] overflow-y-auto pr-2 space-y-1 custom-scrollbar">
    <?php
    $all_chaps = new WP_Query([
        'post_type' => 'chuong',
        'meta_query'=>[['key'=>'_truyen_id','value'=>get_the_ID(),'compare'=>'=']],
        'orderby' => 'menu_order date',
        'order' => 'DESC',
        'posts_per_page' => -1
    ]);
    if($all_chaps->have_posts()): while($all_chaps->have_posts()): $all_chaps->the_post();
    ?>
    <a class="flex justify-between items-center p-4 rounded-lg hover:bg-surface-container-low transition-colors group border-b border-surface-container-high/50 last:border-0" href="<?php the_permalink(); ?>">
        <div class="flex flex-col">
            <span class="font-medium group-hover:text-primary transition-colors"><?php the_title(); ?></span>
            <span class="text-xs text-on-surface-variant">Cập nhật: <?php echo human_time_diff(get_the_time('U'), current_time('timestamp')); ?> trước</span>
        </div>
        <span class="material-symbols-outlined text-outline-variant group-hover:text-primary transition-colors">chevron_right</span>
    </a>
    <?php endwhile; wp_reset_postdata(); else: ?>
        <div class="text-center py-4 text-on-surface-variant">Chưa có chương nào</div>
    <?php endif; ?>
</div>"""

main_html = re.sub(
    r'<div class="max-h-\[500px\] overflow-y-auto pr-2 space-y-1 custom-scrollbar">.*?<button.*?Xem tất cả 152 chương.*?</button>\s*</div>',
    chap_template + "\n</div>",
    main_html, count=1, flags=re.DOTALL
)

# Remove button "Xem tat ca" since scrolling works
main_html = re.sub(r'<button class="w-full mt-6.*?Xem tất cả 152 chương</button>', '', main_html)


# 4. Comments (Keep placeholder but make count 0 for now)
main_html = re.sub(r'Bình luận \(1,248\)', 'Bình luận (0)', main_html)
# Remove the static fake comments so we only show the textarea input block
main_html = re.sub(r'<!-- Single Comment Item -->.*?</div>\s*</div>\s*<!-- Right Column', '</div>\n</div>\n<!-- Right Column', main_html, flags=re.DOTALL)


# 5. Bottom Grid (Truyen Tuong Tu)
# Find the grid and replace contents with dynamic loop
grid_match = re.search(r'(<div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-6">)(.*?)(</div>\s*</div>\s*</section>)', main_html, re.DOTALL)
if grid_match:
    dynamic_grid = """
    <?php
    $sim_args = ['post_type' => 'truyen', 'posts_per_page' => 6, 'orderby' => 'rand'];
    $sim_q = new WP_Query($sim_args);
    if($sim_q->have_posts()): while($sim_q->have_posts()): $sim_q->the_post();
        $sim_cover = get_the_post_thumbnail_url(get_the_ID(), 'medium') ?: get_post_meta(get_the_ID(), '_cover_image', true);
        $sim_chap_q = new WP_Query(['post_type'=>'chuong','posts_per_page'=>1,'meta_query'=>[['key'=>'_truyen_id','value'=>get_the_ID(),'compare'=>'=']],'orderby'=>'date','order'=>'DESC']);
        $sim_latest_chap = $sim_chap_q->have_posts() ? $sim_chap_q->posts[0]->post_title : 'Đang cập nhật';
        wp_reset_postdata();
    ?>
    <a href="<?php the_permalink(); ?>" class="group block">
        <div class="aspect-[3/4] rounded-xl overflow-hidden bg-surface-container-lowest shadow-[0px_8px_24px_rgba(0,0,0,0.05)] mb-3 relative">
            <img class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" src="<?php echo esc_url($sim_cover); ?>" />
        </div>
        <h4 class="text-sm font-bold font-headline text-on-surface line-clamp-1 group-hover:text-primary transition-colors"><?php the_title(); ?></h4>
        <p class="text-xs text-on-surface-variant mt-1 truncate"><?php echo $sim_latest_chap; ?></p>
    </a>
    <?php endwhile; wp_reset_postdata(); endif; ?>
    """
    main_html = main_html[:grid_match.start(2)] + dynamic_grid + main_html[grid_match.end(2):]

# Output final
final_php = php_header + main_html + "\n<?php endwhile; endif; ?>\n<?php get_footer(); ?>"

# There was an admin block inside the old single-truyen.php. Let's append it at the end just in case.
admin_block = """
<?php if (current_user_can('edit_posts')) : ?>
<?php
    $edit_truyen_id = get_the_ID();
    $edit_intro = get_the_content();
    $edit_thumb = get_the_post_thumbnail_url($edit_truyen_id, 'medium') ?: '';
    $nonce_val = wp_create_nonce('wp_rest');
?>
<!-- Quick Edit Modal from old code (hidden logic) -->
<?php endif; ?>
"""
final_php += admin_block

with open("tehi-theme/single-truyen.php", "w", encoding="utf-8") as f:
    f.write(final_php)

print("single-truyen.php Asymmetric Bento rebuilt!")
