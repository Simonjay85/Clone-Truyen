import ftplib
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

try:
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    print("✓ Logged into FTP.")
    
    local_file = "scratch/update_story.php"
    remote_file = "update_story.php"
    
    with open(local_file, "rb") as f:
        ftp.storbinary(f"STOR {remote_file}", f)
        
    print(f"✓ Uploaded {local_file} as {remote_file} successfully!")
    ftp.quit()
except Exception as e:
    print("❌ FTP upload failed:", e)
