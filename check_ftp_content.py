import ftplib
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

try:
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    content = []
    ftp.retrlines('RETR /wp-content/plugins/tehi-crawler-manager/admin/dashboard.php', content.append)
    content_str = "\n".join(content)
    if "fetch_tool.php" in content_str:
        print("YES! fetch_tool.php inclusion was found on the remote server!")
    else:
        print("NO! The file on the remote server is WRONG!")
        
    theme_content = []
    ftp.retrlines('RETR /wp-content/themes/tehi-theme/index.php', theme_content.append)
    theme_str = "\n".join(theme_content)
    if "_views" in theme_str:
        print("YES! _views is in the remote theme index.php!")
    else:
        print("NO! The remote theme index.php is wrong!")
    ftp.quit()
except Exception as e:
    print("Error:", e)
