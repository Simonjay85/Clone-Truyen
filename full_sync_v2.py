import re
import os

def update_file(path, replacements):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    new_content = content
    for pattern, subst in replacements.items():
        new_content = re.sub(pattern, subst, new_content, flags=re.DOTALL)
    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✓ Synchronized: {path}")

# --- HEADER: ADD ANNOUNCEMENT BAR ---
header_rep = {
    r'(</header>)': r'\1\n<!-- THÔNG BÁO CHẠY CHỮ -->\n<div class="truyen-announcement-bar py-2" style="background:rgba(255,255,255,0.8);backdrop-filter:blur(10px);border-bottom:1px solid #eee;overflow:hidden;">\n    <div class="container">\n        <marquee behavior="scroll" direction="left" class="fw-bold text-pink m-0"><i class="fas fa-bullhorn me-2"></i> Chào mừng bạn đến với Đọc Tiểu Thuyết - Website đọc truyện ngôn tình, tiểu thuyết hấp dẫn nhất. Chúc bạn có những giây phút thư giãn!</marquee>\n    </div>\n</div>'
}

# --- SINGLE CHUONG: ADD READER JS LOGIC ---
# I will find the script block and append the logic
chuong_rep = {
    r'(\$\(window\)\.on\(\'beforeunload\', function\(\) \{.*?\}\);)': r'''\1\n\n            // LOGIC CÔNG CỤ ĐỌC\n            const readerContent = $('.msv-khung-truyen-noi-dung');\n            const settPanel = $('#settingsPanel');\n            let fSize = parseInt(localStorage.getItem('reader-f-size')) || 22;\n\n            function applyRSettings() {\n                readerContent.css('font-size', fSize + 'px');\n                $('#fontSizeDisplay').text(fSize + 'px');\n                const thm = localStorage.getItem('reader-thm') || 'white';\n                readerContent.removeClass('reader-theme-sepia reader-theme-dark');\n                $('.theme-dot').removeClass('active');\n                $(`.theme-dot[data-theme="${thm}"]`).addClass('active');\n                if(thm !== 'white') readerContent.addClass('reader-theme-' + thm);\n            }\n            applyRSettings();\n\n            $('#toggleSettings').on('click', function() { settPanel.toggleClass('active'); });\n            $('#fontInc').on('click', function() { fSize = Math.min(fSize + 2, 36); localStorage.setItem('reader-f-size', fSize); applyRSettings(); });\n            $('#fontDec').on('click', function() { fSize = Math.max(fSize - 2, 14); localStorage.setItem('reader-f-size', fSize); applyRSettings(); });\n            $('.theme-dot').on('click', function() { localStorage.setItem('reader-thm', $(this).data('theme')); applyRSettings(); });\n            $('#scrollTop').on('click', function() { window.scrollTo({ top: 0, behavior: 'smooth' }); });\n            $(document).on('click', function(e) { if(!$(e.target).closest('.reader-tools').length) settPanel.removeClass('active'); });'''
}

update_file("tehi-theme/header.php", header_rep)
update_file("tehi-theme/single-chuong.php", chuong_rep)
print("Sync script execution finished.")
