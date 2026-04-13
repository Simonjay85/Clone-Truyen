import re

with open("tehi-theme/single-truyen.php", "r", encoding="utf-8") as f:
    orig = f.read()

admin_block = re.search(r'(<\?php if \(current_user_can\(\'edit_posts\'\)\) : \?>.*)', orig, re.DOTALL)
admin_php = admin_block.group(1) if admin_block else ""

tailwind_ui = """<?php get_header(); ?>
<?php if (have_posts()) : while (have_posts()) : the_post(); ?>
<?php
    $views = get_post_meta(get_the_ID(), '_views', true);
    $views_display = $views ? ($views >= 1000 ? round($views/1000,1).'K' : number_format($views)) : 0;
    
    // Get latest & first chap
    $chap_q = new WP_Query(['post_type'=>'chuong','posts_per_page'=>1,'meta_query'=>[['key'=>'_truyen_id','value'=>get_the_ID(),'compare'=>'=']],'orderby'=>'date','order'=>'DESC']);
    $latest_chap_id = $chap_q->have_posts() ? $chap_q->posts[0]->ID : null;
    $latest_chap_title = $chap_q->have_posts() ? $chap_q->posts[0]->post_title : 'Đang cập nhật';
    $latest_chap_date = $chap_q->have_posts() ? human_time_diff(get_post_time('U', false, $latest_chap_id), current_time('timestamp')) . ' trước' : '';
    
    $first_chap_q = new WP_Query(['post_type'=>'chuong','posts_per_page'=>1,'meta_query'=>[['key'=>'_truyen_id','value'=>get_the_ID(),'compare'=>'=']],'orderby'=>'date','order'=>'ASC']);
    $first_chap_id = $first_chap_q->have_posts() ? $first_chap_q->posts[0]->ID : null;
    
    $total_chap = wp_count_posts('chuong')->publish; // approximation or specific query later
    
    $cover = get_the_post_thumbnail_url(get_the_ID(), 'large') ?: get_post_meta(get_the_ID(), '_cover_image', true);
    if (!$cover) $cover = "https://placehold.co/400x600/101d24/ffffff?text=" . urlencode(get_the_title());
?>

<main class="pt-24 pb-12 max-w-7xl mx-auto px-6">
    <!-- Breadcrumb -->
    <nav class="flex text-sm text-on-surface-variant mb-6 font-['Plus_Jakarta_Sans']">
        <a href="<?php echo home_url('/'); ?>" class="hover:text-primary transition-colors">Trang chủ</a>
        <span class="mx-2">&rsaquo;</span>
        <span class="text-on-surface font-bold"><?php the_title(); ?></span>
    </nav>

    <!-- Glassmorphism Story Hero -->
    <section class="relative bg-surface-container-low rounded-3xl p-6 md:p-10 shadow-lg overflow-hidden mb-12">
        <div class="absolute inset-0 bg-cover bg-center opacity-10 blur-3xl transform scale-110" style="background-image: url('<?php echo esc_url($cover); ?>');"></div>
        <div class="relative z-10 flex flex-col md:flex-row gap-10">
            <!-- Cover Art -->
            <div class="w-full md:w-72 flex-shrink-0">
                <div class="aspect-[3/4] rounded-xl overflow-hidden shadow-[0px_12px_32px_rgba(0,96,169,0.2)]">
                    <img src="<?php echo esc_url($cover); ?>" class="w-full h-full object-cover" />
                </div>
            </div>
            
            <!-- Metadata -->
            <div class="flex-1 flex flex-col justify-center">
                <div class="flex gap-2 mb-4">
                    <span class="bg-surface-container-highest text-on-surface font-bold text-[10px] px-3 py-1 rounded-full uppercase tracking-wider">Tiên Hiệp</span>
                    <span class="bg-primary/10 text-primary font-bold text-[10px] px-3 py-1 rounded-full uppercase tracking-wider">Hoàn Thành</span>
                </div>
                <h1 class="text-4xl md:text-5xl font-extrabold text-on-surface leading-tight mb-4"><?php the_title(); ?></h1>
                
                <div class="flex flex-wrap gap-x-8 gap-y-4 text-sm font-medium text-on-surface-variant mb-8 bg-surface-container-highest/50 p-4 rounded-2xl backdrop-blur-sm w-fit">
                    <div class="flex flex-col">
                        <span class="text-[10px] uppercase tracking-wider opacity-70">Tác giả</span>
                        <span class="text-on-surface font-bold mt-1">Đang cập nhật</span>
                    </div>
                    <div class="w-px bg-outline-variant/30"></div>
                    <div class="flex flex-col">
                        <span class="text-[10px] uppercase tracking-wider opacity-70">Lượt đọc</span>
                        <span class="text-primary font-bold mt-1 flex items-center gap-1"><span class="material-symbols-outlined text-sm">visibility</span> <?php echo $views_display; ?></span>
                    </div>
                    <div class="w-px bg-outline-variant/30"></div>
                    <div class="flex flex-col">
                        <span class="text-[10px] uppercase tracking-wider opacity-70">Chương mới nhất</span>
                        <span class="text-on-surface font-bold mt-1 text-primary"><?php echo $latest_chap_title; ?></span>
                    </div>
                </div>

                <div class="flex flex-wrap items-center gap-4">
                    <?php if ($first_chap_id): ?>
                    <a href="<?php echo get_permalink($first_chap_id); ?>" class="bg-gradient-to-br from-primary to-primary-container text-white font-bold px-8 py-4 rounded-full shadow-lg shadow-primary/20 hover:shadow-primary/40 active:scale-95 transition-all flex items-center gap-2">
                        Đọc Từ Đầu <span class="material-symbols-outlined">menu_book</span>
                    </a>
                    <?php endif; ?>
                    
                    <?php if ($latest_chap_id): ?>
                    <a href="<?php echo get_permalink($latest_chap_id); ?>" class="bg-surface-container-highest text-on-surface hover:bg-surface-dim font-bold px-8 py-4 rounded-full transition-all border border-outline-variant/20 flex items-center gap-2">
                        Chương Mới Nhất
                    </a>
                    <?php endif; ?>
                </div>
            </div>
        </div>
    </section>

    <!-- Synopsis & Chapters Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
        <!-- Main Content -->
        <div class="lg:col-span-8 flex flex-col gap-10">
            <!-- Giới Thiệu -->
            <section class="bg-surface-container-lowest p-8 rounded-3xl shadow-sm border border-outline-variant/10">
                <h2 class="text-2xl font-bold text-on-surface mb-6 flex items-center gap-2">
                    <span class="material-symbols-outlined text-primary">info</span> Giới Thiệu
                </h2>
                <div class="prose prose-slate dark:prose-invert max-w-none text-on-surface-variant font-['Inter'] leading-relaxed">
                    <?php the_content(); ?>
                </div>
            </section>

            <!-- Danh Sách Chương -->
            <section class="bg-surface-container-lowest p-8 rounded-3xl shadow-sm border border-outline-variant/10">
                <div class="flex justify-between items-end mb-6">
                    <h2 class="text-2xl font-bold text-on-surface flex items-center gap-2">
                        <span class="material-symbols-outlined text-primary">format_list_bulleted</span> Danh Sách Chương
                    </h2>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-x-4 gap-y-2">
                    <?php
                    $all_chaps = new WP_Query([
                        'post_type' => 'chuong',
                        'meta_query'=>[['key'=>'_truyen_id','value'=>get_the_ID(),'compare'=>'=']],
                        'orderby' => 'menu_order date',
                        'order' => 'ASC',
                        'posts_per_page' => -1
                    ]);
                    if($all_chaps->have_posts()): while($all_chaps->have_posts()): $all_chaps->the_post();
                    ?>
                    <a href="<?php the_permalink(); ?>" class="group flex items-center py-3 px-4 rounded-xl hover:bg-surface-container-low transition-colors border border-transparent hover:border-outline-variant/20">
                        <span class="font-medium text-on-surface group-hover:text-primary transition-colors line-clamp-1"><?php the_title(); ?></span>
                    </a>
                    <?php endwhile; wp_reset_postdata(); else: ?>
                    <div class="col-span-full text-center py-10 text-on-surface-variant">Chưa có chương nào</div>
                    <?php endif; ?>
                </div>
            </section>
        </div>
        
        <!-- Sidebar -->
        <aside class="lg:col-span-4 flex flex-col gap-6">
            <div class="bg-gradient-to-br from-primary to-primary-container rounded-2xl p-8 text-white relative overflow-hidden shadow-lg shadow-primary/10">
                <div class="relative z-10">
                    <h3 class="text-xl font-bold mb-2">Trở thành Premium</h3>
                    <p class="text-white/80 text-sm mb-6">Đọc truyện không quảng cáo, tải truyện offline và hơn thế nữa.</p>
                    <button class="bg-white text-primary font-bold px-6 py-2 rounded-full text-sm shadow-lg shadow-black/10 hover:shadow-black/20 hover:scale-105 transition-all">Nâng Cấp</button>
                </div>
                <span class="material-symbols-outlined absolute -bottom-8 -right-8 text-[160px] opacity-[0.15] rotate-12">workspace_premium</span>
            </div>
            
            <div class="bg-surface-container-low p-6 rounded-2xl border border-outline-variant/10">
                 <h3 class="font-bold text-on-surface mb-4">Hoạt động sôi nổi</h3>
                 <div class="text-on-surface-variant text-sm text-center py-6">Chưa có bình luận nào</div>
            </div>
        </aside>
    </div>

</main>

<?php endwhile; endif; ?>
""" + admin_php

with open("tehi-theme/single-truyen.php", "w", encoding="utf-8") as f:
    f.write(tailwind_ui)

print("single-truyen.php rewritten!")
