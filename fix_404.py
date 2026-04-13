import ftplib
import requests

PHP_CODE = """<?php
require_once('wp-load.php');
if ( ! current_user_can('manage_options') ) {
   wp_set_current_user(1);
}
flush_rewrite_rules(false);
echo "Rewrite rules flushed!";
"""

try:
    with open("flush.php", "w") as f:
        f.write(PHP_CODE)
    
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    with open("flush.php", "rb") as f:
        ftp.storbinary('STOR flush.php', f)
    ftp.quit()
    
    res = requests.get("https://doctieuthuyet.com/flush.php")
    print(res.text)
except Exception as e:
    print(e)
