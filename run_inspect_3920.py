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
$id = 3920;
$t = get_post($id);
if (!$t) {
    echo json_encode(["error" => "Post 3920 not found"]);
    exit;
}

$metas = get_post_meta($id);
$clean_metas = [];
foreach($metas as $k => $v) {
    // Only fetch interesting keys
    if (strpos($k, '_temply') !== false || strpos($k, 'rank_math') !== false || $k === 'truyen_tacgia') {
        $clean_metas[$k] = maybe_unserialize($v[0]);
    }
}

// Also get chapters details
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
        'content_len' => strlen($c->post_content)
    ];
}

echo json_encode([
    'title' => $t->post_title,
    'content' => $t->post_content,
    'excerpt' => $t->post_excerpt,
    'metas' => $clean_metas,
    'chapters' => $chaps_data
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>"""

    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("temp_inspect_3920.php", "w", encoding="utf-8") as f:
        f.write(php_code)
    
    with open("temp_inspect_3920.php", "rb") as f:
        ftp.storbinary("STOR temp_inspect_3920.php", f)
    ftp.quit()

    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_inspect_3920.php", timeout=30)
        data = req.read().decode('utf-8')
        print(data)
    except Exception as e:
        print("Error:", e)
    finally:
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        try:
            ftp.delete("temp_inspect_3920.php")
        except:
            pass
        ftp.quit()
        if os.path.exists("temp_inspect_3920.php"):
            os.remove("temp_inspect_3920.php")

if __name__ == "__main__":
    run()
