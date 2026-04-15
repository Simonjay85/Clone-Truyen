import ftplib

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    # Upload Theme File
    local1 = "tehi-theme/page-story-studio.php"
    ftp.cwd("/wp-content/themes/tehi-theme/")
    with open(local1, 'rb') as f:
        ftp.storbinary("STOR page-story-studio.php", f)
    print(f"✓ Upload thành công: /wp-content/themes/tehi-theme/page-story-studio.php")
    
    # Upload Plugin File
    local2 = "temply-ai-factory/temply-ai-factory.php"
    ftp.cwd("/wp-content/plugins/temply-ai-factory/")
    with open(local2, 'rb') as f:
        ftp.storbinary("STOR temply-ai-factory.php", f)
    print(f"✓ Upload thành công: /wp-content/plugins/temply-ai-factory/temply-ai-factory.php")
    
    # Upload OpenAI API File
    local3 = "temply-ai-factory/includes/openai-api.php"
    ftp.cwd("/wp-content/plugins/temply-ai-factory/includes/")
    with open(local3, 'rb') as f:
        ftp.storbinary("STOR openai-api.php", f)
    print(f"✓ Upload thành công: /wp-content/plugins/temply-ai-factory/includes/openai-api.php")
    
    ftp.quit()
except Exception as e:
    print("Lỗi:", e)
