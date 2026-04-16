import ftplib

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    local_func = "temply-ai-factory/temply-ai-factory.php"
    ftp.cwd("/wp-content/plugins/temply-ai-factory/")
    with open(local_func, 'rb') as f:
        ftp.storbinary("STOR temply-ai-factory.php", f)
    print(f"✓ Upload thành công: /wp-content/plugins/temply-ai-factory/temply-ai-factory.php")
    
    ftp.quit()
except Exception as e:
    print("Lỗi:", e)
