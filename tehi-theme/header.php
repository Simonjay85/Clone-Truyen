
<!DOCTYPE html>
<html lang="vi">

<head>
  <base href="<?php echo get_site_url(); ?>" />
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
</script>  <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- Preload critical Google Fonts for iOS -->
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Arial:wght@400;600;700&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">

<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,100..900;1,100..900&family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Krub:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Roboto:ital,wght@0,100..900;1,100..900&family=Source+Sans+3:ital,wght@0,200..900;1,200..900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="templates/css/bootstrap.min.css">
<link rel="stylesheet" href="templates/css/hover-min.css" />
<link rel="stylesheet" href="templates/module/swiper/swiper.min.css" />
<link rel="stylesheet" href="templates/css/emojionearea.css">
<!-- Lenis -->
<link rel="stylesheet" href="https://unpkg.com/lenis@1.1.14/dist/lenis.css">

<link rel="stylesheet" href="templates/module/fontawesome-free-6.3.0-web/css/all.css">
<link rel="stylesheet" href="templates/module/sweetalert/sweetalert2.min.css">
<link rel="stylesheet" href="assets/css/nice-select.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css" />
<script src="templates/js/jquery.min.js"></script>

<!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" integrity="sha512-1cK78a1o+ht2JcaW6g8OXYwqpev9+6GqOkz9xmBN9iUUhIndKtxwILGWYOSibOKjLsEdjyjZvYDq/cZwNeak0w==" crossorigin="anonymous" referrerpolicy="no-referrer" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js" integrity="sha512-A7AYk1fGKX6S2SsHywmPkrnzTZHrgiVT7GcQkLGDe2ev0aWb8zejytzS8wjo7PGEXKqJOrjQ4oORtnimIRZBtw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script> -->


<!-- emoji -->
<script src="templates/js/emojionearea.js"></script>

<!-- maginify -->
<link rel="stylesheet" href="templates/css/magnify.css">
<script src="templates/js/jquery.magnify.js"></script>

<!-- select2 -->
<link href="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css" rel="stylesheet" />
<script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js"></script>

<!-- fui toast -->
<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/gh/lelinh014756/fui-toast-js@master/assets/css/toast@1.0.1/fuiToast.min.css">
<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/lelinh014756/fui-toast-js@master/assets/js/toast@1.0.1/fuiToast.min.js"></script>

<!-- DOMPURIFY -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/dompurify/2.3.4/purify.min.js"></script>

<!-- scroll mượt -->
<!-- <script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@latest/bundled/lenis.min.js"></script> -->


<script src="https://cdn.jsdelivr.net/npm/@fancyapps/ui@5.0/dist/fancybox/fancybox.umd.js"></script>
<link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/@fancyapps/ui@5.0/dist/fancybox/fancybox.css" />


<!-- swiper -->
<script src="templates/module/swiper/swiper.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>
<link href="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote-lite.min.css" rel="stylesheet">

<!-- style main -->
<link rel="stylesheet" href="templates/css/style.css?ver=1118">
<link rel="stylesheet" href="templates/css/style-mongdaovien.css?ver=1118">
<link rel="stylesheet" href="templates/css/style-truyen-moi-v1.css?ver=1118">
<link rel="stylesheet" href="templates/css/media.css?ver=1118">


<!-- priceformat -->
<script rel="stylesheet" src="admin/public/js/jquery.priceformat.js"></script>


<!-- gsap -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>

<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>

<!-- Thêm Lenis từ CDN -->
<script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.4/bundled/lenis.min.js"></script>
<!-- cắt chữ split type -->
<script src="https://cdn.jsdelivr.net/npm/split-type@0.3.4/umd/index.min.js"></script>


<!-- văn hiệp skeleton -->
<link rel="stylesheet" href="templates/css/vh-skeleton.css">
<script src="templates/js/vh-skeleton.js"></script>



<!-- vanhiep scripts main js -->
<script src="templates/js/vanhiep_script.js"></script>





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
            duration: toc_do, // Thời gian cuộn mượt
            easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), // Easing mượt mà
            smoothWheel: true, // Kích hoạt cuộn mượt với chuột
            smoothTouch: false, // Không mượt trên cảm ứng
        });
        // Vòng lặp cập nhật Lenis
        function raf(time) {
            lenis.raf(time);
            requestAnimationFrame(raf);
        }
        requestAnimationFrame(raf);
        // lenis scroll bar start 
        $(document).ready(function() {
            const scrollbar = $('.lenis-scrollbar');
            let isScrolling;
            $(window).on('scroll', function() {
                scrollbar.addClass('visible');
                clearTimeout(isScrolling);
                isScrolling = setTimeout(function() {
                    scrollbar.removeClass('visible');
                }, 1000);
            });
            scrollbar.hover(
                function() {
                    scrollbar.addClass('visible');
                },
                function() {
                    isScrolling = setTimeout(function() {
                        scrollbar.removeClass('visible');
                    }, 1000);
                }
            );
        });
        const scrollbar = document.querySelector('.lenis-scrollbar');
        const scrollbarThumb = document.querySelector('.lenis-scrollbar-thumb');
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
        // lenis scroll bar end
        // Đồng bộ GSAP với Lenis
        gsap.registerPlugin(ScrollTrigger);
        lenis.on('scroll', ScrollTrigger.update);
        ScrollTrigger.scrollerProxy(document.body, {
            scrollTop(value) {
                return arguments.length ? lenis.scrollTo(value) : lenis.scroll;
            },
            getBoundingClientRect() {
                return {
                    top: 0,
                    left: 0,
                    width: window.innerWidth,
                    height: window.innerHeight,
                };
            },
        });
        console.log('Lenis initialized');
    }

    document.addEventListener("DOMContentLoaded", function() {
        // Initialize fonts first, then other components
        initializeFonts();
        
        // Gọi hàm khởi tạo Lenis lần đầu tiên
        initLenis();

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
        Fancybox.bind("[data-fancybox]", {
            // Your custom options
        });

        // Khởi tạo skeletons
        initializeVHSkeleton();
        initializeSkeletonOnScroll();

        // Kiểm tra vị trí cuộn và hiển thị hoặc ẩn nút "Back to Top"
        $('body').append('<div id="toTop"><i class="fa-solid fa-chevron-up"></i></div> ');
        $('#toTop').fadeOut();
        $(window).scroll(function() {
            if ($(this).scrollTop() > 500) {
                $('#toTop').fadeIn();
            } else {
                $('#toTop').fadeOut();
            }
        });
        // Handle "Back to Top" button click
        $('#toTop').click(function() {
            scrollToElement('body', 1.2);
            return false;
        });



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
        $(document).on('mouseenter', '.ql-editor , .vh-scrollbar, .select2-results__options, .emojionearea-scroll-area, .emojionearea .emojionearea-editor, .mdv-charts-box-content-item-content, .msv-chuong-list-container, .danh-sach-the-loai-chinh-ul, .tim-kiem-thanh-vien-result, #modalDanhSachChuong .modal-dialog-scrollable .modal-body', function() {
            // Khi hover vào, hủy bỏ Lenis scroll
            if (typeof lenis !== 'undefined' && lenis) {
                lenis.destroy();
                console.log('Lenis destroyed on hover');
            }
        });

        $(document).on('mouseleave', '.ql-editor, .vh-scrollbar, .select2-results__options, .emojionearea-scroll-area, .emojionearea .emojionearea-editor, .mdv-charts-box-content-item-content, .msv-chuong-list-container, .danh-sach-the-loai-chinh-ul, .tim-kiem-thanh-vien-result, #modalDanhSachChuong .modal-dialog-scrollable .modal-body', function() {
            // Khi mouseout, khởi tạo lại Lenis scroll
            if (typeof initLenis === 'function') {
                initLenis();
                console.log('Lenis re-initialized on mouseout');
            }
        });

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
</head>


<body class="index  position-relative" style="--background-body: url(<?php echo get_site_url(); ?>/img_data/images/background-repeat-2.png)">
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
</style>

<header class="mkm-header">
    <div class="mkm-header-container">
        <a href="<?php echo get_site_url(); ?>" class="mkm-logo">
            <img src="<?php echo get_site_url(); ?>/img_data/images/logo-truyen-moi-v1.png" alt="Logo">
        </a>
        
        <div class="mkm-search-form d-none d-md-block">
            <i class="fa-solid fa-search"></i>
            <input type="text" placeholder="Tìm tên truyện, tên người đăng..">
        </div>
        
        <div class="mkm-nav d-none d-md-flex">
            <a href="<?php echo get_site_url(); ?>/the-loai.html"><i class="fa-solid fa-list"></i> Thể loại</a>
            <a href="<?php echo get_site_url(); ?>/hoan-thanh.html"><i class="fa-solid fa-check-circle"></i> Truyện full</a>
            <a href="<?php echo get_site_url(); ?>/bang-xep-hang.html"><i class="fa-solid fa-트로피"></i> BXH</a>
            <a href="<?php echo get_site_url(); ?>/theo-doi.html"><i class="fa-solid fa-bookmark"></i> Theo dõi</a>
            <a href="<?php echo get_site_url(); ?>/dang-nhap" class="mkm-nav-login"><i class="fa-solid fa-user-circle"></i> Đăng nhập</a>
        </div>
        <!-- Mobile Toggle -->
        <button class="btn btn-link d-md-none text-dark">
            <i class="fa-solid fa-bars fs-3"></i>
        </button>
    </div>
</header>

