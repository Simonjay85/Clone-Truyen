import ftplib
import urllib.request

config_content = """<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);

$f = $_GET['f'] ?? '';
if(empty($f)) die('No file');
echo "Loading $f...\n";
require($f);
echo "Loaded successfully.\n";
?>"""

with open("temp_syntax.php", 'w') as f:
    f.write(config_content)

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    with open("temp_syntax.php", "rb") as f:
        ftp.storbinary("STOR temp_syntax.php", f)
    
    ftp.quit()
    
    files = [
        'wp-content/themes/tehi-theme/functions.php',
        'wp-content/themes/tehi-theme/page-story-studio.php',
        'wp-content/plugins/temply-ai-factory/temply-ai-factory.php',
        'wp-content/plugins/temply-ai-factory/includes/openai-api.php'
    ]
    for file in files:
        url = "https://doctieuthuyet.com/temp_syntax.php?f=" + file
        try:
            req = urllib.request.urlopen(url)
            print("Output for", file, ":\n", req.read().decode("utf-8")[:500])
        except urllib.error.HTTPError as e:
            print("HTTPError for", file, e.code, e.reason)
            print(e.read().decode("utf-8"))
except Exception as e:
    print("Error:", e)
