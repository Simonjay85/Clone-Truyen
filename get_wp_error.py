import ftplib
import urllib.request

config_content = """<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
register_shutdown_function(function() {
    $e = error_get_last();
    if($e !== null) {
        echo "\\n--- FATAL ERROR DETECTED ---\\n";
        print_r($e);
    }
});
require('./wp-load.php');
?>"""

with open("temp_syntax.php", 'w') as f:
    f.write(config_content)

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    with open("temp_syntax.php", "rb") as f:
        ftp.storbinary("STOR temp_syntax.php", f)
    
    ftp.quit()
    req = urllib.request.urlopen("https://doctieuthuyet.com/temp_syntax.php")
    print(req.read().decode("utf-8"))
except urllib.error.HTTPError as e:
    print("HTTPError", e.code, e.reason)
    print(e.read().decode("utf-8"))
except Exception as e:
    print("Error:", e)
