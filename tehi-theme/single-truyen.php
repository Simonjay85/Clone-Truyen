<?php get_header(); ?>
<?php if (have_posts()) : while (have_posts()) : the_post(); ?>


<!-- result search mobile form start -->
<div class="mdv-header-find-form mdv-header-find-form-mobile p-2">
    <!-- input search -->
    <input type="text" class="text-search-mobile mb-2" placeholder="Tìm kiếm truyện...">
    <!-- result -->
    <ul class="vanhiep-ul d-flex flex-column gap-1 mdv-header-find-form-ul vh-scrollbar" id="result-tim-kiem-mobile">
        <!-- item start -->
        <!--  -->

        <!-- item end -->
    </ul>
</div>

<!-- result search mobile form end -->

<!-- Mobile Navigation Menu (Off-canvas) -->
<div class="truyen-mobile-nav" id="mobileNav">
    <div class="truyen-mobile-nav-header">
        <button class="truyen-mobile-close" id="mobileClose">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                width="38"
                height="38"
                fill="currentColor"
                class="bi bi-x"
                viewBox="0 0 16 16">
                <path
                    d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z" />
            </svg>
        </button>
    </div>

    <ul class="truyen-mobile-nav-list">
                    <li class="truyen-mobile-nav-item">
                <a href="https://tehitruyen.com/truyen-de-cu.html">Truyện đề cử</a>
            </li>
                    <li class="truyen-mobile-nav-item">
                <a href="https://tehitruyen.com/truyen-moi-cap-nhat.html">Truyện mới cập nhật</a>
            </li>
                    <li class="truyen-mobile-nav-item">
                <a href="https://tehitruyen.com/the-loai.html">Thể loại</a>
            </li>
                    <li class="truyen-mobile-nav-item">
                <a href="https://tehitruyen.com/hoan-thanh.html">Truyện hoàn thành</a>
            </li>
                    <li class="truyen-mobile-nav-item">
                <a href="https://tehitruyen.com/team.html">Team</a>
            </li>
                    <li class="truyen-mobile-nav-item">
                <a href="https://tehitruyen.com/tu-truyen.html">Tủ truyện</a>
            </li>
        

        <!-- profile -->
                <!-- admin dashboard -->
        
    </ul>



</div>

<!-- overlay -->
<div class="truyen-overlay"></div>

<script>
    if (localStorage.getItem('dark-mode') == 'true') {
        $('body').addClass('dark-mode');
        $('.btn-dark-mode-toggle').html('<i class="fa-solid fa-sun"></i>');
    }
    $(document).ready(function() {

        // dark mode toggle
        $('.btn-dark-mode-toggle').on('click', function() {
            $('body').toggleClass('dark-mode');
            // change icon
            // change background color
            // nếu có class mode thì button này khi click trở về icon ban đầu
            if ($('body').hasClass('dark-mode')) {
                $(this).html('<i class="fa-solid fa-sun"></i>');

                $(this).css('transform', 'rotate(360deg)');
                localStorage.setItem('dark-mode', 'true');
            } else {
                $(this).html('<i class="fa-solid fa-moon"></i>');

                $(this).css('transform', 'rotate(0deg)');
                localStorage.setItem('dark-mode', 'false');
            }
            $(this).css('transition', 'all 0.5s ease');

            // rotate icon

            // transition
        });

        // Mobile Menu Toggle
        $("#menuToggle").on("click", () => {
            openMobileMenu();
        });

        $("#mobileClose").on("click", () => {
            closeMobileMenu();
        });

        // Create overlay element
        $("body").append('<div class="truyen-overlay"></div>');

        // Close menu when clicking overlay
        $(".truyen-overlay").on("click", () => {
            closeMobileMenu();
        });

        function openMobileMenu() {
            // Use GSAP for animation
            gsap.to(".truyen-mobile-nav", {
                left: 0,
                duration: 0.3,
                ease: "power2.out",
            });

            // Animate menu items
            gsap.fromTo(
                ".truyen-mobile-nav-item", {
                    opacity: 0,
                    x: -20,
                }, {
                    opacity: 1,
                    x: 0,
                    stagger: 0.05,
                    duration: 0.5,
                    delay: 0.2,
                    ease: "power2.out",
                }
            );

            $(".truyen-overlay").addClass("active");
            $("body").css("overflow", "hidden");
        }

        function closeMobileMenu() {
            gsap.to(".truyen-mobile-nav", {
                left: -280,
                duration: 0.3,
                ease: "power2.in",
            });

            $(".truyen-overlay").removeClass("active");
            $("body").css("overflow", "");
        }
    });
</script>



<script>
    $(document).ready(function() {
        // Logout confirmation
        $('.logout-link').click(function(e) {
            e.preventDefault(); // Prevent default link behavior

            Swal.fire({
                title: 'Bạn có chắc chắn muốn đăng xuất?',
                text: "Bạn sẽ cần đăng nhập lại để truy cập vào tài khoản!",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Đồng ý',
                cancelButtonText: 'Hủy bỏ'
            }).then((result) => {
                if (result.isConfirmed) {
                    // Redirect to the logout URL
                    window.location.href = "https://tehitruyen.com/dang-xuat";
                }
            });
        });


        // TÌM KIẾM START
        if (window.innerWidth > 1024) {
            let typingTimer; // Timer để kiểm soát thời gian chờ
            const debounceTime = 700; // Thời gian chờ (ms)
            const $inputSearch = $('.truyen-search-input'); // Trường input tìm kiếm
            const $resultContainer = $('#result-tim-kiem'); // Kết quả tìm kiếm
            const $resultContainerBox = $('.mdv-header-find-form-pc');
            let currentKeyword = ''; // Biến lưu từ khóa tìm kiếm hiện tại

            // focus addclass overplay active
            $inputSearch.focus(function() {
                $('.truyen-overlay').addClass('active');
            });

            // blur removeclass overplay active
            $inputSearch.blur(function() {
                $('.truyen-overlay').removeClass('active');
            });

            // Xử lý nút "Xem thêm" cho desktop
            $(document).on('click', '.mdv-header-find-form-pc .load-more-results', function(e) {
                e.preventDefault();
                const $btn = $(this);
                const nextPage = parseInt($btn.data('page'));
                const keyword = currentKeyword;

                $btn.html('<i class="fas fa-spinner fa-spin"></i> Đang tải...').prop('disabled', true);

                $.ajax({
                    url: 'sources/ajax/mongdaovien/tim-kiem-truyen.php',
                    type: 'POST',
                    dataType: 'json',
                    data: {
                        keyword: keyword,
                        page: nextPage
                    },
                    success: function(response) {
                        if (response.status === 'success') {
                            // Xóa nút "Xem thêm" cũ
                            $('.mdv-header-find-form-pc .search-load-more').remove();

                            // Thêm kết quả mới
                            $resultContainer.append(response.html);

                            // Cập nhật trạng thái
                            if (!response.has_more) {
                                $('.mdv-header-find-form-pc .search-load-more').remove();
                            }
                        }
                    },
                    error: function() {
                        $btn.html('Xem thêm kết quả <i class="fas fa-chevron-down"></i>').prop('disabled', false);
                        alert('Đã xảy ra lỗi, vui lòng thử lại!');
                    }
                });
            });

            // Lắng nghe sự kiện nhập liệu
            $inputSearch.on('input', function() {
                clearTimeout(typingTimer);
                currentKeyword = $(this).val().trim(); // Cập nhật từ khóa hiện tại
                $resultContainer.fadeOut('fast', function() {
                    $resultContainer.html('<div class="text-center"><div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div></div>').fadeIn('fast');
                });
                typingTimer = setTimeout(function() {
                    if (currentKeyword.length > 0) {
                        $resultContainerBox.addClass('active');
                        $resultContainerBox.fadeIn('fast');
                        searchTruyen(currentKeyword);
                    } else {
                        $resultContainer.fadeOut('fast', function() {
                            $resultContainer.empty();
                        });

                        $resultContainerBox.removeClass('active').fadeOut('fast', function() {
                            $resultContainer.empty();
                        });
                    }
                }, debounceTime);
            });

            function searchTruyen(query) {
                $.ajax({
                    url: 'sources/ajax/mongdaovien/tim-kiem-truyen.php',
                    type: 'POST',
                    dataType: 'json',
                    data: {
                        keyword: query,
                        page: 1
                    },
                    success: function(response) {
                        if (response.status === 'success') {
                            $resultContainer.fadeOut('fast', function() {
                                $resultContainer.html(response.html).fadeIn('fast');
                            });
                        } else {
                            $resultContainer.fadeOut('fast', function() {
                                $resultContainer.html('<li class="p-2 text-center text-muted">Không tìm thấy kết quả nào!</li>').fadeIn('fast');
                            });
                        }
                    },
                    error: function() {
                        $resultContainer.fadeOut('fast', function() {
                            $resultContainer.html('<li class="p-2 text-center text-danger">Lỗi khi tải dữ liệu, vui lòng thử lại!</li>').fadeIn('fast');
                        });
                    }
                });
            }
        } else {
            // Mobile search handling
            let currentKeyword = ''; // Biến lưu từ khóa tìm kiếm hiện tại cho mobile

            $(document).on('click', '.truyen-search-mobile-btn', function() {
                const $searchBox = $('.mdv-header-find-form-mobile');

                if ($searchBox.hasClass('active')) {
                    // Đóng box tìm kiếm
                    $searchBox.addClass('hide-results');
                    $('.truyen-overlay').removeClass('active');
                    $('body').removeClass('overflow-hidden');
                    setTimeout(() => {
                        $searchBox.removeClass('active');
                    }, 300);
                } else {
                    // Mở box tìm kiếm
                    $searchBox.removeClass('hide-results').addClass('active').css('display', 'block');
                    $('.truyen-overlay').addClass('active');
                    $('body').addClass('overflow-hidden');
                    setTimeout(() => {
                        $('.text-search-mobile').focus();
                    }, 100);
                }
            });

            // Xử lý nút "Xem thêm" cho mobile
            $(document).on('click', '.mdv-header-find-form-mobile .load-more-results', function(e) {
                e.preventDefault();
                const $btn = $(this);
                const nextPage = parseInt($btn.data('page'));
                const keyword = currentKeyword;

                $btn.html('<i class="fas fa-spinner fa-spin"></i> Đang tải...').prop('disabled', true);

                $.ajax({
                    url: 'sources/ajax/mongdaovien/tim-kiem-truyen.php',
                    type: 'POST',
                    dataType: 'json',
                    data: {
                        keyword: keyword,
                        page: nextPage
                    },
                    success: function(response) {
                        if (response.status === 'success') {
                            // Xóa nút "Xem thêm" cũ
                            $('.mdv-header-find-form-mobile .search-load-more').remove();

                            // Thêm kết quả mới
                            $('#result-tim-kiem-mobile').append(response.html);

                            // Cập nhật trạng thái
                            if (!response.has_more) {
                                $('.mdv-header-find-form-mobile .search-load-more').remove();
                            }
                        }
                    },
                    error: function() {
                        $btn.html('Xem thêm kết quả <i class="fas fa-chevron-down"></i>').prop('disabled', false);
                        alert('Đã xảy ra lỗi, vui lòng thử lại!');
                    }
                });
            });

            // Đóng form tìm kiếm khi click vào overlay
            $(document).on('click', '.truyen-overlay', function() {
                const $searchBox = $('.mdv-header-find-form-mobile');
                $searchBox.addClass('hide-results');
                $('.truyen-overlay').removeClass('active');
                $('body').removeClass('overflow-hidden');
                setTimeout(() => {
                    $searchBox.removeClass('active');
                }, 300);
            });

            // Xử lý tìm kiếm trên mobile
            let typingTimer;
            const debounceTime = 700;
            const $inputSearch = $('.text-search-mobile');
            const $resultContainer = $('#result-tim-kiem-mobile');

            $inputSearch.on('input', function() {
                clearTimeout(typingTimer);
                currentKeyword = $(this).val().trim(); // Cập nhật từ khóa hiện tại
                $resultContainer.html('<div class="text-center py-4"><div class="spinner-border text-primary" role="status"><span class="visually-hidden">Đang tìm kiếm...</span></div></div>');

                typingTimer = setTimeout(function() {
                    if (currentKeyword.length > 0) {
                        searchTruyen(currentKeyword);
                    } else {
                        $resultContainer.html('<div class="text-center py-4 text-muted">Nhập từ khóa để tìm kiếm...</div>');
                    }
                }, debounceTime);
            });

            function searchTruyen(query) {
                $.ajax({
                    url: 'sources/ajax/mongdaovien/tim-kiem-truyen.php',
                    type: 'POST',
                    dataType: 'json',
                    data: {
                        keyword: query,
                        page: 1
                    },
                    success: function(response) {
                        if (response.status === 'success') {
                            $resultContainer.html(response.html);
                        } else {
                            $resultContainer.html('<div class="text-center py-4 text-muted">Không tìm thấy kết quả nào!</div>');
                        }
                    },
                    error: function() {
                        $resultContainer.html('<div class="text-center py-4 text-danger">Đã xảy ra lỗi, vui lòng thử lại!</div>');
                    }
                });
            }
        }

        // TÌM KIẾM END


        $(document).ready(function() {
            if (window.innerWidth > 1024) {
                const header = document.querySelector(".truyen-header");
                // header top height
                const headerTopHeight = document.querySelector(".truyen-header-top");
                const headerHeight = header.offsetHeight;
                window.addEventListener("scroll", function() {
                    if (window.scrollY > headerHeight) {
                        header.classList.add("active");
                        header.style.transform = "translateY(-" + (headerTopHeight.offsetHeight + 2) + "px)";
                        header.style.transition = "all 0.5s ease-in-out";
                    } else {
                        header.classList.remove("active");
                        header.style.transform = "translateY(0px)";
                        header.style.transition = "all 0.5s ease-in-out";
                    }
                });

            } else {
                const header = document.querySelector(".truyen-header");
                const headerHeight = header.offsetHeight;
                window.addEventListener("scroll", function() {
                    if (window.scrollY > headerHeight) {
                        header.classList.add("active");
                        header.style.transition = "all 0.5s ease-in-out";
                    } else {
                        header.classList.remove("active");
                        header.style.transition = "all 0.5s ease-in-out";
                    }
                });
            }

        });

        // HÀM CẬP NHẬT SỐ THÔNG BÁO CHƯA ĐỌC TRONG HEADER
        function updateHeaderNotificationCount() {
            $.ajax({
                url: "sources/ajax/mongdaovien/cap-nhat-so-thong-bao-header.php",
                type: "POST",
                dataType: "json",
                success: function(response) {
                    if (response.status === "success") {
                        const $countElement = $('.so-thong-bao-cua-doc');
                        const $countContainer = $('.truyen-notification-item-count');

                        if (response.unreadCount > 0) {
                            $countElement.text(response.displayCount);
                            $countContainer.show();
                        } else {
                            $countContainer.hide();
                        }
                    }
                },
                error: function() {
                    console.error("Không thể cập nhật số thông báo header.");
                }
            });
        }

        // Tự động cập nhật số thông báo mỗi 30 giây nếu đã đăng nhập
        
    });
</script>  <!-- Menu mobi start -->
    <!-- Menu mobile end -->
  
  <div class="wrapper wrapper-detail">
    
<section class="mdv-san-pham-show">
    <div class="container">

        <!-- THÔNG TIN TRUYỆN START -->
        <div class="mdv-san-pham-show-thong-tin-truyen-wrapper p-0 p-lg-4 mb-5 mb-lg-4">
            <div class="row gy-4 justify-content-center">
                <div class="col-12 col-lg-9">
                    <div class="mdv-san-pham-show-thong-tin-truyen-item px-4 py-3">
                        <div class="row gy-3">
                            <!-- hình truyện -->
                            <div class="col-12 col-lg-4">
                                <div class="mdv-san-pham-show-thong-tin-truyen-hinh-truyen">
                                    <div class="san-pham-book-item">
                                        <div class="san-pham-book-item-show position-relative">
                                            <div class="san-pham-book-item-show-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/img_data/images/anh_truyen/2436.jpg" data-fancybox>
                                                    <div class="vh-skeleton vh-skeleton-image"></div>
                                                    <img src="https://tehitruyen.com/img_data/images/anh_truyen/2436.jpg" alt="ảnh">
                                                </a>
                                            </div>
                                        </div>

                                    </div>
                                </div>
                            </div>
                            <!-- nội dung truyện -->
                            <div class="col-12 col-lg-8">
                                <div class="mdv-san-pham-show-thong-tin-truyen-noi-dung-truyen">
                                    <div class="ps-lg-3">
                                        <div class="san-pham-show-content">
                                            <!-- tên start -->
                                            <div class="vh-skeleton-container">
                                                <div class="mdv-san-pham-show-name mb-2">
                                                    <?php the_title(); ?></div>
                                                <div class="vh-skeleton vh-skeleton-text"></div>
                                            </div>

                                            <!-- tên end -->


                                            

                                            <!-- thông tin start -->
                                            <div class="mdv-san-pham-comic-info">
                                                <table class="tm-thong-tin-truyen-table">
                                                    <tbody>
                                                        <!-- tác giả -->
                                                        <tr>
                                                            <td>
                                                                <span class="fw-bold">Tác Giả:</span>
                                                            </td>
                                                            <td>
                                                                <div class="mdv-sps-tac-gia">
                                                                    <a class="tac-gia-ten" href="https://tehitruyen.com/tac-gia/dang-cap-nhat">Đang cập nhật</a>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                        <!-- chuyển ngữ -->
                                                        <tr>
                                                            <td>
                                                                <span class="fw-bold">Chuyển Ngữ:</span>
                                                            </td>
                                                            <td>
                                                                <span class="chuyen-ngu-name-text"><a href="https://tehitruyen.com/my-wall/huyenlenh94">Lớp Trưởng</a></span>
                                                            </td>
                                                        </tr>
                                                        <!-- tình trạng -->
                                                        <tr>
                                                            <td>
                                                                <span class="fw-bold">Tình Trạng:</span>
                                                            </td>
                                                            <td>
                                                                 <span class="thong-tin-tinh-trang-text badge bg-success text-light">Hoàn Thành</span>                                                            </td>
                                                        </tr>
                                                        <!-- lượt xem -->
                                                        <tr>
                                                            <td>
                                                                <span class="fw-bold">Lượt Xem:</span>
                                                            </td>
                                                            <td>
                                                                                                                                <span class="san-pham-read-text">387</span>
                                                            </td>
                                                        </tr>
                                                        <!-- lượt thích -->
                                                        <tr>
                                                            <td>
                                                                <span class="fw-bold">Lượt Thích:</span>
                                                            </td>
                                                            <td>
                                                                                                                                <span class="san-pham-read-text">0</span>
                                                            </td>
                                                        </tr>
                                                        <!-- chương mới nhất -->
                                                        <tr>
                                                            <td>
                                                                <span class="fw-bold">Chương mới nhất:</span>
                                                            </td>
                                                            <td>
                                                                                                                                <span class="san-pham-read-text">9</span>
                                                            </td>
                                                        </tr>
                                                        <!-- độ dài -->
                                                        <tr>
                                                            <td>
                                                                <span class="fw-bold">Độ dài:</span>
                                                            </td>
                                                            <td>
                                                                <span class="san-pham-read-text">Đang cập nhật</span>
                                                            </td>
                                                        </tr>
                                                        <!-- lịch đăng -->
                                                        <tr>
                                                            <td>
                                                                <span class="fw-bold">Lịch đăng:</span>
                                                            </td>
                                                            <td>
                                                                <span class="san-pham-read-text">Đang cập nhật</span>
                                                            </td>
                                                        </tr>
                                                        <!-- thể loại -->
                                                        <tr>
                                                            <td>
                                                                <span class="fw-bold">Thể Loại:</span>
                                                            </td>

                                                        </tr>
                                                        <tr>
                                                            <td colspan="2">
                                                                <ul class="san-pham-the-loai vanhiep-ul d-inline-flex flex-wrap align-items-center gap-1 mb-2 position-relative collapsed-the-loai">
                                                                                                                                            <!-- item start -->
                                                                        <li class="san-pham-the-loai-item">

                                                                            <a class="px-2 px-lg-3 py-1 d-inline-flex btn-hover-shine" href="https://tehitruyen.com/the-loai/ngon-tinh">Ngôn tình</a>

                                                                        </li>
                                                                        <!-- item end  -->
                                                                                                                                            <!-- item start -->
                                                                        <li class="san-pham-the-loai-item">

                                                                            <a class="px-2 px-lg-3 py-1 d-inline-flex btn-hover-shine" href="https://tehitruyen.com/the-loai/co-dai">Cổ Đại</a>

                                                                        </li>
                                                                        <!-- item end  -->
                                                                                                                                        <div class="san-pham-the-loai-bg"></div>
                                                                </ul>
                                                            </td>
                                                        </tr>
                                                    </tbody>

                                                </table>



                                                <!-- Báo cáo và copy truyện start -->
                                                <div class="san-pham-show-report-link d-flex justify-content-center justify-content-lg-start align-items-center mt-2">
                                                    <div class="san-pham-show-report me-2">
                                                        <div class="vh-skeleton-container">
                                                            <i class="fa-solid fa-triangle-exclamation"></i> <span class="hvr-underline-from-left">Báo lỗi truyện</span>
                                                            <div class="vh-skeleton vh-skeleton-text"></div>
                                                        </div>
                                                    </div>

                                                    <div class="san-pham-show-link hvr-icon-pulse-grow" data-link="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html" title="Copy link truyện">
                                                        <div class="vh-skeleton-container">
                                                            <i class="hvr-icon fa-solid fa-link"></i> <span>Chia sẻ</span>
                                                            <div class="vh-skeleton vh-skeleton-text"></div>
                                                        </div>
                                                    </div>
                                                </div>


                                                <!-- Đọc tiếp start -->
                                                <div class="san-pham-show-read-next d-flex justify-content-center justify-content-lg-start flex-wrap gap-2 align-items-center mt-3">
                                                                                                        <!-- theo dõi truyện -->



                                                    <!-- Đọc truyện -->
                                                    <div class="san-pham-show-read-next-btn">
                                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=1">
                                                            <div class="vh-skeleton-container">
                                                                <div class="btn-comic-read-next hvr-icon-pop btn-mdv-button-2">
                                                                    <img src="https://tehitruyen.com/templates/images/open-book-white.png" alt="icon" class="icon-doc-truyen-spshow"> Đọc Truyện
                                                                </div>
                                                                <div class="vh-skeleton vh-skeleton-text"></div>
                                                            </div>
                                                        </a>
                                                    </div>
                                                    <!-- Đọc tiếp -->
                                                    <div class="san-pham-show-read-next-btn btn-doc-tiep">
                                                        <div class="vh-skeleton-container">
                                                            <button class="btn-comic-read-next hvr-icon-pop btn-mdv-button-2">
                                                                <i class="fa-solid fa-eye hvr-icon"></i> Đọc tiếp
                                                            </button>
                                                            <div class="vh-skeleton vh-skeleton-text"></div>
                                                        </div>
                                                    </div>

                                                    <!-- thêm 2 button yêu thích và theo dõi -->
                                                                                                        <div class="san-pham-show-read-next-btn">
                                                        <button class="btn-comic-read-next hvr-icon-pop btn-mdv-button-2 btn-yeu-thich-truyen " data-id="2436">
                                                            <i class="fa-solid fa-heart hvr-icon "></i> Yêu thích                                                        </button>
                                                    </div>

                                                    <!-- check theo dõi -->
                                                                                                            <div class="san-pham-show-read-next-btn">
                                                            <a>
                                                                <div class="btn-comic-read-next hvr-icon-pop btn-mdv-button-2 btn-theo-doi-truyen bo-theo-doi">
                                                                    <i class="fa-solid fa-thumbtack"></i> Theo dõi truyện
                                                                </div>
                                                            </a>
                                                        </div>
                                                    
                                                    <!-- Sửa truyện start -->
                                                                                                        <!-- Sửa truyện end -->

                                                </div>
                                                <!-- Đọc tiếp end -->
                                            </div>
                                            <!-- thông tin end -->
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>

                </div>

            </div>
        </div>


        <!-- THÔNG TIN TRUYỆN END -->

        <!-- GIỚI THIỆU TRUYỆN - THÔNG BÁO TÁC GIẢ START -->
        <div class="mdv-sps-gioi-thieu-truyen-tb-tac-gia-wrapper mb-5 mb-lg-5">
            <div class="row">
                <div class="col-12 col-lg-12 ">
                    <div class="mdv-sps-gioi-thieu-truyen-box px-3 px-lg-5 pb-3 pt-3">
                        <!-- title start -->
                        <div class="bee-gioi-thieu-truyen-title-box position-relative text-center ">
                            <div class="bee-gioi-thieu-truyen-title text-uppercase px-3 py-2 rounded-pill">
                                Giới Thiệu
                            </div>
                        </div>
                        <!-- title end -->
                        <div class="mdv-sps-gioi-thieu-truyen-content ">
                            <div class="mdv-san-pham-show-gioi-thieu ">

                                <div class="vh-skeleton-container ">
                                    <div class="mdv-san-pham-show-gioi-thieu-des catchuoi5 collapsed-gioi-thieu position-relative">
                                        <p>VẢ MẶT TRA NAM BÔM BỐP ĐÃ CÁI NƯ LUÔN NÀ HẸ HẸ HẸ</p>
<p>Ta cải nam trang vào quân doanh, vô tình cứu được Tiêu Càn từ đống x.á.c c.h.e.t trở về.</p>
<p>Trong tiệc khánh công, bệ hạ hỏi hắn muốn được ban thưởng gì.</p>
<p>Hắn vì muốn cưới công chúa, liền dùng kiếm hất tung lớp vải bó ngực của ta.</p>
<p>Trước mặt mọi người vạch trần thân phận nữ nhi của ta.</p>
<p>"Nàng khi quân phạm thượng, nay vừa hay có thể thay công chúa gả đến biên tái, coi như chuộc tội lập công."</p>
<p>Ta bị giam trong ngục tối, xiềng xích xuyên qua xương bả vai.</p>
<p>Công chúa mỉm cười nghiền nát xương ngón tay của ta, thả chuột cắn nuốt da thịt ta.</p>
<p>"Dù sao cũng là ngươi cứu Tiêu lang, mới thúc đẩy được mối lương duyên của hắn và ta."</p>
<p>"Bản cung từ bi nhân hậu, đây là thưởng cho ngươi, coi như tạ lễ."</p>
<p>Mùa xuân năm sau, Tiêu Càn cưới công chúa, thăng quan tiến chức, quyền khuynh triều dã.</p>
<p>Còn ta chịu hết nhục nhã, c.h.e.t thảm trong chuồng dê nơi biên tái.</p>
<p>Trở lại một đời, ta quay về ngày bị Tiêu Càn vạch trần thân phận.</p>                                        <div class="san-pham-the-loai-bg"></div>
                                    </div>
                                    <div class="vh-skeleton vh-skeleton-text"></div>
                                </div>
                                <!-- nút xem thêm -->
                                <div class="text-center">
                                    <button type="button" class="btn-xs btn-xem-them">
                                        <div class="vh-skeleton-container ">
                                            Xem thêm
                                            <div class="vh-skeleton vh-skeleton-text"></div>
                                        </div>
                                    </button>

                                </div>

                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
        <!-- GIỚI THIỆU TRUYỆN - THÔNG BÁO TÁC GIẢ END -->


        <!-- danh sách chương START -->
        <div class="mvd-san-pham-show-danh-sach-chuong px-3 px-lg-5 pt-3 pb-3 mb-5 mb-lg-4">
            <div class="">
                <div class="bee-gioi-thieu-truyen-title-box position-relative text-center ">
                    <div class="bee-gioi-thieu-truyen-title text-uppercase px-3 py-2 rounded-pill">
                        Mục Lục
                    </div>
                </div>
                <!-- content start -->
                                <div class="mvd-san-pham-show-dsc-content">
                    <div class="mvd-san-pham-show-dsc-content-box">
                        <div class="row row-cols-2 row-cols-lg-2 gx-4 gy-3">
                                                                <!-- item start -->
                                    <div class="mvd-san-pham-show-dsc-content-item">
                                        <div class="row row-cols-1 row-cols-lg-2">
                                            <div class="col">
                                                <div class="mdv-san-pham-show-dsc-table-chuong-box d-flex flex-column align-items-center">
                                                    <div class="mdv-san-pham-show-dsc-table-chuong">
                                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=1">
                                                            Chương 1                                                        </a>
                                                    </div>
                                                    <div class="mdv-san-pham-show-dsc-table-date d-block d-md-none">
                                                        <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col d-none d-md-block">
                                                <div>
                                                    <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- item end -->
                                                                    <!-- item start -->
                                    <div class="mvd-san-pham-show-dsc-content-item">
                                        <div class="row row-cols-1 row-cols-lg-2">
                                            <div class="col">
                                                <div class="mdv-san-pham-show-dsc-table-chuong-box d-flex flex-column align-items-center">
                                                    <div class="mdv-san-pham-show-dsc-table-chuong">
                                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=2">
                                                            Chương 2                                                        </a>
                                                    </div>
                                                    <div class="mdv-san-pham-show-dsc-table-date d-block d-md-none">
                                                        <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col d-none d-md-block">
                                                <div>
                                                    <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- item end -->
                                                                    <!-- item start -->
                                    <div class="mvd-san-pham-show-dsc-content-item">
                                        <div class="row row-cols-1 row-cols-lg-2">
                                            <div class="col">
                                                <div class="mdv-san-pham-show-dsc-table-chuong-box d-flex flex-column align-items-center">
                                                    <div class="mdv-san-pham-show-dsc-table-chuong">
                                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=3">
                                                            Chương 3                                                        </a>
                                                    </div>
                                                    <div class="mdv-san-pham-show-dsc-table-date d-block d-md-none">
                                                        <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col d-none d-md-block">
                                                <div>
                                                    <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- item end -->
                                                                    <!-- item start -->
                                    <div class="mvd-san-pham-show-dsc-content-item">
                                        <div class="row row-cols-1 row-cols-lg-2">
                                            <div class="col">
                                                <div class="mdv-san-pham-show-dsc-table-chuong-box d-flex flex-column align-items-center">
                                                    <div class="mdv-san-pham-show-dsc-table-chuong">
                                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=4">
                                                            Chương 4                                                        </a>
                                                    </div>
                                                    <div class="mdv-san-pham-show-dsc-table-date d-block d-md-none">
                                                        <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col d-none d-md-block">
                                                <div>
                                                    <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- item end -->
                                                                    <!-- item start -->
                                    <div class="mvd-san-pham-show-dsc-content-item">
                                        <div class="row row-cols-1 row-cols-lg-2">
                                            <div class="col">
                                                <div class="mdv-san-pham-show-dsc-table-chuong-box d-flex flex-column align-items-center">
                                                    <div class="mdv-san-pham-show-dsc-table-chuong">
                                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=5">
                                                            Chương 5                                                        </a>
                                                    </div>
                                                    <div class="mdv-san-pham-show-dsc-table-date d-block d-md-none">
                                                        <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col d-none d-md-block">
                                                <div>
                                                    <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- item end -->
                                                                    <!-- item start -->
                                    <div class="mvd-san-pham-show-dsc-content-item">
                                        <div class="row row-cols-1 row-cols-lg-2">
                                            <div class="col">
                                                <div class="mdv-san-pham-show-dsc-table-chuong-box d-flex flex-column align-items-center">
                                                    <div class="mdv-san-pham-show-dsc-table-chuong">
                                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=6">
                                                            Chương 6                                                        </a>
                                                    </div>
                                                    <div class="mdv-san-pham-show-dsc-table-date d-block d-md-none">
                                                        <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col d-none d-md-block">
                                                <div>
                                                    <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- item end -->
                                                                    <!-- item start -->
                                    <div class="mvd-san-pham-show-dsc-content-item">
                                        <div class="row row-cols-1 row-cols-lg-2">
                                            <div class="col">
                                                <div class="mdv-san-pham-show-dsc-table-chuong-box d-flex flex-column align-items-center">
                                                    <div class="mdv-san-pham-show-dsc-table-chuong">
                                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=7">
                                                            Chương 7                                                        </a>
                                                    </div>
                                                    <div class="mdv-san-pham-show-dsc-table-date d-block d-md-none">
                                                        <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col d-none d-md-block">
                                                <div>
                                                    <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- item end -->
                                                                    <!-- item start -->
                                    <div class="mvd-san-pham-show-dsc-content-item">
                                        <div class="row row-cols-1 row-cols-lg-2">
                                            <div class="col">
                                                <div class="mdv-san-pham-show-dsc-table-chuong-box d-flex flex-column align-items-center">
                                                    <div class="mdv-san-pham-show-dsc-table-chuong">
                                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=8">
                                                            Chương 8                                                        </a>
                                                    </div>
                                                    <div class="mdv-san-pham-show-dsc-table-date d-block d-md-none">
                                                        <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col d-none d-md-block">
                                                <div>
                                                    <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- item end -->
                                                                    <!-- item start -->
                                    <div class="mvd-san-pham-show-dsc-content-item">
                                        <div class="row row-cols-1 row-cols-lg-2">
                                            <div class="col">
                                                <div class="mdv-san-pham-show-dsc-table-chuong-box d-flex flex-column align-items-center">
                                                    <div class="mdv-san-pham-show-dsc-table-chuong">
                                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=9">
                                                            Chương 9                                                        </a>
                                                    </div>
                                                    <div class="mdv-san-pham-show-dsc-table-date d-block d-md-none">
                                                        <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col d-none d-md-block">
                                                <div>
                                                    <span class="thoi-gian-xuat-ban-time">10/04/2026</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- item end -->
                                                        </div>
                    </div>

                    <!-- content end -->
                </div>


            </div>



        </div>
        <!-- danh sách chương END -->



        <!-- bình luận start -->
        <div class="mdv-san-pham-show-comment pt-0 pt-lg-4">


            <!-- content start -->
            <div class="mdv-san-pham-show-comment-box px-3 px-lg-5 pt-0 pb-3">
                                <!-- title start -->
                <div class="bee-gioi-thieu-truyen-title-box position-relative text-center ">
                    <div class="bee-gioi-thieu-truyen-title text-uppercase px-3 py-2 rounded-pill">
                        Bình Luận (<span class="bl-number">0</span>)
                    </div>
                </div>
                <!-- title end -->


                <!-- bình luận form -->
                <div class="row mb-3">
                    <div class="col-12 col-lg-12">
                        <div class="mdv-san-pham-show-comment-form">
                                                            <!-- nếu chưa đăng nhập -->
                                                                <div class="mdv-san-pham-show-binh-luan-chua-dang-nhap p-4 text-center">
                                    <div class="comment-login-prompt mb-3">
                                        <h5 class="mb-2">Chia sẻ cảm nghĩ của bạn nhé!</h5>
                                        <p class="mb-4">Vui lòng đăng nhập để tham gia bình luận cùng chúng mình 💗</p>
                                        <button type="button" class="btn btn-pink-login" onclick="window.location.href='https://tehitruyen.com/dang-nhap.html' ">
                                            Đăng Nhập Ngay
                                        </button>
                                    </div>
                                </div>


                                                    </div>
                    </div>
                </div>
                <!-- bình luận form -->

                <!-- list bình luận start -->
                <div class="mdv-san-pham-show-comment-box-list ">
                    <div class="row">
                        <div class="col-12 col-lg-12">
                            <div class="mdv-san-pham-show-comment-list-box pt-3">
                                <div class="row row-cols-1 gy-3 gy-lg-4" id="result-binh-luan">

                                    <!-- kiểm tra xem đã đăng nhập chưa và có bình luận đang chờ không start -->
                                                                        <!-- kiểm tra xem đã đăng nhập chưa và có bình luận đang chờ không end -->

                                                                            <div class="vh-notification text-center p-3 fs-6">
                                            Truyện này chưa có bình luận nào
                                        </div>
                                    
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- list bình luận end -->
                </div>
                <!-- content end -->
            </div>
            <!-- bình luận end -->

        </div>
</section>


<!-- Modal xem lượt thích -->
<div class="modal fade modal-danh-sach-thich" id="listMemberLike" tabindex="-1" aria-labelledby="listMemberLikeLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">

            <div class="modal-body">
                <div class="modal-danh-sach-thich-box">
                    <div class="fs-5 mb-2">Danh sách yêu thích</div>
                    <div class="modal-danh-sach-thich-content w-100 px-3">
                        <div class="row row-cols-1 gy-1">
                                                            <!-- item start -->
                                <div class="col">
                                    <div class="modal-danh-sach-thich-content-item d-flex align-items-center justify-content-between gap-3">
                                        <!-- avatar -->
                                        <div class="modal-danh-sach-thich-content-item-avatar d-inline-flex align-items-center gap-2">
                                            <div class="mdv-san-pham-show-comment-form-avatar modal-danh-sach-thich-content-item-avatar-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/templates/images/meo.png" data-fancybox>
                                                    <img src="https://tehitruyen.com/templates/images/meo.png" alt="png" class="avatar">
                                                </a>
                                                <img src="https://tehitruyen.com/templates/images/s3.webp" alt="khung avatar" class="frame">
                                            </div>
                                            <!-- tên -->
                                            <div class="modal-danh-sach-thich-content-item-name">
                                                <a href="" class="ten-doc-gia">Vladimir Putin</a>
                                            </div>
                                        </div>
                                        <!-- theo doõi -->
                                        <button class="btn btn-theo-doi-tv hvr-icon-bounce"><i class="hvr-icon fa-solid fa-user-plus"></i></button>
                                    </div>
                                </div>
                                <!-- item end -->
                                                            <!-- item start -->
                                <div class="col">
                                    <div class="modal-danh-sach-thich-content-item d-flex align-items-center justify-content-between gap-3">
                                        <!-- avatar -->
                                        <div class="modal-danh-sach-thich-content-item-avatar d-inline-flex align-items-center gap-2">
                                            <div class="mdv-san-pham-show-comment-form-avatar modal-danh-sach-thich-content-item-avatar-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/templates/images/meo.png" data-fancybox>
                                                    <img src="https://tehitruyen.com/templates/images/meo.png" alt="png" class="avatar">
                                                </a>
                                                <img src="https://tehitruyen.com/templates/images/s3.webp" alt="khung avatar" class="frame">
                                            </div>
                                            <!-- tên -->
                                            <div class="modal-danh-sach-thich-content-item-name">
                                                <a href="" class="ten-doc-gia">Vladimir Putin</a>
                                            </div>
                                        </div>
                                        <!-- theo doõi -->
                                        <button class="btn btn-theo-doi-tv hvr-icon-bounce"><i class="hvr-icon fa-solid fa-user-plus"></i></button>
                                    </div>
                                </div>
                                <!-- item end -->
                                                            <!-- item start -->
                                <div class="col">
                                    <div class="modal-danh-sach-thich-content-item d-flex align-items-center justify-content-between gap-3">
                                        <!-- avatar -->
                                        <div class="modal-danh-sach-thich-content-item-avatar d-inline-flex align-items-center gap-2">
                                            <div class="mdv-san-pham-show-comment-form-avatar modal-danh-sach-thich-content-item-avatar-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/templates/images/meo.png" data-fancybox>
                                                    <img src="https://tehitruyen.com/templates/images/meo.png" alt="png" class="avatar">
                                                </a>
                                                <img src="https://tehitruyen.com/templates/images/s3.webp" alt="khung avatar" class="frame">
                                            </div>
                                            <!-- tên -->
                                            <div class="modal-danh-sach-thich-content-item-name">
                                                <a href="" class="ten-doc-gia">Vladimir Putin</a>
                                            </div>
                                        </div>
                                        <!-- theo doõi -->
                                        <button class="btn btn-theo-doi-tv hvr-icon-bounce"><i class="hvr-icon fa-solid fa-user-plus"></i></button>
                                    </div>
                                </div>
                                <!-- item end -->
                                                            <!-- item start -->
                                <div class="col">
                                    <div class="modal-danh-sach-thich-content-item d-flex align-items-center justify-content-between gap-3">
                                        <!-- avatar -->
                                        <div class="modal-danh-sach-thich-content-item-avatar d-inline-flex align-items-center gap-2">
                                            <div class="mdv-san-pham-show-comment-form-avatar modal-danh-sach-thich-content-item-avatar-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/templates/images/meo.png" data-fancybox>
                                                    <img src="https://tehitruyen.com/templates/images/meo.png" alt="png" class="avatar">
                                                </a>
                                                <img src="https://tehitruyen.com/templates/images/s3.webp" alt="khung avatar" class="frame">
                                            </div>
                                            <!-- tên -->
                                            <div class="modal-danh-sach-thich-content-item-name">
                                                <a href="" class="ten-doc-gia">Vladimir Putin</a>
                                            </div>
                                        </div>
                                        <!-- theo doõi -->
                                        <button class="btn btn-theo-doi-tv hvr-icon-bounce"><i class="hvr-icon fa-solid fa-user-plus"></i></button>
                                    </div>
                                </div>
                                <!-- item end -->
                                                            <!-- item start -->
                                <div class="col">
                                    <div class="modal-danh-sach-thich-content-item d-flex align-items-center justify-content-between gap-3">
                                        <!-- avatar -->
                                        <div class="modal-danh-sach-thich-content-item-avatar d-inline-flex align-items-center gap-2">
                                            <div class="mdv-san-pham-show-comment-form-avatar modal-danh-sach-thich-content-item-avatar-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/templates/images/meo.png" data-fancybox>
                                                    <img src="https://tehitruyen.com/templates/images/meo.png" alt="png" class="avatar">
                                                </a>
                                                <img src="https://tehitruyen.com/templates/images/s3.webp" alt="khung avatar" class="frame">
                                            </div>
                                            <!-- tên -->
                                            <div class="modal-danh-sach-thich-content-item-name">
                                                <a href="" class="ten-doc-gia">Vladimir Putin</a>
                                            </div>
                                        </div>
                                        <!-- theo doõi -->
                                        <button class="btn btn-theo-doi-tv hvr-icon-bounce"><i class="hvr-icon fa-solid fa-user-plus"></i></button>
                                    </div>
                                </div>
                                <!-- item end -->
                                                            <!-- item start -->
                                <div class="col">
                                    <div class="modal-danh-sach-thich-content-item d-flex align-items-center justify-content-between gap-3">
                                        <!-- avatar -->
                                        <div class="modal-danh-sach-thich-content-item-avatar d-inline-flex align-items-center gap-2">
                                            <div class="mdv-san-pham-show-comment-form-avatar modal-danh-sach-thich-content-item-avatar-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/templates/images/meo.png" data-fancybox>
                                                    <img src="https://tehitruyen.com/templates/images/meo.png" alt="png" class="avatar">
                                                </a>
                                                <img src="https://tehitruyen.com/templates/images/s3.webp" alt="khung avatar" class="frame">
                                            </div>
                                            <!-- tên -->
                                            <div class="modal-danh-sach-thich-content-item-name">
                                                <a href="" class="ten-doc-gia">Vladimir Putin</a>
                                            </div>
                                        </div>
                                        <!-- theo doõi -->
                                        <button class="btn btn-theo-doi-tv hvr-icon-bounce"><i class="hvr-icon fa-solid fa-user-plus"></i></button>
                                    </div>
                                </div>
                                <!-- item end -->
                                                            <!-- item start -->
                                <div class="col">
                                    <div class="modal-danh-sach-thich-content-item d-flex align-items-center justify-content-between gap-3">
                                        <!-- avatar -->
                                        <div class="modal-danh-sach-thich-content-item-avatar d-inline-flex align-items-center gap-2">
                                            <div class="mdv-san-pham-show-comment-form-avatar modal-danh-sach-thich-content-item-avatar-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/templates/images/meo.png" data-fancybox>
                                                    <img src="https://tehitruyen.com/templates/images/meo.png" alt="png" class="avatar">
                                                </a>
                                                <img src="https://tehitruyen.com/templates/images/s3.webp" alt="khung avatar" class="frame">
                                            </div>
                                            <!-- tên -->
                                            <div class="modal-danh-sach-thich-content-item-name">
                                                <a href="" class="ten-doc-gia">Vladimir Putin</a>
                                            </div>
                                        </div>
                                        <!-- theo doõi -->
                                        <button class="btn btn-theo-doi-tv hvr-icon-bounce"><i class="hvr-icon fa-solid fa-user-plus"></i></button>
                                    </div>
                                </div>
                                <!-- item end -->
                                                            <!-- item start -->
                                <div class="col">
                                    <div class="modal-danh-sach-thich-content-item d-flex align-items-center justify-content-between gap-3">
                                        <!-- avatar -->
                                        <div class="modal-danh-sach-thich-content-item-avatar d-inline-flex align-items-center gap-2">
                                            <div class="mdv-san-pham-show-comment-form-avatar modal-danh-sach-thich-content-item-avatar-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/templates/images/meo.png" data-fancybox>
                                                    <img src="https://tehitruyen.com/templates/images/meo.png" alt="png" class="avatar">
                                                </a>
                                                <img src="https://tehitruyen.com/templates/images/s3.webp" alt="khung avatar" class="frame">
                                            </div>
                                            <!-- tên -->
                                            <div class="modal-danh-sach-thich-content-item-name">
                                                <a href="" class="ten-doc-gia">Vladimir Putin</a>
                                            </div>
                                        </div>
                                        <!-- theo doõi -->
                                        <button class="btn btn-theo-doi-tv hvr-icon-bounce"><i class="hvr-icon fa-solid fa-user-plus"></i></button>
                                    </div>
                                </div>
                                <!-- item end -->
                                                            <!-- item start -->
                                <div class="col">
                                    <div class="modal-danh-sach-thich-content-item d-flex align-items-center justify-content-between gap-3">
                                        <!-- avatar -->
                                        <div class="modal-danh-sach-thich-content-item-avatar d-inline-flex align-items-center gap-2">
                                            <div class="mdv-san-pham-show-comment-form-avatar modal-danh-sach-thich-content-item-avatar-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/templates/images/meo.png" data-fancybox>
                                                    <img src="https://tehitruyen.com/templates/images/meo.png" alt="png" class="avatar">
                                                </a>
                                                <img src="https://tehitruyen.com/templates/images/s3.webp" alt="khung avatar" class="frame">
                                            </div>
                                            <!-- tên -->
                                            <div class="modal-danh-sach-thich-content-item-name">
                                                <a href="" class="ten-doc-gia">Vladimir Putin</a>
                                            </div>
                                        </div>
                                        <!-- theo doõi -->
                                        <button class="btn btn-theo-doi-tv hvr-icon-bounce"><i class="hvr-icon fa-solid fa-user-plus"></i></button>
                                    </div>
                                </div>
                                <!-- item end -->
                                                            <!-- item start -->
                                <div class="col">
                                    <div class="modal-danh-sach-thich-content-item d-flex align-items-center justify-content-between gap-3">
                                        <!-- avatar -->
                                        <div class="modal-danh-sach-thich-content-item-avatar d-inline-flex align-items-center gap-2">
                                            <div class="mdv-san-pham-show-comment-form-avatar modal-danh-sach-thich-content-item-avatar-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/templates/images/meo.png" data-fancybox>
                                                    <img src="https://tehitruyen.com/templates/images/meo.png" alt="png" class="avatar">
                                                </a>
                                                <img src="https://tehitruyen.com/templates/images/s3.webp" alt="khung avatar" class="frame">
                                            </div>
                                            <!-- tên -->
                                            <div class="modal-danh-sach-thich-content-item-name">
                                                <a href="" class="ten-doc-gia">Vladimir Putin</a>
                                            </div>
                                        </div>
                                        <!-- theo doõi -->
                                        <button class="btn btn-theo-doi-tv hvr-icon-bounce"><i class="hvr-icon fa-solid fa-user-plus"></i></button>
                                    </div>
                                </div>
                                <!-- item end -->
                                                            <!-- item start -->
                                <div class="col">
                                    <div class="modal-danh-sach-thich-content-item d-flex align-items-center justify-content-between gap-3">
                                        <!-- avatar -->
                                        <div class="modal-danh-sach-thich-content-item-avatar d-inline-flex align-items-center gap-2">
                                            <div class="mdv-san-pham-show-comment-form-avatar modal-danh-sach-thich-content-item-avatar-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/templates/images/meo.png" data-fancybox>
                                                    <img src="https://tehitruyen.com/templates/images/meo.png" alt="png" class="avatar">
                                                </a>
                                                <img src="https://tehitruyen.com/templates/images/s3.webp" alt="khung avatar" class="frame">
                                            </div>
                                            <!-- tên -->
                                            <div class="modal-danh-sach-thich-content-item-name">
                                                <a href="" class="ten-doc-gia">Vladimir Putin</a>
                                            </div>
                                        </div>
                                        <!-- theo doõi -->
                                        <button class="btn btn-theo-doi-tv hvr-icon-bounce"><i class="hvr-icon fa-solid fa-user-plus"></i></button>
                                    </div>
                                </div>
                                <!-- item end -->
                                                            <!-- item start -->
                                <div class="col">
                                    <div class="modal-danh-sach-thich-content-item d-flex align-items-center justify-content-between gap-3">
                                        <!-- avatar -->
                                        <div class="modal-danh-sach-thich-content-item-avatar d-inline-flex align-items-center gap-2">
                                            <div class="mdv-san-pham-show-comment-form-avatar modal-danh-sach-thich-content-item-avatar-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/templates/images/meo.png" data-fancybox>
                                                    <img src="https://tehitruyen.com/templates/images/meo.png" alt="png" class="avatar">
                                                </a>
                                                <img src="https://tehitruyen.com/templates/images/s3.webp" alt="khung avatar" class="frame">
                                            </div>
                                            <!-- tên -->
                                            <div class="modal-danh-sach-thich-content-item-name">
                                                <a href="" class="ten-doc-gia">Vladimir Putin</a>
                                            </div>
                                        </div>
                                        <!-- theo doõi -->
                                        <button class="btn btn-theo-doi-tv hvr-icon-bounce"><i class="hvr-icon fa-solid fa-user-plus"></i></button>
                                    </div>
                                </div>
                                <!-- item end -->
                                                            <!-- item start -->
                                <div class="col">
                                    <div class="modal-danh-sach-thich-content-item d-flex align-items-center justify-content-between gap-3">
                                        <!-- avatar -->
                                        <div class="modal-danh-sach-thich-content-item-avatar d-inline-flex align-items-center gap-2">
                                            <div class="mdv-san-pham-show-comment-form-avatar modal-danh-sach-thich-content-item-avatar-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/templates/images/meo.png" data-fancybox>
                                                    <img src="https://tehitruyen.com/templates/images/meo.png" alt="png" class="avatar">
                                                </a>
                                                <img src="https://tehitruyen.com/templates/images/s3.webp" alt="khung avatar" class="frame">
                                            </div>
                                            <!-- tên -->
                                            <div class="modal-danh-sach-thich-content-item-name">
                                                <a href="" class="ten-doc-gia">Vladimir Putin</a>
                                            </div>
                                        </div>
                                        <!-- theo doõi -->
                                        <button class="btn btn-theo-doi-tv hvr-icon-bounce"><i class="hvr-icon fa-solid fa-user-plus"></i></button>
                                    </div>
                                </div>
                                <!-- item end -->
                                                            <!-- item start -->
                                <div class="col">
                                    <div class="modal-danh-sach-thich-content-item d-flex align-items-center justify-content-between gap-3">
                                        <!-- avatar -->
                                        <div class="modal-danh-sach-thich-content-item-avatar d-inline-flex align-items-center gap-2">
                                            <div class="mdv-san-pham-show-comment-form-avatar modal-danh-sach-thich-content-item-avatar-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/templates/images/meo.png" data-fancybox>
                                                    <img src="https://tehitruyen.com/templates/images/meo.png" alt="png" class="avatar">
                                                </a>
                                                <img src="https://tehitruyen.com/templates/images/s3.webp" alt="khung avatar" class="frame">
                                            </div>
                                            <!-- tên -->
                                            <div class="modal-danh-sach-thich-content-item-name">
                                                <a href="" class="ten-doc-gia">Vladimir Putin</a>
                                            </div>
                                        </div>
                                        <!-- theo doõi -->
                                        <button class="btn btn-theo-doi-tv hvr-icon-bounce"><i class="hvr-icon fa-solid fa-user-plus"></i></button>
                                    </div>
                                </div>
                                <!-- item end -->
                                                            <!-- item start -->
                                <div class="col">
                                    <div class="modal-danh-sach-thich-content-item d-flex align-items-center justify-content-between gap-3">
                                        <!-- avatar -->
                                        <div class="modal-danh-sach-thich-content-item-avatar d-inline-flex align-items-center gap-2">
                                            <div class="mdv-san-pham-show-comment-form-avatar modal-danh-sach-thich-content-item-avatar-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/templates/images/meo.png" data-fancybox>
                                                    <img src="https://tehitruyen.com/templates/images/meo.png" alt="png" class="avatar">
                                                </a>
                                                <img src="https://tehitruyen.com/templates/images/s3.webp" alt="khung avatar" class="frame">
                                            </div>
                                            <!-- tên -->
                                            <div class="modal-danh-sach-thich-content-item-name">
                                                <a href="" class="ten-doc-gia">Vladimir Putin</a>
                                            </div>
                                        </div>
                                        <!-- theo doõi -->
                                        <button class="btn btn-theo-doi-tv hvr-icon-bounce"><i class="hvr-icon fa-solid fa-user-plus"></i></button>
                                    </div>
                                </div>
                                <!-- item end -->
                            
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Đóng lại</button>
            </div>
        </div>
    </div>
</div>



<!-- Modal hiển thị danh sách các chương được chọn -->
<div class="modal fade mua-chuong-modal" data-bs-backdrop="static" id="muaChuongModal" tabindex="-1" aria-labelledby="muaChuongModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content mua-chuong-modal-content">
            <div class="modal-header mua-chuong-modal-header">
                <h5 class="modal-title mua-chuong-modal-title" id="muaChuongModalLabel">Danh sách chương đã chọn</h5>
                <button type="button" class="btn-close mua-chuong-modal-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body mua-chuong-modal-body">
                <ul id="danhSachChuongDaChon" class="list-group mua-chuong-list-group mb-4"></ul>
                <div class="mua-chuong-summary">
                    <p>Tổng số chương: <span id="tongSoChuong" class="fw-bold"></span></p>
                    <p>Tổng giá <img src="https://tehitruyen.com/templates/images/dao-nho.png" alt="icon" class="icon-qua-dao-chuong">: <span id="tongGiaDao" class="fw-bold"></span></p>
                    <p>Tổng giá <img src="https://tehitruyen.com/templates/images/hat.png" alt="icon" class="icon-hat">: <span id="tongGiaHat" class="fw-bold"></span></p>
                </div>
            </div>
            <div class="modal-footer mua-chuong-modal-footer">
                <button type="button" class="btn btn-secondary mua-chuong-btn-cancel" data-bs-dismiss="modal">Hủy bỏ</button>
                <button type="button" class="btn btn-conteiner btn-primary mua-chuong-btn-pay">Thanh Toán</button>
            </div>
        </div>
    </div>
</div>

<!-- Modal Donate Đào -->
<div class="modal fade donate-modal" data-bs-backdrop="static" id="donateModal" tabindex="-1" aria-labelledby="donateModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content donate-modal-content">
            <div class="modal-header donate-modal-header">
                <h5 class="modal-title donate-modal-title" id="donateModalLabel">Donate Đào</h5>
                <button type="button" class="btn-close donate-modal-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body donate-modal-body">
                <p class="donate-modal-info">Bạn đang donate cho: <strong>Lớp Trưởng ( huyenlenh94 )</strong></p>
                <p class="donate-modal-info">Số đào hiện có của bạn: <strong><span id="so_dao_hien_co"></span> <img src="https://tehitruyen.com/templates/images/icon-qua-dao.png" alt="icon" class="icon-qua-dao"></strong></p>
                <div class="mb-3">
                    <label for="soDaoDonate" class="form-label">Nhập số đào <img src="https://tehitruyen.com/templates/images/icon-qua-dao.png" alt="icon" class="icon-qua-dao"> muốn donate</label>
                    <input type="text" class="form-control formatprice" id="soDaoDonate" min="1" max="" placeholder="Nhập số đào...">
                </div>
                <p class="donate-modal-remaining">Sau khi donate, số đào còn lại của bạn sẽ là: <span id="soDaoConLai"></span> <img src="https://tehitruyen.com/templates/images/icon-qua-dao.png" alt="icon" class="icon-qua-dao"></p>
            </div>
            <div class="modal-footer donate-modal-footer">
                <button type="button" class="btn btn-secondary donate-btn-cancel" data-bs-dismiss="modal">Hủy bỏ</button>
                <button type="button" class="btn btn-primary donate-btn-confirm">Donate</button>
            </div>
        </div>
    </div>
</div>


<!-- Mua Combo Modal Popup -->
<div class="modal fade" id="comboPurchaseModal" tabindex="-1" aria-labelledby="comboPurchaseModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content combo-modal-content">

            <div class="modal-body">
                                <div class="combo-purchase-form-container">
                                            <div class="combo-purchase-card">
                            <p class="combo-description">Khi mua combo, bạn sẽ sở hữ toàn bộ chương của truyện này.</p>

                            <div class="combo-info-section">
                                <div class="combo-info-row">
                                    <label for="gia-dao-hien-tai" class="combo-label">Đào Hiện Có:</label>
                                    <div type="text" id="gia-dao-hien-tai" class="combo-input" readonly>
                                         <img src="https://tehitruyen.com/templates/images/icon-qua-dao.png" alt="icon" class="dao-up-top-icon">
                                    </div>
                                </div>
                                <div class="combo-info-row">
                                    <label for="gia-dao-tieu-ton" class="combo-label">Giá Đào Tiêu Tốn:</label>
                                    <div type="text" id="gia-dao-tieu-ton" class="combo-input" readonly>
                                        - 0 <img src="https://tehitruyen.com/templates/images/icon-qua-dao.png" alt="icon" class="dao-up-top-icon">
                                    </div>
                                </div>
                                <div class="combo-info-row">
                                    <label for="gia-dao-sau-mua" class="combo-label">Đào Sau Khi Mua:</label>
                                    <div type="text" id="gia-dao-sau-mua" class="combo-input" readonly>
                                        Không đủ Đào <img src="https://tehitruyen.com/templates/images/icon-qua-dao.png" alt="icon" class="dao-up-top-icon">
                                    </div>
                                </div>
                            </div>

                            <div class="combo-action-section">
                                <button class="btn combo-buy-button"><i class="fa-solid fa-cart-shopping"></i> Mua Combo Ngay</button>
                            </div>
                        </div>
                                    </div>
            </div>
        </div>
    </div>
</div>


<!-- Modal đề cử bông -->
<div class="modal fade" id="deCuTruyenModal" tabindex="-1" aria-labelledby="deCuTruyenModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content combo-purchase-card p-4 rounded-md" style="background-color: #fff0f5; border-radius: 15px; border: 1px solid rgb(255, 182, 193);">
            <div class="modal-header border-0">
                <h5 class="modal-title" id="deCuTruyenModalLabel">Đề Cử Truyện</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                                <!-- Notification box -->
                <div class="alert alert-danger d-flex align-items-start gap-2 p-3 mb-4 mdv-de-cu-info-box" role="alert">
                    <i class="fa-solid fa-circle-info pt-1"></i>
                    <span>
                                            </span>
                </div>


                <form id="deCuTruyenForm">
                                        <!-- Input Group for "Bông" -->
                    <div class="mb-3 d-flex align-items-center gap-2">
                        <label class="mdv-de-cu-icon" for="soBongInput">
                            <img src="templates/images/icon-hoa.png" alt="icon" class="de-cu-bong-icon">
                            <span class="text-bong">Bông</span>
                        </label>
                        <input type="text" class="form-control mdv-de-cu-input formatprice" id="soBongInput" min="0" placeholder="Nhập số lượng muốn đề cử, tối thiểu 5000">
                    </div>

                    <!-- Display current "Bông" -->
                    <div class="mb-3 d-flex align-items-center gap-2">
                        <label class="mdv-de-cu-icon" for="currentBong"><img src="templates/images/icon-hoa.png" alt="icon" class="de-cu-bong-icon"> Hiện tại</label>
                        <input type="text" class="form-control mdv-de-cu-input" id="currentBong" value=" Bông" readonly disabled>
                    </div>

                    <!-- Display "Bông" after proposal -->
                    <div class="mb-3 d-flex align-items-center gap-2">
                        <label class="mdv-de-cu-icon" for="afterProposal"><img src="templates/images/icon-hoa.png" alt="icon" class="de-cu-bong-icon"> Sau đề cử</label>
                        <input type="text" class="form-control mdv-de-cu-input" id="afterProposal" value="0 Bông" readonly disabled>
                    </div>

                    <!-- Submit Button -->
                    <div class="text-center">
                        <button type="button" class="btn mdv-de-cu-submit-btn hvr-shrink"><img src="templates/images/icon-hoa.png" alt="icon" class="icon-hoa-nho"> Đề Cử Ngay</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<!-- giới hạn độ tuổi start -->

<!-- giới hạn độ tuổi end -->


<!-- Modal chỉnh sửa thông báo -->
<div class="modal fade" id="editThongBaoModal" tabindex="-1" aria-labelledby="editThongBaoModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="editThongBaoModalLabel">Chỉnh sửa Thông Báo</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <div class="edit-content-comment">
                    <textarea id="emojioneareaThongBao" style="display: none;"></textarea>
                    <div id="emojioneareaWrapper"></div>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Hủy</button>
                <button type="button" class="btn btn-primary" id="saveThongBaoBtn">Lưu</button>
            </div>
        </div>
    </div>
</div>



<!-- Modal Báo lỗi truyện -->
<div class="modal fade" id="baoLoiModal" tabindex="-1" aria-labelledby="baoLoiModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content modal-content-pretty">
            <div class="modal-header modal-header-pretty">
                <h5 class="modal-title" id="baoLoiModalLabel">Báo Lỗi Truyện</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body modal-body-pretty">
                <form id="baoCaoTruyenForm">
                    <input type="hidden" name="id_truyen" value="2436">
                    <input type="hidden" name="pnvn_token" value="ab5cf4c804c2e6605e9571de598f2f6248e61e99">
                    <input type="hidden" name="ten_Truyen" value="Triều Đình Không Dung Nữ Nhân? Ta Là Ngoại Lệ">
                    <input type="hidden" name="link_Truyen" value="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html">
                    <div class="mb-3">
                        <label for="tenTruyen" class="form-label">Tên Truyện</label>
                        <input type="text" class="form-control form-control-pretty" id="tenTruyen" value="Triều Đình Không Dung Nữ Nhân? Ta Là Ngoại Lệ" disabled>
                    </div>
                    <div class="mb-3">
                        <label for="linkTruyen" class="form-label">Link Truyện</label>
                        <input type="hidden" name="link_Truyen" value="https://tehitruyen.com:443/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html">
                        <input type="text" class="form-control form-control-pretty" id="linkTruyen" value="https://tehitruyen.com:443/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html" readonly>
                    </div>
                    <div class="mb-3">
                        <label for="noiDung" class="form-label">Nội dung lời nhắn</label>
                        <textarea class="form-control form-control-pretty" id="noiDung" name="noi_dung" rows="4" placeholder="Nhập nội dung lỗi truyện..." required></textarea>
                    </div>
                    <div class="modal-footer text-center">
                        <button type="submit" class="btn btn-primary btn-primary-pretty">Gửi Báo Cáo</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<!-- Báo cáo và copy truyện end -->


<!-- Modal Thông Báo Đọc Tiếp -->
<div class="modal-doc-tiep-wrapper" style="display: none;">
    <div class="modal-doc-tiep-backdrop"></div>
    <div class="modal-doc-tiep-content">
        <div class="modal-doc-tiep-header">
            <h3 class="modal-doc-tiep-title">Thông báo</h3>
            <button class="modal-doc-tiep-close">&times;</button>
        </div>
        <div class="modal-doc-tiep-body">
            <p class="modal-doc-tiep-message">
                Bạn đã đọc đến <span class="modal-doc-tiep-chapter fw-bold">Chương 1</span>. Bạn muốn đọc tiếp hay đọc lại từ đầu?
            </p>
        </div>
        <div class="modal-doc-tiep-footer gap-3">
            <button class="btn-mdv px-3 py-2 rounded-pill modal-doc-tiep-read-continue">Đọc tiếp</button>
            <button class="btn-mdv bg-danger px-3 py-2 rounded-pill modal-doc-tiep-read-start-over">Đọc từ đầu</button>
        </div>
    </div>
</div>


<!-- MỘNG ĐÀO VIÊN -->
<!-- Include Clipboard.js CDN -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.10/clipboard.min.js"></script>

<script>
    $(document).ready(function() {
        khoiTaoToolTip();
        const mdv_header_height = $(".mdv-header").outerHeight();
        const mdv_header_mobile_height = $(".mdv-menu-mobile").outerHeight();

        var parent_code = '193';
        $(".menu-code-" + parent_code).addClass('active');

        // emoji
        if (window.innerWidth > 1024) {
            $("#emojionearea").emojioneArea({
                pickerPosition: "top",
                filtersPosition: "bottom",
                tonesStyle: "square",
                placeholder: "Nhận xét..."
            });
            $(".emojionearea-rep").emojioneArea({
                pickerPosition: "top",
                filtersPosition: "bottom",
                tonesStyle: "square",
                placeholder: "Trả lời..."
            });
        } else {
            $("#emojionearea").emojioneArea({
                pickerPosition: "top",
                filtersPosition: "bottom",
                tonesStyle: "square",
                placeholder: "Nhận xét..."
            });
            $(".emojionearea-rep").emojioneArea({
                pickerPosition: "top",
                filtersPosition: "bottom",
                tonesStyle: "square",
                placeholder: "Trả lời..."
            });
        }


        // theo dõi truyện start

        $('.btn-theo-doi-truyen').on('click', function() {
            const button = $(this);
            const id_truyen = 2436;
            const id_user = null;

            if (id_user == null) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Bạn cần đăng nhập để sử dụng tính năng này!',
                });
                return;
            }

            if (button.hasClass('theo-doi')) {
                // Nếu đang theo dõi => Hiển thị xác nhận bỏ theo dõi
                Swal.fire({
                    title: 'Bạn có chắc chắn muốn bỏ theo dõi?',
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonText: 'Bỏ theo dõi',
                    cancelButtonText: 'Hủy',
                }).then((result) => {
                    if (result.isConfirmed) {
                        // Gọi ajax để xóa khỏi tủ truyện
                        $.ajax({
                            url: 'sources/ajax/mongdaovien/theo-doi-truyen.php',
                            type: 'POST',
                            dataType: 'json',
                            data: {
                                id_truyen: id_truyen,
                                id_user: id_user
                            },
                            success: function(response) {
                                if (response.status === 'success') {
                                    button.removeClass('theo-doi').addClass('bo-theo-doi');
                                    button.html('<i class="fa-solid fa-thumbtack"></i> Theo dõi truyện');
                                    Swal.fire('Bỏ theo dõi thành công!', '', 'success');
                                } else {
                                    Swal.fire('Có lỗi xảy ra!', response.message || 'Vui lòng thử lại sau.', 'error');
                                }
                            },
                            error: function() {
                                Swal.fire('Có lỗi xảy ra!', 'Vui lòng thử lại sau.', 'error');
                            }
                        });
                    }
                });

            } else {
                // Nếu chưa theo dõi => Hiển thị thông báo theo dõi
                Swal.fire({
                    title: 'Theo dõi truyện này?',
                    text: 'Truyện này sẽ được lưu vào Tủ Truyện, sẽ thông báo cho bạn khi có chương mới',
                    icon: 'info',
                    showCancelButton: true,
                    confirmButtonText: 'Theo dõi',
                    cancelButtonText: 'Hủy',
                }).then((result) => {
                    if (result.isConfirmed) {
                        // Gọi ajax để thêm vào tủ truyện
                        $.ajax({
                            url: 'sources/ajax/mongdaovien/theo-doi-truyen.php',
                            type: 'POST',
                            dataType: 'json',
                            data: {
                                id_truyen: id_truyen,
                                id_user: id_user,
                                time: Math.floor(Date.now() / 1000),
                                thong_bao: 1
                            },
                            success: function(response) {
                                if (response.status === 'success') {
                                    button.removeClass('bo-theo-doi').addClass('theo-doi');
                                    button.html('<i class="fa-solid fa-xmark me-1"></i> Bỏ theo dõi');
                                    Swal.fire('Theo dõi thành công!', '', 'success');
                                } else {
                                    Swal.fire('Có lỗi xảy ra!', response.message || 'Vui lòng thử lại sau.', 'error');
                                }
                            },
                            error: function() {
                                Swal.fire('Có lỗi xảy ra!', 'Vui lòng thử lại sau.', 'error');
                            }
                        });
                    }
                });
            }
        });
        // theo dõi truyện end

        // đề cử truyện start
        // Example: Updating the 'Sau đề cử' field when input changes
        // Định dạng giá trị nhập vào bằng thư viện priceFormat
        $('.formatprice').priceFormat({
            limit: 8,
            prefix: '',
            centsLimit: 0
        });

        // Hàm định dạng số thành số có dấu phẩy
        function number_format(number) {
            return new Intl.NumberFormat('vi-VN').format(number);
        }

        // Xử lý khi người dùng nhập vào số bông muốn đề cử
        $('#soBongInput').on('input', function() {
            // Lấy giá trị người dùng nhập vào và loại bỏ dấu phẩy
            let soBongDeCu = $(this).val().replace(/,/g, '');
            soBongDeCu = parseInt(soBongDeCu) || 0; // Chuyển chuỗi thành số nguyên

            // Lấy số bông hiện có và loại bỏ dấu phẩy
            let soBongHienCo = parseInt("") || 0;

            // Kiểm tra nếu số bông muốn đề cử lớn hơn số bông hiện có
            if (soBongDeCu > soBongHienCo) {
                soBongDeCu = soBongHienCo; // Giới hạn lại số bông đề cử
                $(this).val(number_format(soBongDeCu)); // Cập nhật lại giá trị nhập vào với dấu phẩy
            } else {
                $(this).val(number_format(soBongDeCu)); // Cập nhật lại giá trị nhập vào với dấu phẩy
            }

            // Tính số bông còn lại sau khi đề cử
            let soBongConLai = soBongHienCo - soBongDeCu;
            $('#afterProposal').val(number_format(soBongConLai) + ' Bông');
        });

        // Xử lý click nút đề cử
        $('.btn-de-cu-truyen').on('click', function() {
            const id_truyen = 2436;
            const id_user = null;

            if (id_user == null) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Bạn cần đăng nhập để sử dụng tính năng này!',
                });
                return;
            }

            // Mở modal
            $('#deCuTruyenModal').modal('show');
        });

        // Xử lý khi bấm nút "Đề Cử Ngay"
        $('.mdv-de-cu-submit-btn').on('click', function() {
            const soBongDeCu = parseInt($('#soBongInput').val().replace(/,/g, '')) || 0;

            if (soBongDeCu < 5000) {
                FuiToast.error('Vui lòng nhập số bông lớn hơn hoặc bằng 5.000 để đề cử.');
                return;
            }

            $.ajax({
                url: 'sources/ajax/mongdaovien/de-cu-bong.php',
                type: 'POST',
                data: {
                    id_truyen: 2436,
                    so_bong: soBongDeCu,
                    pnvn_token: "ab5cf4c804c2e6605e9571de598f2f6248e61e99"
                },
                success: function(response) {
                    if (response.status === 'success') {
                        // Cập nhật lại số bông hiện tại và số bông còn lại sau khi đề cử
                        FuiToast.success('Bạn đã đề cử thành công!');
                        $('#deCuTruyenModal').modal('hide');

                        $('#currentBong').val(number_format(response.so_bong_moi) + ' Bông');
                        $('#afterProposal').val(number_format(response.so_bong_moi) + ' Bông');
                        $("#soBongInput").val('');

                        $(".bong-de-cu-number").html(response.tong_bong_truyen);

                        // Cập nhật Đào, Hạt và Bông của tài khoản
                        $(".dao-dang-co").text(response.dao_hien_tai);
                        $(".hat-dang-co").text(response.hat_hien_tai);
                        $(".bong-dang-co").text(response.bong_hien_tai);
                    } else {
                        FuiToast.error(response.message);
                    }
                },
                error: function() {
                    FuiToast.error('Có lỗi xảy ra, vui lòng thử lại sau.');
                }
            });
        });
        // đề cử truyện end

        // Xem thêm cho cả thể loại và giới thiệu truyện
        // Xem thêm và Rút gọn cho cả thể loại và giới thiệu truyện
        $(".btn-xem-them").on("click", function() {
            const isExpanded = $(this).attr("data-expanded") === "true"; // Kiểm tra trạng thái hiện tại của nút

            if (isExpanded) {
                // Rút gọn nội dung
                $(".collapsed-gioi-thieu").css({
                    "-webkit-line-clamp": "5",
                    overflow: "hidden",
                    display: "-webkit-box" // Quay về trạng thái ban đầu
                });

                $(".san-pham-the-loai-bg").removeClass("disabled"); // Kích hoạt lại nền

                // Cập nhật nút về trạng thái "Xem thêm"
                $(this).text("Xem thêm").attr("data-expanded", "false");
            } else {
                // Mở rộng nội dung
                $(".collapsed-gioi-thieu").css({
                    "-webkit-line-clamp": "unset",
                    overflow: "visible",
                    display: "block"
                }).hide().fadeIn(500); // Hiệu ứng fade nhẹ nhàng

                $(".san-pham-the-loai-bg").addClass("disabled"); // Tắt nền

                // Cập nhật nút về trạng thái "Rút gọn"
                $(this).text("Rút gọn").attr("data-expanded", "true");
            }
        });


        // báo cáo truyện start
        // Hiển thị modal khi click vào nút "Báo lỗi truyện"
        $('.san-pham-show-report').on('click', function() {
            $('#baoLoiModal').modal('show');
        });

        // Xử lý form gửi báo cáo truyện
        $('#baoCaoTruyenForm').on('submit', function(event) {
            event.preventDefault();

            // Gửi AJAX
            $.ajax({
                url: 'sources/ajax/mongdaovien/gui-bao-cao-truyen.php',
                type: 'POST',
                dataType: 'json',
                data: $(this).serialize(),
                beforeSend: function() {
                    // Disable button để tránh người dùng click nhiều lần
                    $('#baoCaoTruyenForm button[type="submit"]').prop('disabled', true);
                },
                success: function(response) {
                    // Reset lại form và đóng modal
                    $('#baoCaoTruyenForm')[0].reset();
                    $('#baoLoiModal').modal('hide');

                    if (response.status === 'success') {
                        // Thông báo thành công
                        Swal.fire({
                            icon: 'success',
                            title: 'Gửi thành công',
                            text: 'Báo cáo của bạn đã được gửi. Cảm ơn bạn!',
                        });
                    } else {
                        // Thông báo thất bại
                        Swal.fire({
                            icon: 'error',
                            title: 'Oops...',
                            text: 'Không thể gửi báo cáo!',
                        });
                    }
                },
                error: function(xhr, status, error) {
                    // Thông báo lỗi nếu xảy ra
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Đã có lỗi xảy ra. Vui lòng thử lại sau.',
                    });
                },
                complete: function() {
                    // Enable lại button sau khi xử lý
                    $('#baoCaoTruyenForm button[type="submit"]').prop('disabled', false);
                }
            });
        });

        // báo cáo truyện end

        // click vào chia sẻ truyện start
        // Initialize ClipboardJS for elements with the "san-pham-show-link" class
        var clipboard = new ClipboardJS('.san-pham-show-link', {
            text: function(trigger) {
                // Return the data-link attribute to be copied
                return trigger.getAttribute('data-link');
            }
        });

        // Handle success callback
        clipboard.on('success', function(e) {
            // Show success notification with Fuitoast
            FuiToast.success('Đã copy link truyện');
            e.clearSelection(); // Clear selected text after copying
        });

        // Handle error callback if copying fails
        clipboard.on('error', function(e) {
            FuiToast.error('Không thể copy link, vui lòng thử lại!');
        });
        // click vào chia sẻ truyện end 


        // Xử lý mua chương start

        // Khởi tạo tooltip của Bootstrap cho nút "Mua"
        $(function() {
            $('[data-toggle="tooltip"]').tooltip();
        });

        // Chọn hoặc bỏ chọn tất cả các checkbox mua chương
        $('.check-chapter-all').on('change', function() {
            let isChecked = $(this).is(':checked');
            $('.check-box-mua-chuong').prop('checked', isChecked);
            updateTooltip(); // Cập nhật tooltip sau khi chọn tất cả
        });

        // Khi checkbox chương được chọn hoặc bỏ chọn
        $('.check-box-mua-chuong').on('change', function() {
            updateTooltip();
        });

        // Hàm cập nhật tooltip
        function updateTooltip() {
            let selectedChapters = $('.check-box-mua-chuong:checked');
            if (selectedChapters.length > 0) {
                $('.btn-mua-chuong').attr('title', 'Click vào đây để thanh toán');
                $('.btn-mua-chuong').tooltip('show');
            } else {
                $('.btn-mua-chuong').tooltip('hide');
            }
        }

        // Xử lý khi nhấn vào nút "Mua"
        $('.btn-mua-chuong').on('click', function() {
            const id_user = null;

            if (id_user == null) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Bạn cần đăng nhập để sử dụng tính năng này!',
                });
                return;
            }

            let selectedChapters = $('.check-box-mua-chuong:checked');
            if (selectedChapters.length === 0) {
                // Hiển thị thông báo nếu chưa chọn chương nào
                FuiToast.error('Bạn chưa chọn chương nào để mua');
                return;
            }

            // Tạo danh sách chương đã chọn và giá tiền
            let danhSachHtml = '';
            let tongSoChuong = 0;
            let tongGiaDao = 0;
            let tongGiaHat = 0;

            selectedChapters.each(function() {
                let soChuong = $(this).closest('tr').find('.mdv-san-pham-show-dsc-table-chuong').text();
                let chapterName = $(this).data('chapter-name') || '';
                let giaDao = parseInt($(this).data('gia-dao')) || 0;
                let giaHat = parseInt($(this).data('gia-hat')) || 0;

                tongSoChuong++;
                tongGiaDao += giaDao;
                tongGiaHat += giaHat;

                danhSachHtml += `
            <li class="list-group-item mua-chuong-list-item">
                <div class="mua-chuong-item-line-1">
                    ${soChuong} - ${chapterName}
                </div>
                <div class="mua-chuong-item-line-2 d-flex justify-content-end align-items-center gap-2">
                    ${giaDao > 0 ? '<img src="https://tehitruyen.com/templates/images/dao-nho.png" alt="icon" class="icon-qua-dao-chuong"> ' + giaDao : ''}
                    ${giaHat > 0 ? '<img src="https://tehitruyen.com/templates/images/hat.png" alt="icon" class="icon-hat"> ' + giaHat : ''}
                </div>
            </li>`;
            });

            // Gán danh sách chương đã chọn và tổng giá vào modal và hiển thị modal
            $('#danhSachChuongDaChon').html(danhSachHtml);
            $('#tongSoChuong').text(tongSoChuong);
            $('#tongGiaDao').text(tongGiaDao > 0 ? tongGiaDao + ' Đào' : '0');
            $('#tongGiaHat').text(tongGiaHat > 0 ? tongGiaHat + ' Hạt' : '0');

            $('#muaChuongModal').modal('show');
        });

        // Xử lý Thanh Toán
        $('.mua-chuong-btn-pay').on('click', function() {
            let selectedChapters = $('.check-box-mua-chuong:checked');
            let chaptersData = [];
            let tongGiaDao = 0;
            let tongGiaHat = 0;

            selectedChapters.each(function() {
                chaptersData.push(vanhiep_sanitize_js($(this).data('id-chapter')));
                tongGiaDao += parseInt($(this).data('gia-dao')) || 0;
                tongGiaHat += parseInt($(this).data('gia-hat')) || 0;
            });

            $.ajax({
                url: "sources/ajax/mongdaovien/mua-chuong.php",
                type: 'POST',
                data: {
                    chapters: chaptersData,
                    tong_gia_dao: tongGiaDao,
                    tong_gia_hat: tongGiaHat,
                    id_truyen: vanhiep_sanitize_js('2436'),
                    id_user: vanhiep_sanitize_js(null)
                },
                success: function(response) {
                    if (response.status === 'success') {
                        FuiToast.success('Bạn đã mua chương thành công');
                        // Cập nhật lại Đào của tài khoản
                        $(".dao-dang-co").text(response.dao_hien_tai);
                        $(".hat-dang-co").text(response.hat_hien_tai);
                        $(".bong-dang-co").text(response.bong_hien_tai);

                        $('#muaChuongModal').modal('hide');
                        // Tải lại danh sách chương với hiệu ứng fade
                        $('#result-chuong').fadeOut(500, function() {
                            $.ajax({
                                url: 'sources/ajax/mongdaovien/load-chuong.php',
                                type: 'GET',
                                data: {
                                    id_truyen: vanhiep_sanitize_js('2436')
                                },
                                success: function(newContent) {
                                    $('#result-chuong').html(newContent).fadeIn(500);
                                    attachEventHandlers(); // Gắn lại các sự kiện
                                },
                                error: function() {
                                    FuiToast.error('Có lỗi xảy ra khi tải lại danh sách chương');
                                }
                            });
                        });
                    } else {
                        FuiToast.error(response.message);
                    }
                },
                error: function() {
                    FuiToast.error('Có lỗi xảy ra, vui lòng thử lại');
                }
            });
        });

        // Gọi hàm này ngay khi trang tải lần đầu
        attachEventHandlers();

        // Hàm để gắn lại sự kiện cho các button sau khi nội dung được tải lại
        function attachEventHandlers() {
            // Chọn hoặc bỏ chọn tất cả các checkbox mua chương
            $('.check-chapter-all').on('change', function() {
                let isChecked = $(this).is(':checked');
                $('.check-box-mua-chuong').prop('checked', isChecked);
                updateTooltip();
            });

            // Khi checkbox chương được chọn hoặc bỏ chọn
            $('.check-box-mua-chuong').on('change', function() {
                updateTooltip();
            });

            // Khởi tạo lại tooltip cho nút "Mua"
            $('[data-toggle="tooltip"]').tooltip();
        }

        // xử lý mua chương end

        // XỬ LÝ THEO DÕI - BỎ THEO DÕI START
        // Xử lý khi nhấn vào nút "Theo dõi"
        $(document).on('click', '.btn-theo-doi-profile', function() {
            const id_user = null;
            const id_user_to_follow = 1044;

            if (id_user == null) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Bạn cần đăng nhập để sử dụng tính năng này!',
                });
                return;
            }

            // Kiểm tra nếu người dùng cố gắng theo dõi chính mình
            if (id_user === id_user_to_follow) {
                FuiToast.error('Bạn không thể follow chính mình');
                return;
            }

            $.ajax({
                url: "sources/ajax/mongdaovien/theo-doi-nguoi-choi.php",
                type: 'POST',
                data: {
                    id_user: '1044'
                },
                success: function(response) {
                    if (response.status === 'success') {
                        FuiToast.success('Bạn đã theo dõi thành công');
                        $('.btn-theo-doi-profile').replaceWith(`
                                 <div class="mdv-sps-tac-gia-button-cai-dat mdv-sps-tac-gia-button-cai-dat-donate btn-bo-theo-doi-profile rounded-2 btn-hover-shine" data-bs-toggle="tooltip" title="Click để BỎ Theo Dõi người này">
                                            <i class="fa-solid fa-heart"></i>
                                            </div>
                                `);
                        // Cập nhật lại số người theo dõi
                        updateFollowCount();
                    } else {
                        FuiToast.error(response.message);
                    }
                },
                error: function() {
                    FuiToast.error('Có lỗi xảy ra, vui lòng thử lại');
                }
            });
        });

        // Xử lý khi nhấn vào nút "Bỏ theo dõi"
        $(document).on('click', '.btn-bo-theo-doi-profile', function() {
            const id_user = null;

            if (id_user == null) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Bạn cần đăng nhập để sử dụng tính năng này!',
                });
                return;
            }

            $.ajax({
                url: "sources/ajax/mongdaovien/bo-theo-doi-nguoi-choi.php",
                type: 'POST',
                data: {
                    id_user: '1044'
                },
                success: function(response) {
                    if (response.status === 'success') {
                        FuiToast.success('Bạn đã bỏ theo dõi thành công');
                        $('.btn-bo-theo-doi-profile').replaceWith(`
                                <div class="mdv-sps-tac-gia-button-cai-dat mdv-sps-tac-gia-button-cai-dat-donate btn-theo-doi-profile rounded-2 btn-hover-shine" data-bs-toggle="tooltip" title="Click để Theo Dõi người này">
                                                <i class="fa-regular fa-heart"></i>
                                            </div>
                                `);
                        // Cập nhật lại số người theo dõi
                        updateFollowCount();
                    } else {
                        FuiToast.error(response.message);
                    }
                },
                error: function() {
                    FuiToast.error('Có lỗi xảy ra, vui lòng thử lại');
                }
            });
        });

        // Hàm cập nhật số người theo dõi
        function updateFollowCount() {
            $.ajax({
                url: 'sources/ajax/mongdaovien/load-follow-count.php',
                type: 'GET',
                data: {
                    id_user: 1044                },
                success: function(response) {
                    if (response.status === 'success') {
                        $('#so-nguoi-theo-doi').fadeOut(300, function() {
                            $(this).text(response.follow_count).fadeIn(300);
                        });
                    } else {
                        FuiToast.error(response.message);
                    }
                },
                error: function() {
                    FuiToast.error('Có lỗi xảy ra khi cập nhật số người theo dõi');
                }
            });
        }

        // XỬ LÝ THEO DÕI - BỎ THEO DÕI END

        // button cài đặt start
        $(document).on('click', ".btn-cai-dat-profile", function(e) {
            if (!$(e.target).closest('.btn-cai-dat-profile, .dropdown-settings').length) {
                $('.dropdown-menu').removeClass('show');
            }
        });

        // button cài đặt end

        // xử lý chọc ghẹo start
        $(document).on('click', '.btn-xl-choc-gheo', function() {
            const id_user_duoc_choc = $(this).data('user-duoc-choc');
            const id_user = null;

            if (id_user === null) {
                // Người dùng chưa đăng nhập
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Bạn cần đăng nhập để sử dụng tính năng này!',
                });
                return;
            }

            // Kiểm tra nếu người dùng cố gắng chọc ghẹo chính mình
            if (id_user === id_user_duoc_choc) {
                FuiToast.error('Bạn không thể chọc ghẹo chính mình');
                return;
            }

            // Xác nhận chọc ghẹo
            Swal.fire({
                title: 'Bạn có chắc muốn chọc ghẹo người chơi này?',
                text: "Sau khi chọc ghẹo, bạn sẽ phải đợi 24h để chọc lại!",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Đồng ý',
                cancelButtonText: 'Hủy bỏ'
            }).then((result) => {
                if (result.isConfirmed) {
                    $.ajax({
                        url: 'sources/ajax/mongdaovien/xu-ly-choc-gheo.php',
                        type: 'POST',
                        data: {
                            user_duoc_choc: vanhiep_sanitize_js(id_user_duoc_choc),
                            user_choc: vanhiep_sanitize_js(id_user)
                        },
                        success: function(response) {
                            if (response.status === 'success') {
                                FuiToast.success('Bạn đã chọc ghẹo thành công');
                            } else {
                                FuiToast.error(response.message);
                            }
                        },
                        error: function() {
                            FuiToast.error('Có lỗi xảy ra, vui lòng thử lại');
                        }
                    });
                }
            });
        });

        // xử lý chọc ghẹo end

        // xử lý donate start

        $(document).on('click', '.btn-xl-donate', function() {
            const id_user_duoc_donate = $(this).data('user-duoc-donate');
            const id_user = null;
            let so_dao_hien_co = 0;
            if (id_user === null) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Bạn cần đăng nhập để sử dụng tính năng này!',
                });
                return;
            }

            $.ajax({
                url: 'sources/ajax/mongdaovien/load-tai-khoan.php',
                type: 'POST',
                data: {
                    id_user: id_user
                },
                success: function(response) {
                    if (response.status === 'success') {
                        const tai_khoan = response.tai_khoan;

                        // Cập nhật modal với số đào hiện có của người dùng
                        so_dao_hien_co = tai_khoan.dao;
                        $('#so_dao_hien_co').html(`${number_format(tai_khoan.dao)}`);
                        $('#soDaoConLai').text(number_format(tai_khoan.dao));

                        $('#donateModal').modal('show');
                    } else {
                        FuiToast.error('Có lỗi xảy ra khi tải thông tin tài khoản của bạn.');
                    }
                },
                error: function() {
                    FuiToast.error('Có lỗi xảy ra khi truy vấn tài khoản.');
                }
            });

            // Hiển thị modal donate
            $('#donateModal').modal('show');
            $('.formatprice').priceFormat({
                limit: 8,
                prefix: '',
                centsLimit: 0
            });

            // Hàm định dạng số thành số có dấu phẩy
            function number_format(number) {
                return new Intl.NumberFormat('vi-VN').format(number);
            }

            // Xử lý khi người dùng nhập vào số đào muốn donate
            $('#soDaoDonate').on('input', function() {
                // Lấy giá trị người dùng nhập vào và loại bỏ dấu phẩy
                let soDaoDonate = $(this).val().replace(/,/g, '');
                soDaoDonate = parseInt(soDaoDonate) || 0; // Chuyển chuỗi thành số nguyên

                // Lấy số đào hiện có và loại bỏ dấu phẩy
                let soDaoHienCo = parseInt(so_dao_hien_co) || 0;

                // // Kiểm tra nếu số đào muốn donate lớn hơn số đào hiện có
                if (soDaoDonate > soDaoHienCo) {
                    soDaoDonate = soDaoHienCo;
                    $(this).val(soDaoDonate); // Cập nhật lại giá trị nhập vào với dấu phẩy
                }

                // // Tính số đào còn lại sau khi donate
                let soDaoConLai = soDaoHienCo - soDaoDonate;
                $('#soDaoConLai').text(number_format(soDaoConLai));
            });

            // Xử lý khi bấm nút "Donate"
            $('.donate-btn-confirm').on('click', function() {
                const soDaoDonate = $('#soDaoDonate').val() || 0;
                const user_duoc_donate = $('.btn-xl-donate').data('user-duoc-donate');

                if (soDaoDonate <= 0) {
                    FuiToast.error('Vui lòng nhập số đào hợp lệ để donate.');
                    return;
                }

                Swal.fire({
                    title: 'Bạn có chắc chắn muốn donate?',
                    text: 'Sau khi donate, số đào của bạn sẽ bị trừ.',
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Đồng ý',
                    cancelButtonText: 'Hủy bỏ'
                }).then((result) => {
                    if (result.isConfirmed) {
                        $.ajax({
                            url: 'sources/ajax/mongdaovien/donate-dao.php',
                            type: 'POST',
                            data: {
                                user_duoc_donate: user_duoc_donate,
                                so_dao: soDaoDonate,
                                id_truyen: '2436'
                            },
                            success: function(response) {
                                if (response.status === 'success') {
                                    FuiToast.success('Bạn đã donate thành công!');
                                    // Cập nhật lại Đào của tài khoản
                                    $(".dao-dang-co").text(response.dao_hien_tai);
                                    $(".hat-dang-co").text(response.hat_hien_tai);
                                    $(".bong-dang-co").text(response.bong_hien_tai);

                                    $('#donateModal').modal('hide');
                                } else {
                                    FuiToast.error(response.message);
                                }
                            },
                            error: function() {
                                FuiToast.error('Có lỗi xảy ra, vui lòng thử lại sau.');
                            }
                        });
                    }
                });
            });
        });

        // xử lý donate end


        // css khung chương và tab tác giả start
        function setMinMaxHeight() {
            if ($(window).width() >= 1024) {
                // let profileHeight = $('.mdv-san-pham-show-profile').outerHeight();
                // $('.mdv-san-pham-show-dsc-table tbody').css({
                //     'min-height': profileHeight - 7 + 'px',
                //     'max-height': profileHeight - 7 + 'px',
                // });
                $(".danh-sach-chuong-sp-show").addClass('danh-sach-chuong-sp-show-pc');
            } else {
                // Đặt lại chiều cao khi màn hình nhỏ hơn 1024px
                // $('.mdv-san-pham-show-dsc-table tbody').css({
                //     'min-height': '',
                //     'max-height': '',
                // });

                $(".danh-sach-chuong-sp-show").addClass('vh-scrollbar');
            }
        }

        // Gọi hàm khi tải trang
        setMinMaxHeight();

        // Gọi hàm khi kích thước cửa sổ thay đổi
        $(window).resize(function() {
            setMinMaxHeight();
        });
        // css khung chương và tab tác giả end

        // show full trích dẫn yêu thương start
        $('#toggleIntroduceButton').on('click', function() {
            const $introduceBox = $('#profileIntroduce');

            if ($introduceBox.hasClass('collapsed')) {
                // Mở rộng nội dung
                $introduceBox.hide().removeClass('collapsed').addClass('expanded').fadeIn(300);
                $(this).text('Thu gọn');
            } else {
                // Thu gọn nội dung
                $introduceBox.fadeOut(300, function() {
                    $(this).removeClass('expanded').addClass('collapsed').fadeIn(300);
                });
                $(this).text('Hiển thị đầy đủ');
            }
        });
        // show full trích dẫn yêu thương end


        // xử lý bình luận truyện start
        $(document).on('click', '.btn-gui-binh-luan-truyen', function() {
            // Kiểm tra đăng nhập
            const isLoggedIn = false;
            if (!isLoggedIn) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Bạn chưa đăng nhập!',
                });
                return;
            }

            // Lấy nội dung bình luận và làm sạch bằng DOMPurify
            let noiDung = $('#emojionearea')[0].emojioneArea.getText();
            noiDung = DOMPurify.sanitize(noiDung);

            let soTu = noiDung.trim().split(/\s+/).length;

            // Kiểm tra nội dung quá dài
            if (soTu > 500) {
                Swal.fire({
                    icon: 'warning',
                    title: 'Nội dung quá dài',
                    text: 'Bình luận của bạn không được dài quá 500 từ.',
                });
                return;
            }

            // Ngăn chặn spam bình luận liên tục
            if (this.disabled) {
                Swal.fire({
                    icon: 'error',
                    title: 'Spam bình luận',
                    text: 'Bạn đang bình luận quá nhanh. Vui lòng đợi một chút!',
                });
                return;
            }
            this.disabled = true;
            setTimeout(() => {
                this.disabled = false;
            }, 5000);

            // Gửi AJAX
            $.ajax({
                url: 'sources/ajax/mongdaovien/gui-binh-luan-truyen.php',
                type: 'POST',
                data: {
                    id_truyen: 2436,
                    id_user: 0,
                    noi_dung: noiDung
                },
                dataType: 'json',
                success: function(response) {
                    if (response.status === 'success') {
                        FuiToast.success('Bình luận của bạn đã được gửi thành công.');

                        // Thêm bình luận mới vào danh sách
                        $('#result-binh-luan').prepend(`
                    <div class="mdv-san-pham-show-comment-list-item" style="opacity: 1;">
                        <div class="row ">
                            <div class="col-2">
                                <div class="mdv-san-pham-show-comment-form-avatar mdv-san-pham-show-comment-form-avatar-list-bl ratio ratio-1x1">
                                    <a href="${response.avatar}" data-fancybox>
                                        <img src="${response.avatar}" alt="png" class="avatar">
                                    </a>
                                    <img src="${response.khung_avatar}" alt="khung avatar" class="frame">
                                </div>
                            </div>
                            <div class="col-10">
                                <div class="mdv-san-pham-show-comment-list-item-comment p-3 d-flex flex-column gap-2 ">
                                    <div class="mdv-san-pham-show-comment-list-item-comment-name">
                                        <a href="https://tehitruyen.com/my-wall/${response.username}" class="ten-doc-gia ten-tac-gia">${response.ten_doc_gia}</a> <span class="dang-cho-duyet">(Vừa gửi xong)</span>
                                    </div>
                                    <div class="mdv-san-pham-show-comment-list-item-comment-des">
                                        ${noiDung}
                                    </div>
                                </div>
                                <div class="mdv-san-pham-show-comment-list-item-comment-like-rep p-2 d-flex flex-column flex-md-row align-items-md-center gap-1 gap-md-3 justify-content-md-between">
                                    <div class="mdv-san-pham-show-comment-list-item-comment-like-rep-left d-inline-flex align-items-center gap-3">
                                       
                                        <div class="mdv-san-pham-show-comment-list-item-comment-time">Vừa xong</div>
                                    </div>
                                  
                                </div>
                            </div>
                        </div>
                    </div>
                `);
                        // Làm trống khung nhập bình luận
                        $('#emojionearea')[0].emojioneArea.setText('');
                    } else {
                        FuiToast.error(response.message);
                    }
                },
                error: function() {
                    FuiToast.error('Có lỗi xảy ra, vui lòng thử lại sau.');
                }
            });
        });

        // xử lý bình luận truyện end


        // Xử lý trả lời bình luận start
        $(document).on('click', '.mdv-san-pham-show-comment-list-item-comment-rep', function() {
            // Kiểm tra người dùng đã đăng nhập hay chưa
            const idUser = null;
            if (idUser === null) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Bạn cần đăng nhập để sử dụng tính năng này!',
                });
                return;
            }

            const $replyButton = $(this);
            // Tìm phần tử cha gần nhất là `.col-10`
            const $commentItemContainer = $replyButton.closest('.col-10');
            let $replyBox = $commentItemContainer.find('.mdv-san-pham-show-tra-loi');

            // Nếu chưa có hộp trả lời, thì thêm vào
            if ($replyBox.length === 0) {
                // Tạo HTML cho phần trả lời
                const replyHtml = `
        <div class="mdv-san-pham-show-tra-loi mb-3">
            <div class="mdv-san-pham-show-tra-loi-content">
                <div class="row gx-3">
                    <div class="col-1">
                        <div class="mdv-san-pham-show-comment-form-avatar mdv-san-pham-show-comment-form-avatar-list-bl ratio ratio-1x1">
                            <a href="" data-fancybox>
                                <img src="" alt="png" class="avatar">
                            </a>
                            <img src="" alt="khung avatar" class="frame">
                        </div>
                    </div>
                    <div class="col-9">
                        <div class="mdv-san-pham-show-tra-loi-content-form h-100">
                            <textarea class="emojionearea-rep form-control" rows="3" placeholder="Trả lời..."></textarea>
                        </div>
                    </div>
                    <div class="col-2">
                        <button type="button" class="btn btn-gui-tra-loi d-flex justify-content-center align-items-center w-100 h-100" 
                            data-level-binhluan="${parseInt($replyButton.data('level-binhluan')) + 1}" 
                            data-id-parent="${$replyButton.data('id-binhluan')}">
                            Gửi
                        </button>
                    </div>
                </div>
            </div>
        </div>`;

                // Append vào `.col-10` gần nhất
                $replyBox = $(replyHtml).hide();
                // Khởi tạo emojiArea cho phần reply vừa được thêm vào
                $replyBox.find('.emojionearea-rep').emojioneArea({
                    pickerPosition: 'bottom',
                    filtersPosition: 'top',
                    tonesStyle: 'square',
                    placeholder: 'Trả lời...',
                });
                $commentItemContainer.append($replyBox);
                $replyBox.fadeIn('slow', function() {
                    // Chỉ cuộn đến phần tử nếu chiều cao của `.col-10` lớn hơn 600px
                    if ($commentItemContainer.height() > 600) {
                        const offsetTop = $replyBox.offset().top - 100; // Điều chỉnh giá trị này để phù hợp với giao diện

                        // Kiểm tra nếu biến lenis đã được khởi tạo
                        if (typeof lenis !== 'undefined') {
                            lenis.scrollTo(offsetTop, {
                                duration: 3.5, // Tăng thời gian để cuộn mượt hơn
                                easing: (t) => Math.min(1, 1 - Math.pow(2, -15 * t)), // Easing giống với Lenis
                            });
                        } else {
                            // Sử dụng jQuery nếu Lenis không có
                            $('html, body').animate({
                                scrollTop: offsetTop
                            }, 800); // 800ms để cuộn xuống mượt
                        }
                    }


                    // Focus vào textarea của hộp trả lời
                    $replyBox.find('.emojionearea-rep').focus();

                });
            }
        });




        // Xử lý gửi trả lời bình luận
        $(document).on('click', '.btn-gui-tra-loi', function() {
            const $replyButton = $(this);
            const $replyBox = $replyButton.closest('.mdv-san-pham-show-tra-loi');
            const idTruyen = 2436;
            const idUser = null;

            // Lấy level và id parent từ button "Gửi"
            const levelBinhLuan = $replyButton.data('level-binhluan');
            const idParent = $replyButton.data('id-parent');

            // Lấy nội dung bình luận từ emojiArea
            let noiDung = $replyBox.find('.emojionearea-rep').data("emojioneArea").getText().trim();
            noiDung = DOMPurify.sanitize(noiDung);

            // Kiểm tra nội dung không được rỗng
            if (!noiDung) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Nội dung trả lời không được để trống!',
                });
                return;
            }

            // Kiểm tra người dùng đã đăng nhập chưa
            if (idUser === null) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Bạn cần đăng nhập để sử dụng tính năng này!',
                });
                return;
            }

            // Ajax gửi dữ liệu trả lời bình luận
            $.ajax({
                url: 'sources/ajax/mongdaovien/gui-tra-loi-binh-luan-truyen.php',
                type: 'POST',
                data: {
                    id_truyen: idTruyen,
                    id_user: idUser,
                    noi_dung: noiDung,
                    parent: idParent,
                    level: levelBinhLuan,
                    thoi_gian: Math.floor(Date.now() / 1000) // Thời gian hiện tại (UNIX timestamp)
                },
                success: function(response) {
                    if (response.status === 'success') {
                        // Thông báo thành công bằng FuiToast
                        FuiToast.success(response.message);

                        // Tạo phần tử bình luận mới từ mẫu đã cung cấp
                        const commentItemHtml = `
        <!-- subitem -->
        <div class="mdv-san-pham-show-comment-list-item" style="opacity: 1;">
            <div class="row">
                <div class="col-2">
                    <div class="mdv-san-pham-show-comment-form-avatar mdv-san-pham-show-comment-form-avatar-list-bl ratio ratio-1x1">
                        <a href="${response.avatar}" data-fancybox>
                            <img src="${response.avatar}" alt="png" class="avatar">
                        </a>
                        <img src="${response.khung_avatar}" alt="khung avatar" class="frame">
                    </div>
                </div>
                <div class="col-10">
                    <div class="mdv-san-pham-show-comment-list-item-comment p-3 d-flex flex-column gap-2">
                        <div class="mdv-san-pham-show-comment-list-item-comment-name">
                            <a href="https://tehitruyen.com/my-wall/${response.username}" class="ten-doc-gia">${response.ten_doc_gia}</a>
                            <span class="tra-loi-tag">(Vừa gửi xong)</span>
                        </div>
                        <div class="mdv-san-pham-show-comment-list-item-comment-des">
                            ${noiDung}
                        </div>
                    </div>
                    <!-- thích, bình luận, time -->
                    <div class="mdv-san-pham-show-comment-list-item-comment-like-rep p-2 d-flex flex-column flex-md-row align-items-md-center gap-1 gap-md-3 justify-content-md-between">
                        <div class="mdv-san-pham-show-comment-list-item-comment-like-rep-left d-inline-flex align-items-center gap-3">
                            <div class="mdv-san-pham-show-comment-list-item-comment-time">
                                Vừa xong
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;

                        // Kiểm tra cấp độ của bình luận
                        if (levelBinhLuan >= 3) {
                            // Tìm phần tử cha gần nhất để thêm bình luận (cấp 3 hoặc cao hơn)
                            const $subItemBox = $replyButton.closest('.mdv-san-pham-show-comment-list-subitem-box').first();

                            // Thêm bình luận mới vào phần subitem dưới bình luận cha
                            if ($subItemBox.length > 0) {
                                const $newComment = $(commentItemHtml);
                                $newComment.hide().appendTo($subItemBox).fadeIn('slow');
                            }
                        } else {
                            // Tìm phần tử cha gần nhất để thêm bình luận (cấp 1 hoặc 2)
                            const $commentItemContainer = $replyButton.closest('.mdv-san-pham-show-comment-list-item');
                            const $subItemBox = $commentItemContainer.find('.mdv-san-pham-show-comment-list-subitem-box').first();

                            // Thêm bình luận mới vào phần subitem dưới bình luận cha
                            if ($subItemBox.length > 0) {
                                const $newComment = $(commentItemHtml);
                                $newComment.hide().prependTo($subItemBox).fadeIn('slow');
                            }
                        }

                        // Ẩn hộp trả lời sau khi thêm bình luận thành công
                        $replyBox.fadeOut('slow', function() {
                            $(this).remove();
                        });
                    } else {
                        FuiToast.error(response.message);
                    }
                },
                error: function() {
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Có lỗi xảy ra, vui lòng thử lại sau!',
                    });
                }
            });
        });
        // Xử lý trả lời bình luận end


        // xử lý thích bình luận start
        // Xử lý thích/bỏ thích bình luận
        $(document).on('click', '.mdv-san-pham-show-comment-list-item-comment-like', function() {
            const $likeButton = $(this);
            const idBinhLuan = $likeButton.data('id-binhluan');
            const idUser = null;

            // Kiểm tra người dùng đã đăng nhập chưa
            if (idUser === null) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Bạn cần đăng nhập để sử dụng tính năng này!',
                });
                return;
            }

            // Ajax gửi dữ liệu thích/bỏ thích
            $.ajax({
                url: 'sources/ajax/mongdaovien/like-binh-luan-truyen.php',
                type: 'POST',
                data: {
                    id_binhluan: idBinhLuan,
                    id_user: idUser,
                },
                success: function(response) {
                    if (response.status === 'success') {
                        // Thông báo thành công bằng FuiToast
                        FuiToast.success(response.message);

                        // Cập nhật text nút thích/bỏ thích
                        if (response.action === 'like') {
                            $likeButton.text('Bỏ thích');
                        } else {
                            $likeButton.text('Thích');
                        }

                        // Cập nhật số lượt thích cho phần tử tương ứng
                        const $likeCountContainer = $likeButton.closest('.mdv-san-pham-show-comment-list-item').find('.danh-sach-thich-binh-luan').first();
                        if (response.like_count > 0) {
                            const likeCountHtml = `
                        <span class="mdv-luot-thich" data-id-binhluan="${idBinhLuan}" data-bs-toggle="modal" data-bs-target="#listMemberLike">${response.like_count} lượt thích</span>
                    `;
                            $likeCountContainer.html(likeCountHtml).fadeIn('slow');
                        } else {
                            $likeCountContainer.fadeOut('slow', function() {
                                $(this).empty();
                            });
                        }
                    } else {
                        FuiToast.error(response.message);
                    }
                },
                error: function() {
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Có lỗi xảy ra, vui lòng thử lại sau!',
                    });
                }
            });
        });
        // Xử lý thích/bỏ thích bình luận end


        // xử lý thích bình luận end


        // Xử lý khi click vào "xem lượt thích" để mở modal danh sách thích
        $(document).on('click', '.mdv-luot-thich', function() {
            const idBinhLuan = $(this).data('id-binhluan');

            // Ajax để lấy danh sách những người thích bình luận
            $.ajax({
                url: 'sources/ajax/mongdaovien/lay-danh-sach-thich.php',
                type: 'POST',
                data: {
                    id_binhluan: idBinhLuan,
                },
                success: function(response) {
                    if (response.status === 'success') {
                        // Tạo danh sách người dùng từ dữ liệu trả về
                        let memberListHtml = '';

                        response.data.forEach(user => {
                            let followButtonHtml = '';

                            // Kiểm tra nếu đã theo dõi thì hiển thị nút bỏ theo dõi
                            if (user.da_theo_doi) {
                                followButtonHtml = `<button class="btn btn-bo-theo-doi-tv hvr-icon-bounce" data-id-user="${user.id}"><i class="hvr-icon fa-solid fa-user-minus"></i></button>`;
                            } else {
                                followButtonHtml = `<button class="btn btn-theo-doi-tv hvr-icon-bounce" data-id-user="${user.id}"><i class="hvr-icon fa-solid fa-user-plus"></i></button>`;
                            }

                            memberListHtml += `
                        <!-- item start -->
                        <div class="col">
                            <div class="modal-danh-sach-thich-content-item d-flex align-items-center justify-content-between gap-3">
                                <!-- avatar -->
                                <div class="modal-danh-sach-thich-content-item-avatar d-inline-flex align-items-center gap-2">
                                    <div class="mdv-san-pham-show-comment-form-avatar modal-danh-sach-thich-content-item-avatar-image ratio ratio-1x1">
                                        <a href="${user.avatar}" data-fancybox>
                                            <img src="${user.avatar}" alt="png" class="avatar">
                                        </a>
                                        <img src="${user.khung_avatar}" alt="khung avatar" class="frame">
                                    </div>
                                    <!-- tên -->
                                    <div class="modal-danh-sach-thich-content-item-name">
                                        <a href="https://tehitruyen.com/my-wall/${user.username}" class="ten-doc-gia">${user.ten_hien_thi}</a>
                                    </div>
                                </div>
                                <!-- theo dõi -->
                                ${followButtonHtml}
                            </div>
                        </div>
                        <!-- item end -->
                    `;
                        });

                        // Chèn HTML mới vào modal
                        $('.modal-danh-sach-thich-content .row').html(memberListHtml);
                        // Hiển thị modal
                        $('#listMemberLike').modal('show');
                    } else {
                        FuiToast.error(response.message);
                    }
                },
                error: function() {
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Có lỗi xảy ra, vui lòng thử lại sau!',
                    });
                }
            });
        });
        // Xử lý sự kiện click "xem lượt thích" end




        // Xử lý khi nhấn vào nút "Theo dõi" trong modal danh sách thích
        $(document).on('click', '.btn-theo-doi-tv', function() {
            const $followButton = $(this);
            const id_user = null;
            const id_user_to_follow = $followButton.data('id-user');

            if (id_user == null) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Bạn cần đăng nhập để sử dụng tính năng này!',
                });
                return;
            }

            // Kiểm tra nếu người dùng cố gắng theo dõi chính mình
            if (id_user === id_user_to_follow) {
                FuiToast.error('Bạn không thể theo dõi chính mình');
                return;
            }

            Swal.fire({
                title: 'Bạn có chắc muốn theo dõi người chơi này?',
                text: "Sau khi theo dõi, bạn có thể hủy bỏ bất cứ lúc nào!",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Đồng ý',
                cancelButtonText: 'Hủy bỏ'
            }).then((result) => {
                if (result.isConfirmed) {
                    $.ajax({
                        url: "sources/ajax/mongdaovien/theo-doi-nguoi-choi.php",
                        type: 'POST',
                        data: {
                            id_user: id_user_to_follow
                        },
                        success: function(response) {
                            if (response.status === 'success') {
                                FuiToast.success('Bạn đã theo dõi thành công');
                                $followButton.replaceWith('<button class="btn btn-bo-theo-doi-tv hvr-icon-bounce" data-id-user="' + id_user_to_follow + '"><i class="hvr-icon fa-solid fa-user-minus"></i></button>');
                            } else {
                                FuiToast.error(response.message);
                            }
                        },
                        error: function() {
                            FuiToast.error('Có lỗi xảy ra, vui lòng thử lại');
                        }
                    });
                }
            });
        });

        // Xử lý khi nhấn vào nút "Bỏ theo dõi" trong modal danh sách thích
        $(document).on('click', '.btn-bo-theo-doi-tv', function() {
            const $unfollowButton = $(this);
            const id_user = null;
            const id_user_to_unfollow = $unfollowButton.data('id-user');

            if (id_user == null) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Bạn cần đăng nhập để sử dụng tính năng này!',
                });
                return;
            }

            Swal.fire({
                title: 'Bạn có chắc muốn bỏ theo dõi người chơi này?',
                text: "Sau khi bỏ theo dõi, bạn có thể theo dõi lại bất cứ lúc nào!",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Đồng ý',
                cancelButtonText: 'Hủy bỏ'
            }).then((result) => {
                if (result.isConfirmed) {
                    $.ajax({
                        url: "sources/ajax/mongdaovien/bo-theo-doi-nguoi-choi.php",
                        type: 'POST',
                        data: {
                            id_user: id_user_to_unfollow
                        },
                        success: function(response) {
                            if (response.status === 'success') {
                                FuiToast.success('Bạn đã bỏ theo dõi thành công');
                                $unfollowButton.replaceWith('<button class="btn btn-theo-doi-tv hvr-icon-bounce" data-id-user="' + id_user_to_unfollow + '"><i class="hvr-icon fa-solid fa-user-plus"></i></button>');
                            } else {
                                FuiToast.error(response.message);
                            }
                        },
                        error: function() {
                            FuiToast.error('Có lỗi xảy ra, vui lòng thử lại');
                        }
                    });
                }
            });
        });

        // xử lý load thêm bình luận start

        $(document).on('click', '.btn-xem-them-binh-luan', function() {
            const $button = $(this);
            const offset = $button.data('offset');
            const idTruyen = 2436;

            // Ajax để tải thêm bình luận
            $.ajax({
                url: 'sources/ajax/mongdaovien/load-them-binh-luan-truyen.php',
                type: 'POST',
                data: {
                    id_truyen: idTruyen,
                    offset: offset,
                },
                success: function(response) {
                    if (response.status === 'success') {
                        // Thêm HTML bình luận mới vào dưới cùng của danh sách bình luận
                        $(response.html).hide().appendTo('#result-binh-luan').fadeIn('slow');

                        // Tăng giá trị offset lên 3
                        $button.data('offset', offset + 3);

                        // Kiểm tra nếu không còn bình luận nào thì ẩn nút "Xem thêm"
                        if (!response.has_more) {
                            $button.fadeOut('slow', function() {
                                $(this).remove();
                            });
                        }
                    } else {
                        FuiToast.error(response.message);
                    }
                },
                error: function() {
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Có lỗi xảy ra, vui lòng thử lại sau!',
                    });
                }
            });
        });

        // xử lý load thêm bình luận end

        // xử lý đánh giá sao start
        const $danhGiaContainer = $('#danh-gia-container');
        const daDanhGia = $danhGiaContainer.data('da-danh-gia');

        // Nếu người dùng chưa đánh giá thì cho phép hiệu ứng hover
        if (!daDanhGia) {
            $('.icon-danh-gia').on('mouseenter', function() {
                const sao = $(this).data('sao');
                $(this).prevAll().addBack().css('filter', 'grayscale(0)');
                $(this).nextAll().css('filter', 'grayscale(100%)');
            });

            $('.icon-danh-gia').on('mouseleave', function() {
                $('.icon-danh-gia').css('filter', 'grayscale(100%)');
                $('.icon-danh-gia.active').css('filter', 'grayscale(0)');
            });
        }

        // Xử lý khi click vào quả đào để đánh giá
        $(document).on('click', '.icon-danh-gia', function() {
            // Kiểm tra người dùng đã đăng nhập chưa
            const isLoggedIn = false;
            if (!isLoggedIn) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Bạn cần đăng nhập để sử dụng tính năng này!',
                });
                return;
            }

            let sao = $(this).data('sao');
            sao = DOMPurify.sanitize(sao);
            let idTruyen = $(this).data('id-truyen');
            idTruyen = DOMPurify.sanitize(idTruyen);

            // Gửi đánh giá bằng AJAX
            $.ajax({
                url: 'sources/ajax/mongdaovien/danh-gia-truyen.php',
                type: 'POST',
                data: {
                    id_truyen: idTruyen,
                    sao: sao,
                },
                success: function(response) {
                    if (response.status === 'success') {
                        FuiToast.success('Bạn đã đánh giá thành công!');

                        // Cập nhật giao diện đánh giá
                        $('.icon-danh-gia').each(function() {
                            if ($(this).data('sao') <= sao) {
                                $(this).addClass('active').css('filter', 'grayscale(0)');
                            } else {
                                $(this).removeClass('active').css('filter', 'grayscale(100%)');
                            }
                        });

                        // Cập nhật số sao trung bình và số lượt đánh giá
                        $('#sao-trung-binh').text(response.sao_trung_binh);
                        $('#danh-gia').text(response.count_bl);
                    } else {
                        FuiToast.error(response.message);
                    }
                },
                error: function() {
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Có lỗi xảy ra, vui lòng thử lại sau!',
                    });
                }
            });
        });

        // xử lý đánh giá sao end


        // dropdown sửa truyện start
        $('.btn-product-show-edit-comic').on('click', function() {
            const $dropdown = $(this).next('.edit-comic-dropdown');

            if ($dropdown.hasClass('d-none')) {
                $dropdown.removeClass('d-none').hide().fadeIn('slow');
            } else {
                $dropdown.fadeOut('slow', function() {
                    $(this).addClass('d-none');
                });
            }
        });

        // Hide dropdown when clicking outside
        $(document).on('click', function(event) {
            if (!$(event.target).closest('.dropdown').length) {
                $('.edit-comic-dropdown').removeClass('show');
            }
        });

        // dropdown sửa truyện end

    });
</script>


<!-- mua combo trigger modal -->
<script>
    $(document).on("click", ".button-mua-combo-truyen-ne", function() {
        const idUser = null;
        // Kiểm tra người dùng đã đăng nhập chưa
        if (idUser === null) {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Bạn cần đăng nhập để sử dụng tính năng này!',
            });
            return;
        }
        const gia_combo = 0;
        if (gia_combo <= 0) {
            FuiToast.error("Truyện này chưa mở bán Combo");
            return;
        }

        if ($(this).hasClass('da-mua')) {
            FuiToast.success("Bạn đã mua combo truyện này.");
            return;
        }


        let idTruyen = $(this).data("id-truyen");
        $("#comboPurchaseModal").modal("show");
    });

    // Xử lý khi click vào nút Mua Combo Ngay
    $(document).on("click", ".combo-buy-button", function() {

        const idUser = null;
        // Kiểm tra người dùng đã đăng nhập chưa
        if (idUser === null) {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Bạn cần đăng nhập để sử dụng tính năng này!',
            });
            return;
        }



        // Kiểm tra Đào sau khi mua
        let daoSauKhiMua = $("#gia-dao-sau-mua").text().trim();

        if (daoSauKhiMua === "Không đủ Đào") {
            FuiToast.error("Bạn không đủ Đào để mua combo này. Hãy nạp thêm.");
            return;
        }




        // SweetAlert2 - Hỏi người dùng xác nhận
        Swal.fire({
            title: 'Xác nhận mua Combo',
            text: `Bạn có chắc mua combo truyện này không? Sẽ tốn ${$('#gia-dao-tieu-ton').text().trim()} Đào`,
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Đồng ý'
        }).then((result) => {
            if (result.isConfirmed) {
                // Gửi yêu cầu AJAX mua combo
                $.ajax({
                    url: 'sources/ajax/mongdaovien/mua-combo.php',
                    type: 'POST',
                    dataType: 'json',
                    data: {
                        id_truyen: '2436',
                        gia_combo: 0                    },
                    success: function(response) {
                        if (response.status === 'success') {
                            FuiToast.success("Mua combo truyện thành công!");
                            $(".combo-purchase-form-container").addClass("combo-purchase-form-container-success");
                            $(".combo-purchase-form-container").html(`
                                <div class="combo-purchase-success">
                                    <h3 class="combo-title">Mua Combo Thành Công</h3>
                                    <p class="combo-description">Bạn đã sở hữu toàn bộ chương của truyện này.</p>
                                </div>
                            `);

                            // Cập nhật lại Đào của tài khoản
                            $(".dao-dang-co").text(response.dao_hien_tai);
                            $(".hat-dang-co").text(response.hat_hien_tai);
                            $(".bong-dang-co").text(response.bong_hien_tai);

                            // thêm class đã mua

                            $(".button-mua-combo-truyen-ne").addClass('da-mua');

                            // Tải lại danh sách chương sau khi mua
                            $('#result-chuong').fadeOut(500, function() {
                                $.ajax({
                                    url: 'sources/ajax/mongdaovien/load-chuong.php',
                                    type: 'GET',
                                    data: {
                                        id_truyen: '2436'
                                    },
                                    success: function(newContent) {
                                        $('#result-chuong').html(newContent).fadeIn(500);
                                    },
                                    error: function() {
                                        FuiToast.error('Có lỗi xảy ra khi tải lại danh sách chương');
                                    }
                                });
                            });

                            // Đóng modal sau 1-2 giây
                            setTimeout(function() {
                                $("#comboPurchaseModal").modal("hide");
                            }, 1500);


                        } else {
                            FuiToast.error(response.message);
                        }
                    },
                    error: function() {
                        FuiToast.error("Đã xảy ra lỗi trong quá trình mua combo.");
                    }
                });
            }
        });
    });


    $(document).ready(function() {
        // ID của truyện hiện tại
        var idTruyen = 2436;
        var truyen18Key = "truyen_18_" + idTruyen;

        // Kiểm tra xem đã lưu id_truyen_18 vào localStorage chưa
        if (!localStorage.getItem(truyen18Key)) {
            // Nếu chưa lưu, hiển thị overlay
            // $('.gioi-han-do-tuoi-overlay').show();
            $('.gioi-han-do-tuoi-overlay').fadeIn(500);
        } else {
            // Nếu đã lưu, ẩn overlay ngay lập tức
            $('.gioi-han-do-tuoi-overlay').hide();
        }

        // Khi người dùng nhấn vào nút "Đã hiểu và muốn tiếp tục"
        $('.gioi-han-do-tuoi-btn-continue').on('click', function() {
            // Lưu ID truyện vào localStorage
            localStorage.setItem(truyen18Key, true);

            // Tắt overlay với hiệu ứng mờ dần
            $('.gioi-han-do-tuoi-overlay').fadeOut(300);
        });


        // SỬA THÔNG BÁO TỪ DỊCH TÁC GIẢ START

        // Khởi tạo EmojioneArea cho modal chỉnh sửa
        if (window.innerWidth > 1024) {
            $("#emojioneareaThongBao").emojioneArea({
                pickerPosition: "right",
                filtersPosition: "bottom",
                tonesStyle: "square",
                placeholder: "Nhập nội dung thông báo..."
            });
        } else {
            $("#emojioneareaThongBao").emojioneArea({
                pickerPosition: "top",
                filtersPosition: "bottom",
                tonesStyle: "square",
                placeholder: "Nhập nội dung thông báo..."
            });
        }

        // Hiển thị modal khi click nút chỉnh sửa
        $(".click-sua-thong-bao").on("click", function() {
            // const thongBaoHienTai = $("#profileIntroduce").text().trim(); // Lấy nội dung hiện tại
            // $("#emojioneareaThongBao")[0].emojioneArea.setText(thongBaoHienTai); // Đưa nội dung vào EmojioneArea
            $("#editThongBaoModal").modal("show");
        });

        // Xử lý lưu thông báo
        $("#saveThongBaoBtn").on("click", function() {
            let noiDung = $("#emojioneareaThongBao")[0].emojioneArea.getText(); // Lấy nội dung từ EmojioneArea
            noiDung = DOMPurify.sanitize(noiDung); // Làm sạch nội dung để chống XSS

            // Kiểm tra nội dung
            if (!noiDung.trim()) {
                Swal.fire({
                    icon: "warning",
                    title: "Nội dung trống",
                    text: "Vui lòng nhập nội dung thông báo!"
                });
                return;
            }

            // Gửi AJAX để lưu thông báo
            $.ajax({
                url: "sources/ajax/mongdaovien/cap-nhat-thong-bao.php", // Endpoint xử lý
                type: "POST",
                dataType: "json",
                data: {
                    id_truyen: 2436,
                    thong_bao: noiDung
                },
                success: function(response) {
                    if (response.status === "success") {
                        FuiToast.success("Thông báo đã được cập nhật thành công!");
                        $("#editThongBaoModal").modal("hide");
                        $("#profileIntroduce").html(noiDung); // Cập nhật nội dung mới vào giao diện
                    } else {
                        FuiToast.error(response.message);
                    }
                },
                error: function() {
                    FuiToast.error("Có lỗi xảy ra, vui lòng thử lại sau!");
                }
            });
        });
        // SỬA THÔNG BÁO TỪ DỊCH TÁC GIẢ END


        // XỬ LÝ THÊM VÀO DANH SÁCH ĐỌC START
        $(".btn-add-danh-sach-doc").on("click", function(e) {
            e.preventDefault();

            let $this = $(this); // Đối tượng hiện tại
            let idDanhSach = $this.data("id"); // ID của danh sách đọc
            let idTruyen = $this.data("truyen"); // ID của truyện

            // Hiệu ứng fade
            $this.fadeTo(200, 0.5);

            $.ajax({
                url: "sources/ajax/mongdaovien/ajax_danh_sach_doc.php",
                type: "POST",
                dataType: "json",
                data: {
                    id_danhsachdoc: idDanhSach,
                    id_truyen: idTruyen
                },
                success: function(response) {
                    if (response.status === "added") {
                        // Nếu thêm thành công, thêm dấu check
                        $this.find(".btn-add-danh-sach-doc-right").html('<i class="fa-solid fa-check text-success"></i>');
                        FuiToast.success("Thêm vào danh sách đọc thành công!");
                    } else if (response.status === "removed") {
                        // Nếu xóa thành công, xóa dấu check
                        $this.find(".btn-add-danh-sach-doc-right").html("");
                        FuiToast.info("Đã xóa khỏi danh sách đọc!");
                    } else {
                        FuiToast.error("Có lỗi xảy ra: " + response.message);
                    }
                },
                error: function() {
                    FuiToast.error("Đã xảy ra lỗi. Vui lòng thử lại!");
                },
                complete: function() {
                    $this.fadeTo(200, 1); // Hoàn tất hiệu ứng
                }
            });
        });
        // XỬ LÝ THÊM VÀO DANH SÁCH ĐỌC END


        // XỬ LÝ ĐỌC TIẾP START
        $(".btn-doc-tiep").on("click", function() {
            const idTruyen = 2436; // Lấy ID truyện
            const lastChapter = JSON.parse(localStorage.getItem("lastChapter")) || {};
            const lastReadChapter = lastChapter[idTruyen] || {
                id: 1,
                so_thu_tu: 1
            }; // Mặc định chương 1

            // Gửi AJAX để lấy so_thu_tu từ server
            $.ajax({
                url: "sources/ajax/mongdaovien/get_chapter.php",
                type: "POST",
                dataType: "json",
                data: {
                    id_chapter: lastReadChapter.id
                },
                success: function(response) {
                    if (response.status === "success") {
                        var soThuTu = response.so_thu_tu;
                        if (soThuTu < 1) {
                            soThuTu = 1;
                        }
                        // Hiển thị modal
                        $(".modal-doc-tiep-chapter").text(`Chương ${soThuTu}`);
                        $(".modal-doc-tiep-wrapper").fadeIn();

                        // Sự kiện khi chọn "Đọc tiếp"
                        $(".modal-doc-tiep-read-continue").on("click", function() {
                            const nextChapterUrl = `https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=${soThuTu}`;
                            window.location.href = nextChapterUrl;
                        });

                        // Sự kiện khi chọn "Đọc từ đầu"
                        $(".modal-doc-tiep-read-start-over").on("click", function() {
                            const startOverUrl = `https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=1`;
                            window.location.href = startOverUrl;
                        });

                        // Đóng modal
                        $(".modal-doc-tiep-close, .modal-doc-tiep-backdrop").on("click", function() {
                            $(".modal-doc-tiep-wrapper").fadeOut();
                        });
                    } else {
                        FuiToast.error(response.message || "Không thể tải chương gần nhất.");
                    }
                },
                error: function() {
                    FuiToast.error("Đã xảy ra lỗi khi tải chương gần nhất.");
                },
            });
        });


        // XỬ LÝ ĐỌC TIẾP END

    });
</script>

<!-- Scripts xử lý chức năng yêu thích truyện -->
<script>
    $(document).ready(function() {
        // Xử lý sự kiện click vào nút yêu thích
        $('.btn-yeu-thich-truyen').on('click', function() {
            var idTruyen = $(this).data('id');
            var btnYeuThich = $(this);

            // Gửi AJAX request
            $.ajax({
                url: 'https://tehitruyen.com/sources/ajax/mongdaovien/yeu-thich-truyen.php',
                type: 'POST',
                dataType: 'json',
                data: {
                    id_truyen: idTruyen,
                    id_chapter: 0 // Có thể thay đổi nếu cần
                },
                success: function(response) {
                    if (response.status === 1 || response.status === '1' || response.status === 'success') {
                        // Thành công
                        Swal.fire({
                            title: 'Thành công!',
                            text: response.message,
                            icon: 'success',
                            confirmButtonText: 'Đóng'
                        });

                        // Cập nhật UI tùy theo action
                        if (response.action === 'liked') {
                            btnYeuThich.addClass('da-thich');
                            btnYeuThich.find('i').addClass('text-danger');
                            btnYeuThich.html('<i class="fa-solid fa-heart hvr-icon text-danger"></i> Đã yêu thích');
                        } else if (response.action === 'unliked') {
                            btnYeuThich.removeClass('da-thich');
                            btnYeuThich.find('i').removeClass('text-danger');
                            btnYeuThich.html('<i class="fa-solid fa-heart hvr-icon"></i> Yêu thích');
                        }
                        // Cập nhật lại số lượt thích
                        if (response.tong_luot_thich !== undefined) {
                            $('.luot-thich-text').text(response.tong_luot_thich);
                        }
                    } else if (response.status === 2 || response.status === '2') {
                        // Chưa đăng nhập
                        Swal.fire({
                            title: 'Thông báo!',
                            text: 'Bạn cần đăng nhập để sử dụng tính năng này!',
                            icon: 'warning',
                            confirmButtonText: 'Đăng nhập ngay',
                            showCancelButton: true,
                            cancelButtonText: 'Để sau'
                        }).then((result) => {
                            if (result.isConfirmed) {
                                // Chuyển đến trang đăng nhập
                                window.location.href = 'https://tehitruyen.com/dang-nhap.html';
                            }
                        });
                    } else {
                        // Lỗi khác
                        Swal.fire({
                            title: 'Lỗi!',
                            text: response.message,
                            icon: 'error',
                            confirmButtonText: 'Đóng'
                        });
                    }
                },
                error: function(xhr, status, error) {
                    // Xử lý lỗi AJAX
                    Swal.fire({
                        title: 'Lỗi kết nối!',
                        text: 'Đã xảy ra lỗi khi kết nối đến máy chủ.',
                        icon: 'error',
                        confirmButtonText: 'Thử lại'
                    });
                    console.error(xhr, status, error);
                }
            });
        });
    });
</script>  </div>

  <!-- Google AdSense Display -->
  <div class="adsense-container">
    <ins class="adsbygoogle"
      style="display:block"
      data-ad-format="autorelaxed"
      data-ad-client="ca-pub-2935799637584410"
      data-ad-slot="8234900970"></ins>
    <script>
      (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
  </div>

    
<!-- quảng cáo footer start -->
<div class="tm-footer-wrapper" style="--background-footer: url('https://tehitruyen.com/img_data/images/nen_trang.jpg')">
    <div class="tm-footer-wrapper-container container px-0">

                    <div class="nh-footer-ads">
                <div class="">
                    <div class="nh-footer-ads-box-wrapper p-2">
                        <div class="nh-footer-ads-box position-relative ">
                            <img src="https://tehitruyen.com/img_data/images/Me_Zhihu_-_O_nha_be_Chanh_TeHi_Truyen_1.png" alt="Banner quảng cáo dưới footer" class="nh-footer-ads-img">

                            <!-- theo dõi button start -->
                            <div class="theo-doi-footer-box d-flex justify-content-between align-items-end gap-2">
                                                                    <a href='https://web.facebook.com/chanhvotree05'  rel='follow'  class="nh-footer-ads-btn">
                                        Page Chanh                                    </a>
                                                                    <a href='https://www.facebook.com/groups/490110827304708'  rel='follow'  class="nh-footer-ads-btn">
                                        Mê Zhihu                                    </a>
                                                            </div>

                            <!-- theo dõi button end -->
                        </div>
                    </div>

                </div>
            </div>
            <!-- quảng cáo footer end -->
        
        
<?php endwhile; endif; ?>
<?php get_footer(); ?>