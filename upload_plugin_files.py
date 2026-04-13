import ftplib
import os
import glob

# Upload temply-ai-factory files
plugin_files = glob.glob("temply-ai-factory/**/*.php", recursive=True) + glob.glob("temply-ai-factory/**/*.js", recursive=True)

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    for local in plugin_files:
        # Create remote path
        filename = os.path.basename(local)
        # Handle specific folder structures like includes/ or assets/
        remote_path = f"/wp-content/plugins/temply-ai-factory/{local.split('temply-ai-factory/')[1]}"
        
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
    print("Xong!")
except Exception as e:
    print("Loi:", e)
