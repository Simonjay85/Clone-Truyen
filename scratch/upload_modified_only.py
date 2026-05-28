#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
upload_modified_only.py — Instantly upload only the modified files (header.php and page-latest.php) to the FTP server.
"""

import ftplib
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

def main():
    modified_files = [
        "tehi-theme/header.php",
        "tehi-theme/page-latest.php"
    ]
    
    print("🚀 Starting instant upload of modified files...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        
        for local in modified_files:
            remote_path = f"/wp-content/themes/tehi-theme/{local.split('tehi-theme/')[1]}"
            remote_dir = os.path.dirname(remote_path)
            remote_file = os.path.basename(remote_path)
            
            # Navigate to directory
            ftp.cwd(remote_dir)
            
            with open(local, 'rb') as f:
                ftp.storbinary(f'STOR {remote_file}', f)
            print(f"✓ Uploaded: {local} -> {remote_path}")
            
        ftp.quit()
        print("🎉 SUCCESS! Instantly deployed all modified files.")
    except Exception as e:
        print("❌ Upload Error:", e)

if __name__ == "__main__":
    main()
