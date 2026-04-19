import ftplib
import os

files_to_upload = [
    "tehi-theme/page-bxh.php",
    "tehi-theme/page-completed.php"
]

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    remote_dir = "/wp-content/themes/tehi-theme"
    try:
        ftp.cwd(remote_dir)
    except:
        pass
        
    for local_file in files_to_upload:
        filename = os.path.basename(local_file)
        with open(local_file, 'rb') as f:
            ftp.storbinary(f'STOR {filename}', f)
        print(f"Uploaded {filename}")
        
    ftp.quit()
    print("Done uploading aspect ratio fixes.")
except Exception as e:
    print("Error:", e)
