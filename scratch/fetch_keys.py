#!/usr/bin/env python3
import requests
import ftplib
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

PHP_HELPER = """<?php
require_once('wp-load.php');
echo "KEY:" . get_option('temply_openai_api_key', '');
?>"""

def main():
    print("Uploading get_key_helper.php...")
    with open("get_key_helper.php", "w") as f:
        f.write(PHP_HELPER)
        
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        with open("get_key_helper.php", "rb") as f:
            ftp.storbinary("STOR get_key_helper.php", f)
        ftp.quit()
        print("✓ Uploaded get_key_helper.php")
        
        print("Fetching key...")
        res = requests.get(f"{WP_URL}/get_key_helper.php", timeout=30)
        print("Response:", res.text)
    except Exception as e:
        print("Error:", e)
    finally:
        if os.path.exists("get_key_helper.php"):
            os.remove("get_key_helper.php")
            
        print("Cleaning up remote helper...")
        try:
            ftp = ftplib.FTP(FTP_HOST, timeout=30)
            ftp.login(FTP_USER, FTP_PASS)
            ftp.delete("get_key_helper.php")
            ftp.quit()
            print("✓ Deleted get_key_helper.php from server")
        except Exception as e:
            print("Cleanup error:", e)

if __name__ == "__main__":
    main()
