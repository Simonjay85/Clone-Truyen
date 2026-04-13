<?php
/*
Template Name: Trang Tài Khoản
*/

if (!is_user_logged_in()) {
    auth_redirect();
    exit;
}

get_header();

$current_user = wp_get_current_user();
$user_id = $current_user->ID;
$user_name = $current_user->display_name;
$user_avatar = get_avatar_url($user_id, ['size' => 256]);
if (!$user_avatar) {
    $user_avatar = 'https://lh3.googleusercontent.com/aida-public/AB6AXuCuek6IKokOO6me_wvQfZvLxhfs_erI7QNl1PPxXzr6swLR4HimHULSknbnkM1pj1IlW4Jz614F0kXZXWO0WW_2hbMlt3TPijstsv62KtJPqwJA4H1W8i4eMXSjSTX9s5sJi8E-1bKSQ3QdWMfH_esWLMx5AN2Fkl6sXP8hJIO11DcKnD_05aApcI5hhmqGXtmVe1XJJItJqfncE4HK3DC_WksZqZfMHvayBy16TVjTl-YahcqpflWZn48VYmqyVItm0goNwCxzZaY';
}

$user_desc = get_the_author_meta('description', $user_id);
if (empty($user_desc)) {
    $user_desc = 'Người yêu thích những câu chuyện kỳ ảo và lãng mạn. Đang khám phá thế giới của những trang truyện mỗi ngày.';
}

$points = (int)get_user_meta($user_id, '_author_points', true);
$posts_count = count_user_posts($user_id, 'truyen');
$rank_badge = $points >= 500 ? 'Dịch Giả' : 'Độc Giả Uy Tín';

// Check if WP logout link needed
$logout_url = wp_logout_url(home_url());
?>

<main class="pt-20 pb-16 w-full max-w-[95%] 2xl:max-w-[1600px] mx-auto px-6 w-full">
    <!-- User Profile Header -->
    <header class="mb-12 relative overflow-hidden rounded-[2rem] bg-surface-container-low p-8 md:p-12 border border-surface-container-highest">
        <div class="absolute top-0 right-0 w-1/3 h-full bg-gradient-to-l from-primary/5 to-transparent pointer-events-none"></div>
        <div class="relative z-10 flex flex-col md:flex-row items-center md:items-end gap-8">
            <div class="relative group">
                <div class="w-32 h-32 md:w-40 md:h-40 rounded-[2.5rem] overflow-hidden custom-shadow border-4 border-surface-container-lowest">
                    <img class="w-full h-full object-cover" src="<?php echo esc_url($user_avatar); ?>" />
                </div>
                <a href="<?php echo admin_url('profile.php'); ?>" class="absolute bottom-2 right-2 w-10 h-10 bg-primary text-white rounded-full flex items-center justify-center shadow-lg active:scale-90 transition-transform">
                    <span class="material-symbols-outlined text-sm">edit</span>
                </a>
            </div>
            
            <div class="flex-1 text-center md:text-left">
                <div class="flex flex-col md:flex-row md:items-center justify-between">
                    <div class="flex flex-col md:flex-row md:items-center gap-2 md:gap-4 mb-2 justify-center md:justify-start">
                        <h1 class="text-3xl md:text-4xl font-headline font-extrabold tracking-tight text-on-surface"><?php echo esc_html($user_name); ?></h1>
                        <span class="inline-flex items-center px-3 py-1 bg-primary-container/10 text-primary text-xs font-bold rounded-full border border-primary/20 uppercase tracking-wider">
                            <?php echo esc_html($rank_badge); ?>
                        </span>
                    </div>
                    
                    <a href="<?php echo esc_url($logout_url); ?>" class="mt-4 md:mt-0 text-red-500 font-bold hover:bg-red-50 px-4 py-2 rounded-xl transition-colors text-sm flex items-center gap-2 mx-auto md:mx-0 w-fit">
                         <span class="material-symbols-outlined">logout</span> Đăng xuất
                    </a>
                </div>
                
                <p class="text-on-surface-variant max-w-lg mb-6 leading-relaxed mx-auto md:mx-0"><?php echo esc_html($user_desc); ?></p>
                
                <div class="flex flex-wrap justify-center md:justify-start gap-4">
                    <div class="bg-surface-container-lowest px-6 py-3 rounded-2xl shadow-[0px_4px_16px_rgba(0,0,0,0.03)] border border-outline-variant/20 group hover:border-primary/50 transition-colors">
                        <span class="block text-3xl font-black text-primary font-headline text-shadow-blue"><?php echo number_format($points); ?></span>
                        <span class="text-[10px] font-bold text-outline uppercase tracking-tight flex items-center gap-1"><span class="material-symbols-outlined text-[12px]">monetization_on</span> Điểm Hoa Hồng</span>
                    </div>
                    <div class="bg-surface-container-lowest px-6 py-3 rounded-2xl shadow-[0px_4px_16px_rgba(0,0,0,0.03)] border border-outline-variant/20">
                        <span class="block text-2xl font-bold text-on-surface font-headline"><?php echo number_format($posts_count); ?></span>
                        <span class="text-[10px] font-bold text-outline uppercase tracking-tight flex items-center gap-1"><span class="material-symbols-outlined text-[12px]">edit_document</span> Truyện Đã Đăng</span>
                    </div>
                    <div class="bg-surface-container-lowest px-6 py-3 rounded-2xl shadow-[0px_4px_16px_rgba(0,0,0,0.03)] border border-outline-variant/20">
                        <span class="block text-2xl font-bold text-on-surface font-headline">0</span>
                        <span class="text-[10px] font-bold text-outline uppercase tracking-tight flex items-center gap-1"><span class="material-symbols-outlined text-[12px]">bookmark</span> Đánh dấu</span>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- Main Content Bento Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        <!-- Left Column: Reading Stats & Bookmarks (4/12) -->
        <div class="lg:col-span-4 space-y-8">
            <!-- Bookmarks Quick Access (MOCKUP) -->
            <section class="bg-surface-container-lowest p-6 rounded-[1.5rem] shadow-[0px_4px_24px_rgba(0,0,0,0.02)] border border-outline-variant/20">
                <div class="flex justify-between items-center mb-6">
                    <h2 class="text-lg font-headline font-bold flex items-center gap-2">
                        <span class="material-symbols-outlined text-primary">bookmark</span>
                        Đã đánh dấu
                    </h2>
                    <a class="text-sm font-semibold text-primary hover:underline" href="#">Tất cả</a>
                </div>
                <div class="space-y-4">
                    <div class="flex items-center gap-4 group cursor-pointer">
                        <div class="w-14 h-18 bg-surface-container-high rounded-lg overflow-hidden shrink-0">
                            <img class="w-full h-full object-cover transition-transform group-hover:scale-110" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAy8U5dAYdn_m1a9Lel41LrjE7tM7qx_H39_LdSgp1YPo_gV8q_ZSd21dPGBmxuo3nB75hhg8n0mnt-rS3CYwvPLyit7pOU8gEi3eC9yuMQupUu-N5Jlzdk6RuavxWdB4aU2nxk0EXQT9bdptWxXtcc9nLLkfWCxQGek7zLkV5TC2xzEsMi3T_T5HAmxDh6GB-8mCV9dSs5YSrW7pTsNMKdFrQ28CheCAqKTYAu-MCNFYEngu79PP--EXERFg4boJOlEDGkmv3a8gA"/>
                        </div>
                        <div class="overflow-hidden">
                            <h3 class="font-bold text-sm truncate group-hover:text-primary transition-colors font-headline">Thiên Thần Sa Ngã</h3>
                            <p class="text-xs text-on-surface-variant mt-1 italic">Chương 42 • 2 ngày trước</p>
                        </div>
                    </div>
                    <div class="flex items-center gap-4 group cursor-pointer">
                        <div class="w-14 h-18 bg-surface-container-high rounded-lg overflow-hidden shrink-0">
                            <img class="w-full h-full object-cover transition-transform group-hover:scale-110" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCnXagJO3BRx8pJJ2ys1O3yNaBSElUOpzp96XnngqorKT3tprwlCLMWHDVocyIIX6ATha0mTbR3Ja0eAjBMdDh3euh_m9j1DAaG6Z0Hk6zpG4glzDSccV0wWiPZQg6Ebo1Au9EbatdRfJQfU1gp7Zxuotw97hKe6AEZ5W-BYrVHrKTU6yHpPo0aUmGvoa4X0UcQNnEldDDIrJfzZIzeiJ3yKnmS5GQoquR9LuqB7iEnAqGY2gCg0zrG9r8_quEstG-LBCfDvKx-wOA"/>
                        </div>
                        <div class="overflow-hidden">
                            <h3 class="font-bold text-sm truncate group-hover:text-primary transition-colors font-headline">Lạc Lối Giữa Rừng</h3>
                            <p class="text-xs text-on-surface-variant mt-1 italic">Chương 156 • Vừa xong</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Activity Chart (MOCKUP) -->
            <section class="bg-surface-container-low p-6 rounded-[1.5rem] border border-outline-variant/20">
                <h2 class="text-lg font-headline font-bold mb-6 flex items-center gap-2">
                    <span class="material-symbols-outlined text-primary">analytics</span>
                    Hoạt động tuần này
                </h2>
                <div class="flex items-end justify-between h-32 gap-2 px-2">
                    <div class="w-full bg-primary/20 rounded-t-lg h-[40%] hover:bg-primary transition-all cursor-help" title="T2"></div>
                    <div class="w-full bg-primary/20 rounded-t-lg h-[65%] hover:bg-primary transition-all cursor-help" title="T3"></div>
                    <div class="w-full bg-primary/20 rounded-t-lg h-[30%] hover:bg-primary transition-all cursor-help" title="T4"></div>
                    <div class="w-full bg-primary rounded-t-lg h-[90%] transition-all cursor-help" title="Hôm nay"></div>
                    <div class="w-full bg-surface-container-highest rounded-t-lg h-[15%] transition-all"></div>
                    <div class="w-full bg-surface-container-highest rounded-t-lg h-[10%] transition-all"></div>
                    <div class="w-full bg-surface-container-highest rounded-t-lg h-[5%] transition-all"></div>
                </div>
                <div class="flex justify-between mt-4 text-[10px] font-bold text-outline uppercase tracking-widest px-1">
                    <span>T2</span><span>T3</span><span>T4</span><span class="text-primary">Nay</span><span>T7</span><span>CN</span>
                </div>
            </section>
        </div>

        <!-- Right Column: Recent Work or History (8/12) -->
        <div class="lg:col-span-8 space-y-8">
            <!-- Tabs -->
            <div class="flex items-center gap-8 border-b border-outline-variant mb-4 px-2">
                <button class="pb-4 text-primary border-b-2 border-primary font-headline font-bold flex items-center gap-2">
                    <span class="material-symbols-outlined text-[20px]">auto_stories</span>
                    Truyện của tôi 
                </button>
            </div>

            <!-- Grid of Items (WP_Query for Author's real posts) -->
            <div class="grid grid-cols-2 md:grid-cols-3 gap-6">
                <?php
                if ($posts_count > 0) {
                    $author_query = new WP_Query([
                        'post_type' => 'truyen',
                        'author'    => $user_id,
                        'posts_per_page' => 6
                    ]);
                    
                    if ($author_query->have_posts()) {
                        while ($author_query->have_posts()) {
                            $author_query->the_post();
                            $cover = get_the_post_thumbnail_url(get_the_ID(), 'medium');
                            if(!$cover) $cover = "https://lh3.googleusercontent.com/aida-public/AB6AXuCdLCpBjO7QBzV11EIZu-uGhgB7RyYD9R3SKpBugV-7MEdJ2TuewiUw7yuVcAhiQU9PfXMoCB2fSaE65hcs5Zphzxl3VAd5vux2kmZIYl-KC_dV72r8LTdgZ8ppmWP7PJww2xOEO1J3fzc7yTzUb0iMm-UlEWaHZCGQwChwTHBRum5fsLWarozox93y0maKV9dVhNgFzkjmMBJkuvKBhmTnEYxiSh0ZxDKV5Sasq050yyDFNsiQUvAdXc6aMa2ZAnYe8YvWs4eGAQI";
                            $views = (int)get_post_meta(get_the_ID(), '_views', true);
                            ?>
                            <div class="flex flex-col group cursor-pointer" onclick="window.location.href='<?php the_permalink(); ?>'">
                                <div class="relative aspect-[3/4] rounded-2xl overflow-hidden bg-surface-container-high shadow-[0px_12px_24px_rgba(0,0,0,0.06)] mb-4 border border-outline-variant/10 group-hover:border-primary/30 transition-all">
                                    <img class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" src="<?php echo esc_url($cover); ?>" />
                                    <!-- Edit Badge -->
                                    <div class="absolute top-3 right-3 opacity-0 group-hover:opacity-100 transition-opacity">
                                        <span class="bg-primary text-white text-[10px] font-black px-2 py-1 rounded-md uppercase tracking-wider shadow-lg"><span class="material-symbols-outlined text-[10px]">edit</span></span>
                                    </div>
                                    <div class="absolute bottom-0 left-0 w-full p-4 bg-gradient-to-t from-black/80 to-transparent translate-y-full group-hover:translate-y-0 transition-transform">
                                        <button class="w-full py-2 bg-white/20 backdrop-blur-md text-white text-xs font-bold rounded-lg border border-white/30 hover:bg-primary/80 transition-colors">Quản lý</button>
                                    </div>
                                </div>
                                <h4 class="font-headline font-bold text-on-surface leading-tight group-hover:text-primary transition-colors line-clamp-2" title="<?php the_title_attribute(); ?>"><?php the_title(); ?></h4>
                                <div class="flex items-center justify-between gap-2 mt-2">
                                    <span class="text-xs font-medium text-on-surface-variant flex items-center gap-1"><span class="material-symbols-outlined text-[12px]">visibility</span> Lượt xem</span>
                                    <span class="text-xs font-bold text-primary"><?php echo number_format($views); ?></span>
                                </div>
                            </div>
                            <?php
                        }
                        wp_reset_postdata();
                    }
                } else {
                    echo '
                    <!-- Empty State Add New Card -->
                    <div class="flex flex-col group col-span-3">
                        <a href="'.admin_url('post-new.php?post_type=truyen').'" class="block relative aspect-[21/9] rounded-2xl border-2 border-dashed border-outline-variant flex flex-col items-center justify-center gap-3 hover:border-primary hover:bg-primary/5 transition-all cursor-pointer mb-4">
                            <span class="material-symbols-outlined text-4xl text-outline group-hover:text-primary transition-colors">add_circle</span>
                            <span class="text-sm font-bold text-outline group-hover:text-primary transition-colors">Đăng truyện mới</span>
                        </a>
                    </div>';
                }
                ?>
            </div>
            
            <?php if ($posts_count > 6): ?>
            <div class="flex justify-center pt-8">
                <a href="<?php echo admin_url('edit.php?post_type=truyen'); ?>" class="px-8 py-3 bg-surface-container-low text-primary border border-primary/20 font-bold rounded-full hover:bg-primary hover:text-white transition-all scale-95 active:scale-90 shadow-sm">Mở Kho Quản Lý Toàn Bộ</a>
            </div>
            <?php endif; ?>
        </div>
    </div>
</main>

<?php get_footer(); ?>
