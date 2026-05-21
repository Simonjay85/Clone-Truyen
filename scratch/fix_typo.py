# -*- coding: utf-8 -*-
import ftplib
import urllib.request

def fix():
    php_code = """<?php
require('./wp-load.php');

$args = [
    'post_type' => 'chuong',
    'meta_key' => '_truyen_id',
    'meta_value' => 2190,
    'posts_per_page' => -1
];

$chaps = get_posts($args);
$updated = 0;

foreach($chaps as $c) {
    if(strpos($c->post_content, 'l lặng lẽ') !== false) {
        $new_content = str_replace('l lặng lẽ', 'lặng lẽ', $c->post_content);
        wp_update_post([
            'ID' => $c->ID,
            'post_content' => $new_content
        ]);
        $updated++;
        echo "Successfully updated chapter: " . $c->post_title . "<br>";
    }
}

if($updated === 0) {
    echo "No typo 'l lặng lẽ' found or already updated.<br>";
}
?>"""

    temp_file = "fix_typo_wood_tea.php"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(php_code)
    
    print("Uploading fix_typo_wood_tea.php via FTP...")
    try:
        ftp = ftplib.FTP("51.79.53.190", timeout=30)
        ftp.login("alotoinghe", "Nghia234!")
        with open(temp_file, "rb") as f:
            ftp.storbinary(f"STOR {temp_file}", f)
        print("✓ Uploaded successfully.")
        ftp.quit()
        
        print("Triggering via HTTP...")
        req = urllib.request.urlopen("https://doctieuthuyet.com/fix_typo_wood_tea.php", timeout=90)
        res = req.read().decode('utf-8')
        print("Response from server:")
        print(res)
        
        # Clean up remote
        print("Cleaning up remote file...")
        ftp = ftplib.FTP("51.79.53.190", timeout=30)
        ftp.login("alotoinghe", "Nghia234!")
        ftp.delete(temp_file)
        print("✓ Deleted remote helper.")
        ftp.quit()
        
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    fix()
