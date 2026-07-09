import ftplib
import urllib.request
import json
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

def main():
    php_code = """<?php
require_once('wp-load.php');
header('Content-Type: application/json');

$post_ids = [7466, 7448];
$results = [];

foreach ($post_ids as $pid) {
    $title = get_the_title($pid);
    $thumb_id = get_post_thumbnail_id($pid);
    $thumb_url = wp_get_attachment_url($thumb_id);
    $results[$pid] = [
        'title' => $title,
        'thumb_id' => $thumb_id,
        'thumb_url' => $thumb_url
    ];
}

echo json_encode($results, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>"""

    temp_file = "temp_check_live_details.php"
    
    print("Uploading temp_check_live_details.php...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(php_code)
        
    with open(temp_file, "rb") as f:
        ftp.storbinary(f"STOR {temp_file}", f)
    ftp.quit()
    print("✓ Uploaded.")
    
    print("Invoking remote script...")
    try:
        req = urllib.request.urlopen(f"https://doctieuthuyet.com/{temp_file}", timeout=60)
        output = req.read().decode('utf-8')
        print("\n=== Live Details Output ===")
        print(output)
        print("===========================\n")
    except Exception as e:
        print("Error invoking remote script:", e)
        
    print("Cleaning up remote file...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.delete(temp_file)
    ftp.quit()
    print("✓ Remote file cleaned up.")
    
    if os.path.exists(temp_file):
        os.remove(temp_file)

if __name__ == "__main__":
    main()
