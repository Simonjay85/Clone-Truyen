import re

with open("tehi-theme/single-chuong.php", "r", encoding="utf-8") as f:
    code = f.read()

# Replace the Settings Panel Block and JS logic.
new_settings = """
        <!-- Settings Panel -->
        <div id="settingsPanel" class="hidden absolute bottom-0 right-16 w-80 bg-surface-container-lowest dark:bg-slate-900/95 backdrop-blur-2xl p-6 rounded-[2rem] shadow-[0_24px_64px_rgba(0,0,0,0.2)] border border-outline-variant/20 transition-all origin-bottom-right">
            <div class="flex items-center justify-between mb-6">
                <h4 class="text-lg font-bold text-on-surface font-headline">Cài đặt Đọc</h4>
                <button id="closeSettings" class="w-8 h-8 rounded-full hover:bg-surface-container-high flex items-center justify-center text-on-surface-variant transition-colors"><span class="material-symbols-outlined text-sm">close</span></button>
            </div>
            
            <div class="mb-6 bg-surface-container-low dark:bg-black/20 p-4 rounded-2xl">
                <div class="flex justify-between items-center mb-3">
                    <span class="text-xs font-bold text-on-surface-variant uppercase tracking-wider flex items-center gap-1"><span class="material-symbols-outlined text-sm">format_size</span> Cỡ Chữ</span>
                    <span id="fontSizeDisplay" class="text-sm font-bold text-primary bg-primary-container/30 px-3 py-1 rounded-full">22px</span>
                </div>
                <div class="flex items-center gap-3">
                    <button id="fontDec" class="flex-1 h-12 rounded-xl bg-surface-container-lowest dark:bg-slate-800 text-on-surface flex items-center justify-center hover:bg-surface-variant transition-colors shadow-sm font-bold text-xl border border-outline-variant/10">-</button>
                    <button id="fontInc" class="flex-1 h-12 rounded-xl bg-surface-container-lowest dark:bg-slate-800 text-on-surface flex items-center justify-center hover:bg-surface-variant transition-colors shadow-sm font-bold text-xl border border-outline-variant/10">+</button>
                </div>
            </div>
            
            <div class="bg-surface-container-low dark:bg-black/20 p-4 rounded-2xl">
                <span class="text-xs font-bold text-on-surface-variant uppercase tracking-wider mb-3 flex items-center gap-1"><span class="material-symbols-outlined text-sm">palette</span> Màu Nền</span>
                <div class="grid grid-cols-3 gap-3">
                    <button data-theme="white" class="group relative h-14 rounded-xl border-2 border-transparent bg-slate-50 transition-all hover:scale-105 btn-theme flex items-center justify-center shadow-sm">
                        <span class="text-slate-800 font-bold text-xs uppercase opacity-0 group-hover:opacity-100 transition-opacity">Sáng</span>
                    </button>
                    <button data-theme="sepia" class="group relative h-14 rounded-xl border-2 border-transparent bg-[#F4EAD5] transition-all hover:scale-105 btn-theme flex items-center justify-center shadow-sm">
                        <span class="text-[#5b4636] font-bold text-xs uppercase opacity-0 group-hover:opacity-100 transition-opacity">Sepia</span>
                    </button>
                    <button data-theme="dark" class="group relative h-14 rounded-xl border-2 border-transparent bg-slate-900 transition-all hover:scale-105 btn-theme flex items-center justify-center shadow-sm">
                        <span class="text-slate-300 font-bold text-xs uppercase opacity-0 group-hover:opacity-100 transition-opacity">Tối</span>
                    </button>
                </div>
            </div>
        </div>
"""

code = re.sub(
    r'<!-- Settings Panel -->.*?</div>\s*</div>\s*<!-- QUẢNG CÁO AFFILIATE SHOPEE -->', 
    new_settings + '    </div>\n\n    <!-- QUẢNG CÁO AFFILIATE SHOPEE -->', 
    code, flags=re.DOTALL
)

# And inject logic to handle toggle active states
js_logic = """
    // Themes (Hack using Tailwind dark mode & inline colors)
    const btns = document.querySelectorAll('.btn-theme');
    function applyTheme(theme) {
        if(theme === 'dark') {
            htmlTag.classList.add('dark');
            htmlTag.style.background = '#0f172a'; // slate-900
            content.style.color = '#cbd5e1';
        } else if (theme === 'sepia') {
            htmlTag.classList.remove('dark');
            htmlTag.style.background = '#F4EAD5';
            content.style.color = '#5b4636';
        } else {
            htmlTag.classList.remove('dark');
            htmlTag.style.background = '#f8fafc'; // slate-50
            content.style.color = '#334155'; // slate-700
        }
        
        // Update active rings
        btns.forEach(b => {
             b.style.borderColor = (b.dataset.theme === theme) ? '#3b82f6' : 'transparent';
        });
        
        localStorage.setItem('reader-theme', theme);
    }
"""

code = re.sub(
    r"// Themes \(Hack using Tailwind.*?\n\s+applyTheme\(savedTheme\);",
    js_logic + "\n    const savedTheme = localStorage.getItem('reader-theme') || 'white';\n    applyTheme(savedTheme);",
    code, flags=re.DOTALL
)

# Update Close Settings button logic
code = re.sub(
    r"(if \(toggleSettingsBtn\) {\s+toggleSettingsBtn\.addEventListener\('click', \(\) => {\s+settingsPanel\.classList\.toggle\('hidden'\);\s+}\);\s+})",
    r"\1\n    const closeSettings = document.getElementById('closeSettings');\n    if(closeSettings) closeSettings.addEventListener('click', () => settingsPanel.classList.add('hidden'));",
    code
)


with open("tehi-theme/single-chuong.php", "w", encoding="utf-8") as f:
    f.write(code)

print("Settings redesigned!")
