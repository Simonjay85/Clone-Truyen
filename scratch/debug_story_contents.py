import ftplib
import urllib.request
import os
import json

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

PHP_CODE = """<?php
require('./wp-load.php');
header('Content-Type: application/json');

$args = [
    'post_type' => 'truyen',
    'posts_per_page' => 5,
    'post_status' => 'publish'
];
$query = new WP_Query($args);
$results = [];

foreach ($query->posts as $post) {
    $results[] = [
        'id' => $post->ID,
        'title' => $post->post_title,
        'raw_content_preview' => mb_substr($post->post_content, 0, 400),
        'clean_content_preview' => mb_substr(strip_tags($post->post_content), 0, 200)
    ];
}

echo json_encode($results, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>"""

def main():
    temp_file = "temp_debug_content.php"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(PHP_CODE)
        
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(temp_file, "rb") as f:
        ftp.storbinary(f"STOR {temp_file}", f)
    ftp.quit()
    
    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_debug_content.php")
        print(req.read().decode('utf-8'))
    except Exception as e:
        print("Error:", e)
        
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.delete(temp_file)
    ftp.quit()
    
    if os.path.exists(temp_file):
        os.remove(temp_file)

if __name__ == "__main__":
    main()
