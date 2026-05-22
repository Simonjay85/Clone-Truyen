#!/usr/bin/env python3
import ftplib
import os

print("Starting cover assets upload...")

files_to_upload = [
    ("scratch/3724_final.png", "/wp-content/themes/tehi-theme/temp_cover_3724.png"),
    ("scratch/update_cover_3724.php", "/wp-content/themes/tehi-theme/update_cover_3724.php"),
]

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    for local, remote in files_to_upload:
        if not os.path.exists(local):
            print(f"❌ Local file does not exist: {local}")
            continue
            
        print(f"Uploading {local} to {remote}...")
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
        print(f"✓ Uploaded {local} successfully!")
        
    ftp.quit()
    print("Upload completed successfully!")
except Exception as e:
    print(f"❌ FTP Error: {e}")
