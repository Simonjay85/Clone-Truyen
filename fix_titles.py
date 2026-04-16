import ftplib
import urllib.request

php_code = """<?php
require('./wp-load.php');
$chaps = get_posts(['post_type' => 'chuong', 'posts_per_page' => -1, 'post_status' => 'any']);
$count = 0;
foreach($chaps as $c) {
   $title = $c->post_title;
   $new_title = str_replace(array('*', '#', '[', ']', 'TITLE:', 'TITLE :', 'Title:', 'title:'), '', $title);
   // remove multiple spaces if any
   $new_title = trim(preg_replace('/\s+/', ' ', $new_title));
   if($new_title !== $title) {
       wp_update_post(['ID' => $c->ID, 'post_title' => $new_title]);
       $count++;
   }
}
echo "Fixed $count chapters.";
?>"""

with open("temp_fix_titles.php", "w") as f:
    f.write(php_code)

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    with open("temp_fix_titles.php", "rb") as f:
        ftp.storbinary("STOR temp_fix_titles.php", f)
    ftp.quit()
    req = urllib.request.urlopen("https://doctieuthuyet.com/temp_fix_titles.php")
    print(req.read().decode("utf-8"))
except Exception as e:
    print("Error:", e)
