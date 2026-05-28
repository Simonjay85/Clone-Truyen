#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_ftp_sizes.py — Connect to FTP and check the sizes of jquery.min.js and sweetalert2.min.js on the server.
"""

import ftplib

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

def main():
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    
    files_to_check = [
        "/wp-content/themes/tehi-theme/assets/js/jquery.min.js",
        "/wp-content/themes/tehi-theme/templates/module/sweetalert/sweetalert2.min.js",
        "/wp-content/themes/tehi-theme/front-page.php"
    ]
    
    print("Checking remote file sizes on FTP...")
    for remote in files_to_check:
        try:
            size = ftp.size(remote)
            print(f"✓ {remote} -> {size} bytes")
        except Exception as e:
            print(f"❌ {remote} -> Error: {e}")
            
    ftp.quit()

if __name__ == "__main__":
    main()
