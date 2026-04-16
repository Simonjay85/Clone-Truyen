import ftplib
import urllib.request

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    local_func = "tehi-theme/clear_queue.php"
    ftp.cwd("/wp-content/themes/tehi-theme/")
    with open(local_func, 'rb') as f:
        ftp.storbinary("STOR clear_queue.php", f)
    print(f"✓ Upload thành công")
    
    ftp.quit()

    req = urllib.request.urlopen("https://doctieuthuyet.com/wp-content/themes/tehi-theme/clear_queue.php")
    print(req.read().decode('utf-8'))

except Exception as e:
    print("Lỗi:", e)
