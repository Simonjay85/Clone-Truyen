<style>
.mkm-footer { background: #fff; border-top: 1px solid #e5e7eb; margin-top: 48px; font-family: 'Be Vietnam Pro', sans-serif; }
.mkm-footer-top { max-width: 1200px; margin: 0 auto; padding: 40px 16px 32px; display: grid; grid-template-columns: 1.6fr 1fr 1.4fr 1.2fr 1.2fr; gap: 32px; }
.mkm-footer-brand img { height: 36px; margin-bottom: 12px; }
.mkm-footer-brand p { font-size: 13px; color: #6b7280; line-height: 1.7; margin: 0; }
.mkm-footer-col h4 { font-size: 14px; font-weight: 800; color: #111827; margin: 0 0 14px 0; }
.mkm-footer-col ul { list-style: none; padding: 0; margin: 0; }
.mkm-footer-col ul li { margin-bottom: 8px; }
.mkm-footer-col ul li a { font-size: 13px; color: #6b7280; text-decoration: none; display: flex; align-items: center; gap: 6px; transition: color .15s; }
.mkm-footer-col ul li a:hover { color: #4f46e5; }
.mkm-footer-social { display: flex; flex-direction: column; gap: 10px; margin-bottom: 16px; }
.mkm-footer-social a { display: flex; align-items: center; gap: 10px; padding: 8px 14px; border: 1px solid #e5e7eb; border-radius: 10px; font-size: 13px; font-weight: 600; color: #374151; text-decoration: none; transition: all .15s; }
.mkm-footer-social a:hover { border-color: #4f46e5; color: #4f46e5; background: #f5f3ff; }
.mkm-footer-apps { display: flex; flex-direction: column; gap: 8px; }
.mkm-footer-apps a { display: flex; align-items: center; gap: 8px; background: #111827; color: #fff; border-radius: 10px; padding: 8px 14px; text-decoration: none; font-size: 12px; transition: background .15s; }
.mkm-footer-apps a:hover { background: #4f46e5; }
.mkm-footer-apps a span { font-size: 11px; opacity: .7; display: block; }
.mkm-footer-apps a strong { font-size: 13px; display: block; }
.mkm-footer-disclaimer { background: #fffbeb; border-top: 1px solid #fde68a; }
.mkm-footer-disclaimer-inner { max-width: 1200px; margin: 0 auto; padding: 14px 16px; display: flex; gap: 12px; align-items: flex-start; }
.mkm-footer-disclaimer-inner svg { flex-shrink: 0; color: #f59e0b; margin-top: 2px; }
.mkm-footer-disclaimer p { font-size: 12px; color: #78350f; line-height: 1.6; margin: 0; }
.mkm-footer-bottom { max-width: 1200px; margin: 0 auto; padding: 16px; text-align: center; font-size: 13px; color: #9ca3af; border-top: 1px solid #f3f4f6; }
@media (max-width: 900px) { .mkm-footer-top { grid-template-columns: 1fr 1fr; } }
@media (max-width: 600px) { .mkm-footer-top { grid-template-columns: 1fr; } }
</style>

<footer class="mkm-footer">
    <div class="mkm-footer-top">
        <!-- BRAND -->
        <div class="mkm-footer-brand">
            <a href="<?php echo esc_url(home_url('/')); ?>">
                <img src="<?php echo get_site_url(); ?>/img_data/images/logo-truyen-moi-v1.png" alt="<?php bloginfo('name'); ?>">
            </a>
            <p>Kho truyện full & ngôn tình tuyển chọn – đọc mượt, giao diện hiện đại, nhiều chế độ nền.</p>
        </div>

        <!-- THÔNG TIN -->
        <div class="mkm-footer-col">
            <h4>Thông tin</h4>
            <ul>
                <li><a href="#"><svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>Giới thiệu</a></li>
                <li><a href="#"><svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>Chính sách bảo mật</a></li>
                <li><a href="#"><svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>Điều khoản sử dụng</a></li>
            </ul>
        </div>

        <!-- DANH SÁCH TRUYỆN -->
        <div class="mkm-footer-col">
            <h4>Danh sách truyện</h4>
            <ul>
                <?php
                $cats = get_terms(['taxonomy' => 'the_loai', 'number' => 6, 'orderby' => 'count', 'order' => 'DESC', 'hide_empty' => true]);
                if (!is_wp_error($cats)) foreach($cats as $cat):
                ?>
                <li><a href="<?php echo get_term_link($cat); ?>">• <?php echo esc_html($cat->name); ?></a></li>
                <?php endforeach; ?>
            </ul>
        </div>

        <!-- TOP TRUYỆN -->
        <div class="mkm-footer-col">
            <h4>Top truyện</h4>
            <ul>
                <li><a href="#">• Top ngôn tình hay nhất</a></li>
                <li><a href="#">• Top ngôn tình hiện đại</a></li>
                <li><a href="#">• Top tổng tài hay nhất</a></li>
                <li><a href="#">• Top ngôn tình cổ đại</a></li>
                <li><a href="#">• Top xuyên không hay</a></li>
                <li><a href="#">• Top truyện quân nhân</a></li>
            </ul>
        </div>

        <!-- KẾT NỐI -->
        <div class="mkm-footer-col">
            <h4>Kết nối</h4>
            <p style="font-size:12px; color:#6b7280; margin:0 0 10px;">Theo dõi để nhận thông báo chương mới:</p>
            <div class="mkm-footer-social">
                <a href="#">
                    <svg width="18" height="18" fill="#1877f2" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                    Fanpage
                </a>
                <a href="#">
                    <svg width="18" height="18" fill="#ff0000" viewBox="0 0 24 24"><path d="M23.495 6.205a3.007 3.007 0 0 0-2.088-2.088c-1.87-.501-9.396-.501-9.396-.501s-7.507-.01-9.396.501A3.007 3.007 0 0 0 .527 6.205a31.247 31.247 0 0 0-.522 5.805 31.247 31.247 0 0 0 .522 5.783 3.007 3.007 0 0 0 2.088 2.088c1.868.502 9.396.502 9.396.502s7.506 0 9.396-.502a3.007 3.007 0 0 0 2.088-2.088 31.247 31.247 0 0 0 .5-5.783 31.247 31.247 0 0 0-.5-5.805zM9.609 15.601V8.408l6.264 3.602z"/></svg>
                    YouTube
                </a>
            </div>
            <p style="font-size:12px; color:#6b7280; margin:0 0 8px;">Tải ứng dụng</p>
            <div class="mkm-footer-apps">
                <a href="#">
                    <svg width="20" height="20" fill="white" viewBox="0 0 24 24"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.8-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>
                    <div><span>Tải về</span><strong>App Store</strong></div>
                </a>
                <a href="#">
                    <svg width="20" height="20" fill="white" viewBox="0 0 24 24"><path d="M3.18 23.76c.27.15.54.24.81.24.27 0 .54-.09.81-.24L17.1 12 3.18.24C2.91.09 2.64 0 2.37 0c-.54 0-.99.45-.99.99v22.02c0 .54.45.75.8.75zM17.82 11.28L5.58 4.92 15.6 12 5.58 19.08l12.24-6.36c.54-.27.54-1.17 0-1.44z"/></svg>
                    <div><span>Tải về</span><strong>Google Play</strong></div>
                </a>
            </div>
        </div>
    </div>

    <!-- DISCLAIMER -->
    <div class="mkm-footer-disclaimer">
        <div class="mkm-footer-disclaimer-inner">
            <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
            <p><strong>Tuyên bố miễn trừ trách nhiệm:</strong> <?php bloginfo('name'); ?> là nền tảng tổng hợp và chia sẻ nội dung giải trí. Chúng tôi luôn tôn trọng quyền sở hữu trí tuệ của người khác. Nếu bạn là tác giả hoặc chủ sở hữu bản quyền của bất kỳ nội dung nào trên website, vui lòng liên hệ để chúng tôi gỡ bỏ trong vòng 24-48 giờ.</p>
        </div>
    </div>

    <!-- BOTTOM BAR -->
    <div class="mkm-footer-bottom">
        © <?php echo date('Y'); ?> <?php bloginfo('name'); ?>. All rights reserved.
    </div>
</footer>

<?php wp_footer(); ?>
</body>
</html>
