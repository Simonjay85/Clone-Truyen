import ftplib
import urllib.request

php_code = """<?php
require('./wp-load.php');
$truyens = get_posts(['post_type' => 'truyen', 'posts_per_page' => -1]);
$count = 0;
foreach($truyens as $t) {
    if(empty($t->post_excerpt) || strpos($t->post_excerpt, '1. Bối cảnh') !== false || strlen($t->post_excerpt) < 60) {
        // broken
        $count++;
    }
}
echo "Found $count broken stories.";
?>"""

with open("temp_broken.php", "w") as f:
    f.write(php_code)

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    with open("temp_broken.php", "rb") as f:
        ftp.storbinary("STOR temp_broken.php", f)
    ftp.quit()
    req = urllib.request.urlopen("https://doctieuthuyet.com/temp_broken.php")
    print(req.read().decode("utf-8"))
except Exception as e:
    print("Error:", e)
