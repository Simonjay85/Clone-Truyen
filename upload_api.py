import ftplib
try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    local_func = "temply-ai-factory/includes/openai-api.php"
    ftp.cwd("/wp-content/plugins/temply-ai-factory/includes/")
    with open(local_func, 'rb') as f:
        ftp.storbinary("STOR openai-api.php", f)
    print(f"✓ Upload thành công: openai-api.php")
    
    ftp.quit()
except Exception as e:
    print("Lỗi:", e)
