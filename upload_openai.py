import ftplib
import urllib.request

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    ftp.cwd("/wp-content/plugins/temply-ai-factory/includes/")
    
    with open("temply-ai-factory/includes/openai-api.php", 'rb') as f:
        ftp.storbinary("STOR openai-api.php", f)
        
    print(f"✓ Upload thành công openai-api.php")
    ftp.quit()

except Exception as e:
    print("Lỗi:", e)
