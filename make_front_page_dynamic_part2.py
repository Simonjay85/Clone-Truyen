import re
import os

path = "tehi-theme/front-page.php"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 2. Truyện Khuyên Đọc (Editor's Choice)
rec_pattern = re.compile(r'(<div class="grid grid-cols-1 md:grid-cols-12 gap-6 h-\[500px\]">)(.*?)(</div>\s*</section>)', re.DOTALL)
rec_php = """
<div class="grid grid-cols-1 md:grid-cols-12 gap-6 h-auto md:h-[500px]">
    <?php
    $hot_args = ['post_type' => 'truyen', 'posts_per_page' => 3, 'meta_key' => '_views', 'orderby' => 'meta_value_num', 'order' => 'DESC'];
    $hot_q = new WP_Query($hot_args);
    $count = 0;
    if($hot_q->have_posts()): while($hot_q->have_posts()): $hot_q->the_post();
        $cover = get_the_post_thumbnail_url(get_the_ID(), 'large') ?: get_post_meta(get_the_ID(), '_cover_image', true);
        $views = get_post_meta(get_the_ID(), '_views', true);
        $views_display = $views ? ($views >= 1000 ? round($views/1000,1).'K' : number_format($views)) : 0;
        
        # Get Latest Chap
        $chap_q = new WP_Query(['post_type'=>'chuong','posts_per_page'=>1,'meta_query'=>[['key'=>'_truyen_id','value'=>get_the_ID(),'compare'=>'=']],'orderby'=>'date','order'=>'DESC']);
        $latest_chap = $chap_q->have_posts() ? $chap_q->posts[0]->post_title : 'Đang cập nhật';
        wp_reset_postdata();

        if ($count == 0):
    ?>
    <div class="md:col-span-8 relative group overflow-hidden rounded-xl shadow-xl h-[500px] md:h-full">
        <img class="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" src="<?php echo esc_url($cover); ?>"/>
        <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent"></div>
        <div class="absolute bottom-0 left-0 p-8 w-full z-10">
            <div class="flex gap-2 mb-3">
                <span class="bg-primary-container text-white text-[10px] font-bold px-3 py-1 rounded-full uppercase tracking-wider">Editor's Choice</span>
            </div>
            <h3 class="text-3xl md:text-4xl font-bold text-white mb-3 line-clamp-2"><?php the_title(); ?></h3>
            <p class="text-white/80 max-w-xl line-clamp-2 mb-6"><?php echo wp_trim_words(get_the_excerpt() ?: get_the_content(), 20); ?></p>
            <a href="<?php the_permalink(); ?>" class="inline-flex bg-white text-primary font-bold px-8 py-3 rounded-full hover:bg-blue-50 transition-colors items-center gap-2">
                Đọc ngay <span class="material-symbols-outlined text-sm">menu_book</span>
            </a>
        </div>
    </div>
    <div class="md:col-span-4 flex flex-col gap-6 h-[500px] md:h-full">
    <?php else: ?>
        <div class="flex-1 relative group overflow-hidden rounded-xl shadow-lg h-1/2">
            <img class="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" src="<?php echo esc_url($cover); ?>"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent"></div>
            <a href="<?php the_permalink(); ?>" class="absolute inset-0 z-10"></a>
            <div class="absolute bottom-0 left-0 p-5 z-20 pointer-events-none">
                <h4 class="text-xl font-bold text-white line-clamp-1"><?php the_title(); ?></h4>
                <p class="text-white/70 text-xs mt-1"><?php echo $latest_chap; ?> • <?php echo $views_display; ?> lượt đọc</p>
            </div>
        </div>
    <?php endif; $count++; endwhile; ?>
    </div>
    <?php wp_reset_postdata(); endif; ?>
"""
content = rec_pattern.sub(r'\1' + rec_php + r'\3', content)

# 3. Mới Cập Nhật
new_pattern = re.compile(r'(<div class="grid grid-cols-2 sm:grid-cols-3 xl:grid-cols-4 gap-6">)(.*?)(</div>\s*</section>)', re.DOTALL)
new_php = """
    <?php
    $new_args = ['post_type' => 'truyen', 'posts_per_page' => 12, 'orderby' => 'date', 'order' => 'DESC'];
    $new_q = new WP_Query($new_args);
    if($new_q->have_posts()): while($new_q->have_posts()): $new_q->the_post();
        $cover = get_the_post_thumbnail_url(get_the_ID(), 'medium') ?: get_post_meta(get_the_ID(), '_cover_image', true);
        
        $chap_q = new WP_Query(['post_type'=>'chuong','posts_per_page'=>1,'meta_query'=>[['key'=>'_truyen_id','value'=>get_the_ID(),'compare'=>'=']],'orderby'=>'date','order'=>'DESC']);
        $latest_chap = $chap_q->have_posts() ? $chap_q->posts[0]->post_title : 'Đang cập nhật';
        wp_reset_postdata();
    ?>
    <a href="<?php the_permalink(); ?>" class="group block">
        <div class="relative aspect-[3/4] mb-3 overflow-hidden rounded-xl bg-surface-container-low shadow-sm group-hover:shadow-md transition-all">
            <?php if($cover): ?>
                <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="<?php echo esc_url($cover); ?>" />
            <?php else: ?>
                <div class="w-full h-full bg-gradient-to-br from-blue-100 to-blue-200 flex items-center justify-center p-4">
                    <span class="text-blue-800 font-bold text-center text-sm"><?php the_title(); ?></span>
                </div>
            <?php endif; ?>
            <div class="absolute top-2 right-2 flex flex-col gap-1 z-10">
                <span class="bg-primary-container text-white text-[10px] font-bold px-2 py-0.5 rounded-md shadow-sm">NEW</span>
            </div>
            <div class="absolute inset-0 bg-black/opacity-0 group-hover:bg-black/10 transition-colors z-0"></div>
        </div>
        <h3 class="font-bold text-on-surface group-hover:text-primary transition-colors line-clamp-1"><?php the_title(); ?></h3>
        <p class="text-on-surface-variant text-xs mt-1 truncate"><?php echo $latest_chap; ?> • <?php echo human_time_diff(get_the_time('U'), current_time('timestamp')); ?> trước</p>
    </a>
    <?php endwhile; wp_reset_postdata(); endif; ?>
"""
content = new_pattern.sub(r'\1\n' + new_php + r'\n\3', content)

# 4. BXH
bxh_pattern = re.compile(r'(<div class="space-y-6">)(.*?)(</div>\s*<button)', re.DOTALL)
bxh_php = """
    <?php
    $rank_args = ['post_type' => 'truyen', 'posts_per_page' => 10, 'meta_key' => '_views', 'orderby' => 'meta_value_num', 'order' => 'DESC'];
    $rank_q = new WP_Query($rank_args);
    $idx = 1;
    if($rank_q->have_posts()): while($rank_q->have_posts()): $rank_q->the_post();
        $cover = get_the_post_thumbnail_url(get_the_ID(), 'thumbnail') ?: get_post_meta(get_the_ID(), '_cover_image', true);
        $views = get_post_meta(get_the_ID(), '_views', true);
        $views_display = $views ? ($views >= 1000 ? round($views/1000,1).'K' : number_format($views)) : 0;
        
        $badge_color = 'bg-surface-container-highest text-on-surface-variant';
        if ($idx == 1) $badge_color = 'bg-primary text-white';
        else if ($idx == 2) $badge_color = 'bg-slate-400 text-white';
        else if ($idx == 3) $badge_color = 'bg-amber-600 text-white';
    ?>
    <a href="<?php the_permalink(); ?>" class="flex items-center gap-4 group cursor-pointer">
        <div class="relative flex-shrink-0">
            <span class="absolute -top-2 -left-2 w-6 h-6 <?php echo $badge_color; ?> text-xs font-bold flex items-center justify-center rounded-full shadow-md z-10"><?php echo $idx; ?></span>
            <div class="w-16 h-20 rounded-lg overflow-hidden bg-surface-container-highest">
                <?php if($cover): ?>
                    <img class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300" src="<?php echo esc_url($cover); ?>" />
                <?php else: ?>
                    <div class="w-full h-full bg-blue-100"></div>
                <?php endif; ?>
            </div>
        </div>
        <div class="flex-1 min-w-0">
            <h4 class="font-bold text-on-surface line-clamp-1 group-hover:text-primary transition-colors"><?php the_title(); ?></h4>
            <div class="text-on-surface-variant text-xs flex items-center gap-1 mt-1">
                <span class="material-symbols-outlined text-[14px] text-primary" style="font-variation-settings: 'FILL' 1;">visibility</span> <?php echo $views_display; ?> lượt xem
            </div>
        </div>
    </a>
    <?php $idx++; endwhile; wp_reset_postdata(); endif; ?>
"""
content = bxh_pattern.sub(r'\1\n' + bxh_php + r'\n\3', content)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Dynamicized front-page.php")
