import ftplib
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
LOCAL_BASE = "tehi-theme"
REMOTE_BASE = "/wp-content/themes/tehi-theme"

ftp = ftplib.FTP(FTP_HOST)
ftp.login(FTP_USER, FTP_PASS)

def ensure_dir(ftp, path):
    try:
        ftp.mkd(path)
    except:
        pass # already exists

def upload_dir(ftp, local_dir, remote_dir):
    ensure_dir(ftp, remote_dir)
    for item in os.listdir(local_dir):
        local_path = os.path.join(local_dir, item)
        remote_path = remote_dir + "/" + item
        if os.path.isdir(local_path):
            upload_dir(ftp, local_path, remote_path)
        else:
            try:
                ftp.cwd(remote_dir)
                with open(local_path, 'rb') as f:
                    ftp.storbinary(f'STOR {item}', f)
                print(f"✓ {remote_path}")
            except Exception as e:
                print(f"✗ {remote_path}: {e}")

# Upload templates/ folder
upload_dir(ftp, "tehi-theme/templates", REMOTE_BASE + "/templates")

# Also upload fonts folder if exists
if os.path.exists("tehi-theme/templates/fonts"):
    upload_dir(ftp, "tehi-theme/templates/fonts", REMOTE_BASE + "/templates/fonts")

ftp.quit()
print("\nXong!")
