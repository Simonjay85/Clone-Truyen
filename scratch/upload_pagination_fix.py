import ftplib
import os
import requests

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

def upload_file(local_path, remote_path):
    print(f"Uploading {local_path} to {remote_path}...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    
    parts = remote_path.rsplit("/", 1)
    try:
        ftp.cwd(parts[0])
    except Exception:
        ftp.mkd(parts[0])
        ftp.cwd(parts[0])
        
    with open(local_path, 'rb') as f:
        ftp.storbinary(f'STOR {parts[1]}', f)
        
    ftp.quit()
    print(f"✓ Uploaded successfully!")

def main():
    # File 1: taxonomy-the_loai.php
    local_tax = "/Users/aaronnguyen/TN/App/doctieuthuyet/tehi-theme/taxonomy-the_loai.php"
    remote_tax = "/wp-content/themes/tehi-theme/taxonomy-the_loai.php"
    upload_file(local_tax, remote_tax)
    
    # File 2: page-directory.php
    local_dir = "/Users/aaronnguyen/TN/App/doctieuthuyet/tehi-theme/page-directory.php"
    remote_dir = "/wp-content/themes/tehi-theme/page-directory.php"
    upload_file(local_dir, remote_dir)
    
    # Purge Cache
    print("Purging LiteSpeed cache...")
    try:
        r = requests.get("https://doctieuthuyet.com/wp-content/themes/tehi-theme/clear_lscache.php", timeout=15)
        print("Purge response:", r.text)
    except Exception as e:
        print("Could not trigger cache purge directly:", e)

if __name__ == "__main__":
    main()
