<?php
/**
 * Template Name: Xưởng Sáng Tác AI
 * Template Post Type: page
 *
 * Trang công cụ tạo truyện AI dành cho cộng tác viên.
 * Cho phép tạo ra câu chuyện hoàn chỉnh từ ý tưởng, sau đó duyệt và tách thành chương.
 */

// ====================================================
// AUTH WALL: Show login form or permission error for non-admins
// ====================================================
$is_logged_in = is_user_logged_in();
$is_admin     = $is_logged_in && (current_user_can('administrator') || current_user_can('editor'));

if (!$is_logged_in || !$is_admin):
    $current_user_temp = wp_get_current_user();
?>
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Đăng nhập | Xưởng Sáng Tác AI</title>
    <meta name="robots" content="noindex, nofollow">
    <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Be Vietnam Pro', sans-serif;
            background: #0a0a14;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            color: #e2e8f0;
        }
        /* Animated background */
        .auth-bg {
            position: fixed; inset: 0; z-index: 0;
            background: radial-gradient(ellipse at 20% 50%, rgba(99,102,241,0.15) 0%, transparent 60%),
                        radial-gradient(ellipse at 80% 20%, rgba(167,139,250,0.1) 0%, transparent 50%),
                        radial-gradient(ellipse at 60% 80%, rgba(16,185,129,0.08) 0%, transparent 50%);
        }
        .auth-bg::before {
            content: '';
            position: absolute; inset: 0;
            background-image: radial-gradient(circle, rgba(255,255,255,0.04) 1px, transparent 1px);
            background-size: 40px 40px;
        }
        /* Card */
        .auth-card {
            position: relative; z-index: 1;
            background: rgba(255,255,255,0.04);
            backdrop-filter: blur(24px);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 20px;
            padding: 40px;
            width: 100%;
            max-width: 420px;
            box-shadow: 0 24px 80px rgba(0,0,0,0.4);
        }
        .auth-logo {
            text-align: center;
            margin-bottom: 28px;
        }
        .auth-logo-icon {
            font-size: 40px;
            display: block;
            margin-bottom: 10px;
        }
        .auth-logo-title {
            font-size: 22px;
            font-weight: 800;
            color: #fff;
        }
        .auth-logo-sub {
            font-size: 13px;
            color: rgba(255,255,255,0.4);
            margin-top: 4px;
        }
        .auth-badge {
            display: inline-block;
            background: linear-gradient(135deg, #6366f1, #a78bfa);
            color: #fff;
            padding: 2px 10px;
            border-radius: 20px;
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            margin-left: 6px;
            vertical-align: middle;
        }
        /* Login form */
        .auth-label {
            display: block;
            font-size: 12px;
            font-weight: 600;
            color: rgba(255,255,255,0.5);
            margin-bottom: 6px;
            text-transform: uppercase;
            letter-spacing: .8px;
        }
        .auth-input {
            width: 100%;
            background: rgba(0,0,0,0.3);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 10px;
            color: #e2e8f0;
            font-family: inherit;
            font-size: 14px;
            padding: 12px 14px;
            outline: none;
            transition: border-color .2s;
            margin-bottom: 16px;
        }
        .auth-input:focus { border-color: #6366f1; }
        .auth-input::placeholder { color: rgba(255,255,255,0.2); }
        .auth-btn {
            width: 100%;
            padding: 14px;
            border: none;
            border-radius: 10px;
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            color: #fff;
            font-family: inherit;
            font-size: 15px;
            font-weight: 700;
            cursor: pointer;
            transition: all .2s;
            margin-top: 4px;
        }
        .auth-btn:hover { transform: translateY(-1px); box-shadow: 0 8px 24px rgba(99,102,241,0.4); }
        .auth-divider {
            text-align: center;
            color: rgba(255,255,255,0.2);
            font-size: 12px;
            margin: 20px 0;
            position: relative;
        }
        .auth-divider::before, .auth-divider::after {
            content: '';
            position: absolute;
            top: 50%;
            width: calc(50% - 30px);
            height: 1px;
            background: rgba(255,255,255,0.08);
        }
        .auth-divider::before { left: 0; }
        .auth-divider::after { right: 0; }
        .auth-notice {
            background: rgba(239,68,68,0.1);
            border: 1px solid rgba(239,68,68,0.25);
            border-radius: 10px;
            padding: 12px 14px;
            font-size: 13px;
            color: #fca5a5;
            margin-bottom: 20px;
            display: flex;
            gap: 8px;
            align-items: flex-start;
        }
        .auth-home-link {
            display: block;
            text-align: center;
            margin-top: 20px;
            color: rgba(255,255,255,0.3);
            font-size: 13px;
            text-decoration: none;
            transition: color .2s;
        }
        .auth-home-link:hover { color: rgba(255,255,255,0.6); }
        /* Permission denied state */
        .perm-icon { font-size: 52px; text-align: center; margin-bottom: 16px; }
        .perm-title { font-size: 20px; font-weight: 800; color: #fff; text-align: center; margin-bottom: 8px; }
        .perm-sub { font-size: 13px; color: rgba(255,255,255,0.45); text-align: center; line-height: 1.6; margin-bottom: 24px; }
        .perm-user {
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 10px;
            padding: 12px 16px;
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 20px;
        }
        .perm-user-avatar {
            width: 40px; height: 40px; border-radius: 50%;
            background: linear-gradient(135deg, #6366f1, #a78bfa);
            display: flex; align-items: center; justify-content: center;
            font-size: 18px; flex-shrink: 0;
        }
        .perm-user-name { font-weight: 700; color: #fff; font-size: 14px; }
        .perm-user-role { font-size: 12px; color: rgba(255,255,255,0.35); }
        .perm-logout {
            display: block; width: 100%; padding: 12px;
            border: 1px solid rgba(255,255,255,0.1); border-radius: 10px;
            background: transparent; color: rgba(255,255,255,0.6);
            font-family: inherit; font-size: 13px; font-weight: 600;
            cursor: pointer; text-align: center; text-decoration: none;
            transition: all .2s;
        }
        .perm-logout:hover { background: rgba(255,255,255,0.06); color: #fff; }
    </style>
</head>
<body>
    <div class="auth-bg"></div>

    <div class="auth-card">
        <div class="auth-logo">
            <span class="auth-logo-icon">✨</span>
            <div class="auth-logo-title">Story Studio <span class="auth-badge">AI</span></div>
            <div class="auth-logo-sub">Xưởng Sáng Tác Trí Tuệ Nhân Tạo</div>
        </div>

        <?php if (!$is_logged_in): ?>
            <!-- ===== LOGIN FORM ===== -->
            <?php if (!empty($_GET['login']) && $_GET['login'] === 'failed'): ?>
            <div class="auth-notice">
                ⚠️ Tên đăng nhập hoặc mật khẩu không đúng. Thử lại nhé!
            </div>
            <?php endif; ?>

            <form method="post" action="<?php echo esc_url(site_url('wp-login.php', 'login_post')); ?>">
                <input type="hidden" name="redirect_to" value="<?php echo esc_attr(get_permalink()); ?>">
                <input type="hidden" name="testcookie" value="1">

                <label class="auth-label" for="studio-user">Tên đăng nhập / Email</label>
                <input type="text" id="studio-user" name="log" class="auth-input" placeholder="Nhập tài khoản..." autocomplete="username" required>

                <label class="auth-label" for="studio-pass">Mật khẩu</label>
                <input type="password" id="studio-pass" name="pwd" class="auth-input" placeholder="••••••••" autocomplete="current-password" required>

                <button type="submit" class="auth-btn" name="wp-submit" value="Log In">
                    🔐 Đăng nhập vào Studio
                </button>
            </form>

            <div class="auth-divider">Chỉ Admin / Biên tập viên mới có quyền</div>

        <?php else: ?>
            <!-- ===== PERMISSION DENIED (logged in but not admin) ===== -->
            <div class="perm-icon">🔒</div>
            <div class="perm-title">Bạn không có quyền truy cập</div>
            <div class="perm-sub">Xưởng Sáng Tác AI chỉ dành cho tài khoản <strong style="color:#a78bfa;">Quản trị viên</strong> hoặc <strong style="color:#a78bfa;">Biên tập viên</strong>. Hãy liên hệ Admin để được cấp quyền.</div>

            <div class="perm-user">
                <div class="perm-user-avatar">👤</div>
                <div>
                    <div class="perm-user-name"><?php echo esc_html($current_user_temp->display_name); ?></div>
                    <div class="perm-user-role"><?php echo esc_html(implode(', ', $current_user_temp->roles)); ?></div>
                </div>
            </div>

            <a href="<?php echo wp_logout_url(get_permalink()); ?>" class="perm-logout">
                ↩ Đăng xuất và dùng tài khoản khác
            </a>
        <?php endif; ?>

        <a href="<?php echo home_url(); ?>" class="auth-home-link">← Quay về trang chủ</a>
    </div>
</body>
</html>
<?php
// Stop here - don't render the studio
die();
endif;
// ====================================================
// END AUTH WALL - only admins/editors reach below here
// ====================================================

$current_user = wp_get_current_user();
$ajax_url = admin_url('admin-ajax.php');
$nonce = wp_create_nonce('temply_ai_nonce');
?>
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Xưởng Sáng Tác AI ✨ | Bệnh Viện Truyện</title>
    <meta name="robots" content="noindex, nofollow">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <?php wp_head(); ?>
    <style>
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        
        body {
            font-family: 'Be Vietnam Pro', sans-serif;
            background: #0f0f17;
            color: #e2e8f0;
            min-height: 100vh;
            overflow-x: hidden;
        }

        /* ====== HEADER ====== */
        .studio-nav {
            background: rgba(15, 15, 23, 0.9);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid rgba(255,255,255,0.07);
            padding: 0 24px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        .studio-logo {
            display: flex;
            align-items: center;
            gap: 10px;
            font-weight: 800;
            font-size: 18px;
            color: #fff;
            text-decoration: none;
        }
        .studio-logo-badge {
            background: linear-gradient(135deg, #6366f1, #a78bfa);
            color: #fff;
            padding: 2px 10px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
        }
        .studio-nav-right { display: flex; align-items: center; gap: 16px; font-size: 13px; }
        .studio-user-chip { 
            background: rgba(255,255,255,0.07); 
            border: 1px solid rgba(255,255,255,0.1);
            padding: 6px 14px; border-radius: 20px; font-size: 13px; color: #cbd5e1; 
        }
        .studio-home-link { color: #7c86a2; text-decoration: none; font-size: 13px; transition: color .2s; }
        .studio-home-link:hover { color: #e2e8f0; }

        /* ====== MAIN LAYOUT ====== */
        .studio-layout {
            display: grid !important;
            grid-template-columns: 360px 1fr !important;
            height: calc(100vh - 60px);
            overflow: hidden;
        }
        .studio-layout > aside { grid-column: 1; grid-row: 1; }
        .studio-layout > main  { grid-column: 2; grid-row: 1; min-width: 0; }

        /* ====== SIDEBAR (Control Panel) ====== */
        .studio-sidebar {
            background: #13131f;
            border-right: 1px solid rgba(255,255,255,0.06);
            overflow-y: auto;
            padding: 24px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        .panel-title {
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            color: #6b7a99;
            margin-bottom: 12px;
        }
        .ctrl-group {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.07);
            border-radius: 12px;
            padding: 16px;
        }
        .ctrl-label {
            font-size: 12px;
            font-weight: 600;
            color: #94a3b8;
            margin-bottom: 8px;
            display: block;
        }
        .ctrl-input, .ctrl-textarea, .ctrl-select {
            width: 100%;
            background: rgba(0,0,0,0.3);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 8px;
            color: #e2e8f0;
            font-family: inherit;
            font-size: 13px;
            padding: 10px 12px;
            outline: none;
            transition: border-color .2s;
            resize: vertical;
        }
        .ctrl-input:focus, .ctrl-textarea:focus, .ctrl-select:focus {
            border-color: #6366f1;
        }
        .ctrl-textarea { min-height: 80px; }
        .ctrl-select option { background: #1e1e2e; }

        /* Genre tags */
        .genre-tags { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px; }
        .genre-tag {
            padding: 5px 12px;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.1);
            font-size: 12px;
            color: #94a3b8;
            cursor: pointer;
            transition: all .2s;
        }
        .genre-tag:hover, .genre-tag.active {
            border-color: #6366f1;
            color: #a78bfa;
            background: rgba(99,102,241,0.15);
        }

        /* Action buttons */
        .btn-generate {
            width: 100%;
            padding: 14px;
            border-radius: 10px;
            border: none;
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            color: #fff;
            font-family: inherit;
            font-size: 15px;
            font-weight: 700;
            cursor: pointer;
            transition: all .2s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            position: relative;
            overflow: hidden;
        }
        .btn-generate:hover { transform: translateY(-1px); box-shadow: 0 8px 24px rgba(99,102,241,0.35); }
        .btn-generate:disabled { opacity: 0.6; cursor: not-allowed; transform: none; }

        .btn-split {
            width: 100%;
            padding: 12px;
            border-radius: 10px;
            border: 1px dashed #8b5cf6;
            background: rgba(139,92,246,0.08);
            color: #a78bfa;
            font-family: inherit;
            font-size: 14px;
            font-weight: 700;
            cursor: pointer;
            transition: all .2s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        .btn-split:hover { background: rgba(139,92,246,0.2); border-color: #a78bfa; }
        .btn-split:disabled { opacity: 0.4; cursor: not-allowed; }

        .btn-new {
            width: 100%;
            padding: 10px;
            border-radius: 10px;
            border: 1px solid rgba(255,255,255,0.1);
            background: transparent;
            color: #94a3b8;
            font-family: inherit;
            font-size: 13px;
            cursor: pointer;
            transition: all .2s;
        }
        .btn-new:hover { background: rgba(255,255,255,0.05); color: #e2e8f0; }

        /* Stats */
        .stats-row { display: flex; gap: 12px; margin-top: 4px; }
        .stat-chip {
            flex: 1;
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.07);
            border-radius: 8px;
            padding: 10px;
            text-align: center;
        }
        .stat-chip .val { font-size: 20px; font-weight: 800; color: #a78bfa; }
        .stat-chip .lbl { font-size: 11px; color: #6b7a99; margin-top: 2px; }

        /* Progress bar */
        .progress-wrap {
            display: none;
            flex-direction: column;
            gap: 8px;
            padding: 12px;
            background: rgba(99,102,241,0.08);
            border: 1px solid rgba(99,102,241,0.2);
            border-radius: 10px;
        }
        .progress-wrap.active { display: flex; }
        .progress-label { font-size: 12px; color: #94a3b8; }
        .progress-bar-bg { width: 100%; height: 4px; background: rgba(255,255,255,0.08); border-radius: 99px; overflow: hidden; }
        .progress-bar-fill { height: 100%; background: linear-gradient(90deg, #6366f1, #a78bfa); border-radius: 99px; width: 0%; transition: width .4s ease; }
        
        /* Result chapters list */
        .chapters-list { display: flex; flex-direction: column; gap: 8px; max-height: 240px; overflow-y: auto; }
        .chapter-chip {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 12px;
            background: rgba(16,185,129,0.05);
            border: 1px solid rgba(16,185,129,0.15);
            border-radius: 8px;
            font-size: 12px;
            color: #6ee7b7;
        }
        .chapter-chip .num { 
            width: 24px; height: 24px; border-radius: 6px; 
            background: rgba(16,185,129,0.2); color: #10b981; 
            display: flex; align-items: center; justify-content: center; 
            font-size: 11px; font-weight: 700; flex-shrink: 0; 
        }

        /* ====== EDITOR AREA ====== */
        .studio-editor {
            display: flex;
            flex-direction: column;
            overflow: hidden;
            background: #0f0f17;
            min-height: 0;
        }
        .editor-toolbar {
            background: #17172a;
            border-bottom: 1px solid rgba(255,255,255,0.06);
            padding: 10px 20px;
            display: flex;
            align-items: center;
            gap: 12px;
            flex-shrink: 0;
        }
        .editor-status {
            font-size: 12px;
            color: #6b7a99;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .status-dot { width: 8px; height: 8px; border-radius: 50%; background: #4b5563; flex-shrink: 0; }
        .status-dot.active { background: #10b981; box-shadow: 0 0 8px rgba(16,185,129,0.5); animation: pulse 2s infinite; }
        .status-dot.loading { background: #f59e0b; box-shadow: 0 0 8px rgba(245,158,11,0.5); animation: pulse .8s infinite; }
        @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.4} }
        
        .editor-word-count { margin-left: auto; font-size: 12px; color: #4b5563; font-variant-numeric: tabular-nums; }

        .editor-content-area {
            flex: 1;
            overflow-y: auto;
            padding: 32px;
        }
        
        /* Empty State */
        .editor-empty {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
            color: #374151;
            text-align: center;
            gap: 16px;
        }
        .editor-empty-icon { font-size: 64px; opacity: 0.3; }
        .editor-empty-title { font-size: 20px; font-weight: 700; color: #4b5563; }
        .editor-empty-sub { font-size: 14px; color: #374151; max-width: 360px; line-height: 1.6; }

        /* AI writing animation area */
        .story-output {
            display: none;
            flex-direction: column;
            gap: 0;
        }
        .story-output.visible { display: flex; }
        
        .story-post-title {
            font-size: 28px;
            font-weight: 800;
            color: #fff;
            margin-bottom: 24px;
            line-height: 1.3;
            border-bottom: 1px solid rgba(255,255,255,0.06);
            padding-bottom: 20px;
        }

        .story-text {
            font-size: 16px;
            line-height: 1.9;
            color: #cbd5e1;
        }
        .story-text h2, .story-text h3 {
            color: #a78bfa;
            font-size: 18px;
            font-weight: 700;
            margin: 32px 0 12px;
            padding: 8px 16px;
            background: rgba(99,102,241,0.08);
            border-left: 3px solid #6366f1;
            border-radius: 4px;
        }
        .story-text p {
            margin-bottom: 1.4em;
        }
        .text-cursor { 
            display: inline-block; 
            width: 2px; height: 1em; 
            background: #a78bfa; 
            vertical-align: text-bottom; 
            animation: blink .6s step-end infinite;
        }
        @keyframes blink { 50%{opacity:0} }

        /* Notification Toast */
        .toast-wrap { position: fixed; bottom: 24px; right: 24px; z-index: 999; display: flex; flex-direction: column; gap: 8px; pointer-events: none; }
        .toast {
            background: #1e1e2e;
            border: 1px solid rgba(255,255,255,0.1);
            padding: 12px 18px;
            border-radius: 10px;
            font-size: 13px;
            color: #e2e8f0;
            box-shadow: 0 8px 24px rgba(0,0,0,0.3);
            opacity: 0;
            transform: translateY(10px);
            transition: all .3s;
            pointer-events: all;
            max-width: 320px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .toast.show { opacity: 1; transform: translateY(0); }
        .toast.success { border-color: rgba(16,185,129,0.3); }
        .toast.error { border-color: rgba(239,68,68,0.3); }

        /* Confirm overlay */
        .confirm-overlay {
            position: fixed; inset: 0;
            background: rgba(0,0,0,0.7);
            z-index: 200;
            display: none;
            align-items: center;
            justify-content: center;
        }
        .confirm-overlay.active { display: flex; }
        .confirm-box {
            background: #1e1e2e;
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 32px;
            max-width: 400px;
            width: 90%;
            text-align: center;
        }
        .confirm-icon { font-size: 48px; margin-bottom: 16px; }
        .confirm-title { font-size: 18px; font-weight: 700; color: #fff; margin-bottom: 8px; }
        .confirm-sub { font-size: 14px; color: #94a3b8; margin-bottom: 24px; line-height: 1.6; }
        .confirm-btns { display: flex; gap: 12px; }
        .confirm-btn-yes { 
            flex: 1; padding: 12px; border: none; border-radius: 8px; 
            background: #6366f1; color: #fff; font-family: inherit; font-weight: 700; font-size: 14px; cursor: pointer; 
        }
        .confirm-btn-no { 
            flex: 1; padding: 12px; border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; 
            background: transparent; color: #94a3b8; font-family: inherit; font-weight: 600; font-size: 14px; cursor: pointer; 
        }

        /* Mobile responsive */
        @media (max-width: 768px) {
            .studio-layout { grid-template-columns: 1fr !important; height: auto !important; overflow: auto; }
            .studio-layout > aside { grid-column: 1; grid-row: 1; }
            .studio-layout > main  { grid-column: 1; grid-row: 2; min-height: 80vh; }
            .studio-sidebar { max-height: none; padding: 16px; }
            .editor-content-area { padding: 16px; }
            .studio-nav { padding: 0 12px; }
            .studio-user-chip { display: none; }
            .studio-home-link { font-size: 11px; white-space: nowrap; text-align: center; line-height: 1.2; }
            .studio-nav-right { gap: 8px; }
        }
    </style>
</head>
<body>

    <!-- NAV -->
    <nav class="studio-nav">
        <a href="<?php echo home_url(); ?>" class="studio-logo">
            ✨ Story Studio
            <span class="studio-logo-badge">AI</span>
        </a>
        <div class="studio-nav-right">
            <button onclick="document.getElementById('ss-usage-overlay').style.display='flex'; templyLoadGeminiUsage();" style="background:rgba(99,102,241,0.15); border:1px solid rgba(99,102,241,0.5); padding:6px 14px; border-radius:20px; font-size:13px; color:#a5b4fc; cursor:pointer; font-weight:bold; display:flex; gap:6px; align-items:center; transition:all 0.2s;" onmouseover="this.style.background='rgba(99,102,241,0.3)'" onmouseout="this.style.background='rgba(99,102,241,0.15)'">
                📊 API Quota
            </button>
            <span class="studio-user-chip">👤 <?php echo esc_html($current_user->display_name); ?></span>
            <a href="<?php echo home_url(); ?>" class="studio-home-link">← Về trang chủ</a>
        </div>
    </nav>

    <!-- MAIN LAYOUT -->
    <div class="studio-layout">

        <!-- SIDEBAR CONTROL PANEL -->
        <aside class="studio-sidebar">

            <!-- Mode tabs -->
            <div style="display:flex;gap:6px;margin-bottom:14px;">
                <button id="tab-create" onclick="switchTab('create')" style="flex:1;padding:9px;border-radius:8px;border:none;background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;">✨ Sáng Tác</button>
                <button id="tab-scrape" onclick="switchTab('scrape')" style="flex:1;padding:9px;border-radius:8px;border:1px solid rgba(251,191,36,0.4);background:rgba(251,191,36,0.07);color:#fbbf24;font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;">🕷️ Cào Truyện</button>
            </div>

            <!-- PANEL: Sáng Tác (default) -->
            <div id="panel-create">
            <div>
                <p class="panel-title">⚙️ Cấu hình Truyện</p>

                <div class="ctrl-group" style="margin-bottom: 12px;">
                    <label class="ctrl-label" style="display:flex; justify-content:space-between; align-items:center;">
                        <span>Engine AI Sáng Tác</span>
                        <button onclick="document.getElementById('ss-usage-overlay').style.display='flex'; templyLoadGeminiUsage();" style="background:rgba(99,102,241,0.15); border:1px solid rgba(99,102,241,0.5); padding:3px 8px; border-radius:12px; font-size:11px; color:#a5b4fc; cursor:pointer; font-weight:bold; display:flex; gap:4px; align-items:center; transition:all 0.2s;" onmouseover="this.style.background='rgba(99,102,241,0.3)'" onmouseout="this.style.background='rgba(99,102,241,0.15)'" type="button">
                            📊 Xem Quota
                        </button>
                    </label>
                    <select class="ctrl-select" id="ss-ai-model">
                        <option value="gemini-2.5-flash">Google Gemini Flash (Miễn phí - Nên dùng)</option>
                        <option value="gemini-2.0-flash">Google Gemini 2.0 Flash (Dự phòng)</option>
                        <option value="gemini-1.5-pro">Google Gemini Pro (Trả phí - Chất lượng cao)</option>
                    </select>
                </div>

                <div class="ctrl-group" style="margin-bottom: 12px;">
                    <label class="ctrl-label">Tiêu đề / Tên Truyện</label>
                    <input type="text" class="ctrl-input" id="ss-title" placeholder="Ví dụ: Chiếc Nhẫn Quyền Năng...">
                    <div id="title-suggestions" style="margin-top:8px; display:flex; gap:6px; flex-wrap:wrap;"></div>
                </div>

                <div class="ctrl-group" style="margin-bottom: 12px;">
                    <div style="display:flex; justify-content:space-between; align-items:flex-end;">
                        <label class="ctrl-label">Ý tưởng cốt truyện (Prompt)</label>
                        <button onclick="renderAutoPilotModal()" style="padding:4px 10px; border-radius:6px; border:1px solid rgba(79,70,229,0.4); background:rgba(79,70,229,0.15); color:#818cf8; font-weight:700; font-size:11px; cursor:pointer;" title="Mở bảng theo dõi hàng đợi Auto-Pilot">🚀 Trạm Auto-Pilot</button>
                    </div>
                    <textarea class="ctrl-textarea" id="ss-prompt" placeholder="Mô tả ngắn gọn: Nhân vật, bối cảnh, xung đột chính..."></textarea>
                    <div style="display:flex; gap:8px; margin-top:8px;">
                        <div style="flex:1; display:flex; align-items:center;">
                            <input type="number" id="ss-brainstorm-count" value="10" min="3" max="30" style="width:40px; padding:8px 4px; border-radius:8px 0 0 8px; border:1px solid rgba(16,185,129,0.4); border-right:none; background:rgba(16,185,129,0.03); color:#10b981; font-weight:700; text-align:center; font-size:12px; outline:none;" title="Số lượng Idea">
                            <button id="ss-btn-brainstorm" style="flex:1;padding:8px;border-radius:0 8px 8px 0;border:1px solid rgba(16,185,129,0.4);background:rgba(16,185,129,0.07);color:#10b981;font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:6px;transition:all .2s;" onmouseover="this.style.background='rgba(16,185,129,0.14)'" onmouseout="this.style.background='rgba(16,185,129,0.07)'">
                                <span id="ss-brainstorm-icon">💡</span> Gợi ý Kịch Bản
                            </button>
                        </div>
                        <button id="ss-btn-autodetect" style="flex:1;padding:8px;border-radius:8px;border:1px solid rgba(251,191,36,0.4);background:rgba(251,191,36,0.07);color:#fbbf24;font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:6px;transition:all .2s;" onmouseover="this.style.background='rgba(251,191,36,0.14)'" onmouseout="this.style.background='rgba(251,191,36,0.07)'">
                            <span id="ss-autodetect-icon">🤖</span> Gợi ý Tiêu đề
                        </button>
                    </div>
                </div>

                <div class="ctrl-group" style="margin-bottom: 12px;">
                    <label class="ctrl-label">Thể loại <span style="font-size:10px;color:#6b7a99;font-weight:400;">(Chọn 1 hoặc nhiều)</span></label>
                    <div class="genre-tags" id="ss-genres">
                        <span class="genre-tag" data-genre="Ngôn Tình">Ngôn Tình</span>
                        <span class="genre-tag" data-genre="Tiên Hiệp">Tiên Hiệp</span>
                        <span class="genre-tag" data-genre="Hài Hước">Hài Hước</span>
                        <span class="genre-tag" data-genre="Trinh Thám">Trinh Thám</span>
                        <span class="genre-tag" data-genre="Kiếm Hiệp">Kiếm Hiệp</span>
                        <span class="genre-tag" data-genre="Huyền Huyễn">Huyền Huyễn</span>
                        <span class="genre-tag" data-genre="Trọng Sinh">Trọng Sinh</span>
                        <span class="genre-tag" data-genre="Đô Thị">Đô Thị</span>
                        <span class="genre-tag" data-genre="Dị Giới">Dị Giới</span>
                        <span class="genre-tag" data-genre="Võ Hiệp">Võ Hiệp</span>
                        <span class="genre-tag" data-genre="Xuyên Không">Xuyên Không</span>
                        <span class="genre-tag" data-genre="Gia Đấu">Gia Đấu</span>
                        <span class="genre-tag" data-genre="Học Đường">Học Đường</span>
                        <span class="genre-tag" data-genre="Cung Đấu">Cung Đấu</span>
                        <span class="genre-tag" data-genre="Mạt Thế">Mạt Thế</span>
                        <span class="genre-tag" data-genre="Zombie">Zombie</span>
                        <span class="genre-tag" data-genre="Quân Sự">Quân Sự</span>
                        <span class="genre-tag" data-genre="Khoa Huyễn">Khoa Huyễn</span>
                        <span class="genre-tag" data-genre="Kinh Dị">Kinh Dị</span>
                        <span class="genre-tag" data-genre="Game">Game</span>
                        <span class="genre-tag" data-genre="Điền Văn">Điền Văn</span>
                        <span class="genre-tag" data-genre="Đam Mỹ">Đam Mỹ</span>
                        <span class="genre-tag" data-genre="Nữ Cường">Nữ Cường</span>
                        <span class="genre-tag" data-genre="Lịch Sử">Lịch Sử</span>
                        <span class="genre-tag" data-genre="Thể Thao">Thể Thao</span>
                        <span class="genre-tag" data-genre="Vả Mặt">Vả Mặt</span>
                        <span class="genre-tag" data-genre="Hệ Thống">Hệ Thống</span>
                        <span class="genre-tag" data-genre="Không Gian">Không Gian</span>
                    </div>
                </div>

                <div class="ctrl-group" style="margin-bottom: 12px;">
                    <label class="ctrl-label">Giọng văn</label>
                    <select class="ctrl-select" id="ss-tone">
                        <option value="lãng mạn, cảm xúc sâu lắng">💕 Lãng mạn & xúc cảm</option>
                        <option value="hài hước, dí dỏm, tươi sáng">😄 Vui tươi & hài hước</option>
                        <option value="hùng tráng, mạnh mẽ, chí khí">⚔️ Hùng tráng & mạnh mẽ</option>
                        <option value="bí ẩn, hồi hộp, căng thẳng">🔍 Bí ẩn & hồi hộp</option>
                        <option value="nhẹ nhàng, trữ tình, thơ mộng">🌸 Nhẹ nhàng & trữ tình</option>
                        <option value="cuồng nhiệt, mãnh liệt, đam mê">🔥 Cuồng nhiệt & đam mê</option>
                        <option value="kinh dị, rùng rợn">👻 Kinh dị & rùng rợn</option>
                        <option value="triết lý, suy tư, sâu sắc">🧠 Triết lý & sâu sắc</option>
                    </select>
                </div>

                <div class="ctrl-group" style="margin-bottom: 16px;">
                    <label class="ctrl-label">Số chương muốn tạo (mỗi chương ~2000 từ)</label>
                    <input type="number" class="ctrl-input" id="ss-chapters" value="10" min="1" max="100" oninput="updateChapterNote(this.value)">
                    <div id="chapter-count-note" style="font-size:11px;color:#6b7a99;margin-top:6px;">⚡ AI sẽ tạo từng batch 3 chương — tự động ghép lại</div>
                </div>
                <script>
                function updateChapterNote(v) {
                    const note = document.getElementById('chapter-count-note');
                    const batches = Math.ceil(parseInt(v) / 3);
                    if (parseInt(v) > 3) {
                        note.innerHTML = `⚡ Sẽ gọi AI <strong>${batches} lần</strong> (mỗi lần 3 chương) — thời gian khoảng <strong>${batches * 30}-${batches * 60}s</strong>`;
                        note.style.color = '#f59e0b';
                    } else {
                        note.innerHTML = '⚡ AI sẽ tạo 1 lần — nhanh (~20-30s)';
                        note.style.color = '#6b7a99';
                    }
                }
                updateChapterNote(document.getElementById('ss-chapters').value);
                </script>
            </div>

            <!-- Progress indicator -->
            <div class="progress-wrap" id="ss-progress">
                <div class="progress-label" id="ss-progress-label">Đang kết nối AI...</div>
                <div class="progress-bar-bg"><div class="progress-bar-fill" id="ss-progress-fill"></div></div>
            </div>

            <!-- Stats -->
            <div class="stats-row" id="ss-stats" style="display: none;">
                <div class="stat-chip">
                    <div class="val" id="stat-words">0</div>
                    <div class="lbl">Từ</div>
                </div>
                <div class="stat-chip">
                    <div class="val" id="stat-chapters">0</div>
                    <div class="lbl">Chương</div>
                </div>
            </div>

            <!-- AI Review Button -->
            <button id="ss-btn-review" style="display:none; width:100%; margin-top:10px; padding:10px 14px; border-radius:10px; border:1px solid rgba(251,191,36,0.4); background:rgba(251,191,36,0.08); color:#fbbf24; font-family:inherit; font-size:13px; font-weight:700; cursor:pointer; transition:all 0.2s;" onmouseover="this.style.background='rgba(251,191,36,0.18)'" onmouseout="this.style.background='rgba(251,191,36,0.08)'">
                🔍 AI Nhận xét & Góp ý truyện
            </button>

            <!-- Main CTA -->
            <button class="btn-generate" id="ss-btn-generate">
                <span id="ss-btn-icon">✨</span>
                <span id="ss-btn-text">Bắt đầu Sáng Tác</span>
            </button>

            <!-- Two-mode action area -->
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:4px;">
                <button class="btn-split" id="ss-btn-split" disabled style="font-size:12px;">
                    ✂️ Tách & Đăng ngay
                </button>
                <button id="ss-btn-autopilot" disabled style="padding:12px;border-radius:10px;border:1px solid rgba(16,185,129,0.5);background:rgba(16,185,129,0.08);color:#10b981;font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;transition:all .2s;" onmouseover="this.disabled||this.style.setProperty('background','rgba(16,185,129,0.2)')" onmouseout="this.style.setProperty('background','rgba(16,185,129,0.08)')">
                    🤖 Lên lịch Auto-Pilot
                </button>
            </div>

            <button class="btn-new" id="ss-btn-new" style="display:none;">
                ↺ Tạo truyện mới
            </button>

            <!-- Chapters created list -->
            <div id="ss-chapters-created" style="display: none;">
                <p class="panel-title" style="margin-bottom: 8px;">✅ Đã tạo thành công</p>
                <div class="chapters-list" id="ss-chapters-list"></div>
            </div>

            <!-- SCHEDULING UI -->
            <div id="ss-schedule-panel" style="display:none; margin-top:16px; padding:14px; background:rgba(99,102,241,0.07); border:1px solid rgba(99,102,241,0.25); border-radius:12px;">
                <p class="ctrl-label" style="margin-bottom:10px;">📅 Lên lịch đăng bài</p>
                <input type="datetime-local" id="ss-publish-date" class="ctrl-input" style="margin-bottom:10px;">
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
                    <button id="ss-btn-publish-now" style="padding:9px 12px;border-radius:8px;border:none;background:linear-gradient(135deg,#10b981,#059669);color:#fff;font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;">🚀 Đăng ngay</button>
                    <button id="ss-btn-schedule" style="padding:9px 12px;border-radius:8px;border:none;background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;">📅 Lên lịch</button>
                </div>
            </div>

            </div> <!-- /panel-create -->

            <!-- PANEL: Cào & Viết Lại (hidden by default) -->
            <div id="panel-scrape" style="display:none;">
                <p class="panel-title">🕷️ Cào &amp; Viết Lại</p>

                <!-- Bookmarklet install shortcut -->
                <div style="text-align:center;margin-bottom:12px;">
                    <button onclick="var g=document.getElementById('bookmarklet-guide');g.style.display='flex';" style="padding:8px 16px;border-radius:8px;border:1px solid rgba(99,102,241,0.4);background:rgba(99,102,241,0.08);color:#a5b4fc;font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;">🔖 Cài Bookmarklet 1-click</button>
                    <p style="font-size:10px;color:#6b7280;margin-top:4px;">Cào được meokammap, Cloudflare sites...</p>
                </div>

                <!-- URL or Paste -->
                <div class="ctrl-group">
                    <label class="ctrl-label">🔗 URL trang truyện</label>
                    <div style="font-size:10px;color:#10b981;margin-bottom:5px;">✅ Server-side: <strong>tehitruyen.com, truyenfull.vn</strong> | 🔖 Bookmarklet: meokammap + site Cloudflare</div>
                    <div style="display:flex;gap:6px;margin-bottom:6px;">
                        <input type="url" id="scrape-url" class="ctrl-input" placeholder="https://tehitruyen.com/truyen.html?chuong=1" style="flex:1;font-size:12px;">
                        <select id="scrape-chapter-count" style="padding:8px;border-radius:8px;border:1px solid rgba(255,255,255,0.1);background:#1e293b;color:#e2e8f0;font-size:12px;width:60px;">
                            <option value="1">1ch</option>
                            <option value="3">3ch</option>
                            <option value="5">5ch</option>
                            <option value="10">10ch</option>
                        </select>
                        <button id="btn-fetch-url" style="padding:8px 12px;border-radius:8px;border:none;background:#374151;color:#e2e8f0;font-size:12px;cursor:pointer;white-space:nowrap;">🕷️ Cào</button>
                    </div>
                    <label class="ctrl-label">📋 Hoặc dán nội dung truyện gốc vào đây</label>
                    <textarea id="scrape-content" class="ctrl-input" rows="6" style="resize:vertical;font-size:12px;line-height:1.5;" placeholder="Dán nội dung chương/truyện bất kỳ vào đây..."></textarea>
                    <div id="scrape-word-count" style="font-size:11px;color:#6b7280;text-align:right;margin-top:3px;">0 từ</div>
                </div>

                <!-- Mode Selector -->
                <div class="ctrl-group">
                    <label class="ctrl-label">🎯 Chế độ AI</label>
                    <select id="scrape-mode" class="ctrl-select" onchange="toggleScrapeMode(this.value)">
                        <option value="insight">📊 Phân tích xu hướng (Trend Insight)</option>
                        <option value="custom">🎨 Custom Prompt (Tự viết lệnh)</option>
                        <option value="transform">🔄 Đổi nhân vật &amp; bối cảnh hoàn toàn</option>
                        <option value="rewrite">✍️ Viết lại giữ cốt (Rủi ro bản quyền cao)</option>
                    </select>
                </div>

                <!-- Insight mode info -->
                <div id="scrape-insight-info" class="ctrl-group" style="background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.2);border-radius:8px;padding:10px;font-size:12px;color:#6ee7b7;">
                    📊 <strong>Trend Insight:</strong> AI sẽ phân tích danh sách truyện/nội dung và trả về: Motif đang hot, Thể loại nổi bật, Gợi ý ý tưởng độc quyền của riêng anh.
                </div>

                <!-- Custom prompt (hidden by default) -->
                <div id="scrape-custom-prompt-wrap" class="ctrl-group" style="display:none;">
                    <label class="ctrl-label">✏️ Prompt tùy chỉnh của anh</label>
                    <textarea id="scrape-custom-prompt" class="ctrl-input" rows="5" style="resize:vertical;font-size:12px;line-height:1.6;" placeholder='Ví dụ: "Dựa trên tình tiết này, viết một kịch bản hoàn toàn mới với bối cảnh Việt Nam hiện đại. Nhân vật chính là Lão Cửu - lão già ẩn danh công nghệ. Đổi toàn bộ tên người, địa danh, cách xử lý tình huống."'></textarea>
                    <div style="font-size:11px;color:#10b981;margin-top:4px;">💡 Càng chi tiết → AI càng ra đúng ý anh!</div>
                </div>

                <!-- Common options (hidden for insight mode) -->
                <div id="scrape-write-options" style="display:none;">
                    <div class="ctrl-group">
                        <label class="ctrl-label">🎙️ Giọng văn</label>
                        <select id="scrape-tone" class="ctrl-select">
                            <option value="hài hước, nhẹ nhàng">😄 Hài hước, nhẹ nhàng</option>
                            <option value="lãng mạn, cảm xúc">💕 Lãng mạn, cảm xúc</option>
                            <option value="hùng tráng, mạnh mẽ">⚔️ Hùng tráng, mạnh mẽ</option>
                            <option value="huyền bí, triết lý">🌙 Huyền bí, triết lý</option>
                            <option value="hiện đại, trẻ trung">🌟 Hiện đại, trẻ trung</option>
                        </select>
                    </div>
                    <div class="ctrl-group">
                        <label class="ctrl-label">📖 Tên bài viết WordPress</label>
                        <input type="text" id="scrape-wp-title" class="ctrl-input" placeholder="Tên truyện trên website...">
                    </div>
                    <div class="ctrl-group">
                        <label class="ctrl-label">✍️ Tên truyện mới (để trống = AI tự đặt)</label>
                        <input type="text" id="scrape-new-title" class="ctrl-input" placeholder="Để trống = AI tự đặt tên">
                    </div>
                </div>

                <!-- Copyright warning -->
                <div id="scrape-copyright-warn" style="display:none;background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.25);border-radius:8px;padding:10px;margin-bottom:10px;font-size:11px;color:#fca5a5;">
                    ⚠️ <strong>Lưu ý bản quyền:</strong> Chế độ "Viết lại giữ nguyên cốt" có rủi ro cao về trùng lặp nội dung và bản quyền. Google có thể phạt duplicate content. Anh nên dùng làm cảm hứng và tự chỉnh sửa tay trước khi đăng.
                </div>

                <!-- Action buttons -->
                <button id="btn-analyze-trend" style="width:100%;padding:12px;border-radius:10px;border:none;background:linear-gradient(135deg,#10b981,#059669);color:#fff;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;margin-bottom:6px;">
                    📊 Phân tích xu hướng
                </button>
                <button id="btn-rewrite" style="width:100%;padding:12px;border-radius:10px;border:none;background:linear-gradient(135deg,#f59e0b,#d97706);color:#fff;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;margin-bottom:8px;display:none;">
                    🔮 Lấy Cốt - Thay Hồn
                </button>
                <div id="scrape-status" style="font-size:12px;color:#6b7280;text-align:center;min-height:18px;"></div>
            </div>
            <!-- /panel-scrape -->

            <!-- panel-factory removed: merged into panel-create -->

        </aside>

        <!-- EDITOR PANEL -->
        <main class="studio-editor">
            <div class="editor-toolbar">
                <div class="editor-status">
                    <div class="status-dot" id="ss-status-dot"></div>
                    <span id="ss-status-text">Chờ lệnh</span>
                </div>
                <div class="editor-word-count" id="ss-word-count">0 từ</div>
            </div>

            <div class="editor-content-area" id="ss-content-area">

                <!-- Empty state -->
                <div class="editor-empty" id="ss-empty-state">
                    <div class="editor-empty-icon">📖</div>
                    <div class="editor-empty-title">Xưởng Sáng Tác AI</div>
                    <div class="editor-empty-sub">Nhập ý tưởng câu chuyện của bạn vào bảng điều khiển bên trái, sau đó bấm "Bắt đầu Sáng Tác" để AI viết ra một bộ truyện hoàn chỉnh. Bạn sẽ đọc duyệt và bấm một nút để tách thành các chương!</div>
                </div>

                <!-- Story output area -->
                <div class="story-output" id="ss-story-output">
                    <h1 class="story-post-title" id="ss-story-title-display"></h1>
                    <div class="story-text" id="ss-story-text" contenteditable="true" spellcheck="false" style="outline:none; border-radius:8px; transition:background 0.2s;" onfocus="this.style.background='rgba(255,255,255,0.02)'" onblur="this.style.background='transparent'"></div>
                </div>

                <!-- Agentic Terminal Area -->
                <div id="ss-agentic-terminal" style="display:none; flex-direction:column; background:#000; border:1px solid rgba(16,185,129,0.3); border-radius:12px; height:100%; min-height:400px; overflow-y:auto; padding:20px; font-family:'Courier New', Courier, monospace; font-size:13px; line-height:1.6;">
                    <div style="color:#10b981; font-weight:bold; margin-bottom:12px;">> SYSTEM READY. WAITING FOR AGENTIC COMMAND...</div>
                </div>

            </div>
        </main>

    </div>

    <!-- Floating AI Toolbar -->
    <div id="ai-floating-toolbar" style="display:none; position:absolute; z-index:9999; background:#1e1b4b; border:1px solid rgba(99,102,241,0.5); border-radius:8px; padding:6px; box-shadow:0 10px 25px rgba(0,0,0,0.5); gap:6px; align-items:center;">
        <button class="ai-tool-btn" data-action="improve" title="✨ Hay hơn" style="padding:6px 10px; border-radius:6px; border:none; background:rgba(99,102,241,0.2); color:#a5b4fc; cursor:pointer; font-size:12px; font-weight:600; white-space:nowrap;">✨ Hay hơn</button>
        <button class="ai-tool-btn" data-action="expand" title="📝 Dài hơn" style="padding:6px 10px; border-radius:6px; border:none; background:rgba(99,102,241,0.2); color:#a5b4fc; cursor:pointer; font-size:12px; font-weight:600; white-space:nowrap;">📝 Dài hơn</button>
        <button class="ai-tool-btn" data-action="fix" title="✅ Sửa lỗi" style="padding:6px 10px; border-radius:6px; border:none; background:rgba(99,102,241,0.2); color:#a5b4fc; cursor:pointer; font-size:12px; font-weight:600; white-space:nowrap;">✅ Sửa lỗi</button>
        <button class="ai-tool-btn" data-action="custom" title="💬 Tự nhập" style="padding:6px 10px; border-radius:6px; border:none; background:rgba(99,102,241,0.2); color:#a5b4fc; cursor:pointer; font-size:12px; font-weight:600; white-space:nowrap;">💬 Tự nhập</button>
    </div>

    <!-- Confirm dialog -->
    <div class="confirm-overlay" id="ss-confirm">
        <div class="confirm-box">
            <div class="confirm-icon">✂️</div>
            <div class="confirm-title">Tách thành các Chương?</div>
            <div class="confirm-sub">Hệ thống sẽ đọc các tiêu đề "Chương 1, Chương 2..." trong văn bản và tự động tạo bài viết con tương ứng. Văn bản gốc của truyện sẽ được giữ nguyên an toàn.</div>
            <div class="confirm-btns">
                <button class="confirm-btn-yes" id="ss-confirm-yes">✅ Tách ngay!</button>
                <button class="confirm-btn-no" id="ss-confirm-no">Kiểm tra thêm</button>
            </div>
        </div>
    </div>

    <!-- AI Review Modal -->
    <div id="ss-review-overlay" style="display:none; position:fixed; inset:0; background:rgba(0,0,0,0.75); z-index:10000; align-items:center; justify-content:center;">
        <div style="background:#13131f; border:1px solid rgba(251,191,36,0.3); border-radius:16px; max-width:680px; width:95%; max-height:85vh; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 25px 60px rgba(0,0,0,0.6);">
            <div style="padding:20px 24px; border-bottom:1px solid rgba(255,255,255,0.07); display:flex; align-items:center; justify-content:space-between; background:rgba(251,191,36,0.06);">
                <div>
                    <div style="font-size:16px; font-weight:800; color:#fbbf24;">🔍 AI Nhận xét & Góp ý</div>
                    <div style="font-size:12px; color:#6b7280; margin-top:2px;">Phân tích chuyên sâu từ Gemini AI</div>
                </div>
                <button onclick="document.getElementById('ss-review-overlay').style.display='none'" style="background:none; border:none; color:#6b7280; font-size:20px; cursor:pointer; padding:4px 8px; border-radius:6px;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#6b7280'">✕</button>
            </div>
            <div id="ss-review-content" style="padding:24px; overflow-y:auto; flex:1; line-height:1.8; font-size:14px; color:#d1d5db;">
                <div style="text-align:center; padding:40px; color:#6b7280;">⏳ AI đang phân tích truyện...</div>
            </div>
        </div>
    </div>

    <!-- Usage Monitor Modal -->
    <div id="ss-usage-overlay" style="display:none; position:fixed; inset:0; background:rgba(0,0,0,0.85); z-index:10000; align-items:center; justify-content:center; backdrop-filter:blur(4px);">
        <div style="background:#0f0f17; border:1px solid rgba(99,102,241,0.3); border-radius:16px; max-width:900px; width:95%; max-height:90vh; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 25px 60px rgba(0,0,0,0.7);">
            
            <div style="background:linear-gradient(90deg, #3730a3, #4338ca); padding:16px 24px; border-bottom:1px solid rgba(255,255,255,0.07); display:flex; align-items:center; justify-content:space-between;">
                <div style="display:flex; align-items:center; gap:12px;">
                    <div style="width:36px; height:36px; background:rgba(255,255,255,0.15); border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:20px;">🌌</div>
                    <div>
                        <div style="font-size:16px; font-weight:800; color:#fff;">Gemini Free Tier Monitor</div>
                        <div style="font-size:12px; color:#c7d2fe; margin-top:2px;">Theo dõi hạn mức tự động fallback (Flash → Pro)</div>
                    </div>
                </div>
                <div style="display:flex; align-items:center; gap:10px;">
                    <button id="gemini-refresh-btn" onclick="templyLoadGeminiUsage()" style="background:rgba(255,255,255,0.2); border:none; color:#fff; font-size:13px; font-weight:600; cursor:pointer; padding:8px 16px; border-radius:8px; display:flex; gap:6px; align-items:center; transition:background 0.2s;" onmouseover="this.style.background='rgba(255,255,255,0.3)'" onmouseout="this.style.background='rgba(255,255,255,0.2)'">
                        <svg class="w-4 h-4" style="width:16px;height:16px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
                        Làm mới
                    </button>
                    <button onclick="document.getElementById('ss-usage-overlay').style.display='none'" style="background:none; border:none; color:#c7d2fe; font-size:24px; cursor:pointer; padding:0 8px; line-height:1;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#c7d2fe'">✕</button>
                </div>
            </div>

            <!-- Alert Banner -->
            <div id="gemini-alert-banner" style="display:none; padding:12px 24px; background:rgba(239,68,68,0.1); border-bottom:1px solid rgba(239,68,68,0.2); align-items:center; gap:10px;">
                <svg style="width:20px;height:20px;color:#ef4444;" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path></svg>
                <span id="gemini-alert-text" style="font-size:13px; font-weight:700; color:#ef4444;"></span>
            </div>

            <div style="padding:24px; overflow-y:auto; flex:1; display:flex; flex-direction:column; gap:24px;">
                <!-- Today Cards -->
                <div id="gemini-today-cards" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(250px, 1fr)); gap:16px;">
                    <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.05); border-radius:12px; height:120px; display:flex; align-items:center; justify-content:center; color:#6b7280;">Đang tải...</div>
                </div>

                <!-- History Table -->
                <div>
                    <h3 style="font-size:14px; font-weight:800; color:#94a3b8; margin-bottom:12px; display:flex; align-items:center; gap:8px;">
                        <svg style="width:16px;height:16px;color:#8b5cf6;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                        Lịch Sử 7 Ngày Gần Nhất
                    </h3>
                    <div style="overflow-x:auto; border-radius:12px; border:1px solid rgba(255,255,255,0.06); background:rgba(0,0,0,0.2);">
                        <table style="width:100%; border-collapse:collapse; text-align:left; font-size:13px; color:#cce2ff;">
                            <thead style="background:rgba(255,255,255,0.03); border-bottom:1px solid rgba(255,255,255,0.06);">
                                <tr>
                                    <th style="padding:12px 16px; font-weight:700; color:#94a3b8; text-transform:uppercase; font-size:11px;">Ngày</th>
                                    <th style="padding:12px 16px; font-weight:800; color:#60a5fa; text-align:center;">FLASH 2.5</th>
                                    <th style="padding:12px 16px; font-weight:800; color:#818cf8; text-align:center;">FLASH 2.0</th>
                                    <th style="padding:12px 16px; font-weight:800; color:#c084fc; text-align:center;">PRO 1.5</th>
                                    <th style="padding:12px 16px; font-weight:800; color:#94a3b8; text-align:center;">Tổng</th>
                                </tr>
                            </thead>
                            <tbody id="gemini-history-body">
                                <tr><td colspan="5" style="text-align:center; padding:30px; color:#4b5563;">Đang tải dữ liệu...</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Explanation -->
                <div style="background:rgba(99,102,241,0.04); border:1px solid rgba(99,102,241,0.15); border-radius:12px; padding:16px;">
                    <p style="font-size:12px; font-weight:800; color:#818cf8; margin-bottom:8px;">🔄 Tự Động Fallback</p>
                    <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap; font-size:12px; color:#94a3b8;">
                        <span style="background:rgba(59,130,246,0.15); color:#60a5fa; padding:4px 10px; border-radius:20px; font-weight:600; border:1px solid rgba(59,130,246,0.3);">Flash 2.5 (500)</span>
                        <span>→ hết quota →</span>
                        <span style="background:rgba(99,102,241,0.15); color:#818cf8; padding:4px 10px; border-radius:20px; font-weight:600; border:1px solid rgba(99,102,241,0.3);">Flash 2.0 (1500)</span>
                        <span>→ hết quota →</span>
                        <span style="background:rgba(168,85,247,0.15); color:#c084fc; padding:4px 10px; border-radius:20px; font-weight:600; border:1px solid rgba(168,85,247,0.3);">Pro 1.5 (50)</span>
                    </div>
                    <p style="font-size:11px; color:#6b7280; margin-top:8px;">Quota làm mới lúc 00:00 UTC (07:00 SA giờ Việt Nam).</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Toast container -->
    <div class="toast-wrap" id="ss-toasts"></div>


    <script>
    const GEMINI_MODELS = {
        'gemini-2.5-flash': { label: 'Flash 2.5', color: 'blue',   limit: 500  },
        'gemini-2.0-flash':               { label: 'Flash 2.0', color: 'indigo', limit: 1500 },
        'gemini-1.5-pro':                 { label: 'Pro 1.5',   color: 'purple', limit: 50   },
    };

    function templyLoadGeminiUsage() {
        const btn = document.getElementById('gemini-refresh-btn');
        btn.style.opacity = '0.5';

        fetch('<?php echo esc_url($ajax_url); ?>', {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            body: new URLSearchParams({
                action: 'temply_gemini_usage_stats',
                nonce: '<?php echo esc_js($nonce); ?>'
            })
        }).then(async res => {
            const text = await res.text();
            try {
                return JSON.parse(text);
            } catch(e) {
                throw new Error('Server returned invalid JSON: ' + text);
            }
        }).then(res => {
            btn.style.opacity = '1';
            const tbody = document.getElementById('gemini-history-body');
            const todayCards = document.getElementById('gemini-today-cards');
            if (res === -1 || res === "-1") {
                tbody.innerHTML = '<tr><td colspan="5" style="color:#ef4444;text-align:center;">Lỗi xác thực Nonce (-1). Hãy load lại trang.</td></tr>';
                todayCards.innerHTML = '';
                return;
            }
            if (!res.success) {
                tbody.innerHTML = `<tr><td colspan="5" style="color:#ef4444;text-align:center;">Lỗi backend: ${res.data?.message || JSON.stringify(res.data) || 'Không thể tải'}</td></tr>`;
                todayCards.innerHTML = '';
                return;
            }
            const { days, limits, today } = res.data;
            renderTodayCards(days[today] || { usage: {}, exhausted: [] }, today);
            renderHistoryTable(days, today);
            checkAlerts(days[today] || { exhausted: [] });
        }).catch((err) => {
            btn.style.opacity = '1';
            document.getElementById('gemini-history-body').innerHTML = `<tr><td colspan="5" style="color:#ef4444;text-align:center;">${err.message}</td></tr>`;
            document.getElementById('gemini-today-cards').innerHTML = '';
        });
    }

    function renderTodayCards(todayData, today) {
        const container = document.getElementById('gemini-today-cards');
        let html = '';
        Object.entries(GEMINI_MODELS).forEach(([modelId, meta]) => {
            const used      = todayData.usage[modelId] || 0;
            const limit     = meta.limit;
            const pct       = Math.min(100, Math.round(used / limit * 100));
            const remaining = Math.max(0, limit - used);
            const exhausted = todayData.exhausted.includes(modelId);
            
            let colorHex = meta.color === 'blue' ? '#3b82f6' : (meta.color === 'indigo' ? '#6366f1' : '#a855f7');
            let bgLight  = meta.color === 'blue' ? 'rgba(59,130,246,0.05)' : (meta.color === 'indigo' ? 'rgba(99,102,241,0.05)' : 'rgba(168,85,247,0.05)');
            let bdColor  = meta.color === 'blue' ? 'rgba(59,130,246,0.2)' : (meta.color === 'indigo' ? 'rgba(99,102,241,0.2)' : 'rgba(168,85,247,0.2)');

            const barColor = exhausted ? '#ef4444' : (pct >= 80 ? '#f59e0b' : colorHex);
            const statusBadge = exhausted
                ? `<span style="font-size:10px; background:rgba(239,68,68,0.2); color:#fca5a5; padding:2px 8px; border-radius:12px; font-weight:800; border:1px solid rgba(239,68,68,0.4);">❌ HẾT QUOTA</span>`
                : (pct >= 80
                    ? `<span style="font-size:10px; background:rgba(245,158,11,0.2); color:#fcd34d; padding:2px 8px; border-radius:12px; font-weight:800; border:1px solid rgba(245,158,11,0.4);">⚠ GẦN HẾT</span>`
                    : `<span style="font-size:10px; background:rgba(16,185,129,0.2); color:#6ee7b7; padding:2px 8px; border-radius:12px; font-weight:800; border:1px solid rgba(16,185,129,0.4);">✅ Sẵn sàng</span>`);

            html += `
            <div style="background:${bgLight}; border:1px solid ${bdColor}; border-radius:12px; padding:16px;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
                    <div>
                        <div style="font-size:13px; font-weight:800; color:${colorHex}; text-transform:uppercase; letter-spacing:1px;">${meta.label}</div>
                        <div style="font-size:11px; color:#6b7280; margin-top:2px;">${modelId.substring(0, 15)}...</div>
                    </div>
                    ${statusBadge}
                </div>
                <div style="margin-bottom:12px;">
                    <div style="display:flex; justify-content:space-between; font-size:12px; color:#94a3b8; margin-bottom:6px;">
                        <span>Đã dùng</span>
                        <span style="font-weight:800; color:${colorHex};">${used} / ${limit}</span>
                    </div>
                    <div style="height:6px; background:rgba(255,255,255,0.05); border-radius:10px; overflow:hidden;">
                        <div style="height:100%; background:${barColor}; width:${pct}%; transition:width 0.5s ease;"></div>
                    </div>
                </div>
                <div style="font-size:11px; ${exhausted ? 'color:#f87171; font-weight:700;' : 'color:#6b7280;'}">
                    ${exhausted ? '🚨 Đã chuyển sang model dự phòng' : `Còn lại <strong style="color:#d1d5db;">${remaining}</strong> requests`}
                </div>
            </div>`;
        });
        container.innerHTML = html;
    }

    function renderHistoryTable(days, today) {
        const tbody = document.getElementById('gemini-history-body');
        const models = Object.keys(GEMINI_MODELS);
        let rows = '';
        Object.entries(days).reverse().forEach(([date, data]) => {
            const isToday = date === today;
            const dayLabel = isToday ? `<strong style="color:#fff;">${date}</strong> <span style="font-size:10px; background:rgba(99,102,241,0.2); color:#a5b4fc; padding:2px 6px; border-radius:10px; margin-left:6px;">Hôm nay</span>` : date;
            let total = 0;
            const cells = models.map(m => {
                const used = data.usage[m] || 0;
                const exhausted = data.exhausted.includes(m);
                total += used;
                if (used === 0 && !exhausted) return `<td style="text-align:center; padding:12px 16px; color:#4b5563;">—</td>`;
                const meta = GEMINI_MODELS[m];
                const c = meta.color === 'blue' ? 'color:#60a5fa;' : (meta.color === 'indigo' ? 'color:#818cf8;' : 'color:#c084fc;');
                
                const badge = exhausted
                    ? `<span style="font-size:13px; font-weight:800; color:#ef4444;">${used} <span style="font-size:10px;">❌</span></span>`
                    : `<span style="font-size:13px; font-weight:800; ${c}">${used}</span>`;
                return `<td style="text-align:center; padding:12px 16px;">${badge}</td>`;
            }).join('');
            
            rows += `<tr style="${isToday ? 'background:rgba(255,255,255,0.05);' : 'border-bottom:1px solid rgba(255,255,255,0.02);'}">
                <td style="padding:12px 16px; color:#94a3b8;">${dayLabel}</td>
                ${cells}
                <td style="text-align:center; padding:12px 16px; font-weight:800; color:#cbd5e1;">${total > 0 ? total : '—'}</td>
            </tr>`;
        });
        tbody.innerHTML = rows || '<tr><td colspan="5" style="text-align:center; padding:30px; color:#4b5563;">Chưa có dữ liệu lịch sử</td></tr>';
    }

    function checkAlerts(todayData) {
        const banner = document.getElementById('gemini-alert-banner');
        const alertText = document.getElementById('gemini-alert-text');
        const exhausted = todayData.exhausted || [];
        const flash25 = 'gemini-2.5-flash';
        const pro15   = 'gemini-1.5-pro';

        if (exhausted.includes(pro15)) {
            banner.style.display = 'flex';
            alertText.innerHTML = '🚨 TẤT CẢ GEMINI ĐÃ HẾT QUOTA HÔM NAY! Toàn bộ yêu cầu sẽ thất bại cho đến khi reset lúc 07:00 SA.';
            banner.style.background = 'rgba(239, 68, 68, 0.15)';
            banner.style.borderColor = 'rgba(239, 68, 68, 0.3)';
            alertText.style.color = '#f87171';
        } else if (exhausted.includes(flash25)) {
            banner.style.display = 'flex';
            alertText.innerHTML = '⚠️ Flash 2.5 đã hết quota — hệ thống tự động đổi sang dùng model đắt hơn là Flash 2.0 / Pro 1.5.';
            banner.style.background = 'rgba(245, 158, 11, 0.15)';
            banner.style.borderColor = 'rgba(245, 158, 11, 0.3)';
            alertText.style.color = '#fbbf24';
        } else {
            banner.style.display = 'none';
        }
    }

    window.templyLoadGeminiUsage = templyLoadGeminiUsage;

    (function() {
        const AJAX_URL = '<?php echo esc_url($ajax_url); ?>';
        const NONCE = '<?php echo esc_js($nonce); ?>';

        // ---- Helper: Call Gemini directly from browser ----
        async function callGeminiFromBrowser(prompt, gemini_key, ai_model) {
            let model = ai_model || 'gemini-2.5-flash';
            let fallbackChain = [];
            if (model.includes('flash') && model !== 'gemini-2.0-flash') fallbackChain = ['gemini-2.5-flash', 'gemini-2.0-flash', 'gemini-1.5-pro'];
            else if (model === 'gemini-2.0-flash') fallbackChain = ['gemini-2.0-flash', 'gemini-1.5-pro'];
            else fallbackChain = [model];
            
            let lastError = null;
            for (let i = 0; i < fallbackChain.length; i++) {
                let currentModel = fallbackChain[i];
                const url = `https://generativelanguage.googleapis.com/v1beta/models/${currentModel}:generateContent?key=${gemini_key}`;
                const timeoutMs = currentModel.includes('flash') ? 180000 : 360000;
                const controller = new AbortController();
                const timer = setTimeout(() => controller.abort(), timeoutMs);
                
                try {
                    let resp = await fetch(url, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ contents: [{ parts: [{ text: prompt }] }] }),
                        signal: controller.signal
                    });
                    clearTimeout(timer);
                    const data = await resp.json();
                    
                    if (data.error) {
                        if (data.error.code === 429 && i < fallbackChain.length - 1) {
                            console.warn(`[Gemini Fallback] Quota exhausted for ${currentModel}. Switching to ${fallbackChain[i+1]}...`);
                            showToast(`⚠️ Hết giới hạn ${currentModel}, tự động chuyển sang ${fallbackChain[i+1]}!`, 'error');
                            const f1 = new FormData();
                            f1.append('action', 'temply_track_gemini_usage_browser');
                            f1.append('model', currentModel);
                            f1.append('status', 'exhausted');
                            fetch(AJAX_URL, { method: 'POST', body: f1 });
                            continue; // Try next model
                        }
                        throw new Error('❌ Gemini API: ' + data.error.message + ' (Mã: ' + data.error.code + ')');
                    }
                    const text = data?.candidates?.[0]?.content?.parts?.[0]?.text || '';
                    if (!text) throw new Error('Gemini trả về rỗng. Kiểm tra lại API Key và Quota.');
                    
                    // Log success usage to server asynchronously
                    const f2 = new FormData();
                    f2.append('action', 'temply_track_gemini_usage_browser');
                    f2.append('model', currentModel);
                    f2.append('status', 'success');
                    fetch(AJAX_URL, { method: 'POST', body: f2 });
                    
                    return text;
                } catch(netErr) {
                    clearTimeout(timer);
                    if (netErr.name === 'AbortError') {
                        lastError = new Error(`AI mất quá lâu để phản hồi (>${timeoutMs/1000} giây). Hãy giảm dung lượng văn bản.`);
                    } else {
                        lastError = new Error('Không thể kết nối Gemini từ trình duyệt: ' + netErr.message);
                    }
                    // Do NOT continue the loop on pure network/abort errors unless it's a 429 Quota exhausted
                    throw lastError;
                }
            }
            throw lastError;
        }

        let generatedHTML = '';
        let currentPostId = 0;
        let selectedGenres = [];
        let isGenerating = false;

        // ---- Tab switcher ----
        // ---- Toggle scrape mode UI ----
        window.toggleScrapeMode = function(mode) {
            const insightInfo   = document.getElementById('scrape-insight-info');
            const customWrap    = document.getElementById('scrape-custom-prompt-wrap');
            const writeOpts     = document.getElementById('scrape-write-options');
            const copyrightWarn = document.getElementById('scrape-copyright-warn');
            const btnAnalyze    = document.getElementById('btn-analyze-trend');
            const btnRewriteEl  = document.getElementById('btn-rewrite');

            // Reset
            insightInfo.style.display   = 'none';
            customWrap.style.display    = 'none';
            writeOpts.style.display     = 'none';
            copyrightWarn.style.display = 'none';
            btnAnalyze.style.display    = 'none';
            btnRewriteEl.style.display  = 'none';

            if (mode === 'insight') {
                insightInfo.style.display = 'block';
                btnAnalyze.style.display  = 'block';
            } else if (mode === 'custom') {
                customWrap.style.display   = 'block';
                writeOpts.style.display    = 'block';
                btnRewriteEl.style.display = 'block';
            } else if (mode === 'transform') {
                writeOpts.style.display    = 'block';
                btnRewriteEl.style.display = 'block';
            } else if (mode === 'rewrite') {
                writeOpts.style.display     = 'block';
                copyrightWarn.style.display = 'block';
                btnRewriteEl.style.display  = 'block';
            }
        };
        // Run on load (insight is default)
        toggleScrapeMode('insight');

        // ---- Trend Insight button ----
        const btnAnalyzeTrend = document.getElementById('btn-analyze-trend');
        if (btnAnalyzeTrend) {
            btnAnalyzeTrend.addEventListener('click', async () => {
                const content = scrapeContentEl?.value.trim() || '';
                if (content.length < 50) { alert('Hãy dán danh sách truyện hoặc nội dung cần phân tích!'); return; }

                btnAnalyzeTrend.textContent = '⏳ Đang phân tích...';
                btnAnalyzeTrend.disabled = true;
                document.getElementById('scrape-status').textContent = 'AI đang phân tích xu hướng thị trường...';

                try {
                    const keyFD = new FormData();
                    keyFD.append('action', 'temply_studio_autodetect_prompt');
                    keyFD.append('action_nonce', NONCE);
                    keyFD.append('prompt', content.slice(0, 500));
                    const keyRes = await fetch(AJAX_URL, { method: 'POST', body: keyFD }).then(r => r.json());
                    if (!keyRes.success) throw new Error('Không lấy được key AI');
                    const { gemini_key } = keyRes.data;

                    const trendPrompt = `Bạn là chuyên gia phân tích thị trường truyện online Việt Nam.
Hãy phân tích đoạn nội dung/danh sách truyện sau và trả về báo cáo insight ngắn gọn bằng tiếng Việt:

--- DỮ LIỆU ---
${content.slice(0, 10000)}

--- YÊU CẦU ---
1. Top 3-5 MOTIF/Tình tiết đang hot nhất (ví dụ: vả mặt, ẩn thân, hệ thống, chủ tịch, trọng sinh)
2. Thể loại nổi bật nhất
3. Giọng văn phổ biến nhất
4. 3-5 GỢI Ý ý tưởng truyện HOÀN TOÀN NGUYÊN GỐC cho tôi dựa trên xu hướng này (đặt tên cụ thể)
5. Cảnh báo: Nội dung nào đang bão hòa (tránh làm)

Trình bày dạng markdown có emoji cho dễ đọc.`;

                    const aiModel = document.getElementById('ss-ai-model')?.value || 'gemini-2.5-flash';
                    const insight = await callGeminiFromBrowser(trendPrompt, gemini_key, aiModel);

                    // Show insight in editor panel
                    document.getElementById('ss-story-title-display').textContent = '📊 Trend Insight Report';
                    document.getElementById('ss-story-text').innerHTML = '<div style="line-height:1.8;font-size:14px;">' + insight.replace(/\n/g,'<br>').replace(/\*\*(.*?)\*\*/g,'<strong>$1</strong>').replace(/^#+\s(.+)$/gm,'<h3>$1</h3>') + '</div>';
                    document.getElementById('ss-story-output').classList.add('visible');
                    document.getElementById('ss-empty-state').style.display = 'none';

                    document.getElementById('scrape-status').textContent = '✅ Phân tích xong! Xem kết quả bên phải.';
                    showToast('📊 Trend Insight đã sẵn sàng!', 'success');
                } catch(e) {
                    document.getElementById('scrape-status').textContent = '❌ Lỗi: ' + e.message;
                    showToast('❌ ' + e.message, 'error');
                } finally {
                    btnAnalyzeTrend.textContent = '📊 Phân tích xu hướng';
                    btnAnalyzeTrend.disabled = false;
                }
            });
        }

        window.switchTab = function(tab) {
            const activeStyle = (color1, color2) => `flex:1;padding:9px;border-radius:8px;border:none;background:linear-gradient(135deg,${color1},${color2});color:#fff;font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;`;
            const inactiveStyle = (r, g, b, hex) => `flex:1;padding:9px;border-radius:8px;border:1px solid rgba(${r},${g},${b},0.4);background:rgba(${r},${g},${b},0.07);color:${hex};font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;`;
            
            document.getElementById('panel-create').style.display = (tab === 'create') ? 'block' : 'none';
            document.getElementById('panel-scrape').style.display = (tab === 'scrape') ? 'block' : 'none';
            
            document.getElementById('tab-create').style.cssText = (tab === 'create') ? activeStyle('#6366f1', '#8b5cf6') : inactiveStyle(99, 102, 241, '#6366f1');
            document.getElementById('tab-scrape').style.cssText = (tab === 'scrape') ? activeStyle('#f59e0b', '#d97706') : inactiveStyle(251, 191, 36, '#fbbf24');

            // Hide terminal when switching away from create (terminal only shows when auto-pilot is running)
            if (tab !== 'create') {
                document.getElementById('ss-agentic-terminal').style.display = 'none';
                if (!generatedHTML) {
                    document.getElementById('ss-empty-state').style.display = 'flex';
                    document.getElementById('ss-story-output').classList.remove('visible');
                }
            }
            document.getElementById('ss-status-text').textContent = isGenerating ? 'Đang viết...' : 'Chờ lệnh';
        };

        // ---- Scrape word counter ----
        const scrapeContentEl = document.getElementById('scrape-content');
        if (scrapeContentEl) {
            scrapeContentEl.addEventListener('input', () => {
                const words = scrapeContentEl.value.trim().split(/\s+/).filter(w => w).length;
                document.getElementById('scrape-word-count').textContent = words.toLocaleString() + ' từ';
            });
        }

        // ---- Fetch URL from browser ----
        const btnFetchUrl = document.getElementById('btn-fetch-url');
        if (btnFetchUrl) {
            btnFetchUrl.addEventListener('click', async () => {
                const url = document.getElementById('scrape-url').value.trim();
                if (!url) { alert('Vui lòng nhập URL truyện!'); return; }
                btnFetchUrl.textContent = '⏳';
                btnFetchUrl.disabled = true;
                document.getElementById('scrape-status').textContent = 'Đang cào nội dung...';

                // Detect if site supports server-side scraping
                const serverSupportedSites = ['tehitruyen.com', 'truyenfull.vn', 'metruyenchu.com', 'truyencv.com', 'tangthuvien.vn'];
                let urlHostname = '';
                try { urlHostname = new URL(url).hostname.replace(/^www\./, ''); } catch(e) {}
                const useServer = serverSupportedSites.some(s => urlHostname.includes(s));

                try {
                    let text = '', pageTitle = '';

                    if (useServer) {
                        // ✅ Server-side scraping (no CORS issues, supports tehitruyen.com)
                        document.getElementById('scrape-status').textContent = `✅ ${urlHostname} hỗ trợ cào server! Đang lấy nội dung...`;
                        const multiCount = document.getElementById('scrape-chapter-count')?.value || 1;
                        const fd = new FormData();
                        fd.append('action', 'temply_studio_scrape_url');
                        fd.append('action_nonce', NONCE);
                        fd.append('url', url);
                        fd.append('chapters', multiCount);
                        const res = await fetch(AJAX_URL, { method: 'POST', body: fd }).then(r => r.json());
                        if (!res.success) throw new Error(res.data?.message || 'Lỗi cào server');
                        text = res.data.text;
                        pageTitle = res.data.title;
                        document.getElementById('scrape-status').textContent = `✅ Cào xong ${res.data.chapters} chương (${res.data.wordCount} từ) từ ${res.data.source}!`;
                    } else {
                        // Fallback: browser-side via proxy
                        document.getElementById('scrape-status').textContent = `⚠️ ${urlHostname} cần proxy (có thể bị Cloudflare block)...`;
                        const proxyUrl = `https://api.allorigins.win/raw?url=${encodeURIComponent(url)}`;
                        const resp = await fetch(proxyUrl, { signal: AbortSignal.timeout(15000) });
                        if (!resp.ok) throw new Error('Proxy trả về HTTP ' + resp.status + '. Site này cần dùng Bookmarklet!');
                        const html = await resp.text();
                        const parser = new DOMParser();
                        const doc = parser.parseFromString(html, 'text/html');
                        ['script','style','nav','footer','header','aside'].forEach(tag => doc.querySelectorAll(tag).forEach(el => el.remove()));
                        const selectors = ['#noi_dung_truyen', '#chapter-c', '.chapter-c', '#box_doc', '.content', 'article', 'main', 'body'];
                        for (const sel of selectors) {
                            const el = doc.querySelector(sel);
                            if (el && el.innerText && el.innerText.length > 500) { text = el.innerText.trim(); break; }
                        }
                        if (!text) text = doc.body.innerText.trim();
                        if (text.length < 200) throw new Error('Không trích xuất được nội dung. Hãy dùng Bookmarklet!');
                        pageTitle = doc.querySelector('h1, title')?.textContent?.trim() || '';
                        document.getElementById('scrape-status').textContent = '✅ Cào thành công qua proxy!';
                    }

                    scrapeContentEl.value = text.slice(0, 50000);
                    scrapeContentEl.dispatchEvent(new Event('input'));
                    if (pageTitle) {
                        document.getElementById('scrape-wp-title').value = pageTitle;
                    }
                } catch(e) {
                    document.getElementById('scrape-status').textContent = '❌ ' + e.message;
                } finally {
                    btnFetchUrl.textContent = '🕷️ Cào';
                    btnFetchUrl.disabled = false;
                }
            });
        }

        // ---- Lấy Cốt - Thay Hồn ----
        const btnRewrite = document.getElementById('btn-rewrite');
        if (btnRewrite) {
            btnRewrite.addEventListener('click', async () => {
                const content = scrapeContentEl?.value.trim() || '';
                if (content.length < 100) { alert('Nội dung quá ngắn! Hãy dán ít nhất một chương truyện.'); return; }

                const mode    = document.getElementById('scrape-mode').value;
                const tone    = document.getElementById('scrape-tone').value;
                const newTitle = document.getElementById('scrape-new-title').value.trim();
                const wpTitle  = document.getElementById('scrape-wp-title').value.trim() || 'Truyện Viết Lại';

                const modePrompts = {
                    rewrite: 'Hãy viết lại đoạn truyện này hoàn toàn bằng tiếng Việt với giọng văn mới, nhưng GIỮ NGUYÊN cốt truyện, sự kiện, và cung bậc cảm xúc. Thay đổi cách diễn đạt, câu văn, và phong cách viết.',
                    transform: 'Hãy phân tích cốt truyện của đoạn này, sau đó viết lại HOÀN TOÀN với nhân vật mới tên khác, bối cảnh địa lý và thời đại khác, nhưng giữ nguyên xung đột và diễn biến cốt lõi.',
                    custom: document.getElementById('scrape-custom-prompt')?.value.trim() || 'Hãy sáng tác một câu chuyện mới dựa trên cảm hứng từ đoạn nội dung này.'
                };

                let prompt;
                if (mode === 'custom') {
                    // Custom: user's full prompt + content appended
                    const customInstr = modePrompts.custom;
                    prompt = customInstr + '\n\n';
                    prompt += `Giọng văn: ${tone}.\n`;
                    prompt += `YÊU CẦU KỸ THUẬT: Viết bằng tiếng Việt, 1500-3000 từ, có tiêu đề chương format "Chương X: [tên]", không giải thích thêm.\n\n`;
                    prompt += `--- TÀI LIỆU THAM KHẢO ---\n${content.slice(0, 15000)}`;
                } else {
                    prompt = modePrompts[mode] + '\n\n';
                    prompt += `Giọng văn: ${tone}.\n`;
                    if (newTitle) prompt += `Đặt tên truyện mới là: "${newTitle}".\n`;
                    prompt += `YÊU CẦU: Viết bằng tiếng Việt, 1500-3000 từ, có tiêu đề chương rõ ràng format "Chương X: [tên]", không giải thích thêm.\n\n`;
                    prompt += `--- NỘI DUNG GỐC ---\n${content.slice(0, 15000)}`;
                }

                // Get gemini key from server
                btnRewrite.textContent = '⏳ Đang xử lý...';
                btnRewrite.disabled = true;
                document.getElementById('scrape-status').textContent = 'Đang lấy key AI...';

                try {
                    const keyFD = new FormData();
                    keyFD.append('action', 'temply_studio_get_prompt');
                    keyFD.append('action_nonce', NONCE);
                    keyFD.append('title', wpTitle);
                    keyFD.append('prompt', 'rewrite');
                    keyFD.append('genre', 'Tổng Hợp');
                    keyFD.append('chapters', '1');
                    keyFD.append('tone', tone);
                    const keyRes = await fetch(AJAX_URL, { method: 'POST', body: keyFD }).then(r => r.json());
                    if (!keyRes.success) throw new Error('Không lấy được key AI');
                    const { gemini_key } = keyRes.data;

                    document.getElementById('scrape-status').textContent = 'Gemini đang viết lại... (30-90 giây)';

                    const aiModel = document.getElementById('ss-ai-model')?.value || 'gemini-2.5-flash';
                    const rewritten = await callGeminiFromBrowser(prompt, gemini_key, aiModel);

                    // Create a draft post via server
                    document.getElementById('scrape-status').textContent = 'Đang lưu bài viết...';
                    const draftFD = new FormData();
                    draftFD.append('action', 'temply_studio_create_draft');
                    draftFD.append('action_nonce', NONCE);
                    draftFD.append('title', newTitle || wpTitle);
                    const draftRes = await fetch(AJAX_URL, { method: 'POST', body: draftFD }).then(r => r.json());
                    if (!draftRes.success) throw new Error('Không tạo bài viết');
                    currentPostId = draftRes.data.post_id;

                    // Save rewritten content
                    const saveFD = new FormData();
                    saveFD.append('action', 'temply_studio_save_content');
                    saveFD.append('action_nonce', NONCE);
                    saveFD.append('post_id', currentPostId);
                    saveFD.append('raw_text', rewritten);
                    const saveRes = await fetch(AJAX_URL, { method: 'POST', body: saveFD }).then(r => r.json());
                    if (!saveRes.success) throw new Error('Không lưu được nội dung');

                    // Show in editor
                    generatedHTML = saveRes.data.content;
                    document.getElementById('ss-story-title-display').textContent = newTitle || wpTitle;
                    document.getElementById('ss-story-text').innerHTML = generatedHTML;
                    document.getElementById('ss-story-output').classList.add('visible');
                    document.getElementById('ss-empty-state').style.display = 'none';
                    document.getElementById('ss-schedule-panel').style.display = 'block';
                    const tmr = new Date(); tmr.setDate(tmr.getDate() + 1); tmr.setHours(8, 0, 0, 0);
                    document.getElementById('ss-publish-date').value = tmr.toISOString().slice(0, 16);

                    document.getElementById('scrape-status').innerHTML = '✅ Xong! Kiểm tra bên phải và lên lịch đăng.';
                    showToast('✅ Viết lại thành công! Kiểm tra nội dung bên phải.', 'success');
                    switchTab('create'); // Switch back to show schedule panel
                } catch(e) {
                    document.getElementById('scrape-status').textContent = '❌ Lỗi: ' + e.message;
                    showToast('❌ ' + e.message, 'error');
                } finally {
                    btnRewrite.textContent = '🔮 Lấy Cốt - Thay Hồn';
                    btnRewrite.disabled = false;
                }
            });
        }

        // ---- DOM refs ----
        const btnGenerate = document.getElementById('ss-btn-generate');
        const btnSplit     = document.getElementById('ss-btn-split');
        const btnAutoPilot = document.getElementById('ss-btn-autopilot');
        const btnNew       = document.getElementById('ss-btn-new');
        const statusDot   = document.getElementById('ss-status-dot');
        const statusText  = document.getElementById('ss-status-text');
        const progressWrap = document.getElementById('ss-progress');
        const progressFill = document.getElementById('ss-progress-fill');
        const progressLabel = document.getElementById('ss-progress-label');
        const emptyState  = document.getElementById('ss-empty-state');
        const storyOutput = document.getElementById('ss-story-output');
        const storyTitleDisplay = document.getElementById('ss-story-title-display');
        const storyText   = document.getElementById('ss-story-text');
        const wordCountEl = document.getElementById('ss-word-count');
        const statsEl     = document.getElementById('ss-stats');
        const statWords   = document.getElementById('stat-words');
        const statChapters = document.getElementById('stat-chapters');

        // ---- Genre tags ----
        document.querySelectorAll('.genre-tag').forEach(tag => {
            tag.addEventListener('click', () => {
                tag.classList.toggle('active');
                const genre = tag.dataset.genre;
                if (tag.classList.contains('active')) {
                    selectedGenres.push(genre);
                } else {
                    selectedGenres = selectedGenres.filter(g => g !== genre);
                }
            });
        });

        // ---- Auto-detect genres & tone from prompt ----
        const btnAutoDetect = document.getElementById('ss-btn-autodetect');
        if (btnAutoDetect) {
            btnAutoDetect.addEventListener('click', async () => {
                const prompt = document.getElementById('ss-prompt').value.trim();
                if (!prompt) { showToast('Nhập mô tả Ý tưởng trước rồi bấm Gợi ý!', 'error'); return; }

                const icon = document.getElementById('ss-autodetect-icon');
                icon.textContent = '⏳';
                btnAutoDetect.disabled = true;

                try {
                    const aiModel = document.getElementById('ss-ai-model') ? document.getElementById('ss-ai-model').value : 'gemini-2.5-flash';

                    // Get key + autodetect prompt from server
                    const fd = new FormData();
                    fd.append('action', 'temply_studio_autodetect_prompt');
                    fd.append('action_nonce', NONCE);
                    fd.append('prompt', prompt);

                    const keyRes = await fetch(AJAX_URL, { method: 'POST', body: fd }).then(r => r.json());
                    if (!keyRes.success) throw new Error(keyRes.data?.message || 'Lỗi!');

                    const { ai_prompt: autoPrompt, gemini_key } = keyRes.data;

                    const rawJson = await callGeminiFromBrowser(autoPrompt + '\n\nRespond ONLY in valid JSON: {"genres":["..."],"tone":"...", "titles":["..."], "chapters": 10}', gemini_key, aiModel);

                    // Extract JSON
                    const match = rawJson.match(/\{[\s\S]*\}/);
                    const data = JSON.parse(match ? match[0] : rawJson);

                    const genres = data.genres || [];
                    const tone = data.tone || '';
                    const titles = data.titles || [];
                    const suggestedChapters = data.chapters || 10;

                    // 1. Suggest Titles
                    const titleInput = document.getElementById('ss-title');
                    const suggestionsWrap = document.getElementById('title-suggestions');
                    if (titleInput && suggestionsWrap) {
                        suggestionsWrap.innerHTML = '';
                        if (titles.length > 0) {
                            if (!titleInput.value.trim()) {
                                titleInput.value = titles[0]; // Auto-fill first
                            }
                            // Render clickable tags
                            titles.forEach(t => {
                                const span = document.createElement('span');
                                span.style.cssText = 'font-size:11px; padding:4px 8px; border-radius:6px; background:rgba(99,102,241,0.1); color:#a5b4fc; cursor:pointer; border:1px solid rgba(99,102,241,0.3); transition:all 0.2s';
                                span.onmouseover = () => span.style.background = 'rgba(99,102,241,0.2)';
                                span.onmouseout = () => span.style.background = 'rgba(99,102,241,0.1)';
                                span.textContent = t;
                                span.onclick = () => { titleInput.value = t; };
                                suggestionsWrap.appendChild(span);
                            });
                        }
                    }

                    // 2. Clear & Apply old selections
                    selectedGenres = [];
                    document.querySelectorAll('.genre-tag').forEach(t => t.classList.remove('active'));

                    // Apply AI suggested genres
                    genres.forEach(g => {
                        const tag = document.querySelector(`.genre-tag[data-genre="${g}"]`);
                        if (tag) { tag.classList.add('active'); selectedGenres.push(g); }
                    });

                    // 3. Apply tone
                    const toneSelect = document.getElementById('ss-tone');
                    for (let opt of toneSelect.options) {
                        if (opt.value.includes(tone) || tone.includes(opt.value.split(',')[0])) { opt.selected = true; break; }
                    }

                    // 4. Apply suggested chapters
                    const chapterInput = document.getElementById('ss-chapters');
                    if (chapterInput && suggestedChapters) {
                        chapterInput.value = suggestedChapters;
                        if(typeof updateChapterNote === 'function') updateChapterNote(suggestedChapters);
                    }

                    showToast(`🎯 Gợi ý: ${genres.join(', ')} | ${suggestedChapters} Chương | Giọng: ${tone}`);
                } catch(e) {
                    showToast('Lỗi: ' + e.message, 'error');
                } finally {
                    icon.textContent = '🤖';
                    btnAutoDetect.disabled = false;
                }
            });
        }

        // ---- Toast helper ----
        function showToast(msg, type = 'success') {
            const el = document.createElement('div');
            el.className = `toast ${type}`;
            el.innerHTML = `<span>${type === 'success' ? '✅' : '❌'}</span> ${msg}`;
            document.getElementById('ss-toasts').appendChild(el);
            setTimeout(() => el.classList.add('show'), 10);
            setTimeout(() => {
                el.classList.remove('show');
                setTimeout(() => el.remove(), 300);
            }, 4000);
        }

        // ---- Set status ----
        function setStatus(text, state = 'idle') {
            statusText.textContent = text;
            statusDot.className = 'status-dot';
            if (state === 'active') statusDot.classList.add('active');
            if (state === 'loading') statusDot.classList.add('loading');
        }

        // ---- Progress helper ----
        function setProgress(pct, label) {
            progressWrap.classList.add('active');
            progressFill.style.width = pct + '%';
            if (label) progressLabel.textContent = label;
        }
        function hideProgress() {
            progressWrap.classList.remove('active');
            progressFill.style.width = '0%';
        }

        // ---- Word count ----
        function updateWordCount() {
            const text = storyText.innerText || '';
            const words = text.trim().split(/\s+/).filter(w => w).length;
            wordCountEl.textContent = words.toLocaleString('vi-VN') + ' từ';
            statWords.textContent = words.toLocaleString('vi-VN');
            const chapters = (text.match(/Chương\s+\d+/gi) || []).length;
            statChapters.textContent = chapters;
            return {words, chapters};
        }

        // ---- Main Generate Flow ----
        btnGenerate.addEventListener('click', async () => {
            if (isGenerating) return;

            const title = document.getElementById('ss-title').value.trim();
            const prompt = document.getElementById('ss-prompt').value.trim();
            const chapCount = document.getElementById('ss-chapters').value;
            const tone = document.getElementById('ss-tone').value;

            if (!title) { showToast('Vui lòng nhập Tiêu đề truyện!', 'error'); return; }
            if (!prompt) { showToast('Vui lòng mô tả ý tưởng cốt truyện!', 'error'); return; }

            isGenerating = true;
            btnGenerate.disabled = true;
            btnSplit.disabled = true;
            if (btnAutoPilot) btnAutoPilot.disabled = true;
            document.getElementById('ss-btn-icon').textContent = '⏳';
            document.getElementById('ss-btn-text').textContent = 'Đang sáng tác...';

            emptyState.style.display = 'none';
            storyOutput.classList.add('visible');
            storyTitleDisplay.textContent = title;
            storyText.innerHTML = '<span class="text-cursor"></span>';

            setStatus('AI đang viết truyện...', 'loading');
            setProgress(5, 'Đang khởi động AI...');

            try {
                // Step 1: Skip pre-creating draft to avoid empty drafts if generation fails or user aborts
                currentPostId = 0;

                // Step 2: Generate story content via AI -- called FROM BROWSER directly
                setProgress(20, 'AI đang sáng tác nội dung...');
                const genre = selectedGenres.join(', ') || 'Phổ thông';
                const aiModel = document.getElementById('ss-ai-model') ? document.getElementById('ss-ai-model').value : 'gemini-2.5-flash';

                // Step 2a: Get prompt + API key from server (PHP just builds prompt, doesn't call AI)
                const promptFD = new FormData();
                promptFD.append('action', 'temply_studio_get_prompt');
                promptFD.append('action_nonce', NONCE);
                promptFD.append('title', title);
                promptFD.append('prompt', prompt);
                promptFD.append('genre', genre);
                promptFD.append('chapters', chapCount);
                promptFD.append('tone', tone);

                const promptRes = await fetch(AJAX_URL, { method: 'POST', body: promptFD }).then(r => r.json());
                if (!promptRes.success) throw new Error(promptRes.data?.message || 'Không lấy được prompt!');

                const { prompt: aiPrompt, gemini_key, has_key } = promptRes.data;

                let rawContent = '';

                const totalChaps = parseInt(chapCount);
                const BATCH_SIZE = 3; // chapters per Gemini call
                const totalBatches = Math.ceil(totalChaps / BATCH_SIZE);

                if (has_key && aiModel !== 'openai') {
                    // Batch generation: call Gemini once per batch of 3 chapters
                    for (let batch = 0; batch < totalBatches; batch++) {
                        const chStart = batch * BATCH_SIZE + 1;
                        const chEnd   = Math.min(chStart + BATCH_SIZE - 1, totalChaps);
                        const batchPct = 35 + Math.floor((batch / totalBatches) * 45);
                        setProgress(batchPct, `Viết chương ${chStart}–${chEnd} / ${totalChaps}...`);

                        // Build batch prompt
                        let batchPrompt = aiPrompt
                            .replace(`Viết đúng ${totalChaps} chương`, `Viết đúng ${chEnd - chStart + 1} chương (từ Chương ${chStart} đến Chương ${chEnd})`)
                            .replace('Hãy bắt đầu viết ngay bây giờ:', `Ghi nhớ: đây là phần ${batch + 1}/${totalBatches} của bộ truyện. Tiếp tục xây dựng tình tiết hấp dẫn, TUYỆT ĐỐI KHÔNG BẮT ĐẦU LẠI TỪ ĐẦU.\nHãy bắt đầu viết NGAY TỪ Chương ${chStart}:`);

                        // If not the first batch, don't ask for Title and Description again
                        // AND MUST INCLUDE THE PREVIOUS GENERATED CONTEXT SO IT DOESN'T REPEAT PLOTS!
                        if (batch > 0) {
                            batchPrompt = batchPrompt.replace(/1\. BẮT BUỘC bắt đầu bằng dòng: "Tiêu đề:.*?\n/g, '')
                                                     .replace(/2\. BẮT BUỘC dòng thứ hai là: "Mô tả:.*?\n/g, '');
                                                     
                            let safeContext = rawContent;
                            if (safeContext.length > 500000) safeContext = "..." + safeContext.slice(-500000);
                            
                            batchPrompt = `[CỐT TRUYỆN ĐÃ XẢY RA TRONG CÁC CHƯƠNG TRƯỚC - HÃY ĐỌC THẬT KỸ ĐỂ DUY TRÌ TÍNH NHẤT QUÁN CỦA TÊN NHÂN VẬT VÀ TÌNH TIẾT, TUYỆT ĐỐI KHÔNG LẶP LẠI VÀ KHÔNG VIẾT LẠI DOẠN MỞ ĐẦU NÀY NỮA]:\n${safeContext}\n\n[HẾT TÓM TẮT TRƯỚC HÃY TIẾP TỤC] MỤC TIÊU TIẾP THEO:\n\n` + batchPrompt;
                        }

                        const batchContent = await callGeminiFromBrowser(batchPrompt, gemini_key, aiModel);
                        rawContent += (rawContent ? '\n\n' : '') + batchContent;

                        // Show preview as it's generated
                        if (batch === 0) {
                            storyText.innerHTML = '<p style="color:#a5b4fc;font-size:13px;">⏳ Đang tạo thêm chương... (' + (batch+1) + '/' + totalBatches + ' batch)</p>' + batchContent.replace(/\n/g,'<br>');
                        } else {
                            const prog = storyText.querySelector('p[style]');
                            if (prog) prog.textContent = '⏳ Đang tạo thêm chương... (' + (batch+1) + '/' + totalBatches + ' batch)';
                        }
                    }
                } else {
                    // Fallback: ask server to use Pollinations
                    const storyFD = new FormData();
                    storyFD.append('action', 'temply_studio_generate_story');
                    storyFD.append('action_nonce', NONCE);
                    storyFD.append('post_id', currentPostId);
                    storyFD.append('title', title);
                    storyFD.append('prompt', prompt);
                    storyFD.append('genre', genre);
                    storyFD.append('chapters', chapCount);
                    storyFD.append('tone', tone);
                    storyFD.append('ai_model', 'openai');
                    const genRes = await fetch(AJAX_URL, { method: 'POST', body: storyFD }).then(r => r.json());
                    if (!genRes.success) throw new Error(genRes.data?.message || 'Lỗi khi tạo nội dung!');
                    rawContent = genRes.data.raw_content || '';
                }

                setProgress(85, 'Đang lưu nội dung...');

                // Step 3: Save the AI content to WordPress via server
                const saveFD = new FormData();
                saveFD.append('action', 'temply_studio_save_content');
                saveFD.append('action_nonce', NONCE);
                saveFD.append('post_id', currentPostId);
                saveFD.append('raw_text', rawContent);
                saveFD.append('title', title);
                saveFD.append('genre', genre);
                const saveRes = await fetch(AJAX_URL, { method: 'POST', body: saveFD }).then(r => r.json());
                if (!saveRes.success) throw new Error(saveRes.data?.message || 'Lỗi khi lưu nội dung!');
                currentPostId = saveRes.data.post_id;

                setProgress(95, 'Hoàn thiện truyện...');

                // Display the content with a typewriter-like progressive reveal
                generatedHTML = saveRes.data.content;
                storyText.innerHTML = '';

                // Parse content into paragraphs and render gradually
                const tempDiv = document.createElement('div');
                tempDiv.innerHTML = generatedHTML;
                const nodes = Array.from(tempDiv.childNodes);

                for (let i = 0; i < nodes.length; i++) {
                    storyText.appendChild(nodes[i].cloneNode(true));
                    if (i % 3 === 0) {
                        setProgress(90 + Math.floor((i / nodes.length) * 10), 'Hiển thị nội dung...');
                        await new Promise(r => setTimeout(r, 5));
                    }
                }

                setProgress(100, 'Hoàn tất!');
                updateWordCount();

                statsEl.style.display = 'flex';
                btnSplit.disabled = false;
                if (btnAutoPilot) btnAutoPilot.disabled = false;
                btnNew.style.display = 'block';
                document.getElementById('ss-btn-review').style.display = 'block';
                setStatus('Truyện đã sẵn sàng để duyệt', 'active');

                const {chapters: chapDone} = updateWordCount();
                showToast(`✨ Đã tạo xong ${chapDone} chương truyện "${title}"! Đọc duyệt và nhấn Tách Chương khi OK.`);

                // Show scheduling panel
                const schedPanel = document.getElementById('ss-schedule-panel');
                if (schedPanel) {
                    schedPanel.style.display = 'block';
                    const tmr = new Date(); tmr.setDate(tmr.getDate() + 1); tmr.setHours(8, 0, 0, 0);
                    document.getElementById('ss-publish-date').value = tmr.toISOString().slice(0, 16);
                }

            } catch(err) {
                setStatus('Lỗi: ' + err.message, 'idle');
                showToast('Lỗi: ' + err.message, 'error');
                storyText.innerHTML = `<p style="color:#f87171;">⚠️ Lỗi: ${err.message}</p>`;
            } finally {
                isGenerating = false;
                btnGenerate.disabled = false;
                document.getElementById('ss-btn-icon').textContent = '✨';
                document.getElementById('ss-btn-text').textContent = 'Tái sáng tác (tạo lại)';
                setTimeout(hideProgress, 1200);
            }
        });

        // ---- AI Review Handler ----
        const btnReviewStory = document.getElementById('ss-btn-review');
        if (btnReviewStory) {
            btnReviewStory.addEventListener('click', async () => {
                const storyContent = storyText.innerText || '';
                const storyTitle = storyTitleDisplay.textContent || 'Truyện chưa đặt tên';
                if (storyContent.length < 200) { showToast('Chưa có nội dung để nhận xét!', 'error'); return; }

                const overlay = document.getElementById('ss-review-overlay');
                const reviewContent = document.getElementById('ss-review-content');
                overlay.style.display = 'flex';
                reviewContent.innerHTML = '<div style="text-align:center;padding:40px;color:#6b7280;">⏳ Gemini AI đang đọc và phân tích truyện của anh...</div>';

                btnReviewStory.textContent = '⏳ Đang nhận xét...';
                btnReviewStory.disabled = true;

                try {
                    const keyFD = new FormData();
                    keyFD.append('action', 'temply_studio_autodetect_prompt');
                    keyFD.append('action_nonce', NONCE);
                    keyFD.append('prompt', storyTitle);
                    const keyRes = await fetch(AJAX_URL, { method: 'POST', body: keyFD }).then(r => r.json());
                    if (!keyRes.success) throw new Error('Không lấy được key AI');

                    const aiModel = document.getElementById('ss-ai-model')?.value || 'gemini-2.5-flash';
                    const reviewPrompt = `Bạn là một biên tập viên văn học chuyên nghiệp, có kinh nghiệm đánh giá truyện mạng Việt Nam.

Hãy đọc bộ truyện có tiêu đề: "${storyTitle}" và viết bài NHẬN XÉT CHUYÊN SÂU theo cấu trúc sau:

## 1. ✅ Điểm Mạnh Nổi Bật
(Liệt kê 3-5 điểm hay, cụ thể về tình tiết, nhân vật, giọng văn, hook)

## 2. 🔧 Hạt Sạn Cần Điều Chỉnh  
(Phân tích từng vấn đề: logic dòng thời gian, tính nhất quán bối cảnh, nhân vật thiếu chiều sâu, v.v. — góp ý cụ thể từng điểm kèm gợi ý sửa)

## 3. 💡 Gợi Ý Phát Triển
(3-5 hướng mở rộng hoặc cải thiện để câu chuyện hấp dẫn hơn)

## 4. 🎯 Điểm Tiềm Năng Viral
(Yếu tố nào có thể viral trên mạng xã hội Việt Nam)

## 5. ⭐ Tổng Điểm
(Chấm điểm từng hạng mục: Cốt truyện /10, Nhân vật /10, Văn phong /10, Độc tính /10)

Viết bằng tiếng Việt, thẳng thắn nhưng mang tính xây dựng. KHÔNG khen chung chung.

--- NỘI DUNG TRUYỆN ---
${storyContent.slice(0, 25000)}`;

                    const review = await callGeminiFromBrowser(reviewPrompt, keyRes.data.gemini_key, aiModel);

                    // Format markdown-ish output
                    const formatted = review
                        .replace(/## (\d+\..+)/g, '<h3 style="color:#fbbf24;margin:20px 0 10px;font-size:15px;">$1</h3>')
                        .replace(/\*\*(.+?)\*\*/g, '<strong style="color:#e5e7eb;">$1</strong>')
                        .replace(/^(\d+\..+)$/gm, '<div style="margin:6px 0;">$1</div>')
                        .replace(/^[-–•]\s(.+)$/gm, '<li style="margin:5px 0 5px 16px;list-style:disc;">$1</li>')
                        .replace(/\n{2,}/g, '</p><p style="margin:8px 0;">')
                        .replace(/\n/g, '<br>');

                    reviewContent.innerHTML = '<p style="margin:8px 0;">' + formatted + '</p>';
                    
                    // Add Fix Button & Custom User Request Field
                    reviewContent.innerHTML += `
                        <div style="margin-top:24px; padding-top:20px; border-top:1px solid rgba(255,255,255,0.05);">
                            <label style="display:block; font-size:13px; font-weight:700; color:#fbbf24; margin-bottom:8px;">💡 Yêu cầu bổ sung của bạn (tuỳ chọn):</label>
                            <textarea id="ss-custom-fix-prompt" placeholder="Ví dụ: Đổi kết truyện bi thảm hơn, cho nhân vật nam phụ ác hơn, hay lược bỏ đoạn miêu tả cảnh tĩnh tĩnh..." style="width:100%; height:80px; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:12px; color:#fff; font-family:inherit; font-size:13px; resize:vertical; margin-bottom:16px; box-sizing:border-box;"></textarea>
                            
                            <div style="text-align:center;">
                                <button id="ss-btn-apply-fix" style="padding:14px 28px; border-radius:10px; border:none; background:linear-gradient(135deg, #fbbf24, #f59e0b); color:#111827; font-weight:800; font-size:15px; cursor:pointer; box-shadow:0 4px 15px rgba(245,158,11,0.3); transition:transform 0.2s;">
                                    ✨ Áp dụng Góp ý & Viết lại Truyện
                                </button>
                                <div style="font-size:11px; color:#6b7280; margin-top:8px;">Hệ thống sẽ giữ nguyên dàn ý và sửa lại văn bản dựa trên các hạt sạn được nêu.</div>
                            </div>
                        </div>
                    `;

                    // Handle Fix feature
                    const btnApplyFix = document.getElementById('ss-btn-apply-fix');
                    if (btnApplyFix) {
                        btnApplyFix.addEventListener('click', async function() {
                            this.disabled = true;
                            this.innerHTML = '⏳ Hệ thống đang viết lại... (Vui lòng không đóng hộp thoại)';
                            this.style.opacity = '0.7';

                            try {
                                const customRequest = document.getElementById('ss-custom-fix-prompt')?.value.trim() || '';
                                
                                // Extract chapters from current text
                                const contentText = storyText.innerText || '';
                                // Split by "Chương " but keep it (using positive regex if possible, or manual slice)
                                let chapters = [];
                                const parts = contentText.split(/(?=Chương\s+\d+[:\-–.])/i);
                                if (parts.length > 1 && parts[0].trim().length < 50) {
                                    // Remove empty first chunk
                                    parts.shift();
                                }
                                
                                if (parts.length <= 1) {
                                    chapters = [contentText]; // No clear chapter structure, chunk as 1
                                } else {
                                    chapters = parts;
                                }

                                // We batch rewrite 2 chapters at a time to avoid Gemini output truncation
                                const BATCH_SIZE = 2;
                                const totalBatches = Math.ceil(chapters.length / BATCH_SIZE);
                                let newFullStory = '';

                                for (let i = 0; i < totalBatches; i++) {
                                    this.textContent = `⏳ Đang sửa phần ${i+1}/${totalBatches}...`;
                                    
                                    const chunkChaps = chapters.slice(i * BATCH_SIZE, (i + 1) * BATCH_SIZE).join('\n\n');
                                    
                                    const fixPrompt = `Bạn là một biên tập viên văn học tinh tế.
Dựa vào BÀI NHẬN XÉT GÓP Ý TRUYỆN sau đây:

--- NHẬN XÉT ---
${review.slice(0, 4000)}
--- HẾT NHẬN XÉT ---
${customRequest ? `\n--- YÊU CẦU THÊM TỪ TÁC GIẢ BẮT BUỘC PHẢI NGHE THEO ---\n${customRequest}\n----------------------------------------------------\n` : ''}

YÊU CẦU:
Hãy SỬA CHỮA, TỐI ƯU VÀ VIẾT LẠI hoàn chỉnh đoạn truyện bên dưới.
1. Khắc phục triệt để các "Hạt sạn" và mâu thuẫn được nêu trong nhận xét.
2. Thêm thắt chi tiết miêu tả, chiều sâu tâm lý nhân vật nếu nhận xét có gợi ý.
${customRequest ? '3. BẮT BUỘC SỬA ĐỔI dựa trên "YÊU CẦU THÊM TỪ TÁC GIẢ".' : ''}
4. BẮT BUỘC giữ nguyên cấu trúc tiêu đề "Chương X: [Tên]" ở đầu mỗi chương.
5. Trả về toàn bộ phần văn bản đã sửa (không giải thích thêm).

--- ĐOẠN TRUYỆN CẦN SỬA ---
${chunkChaps}`;

                                    const chunkRewritten = await callGeminiFromBrowser(fixPrompt, keyRes.data.gemini_key, aiModel);
                                    newFullStory += (newFullStory ? '\n\n' : '') + chunkRewritten;
                                }

                                // Replace editor content with fixed story
                                storyText.innerHTML = newFullStory.replace(/\n\n/g, '</p><p>').replace(/\n/g, '<br>');
                                // Wrap in <p> if not already
                                if (!storyText.innerHTML.startsWith('<p>')) {
                                    storyText.innerHTML = '<p>' + storyText.innerHTML + '</p>';
                                }
                                
                                // Clean up formatting for headings 
                                storyText.innerHTML = storyText.innerHTML.replace(/<p>(Chương\s+\d+[:\-–.].*?)<\/p>/gi, '<h2>$1</h2>');

                                showToast('✨ Truyện đã được cải thiện theo góp ý!', 'success');
                                document.getElementById('ss-review-overlay').style.display = 'none';
                                updateWordCount();

                            } catch (err) {
                                alert('Lỗi khi sửa truyện: ' + err.message);
                            } finally {
                                this.innerHTML = '✨ Áp dụng Góp ý & Viết lại Truyện';
                                this.disabled = false;
                                this.style.opacity = '1';
                            }
                        });
                    }

                    showToast('✅ AI đã nhận xét xong!', 'success');
                } catch(e) {
                    reviewContent.innerHTML = `<p style="color:#f87171;">❌ Lỗi: ${e.message}</p>`;
                } finally {
                    btnReviewStory.textContent = '🔍 AI Nhận xét & Góp ý truyện';
                    btnReviewStory.disabled = false;
                }
            });
        }

        // ---- Split chapters ----
        btnSplit.addEventListener('click', () => {
            if (!currentPostId || !generatedHTML) {
                showToast('Chưa có nội dung để tách!', 'error');
                return;
            }
            document.getElementById('ss-confirm').classList.add('active');
        });

        document.getElementById('ss-confirm-yes').addEventListener('click', async () => {
            document.getElementById('ss-confirm').classList.remove('active');
            btnSplit.disabled = true;
            setStatus('Đang tách và đăng các chương lên...', 'loading');
            setProgress(10, 'Đang xử lý tách chương...');

            try {
                const fd = new FormData();
                fd.append('action', 'temply_ai_split_chapters');
                fd.append('action_nonce', NONCE);
                fd.append('post_id', currentPostId);
                fd.append('content', generatedHTML);

                const res = await fetch(AJAX_URL, { method: 'POST', body: fd }).then(r => r.json());
                setProgress(100, 'Hoàn tất!');

                if (res.success) {
                    setStatus(`Đã đăng ${res.data.count} chương thành công!`, 'active');
                    showToast(`🎉 Tách thành công ${res.data.count} chương! Vào WP Admin để kiểm tra.`);

                    // Render list
                    document.getElementById('ss-chapters-created').style.display = 'block';
                    const listEl = document.getElementById('ss-chapters-list');
                    listEl.innerHTML = `[${res.data.count} chương]`.replace(/\[(\d+) chương\]/, (_, n) => {
                        let html = '';
                        for (let i = 1; i <= Math.min(parseInt(n), 20); i++) {
                            html += `<div class="chapter-chip"><span class="num">${i}</span>Chương ${i} đã đăng ✓</div>`;
                        }
                        if (parseInt(n) > 20) html += `<div class="chapter-chip" style="justify-content:center; color:#a78bfa">...và ${parseInt(n)-20} chương khác</div>`;
                        return html;
                    });
                } else {
                    throw new Error(res.data?.message || 'Tách chương thất bại!');
                }
            } catch(err) {
                showToast(err.message, 'error');
                setStatus('Lỗi tách chương', 'idle');
                btnSplit.disabled = false;
            } finally {
                setTimeout(hideProgress, 1000);
            }
        });

        document.getElementById('ss-confirm-no').addEventListener('click', () => {
            document.getElementById('ss-confirm').classList.remove('active');
        });

        // ---- New story ----
        btnNew.addEventListener('click', () => {
            if (!confirm('Tạo truyện mới sẽ xoá nội dung hiện tại khỏi màn hình (dữ liệu đã lưu trên server vẫn còn). Bạn chắc chắn?')) return;
            generatedHTML = '';
            currentPostId = 0;
            selectedGenres = [];
            document.querySelectorAll('.genre-tag.active').forEach(t => t.classList.remove('active'));
            document.getElementById('ss-title').value = '';
            document.getElementById('ss-prompt').value = '';
            storyText.innerHTML = '';
            storyTitleDisplay.textContent = '';
            storyOutput.classList.remove('visible');
            emptyState.style.display = 'flex';
            btnSplit.disabled = true;
            btnNew.style.display = 'none';
            statsEl.style.display = 'none';
            document.getElementById('ss-chapters-created').style.display = 'none';
            document.getElementById('ss-btn-text').textContent = 'Bắt đầu Sáng Tác';
            document.getElementById('ss-schedule-panel').style.display = 'none';
            setStatus('Chờ lệnh', 'idle');
        });

        // ---- Floating AI Toolbar (Text Selection) ----
        const floatToolbar = document.getElementById('ai-floating-toolbar');
        let currentSelectionRange = null;

        document.addEventListener('selectionchange', () => {
            const selection = window.getSelection();
            if (selection.rangeCount > 0 && !selection.isCollapsed) {
                const range = selection.getRangeAt(0);
                if (storyText.contains(range.commonAncestorContainer)) {
                    const rect = range.getBoundingClientRect();
                    floatToolbar.style.display = 'flex';
                    floatToolbar.style.top = (rect.top + window.scrollY - floatToolbar.offsetHeight - 8) + 'px';
                    floatToolbar.style.left = (rect.left + window.scrollX + (rect.width/2) - (floatToolbar.offsetWidth/2)) + 'px';
                    currentSelectionRange = range;
                } else if (!floatToolbar.contains(selection.anchorNode)) {
                    floatToolbar.style.display = 'none';
                }
            } else {
                setTimeout(() => {
                    const activeEl = document.activeElement;
                    if (!floatToolbar.contains(activeEl)) {
                        floatToolbar.style.display = 'none';
                    }
                }, 100);
            }
        });

        document.querySelectorAll('.ai-tool-btn').forEach(btn => {
            btn.addEventListener('click', async (e) => {
                e.preventDefault();
                e.stopPropagation();
                if (!currentSelectionRange) return;
                
                const action = btn.getAttribute('data-action');
                const selectedText = currentSelectionRange.toString();
                if (!selectedText.trim()) return;

                let prompt = '';
                if (action === 'improve') prompt = 'Hãy viết lại đoạn văn sau bằng tiếng Việt sao cho tự nhiên, mượt mà và hấp dẫn hơn, nhưng giữ nguyên ý chính. Chỉ trả về đoạn văn đã sửa, KHÔNG giải thích gì thêm:\n\n' + selectedText;
                else if (action === 'expand') prompt = 'Hãy mở rộng đoạn văn sau một cách chi tiết hơn, thêm miêu tả cảnh vật, cảm xúc hoặc hành động phù hợp. Chỉ trả về kết quả tiếng Việt, KHÔNG giải thích thêm:\n\n' + selectedText;
                else if (action === 'fix') prompt = 'Hãy sửa mọi lỗi chính tả, dấu câu và ngữ pháp trong đoạn văn sau (nếu có). Chỉ trả về đoạn văn đã sửa tiếng Việt, KHÔNG giải thích thêm:\n\n' + selectedText;
                else if (action === 'custom') {
                    const customInstr = window.prompt('Bạn muốn AI làm gì với đoạn văn này? (VD: Đổi xưng hô, sửa lối văn,...)');
                    if (!customInstr) return;
                    prompt = `Dựa vào hướng dẫn sau: "${customInstr}". Hãy sửa lại đoạn văn bên dưới bằng tiếng Việt và chỉ trả về đoạn văn đã sửa, KHÔNG giải thích:\n\n${selectedText}`;
                }

                const origText = btn.textContent;
                btn.textContent = '⏳...';
                floatToolbar.style.pointerEvents = 'none';

                try {
                    // Get key
                    const keyFD = new FormData();
                    keyFD.append('action', 'temply_studio_autodetect_prompt');
                    keyFD.append('action_nonce', NONCE);
                    keyFD.append('prompt', 'get_key_only');
                    const keyRes = await fetch(AJAX_URL, { method: 'POST', body: keyFD }).then(r => r.json());
                    if (!keyRes.success) throw new Error('Không lấy được key');
                    
                    const aiModel = document.getElementById('ss-ai-model')?.value || 'gemini-2.5-flash';
                    const resultText = await callGeminiFromBrowser(prompt, keyRes.data.gemini_key, aiModel);
                    
                    // Replace text in DOM
                    currentSelectionRange.deleteContents();
                    currentSelectionRange.insertNode(document.createTextNode(resultText));
                    
                    showToast('✨ Đoạn văn đã được cải thiện!', 'success');
                } catch(err) {
                    showToast('Lỗi AI: ' + err.message, 'error');
} finally {
                    btn.textContent = origText;
                    floatToolbar.style.display = 'none';
                    floatToolbar.style.pointerEvents = 'auto';
                    window.getSelection().removeAllRanges();
                    currentSelectionRange = null;
                }
            });
        });

        // ---- Helper: Extract JSON from text ----
        function extractJsonFromArrayText(text) {
            try {
                const s = text.substring(text.indexOf('['), text.lastIndexOf(']') + 1);
                return JSON.parse(s);
            } catch (e) {
                return null;
            }
        }

        // ==========================================
        // FEATURE: Brainstorm Prompts
        // ==========================================
        document.getElementById('ss-btn-brainstorm').addEventListener('click', async function() {
            const promptBox = document.getElementById('ss-prompt');
            const userKeyword = promptBox.value.trim();
            const selectedGenres = Array.from(document.querySelectorAll('#ss-genres .genre-tag.active')).map(el => el.dataset.genre).join(', ');
            const selectedTone = document.getElementById('ss-tone').value;
            const bCount = document.getElementById('ss-brainstorm-count').value || 10;

            if (!selectedGenres && !userKeyword) {
                showToast('🚨 Vui lòng chọn ít nhất 1 Thể loại hoặc gõ vài từ khóa trước khi Brainstorm!', 'error');
                return;
            }

            const btn = this;
            const icon = document.getElementById('ss-brainstorm-icon');
            btn.disabled = true;
            btn.style.opacity = '0.7';
            icon.innerHTML = '⏳';
            showToast(`💡 Đang suy nghĩ ${bCount} kịch bản...`, 'info');

            try {
                // 1. Fetch AI Prompt from Server
                const fd = new FormData();
                fd.append('action', 'temply_studio_brainstorm_prompts');
                fd.append('action_nonce', NONCE);
                fd.append('genres', selectedGenres);
                fd.append('tone', selectedTone);
                fd.append('prompt', userKeyword);
                fd.append('count', bCount);

                const res = await fetch(AJAX_URL, { method: 'POST', body: fd }).then(r => r.json());
                if (!res.success) throw new Error(res.data.message || 'Lỗi lấy Brainstorm Prompt');

                const systemPrompt = res.data.ai_prompt;
                const apiKey = res.data.gemini_key;
                const aiModel = document.getElementById('ss-ai-model').value || 'gemini-2.5-flash';

                // 2. Call Gemini
                showToast('🤖 Đang yêu cầu AI đẻ idea...', 'info');
                const aiResult = await callGeminiFromBrowser(systemPrompt, apiKey, aiModel);
                
                // 3. Parse Result
                let prompts = extractJsonFromArrayText(aiResult);
                if (!prompts || !Array.isArray(prompts) || prompts.length === 0) {
                    console.error("AI Result Parsing Error:", aiResult);
                    throw new Error('AI không trả về đúng định dạng Mảng JSON.');
                }

                // 4. Render UI Modal
                renderBrainstormModal(prompts);
                
                showToast(`✅ Đã tạo xong ${bCount} kịch bản!`, 'success');
            } catch (err) {
                showToast('❌ Lỗi: ' + err.message, 'error');
            } finally {
                btn.disabled = false;
                btn.style.opacity = '1';
                icon.innerHTML = '💡';
            }
        });

        function renderBrainstormModal(prompts) {
            let existingParams = document.getElementById('ss-brainstorm-modal');
            if (existingParams) existingParams.remove();

            const c = document.createElement('div');
            c.id = 'ss-brainstorm-modal';
            c.style.cssText = 'position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.85);backdrop-filter:blur(10px);z-index:999999;display:flex;align-items:center;justify-content:center;padding:20px;';
            
            let listHtml = '';
            window.__currentBrainstormPrompts = prompts; // Lưu tạm để AI Evaluate gọi lại

            prompts.forEach((pObj, index) => {
                if(typeof pObj === 'string') pObj = { title: 'Kịch bản #' + (index+1), genres: 'Mặc định', prompt: pObj };
                const safePayload = encodeURIComponent(JSON.stringify(pObj));
                const encodedPromptText = pObj.prompt.replace(/"/g, '&quot;');
                
                listHtml += `
                <label id="bs-prompt-card-${index}" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); border-radius:12px; padding:16px; margin-bottom:12px; display:flex; gap:12px; cursor:pointer; align-items:flex-start; transition:background 0.2s;" onmouseover="this.style.background='rgba(255,255,255,0.06)'" onmouseout="this.style.background='rgba(255,255,255,0.03)'">
                    <input type="checkbox" class="brainstorm-checkbox" data-payload="${safePayload}" value="${encodedPromptText}" style="margin-top:2px; width:18px; height:18px;">
                    <div style="flex:1;">
                        <div style="font-size:14px; font-weight:800; color:#10b981; margin-bottom:4px;">${pObj.title || ('Kịch bản #' + (index+1))}</div>
                        <div style="font-size:11px; font-weight:700; color:#cbd5e1; background:rgba(245,158,11,0.15); border:1px solid rgba(245,158,11,0.3); padding:2px 8px; border-radius:20px; display:inline-block; margin-bottom:8px;">🏷️ ${pObj.genres || 'Đa thể loại'}</div>
                        <p style="font-size:13px; color:#94a3b8; line-height:1.6; margin:0;">${pObj.prompt}</p>
                        <div id="bs-prompt-eval-${index}" style="margin-top:10px;"></div>
                    </div>
                </label>`;
            });

            c.innerHTML = `
                <div style="background:#1e293b; border:1px solid rgba(255,255,255,0.1); border-radius:16px; width:100%; max-width:850px; max-height:85vh; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 25px 50px -12px rgba(0,0,0,0.8);">
                    <div style="padding:20px; border-bottom:1px solid rgba(255,255,255,0.1); display:flex; justify-content:space-between; align-items:center;">
                        <div style="display:flex; align-items:center; gap:12px;">
                            <h2 style="margin:0; font-size:18px; color:#fff; font-weight:800;">💡 Gợi Ý Kịch Bản</h2>
                            <button onclick="handleBrainstormEvaluate()" id="bs-btn-evaluate" style="background:rgba(217,70,239,0.15); color:#d946ef; border:1px solid rgba(217,70,239,0.3); padding:6px 12px; border-radius:6px; font-size:12px; font-weight:700; cursor:pointer;" title="AI tự động phân tích độ Mặn/Nhạt của các idea này">🤖 AI Đánh Giá Cốt Truyện</button>
                        </div>
                        <button onclick="document.getElementById('ss-brainstorm-modal').remove()" style="background:transparent; border:none; color:#94a3b8; font-size:24px; cursor:pointer; line-height:1;">&times;</button>
                    </div>
                    <div style="padding:16px; background:rgba(0,0,0,0.2); border-bottom:1px solid rgba(255,255,255,0.05); display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px;">
                        <label style="display:flex; align-items:center; gap:6px; cursor:pointer; color:#10b981; font-size:13px; font-weight:700;">
                            <input type="checkbox" id="bs-check-all" onchange="document.querySelectorAll('.brainstorm-checkbox').forEach(cb => cb.checked = this.checked)" style="width:16px;height:16px;"> Chọn tất cả
                        </label>
                        <div style="display:flex; align-items:center; gap:12px; flex-wrap:wrap;">
                            <div style="display:flex; align-items:center; gap:8px;">
                                <span style="color:#94a3b8; font-size:13px;">Độ dài:</span>
                                <input type="number" id="bs-chapters-min" value="20" min="5" style="width:45px; background:transparent; border:1px solid rgba(255,255,255,0.2); color:#fff; border-radius:6px; padding:4px; text-align:center; font-size:13px;">
                                <span style="color:#94a3b8; font-size:13px;">-</span>
                                <input type="number" id="bs-chapters-max" value="40" min="5" style="width:45px; background:transparent; border:1px solid rgba(255,255,255,0.2); color:#fff; border-radius:6px; padding:4px; text-align:center; font-size:13px;">
                                <span style="color:#94a3b8; font-size:13px;">chương</span>
                            </div>
                            <div style="display:flex; align-items:center; gap:8px;">
                                <span style="color:#94a3b8; font-size:13px;">Tốc độ:</span>
                                <select id="bs-interval" style="background:transparent; border:1px solid rgba(255,255,255,0.2); color:#fff; border-radius:6px; padding:4px; font-size:13px;">
                                    <option value="every_five_minutes" style="color:#000;">5 Phút/Chương</option>
                                    <option value="hourly" style="color:#000;">1 Giờ/Chương</option>
                                    <option value="twicedaily" style="color:#000;">12 Giờ/Chương</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div style="padding:20px; overflow-y:auto; flex:1;">
                        ${listHtml}
                    </div>
                    <div style="padding:16px; border-top:1px solid rgba(255,255,255,0.1); display:flex; justify-content:flex-end; gap:12px; background:rgba(0,0,0,0.2);">
                        <button onclick="handleBrainstormAction('replace')" id="bs-btn-replace" style="background:rgba(255,255,255,0.1); color:#fff; border:none; padding:10px 16px; border-radius:8px; font-weight:700; cursor:pointer;">✏️ Thay thế vào ô Sáng Tác</button>
                        <button onclick="handleBrainstormAction('autopilot')" id="bs-btn-autopilot" style="background:#4f46e5; color:#fff; border:none; padding:10px 16px; border-radius:8px; font-weight:700; cursor:pointer;">🚀 Đẩy các kịch bản vào phần Auto-Pilot</button>
                    </div>
                </div>
            `;
            document.body.appendChild(c);
        }

        window.handleBrainstormAction = async function(type) {
            const checks = document.querySelectorAll('.brainstorm-checkbox:checked');
            if(checks.length === 0) {
                showToast('Chưa chọn kịch bản nào!', 'error'); return;
            }

            if(type === 'replace') {
                if(checks.length > 1) {
                    showToast('Cảnh báo: Chỉ cho phép chọn 1 kịch bản để thay thế vào ô Sáng tác!', 'warning'); return;
                }
                const pObj = JSON.parse(decodeURIComponent(checks[0].getAttribute('data-payload')));
                let formattedPrompt = `[TÊN TRUYỆN]\n${pObj.title}\n\n[THỂ LOẠI]\n${pObj.genres}\n\n[TÓM TẮT]\n${pObj.prompt}`;
                document.getElementById('ss-prompt').value = formattedPrompt;
                document.getElementById('ss-brainstorm-modal').remove();
                showToast('✅ Đã chọn kịch bản mồi!');
                return;
            }

            if(type === 'autopilot') {
                const btn = document.getElementById('bs-btn-autopilot');
                btn.disabled = true; btn.innerHTML = '⏳ Đang lên Hàng Đợi...';
                
                const selectedPrompts = Array.from(checks).map(el => {
                    return JSON.parse(decodeURIComponent(el.getAttribute('data-payload')));
                });
                const bs_chapters_min = document.getElementById('bs-chapters-min').value;
                const bs_chapters_max = document.getElementById('bs-chapters-max').value;
                const bs_interval = document.getElementById('bs-interval').value;

                try {
                    const fd = new FormData();
                    fd.append('action', 'temply_studio_batch_autopilot_push');
                    fd.append('action_nonce', NONCE);
                    fd.append('payload', JSON.stringify({
                        prompts: selectedPrompts,
                        chapters_min: bs_chapters_min,
                        chapters_max: bs_chapters_max,
                        interval: bs_interval
                    }));
                    
                    const res = await fetch(AJAX_URL, { method: 'POST', body: fd }).then(r => r.json());
                    if(!res.success) throw new Error(res.data.message || 'Lỗi server');

                    document.getElementById('ss-brainstorm-modal').remove();
                    
                    // Hiển thị Dialog thay vì Toast để user biết cái gì vừa xảy ra
                    const successModal = document.createElement('div');
                    successModal.style.cssText = 'position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.85);backdrop-filter:blur(5px);z-index:999999;display:flex;align-items:center;justify-content:center;padding:20px;';
                    successModal.innerHTML = `
                        <div style="background:#1e293b; border:1px solid rgba(16,185,129,0.3); border-radius:16px; padding:32px; text-align:center; max-width:400px; box-shadow:0 25px 50px -12px rgba(0,0,0,0.8);">
                            <div style="font-size:48px; margin-bottom:16px;">🚀</div>
                            <h3 style="color:#10b981; margin:0 0 12px 0; font-size:20px; font-weight:800;">Đẩy Lên Auto-Pilot Thành Công!</h3>
                            <p style="color:#cbd5e1; font-size:14px; line-height:1.6; margin:0 0 24px 0;">Đã lên lịch sản xuất tự động cho <b>${selectedPrompts.length}</b> truyện vào hàng chờ. AI sẽ âm thầm phân tích và viết từng chương phía sau hệ thống.</p>
                            <div style="display:flex; gap:12px; justify-content:center;">
                                <button onclick="this.parentElement.parentElement.parentElement.remove()" style="background:rgba(255,255,255,0.1); color:#fff; border:none; padding:10px 16px; border-radius:8px; font-weight:700; cursor:pointer; flex:1;">Đóng</button>
                                <button onclick="this.parentElement.parentElement.parentElement.remove(); renderAutoPilotModal()" style="background:#4f46e5; color:#fff; border:none; padding:10px 16px; border-radius:8px; font-weight:700; cursor:pointer; flex:1;">Mở Trạm Giám Sát</button>
                            </div>
                        </div>
                    `;
                    document.body.appendChild(successModal);

                } catch(e) {
                    btn.disabled = false; btn.innerHTML = '🚀 Đẩy vào Auto-Pilot';
                    showToast('❌ Lỗi: ' + e.message, 'error');
                }
            }
        };

        window.handleBrainstormEvaluate = async function() {
            const btn = document.getElementById('bs-btn-evaluate');
            btn.disabled = true;
            const originalText = btn.innerHTML;
            btn.innerHTML = '⏳ AI đang săm soi...';
            showToast('🤖 AI đang phân tích toàn bộ kịch bản...', 'info');

            try {
                const fd = new FormData();
                fd.append('action', 'temply_studio_evaluate_prompts');
                fd.append('action_nonce', NONCE);
                fd.append('payload', JSON.stringify(window.__currentBrainstormPrompts));

                const res = await fetch(AJAX_URL, { method: 'POST', body: fd }).then(r => r.json());
                if(!res.success) throw new Error(res.data.message || 'Lỗi lấy Evaluate Prompt');

                const sys = res.data.ai_sys_prompt;
                const usr = res.data.ai_usr_prompt;
                const apiKey = res.data.gemini_key;
                const aiModel = document.getElementById('ss-ai-model').value || 'gemini-2.5-flash';

                const aiResult = await callGeminiFromBrowser(sys + "\n" + usr, apiKey, aiModel);
                
                let evals = extractJsonFromArrayText(aiResult);
                if (!evals || !Array.isArray(evals)) throw new Error('AI trả về sai định dạng.');

                evals.forEach((ev, idx) => {
                    const box = document.getElementById('bs-prompt-eval-' + idx);
                    if(box) {
                        box.innerHTML = `
                            <div style="background:rgba(217,70,239,0.08); border:1px solid rgba(217,70,239,0.2); padding:10px 12px; border-radius:8px; display:flex; gap:10px; align-items:flex-start;">
                                <div style="font-size:16px; font-weight:900; color:#d946ef; white-space:nowrap;">${ev.score}</div>
                                <div style="font-size:12px; color:#fdf4ff; line-height:1.5;">${ev.review}</div>
                            </div>
                        `;
                    }
                });
                showToast('✨ Đã chấm điểm xong!', 'success');
                btn.innerHTML = '✅ Đã Đánh Giá';
            } catch(e) {
                showToast('❌ Đánh giá lỗi: ' + e.message, 'error');
                btn.disabled = false;
                btn.innerHTML = originalText;
            }
        };

        // ==========================================
        // AUTO-PILOT QUEUE VIEWER (FRONT-END)
        // ==========================================
        window.renderAutoPilotModal = async function() {
            try {
                showToast('Đang tải dữ liệu Hàng đợi Auto-Pilot...', 'info');
                const fd = new FormData();
                fd.append('action', 'temply_studio_get_autopilot_queue');
                fd.append('action_nonce', NONCE);

                const res = await fetch(AJAX_URL, { method: 'POST', body: fd }).then(r => r.json());
                if(!res.success) throw new Error(res.data?.message || 'Lỗi lấy queue');

                const config = res.data.config;
                const queue = config?.queue || [];
                
                const c = document.createElement('div');
                c.id = 'ss-autopilot-modal';
                c.style.cssText = 'position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.85);backdrop-filter:blur(10px);z-index:999999;display:flex;align-items:center;justify-content:center;padding:20px;';
                
                let listHtml = '';
                if(queue.length === 0) {
                    listHtml = `<div style="padding:40px; text-align:center; color:#94a3b8;">Hàng đợi đang trống. Hãy dùng Gợi ý kịch bản để đẩy thêm truyện vào Lò nhé!</div>`;
                } else {
                    queue.forEach((q, idx) => {
                        const target = q.target_chapters || 20;
                        const left = q.chapters_left || target;
                        const done = target - left;
                        const pct = Math.floor((done / target) * 100);
                        let statusColor = '#94a3b8';
                        let statusText = q.status;
                        if(statusText === 'draft_outline') { statusColor = '#f59e0b'; statusText = 'Đang xếp Dàn Ý'; }
                        else if(statusText === 'writing') { statusColor = '#10b981'; statusText = 'Đang Cày Chữ'; }
                        else if(statusText === 'pending') { statusColor = '#3b82f6'; statusText = 'Đang chờ Tới Lượt'; }

                        listHtml += `
                        <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); border-radius:12px; padding:16px; margin-bottom:12px; display:flex; gap:16px; align-items:center;">
                            <div style="width:40px; height:40px; background:rgba(79,70,229,0.2); color:#818cf8; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:16px; flex-shrink:0;">
                                #${idx+1}
                            </div>
                            <div style="flex:1;">
                                <div style="font-size:15px; font-weight:800; color:#fff; margin-bottom:4px;">${q.title || 'Truyện Chờ Phân Tích'}</div>
                                <div style="display:flex; gap:8px; font-size:12px; margin-bottom:12px;">
                                    <span style="background:rgba(16,185,129,0.1); color:#10b981; padding:2px 8px; border-radius:12px;">${statusText}</span>
                                    <span style="background:rgba(255,255,255,0.1); color:#cbd5e1; padding:2px 8px; border-radius:12px;">${q.genre || 'Chưa định hình'}</span>
                                </div>
                                <div style="background:rgba(0,0,0,0.5); height:8px; border-radius:4px; overflow:hidden; position:relative;">
                                    <div style="background:linear-gradient(90deg, #4f46e5, #ec4899); position:absolute; top:0; left:0; bottom:0; width:${pct}%; transition:width 0.5s;"></div>
                                </div>
                                <div style="font-size:11px; color:#64748b; margin-top:6px; text-align:right;">Tiến độ: ${done}/${target} (${pct}%)</div>
                            </div>
                            <button onclick="handleAutoPilotRemove(${idx})" style="background:rgba(239,68,68,0.1); color:#ef4444; border:1px solid rgba(239,68,68,0.3); padding:8px; border-radius:8px; cursor:pointer;" title="Xoá truyện này khỏi hàng đợi">❌</button>
                        </div>`;
                    });
                }

                c.innerHTML = `
                    <div style="background:#1e293b; border:1px solid rgba(255,255,255,0.1); border-radius:16px; width:100%; max-width:700px; max-height:85vh; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 25px 50px -12px rgba(0,0,0,0.8);">
                        <div style="padding:20px; border-bottom:1px solid rgba(255,255,255,0.1); display:flex; justify-content:space-between; align-items:center;">
                            <h2 style="margin:0; font-size:20px; color:#fff; font-weight:800;">🚀 Trạm Giám Sát Auto-Pilot</h2>
                            <button onclick="document.getElementById('ss-autopilot-modal').remove()" style="background:transparent; border:none; color:#94a3b8; font-size:24px; cursor:pointer; line-height:1;">&times;</button>
                        </div>
                        <div style="padding:16px; background:rgba(0,0,0,0.2); border-bottom:1px solid rgba(255,255,255,0.05); display:flex; justify-content:space-between; font-size:13px; color:#cbd5e1;">
                            <div>Tốc độ cấu hình chung: <b style="color:#10b981;">${config.interval || 'every_five_minutes'}</b></div>
                            <div>Tổng đang chạy: <b style="color:#d946ef;">${queue.length} truyện</b></div>
                        </div>
                        <div style="padding:20px; overflow-y:auto; flex:1; background:#0f172a;">
                            ${listHtml}
                        </div>
                    </div>
                `;
                
                document.body.appendChild(c);
            } catch(e) {
                showToast('Lỗi: ' + e.message, 'error');
            }
        };

        window.handleAutoPilotRemove = async function(idx) {
            if(!confirm('Bạn có chắc xoá truyện này khỏi Hàng Đợi không?')) return;
            try {
                const fd = new FormData();
                fd.append('action', 'temply_studio_remove_autopilot_item');
                fd.append('action_nonce', NONCE);
                fd.append('index', idx);
                const res = await fetch(AJAX_URL, { method: 'POST', body: fd }).then(r => r.json());
                if(!res.success) throw new Error(res.data?.message || 'Lỗi server');
                showToast(res.data.message, 'success');
                document.getElementById('ss-autopilot-modal').remove();
                renderAutoPilotModal(); // re-render
            } catch(e) {
                showToast(e.message, 'error');
            }
        };

        // ==========================================
        // ACTION: Auto Detect (Autofill Title, Genre, Tone)
        // ==========================================

        // ---- Schedule / Publish Now buttons ----
        async function handleSchedule(publishNow) {
            if (!currentPostId) { showToast('Chưa có truyện để đăng!', 'error'); return; }
            
            // 1. Lưu lại các chỉnh sửa thủ công của người dùng trước
            const origContent = storyText.innerHTML;
            if (origContent) {
                document.getElementById('scrape-status').textContent = 'Đang lưu nội dung chỉnh sửa...';
                const saveFD = new FormData();
                saveFD.append('action', 'temply_studio_save_content');
                saveFD.append('action_nonce', NONCE);
                saveFD.append('post_id', currentPostId);
                saveFD.append('raw_text', origContent);
                await fetch(AJAX_URL, { method: 'POST', body: saveFD });
            }

            const dateVal = document.getElementById('ss-publish-date').value;
            const fd = new FormData();
            fd.append('action', 'temply_studio_schedule');
            fd.append('action_nonce', NONCE);
            fd.append('post_id', currentPostId);
            if (!publishNow && dateVal) {
                // Convert local datetime to MySQL format
                const d = new Date(dateVal);
                const pad = n => String(n).padStart(2, '0');
                const mysqlDate = `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`;
                fd.append('publish_date', mysqlDate);
            }
            try {
                const res = await fetch(AJAX_URL, { method: 'POST', body: fd }).then(r => r.json());
                if (res.success) {
                    showToast('✅ ' + res.data.message, 'success');
                    document.getElementById('ss-schedule-panel').style.display = 'none';
                    setStatus(publishNow ? 'Đã xuất bản truyện!' : 'Truyện đã vào lịch đăng!', 'active');
                } else {
                    showToast('❌ ' + (res.data?.message || 'Lỗi!'), 'error');
                }
            } catch(e) {
                showToast('❌ Lỗi: ' + e.message, 'error');
            }
        }

        const btnPublishNow = document.getElementById('ss-btn-publish-now');
        const btnSchedule   = document.getElementById('ss-btn-schedule');
        if (btnPublishNow) btnPublishNow.addEventListener('click', () => handleSchedule(true));
        if (btnSchedule)   btnSchedule.addEventListener('click',   () => handleSchedule(false));

    // ---- Bookmarklet receiver (postMessage from external sites) ----
    window.addEventListener('message', function(e) {
        try {
            const data = JSON.parse(e.data);
            if (data.type !== 'temply_scrape_data') return;

            // Switch to scrape tab
            if (window.switchTab) window.switchTab('scrape');

            // Fill content
            const scrapeEl = document.getElementById('scrape-content');
            if (scrapeEl) {
                scrapeEl.value = data.text || '';
                scrapeEl.dispatchEvent(new Event('input'));
            }
            // Fill title
            if (data.title) {
                const wpTitleEl = document.getElementById('scrape-wp-title');
                if (wpTitleEl) wpTitleEl.value = data.title;
            }
            // Show success toast
            if (window.showToast) {
                window.showToast('📥 Đã nhận nội dung từ bookmarklet! (' + (data.wordCount || 0) + ' từ)', 'success');
            }
            document.getElementById('scrape-status').textContent = '✅ Nội dung từ ' + (data.source || 'trang web') + ' đã được tải vào. Chọn chế độ AI và bấm xử lý!';
        } catch(e2) { /* ignore non-JSON messages */ }
    });

    // ==============================================
    // AUTO-PILOT / AGENTIC WORKFLOW SYSTEM
    // (Triggered by "Lên lịch Auto-Pilot" button in Sáng Tác panel)
    // ==============================================
    const agenticTerminal = document.getElementById('ss-agentic-terminal');
    
    function logTerminal(msg, type = 'info') {
        const line = document.createElement('div');
        line.style.marginBottom = '6px';
        if (type === 'success') { line.style.color = '#10b981'; line.textContent = '✓ ' + msg; }
        else if (type === 'error') { line.style.color = '#ef4444'; line.style.fontWeight = 'bold'; line.textContent = '✗ ' + msg; }
        else if (type === 'action') { line.style.color = '#fbbf24'; line.style.fontWeight = 'bold'; line.textContent = '> ' + msg; }
        else { line.style.color = '#d1d5db'; line.textContent = '- ' + msg; }
        agenticTerminal.appendChild(line);
        agenticTerminal.scrollTop = agenticTerminal.scrollHeight;
    }

    if (btnAutoPilot) {
        btnAutoPilot.addEventListener('click', async function() {
            // Read ALL values from the Sáng Tác panel
            const aiModel    = document.getElementById('ss-ai-model')?.value || 'gemini-2.5-flash';
            const promptStr  = document.getElementById('ss-prompt')?.value?.trim() || '';
            const tone       = document.getElementById('ss-tone')?.value || 'hùng tráng, mạnh mẽ';
            const numChapters = document.getElementById('ss-chapters')?.value || '5';
            const genre = selectedGenres.length > 0 ? selectedGenres.join(', ') : (document.querySelector('.genre-tag.active')?.dataset?.genre || 'Tu Tiên');

            btnAutoPilot.disabled = true;
            btnAutoPilot.innerHTML = '⚙️ Đang Auto-Pilot...';
            btnSplit.disabled = true;

            // Switch editor view to terminal
            storyOutput.classList.remove('visible');
            emptyState.style.display = 'none';
            agenticTerminal.innerHTML = '<div style="color:#10b981; font-weight:bold; margin-bottom:12px;">> AUTO-PILOT MODE ACTIVE — Chạy Agentic Pipeline...</div>';
            agenticTerminal.style.display = 'flex';
            setStatus('Agentic Auto-Pilot đang chạy...', 'loading');

            try {
                // STEP 1: Oracle (World Building)
                logTerminal('[1] The Oracle — Khởi tạo Bối cảnh / Thế giới...', 'info');
                let r1 = await fetch(AJAX_URL, {
                    method: 'POST', headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                    body: new URLSearchParams({action: 'temply_step_oracle', nonce: NONCE, ai_model: aiModel, genre: genre, tone: tone, keywords: promptStr})
                }).then(r => r.json());
                if (!r1.success) throw new Error(r1.data?.message || 'Lỗi Oracle');
                const worldData = r1.data.result;
                logTerminal('Thế giới đã được định hình!', 'success');

                // STEP 2: Puppet Master (Characters)
                logTerminal('[2] The Puppet Master — Đúc nhân vật...', 'info');
                let r2 = await fetch(AJAX_URL, {
                    method: 'POST', headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                    body: new URLSearchParams({action: 'temply_step_puppet', nonce: NONCE, ai_model: aiModel, world: worldData, keywords: promptStr})
                }).then(r => r.json());
                if (!r2.success) throw new Error(r2.data?.message || 'Lỗi Puppet');
                const charData = r2.data.result;
                logTerminal('Dàn nhân vật đã sẵn sàng!', 'success');

                // STEP 3: Architect (Chapter Outline)
                logTerminal(`[3] The Architect — Lên khung ${numChapters} chương...`, 'info');
                let r3 = await fetch(AJAX_URL, {
                    method: 'POST', headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                    body: new URLSearchParams({action: 'temply_step_architect', nonce: NONCE, ai_model: aiModel, world: worldData, characters: charData, num_chapters: numChapters, keywords: promptStr})
                }).then(r => r.json());
                if (!r3.success) throw new Error(r3.data?.message || 'Lỗi Architect');
                const outlineArr = r3.data.result;
                if (!Array.isArray(outlineArr) || outlineArr.length === 0) throw new Error('Dàn ý trả về rỗng.');
                logTerminal(`Chốt xong dàn ý ${outlineArr.length} chương!`, 'success');

                // STEP 4: Publisher (Create Parent Post)
                logTerminal('[4] The Publisher — Tạo bài viết gốc + ảnh bìa...', 'info');
                let r4 = await fetch(AJAX_URL, {
                    method: 'POST', headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                    body: new URLSearchParams({action: 'temply_step_create_story', nonce: NONCE, ai_model: aiModel, world: worldData, characters: charData, genre: genre, tone: tone, keywords: promptStr})
                }).then(r => r.json());
                if (!r4.success) throw new Error(r4.data?.message || 'Lỗi Publisher');
                const truyenId = r4.data.truyen_id;
                logTerminal(`Truyện gốc đã tạo: "${r4.data.title}" (ID: ${truyenId})`, 'success');

                // STEP 5: Ghostwriter Loop
                logTerminal(`[5] The Ghostwriter — Bắt đầu viết ${outlineArr.length} chương...`, 'action');
                for (let i = 0; i < outlineArr.length; i++) {
                    const chapMeta = outlineArr[i];
                    logTerminal(`Đang viết Chương ${chapMeta.chap_num}: "${chapMeta.title}"...`, 'info');
                    let rChap = await fetch(AJAX_URL, {
                        method: 'POST', headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                        body: new URLSearchParams({
                            action: 'temply_step_write_chapter', nonce: NONCE, ai_model: aiModel,
                            truyen_id: truyenId, chap_num: chapMeta.chap_num, chap_title: chapMeta.title, summary: chapMeta.summary,
                            world: worldData, characters: charData, genre: genre, tone: tone, keywords: promptStr, custom_comments: '',
                            is_final_chapter: (i === outlineArr.length - 1 ? 1 : 0)
                        })
                    }).then(r => r.json());
                    if (!rChap.success) {
                        logTerminal(`Lỗi chương ${chapMeta.chap_num}: ${rChap.data?.message}. Bỏ qua & tiếp tục.`, 'error');
                    } else {
                        logTerminal(`✓ Xong: "${rChap.data.title}"`, 'success');
                    }
                }

                logTerminal(`\n🎉 AUTO-PILOT HOÀN TẤT! Truyện ID ${truyenId} đã có ${outlineArr.length} chương trên website.`, 'action');
                showToast('🤖 Auto-Pilot hoàn tất! Kiểm tra truyện mới trên website.', 'success');
                setStatus('Auto-Pilot hoàn tất!', 'active');

            } catch(e) {
                logTerminal('LỖI: ' + e.message, 'error');
                showToast('❌ ' + e.message, 'error');
                setStatus('Lỗi Auto-Pilot', '');
            } finally {
                btnAutoPilot.disabled = false;
                btnAutoPilot.innerHTML = '🤖 Lên lịch Auto-Pilot';
                btnSplit.disabled = false;
            }
        });
    }
    
    })(); // End main IIFE containing Story Studio logic
    </script>

    <!-- Bookmarklet Install Guide -->
    <div id="bookmarklet-guide" style="display:none; position:fixed; top:0; left:0; right:0; bottom:0; background:rgba(0,0,0,0.8); z-index:9999; align-items:center; justify-content:center;">
        <div style="background:#1e1b4b; border:1px solid rgba(99,102,241,0.4); border-radius:16px; max-width:560px; width:90%; padding:28px; max-height:90vh; overflow-y:auto;">
            <h2 style="color:#a5b4fc; font-size:18px; margin-bottom:6px;">🔖 Cài Bookmarklet Cào Truyện</h2>
            <p style="color:#6b7280; font-size:13px; margin-bottom:20px;">Bookmarklet giúp anh cào bất kỳ trang truyện nào (kể cả Cloudflare) bằng 1 cú click.</p>

            <div style="margin-bottom:16px;">
                <p style="color:#e2e8f0; font-size:13px; font-weight:600; margin-bottom:8px;">📱 Cách 1: Kéo link này vào Bookmark Bar</p>
                <a id="bookmarklet-drag-link"
                   href="javascript:(function(){var s=document.createElement('script');s.src='https://doctieuthuyet.com/?temply_bookmarklet=1&t='+Date.now();document.body.appendChild(s);})();"
                   style="display:inline-block; padding:10px 16px; background:linear-gradient(135deg,#6366f1,#8b5cf6); color:#fff; border-radius:8px; text-decoration:none; font-weight:700; font-size:14px; cursor:grab;"
                   draggable="true">
                    🕷️ Temply Cào Truyện
                </a>
                <p style="color:#6b7280; font-size:11px; margin-top:6px;">← Kéo cái này vào thanh bookmark của trình duyệt</p>
            </div>

            <div style="margin-bottom:20px;">
                <p style="color:#e2e8f0; font-size:13px; font-weight:600; margin-bottom:8px;">📋 Cách 2 (Safari/iOS): Copy rồi thêm bookmark thủ công</p>
                <div style="background:#0f172a; border-radius:8px; padding:12px; font-family:monospace; font-size:10px; color:#6ee7b7; word-break:break-all; max-height:120px; overflow-y:auto;" id="bookmarklet-code">Đang tạo code...</div>
                <button onclick="navigator.clipboard.writeText(document.getElementById('bookmarklet-code').textContent).then(()=>alert('Đã copy! Giờ vào Safari > Bookmarks > Edit > thay URL bằng code vừa copy.'))" style="margin-top:8px; padding:6px 12px; border-radius:6px; border:none; background:#374151; color:#e2e8f0; font-size:12px; cursor:pointer;">📋 Copy Code</button>
            </div>

            <div style="background:rgba(16,185,129,0.08); border:1px solid rgba(16,185,129,0.2); border-radius:8px; padding:12px; margin-bottom:16px; font-size:12px; color:#6ee7b7;">
                <strong>Cách dùng sau khi cài:</strong><br>
                1. Vào trang truyện muốn cào (ví dụ meokammap.com)<br>
                2. Bấm bookmark "🕷️ Temply Cào Truyện"<br>
                3. Studio tự động mở và nhận nội dung ✅
            </div>

            <button onclick="document.getElementById('bookmarklet-guide').style.display='none'" style="width:100%; padding:10px; border-radius:8px; border:none; background:#374151; color:#e2e8f0; font-family:inherit; cursor:pointer;">Đóng</button>
        </div>
    </div>

    <script>
    // Generate bookmarklet code
    (function() {
        var studioUrl = '<?php echo esc_js(get_permalink(get_page_by_path("story-studio"))); ?>';
        if (!studioUrl || studioUrl === 'false') studioUrl = '<?php echo esc_js(home_url("/story-studio/")); ?>';

        var code = `javascript:(function(){
var title=document.querySelector('h1,#tenChapter,.truyen-chapter-title')?.innerText||document.title;
var selectors=['#noi_dung_truyen','#chapter-c','.chapter-c','#box_doc','.chapter-content','.story-content','.content-story','article','.content','main'];
var text='';
for(var i=0;i<selectors.length;i++){var el=document.querySelector(selectors[i]);if(el&&el.innerText&&el.innerText.length>300){text=el.innerText.trim();break;}}
if(!text)text=document.body.innerText.trim();
text=text.slice(0,50000);
var words=text.split(/\s+/).filter(Boolean).length;
var w=window.open('${studioUrl}?from_bookmarklet=1','_blank');
var tries=0;
var send=setInterval(function(){
tries++;
try{w.postMessage(JSON.stringify({type:'temply_scrape_data',text:text,title:title,source:location.hostname,wordCount:words}),'${studioUrl.replace(/\/[^/]*$/, '')}');}catch(e){}
if(tries>8)clearInterval(send);
},1000);
})();`;

        document.getElementById('bookmarklet-code').textContent = code;
        var link = document.getElementById('bookmarklet-drag-link');
        if (link) link.href = code.replace(/\n/g, ' ').replace(/\s+/g, ' ');
    })();
    </script>

</body>
</html>
<?php // No get_footer() - standalone page ?>
