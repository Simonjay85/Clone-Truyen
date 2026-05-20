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
    print("🔄 NOVEL META UPDATER (HIGH-IMPACT TITLE & HOOK)")
    print("=" * 60)

    # 1. Prepare the PHP updater script
    php_code = """<?php
require('./wp-load.php');

$story_id = 2052;

// Check if story exists
$post = get_post($story_id);
if (!$post) {
    die("Error: Story not found!");
}

$new_title = "Thần Y Phòng Khám Quận 5: Vợ Tôi Là Siêu Tỷ Phú";
$new_content = '<p><strong>&quot;Năm đó, sếp giật công trình nghiên cứu, bảo vệ ném hành lý của tôi ra đường Nguyễn Trãi dưới cơn mưa tầm tã. Hắn khóa tài khoản Vietcombank, ép tôi vào đường cùng và cười khẩy: \\\'Mày chỉ là một con thực tập sinh quèn rách rưới!\\\'&quot;</strong></p><p><strong>&quot;Thế nhưng hắn không ngờ, chỉ một tháng sau, tôi đứng trên đỉnh cao y học Sài Gòn, nắm giữ Nhân Y Đường, châm một cây kim cứu sống siêu tỷ phú đứng đầu Trịnh Gia. Và bên cạnh tôi, là cô con gái độc nhất của Trịnh Gia – siêu mỹ nhân tài phiệt nắm trong tay hàng ngàn tỷ đồng...&quot;</strong></p><hr /><p>Lâm Trần là một bác sĩ thực tập thiên tài tại phòng khám đa khoa An Tâm ở Quận 5, người đã cống hiến cả thanh xuân để nghiên cứu ra liệu pháp đột phá tái tạo tế bào gan bằng thảo dược tự nhiên. Thế nhưng, sự thật tàn nhẫn ập đến khi Trưởng khoa Hoàng Vĩnh – một kẻ tham lam và xảo quyệt – đã cướp đoạt toàn bộ công trình của anh, biến nó thành của riêng rồi đuổi anh ra khỏi phòng khám trong nhục nhã.</p><p>Giữa cơn mưa tầm tã của Sài Gòn, Lâm Trần gặp gỡ Minh Thư, ái nữ sắc sảo của siêu tập đoàn y tế Trịnh Gia. Được sự hậu thuẫn mạnh mẽ của cô, anh quyết định mở phòng khám y học cổ truyền &quot;Nhân Y Đường&quot; ngay đối diện kẻ thù, bắt đầu hành trình lấy lại danh dự và vươn lên đỉnh cao y học. Những trận chiến y lý nghẹt thở, những cú lật kèo pháp lý ngoạn mục và sự trừng phạt đích đáng cho kẻ phản bội đang chờ đón bạn trong tác phẩm này.</p>';

// Update post
$result = wp_update_post([
    'ID'           => $story_id,
    'post_title'   => $new_title,
    'post_content' => $new_content
]);

if (is_wp_error($result)) {
    echo "Error updating story: " . $result->get_error_message();
} else {
    echo "Success! Updated Story ID $story_id with new title and hook.";
}
?>'
"""

    temp_file = "temp_update_story.php"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(php_code)
    print("✓ Created temp_update_story.php local script.")

    # 2. Upload via FTP
    print("Uploading temp_update_story.php to server via FTP...")
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
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_update_story.php", timeout=90)
        response_text = req.read().decode('utf-8')
        print("✓ Server response:", response_text)
    except Exception as e:
        print("❌ HTTP Execution Error:", e)
        # Continue cleanup anyway

    # 4. Clean up FTP and local files
    print("Cleaning up remote and local temporary files...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete(temp_file)
        print("✓ Deleted temp_update_story.php from remote server.")
        ftp.quit()
    except Exception as e:
        print("⚠️ Failed to delete remote file:", e)

    if os.path.exists(temp_file):
        os.remove(temp_file)
        print("✓ Cleaned up local temp_update_story.php.")

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
                    novel["intro"] = php_code.split("new_content = '")[1].split("';")[0]
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
