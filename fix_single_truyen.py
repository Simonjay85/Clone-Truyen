import re

with open("tehi-theme/single-truyen.php", "r", encoding="utf-8") as f:
    code = f.read()

# Fix padding for header overlap: change pt-16 to pt-24
code = code.replace('<main class="pt-16 min-h-screen">', '<main class="pt-24 min-h-screen">')

# Remove duplicate buttons
duplicate_block = """</div>
<div class="flex flex-wrap gap-4">
<button class="px-10 py-4 bg-primary text-white rounded-full font-bold primary-gradient shadow-lg flex items-center gap-2 group hover:shadow-primary-container/30 transition-all">
<span class="material-symbols-outlined" data-weight="fill">auto_stories</span>
                                Đọc ngay
                            </button>
<button class="px-10 py-4 border-2 border-outline-variant text-on-surface-variant rounded-full font-bold hover:bg-surface-container-low transition-all flex items-center gap-2">
<span class="material-symbols-outlined">bookmark</span>
                                Theo dõi
                            </button>
</div>"""

code = code.replace(duplicate_block, "</div>")

with open("tehi-theme/single-truyen.php", "w", encoding="utf-8") as f:
    f.write(code)

print("Fixed single-truyen overlap and duplicates")
