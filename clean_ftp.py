import ftplib
try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    ftp.cwd("/")
    ftp.delete("test_db.php")
    ftp.delete("test_wp.php")
    ftp.delete("test_wp2.php")
    ftp.quit()
    print("Cleaned up FTP test files")
except Exception as e:
    print("Error:", e)
