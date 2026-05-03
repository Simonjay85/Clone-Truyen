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

<?php if (!is_singular('chuong')): ?>
</main><!-- /main-content -->
<footer class="mkm-footer">
    <div class="mkm-footer-top">
        <!-- ... inside stays the same ... -->
        <!-- BRAND -->
        <div class="mkm-footer-brand">
            <a href="<?php echo esc_url(home_url('/')); ?>">
                <img src="<?php echo get_template_directory_uri(); ?>/img_data/images/logo-truyen-moi-v1.png" alt="<?php bloginfo('name'); ?>">
            </a>
            <p>Kho truyện full & ngôn tình tuyển chọn – đọc mượt, giao diện hiện đại, nhiều chế độ nền.</p>
        </div>

        <!-- THÔNG TIN -->
        <div class="mkm-footer-col">
            <h4>Thông tin</h4>
            <ul>
                <li><a href="<?php echo esc_url(home_url('/gioi-thieu/')); ?>"><svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>Giới thiệu</a></li>
                <li><a href="<?php echo esc_url(home_url('/chinh-sach-bao-mat/')); ?>"><svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>Chính sách bảo mật</a></li>
                <li><a href="<?php echo esc_url(home_url('/dieu-khoan-su-dung/')); ?>"><svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>Điều khoản sử dụng</a></li>
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
                <li><a href="<?php echo esc_url(home_url('/bang-xep-hang/')); ?>">• Top ngôn tình hay nhất</a></li>
                <li><a href="<?php echo esc_url(home_url('/?s=ngon+tinh+hien+dai')); ?>">• Top ngôn tình hiện đại</a></li>
                <li><a href="<?php echo esc_url(home_url('/?s=tong+tai')); ?>">• Top tổng tài hay nhất</a></li>
                <li><a href="<?php echo esc_url(home_url('/?s=ngon+tinh+co+dai')); ?>">• Top ngôn tình cổ đại</a></li>
                <li><a href="<?php echo esc_url(home_url('/?s=xuyen+khong')); ?>">• Top xuyên không hay</a></li>
                <li><a href="<?php echo esc_url(home_url('/?s=quan+nhan')); ?>">• Top truyện quân nhân</a></li>
            </ul>
        </div>

        <!-- KẾT NỐI -->
        <div class="mkm-footer-col">
            <h4>Kết nối</h4>
            <p style="font-size:12px; color:#6b7280; margin:0 0 10px;">Theo dõi để nhận thông báo chương mới:</p>
            <div class="mkm-footer-social">
                <a href="<?php echo esc_url(get_option('tehi_facebook_group_url') ?: home_url('/')); ?>">
                    <svg width="18" height="18" fill="#1877f2" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                    Fanpage
                </a>
                <a href="<?php echo esc_url(home_url('/nhom-dich/')); ?>">
                    <svg width="18" height="18" fill="#ff0000" viewBox="0 0 24 24"><path d="M23.495 6.205a3.007 3.007 0 0 0-2.088-2.088c-1.87-.501-9.396-.501-9.396-.501s-7.507-.01-9.396.501A3.007 3.007 0 0 0 .527 6.205a31.247 31.247 0 0 0-.522 5.805 31.247 31.247 0 0 0 .522 5.783 3.007 3.007 0 0 0 2.088 2.088c1.868.502 9.396.502 9.396.502s7.506 0 9.396-.502a3.007 3.007 0 0 0 2.088-2.088 31.247 31.247 0 0 0 .5-5.783 31.247 31.247 0 0 0-.5-5.805zM9.609 15.601V8.408l6.264 3.602z"/></svg>
                    YouTube
                </a>
            </div>
            <p style="font-size:12px; color:#6b7280; margin:0 0 8px;">Tải ứng dụng</p>
            <div class="mkm-footer-apps">
                <a href="<?php echo esc_url(home_url('/')); ?>" aria-label="App Store">
                    <svg width="20" height="20" fill="white" viewBox="0 0 24 24"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.8-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>
                    <div><span>Tải về</span><strong>App Store</strong></div>
                </a>
                <a href="<?php echo esc_url(home_url('/')); ?>" aria-label="Google Play">
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
<?php else: ?>
</main><!-- /main-content -->
<?php endif; ?>

<!-- AUTH MODAL -->
<style>#mkmAuthModal { opacity: 0; pointer-events: none; visibility: hidden; transition: all 0.3s ease; } #mkmAuthModal.active { opacity: 1; pointer-events: auto; visibility: visible; } #mkmAuthModal .mkm-auth-modal { max-height: 90vh; overflow-y: auto; }</style>
<div class="mkm-auth-overlay" id="mkmAuthModal">
    <div class="mkm-auth-modal">
        <!-- Header -->
        <div class="mkm-auth-header">
            <div class="mkm-auth-tabs">
                <button class="mkm-auth-tab active" data-tab="login" onclick="mkmSwitchAuthTab('login')">Đăng nhập</button>
                <div class="mkm-auth-tab-divider">/</div>
                <button class="mkm-auth-tab" data-tab="register" onclick="mkmSwitchAuthTab('register')">Đăng ký</button>
            </div>
            <button class="mkm-auth-close" onclick="mkmCloseAuthModal()">×</button>
        </div>
        
        <div class="mkm-auth-body">
            <!-- LOGIN FORM -->
            <form id="mkmLoginForm" class="mkm-auth-form active" onsubmit="mkmSubmitAuth(event, 'login')">
                <div class="mkm-form-group">
                    <label>Email</label>
                    <div class="mkm-input-wrap">
                        <i class="fa-regular fa-envelope"></i>
                        <input type="email" name="user_email" placeholder="you@example.com" required>
                    </div>
                </div>
                <div class="mkm-form-group">
                    <label>Mật khẩu</label>
                    <div class="mkm-input-wrap">
                        <i class="fa-solid fa-lock"></i>
                        <input type="password" name="user_pass" placeholder="••••••••" required>
                        <i class="fa-regular fa-eye mkm-pwd-toggle" onclick="mkmTogglePwd(this)"></i>
                    </div>
                </div>
                
                <div class="mkm-auth-options">
                    <a href="<?php echo wp_lostpassword_url(); ?>" class="mkm-auth-link">Quên mật khẩu?</a>
                </div>
                
                <div class="mkm-auth-alert" id="mkmLoginAlert" style="display:none;"></div>
                
                <button type="submit" class="mkm-btn-primary mkm-btn-submit">
                    <i class="fa-solid fa-arrow-right-to-bracket"></i> Đăng nhập
                </button>
                
                <!-- Google Login Button (Requires Nextend Social Login) -->
                <a href="<?php echo get_site_url(); ?>/?loginSocial=google" class="mkm-btn-google">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" alt="Google"> Tiếp tục với Google
                </a>
                
                <div class="mkm-auth-footer-text">
                    Chưa có tài khoản? <button type="button" onclick="mkmSwitchAuthTab('register')" style="background:none;border:none;color:#4f46e5;cursor:pointer;font:inherit;font-weight:600;padding:0;">Đăng ký</button>
                </div>
                
                <div class="mkm-auth-close-text" onclick="mkmCloseAuthModal()">Đóng</div>
            </form>

            <!-- REGISTER FORM -->
            <form id="mkmRegisterForm" class="mkm-auth-form" onsubmit="mkmSubmitAuth(event, 'register')">
                <div class="mkm-form-group">
                    <label>Tên hiển thị</label>
                    <div class="mkm-input-wrap">
                        <i class="fa-regular fa-user"></i>
                        <input type="text" name="user_display" placeholder="VD: Mèo Mập" required>
                    </div>
                </div>
                <div class="mkm-form-group">
                    <label>Email</label>
                    <div class="mkm-input-wrap">
                        <i class="fa-regular fa-envelope"></i>
                        <input type="email" name="user_email" placeholder="you@example.com" required>
                    </div>
                </div>
                <div class="mkm-form-group">
                    <label>Mật khẩu</label>
                    <div class="mkm-input-wrap">
                        <i class="fa-solid fa-lock"></i>
                        <input type="password" name="user_pass" placeholder="Tối thiểu 6 ký tự" minlength="6" required>
                         <i class="fa-regular fa-eye mkm-pwd-toggle" onclick="mkmTogglePwd(this)"></i>
                    </div>
                </div>
                
                <div class="mkm-auth-alert" id="mkmRegisterAlert" style="display:none;"></div>
                
                <button type="submit" class="mkm-btn-primary mkm-btn-submit">
                    <i class="fa-solid fa-user-plus"></i> Đăng ký
                </button>
                
                <!-- Google Login Button -->
                <a href="<?php echo get_site_url(); ?>/?loginSocial=google" class="mkm-btn-google">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" alt="Google"> Tiếp tục với Google
                </a>
                
                <div class="mkm-auth-footer-text">
                    Đã có tài khoản? <button type="button" onclick="mkmSwitchAuthTab('login')" style="background:none;border:none;color:#4f46e5;cursor:pointer;font:inherit;font-weight:600;padding:0;">Đăng nhập</button>
                </div>
                
                <div class="mkm-auth-close-text" onclick="mkmCloseAuthModal()">Đóng</div>
            </form>
        </div>
    </div>
</div>

<script>
// JS Logic for the Auth Modal
function mkmOpenAuthModal(tab = 'login') {
    const modal = document.getElementById('mkmAuthModal');
    if (!modal) return;
    modal.classList.add('active');
    mkmSwitchAuthTab(tab);
    document.body.style.overflow = 'hidden';
}
function mkmCloseAuthModal() {
    const modal = document.getElementById('mkmAuthModal');
    if (!modal) return;
    modal.classList.remove('active');
    document.body.style.overflow = '';
}
function mkmSwitchAuthTab(tab) {
    // Reset tabs
    document.querySelectorAll('.mkm-auth-tab').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.mkm-auth-form').forEach(el => el.classList.remove('active'));
    // Set active
    const activeTab = document.querySelector('.mkm-auth-tab[data-tab="'+tab+'"]');
    const activeForm = document.getElementById(tab === 'login' ? 'mkmLoginForm' : 'mkmRegisterForm');
    if (activeTab) activeTab.classList.add('active');
    if (activeForm) activeForm.classList.add('active');
}
function mkmTogglePwd(icon) {
    const input = icon.previousElementSibling;
    if (!input) return;
    if (input.type === 'password') {
        input.type = 'text';
        icon.classList.remove('fa-eye');
        icon.classList.add('fa-eye-slash');
    } else {
        input.type = 'password';
        icon.classList.remove('fa-eye-slash');
        icon.classList.add('fa-eye');
    }
}
function mkmSubmitAuth(e, type) {
    e.preventDefault();
    const form = e.target;
    const btn = form.querySelector('.mkm-btn-submit');
    const alertBox = form.querySelector('.mkm-auth-alert');
    const formData = new FormData(form);
    formData.append('action', type === 'login' ? 'tehi_ajax_login' : 'tehi_ajax_register');
    
    // UI Loading state
    const originalBtnText = btn.innerHTML;
    btn.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Đang xử lý...';
    btn.disabled = true;
    btn.style.opacity = '0.7';
    alertBox.style.display = 'none';

    fetch('<?php echo admin_url("admin-ajax.php"); ?>', {
        method: 'POST',
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        alertBox.style.display = 'block';
        if(data.success) {
            alertBox.style.backgroundColor = '#d1fae5';
            alertBox.style.color = '#065f46';
            alertBox.innerHTML = '<i class="fa-solid fa-check-circle"></i> ' + data.data.message;
            setTimeout(() => { window.location.reload(); }, 1000);
        } else {
            alertBox.style.backgroundColor = '#fee2e2';
            alertBox.style.color = '#991b1b';
            alertBox.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> ' + data.data.message;
            btn.innerHTML = originalBtnText;
            btn.disabled = false;
            btn.style.opacity = '1';
        }
    })
    .catch(err => {
        alert("Lỗi kết nối máy chủ!");
        btn.innerHTML = originalBtnText;
        btn.disabled = false;
        btn.style.opacity = '1';
    });
}
// Scroll to top logic
<?php if (!is_singular('chuong')): ?>
document.addEventListener("DOMContentLoaded", function() {
    let mkmScrollBtn = document.createElement("button");
    mkmScrollBtn.innerHTML = '<svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 10l7-7m0 0l7 7m-7-7v18"/></svg>';
    mkmScrollBtn.title = "Lên đầu trang";
    mkmScrollBtn.style.cssText = "display:none; position:fixed; bottom:30px; right:30px; z-index:99; width:45px; height:45px; border:none; outline:none; background:linear-gradient(135deg, #f97316, #ea580c); color:white; cursor:pointer; border-radius:50%; box-shadow:0 4px 12px rgba(234,88,12,0.3); transition:all 0.3s; align-items:center; justify-content:center;";
    document.body.appendChild(mkmScrollBtn);

    mkmScrollBtn.addEventListener("mouseover", () => mkmScrollBtn.style.transform = "translateY(-3px)");
    mkmScrollBtn.addEventListener("mouseout", () => mkmScrollBtn.style.transform = "translateY(0)");

    window.addEventListener("scroll", function() {
        if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
            mkmScrollBtn.style.display = "flex";
        } else {
            mkmScrollBtn.style.display = "none";
        }
    });

    mkmScrollBtn.addEventListener("click", function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});
<?php endif; ?>
</script>

<div id="shareModal" style="display:none;"></div>
<?php wp_footer(); ?>
</body>
</html>
