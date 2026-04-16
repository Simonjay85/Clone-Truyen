import ftplib

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    # Upload Theme Functions
    local_func = "temply-ai-factory/admin-ui.php"
    ftp.cwd("/wp-content/plugins/temply-ai-factory/")
    with open(local_func, 'rb') as f:
        ftp.storbinary("STOR admin-ui.php", f)
    print(f"✓ Upload thành công: /wp-content/plugins/temply-ai-factory/admin-ui.php")
    
    ftp.quit()
except Exception as e:
    print("Lỗi:", e)
