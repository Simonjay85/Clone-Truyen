import json, urllib.request, openpyxl

story_data = {
    "secret_token": "ZEN_TRUYEN_2026_BYPASS",
    "story_id": 5522,
    "title": "Bị Copy Toàn Bộ Source Code Ứng Dụng 10 Triệu User, Tôi Viết Lại Từ Đầu Khiến Bản Gốc Phải Đóng Cửa",
    "intro": "<p>Trần Đình Khải — lập trình viên Hà Nội — tự mình xây dựng ứng dụng học tiếng Anh LearnVN, đạt 10 triệu người dùng. Khi CTO Nguyễn Minh Kiệt — đồng sáng lập — bí mật copy toàn bộ source code, lập công ty riêng EduPro, và bán data user cho bên thứ ba, Khải mất tất cả: code, user, và niềm tin.</p>\n<p>Nhưng Khải có một thứ mà Kiệt không thể copy: kiến trúc trong đầu. Và anh viết lại từ số không — lần này, mã nguồn mở.</p>",
    "author": "Trần Đình Khải",
    "chapters": []
}

chapters = [
    {
        "title": "Chương 1: Git Push Cuối Cùng",
        "content": """<p>Trần Đình Khải phát hiện mình bị phản bội lúc hai giờ sáng — khi anh đang debug một cái bug nhỏ trên LearnVN.</p>

<p>Anh mở GitHub repository — private repo, chỉ hai người có access: anh (CEO) và Nguyễn Minh Kiệt (CTO, đồng sáng lập). Log hiển thị: Kiệt đã clone toàn bộ repo vào lúc mười một giờ đêm hôm qua, download hết — backend, frontend, database schema, API keys, và quan trọng nhất: toàn bộ dữ liệu người dùng.</p>

<p>Mười triệu người dùng. Tên, email, lịch sử học tập, điểm số, phương thức thanh toán — tất cả nằm trong cái clone đó.</p>

<p>Khải ba mươi tuổi, lập trình viên tự học, chưa có bằng đại học. Anh bỏ Đại học Bách khoa năm thứ hai — vì không chịu nổi chương trình cũ kỹ, và vì anh đã biết code tốt hơn hầu hết giảng viên. Anh viết LearnVN trong phòng trọ ở Cầu Giấy — một mình, từ dòng code đầu tiên, bằng React Native, Node.js, và MongoDB.</p>

<p>LearnVN: ứng dụng học tiếng Anh miễn phí, gamified — học bằng game, streak, leaderboard. Khác Duolingo ở chỗ: nội dung được thiết kế riêng cho người Việt — phát âm /r/ và /l/ (lỗi phổ biến nhất), ngữ pháp so sánh Việt-Anh, và từ vựng theo ngữ cảnh thực tế (đi chợ, gọi Grab, xin việc).</p>

<p>Ba năm build, từ 0 đến 10 triệu user. Không gọi vốn, không investor — Khải làm mọi thứ bằng tiền quảng cáo trong app và gói premium giá ba mươi nghìn đồng/tháng.</p>

<p>Kiệt — bạn đại học cũ — gia nhập năm thứ hai, khi LearnVN đạt hai triệu user. Khải cần người lo infrastructure — server, database, DevOps — và Kiệt giỏi mảng đó. Hai người thỏa thuận miệng: Khải 70%, Kiệt 30%.</p>

<p>Không hợp đồng. Không giấy tờ. Vì "bạn bè tin nhau."</p>

<p>Khải gọi Kiệt.</p>

<p>"Kiệt, mày clone repo lúc mười một giờ đêm. Tại sao?"</p>

<p>Im lặng. Rồi Kiệt nói — giọng bình thản, như thể đã chuẩn bị sẵn:</p>

<p>"Khải, tao lập công ty riêng rồi. EduPro. Tao dùng codebase LearnVN làm nền tảng — nhưng rebrand, cải thiện UI, và target thị trường khác. Tao cũng có quyền — tao viết 40% codebase."</p>

<p>"Mày clone CẢ database. Mười triệu user. Data cá nhân. Mày không có quyền làm vậy."</p>

<p>"Khải, mình không có hợp đồng. Không có gì chứng minh ai sở hữu gì. Mày kiện tao thì tao kiện ngược — tao nói tao viết 60%, mày viết 40%. Ai tin ai?"</p>

<p>Khải cúp máy. Tay run — không phải vì sợ, mà vì giận. Giận mình tin nhầm người. Giận mình không ký hợp đồng. Giận vì mười triệu người dùng tin tưởng giao data cho LearnVN — và giờ data đó nằm trong tay một kẻ mà Khải không còn tin.</p>

<p>Anh revoke access của Kiệt khỏi GitHub, đổi mật khẩu server, rotate API keys. Nhưng muộn — Kiệt đã có bản sao hoàn chỉnh.</p>"""
    },
    {
        "title": "Chương 2: Mẹ Và Cuốn Từ Điển Cũ",
        "content": """<p>Khải code vì mẹ.</p>

<p>Bà Trần Thị Hoa — giáo viên tiếng Anh trường THCS Gia Lâm — dạy học hai mươi lăm năm, lương bốn triệu, lớp năm mươi học sinh, sách giáo khoa cũ mười năm.</p>

<p>Mỗi tối, bà Hoa ngồi soạn bài — bằng cuốn từ điển Oxford cũ, bìa đã bong, trang giấy ố vàng, mua từ năm 1995 ở nhà sách Ngoại văn Tràng Tiền. Bà dạy tiếng Anh cho học sinh nông thôn — những đứa trẻ mà tiếng Anh duy nhất chúng nghe là từ bà, vì ở nhà không có internet, không có YouTube, không có Netflix.</p>

<p>"Mẹ ơi, sao mẹ không dùng app học tiếng Anh?"</p>

<p>"Con ơi, app gì cũng bằng tiếng Anh. Học sinh mẹ không biết tiếng Anh — thì làm sao dùng app tiếng Anh để học tiếng Anh?"</p>

<p>Câu hỏi đó — năm 2019 — là lý do Khải viết LearnVN. Anh viết app bằng tiếng Việt hoàn toàn — giao diện Việt, hướng dẫn Việt, giải thích ngữ pháp bằng so sánh Việt-Anh. Vì mẹ anh đúng: người Việt cần học tiếng Anh bằng tiếng Việt trước — rồi mới chuyển sang tiếng Anh.</p>

<p>Bà Hoa là người dùng đầu tiên — bà tải app, dùng thử, rồi cho cả lớp năm mươi học sinh dùng. Mỗi tối, bà chấm bài trên app thay vì trên giấy — và lần đầu tiên trong hai mươi lăm năm dạy học, bà thấy kết quả từng em theo thời gian thực.</p>

<p>"Con ơi, app con hay lắm. Nhưng có mấy chỗ phát âm sai — em Hùng lớp 7A nó nói 'rice' thành 'lice' mà app vẫn cho đúng."</p>

<p>Khải sửa. Anh viết module phát âm riêng cho người Việt — train AI nhận diện lỗi phát âm /r/-/l/, /s/-/sh/, /th/-/đ/ — những lỗi mà chỉ người Việt mắc.</p>

<p>Module đó là thứ làm LearnVN khác biệt — và là thứ mà Kiệt đã clone.</p>

<p>Khi Khải kể cho mẹ về việc Kiệt phản bội, bà Hoa im lặng rất lâu. Rồi bà nói:</p>

<p>"Con ơi, người ta ăn cắp code của con — nhưng không ăn cắp được cái đầu con. Con viết lại đi. Mẹ chờ."</p>"""
    },
    {
        "title": "Chương 3: Rewrite From Scratch",
        "content": """<p>Khải quyết định: không kiện (vì không có hợp đồng, kiện tụng sẽ kéo dài và tốn tiền), mà viết lại từ đầu — hoàn toàn mới, kiến trúc mới, công nghệ mới, và lần này: mã nguồn mở (open source).</p>

<p>Lý do open source: "Nếu code của tao mở, thì không ai ăn cắp được — vì ai cũng có rồi. Và nếu ai cũng có, thì giá trị không nằm ở code — mà nằm ở community, ở data riêng mà user tạo ra, và ở tốc độ cải tiến."</p>

<p>Dự án mới: LearnFree — mã nguồn mở, miễn phí hoàn toàn, không quảng cáo, không premium. Mô hình tài trợ: donation và grant từ quỹ giáo dục.</p>

<p>Tech stack mới: Flutter (cross-platform, thay React Native), Rust backend (nhanh hơn, an toàn hơn Node.js), PostgreSQL (thay MongoDB — vì relational data phù hợp hơn cho education), và self-hosted (không phụ thuộc cloud vendor).</p>

<p>Khải viết một mình — lại một mình, như ba năm trước. Phòng trọ Cầu Giấy, laptop ThinkPad cũ, ba màn hình (hai mua second-hand), cà phê đen, và code.</p>

<p>Lịch trình: code từ sáu giờ sáng đến hai giờ sáng. Ngủ bốn tiếng. Ăn cơm hộp Grab. Tắm nhanh. Code tiếp.</p>

<p>Tuần 1: setup repo GitHub công khai, viết README, thiết kế database schema.</p>

<p>Tuần 2-4: backend API — auth, user management, lesson engine, progress tracking.</p>

<p>Tuần 5-8: frontend — Flutter app, UI/UX mới (tối giản hơn LearnVN, nhanh hơn, dễ dùng hơn).</p>

<p>Tuần 9-12: AI pronunciation module — lần này train lại từ đầu, dùng Whisper (OpenAI) fine-tuned trên dataset phát âm tiếng Việt mà Khải tự thu thập (nhờ mẹ và học sinh lớp mẹ ghi âm).</p>

<p>Ba tháng. Từ dòng code đầu tiên đến app hoàn chỉnh.</p>

<p>Khải push commit cuối cùng lúc ba giờ sáng, tag version 1.0.0, viết release note:</p>

<p>"LearnFree v1.0.0. Free. Open source. Forever. Because education should not be locked behind a paywall — or stolen behind a closed repo."</p>

<p>GitHub stars trong tuần đầu: năm nghìn. Tuần thứ hai: hai mươi nghìn. Trending #1 trên GitHub trong mục Education.</p>"""
    },
    {
        "title": "Chương 4: EduPro Sụp Đổ",
        "content": """<p>Trong khi Khải viết lại từ đầu, Kiệt ra mắt EduPro — clone LearnVN với UI mới, rebrand, và gói premium giá năm mươi nghìn đồng/tháng.</p>

<p>EduPro thu hút nhanh — vì codebase vốn đã tốt (Khải viết), và Kiệt dùng data user clone được để target quảng cáo chính xác. Ba tháng đầu: hai triệu download, doanh thu năm tỷ đồng.</p>

<p>Nhưng Kiệt có một vấn đề: anh ta là DevOps, không phải developer sản phẩm. Anh ta biết chạy server, deploy, scale — nhưng không biết cải tiến sản phẩm. Bug xuất hiện, Kiệt không fix được (vì không hiểu kiến trúc mà Khải thiết kế). Feature mới không ra — vì Kiệt không biết viết feature, chỉ biết copy.</p>

<p>User bắt đầu complain: "App không cập nhật," "Bug phát âm chưa sửa," "Chức năng mới hứa từ ba tháng trước vẫn chưa có."</p>

<p>Và rồi — vụ bê bối data.</p>

<p>Một phóng viên công nghệ — Lê Minh Tú, báo VnExpress — điều tra EduPro và phát hiện: Kiệt đã bán data user cho một công ty quảng cáo — tên, email, số điện thoại, thói quen học tập — giá hai mươi triệu đồng cho gói một triệu user. Tổng cộng bán data mười triệu user: hai trăm triệu đồng.</p>

<p>Bài báo VnExpress: "EduPro bán dữ liệu 10 triệu người dùng cho bên thứ ba — vi phạm PDPA (Nghị định 13/2023 về Bảo vệ Dữ liệu Cá nhân)."</p>

<p>Bốn trăm nghìn lượt xem. User phẫn nộ. Đánh giá App Store tụt từ 4.5 sao xuống 1.2 sao trong một tuần. Hashtag #XoaEduPro trending trên Twitter Việt Nam.</p>

<p>Bộ Công an — Cục An ninh mạng — vào cuộc điều tra. Kiệt bị triệu tập.</p>

<p>Khải đọc tin, không vui — chỉ buồn. Buồn vì mười triệu người dùng đã tin tưởng giao data cho LearnVN, và data đó bị bán bởi kẻ mà Khải từng gọi là bạn.</p>"""
    },
    {
        "title": "Chương 5: Kiệt Lĩnh Án",
        "content": """<p>Tòa án Nhân dân Hà Nội xét xử Nguyễn Minh Kiệt hai tội danh: "Vi phạm quy định về bảo vệ dữ liệu cá nhân" (Nghị định 13/2023) và "Xâm phạm quyền sở hữu trí tuệ" (theo đơn tố cáo bổ sung của Khải — luật sư pro bono giúp nộp đơn dựa trên git commit history cho thấy Khải viết 85% codebase).</p>

<p>Git commit history — bằng chứng không ai ngờ tới. Mỗi dòng code trên GitHub có metadata: ai viết, viết lúc nào, commit message gì. Ba năm commit history cho thấy rõ: 85% commit từ account Khải, 15% từ account Kiệt (chủ yếu DevOps, CI/CD, server config). Khải viết sản phẩm, Kiệt chạy server — rõ ràng.</p>

<p>Tòa tuyên: Kiệt ba năm tù giam — hai năm cho tội bán data, một năm cho tội xâm phạm sở hữu trí tuệ. Bồi thường Khải: ba trăm triệu đồng. EduPro: đóng cửa, xóa toàn bộ data user.</p>

<p>Khải đứng ngoài tòa, tay cầm laptop. Anh không vào phòng xử — không muốn nhìn Kiệt bị còng tay. Ba năm trước, hai đứa ngồi quán cà phê Cầu Giấy, plan LearnVN, vẽ wireframe trên khăn giấy, cười nói về việc "thay đổi giáo dục Việt Nam." Giờ một đứa đi tù, một đứa đứng ngoài tòa.</p>

<p>Mẹ Khải gọi: "Con ơi, Kiệt bị tù rồi. Con có buồn không?"</p>

<p>"Buồn, mẹ. Buồn vì tao mất một người bạn. Nhưng tao không mất code — vì tao viết lại rồi. Và tao không mất user — vì LearnFree đang có năm triệu người dùng."</p>

<p>"Con giỏi lắm."</p>

<p>"Con không giỏi. Con chỉ không bỏ cuộc."</p>"""
    },
    {
        "title": "Chương 6: LearnFree — Open Source Toàn Cầu",
        "content": """<p>Một năm sau khi launch.</p>

<p>LearnFree: tám triệu người dùng trên toàn thế giới — Việt Nam, Indonesia, Thái Lan, Philippines, Myanmar. App được dịch sang mười hai ngôn ngữ bởi cộng đồng contributor — lập trình viên tình nguyện từ ba mươi quốc gia.</p>

<p>GitHub: 45.000 stars, 2.000 contributors, 500 pull requests mỗi tháng. LearnFree trở thành dự án open source education lớn nhất Đông Nam Á.</p>

<p>Mô hình tài trợ: Google.org tài trợ 200.000 USD cho hai năm phát triển. Mozilla Foundation tài trợ 50.000 USD. UNICEF Việt Nam hợp tác triển khai tại mười tỉnh vùng cao.</p>

<p>Khải thuê văn phòng nhỏ ở Cầu Giấy — bốn mươi mét vuông, bốn nhân viên full-time, mười contributor part-time trên GitHub. Anh không gọi đó là "công ty" — anh gọi là "community."</p>

<p>"LearnFree không phải sản phẩm của tao. Nó là sản phẩm của cộng đồng. Tao chỉ viết dòng code đầu tiên — bốn mươi lăm nghìn người viết tiếp."</p>

<p>Đặc biệt: AI pronunciation module — module mà Khải train lại từ đầu, dùng dataset do mẹ và học sinh Gia Lâm ghi âm — giờ đã được mở rộng sang mười hai ngôn ngữ. Một lập trình viên Indonesia fine-tune cho tiếng Bahasa, một developer Philippines cho tiếng Tagalog, một contributor Myanmar cho tiếng Miến.</p>

<p>Google I/O 2024 — Khải được mời nói chuyện trên sân khấu chính, chủ đề: "Open Source Education: How a Solo Developer from Hanoi Built a Movement."</p>

<p>"I built LearnVN alone, in a rented room in Hanoi. My cofounder stole the code. I rewrote it from scratch — but this time, I made it open source. Because if everyone owns the code, no one can steal it."</p>

<p>"Education should be free. Code should be free. And trust — once broken — should be rebuilt, not hidden."</p>

<p>Vỗ tay đứng. Năm nghìn developer tại Shoreline Amphitheatre.</p>"""
    },
    {
        "title": "Chương 7: Lớp Học Vùng Cao",
        "content": """<p>UNICEF Việt Nam triển khai LearnFree tại mười tỉnh vùng cao — Hà Giang, Lào Cai, Lai Châu, Sơn La, Điện Biên, Yên Bái, Cao Bằng, Bắc Kạn, Lạng Sơn, Tuyên Quang.</p>

<p>Mô hình: tablet giá rẻ (Lenovo Tab M8, tài trợ bởi Google.org) cài sẵn LearnFree, phát cho học sinh từ lớp 3 đến lớp 9 tại các trường vùng cao. Một trăm trường, mười nghìn tablet, mười nghìn học sinh.</p>

<p>Khải đích thân đi Hà Giang — đường đèo Mã Pí Lèng, xe máy, bốn tiếng từ TP. Hà Giang đến trường Tiểu học Sủng Là, xã Sủng Là, huyện Đồng Văn.</p>

<p>Lớp học: tường đá xếp, mái tôn, bàn gỗ cũ, ba mươi hai học sinh Hmông. Cô giáo — Vàng Thị Mỷ, hai mươi bốn tuổi, người Hmông, tốt nghiệp sư phạm Hà Giang — đang dạy tiếng Anh bằng bảng phấn và giọng phát âm tự học.</p>

<p>Khải phát tablet cho từng em. Mở app LearnFree. Bài đầu tiên: "Hello. My name is..."</p>

<p>Một em — Sùng A Páo, lớp 4, chín tuổi, mặt đỏ vì lạnh — chạm vào màn hình, nghe phát âm, rồi nói theo: "Hê-lô. Mai-nem-ít Páo."</p>

<p>App chấm: "Good! Try again — press the blue button to hear the correct pronunciation."</p>

<p>Páo nhấn nút xanh, nghe, nói lại: "Hello. My name is Páo."</p>

<p>App: "Excellent! ⭐⭐⭐"</p>

<p>Páo cười — nụ cười rộng, hở răng sún, mắt sáng. Lần đầu tiên em nghe giọng người bản ngữ nói tiếng Anh — qua chiếc tablet bảy triệu đồng, chạy app miễn phí, viết bởi một anh lập trình viên ở Cầu Giấy.</p>

<p>Cô Mỷ khóc — không buồn, mà vui. Vì cô dạy tiếng Anh ba năm mà chưa bao giờ nghe được phát âm chuẩn cho học sinh — vì cô cũng tự học, cũng sai phát âm, cũng không có ai sửa.</p>

<p>"Anh Khải ơi, cảm ơn anh. Em dạy tiếng Anh mà em cũng không biết phát âm đúng. Giờ app dạy giùm em."</p>

<p>Khải đứng cuối lớp, nhìn ba mươi hai em Hmông cầm tablet, học tiếng Anh — và anh hiểu: đây là lý do anh viết code. Không phải cho mười triệu user, không phải cho GitHub stars, không phải cho Google I/O. Mà cho Sùng A Páo — em bé Hmông chín tuổi nói "Hello" lần đầu tiên trên đỉnh Mã Pí Lèng.</p>"""
    },
    {
        "title": "Chương 8: Commit Tiếp Theo",
        "content": """<p>Đêm, phòng trọ Cầu Giấy.</p>

<p>Khải ngồi trước laptop ThinkPad — ba màn hình sáng, terminal mở, VS Code trên màn hình chính. Anh đang viết feature mới cho LearnFree: offline mode — cho phép học sinh vùng cao học tiếng Anh KHÔNG cần internet.</p>

<p>Vì Hà Giang không có 4G ổn định. Sủng Là không có WiFi. Và Sùng A Páo không thể học nếu app cần mạng.</p>

<p>Offline mode: download toàn bộ bài học, audio, và AI pronunciation model xuống tablet — khoảng 500MB — và chạy hoàn toàn offline. AI phát âm chạy on-device bằng TensorFlow Lite — nhỏ gọn, nhanh, không cần server.</p>

<p>Khải viết từ tám giờ tối đến hai giờ sáng. Coffee đen. Mì gói. Và code.</p>

<p>Hai giờ sáng, anh push commit:</p>

<p><code>git commit -m "feat: offline mode with on-device pronunciation AI. For Pao and kids in Ha Giang who don't have internet."</code></p>

<p><code>git push origin main</code></p>

<p>Commit message đó — "For Pao" — được 2.000 developer trên GitHub heart. Một contributor từ Kenya comment: "I'm building the same thing for Swahili learners. Can I reuse your offline module?" Khải reply: "It's open source. It's yours."</p>

<hr>

<p>Anh đóng laptop, nhìn ra cửa sổ. Cầu Giấy đêm khuya — đèn đường vàng, xe máy thưa thớt, quán phở đã đóng. Giống hệt ba năm trước — khi anh ngồi đây, viết dòng code đầu tiên của LearnVN.</p>

<p>Nhưng ba năm trước, anh viết một mình, trong private repo, cho mười triệu user mà anh không bao giờ gặp. Giờ anh viết cùng bốn mươi lăm nghìn người, trong public repo, cho Sùng A Páo và những em bé mà anh đã gặp.</p>

<p>Anh mở ví, lấy tấm ảnh — mẹ đứng trước lớp học Gia Lâm, tay cầm cuốn từ điển Oxford cũ, bìa bong. Tấm ảnh Khải mang theo từ năm mười tám tuổi — khi anh bỏ đại học, mẹ không giận, chỉ nói: "Con làm gì thì làm — miễn là con giúp được người khác học."</p>

<p>"Mẹ ơi, con đang giúp. Bằng code."</p>

<p>Anh nhét ảnh lại vào ví, tắt đèn, nằm xuống. Bốn tiếng ngủ. Sáng mai, sáu giờ, anh sẽ dậy, mở laptop, và viết commit tiếp theo.</p>

<p>Vì code — như giáo dục — không bao giờ xong. Nó chỉ có version tiếp theo.</p>"""
    }
]

story_data["chapters"] = chapters

print("✅ Truyện 5522 viết xong — 8 CHƯƠNG!")
for i, ch in enumerate(chapters):
    print(f"  Ch{i+1}: {ch['title']} — {len(ch['content'])} chars")

print("\n📤 Uploading...")
url = "https://doctieuthuyet.com/overwrite_story_v13.php"
payload = json.dumps(story_data).encode('utf-8')
req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
try:
    resp = urllib.request.urlopen(req, timeout=120)
    result = json.loads(resp.read().decode('utf-8'))
    print(f"  ✅ Success! ID={result['story_id']}, Chapters={result['chapters_count']}")
except Exception as e:
    print(f"  ❌ Error: {e}")

print("\n📊 Updating Excel...")
wb = openpyxl.load_workbook("danh_sach_truyen_doctieuthuyet.xlsx")
ws = wb.active
for r in range(5, ws.max_row+1):
    if ws.cell(row=r, column=2).value and str(ws.cell(row=r, column=2).value).strip() == "5522":
        ws.cell(row=r, column=6).value = 8
        ws.cell(row=r, column=12).value = "Lập trình viên bị CTO clone toàn bộ source code app 10 triệu user. Viết lại open source, kẻ cắp bán data bị tù 3 năm. App mới triển khai tại vùng cao."
        ws.cell(row=r, column=13).value = "REWRITE TOÀN BỘ: 10 chương quá ngắn → 8 CHƯƠNG ĐẦY ĐẶN"
        ws.cell(row=r, column=14).value = "☑️ Đã sửa"
        print(f"  ✅ Excel updated row {r}")
        break
wb.save("danh_sach_truyen_doctieuthuyet.xlsx")
print("\n✅ HOÀN THÀNH TRUYỆN 5522!")
