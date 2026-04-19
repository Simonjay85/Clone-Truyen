<?php get_header(); ?>


<style>
/* ── PAGE TEMPLATE STYLES ── */
.pg-main { background: #fff; min-height: 60vh; padding-bottom: 80px; }

/* Hero */
.pg-hero { position: relative; width: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; overflow: hidden; padding: 80px 16px 48px; text-align: center; background: linear-gradient(135deg, #eef2ff 0%, #f5f3ff 100%); }
.pg-hero-bg { position: absolute; inset: 0; width: 100%; height: 100%; }
.pg-hero-bg img { width: 100%; height: 100%; object-fit: cover; filter: blur(20px); opacity: 0.35; transform: scale(1.1); }
.pg-hero-bg-overlay { position: absolute; inset: 0; background: linear-gradient(to top, rgba(248,249,250,0.95), rgba(248,249,250,0.5) 50%, transparent); }
.pg-hero-content { position: relative; z-index: 10; max-width: 760px; }
.pg-hero-badge { display: inline-flex; align-items: center; gap: 6px; padding: 6px 16px; border-radius: 999px; background: rgba(255,255,255,0.6); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.4); font-size: 12px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; color: #374151; margin-bottom: 20px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
.pg-hero-badge .material-symbols-outlined { font-size: 16px; }
.pg-hero-title { font-size: clamp(1.8rem, 5vw, 2.8rem); font-weight: 900; color: #111827; line-height: 1.2; margin: 0 0 12px; }
.pg-hero-date { font-size: 14px; color: #6b7280; font-weight: 500; display: flex; align-items: center; justify-content: center; gap: 6px; }
.pg-hero-date .material-symbols-outlined { font-size: 14px; }

/* Content Card */
.pg-card-wrap { width: 98%; max-width: 100%; margin: -40px auto 0; position: relative; z-index: 20; padding: 0 16px; box-sizing: border-box; }
.pg-card { background: #f8f9fa; border-radius: 32px; padding: clamp(24px, 5vw, 64px); box-shadow: 0 20px 60px rgba(0,0,0,0.08), 0 1px 0 rgba(0,0,0,0.04); border: 1px solid rgba(0,0,0,0.06); }

/* Prose - typography for WP content */
.pg-prose { max-width: 1100px; margin: 0 auto; font-size: 17px; line-height: 1.8; color: #000000; font-family: 'Be Vietnam Pro', system-ui, sans-serif; }
.pg-prose p { margin: 0 0 1.25em; color: #000000; text-align: justify; }
.pg-prose h1 { font-size: 2em; font-weight: 900; color: #000000; margin: 0 0 0.75em; line-height: 1.25; }
.pg-prose h2 { font-size: 1.5em; font-weight: 800; color: #000000; margin: 2em 0 0.75em; line-height: 1.3; padding-bottom: 0.4em; border-bottom: 2px solid #e5e7eb; }
.pg-prose h3 { font-size: 1.2em; font-weight: 700; color: #000000; margin: 1.5em 0 0.5em; }
.pg-prose h4 { font-size: 1em; font-weight: 700; color: #000000; margin: 1.25em 0 0.5em; }
.pg-prose ul { list-style: disc; padding-left: 1.75em; margin: 0 0 1.25em; }
.pg-prose ol { list-style: decimal; padding-left: 1.75em; margin: 0 0 1.25em; }
.pg-prose li { margin-bottom: 0.5em; color: #000000; }
.pg-prose a { color: #4f46e5; text-decoration: none; font-weight: 500; }
.pg-prose a:hover { text-decoration: underline; }
.pg-prose strong, .pg-prose b { font-weight: 700; color: #000000; }
.pg-prose blockquote { border-left: 4px solid #4f46e5; margin: 1.5em 0; padding: 0.75em 1.25em; background: #f5f3ff; border-radius: 0 8px 8px 0; color: #374151; font-style: italic; }
.pg-prose img { max-width: 100%; border-radius: 16px; }
.pg-prose hr { border: none; border-top: 1px solid #e5e7eb; margin: 2em 0; }
.pg-prose table { width: 100%; border-collapse: collapse; margin: 1.5em 0; }
.pg-prose th, .pg-prose td { padding: 10px 14px; border: 1px solid #e5e7eb; text-align: left; }
.pg-prose th { background: #f3f4f6; font-weight: 700; color: #374151; }
.pg-prose code { background: #f4f4f5; padding: 2px 6px; border-radius: 4px; font-size: 0.9em; color: #e11d48; font-family: monospace; }

/* Custom Contact Card */
.pg-contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; align-items: start; }
@media (max-width: 700px) { .pg-contact-grid { grid-template-columns: 1fr; } }
.pg-contact-left { background: linear-gradient(135deg, #2563eb 0%, #4f46e5 100%); padding: 32px; border-radius: 24px; color: #fff; box-shadow: 0 20px 40px rgba(79,70,229,0.25); }
.pg-contact-left .material-symbols-outlined { font-size: 48px; margin-bottom: 16px; opacity: 0.9; display: block; }
.pg-contact-left h2 { font-size: 1.6em; font-weight: 900; margin: 0 0 12px; }
.pg-contact-left p { color: #bfdbfe; font-size: 15px; line-height: 1.7; margin: 0 0 24px; }
.pg-contact-info-item { display: flex; align-items: center; gap: 14px; background: rgba(255,255,255,0.1); padding: 14px 16px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.2); margin-bottom: 12px; }
.pg-contact-info-item .material-symbols-outlined { font-size: 22px; background: rgba(255,255,255,0.2); width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.pg-contact-info-label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #93c5fd; margin-bottom: 4px; }
.pg-contact-info-value { font-weight: 700; font-size: 16px; }
.pg-contact-right { background: #fff; padding: 32px; border-radius: 24px; border: 1px solid #f3f4f6; box-shadow: 0 4px 24px rgba(0,0,0,0.04); }
.pg-contact-right h3 { font-size: 1.1em; font-weight: 800; color: #1f2937; margin: 0 0 24px; }
.pg-form-group { margin-bottom: 18px; }
.pg-form-group label { display: block; font-size: 13px; font-weight: 700; color: #374151; margin-bottom: 8px; }
.pg-form-group input, .pg-form-group textarea { width: 100%; background: #f9fafb; border: 1.5px solid #e5e7eb; border-radius: 12px; padding: 12px 16px; font-size: 15px; color: #374151; outline: none; transition: border-color 0.2s, background 0.2s; font-family: inherit; }
.pg-form-group input:focus, .pg-form-group textarea:focus { border-color: #4f46e5; background: #fff; }
.pg-form-group textarea { min-height: 120px; resize: vertical; }
.pg-form-submit { width: 100%; background: #4f46e5; color: #fff; border: none; border-radius: 12px; padding: 14px; font-size: 15px; font-weight: 700; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; transition: background 0.2s; font-family: inherit; }
.pg-form-submit:hover { background: #4338ca; }
</style>

<main class="pg-main">
    <?php if(have_posts()): while(have_posts()): the_post(); ?>

    <!-- Hero -->
    <div class="pg-hero">
        <?php if(has_post_thumbnail()): ?>
        <div class="pg-hero-bg">
            <img src="<?php echo get_the_post_thumbnail_url(get_the_ID(), 'full'); ?>" alt="Cover" width="1200" height="400" loading="eager" fetchpriority="high">
            <div class="pg-hero-bg-overlay"></div>
        </div>
        <?php endif; ?>
        <div class="pg-hero-content">
            <div class="pg-hero-badge">
                <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg> Chuyên mục Hệ thống
            </div>
            <h1 class="pg-hero-title"><?php the_title(); ?></h1>
            <p class="pg-hero-date">
                <svg width="13" height="13" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                Cập nhật lần cuối: <?php echo get_the_modified_date('d/m/Y'); ?>
            </p>
        </div>
    </div>

    <!-- Content Card -->
    <div class="pg-card-wrap">
        <div class="pg-card">
            <?php
                $post_slug = get_post_field('post_name', get_post());
                if($post_slug === 'lien-he-quang-cao' || $post_slug === 'lien-he'):
            ?>
            <!-- Custom Contact Layout -->
            <div class="pg-contact-grid">
                <div class="pg-contact-left">
                    <svg style="display:block;margin-bottom:16px;opacity:.9" width="40" height="40" fill="none" viewBox="0 0 24 24" stroke="#fff" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M11 5.882V19.24a1.76 1.76 0 01-3.417.592l-2.147-6.15M18 13a3 3 0 100-6M5.436 13.683A4.001 4.001 0 017 6h1.832c4.1 0 7.625-1.234 9.168-3v14c-1.543-1.766-5.067-3-9.168-3H7a3.988 3.988 0 01-1.564-.317z"/></svg>
                    <h2>Hợp tác &amp; Quảng cáo</h2>
                    <p>Đưa thương hiệu của bạn tiếp cận hàng triệu độc giả trung thành mỗi tháng trên hệ thống <strong>Đọc Tiểu Thuyết</strong>. Chúng tôi mang đến những giải pháp hiển thị độ chuyển đổi cao nhất.</p>
                    <div class="pg-contact-info-item">
                        <svg style="flex-shrink:0;width:20px;height:20px;background:rgba(255,255,255,.2);border-radius:50%;padding:8px;box-sizing:content-box" fill="none" viewBox="0 0 24 24" stroke="#fff" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                        <div>
                            <div class="pg-contact-info-label">Email liên hệ</div>
                            <div class="pg-contact-info-value">ads@doctieuthuyet.com</div>
                        </div>
                    </div>
                    <div class="pg-contact-info-item">
                        <svg style="flex-shrink:0;width:20px;height:20px;background:rgba(255,255,255,.2);border-radius:50%;padding:8px;box-sizing:content-box" fill="none" viewBox="0 0 24 24" stroke="#fff" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M9.172 9.172L5.636 5.636m3.536 9.192l-3.536 3.536M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-5 0a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
                        <div>
                            <div class="pg-contact-info-label">Telegram / Zalo</div>
                            <div class="pg-contact-info-value">@DTT_Support_Ads</div>
                        </div>
                    </div>
                </div>
                <div class="pg-contact-right">
                    <h3>Gửi thông điệp ngay</h3>
                    <form onsubmit="event.preventDefault(); alert('Cảm ơn bạn! Yêu cầu liên hệ đã được gửi.');">
                        <div class="pg-form-group">
                            <label>Tên công ty / Cá nhân *</label>
                            <input type="text" required placeholder="VD: Công ty TNHH Truyền Thông ACB">
                        </div>
                        <div class="pg-form-group">
                            <label>Số điện thoại / Zalo *</label>
                            <input type="text" required placeholder="Số điện thoại liên lạc">
                        </div>
                        <div class="pg-form-group">
                            <label>Nội dung hợp tác muốn triển khai *</label>
                            <textarea required placeholder="VD: Đặt banner trang chủ, thông cáo báo chí, pop-up..."></textarea>
                        </div>
                        <button type="submit" class="pg-form-submit">
                            Gửi Yêu Cầu Hợp Tác <span class="material-symbols-outlined" style="font-size:18px">send</span>
                        </button>
                    </form>
                </div>
            </div>
            <?php else: ?>
            <!-- Standard WP content with prose styles -->
            <div class="pg-prose">
                <?php the_content(); ?>
            </div>
            <?php endif; ?>
        </div>
    </div>

    <?php endwhile; endif; ?>
</main>

<?php get_footer(); ?>
