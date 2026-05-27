import ftplib
import urllib.request
import json
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

def run():
    php_code = """<?php
require('./wp-load.php');
$openai = get_option('temply_openai_api_key', '');
$gemini_paid = get_option('temply_gemini_api_key', '');
$gemini_free = get_option('temply_gemini_api_key_free', '');
$claude = get_option('temply_claude_api_key', '');

echo json_encode([
    'openai' => empty($openai) ? 'empty' : 'set (ends with ' . substr($openai, -5) . ')',
    'gemini_paid' => empty($gemini_paid) ? 'empty' : 'set',
    'gemini_free' => empty($gemini_free) ? 'empty' : 'set',
    'claude' => empty($claude) ? 'empty' : 'set'
]);
?>"""

    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("temp_test_keys.php", "w", encoding="utf-8") as f:
        f.write(php_code)
    
    with open("temp_test_keys.php", "rb") as f:
        ftp.storbinary("STOR temp_test_keys.php", f)
    ftp.quit()

    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_test_keys.php", timeout=30)
        data = req.read().decode('utf-8')
        print(data)
    except Exception as e:
        print("Error:", e)
    finally:
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        try:
            ftp.delete("temp_test_keys.php")
        except:
            pass
        ftp.quit()
        if os.path.exists("temp_test_keys.php"):
            os.remove("temp_test_keys.php")

if __name__ == "__main__":
    run()
