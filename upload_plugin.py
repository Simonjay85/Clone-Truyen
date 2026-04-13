import os
import ftplib

PLUGIN_DIR = "temply-ai-factory"
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
REMOTE_BASE = "/wp-content/plugins/temply-ai-factory"

try:
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    
    # Ensure remote base dir exists
    ftp.cwd("/")
    for folder in REMOTE_BASE[1:].split('/'):
        try:
            ftp.cwd(folder)
        except:
            ftp.mkd(folder)
            ftp.cwd(folder)
    
    # Upload files
    for root, dirs, files in os.walk(PLUGIN_DIR):
        for d in dirs:
            rel_dir = os.path.relpath(os.path.join(root, d), PLUGIN_DIR).replace("\\\\", "/")
            ftp.cwd("/")
            current = REMOTE_BASE
            for p in rel_dir.split("/"):
                current += f"/{p}"
                try:
                    ftp.cwd(current)
                except:
                    ftp.mkd(current)
                    
        for file in files:
            if file.endswith('.DS_Store'): continue
            local_path = os.path.join(root, file)
            rel_path = os.path.relpath(local_path, PLUGIN_DIR).replace("\\\\", "/")
            remote_path = f"{REMOTE_BASE}/{rel_path}"
            
            parts = remote_path.rsplit("/", 1)
            ftp.cwd("/")
            for folder in parts[0][1:].split('/'):
                try:
                    ftp.cwd(folder)
                except:
                    pass
            
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {parts[1]}', f)
            print(f"✓ {local_path} -> {remote_path}")
            
    ftp.quit()
    print("Plugin Upload completed!")
except Exception as e:
    print(f"Lỗi: {e}")

