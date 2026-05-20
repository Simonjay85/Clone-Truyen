import ftplib
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

modified_files = [
    "tehi-theme/front-page.php",
    "tehi-theme/functions.php",
    "tehi-theme/page-bangxephang.php",
    "tehi-theme/page-completed.php",
    "tehi-theme/page-directory.php",
    "tehi-theme/page-profile.php",
    "tehi-theme/search.php",
    "tehi-theme/single-chuong.php",
    "tehi-theme/single-truyen.php",
    "tehi-theme/taxonomy-the_loai.php"
]

print("=== BẮT ĐẦU UPLOAD CÁC FILE THEME THAY ĐỔI ===")
try:
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    print("✓ Đăng nhập FTP thành công!")
    
    for local in modified_files:
        if not os.path.exists(local):
            print(f"⚠ File không tồn tại: {local}")
            continue
            
        filename = os.path.basename(local)
        remote_path = f"/wp-content/themes/tehi-theme/{local.split('tehi-theme/')[1]}"
        parts = remote_path.rsplit("/", 1)
        
        try:
            ftp.cwd(parts[0])
        except Exception as e:
            print(f"Cố gắng tạo thư mục {parts[0]}...")
            # Tạo thư mục đệ quy
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
except Exception as e:
    print("Lỗi FTP:", e)
