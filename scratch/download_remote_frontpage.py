import ftplib

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
REMOTE_FILE = "/wp-content/themes/tehi-theme/front-page.php"
LOCAL_FILE = "scratch/remote_front-page.php"

try:
    print("Connecting to FTP...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    
    print(f"Downloading {REMOTE_FILE}...")
    with open(LOCAL_FILE, "wb") as f:
        ftp.retrbinary(f"RETR {REMOTE_FILE}", f.write)
        
    print(f"Successfully downloaded to {LOCAL_FILE}")
    ftp.quit()
except Exception as e:
    print("Error:", e)
