#!/usr/bin/env python3
import json
import os
import sys
import re

# Add scratch to path to import novel_editor
sys.path.append("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch")
import novel_editor

def main():
    dump_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/story_3940_dump.json"
    if not os.path.exists(dump_path):
        print(f"Error: {dump_path} does not exist. Please run fetch first.")
        return

    with open(dump_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    chapters = data["chapters"]
    print(f"Loaded {len(chapters)} chapters to polish.")

    # We will rename the protagonist: 
    # "Nguyễn Lâm Phong" -> "Vũ Hoài Lâm"
    # "Lâm Phong" -> "Hoài Lâm"
    # "Phong" -> "Lâm" (with boundary care)
    
    # We will upload the helper
    print("Uploading novel_editor.php helper to production...")
    novel_editor.upload_helper()

    try:
        for idx, ch in enumerate(chapters):
            ch_id = ch["id"]
            title = ch["title"]
            content = ch["content"]

            print(f"\nProcessing Chapter {idx+1}: {title} (ID: {ch_id})")

            # 1. Apply general character renaming
            # Use safe replaces for exact patterns to avoid breaking HTML tags or words like "phòng"
            # "Nguyễn Lâm Phong" -> "Vũ Hoài Lâm"
            content = content.replace("Nguyễn Lâm Phong", "Vũ Hoài Lâm")
            content = content.replace("Lâm Phong", "Hoài Lâm")
            
            # Replace single "Phong" where it represents the name:
            # Let's replace " Phong" -> " Lâm", " Phong," -> " Lâm,", " Phong." -> " Lâm.", " Phong!" -> " Lâm!"
            content = content.replace(" Phong ", " Lâm ")
            content = content.replace(" Phong,", " Lâm,")
            content = content.replace(" Phong.", " Lâm.")
            content = content.replace(" Phong!", " Lâm!")
            content = content.replace(" Phong?", " Lâm?")
            content = content.replace(">Phong ", ">Lâm ")
            content = content.replace(">Phong,", ">Lâm,")
            content = content.replace(">Phong.", ">Lâm.")
            content = content.replace("của Phong", "của Lâm")
            content = content.replace("với Phong", "với Lâm")
            content = content.replace("cho Phong", "cho Lâm")
            content = content.replace("bên Phong", "bên Lâm")
            content = content.replace("tay Phong", "tay Lâm")
            content = content.replace("nhìn Phong", "nhìn Lâm")
            
            # Sửa luôn trong Tiêu đề nếu có tên Phong
            title = title.replace("Nguyễn Lâm Phong", "Vũ Hoài Lâm").replace("Lâm Phong", "Hoài Lâm").replace("Phong", "Lâm")

            # 2. If it is Chapter 1, apply the deep prose refinement
            if idx == 0:
                print("Refining Chapter 1 prose (dialogues and logical flow)...")
                
                # Replace Viện trưởng's paragraph
                old_vieng_truong = '<p>"Câm miệng!" Lê Hữu Hoài - Viện trưởng Viện Phổi Việt - Đức, đập mạnh tay xuống bàn họp vang lên một tiếng cộc khô khốc, chói tai. Sắc mặt ông ta xám ngoét không còn một giọt máu vì giận dữ, trán lấm tấm mồ hôi lạnh rỉ ra dọc thái dương khi bí mật đen tối bị phơi bày trước toàn thể ban giám đốc. "Mày chỉ là một thằng bác sĩ Đông y quèn, quanh năm bốc lá cây và châm cứu rác rưởi, có tư cách gì mà phán xét công nghệ sinh học hàng triệu đô của tập đoàn đa quốc gia NexaCorp? Đề tài nghiên cứu thảo dược phế nang của mày chỉ là đống giấy lộn vô giá trị! Bảo vệ đâu, thu hồi toàn bộ tài liệu y khoa và tống cổ thằng này ra khỏi viện ngay lập tức!"</p>'
                
                new_vieng_truong = '<p>"Cậu Lâm, hãy giữ chừng mực!" Lê Hữu Hoài - Viện trưởng Viện Phổi Việt - Đức, gõ mạnh tay xuống bàn họp, giọng nói lạnh lùng cắt ngang. Sắc mặt ông ta xám ngoét không còn một giọt máu vì giận dữ, trán lấm tấm mồ hôi lạnh rỉ ra dọc thái dương khi bí mật đen tối bị phơi bày trước toàn thể ban giám đốc. "Viện Phổi Quốc tế vận hành dựa trên các thử nghiệm lâm sàng mù đôi theo chuẩn FDA, chứ không phải vài phương pháp cổ truyền cảm tính chưa được số hóa. Báo cáo phản biện của cậu hoàn toàn thiếu cơ sở thống kê và mang tính định kiến cá nhân đối với sản phẩm Nexa-09 của tập đoàn đối tác. Vì lý do an toàn thông tin và uy tín của viện, hội đồng kỷ luật quyết định đình chỉ công tác của cậu từ hôm nay. Ban an ninh đâu, niêm phong tài liệu lab và thu hồi thẻ công tác nội bộ của cậu Lâm!"</p>'
                
                if old_vieng_truong in content:
                    content = content.replace(old_vieng_truong, new_vieng_truong)
                    print("✓ Viện trưởng paragraph replaced successfully!")
                else:
                    # Attempt fallback replacing with "Lâm" already applied
                    old_vieng_truong_lam = old_vieng_truong.replace("Nguyễn Lâm Phong", "Vũ Hoài Lâm").replace("Lâm Phong", "Hoài Lâm").replace("Phong", "Lâm")
                    if old_vieng_truong_lam in content:
                        content = content.replace(old_vieng_truong_lam, new_vieng_truong)
                        print("✓ Viện trưởng paragraph (renamed) replaced successfully!")
                    else:
                        print("⚠️ Could not find Viện trưởng paragraph in content, using regex fallback...")
                        # Regex search
                        pat = r'<p>"Câm miệng!".*?Lê Hữu Hoài.*?</p>'
                        content = re.sub(pat, new_vieng_truong, content)

                # Replace Phan Mỹ Hạnh's paragraph (and the ring-throwing)
                old_hanh_ring = '<p>"Nguyễn Lâm Phong, anh bớt lôi chuyện tình cảm xưa cũ ra đây để kể công đi!" Phan Mỹ Hạnh rút chiếc nhẫn đính hôn bằng bạc trên ngón tay ra, ném thẳng vào mặt Phong không thương tiếc. Chiếc nhẫn rơi xuống nền gạch, nảy lên mấy vòng rồi nằm im lìm trong góc tối. "Đôi bàn tay chỉ biết bốc thuốc Nam rách rưới của anh làm sao so được với tầm vóc thế giới của anh Dũng? Tập đoàn NexaCorp đã đồng ý rót hai trăm tỷ đồng để mua đứt bản quyền nghiên cứu của Viện Phổi và đưa dự án Nexa-09 niêm yết trên sàn chứng khoán. Loại nghèo hèn, bảo thủ như anh chỉ làm cản trở con đường tiến thân của tôi và gia tộc. Anh đã hết giá trị lợi dụng rồi, cút đi!"</p>'
                
                new_hanh_ring = '<p>"Vũ Hoài Lâm, anh nên thực tế một chút." Phan Mỹ Hạnh tháo chiếc nhẫn đính hôn ra, dứt khoát đặt lên mặt bàn trơn láng. Tiếng kim loại va chạm với gỗ trắc vang lên một tiếng cạch khô khốc, báo hiệu một sự đứt gãy không thể hàn gắn giữa hai thế giới. "Hợp đồng liên doanh trị giá hai trăm tỷ đồng của NexaCorp là tương lai của cả viện và gia tộc tôi. Sự cố chấp bám víu vào mấy bài thuốc thảo dược chưa được kiểm chứng của anh chỉ kéo lùi mọi người lại. Đôi bàn tay bốc thuốc Nam của anh không thể giúp anh đứng trên sàn chứng khoán IPO. Loại nghèo hèn, bảo thủ như anh chỉ làm cản trở con đường tiến thân của tôi và gia tộc. Anh đã hết giá trị lợi dụng rồi, cút đi!"</p>'
                
                if old_hanh_ring in content:
                    content = content.replace(old_hanh_ring, new_hanh_ring)
                    print("✓ Phan Mỹ Hạnh ring paragraph replaced successfully!")
                else:
                    old_hanh_ring_lam = old_hanh_ring.replace("Nguyễn Lâm Phong", "Vũ Hoài Lâm").replace("Lâm Phong", "Hoài Lâm").replace("Phong", "Lâm")
                    if old_hanh_ring_lam in content:
                        content = content.replace(old_hanh_ring_lam, new_hanh_ring)
                        print("✓ Phan Mỹ Hạnh ring paragraph (renamed) replaced successfully!")
                    else:
                        print("⚠️ Could not find Phan Mỹ Hạnh ring paragraph, using regex fallback...")
                        pat = r'<p>.*Phan Mỹ Hạnh rút chiếc nhẫn.*?</p>'
                        content = re.sub(pat, new_hanh_ring, content)

                # Replace expulsion paragraph
                old_expulsion = '<p>Trần Quốc Dũng khẩy môi cười nham hiểm đầy vẻ đắc ý của kẻ chiến thắng. Hắn ra hiệu cho ba gã bảo vệ lực lưỡng lao vào giật phăng túi xách đơn sơ của Phong, bẻ gãy thẻ hành nghề và thô bạo kéo anh ra khỏi sảnh chính của bệnh viện. Phong bị đẩy ngã xuống bậc thềm đá, toàn thân sũng nước dưới cơn mưa giông sấm sét tầm tã của Hà Nội. Nước mưa lạnh buốt ngấm vào da thịt, nhưng không lạnh bằng sự phản bội tàn nhẫn của những kẻ anh từng coi là người thân. Phong đứng dậy giữa màn đêm đen tối, đôi mắt đỏ ngầu nhìn lên tòa nhà Viện Phổi rực rỡ ánh đèn. Anh khẽ siết chặt đôi bàn tay, giọng nói thì thầm nhưng kiên định xuyên qua tiếng sấm truyền: "Lê Hữu Hoài, Phan Mỹ Hạnh, Trần Quốc Dũng... Các người hãy nhớ lấy ngày hôm nay. Tôi sẽ khiến các người phải tự quỳ gối dưới chân tôi để cầu xin sự tha thứ!"</p>'
                
                new_expulsion = '<p>Trần Quốc Dũng khẽ gật đầu đắc ý. Ba gã bảo vệ lập tức tiến lên, thô bạo tịch thu túi tài liệu kỹ thuật, khóa tài khoản truy cập máy chủ của Lâm và áp giải anh ra khỏi sảnh chính ngay trong đêm mưa giông sấm sét tầm tã của Hà Nội. Lâm bị đẩy ngã xuống bậc thềm đá, toàn thân sũng nước dưới màn mưa buốt giá. Nước mưa lạnh buốt ngấm vào da thịt, nhưng không lạnh bằng sự phản bội tàn nhẫn của những kẻ anh từng coi là người thân. Lâm đứng dậy giữa màn đêm đen tối, đôi mắt đỏ ngầu nhìn lên tòa nhà Viện Phổi rực rỡ ánh đèn. Anh khẽ siết chặt đôi bàn tay, giọng nói thì thầm nhưng kiên định xuyên qua tiếng sấm truyền: "Lê Hữu Hoài, Phan Mỹ Hạnh, Trần Quốc Dũng... Các người hãy nhớ lấy ngày hôm nay. Tôi sẽ khiến các người phải tự quỳ gối dưới chân tôi để cầu xin sự tha thứ!"</p>'
                
                if old_expulsion in content:
                    content = content.replace(old_expulsion, new_expulsion)
                    print("✓ Expulsion paragraph replaced successfully!")
                else:
                    old_expulsion_lam = old_expulsion.replace("Nguyễn Lâm Phong", "Vũ Hoài Lâm").replace("Lâm Phong", "Hoài Lâm").replace("Phong", "Lâm")
                    if old_expulsion_lam in content:
                        content = content.replace(old_expulsion_lam, new_expulsion)
                        print("✓ Expulsion paragraph (renamed) replaced successfully!")
                    else:
                        print("⚠️ Could not find expulsion paragraph, using regex fallback...")
                        pat = r'<p>Trần Quốc Dũng khẩy môi.*?</p>'
                        content = re.sub(pat, new_expulsion, content)

            # Upload the polished chapter content back to the live site
            print(f"Uploading updated chapter {ch_id} to doctieuthuyet.com...")
            res = novel_editor.update_chapter(ch_id, title, content)
            if res.get("success"):
                print(f"✅ Success! Chapter {ch_id} updated successfully on production.")
            else:
                print(f"❌ Error updating chapter {ch_id}: {res.get('error')}")

        # Also update story title/meta to reflect the main character's rename if needed
        # (The main story title is: "Bác Sĩ Đông Y Bị Đuổi Khỏi Viện Phổi...") which does not contain the name, so we are good!
        print("\n✓ Entire story ID 3940 has been polished and updated!")

    finally:
        print("Cleaning up production helper...")
        novel_editor.remove_helper()
        print("✓ Polishing operation finished.")

if __name__ == "__main__":
    main()
