import ftplib
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
LOCAL_DIR = "tehi-crawler-manager"
REMOTE_DIR = "/wp-content/plugins/tehi-crawler-manager"

def ftp_upload_dir(ftp, local_dir, remote_dir):
    try:
        ftp.mkd(remote_dir)
    except Exception as e:
        pass # Directory probably exists

    ftp.cwd(remote_dir)
    for root, dirs, files in os.walk(local_dir):
        # Calculate relative path
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

ftp = ftplib.FTP(FTP_HOST)
ftp.login(FTP_USER, FTP_PASS)
ftp_upload_dir(ftp, LOCAL_DIR, REMOTE_DIR)
ftp.quit()
print("FTP Upload Complete!")
