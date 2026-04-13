import ftplib
import requests

PHP_CODE = """<?php
require_once('wp-load.php');
if ( ! current_user_can('manage_options') ) {
   wp_set_current_user(1); // Force admin
}
include WP_PLUGIN_DIR . '/tehi-crawler-manager/admin/dashboard.php';
"""

with open("test_ui.php", "w") as f:
    f.write(PHP_CODE)

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    with open("test_ui.php", "rb") as f:
        ftp.storbinary('STOR test_ui.php', f)
    ftp.quit()
    
    res = requests.get("https://doctieuthuyet.com/test_ui.php")
    print(res.text[:3000])
except Exception as e:
    print(e)
