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
    

<section class="msv-san-pham-detail mdv-san-pham-detail ">
    <div class="container">
        <div class="mdv-san-pham-detail-box rounded p-3 position-relative mb-5 mb-lg-5">
            <!-- khung tool start -->
            <div class="mdv-san-pham-detail-khung-tool ">
                <div class="mdv-san-pham-detail-khung-tool-box ">
                    <ul class="vanhiep-ul d-flex flex-column mdv-san-pham-detail-khung-tool-box-ul ">


                        <!-- chế độ sáng tối -->
                        <li class="btn-che-do-sang-toi">
                            <a class="d-inline-flex " data-bs-toggle="tooltip" data-bs-placement="left" title="Chế độ sáng/tối">
                                <i class="fa-solid fa-moon"></i>
                            </a>
                        </li>
                        <!-- chỉnh cỡ chữ -->
                        <li class="btn-chinh-co-chu-tool position-relative">
                            <a class="d-inline-flex ">
                                <i class="fa-solid fa-a"></i>
                            </a>
                        </li>

                    </ul>

                    <!-- Box chỉnh cỡ chữ nằm bên trái của nút chỉnh cỡ chữ -->
                    <div id="fontSizeBox" class="font-size-box d-none">
                        <label for="fontSizeRange" class="font-size-label">Chỉnh cỡ chữ</label>
                        <input type="range" id="fontSizeRange" min="12" max="32" value="18"
                            style=" border-radius: 15px; outline: none; cursor: pointer; touch-action: manipulation;">

                        <!-- HTML -->
                        <div class="toggle-switch">
                            <label for="removeBreaksToggle" class="font-size-label">Ẩn Dấu Xuống Dòng</label>
                            <input type="checkbox" id="removeBreaksToggle">
                            <span class="slider"></span>
                        </div>

                    </div>

                    <!-- Danh sách chương, sẽ ẩn khi trang tải -->
                    <div class="msv-chuong-list-container-left" id="chuongListLeft">
                        <ul class="msv-chuong-list p-0">
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=1" class="msv-chuong-link">
                                        <span class="msv-chuong-title ">Chương 1:</span>
                                    </a>
                                </li>
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=2" class="msv-chuong-link">
                                        <span class="msv-chuong-title ">Chương 2:</span>
                                    </a>
                                </li>
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=3" class="msv-chuong-link">
                                        <span class="msv-chuong-title ">Chương 3:</span>
                                    </a>
                                </li>
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=4" class="msv-chuong-link">
                                        <span class="msv-chuong-title ">Chương 4:</span>
                                    </a>
                                </li>
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=5" class="msv-chuong-link">
                                        <span class="msv-chuong-title ">Chương 5:</span>
                                    </a>
                                </li>
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=6" class="msv-chuong-link">
                                        <span class="msv-chuong-title ">Chương 6:</span>
                                    </a>
                                </li>
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=7" class="msv-chuong-link">
                                        <span class="msv-chuong-title ">Chương 7:</span>
                                    </a>
                                </li>
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=8" class="msv-chuong-link">
                                        <span class="msv-chuong-title ">Chương 8:</span>
                                    </a>
                                </li>
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=9" class="msv-chuong-link">
                                        <span class="msv-chuong-title ">Chương 9:</span>
                                    </a>
                                </li>
                                                    </ul>
                    </div>


                </div>
            </div>
            <!-- khung tool end -->
            <!-- breadcrumb start -->
                        <nav aria-label="breadcrumb " class="mdv-doc-truyen-breadcrumb px-3 py-2 rounded-3 ">
                <ol class="breadcrumb">
                    <li class="breadcrumb-item"><a href="https://tehitruyen.com/">Trang chủ</a></li>
                    <li class="breadcrumb-item"><a href='https://tehitruyen.com/hoan-thanh.html' >Truyện hoàn thành</a></li>
                    <li class="breadcrumb-item"><a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html">Triều Đình Không Dung Nữ Nhân? Ta Là Ngoại Lệ</a></li>
                    <li class="breadcrumb-item active" aria-current="page"><a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=1">Chương 1</a></li>
                </ol>
            </nav>
            <!-- breadcrumb end -->
            <!-- Chương title start -->
            <div class="mdv-san-pham-detail-chuong-title text-center">
                <span class="mdv-san-pham-detail-chuong-title-label"><span class="mdv-san-pham-detail-chuong-title-text">Chương 1:</span>
            </div>
            <!-- Chương Title End -->
            <!-- thời gian đăng,lượt xem, bình luận start -->
            <div class="mdv-san-pham-detail-tgian-lx-bl-box mb-3 mb-lg-3 d-flex flex-column flex-md-row justify-content-center align-items-center gap-1 gap-md-3">
                <div class="mdv-san-pham-detail-tgian">
                    <small> <i class="fa-regular fa-clock"></i> Đăng lúc 17:31 - 10/04/2026</small>
                </div>
                <div class="mdv-san-pham-detail-lx-bl d-inline-flex align-items-center gap-2">
                    <div class="mdv-san-pham-detail-lx">
                        <small><i class="fa-solid fa-eye"></i> 16</small>
                    </div>
                    <div class="mdv-san-pham-detail-bl">
                        <small> <i class="fa-solid fa-comments"></i> 0</small>
                    </div>
                </div>
            </div>
            <!-- thời gian đăng,lượt xem, bình luận end -->

            <!-- Chương Trước, Sau Start -->
            <div class="mdv-breadcrumb-chuong-box d-flex justify-content-center  gap-1 position-relative">
                <!-- Nút Chương Trước -->
                <a href="#" class="d-inline-flex  mdv-chuong-button mdv-chuong-button-truoc hvr-icon-back disabled" style="pointer-events: none; filter: grayscale(100%); background-color: #d3d3d3;">
                    <i class="fa-solid fa-arrow-left-long hvr-icon"></i>
                    <span class="mdv-chuong-button-text">Trước</span>
                </a>

                <!-- Nút Tìm Chương -->
                <div class="h-100 mdv-chuong-button-tim-box position-relative">
                    <a class="mdv-chuong-button mdv-chuong-button-tim hvr-icon-pulse-grow" id="timChuongBtn">
                        <i class="fa-solid fa-list hvr-icon"></i>
                        <span class="mdv-chuong-button-text">Chương 1</span>
                    </a>
                    <!-- Danh sách chương, sẽ ẩn khi trang tải -->
                    <div class="msv-chuong-list-container position-absolute" id="chuongList" style="display: none;">
                        <ul class="msv-chuong-list p-0">
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=1" title="Chương 1:" class="msv-chuong-link">
                                        <span class="msv-chuong-number ">Chương 1:</span>
                                    </a>
                                </li>
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=2" title="Chương 2:" class="msv-chuong-link">
                                        <span class="msv-chuong-number ">Chương 2:</span>
                                    </a>
                                </li>
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=3" title="Chương 3:" class="msv-chuong-link">
                                        <span class="msv-chuong-number ">Chương 3:</span>
                                    </a>
                                </li>
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=4" title="Chương 4:" class="msv-chuong-link">
                                        <span class="msv-chuong-number ">Chương 4:</span>
                                    </a>
                                </li>
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=5" title="Chương 5:" class="msv-chuong-link">
                                        <span class="msv-chuong-number ">Chương 5:</span>
                                    </a>
                                </li>
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=6" title="Chương 6:" class="msv-chuong-link">
                                        <span class="msv-chuong-number ">Chương 6:</span>
                                    </a>
                                </li>
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=7" title="Chương 7:" class="msv-chuong-link">
                                        <span class="msv-chuong-number ">Chương 7:</span>
                                    </a>
                                </li>
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=8" title="Chương 8:" class="msv-chuong-link">
                                        <span class="msv-chuong-number ">Chương 8:</span>
                                    </a>
                                </li>
                                                            <li class="msv-chuong-item">
                                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=9" title="Chương 9:" class="msv-chuong-link">
                                        <span class="msv-chuong-number ">Chương 9:</span>
                                    </a>
                                </li>
                                                    </ul>
                    </div>
                </div>

                <!-- Nút Chương Sau -->
                <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=2" class="d-inline-flex mdv-chuong-button mdv-chuong-button-sau hvr-icon-forward " style="">
                    <span class="mdv-chuong-button-text">Sau</span>
                    <i class="fa-solid fa-arrow-right-long hvr-icon"></i>
                </a>
            </div>
            <!-- Chương Trước, Sau End -->



            <!-- KHUNG TRUYỆN START -->
            <div class="msv-khung-truyen mdv-khung-truyen px-2  p-lg-3 pt-4 ">
                <input type="hidden" name="coin_chapter" id="coin_chapter" value="0">
                <input type="hidden" name="id_truyen" id="id_truyen" value="2436">
                <input type="hidden" name="chapter_tap" id="chapter_tap" value="1">
                <input type="hidden" name="username" id="username" value="">

                <!-- Thông báo affiliate Shopee -->
                                    <div id="affiliate-notification" class="affiliate-notification">
                        <div class="affiliate-overlay"></div>
                        <div class="affiliate-modal">
                            <div class="affiliate-modal-header">
                                <div class="affiliate-logo">
                                                                        <img src="https://tehitruyen.com/img_data/images/logo-tehitruyen-v1-nen_anh.png" alt="Logo">
                                </div>
                                <h3 class="affiliate-title">Thông Báo Đặc Biệt</h3>
                            </div>
                            <div class="affiliate-modal-body">
                                <div class="affiliate-content">
                                                                <p style="text-align: center;">
                                <span style="font-size: 18px; font-weight: bold; color: #e43f5a;">Chương này có quảng cáo!</span>
                            </p>
                            <p><br></p><ol>
                                <li>Nội dung chương sẽ tự động hiển thị sau khi bạn nhấp vào liên kết</li>
                            </ol>
                            <p style="text-align: center;"><strong>Cảm ơn bạn đã ủng hộ chúng tôi!</strong></p>
                                                        </div>
                                <div class="affiliate-cta">
                                    <a href="https://s.shopee.vn/1BHSFYKG55"
                                        class="affiliate-button"
                                        target="_blank"
                                        id="affiliate-link"
                                        data-truyen-id="2436"
                                        onclick="return trackAffiliateClick(2436)">
                                        <span class="affiliate-button-text">Tiếp Tục Đọc Truyện</span>
                                        <span class="affiliate-button-icon">
                                            <i class="fas fa-arrow-right"></i>
                                        </span>
                                    </a>
                                </div>
                            </div>
                            <div class="affiliate-modal-footer">
                                <div class="affiliate-disclaimer">
                                    <p>Đây là liên kết quảng cáo từ nhà tài trợ của chúng tôi</p>
                                </div>
                            </div>
                        </div>
                    </div>
                
                <style>
                    .affiliate-notification {
                        position: fixed;
                        top: 0;
                        left: 0;
                        width: 100%;
                        height: 100%;
                        z-index: 9999;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    }

                    .affiliate-overlay {
                        position: absolute;
                        top: 0;
                        left: 0;
                        width: 100%;
                        height: 100%;
                        background: rgba(0, 0, 0, 0.7);
                        backdrop-filter: blur(5px);
                    }

                    .affiliate-modal {
                        position: relative;
                        width: 90%;
                        max-width: 550px;
                        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
                        border-radius: 15px;
                        overflow: hidden;
                        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
                        color: #fff;
                        border: 1px solid rgba(255, 255, 255, 0.1);
                        animation: modalFadeIn 0.5s ease forwards;
                    }

                    @keyframes modalFadeIn {
                        from {
                            opacity: 0;
                            transform: translateY(50px);
                        }

                        to {
                            opacity: 1;
                            transform: translateY(0);
                        }
                    }

                    .affiliate-modal-header {
                        padding: 25px;
                        text-align: center;
                        background: linear-gradient(135deg, #0f3460 0%, #1a1a2e 100%);
                        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                        position: relative;
                    }

                    .affiliate-logo {
                        margin-bottom: 15px;
                    }

                    .affiliate-logo img {
                        height: 60px;
                        filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.3));
                    }

                    .affiliate-title {
                        margin: 0;
                        font-size: 24px;
                        font-weight: 700;
                        color: #fff;
                        text-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
                        letter-spacing: 1px;
                    }

                    .affiliate-modal-body {
                        padding: 30px;
                    }

                    .affiliate-content {
                        margin-bottom: 25px;
                        font-size: 16px;
                        line-height: 1.6;
                        color: rgba(255, 255, 255, 0.9);
                        text-align: center;
                    }

                    .affiliate-content img {
                        max-width: 100%;
                        border-radius: 8px;
                        margin: 15px 0;
                    }

                    .affiliate-cta {
                        text-align: center;
                        margin: 30px 0 15px;
                    }

                    .affiliate-button {
                        display: inline-flex;
                        align-items: center;
                        justify-content: center;
                        padding: 14px 32px;
                        background: linear-gradient(135deg, #e94560 0%, #e43f5a 100%);
                        color: #fff;
                        text-decoration: none;
                        border-radius: 50px;
                        font-weight: 600;
                        font-size: 16px;
                        transition: all 0.3s ease;
                        box-shadow: 0 10px 20px rgba(233, 69, 96, 0.3);
                        border: none;
                        cursor: pointer;
                        position: relative;
                        overflow: hidden;
                    }

                    .affiliate-button::before {
                        content: '';
                        position: absolute;
                        top: 0;
                        left: -100%;
                        width: 100%;
                        height: 100%;
                        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
                        transition: all 0.6s ease;
                    }

                    .affiliate-button:hover {
                        transform: translateY(-5px);
                        box-shadow: 0 15px 25px rgba(233, 69, 96, 0.4);
                        color: #fff;
                        text-decoration: none;
                    }

                    .affiliate-button:hover::before {
                        left: 100%;
                    }

                    .affiliate-button-text {
                        margin-right: 10px;
                    }

                    .affiliate-button-icon {
                        display: inline-flex;
                        align-items: center;
                        justify-content: center;
                    }

                    .affiliate-modal-footer {
                        padding: 15px 30px;
                        background: rgba(0, 0, 0, 0.2);
                        border-top: 1px solid rgba(255, 255, 255, 0.05);
                    }

                    .affiliate-disclaimer {
                        font-size: 12px;
                        color: rgba(255, 255, 255, 0.5);
                        text-align: center;
                    }

                    /* Hiệu ứng pulsating cho nút */
                    @keyframes pulse {
                        0% {
                            box-shadow: 0 0 0 0 rgba(233, 69, 96, 0.7);
                        }

                        70% {
                            box-shadow: 0 0 0 15px rgba(233, 69, 96, 0);
                        }

                        100% {
                            box-shadow: 0 0 0 0 rgba(233, 69, 96, 0);
                        }
                    }

                    .affiliate-button {
                        animation: pulse 1.5s infinite;
                    }

                    .hidden-content {
                        display: none;
                    }
                </style>



                <!-- Nội dung truyện -->
                <div class="msv-khung-truyen-noi-dung py-3 doc-quyen watermarked-content" style="--text-copyright: 'Độc quyền tại Tehitruyen'">

                    <div id="noi_dung_truyen" class="hidden-content">
                        
                            <?php the_content(); ?>
</div>

                </div>
                <!-- Nội dung Truyện end -->



                <!-- chương trước, sau 2 start -->
                <div class="mdv-breadcrumb-chuong-box mdv-breadcrumb-chuong-box-2 mt-3 d-flex justify-content-center align-items-center gap-1 position-relative">
                    <!-- Nút Chương Trước -->
                    <a href="#" class="mdv-chuong-button mdv-chuong-button-truoc hvr-icon-back disabled" style="pointer-events: none; filter: grayscale(100%); background-color: #d3d3d3;">
                        <i class="fa-solid fa-arrow-left-long hvr-icon"></i>
                        <span class="mdv-chuong-button-text">Trước</span>
                    </a>
                    <!-- Nút Tìm Chương -->
                    <div class="mdv-chuong-button-tim-box position-relative">
                        <a class="mdv-chuong-button mdv-chuong-button-tim hvr-icon-pulse-grow" id="timChuongBtn2">
                            <i class="fa-solid fa-list hvr-icon"></i>
                            <span class="mdv-chuong-button-text"> Chương 1</span>
                        </a>
                        <!-- Danh sách chương, sẽ ẩn khi trang tải -->
                        <div class="msv-chuong-list-container msv-chuong-list-container-2 position-absolute" id="chuongList2" style="display: none;">
                            <ul class="msv-chuong-list p-0">
                                                                    <li class="msv-chuong-item">
                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=1" title="Chương 1:" class="msv-chuong-link">
                                            <span class="msv-chuong-number ">Chương 1:</span>
                                        </a>
                                    </li>
                                                                    <li class="msv-chuong-item">
                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=2" title="Chương 2:" class="msv-chuong-link">
                                            <span class="msv-chuong-number ">Chương 2:</span>
                                        </a>
                                    </li>
                                                                    <li class="msv-chuong-item">
                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=3" title="Chương 3:" class="msv-chuong-link">
                                            <span class="msv-chuong-number ">Chương 3:</span>
                                        </a>
                                    </li>
                                                                    <li class="msv-chuong-item">
                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=4" title="Chương 4:" class="msv-chuong-link">
                                            <span class="msv-chuong-number ">Chương 4:</span>
                                        </a>
                                    </li>
                                                                    <li class="msv-chuong-item">
                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=5" title="Chương 5:" class="msv-chuong-link">
                                            <span class="msv-chuong-number ">Chương 5:</span>
                                        </a>
                                    </li>
                                                                    <li class="msv-chuong-item">
                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=6" title="Chương 6:" class="msv-chuong-link">
                                            <span class="msv-chuong-number ">Chương 6:</span>
                                        </a>
                                    </li>
                                                                    <li class="msv-chuong-item">
                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=7" title="Chương 7:" class="msv-chuong-link">
                                            <span class="msv-chuong-number ">Chương 7:</span>
                                        </a>
                                    </li>
                                                                    <li class="msv-chuong-item">
                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=8" title="Chương 8:" class="msv-chuong-link">
                                            <span class="msv-chuong-number ">Chương 8:</span>
                                        </a>
                                    </li>
                                                                    <li class="msv-chuong-item">
                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=9" title="Chương 9:" class="msv-chuong-link">
                                            <span class="msv-chuong-number ">Chương 9:</span>
                                        </a>
                                    </li>
                                                            </ul>
                        </div>

                    </div>



                    <!-- Nút Chương Sau -->
                    <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=2" class="mdv-chuong-button mdv-chuong-button-sau hvr-icon-forward " style="">
                        <span class="mdv-chuong-button-text">Sau</span>
                        <i class="fa-solid fa-arrow-right-long hvr-icon"></i>
                    </a>
                </div>
                <!-- chương trước, sau 2 end -->



            </div>

            <!-- KHUNG TRUYỆN END -->

        </div>


        <!-- bình luận, truyện đề cử start -->
        <div class="mdv-binh-luan-truyen-de-cu-container overflow-visible mt-3 mt-lg-4">
            <div class="row gx-4 gy-5">

                <!-- bình luận start -->
                <div class="col-12 col-lg-8 position-relative" style="z-index:6">
                    <div class="mdv-san-pham-show-comment pt-0 pt-lg-0 px-0">

                                                <!-- title start -->
                        <div class="bee-gioi-thieu-truyen-title-box w-100 position-relative text-center ">
                            <div class="bee-gioi-thieu-truyen-title d-inline-flex text-uppercase px-3 py-2 rounded-pill">
                                Bình Luận (<span class="bl-number">0</span>)
                            </div>
                        </div>
                        <!-- title end -->



                        <!-- content start -->
                        <div class="mdv-san-pham-show-comment-box p-2">
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
                                                        Chương này chưa có bình luận nào
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
                </div>

                <!-- bình luận end -->


                <!-- truyện đề cử start -->
                                <div class="col-12 col-lg-4">
                    <div class="mdv-san-pham-detail-truyen-de-cu-container rounded px-0 pt-0 pb-3">
                        <!-- title start -->
                        <div class="bee-gioi-thieu-truyen-title-box w-100 position-relative text-center d-block d-lg-none ">
                            <div class="bee-gioi-thieu-truyen-title d-inline-flex text-uppercase px-3 py-2 rounded-pill">
                                Truyện Cùng Thể Loại
                            </div>
                        </div>
                        <!-- title end -->
                        <h5 class="truyen-de-cu-title mb-4 d-none d-lg-block pt-3">truyện cùng thể loại</h5>
                        <!-- pc start -->
                        <div class="truyen-de-cu-list d-none d-lg-block px-3">
                                                            <div class="truyen-de-cu-item d-flex align-items-center gap-3 mb-3">
                                    <div class="truyen-de-cu-image">
                                        <div class="top-item-comic-image-book-cover position-relative">
                                            <div class="top-item-comic-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html">
                                                    <img src="https://tehitruyen.com/img_data/images/anh_truyen/2436.jpg" alt="Trận Văn Trường Sinh">
                                                </a>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="truyen-de-cu-info">
                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html" class="truyen-de-cu-title-link">Triều Đình Không Dung Nữ Nh...</a>
                                        <div class="truyen-de-cu-meta d-flex flex-column align-items-center align-items-lg-start">
                                            <span class="truyen-tacgia"><i class="fa-solid fa-book-open"></i> Tác giả: <span class="truyen-tacgia-text">Đang cập nhật</span></span>
                                            <span class="truyen-luotxem"><i class="fa-solid fa-eye"></i> <span class="luot-xem-span me-1">Lượt xem:</span> 409</span>
                                        </div>
                                    </div>
                                </div>
                                                            <div class="truyen-de-cu-item d-flex align-items-center gap-3 mb-3">
                                    <div class="truyen-de-cu-image">
                                        <div class="top-item-comic-image-book-cover position-relative">
                                            <div class="top-item-comic-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/thanh-chu-hoang-mac-da-la-gi.html">
                                                    <img src="https://tehitruyen.com/img_data/images/anh_truyen/2249.jpg" alt="Trận Văn Trường Sinh">
                                                </a>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="truyen-de-cu-info">
                                        <a href="https://tehitruyen.com/thanh-chu-hoang-mac-da-la-gi.html" class="truyen-de-cu-title-link">Thành Chủ Hoang Mạc Đã Là Gì</a>
                                        <div class="truyen-de-cu-meta d-flex flex-column align-items-center align-items-lg-start">
                                            <span class="truyen-tacgia"><i class="fa-solid fa-book-open"></i> Tác giả: <span class="truyen-tacgia-text">Đang cập nhật</span></span>
                                            <span class="truyen-luotxem"><i class="fa-solid fa-eye"></i> <span class="luot-xem-span me-1">Lượt xem:</span> 894</span>
                                        </div>
                                    </div>
                                </div>
                                                            <div class="truyen-de-cu-item d-flex align-items-center gap-3 mb-3">
                                    <div class="truyen-de-cu-image">
                                        <div class="top-item-comic-image-book-cover position-relative">
                                            <div class="top-item-comic-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/ta-cung-ca-ca-trong-sinh-thay-doi-ket-cuc.html">
                                                    <img src="https://tehitruyen.com/img_data/images/anh_truyen/2250.jpg" alt="Trận Văn Trường Sinh">
                                                </a>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="truyen-de-cu-info">
                                        <a href="https://tehitruyen.com/ta-cung-ca-ca-trong-sinh-thay-doi-ket-cuc.html" class="truyen-de-cu-title-link">Ta Cùng Ca Ca Trọng Sinh Th...</a>
                                        <div class="truyen-de-cu-meta d-flex flex-column align-items-center align-items-lg-start">
                                            <span class="truyen-tacgia"><i class="fa-solid fa-book-open"></i> Tác giả: <span class="truyen-tacgia-text">Đang cập nhật</span></span>
                                            <span class="truyen-luotxem"><i class="fa-solid fa-eye"></i> <span class="luot-xem-span me-1">Lượt xem:</span> 484</span>
                                        </div>
                                    </div>
                                </div>
                                                            <div class="truyen-de-cu-item d-flex align-items-center gap-3 mb-3">
                                    <div class="truyen-de-cu-image">
                                        <div class="top-item-comic-image-book-cover position-relative">
                                            <div class="top-item-comic-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/nhi-cong-tu-len-lut-giau-ta.html">
                                                    <img src="https://tehitruyen.com/img_data/images/anh_truyen/2251.jpg" alt="Trận Văn Trường Sinh">
                                                </a>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="truyen-de-cu-info">
                                        <a href="https://tehitruyen.com/nhi-cong-tu-len-lut-giau-ta.html" class="truyen-de-cu-title-link">Nhị Công Tử Lén Lút Giấu Ta</a>
                                        <div class="truyen-de-cu-meta d-flex flex-column align-items-center align-items-lg-start">
                                            <span class="truyen-tacgia"><i class="fa-solid fa-book-open"></i> Tác giả: <span class="truyen-tacgia-text">Đang cập nhật</span></span>
                                            <span class="truyen-luotxem"><i class="fa-solid fa-eye"></i> <span class="luot-xem-span me-1">Lượt xem:</span> 944</span>
                                        </div>
                                    </div>
                                </div>
                                                            <div class="truyen-de-cu-item d-flex align-items-center gap-3 mb-3">
                                    <div class="truyen-de-cu-image">
                                        <div class="top-item-comic-image-book-cover position-relative">
                                            <div class="top-item-comic-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/ta-nhat-duoc-hoang-de-mat-tri-nho.html">
                                                    <img src="https://tehitruyen.com/img_data/images/anh_truyen/2252.jpg" alt="Trận Văn Trường Sinh">
                                                </a>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="truyen-de-cu-info">
                                        <a href="https://tehitruyen.com/ta-nhat-duoc-hoang-de-mat-tri-nho.html" class="truyen-de-cu-title-link">Ta Nhặt Được Hoàng Đế Mất T...</a>
                                        <div class="truyen-de-cu-meta d-flex flex-column align-items-center align-items-lg-start">
                                            <span class="truyen-tacgia"><i class="fa-solid fa-book-open"></i> Tác giả: <span class="truyen-tacgia-text">Đang cập nhật</span></span>
                                            <span class="truyen-luotxem"><i class="fa-solid fa-eye"></i> <span class="luot-xem-span me-1">Lượt xem:</span> 560</span>
                                        </div>
                                    </div>
                                </div>
                                                            <div class="truyen-de-cu-item d-flex align-items-center gap-3 mb-3">
                                    <div class="truyen-de-cu-image">
                                        <div class="top-item-comic-image-book-cover position-relative">
                                            <div class="top-item-comic-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/nhi-thieu-gia-la-hac-xa.html">
                                                    <img src="https://tehitruyen.com/img_data/images/anh_truyen/2253.jpg" alt="Trận Văn Trường Sinh">
                                                </a>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="truyen-de-cu-info">
                                        <a href="https://tehitruyen.com/nhi-thieu-gia-la-hac-xa.html" class="truyen-de-cu-title-link">Nhị Thiếu Gia Là Hắc Xà</a>
                                        <div class="truyen-de-cu-meta d-flex flex-column align-items-center align-items-lg-start">
                                            <span class="truyen-tacgia"><i class="fa-solid fa-book-open"></i> Tác giả: <span class="truyen-tacgia-text">Đang cập nhật</span></span>
                                            <span class="truyen-luotxem"><i class="fa-solid fa-eye"></i> <span class="luot-xem-span me-1">Lượt xem:</span> 776</span>
                                        </div>
                                    </div>
                                </div>
                                                            <div class="truyen-de-cu-item d-flex align-items-center gap-3 mb-3">
                                    <div class="truyen-de-cu-image">
                                        <div class="top-item-comic-image-book-cover position-relative">
                                            <div class="top-item-comic-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/anh-trang-sang-roi-bui-tran.html">
                                                    <img src="https://tehitruyen.com/img_data/images/anh_truyen/2254.jpg" alt="Trận Văn Trường Sinh">
                                                </a>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="truyen-de-cu-info">
                                        <a href="https://tehitruyen.com/anh-trang-sang-roi-bui-tran.html" class="truyen-de-cu-title-link">Ánh Trăng Sáng Rọi Bụi Trần</a>
                                        <div class="truyen-de-cu-meta d-flex flex-column align-items-center align-items-lg-start">
                                            <span class="truyen-tacgia"><i class="fa-solid fa-book-open"></i> Tác giả: <span class="truyen-tacgia-text">Đang cập nhật</span></span>
                                            <span class="truyen-luotxem"><i class="fa-solid fa-eye"></i> <span class="luot-xem-span me-1">Lượt xem:</span> 2,029</span>
                                        </div>
                                    </div>
                                </div>
                                                            <div class="truyen-de-cu-item d-flex align-items-center gap-3 mb-3">
                                    <div class="truyen-de-cu-image">
                                        <div class="top-item-comic-image-book-cover position-relative">
                                            <div class="top-item-comic-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/ta-bi-ep-cai-trang-thanh-quy-phi-nao-ngo-bi-hoang-thuong-de-mat-den.html">
                                                    <img src="https://tehitruyen.com/img_data/images/anh_truyen/2256.jpg" alt="Trận Văn Trường Sinh">
                                                </a>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="truyen-de-cu-info">
                                        <a href="https://tehitruyen.com/ta-bi-ep-cai-trang-thanh-quy-phi-nao-ngo-bi-hoang-thuong-de-mat-den.html" class="truyen-de-cu-title-link">Ta Bị Ép Cải Trang Thành Qu...</a>
                                        <div class="truyen-de-cu-meta d-flex flex-column align-items-center align-items-lg-start">
                                            <span class="truyen-tacgia"><i class="fa-solid fa-book-open"></i> Tác giả: <span class="truyen-tacgia-text">Đang cập nhật</span></span>
                                            <span class="truyen-luotxem"><i class="fa-solid fa-eye"></i> <span class="luot-xem-span me-1">Lượt xem:</span> 3,541</span>
                                        </div>
                                    </div>
                                </div>
                                                            <div class="truyen-de-cu-item d-flex align-items-center gap-3 mb-3">
                                    <div class="truyen-de-cu-image">
                                        <div class="top-item-comic-image-book-cover position-relative">
                                            <div class="top-item-comic-image ratio ratio-1x1">
                                                <a href="https://tehitruyen.com/cuoi-phu-than-kinh-diem-cua-vi-hon-phu.html">
                                                    <img src="https://tehitruyen.com/img_data/images/anh_truyen/2257.jpg" alt="Trận Văn Trường Sinh">
                                                </a>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="truyen-de-cu-info">
                                        <a href="https://tehitruyen.com/cuoi-phu-than-kinh-diem-cua-vi-hon-phu.html" class="truyen-de-cu-title-link">Cưới Phụ Thân Kinh Diễm Của...</a>
                                        <div class="truyen-de-cu-meta d-flex flex-column align-items-center align-items-lg-start">
                                            <span class="truyen-tacgia"><i class="fa-solid fa-book-open"></i> Tác giả: <span class="truyen-tacgia-text">Đang cập nhật</span></span>
                                            <span class="truyen-luotxem"><i class="fa-solid fa-eye"></i> <span class="luot-xem-span me-1">Lượt xem:</span> 1,219</span>
                                        </div>
                                    </div>
                                </div>
                                                    </div>
                        <!-- pc end -->

                        <!-- mobile start -->
                        <div class="truyen-de-cu-list-mobile d-block d-lg-none px-3">
                            <!-- swiper slide start -->
                            <div class="lt-swiper-box-container position-relative">

                                <!-- Swiper -->
                                <div class="swiper swiper-slider-truyen-cung-tac-gia">
                                    <div class="swiper-wrapper py-3">
                                                                                    <!-- item start -->
                                            <div class="swiper-slide px-1">
                                                <div class="swiper-slider-advertise-item rounded-3  overflow-hidden ">
                                                    <div class="swiper-slider-advertise-item-box overflow-hidden d-flex flex-column gap-2 position-relative">
                                                        <!-- hình -->
                                                        <div class="swiper-slider-advertise-item-image ratio ratio-1x1">
                                                            <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html" title="Triều Đình Không Dung Nữ Nhân? Ta Là Ngoại Lệ">
                                                                <img data-src="https://tehitruyen.com/img_data/images/anh_truyen/2436.jpg" alt="truyện Triều Đình Không Dung Nữ Nhân? Ta Là Ngoại Lệ">
                                                            </a>
                                                        </div>
                                                        <!-- tên -->
                                                        <a href="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html" class="name-comic-advertise" title="Triều Đình Không Dung Nữ Nhân? Ta Là Ngoại Lệ">Triều Đình Khô...</a>

                                                        <!-- logo 18+ start -->
                                                                                                                <!-- logo 18+ end -->
                                                    </div>


                                                </div>
                                            </div>
                                            <!-- item end -->
                                                                                    <!-- item start -->
                                            <div class="swiper-slide px-1">
                                                <div class="swiper-slider-advertise-item rounded-3  overflow-hidden ">
                                                    <div class="swiper-slider-advertise-item-box overflow-hidden d-flex flex-column gap-2 position-relative">
                                                        <!-- hình -->
                                                        <div class="swiper-slider-advertise-item-image ratio ratio-1x1">
                                                            <a href="https://tehitruyen.com/thanh-chu-hoang-mac-da-la-gi.html" title="Thành Chủ Hoang Mạc Đã Là Gì">
                                                                <img data-src="https://tehitruyen.com/img_data/images/anh_truyen/2249.jpg" alt="truyện Thành Chủ Hoang Mạc Đã Là Gì">
                                                            </a>
                                                        </div>
                                                        <!-- tên -->
                                                        <a href="https://tehitruyen.com/thanh-chu-hoang-mac-da-la-gi.html" class="name-comic-advertise" title="Thành Chủ Hoang Mạc Đã Là Gì">Thành Chủ Hoan...</a>

                                                        <!-- logo 18+ start -->
                                                                                                                <!-- logo 18+ end -->
                                                    </div>


                                                </div>
                                            </div>
                                            <!-- item end -->
                                                                                    <!-- item start -->
                                            <div class="swiper-slide px-1">
                                                <div class="swiper-slider-advertise-item rounded-3  overflow-hidden ">
                                                    <div class="swiper-slider-advertise-item-box overflow-hidden d-flex flex-column gap-2 position-relative">
                                                        <!-- hình -->
                                                        <div class="swiper-slider-advertise-item-image ratio ratio-1x1">
                                                            <a href="https://tehitruyen.com/ta-cung-ca-ca-trong-sinh-thay-doi-ket-cuc.html" title="Ta Cùng Ca Ca Trọng Sinh Thay Đổi Kết Cục">
                                                                <img data-src="https://tehitruyen.com/img_data/images/anh_truyen/2250.jpg" alt="truyện Ta Cùng Ca Ca Trọng Sinh Thay Đổi Kết Cục">
                                                            </a>
                                                        </div>
                                                        <!-- tên -->
                                                        <a href="https://tehitruyen.com/ta-cung-ca-ca-trong-sinh-thay-doi-ket-cuc.html" class="name-comic-advertise" title="Ta Cùng Ca Ca Trọng Sinh Thay Đổi Kết Cục">Ta Cùng Ca Ca ...</a>

                                                        <!-- logo 18+ start -->
                                                                                                                <!-- logo 18+ end -->
                                                    </div>


                                                </div>
                                            </div>
                                            <!-- item end -->
                                                                                    <!-- item start -->
                                            <div class="swiper-slide px-1">
                                                <div class="swiper-slider-advertise-item rounded-3  overflow-hidden ">
                                                    <div class="swiper-slider-advertise-item-box overflow-hidden d-flex flex-column gap-2 position-relative">
                                                        <!-- hình -->
                                                        <div class="swiper-slider-advertise-item-image ratio ratio-1x1">
                                                            <a href="https://tehitruyen.com/nhi-cong-tu-len-lut-giau-ta.html" title="Nhị Công Tử Lén Lút Giấu Ta">
                                                                <img data-src="https://tehitruyen.com/img_data/images/anh_truyen/2251.jpg" alt="truyện Nhị Công Tử Lén Lút Giấu Ta">
                                                            </a>
                                                        </div>
                                                        <!-- tên -->
                                                        <a href="https://tehitruyen.com/nhi-cong-tu-len-lut-giau-ta.html" class="name-comic-advertise" title="Nhị Công Tử Lén Lút Giấu Ta">Nhị Công Tử Lé...</a>

                                                        <!-- logo 18+ start -->
                                                                                                                <!-- logo 18+ end -->
                                                    </div>


                                                </div>
                                            </div>
                                            <!-- item end -->
                                                                                    <!-- item start -->
                                            <div class="swiper-slide px-1">
                                                <div class="swiper-slider-advertise-item rounded-3  overflow-hidden ">
                                                    <div class="swiper-slider-advertise-item-box overflow-hidden d-flex flex-column gap-2 position-relative">
                                                        <!-- hình -->
                                                        <div class="swiper-slider-advertise-item-image ratio ratio-1x1">
                                                            <a href="https://tehitruyen.com/ta-nhat-duoc-hoang-de-mat-tri-nho.html" title="Ta Nhặt Được Hoàng Đế Mất Trí Nhớ">
                                                                <img data-src="https://tehitruyen.com/img_data/images/anh_truyen/2252.jpg" alt="truyện Ta Nhặt Được Hoàng Đế Mất Trí Nhớ">
                                                            </a>
                                                        </div>
                                                        <!-- tên -->
                                                        <a href="https://tehitruyen.com/ta-nhat-duoc-hoang-de-mat-tri-nho.html" class="name-comic-advertise" title="Ta Nhặt Được Hoàng Đế Mất Trí Nhớ">Ta Nhặt Được H...</a>

                                                        <!-- logo 18+ start -->
                                                                                                                <!-- logo 18+ end -->
                                                    </div>


                                                </div>
                                            </div>
                                            <!-- item end -->
                                                                                    <!-- item start -->
                                            <div class="swiper-slide px-1">
                                                <div class="swiper-slider-advertise-item rounded-3  overflow-hidden ">
                                                    <div class="swiper-slider-advertise-item-box overflow-hidden d-flex flex-column gap-2 position-relative">
                                                        <!-- hình -->
                                                        <div class="swiper-slider-advertise-item-image ratio ratio-1x1">
                                                            <a href="https://tehitruyen.com/nhi-thieu-gia-la-hac-xa.html" title="Nhị Thiếu Gia Là Hắc Xà">
                                                                <img data-src="https://tehitruyen.com/img_data/images/anh_truyen/2253.jpg" alt="truyện Nhị Thiếu Gia Là Hắc Xà">
                                                            </a>
                                                        </div>
                                                        <!-- tên -->
                                                        <a href="https://tehitruyen.com/nhi-thieu-gia-la-hac-xa.html" class="name-comic-advertise" title="Nhị Thiếu Gia Là Hắc Xà">Nhị Thiếu Gia ...</a>

                                                        <!-- logo 18+ start -->
                                                                                                                <!-- logo 18+ end -->
                                                    </div>


                                                </div>
                                            </div>
                                            <!-- item end -->
                                                                                    <!-- item start -->
                                            <div class="swiper-slide px-1">
                                                <div class="swiper-slider-advertise-item rounded-3  overflow-hidden ">
                                                    <div class="swiper-slider-advertise-item-box overflow-hidden d-flex flex-column gap-2 position-relative">
                                                        <!-- hình -->
                                                        <div class="swiper-slider-advertise-item-image ratio ratio-1x1">
                                                            <a href="https://tehitruyen.com/anh-trang-sang-roi-bui-tran.html" title="Ánh Trăng Sáng Rọi Bụi Trần">
                                                                <img data-src="https://tehitruyen.com/img_data/images/anh_truyen/2254.jpg" alt="truyện Ánh Trăng Sáng Rọi Bụi Trần">
                                                            </a>
                                                        </div>
                                                        <!-- tên -->
                                                        <a href="https://tehitruyen.com/anh-trang-sang-roi-bui-tran.html" class="name-comic-advertise" title="Ánh Trăng Sáng Rọi Bụi Trần">Ánh Trăng Sáng...</a>

                                                        <!-- logo 18+ start -->
                                                                                                                <!-- logo 18+ end -->
                                                    </div>


                                                </div>
                                            </div>
                                            <!-- item end -->
                                                                                    <!-- item start -->
                                            <div class="swiper-slide px-1">
                                                <div class="swiper-slider-advertise-item rounded-3  overflow-hidden ">
                                                    <div class="swiper-slider-advertise-item-box overflow-hidden d-flex flex-column gap-2 position-relative">
                                                        <!-- hình -->
                                                        <div class="swiper-slider-advertise-item-image ratio ratio-1x1">
                                                            <a href="https://tehitruyen.com/ta-bi-ep-cai-trang-thanh-quy-phi-nao-ngo-bi-hoang-thuong-de-mat-den.html" title="Ta Bị Ép Cải Trang Thành Quý Phi Nào Ngờ Bị Hoàng Thượng Để Mắt Đến">
                                                                <img data-src="https://tehitruyen.com/img_data/images/anh_truyen/2256.jpg" alt="truyện Ta Bị Ép Cải Trang Thành Quý Phi Nào Ngờ Bị Hoàng Thượng Để Mắt Đến">
                                                            </a>
                                                        </div>
                                                        <!-- tên -->
                                                        <a href="https://tehitruyen.com/ta-bi-ep-cai-trang-thanh-quy-phi-nao-ngo-bi-hoang-thuong-de-mat-den.html" class="name-comic-advertise" title="Ta Bị Ép Cải Trang Thành Quý Phi Nào Ngờ Bị Hoàng Thượng Để Mắt Đến">Ta Bị Ép Cải T...</a>

                                                        <!-- logo 18+ start -->
                                                                                                                <!-- logo 18+ end -->
                                                    </div>


                                                </div>
                                            </div>
                                            <!-- item end -->
                                                                                    <!-- item start -->
                                            <div class="swiper-slide px-1">
                                                <div class="swiper-slider-advertise-item rounded-3  overflow-hidden ">
                                                    <div class="swiper-slider-advertise-item-box overflow-hidden d-flex flex-column gap-2 position-relative">
                                                        <!-- hình -->
                                                        <div class="swiper-slider-advertise-item-image ratio ratio-1x1">
                                                            <a href="https://tehitruyen.com/cuoi-phu-than-kinh-diem-cua-vi-hon-phu.html" title="Cưới Phụ Thân Kinh Diễm Của Vị Hôn Phu">
                                                                <img data-src="https://tehitruyen.com/img_data/images/anh_truyen/2257.jpg" alt="truyện Cưới Phụ Thân Kinh Diễm Của Vị Hôn Phu">
                                                            </a>
                                                        </div>
                                                        <!-- tên -->
                                                        <a href="https://tehitruyen.com/cuoi-phu-than-kinh-diem-cua-vi-hon-phu.html" class="name-comic-advertise" title="Cưới Phụ Thân Kinh Diễm Của Vị Hôn Phu">Cưới Phụ Thân ...</a>

                                                        <!-- logo 18+ start -->
                                                                                                                <!-- logo 18+ end -->
                                                    </div>


                                                </div>
                                            </div>
                                            <!-- item end -->
                                                                            </div>
                                    <div class="lt-pagination-box swiper-pagination-truyen-noi-bat-box text-center">
                                        <div class="swiper-pagination-truyen-cung-tac-gia"></div>
                                    </div>
                                </div>
                                <!-- swiper slide end -->
                                <img src="https://tehitruyen.com/templates/images/btn-lt-prev.png" alt="icon" class="btn-icon-swiper-prev btn-swiper-truyen-cung-tac-gia-prev ">
                                <img src="https://tehitruyen.com/templates/images/btn-lt-next.png" alt="icon" class="btn-icon-swiper-next btn-swiper-truyen-cung-tac-gia-next ">
                            </div>
                        </div>
                        <!-- mobile end -->
                    </div>
                </div>
                <!-- truyện đề cử end -->


            </div>
        </div>
        <!-- bình luận, truyện đề cử end -->

    </div>
</section>


<!-- Modal Donate -->
<div class="modal fade donate-modal" data-bs-backdrop="static" id="donateModal" tabindex="-1" aria-labelledby="donateModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content donate-modal-content">
            <div class="modal-header donate-modal-header">
                <h5 class="modal-title donate-modal-title" id="donateModalLabel">Tặng Đào</h5>
                <button type="button" class="btn-close donate-modal-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body donate-modal-body">
                                <p class="donate-modal-info">Tặng Đào cho: <strong>Lớp Trưởng (huyenlenh94)</strong></p>
                <p class="donate-modal-info">Số đào hiện có của bạn: <strong><span id="so_dao_hien_co"></span> <img src="https://tehitruyen.com/templates/images/icon-qua-dao.png" alt="icon" class="icon-qua-dao"></strong></p>
                <div class="mb-3">
                    <label for="soDaoDonate" class="form-label">Nhập số đào <img src="https://tehitruyen.com/templates/images/icon-qua-dao.png" alt="icon" class="icon-qua-dao"> muốn tặng</label>
                    <input type="text" class="form-control formatprice" id="soDaoDonate" min="1" max="" placeholder="Nhập số đào...">
                </div>
                <p class="donate-modal-remaining">Sau khi tặng, số đào còn lại của bạn sẽ là: <span id="soDaoConLai"></span> <img src="https://tehitruyen.com/templates/images/icon-qua-dao.png" alt="icon" class="icon-qua-dao"></p>
            </div>
            <div class="modal-footer donate-modal-footer">
                <button type="button" class="btn btn-secondary donate-btn-cancel" data-bs-dismiss="modal">Hủy bỏ</button>
                <button type="button" class="btn btn-primary donate-btn-confirm">Tặng Đào</button>
            </div>
        </div>
    </div>
</div>


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

<!-- Modal Mua Chương -->
<div class="modal fade mua-chuong-modal" data-bs-backdrop="static" id="muaChuongModal" tabindex="-1" aria-labelledby="muaChuongModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content mua-chuong-modal-content">
            <div class="modal-header mua-chuong-modal-header">
                <h5 class="modal-title mua-chuong-modal-title" id="muaChuongModalLabel">Mua Chương</h5>
                <button type="button" class="btn-close mua-chuong-modal-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body mua-chuong-modal-body">
                <div class="mua-chuong-summary">
                    <p><strong>Tên truyện:</strong> Triều Đình Không Dung Nữ Nhân? Ta Là Ngoại Lệ</p>
                    <p><strong>Tên chương:</strong> Chương 1:</p>
                    <p><strong>Giá đào:</strong> 0 <img src="https://tehitruyen.com/templates/images/dao-nho.png" alt="icon" class="icon-qua-dao-chuong "> </p>
                    <p><strong>Giá hạt:</strong> 0 <img src="https://tehitruyen.com/templates/images/hat.png" alt="icon" class="icon-hat"> </p>
                </div>
            </div>
            <div class="modal-footer mua-chuong-modal-footer">
                <button type="button" class="btn btn-secondary mua-chuong-btn-cancel" data-bs-dismiss="modal">Hủy bỏ</button>
                <button type="button" class="btn btn-primary mua-chuong-btn-pay">Thanh Toán</button>
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
                    <input type="hidden" name="pnvn_token" value="462a07709ff85bdcb946dfda56451dd281620f04">
                    <input type="hidden" name="ten_truyen" value="Triều Đình Không Dung Nữ Nhân? Ta Là Ngoại Lệ">
                    <input type="hidden" name="link_truyen" value="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html">
                    <input type="hidden" name="id_chapter" value="13365">

                    <div class="mb-3">
                        <label for="tenTruyen" class="form-label">Tên Truyện</label>
                        <input type="text" class="form-control form-control-pretty" id="tenTruyen" value="Triều Đình Không Dung Nữ Nhân? Ta Là Ngoại Lệ" disabled>
                    </div>

                    <div class="mb-3">
                        <label for="linkTruyen" class="form-label">Link Truyện</label>
                        <input type="text" class="form-control form-control-pretty" id="linkTruyen" value="https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html" disabled>
                    </div>

                    <div class="mb-3">
                        <label for="tenChapter" class="form-label">Tên Chapter</label>
                        <input type="text" class="form-control form-control-pretty" id="tenChapter" value="Chương 1:" disabled>
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








<!-- mộng đào viên -->
<!-- kích hoạt tooltips -->
<script>
    $(document).ready(function() {
        var parent_code = '193';
        $(".menu-code-" + parent_code).addClass('active');
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
        var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl)
        });

        // Khi nhấn vào nút "Tìm chương" - cho #timChuongBtn
        $('#timChuongBtn').on('click', function() {
            // Toggle hiển thị danh sách chương
            $('#chuongList').slideToggle(300);
        });

        // Đóng danh sách chương khi nhấn ngoài khu vực
        $(document).on('click', function(event) {
            if (!$(event.target).closest('#timChuongBtn, #chuongList').length) {
                $('#chuongList').slideUp(300);
            }
        });

        // Khi nhấn vào nút "Tìm chương" - cho #timChuongBtn2
        $('#timChuongBtn2').on('click', function() {
            // Toggle hiển thị danh sách chương phía trên nút
            $('#chuongList2').slideToggle(300);
        });

        // Đóng danh sách chương khi nhấn ngoài khu vực
        $(document).on('click', function(event) {
            if (!$(event.target).closest('#timChuongBtn2, #chuongList2').length) {
                $('#chuongList2').slideUp(300);
            }
        });
    })
</script>

<!-- tool bar bên phải -->
<script>
    $(document).ready(function() {
        // Biến kiểm tra người dùng có quyền đọc chương không
        const isUserAuthorized = false;
        // Khi nhấn vào nút "Danh sách chương"
        $('.mdv-btn-danh-sach-chuong-xem').on('click', function() {
            // Toggle hiển thị danh sách chương
            $('#chuongListLeft').toggleClass('show');

            // Ẩn hoặc hiện tooltip dựa vào trạng thái của danh sách chương
            if ($('#chuongListLeft').hasClass('show')) {
                $(this).tooltip('hide'); // Ẩn tooltip
            } else {
                $(this).tooltip('show'); // Hiện lại tooltip
            }
        });

        $('.mdv-btn-danh-sach-chuong-xem-mobile').on('click', function() {
            // Toggle hiển thị danh sách chương
            $('#chuongListLeftMobile').toggleClass('show');

            // Ẩn hoặc hiện tooltip dựa vào trạng thái của danh sách chương
            if ($('#chuongListLeftMobile').hasClass('show')) {
                $(this).tooltip('hide'); // Ẩn tooltip
            } else {
                $(this).tooltip('show'); // Hiện lại tooltip
            }
        });

        // Đóng danh sách chương khi nhấn ngoài khu vực
        $(document).on('click', function(event) {
            if (!$(event.target).closest('.mdv-btn-danh-sach-chuong-xem, #chuongListLeft').length) {
                $('#chuongListLeft').removeClass('show');
                $('.mdv-btn-danh-sach-chuong-xem').tooltip('hide'); // Hiện lại tooltip khi đóng danh sách
            }

            if (!$(event.target).closest('.mdv-btn-danh-sach-chuong-xem-mobile, #chuongListLeftMobile').length) {
                $('#chuongListLeftMobile').removeClass('show');
                $('.mdv-btn-danh-sach-chuong-xem-mobile').tooltip('hide'); // Hiện lại tooltip khi đóng danh sách
            }
        });
    });
</script>

<!-- bình luận -->

<script>
    $(document).ready(function() {
        // Kiểm tra xem người dùng đã đăng nhập chưa
        const isLoggedIn = false;

        // Xử lý khi nhấn vào nút xác nhận mật khẩu
        $('#btnSubmitPassword').click(function() {
            const password = $('#chapterPassword').val();

            $.ajax({
                url: 'sources/ajax/mongdaovien/check-password.php',
                type: 'POST',
                data: {
                    id_chapter: 13365,
                    password: password
                },
                success: function(response) {
                    if (response.status === 'success') {
                        FuiToast.success('Mật khẩu chính xác!');

                        // Lưu thông tin rằng người dùng đã nhập đúng mật khẩu để không yêu cầu lại
                        sessionStorage.setItem('chapter_' + response.id_chapter + '_unlocked', true);

                        $('#passwordFormContainer').fadeOut('slow', function() {
                            // Nếu chương có giá trị thì hiển thị form mua chương
                            if (response.vip_notice === true) {
                                $('#noi_dung_truyen').html(response.vip_content).fadeIn('slow');
                            } else {
                                // Nếu chương không có giá trị, hiển thị nội dung chương
                                $('#noi_dung_truyen').html(response.noi_dung).fadeIn('slow');
                            }
                        });
                    } else {
                        FuiToast.error('Mật khẩu không chính xác, vui lòng thử lại.');
                    }
                },
                error: function() {
                    FuiToast.error('Có lỗi xảy ra, vui lòng thử lại sau.');
                }
            });
        });

        // xử lý mua chương start
        $(document).on('click', '#btnMuaChuong', function() {
            if (!isLoggedIn) {
                FuiToast.error('Bạn cần đăng nhập để mua chương!');
                return;
            }
            $('#muaChuongModal').modal('show');
        });

        $(document).on('click', '.mua-chuong-btn-pay', function() {
            $.ajax({
                url: 'sources/ajax/mongdaovien/mua-chuong-detail.php',
                type: 'POST',
                data: {
                    id_truyen: 2436,
                    chapters: [13365],
                    tong_gia_dao: 0,
                    tong_gia_hat: 0,
                    id_user: 0                },
                success: function(response) {
                    if (response.status === 'success') {
                        FuiToast.success('Thanh toán thành công! Chương đã được mở khóa.');

                        $('#muaChuongModal').modal('hide');
                        $('#vipNotice').fadeOut('slow', function() {
                            $('#noi_dung_truyen').html(`
                            <p>Ta cải nam trang vào quân doanh, vô tình cứu được Tiêu Càn từ đống x.á.c c.h.e.t trở về. </p><p><br></p>Trong tiệc khánh công, bệ hạ hỏi hắn muốn được ban thưởng gì. <p><br></p>Hắn vì muốn cưới công chúa, liền dùng kiếm hất tung lớp vải bó ngực của ta.<p><br></p>Trước mặt mọi người vạch trần thân phận nữ nhi của ta. <p><br></p>"Nàng khi quân phạm thượng, nay vừa hay có thể thay công chúa gả đến biên tái, coi như chuộc tội lập công." <p><br></p>Ta bị giam trong ngục tối, xiềng xích xuyên qua xương bả vai. <p><br></p>Công chúa mỉm cười nghiền nát xương ngón tay của ta, thả chuột cắn nuốt da thịt ta. <p><br></p>"Dù sao cũng là ngươi cứu Tiêu lang, mới thúc đẩy được mối lương duyên của hắn và ta."<p><br></p>"Bản cung từ bi nhân hậu, đây là thưởng cho ngươi, coi như tạ lễ."<p><br></p>Mùa xuân năm sau, Tiêu Càn cưới công chúa, thăng quan tiến chức, quyền khuynh triều dã. <p><br></p>Còn ta chịu hết nhục nhã, c.h.e.t thảm trong chuồng dê nơi biên tái. <p><br></p>Trở lại một đời, ta quay về ngày bị Tiêu Càn vạch trần thân phận. <p><br></p>1<p><br></p>Ngày Tiêu Càn cưới công chúa, cỏ xuân xanh mơn mởn. <p><br></p>Kinh thành mười dặm hồng trang, rầm rộ phô trương. <p><br></p>Còn ta quần áo rách rưới, toàn thân đầy vết thương, bị xích sắt trói buộc, mỗi bước chân in một dấu m.á.u. <p><br></p>Đại Tống nghị hòa với Kim triều, Kim triều trả lại một tòa thành, đổi lấy Đại Tống hòa thân. <p><br></p>Bệ hạ có chỉ, lệnh cho ta thay công chúa đến biên tái xa xôi. <p><br></p>Bách tính không hiểu chuyện thì thầm chỉ trỏ. <p><br></p>Có đồng cảm, cũng có khinh bỉ. <p><br></p>Gió xuân se lạnh, trên người ta chỉ có một lớp áo mỏng, lạnh đến tím tái cả người. <p><br></p>Thủ lĩnh người Kim phụ trách đón tiếp bị mù một mắt. <p><br></p>Ta nhớ hắn là Hoàn Nhan Liệt, chủ soái năm đó ở Bạch Đầu Nhai. <p><br></p>Năm đó, ta mười bảy tuổi được thăng chức làm phó tướng cho tướng quân Tiêu Càn. <p><br></p>Trận chiến ở Bạch Đầu Nhai, chủ lực triều đình bị tập kích, chủ tướng Tiêu Càn mất tích. <p><br></p>Ta một mình một ngựa, từ trong đống xác c.h.e.t moi Tiêu Càn toàn thân đầy m.á.u, mười ngón tay ta cũng nhuốm đầy m.á.u tươi. <p><br></p>Cõng hắn đi trong Tuyết Sơn suốt một đêm. <p><br></p>Khi viện quân Đại Tống đến, tóc mai ta đóng đầy băng sương, lạnh đến mức gần như ngất đi. <p><br></p>Năm đó, để cứu Tiêu Càn, ta từng bắn một mũi tên xuyên qua mắt trái của Hoàn Nhan Liệt. <p><br></p>Hắn hận không thể ăn tươi n.u.ố.t sống ta. <p><br></p>Nay mới qua ba năm, ta lại rơi vào tay kẻ thù. <p><br></p>Ánh mắt thèm thuồng của Hoàn Nhan Liệt đảo qua người ta. <p><br></p>Hắn kéo ta vào lòng cười ha hả. <p><br></p>"Tiểu phó tướng lại là nữ nhân!"<p><br></p>"Không ngủ được với công chúa kim chi ngọc diệp của các ngươi, ngủ với ngươi hình như cũng không tồi!"<p><br></p>Hắn lấy ra một mũi tên, như mèo vờn chuột miêu tả hốc mắt của ta. <p><br></p>"Nghe nói ngươi là bị nghiệm thân ngay tại Kim Loan điện, vậy chẳng phải rất nhiều nam nhân đã nhìn thấy thân thể của ngươi rồi sao?"<p><br></p>"Nữ nhân Đại Tống coi trọng trinh tiết nhất, ngươi như vậy, có phải nên gọi là..."<p><br></p>Hắn cắn vào tai ta một cách mờ ám, lưỡi ướt át liếm láp vành tai, từ kẽ răng nghiến ra hai chữ đó. <p><br></p>"Phế phẩm."<p><br></p>Vừa dứt lời, cây trâm vàng trong tay ta đã đâm thẳng vào yết hầu hắn. <p><br></p>Trong chớp mắt, chỉ cần thêm một tấc nữa là có thể lấy mạng hắn. <p><br></p>Nhưng trước khi đi, xương ngón tay của ta đã bị nghiền nát, mất đi sự chính xác. <p><br></p>Hoàn Nhan Liệt đẩy ta ra. <p><br></p>Cơn giận dữ khiến hắn liên tục đá vào người ta. <p><br></p>M.á.u không ngừng tuôn ra từ miệng và mũi ta. <p><br></p>Hắn nắm lấy cánh tay ta bẻ mạnh một cái, cơn đau khiến ta hét lên. <p><br></p>"Không phải là bách bộ xuyên dương, Hồng Anh Thương đứng đầu quân đội sao?"<p><br></p>"Bây giờ ngươi chỉ là một phế nhân, ta muốn xem xem xương cốt của ngươi cứng đến đâu."<p><br></p>Hắn hạ lệnh nhốt ta vào chuồng dê, đêm nay ta chính là con dê chờ bị g.i.e.t thịt. <p><br></p>Vô số đôi mắt u ám như những con thú đang ẩn nấp, thèm thuồng nhìn chằm chằm vào làn da lộ ra ngoài lớp áo của ta. <p><br></p>Giữa mùa đông tháng chạp, tuyết lớn rơi không ngớt. <p><br></p>Ta đột nhiên đập đầu vào tảng đá trong chuồng dê. <p><br></p>Một tiếng vang giòn tan, âm thanh của xương sọ vỡ vụn. <p><br></p>Trước mắt là một màu đỏ trắng. <p><br></p>Vô số oán hận thiêu đốt ta. <p><br></p>Trước khi c.h.e.t, những ký ức như đèn kéo quân hiện lên. <p><br></p>Năm đó chạy trốn trong Tuyết Sơn, ta cứu được Tiêu Càn. <p><br></p>Khi đó cũng có tuyết lớn như vậy. <p><br></p>Ta và Tiêu Càn ôm nhau sưởi ấm trong băng tuyết. <p><br></p>Ta vừa khát vừa mệt, sắp mất đi ý thức. <p><br></p>Hắn thoi thóp, dùng chút sức lực cuối cùng r.ạ.c.h cổ tay. <p><br></p>Đưa m.á.u ấm vào miệng ta. <p><br></p>Khi đó, mọi thứ đều hiện rõ trước mắt. <p><br></p>Nhưng tất cả những điều này đã khiến ta hiểu lầm hắn. <p><br></p>Tiêu Càn, chính là một kẻ ti tiện. <p><br></p>2<p><br></p>Cơn đau trước khi c.h.e.t dường như vẫn còn đó. <p><br></p>Ta mở mắt ra. <p><br></p>Cung điện nguy nga, bậc thang bằng ngọc. <p><br></p>Ta vậy mà đã quay về ngày yến tiệc khánh công. <p><br></p>Cơn thịnh nộ ngập trời khiến ta siết chặt miếng ngọc bội trong tay. <p><br></p>Là miếng ngọc bội Tiêu Càn tặng ta. <p><br></p>Mười ngón tay ghim vào lòng bàn tay đến bật m.á.u. <p><br></p>Ta đã quay về khởi điểm của mọi bất hạnh. <p><br></p>Năm đó, ta mười bảy tuổi, cứu được Tiêu Càn, khi ta hôn mê, hắn biết ta là nữ nhân. <p><br></p>Khi ta tỉnh lại, hắn mặt mày tái nhợt, tự tay đút thuốc đến bên môi ta. <p><br></p>Ngọn nến trong trướng lay động, chiếu vào đôi mắt hắn đang mỉm cười. <p><br></p>"Không ngờ Tuyết tiểu phó tướng dũng mãnh, lại là một cô nương."<p><br></p>Hắn không vạch trần ta, chúng ta cùng nhau vượt qua ba năm c.h.é.m g.i.e.t trên chiến trường.<p></p>
                        `).fadeIn('slow');
                        });
                    } else {
                        FuiToast.error(`Thanh toán thất bại: ${response.message}`);
                    }
                },
                error: function() {
                    FuiToast.error('Có lỗi xảy ra, vui lòng thử lại sau!');
                }
            });
        });
        // xử lý mua chương end

        // xử lý lưu vào tủ truyện start

        // Lưu hoặc bỏ lưu vào Tủ Truyện
        $('.btn-them-vao-tu-truyen-tool').on('click', function() {
            const button = $(this);
            const id_truyen = 2436;
            const id_user = null;

            if (id_user == null) {
                FuiToast.error('Bạn cần đăng nhập để sử dụng tính năng này!');
                return;
            }

            if (button.hasClass('luu')) {
                // Gọi AJAX để xóa khỏi Tủ Truyện
                $.ajax({
                    url: 'sources/ajax/mongdaovien/bo-theo-doi-truyen.php',
                    type: 'POST',
                    data: {
                        id_truyen: id_truyen,
                        id_user: id_user
                    },
                    success: function(response) {
                        if (response === 'success') {
                            button.removeClass('luu').addClass('bo-luu');
                            button.find('.icon-tu-truyen-img-tool').removeClass('active');
                            FuiToast.success('Bỏ lưu thành công!');
                        } else {
                            FuiToast.error('Có lỗi xảy ra! Vui lòng thử lại sau.');
                        }
                    },
                    error: function() {
                        FuiToast.error('Đã xảy ra lỗi trong quá trình gửi yêu cầu.');
                    }
                });

            } else {
                // Gọi AJAX để thêm vào Tủ Truyện
                $.ajax({
                    url: 'sources/ajax/mongdaovien/theo-doi-truyen.php',
                    type: 'POST',
                    data: {
                        id_truyen: id_truyen,
                        id_user: id_user,
                        time: Math.floor(Date.now() / 1000),
                        thong_bao: 1
                    },
                    success: function(response) {
                        if (response === 'success') {
                            button.removeClass('bo-luu').addClass('luu');
                            button.find('.icon-tu-truyen-img-tool').addClass('active');
                            // button.find('.icon-tu-truyen-img-tool').attr('src', 'https://tehitruyen.com/templates/images/school-organe-saved.png');
                            FuiToast.success('Lưu thành công vào Tủ Truyện!');
                        } else {
                            FuiToast.error('Có lỗi xảy ra! Vui lòng thử lại sau.');
                        }
                    },
                    error: function() {
                        FuiToast.error('Đã xảy ra lỗi trong quá trình gửi yêu cầu.');
                    }
                });
            }
        });
        // xử lý lưu vào tủ truyện end



        // bình luận truyện start
        // emoji
        if (window.innerWidth > 1024) {
            $("#emojionearea").emojioneArea({
                pickerPosition: "right",
                filtersPosition: "bottom",
                tonesStyle: "square",
                placeholder: "Nhận xét..."
            });
            $(".emojionearea-rep").emojioneArea({
                pickerPosition: "right",
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
                    noi_dung: noiDung,
                    id_chapter: 13365                },
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
                        $(".vh-notification").html('');
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
                    pickerPosition: 'right',
                    filtersPosition: 'bottom',
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
                    thoi_gian: Math.floor(Date.now() / 1000), // Thời gian hiện tại (UNIX timestamp),
                    id_chapter: 13365                },
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
                    id_chapter: 13365                },
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
                        $button.fadeOut('slow', function() {
                            $(this).remove();
                        });
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


        // bình luận truyện end


        // khi click vào button tool bình luận scroll xuống start
        // Khi nhấn vào nút bình luận
        $('.btn-scroll-binh-luan-tool a').on('click', function(e) {
            e.preventDefault(); // Ngăn chặn hành động mặc định của thẻ <a>

            // Kiểm tra xem Lenis có tồn tại không
            if (window.lenis) {
                const target = document.querySelector('.mdv-san-pham-show-comment');
                if (target) {
                    window.lenis.scrollTo(target, {
                        offset: 0,
                        duration: 2.5,
                        immediate: false,
                    });
                }
            } else {
                // Trường hợp không có Lenis, cuộn bằng jQuery như bình thường
                $('html, body').animate({
                    scrollTop: $('.mdv-san-pham-show-comment').offset().top
                }, 800); // 800ms để cuộn xuống mượt
            }
        });


        // khi click vào button tool bình luận scroll xuống end


        // xử lý báo lỗi truyện start
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
                        // Thông báo thất bại
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
        // xử lý báo lỗi truyện end

    });
</script>

<!-- chế độ sáng tối start -->
<script>
    // Kiểm tra chế độ đã lưu trong localStorage và đặt lại cho trang
    if (localStorage.getItem('darkMode') === 'enabled') {
        $('body').addClass('dark-mode');
        $('.btn-che-do-sang-toi i').removeClass('fa-moon').addClass('fa-sun');
    }

    // Xử lý khi click vào nút chuyển chế độ sáng/tối
    $('.btn-che-do-sang-toi').on('click', function() {
        $('body').toggleClass('dark-mode');

        // Thay đổi icon giữa mặt trời và mặt trăng
        const icon = $(this).find('i');
        if ($('body').hasClass('dark-mode')) {
            icon.removeClass('fa-moon').addClass('fa-sun');
            // Lưu trạng thái chế độ tối vào localStorage
            localStorage.setItem('darkMode', 'enabled');
            // hide tooltip
            $('[data-bs-toggle="tooltip"]').tooltip('hide');
        } else {
            icon.removeClass('fa-sun').addClass('fa-moon');
            // Xóa trạng thái chế độ tối khỏi localStorage
            localStorage.setItem('darkMode', 'disabled');
            // hide tooltip
            $('[data-bs-toggle="tooltip"]').tooltip('hide');
        }
    });
    //

    // XỬ LÝ TẶNG QUÀ START

    // Show modal when clicking on "Tặng Quà"
    $(document).on('click', '.btn-tang-qua', function() {
        const userId = null;
        const authorId = 1044; // Replace with appropriate author ID
        let so_dao_hien_co = 0;
        if (userId === null) {
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
                id_user: userId
            },
            success: function(response) {
                if (response.status === 'success') {
                    const userInfo = response.tai_khoan;
                    // Cập nhật modal với số đào hiện có của người dùng
                    so_dao_hien_co = userInfo.dao;
                    $('#so_dao_hien_co').html(number_format(userInfo.dao));
                    $('#soDaoConLai').text(number_format(userInfo.dao));
                    $('#donateModal').modal('show');
                } else {
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Không thể tải thông tin tài khoản của bạn.',
                    });
                }
            },
            error: function() {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Có lỗi xảy ra khi truy vấn tài khoản.',
                });
            },
        });

        $('.formatprice').priceFormat({
            prefix: '',
            thousandsSeparator: ',',
            centsLimit: 0,
        });

        function number_format(number) {
            return new Intl.NumberFormat('vi-VN').format(number);
        }

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

        $('.donate-btn-confirm').on('click', function() {
            const donateAmount = parseInt($('#soDaoDonate').val().replace(/,/g, '')) || 0;

            if (donateAmount <= 0) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Vui lòng nhập số đào hợp lệ để donate.',
                });
                return;
            }

            $.ajax({
                url: 'sources/ajax/mongdaovien/donate-dao-editor.php',
                type: 'POST',
                data: {
                    user_duoc_donate: authorId,
                    so_dao: donateAmount,
                    id_truyen: '2436',
                    id_chapter: '13365'
                },
                success: function(response) {
                    if (response.status === 'success') {
                        Swal.fire({
                            icon: 'success',
                            title: 'Thành công!',
                            text: response.message,
                        });

                        $('.dao-dang-co').text(response.dao_hien_tai);
                        $('#donateModal').modal('hide');
                    } else {
                        Swal.fire({
                            icon: 'error',
                            title: 'Oops...',
                            text: response.message,
                        });
                    }
                },
                error: function() {
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Có lỗi xảy ra, vui lòng thử lại sau.',
                    });
                },
            });
        });
    });

    // XỬ LÝ TẶNG QUÀ END



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
    $('.btn-de-cu-bong').on('click', function() {
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
                pnvn_token: "462a07709ff85bdcb946dfda56451dd281620f04"
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
</script>
<!-- chế độ sáng tối end -->

<!-- <script src="https://code.responsivevoice.org/responsivevoice.js?key=240jsndI"></script> -->
<style>
    /* Style cho thanh range với phần đã chọn */
    #fontSizeRange {
        width: 100%;
        height: 6px;
        border-radius: 3px;
        background: linear-gradient(to right, var(--primary-color) 0%, var(--primary-color) 50%, #ddd 50%, #ddd 100%);
        outline: none;
        -webkit-appearance: none;
    }

    #fontSizeRange::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background: var(--primary-color);
        cursor: pointer;
        border: 2px solid white;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    #fontSizeRange::-moz-range-thumb {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background: var(--primary-color);
        cursor: pointer;
        border: 2px solid white;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    .font-size-value {
        text-align: center;
        margin-top: 8px;
        font-size: 0.9rem;
        color: #666;
    }
</style>
<script>
    // Script chính
    (function() {
        // DOM Elements
        const fontSizeBox = document.getElementById("fontSizeBox");
        const fontSizeRange = document.getElementById("fontSizeRange");
        const fontSizeValue = document.getElementById("fontSizeValue");
        const contentElement = document.getElementById("noi_dung_truyen");
        const removeBreaksToggle = document.getElementById("removeBreaksToggle");

        // Kiểm tra phần tử tồn tại
        if (!fontSizeBox || !fontSizeRange || !contentElement) {
            console.error("❌ Một hoặc nhiều phần tử cần thiết không tồn tại trong DOM");
            return;
        }

        // Hàm cập nhật màu nền cho thanh range
        function updateRangeBackground(value) {
            const min = parseInt(fontSizeRange.min);
            const max = parseInt(fontSizeRange.max);
            const percentage = ((value - min) / (max - min)) * 100;
            fontSizeRange.style.background = `linear-gradient(to right, var(--primary-color) 0%, var(--primary-color) ${percentage}%, #ddd ${percentage}%, #ddd 100%)`;
        }

        // Hàm cập nhật cỡ chữ
        function updateFontSize(value) {
            const newSize = parseInt(value);
            if (isNaN(newSize)) return;

            try {
                // Áp dụng font-size cho phần tử nội dung
                contentElement.style.fontSize = newSize + "px";

                // Cập nhật giá trị hiển thị
                if (fontSizeValue) {
                    fontSizeValue.textContent = newSize;
                }

                // Cập nhật màu nền cho thanh range
                updateRangeBackground(newSize);

                // Lưu vào localStorage
                try {
                    localStorage.setItem("fontSize", newSize);
                    console.log('💾 Đã lưu cỡ chữ:', newSize + "px");
                } catch (e) {
                    console.warn('⚠️ Không thể lưu vào localStorage:', e.message);
                }

                console.log(`🎨 Đã áp dụng cỡ chữ: ${newSize}px`);
            } catch (e) {
                console.error('❌ Lỗi khi cập nhật cỡ chữ:', e);
            }
        }

        // Hàm áp dụng trạng thái ẩn xuống dòng
        function triggerBreakToggle() {
            if (!contentElement) return;

            if (removeBreaksToggle && removeBreaksToggle.checked) {
                // Ẩn các thẻ <br>
                contentElement.classList.add("remove-breaks");

                // Xóa thẻ <br> trong các thẻ <p> chỉ chứa <br>
                const paragraphs = contentElement.querySelectorAll('p');
                paragraphs.forEach(p => {
                    // Kiểm tra nếu đoạn chỉ chứa <br> (có thể có khoảng trắng)
                    const innerHTMLTrimmed = p.innerHTML.replace(/\s/g, '');
                    if (innerHTMLTrimmed === '<br>') {
                        // Giữ lại thẻ <p> nhưng xóa thẻ <br> bên trong
                        p.innerHTML = '';
                    }
                });
            } else {
                // Khi tắt, khôi phục lại nội dung ban đầu
                contentElement.classList.remove("remove-breaks");

                // Khôi phục lại các thẻ <br> đã bị xóa (nếu có lưu trữ)
                const paragraphs = contentElement.querySelectorAll('p');
                paragraphs.forEach(p => {
                    // Nếu đoạn trống và trước đó có thể là <br>
                    if (p.innerHTML === '') {
                        // Kiểm tra xem đoạn này có data attribute lưu trữ nội dung cũ không
                        const originalContent = p.getAttribute('data-original-content');
                        if (originalContent) {
                            p.innerHTML = originalContent;
                            p.removeAttribute('data-original-content');
                        }
                    }
                });
            }
        }


        // Thiết lập sự kiện cho thanh trượt
        function setupFontSizeEvents() {
            const updateAndSave = function() {
                updateFontSize(this.value);
            };

            fontSizeRange.addEventListener('input', updateAndSave);
            fontSizeRange.addEventListener('change', updateAndSave);

            // Xử lý chạm trên thiết bị di động
            let touchStartValue = null;
            fontSizeRange.addEventListener('touchstart', function(e) {
                touchStartValue = this.value;
                this.style.zIndex = '1000';
            }, {
                passive: true
            });

            fontSizeRange.addEventListener('touchend', function(e) {
                this.style.zIndex = '';
                if (touchStartValue !== null && this.value !== touchStartValue) {
                    updateAndSave.call(this);
                }
                touchStartValue = null;
            }, {
                passive: true
            });
        }

        // Xử lý sự kiện toggle ẩn xuống dòng
        function setupRemoveBreaksToggle() {
            if (!removeBreaksToggle) return;

            // Lưu trữ nội dung gốc trước khi thay đổi
            const paragraphs = contentElement.querySelectorAll('p');
            paragraphs.forEach(p => {
                const innerHTMLTrimmed = p.innerHTML.replace(/\s/g, '');
                if (innerHTMLTrimmed === '<br>' && !p.hasAttribute('data-original-content')) {
                    p.setAttribute('data-original-content', '<br>');
                }
            });

            // Xử lý khi thay đổi trạng thái checkbox
            removeBreaksToggle.addEventListener('change', function() {
                triggerBreakToggle();
                try {
                    localStorage.setItem("removeBreaks", this.checked);
                    console.log('💾 Đã lưu trạng thái ẩn xuống dòng:', this.checked);
                } catch (e) {
                    console.warn('⚠️ Không thể lưu trạng thái ẩn xuống dòng:', e.message);
                }
            });

            // Xử lý khi click vào slider (toggle switch)
            const slider = document.querySelector(".toggle-switch .slider");
            if (slider) {
                slider.addEventListener("click", function(e) {
                    // Ngăn sự kiện click lan ra ngoài
                    e.stopPropagation();
                    // Đảo ngược trạng thái của checkbox
                    removeBreaksToggle.checked = !removeBreaksToggle.checked;
                    // Kích hoạt sự kiện change
                    removeBreaksToggle.dispatchEvent(new Event('change'));
                });
            }
        }

        // Xử lý khi nhấn vào nút chỉnh cỡ chữ
        function setupToolButtonEvent() {
            const toolButton = document.querySelector(".btn-chinh-co-chu-tool");
            if (!toolButton) return;

            toolButton.addEventListener("click", function(e) {
                e.stopPropagation();
                fontSizeBox.classList.toggle("d-none");

                if (!fontSizeBox.classList.contains("d-none")) {
                    // Hiển thị với animation
                    gsap.fromTo(fontSizeBox, {
                        opacity: 0,
                        y: 20
                    }, {
                        opacity: 1,
                        y: 0,
                        duration: 0.3,
                        ease: "power2.out"
                    });
                }
            });
        }

        // Ẩn box khi click bên ngoài
        function setupAutoHide() {
            document.addEventListener('click', function(e) {
                if (fontSizeBox && !fontSizeBox.classList.contains("d-none")) {
                    const isClickInside = fontSizeBox.contains(e.target) ||
                        document.querySelector(".btn-chinh-co-chu-tool")?.contains(e.target);

                    if (!isClickInside) {
                        gsap.to(fontSizeBox, {
                            opacity: 0,
                            y: 20,
                            duration: 0.3,
                            ease: "power2.in",
                            onComplete: () => {
                                fontSizeBox.classList.add("d-none");
                            }
                        });
                    }
                }
            });
        }

        // Khởi tạo khi DOM sẵn sàng
        document.addEventListener("DOMContentLoaded", function() {
            // Thiết lập sự kiện
            setupFontSizeEvents();
            setupToolButtonEvent();
            setupAutoHide();
            setupRemoveBreaksToggle();

            // Áp dụng cỡ chữ đã lưu
            try {
                const savedFontSize = localStorage.getItem("fontSize");
                if (savedFontSize) {
                    const numericSize = parseInt(savedFontSize);
                    if (!isNaN(numericSize) && numericSize >= 12 && numericSize <= 32) {
                        fontSizeRange.value = numericSize;
                        updateFontSize(numericSize);
                    }
                } else {
                    // Áp dụng giá trị mặc định
                    updateFontSize(fontSizeRange.value);
                }
            } catch (e) {
                console.warn('⚠️ Không thể đọc cỡ chữ đã lưu:', e.message);
            }

            // Áp dụng trạng thái ẩn xuống dòng đã lưu
            try {
                const removeBreaksStored = localStorage.getItem("removeBreaks");
                if (removeBreaksStored !== null) {
                    const isChecked = removeBreaksStored === "true";
                    if (removeBreaksToggle) {
                        removeBreaksToggle.checked = isChecked;
                        triggerBreakToggle();
                    }
                }
            } catch (e) {
                console.warn('⚠️ Không thể đọc trạng thái ẩn xuống dòng:', e.message);
            }

            // Kiểm tra thiết bị di động & bật mặc định "ẩn xuống dòng"
            const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
            if (isMobile && localStorage.getItem("removeBreaks") === null && removeBreaksToggle) {
                removeBreaksToggle.checked = true;
                triggerBreakToggle();
                try {
                    localStorage.setItem("removeBreaks", "true");
                    console.log('💾 Đã bật mặc định ẩn xuống dòng cho thiết bị di động');
                } catch (e) {
                    console.warn('⚠️ Không thể lưu trạng thái ẩn xuống dòng mặc định:', e.message);
                }
            }
        });
    })();
</script>


<script>
    // Hủy bỏ user-select và ngăn chặn các hành động không mong muốn
    setInterval(function() {
        // Hủy bỏ vùng chọn văn bản
        const selection = window.getSelection();
        if (selection && selection.rangeCount > 0) {
            const selectedText = selection.toString();
            if (selectedText.length > 0) {
                selection.removeAllRanges(); // Hủy bỏ vùng chọn
            }
        }



    }, 1000); // Kiểm tra mỗi 1000ms

    document.addEventListener("copy", (event) => {
        event.clipboardData.setData("text/plain", "Nội dung đã bị chặn sao chép!");
        event.preventDefault(); // Ngăn sao chép nội dung thực tế
        console.warn("Hành động sao chép đã bị thay thế.");
    });
</script>
    <script>
        // Xử lý affiliate click và hiển thị nội dung
        function trackAffiliateClick(truyen_id) {
            // Lưu cookie trạng thái đã click
            setCookie('affiliate_clicked', truyen_id + ':' + Math.floor(Date.now() / 1000), 30);

            // Lấy các phần tử cần thao tác
            var affiliateNotification = document.getElementById('affiliate-notification');
            var chapterContent = document.getElementById('chapter-content');

            // Gửi AJAX để lưu lượt click
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'sources/ajax/mongdaovien/action_click_affiliate.php', true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4) {
                    console.log('Đã ghi nhận lượt click affiliate');

                    // Ẩn thông báo affiliate
                    if (affiliateNotification) {
                        affiliateNotification.style.display = 'none';
                    }

                    // Hiển thị nội dung chương
                    if (chapterContent) {
                        chapterContent.style.display = 'block';
                    } else {
                        // Tìm các phần tử chương có thể có
                        var contentElements = document.querySelectorAll('.chapter-content, .chapter-detail, .noi-dung, .content-chapter');
                        contentElements.forEach(function(el) {
                            el.style.display = 'block';
                        });
                    }
                }
            };
            xhr.send('action=track_affiliate_click&truyen_id=' + truyen_id);

            // Cho phép chuyển hướng đi
            return true;
        }

        // Hàm set cookie
        function setCookie(name, value, days) {
            var expires = '';
            if (days) {
                var date = new Date();
                date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
                expires = '; expires=' + date.toUTCString();
            }
            document.cookie = name + '=' + value + expires + '; path=/';
        }

        // Hàm kiểm tra trạng thái cookie khi tải trang
        function checkAffiliateStatus() {
            // Lấy trạng thái đã click từ cookie
            var clicked = getCookie('affiliate_clicked');
            var truyen_id = 2436;

            // Nếu là admin, không hiển thị affiliate
            
            if (clicked) {
                // Kiểm tra thời gian đã click
                var parts = clicked.split(':');
                if (parts.length === 2) {
                    var clickedTruyenId = parts[0];
                    var timestamp = parseInt(parts[1]);
                    var timeInterval = 30;

                    // Nếu truyện giống nhau và chưa hết thời gian
                    if (clickedTruyenId == truyen_id && (Date.now() / 1000 - timestamp) <= (timeInterval * 60)) {
                        hideAffiliateNotice();
                        return;
                    }
                }
            }

            // Nếu chưa click, hiển thị thông báo affiliate
            showAffiliateNotice();
        }

        // Hàm lấy cookie
        function getCookie(name) {
            var nameEQ = name + '=';
            var ca = document.cookie.split(';');
            for (var i = 0; i < ca.length; i++) {
                var c = ca[i];
                while (c.charAt(0) === ' ') c = c.substring(1, c.length);
                if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
            }
            return null;
        }

        // Ẩn thông báo affiliate và hiển thị nội dung
        function hideAffiliateNotice() {
            var notification = document.getElementById('affiliate-notification');
            if (notification) {
                notification.style.display = 'none';
            }

            // Hiển thị nội dung chương
            var chapterContent = document.getElementById('chapter-content');
            if (chapterContent) {
                chapterContent.style.display = 'block';
            } else {
                // Tìm các phần tử nội dung có thể có
                var contentElements = document.querySelectorAll('.chapter-content, .chapter-detail, .noi-dung, .content-chapter');
                contentElements.forEach(function(el) {
                    el.style.display = 'block';
                });
            }
        }

        // Hiển thị thông báo affiliate
        function showAffiliateNotice() {
            var notification = document.getElementById('affiliate-notification');
            if (notification) {
                // Ẩn nội dung chương
                var chapterContent = document.getElementById('chapter-content');
                if (chapterContent) {
                    chapterContent.style.display = 'none';
                } else {
                    // Tìm các phần tử nội dung có thể có
                    var contentElements = document.querySelectorAll('.chapter-content, .chapter-detail, .noi-dung, .content-chapter');
                    contentElements.forEach(function(el) {
                        el.style.display = 'none';
                    });
                }

                // Hiển thị thông báo
                notification.style.display = 'flex';
            }
        }

        // Kiểm tra khi trang đã tải xong
        document.addEventListener('DOMContentLoaded', function() {

        });
        // Kiểm tra trạng thái affiliate
        if (document.getElementById('affiliate-notification')) {
            checkAffiliateStatus();
        }
    </script>

    <script>
        // Biến toàn cục để lưu trữ trạng thái
        var affiliateCookieName = 'affiliate_clicked';

        // Hàm xử lý click vào liên kết affiliate
        function trackAffiliateClick(truyen_id) {
            // Lưu cookie
            setCookie(affiliateCookieName, truyen_id + ':' + Math.floor(Date.now() / 1000), 30);

            // Gửi AJAX theo dõi click
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'sources/ajax/mongdaovien/action_click_affiliate.php', true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4) {
                    console.log('Đã ghi nhận affiliate click thành công');

                    // Ẩn modal affiliate
                    var affiliateNotification = document.getElementById('affiliate-notification');
                    if (affiliateNotification) {
                        affiliateNotification.style.display = 'none';
                    }

                    // Hiển thị nội dung chương
                    showChapterContent();
                }
            };

            xhr.send('action=track_affiliate_click&truyen_id=' + truyen_id);

            // Hiển thị nội dung ngay lập tức, không đợi AJAX hoàn thành
            showChapterContent();

            // Trả về true để cho phép mở link trong tab mới
            return true;
        }

        // Hiển thị nội dung chương
        function showChapterContent() {
            // Hiển thị nội dung chương
            var content = document.getElementById('noi_dung_truyen');
            if (content) {
                content.classList.remove('hidden-content');
            }
        }

        // Hàm kiểm tra cookie khi tải trang
        function checkAffiliateStatus() {
            var truyen_id = 2436;
            var clicked = getCookie(affiliateCookieName);

            // Nếu là admin, luôn hiển thị nội dung
            
            if (clicked) {
                // Đã click trước đó, kiểm tra ID truyện và thời gian
                var parts = clicked.split(':');
                if (parts.length === 2) {
                    var clickedTruyenId = parts[0];
                    var timestamp = parseInt(parts[1]);
                    var timeInterval = 30;

                    // Nếu là truyện hiện tại và chưa hết thời gian
                    if (clickedTruyenId == truyen_id && (Date.now() / 1000 - timestamp) <= (timeInterval * 60)) {
                        // Hiển thị nội dung và ẩn modal
                        showChapterContent();
                        hideAffiliateModal();
                        return;
                    }
                }
            }

            // Chưa click hoặc đã hết hạn, ẩn nội dung và hiển thị modal
            hideChapterContent();
            showAffiliateModal();
        }

        // Ẩn modal affiliate
        function hideAffiliateModal() {
            var modal = document.getElementById('affiliate-notification');
            if (modal) {
                modal.style.display = 'none';
            }
        }

        // Hiển thị modal affiliate
        function showAffiliateModal() {
            var modal = document.getElementById('affiliate-notification');
            if (modal) {
                modal.style.display = 'flex';
            }
        }

        // Ẩn nội dung chương
        function hideChapterContent() {
            var content = document.getElementById('noi_dung_truyen');
            if (content) {
                content.classList.add('hidden-content');
            }
        }

        // Hàm lấy cookie
        function getCookie(name) {
            var nameEQ = name + "=";
            var ca = document.cookie.split(';');
            for (var i = 0; i < ca.length; i++) {
                var c = ca[i];
                while (c.charAt(0) === ' ') c = c.substring(1, c.length);
                if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
            }
            return null;
        }

        // Hàm đặt cookie
        function setCookie(name, value, days) {
            var expires = "";
            if (days) {
                var date = new Date();
                date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
                expires = "; expires=" + date.toUTCString();
            }
            document.cookie = name + "=" + (value || "") + expires + "; path=/";
        }

        // Kiểm tra khi trang tải xong
        document.addEventListener('DOMContentLoaded', function() {
            // Kiểm tra trạng thái affiliate để hiển thị/ẩn nội dung
            checkAffiliateStatus();
        });
    </script>

<!-- Thêm JavaScript để kiểm tra thời gian đọc -->
<script>
    $(document).ready(function() {
        // Kiểm tra xem đã có session lưu lượt đọc chưa
                    const startTime = Math.floor(Date.now() / 1000);
            let requiredTime = 100;
            let hasIncremented = false;
            let showDisplay = 0;
            console.log('Bắt đầu đếm thời gian đọc');

            // Hiển thị thời gian còn lại cho người dùng
            let timeLeftDisplay = $('<div>', {
                class: 'time-left-display',
                css: {
                    position: 'fixed',
                    bottom: '20px',
                    left: '20px',
                    padding: '10px 15px',
                    background: 'rgba(0, 0, 0, 0.7)',
                    color: '#fff',
                    borderRadius: '5px',
                    zIndex: 1000,
                    fontSize: '14px',
                    display: showDisplay ? 'block' : 'none'
                }
            }).appendTo('body');

            // Kiểm tra thời gian mỗi giây
            const timer = setInterval(function() {
                if (hasIncremented) {
                    clearInterval(timer);
                    return;
                }

                let currentTime = Math.floor(Date.now() / 1000);
                let timeSpent = currentTime - startTime;
                let timeLeft = requiredTime - timeSpent;

                // Hiển thị thời gian còn lại
                if (timeLeft > 0 && showDisplay) {
                    timeLeftDisplay.html(`<i class="fas fa-clock me-2"></i><span class="time-left-text">Thời gian còn lại:</span> ${timeLeft} giây`).fadeIn();
                }

                // Nếu đã đọc đủ thời gian
                if (timeSpent >= requiredTime && !hasIncremented) {
                    hasIncremented = true;

                    // Gửi request tăng lượt đọc
                    $.ajax({
                        url: 'sources/ajax/mongdaovien/tang-luot-doc.php',
                        type: 'POST',
                        data: {
                            chapter_id: 13365,
                            id_truyen: 2436                        },
                        success: function(response) {
                            try {
                                let result = JSON.parse(response);
                                if (result.status === 'success') {
                                    // Hiển thị thông báo thành công (chỉ khi cấu hình cho phép)
                                    if (showDisplay) {
                                        timeLeftDisplay.html('<i class="fas fa-check-circle me-2"></i>Đã ghi nhận lượt đọc')
                                            .css('background', 'rgba(40, 167, 69, 0.7)')
                                            .delay(3000)
                                            .fadeOut();
                                    }
                                }
                            } catch (e) {
                                console.error('Error parsing response:', e);
                            }
                        },
                        error: function() {
                            // Hiển thị thông báo lỗi (chỉ khi cấu hình cho phép)
                            if (showDisplay) {
                                timeLeftDisplay.html('<i class="fas fa-exclamation-circle me-2"></i>Lỗi ghi nhận lượt đọc')
                                    .css('background', 'rgba(220, 53, 69, 0.7)')
                                    .delay(3000)
                                    .fadeOut();
                            }
                        }
                    });

                    clearInterval(timer);
                }
            }, 1000);

            // Thêm CSS cho hiệu ứng
            $('<style>')
                .text(`
                .time-left-display {
                    animation: fadeInUp 0.3s ease-out;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
                    backdrop-filter: blur(5px);
                }
                @keyframes fadeInUp {
                    from {
                        opacity: 0;
                        transform: translateY(20px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }
                .time-left-display i {
                    animation: pulse 1s infinite;
                }
                @keyframes pulse {
                    0% { transform: scale(1); }
                    50% { transform: scale(1.1); }
                    100% { transform: scale(1); }
                }
            `)
                .appendTo('head');

            // Xử lý khi người dùng rời trang
            $(window).on('beforeunload', function() {
                clearInterval(timer);
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