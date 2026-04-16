import ftplib
import urllib.request

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    ftp.cwd("/wp-content/themes/tehi-theme/")
    
    with open("tehi-theme/update_excerpt.php", 'rb') as f:
        ftp.storbinary("STOR update_excerpt.php", f)
        
    with open("tehi-theme/single-truyen.php", 'rb') as f:
        ftp.storbinary("STOR single-truyen.php", f)
        
    print(f"✓ Upload thành công")
    ftp.quit()

    req = urllib.request.urlopen("https://doctieuthuyet.com/wp-content/themes/tehi-theme/update_excerpt.php")
    print(req.read().decode('utf-8'))

except Exception as e:
    print("Lỗi:", e)
