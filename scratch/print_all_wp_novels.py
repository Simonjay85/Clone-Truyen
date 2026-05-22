import ftplib
import urllib.request
import json

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

PHP_CODE = """<?php
require_once('wp-load.php');
$truyens = get_posts([
    'post_type' => 'truyen',
    'posts_per_page' => -1,
    'post_status' => 'any',
    'orderby' => 'date',
    'order' => 'DESC'
]);

$list = [];
foreach ($truyens as $t) {
    $chapters = get_posts([
        'post_type' => 'chuong',
        'meta_key' => '_truyen_id',
        'meta_value' => $t->ID,
        'posts_per_page' => -1,
        'fields' => 'ids'
    ]);
    
    $list[] = [
        'id' => $t->ID,
        'title' => $t->post_title,
        'status' => $t->post_status,
        'date' => $t->post_date,
        'slug' => $t->post_name,
        'chapters_count' => count($chapters)
    ];
}
echo json_encode($list, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>"""

def main():
    temp_file = "temp_print_all_wp_novels.php"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(PHP_CODE)
        
    print("Uploading temp_print_all_wp_novels.php via FTP...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(temp_file, "rb") as f:
        ftp.storbinary(f"STOR {temp_file}", f)
    ftp.quit()
    
    print("Executing query...")
    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_print_all_wp_novels.php", timeout=60)
        data = json.loads(req.read().decode('utf-8'))
        print(f"Total stories queried: {len(data)}")
        
        for idx, item in enumerate(data):
            print(f"{idx+1:02d}. ID: {item['id']} | Chapters: {item['chapters_count']} | Status: {item['status']} | Date: {item['date']} | Title: {item['title']}")
            
    except Exception as e:
        print("Error during execution:", e)
        
    print("Cleaning up...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.delete(temp_file)
    ftp.quit()
    print("Done.")

if __name__ == "__main__":
    main()
