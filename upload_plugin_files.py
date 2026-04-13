import ftplib
import os
import glob

# Upload temply-ai-factory files
plugin_files = glob.glob("temply-ai-factory/**/*.php", recursive=True) + glob.glob("temply-ai-factory/**/*.js", recursive=True) + glob.glob("temply-ai-factory/**/*.css", recursive=True)

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    for local in plugin_files:
        filename = os.path.basename(local)
        remote_path = f"/wp-content/plugins/temply-ai-factory/{local.split('temply-ai-factory/')[1]}"
        
        parts = remote_path.rsplit("/", 1)
        try:
            ftp.cwd(parts[0])
        except:
            # We might have to make multiple dirs, but usually just 1 level
            try:
                ftp.mkd(parts[0])
                ftp.cwd(parts[0])
            except:
                pass # skip if multi-level fails for now
                
        with open(local, 'rb') as f:
            ftp.storbinary(f'STOR {parts[1]}', f)
        print(f"✓ {local} -> {remote_path}")
        
    ftp.quit()
    print("Xong Upload Plugin!")
except Exception as e:
    print("Loi:", e)
