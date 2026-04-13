import ftplib
import os
import glob

# Upload tehi-theme files
theme_files = glob.glob("tehi-theme/**/*.php", recursive=True) + glob.glob("tehi-theme/**/*.js", recursive=True) + glob.glob("tehi-theme/**/*.css", recursive=True)

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    for local in theme_files:
        # Create remote path
        filename = os.path.basename(local)
        remote_path = f"/wp-content/themes/tehi-theme/{local.split('tehi-theme/')[1]}"
        
        parts = remote_path.rsplit("/", 1)
        # Attempt to change to remote directory, create it if missing
        try:
            ftp.cwd(parts[0])
        except:
            ftp.mkd(parts[0])
            ftp.cwd(parts[0])
            
        with open(local, 'rb') as f:
            ftp.storbinary(f'STOR {parts[1]}', f)
        print(f"✓ {local} -> {remote_path}")
        
    ftp.quit()
    print("Xong Upload Theme!")
except Exception as e:
    print("Loi:", e)
