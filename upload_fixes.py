import ftplib

files_to_upload = [
    ("tehi-theme/header.php", "/wp-content/themes/tehi-theme/header.php"),
    ("tehi-theme/footer.php", "/wp-content/themes/tehi-theme/footer.php"),
    ("tehi-theme/single-truyen.php", "/wp-content/themes/tehi-theme/single-truyen.php"),
    ("tehi-theme/single-chuong.php", "/wp-content/themes/tehi-theme/single-chuong.php"),
]

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    for local, remote in files_to_upload:
        parts = remote.rsplit("/", 1)
        ftp.cwd("/")
        if len(parts) > 1:
            for folder in parts[0][1:].split('/'):
                try:
                    ftp.cwd(folder)
                except:
                    pass
        with open(local, 'rb') as f:
            ftp.storbinary(f'STOR {parts[1]}', f)
        print(f"✓ {local}")
    ftp.quit()
    print("Upload completed!")
except Exception as e:
    print(f"Lỗi: {e}")
