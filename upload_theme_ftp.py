import ftplib
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
LOCAL_DIR = "tehi-theme"
REMOTE_DIR = "/wp-content/themes/tehi-theme"

def ftp_upload_dir(ftp, local_dir, remote_dir):
    try:
        ftp.mkd(remote_dir)
    except:
        pass
    ftp.cwd(remote_dir)
    for root, dirs, files in os.walk(local_dir):
        rel_path = os.path.relpath(root, local_dir)
        if rel_path == '.':
            target_dir = remote_dir
        else:
            target_dir = f"{remote_dir}/{rel_path.replace(os.path.sep, '/')}"
            try:
                ftp.mkd(target_dir)
            except:
                pass
        
        ftp.cwd(target_dir)
        for fname in files:
            local_path = os.path.join(root, fname)
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {fname}', f)
                print(f"Uploaded: {target_dir}/{fname}")

try:
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    ftp_upload_dir(ftp, LOCAL_DIR, REMOTE_DIR)
    ftp.quit()
    print("Theme FTP Upload Complete!")
except Exception as e:
    print(e)
