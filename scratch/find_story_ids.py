import urllib.request
import ftplib
import os
import json

php_code = """<?php
require('./wp-load.php');

$slugs = [
    'noi-nhuc-bi-xua-duoi-o-dao-yen-ky-su-lat-keo-bang-chung-thu-pasteur-dap-tan-tap-doan-yen-gia-nghin-ty',
    'chang-re-nuoi-tom-hum-bi-gia-dinh-vo-khinh-re-lat-keo-thau-tom-tap-doan-thuy-san-nghin-ty'
];

$results = [];
foreach ($slugs as $slug) {
    $posts = get_posts([
        'post_type' => 'truyen',
        'name' => $slug,
        'posts_per_page' => 1
    ]);
    if (!empty($posts)) {
        $results[$slug] = $posts[0]->ID;
    } else {
        // Fallback search by containing title keyword
        $keyword = (strpos($slug, 'yen') !== false) ? 'Đảo Yến' : 'Tôm Hùm';
        $fallback = get_posts([
            'post_type' => 'truyen',
            's' => $keyword,
            'posts_per_page' => 1
        ]);
        if (!empty($fallback)) {
            $results[$slug] = $fallback[0]->ID;
        } else {
            $results[$slug] = "NOT_FOUND";
        }
    }
}

header('Content-Type: application/json');
echo json_encode($results, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>"""

def main():
    print("Writing temp_find_ids.php...")
    with open("temp_find_ids.php", "w", encoding="utf-8") as f:
        f.write(php_code)
        
    print("Uploading via FTP...")
    try:
        ftp = ftplib.FTP("51.79.53.190")
        ftp.login("alotoinghe", "Nghia234!")
        with open("temp_find_ids.php", "rb") as f:
            ftp.storbinary("STOR temp_find_ids.php", f)
        ftp.quit()
        
        print("Querying endpoint...")
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_find_ids.php")
        print("Story IDs:")
        print(req.read().decode('utf-8'))
        
        # Cleanup
        ftp = ftplib.FTP("51.79.53.190")
        ftp.login("alotoinghe", "Nghia234!")
        ftp.delete("temp_find_ids.php")
        ftp.quit()
        
        if os.path.exists("temp_find_ids.php"):
            os.remove("temp_find_ids.php")
            
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
