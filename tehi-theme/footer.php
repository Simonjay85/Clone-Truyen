</script>

<!-- Mới cập nhật Swiper -->
<script>
  var swiper_slider_moi_cap_nhat = new Swiper(".swiper-slider-truyen-cung-tac-gia", {
    slidesPerView: 3,
    spaceBetween: 0
    // loop: true,
  });
</script>

<footer class="truyen-footer position-relative bg-light mt-5 border-top border-2 border-primary">
    <div class="container py-4">
        <div class="row text-center text-md-start align-items-center">
            <div class="col-md-6 mb-3 mb-md-0">
                <a href="<?php echo esc_url(home_url('/')); ?>" class="d-inline-flex align-items-center gap-2 text-decoration-none">
                    <img src="https://tehitruyen.com/img_data/images/logo-truyen-moi-v1.png" alt="TeHi Truyện" style="height: 40px; max-width: 100%; object-fit: contain;">
                </a>
                <p class="mt-3 text-muted" style="font-size: 0.9rem;">
                    TeHi Truyện – Đọc Truyện Ngôn Tình Hay Nhất 2026 chọn lọc, nội dung cuốn hút.
                </p>
            </div>
            <div class="col-md-6 text-center text-md-end">
                <p class="mb-0 text-muted" style="font-size: 0.85rem;">
                    © 2026 <a href="<?php echo esc_url(home_url('/')); ?>" class="fw-bold text-decoration-none text-primary">TeHiTruyen.com</a>. Mọi quyền được bảo lưu.
                </p>
                <div class="d-flex justify-content-center justify-content-md-end gap-2 mt-2">
                    <a href="#" class="text-secondary"><i class="fa-brands fa-facebook fs-5 hover-text-primary transition-all"></i></a>
                    <a href="#" class="text-secondary"><i class="fa-brands fa-twitter fs-5 hover-text-primary transition-all"></i></a>
                    <a href="#" class="text-secondary"><i class="fa-brands fa-telegram fs-5 hover-text-primary transition-all"></i></a>
                </div>
            </div>
        </div>
    </div>
</footer>

<?php wp_footer(); ?>
</body>
</html>
