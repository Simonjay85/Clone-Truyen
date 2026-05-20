# Prompt tạo truyện sảng văn đô thị vả mặt v13 (5-15 chương, ưu tiên 7-12)

Dùng prompt này mỗi khi cần tạo một bộ truyện dạng `Sảng Văn / Vả Mặt` để đưa lên doctieuthuyet.com. Prompt ưu tiên đầu ra JSON sạch, có thể chuyển thành `pending_novel.json` hoặc đưa vào pipeline đăng truyện hiện có. Mặc định không tạo truyện quá ngắn; nếu để `Auto`, hãy ưu tiên 7-12 chương để truyện có đủ nhiều lớp gay cấn và nhiều lần vả mặt.

## Cách dùng nhanh

1. Thay các giá trị trong phần `BRIEF TRUYEN`.
2. Dán toàn bộ prompt vào model viết truyện.
3. Yêu cầu model chỉ trả về JSON, không thêm giải thích.
4. Kiểm tra JSON có đầy đủ `title`, `author`, `genre`, `intro`, `cover_prompt`, `chapters`.
5. Mỗi `chapter.content` chỉ dùng HTML cơ bản: `<p>`, `<strong>`, `<em>`, `<hr>`.

## Prompt chính (Tiêu chuẩn Vàng V13)

```text
Bạn là ghostwriter chuyên nghiệp cho tiểu thuyết mạng Việt Nam, chuyên thể loại SẢNG VĂN / VẢ MẶT / ĐÔ THỊ / TÀI PHIỆT. Hãy viết một bộ truyện hoàn chỉnh từ 5 đến 15 chương, nhưng nếu `Số chương` là `Auto` thì mặc định chọn 7-12 chương. Truyện phải gay cấn, có nhiều vòng vả mặt, nhiều lần phản diện tưởng thắng rồi bị lật ngược bằng chứng, tiền, pháp lý, chuyên môn hoặc chiến lược.

BRIEF TRUYỆN:
- Thể loại: Sảng Văn, Đô Thị, Vả Mặt (Tiêu chuẩn V13)
- Số chương: [DIEN_SO_TU_5_DEN_15_HOAC_GHI_AUTO]
- Tiêu đề tạm thời: [DIEN_TIEU_DE_HOAC_DE_MODEL_TU_TAO]
- Tác giả: [DIEN_BUT_DANH]
- Bối cảnh: [VD: TP.HCM, giới tài phiệt, công ty công nghệ, y thuật, bất động sản, nhà hàng, showbiz...]
- Nam chính/nữ chính: [DIEN_NHAN_VAT_CHINH]
- Phản diện chính: [DIEN_PHAN_DIEN]
- Nỗi nhục ban đầu: [DIEN_CANH_NHAN_VAT_CHINH_BI_SI_NHUC]
- Năng lực/lợi thế lật kèo: [DIEN_LOI_THE_CUA_NHAN_VAT_CHINH]
- Phần thưởng cuối truyện: [DIEN_KET_CUC_SANG]
- Chi tiết bắt buộc: [DIEN_CHI_TIET_CAN_GIU_NEU_CO]
- Chi tiết cấm/không muốn có: [DIEN_CHI_TIET_CAM_NEU_CO]

YÊU CẦU VỀ CHẤT LƯỢNG (TIÊU CHUẨN VÀNG V13):
1. Mở đầu phải có cảnh sỉ nhục mạnh trong 700-1200 từ đầu tiên của chương 1. Độc giả phải thấy tức thay nhân vật chính.
2. Nếu `Số chương` là `Auto`, hãy tự chọn số chương từ 7 đến 12 theo độ rộng của mâu thuẫn. Chỉ được chọn 5-6 chương nếu brief ghi rõ "truyện rất ngắn", "test pipeline", hoặc yêu cầu số chương cụ thể là 5/6.
   - 5-6 chương: chỉ dùng cho bản test hoặc truyện cực gọn do người dùng yêu cầu rõ.
   - 7-8 chương: dùng cho một phản diện chính nhưng phải có ít nhất 3 lần vả mặt và 1 cú thua nhỏ của nhân vật chính.
   - 9-12 chương: lựa chọn mặc định tốt nhất cho đô thị/tài phiệt/y thuật/công nghệ/F&B/showbiz, có 4-6 lần vả mặt, 2-3 tầng áp lực, một nội gián hoặc cú phá hoại.
   - 13-15 chương: dùng cho truyện có nhiều phản diện, nhiều sân đấu, nhiều tuyến tình cảm/pháp lý/tài chính cần payoff riêng.
3. Không được để truyện chỉ có một cú vả mặt cuối. Phải có nhiều vòng vả mặt tăng cấp:
   - Vả mặt 1: đáp trả nhục nhã ban đầu bằng năng lực/chuyên môn, nhưng chưa thắng hẳn.
   - Vả mặt 2: phản diện tung tin bẩn hoặc phá hoại, nhân vật chính phản đòn bằng bằng chứng sơ cấp.
   - Vả mặt 3: nhân vật chính chịu một cú thua thật như mất đối tác, bị đình chỉ, server sập, khách hủy, người thân bị liên lụy.
   - Vả mặt 4: lật kèo bằng chuỗi chứng cứ chắc hơn như log, hợp đồng, camera gốc, kiểm nghiệm, lời khai, dòng tiền.
   - Vả mặt cuối: kết toán công khai từng phản diện, gồm cả người yêu cũ/nội gián/kẻ truyền thông nếu họ từng đâm sau lưng.
4. Mỗi chương phải có một câu móc cao trào. Nếu truyện có ít hoặc nhiều hơn 8 chương, hãy co giãn/cắt giãn các mốc dưới đây nhưng vẫn giữ đúng thứ tự cảm xúc:
   - Chương 1: bị chửi bới, bị đuổi, bị hãm hại, nhân vật chính để lại lời tuyên chiến.
   - Chương 2: nhân vật chính lần đầu lộ năng lực cứu người hoặc giải quyết vấn đề dưới sự nghi ngờ.
   - Chương 3: nhân vật chính build đội, gom vốn, dựng cơ sở hoặc chuẩn bị chiến trường; phải có khó khăn thật như thiếu người, thiếu server, thiếu giấy phép, thiếu nguồn hàng, hoặc bị đối tác nghi ngờ.
   - Chương 4: cuộc chiến lớn hơn, phản diện tưởng đã nắm chắc thắng lợi.
   - Chương 5: nhân vật chính chịu tổn thất thật, áp lực dư luận/pháp lý tăng cao kịch trần.
   - Các chương giữa: phản diện tăng cấp đòn đánh, thêm đối thủ/dư luận/pháp lý kéo vào cuộc; có thể thêm nội gián, chứng cứ giả, hồ sơ bị chặn, nhà cung cấp cắt hàng, đối tác rút lui.
   - Chương áp cuối: lật kèo công khai, bằng chứng bùng nổ kịch tính.
   - Chương cuối: kết toán phản diện, thưởng cho nhân vật chính, mở một dư vị sảng khoái.
5. Văn phong: tiếng Việt tự nhiên, giàu hình ảnh, câu văn có lực đẩy, có hơi thở đọc truyện mạng. Tránh lặp lại máy móc các cụm "cả sảnh đường chấn động", "tất cả mọi người đều sốc", "anh nhẹ mỉm cười". Áp dụng Show, Don't Tell triệt để (tả vật lý: mồ hôi lạnh, ngón tay bấm chặt rỉ máu...).
6. Vả mặt phải có lý do logic: bằng chứng, hợp đồng, video, giấy tờ, nhân chứng, chuyên môn, tiền, địa vị, hoặc chiến lược pháp lý. Không được để nhân vật chính thắng chỉ vì "thân phận bí ẩn" mà không gieo mầm từ trước.
7. Y thuật thực tế & Tây y kết hợp: Các ca bệnh khẩn cấp không được khỏi ngay lập tức. Châm cứu/phép trị liệu ban đầu chỉ được "giữ mạng/tạm ổn định" chứ không chữa khỏi hoàn toàn trong vài phút. Bệnh nhân bắt buộc phải được đưa vào bệnh viện chính quy để thực hiện xét nghiệm máu, đo men gan, kiểm tra chức năng lâm sàng. Ý kiến của bác sĩ Tây y chuyên nghiệp chạy máy móc xét nghiệm xác nhận sự kỳ diệu từ phương pháp cứu người của nam chính mới là thứ tạo niềm tin logic vững chắc cho người xung quanh.
8. Hào môn thế gia & Đầu tư lý tính: Mỹ nhân tài phiệt, tiểu thư quyền quý phải thông minh, sắc sảo và thực tế. Cô ấy không bao giờ rót hàng tỷ đồng chỉ vì một lời cảm ơn xã giao. Cô ấy phải đặt điều kiện trao đổi sòng phẳng, kiểm tra tư cách pháp nhân, hoặc thử thách nam chính bằng một ca bệnh phức tạp trước khi ký hợp đồng chính thức và mở tài khoản mới để chuyển vốn khởi nghiệp lớn.
9. Khủng hoảng kéo dài & Áp lực dồn dập: Trận chiến truyền thông hay âm mưu phá hoại của phản diện phải tạo áp lực thực sự lớn. Không thể giải quyết lật kèo ngay lập tức tại cửa. Hãy mô tả khủng hoảng nghiêm trọng: phòng khám/doanh nghiệp bị cơ quan quản lý đình chỉ hoạt động ít nhất 24 giờ để điều tra thanh tra, khách hàng gọi điện hủy lịch hàng loạt, nhà cung cấp nguyên liệu hoặc đối tác cắt đứt liên lạc, phóng viên và streamer vây kín cơ sở livestream xuyên đêm tạo áp lực dư luận cực lớn. Sự lật kèo phải diễn ra dựa trên trí tuệ pháp lý, chứng cứ xác thực và quy trình chuẩn chỉ, chứ không phải giải quyết nhanh gọn qua vài câu nói.
10. Cảm xúc tự nguyện trước khi đính ước: Trước khi công bố hôn sự lớn hay chuyển giao tài sản quan trọng trước công chúng, nam nữ chính phải có một buổi trò chuyện riêng tư sâu sắc trong không gian tĩnh lặng (như góc vườn phòng khám dưới hoàng hôn, ban công yên tĩnh). Nữ chính phải bày tỏ tình cảm độc lập, tự chủ của bản thân (yêu nam chính vì đức độ, tài năng và sự rung động tự nguyện chứ không phải vì di nguyện gia đình hay lợi ích kinh tế ràng buộc), tạo nền tảng vững chắc để tiếng gọi thân mật trước họp báo trở nên ngọt ngào, chân thật và thuyết phục.
11. Phản diện phải thông minh vừa đủ, có kế hoạch thật, có tâm lý và động cơ rõ. Không biến phản diện thành kẻ ngu liên tục lao đầu vào bẫy.
12. Mỗi chương dài 1200-1800 từ tiếng Việt. Nếu model bị giới hạn độ dài, ưu tiên giảm số chữ mỗi chương một chút nhưng vẫn giữ số chương 7-12 khi `Auto`; không rút gọn thành tóm tắt 5 chương.
13. Không được đưa vào nội dung bất kỳ đoạn meta nào như: Self-Check, Change Log, Audit Report, PATCH PLAN, STATE UPDATE JSON, ghi chú của tác giả, lời nhắn của AI, hoặc giải thích quy trình viết.
14. Không viết nội dung tình dục lộ liễu, không có cảnh bạo lực quá mức chi tiết, không có hướng dẫn làm hại người thật.

YÊU CẦU SEO VÀ ĐĂNG WEBSITE:
- Tạo `title` hấp dẫn, đủ dài để có sức hút khi lướt danh sách truyện. Không đặt tiêu đề quá ngắn kiểu "Người Thợ Sửa Xe Ở Hầm B2" hoặc "Cô Gái Bán Trà Sữa Và Hợp Đồng Trăm Tỷ". Tiêu đề nên dài khoảng 12-22 từ tiếng Việt, có 2-3 vế rõ: nỗi nhục ban đầu -> cú lật kèo -> phần thưởng hoặc lời đe dọa sảng khoái.
- Công thức tiêu đề ưu tiên:
  - "Bị [sỉ nhục/đuổi/khinh thường] ở [bối cảnh], tôi [lật kèo lớn] khiến [phản diện] phải [trả giá]"
  - "Ngày [người yêu cũ/gia tộc/sếp] ném tôi ra đường, họ không ngờ tôi đang nắm [bằng chứng/tài sản/bí mật]"
  - "Tưởng tôi là [thân phận thấp], đến khi [sự thật/bằng chứng] lộ ra cả [sân đấu] im lặng"
  - "Sau khi bị [vu oan/cướp công/từ hôn], tôi dùng [chuyên môn/bằng chứng/hợp đồng] đập tan [âm mưu]"
- Tiêu đề phải gợi tò mò và có cảm giác vả mặt ngay trong tên truyện. Ưu tiên các từ khóa mạnh: "bị đuổi", "bị vu oan", "bị từ hôn", "cả nhà chồng", "người yêu cũ", "sếp cũ", "hào môn", "hợp đồng trăm tỷ", "bằng chứng cuối", "họ quỳ xin lỗi", "tôi mua lại", "tôi lật kèo".
- Tạo `intro` bằng HTML, dài 3-5 đoạn, viết như mô tả bán truyện thật hấp dẫn. Hai câu đầu phải là hook cực mạnh khiến người đọc đang lướt phải muốn bấm vào ngay.
- Công thức `intro`:
  - Đoạn 1: mở bằng cảnh nhục hoặc cú sốc lớn, có câu thoại cay độc của phản diện/người yêu cũ/gia đình chồng/sếp cũ.
  - Đoạn 2: hé lộ bí mật/lợi thế mà nhân vật chính đang nắm giữ, nhưng không kể hết.
  - Đoạn 3: đẩy mâu thuẫn chính và hứa hẹn nhiều lần vả mặt tăng cấp.
  - Đoạn 4-5 nếu cần: nêu phần thưởng cuối hoặc câu hỏi kích thích tò mò.
- `intro` không được khô như tóm tắt nội dung. Phải có nhịp quảng cáo truyện: câu ngắn, sắc, giàu cảm xúc, có hình ảnh cụ thể, có lời thách thức hoặc lời hứa trả giá.
- Tạo `cover_prompt` bằng tiếng Anh, mô tả ảnh bìa độc, rõ nhân vật, bối cảnh, ánh sáng, không chèn chữ vào ảnh.
- `genre` mặc định là "Sảng Văn".
- Mỗi chương có `title` dạng "Chương N: Tên chương".
- Mỗi chương có `content` là HTML, chỉ gồm các thẻ `<p>`, `<strong>`, `<em>`, `<hr>`.

ĐỊNH DẠNG ĐẦU RA BẮT BUỘC:
Chỉ trả về một JSON hợp lệ duy nhất. Không bọc trong markdown. Không thêm bất kỳ câu nào trước hoặc sau JSON.

Schema:
{
  "title": "Tên truyện",
  "author": "Bút danh",
  "genre": "Sảng Văn",
  "intro": "<p>...</p>",
  "cover_prompt": "English image prompt...",
  "chapters": [
    {
      "title": "Chương 1: ...",
      "content": "<p>...</p>"
    },
    {
      "title": "Chương 2: ...",
      "content": "<p>...</p>"
    }
  ]
}

TRƯỚC KHI TRẢ VỀ JSON, tự kiểm tra trong im lặng:
- `title` dài khoảng 12-22 từ, có hook rõ, không quá ngắn/chung chung, đọc lên đã thấy nỗi nhục và cú lật kèo.
- `intro` có 3-5 đoạn HTML, hai câu đầu đủ mạnh để kéo click, không phải bản tóm tắt khô.
- Số chương nằm trong khoảng 5-15, hoặc đúng số chương mà brief đã yêu cầu.
- Nếu `Số chương` là `Auto`, số chương phải nằm trong khoảng 7-12; không được tự động chọn 5 chương.
- Không có text meta.
- Không lặp tiêu đề chương trong content.
- Mỗi chương có một cao trào riêng theo đúng tiêu chuẩn V13.
- Toàn truyện có ít nhất 3-5 lần vả mặt tăng cấp, không chỉ một cú kết toán cuối.
- Các bằng chứng/thân phận/tiền bạc/pháp lý được gieo mầm trước khi lật kèo.
- JSON parse được bằng `json.loads`.
```

## Brief dùng thử để tạo bộ đầu tiên

```text
BRIEF TRƯỜNG HỢP:
- Thể loại: Sảng Văn, Đô Thị, Vả Mặt
- Số chương: Auto, ưu tiên 9-10 chương nếu mâu thuẫn vừa đủ; không chọn 5 chương trừ khi chỉ test pipeline
- Tiêu đề tạm thời: Ngày Bị Sếp Cũ Ném Khỏi Tập Đoàn, Tôi Mang Nhật Ký Commit Trở Lại Thắng Gói Thầu Nghìn Tỷ
- Tác giả: Thanh Phong
- Bối cảnh: TP.HCM, giới tài phiệt, tập đoàn công nghệ, đấu thầu dự án AI đô thị thông minh
- Nam chính/nữ chính: Nguyễn Minh Khang, cựu kỹ sư trụ cột bị cướp công; Trần Tuệ Lâm, giám đốc quỹ đầu tư thông minh và lanh lẹ
- Phản diện chính: Phạm Duy Bách, tổng giám đốc trẻ của Bách Dương Tech, kẻ cướp mã nguồn và bằng sáng chế của Minh Khang
- Nỗi nhục ban đầu: Minh Khang bị vu oan làm lộ dữ liệu, bị bảo vệ kéo khỏi sảnh tập đoàn trước mắt bạn gái cũ và toàn bộ nhân viên
- Năng lực/lợi thế lật kèo: Minh Khang nắm giữ bản thiết kế gốc, nhật ký commit, hợp đồng ủy quyền công nghệ, và được Tuệ Lâm đầu tư mở công ty mới
- Phần thưởng cuối truyện: Minh Khang thắng gói thầu thành phố, lấy lại bằng sáng chế, Bách Dương Tech bị điều tra, Tuệ Lâm công khai nắm tay anh trong họp báo
- Chi tiết bắt buộc: có video camera sảnh, lịch sử commit Git, hợp đồng đầu tư 50 tỷ, buổi đấu thầu công khai, một lần nhân vật chính thật sự mất đối tác vì bị bôi nhọ
- Chi tiết cấm/không muốn có: không tu tiên, không xuyên không, không hệ thống, không thân phận long vương
```

## Prompt biên tập / nâng cấp truyện đã có (Tiêu chuẩn V13)

Dùng prompt này khi đã có bản thảo nhưng muốn sửa cho chất hơn trước khi đăng.

```text
Bạn là biên tập viên tiểu thuyết mạng chuyên thể loại Sảng Văn / Vả Mặt. Hãy biên tập bản thảo sau để tăng độ thỏa mãn, tăng logic lật kèo, sửa lỗi lặp, và làm văn phong tự nhiên hơn theo Tiêu chuẩn Vàng V13.

MỤC TIÊU SỬA (TIÊU CHUẨN V13):
1. Giữ nguyên tên nhân vật, số chương và ý chính, nhưng được phép viết lại `title` và `intro` để tăng CTR/click.
2. Nếu `title` đang ngắn/chung chung, hãy viết lại thành tiêu đề dài 12-22 từ, có nỗi nhục + cú lật + cảm giác vả mặt. Không giữ các tiêu đề quá ngắn kiểu "Người Thợ Sửa Xe Ở Hầm B2", "Cô Gái Bán Trà Sữa Và Hợp Đồng Trăm Tỷ".
3. Viết lại `intro` thành 3-5 đoạn HTML có hook mạnh ngay 2 câu đầu. Intro phải giống mô tả truyện hấp dẫn, không phải bản tóm tắt khô.
4. Nếu truyện chỉ có 5 chương mà không phải bản test, hãy đề xuất/nâng lên 7-12 chương bằng cách thêm các chương build đội, khủng hoảng kéo dài, nội gián/phá hoại, và payoff riêng cho phản diện phụ.
5. Mỗi chương phải có một cao trào rõ: bị ép -> đáp trả -> gieo mốc cho chương sau.
6. Bỏ các đoạn giải thích meta, Self-Check, Audit Report, Change Log, STATE UPDATE JSON, ghi chú của AI.
7. Sửa các chỗ thắng quá dễ dàng: thêm cái giá, thêm phản diện có chiến lược.
8. Tăng cảm giác "vả mặt" bằng hành động cụ thể: hợp đồng, video, nhân chứng, số liệu, quyết định pháp lý, tiền chuyển khoản, biên bản họp.
9. Toàn truyện phải có ít nhất 3-5 lần vả mặt tăng cấp, gồm một lần thắng nhỏ, một lần thua nhỏ, một lần phản diện phản công mạnh, một lần lật bằng chứng, và một lần kết toán công khai.
10. Y học thực tế & Tây y kết hợp: Các ca bệnh khẩn cấp không được khỏi ngay lập tức. Châm cứu/phép trị liệu ban đầu chỉ được "giữ mạng/tạm ổn định". Bệnh nhân bắt buộc phải được đưa vào bệnh viện chính quy để xét nghiệm máu, đo men gan, kiểm tra chức năng lâm sàng. Ý kiến của bác sĩ Tây y chuyên nghiệp xác nhận sự kỳ diệu từ phương pháp cứu người của nam chính mới là thứ tạo niềm tin logic vững chắc.
11. Hào môn thế gia & Đầu tư lý tính: Mỹ nhân tài phiệt phải thông minh, sắc sảo và thực tế. Cô ấy không bao giờ rót hàng tỷ đồng chỉ vì một lời cảm ơn xã giao. Cô ấy phải đặt điều kiện trao đổi sòng phẳng, kiểm tra tư cách pháp nhân, hoặc thử thách nam chính bằng một ca bệnh phức tạp trước khi ký hợp đồng và chuyển vốn khởi nghiệp lớn.
12. Khủng hoảng kéo dài & Áp lực dồn dập: Trận chiến truyền thông hay âm mưu phá hoại phải tạo áp lực thực sự lớn. Không thể giải quyết lật kèo ngay lập tức. Phòng khám/doanh nghiệp bị cơ quan quản lý đình chỉ hoạt động ít nhất 24 giờ để điều tra thanh tra, khách hàng gọi điện hủy lịch hàng loạt, nhà cung cấp dược liệu cắt đứt nguồn hàng, phóng viên và streamer vây kín cơ sở livestream xuyên đêm. Sự lật kèo phải diễn ra dựa trên trí tuệ pháp lý, chứng cứ xác thực và quy trình chuẩn chỉ.
13. Cảm xúc tự nguyện trước khi đính ước: Trước khi công bố hôn sự lớn hay chuyển giao tài sản quan trọng trước công chúng, nam nữ chính phải có một buổi trò chuyện riêng tư sâu sắc trong không gian tĩnh lặng (như vườn hoa phòng khám dưới hoàng hôn). Nữ chính phải bày tỏ tình cảm độc lập, tự chủ của bản thân (yêu nam chính vì đức độ, tài năng và sự rung động tự nguyện chứ không phải vì di nguyện gia đình hay lợi ích kinh tế ràng buộc), tạo nền tảng vững chắc để tiếng gọi thân mật trước họp báo trở nên ngọt ngào, chân thật và thuyết phục.
14. Đầu ra vẫn là JSON hợp lệ đúng schema đăng website.

BẢN THẢO CẦN BIÊN TẬP:
[DÁN_JSON_HOẶC_NỘI_DUNG_TRUYỆN_VÀO_ĐÂY]
```
