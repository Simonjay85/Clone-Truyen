import ftplib

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    ftp.cwd("/wp-content/plugins/tehi-crawler-manager/admin")
    with open("tehi-crawler-manager/admin/fetch_tool.php", 'rb') as f:
        ftp.storbinary('STOR fetch_tool.php', f)
    ftp.quit()
    print("Done uploading fetch_tool.php")
except Exception as e:
    print(e)
