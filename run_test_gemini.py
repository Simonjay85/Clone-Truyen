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
require_once(ABSPATH . 'wp-content/plugins/temply-ai-factory/includes/openai-api.php');

$sys = "You are a helpful assistant.";
$user = "Say hello in Vietnamese.";

$res = temply_call_gemini($sys, $user, 0.7);
if (is_wp_error($res)) {
    echo json_encode(["success" => false, "error" => $res->get_error_message()]);
} else {
    echo json_encode(["success" => true, "result" => $res]);
}
?>"""

    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("temp_test_gemini.php", "w", encoding="utf-8") as f:
        f.write(php_code)
    
    with open("temp_test_gemini.php", "rb") as f:
        ftp.storbinary("STOR temp_test_gemini.php", f)
    ftp.quit()

    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_test_gemini.php", timeout=30)
        data = req.read().decode('utf-8')
        print(data)
    except Exception as e:
        print("Error:", e)
    finally:
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        try:
            ftp.delete("temp_test_gemini.php")
        except:
            pass
        ftp.quit()
        if os.path.exists("temp_test_gemini.php"):
            os.remove("temp_test_gemini.php")

if __name__ == "__main__":
    run()
