import os, glob

# Fix header body classes
for header in ["tehi-theme/header.php", "tehi-theme/header-home.php"]:
    with open(header, "r", encoding="utf-8") as f:
        code = f.read()
    if 'flex flex-col min-h-screen' not in code:
        code = code.replace('<body class="', '<body class="flex flex-col min-h-screen ')
    with open(header, "w", encoding="utf-8") as f:
        f.write(code)

# Fix main tags
for tpl in glob.glob("tehi-theme/*.php"):
    with open(tpl, "r", encoding="utf-8") as f:
        code = f.read()
    if '<main class="' in code and 'flex-grow' not in code:
        code = code.replace('<main class="', '<main class="flex-grow ')
        with open(tpl, "w", encoding="utf-8") as f:
            f.write(code)

print("Fixed footer whitespace")
