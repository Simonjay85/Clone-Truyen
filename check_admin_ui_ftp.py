import ftplib

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    lines = []
    ftp.retrlines('RETR /wp-content/plugins/temply-ai-factory/admin-ui.php', lines.append)
    
    print("\n".join(lines[:20]))
    print(f"Total lines: {len(lines)}")
    ftp.quit()
except Exception as e:
    print("Cannot read log:", e)
