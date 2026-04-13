def fix_header(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Danh mục -> /danh-muc
    content = content.replace('href="#">Danh mục', 'href="/danh-muc">Danh mục')
    content = content.replace('href="#">Danh Mục', 'href="/danh-muc">Danh Mục')
    
    # Truyện mới cập nhật -> /truyen-moi
    content = content.replace('href="#">Truyện mới', 'href="/truyen-moi">Truyện mới')
    content = content.replace('href="#">Truyện mới cập nhật', 'href="/truyen-moi">Truyện mới')
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

fix_header("tehi-theme/header.php")
fix_header("tehi-theme/header-home.php")
print("Headers fixed")

