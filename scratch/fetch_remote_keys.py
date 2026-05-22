import ftplib
import requests
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

def main():
    # 1. Create the temp php file
    php_content = """<?php
require_once('wp-load.php');
echo "GEMINI_KEY:" . get_option('temply_gemini_api_key', '') . "\\n";
echo "GEMINI_FREE_KEY:" . get_option('temply_gemini_api_key_free', '') . "\\n";
echo "OPENAI_KEY:" . get_option('temply_openai_api_key', '') . "\\n";
echo "CLAUDE_KEY:" . get_option('temply_claude_api_key', '') . "\\n";
?>"""
    
    with open("fetch_keys_temp.php", "w") as f:
        f.write(php_content)
        
    print("Uploading fetch_keys_temp.php to FTP root...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        with open("fetch_keys_temp.php", "rb") as f:
            ftp.storbinary("STOR fetch_keys_temp.php", f)
        ftp.quit()
        print("✓ Uploaded successfully.")
        
        print("Executing script on remote server...")
        res = requests.get(f"{WP_URL}/fetch_keys_temp.php", timeout=30)
        print("="*40)
        print("REMOTE KEYS OUTPUT:")
        print(res.text)
        print("="*40)
        
    except Exception as e:
        print("Error during execution:", e)
    finally:
        # Clean up local
        if os.path.exists("fetch_keys_temp.php"):
            os.remove("fetch_keys_temp.php")
            
        print("Cleaning up remote file...")
        try:
            ftp = ftplib.FTP(FTP_HOST, timeout=30)
            ftp.login(FTP_USER, FTP_PASS)
            ftp.delete("fetch_keys_temp.php")
            ftp.quit()
            print("✓ Remote cleanup completed.")
        except Exception as e:
            print("Remote cleanup error:", e)

if __name__ == "__main__":
    main()
