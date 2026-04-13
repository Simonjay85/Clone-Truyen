php_code_teams = """<?php
/*
Template Name: Nhóm Dịch
*/
get_header();
?>

<main class="flex-grow pt-24 pb-20 max-w-7xl mx-auto px-6 w-full min-h-screen">
    <!-- Hero Banner -->
    <section class="mb-16 relative overflow-hidden bg-surface-container-low rounded-[2rem] p-8 md:p-12 border border-outline-variant/10 shadow-[0px_4px_32px_rgba(0,0,0,0.02)]">
        <div class="absolute top-0 right-0 w-1/2 h-full opacity-10 pointer-events-none">
            <!-- abstract geometry bg -->
            <div class="absolute right-0 w-96 h-96 bg-primary rounded-full blur-[100px] -mt-20 -mr-20"></div>
        </div>

        <div class="relative z-10 flex flex-col lg:flex-row items-center justify-between gap-12">
            <div class="max-w-xl">
                <div class="inline-block px-4 py-1.5 bg-primary-fixed text-on-primary-fixed-variant rounded-full text-[11px] font-black tracking-widest uppercase mb-6 shadow-sm">Cộng Đồng Dịch Thuật</div>
                <h1 class="text-4xl md:text-5xl font-extrabold font-headline text-on-background tracking-tight mb-4 leading-tight">
                    Những Người Truyền Tải <span class="bg-clip-text text-transparent bg-gradient-to-r from-primary to-primary-container">Cảm Hứng Số.</span>
                </h1>
                <p class="text-on-surface-variant text-lg mb-8 leading-relaxed">Khám phá các nhóm dịch tâm huyết, những người đứng sau hàng ngàn chương truyện hấp dẫn tại tehitruyen.com.</p>
                
                <div class="flex items-center gap-4 bg-surface-container-highest/50 w-fit p-2 rounded-full border border-outline-variant/20 shadow-sm">
                    <div class="flex -space-x-3 pl-2">
                        <img class="w-10 h-10 rounded-full border-2 border-surface object-cover shadow-sm bg-slate-200" src="https://placehold.co/100?text=U1">
                        <img class="w-10 h-10 rounded-full border-2 border-surface object-cover shadow-sm bg-amber-200" src="https://placehold.co/100?text=U2">
                        <img class="w-10 h-10 rounded-full border-2 border-surface object-cover shadow-sm bg-primary/20" src="https://placehold.co/100?text=U3">
                        <div class="w-10 h-10 rounded-full border-2 border-surface bg-primary text-white flex items-center justify-center text-[10px] font-bold shadow-sm z-10">+120</div>
                    </div>
                    <p class="text-xs font-medium text-on-surface-variant pr-4">Tham gia cùng hơn <span class="font-bold text-on-surface">2,000</span> dịch giả chuyên nghiệp</p>
                </div>
            </div>

            <!-- Dashboard Mini Mock -->
            <div class="w-full lg:w-[450px] bg-white/60 backdrop-blur-xl rounded-2xl p-6 shadow-[0px_24px_48px_rgba(0,96,169,0.08)] border border-white relative hidden md:block transform rotate-1 hover:rotate-0 transition-transform duration-500">
                <div class="flex items-center gap-4 mb-6">
                    <div class="w-12 h-12 bg-primary/10 text-primary rounded-xl flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">menu_book</span>
                    </div>
                    <div>
                        <h4 class="font-bold text-on-surface font-headline">Hệ Thống Rank</h4>
                        <p class="text-[11px] text-outline font-medium tracking-wide">Cập nhật 2 phút trước</p>
                    </div>
                </div>
                <div class="space-y-4">
                    <div>
                        <div class="flex justify-between text-xs font-bold mb-2">
                            <span class="text-on-surface">Top Nhóm Tháng</span>
                            <span class="text-primary tracking-wide">8,420 điểm</span>
                        </div>
                        <div class="h-2 w-full bg-surface-container rounded-full overflow-hidden">
                            <div class="h-full bg-primary rounded-full" style="width: 85%"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section Title -->
    <div class="flex flex-col sm:flex-row items-center justify-between mb-10 gap-4">
        <div>
            <h2 class="text-2xl font-extrabold font-headline text-on-surface tracking-tight mb-1">Nhóm Dịch Tiêu Biểu</h2>
            <p class="text-sm text-on-surface-variant">Dựa trên số lượng chương và lượt đọc trong tháng</p>
        </div>
        <div class="flex gap-2 text-outline">
            <button class="w-10 h-10 rounded-full border border-outline-variant/30 flex items-center justify-center hover:bg-surface-container-low transition-colors"><span class="material-symbols-outlined text-[20px]">filter_list</span></button>
            <button class="w-10 h-10 rounded-full border border-outline-variant/30 flex items-center justify-center hover:bg-surface-container-low transition-colors"><span class="material-symbols-outlined text-[20px]">sort</span></button>
        </div>
    </div>

    <!-- Teams Grid Mockup -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        
        <!-- Team 1 -->
        <div class="bg-surface-container-lowest border border-outline-variant/20 rounded-[2rem] p-8 hover:shadow-[0px_20px_40px_rgba(0,0,0,0.06)] hover:border-primary/20 transition-all duration-300 group flex flex-col h-full">
            <div class="flex justify-between items-start mb-6">
                <div class="w-16 h-16 rounded-2xl bg-primary/5 border border-primary/10 flex items-center justify-center text-primary font-black text-2xl font-headline group-hover:scale-110 transition-transform">TP</div>
                <span class="bg-primary-container text-on-primary-container px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-widest shadow-sm">TOP 1</span>
            </div>
            <h3 class="text-xl font-bold font-headline mb-2 text-on-surface">Thần Phong Team</h3>
            <p class="text-sm text-on-surface-variant mb-6 flex-grow leading-relaxed">Chuyên dòng tiên hiệp, huyền huyễn với tốc độ dịch "bàn thờ". Đảm bảo chất lượng từng câu chữ.</p>
            <div class="flex gap-4 mb-8">
                <div class="flex-1 bg-surface-container-low p-3 rounded-xl text-center border border-outline-variant/10">
                    <div class="text-primary font-black font-headline text-lg">42</div>
                    <div class="text-[9px] text-outline font-bold uppercase tracking-widest mt-1">Thành viên</div>
                </div>
                <div class="flex-1 bg-surface-container-low p-3 rounded-xl text-center border border-outline-variant/10">
                    <div class="text-primary font-black font-headline text-lg">12.5k</div>
                    <div class="text-[9px] text-outline font-bold uppercase tracking-widest mt-1">Chương dịch</div>
                </div>
            </div>
            <div>
                <p class="text-[10px] font-bold uppercase tracking-widest text-outline mb-3 flex items-center gap-1">
                    <span class="material-symbols-outlined text-[14px]">menu_book</span> Truyện đang dịch
                </p>
                <div class="flex flex-wrap gap-2 text-[11px] font-bold text-on-surface">
                    <span class="bg-surface-container-high px-3 py-1.5 rounded-md hover:bg-secondary-container transition-colors cursor-pointer">Vạn Cổ Đệ Nhất Thần</span>
                    <span class="bg-surface-container-high px-3 py-1.5 rounded-md hover:bg-secondary-container transition-colors cursor-pointer">Đại Chúa Tể</span>
                    <span class="bg-surface-container-high px-3 py-1.5 rounded-md hover:bg-secondary-container transition-colors cursor-pointer text-outline">+5 truyện khác</span>
                </div>
            </div>
        </div>

        <!-- Team 2 -->
        <div class="bg-surface-container-lowest border border-outline-variant/20 rounded-[2rem] p-8 hover:shadow-[0px_20px_40px_rgba(0,0,0,0.06)] hover:border-primary/20 transition-all duration-300 group flex flex-col h-full">
            <div class="flex justify-between items-start mb-6">
                <div class="w-16 h-16 rounded-2xl bg-emerald-50 border border-emerald-100 flex items-center justify-center text-emerald-600 font-black text-2xl font-headline group-hover:scale-110 transition-transform">HN</div>
                <span class="bg-surface-variant text-on-surface-variant px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-widest border border-outline-variant/30 flex items-center gap-1"><span class="material-symbols-outlined text-[10px]">verified</span> VERIFIED</span>
            </div>
            <h3 class="text-xl font-bold font-headline mb-2 text-on-surface">Hàn Nguyệt Các</h3>
            <p class="text-sm text-on-surface-variant mb-6 flex-grow leading-relaxed">Nơi quy tụ những tâm hồn lãng mạn, chuyên trị các dòng ngôn tình, trọng sinh và cung đấu.</p>
            <div class="flex gap-4 mb-8">
                <div class="flex-1 bg-surface-container-low p-3 rounded-xl text-center border border-outline-variant/10">
                    <div class="text-emerald-600 font-black font-headline text-lg">18</div>
                    <div class="text-[9px] text-outline font-bold uppercase tracking-widest mt-1">Thành viên</div>
                </div>
                <div class="flex-1 bg-surface-container-low p-3 rounded-xl text-center border border-outline-variant/10">
                    <div class="text-emerald-600 font-black font-headline text-lg">5.2k</div>
                    <div class="text-[9px] text-outline font-bold uppercase tracking-widest mt-1">Chương dịch</div>
                </div>
            </div>
            <div>
                <p class="text-[10px] font-bold uppercase tracking-widest text-outline mb-3 flex items-center gap-1">
                    <span class="material-symbols-outlined text-[14px]">menu_book</span> Truyện đang dịch
                </p>
                <div class="flex flex-wrap gap-2 text-[11px] font-bold text-on-surface">
                    <span class="bg-surface-container-high px-3 py-1.5 rounded-md hover:bg-secondary-container transition-colors cursor-pointer">Gió Ấm Không Bằng...</span>
                    <span class="bg-surface-container-high px-3 py-1.5 rounded-md hover:bg-secondary-container transition-colors cursor-pointer">Nhất Dạ Phu Thê</span>
                </div>
            </div>
        </div>

        <!-- Team 3 -->
        <div class="bg-surface-container-lowest border border-outline-variant/20 rounded-[2rem] p-8 hover:shadow-[0px_20px_40px_rgba(0,0,0,0.06)] hover:border-primary/20 transition-all duration-300 group flex flex-col h-full">
            <div class="flex justify-between items-start mb-6">
                <div class="w-16 h-16 rounded-2xl bg-amber-500 border border-amber-600 flex items-center justify-center text-white font-black text-2xl font-headline group-hover:scale-110 transition-transform">LS</div>
                <span class="bg-red-500 text-white px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-widest shadow-sm">HOT</span>
            </div>
            <h3 class="text-xl font-bold font-headline mb-2 text-on-surface">Linh Sơn Tự</h3>
            <p class="text-sm text-on-surface-variant mb-6 flex-grow leading-relaxed">Tập trung vào các tác phẩm kinh điển và những bộ tiểu thuyết có chiều sâu văn hóa cao.</p>
            <div class="flex gap-4 mb-8">
                <div class="flex-1 bg-surface-container-low p-3 rounded-xl text-center border border-outline-variant/10">
                    <div class="text-amber-600 font-black font-headline text-lg">25</div>
                    <div class="text-[9px] text-outline font-bold uppercase tracking-widest mt-1">Thành viên</div>
                </div>
                <div class="flex-1 bg-surface-container-low p-3 rounded-xl text-center border border-outline-variant/10">
                    <div class="text-amber-600 font-black font-headline text-lg">8.9k</div>
                    <div class="text-[9px] text-outline font-bold uppercase tracking-widest mt-1">Chương dịch</div>
                </div>
            </div>
            <div>
                <p class="text-[10px] font-bold uppercase tracking-widest text-outline mb-3 flex items-center gap-1">
                    <span class="material-symbols-outlined text-[14px]">menu_book</span> Truyện đang dịch
                </p>
                <div class="flex flex-wrap gap-2 text-[11px] font-bold text-on-surface">
                    <span class="bg-surface-container-high px-3 py-1.5 rounded-md hover:bg-secondary-container transition-colors cursor-pointer">Chuỗi Hạt Ngọc Trai</span>
                    <span class="bg-surface-container-high px-3 py-1.5 rounded-md hover:bg-secondary-container transition-colors cursor-pointer">Đường Về Cố Hương</span>
                    <span class="bg-surface-container-high px-3 py-1.5 rounded-md hover:bg-secondary-container transition-colors cursor-pointer text-outline">Tuyết Sơn</span>
                </div>
            </div>
        </div>
    </div> <!-- Close Grid Row 1 -->

    <!-- Call to action block -->
    <div class="mt-20 bg-gradient-to-br from-surface-container-lowest to-surface px-8 py-16 rounded-[3rem] text-center border-4 border-primary/20 shadow-2xl relative overflow-hidden group">
        <div class="absolute inset-0 bg-primary/5 opacity-0 group-hover:opacity-100 transition-opacity duration-1000"></div>
        <div class="w-16 h-16 bg-primary-container text-primary rounded-full flex items-center justify-center mx-auto mb-6 shadow-inner pointer-events-none">
            <span class="material-symbols-outlined text-3xl">group_add</span>
        </div>
        <h2 class="text-3xl font-extrabold font-headline mb-4 relative z-10 text-on-background">Bạn Có Nhóm Dịch?</h2>
        <p class="text-on-surface-variant max-w-xl mx-auto mb-10 leading-relaxed text-lg relative z-10">Hãy đưa đứa con tinh thần của bạn đến với cộng đồng lớn nhất. Chúng tôi cung cấp công cụ quản lý chương và doanh thu minh bạch nhất.</p>
        <div class="flex justify-center gap-4 relative z-10 font-headline">
            <button class="bg-primary text-white font-bold px-10 py-3.5 rounded-full shadow-xl hover:-translate-y-1 hover:shadow-primary/40 transition-all" onclick="alert('Đang cập nhật tính năng Nhóm Dịch')">Đăng ký Nhóm ngay</button>
            <button class="bg-transparent border-2 border-outline-variant/30 text-on-surface font-bold px-8 py-3.5 rounded-full hover:bg-surface-container transition-colors">Tìm hiểu thêm</button>
        </div>
    </div>
</main>

<?php get_footer(); ?>
"""

with open("tehi-theme/page-teams.php", "w", encoding="utf-8") as f:
    f.write(php_code_teams)

print("Created page-teams.php")
