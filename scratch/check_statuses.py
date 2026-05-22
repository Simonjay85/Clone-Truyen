import ftplib
import urllib.request
import json

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

PHP_CODE = """<?php
require_once('wp-load.php');
$truyens = get_posts([
    'post_type' => 'truyen',
    'posts_per_page' => -1,
    'post_status' => 'any'
]);

$list = [];
foreach ($truyens as $t) {
    $list[] = [
        'id' => $t->ID,
        'title' => $t->post_title,
        'status' => $t->post_status
    ];
}
echo json_encode($list, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>"""

def main():
    temp_file = "temp_check_statuses.php"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(PHP_CODE)
        
    print("Uploading temp_check_statuses.php via FTP...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(temp_file, "rb") as f:
        ftp.storbinary(f"STOR {temp_file}", f)
    ftp.quit()
    print("✓ Uploaded.")
    
    print("Executing check via HTTP...")
    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_check_statuses.php", timeout=60)
        data = json.loads(req.read().decode('utf-8'))
        print(f"Total stories queried: {len(data)}")
        
        status_counts = {}
        for item in data:
            status = item['status']
            status_counts[status] = status_counts.get(status, 0) + 1
            if status != 'publish':
                print(f"⚠️ {item['id']}: {item['title']} is in status '{status}'")
                
        print("Status Summary:")
        for status, count in status_counts.items():
            print(f"  - {status}: {count}")
            
    except Exception as e:
        print("Error:", e)
        
    print("Cleaning up...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.delete(temp_file)
    ftp.quit()
    print("✓ Remote cleanup done.")

if __name__ == "__main__":
    main()
