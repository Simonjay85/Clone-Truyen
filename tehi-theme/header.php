<?php
// ── Browser Cache Headers for static pages ──
if (!is_user_logged_in() && !is_admin()) {
    header('Cache-Control: public, max-age=3600, s-maxage=86400, stale-while-revalidate=604800');
    header('Vary: Accept-Encoding');
}
?>
<!DOCTYPE html>
<html lang="vi">

<head>
  <meta charset="utf-8">
  <meta http-equiv="x-ua-compatible" content="IE=edge">

  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title><?php wp_title('|', true, 'right'); ?><?php bloginfo('name'); ?></title>
<meta name="keywords" content="<?php bloginfo('name'); ?>, Đọc Truyện Ngôn, Đọc Truyện Ngôn Tình, truyện ngôn tình full, truyện ngôn tình mới nhất, ngôn tình hiện đại, đọc truyện miễn phí" />
<meta name="description" content="<?php echo esc_attr(wp_trim_words(wp_strip_all_tags(get_the_excerpt() ?: '<?php bloginfo(\'name\'); ?> – Đọc Truyện Ngôn Tình Hay Nhất 2026.'), 25, '...')); ?>" />
<link href="<?php echo esc_url(get_permalink()); ?>" rel="canonical" />
<link href="<?php echo get_site_url(); ?>/img_data/images/icon_tehi_truyen_2025.png" rel="shortcut icon" type="image/x-icon" />
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-BMCE7V4VHX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-BMCE7V4VHX');
</script><!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="<?php echo esc_attr(get_the_title() ?: get_bloginfo('name')); ?>">
<meta name="twitter:site" content="@<?php bloginfo('name'); ?>">
<meta name="twitter:description" content="<?php echo esc_attr(wp_trim_words(wp_strip_all_tags(get_the_excerpt()), 25, '...')); ?>">
<meta name="twitter:image" content="<?php echo esc_url(get_the_post_thumbnail_url() ?: get_site_url() . '/img_data/images/icon_tehi_truyen_2025.png'); ?>">
<meta name="twitter:image:alt" content="<?php echo esc_attr(get_the_title()); ?>">
<!-- Open Graph -->
<meta property="og:type" content="<?php echo is_single() ? 'article' : 'website'; ?>">
<meta property="og:url" content="<?php echo esc_url(get_permalink()); ?>" />
<meta property="og:title" content="<?php echo esc_attr(get_the_title() ?: get_bloginfo('name')); ?>" />
<meta property="og:image" content="<?php echo esc_url(get_the_post_thumbnail_url() ?: get_site_url() . '/img_data/images/icon_tehi_truyen_2025.png'); ?>" />
<meta property="og:description" content="<?php echo esc_attr(wp_trim_words(wp_strip_all_tags(get_the_excerpt() ?: '<?php bloginfo(\'name\'); ?> – Đọc Truyện Ngôn Tình Hay Nhất 2026.'), 25, '...')); ?>" />
<!-- Khai báo ngôn ngữ -->
<script type="application/ld+json">
    {
        "@context": "http://schema.org",
        "@type": "Organization",
        "legalname": "<?php bloginfo('name'); ?>",
        "url": "<?php echo get_site_url(); ?>",
        "contactPoint": [{
            "@type": "ContactPoint",
            "telephone": "+840373685221",
            "contactType": "customer service",
            "contactOption": "TollFree",
            "areaServed": "VN"
        }],
        "logo": "<?php echo get_site_url(); ?>/img_data/images/logo-truyen-moi-v1.png"
    }
</script>
<!-- DNS Prefetch for speed -->
<link rel="dns-prefetch" href="//cdn.jsdelivr.net">
<link rel="dns-prefetch" href="//cdnjs.cloudflare.com">
<link rel="dns-prefetch" href="//fonts.googleapis.com">
<link rel="dns-prefetch" href="//fonts.gstatic.com">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- Be Vietnam Pro - non-blocking -->
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="preload" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet"></noscript>
<style>
/* System font fallback while web font loads */
body, h1, h2, h3, h4, h5, h6, p, a, div, span, button, input, textarea, select, label, strong, b, i, em {
    font-family: 'Be Vietnam Pro', ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif !important;
}
.fa, .fas, .far, .fal, .fad, .fab, .fa-solid, .fa-brands, .fa-regular {
    font-family: "Font Awesome 6 Free", "Font Awesome 5 Free", "FontAwesome" !important;
}
.fas, .fa-solid { font-weight: 900 !important; }
.fa-brands { font-family: "Font Awesome 6 Brands" !important; }
}
</style>

<!-- ══ CRITICAL CSS - Only what's needed for above-fold render ══ -->
<!-- bootstrap: grid + utilities needed before render -->
<link rel="stylesheet" href="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/css/bootstrap.min.css">
<!-- base theme vars + body font (6.8KB) -->
<link rel="stylesheet" href="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/css/style.css?ver=1120">

<!-- ══ NON-CRITICAL CSS (async via print trick - most reliable) ══ -->
<!-- FontAwesome - icons not above-fold critical -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" media="print" onload="this.media='all'">
<!-- style-truyen-moi-v1.css - page-specific -->
<link rel="stylesheet" href="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/css/style-truyen-moi-v1.css?ver=1120" media="print" onload="this.media='all'">
<!-- media.css - responsive breakpoints only -->
<link rel="stylesheet" href="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/css/media.css?ver=1120" media="print" onload="this.media='all'">
<!-- style-mongdaovien.css - large 280KB, non-critical -->
<link rel="stylesheet" href="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/css/style-mongdaovien.css?ver=1120" media="print" onload="this.media='all'">
<!-- bootstrap-icons - icon pack -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css" media="print" onload="this.media='all'">
<!-- swiper CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css" media="print" onload="this.media='all'">
<!-- misc UI extras -->
<link rel="stylesheet" href="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/css/vh-skeleton.css" media="print" onload="this.media='all'">
<link rel="stylesheet" href="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/css/hover-min.css" media="print" onload="this.media='all'">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fancyapps/ui@5.0/dist/fancybox/fancybox.css" media="print" onload="this.media='all'">
<noscript>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/css/style-truyen-moi-v1.css?ver=1120">
  <link rel="stylesheet" href="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/css/media.css?ver=1120">
  <link rel="stylesheet" href="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/css/style-mongdaovien.css?ver=1120">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css">
  <link rel="stylesheet" href="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/css/vh-skeleton.css">
  <link rel="stylesheet" href="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/css/hover-min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fancyapps/ui@5.0/dist/fancybox/fancybox.css">
</noscript>

<!-- ══ PAGE-SPECIFIC CSS (not on reading page) ══ -->
<?php if (!is_singular('chuong')): ?>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css" media="print" onload="this.media='all'">
<link rel="stylesheet" href="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/css/emojionearea.css" media="print" onload="this.media='all'">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lelinh014756/fui-toast-js@master/assets/css/toast@1.0.1/fuiToast.min.css" media="print" onload="this.media='all'">
<noscript>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css">
  <link rel="stylesheet" href="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/css/emojionearea.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lelinh014756/fui-toast-js@master/assets/css/toast@1.0.1/fuiToast.min.css">
</noscript>
<?php endif; ?>

<!-- ══ JQUERY: defer first – guarantees load order before other defer scripts ══ -->
<script defer src="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/js/jquery.min.js"></script>

<!-- ══ ALL JS: defer (won't block render, runs in order after jQuery) ══ -->
<script defer src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/@fancyapps/ui@5.0/dist/fancybox/fancybox.umd.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.4/bundled/lenis.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/dompurify/2.3.4/purify.min.js"></script>
<script defer src="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/js/vh-skeleton.js"></script>
<script defer src="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/js/vanhiep_script.js"></script>

<!-- ══ PAGE-SPECIFIC JS (not on reading page) ══ -->
<?php if (!is_singular('chuong')): ?>
<script defer src="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js"></script>
<script defer src="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/assets/js/emojionearea.js"></script>
<script defer src="https://cdn.jsdelivr.net/gh/lelinh014756/fui-toast-js@master/assets/js/toast@1.0.1/fuiToast.min.js"></script>
<script defer src="<?php echo get_site_url(); ?>/wp-content/themes/tehi-theme/templates/module/sweetalert/sweetalert2.min.js"></script>
<?php endif; ?>





<script>
    let lenis; // Khai báo biến lenis toàn cục
    let destroyTimeout; // Biến lưu timeout để kiểm tra thời gian hover
    var currentPage = 'index';

    // 🌟 Font loading optimization for iOS
    let fontsLoaded = false;
    let fontLoadPromise = null;

    // Check if FontFaceSet API is supported (for modern browsers)
    function checkFontsLoaded() {
        if (document.fonts && document.fonts.ready) {
            return document.fonts.ready;
        }
        // Fallback for older browsers
        return new Promise((resolve) => {
            setTimeout(resolve, 1000); // Wait 1s for fonts to load
        });
    }

    // Improved font handling with iOS support
    async function initializeFonts() {
        try {
            // Wait for fonts to be ready
            await checkFontsLoaded();
            fontsLoaded = true;
            console.log('Fonts loaded successfully');
            
            // Apply font selection after fonts are ready
            applyFontSelection();
        } catch (error) {
            console.warn('Font loading error:', error);
            // Still apply fonts as fallback
            applyFontSelection();
        }
    }

    function applyFontSelection() {
        // 🌟 Font mặc định (Arial for better iOS compatibility)
        const defaultFont = "arial-font";
        let selectedFont = localStorage.getItem("selectedFont");

        // Nếu chưa có font nào được chọn, đặt font mặc định
        if (!selectedFont) {
            selectedFont = defaultFont;
            localStorage.setItem("selectedFont", selectedFont);
        }

        // Xóa class font cũ trước khi áp dụng font mới
        document.documentElement.classList.remove("roboto-font", "arial-font", "times-font", "lato-font", "josefinsans-font");
        
        // Apply new font class with delay for iOS
        setTimeout(() => {
            document.documentElement.classList.add(selectedFont);
            console.log('Font applied:', selectedFont);
        }, 100);
    }

    var toc_do_cuon_number = '5';
    var toc_do = 1;
    if (toc_do_cuon_number == 1) {
        toc_do = 30.0;
    } else if (toc_do_cuon_number == 2) {
        toc_do = 10.0;
    } else if (toc_do_cuon_number == 3) {
        toc_do = 6.0;
    } else if (toc_do_cuon_number == 4) {
        toc_do = 3.5;
    } else if (toc_do_cuon_number == 5) {
        toc_do = 1.1;
    } else {
        // off
        toc_do = 1.0;
    }


    // Hàm khởi tạo Lenis 
    function initLenis() {
        lenis = new Lenis({
            autoRaf: true, // Use modern automatic RequestAnimationFrame handling
            lerp: 0.1, // Optimal standard smoothing value
            smoothWheel: true, // Smooth on desktop
            smoothTouch: false, // Standard mobile scrolling
        });
        
        // lenis scroll bar start (vanilla JS – no jQuery dependency)
        const scrollbarEl = document.querySelector('.lenis-scrollbar');
        if (scrollbarEl) {
            let isScrollingTimer;
            window.addEventListener('scroll', function() {
                scrollbarEl.classList.add('visible');
                clearTimeout(isScrollingTimer);
                isScrollingTimer = setTimeout(function() {
                    scrollbarEl.classList.remove('visible');
                }, 1000);
            });
            scrollbarEl.addEventListener('mouseenter', function() {
                scrollbarEl.classList.add('visible');
            });
            scrollbarEl.addEventListener('mouseleave', function() {
                isScrollingTimer = setTimeout(function() {
                    scrollbarEl.classList.remove('visible');
                }, 1000);
            });
        }
        const scrollbar = document.querySelector('.lenis-scrollbar');
        const scrollbarThumb = document.querySelector('.lenis-scrollbar-thumb');
        if (scrollbar && scrollbarThumb) {
            lenis.on('scroll', ({
                scroll,
                limit
            }) => {
                const scrollRatio = scroll / limit;
                const thumbPosition = scrollRatio * (scrollbar.clientHeight - scrollbarThumb.clientHeight);
                scrollbarThumb.style.transform = `translateY(${thumbPosition}px)`;
            });
            // Drag functionality for scrollbar thumb
            let isDragging = false;
            let startY = 0;
            let startScroll = 0;
            scrollbarThumb.addEventListener('mousedown', (e) => {
                isDragging = true;
            });
            document.addEventListener('mousemove', (e) => {
                if (!isDragging) return;
                const deltaY = e.clientY - startY;
                const scrollAmount = deltaY * (lenis.limit / (scrollbar.clientHeight - scrollbarThumb.clientHeight));
                lenis.scrollTo(startScroll + scrollAmount, { immediate: true });
            });
            document.addEventListener('mouseup', () => {
                if (isDragging) {
                    isDragging = false;
                    document.body.style.userSelect = '';
                }
            });
        }
        // lenis scroll bar end
        // Đồng bộ GSAP với Lenis (only if GSAP available)
        if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
            gsap.registerPlugin(ScrollTrigger);
            lenis.on('scroll', ScrollTrigger.update);
            ScrollTrigger.scrollerProxy(document.body, {
                scrollTop(value) {
                    return arguments.length ? lenis.scrollTo(value) : lenis.scroll;
                },
                getBoundingClientRect() {
                    return { top: 0, left: 0, width: window.innerWidth, height: window.innerHeight };
                },
            });
        }
        console.log('Lenis initialized');
    }

    // ── Wait for Lenis library to load (deferred) before calling initLenis ──
    function tryInitLenis(attempt) {
        attempt = attempt || 0;
        if (typeof Lenis !== 'undefined') {
            initLenis();
        } else if (attempt < 50) {
            // Retry every 100ms for up to 5 seconds
            setTimeout(function() { tryInitLenis(attempt + 1); }, 100);
        } else {
            console.warn('Lenis library did not load in time');
        }
    }

    document.addEventListener("DOMContentLoaded", function() {
        // Initialize fonts first, then other components
        initializeFonts();
        
        // Gọi hàm khởi tạo Lenis với retry (vì Lenis load defer)
        tryInitLenis();


        // Kiểm tra nếu phần tử scrollbarThumb tồn tại trước khi thêm sự kiện
        const scrollbarThumb = document.querySelector('.lenis-scrollbar-thumb');
        if (scrollbarThumb) {
            // Drag functionality for scrollbar thumb
            let isDragging = false;
            let startY = 0;
            let startScroll = 0;
            scrollbarThumb.addEventListener('mousedown', (e) => {
                isDragging = true;
                startY = e.clientY;
                startScroll = lenis.scroll;
                document.body.style.userSelect = 'none'; // Disable text selection
            });
            document.addEventListener('mousemove', (e) => {
                if (!isDragging) return;
                const deltaY = e.clientY - startY;
                const scrollAmount = deltaY * (lenis.limit / (scrollbarThumb.parentElement.clientHeight - scrollbarThumb.clientHeight));
                lenis.scrollTo(startScroll + scrollAmount, {
                    immediate: true
                });
            });
            document.addEventListener('mouseup', () => {
                if (isDragging) {
                    isDragging = false;
                    document.body.style.userSelect = ''; // Re-enable text selection
                }
            });
        }
        // Init Fancybox safely (may be deferred)
        if (typeof Fancybox !== 'undefined') {
            Fancybox.bind("[data-fancybox]", {});
        } else {
            window.addEventListener('load', function() {
                if (typeof Fancybox !== 'undefined') Fancybox.bind("[data-fancybox]", {});
            });
        }

        // Khởi tạo skeletons – only when jQuery is available
        if (typeof $ !== 'undefined') {
            initializeVHSkeleton();
            initializeSkeletonOnScroll();
        } else {
            window.addEventListener('load', function() {
                if (typeof initializeVHSkeleton === 'function') initializeVHSkeleton();
                if (typeof initializeSkeletonOnScroll === 'function') initializeSkeletonOnScroll();
            });
        }

        // Kiểm tra vị trí cuộn và hiển thị hoặc ẩn nút "Back to Top"
        function initToTopButton() {
            var toTopHtml = '<div id="toTop"><i class="fa-solid fa-chevron-up"></i></div>';
            if (!document.getElementById('toTop')) document.body.insertAdjacentHTML('beforeend', toTopHtml);
            var toTopEl = document.getElementById('toTop');
            if (!toTopEl) return;
            toTopEl.style.display = 'none';
            window.addEventListener('scroll', function() {
                toTopEl.style.display = window.scrollY > 500 ? 'flex' : 'none';
            });
            toTopEl.addEventListener('click', function() {
                scrollToElement('body', 1.2);
            });
        }
        initToTopButton();



        // chữ title start
        // Refresh ScrollTrigger sau khi khởi tạo animation
        ScrollTrigger.refresh();

        // trang liên hệ start
        if (currentPage == 'lien-he') {
            // Hiệu ứng GSAP cho ".hq-contact-page-section-title-item span" khi trang load xong
            gsap.fromTo(
                ".hq-contact-page-section-title-item span", // Chọn tất cả các span bên trong phần tử tiêu đề
                {
                    y: -100, // Ban đầu di chuyển lên trên (ẩn đi)
                    opacity: 0, // Ban đầu ẩn
                    willChange: "transform, opacity" // Khai báo thuộc tính sẽ thay đổi để tối ưu hiệu suất
                }, {
                    y: 0, // Di chuyển về vị trí ban đầu
                    opacity: 1, // Hiển thị hoàn toàn
                    duration: 0.6, // Thời gian thực hiện hiệu ứng mỗi phần tử
                    ease: "power3.out", // Hiệu ứng nhanh dần và mượt mà
                    stagger: 0.2 // Khoảng thời gian giữa các phần tử để thực hiện hiệu ứng lần lượt
                }
            );

            // Hiệu ứng parallax cho hình ảnh khi scroll đến trigger hq-contact-page-introduce
            gsap.utils.toArray(".hq-contact-page-introduce-image img").forEach((image) => {
                gsap.fromTo(
                    image, {
                        y: -70, // Di chuyển lên trên một chút để tạo hiệu ứng parallax
                    }, {
                        y: 70, // Di chuyển xuống dưới khi scroll
                        ease: "none",
                        scrollTrigger: {
                            trigger: ".hq-contact-page-introduce",
                            start: "top bottom",
                            end: "bottom top",
                            scrub: true, // Tạo hiệu ứng parallax mượt mà
                        },
                    }
                );
            });

            // Hiệu ứng bay lên cho .hq-contact-page-introduce-content
            gsap.utils.toArray(".hq-contact-page-introduce-content").forEach((content) => {
                gsap.fromTo(
                    content, {
                        y: 100, // Ban đầu di chuyển xuống
                        opacity: 0, // Ẩn đi
                        willChange: "transform, opacity"
                    }, {
                        y: 0, // Di chuyển về vị trí ban đầu
                        opacity: 1, // Hiện thị hoàn toàn
                        duration: 1, // Thời gian thực hiện hiệu ứng
                        ease: "power3.out", // Hiệu ứng nhanh dần và mượt mà
                        scrollTrigger: {
                            trigger: ".hq-contact-page-introduce",
                            start: "top bottom",
                            end: "bottom top",
                            scrub: true, // Tạo hiệu ứng mượt mà
                        },
                    }
                );
            });
        }
        // trang liên hệ end

        // Tạo hiệu ứng chữ title với SplitType và GSAP - Wait for fonts
        setTimeout(function() {
            if (fontsLoaded || document.readyState === 'complete') {
                initTextAnimations();
            } else {
                // Retry after more time if fonts not loaded
                setTimeout(initTextAnimations, 1000);
            }
        }, 200);

        // hover vào box scrollbar dừng lại
        // Xử lý hover trên phần tử .ql-editor
        // Pause/resume Lenis when hovering scrollable elements (no jQuery needed)
        var scrollableSelectors = [
            '.ql-editor', '.vh-scrollbar', '.select2-results__options',
            '.emojionearea-scroll-area', '.msv-chuong-list-container',
            '.danh-sach-the-loai-chinh-ul', '#modalDanhSachChuong .modal-body'
        ];
        document.addEventListener('mouseenter', function(e) {
            var target = e.target;
            var isScrollable = scrollableSelectors.some(function(sel) {
                return target.matches && target.matches(sel);
            });
            if (isScrollable && typeof lenis !== 'undefined' && lenis) {
                lenis.stop();
            }
        }, true);
        document.addEventListener('mouseleave', function(e) {
            var target = e.target;
            var isScrollable = scrollableSelectors.some(function(sel) {
                return target.matches && target.matches(sel);
            });
            if (isScrollable && typeof lenis !== 'undefined' && lenis) {
                lenis.start();
            }
        }, true);

    });

    // Separate function for text animations to ensure fonts are ready
    function initTextAnimations() {
        try {
            let textTitles = gsap.utils.toArray('.vanhiep-title'); // Tìm tất cả các tiêu đề
            textTitles.forEach((title) => {
                let splitTitle = new SplitType(title, {
                    types: 'chars'
                }); // Tách từng ký tự
                // Tạo hoạt hình cho các ký tự với GSAP và ScrollTrigger
                gsap.to(
                    splitTitle.chars, // Áp dụng cho từng ký tự đã tách
                    {
                        autoAlpha: 1,
                        y: 0,
                        stagger: 0.1, // Thời gian giữa các ký tự
                        rotate: 0,
                        ease: 'power2.out',
                        scrollTrigger: {
                            // markers: true, // Bật marker để debug (có thể tắt sau)
                            trigger: title, // Kích hoạt khi cuộn đến tiêu đề
                            start: 'top 80%', // Bắt đầu khi tiêu đề vào 50% viewport
                        },
                    }
                );
            });
        } catch (error) {
            console.warn('Text animation error:', error);
        }
    }

    function scrollToElement(selector, duration = 3.0) {
        const isMobile = window.matchMedia("(max-width: 768px)").matches; // Kiểm tra nếu là thiết bị di động hoặc tablet
        const element = document.querySelector(selector);

        if (!element) {
            console.warn(`Phần tử với selector "${selector}" không tồn tại.`);
            return;
        }

        if (isMobile) {
            // Cuộn bằng cách sử dụng scrollTo cho mobile và tablet
            const offsetTop = element.offsetTop;
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        } else {
            // Cuộn bằng cách sử dụng Lenis cho PC, Laptop
            if (typeof lenis !== 'undefined') {
                lenis.scrollTo(selector, {
                    duration: duration,
                    offset: -80,
                });
            } else {
                console.warn('Lenis chưa được khởi tạo.');
            }
        }
    }
</script>




<!-- 
<script>
    $(document).ready(function() {
        setTimeout(function() {
           
            let parallax = gsap.utils.toArray(".parallax");
            parallax.forEach((box, key) => {
                var box_parent = $(box).parents(".parallax-box");
                gsap.to(box, {
                    y: '50%',
                    scrollTrigger: {
                        trigger: box_parent,
                        scrub: 1,
                        markers: true,
                        start: "top bottom"
                    }
                })
            });
        }, 1000);


    });
</script> -->

<?php 
global $tehi_tailwind_page;
if (!empty($tehi_tailwind_page)): 
?>
<!-- Inject Tailwind for generated pages only -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
<script src="https://cdn.tailwindcss.com"></script>
<script>
    tailwind.config = {
        theme: {
            extend: {
                colors: {
                    "primary": "#0060a9",
                    "on-primary": "#ffffff",
                    "primary-container": "#d3e3fd",
                    "on-primary-container": "#001c39",
                    "secondary": "#535f70",
                    "on-secondary": "#ffffff",
                    "secondary-container": "#d7e3f8",
                    "on-secondary-container": "#101c2b",
                    "error": "#ba1a1a",
                    "background": "#fdfcff",
                    "on-background": "#1a1c1e",
                    "surface": "#fdfcff",
                    "on-surface": "#1a1c1e",
                    "surface-variant": "#dfe2eb",
                    "on-surface-variant": "#43474e",
                    "outline": "#73777f",
                    "outline-variant": "#c3c6cf",
                    "surface-container-lowest": "#ffffff",
                    "surface-container-low": "#f7f2fa",
                    "surface-container": "#f3edf7",
                    "surface-container-high": "#ece6f0",
                    "surface-container-highest": "#e6e0e9"
                },
                fontFamily: {
                    sans: ['"Be Vietnam Pro"', 'sans-serif'],
                    headline: ['"Be Vietnam Pro"', 'sans-serif']
                }
</script>
<style>
/* Prevent Tailwind from overriding Material Icon font */
.material-symbols-outlined {
  font-family: 'Material Symbols Outlined' !important;
  font-weight: normal !important;
  font-style: normal !important;
  display: inline-block;
  line-height: 1;
  text-transform: none;
  letter-spacing: normal;
  word-wrap: normal;
  white-space: nowrap;
  direction: ltr;
}
</style>
<?php endif; ?>
</head>


<body class="index  position-relative" style="--background-body: url(<?php echo get_template_directory_uri(); ?>/img_data/images/background-repeat-2.png)">
  <!-- <div class="anh-nen lt-truyen-body"></div> -->
  <!-- lenis scroll bar start -->
  <div class="lenis-scrollbar">
    <div class="lenis-scrollbar-thumb"></div>
  </div>
  <!-- lenis scroll bar end -->
  <div id="fui-toast"></div>
  

  

  




<!-- Header Navigation -->

<style>
/* Meokammap Header Styles */
.mkm-header { background: #fff; box-shadow: 0 2px 10px rgba(0,0,0,0.05); position: sticky; top: 0; z-index: 1000; }
.mkm-header-container { max-width: 1200px; margin: 0 auto; padding: 0 15px; display: flex; align-items: center; justify-content: space-between; height: 64px; }
.mkm-logo img { height: 40px; }
.mkm-search-form { flex-grow: 1; max-width: 400px; margin: 0 20px; position: relative; }
.mkm-search-form input { width: 100%; border: 1px solid #e1e4e8; border-radius: 20px; padding: 8px 15px 8px 35px; outline: none; transition: border-color 0.2s; }
.mkm-search-form input:focus { border-color: #1890ff; }
.mkm-search-form i { position: absolute; left: 12px; top: 50%; transform: translateY(-50%); color: #888; }
.mkm-nav { display: flex; align-items: center; gap: 20px; }
.mkm-nav a { color: #333; font-weight: 600; font-size: 14px; text-decoration: none; transition: color 0.2s; }
.mkm-nav a:hover { color: #1890ff; }
.mkm-nav-login { color: #1890ff !important; display: flex; align-items: center; gap: 5px; }

@media (max-width: 768px) {
    .mkm-nav { display: none; }
    .mkm-search-form { display: none; }
}

/* Mobile Menu Styles */
.mkm-mobile-menu {
    display: none;
    background: #fff;
    border-top: 1px solid #f3f4f6;
    padding: 16px;
    box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
    position: absolute;
    top: 64px;
    left: 0;
    right: 0;
    z-index: 999;
}
.mkm-mobile-menu.open {
    display: block;
    animation: slideDown 0.2s ease-out;
}
@keyframes slideDown {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}
.mkm-mobile-search {
    display: flex;
    margin-bottom: 16px;
}
.mkm-mobile-search input {
    flex: 1;
    border: 1px solid #e5e7eb;
    border-radius: 8px 0 0 8px;
    padding: 10px 14px;
    outline: none;
    font-size: 14px;
}
.mkm-mobile-search button {
    background: #4f46e5;
    color: #fff;
    border: none;
    padding: 0 16px;
    border-radius: 0 8px 8px 0;
    cursor: pointer;
}
.mkm-mobile-nav {
    display: flex;
    flex-direction: column;
}
.mkm-mobile-nav a {
    color: #374151;
    font-weight: 600;
    font-size: 15px;
    text-decoration: none;
    padding: 12px 6px;
    border-bottom: 1px dashed #e5e7eb;
}
.mkm-mobile-nav a:last-child {
    border-bottom: none;
}
</style>

<header class="mkm-header">
    <div class="mkm-header-container">
        <!-- Text Logo "DTT" as requested -->
        <a href="<?php echo get_site_url(); ?>" class="mkm-logo" style="text-decoration: none;">
            <span style="font-weight: 900; font-size: 24px; color: #1e1e2d; letter-spacing: -1px;">
                DTT<span style="color: #6366f1;">.</span>
            </span>
        </a>
        
        <form class="mkm-search-form d-none d-md-block hidden md:block" action="<?php echo esc_url(home_url('/')); ?>" method="get">
            <i class="fa-solid fa-search"></i>
            <input type="text" name="s" placeholder="Tìm tên truyện, tên người đăng..">
        </form>
        
        <div class="mkm-nav d-none d-md-flex hidden md:flex">
            <a href="<?php echo get_site_url(); ?>/the-loai.html"><i class="fa-solid fa-list"></i> Thể loại</a>
            <a href="<?php echo get_site_url(); ?>/hoan-thanh.html"><i class="fa-solid fa-check-circle"></i> Truyện full</a>
            <a href="<?php echo get_site_url(); ?>/bang-xep-hang.html"><i class="fa-solid fa-trophy"></i> BXH</a>
            <a href="<?php echo get_site_url(); ?>/theo-doi.html"><i class="fa-solid fa-bookmark"></i> Theo dõi</a>
            <?php if(is_user_logged_in()): ?>
                <a href="<?php echo admin_url('profile.php'); ?>" class="mkm-nav-login"><img src="<?php echo esc_url(get_avatar_url(get_current_user_id())); ?>" style="width:24px;height:24px;border-radius:50%;object-fit:cover;"> Tài khoản</a>
            <?php else: ?>
                <a href="javascript:void(0)" onclick="mkmOpenAuthModal('login')" class="mkm-nav-login"><i class="fa-solid fa-user-circle"></i> Đăng nhập</a>
            <?php endif; ?>
        </div>
        <button id="mkm-mobile-menu-btn" class="btn btn-link d-md-none" onclick="document.getElementById('mkm-mobile-menu').classList.toggle('open')" aria-label="Mở menu" style="background:transparent; border:none; padding:10px; display:flex; align-items:center; justify-content:center;">
            <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#1e1e2d" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="3" y1="6" x2="21" y2="6"/>
                <line x1="3" y1="12" x2="21" y2="12"/>
                <line x1="3" y1="18" x2="21" y2="18"/>
            </svg>
        </button>
    </div>
    
    <!-- Mobile Dropdown Menu -->
    <div id="mkm-mobile-menu" class="mkm-mobile-menu">
        <form class="mkm-mobile-search" action="<?php echo esc_url(home_url('/')); ?>" method="get">
            <input type="text" name="s" placeholder="Tìm tên truyện...">
            <button type="submit"><svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg></button>
        </form>
        <div class="mkm-mobile-nav">
            <a href="<?php echo get_site_url(); ?>/the-loai.html">Thể loại</a>
            <a href="<?php echo get_site_url(); ?>/hoan-thanh.html">Truyện full</a>
            <a href="<?php echo get_site_url(); ?>/bang-xep-hang.html">Bảng xếp hạng</a>
            <a href="<?php echo get_site_url(); ?>/theo-doi.html">Theo dõi</a>
            <?php if(is_user_logged_in()): ?>
                <a href="<?php echo admin_url('profile.php'); ?>" style="color:#4f46e5; display:flex; align-items:center; gap:8px;">
                    <img src="<?php echo esc_url(get_avatar_url(get_current_user_id())); ?>" style="width:28px;height:28px;border-radius:50%;object-fit:cover;"> Tài khoản
                </a>
            <?php else: ?>
                <a href="javascript:void(0)" onclick="mkmOpenAuthModal('login')" style="color:#4f46e5;">Đăng nhập</a>
            <?php endif; ?>
        </div>
    </div>
</header>

