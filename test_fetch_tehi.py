import ftplib
import requests

PHP_CODE = """<?php
require_once('wp-load.php');
$response = wp_remote_post( 'https://tehitruyen.com/sources/ajax/mongdaovien/load-truyen-hoan-thanh.php', array(
    'body' => array('page' => 1),
    'timeout' => 15,
    'user-agent' => 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
) );
if ( is_wp_error( $response ) ) {
    echo "ERROR: " . $response->get_error_message();
} else {
    $body = wp_remote_retrieve_body($response);
    echo "STATUS: " . wp_remote_retrieve_response_code($response) . "\n";
    echo "BODY LENGTH: " . strlen($body) . "\n";
    echo substr($body, 0, 500);
}
"""

with open("test_tehi.php", "w") as f:
    f.write(PHP_CODE)

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    with open("test_tehi.php", "rb") as f:
        ftp.storbinary('STOR test_tehi.php', f)
    ftp.quit()
    
    res = requests.get("https://doctieuthuyet.com/test_tehi.php")
    print(res.text[:1000])
except Exception as e:
    print(e)
