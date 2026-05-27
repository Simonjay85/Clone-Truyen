#!/usr/bin/env python3
"""Upload fix_dup_chapters.php to server."""
import ftplib
ftp = ftplib.FTP("51.79.53.190", timeout=30)
ftp.login("alotoinghe", "Nghia234!")
with open("fix_dup_chapters.php", "rb") as f:
    ftp.storbinary("STOR fix_dup_chapters.php", f)
ftp.quit()
print("Uploaded fix_dup_chapters.php")
