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

function get_full_post_data($id) {
    $t = get_post($id);
    if (!$t) return null;
    
    $chaps = get_posts([
        'post_type' => 'chuong',
        'meta_key' => '_truyen_id',
        'meta_value' => $id,
        'posts_per_page' => -1,
        'orderby' => 'menu_order date',
        'order' => 'ASC'
    ]);
    
    $chaps_data = [];
    foreach($chaps as $c) {
        $chaps_data[] = [
            'id' => $c->ID,
            'title' => $c->post_title,
            'content' => $c->post_content,
            'date' => $c->post_date,
            'status' => $c->post_status
        ];
    }
    
    $metas = get_post_meta($id);
    $clean_metas = [];
    foreach($metas as $k => $v) {
        $clean_metas[$k] = maybe_unserialize($v[0]);
    }
    
    return [
        'id' => $t->ID,
        'title' => $t->post_title,
        'content' => $t->post_content,
        'excerpt' => $t->post_excerpt,
        'status' => $t->post_status,
        'date' => $t->post_date,
        'metas' => $clean_metas,
        'chapters' => $chaps_data
    ];
}

$backup = [
    '3920' => get_full_post_data(3920),
    '2710' => get_full_post_data(2710),
    '2703' => get_full_post_data(2703)
];

echo json_encode($backup, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>"""

    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("temp_backup.php", "w", encoding="utf-8") as f:
        f.write(php_code)
    
    with open("temp_backup.php", "rb") as f:
        ftp.storbinary("STOR temp_backup.php", f)
    ftp.quit()

    try:
        print("Fetching backup data...")
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_backup.php", timeout=60)
        data = req.read().decode('utf-8')
        
        # Save to local backups folder
        os.makedirs("backups", exist_ok=True)
        backup_file = "backups/stories_backup_3920_2710_2703.json"
        with open(backup_file, "w", encoding="utf-8") as out:
            out.write(data)
        print(f"Backup saved successfully to {backup_file}")
    except Exception as e:
        print("Error during backup:", e)
    finally:
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        try:
            ftp.delete("temp_backup.php")
        except:
            pass
        ftp.quit()
        if os.path.exists("temp_backup.php"):
            os.remove("temp_backup.php")

if __name__ == "__main__":
    run()
