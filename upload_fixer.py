import ftplib

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    with open("delete_specific.php", 'rb') as f:
        ftp.storbinary("STOR delete_specific.php", f)
        
    print("✓ Upload delete_specific.php thành công!")
    ftp.quit()
except Exception as e:
    print("Lỗi:", e)
