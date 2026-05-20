import os
import json
import requests
import ftplib
import urllib.parse
import random

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

# The story written directly by Antigravity under V11 Masterpiece specifications
novel_data = {
  "title": "Chàng Rể Hào Môn Miền Tây",
  "author": "Phong Vũ Miền Tây",
  "genre": "Sảng Văn",
  "intro": "<p>Lâm Phong là một thiếu gia của tập đoàn vận tải biển hàng đầu Việt Nam, vì muốn tìm kiếm một tình yêu đích thực không vụ lợi nên đã ẩn thân làm công nhân cày cuốc tại một vườn sầu riêng ở Bến Tre. Tại đây, anh gặp gỡ và yêu thương Minh Thư, cô con gái chủ vườn kiên cường và nhân hậu.</p><p>Nhưng cuộc sống yên bình miền sông nước nhanh chóng bị phá vỡ khi những thế lực tham lam âm mưu cướp đoạt mảnh đất vàng của gia đình cô. Đối mặt với âm mưu thâm hiểm của đối thủ phân phối độc quyền và món nợ ngân hàng Agribank lên tới 30 tỷ đồng, Lâm Phong sẽ phải làm gì để bảo vệ người con gái mình yêu? Một câu chuyện vả mặt sảng khoái với những cú lật kèo ngoạn mục nghẹt thở đang chờ đón bạn.</p>",
  "cover_prompt": "An anime illustration of a handsome young Vietnamese man in simple linen clothes standing next to a beautiful girl in a lush durian orchard in Ben Tre, Southern Vietnam. Bright sun rays filtering through leafy trees, professional book cover, vivid colors, cinematic lighting",
  "chapters": [
    {
      "title": "Chương 1: Kẻ Khốn Khó Của Cù Lao",
      "content": "<p>Lâm Phong đứng dưới cái nắng gay gắt của cù lao Minh Châu, mồ hôi lạnh thấm đẫm chiếc áo sơ mi bạc màu. Đôi bàn tay vốn thon dài của một nghệ sĩ nay đã hằn lên những vết chai sạn vì cuốc đất. Anh lặng lẽ bưng thúng phân bón hữu cơ nặng trĩu, bước từng bước nặng nề qua hàng sầu riêng Ri6 thẳng tắp.</p><p>\"Đồ vô dụng! Chỉ có mỗi việc xách nước tưới cây cũng làm trễ nải! Đúng là thứ nghèo hèn rách nát!\" Bà Liễu, mẹ kế của Minh Thư, cất giọng chói tai từ hiên nhà ba tầng lợp ngói đỏ. Bà ta vừa dứt lời thì nhổ một ngụm nước trà xuống nền gạch bóng loáng, ánh mắt đầy sự khinh miệt đổ dồn vào Lâm Phong.</p><p>Kế bên bà là Hoàng Bách, thiếu gia của tập đoàn hóa chất bảo vệ thực vật độc quyền tại miền Tây. Hắn cười khẩy, ngón tay xoay xoay chiếc chìa khóa xe Mercedes bóng loáng. Hắn bước xuống bậc thềm, giẫm chiếc giày tây da sáng loáng trực tiếp lên thúng phân của Lâm Phong: \"Mày nhìn cái gì? Thằng rác rưởi làm thuê cả đời cũng không mua nổi một cái bánh xe của tao đâu. Khôn hồn thì tránh xa Minh Thư ra!\"</p><p>Lâm Phong bấm chặt ngón tay vào lòng bàn tay rỉ máu. Móng tay ghim sâu khiến anh đau buốt, nhưng nét mặt anh vẫn bình thản đến lạ lùng. Anh lặng lẽ cúi đầu tiếp tục công việc của mình. Phản diện luôn tự đắc ở đỉnh cao, nhưng hắn không bao giờ biết được rằng, người thanh niên rách rưới trước mặt hắn chỉ cần một cái nhấc tay là có thể mua đứt cả cơ nghiệp của gia đình hắn.</p>"
    },
    {
      "title": "Chương 2: Ánh Sáng Nơi Vườn Sầu",
      "content": "<p>Tiếng chửi bới vang vọng khắp một góc cù lao khiến Minh Thư không thể ngồi yên. Cô từ phía cuối vườn vội vã bước tới, chiếc nón lá khẽ nghiêng, che đi khuôn mặt thanh tú đầy kiên định. Thấy Lâm Phong bị sỉ nhục, đôi lông mày liễu của cô nhíu chặt lại.</p><p>\"Dì Liễu! Hoàng Bách! Hai người thôi đi!\" Minh Thư bước lên đứng chắn trước Lâm Phong. Đôi mắt cô ánh lên sự kiên định: \"Lâm Phong là người con thuê làm việc. Anh ấy làm lụng cật lực từ 4 giờ sáng, không ai có quyền sỉ nhục anh ấy cả! Ở đây không nghênh tiếp những người không có sự tôn trọng tối thiểu!\"</p><p>Bà Liễu tím mặt định gào lên, nhưng Minh Thư đã nhanh chóng quay sang Lâm Phong. Cô khẽ rút chiếc khăn mùi soa nhỏ dịu dàng lau đi vệt bùn và mồ hôi trên trán anh: \"Anh Phong, anh có sao không? Đừng để tâm những lời rác rưởi đó.\"</p><p>Hành động dịu dàng của cô làm Lâm Phong rung động sâu sắc. Giữa thế giới đầy rẫy sự giả tạo và thực dụng, Minh Thư chính là ánh sáng thuần khiết nhất giữ chân anh lại mảnh đất này. Cô quay sang công bố trước mặt bà Liễu: \"Từ hôm nay, Lâm Phong sẽ là trợ lý kỹ thuật trực tiếp cho con. Mọi việc trong vườn sầu riêng này đều do con và anh ấy quản lý!\"</p>"
    },
    {
      "title": "Chương 3: Bẫy Ép Hôn Ba Mươi Tỷ",
      "content": "<p>Hoàng Bách điên cuồng vì bị từ chối công khai trước mặt Lâm Phong. Hắn thề sẽ dẫm nát vườn sầu riêng này và cướp bằng được Minh Thư về làm vợ hành hạ. Hắn lập tức liên kết với các thương lái đầu nậu độc quyền ép giá thu mua sầu riêng của Minh Thư xuống mức rẻ mạt, khiến hàng chục tấn trái cây chín không thể xuất khẩu.</p><p>Không dừng lại ở đó, Hoàng Bách cấu kết với một trưởng phòng tín dụng ngân hàng Agribank chi nhánh Bến Tre - kẻ vốn nhận hối lộ của gia đình hắn hàng năm. Gã cán bộ này lập tức ký trát đóng băng tài sản và yêu cầu gia đình Minh Thư thanh toán khẩn cấp món nợ gốc 30 tỷ đồng đã đến hạn, không cho phép gia hạn nợ dù chỉ một ngày.</p><p>Bà Liễu khóc lóc om sòm, cầm tờ đơn thỏa thuận đính hôn ép buộc Minh Thư ký tên: \"Mày nhìn đi! Nếu không gả cho thiếu gia Hoàng Bách, ngân hàng sẽ siết nợ toàn bộ khu vườn này! Cha mày đang nằm liệt giường, mày muốn cả nhà ra đường ở sao?\"</p><p>Minh Thư nắm chặt tay Lâm Phong, nước mắt giọt giọt rơi trên tờ sổ đỏ. Cô kiên quyết lắc đầu: \"Lâm Phong, dù có phải mất sạch vườn, em cũng không bao giờ gả cho kẻ đê tiện đó. Em sẽ cùng anh gánh vác tất cả!\"</p>"
    },
    {
      "title": "Chương 4: Đêm Đen Và Thuốc Độc",
      "content": "<p>Trong đêm mưa giông bão bùng sấm chớp đầy trời của miền Tây, Hoàng Bách đã thực hiện một nước cờ tàn độc. Hắn thuê một nhóm tay sai lẻn vào cù lao Minh Châu, đổ trực tiếp hàng chục lít hóa chất diệt cỏ cực độc vào hệ thống bể chứa tưới tiêu tự động của vườn sầu riêng.</p><p>Sáng hôm sau, khi cơn bão vừa qua đi, Lâm Phong bàng hoàng bước ra vườn. Cảnh tượng trước mắt khiến anh chết lặng. Toàn bộ sầu riêng non rụng đầy gốc, lá héo úa xơ xác, mùi hóa chất nồng nặc bốc lên. Minh Thư chạy ra, nhìn khu vườn tâm huyết của người cha đang thoi thóp héo tàn từng giây, cô đứng không vững, hai gối đập mạnh xuống đất cộp một tiếng.</p><p>Đúng lúc đó, bà Liễu cùng Hoàng Bách và gã cán bộ ngân hàng xuất hiện cùng với trát siết nợ đỏ chót. Hoàng Bách đắc ý cười vang: \"Vườn đã chết sạch rồi! Giờ ký bán rẻ mảnh đất này cho tao với giá 2 tỷ đồng, tao sẽ giúp trả nợ. Nếu không, cảnh sát sẽ cưỡng chế niêm phong ngay bây giờ!\"</p><p>Minh Thư suy sụp hoàn toàn, môi trắng bệch không còn một giọt máu. Cô nhắm mắt, tay run rẩy cầm cây bút định ký tên dưới áp lực nghẹt thở của phản diện.</p>"
    },
    {
      "title": "Chương 5: Khủng Hoảng Cực Đại",
      "content": "<p>Minh Thư kiệt sức hoàn toàn và ngất lịm ngay tại chỗ. Lâm Phong lập tức bế cô chạy thẳng đến bệnh viện đa khoa Cần Thơ cấp cứu. Nhìn cô gái kiên cường ngày nào nay nằm yếu ớt trên giường bệnh với ống truyền dịch, trái tim Lâm Phong nhói đau dữ dội.</p><p>Nhưng Hoàng Bách và bà Liễu vẫn không buông tha. Họ kéo theo đám vệ sĩ xông thẳng vào phòng bệnh VIP. Hoàng Bách ném bản hợp đồng chuyển nhượng đất lên ngực Minh Thư: \"Ký đi! Tao đã chặn đứng mọi nguồn vay của mày ở tất cả các ngân hàng tại miền Tây này rồi. Không có tao, cha con mày chỉ có nước nhảy sông tự tử!\"</p><p>Hắn vừa nói vừa giơ tay định tát vào mặt Minh Thư để ép buộc cô. Nhưng ngay trong khoảnh khắc bàn tay dơ bẩn của hắn định hạ xuống, một bàn tay thép đã khóa chặt lấy cổ tay hắn. Lâm Phong đứng đó, đôi mắt lạnh lùng như băng giá vạn năm, lực bóp cực mạnh khiến xương cổ tay Hoàng Bách kêu lên răng rắc.</p><p>\"Mày... thằng rác rưởi này buông tao ra! Đám bảo vệ đâu, đánh chết nó cho tao!\" Hoàng Bách đau đớn gào lên thảm thiết.</p>"
    },
    {
      "title": "Chương 6: Hào Môn Trỗi Dậy - Ván Bài Lật Ngửa",
      "content": "<p>Lâm Phong không hề nao núng. Anh một tay xách cổ Hoàng Bách ném mạnh xuống sàn phòng bệnh. Anh rút chiếc điện thoại mạ vàng Vertu độc bản ra, điềm tĩnh bấm số gọi trực tiếp cho Tổng giám đốc Agribank Việt Nam và Chủ tịch Tập đoàn vận tải biển Viễn Đông.</p><p>\"Tôi là Lâm Phong. Kích hoạt siêu tài khoản VIP của tôi tại Agribank. Mua đứt toàn bộ chi nhánh Agribank Bến Tre ngay lập tức. Sa thải gã trưởng phòng nhận hối lộ. Đồng thời, điều động 50 hạm đội drone nông nghiệp công nghệ sinh học từ kho dự trữ Singapore bay thẳng về cù lao Minh Châu cứu vườn sầu riêng.\"</p><p>Hoàng Bách bò dậy dưới đất cười sặc sụa: \"Mày điên rồi à? Thằng nghèo hèn lại nằm mơ làm chủ tịch sao?\"</p><p>Nhưng chỉ đúng 10 phút sau, điện thoại của gã cán bộ ngân hàng và cha của Hoàng Bách đồng loạt đổ chuông liên hồi. Sắc mặt họ lập tức biến đổi, mồ hôi lạnh chảy ròng ròng ướt sũng lưng áo. Gã cán bộ ngân hàng quỳ rụp xuống đất, run rẩy van xin: \"Thiếu gia Lâm Phong... tôi sai rồi! Tôi bị ép buộc! Xin ngài đừng phong tỏa tài sản của tôi!\"</p><p>Đồng thời, đại diện Cục Cảnh sát kinh tế C03 Bộ Công An ập vào phòng bệnh, còng tay Hoàng Bách và cha hắn ngay lập tức vì tội danh đầu độc môi trường nông nghiệp quy mô lớn và hối lộ quan chức. Vườn sầu riêng của Minh Thư được cứu sống thần kỳ bởi công nghệ sinh học cao cấp, trở nên xanh tươi hơn bao giờ hết.</p><p>Lâm Phong nắm chặt bàn tay Minh Thư, dịu dàng nói: \"Anh xin lỗi vì đã giấu em. Từ nay về sau, không ai có thể bắt nạt em được nữa.\" Đám cưới thế kỷ diễn ra trên sông nước miền Tây với sính lễ 100 tỷ đồng và hạm đội Maybach xếp dài bến phà, ghi dấu vinh quang tối thượng của chàng rể hào môn ẩn sĩ.</p>"
    }
  ]
}

def main():
    print("=" * 60)
    print("🌟 ANTIGRAVITY DIRECT-PUBLISHING MASTERPIECE ENGINE")
    print("=" * 60)
    
    # Construct Cover Image URL via Pollinations
    escaped_prompt = urllib.parse.quote(novel_data['cover_prompt'] + ", masterpiece, highly detailed book cover, anime illustration style, vivid lighting")
    cover_url = f"https://image.pollinations.ai/prompt/{escaped_prompt}?width=800&height=1200&seed={random.randint(1, 99999)}&nologo=true"
    
    # Step 1: Upload publish_novel.php helper script via FTP
    print("\n[Antigravity] Uploading publish_novel.php helper script via FTP...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        
        # Read the publish_novel.php file from workspace root
        with open("publish_novel.php", "rb") as f:
            ftp.storbinary("STOR publish_novel.php", f)
        print("✓ Helper uploaded successfully to remote.")
        ftp.quit()
    except Exception as e:
        print("❌ FTP Upload Error for helper script:", e)
        return
        
    # Step 2: Trigger story publication via HTTP call to publish_novel.php
    print("\n[Antigravity] Direct-publishing the story to database...")
    payload = {
        "secret_token": "ZEN_TRUYEN_2026_BYPASS",
        "title": novel_data['title'],
        "intro": novel_data['intro'],
        "author": novel_data['author'],
        "genre": novel_data['genre'],
        "cover_url": cover_url,
        "chapters": novel_data['chapters']
    }
    
    try:
        api_url = f"{WP_URL}/publish_novel.php"
        res = requests.post(api_url, json=payload, timeout=90)
        res_data = res.json()
        
        if res_data.get('success'):
            print("=" * 60)
            print("🎉 NOVEL DIRECT-PUBLISHED SUCCESSFULLY BY ANTIGRAVITY!")
            print(f"Story ID: {res_data['story_id']}")
            print(f"Title: {res_data['title']}")
            print(f"Author: {res_data['author']}")
            print(f"Cover Status: {res_data['cover_status']}")
            print(f"Chapters Published: {res_data['chapters_count']}")
            print("=" * 60)
            
            # Clean up the publish helper script from remote for security
            try:
                ftp = ftplib.FTP(FTP_HOST, timeout=30)
                ftp.login(FTP_USER, FTP_PASS)
                ftp.delete("publish_novel.php")
                print("✓ Remote helper script publish_novel.php deleted successfully.")
                ftp.quit()
            except:
                pass
                
            # Update local existing novels list cache
            try:
                with open("existing_novels.json", "r", encoding="utf-8") as f:
                    existing = json.load(f)
            except:
                existing = []
                
            new_novel_entry = {
                "id": res_data['story_id'],
                "title": res_data['title'],
                "slug": res_data['title'].lower().replace(" ", "-"),
                "intro": novel_data['intro']
            }
            existing.append(new_novel_entry)
            with open("existing_novels.json", "w", encoding="utf-8") as f:
                json.dump(existing, f, ensure_ascii=False, indent=2)
            print("✓ Local database cache existing_novels.json updated successfully.")
            
        else:
            print("❌ Publication failed:", res_data)
            
    except Exception as e:
        print("❌ HTTP trigger call failed:", e)

if __name__ == "__main__":
    main()
