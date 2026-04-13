import re

# 1. Update logo to DTT in header.php
with open("tehi-theme/header.php", "r", encoding="utf-8") as f:
    h_code = f.read()
h_code = h_code.replace("Đọc truyện chữ <span class=\"text-primary\">Online</span>", "DTT")
h_code = h_code.replace("Đọc truyện chữ Online", "DTT")
with open("tehi-theme/header.php", "w", encoding="utf-8") as f:
    f.write(h_code)

# Update logo to DTT in header-home.php
with open("tehi-theme/header-home.php", "r", encoding="utf-8") as f:
    hh_code = f.read()
hh_code = hh_code.replace("Đọc truyện chữ <span class=\"text-primary\">Online</span>", "DTT")
hh_code = hh_code.replace("Đọc truyện chữ Online", "DTT")
with open("tehi-theme/header-home.php", "w", encoding="utf-8") as f:
    f.write(hh_code)

# 2. Fix Settings Panel in single-chuong.php (Inline styles for bg, add Font chooser)
with open("tehi-theme/single-chuong.php", "r", encoding="utf-8") as f:
    c_code = f.read()

new_panel = """
        <!-- Settings Panel -->
        <div id="settingsPanel" class="hidden absolute bottom-0 right-16 w-80 bg-surface-container-lowest dark:bg-slate-900/95 backdrop-blur-2xl p-6 rounded-[2rem] shadow-[0_24px_64px_rgba(0,0,0,0.2)] border border-outline-variant/20 transition-all origin-bottom-right">
            <div class="flex items-center justify-between mb-6">
                <h4 class="text-lg font-bold text-on-surface font-headline">Cài đặt Đọc</h4>
                <button id="closeSettings" class="w-8 h-8 rounded-full hover:bg-surface-container-high flex items-center justify-center text-on-surface-variant transition-colors"><span class="material-symbols-outlined text-sm">close</span></button>
            </div>
            
            <div class="mb-4 bg-surface-container-low dark:bg-black/20 p-4 rounded-2xl">
                <div class="flex justify-between items-center mb-3">
                    <span class="text-xs font-bold text-on-surface-variant uppercase tracking-wider flex items-center gap-1"><span class="material-symbols-outlined text-sm">format_size</span> Cỡ Chữ</span>
                    <span id="fontSizeDisplay" class="text-sm font-bold text-primary bg-primary-container/30 px-3 py-1 rounded-full">22px</span>
                </div>
                <div class="flex items-center gap-3">
                    <button id="fontDec" class="flex-1 h-10 rounded-xl bg-surface-container-lowest dark:bg-slate-800 text-on-surface flex items-center justify-center hover:bg-surface-variant transition-colors shadow-sm font-bold text-xl border border-outline-variant/10">-</button>
                    <button id="fontInc" class="flex-1 h-10 rounded-xl bg-surface-container-lowest dark:bg-slate-800 text-on-surface flex items-center justify-center hover:bg-surface-variant transition-colors shadow-sm font-bold text-xl border border-outline-variant/10">+</button>
                </div>
            </div>
            
            <div class="mb-4 bg-surface-container-low dark:bg-black/20 p-4 rounded-2xl">
                <span class="text-xs font-bold text-on-surface-variant uppercase tracking-wider mb-3 flex items-center gap-1"><span class="material-symbols-outlined text-sm">title</span> Phông Chữ</span>
                <div class="grid grid-cols-2 gap-2">
                    <button data-font="sans" class="h-10 rounded-xl border border-outline-variant/20 bg-surface-container-lowest dark:bg-slate-800 transition-all font-sans font-medium text-sm btn-font hover:border-primary">Sans-serif</button>
                    <button data-font="serif" class="h-10 rounded-xl border border-outline-variant/20 bg-surface-container-lowest dark:bg-slate-800 transition-all font-serif font-medium text-sm btn-font hover:border-primary">Serif (Sách)</button>
                </div>
            </div>
            
            <div class="bg-surface-container-low dark:bg-black/20 p-4 rounded-2xl">
                <span class="text-xs font-bold text-on-surface-variant uppercase tracking-wider mb-3 flex items-center gap-1"><span class="material-symbols-outlined text-sm">palette</span> Màu Nền</span>
                <div class="grid grid-cols-3 gap-3">
                    <button data-theme="white" style="background-color: #f8fafc; border-color: #cbd5e1" class="h-12 rounded-xl border-2 transition-all hover:scale-105 btn-theme shadow-sm"></button>
                    <button data-theme="sepia" style="background-color: #F4EAD5; border-color: #d6ccb8" class="h-12 rounded-xl border-2 transition-all hover:scale-105 btn-theme shadow-sm"></button>
                    <button data-theme="dark" style="background-color: #0f172a; border-color: #334155" class="h-12 rounded-xl border-2 transition-all hover:scale-105 btn-theme shadow-sm"></button>
                </div>
            </div>
        </div>
"""

c_code = re.sub(
    r'<!-- Settings Panel -->.*?</div>\s*</div>\s*<!-- QUẢNG CÁO', 
    new_panel + '    </div>\n\n    <!-- QUẢNG CÁO', 
    c_code, flags=re.DOTALL
)

# Insert logic for Font changing and update theme logic stringency
js_logic = """
    // Reader Settings
    const btns = document.querySelectorAll('.btn-theme');
    const fontBtns = document.querySelectorAll('.btn-font');
    
    function applyTheme(theme) {
        if(theme === 'dark') {
            htmlTag.classList.add('dark');
            htmlTag.style.background = '#0f172a';
            content.style.color = '#cbd5e1';
        } else if (theme === 'sepia') {
            htmlTag.classList.remove('dark');
            htmlTag.style.background = '#F4EAD5';
            content.style.color = '#5b4636';
        } else {
            htmlTag.classList.remove('dark');
            htmlTag.style.background = '#f8fafc';
            content.style.color = '#334155';
        }
        
        btns.forEach(b => {
             b.style.borderWidth = '2px';
             if (b.dataset.theme === theme) {
                 b.style.borderColor = '#3b82f6'; // Blue highlight
             } else {
                 if(b.dataset.theme==='white') b.style.borderColor = '#cbd5e1';
                 if(b.dataset.theme==='sepia') b.style.borderColor = '#d6ccb8';
                 if(b.dataset.theme==='dark') b.style.borderColor = '#334155';
             }
        });
        localStorage.setItem('reader-theme', theme);
    }

    function applyFont(fontArg) {
        if(fontArg === 'serif') {
            content.style.fontFamily = 'Lora, Cambria, "Times New Roman", serif';
        } else {
            content.style.fontFamily = '"Plus Jakarta Sans", Inter, sans-serif';
        }
        fontBtns.forEach(b => {
            if (b.dataset.font === fontArg) {
                b.style.borderColor = '#3b82f6';
                b.style.color = '#3b82f6';
            } else {
                b.style.borderColor = '';
                b.style.color = '';
            }
        });
        localStorage.setItem('reader-font', fontArg);
    }
"""

# Replace the old applyTheme logic
c_code = re.sub(
    r"// Themes \(Hack using Tailwind.*?\n\s+applyTheme\(savedTheme\);",
    js_logic + """
    const savedTheme = localStorage.getItem('reader-theme') || 'white';
    applyTheme(savedTheme);
    const savedFont = localStorage.getItem('reader-font') || 'sans';
    applyFont(savedFont);

    btns.forEach(b => b.addEventListener('click', () => applyTheme(b.dataset.theme)));
    fontBtns.forEach(b => b.addEventListener('click', () => applyFont(b.dataset.font)));
    """,
    c_code, flags=re.DOTALL
)

with open("tehi-theme/single-chuong.php", "w", encoding="utf-8") as f:
    f.write(c_code)

print("Updated settings and logo!")
