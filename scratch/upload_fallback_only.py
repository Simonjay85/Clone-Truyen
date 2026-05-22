import ftplib
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
LOCAL_FILE = "tehi-theme/img_data/images/no-image-cover.png"
REMOTE_DIR = "/wp-content/themes/tehi-theme/img_data/images"
REMOTE_FILE = "no-image-cover.png"

try:
    print("Connecting to FTP...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    
    print(f"Navigating to {REMOTE_DIR}...")
    ftp.cwd(REMOTE_DIR)
    
    print(f"Uploading {LOCAL_FILE} to {REMOTE_FILE}...")
    with open(LOCAL_FILE, 'rb') as f:
        ftp.storbinary(f'STOR {REMOTE_FILE}', f)
        
    print("Upload complete!")
    ftp.quit()
except Exception as e:
    print("Error:", e)
