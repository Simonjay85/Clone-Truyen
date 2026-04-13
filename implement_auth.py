import re

auth_markup = """
<!-- GLOBAL AUTH MODAL -->
<div id="globalAuthModal" class="fixed inset-0 z-[999] flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm hidden transition-opacity duration-300">
    <div class="w-full max-w-md relative scale-95 opacity-0 transition-all duration-300 transform" id="authModalContent">
        <button onclick="closeAuthModal()" class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center rounded-full bg-surface-container-high/50 hover:bg-red-500 hover:text-white text-on-surface transition-colors z-50">
            <span class="material-symbols-outlined text-lg">close</span>
        </button>
        
        <div class="glass-card rounded-[2rem] p-8 shadow-[0px_12px_32px_rgba(0,96,169,0.06)] bg-white ring-1 ring-outline-variant/15">
            <div class="text-center mb-6">
                <span class="headline text-2xl font-extrabold tracking-tight text-primary">tehitruyen.com</span>
            </div>
            <div class="flex flex-col gap-6">
                <div class="text-center">
                    <h2 class="headline text-xl font-bold text-on-surface">Chào mừng trở lại</h2>
                    <p class="text-xs text-on-surface-variant mt-1">Đăng nhập để tiếp tục hành trình đọc của bạn</p>
                </div>
                <!-- Social Logins -->
                <div class="grid grid-cols-2 gap-4">
                    <button class="flex items-center justify-center gap-2 py-3 px-4 rounded-xl bg-surface-container-lowest border border-outline-variant/30 text-on-surface text-sm font-semibold hover:bg-surface-container-low transition-all duration-300">
                        <svg class="w-5 h-5" viewBox="0 0 24 24">
                            <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"></path>
                            <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"></path>
                            <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z" fill="#FBBC05"></path>
                            <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"></path>
                        </svg>
                        Google
                    </button>
                    <button class="flex items-center justify-center gap-2 py-3 px-4 rounded-xl bg-surface-container-lowest border border-outline-variant/30 text-on-surface text-sm font-semibold hover:bg-surface-container-low transition-all duration-300">
                        <svg class="w-5 h-5 text-[#1877F2]" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"></path>
                        </svg>
                        Facebook
                    </button>
                </div>
                <!-- Input Form -->
                <form class="space-y-4" onsubmit="event.preventDefault(); alert('He thong dang tich hop Backend. Vui long tro lai sau.');">
                    <div class="space-y-2">
                        <label class="block text-xs font-semibold text-on-surface ml-1">Email</label>
                        <div class="relative">
                            <input class="w-full pl-5 pr-4 py-3 bg-surface-container-highest/30 border border-outline-variant/30 rounded-xl focus:ring-2 focus:ring-primary/20 focus:bg-white transition-all duration-300 outline-none text-sm" placeholder="name@example.com" type="email">
                        </div>
                    </div>
                    <div class="space-y-2">
                        <div class="flex justify-between items-center px-1">
                            <label class="text-xs font-semibold text-on-surface">Mật khẩu</label>
                            <a class="text-[10px] font-semibold text-primary hover:underline" href="#">Quên mật khẩu?</a>
                        </div>
                        <div class="relative">
                            <input class="w-full pl-5 pr-12 py-3 bg-surface-container-highest/30 border border-outline-variant/30 rounded-xl focus:ring-2 focus:ring-primary/20 focus:bg-white transition-all duration-300 outline-none text-sm" placeholder="••••••••" type="password">
                        </div>
                    </div>
                    <button class="primary-gradient bg-primary w-full py-3.5 rounded-full text-white font-bold text-sm tracking-wide shadow-lg shadow-primary/20 hover:scale-[1.02] active:scale-95 transition-all duration-300 mt-2" type="submit">
                        Đăng nhập
                    </button>
                </form>
                <div class="text-center">
                    <p class="text-xs text-on-surface-variant">Chưa có tài khoản? <a class="text-primary font-bold hover:underline" href="#">Đăng ký ngay</a></p>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
    function openAuthModal() {
        const m = document.getElementById('globalAuthModal');
        const c = document.getElementById('authModalContent');
        if(m) {
            m.classList.remove('hidden');
            setTimeout(() => {
                c.classList.remove('scale-95', 'opacity-0');
                c.classList.add('scale-100', 'opacity-100');
            }, 10);
        }
    }
    function closeAuthModal() {
        const m = document.getElementById('globalAuthModal');
        const c = document.getElementById('authModalContent');
        if(m) {
            c.classList.remove('scale-100', 'opacity-100');
            c.classList.add('scale-95', 'opacity-0');
            setTimeout(() => {
                m.classList.add('hidden');
            }, 300);
        }
    }
    // Listen for dark background click
    document.addEventListener('click', (e) => {
        const m = document.getElementById('globalAuthModal');
        if(e.target === m) {
            closeAuthModal();
        }
    });
</script>
"""

def inject_to_footer(filename):
    with open(filename, "r", encoding="utf-8") as f:
        code = f.read()
    if 'id="globalAuthModal"' not in code:
        code = code.replace("</body>", auth_markup + "\n</body>")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Injected auth modal into {filename}")

def modify_header_links(filename):
    with open(filename, "r", encoding="utf-8") as f:
        code = f.read()
    
    # Replace anchor tags for login/register with buttons opening the modal
    replacements = [
        (r'<a href="#" class="text-on-surface-variant font-semibold hover:text-primary transition-colors cursor-pointer">Đăng nhập</a>', 
         r'<button onclick="openAuthModal()" class="text-on-surface-variant font-semibold hover:text-primary transition-colors cursor-pointer">Đăng nhập</button>'),
         
        (r'<a href="#" class="px-6 py-2 bg-primary text-white rounded-full font-bold primary-gradient shadow-lg shadow-primary/20 hover:scale-105 transition-transform">Đăng ký</a>',
         r'<button onclick="openAuthModal()" class="px-6 py-2 bg-primary text-white rounded-full font-bold primary-gradient shadow-lg shadow-primary/20 hover:scale-105 transition-transform">Đăng ký</button>'),
         
        (r'<a href="#" class="hidden md:block text-on-surface-variant font-semibold hover:text-primary transition-colors cursor-pointer">Đăng nhập</a>',
         r'<button onclick="openAuthModal()" class="hidden md:block text-on-surface-variant font-semibold hover:text-primary transition-colors cursor-pointer">Đăng nhập</button>'),
         
        (r'<a href="#" class="hidden md:block px-6 py-2 bg-primary text-[color:var\(--on-primary\)] rounded-full font-bold primary-gradient shadow-lg shadow-primary/20 hover:scale-105 transition-transform">Đăng ký</a>',
         r'<button onclick="openAuthModal()" class="hidden md:block px-6 py-2 bg-primary text-white rounded-full font-bold primary-gradient shadow-lg shadow-primary/20 hover:scale-105 transition-transform">Đăng ký</button>')
    ]
    
    for old, new in replacements:
        code = re.sub(old, new, code)
        
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Updated header logic in {filename}")

inject_to_footer("tehi-theme/footer.php")
inject_to_footer("tehi-theme/footer-home.php")
modify_header_links("tehi-theme/header.php")
modify_header_links("tehi-theme/header-home.php")
