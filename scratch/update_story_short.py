# -*- coding: utf-8 -*-
import ftplib
import urllib.request
import json
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
STORY_ID = 2052

def main():
    print("=" * 60)
    print("🔄 NOVEL META UPDATER (SHORT & PUNCHY HOOK ONLY)")
    print("=" * 60)

    # 1. Prepare the PHP updater script
    # We use double newlines (\n\n) so that even if HTML is stripped, standard text-rendering shows proper paragraphs.
    # We make it extremely punchy and concise, removing the long redundant paragraphs.
    new_intro_text = (
        "\"Năm đó, sếp giật công trình nghiên cứu, bảo vệ ném hành lý của tôi ra đường Nguyễn Trãi dưới cơn mưa tầm tã. Hắn khóa tài khoản Vietcombank, ép tôi vào đường cùng và cười khẩy: 'Mày chỉ là một con thực tập sinh quèn rách rưới!'\"\n\n"
        "\"Thế nhưng hắn không ngờ, chỉ một tháng sau, tôi đứng trên đỉnh cao y học Sài Gòn, mở phòng khám Nhân Y Đường, châm một cây kim cứu sống siêu tỷ phú đứng đầu Trịnh Gia. Và bên cạnh tôi, là cô con gái độc nhất của Trịnh Gia – siêu mỹ nhân tài phiệt cùng tôi vạch trần kẻ phản bội!\""
    )

    # PHP code to update the story's post_content (introduction)
    php_code = f"""<?php
require('./wp-load.php');

$story_id = {STORY_ID};

$post = get_post($story_id);
if (!$post) {{
    die("Error: Story not found!");
}}

$new_title = "Thần Y Phòng Khám Quận 5: Vợ Tôi Là Siêu Tỷ Phú";
$new_content = '"Năm đó, sếp giật công trình nghiên cứu, bảo vệ ném hành lý của tôi ra đường Nguyễn Trãi dưới cơn mưa tầm tã. Hắn khóa tài khoản Vietcombank, ép tôi vào đường cùng và cười khẩy: \\\'Mày chỉ là một con thực tập sinh quèn rách rưới!\\\'"\\n\\n"Thế nhưng hắn không ngờ, chỉ một tháng sau, tôi đứng trên đỉnh cao y học Sài Gòn, mở phòng khám Nhân Y Đường, châm một cây kim cứu sống siêu tỷ phú đứng đầu Trịnh Gia. Và bên cạnh tôi, là cô con gái độc nhất của Trịnh Gia – siêu mỹ nhân tài phiệt cùng tôi vạch trần kẻ phản bội!"';

// Update post
$result = wp_update_post([
    'ID'           => $story_id,
    'post_title'   => $new_title,
    'post_content' => $new_content
]);

if (is_wp_error($result)) {{
    echo "Error updating story: " . $result->get_error_message();
}} else {{
    echo "Success! Updated Story ID $story_id with short and punchy hook.";
}}
?>"""

    temp_file = "temp_update_story_short.php"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(php_code)
    print("✓ Created temp_update_story_short.php local script.")

    # 2. Upload via FTP
    print("Uploading temp_update_story_short.php to server via FTP...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        with open(temp_file, "rb") as f:
            ftp.storbinary(f"STOR {temp_file}", f)
        print("✓ Uploaded updater script to remote root.")
        ftp.quit()
    except Exception as e:
        print("❌ FTP Upload Error:", e)
        return

    # 3. Request the PHP page to execute updates
    print("Executing updates via HTTP request...")
    try:
        req = urllib.request.urlopen(f"https://doctieuthuyet.com/{temp_file}", timeout=90)
        response_text = req.read().decode('utf-8')
        print("✓ Server response:", response_text)
    except Exception as e:
        print("❌ HTTP Execution Error:", e)

    # 4. Clean up FTP and local files
    print("Cleaning up remote and local temporary files...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete(temp_file)
        print("✓ Deleted remote temp script.")
        ftp.quit()
    except Exception as e:
        print("⚠️ Failed to delete remote file:", e)

    if os.path.exists(temp_file):
        os.remove(temp_file)
        print("✓ Cleaned up local temp script.")

    # 5. Update local registry (existing_novels.json)
    existing_path = "existing_novels.json"
    if os.path.exists(existing_path):
        try:
            with open(existing_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            updated = False
            for novel in data:
                if novel.get("id") == STORY_ID:
                    novel["title"] = "Thần Y Phòng Khám Quận 5: Vợ Tôi Là Siêu Tỷ Phú"
                    novel["intro"] = new_intro_text
                    updated = True
                    break
            
            if updated:
                with open(existing_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print("✓ Updated existing_novels.json registry.")
        except Exception as e:
            print("⚠️ Failed to update local registry:", e)

    print("=" * 60)
    print("🎉 PROCESS COMPLETE!")
    print("=" * 60)

if __name__ == "__main__":
    main()
