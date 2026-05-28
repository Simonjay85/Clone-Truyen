import ftplib
import hashlib

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

files = [
    ("/wp-content/themes/tehi-theme/header.php", "scratch/remote_header.php", "/Users/aaronnguyen/TN/App/doctieuthuyet/tehi-theme/header.php"),
    ("/wp-content/themes/tehi-theme/footer.php", "scratch/remote_footer.php", "/Users/aaronnguyen/TN/App/doctieuthuyet/tehi-theme/footer.php"),
]

try:
    print("Connecting to FTP...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    
    for remote, local_temp, local_real in files:
        print(f"Downloading {remote}...")
        with open(local_temp, "wb") as f:
            ftp.retrbinary(f"RETR {remote}", f.write)
            
        with open(local_real, "r", encoding="utf-8") as f:
            real_content = f.read()
        with open(local_temp, "r", encoding="utf-8") as f:
            temp_content = f.read()
            
        real_md5 = hashlib.md5(real_content.encode('utf-8')).hexdigest()
        temp_md5 = hashlib.md5(temp_content.encode('utf-8')).hexdigest()
        
        print(f"File: {remote}")
        print(f"  Local size:  {len(real_content)} bytes, MD5: {real_md5}")
        print(f"  Remote size: {len(temp_content)} bytes, MD5: {temp_md5}")
        if real_md5 == temp_md5:
            print("  ✅ MATCH!")
        else:
            print("  ⚠️ MISMATCH!")
            
    ftp.quit()
except Exception as e:
    print("Error:", e)
