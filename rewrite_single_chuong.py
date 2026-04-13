import re

with open("tehi-theme/single-chuong.php", "r", encoding="utf-8") as f:
    orig = f.read()

# 1. Look for the PHP block at the top handling chapters_query
php_block = re.search(r'(<\?php\s*get_header.*?\?>.*?)(<style>|<!-- breadcrumb start -->|<nav)', orig, re.DOTALL | re.IGNORECASE)
if php_block:
    top_php = php_block.group(1)
    
# Wait, let's just write the Tailwind structure manually because it's much safer than regexing 3400 lines of chaotic Bootstrap.

tailwind_reader = """<?php get_header(); ?>
<?php if (have_posts()) : while (have_posts()) : the_post(); ?>
<?php
    // Bắt đầu Lấy Data
    $truyen_id = get_post_meta(get_the_ID(), '_truyen_id', true);
    $parent_story = get_post($truyen_id);
    $story_title = $parent_story ? $parent_story->post_title : 'Đọc Tiểu Thuyết';
    $story_link = $parent_story ? get_permalink($truyen_id) : home_url('/');

    $chapters_query = new WP_Query([
        'post_type' => 'chuong',
        'meta_query' => [['key' => '_truyen_id', 'value' => $truyen_id, 'compare' => '=']],
        'orderby' => 'menu_order date',
        'order' => 'ASC',
        'posts_per_page' => -1
    ]);
    
    $chapter_posts = $chapters_query->posts;
    $current_id = get_the_ID();
    $current_index = -1;
    foreach ($chapter_posts as $index => $chap) {
        if ($chap->ID == $current_id) { $current_index = $index; break; }
    }
    
    $prev_link = '#'; $next_link = '#';
    $is_first = ($current_index <= 0);
    $is_last = ($current_index == count($chapter_posts) - 1 || $current_index == -1);
    if (!$is_first) { $prev_link = get_permalink($chapter_posts[$current_index - 1]->ID); }
    if (!$is_last) { $next_link = get_permalink($chapter_posts[$current_index + 1]->ID); }
?>

<!-- Đưa Affiliate styles cho nó sạch sẽ -->
<?php if ( get_option("tehi_aff_enabled") ): ?>
<style>
.affiliate-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.8); backdrop-filter: blur(8px); z-index: 99990; display: flex; align-items: center; justify-content: center; }
.affiliate-modal { background: #fff; width: 90%; max-width: 400px; border-radius: 24px; overflow: hidden; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25); text-align: center; }
.affiliate-header { padding: 32px 24px 24px; background: linear-gradient(135deg, #0060a9, #3f9cfb); color: #fff; }
.affiliate-body { padding: 32px 24px; }
</style>
<?php endif; ?>

<main class="pt-24 pb-20 max-w-4xl mx-auto px-4 md:px-8">
    
    <!-- Breadcrumb -->
    <nav class="flex justify-center text-sm font-medium text-on-surface-variant mb-6 font-['Plus_Jakarta_Sans']">
        <a href="<?php echo home_url('/'); ?>" class="hover:text-primary transition-colors">Trang chủ</a>
        <span class="mx-2">&rsaquo;</span>
        <a href="<?php echo $story_link; ?>" class="hover:text-primary transition-colors"><?php echo $story_title; ?></a>
        <span class="mx-2">&rsaquo;</span>
        <span class="text-on-surface font-bold"><?php the_title(); ?></span>
    </nav>
    
    <!-- Title -->
    <div class="text-center mb-8">
        <h1 class="text-3xl md:text-5xl font-bold text-on-surface mb-4 font-['Plus_Jakarta_Sans']"><?php the_title(); ?></h1>
        <p class="text-on-surface-variant text-sm flex items-center justify-center gap-4">
            <span><span class="material-symbols-outlined text-sm align-middle">schedule</span> <?php echo get_the_date('H:i - d/m/Y'); ?></span>
        </p>
    </div>
    
    <!-- Navigation (Top) -->
    <div class="flex justify-center items-center gap-4 mb-10">
        <a href="<?php echo $prev_link; ?>" class="rounded-full bg-surface-container-high text-on-surface px-6 py-2.5 font-bold hover:bg-surface-variant transition-colors flex items-center gap-2 <?php echo $is_first ? 'opacity-50 pointer-events-none' : ''; ?>">
            <span class="material-symbols-outlined">arrow_back</span> Trước
        </a>
        <button id="chapterListToggle" class="rounded-full bg-primary/10 text-primary px-6 py-2.5 font-bold hover:bg-primary/20 transition-colors flex items-center gap-2">
            <span class="material-symbols-outlined">list</span> <?php the_title(); ?>
        </button>
        <a href="<?php echo $next_link; ?>" class="rounded-full bg-surface-container-high text-on-surface px-6 py-2.5 font-bold hover:bg-surface-variant transition-colors flex items-center gap-2 <?php echo $is_last ? 'opacity-50 pointer-events-none' : ''; ?>">
            Sau <span class="material-symbols-outlined">arrow_forward</span>
        </a>
    </div>

    <!-- Dropdown (Hidden initially) -->
    <div id="chapterListDropdown" class="hidden max-w-md mx-auto mb-10 bg-surface-container-highest p-2 rounded-2xl max-h-64 overflow-y-auto shadow-inner">
        <?php foreach ($chapter_posts as $chap): $active = ($chap->ID == $current_id) ? 'bg-primary text-white font-bold' : 'text-on-surface hover:bg-surface-container-low'; ?>
            <a href="<?php echo get_permalink($chap->ID); ?>" class="block px-4 py-3 rounded-xl <?php echo $active; ?> transition-colors truncate">
                <?php echo get_the_title($chap->ID); ?>
            </a>
        <?php endforeach; ?>
    </div>

    <!-- CÔNG CỤ ĐỌC TRUYỆN (Floating Glassmorphism UI) -->
    <div class="fixed right-6 bottom-10 z-50 flex flex-col gap-3">
        <!-- Settings Toggle button -->
        <button id="toggleSettings" class="w-12 h-12 rounded-full bg-white/90 backdrop-blur-md shadow-[0_12px_32px_rgba(0,0,0,0.1)] border border-white/20 text-on-surface-variant hover:text-primary transition-all flex items-center justify-center">
            <span class="material-symbols-outlined">settings</span>
        </button>
        <!-- Home button -->
        <a href="<?php echo home_url('/'); ?>" class="w-12 h-12 rounded-full bg-white/90 backdrop-blur-md shadow-[0_12px_32px_rgba(0,0,0,0.1)] border border-white/20 text-on-surface-variant hover:text-primary transition-all flex items-center justify-center">
            <span class="material-symbols-outlined">home</span>
        </a>
        <button id="scrollTop" class="w-12 h-12 rounded-full bg-primary text-white shadow-lg shadow-primary/30 transition-all flex items-center justify-center">
            <span class="material-symbols-outlined">arrow_upward</span>
        </button>
        
        <!-- Settings Panel -->
        <div id="settingsPanel" class="hidden absolute bottom-0 right-16 w-64 bg-white/90 dark:bg-slate-900/90 backdrop-blur-xl p-5 rounded-3xl shadow-[0_12px_32px_rgba(0,0,0,0.15)] border border-outline-variant/20">
            <h4 class="font-bold text-on-surface mb-4 font-['Plus_Jakarta_Sans']">Cài đặt Đọc</h4>
            <div class="mb-4">
                <span class="text-xs font-bold text-on-surface-variant uppercase tracking-wider mb-2 block">Cỡ Chữ</span>
                <div class="flex items-center gap-3">
                    <button id="fontDec" class="w-8 h-8 rounded-full bg-surface-container-high text-on-surface flex items-center justify-center hover:bg-surface-variant transition-colors">-</button>
                    <span id="fontSizeDisplay" class="flex-1 text-center font-bold">22px</span>
                    <button id="fontInc" class="w-8 h-8 rounded-full bg-surface-container-high text-on-surface flex items-center justify-center hover:bg-surface-variant transition-colors">+</button>
                </div>
            </div>
            <div>
                <span class="text-xs font-bold text-on-surface-variant uppercase tracking-wider mb-2 block">Màu Nền</span>
                <div class="flex gap-2">
                    <button data-theme="white" class="w-10 h-10 rounded-full border-2 border-outline-variant/30 bg-[#fbf9f8] btn-theme"></button>
                    <button data-theme="sepia" class="w-10 h-10 rounded-full border-2 border-outline-variant/30 bg-[#f4ecd8] btn-theme"></button>
                    <button data-theme="dark" class="w-10 h-10 rounded-full border-2 border-outline-variant/30 bg-[#1a1a2e] btn-theme"></button>
                </div>
            </div>
        </div>
    </div>

    <!-- QUẢNG CÁO AFFILIATE SHOPEE -->
    <?php if ( get_option("tehi_aff_enabled") && !isset($_COOKIE['tehi_aff_passed']) ): ?>
    <div id="affiliate-notification" class="affiliate-overlay">
        <div class="affiliate-modal animate-slideUp">
            <div class="affiliate-header">
                <h3 class="text-2xl font-bold font-['Plus_Jakarta_Sans']">Thông Báo Đặc Biệt</h3>
            </div>
            <div class="affiliate-body">
                <span class="material-symbols-outlined text-6xl text-primary mb-4">shopping_bag</span>
                <p class="text-xl font-bold text-error mb-2">Chương này có quảng cáo!</p>
                <p class="text-on-surface-variant text-sm mb-8">Nội dung chương sẽ tự động hiển thị sau khi bạn bấm xem qua nhà tài trợ.</p>
                
                <a href="<?php echo esc_url(get_option("tehi_aff_url", home_url("/"))); ?>" target="_blank" onclick="document.cookie='tehi_aff_passed=1;path=/'; document.getElementById('affiliate-notification').style.display='none'; document.getElementById('noi_dung_truyen').classList.remove('hidden');" class="bg-gradient-to-br from-primary to-primary-container text-white font-bold w-full py-4 rounded-xl shadow-lg hover:shadow-xl transition-all flex items-center justify-center gap-2">
                    Tiếp Tục Đọc Truyện <span class="material-symbols-outlined">arrow_forward</span>
                </a>
                <p class="text-[10px] text-on-surface-variant mt-4 uppercase tracking-widest">CẢM ƠN BẠN ĐÃ ỦNG HỘ</p>
            </div>
        </div>
    </div>
    <?php endif; ?>

    <!-- NỘI DUNG TRUYỆN -->
    <div id="noi_dung_truyen" class="prose max-w-none font-['Inter'] leading-relaxed text-on-surface-variant <?php echo (get_option("tehi_aff_enabled") && !isset($_COOKIE['tehi_aff_passed'])) ? "hidden" : ""; ?>" style="font-size: 22px;">
        <?php echo get_the_content(); ?>
    </div>

    <!-- Navigation (Bottom) -->
    <div class="flex justify-center items-center gap-4 mt-16 pb-10 border-t border-outline-variant/10 pt-10">
        <a href="<?php echo $prev_link; ?>" class="rounded-full bg-surface-container-high text-on-surface px-8 py-4 font-bold hover:bg-surface-variant transition-colors flex items-center gap-2 <?php echo $is_first ? 'opacity-50 pointer-events-none' : ''; ?>">
            <span class="material-symbols-outlined">arrow_back</span> Chương Trước
        </a>
        <a href="<?php echo $next_link; ?>" class="rounded-full bg-gradient-to-br from-primary to-primary-container text-white px-8 py-4 font-bold shadow-lg shadow-primary/20 hover:shadow-primary/40 transition-colors flex items-center gap-2 <?php echo $is_last ? 'opacity-50 pointer-events-none' : ''; ?>">
            Chương Sau <span class="material-symbols-outlined">arrow_forward</span>
        </a>
    </div>

</main>

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Dropdown toggle
    const toggleBtn = document.getElementById('chapterListToggle');
    const dropdown = document.getElementById('chapterListDropdown');
    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            dropdown.classList.toggle('hidden');
        });
    }

    // Tools toggle
    const toggleSettingsBtn = document.getElementById('toggleSettings');
    const settingsPanel = document.getElementById('settingsPanel');
    if (toggleSettingsBtn) {
        toggleSettingsBtn.addEventListener('click', () => {
            settingsPanel.classList.toggle('hidden');
        });
    }

    // Scroll top
    const scrollTopBtn = document.getElementById('scrollTop');
    if (scrollTopBtn) {
        scrollTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Reader Settings
    const content = document.getElementById('noi_dung_truyen');
    const fontDisplay = document.getElementById('fontSizeDisplay');
    const htmlTag = document.documentElement;
    let currentSize = parseInt(localStorage.getItem('reader-size')) || 22;
    
    function applySize() {
        content.style.fontSize = currentSize + 'px';
        fontDisplay.innerText = currentSize + 'px';
        localStorage.setItem('reader-size', currentSize);
    }
    applySize();

    document.getElementById('fontInc').addEventListener('click', () => { currentSize+=2; applySize(); });
    document.getElementById('fontDec').addEventListener('click', () => { currentSize=Math.max(14, currentSize-2); applySize(); });

    // Themes (Hack using Tailwind dark mode & inline colors)
    const btns = document.querySelectorAll('.btn-theme');
    function applyTheme(theme) {
        if(theme === 'dark') {
            htmlTag.classList.add('dark');
            htmlTag.style.background = '#1a1a2e';
            content.style.color = '#e0e0e0';
        } else if (theme === 'sepia') {
            htmlTag.classList.remove('dark');
            htmlTag.style.background = '#f4ecd8';
            content.style.color = '#5b4636';
        } else {
            htmlTag.classList.remove('dark');
            htmlTag.style.background = '#fbf9f8';
            content.style.color = ''; // fallback to text-on-surface-variant
        }
        localStorage.setItem('reader-theme', theme);
    }

    const savedTheme = localStorage.getItem('reader-theme') || 'white';
    applyTheme(savedTheme);

    btns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            applyTheme(e.target.dataset.theme);
        });
    });
});
</script>

<?php endwhile; endif; ?>
<?php get_footer(); ?>
"""

with open("tehi-theme/single-chuong.php", "w", encoding="utf-8") as f:
    f.write(tailwind_reader)

print("single-chuong.php rewritten!")
