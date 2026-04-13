import re

with open("tehi-theme/single-truyen.php", "r", encoding="utf-8") as f:
    code = f.read()

# The ghost text block looks like this:
# <div class="absolute inset-0 z-0 flex items-center justify-center opacity-20 filter blur-xl transform scale-150 pointer-events-none select-none">
#     <h1 class="text-[120px] font-black text-white whitespace-nowrap overflow-hidden opacity-50"><?php the_title(); ?></h1>
# </div>

# Let's remove any div containing the huge blurred title.
code = re.sub(r'<div class="absolute inset-0 z-0 flex items-center justify-center.*?</h1.*?>\s*</div>', '', code, flags=re.DOTALL)

with open("tehi-theme/single-truyen.php", "w", encoding="utf-8") as f:
    f.write(code)

print("Removed ghost text")
