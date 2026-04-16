import urllib.request
import json
import ftplib

php_code = """<?php
require('./wp-load.php');
$truyens = get_posts(['post_type' => 'truyen', 'name' => 'bong-sen-do-giua-bien-mau', 'posts_per_page' => 1]);
if(empty($truyens)) die("Not found");
$t = $truyens[0];
$chaps = get_posts([
    'post_type' => 'chuong',
    'meta_key' => '_truyen_id',
    'meta_value' => $t->ID,
    'posts_per_page' => -1,
    'orderby' => 'ID',
    'order' => 'ASC'
]);

$full_text = "TÓM TẮT MỚI: " . wp_strip_all_tags($t->post_excerpt) . "\n\n";

foreach($chaps as $c) {
    $full_text .= "=== " . $c->post_title . " ===\n";
    $full_text .= wp_strip_all_tags($c->post_content) . "\n\n";
}

echo mb_substr($full_text, 0, 95000); // output max characters so we don't crash
?>"""

with open("temp_read.php", "w") as f:
    f.write(php_code)

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    with open("temp_read.php", "rb") as f:
        ftp.storbinary("STOR temp_read.php", f)
    ftp.quit()
    req = urllib.request.urlopen("https://doctieuthuyet.com/temp_read.php")
    with open("bong_sen_do_full.txt", "w") as f:
        f.write(req.read().decode('utf-8'))
    print("Downloaded full story to bong_sen_do_full.txt")
except Exception as e:
    print("Error:", e)
