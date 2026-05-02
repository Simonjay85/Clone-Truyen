<?php get_header(); ?>
<?php if (have_posts()) : while (have_posts()) : the_post(); ?>
<?php
// Lấy Truyen ID từ meta của chương
$truyen_id = get_post_meta(get_the_ID(), '_truyen_id', true);
$truyen_title = $truyen_id ? get_the_title($truyen_id) : 'Truyện Không Rõ';
$truyen_link = $truyen_id ? get_permalink($truyen_id) : '#';
$facebook_group_url = esc_url(get_option('tehi_facebook_group_url', ''));
$unlock_guide_url   = esc_url(get_option('tehi_unlock_guide_url', ''));

// Lấy danh sách toàn bộ chương của truyện để làm nút Prev/Next
$chapters = [];
if ($truyen_id) {
    $chapters = get_posts([
        'post_type'      => 'chuong',
        'posts_per_page' => -1,
        'meta_key'       => '_truyen_id',
        'meta_value'     => $truyen_id,
        'orderby'        => 'ID', 
        'order'          => 'ASC'
    ]);
}

$prev_chap = null;
$next_chap = null;
$curr_id = get_the_ID();

// Tìm vị trí của chương hiện tại
for($i=0; $i<count($chapters); $i++) {
    if($chapters[$i]->ID == $curr_id) {
        if($i > 0) $prev_chap = $chapters[$i-1];
        if($i < count($chapters)-1) $next_chap = $chapters[$i+1];
        break;
    }
}
?>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,700;1,400;1,500&display=swap" rel="stylesheet">
<style>
/* Reading Mode UI */
header.mkm-header { display: none !important; }
.r-wrap { width: 100% !important; display: block !important; clear: both !important; background: #FFFDF0; min-height: 100vh; font-family: 'Lora', Georgia, serif; position: relative; }
.r-hdr { background: #fff; height: 60px; padding: 0 16px; border-bottom: 1px solid #e5e7eb; display:flex; justify-content:space-between; align-items:center; position: sticky; top: 0; z-index: 50; box-shadow: 0 1px 3px rgba(0,0,0,0.02); }
.r-hdr-left { display: flex; align-items: center; gap: 12px; font-family: ui-sans-serif, system-ui, sans-serif; }
.r-back-btn { display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 50%; color: #374151; text-decoration: none; background: #f3f4f6; transition: background .2s; }
.r-back-btn:hover { background: #e5e7eb; }
.r-story-name { font-size: 15px; font-weight: 700; color: #111827; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 250px; text-decoration: none; }
.r-story-name:hover { color: #6366f1; text-decoration: underline; }

.r-hdr-right { display: flex; gap: 8px; }
.r-icon-btn { display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 8px; border: none; background: #fff; color: #374151; cursor: pointer; transition: background .2s; font-size: 18px; }
.r-icon-btn:hover { background: #f3f4f6; }

/* Content Area */
.r-container { max-width: 800px; margin: 20px auto; padding: 40px 20px 80px 20px; background: #FFFDF0; border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); }
.r-title { text-align: center; font-size: 26px; font-weight: 700; color: #2d1f0e; margin-bottom: 24px; line-height: 1.4; font-family: 'Lora', Georgia, serif; }
.r-content { font-size: 20px; line-height: 1.9; color: #2d2116; text-align: justify; word-wrap: break-word; font-family: 'Lora', Georgia, serif; letter-spacing: 0.01em; }
.r-content p { margin-bottom: 1.5em; }
.r-content img { border-radius: 10px !important; box-shadow: 0 4px 12px rgba(0,0,0,0.08); display: block; margin: 0 auto; max-width: 100%; width: 100%; height: auto; }

/* Navigation Inline */
.r-nav { display: flex; justify-content: center; align-items: center; gap: 12px; margin-top: 40px; padding-top: 30px; border-top: 1px dashed #d1d5db; font-family: ui-sans-serif, system-ui, sans-serif; }
.r-nav a { padding: 10px 20px; border-radius: 20px; font-weight: 600; text-decoration: none; display:flex; align-items:center; justify-content:center; gap:8px; transition:all .2s; font-size: 14px;}
.r-nav-prev, .r-nav-next { background: #f97316; color: #fff; flex: 1; max-width: 200px; }
.r-nav-prev.dis, .r-nav-next.dis { background: #e5e7eb; color: #9ca3af; pointer-events: none; }
.r-nav-list { background: #10b981; color: #fff; padding: 10px 16px; border-radius: 20px; }
.r-nav a:hover { opacity: 0.9; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }

/* Floating Actions */
.r-fab-top { position: fixed; bottom: 100px; left: 30px; width: 44px; height: 44px; background: #111827; color: #fff; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 20px; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border: none; opacity: 0; pointer-events: none; transition: opacity 0.3s; z-index: 100;}
.r-fab-top.show { opacity: 1; pointer-events: all; }

/* Mobile Navigation Bar */
.r-mob-nav { display: none; position: fixed; bottom: 0; left: 0; width: 100%; background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); border-top: 1px solid #e5e7eb; z-index: 190; padding-bottom: env(safe-area-inset-bottom); box-shadow: 0 -4px 10px rgba(0,0,0,0.05); }
.r-mob-nav-inner { display: flex; justify-content: space-between; align-items: center; height: 60px; padding: 0 10px; }
.r-mob-nav-item { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; color: #6b7280; text-decoration: none; font-size: 10px; gap: 4px; border: none; background: none; }
.r-mob-nav-item.active { color: #6366f1; }
.r-mob-nav-item svg { width: 22px; height: 22px; }
.r-mob-nav-item.dis { opacity: 0.4; pointer-events: none; }
.r-mob-nav-center { width: auto; margin: -20px 5px 0 5px; padding: 6px 16px; background: #fff; border: 1px solid #e0e7ff; color: #6366f1; border-radius: 20px; font-weight: 700; display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 11px; box-shadow: 0 4px 6px rgba(99,102,241,0.1); cursor:pointer;}
.r-mob-nav-center span.chap-progress { color: #9ca3af; font-weight: 500; font-size: 9px; margin-top:2px; }

/* FAB & Speed Dial */
.r-speed-dial { position: fixed; right: 20px; bottom: 85px; z-index: 195; display: flex; flex-direction: column; align-items: flex-end; gap: 12px; transition: all 0.3s; display:none; }
.r-sd-actions { display: flex; flex-direction: column; gap: 12px; align-items: flex-end; opacity: 0; pointer-events: none; transform: translateY(20px); transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
.r-speed-dial.open .r-sd-actions { opacity: 1; pointer-events: auto; transform: translateY(0); }
.r-sd-btn { display: flex; align-items: center; gap: 10px; background: #fff; border: 1px solid #e5e7eb; padding: 6px 12px 6px 6px; border-radius: 30px; color: #374151; font-size: 13px; font-weight: 600; box-shadow: 0 4px 10px rgba(0,0,0,0.08); cursor: pointer; white-space:nowrap; }
.r-sd-icon { width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 1px solid #e5e7eb; background:#f9fafb; margin-right:4px;}
.r-sd-fab { width: 48px; height: 48px; border-radius: 50%; background: #9253ff; color: #fff; cursor: pointer; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(146, 83, 255, 0.4); border: none; font-size: 24px; transition: transform 0.3s; }
.r-speed-dial.open .r-sd-fab { transform: rotate(45deg); background: #374151; box-shadow: 0 4px 12px rgba(0,0,0,0.2); }

@media (max-width: 800px) {
    .r-nav { display: none !important; }
    .r-mob-nav { display: block; }
    .r-speed-dial { display: flex; }
    .r-container { padding: 10px 0 90px 0 !important; margin: 0; border-radius: 0; box-shadow: none; }
    .r-content { padding: 0 5px; }
    .r-content img { border-radius: 0 !important; width: 100%; max-width: 100%; margin-bottom: 0 !important; }
    figure.wp-block-image { margin: 0 !important; }
}

/* Modals */
.r-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 100; display: none; opacity: 0; transition: opacity 0.3s; }
.r-modal { position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%) scale(0.95); background: #fff; width: 90%; max-width: 400px; border-radius: 16px; z-index: 101; display: none; opacity: 0; transition: all 0.3s; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1); overflow:hidden; font-family: ui-sans-serif, system-ui, sans-serif;}
.r-modal-hdr { padding: 16px 20px; border-bottom: 1px solid #e5e7eb; display: flex; justify-content: space-between; align-items: center; background: #f9fafb; font-weight: 700; color: #111827; }
.r-modal-close { background: none; border: none; font-size: 24px; color: #6b7280; cursor: pointer; line-height: 1; }
.r-modal-body { padding: 20px; max-height: 60vh; overflow-y: auto; }
.r-show .r-overlay, .r-show .r-modal { display: block; }
.r-show.r-active .r-overlay { opacity: 1; }
.r-show.r-active .r-modal { opacity: 1; transform: translate(-50%, -50%) scale(1); }

/* TOC Styles */
.r-toc-list { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; }
.r-toc-item { padding: 12px; border-radius: 8px; border: 1px solid #f3f4f6; text-decoration: none; color: #374151; font-size: 14px; font-weight: 500; transition: background .2s; min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; display: block; }
.r-toc-item:hover { background: #f9fafb; border-color: #e5e7eb; }
.r-toc-item.active { background: #e0e7ff; border-color: #c7d2fe; color: #4f46e5; font-weight: 600; }
.r-toc-search { width: 100%; padding: 10px 16px; border: 1px solid #e5e7eb; border-radius: 8px; margin-bottom: 16px; outline: none; font-size: 14px; }

/* Settings Styles */
.r-set-row { margin-bottom: 20px; }
.r-set-label { font-size: 13px; font-weight: 600; color: #6b7280; margin-bottom: 10px; display: block; text-transform: uppercase; letter-spacing: 0.5px; }
.r-set-group { display: flex; gap: 12px; }
.r-set-btn { flex: 1; padding: 10px; border: 1px solid #e5e7eb; border-radius: 8px; background: #fff; cursor: pointer; font-weight: 600; font-size: 14px; color: #374151; transition: all .2s; }
.r-set-btn:hover { border-color: #9ca3af; }
.r-bg-theme1 { background: #f5f3f7 !important; color: #111827 !important; } /* Light Purple Pink background */
.r-bg-theme2 { background: #000000 !important; color: #e5e7eb !important; border-color: #374151 !important;}
.r-bg-theme2 .r-container { background: #111827 !important; box-shadow: none !important; border: 1px solid #1f2937; }
.r-bg-theme2 .r-hdr { background: #111827 !important; border-bottom-color: #1f2937 !important; }
.r-bg-theme2 .r-hdr .r-story-name { color: #e5e7eb !important; }
.r-bg-theme2 .r-icon-btn, .r-bg-theme2 .r-back-btn, .r-bg-theme2 .r-sd-btn { background: #1f2937 !important; color: #e5e7eb !important; border-color: #374151 !important; }
.r-bg-theme2 .r-title { color: #f3f4f6 !important; }
.r-bg-theme3 { background: #edf2f7 !important; color: #111827 !important; }

/* Chapter Lock */
.r-hidden-content { display: none; }
.r-lock-box { background: #f8faff; border: 1px solid #e0e7ff; border-radius: 12px; padding: 24px; text-align: center; margin: 30px 0; font-family: ui-sans-serif, system-ui, sans-serif; }
.r-bg-theme2 .r-lock-box { background: #1f2937; border-color: #374151; }
.r-lock-req { font-size: 12px; color: #6366f1; font-weight: 600; text-transform: uppercase; margin-bottom: 8px; display: block; }
.r-lock-title { font-size: 20px; font-weight: 700; color: #111827; margin-bottom: 8px; }
.r-bg-theme2 .r-lock-title { color: #f3f4f6; }
.r-lock-desc { font-size: 14px; color: #4b5563; margin-bottom: 20px; line-height: 1.5; }
.r-bg-theme2 .r-lock-desc { color: #9ca3af; }
.r-lock-btn { background: #3b82f6; color: #fff; border: none; padding: 12px 24px; border-radius: 8px; font-weight: 600; font-size: 15px; cursor: pointer; transition: all 0.2s; display: inline-block; text-decoration: none; box-shadow: 0 4px 12px rgba(59,130,246,0.3); }
.r-lock-btn:hover { background: #2563eb; transform: translateY(-2px); }
.r-lock-btn.disabled { background: #e5e7eb; color: #6b7280; cursor: not-allowed; box-shadow: none; pointer-events: none; }
.r-lock-link { display: block; margin-top: 16px; font-size: 13px; color: #3b82f6; text-decoration: none; font-weight: 500; }
.r-lock-link:hover { text-decoration: underline; }

/* Mobile Adjustments */
@media (max-width: 640px) {
    .r-story-name { max-width: 180px; font-size: 14px;}
    .r-title { font-size: 22px; margin-bottom: 20px;}
    .r-content { font-size: 20px; line-height: 1.6; }
    .r-container { padding: 20px 15px 80px 15px; }
    .r-nav { gap: 8px; }
    .r-nav a { padding: 10px 12px; font-size: 13px; }
    .r-nav-prev::before { content: '← '; }
    .r-nav-next::after { content: ' →'; }
    .r-nav-prev span, .r-nav-next span { display: none; }
}
/* Paragraph Comments */
.r-para-wrap { position: relative; }
.r-para-wrap:hover .r-para-btn { opacity: 1; }
.r-para-btn { opacity: 0; position: absolute; right: -44px; top: 2px; width: 32px; height: 32px; border-radius: 50%; background: #6366f1; border: none; color: #fff; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: opacity 0.2s; box-shadow: 0 2px 6px rgba(99,102,241,0.3); z-index: 10; }
@media (max-width: 800px) { 
    .r-para-btn { opacity: 0; right: 0; top: -20px; left: auto; width: 26px; height: 26px; font-size: 11px; } 
}
.r-cmt-count { position: absolute; right: -46px; top: 36px; background: #ef4444; color: #fff; font-size: 10px; font-weight: 700; border-radius: 10px; padding: 1px 5px; font-family: ui-sans-serif, sans-serif; display: none; }
@media (max-width: 800px) {
    .r-cmt-count { right: 0; top: 8px; }
}
/* Comments Panel */
.r-cmt-panel { position: fixed; right: 0; top: 0; height: 100%; width: 360px; background: #fff; z-index: 200; box-shadow: -8px 0 24px rgba(0,0,0,0.1); transform: translateX(100%); transition: transform 0.3s ease; font-family: ui-sans-serif, system-ui, sans-serif; display: flex; flex-direction: column; }
.r-cmt-panel.open { transform: translateX(0); }
.r-cmt-panel-hdr { padding: 20px; border-bottom: 1px solid #e5e7eb; display: flex; justify-content: space-between; align-items: center; background: #f9fafb; }
.r-cmt-panel-title { font-weight: 700; color: #111827; font-size: 15px; }
.r-cmt-close { background: none; border: none; font-size: 24px; color: #6b7280; cursor: pointer; }
.r-cmt-body { flex: 1; overflow-y: auto; padding: 20px; }
.r-cmt-form { padding: 16px 20px; border-top: 1px solid #e5e7eb; }
.r-cmt-form textarea { width: 100%; border: 1px solid #e5e7eb; border-radius: 8px; padding: 10px; font-size: 14px; resize: none; outline: none; font-family: inherit; }
.r-cmt-form-btns { display: flex; justify-content: flex-end; gap: 8px; margin-top: 8px; }
.r-cmt-submit { background: #6366f1; color: #fff; border: none; padding: 8px 16px; border-radius: 8px; font-weight: 600; font-size: 14px; cursor: pointer; }
.r-cmt-item { padding: 12px 0; border-bottom: 1px solid #f3f4f6; }
.r-cmt-item:last-child { border: none; }
.r-cmt-author { font-weight: 700; font-size: 13px; color: #111827; }
.r-cmt-date { font-size: 11px; color: #9ca3af; margin-left: 8px; }
.r-cmt-text { font-size: 14px; color: #374151; margin-top: 4px; line-height: 1.5; }
.r-cmt-empty { text-align: center; padding: 40px 20px; color: #9ca3af; font-size: 14px; }
.r-cmt-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.3); z-index: 199; display:none; }
.r-cmt-overlay.open { display: block; }
</style>

<div class="r-wrap" id="rWrap">
    <!-- Header -->
    <div class="r-hdr" id="rHdr">
        <div class="r-hdr-left">
            <a href="<?php echo esc_url($truyen_link); ?>" class="r-back-btn" title="Quay lại Truyện">
                <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"/></svg>
            </a>
            <a href="<?php echo esc_url($truyen_link); ?>" class="r-story-name" title="<?php echo esc_attr($truyen_title); ?>">
                <?php echo esc_html($truyen_title); ?>
            </a>
        </div>
        <div class="r-hdr-right">
            <button class="r-icon-btn" onclick="appModal.open('tocModal')" title="Mục lục">
                <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"/></svg>
            </button>
            <button class="r-icon-btn" onclick="appModal.open('setModal')" title="Cài đặt">
                <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
            </button>
        </div>
    </div>

    <!-- Reading Area -->
    <div class="r-container">
        <h1 class="r-title"><?php the_title(); ?></h1>
        
        <div class="r-nav" style="margin-top:0; border:none; padding:0; margin-bottom:30px;">
            <a href="<?php echo $prev_chap ? get_permalink($prev_chap->ID) : '#'; ?>" class="r-nav-prev <?php echo $prev_chap ? '' : 'dis'; ?>"><span>Chương trước</span></a>
            <a href="javascript:void(0)" onclick="appModal.open('tocModal')" class="r-nav-list"><svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"/></svg></a>
            <a href="<?php echo $next_chap ? get_permalink($next_chap->ID) : '#'; ?>" class="r-nav-next <?php echo $next_chap ? '' : 'dis'; ?>"><span>Chương sau</span></a>
        </div>

        <div class="r-content" id="rContent">
            <?php 
            // Render nội dung với hỗ trợ Bình luận Theo Đoạn
            $raw_content = get_the_content();
            $paragraphs = preg_split('/(<\/p>\s*<p[^>]*>|<br\s*\/?><br\s*\/?>)/i', $raw_content);
            $p_idx = 0;
            
            // Logic Khoá Chương
            $is_locked = get_post_meta(get_the_ID(), '_is_locked', true); 
            if ($is_locked === '') $is_locked = true; // Bật khoá mặc định (có thể đổi thành false tuỳ logic)
            $lock_index = 2; // Số đoạn hiển thị trước khi khoá
            
            foreach ($paragraphs as $ptext) {
                $ptext = trim($ptext);
                if (empty($ptext)) continue;
                // Ensure wrapped in <p>
                if (!preg_match('/^<p/i', $ptext)) $ptext = '<p>' . $ptext;
                if (!preg_match('/<\/p>\s*$/i', $ptext)) $ptext .= '</p>';
                
                if ($is_locked && $p_idx == $lock_index) {
                    $lock_btn_html = $facebook_group_url
                        ? '<a href="' . esc_url($facebook_group_url) . '" target="_blank" rel="noopener" class="r-lock-btn" onclick="unlockChapter(event)">Tham gia nhóm Facebook</a>'
                        : '<span class="r-lock-btn disabled" aria-disabled="true">Nhóm Facebook chưa được cấu hình</span>';
                    $guide_link_html = $unlock_guide_url
                        ? '<a href="' . esc_url($unlock_guide_url) . '" class="r-lock-link">Xem hướng dẫn mở khóa</a>'
                        : '';

                    echo '<div class="r-lock-box" id="rLockBox">
                        <span class="r-lock-req">Yêu cầu</span>
                        <h3 class="r-lock-title">Tham gia nhóm Facebook để đọc tiếp</h3>
                        <p class="r-lock-desc">Nhấn nút dưới đây để tham gia, sau đó quay lại trang — chương sẽ được mở khóa.</p>
                        ' . $lock_btn_html . '
                        ' . $guide_link_html . '
                    </div>';
                    echo '<div class="r-hidden-content" id="rHiddenContent">';
                }

                echo '<div class="r-para-wrap" data-pidx="' . $p_idx . '">';
                echo $ptext;
                echo '<button class="r-para-btn" onclick="pCmt.open(' . $p_idx . ')" title="Bình luận đoạn này">💬</button>';
                echo '</div>';
                $p_idx++;
            }
            
            if ($is_locked && $p_idx > $lock_index) {
                echo '</div>'; // End .r-hidden-content
            }
            ?>
        </div>

        <div class="r-nav">
            <a href="<?php echo $prev_chap ? get_permalink($prev_chap->ID) : '#'; ?>" class="r-nav-prev <?php echo $prev_chap ? '' : 'dis'; ?>"><span>Chương trước</span></a>
            <a href="javascript:void(0)" onclick="appModal.open('tocModal')" class="r-nav-list"><svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"/></svg></a>
            <a href="<?php echo $next_chap ? get_permalink($next_chap->ID) : '#'; ?>" class="r-nav-next <?php echo $next_chap ? '' : 'dis'; ?>"><span>Chương sau</span></a>
        </div>
    </div>
    
    
    <!-- Speed Dial Mobile HTML -->
    <div class="r-speed-dial" id="speedDial">
        
        <div class="r-sd-actions">
            <button class="r-sd-btn" onclick="appTTS.toggle()" id="ttsBtn">
                <span class="r-sd-icon"><svg width="18" height="18" fill="none" stroke="#6366f1" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 2a6 6 0 00-6 6v4a6 6 0 0012 0V8a6 6 0 00-6-6zM8 12h8M12 22v-4"/></svg></span>
                <span id="ttsLabel">Nghe truyện</span>
            </button>
            <button class="r-sd-btn" onclick="pCmt.openMode('all')">
                <span class="r-sd-icon"><svg width="18" height="18" fill="none" stroke="#6366f1" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg></span>
                Bình luận
            </button>
            <button class="r-sd-btn" onclick="appLike.toggle()">
                <span class="r-sd-icon"><svg id="likeIcon" width="18" height="18" fill="none" stroke="#ef4444" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg></span>
                <span id="likeCount"><?php echo (int)get_post_meta($truyen_id, 'truyen_yeu_thich', true); ?></span> lượt thích
            </button>
        </div>
        <button class="r-sd-fab" onclick="this.parentElement.classList.toggle('open')">
            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/></svg>
        </button>
    </div>

    <!-- Mobile Tab HTML -->
    <div class="r-mob-nav">
        <div class="r-mob-nav-inner">
            <a href="<?php echo get_site_url(); ?>" class="r-mob-nav-item">
                <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
                Home
            </a>
            <a href="<?php echo $prev_chap ? get_permalink($prev_chap->ID) : 'javascript:void(0)'; ?>" class="r-mob-nav-item <?php echo $prev_chap ? '' : 'dis'; ?>">
                <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"/></svg>
                Trước
            </a>
            <button class="r-mob-nav-item r-mob-nav-center" onclick="appModal.open('tocModal')">
                <div style="display:flex;align-items:center;gap:4px;"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg> Chương</div>
                <?php 
                    $curr_index = array_search($curr_id, array_column($chapters, 'ID'));
                    $chap_txt = ($curr_index !== false) ? 'Ch. ' . ($curr_index + 1) . ' / ' . count($chapters) : 'TOC';
                ?>
                <span class="chap-progress"><?php echo $chap_txt; ?></span>
            </button>
            <a href="<?php echo $next_chap ? get_permalink($next_chap->ID) : 'javascript:void(0)'; ?>" class="r-mob-nav-item <?php echo $next_chap ? '' : 'dis'; ?>">
                <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"/></svg>
                Sau
            </a>
            <button class="r-mob-nav-item" onclick="appModal.open('setModal')">
                <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35H12a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
                Cài đặt
            </button>
        </div>
    </div>

    <!-- Float to top -->
    <button onclick="window.scrollTo({top: 0, behavior: 'smooth'})" class="r-fab-top" id="fabTop">
        <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 15l7-7 7 7"/></svg>
    </button>
</div>

<!-- Modal TOC -->
<div id="tocModal" class="r-modal-wrap">
    <div class="r-overlay" onclick="appModal.close('tocModal')"></div>
    <div class="r-modal">
        <div class="r-modal-hdr">
            <span>Danh sách chương</span>
            <button class="r-modal-close" onclick="appModal.close('tocModal')">&times;</button>
        </div>
        <div class="r-modal-body">
            <input type="text" class="r-toc-search" id="qCh" placeholder="Tìm chương nhanh...">
            <div class="r-toc-list">
                <?php foreach($chapters as $chap): ?>
                <a href="<?php echo get_permalink($chap->ID); ?>" class="r-toc-item <?php echo ($chap->ID == $curr_id) ? 'active' : ''; ?>">
                    <?php echo esc_html($chap->post_title); ?>
                </a>
                <?php endforeach; ?>
            </div>
        </div>
    </div>
</div>

<!-- Modal Settings -->
<div id="setModal" class="r-modal-wrap">
    <div class="r-overlay" onclick="appModal.close('setModal')"></div>
    <div class="r-modal">
        <div class="r-modal-hdr">
            <span>Cài đặt Đọc truyện</span>
            <button class="r-modal-close" onclick="appModal.close('setModal')">&times;</button>
        </div>
        <div class="r-modal-body">
            <div class="r-set-row">
                <span class="r-set-label">Cỡ chữ</span>
                <div class="r-set-group">
                    <button class="r-set-btn" onclick="rSet.font(-2)">Nhỏ (A-)</button>
                    <button class="r-set-btn" onclick="rSet.font(2)">Lớn (A+)</button>
                </div>
            </div>
            <div class="r-set-row">
                <span class="r-set-label">Kiểu Chữ</span>
                <div class="r-set-group" style="flex-wrap: wrap;">
                    <button class="r-set-btn" onclick="rSet.fontFamily('Lora, Georgia, serif')" style="font-family:Lora,serif;">Lora (Mặc định)</button>
                    <button class="r-set-btn" onclick="rSet.fontFamily('Be Vietnam Pro, sans-serif')">Vietnam Pro</button>
                    <button class="r-set-btn" onclick="rSet.fontFamily('Georgia, serif')" style="font-family:Georgia,serif;">Georgia</button>
                </div>
            </div>
            <div class="r-set-row">
                <span class="r-set-label">Phông Nền</span>
                <div class="r-set-group" style="flex-wrap: wrap;">
                    <button class="r-set-btn r-bg-theme1" onclick="rSet.bg('theme1')">Sáng</button>
                    <button class="r-set-btn r-bg-theme3" onclick="rSet.bg('theme3')">Mắt</button>
                    <button class="r-set-btn r-bg-theme2" onclick="rSet.bg('theme2')">Ban đêm</button>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
const appModal = {
    open: (id) => {
        let el = document.getElementById(id);
        if (!el) return;
        el.classList.add('r-show');
        setTimeout(() => el.classList.add('r-active'), 10);
        document.body.style.overflow = 'hidden';
    },
    close: (id) => {
        let el = document.getElementById(id);
        if (!el) return;
        el.classList.remove('r-active');
        setTimeout(() => { el.classList.remove('r-show'); document.body.style.overflow = ''; }, 300);
    }
}

// Float Top Visibility
window.addEventListener('scroll', () => {
    let fab = document.getElementById('fabTop');
    if (!fab) return;
    if(window.scrollY > 500) fab.classList.add('show');
    else fab.classList.remove('show');
});

// Search chapters
const qChInput = document.getElementById('qCh');
if (qChInput) {
    qChInput.addEventListener('keyup', function() {
        let val = this.value.toLowerCase();
        document.querySelectorAll('.r-toc-item').forEach(el => {
            el.style.display = el.innerText.toLowerCase().includes(val) ? 'block' : 'none';
        });
    });
}

// Reading Settings Controller
let currSize = 20;
const rSet = {
    fontFamily: (fm) => {
        let style = document.getElementById('rSetStyleFont');
        if(!style) { style = document.createElement('style'); style.id = 'rSetStyleFont'; document.head.appendChild(style); }
        style.innerHTML = `.r-wrap, .r-content, .r-title, .r-content p, .r-content span, .r-content div { font-family: ${fm} !important; }`;
        localStorage.setItem('rfm', fm);
    },
    font: (diff) => {
        currSize += diff;
        if(currSize < 14) currSize = 14;
        if(currSize > 40) currSize = 40;
        let style = document.getElementById('rSetStyleSize');
        if(!style) { style = document.createElement('style'); style.id = 'rSetStyleSize'; document.head.appendChild(style); }
        style.innerHTML = `.r-content, .r-content p, .r-content span, .r-content div { font-size: ${currSize}px !important; line-height: 1.8 !important; }`;
        localStorage.setItem('rsz', currSize);
    },
    bg: (theme) => {
        let wr = document.getElementById('rWrap');
        let hd = document.getElementById('rHdr');
        let ct = document.getElementById('rContent');
        let container = document.querySelector('.r-container');
        
        let styleBg = document.getElementById('rSetStyleBg');
        if(!styleBg) { styleBg = document.createElement('style'); styleBg.id = 'rSetStyleBg'; document.head.appendChild(styleBg); }

        if(theme === 'theme2') { // Dark mode
            styleBg.innerHTML = `
                html, body, #rWrap { background: #000000 !important; }
                .r-container { background: #111827 !important; border: 1px solid #1f2937 !important; box-shadow: none !important; }
                #rHdr { background: #111827 !important; border-color: #1f2937 !important; }
                #rContent, #rContent p, #rContent span, #rContent div { color: #d1d5db !important; }
                .r-title, .r-story-name { color: #f3f4f6 !important; }
                .r-back-btn, .r-icon-btn { background: #1f2937 !important; color: #d1d5db !important; }
                .r-sd-btn { background: #1f2937 !important; color: #e5e7eb !important; border-color: #374151 !important; }
            `;
        } else if(theme === 'theme3') { // Eye care
            styleBg.innerHTML = `
                html, body, #rWrap { background: #edf2f7 !important; }
                .r-container { background: #FFFDF0 !important; border: none !important; }
                #rHdr { background: #fff !important; border-color: #e5e7eb !important; }
                #rContent, #rContent p, #rContent span, #rContent div { color: #2d3748 !important; }
                .r-title, .r-story-name { color: #111827 !important; }
                .r-back-btn, .r-icon-btn { background: #f3f4f6 !important; color: #111827 !important; }
                .r-sd-btn { background: #fff !important; color: #374151 !important; border-color: #e5e7eb !important; }
            `;
        } else { // Light mode (theme1)
            styleBg.innerHTML = `
                html, body, #rWrap { background: #f5f3f7 !important; }
                .r-container { background: #FFFDF0 !important; border: none !important; }
                #rHdr { background: #fff !important; border-color: #e5e7eb !important; }
                #rContent, #rContent p, #rContent span, #rContent div { color: #333 !important; }
                .r-title, .r-story-name { color: #111827 !important; }
                .r-back-btn, .r-icon-btn { background: #f3f4f6 !important; color: #111827 !important; }
                .r-sd-btn { background: #fff !important; color: #374151 !important; border-color: #e5e7eb !important; }
            `;
        }
        localStorage.setItem('rbg', theme);
    },
    init: () => {
        let sz = localStorage.getItem('rsz');
        if(sz) { currSize = parseInt(sz); document.getElementById('rContent').style.fontSize = currSize + 'px'; }
        let bg = localStorage.getItem('rbg');
        if(bg) rSet.bg(bg);
        let fm = localStorage.getItem('rfm');
        if(fm) rSet.fontFamily(fm);
    }
}
rSet.init();

// Chapter Lock Logic
function unlockChapter(e) {
    localStorage.setItem('unlocked_fb', '1');
    window.addEventListener('focus', function onFocus() {
        if(localStorage.getItem('unlocked_fb')) {
            let lockBox = document.getElementById('rLockBox');
            let hiddenContent = document.getElementById('rHiddenContent');
            if(lockBox) lockBox.style.display = 'none';
            if(hiddenContent) hiddenContent.style.display = 'block';
            window.removeEventListener('focus', onFocus);
        }
    }, { once: true });
}

document.addEventListener('DOMContentLoaded', () => {
    if(localStorage.getItem('unlocked_fb')) {
        let lockBox = document.getElementById('rLockBox');
        let hiddenContent = document.getElementById('rHiddenContent');
        if(lockBox) lockBox.style.display = 'none';
        if(hiddenContent) hiddenContent.style.display = 'block';
    }
});
</script>

<?php endwhile; endif; ?>

<!-- Paragraph Comments Slide Panel -->
<div class="r-cmt-overlay" id="cmtOverlay" onclick="pCmt.close()"></div>
<div class="r-cmt-panel" id="cmtPanel">
    <div class="r-cmt-panel-hdr">
        <span class="r-cmt-panel-title" id="cmtPanelTitle">💬 Bình luận đoạn</span>
        <button class="r-cmt-close" onclick="pCmt.close()">&times;</button>
    </div>
    <div class="r-cmt-body" id="cmtBody">
        <div class="r-cmt-empty">Đang tải bình luận...</div>
    </div>
    <div class="r-cmt-form">
        <textarea id="cmtInput" rows="3" placeholder="Viết cảm nhận của bạn về đoạn này..."></textarea>
        <div class="r-cmt-form-btns">
            <button class="r-cmt-submit" onclick="pCmt.submit()">Gửi bình luận</button>
        </div>
    </div>
</div>

<script>
const pCmt = {
    postId: <?php echo get_the_ID(); ?>,
    nonce: '<?php echo wp_create_nonce("temply_ai_nonce"); ?>',
    ajaxUrl: '<?php echo admin_url("admin-ajax.php"); ?>',
    currentP: -1,
    
    open(p_idx) {
        this.currentP = p_idx;
        document.getElementById('cmtPanelTitle').textContent = `💬 Bình luận đoạn #${p_idx + 1}`;
        document.getElementById('cmtPanel').classList.add('open');
        document.getElementById('cmtOverlay').classList.add('open');
        document.body.style.overflow = 'hidden';
        this.load(p_idx);
    },
    
    close() {
        document.getElementById('cmtPanel').classList.remove('open');
        document.getElementById('cmtOverlay').classList.remove('open');
        document.body.style.overflow = '';
        this.currentP = -1;
    },
    
    async load(p_idx) {
        const body = document.getElementById('cmtBody');
        body.innerHTML = '<div class="r-cmt-empty">⏳ Đang tải...</div>';
        
        const fd = new FormData();
        fd.append('action', 'temply_load_paragraph_comments');
        fd.append('post_id', this.postId);
        fd.append('p_index', p_idx);
        fd.append('request_type', 'chunk');
        
        try {
            const r = await fetch(this.ajaxUrl, { method: 'POST', body: fd });
            const res = await r.json();
            if (res.success) {
                body.innerHTML = res.data.html || '<div class="r-cmt-empty">Chưa có bình luận nào. Bạn hãy là người đầu tiên!</div>';
            }
        } catch(e) {
            body.innerHTML = '<div class="r-cmt-empty">Không tải được bình luận.</div>';
        }
    },
    
    async submit() {
        if (this.currentP < 0) return;
        const input = document.getElementById('cmtInput');
        const text = input.value.trim();
        if (!text) return alert('Vui lòng nhập nội dung bình luận!');
        
        const btn = document.querySelector('.r-cmt-submit');
        btn.disabled = true; btn.textContent = 'Đang gửi...';
        
        const fd = new FormData();
        fd.append('action', 'temply_add_paragraph_comment');
        fd.append('nonce', this.nonce);
        fd.append('post_id', this.postId);
        fd.append('p_index', this.currentP);
        fd.append('comment_content', text);
        fd.append('author_name', 'Độc giả');
        
        try {
            const r = await fetch(this.ajaxUrl, { method: 'POST', body: fd });
            const res = await r.json();
            if (res.success) {
                input.value = '';
                this.load(this.currentP); // Reload comments
            } else {
                alert(res.data?.message || 'Gửi thất bại!');
            }
        } catch(e) {
            alert('Lỗi kết nối!');
        } finally {
            btn.disabled = false; btn.textContent = 'Gửi bình luận';
        }
    }
};
</script>


<script>
// --- Nghe Truyện (TTS API) ---
const appTTS = {
    isPlaying: false,
    utterance: null,
    paragraphs: [],
    currentIndex: 0,
    
    init() {
        this.paragraphs = Array.from(document.querySelectorAll('.r-para-wrap')).map(el => el.textContent.replace('💬', '').trim()).filter(t => t.length > 0);
    },
    
    toggle() {
        if (!('speechSynthesis' in window)) return alert('Trình duyệt của bạn không hỗ trợ đọc Text-to-Speech!');
        if (this.paragraphs.length === 0) this.init();
        
        const btnL = document.getElementById('ttsLabel');
        if (this.isPlaying) {
            window.speechSynthesis.cancel();
            this.isPlaying = false;
            btnL.textContent = 'Nghe truyện';
            this.currentIndex = 0;
            return;
        }
        
        this.isPlaying = true;
        btnL.textContent = 'Đang đọc (Chạm dừng)';
        this.playNext();
    },
    
    playNext() {
        if (!this.isPlaying) return;
        if (this.currentIndex >= this.paragraphs.length) {
            this.isPlaying = false;
            document.getElementById('ttsLabel').textContent = 'Nghe truyện';
            this.currentIndex = 0;
            return;
        }
        
        const text = this.paragraphs[this.currentIndex];
        this.utterance = new SpeechSynthesisUtterance(text);
        this.utterance.lang = 'vi-VN';
        this.utterance.rate = 1.0;
        this.utterance.pitch = 1.0;
        
        // Highlight paragraph
        document.querySelectorAll('.r-para-wrap').forEach(el => el.style.backgroundColor = 'transparent');
        const currentParaHtml = document.querySelectorAll('.r-para-wrap')[this.currentIndex];
        if(currentParaHtml) {
            currentParaHtml.style.backgroundColor = 'rgba(99, 102, 241, 0.1)';
            currentParaHtml.scrollIntoView({behavior:'smooth', block:'center'});
        }
        
        this.utterance.onend = () => {
            this.currentIndex++;
            this.playNext();
        };
        
        this.utterance.onerror = () => {
            console.error('SpeechSynthesis API Error');
            this.currentIndex++;
            this.playNext();
        };
        
        window.speechSynthesis.speak(this.utterance);
    }
};

// --- Yêu Thích ---
const appLike = {
    toggle() {
        let lkey = 'liked_' + <?php echo $truyen_id; ?>;
        if (localStorage.getItem(lkey)) return alert('Bạn đã thích truyện này rồi!');
        
        const fd = new FormData();
        fd.append('action', 'temply_like_chapter');
        fd.append('post_id', <?php echo $truyen_id; ?>);
        
        fetch('<?php echo admin_url('admin-ajax.php'); ?>', { method: 'POST', body: fd })
        .then(r => r.json())
        .then(res => {
            if (res.success) {
                document.getElementById('likeCount').textContent = res.data.likes;
                document.getElementById('likeIcon').style.fill = '#ef4444';
                localStorage.setItem(lkey, '1');
            }
        });
    }
};

// Modify pCmt to support mode 'all'
if (typeof pCmt !== 'undefined') {
    pCmt.openMode = function(mode) {
        if (mode === 'all') {
            document.getElementById('cmtPanelTitle').textContent = `💬 Bình luận chung`;
            this.currentP = -1; // -1 represents global chapter comment
            document.getElementById('cmtPanel').classList.add('open');
            document.getElementById('cmtOverlay').classList.add('open');
            document.body.style.overflow = 'hidden';
            this.load(-1);
            document.querySelector('.r-speed-dial').classList.remove('open');
        } else {
            this.open(mode);
        }
    };
    
    // Check if already liked
    window.addEventListener('DOMContentLoaded', () => {
        if (localStorage.getItem('liked_' + <?php echo $truyen_id; ?>)) {
            document.getElementById('likeIcon').style.fill = '#ef4444';
        }
    });
}
</script>

<?php get_footer(); ?>
