<?php
/*
Template Name: Bảng Xếp Hạng
*/
global $tehi_tailwind_page;
$tehi_tailwind_page = true;
get_header();

$time_filter = isset($_GET['time']) ? $_GET['time'] : 'all';
$top_filter = isset($_GET['top']) ? (int)$_GET['top'] : 100;

$query_args = [
    'post_type' => 'truyen',
    'posts_per_page' => $top_filter,
    'meta_key' => '_views',
    'orderby' => 'meta_value_num',
    'order' => 'DESC'
];

// Fallback logic for time filtering since views are all-time.
// We filter by post_modified to show trending/active within that timeframe.
if ($time_filter !== 'all') {
    $date_query = [];
    if ($time_filter === 'day') {
        $date_query = ['after' => '1 day ago'];
    } elseif ($time_filter === 'week') {
        $date_query = ['after' => '1 week ago'];
    } elseif ($time_filter === 'month') {
        $date_query = ['after' => '1 month ago'];
    } elseif ($time_filter === 'year') {
        $date_query = ['after' => '1 year ago'];
    }
    
    if (!empty($date_query)) {
        $query_args['date_query'] = [
            array_merge($date_query, ['column' => 'post_modified_gmt'])
        ];
    }
}

$bxh_query = new WP_Query($query_args);
$posts = $bxh_query->posts;

// Helper variables
$bg_image = "https://lh3.googleusercontent.com/aida-public/AB6AXuBV_SP1Lo5K64DTSZmS8kWMxUUBd-Vbi2TEetTZaMs5X_QwTAja1I0K-yM2KMObZYiWz3ohHAgh0g00e9Om8UE-x3H_0iCihRdoy25RvXkpgjZuvIDQLkB2nJ-Pj6Loo4dJkr1avsg80s9n676nonOdgYCusDVhpBK0U50krmKpNGn0GBFFb1b3OFe2vaWgE_Oui4rW9m2cuyirydWRJh79PHWKIcPjm6WKnIcF9FlQ6CyrvwSe_XDrKwhVV5jGfqbVXFXVariiVeo";

?>

<main class="pt-24 pb-20 px-4 w-full max-w-[95%] 2xl:max-w-[1400px] mx-auto flex-grow">
    
    <!-- Hero / Header Section -->
    <header class="mb-10 relative overflow-hidden flex flex-col md:flex-row items-center justify-between rounded-[2rem] bg-gradient-to-r from-surface-container-low to-surface-container-highest p-8 md:p-12 border border-gray-200 shadow-sm">
        
        <!-- Background decorative blob -->
        <div class="absolute -top-40 -right-40 w-96 h-96 bg-blue-600/10 rounded-full blur-[80px] pointer-events-none"></div>

        <div class="relative z-10 md:w-3/5">
            <nav class="flex items-center gap-2 text-xs font-bold text-gray-500 mb-6 uppercase tracking-widest">
                <a href="<?php echo home_url(); ?>" class="hover:text-blue-600 transition-colors">Trang chủ</a>
                <span class="material-symbols-outlined text-[14px]">chevron_right</span>
                <span class="text-blue-600 border-b border-blue-600/30">Bảng Xếp Hạng</span>
            </nav>
            <h1 class="font-headline text-5xl md:text-6xl font-black tracking-tighter text-gray-900 mb-6">
                Bảng <span class="bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-blue-400">Xếp Hạng</span>
            </h1>
            <p class="text-gray-500 text-lg font-medium leading-relaxed max-w-prose border-l-4 border-blue-600/30 pl-4">
                Vinh danh những cực phẩm được cộng đồng yêu thích nhất. Đua top khốc liệt, tranh giành ngôi vương.
            </p>
        </div>

        <div class="relative z-10 hidden md:block">
            <!-- Clear vibrant image instead of blurred -->
            <div class="w-56 h-56 rounded-full overflow-hidden border-4 border-white shadow-xl shadow-blue-600/20 transform rotate-3 hover:rotate-0 transition-transform duration-500">
                <img class="w-full h-full object-cover" src="<?php echo esc_url($bg_image); ?>" alt="Rankings"/>
            </div>
        </div>
    </header>

    <!-- Filters & Controls -->
    <div class="mb-12 flex flex-col xl:flex-row items-center justify-between gap-6 bg-white p-4 rounded-3xl border border-gray-200 shadow-sm sticky top-20 z-40">
        
        <!-- Time Tabs -->
        <div class="flex flex-wrap gap-1 bg-gray-100 p-1.5 rounded-2xl w-full xl:w-auto">
            <?php 
                $current_url_path = strtok($_SERVER["REQUEST_URI"], '?');
                $times = ['day' => 'Ngày', 'week' => 'Tuần', 'month' => 'Tháng', 'year' => 'Năm', 'all' => 'Tất cả'];
                foreach($times as $k => $v): 
                    $active = ($time_filter === $k);
            ?>
            <a href="<?php echo esc_url($current_url_path); ?>?time=<?php echo $k; ?>&top=<?php echo $top_filter; ?>" class="flex-1 xl:flex-none text-center py-2 px-6 rounded-xl font-bold text-sm transition-all duration-300 <?php echo $active ? 'bg-blue-600 shadow-[0_2px_8px_rgba(0,0,0,0.06)] text-white' : 'text-gray-500 hover:text-blue-600 hover:bg-white/50'; ?>">
                <?php echo $v; ?>
            </a>
            <?php endforeach; ?>
        </div>

        <!-- Limits & Layout Tools -->
        <div class="flex items-center gap-4 w-full xl:w-auto justify-between xl:justify-end">
            <span class="text-xs font-bold text-gray-400 uppercase tracking-widest hidden md:inline">Hiển thị</span>
            <div class="flex gap-2">
                <?php foreach([10, 50, 100] as $lim): $active = ($top_filter === $lim); ?>
                <a href="<?php echo esc_url($current_url_path); ?>?time=<?php echo $time_filter; ?>&top=<?php echo $lim; ?>" class="px-4 py-1.5 rounded-full text-xs font-bold transition-all border <?php echo $active ? 'bg-blue-600 text-white border-blue-600 shadow-md shadow-blue-600/20' : 'bg-gray-100est text-gray-900 border-gray-300 hover:border-blue-600/50'; ?>">
                    Top <?php echo $lim; ?>
                </a>
                <?php endforeach; ?>
            </div>
        </div>
    </div>

    <!-- Leaderboard Content -->
    <?php if (count($posts) > 0) : ?>
    
    <!-- TOP 3 PODIUM -->
    <div class="grid grid-cols-3 gap-2 md:gap-8 mb-10 md:mb-16 items-end mt-8 md:mt-0">
        <?php 
        // We rearrange the top 3 visually: Rank 2, Rank 1, Rank 3 on Desktop AND Mobile
        $top3 = array_slice($posts, 0, 3);
        $order_classes = ['order-2', 'order-1', 'order-3']; // Both Mobile and Desktop Order: 2, 1, 3
        $heights = ['h-[220px] md:h-[460px]', 'h-[250px] md:h-[500px]', 'h-[200px] md:h-[420px]']; // Responsive heights
        $badges = [
            2 => ['Silver', 'bg-slate-300 text-slate-800 border-slate-400', '★'],
            1 => ['Gold', 'bg-gradient-to-r from-amber-300 to-yellow-500 text-amber-900 border-yellow-300', '♛'],
            3 => ['Bronze', 'bg-[#cd7f32]/20 text-[#cd7f32] border-[#cd7f32]/30', '★']
        ];
        
        foreach ($top3 as $idx => $post) : 
            $rank = $idx + 1;
            setup_postdata($post);
            $views = (int)get_post_meta($post->ID, '_views', true);
            $formatted_views = $views > 1000 ? round($views/1000, 1) . 'K' : $views;
            $author = get_post_meta($post->ID, 'truyen_tacgia', true);
            if(!$author) $author = 'Bạch Lão Đại';
            $cover = has_post_thumbnail($post->ID) ? get_the_post_thumbnail_url($post->ID, 'large') : 'https://placehold.co/400x600?text=Cover';
            
            // Map array index to display structure
            $disp_idx = ($rank == 1) ? 1 : (($rank == 2) ? 0 : 2);
            $badge = $badges[$rank];
        ?>
        <div class="relative group cursor-pointer <?php echo $order_classes[$disp_idx]; ?> flex flex-col justify-end" onclick="window.location.href='<?php echo get_permalink($post->ID); ?>'">
            
            <!-- Podium Card -->
            <div class="bg-white rounded-xl md:rounded-3xl p-2 md:p-4 shadow-[0_8px_30px_rgba(0,0,0,0.04)] border border-gray-200 group-hover:shadow-[0_20px_40px_rgba(0,96,169,0.1)] group-hover:border-blue-600/20 transition-all duration-500 flex flex-col items-center <?php echo $heights[$disp_idx]; ?>">
                
                <!-- Rank Medal -->
                <div class="absolute -top-4 md:-top-6 left-1/2 -translate-x-1/2 w-8 h-8 md:w-14 md:h-14 rounded-full flex items-center justify-center font-black text-xs md:text-2xl shadow-md border-2 z-20 <?php echo $badge[1]; ?> transform group-hover:scale-110 transition-transform">
                    <?php echo $rank; ?>
                </div>

                <!-- Cover Image -->
                <!-- Mobile: hide cover? No, keep it small! Aspect 3/4 -->
                <div class="w-full aspect-[3/4] rounded-lg md:rounded-2xl overflow-hidden mt-3 md:mt-6 mb-2 md:mb-5 relative shadow-inner">
                    <img src="<?php echo esc_url($cover); ?>" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                    <!-- Decoration tag -->
                    <?php if($rank == 1): ?>
                    <div class="absolute font-headline bottom-0 w-full bg-gradient-to-t from-black/80 to-transparent py-1 md:py-4 md:pt-10 text-center text-white font-black tracking-widest text-[8px] md:text-sm uppercase">Cực Phẩm</div>
                    <?php endif; ?>
                </div>

                <!-- Info -->
                <div class="flex flex-col flex-grow w-full text-center mt-auto justify-end">
                    <h3 class="font-headline font-bold text-gray-900 text-[10px] md:text-[17px] leading-tight md:leading-snug line-clamp-2 md:mb-2 group-hover:text-blue-600 transition-colors"><?php echo get_the_title($post->ID); ?></h3>
                    <p class="hidden md:flex text-xs font-semibold text-outline mb-4 justify-center items-center gap-1"><span class="material-symbols-outlined text-[14px]">edit</span> <?php echo esc_html($author); ?></p>
                    
                    <!-- Views metric -->
                    <div class="mt-auto hidden md:inline-flex items-center justify-center gap-1.5 <?php echo $rank==1 ? 'bg-blue-600-container text-on-primary-container':'bg-surface-container-high text-gray-500'; ?> px-4 py-2 rounded-xl font-bold text-sm w-full">
                        <span class="material-symbols-outlined text-[16px]">local_fire_department</span> <?php echo number_format($views); ?> Lượt xem
                    </div>
                </div>
            </div>
        </div>
        <?php endforeach; wp_reset_postdata(); ?>
    </div>


    <!-- LIST VIEW RANK 4 TO END -->
    <?php if (count($posts) > 3): ?>
    <div class="bg-white rounded-3xl p-2 md:p-6 shadow-sm border border-gray-200">
        
        <!-- List Header -->
        <div class="hidden md:flex items-center px-6 py-4 border-b border-surface-variant/50 text-xs font-bold text-outline uppercase tracking-wider mb-2">
            <div class="w-16 text-center">Hạng</div>
            <div class="w-20">Ảnh bìa</div>
            <div class="flex-grow">Tên Tác Phẩm</div>
            <div class="w-48 text-right">Tương tác</div>
        </div>

        <div class="flex flex-col gap-2">
            <?php 
            $list_posts = array_slice($posts, 3);
            foreach ($list_posts as $idx => $post) :
                $rank = $idx + 4;
                setup_postdata($post);
                $views = (int)get_post_meta($post->ID, '_views', true);
                $formatted_views = $views > 1000 ? round($views/1000, 1) . 'K' : $views;
                $author = get_post_meta($post->ID, 'truyen_tacgia', true);
                if(!$author) $author = 'Bạch Lão Đại';
                $cover = has_post_thumbnail($post->ID) ? get_the_post_thumbnail_url($post->ID, 'thumbnail') : 'https://placehold.co/100x150?text=Cover';
                $terms = get_the_terms($post->ID, 'the_loai');
                $term_name = $terms && !is_wp_error($terms) ? $terms[0]->name : 'Thể loại';
                $chaps = wp_count_posts('chuong')->publish;
            ?>
            
            <a href="<?php echo get_permalink($post->ID); ?>" class="flex items-center gap-3 md:gap-6 p-3 md:px-6 md:py-4 rounded-2xl hover:bg-gray-100est border border-transparent hover:border-blue-600/20 hover:shadow-[0_4px_12px_rgba(0,96,169,0.05)] transition-all group">
                
                <!-- Rank Number -->
                <div class="w-8 md:w-16 flex-shrink-0 text-center font-headline font-black text-2xl md:text-3xl text-gray-400 group-hover:text-blue-600 transition-colors">
                    <?php echo $rank; ?>
                </div>

                <!-- Cover -->
                <div class="w-12 h-16 md:w-16 md:h-20 flex-shrink-0 rounded-lg overflow-hidden shadow-inner hidden sm:block">
                    <img src="<?php echo esc_url($cover); ?>" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                </div>

                <!-- Main Info -->
                <div class="flex-grow min-w-0">
                    <h3 class="font-headline font-bold text-gray-900 text-[15px] md:text-[17px] mb-1 line-clamp-1 group-hover:text-blue-600 transition-colors"><?php echo get_the_title($post->ID); ?></h3>
                    <div class="flex flex-wrap items-center gap-x-3 gap-y-1 text-[11px] md:text-xs text-gray-500 font-medium">
                        <span class="flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">edit</span> <?php echo esc_html($author); ?></span>
                        <span class="w-1 h-1 bg-outline-variant rounded-full hidden sm:block"></span>
                        <span class="text-tertiary hidden sm:block"><?php echo esc_html($term_name); ?></span>
                        <span class="w-1 h-1 bg-outline-variant rounded-full hidden sm:block"></span>
                        <span class="text-secondary"><?php echo number_format($chaps); ?> Chương</span>
                    </div>
                </div>

                <!-- Stats Right -->
                <div class="w-auto md:w-48 flex-shrink-0 text-right">
                    <div class="inline-flex items-center gap-1 bg-surface-container-high px-3 py-1.5 rounded-full text-blue-600 font-bold text-xs md:text-sm shadow-sm group-hover:bg-blue-600-container transition-colors">
                        <span class="material-symbols-outlined text-[14px]">visibility</span> 
                        <span class="hidden sm:inline"><?php echo number_format($views); ?></span>
                        <span class="sm:hidden"><?php echo $formatted_views; ?></span>
                    </div>
                </div>
            </a>
            
            <?php endforeach; wp_reset_postdata(); ?>
        </div>
    </div>
    <?php endif; ?>

    <?php else: ?>
    
    <div class="bg-gray-100 rounded-3xl p-16 text-center border border-gray-200 mt-8">
        <div class="w-24 h-24 mx-auto bg-surface-container rounded-full flex items-center justify-center mb-6">
            <span class="material-symbols-outlined text-4xl text-outline">snooze</span>
        </div>
        <h3 class="font-headline text-2xl font-bold text-gray-900 mb-2">Chưa có dữ liệu</h3>
        <p class="text-gray-500">Không tìm thấy truyện nào thỏa mãn mốc giới hạn thời gian này. Vui lòng chọn hiển thị Tất cả.</p>
    </div>

    <?php endif; ?>

    <!-- Leaderboard Empty State Fallback handled earlier -->
</main>

<script>
// Pjax Smooth Filtering for BXH (Leaderboard)
document.addEventListener('DOMContentLoaded', function() {
    const mainContainer = document.querySelector('main');
    
    document.body.addEventListener('click', function(e) {
        const link = e.target.closest('a[href*="?time="]');
        if (!link) return; // Not a filter link
        
        e.preventDefault();
        const url = link.getAttribute('href');
        
        // Add loading state
        mainContainer.style.opacity = '0.4';
        mainContainer.style.transition = 'opacity 0.25s ease';
        mainContainer.style.pointerEvents = 'none';
        
        // Update URL
        window.history.pushState({path: url}, '', url);
        
        // Fetch new data smoothly
        fetch(url)
            .then(res => res.text())
            .then(html => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const newMain = doc.querySelector('main');
                
                if (newMain) {
                    mainContainer.innerHTML = newMain.innerHTML;
                }
                
                mainContainer.style.opacity = '1';
                mainContainer.style.pointerEvents = 'auto';
            })
            .catch(err => {
                window.location.href = url; // Fallback smoothly
            });
    });
    
    // Support back button history navigation smoothly
    window.addEventListener('popstate', function(e) {
        window.location.reload();
    });
});
</script>

<?php get_footer(); ?>
