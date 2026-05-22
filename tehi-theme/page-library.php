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
        <div class="bg-gradient-to-r from-blue-600/10 to-indigo-600/10 border border-blue-600/20 rounded-2xl p-6 text-left mb-10 flex flex-col md:flex-row items-center justify-between gap-4">
            <div class="flex items-center gap-4">
                <span class="material-symbols-outlined text-4xl text-blue-600 opacity-90 hidden sm:block">cloud_sync</span>
                <div>
                    <h3 class="font-headline text-lg font-bold text-gray-900 mb-1">Đồng bộ tủ truyện của bạn</h3>
                    <p class="text-gray-500 text-sm max-w-xl">Bạn đang xem tủ truyện dưới quyền Khách. Đăng nhập hoặc tạo tài khoản để đồng bộ danh sách theo dõi này trên mọi thiết bị di động, tablet hoặc laptop!</p>
                </div>
            </div>
            <button class="bg-blue-600 text-white font-bold text-sm px-6 py-3 rounded-full shadow-md hover:bg-blue-700 transition-colors shrink-0" onclick="alert('Tính năng đồng bộ tài khoản đang được tối ưu hóa!')">Đăng nhập ngay</button>
        </div>
    <?php endif; ?>

    <!-- Bento Style Feature Section (Displayed to show UI capabilities even if guest) -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-12">
        <!-- Featured Reading -->
        <?php 
        $rp = get_posts(['post_type' => 'truyen', 'posts_per_page' => 1, 'orderby' => 'rand']);
        if($rp): 
            $curr_feature = $rp[0];
            $cf_cover = has_post_thumbnail($curr_feature->ID) ? get_the_post_thumbnail_url($curr_feature->ID, 'large') : get_template_directory_uri() . '/img_data/images/no-image-cover-v5.png?v=5';
            $cf_chaps = wp_count_posts('chuong')->publish;
        ?>
        <div class="md:col-span-3 bg-gray-50 rounded-3xl p-6 md:p-8 relative overflow-hidden flex flex-col sm:flex-row gap-8 items-center border border-gray-200 shadow-sm">
            <div class="relative z-10 w-48 shrink-0 aspect-[4/3] rounded-2xl overflow-hidden shadow-2xl rotate-[-2deg] hover:rotate-0 transition-transform duration-500 border-4 border-white/50">
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
                        <div id="lib-following-count" class="text-4xl font-extrabold font-headline tracking-tighter text-blue-600-container">0</div>
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
    <div class="flex items-center justify-between mb-8">
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

    <!-- Empty State -->
    <div id="lib-empty-state" class="hidden text-center py-16 px-4 bg-gray-50 border border-gray-200 rounded-3xl mb-12 shadow-sm">
        <div class="w-20 h-20 bg-blue-50 text-blue-600 rounded-full flex items-center justify-center mx-auto mb-6 shadow-inner">
            <span class="material-symbols-outlined text-4xl">auto_stories</span>
        </div>
        <h3 class="font-headline text-2xl font-bold text-gray-900 mb-2">Tủ truyện của bạn đang trống</h3>
        <p class="text-gray-500 max-w-md mx-auto mb-8 text-sm leading-relaxed">Hãy khám phá hàng ngàn tiểu thuyết xuất sắc và bấm "Theo dõi" để lưu lại những câu chuyện yêu thích tại đây nhé!</p>
        <a href="/" class="inline-flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white font-bold px-8 py-3.5 rounded-full shadow-lg hover:-translate-y-0.5 transition-all text-sm">
            Khám phá ngay <span class="material-symbols-outlined text-[18px]">explore</span>
        </a>
    </div>

    <!-- Skeleton Screen Grid -->
    <div id="lib-skeleton-grid" class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-x-6 gap-y-10">
        <?php for($i = 0; $i < 4; $i++): ?>
        <div class="flex flex-col h-full bg-transparent animate-pulse">
            <div class="relative aspect-[4/3] rounded-2xl bg-gray-200 mb-3 border border-gray-200"></div>
            <div class="h-5 bg-gray-200 rounded-md w-3/4 mb-3"></div>
            <div class="flex justify-between items-center mb-3">
                <div class="h-3 bg-gray-200 rounded w-1/3"></div>
                <div class="h-4 bg-gray-200 rounded w-12"></div>
            </div>
            <div class="h-1.5 w-full bg-gray-100 rounded-full"></div>
        </div>
        <?php endfor; ?>
    </div>

    <!-- Populated Story Grid -->
    <div id="lib-story-grid" class="hidden grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-x-6 gap-y-10">
    </div>

    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const followingCountEl = document.getElementById('lib-following-count');
        const skeletonGrid = document.getElementById('lib-skeleton-grid');
        const emptyState = document.getElementById('lib-empty-state');
        const storyGrid = document.getElementById('lib-story-grid');
        
        // Read from localStorage
        let followed = JSON.parse(localStorage.getItem('tehi_followed_stories') || '[]');
        
        // Update statistics counter
        if (followingCountEl) {
            followingCountEl.textContent = followed.length;
        }
        
        // Check if empty
        if (followed.length === 0) {
            if (skeletonGrid) skeletonGrid.classList.add('hidden');
            if (emptyState) emptyState.classList.remove('hidden');
            return;
        }
        
        // Fetch dynamic story cards from server
        const formData = new FormData();
        formData.append('action', 'tehi_get_followed_stories');
        followed.forEach(id => formData.append('ids[]', id));
        
        fetch('<?php echo admin_url('admin-ajax.php'); ?>', {
            method: 'POST',
            body: formData
        })
        .then(res => res.json())
        .then(data => {
            if (skeletonGrid) {
                skeletonGrid.classList.add('hidden');
            }
            
            if (data.success && data.data.count > 0) {
                if (storyGrid) {
                    storyGrid.innerHTML = data.data.html;
                    storyGrid.classList.remove('hidden');
                    
                    // Bind unfollow actions on returned cards
                    bindUnfollowActions();
                }
            } else {
                if (emptyState) emptyState.classList.remove('hidden');
            }
        })
        .catch(err => {
            console.error('Lỗi tải tủ truyện:', err);
            if (skeletonGrid) skeletonGrid.classList.add('hidden');
            if (emptyState) emptyState.classList.remove('hidden');
        });
        
        function bindUnfollowActions() {
            const unfollowButtons = document.querySelectorAll('.btn-unfollow-card');
            unfollowButtons.forEach(btn => {
                btn.addEventListener('click', function(e) {
                    e.stopPropagation();
                    e.preventDefault();
                    
                    const storyId = parseInt(this.getAttribute('data-id'));
                    if (!storyId) return;
                    
                    if (confirm('Bạn có muốn bỏ theo dõi truyện này không?')) {
                        // Update localStorage
                        followed = JSON.parse(localStorage.getItem('tehi_followed_stories') || '[]');
                        const index = followed.indexOf(storyId);
                        if (index > -1) {
                            followed.splice(index, 1);
                            localStorage.setItem('tehi_followed_stories', JSON.stringify(followed));
                        }
                        
                        // Update UI stats
                        if (followingCountEl) {
                            followingCountEl.textContent = followed.length;
                        }
                        
                        // Find card element and animate out
                        const card = this.closest('.story-card-library');
                        if (card) {
                            card.style.opacity = '0';
                            card.style.transform = 'scale(0.8)';
                            setTimeout(() => {
                                card.remove();
                                
                                // If library becomes empty after deletion
                                if (followed.length === 0) {
                                    if (storyGrid) storyGrid.classList.add('hidden');
                                    if (emptyState) emptyState.classList.remove('hidden');
                                }
                            }, 300);
                        }
                    }
                });
            });
        }
    });
    </script>

</main>

<?php get_footer(); ?>
