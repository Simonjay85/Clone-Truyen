#!/usr/bin/env python3
import json
import os
import sys
import re

# Add scratch to path to import novel_editor
sys.path.append("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch")
import novel_editor

def clean_duplicates_and_empty_paragraphs(content):
    # Some paragraphs might be duplicated during draft generation, let's clean up any double paragraph tags if they exist.
    # E.g. <p>Tôi sẽ không đi...</p> which we saw repeated multiple times in Chapter 1 dump!
    # Let's clean repetitive adjacent lines to make the prose look exceptionally clean.
    lines = content.split("\n")
    unique_lines = []
    prev = None
    for line in lines:
        stripped = line.strip()
        if stripped == prev and len(stripped) > 30:
            # Skip duplicate adjacent lines (longer than 30 chars)
            continue
        unique_lines.append(line)
        if stripped:
            prev = stripped
    return "\n".join(unique_lines)

def main():
    dump_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/active_story_3940_dump.json"
    if not os.path.exists(dump_path):
        print(f"Error: {dump_path} does not exist. Please run fetch_active_3940 first.")
        return

    with open(dump_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    chapters = data["chapters"]
    print(f"Loaded {len(chapters)} active chapters to polish.")

    # We will upload the helper
    print("Uploading novel_editor.php helper to production...")
    novel_editor.upload_helper()

    try:
        for idx, ch in enumerate(chapters):
            ch_id = ch["id"]
            title = ch["title"]
            content = ch["content"]

            print(f"\nProcessing Chapter {idx+1}: {title} (ID: {ch_id})")

            # 1. Apply prose refinements specifically to Chapter 1 (ID 3986)
            if ch_id == 3986:
                print("Refining Chapter 1 prose (dialogues, ring-throwing, and logic)...")
                
                # Replace Viện trưởng's dialogue
                old_vieng_truong = (
                    '<p>Viện trưởng Lê Hữu Hoài đứng đầu bàn dài, ánh mắt sắc lạnh như dao cạo, giọng nói của ông vang lên đầy uy quyền và tàn nhẫn như tiếng sét đánh ngang tai.</p>\n'
                    '<p>“Nguyễn Lâm Phong, tôi chính thức tuyên bố trục xuất anh khỏi Viện Phổi Quốc Tế. Từ giờ phút này, anh không còn là nhân viên của chúng tôi, cũng không còn được phép đặt chân lên mảnh đất này nữa.”</p>'
                )
                new_vieng_truong = (
                    '<p>Viện trưởng Lê Hữu Hoài đứng đầu bàn họp dài, gõ ngón tay lên mặt bàn trơn láng, giọng nói của ông lạnh lùng và dứt khoát cắt ngang.</p>\n'
                    '<p>“Cậu Lâm, hội đồng kỷ luật của Viện Phổi Quốc Tế đã xem xét kỹ lưỡng. Vì những phản biện lâm sàng phi khoa học, thiếu số liệu thống kê chuẩn của cậu gây ảnh hưởng đến dự án hợp tác liên doanh của viện, chúng tôi chính thức đình chỉ công tác của cậu từ hôm nay. Ban an ninh đâu, niêm phong tài liệu lab và thu hồi thẻ công tác nội bộ của cậu Lâm!”</p>'
                )
                content = content.replace(old_vieng_truong, new_vieng_truong)

                # Replace Phan Mỹ Hạnh's entrance and ring-throwing
                old_hanh_ring = (
                    '“Anh xem đây, chiếc nhẫn đính hôn mà anh đã tốn bao công sức để mua, giờ đây nó chỉ là thứ rác rưởi vô dụng mà anh không xứng đáng đeo trên tay.”</p>\n'
                    '<p>Phan Mỹ Hạnh rút chiếc nhẫn bạc từ trong túi áo, ném mạnh xuống sàn nhà, tiếng kim loại va vào sàn đá hoa cương phát ra âm thanh chói tai như tiếng khóc của một đứa trẻ.</p>\n'
                    '<p>Chiếc nhẫn lăn lóc trên sàn, dừng lại ngay trước mặt Phong, ánh sáng phản chiếu lên bề mặt lạnh lẽo của nó như một nhát dao cứa vào tim anh.</p>\n'
                    '<p>“Anh còn nghĩ mình là ai? Một kẻ nghèo hèn, vô dụng, không có tiền, không có quyền lực, không có tương lai. Anh không xứng đáng với tôi, cũng không xứng đáng với bất kỳ ai ở đây.”'
                )
                new_hanh_ring = (
                    '“Vũ Hoài Lâm, anh nên thực tế một chút.” Phan Mỹ Hạnh tháo chiếc nhẫn đính hôn ra, dứt khoát đặt lên mặt bàn trơn láng. Tiếng kim loại va chạm với gỗ trắc vang lên một tiếng cạch khô khốc, báo hiệu một sự đứt gãy không thể hàn gắn giữa hai thế giới. “Hợp đồng liên doanh trị giá hai trăm tỷ đồng của NexaCorp là tương lai phát triển của cả viện và gia tộc tôi. Sự cố chấp bám víu vào mấy bài thuốc thảo dược chưa được kiểm chứng của anh chỉ kéo lùi mọi người lại. Đôi bàn tay bốc thuốc Nam của anh không thể giúp anh đứng trên sàn chứng khoán IPO. Anh không xứng đáng với tôi, cũng không xứng đáng với bất kỳ ai ở đây.”'
                )
                content = content.replace(old_hanh_ring, new_hanh_ring)

                # Replace Trần Quốc Dũng's expulsion
                old_expulsion = (
                    '<p>Trần Quốc Dũng bước tới, nắm lấy tay Phong, giọng nói của anh đầy đe dọa.</p>\n'
                    '<p>“Đi thôi, anh. Đừng làm mất thêm thời gian của chúng tôi. Chúng tôi không còn muốn nhìn thấy mặt anh nữa.”</p>'
                )
                new_expulsion = (
                    '<p>Trần Quốc Dũng khẽ gật đầu đắc ý. Ba gã bảo vệ lập tức tiến lên, thô bạo tịch thu túi tài liệu kỹ thuật, khóa tài khoản truy cập máy chủ của Lâm và áp giải anh ra khỏi sảnh chính ngay trong đêm mưa giông sấm sét tầm tã của Hà Nội. Lâm bị đẩy ngã xuống bậc thềm đá, toàn thân sũng nước dưới màn mưa buốt giá. Nước mưa lạnh buốt ngấm vào da thịt, nhưng không lạnh bằng sự phản bội tàn nhẫn của những kẻ anh từng coi là người thân.</p>'
                )
                content = content.replace(old_expulsion, new_expulsion)
                
                # Clean up any duplicated lines in Chapter 1
                content = clean_duplicates_and_empty_paragraphs(content)

            # 2. Apply global character renaming to ALL chapters
            content = content.replace("Nguyễn Lâm Phong", "Vũ Hoài Lâm")
            content = content.replace("Lâm Phong", "Hoài Lâm")
            
            # Safe boundary word replacements using regex for single "Phong"
            content = re.sub(r'\bPhong\b', 'Lâm', content)
            
            # Sửa luôn trong Tiêu đề nếu có tên Phong
            title = title.replace("Nguyễn Lâm Phong", "Vũ Hoài Lâm").replace("Lâm Phong", "Hoài Lâm").replace("Phong", "Lâm")

            # Upload the polished chapter content back to the live site
            print(f"Uploading updated chapter {ch_id} to doctieuthuyet.com...")
            res = novel_editor.update_chapter(ch_id, title, content)
            if res.get("success"):
                print(f"✅ Success! Chapter {ch_id} updated successfully on production.")
            else:
                print(f"❌ Error updating chapter {ch_id}: {res.get('error')}")

        print("\n✓ Active story ID 3940 has been polished, renamed, and updated on production!")

    finally:
        print("Cleaning up production helper...")
        novel_editor.remove_helper()
        print("✓ Polishing operation finished.")

if __name__ == "__main__":
    main()
