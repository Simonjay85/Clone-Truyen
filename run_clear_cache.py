import ftplib
import urllib.request

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    with open('tehi-theme/clear_lscache.php', 'rb') as f:
        ftp.storbinary('STOR /wp-content/themes/tehi-theme/clear_lscache.php', f)
    print("Uploaded clear_lscache.php")
    ftp.quit()

    req = urllib.request.urlopen("https://doctieuthuyet.com/wp-content/themes/tehi-theme/clear_lscache.php")
    print(req.read().decode('utf-8'))

except Exception as e:
    print("Error:", e)
