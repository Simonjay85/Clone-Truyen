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
$t = get_post(3954);
if (!$t) {
    echo json_encode(["error" => "Post 3954 not found"]);
    exit;
}
echo json_encode([
    'title' => $t->post_title,
    'excerpt' => $t->post_excerpt,
    'content' => $t->post_content,
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>"""

    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("temp_inspect.php", "w", encoding="utf-8") as f:
        f.write(php_code)
    
    with open("temp_inspect.php", "rb") as f:
        ftp.storbinary("STOR temp_inspect.php", f)
    ftp.quit()

    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_inspect.php", timeout=30)
        data = req.read().decode('utf-8')
        print(data)
    except Exception as e:
        print("Error:", e)
    finally:
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("temp_inspect.php")
        ftp.quit()
        if os.path.exists("temp_inspect.php"):
            os.remove("temp_inspect.php")

if __name__ == "__main__":
    run()
