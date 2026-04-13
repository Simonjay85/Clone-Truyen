import ftplib
try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    # Check .htaccess content on server
    lines = []
    ftp.retrlines('RETR .htaccess', lines.append)
    print("Current .htaccess content:")
    print("\n".join(lines))
    
    # Check file size
    size = ftp.size('.htaccess')
    print("\nFile size:", size, "bytes")
    ftp.quit()
except Exception as e:
    print("Error:", e)
