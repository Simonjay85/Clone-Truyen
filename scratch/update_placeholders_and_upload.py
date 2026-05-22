import os
import ftplib

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
THEME_DIR = "/Users/aaronnguyen/TN/App/doctieuthuyet/tehi-theme"

modified_files = []

print("=== BẮT ĐẦU CẬP NHẬT PHIÊN BẢN PLACEHOLDER (v=2 -> v=3) ===")

# Duyệt tất cả các file PHP trong thư mục theme
for root, dirs, files in os.walk(THEME_DIR):
    for file in files:
        if file.endswith(".php"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            
            if "no-image-cover.png?v=2" in content:
                new_content = content.replace("no-image-cover.png?v=2", "no-image-cover.png?v=3")
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                
                # Tính toán đường dẫn tương đối so với workspace
                rel_path = os.path.relpath(filepath, "/Users/aaronnguyen/TN/App/doctieuthuyet")
                modified_files.append(rel_path)
                print(f"✓ Đã cập nhật file: {rel_path}")

if not modified_files:
    print("⚠ Không tìm thấy file nào cần cập nhật.")
else:
    print(f"\nTìm thấy {len(modified_files)} file cần upload. Bắt đầu upload FTP...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        print("✓ Đăng nhập FTP thành công!")
        
        for local in modified_files:
            filename = os.path.basename(local)
            # Đường dẫn remote tương ứng trong thư mục theme trên server
            # Ví dụ: local = "tehi-theme/front-page.php" -> remote = "/wp-content/themes/tehi-theme/front-page.php"
            theme_part = local.split('tehi-theme/')[1]
            remote_path = f"/wp-content/themes/tehi-theme/{theme_part}"
            parts = remote_path.rsplit("/", 1)
            
            try:
                ftp.cwd(parts[0])
            except Exception as e:
                print(f"Tạo thư mục {parts[0]}...")
                current_dir = ""
                for folder in parts[0].split("/"):
                    if not folder:
                        continue
                    current_dir += f"/{folder}"
                    try:
                        ftp.cwd(current_dir)
                    except:
                        ftp.mkd(current_dir)
                ftp.cwd(parts[0])
                
            with open(local, 'rb') as f:
                ftp.storbinary(f'STOR {parts[1]}', f)
            print(f"✓ Đã upload: {local} -> {remote_path}")
            
        ftp.quit()
        print("=== UPLOAD THÀNH CÔNG TOÀN BỘ FILE THEME ===")
        
        # Gọi script clear cache trên server để cập nhật thay đổi ngay lập tức
        import requests
        print("\n=== ĐANG XOÁ CACHE LITESPEED TRÊN SERVER ===")
        r = requests.get("https://doctieuthuyet.com/wp-content/themes/tehi-theme/clear_lscache.php", timeout=15)
        print("Kết quả xoá cache:", r.text.strip())
        
    except Exception as e:
        print("Lỗi FTP hoặc API:", e)
