<?php global $tehi_tailwind_page;
$tehi_tailwind_page = true;
get_header(); ?>

<main class="flex-grow w-full bg-white dark:bg-black pb-20">
    <?php if(have_posts()): while(have_posts()): the_post(); ?>
    
    <!-- Hero Header -->
    <div class="relative w-full h-auto flex flex-col items-center justify-center overflow-hidden pt-20 pb-4">
        <?php if(has_post_thumbnail()): ?>
            <div class="absolute inset-0 w-full h-full pointer-events-none">
                <img src="<?php echo get_the_post_thumbnail_url(get_the_ID(), 'full'); ?>" class="w-full h-full object-cover blur-xl opacity-40 dark:opacity-20 scale-110" alt="Cover">
                <div class="absolute inset-0 bg-gradient-to-t from-surface-container via-surface-container/60 to-transparent dark:from-black dark:via-black/70"></div>
            </div>
        <?php else: ?>
            <div class="absolute inset-0 bg-gradient-to-br from-blue-600-container to-purple-100 dark:from-indigo-950 dark:to-slate-900 opacity-80 pointer-events-none"></div>
        <?php endif; ?>
        
        <div class="relative z-10 text-center px-4 max-w-4xl mx-auto">
            <div class="inline-flex items-center justify-center gap-2 px-4 py-1.5 rounded-full bg-white/30 dark:bg-black/40 backdrop-blur-md border border-white/20 dark:border-white/10 text-sm font-bold tracking-wide mb-6 text-gray-900 uppercase shadow-sm">
                <span class="material-symbols-outlined text-[18px]">article</span> Chuyên mục Hệ thống
            </div>
            <h1 class="text-4xl md:text-5xl lg:text-5xl font-black text-gray-900 mb-4 !leading-tight text-balance drop-shadow-sm">
                <?php the_title(); ?>
            </h1>
            <p class="text-gray-500 font-medium text-lg flex items-center justify-center gap-2 pb-16">
                <span class="material-symbols-outlined text-sm">update</span> Cập nhật lần cuối: <?php echo get_the_modified_date('d/m/Y'); ?>
            </p>
        </div>
    </div>

    <!-- Content Area -->
    <div class="w-full max-w-[95%] 2xl:max-w-[1600px] mx-auto px-8 sm:px-10 relative z-20 -mt-10">
        <div class="bg-[#F8F9FA] dark:bg-[#111315] rounded-[2rem] p-8 sm:p-12 md:p-16 shadow-2xl w-full border border-slate-200/60 dark:border-white/5 ring-1 ring-black/5 dark:ring-white/5">
            <div class="prose prose-slate dark:prose-invert max-w-4xl mx-auto text-justify prose-p:text-justify prose-headings:font-extrabold md:prose-h2:text-3xl md:prose-h3:text-2xl prose-h2:text-slate-800 prose-h2:dark:text-white prose-h2:mt-10 prose-h3:text-slate-700 prose-h3:dark:text-slate-200 prose-h3:mt-8 prose-a:text-blue-600 prose-img:rounded-2xl text-[17px] leading-[1.8] font-medium prose-p:text-slate-700 dark:prose-p:text-slate-300 prose-li:text-slate-700 dark:prose-li:text-slate-300">
                <?php 
                    $post_slug = get_post_field( 'post_name', get_post() );
                    if($post_slug === 'lien-he-quang-cao' || $post_slug === 'lien-he'):
                ?>
                    <!-- Custom Bắt Mắt Liên Hệ Quảng Cáo -->
                    <div class="not-prose grid grid-cols-1 md:grid-cols-2 gap-8 items-start mt-[-20px]">
                        <div class="bg-gradient-to-br from-blue-600 to-indigo-700 p-8 rounded-3xl text-white shadow-xl shadow-blue-600/20">
                            <span class="material-symbols-outlined text-5xl mb-6 opacity-90">campaign</span>
                            <h2 class="text-3xl font-black mb-4 tracking-tight">Hợp tác & Quảng cáo</h2>
                            <p class="text-blue-100 font-medium mb-8 leading-relaxed">Đưa thương hiệu của bạn tiếp cận hàng triệu độc giả trung thành mỗi tháng trên hệ thống <strong>Đọc Tiểu Thuyết</strong>. Chúng tôi mang đến những giải pháp hiển thị độ chuyển đổi cao nhất.</p>
                            
                            <div class="space-y-6">
                                <div class="flex items-center gap-4 bg-white/10 p-4 rounded-2xl border border-white/20">
                                    <div class="w-12 h-12 bg-white/20 rounded-full flex items-center justify-center shrink-0 text-white"><span class="material-symbols-outlined">mail</span></div>
                                    <div>
                                        <div class="text-blue-200 text-xs font-bold uppercase tracking-wider mb-1">Email liên hệ</div>
                                        <div class="font-bold text-lg">ads@doctieuthuyet.com</div>
                                    </div>
                                </div>
                                <div class="flex items-center gap-4 bg-white/10 p-4 rounded-2xl border border-white/20">
                                    <div class="w-12 h-12 bg-white/20 rounded-full flex items-center justify-center shrink-0 text-white"><span class="material-symbols-outlined">support_agent</span></div>
                                    <div>
                                        <div class="text-blue-200 text-xs font-bold uppercase tracking-wider mb-1">Telegram / Zalo</div>
                                        <div class="font-bold text-lg">@DTT_Support_Ads</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="bg-white p-8 rounded-3xl border border-gray-100 shadow-[0_8px_30px_rgb(0,0,0,0.04)]">
                            <h3 class="text-xl font-black text-gray-800 mb-6 font-headline">Gửi thông điệp ngay</h3>
                            <form class="space-y-5" onsubmit="event.preventDefault(); alert('Cảm ơn bạn! Yêu cầu liên hệ đã được gửi đến bộ phận quảng cáo.');">
                                <div>
                                    <label class="block text-sm font-bold text-gray-700 mb-2">Tên công ty / Cá nhân *</label>
                                    <input type="text" required class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 outline-none focus:border-blue-600 focus:bg-white transition-all text-gray-800 font-medium" placeholder="VD: Công ty TNHH Truyền Thông ACB">
                                </div>
                                <div>
                                    <label class="block text-sm font-bold text-gray-700 mb-2">Số điện thoại / Zalo *</label>
                                    <input type="text" required class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 outline-none focus:border-blue-600 focus:bg-white transition-all text-gray-800 font-medium" placeholder="Số điện thoại liên lạc">
                                </div>
                                <div>
                                    <label class="block text-sm font-bold text-gray-700 mb-2">Nội dung hợp tác muốn triển khai *</label>
                                    <textarea required class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 outline-none focus:border-blue-600 focus:bg-white transition-all text-gray-800 min-h-[120px] font-medium" placeholder="VD: Đặt banner trang chủ, thông cáo báo chí, pop-up..."></textarea>
                                </div>
                                <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3.5 rounded-xl transition-colors shadow-lg shadow-blue-600/20 active:translate-y-0.5 mt-2 flex items-center justify-center gap-2">
                                    <span>Gửi Yêu Cầu Hợp Tác</span> <span class="material-symbols-outlined text-[20px]">send</span>
                                </button>
                            </form>
                        </div>
                    </div>
                <!-- End Custom -->
                <?php else:
                    the_content(); 
                endif; 
                ?>
            </div>
        </div>
    </div>
    
    <?php endwhile; endif; ?>
</main>

<?php get_footer(); ?>
