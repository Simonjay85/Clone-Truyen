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

function get_story_chaps($id) {
    $chaps = get_posts([
        'post_type' => 'chuong',
        'meta_key' => '_truyen_id',
        'meta_value' => $id,
        'posts_per_page' => -1,
        'orderby' => 'menu_order date',
        'order' => 'ASC'
    ]);
    $res = [];
    foreach($chaps as $c) {
        $res[] = [
            'id' => $c->ID,
            'title' => $c->post_title,
            'date' => $c->post_date,
            'content_len' => mb_strlen(wp_strip_all_tags($c->post_content), 'utf-8')
        ];
    }
    return $res;
}

echo json_encode([
    'story_2710' => [
        'title' => get_post(2710)->post_title,
        'date' => get_post(2710)->post_date,
        'chapters' => get_story_chaps(2710)
    ],
    'story_2703' => [
        'title' => get_post(2703)->post_title,
        'date' => get_post(2703)->post_date,
        'chapters' => get_story_chaps(2703)
    ]
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>"""

    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("temp_inspect_duplicates.php", "w", encoding="utf-8") as f:
        f.write(php_code)
    
    with open("temp_inspect_duplicates.php", "rb") as f:
        ftp.storbinary("STOR temp_inspect_duplicates.php", f)
    ftp.quit()

    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_inspect_duplicates.php", timeout=30)
        data = req.read().decode('utf-8')
        print(data)
    except Exception as e:
        print("Error:", e)
    finally:
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        try:
            ftp.delete("temp_inspect_duplicates.php")
        except:
            pass
        ftp.quit()
        if os.path.exists("temp_inspect_duplicates.php"):
            os.remove("temp_inspect_duplicates.php")

if __name__ == "__main__":
    run()
