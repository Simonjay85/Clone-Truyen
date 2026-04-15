import re

with open('tehi-theme/single-chuong.php', 'r') as f:
    content = f.read()

# Add CSS for new UI
new_css = """
/* FAB */
.r-fab-top { position: fixed; bottom: 100px; left: 30px; width: 44px; height: 44px; border-radius: 50%; background: #111827; color: #fff; border: none; display: flex; align-items: center; justify-content: center; cursor: pointer; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); opacity: 0; pointer-events: none; transition: all 0.3s; z-index: 100; transform: translateY(20px); }
.r-fab-top.show { opacity: 1; pointer-events: auto; transform: translateY(0); }

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
    .r-container { padding-bottom: 90px; }
}
"""
content = re.sub(r'/\* FAB \*/.*?(?=/\* Modal General \*/)', new_css, content, flags=re.DOTALL)

# Add HTML code before Float to top
html_code = """
    <!-- Speed Dial Mobile HTML -->
    <div class="r-speed-dial" id="speedDial">
        <div class="r-sd-actions">
            <button class="r-sd-btn" onclick="alert('Tính năng Nghe truyện đang được phát triển!')">
                <span class="r-sd-icon"><svg width="18" height="18" fill="none" stroke="#6366f1" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 2a6 6 0 00-6 6v4a6 6 0 0012 0V8a6 6 0 00-6-6zM8 12h8M12 22v-4"/></svg></span>
                Nghe truyện
            </button>
            <button class="r-sd-btn" onclick="document.body.scrollIntoView({behavior:'smooth', block:'end'})">
                <span class="r-sd-icon"><svg width="18" height="18" fill="none" stroke="#6366f1" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg></span>
                Bình luận
            </button>
            <button class="r-sd-btn" onclick="alert('Đã thêm vào mục Yêu Thích!')">
                <span class="r-sd-icon"><svg width="18" height="18" fill="none" stroke="#ef4444" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg></span>
                <span id="likeCount"><?php echo rand(2,10); ?></span> lượt thích
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
                <div style="display:flex;align-items:center;gap:4px;"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253A10.024 10.024 0 0113.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg> Chương</div>
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
"""
content = re.sub(r'<!-- Float to top -->', html_code + '\n    <!-- Float to top -->', content)

with open('tehi-theme/single-chuong.php', 'w') as f:
    f.write(content)
