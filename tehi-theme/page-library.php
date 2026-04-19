<?php
/*
Template Name: Tủ Truyện
*/
global $tehi_tailwind_page;
$tehi_tailwind_page = true;
get_header();

// Mock User checking
$is_logged_in = is_user_logged_in();
// If we had bookmarks meta, we'd query it. For now, fetch latest 10.
$library_query = new WP_Query([
    'post_type' => 'truyen',
    'posts_per_page' => 10,
    'orderby' => 'rand' // Mock library
]);

// Mock Stats
$chaps_read = 142;
$following = 12;
$rank_name = "Độc Giả Uyên Bác";
?>

<main class="flex-grow pt-20 pb-16 px-6 w-full max-w-[95%] 2xl:max-w-[1600px] mx-auto w-full min-h-screen">
    <!-- Header Section -->
    <header class="mb-10">
        <div class="flex flex-col md:flex-row md:items-end justify-between gap-6">
            <div>
                <h1 class="text-4xl font-extrabold tracking-tight font-headline text-gray-900 mb-2">Tủ Truyện</h1>
                <p class="text-gray-500 max-w-prose">Quản lý kho tàng tri thức và những câu chuyện yêu thích của bạn trong một không gian tối giản và tinh tế.</p>
            </div>
            <div class="flex gap-2 bg-gray-50 p-1.5 rounded-xl border border-gray-200 shadow-sm flex-wrap">
                <button class="px-5 py-2.5 rounded-lg text-sm font-bold font-headline text-blue-600 bg-gray-50est shadow-sm transition-all focus:outline-none">Đang theo dõi</button>
                <button class="px-5 py-2.5 rounded-lg text-sm font-medium font-headline text-slate-500 hover:text-blue-600 hover:bg-gray-50est/50 transition-all focus:outline-none opacity-50 cursor-not-allowed" title="Sắp ra mắt">Lịch sử</button>
                <button class="px-5 py-2.5 rounded-lg text-sm font-medium font-headline text-slate-500 hover:text-blue-600 hover:bg-gray-50est/50 transition-all focus:outline-none opacity-50 cursor-not-allowed" title="Sắp ra mắt">Yêu thích</button>
            </div>
        </div>
    </header>

    <?php if(!$is_logged_in): ?>
        <div class="bg-blue-600/5 border border-blue-600/20 rounded-3xl p-12 text-center mb-12">
            <span class="material-symbols-outlined text-6xl text-blue-600 mb-4 opacity-80">account_circle</span>
            <h2 class="font-headline text-2xl font-bold mb-2">Bạn chưa đăng nhập</h2>
            <p class="text-gray-500 mb-6 max-w-md mx-auto">Hãy đăng nhập hoặc tạo tài khoản để hệ thống có thể lưu lại những bộ truyện yêu thích và tiến độ đọc của bạn xuyên suốt các thiết bị.</p>
            <button class="bg-blue-600 text-white font-bold px-8 py-3 rounded-full shadow-lg hover:-translate-y-1 transition-transform" onclick="alert('Module Đăng Nhập Đang Tối Ưu')">Đăng Nhập Ngay</button>
        </div>
    <?php endif; ?>

    <!-- Bento Style Feature Section (Displayed to show UI capabilities even if guest) -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-12 <?php if(!$is_logged_in) echo 'opacity-50 pointer-events-none grayscale-[0.3] blur-[1px]'; ?>">
        <!-- Featured Reading -->
        <?php 
        $rp = get_posts(['post_type' => 'truyen', 'posts_per_page' => 1, 'orderby' => 'rand']);
        if($rp): 
            $curr_feature = $rp[0];
            $cf_cover = has_post_thumbnail($curr_feature->ID) ? get_the_post_thumbnail_url($curr_feature->ID, 'large') : 'https://placehold.co/400x600';
            $cf_chaps = wp_count_posts('chuong')->publish;
        ?>
        <div class="md:col-span-3 bg-gray-50 rounded-3xl p-6 md:p-8 relative overflow-hidden flex flex-col sm:flex-row gap-8 items-center border border-gray-200 shadow-sm">
            <div class="relative z-10 w-48 shrink-0 aspect-[3/4] rounded-2xl overflow-hidden shadow-2xl rotate-[-2deg] hover:rotate-0 transition-transform duration-500 border-4 border-white/50">
                <img class="w-full h-full object-cover" src="<?php echo esc_url($cf_cover); ?>"/>
            </div>
            <div class="relative z-10 flex-1 w-full">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-blue-600-container/30 text-blue-600 text-[10px] font-black tracking-widest uppercase mb-4 shadow-sm border border-blue-600-container">
                    <span class="material-symbols-outlined text-[14px]" style="font-variation-settings: 'FILL' 1;">play_circle</span> ĐANG ĐỌC
                </span>
                <h2 class="text-2xl md:text-3xl font-bold font-headline mb-3 text-gray-900 line-clamp-2"><?php echo esc_html($curr_feature->post_title); ?></h2>
                <p class="text-gray-500 mb-6 line-clamp-2 text-sm leading-relaxed opacity-80">Tiếp tục cuộc hành trình dang dở của bạn...</p>
                <div class="space-y-4 max-w-md">
                    <div class="flex items-center justify-between text-[11px] font-bold mb-1 uppercase tracking-wider text-gray-400">
                        <span>Tiến độ: Chương 3 / <?php echo $cf_chaps; ?></span>
                        <span class="text-blue-600">15%</span>
                    </div>
                    <div class="h-2 w-full bg-gray-100 rounded-full overflow-hidden shadow-inner">
                        <div class="h-full bg-gradient-to-r from-blue-600 to-blue-600-container rounded-full w-[15%]"></div>
                    </div>
                    <button class="mt-4 flex items-center justify-center gap-2 bg-blue-600 text-white px-8 py-3.5 rounded-full font-bold shadow-lg shadow-blue-600/20 hover:shadow-blue-600/40 hover:-translate-y-0.5 active:translate-y-0 transition-all text-sm w-full md:w-auto" onclick="window.location.href='<?php echo get_permalink($curr_feature->ID); ?>'">
                        Đọc tiếp chương 3 <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
                    </button>
                </div>
            </div>
            <!-- Abstract Background Elements -->
            <div class="absolute top-[-10%] right-[-5%] w-64 h-64 bg-blue-600/5 rounded-full blur-3xl pointer-events-none"></div>
            <div class="absolute bottom-[-10%] left-[-5%] w-48 h-48 bg-indigo-100/20 rounded-full blur-3xl pointer-events-none"></div>
        </div>
        <?php endif; ?>

        <!-- Stats Card -->
        <div class="md:col-span-1 bg-gradient-to-br from-slate-900 to-slate-800 rounded-3xl p-8 text-white flex flex-col justify-between shadow-xl relative overflow-hidden group">
            <div class="absolute top-0 right-0 w-32 h-32 bg-white/5 rounded-full blur-2xl group-hover:scale-150 transition-transform duration-700"></div>
            <div class="relative z-10">
                <h3 class="font-headline font-bold text-lg mb-8 text-slate-300 opacity-90">Thống kê của bạn</h3>
                <div class="space-y-8">
                    <div>
                        <div class="text-4xl font-extrabold font-headline tracking-tighter"><?php echo $chaps_read; ?></div>
                        <div class="text-slate-400 text-xs font-medium uppercase tracking-wider mt-1 opacity-80">Chương đã đọc tuần này</div>
                    </div>
                    <div>
                        <div class="text-4xl font-extrabold font-headline tracking-tighter text-blue-600-container"><?php echo $following; ?></div>
                        <div class="text-slate-400 text-xs font-medium uppercase tracking-wider mt-1 opacity-80">Bộ truyện đang theo dõi</div>
                    </div>
                </div>
            </div>
            
            <div class="pt-6 border-t border-white/10 mt-8 relative z-10">
                <div class="flex items-center gap-4 bg-white/5 p-3 rounded-2xl">
                    <div class="w-12 h-12 rounded-full bg-gradient-to-br from-amber-400 to-amber-600 flex items-center justify-center shrink-0 shadow-lg border-2 border-slate-800">
                        <span class="material-symbols-outlined text-white" style="font-variation-settings: 'FILL' 1;">military_tech</span>
                    </div>
                    <div>
                        <div class="text-[10px] text-slate-400 font-bold uppercase tracking-widest mb-0.5">Hạng hiện tại</div>
                        <div class="font-bold text-sm text-amber-50"><?php echo esc_html($rank_name); ?></div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Section Title -->
    <div class="flex items-center justify-between mb-8 <?php if(!$is_logged_in) echo 'opacity-50 pointer-events-none'; ?>">
        <h3 class="text-2xl font-bold font-headline text-gray-900">Đang theo dõi</h3>
        <div class="flex items-center gap-2 bg-gray-50 p-1 rounded-lg border border-gray-200">
            <button class="p-2 rounded-md bg-gray-50est shadow-sm text-blue-600 transition-all focus:outline-none">
                <span class="material-symbols-outlined text-[20px]" style="font-variation-settings: 'FILL' 1;">grid_view</span>
            </button>
            <button class="p-2 rounded-md hover:bg-white-high text-gray-500 transition-all focus:outline-none opacity-50">
                <span class="material-symbols-outlined text-[20px]">view_list</span>
            </button>
        </div>
    </div>

    <!-- Story Grid -->
    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-x-6 gap-y-10 <?php if(!$is_logged_in) echo 'opacity-50 pointer-events-none grayscale-[0.5] blur-[2px]'; ?>">
        <?php 
        if ($library_query->have_posts()) :
            while ($library_query->have_posts()) : $library_query->the_post();
                $cover = has_post_thumbnail() ? get_the_post_thumbnail_url(get_the_ID(), 'large') : 'https://placehold.co/400x600?text=Cover';
                $chapters_arr = get_posts(['post_type' => 'chuong', 'meta_key' => '_truyen_id', 'meta_value' => get_the_ID(), 'posts_per_page' => -1, 'fields' => 'ids']); $chaps = count($chapters_arr);
                $prog = rand(5, 95); // mock reading progress %
        ?>
        <!-- Story Card -->
        <div class="group flex flex-col h-full bg-transparent">
            <div class="relative aspect-[3/4] rounded-2xl overflow-hidden mb-3 shadow-[0px_8px_24px_rgba(0,0,0,0.06)] group-hover:shadow-[0px_16px_40px_rgba(0,96,169,0.15)] transition-all duration-300 border border-gray-200 group-hover:-translate-y-1">
                <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" src="<?php echo esc_url($cover); ?>"/>
                
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
                    <button class="w-full py-2 bg-white text-blue-600 text-sm font-bold rounded-xl shadow-lg active:scale-95 transition-transform" onclick="window.location.href='<?php the_permalink(); ?>'">Đọc tiếp</button>
                </div>
                
                <!-- Random Badge -->
                <?php if($prog > 80): ?>
                    <div class="absolute top-2 right-2"><span class="bg-blue-600 text-white text-[9px] font-black px-2 py-1 rounded-md shadow-sm uppercase tracking-wider">FULL</span></div>
                <?php elseif($prog < 20): ?>
                    <div class="absolute top-2 right-2"><span class="bg-indigo-100 text-indigo-800 text-[9px] font-black px-2 py-1 rounded-md shadow-sm uppercase tracking-wider">NEW</span></div>
                <?php else: ?>
                    <div class="absolute top-2 right-2"><span class="bg-red-500 text-white text-[9px] font-black px-2 py-1 rounded-md shadow-sm uppercase tracking-wider">HOT</span></div>
                <?php endif; ?>
            </div>
            
            <div class="flex-grow flex flex-col px-1">
                <h4 class="font-bold font-headline text-[15px] text-gray-900 line-clamp-1 group-hover:text-blue-600 transition-colors leading-snug mb-2"><?php the_title(); ?></h4>
                <div class="flex items-center justify-between text-[11px] font-bold text-gray-400 uppercase tracking-wider mb-2 mt-auto">
                    <span>Đã đọc <?php echo round($prog/100 * $chaps); ?>/<?php echo $chaps; ?></span>
                    <span class="text-blue-600 bg-blue-600/5 px-1 rounded"><?php echo $prog; ?>%</span>
                </div>
                <div class="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden shadow-inner">
                    <div class="h-full bg-gradient-to-r from-blue-600 to-blue-600-container rounded-full" style="width: <?php echo $prog; ?>%"></div>
                </div>
            </div>
        </div>
        <?php 
            endwhile; 
            wp_reset_postdata();
        endif; 
        ?>
    </div>

</main>

<?php get_footer(); ?>
