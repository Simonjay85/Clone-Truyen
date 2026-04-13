import re

rank_template = """<?php
/*
Template Name: Bảng Xếp Hạng
*/
get_header(); 

// Query Top 10 posts by views
$args = array(
    'post_type'      => 'truyen',
    'posts_per_page' => 10,
    'meta_key'       => '_views',
    'orderby'        => 'meta_value_num',
    'order'          => 'DESC'
);
$ranking_query = new WP_Query($args);

$top3 = array();
$others = array();

if ($ranking_query->have_posts()) {
    $count = 0;
    while ($ranking_query->have_posts()) {
        $ranking_query->the_post();
        $views = (int)get_post_meta(get_the_ID(), '_views', true);
        $views_display = current_user_can('administrator') ? number_format($views) : number_format($views); // format later

        // Simplified view formatting (e.g. 512.8K if > 1000)
        if ($views >= 1000000) {
            $views_formatted = round($views / 1000000, 1) . 'M';
        } else if ($views >= 1000) {
            $views_formatted = round($views / 1000, 1) . 'K';
        } else {
            $views_formatted = $views;
        }

        $author = get_post_meta(get_the_ID(), 'truyen_tacgia', true);
        if(!$author) $author = 'Đang cập nhật';

        $data = array(
            'title' => get_the_title(),
            'link' => get_permalink(),
            'img' => has_post_thumbnail() ? get_the_post_thumbnail_url(get_the_ID(), 'large') : 'https://placehold.co/400x600',
            'author' => $author,
            'views' => $views_formatted,
            'chapters' => wp_count_posts('chuong')->publish // Mock chapters count
        );

        if ($count < 3) {
            $top3[] = $data;
        } else {
            $data['rank'] = $count + 1;
            $others[] = $data;
        }
        $count++;
    }
    wp_reset_postdata();
}
?>

<main class="pt-24 pb-16 px-6 max-w-7xl mx-auto min-h-screen">
    <!-- Header Section -->
    <header class="mb-10 text-center md:text-left">
        <h1 class="font-headline text-4xl font-extrabold text-on-background tracking-tight mb-2">Bảng Xếp Hạng</h1>
        <p class="text-on-surface-variant max-w-2xl">Khám phá những tác phẩm được yêu thích nhất và vinh danh những dịch giả tâm huyết trong cộng đồng.</p>
    </header>

    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
        <!-- Left Column: Rankings List -->
        <div class="lg:col-span-8">
            <!-- Tabs -->
            <div class="flex flex-wrap gap-2 mb-8 bg-surface-container-low p-1.5 rounded-2xl w-fit">
                <button class="px-6 py-2.5 rounded-xl bg-surface-container-lowest text-primary font-bold shadow-sm transition-all text-sm">Toàn Thế Giới</button>
            </div>

            <!-- Top 3 Podium (Visual Focus) -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12 items-end">
                <?php if (isset($top3[1])): ?>
                <!-- Rank 2 -->
                <div class="order-2 md:order-1 bg-surface-container-lowest p-6 rounded-3xl shadow-[0px_12px_32px_rgba(0,96,169,0.04)] text-center relative overflow-hidden group hover:border hover:border-outline-variant/30 cursor-pointer" onclick="window.location.href='<?php echo esc_url($top3[1]['link']); ?>'">
                    <div class="absolute top-4 left-4 bg-slate-200 text-slate-700 w-10 h-10 rounded-full flex items-center justify-center font-bold text-xl z-10 shadow-inner">2</div>
                    <div class="relative mb-4 mx-auto w-32 aspect-[3/4] rounded-xl overflow-hidden shadow-lg group-hover:scale-105 transition-transform duration-500">
                        <img class="w-full h-full object-cover" src="<?php echo esc_url($top3[1]['img']); ?>" />
                    </div>
                    <h3 class="font-headline font-bold text-lg mb-1 line-clamp-1"><?php echo esc_html($top3[1]['title']); ?></h3>
                    <p class="text-xs text-on-surface-variant mb-3">Tác giả: <?php echo esc_html($top3[1]['author']); ?></p>
                    <div class="flex items-center justify-center gap-2 text-primary font-semibold text-sm">
                        <span class="material-symbols-outlined text-sm" data-icon="visibility">visibility</span>
                        <?php echo esc_html($top3[1]['views']); ?>
                    </div>
                </div>
                <?php endif; ?>

                <?php if (isset($top3[0])): ?>
                <!-- Rank 1 (Featured) -->
                <div class="order-1 md:order-2 bg-gradient-to-b from-primary-fixed/20 to-surface-container-lowest p-8 rounded-3xl shadow-[0px_20px_48px_rgba(0,96,169,0.12)] text-center relative overflow-hidden border border-primary/20 group cursor-pointer hover:border-primary/50 transition-colors" onclick="window.location.href='<?php echo esc_url($top3[0]['link']); ?>'">
                    <div class="absolute top-4 left-1/2 -translate-x-1/2 bg-yellow-400 text-on-tertiary-container w-14 h-14 rounded-full flex items-center justify-center font-extrabold text-2xl z-10 shadow-lg border-4 border-white">1</div>
                    <div class="relative mb-6 mx-auto w-44 aspect-[3/4] rounded-2xl overflow-hidden shadow-2xl group-hover:scale-105 transition-transform duration-500">
                        <img class="w-full h-full object-cover" src="<?php echo esc_url($top3[0]['img']); ?>" />
                    </div>
                    <h3 class="font-headline font-extrabold text-xl mb-2 text-primary line-clamp-2"><?php echo esc_html($top3[0]['title']); ?></h3>
                    <p class="text-sm text-on-surface-variant mb-4">Tác giả: <?php echo esc_html($top3[0]['author']); ?></p>
                    <div class="inline-flex items-center justify-center gap-3 bg-primary text-white px-5 py-2 rounded-full font-bold text-sm shadow-md">
                        <span class="material-symbols-outlined" data-icon="trending_up">trending_up</span>
                        <?php echo esc_html($top3[0]['views']); ?> Lượt đọc
                    </div>
                </div>
                <?php endif; ?>

                <?php if (isset($top3[2])): ?>
                <!-- Rank 3 -->
                <div class="order-3 bg-surface-container-lowest p-6 rounded-3xl shadow-[0px_12px_32px_rgba(0,96,169,0.04)] text-center relative overflow-hidden group hover:border hover:border-outline-variant/30 cursor-pointer" onclick="window.location.href='<?php echo esc_url($top3[2]['link']); ?>'">
                    <div class="absolute top-4 left-4 bg-orange-100 text-orange-700 w-10 h-10 rounded-full flex items-center justify-center font-bold text-xl z-10 shadow-inner">3</div>
                    <div class="relative mb-4 mx-auto w-32 aspect-[3/4] rounded-xl overflow-hidden shadow-lg group-hover:scale-105 transition-transform duration-500">
                        <img class="w-full h-full object-cover" src="<?php echo esc_url($top3[2]['img']); ?>" />
                    </div>
                    <h3 class="font-headline font-bold text-lg mb-1 line-clamp-1"><?php echo esc_html($top3[2]['title']); ?></h3>
                    <p class="text-xs text-on-surface-variant mb-3">Tác giả: <?php echo esc_html($top3[2]['author']); ?></p>
                    <div class="flex items-center justify-center gap-2 text-primary font-semibold text-sm">
                        <span class="material-symbols-outlined text-sm" data-icon="visibility">visibility</span>
                        <?php echo esc_html($top3[2]['views']); ?>
                    </div>
                </div>
                <?php endif; ?>
            </div>

            <!-- List Items (4-10) -->
            <div class="space-y-4">
                <?php foreach ($others as $item): ?>
                <a href="<?php echo esc_url($item['link']); ?>" class="block">
                    <div class="bg-surface-container-lowest p-4 rounded-2xl flex items-center gap-6 shadow-sm hover:shadow-md transition-all group hover:border hover:border-primary/20">
                        <div class="w-12 text-center flex-shrink-0">
                            <span class="text-4xl font-black text-outline-variant/40 italic font-headline rank-number-outline">
                                <?php echo str_pad($item['rank'], 2, '0', STR_PAD_LEFT); ?>
                            </span>
                        </div>
                        <div class="w-16 h-20 rounded-lg overflow-hidden flex-shrink-0">
                            <img class="w-full h-full object-cover" src="<?php echo esc_url($item['img']); ?>" />
                        </div>
                        <div class="flex-grow">
                            <h4 class="font-bold text-lg group-hover:text-primary transition-colors line-clamp-1"><?php echo esc_html($item['title']); ?></h4>
                            <div class="flex flex-wrap items-center gap-4 mt-1 text-sm text-on-surface-variant">
                                <span class="flex items-center gap-1"><span class="material-symbols-outlined text-sm" data-icon="person">person</span> <?php echo esc_html($item['author']); ?></span>
                                <span class="flex items-center gap-1"><span class="material-symbols-outlined text-sm" data-icon="auto_stories">auto_stories</span> HOT</span>
                            </div>
                        </div>
                        <div class="text-right hidden sm:block flex-shrink-0 min-w-24">
                            <div class="text-primary font-bold text-lg"><?php echo esc_html($item['views']); ?></div>
                            <div class="text-[10px] text-on-surface-variant uppercase tracking-wider font-semibold">Lượt đọc</div>
                        </div>
                    </div>
                </a>
                <?php endforeach; ?>
            </div>
            
            <?php if (empty($top3)): ?>
            <div class="text-center py-20 opacity-50">
                <p>Chưa có đủ dữ liệu bảng xếp hạng.</p>
            </div>
            <?php endif; ?>
        </div>

        <!-- Right Column: Translators Hall of Fame (Static for now) -->
        <div class="lg:col-span-4 space-y-10">
            <section class="bg-surface-container-low/50 rounded-[2rem] p-8 border border-white/40">
                <div class="flex items-center justify-between mb-8">
                    <h2 class="font-headline font-extrabold text-xl">Vinh Danh Dịch Giả</h2>
                    <span class="material-symbols-outlined text-primary" data-icon="military_tech">military_tech</span>
                </div>
                
                <div class="space-y-6">
                    <!-- Top Group 1 -->
                    <div class="flex items-center gap-4 p-4 rounded-2xl bg-surface-container-lowest shadow-sm hover:translate-x-1 transition-transform cursor-pointer">
                        <div class="w-14 h-14 rounded-full overflow-hidden border-2 border-primary ring-4 ring-primary/5">
                            <img class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAQ4yTXrGQ_eFi6CN9ftADatHjTTssiJtk-POsW9Bm1OUeRUM7SxHV45zL7T_QfaZYYDCTvZ8cNPK0ik_T-i-NJ3kiEehm5r8aa8Y-xd7tlGv7sUfBN1Ftrj63fwJ2v9FwZs-qKTIXEdImPOByBvx2Kk8CZEQUhAY12aY2PrZsegSL8CRHH4oBLQnFT24LZIlZEtHVEcTntFgvWlf_LhRldIo5mjMOEBP9Gc00qwimEDww_9CqCmokAFyt1E1xWdwhYdAQHnhNNm6s" />
                        </div>
                        <div class="flex-grow">
                            <div class="font-bold text-on-background">Nhóm Phượng Hoàng</div>
                            <div class="text-xs text-on-surface-variant font-medium">1.2k Chương / Tháng</div>
                        </div>
                        <div class="bg-primary/10 text-primary px-3 py-1 rounded-full font-bold text-xs">TOP 1</div>
                    </div>

                    <!-- Top Group 2 -->
                    <div class="flex items-center gap-4 p-4 rounded-2xl bg-surface-container-lowest/60 hover:bg-surface-container-lowest transition-all hover:translate-x-1 cursor-pointer">
                        <div class="w-12 h-12 rounded-full overflow-hidden border-2 border-outline-variant">
                            <img class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCb_ptntHeuPeE1Wb5L4_IWDtCWGPJHhWaoJJk3rqQ4Fx-PctWpXLlMe-bWmoiR-d_fyS5tzhBdJeri8yf3aLXHBXUNe5GyHZOzRPnTyRjjfJaD_YqSJQffXxfz5K3vKF6FthgtwlvoeSzG0NvkgxWrmEZI9QIrkHdsYu8rL8dYc8nVNG1AFD24EJtYKAS2KIO14lFfWy-15QcqsLWka0K6mcgjfEt4T1XIYNVcsXE6YwgCqwlbdpd9mf_vZt_zJQT8zBrt3vt7B8o" />
                        </div>
                        <div class="flex-grow">
                            <div class="font-bold text-on-background">Sắc Việt Team</div>
                            <div class="text-xs text-on-surface-variant font-medium">942 Chương / Tháng</div>
                        </div>
                        <div class="bg-slate-200 text-slate-700 px-3 py-1 rounded-full font-bold text-xs">TOP 2</div>
                    </div>

                    <!-- Top Group 3 -->
                    <div class="flex items-center gap-4 p-4 rounded-2xl bg-surface-container-lowest/60 hover:bg-surface-container-lowest transition-all hover:translate-x-1 cursor-pointer">
                        <div class="w-12 h-12 rounded-full overflow-hidden border-2 border-outline-variant">
                            <img class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCUmeHaaI_KUEIaU4_pJvsSsmaMtXXoHoi4S5zMv_cxhk2gsHtEoz3DJq0e-Q_RWB4G_8SckZH7q9hVlebKdMu4yhfru0pXwMrwlfTpMZ8QZeLxxMVuqS0Qtxju3uXgMWFW-RjezopZef561iux-L-oAD3bNo9gGJV1DwMs2CbpGsZM5UFDxCZk-IucolnjdNcBDgX4Q9e8eKwupvTTi-9oSZr2sHguh8gusnbNWZ-WRI588N1BtqIjlmLsw5XRuqRiNOdysLsTYZM" />
                        </div>
                        <div class="flex-grow">
                            <div class="font-bold text-on-background">Độc Hành Giả</div>
                            <div class="text-xs text-on-surface-variant font-medium">756 Chương / Tháng</div>
                        </div>
                        <div class="bg-orange-100 text-orange-700 px-3 py-1 rounded-full font-bold text-xs">TOP 3</div>
                    </div>
                </div>
            </section>
        </div>
    </div>
</main>
<?php get_footer(); ?>
"""

with open("tehi-theme/page-bangxephang.php", "w", encoding="utf-8") as f:
    f.write(rank_template)

# Now update header lines to target /bang-xep-hang/
def update_nav(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We need to target the ranking link. They might have a hash currently href="#"
    content = content.replace('<a href="#" class="text-slate-600 dark:text-slate-400 hover:text-primary transition-colors font-semibold">Bảng xếp hạng</a>', '<a href="/bang-xep-hang" class="text-slate-600 dark:text-slate-400 hover:text-primary transition-colors font-semibold">Bảng xếp hạng</a>')
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

update_nav("tehi-theme/header.php")
update_nav("tehi-theme/header-home.php")

print("Created page-bangxephang.php")
