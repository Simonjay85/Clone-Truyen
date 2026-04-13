import ftplib

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    # Try reading the wp-content/debug.log
    lines = []
    ftp.retrlines('RETR /wp-content/debug.log', lines.append)
    
    for line in lines[-50:]:  # Check last 50 lines
        print(line)
        
    ftp.quit()
except Exception as e:
    print("Cannot read log:", e)
