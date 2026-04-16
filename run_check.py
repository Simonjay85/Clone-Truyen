import ftplib
import urllib.request

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    ftp.cwd("/wp-content/themes/tehi-theme/")
    with open("check_stories.php", 'rb') as f:
        ftp.storbinary("STOR check_stories.php", f)
        
    print(f"✓ Upload thành công")
    ftp.quit()

    req = urllib.request.urlopen("https://doctieuthuyet.com/wp-content/themes/tehi-theme/check_stories.php")
    print(req.read().decode('utf-8'))

except Exception as e:
    print("Lỗi:", e)
