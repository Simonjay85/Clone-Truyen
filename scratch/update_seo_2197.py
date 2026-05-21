# -*- coding: utf-8 -*-
import ftplib
import urllib.request
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
STORY_ID = 2197

def main():
    print("=" * 60)
    print("🔄 UPDATING STORY SEO & RANKMATH INFO (STORY 2197)")
    print("=" * 60)

    # 1. Prepare PHP code
    php_code = """<?php
require('./wp-load.php');

$story_id = 2197;

$intro = '<p><strong>&quot;Ngày tôi đến ra mắt, bà ấy nhìn đôi ủng xi măng trên chân tôi rồi phẩy tay: \\\'Thợ hồ mà dám đòi cưới con gái tôi? Trọng Khải, con rể tương lai của ta, là thiếu gia nhà giàu, đi xe hơi bóng loáng. Còn ngươi chỉ là một thằng thợ hồ rẻ rách!\\\'&quot;</strong></p><p><strong>&quot;Trần Hùng cười nhạt, gạt bỏ sự khinh khi. Ba năm chịu đựng thử thách ẩn thân đã kết thúc, vị thế Chủ tịch Tập đoàn Đế Vương chính thức thức tỉnh, thâu tóm toàn bộ siêu dự án KCN VSIP 3 và buộc toàn bộ giới tài phiệt Bình Dương phải quỳ gối xin lỗi...&quot;</strong></p><hr /><p>Trần Hùng từng là một kỹ sư xây dựng đầy tài năng, nhưng vì một chữ tình, anh chấp nhận lùi về phía sau làm thợ hồ ẩn dật để gia đình nhà vợ leo lên vị trí cao. Đổi lại, anh nhận được sự khinh miệt thấu xương từ mẹ vợ và màn ly hôn tuyệt tình từ người vợ Thu Thủy để chạy theo gã nhân tình giàu có Lê Trọng Khải.</p><p>Họ không ngờ rằng, anh chính là người thừa kế duy nhất của Tập đoàn Đế Vương – siêu thế lực kinh tế bí ẩn nắm trong tay khối tài sản khổng lồ. Đồng thời, bên cạnh anh giờ đây là Thu Hà – nữ giám đốc giám sát sắc sảo, xinh đẹp nhất ngành xây dựng Bình Dương. Trận chiến vả mặt kinh điển, thâu tóm các đại dự án nghìn tỷ và hành trình vươn lên đỉnh cao bá chủ bắt đầu!</p>';

$excerpt = '"Ngày tôi đến ra mắt, bà ấy nhìn đôi ủng xi măng trên chân tôi rồi phẩy tay: \\\'Thợ hồ mà dám đòi cưới con gái tôi? Trọng Khải, con rể tương lai của ta, là thiếu gia nhà giàu, đi xe hơi bóng loáng. Còn ngươi chỉ là một thằng thợ hồ rẻ rách!\\\'" Trần Hùng cười nhạt, gạt bỏ sự khinh khi. Ba năm chịu đựng thử thách đã kết thúc, tổng thầu lớn nhất Bình Dương chính thức thức tỉnh, khiến cả giới tài phiệt phải quỳ gối!';

$result = wp_update_post([
    'ID'           => $story_id,
    'post_content' => $intro,
    'post_excerpt' => $excerpt
]);

// Update RankMath SEO Postmeta
update_post_meta($story_id, '_rank_math_description', $excerpt);
update_post_meta($story_id, '_rank_math_title', '%title%');
update_post_meta($story_id, '_rank_math_focus_keyword', 'thợ hồ nghìn tỷ');

if (is_wp_error($result)) {
    echo "Error updating story SEO: " . $result->get_error_message();
} else {
    if (function_exists('litespeed_purge_all')) {
        litespeed_purge_all();
    }
    echo "Success! SEO Info and RankMath metadata updated.";
}
?>'
"""

    temp_file = "temp_update_seo_2197.php"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(php_code)
    print("✓ Created local temp script.")

    # 2. Upload via FTP
    print("Uploading temp script to server via FTP...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        with open(temp_file, "rb") as f:
            ftp.storbinary(f"STOR {temp_file}", f)
        print("✓ Uploaded to server.")
        ftp.quit()
    except Exception as e:
        print("❌ FTP Upload Error:", e)
        return

    # 3. Request the page
    print("Executing updates via HTTP...")
    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_update_seo_2197.php", timeout=90)
        response_text = req.read().decode('utf-8')
        print("✓ Server response:", response_text)
    except Exception as e:
        print("❌ HTTP Execution Error:", e)

    # 4. Cleanup
    print("Cleaning up remote and local files...")
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
        print("✓ Cleaned up local temp file.")

    print("=" * 60)
    print("🎉 SEO META UPDATE PROCESS COMPLETE!")
    print("=" * 60)

if __name__ == "__main__":
    main()
