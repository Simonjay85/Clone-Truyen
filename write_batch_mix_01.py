#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
write_batch_mix_01.py — Batch 1: 5 Truyện Sảng Văn CẢI TIẾN (Stories 1-5)
===========================================================================
Template A cải tiến: Ch5 có twist, Ch8 là climax, Ch9 đa dạng
Story 1: Họa sĩ NFT bị cướp tác phẩm (cover 4)
Story 2: Nữ KTS bị đạo thiết kế (cover 5)
Story 3: Dev bị copy source code (cover 6)
Story 4: BS da liễu bị cướp công thức mỹ phẩm (cover 7)
Story 5: Nhà văn bị đạo văn bestseller (cover 8)
"""

import json, os, sys, re, time, random, subprocess, ftplib, requests

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
SECRET_TOKEN = "ZEN_TRUYEN_2026_BYPASS"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

def split_sentences(text):
    t = re.sub(r'\s+', ' ', text).strip()
    abbrevs = ["TS.", "BS.", "PGS.", "GS.", "CEO.", "CFO.", "CTO.", "Dr.", "Mr.", "Mrs.", "Ph.D.", "HĐQT.", "IPO.", "PCCC.", "KTS.", "NFT.", "USD."]
    for i, a in enumerate(abbrevs):
        t = t.replace(a, f"__A{i}__")
    t = re.sub(r'([.!?]["\'\"]?)\s+(?=[A-ZÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄĐÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ"\'\"\d])', r'\1‖', t)
    for i, a in enumerate(abbrevs):
        t = t.replace(f"__A{i}__", a)
    return [s.strip() for s in t.split("‖") if s.strip()]

def fmt(raw):
    clean = re.sub(r'<[^>]+>', ' ', raw)
    return "\n".join(f"<p>{s}</p>" for s in split_sentences(clean)) + "\n"

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 1: HỌA SĨ NFT BỊ CƯỚP TÁC PHẨM
# Template A Cải Tiến: twist ở Ch5, climax Ch8
# ═══════════════════════════════════════════════════════════════════════════════

S1_TITLE = "BỊ CƯỚP TOÀN BỘ BST NFT TRIỆU ĐÔ, TÔI VẼ LẠI TỪ SỐ 0 KHIẾN KẺ TRỘM PHÁ SẢN TRÊN CHÍNH SÀN GIAO DỊCH"
S1_AUTHOR = "Hoàng Minh Trí"
S1_COVER = "base_cover_4.png"
S1_INTRO = """<p><strong>"Ba năm tôi vẽ không ngủ, tạo ra bộ sưu tập nghệ thuật số 'Linh Hồn Việt' — 888 tác phẩm NFT mang hồn văn hóa Việt Nam. Đổi lại, ngay trước đêm mint chính thức, đồng sáng lập cướp toàn bộ smart contract, đổi ví chủ sở hữu, và bán hết trong 12 phút."</strong></p>
<p>Hoàng Minh Trí, họa sĩ kỹ thuật số tài năng nhất thế hệ Gen Z Việt Nam, bị Dương Quốc Bảo — đồng sáng lập kiêm CTO của dự án — cướp trắng 888 tác phẩm NFT trị giá hai triệu đô trước đêm ra mắt.</p>
<p>Mất tất cả tác phẩm, bị cộng đồng crypto nghi ngờ là "rug pull," Trí vẽ lại từ số 0 — nhưng lần này, anh vẽ bằng cả cơn giận và nỗi đau, tạo ra bộ sưu tập mới khiến cả thế giới NFT phải quỳ gối.</p>"""

S1_CHAPTERS = [
("Chương 1: Đêm Bị Cướp", """Hai giờ sáng, căn studio tầng áp mái ở Thảo Điền, Hoàng Minh Trí đang livestream countdown trên Discord cho cộng đồng mười lăm nghìn người. Bộ sưu tập "Linh Hồn Việt" — 888 NFT vẽ tay, mỗi tác phẩm là một linh vật, thần thoại, hoặc biểu tượng văn hóa Việt Nam theo phong cách cyberpunk — sẽ mint trên Ethereum trong đúng hai tiếng nữa.

Ba năm vẽ. Mỗi tác phẩm mất trung bình mười hai giờ — từ sketch bút chì, scan, digital painting trên Procreate, rồi render final trên Photoshop. 888 tác phẩm nhân mười hai giờ — hơn mười nghìn giờ lao động nghệ thuật.

"Mọi người ơi, hai tiếng nữa thôi!" Trí cười trước camera, mắt thâm quầng nhưng rực sáng. Discord chat tràn ngập emoji lửa và trái tim.

Rồi anh thấy nó.

Wallet address trên smart contract — address mà Trí đã kiểm tra hàng trăm lần — đã thay đổi. Không phải ví chung của hai người sáng lập. Mà là một ví lạ.

Trí mở Etherscan, tay run. Lịch sử giao dịch: ba mươi phút trước, smart contract đã được update owner thành ví 0x7aB3...dF92. Và mười phút trước — 888 NFT đã được mint và list trên OpenSea với giá floor 0.5 ETH.

"Không... không thể..." Trí lẩm bẩm.

Anh gọi Dương Quốc Bảo — đồng sáng lập, CTO phụ trách blockchain — mười lần. Không ai nghe. Gọi lần thứ mười một, số điện thoại đã bị chặn.

Discord bắt đầu loạn: "RUG PULL!" "SCAM!" "Hoàng Minh Trí lừa đảo!" Cộng đồng mười lăm nghìn người quay lưng trong năm phút. Twitter trending: #LinhHonVietScam.

Trí ngồi sụp xuống sàn studio, laptop vẫn mở, Discord vẫn chửi rủa. Ba năm vẽ, mười nghìn giờ, 888 tác phẩm — bị cướp trong ba mươi phút bởi chính người anh tin tưởng nhất.

Bảo — thằng bạn đại học, thằng bạn cùng nhậu, thằng bạn anh chia năm mươi phần trăm equity — đã cướp toàn bộ, mint lậu, bán hết 888 NFT trong mười hai phút, thu về bốn trăm bốn mươi bốn ETH — khoảng một triệu hai trăm nghìn đô tại thời điểm đó — rồi biến mất."""),

("Chương 2: Vẽ Lại Từ Số 0", """Ba ngày sau vụ cướp, Trí khóa tất cả mạng xã hội, tắt điện thoại, nhốt mình trong studio. Anh không ăn, không ngủ, chỉ vẽ.

Nhưng lần này khác. Ba năm trước, anh vẽ "Linh Hồn Việt" bằng đam mê — nét vẽ mềm mại, màu sắc hài hòa, phong cách fantasy nhẹ nhàng. Lần này, anh vẽ bằng cơn giận.

Bộ sưu tập mới: "Tro Tàn" — 999 tác phẩm. Mỗi tác phẩm là một biểu tượng Việt Nam bị phá hủy rồi tái sinh từ tro: rồng cháy thành tro rồi mọc lại bằng lửa xanh, áo dài bị xé nát rồi khâu lại bằng dây thép, đèn lồng Hội An vỡ tan rồi ghép lại bằng ánh sáng neon.

Phong cách: dark art, glitch effect, cyberpunk dystopia. Không còn đẹp dịu dàng — mà đẹp dữ dội, đau đớn, và đầy sức mạnh.

"Tôi vẽ 'Linh Hồn Việt' bằng tình yêu. Tôi vẽ 'Tro Tàn' bằng sự thật — rằng bị phản bội không giết được nghệ sĩ, nó chỉ làm nghệ sĩ vẽ hay hơn," Trí viết trên trang cá nhân duy nhất anh mở lại — một thread Twitter dài bảy tweet kể toàn bộ câu chuyện.

Thread viral — năm triệu lượt đọc trong hai mươi bốn giờ. Cộng đồng crypto quốc tế chuyển từ "scam" sang "respect." Beeple, nghệ sĩ NFT nổi tiếng nhất thế giới, retweet: "This is what real art looks like. @HoangMinhTri I'm watching."

Hai tháng, 999 tác phẩm hoàn thành."""),

("Chương 3: Mint Đêm Trăng Rằm", """Trí chọn đêm rằm tháng Tám — Tết Trung Thu — để mint "Tro Tàn." Không qua OpenSea. Anh tự viết smart contract mới — lần này, private key chỉ một mình anh giữ, multi-sig wallet, audit bởi CertiK.

Mint price: 0.08 ETH — rẻ hơn nhiều so với "Linh Hồn Việt" bản cũ. "Tôi không vẽ cho đại gia crypto. Tôi vẽ cho người yêu nghệ thuật," Trí tuyên bố.

999 NFT sold out trong bảy phút. Revenue: gần tám mươi ETH — khoảng hai trăm nghìn đô. Ít hơn số Bảo cướp? Đúng. Nhưng lần này, mỗi đồng đều sạch.

Royalty 10% trên mọi giao dịch thứ cấp. Tuần đầu sau mint, volume giao dịch trên secondary market đạt năm trăm ETH — Trí nhận năm mươi ETH royalty. Floor price tăng từ 0.08 lên 1.2 ETH trong hai tuần.

Sotheby's liên hệ: muốn đấu giá bản physical print limited edition của "Tro Tàn" tại New York."""),

("Chương 4: Bảo Phản Công", """Bảo không biến mất. Gã ẩn danh trên blockchain, nhưng vẫn hoạt động. Khi thấy "Tro Tàn" thành công, gã tung chiêu bẩn: lập tài khoản ẩn danh tố Trí "đạo ý tưởng từ Linh Hồn Việt" — bộ sưu tập mà chính gã cướp.

"Linh Hồn Việt là tài sản của tôi. Hoàng Minh Trí chỉ là nhân viên thuê vẽ. Tro Tàn là phiên bản copy," Bảo viết trên Twitter từ account ẩn danh.

Gã còn thuê bot farm report tài khoản Twitter và OpenSea của Trí, khiến "Tro Tàn" bị gỡ khỏi OpenSea tạm thời — "under review for copyright claim."

Cộng đồng lại dao động. Floor price "Tro Tàn" giảm từ 1.2 xuống 0.4 ETH trong ba ngày.

Trí bình tĩnh. Anh không phản bác bằng lời. Anh mở Procreate, bật screen recording, và livestream quá trình vẽ một tác phẩm mới trong tám tiếng liên tục — từ sketch đến final. Mười lăm nghìn người xem trực tiếp.

"Đây là cách tôi vẽ. Mỗi nét cọ, mỗi layer, mỗi màu — là của tôi. Ai muốn nói tôi đạo, hãy ngồi vẽ tám tiếng đi rồi nói."

Clip tám tiếng được cắt thành video năm phút, đạt hai mươi triệu lượt xem trên TikTok."""),

("Chương 5: Bí Mật Đen Tối Của Bảo", """Trong khi Trí vẽ, một thành viên cộng đồng tên CryptoDetective_VN âm thầm truy vết blockchain. Ví 0x7aB3...dF92 mà Bảo dùng để cướp "Linh Hồn Việt" không chỉ chứa tiền từ vụ cướp — nó còn liên kết với ba dự án NFT scam khác ở Thái Lan, Indonesia, và Philippines.

Bảo không phải lần đầu. Gã là kẻ chuyên nghiệp — gia nhập dự án NFT với tư cách CTO, chiếm quyền smart contract, cướp tiền mint, rồi biến mất. Bốn dự án, bốn quốc gia, tổng thiệt hại hơn năm triệu đô.

CryptoDetective_VN public toàn bộ on-chain evidence trên Twitter — thread dài hai mươi tweet, mỗi tweet kèm screenshot Etherscan. Thread đạt mười triệu impressions.

Cộng đồng crypto quốc tế gắn tag: #CatchDuongBao. Interpol vào cuộc vì nạn nhân ở bốn quốc gia. FBI Cyber Division phối hợp.

"Tro Tàn" floor price tăng vọt từ 0.4 lên 3.5 ETH — vì giờ ai cũng biết: Trí là nạn nhân thật, và "Tro Tàn" là tác phẩm nghệ thuật thật."""),

("Chương 6: Đấu Giá Sotheby's", """Sotheby's New York tổ chức đấu giá "Tro Tàn: Genesis" — tác phẩm số 1 trong bộ 999, bản physical print kích thước hai mét nhân ba mét, kèm NFT gốc.

Giá khởi điểm: năm mươi nghìn đô. Giá chốt: bốn trăm hai mươi nghìn đô — kỷ lục cho nghệ sĩ Đông Nam Á tại Sotheby's.

Người mua: một nhà sưu tập Nhật Bản, nói với báo chí: "Tôi mua vì câu chuyện. Nghệ thuật bị cướp rồi tái sinh — đó là tinh thần wabi-sabi hoàn hảo."

Tổng giá trị bộ sưu tập "Tro Tàn" trên thị trường thứ cấp: mười hai triệu đô — gấp mười lần số Bảo cướp.

Trí ký hợp đồng với SuperRare — sàn NFT cao cấp nhất — trở thành nghệ sĩ Việt Nam đầu tiên có "Curated Artist" status."""),

("Chương 7: Bà Ngoại Và Cuốn Truyện Tranh", """Trí vẽ từ nhỏ vì bà ngoại. Bà Hoàng Thị Lý, tám mươi tuổi, bán bánh cuốn ở chợ Bến Thành. Bà không biết chữ, nhưng mỗi tối bà kể chuyện cổ tích cho Trí bằng miệng — Sơn Tinh Thủy Tinh, Thánh Gióng, Cóc kiện Trời — và Trí vẽ lại thành truyện tranh trên giấy vở.

"Bà ơi, con vẽ Thánh Gióng cưỡi ngựa sắt bay lên trời nè!"

"Đẹp quá con ơi! Nhưng ngựa sắt phải to hơn nữa, Thánh Gióng nhà mình hùng dũng lắm!"

"Linh Hồn Việt" — 888 tác phẩm — mỗi tác phẩm đều bắt nguồn từ những câu chuyện bà kể. Rồng, phượng, kỳ lân, rùa — tất cả từ giọng kể trầm ấm của bà trong căn nhà nhỏ ở Sài Gòn.

Khi Trí kể cho bà về vụ bị cướp, bà im lặng một lúc rồi nói: "Con ơi, người ta cướp được tranh, nhưng cướp sao được tay con? Con vẽ lại đi."

Câu nói đó — "cướp sao được tay con" — Trí khắc lên NFT số 888 của "Tro Tàn." Tác phẩm này không bán. Giữ mãi."""),

("Chương 8: Bảo Bị Bắt — Đối Đầu Cuối Cùng", """Interpol phối hợp cảnh sát Thái Lan bắt Dương Quốc Bảo tại một resort ở Phuket — nơi gã đang tiêu tiền cướp. Wallet bị freeze bởi lệnh tòa: ba trăm ETH còn lại trong ví.

Nhưng trước khi bị bắt, Bảo kịp gửi một email cuối cho Trí:

"Trí, mày giỏi vẽ nhưng mày ngu kinh doanh. Tao chỉ lấy cái mà mày không biết bảo vệ. Đó là bài học miễn phí."

Trí đọc email, không trả lời. Thay vào đó, anh vẽ một tác phẩm mới: chân dung Bảo — nhưng mặt Bảo được vẽ bằng hàng nghìn nét chữ nhỏ xíu, mỗi nét chữ là tên một nạn nhân của bốn vụ scam. Tác phẩm tên "Mặt Nạ" — đấu giá từ thiện, toàn bộ tiền quyên góp cho nạn nhân crypto scam.

"Mặt Nạ" bán được một trăm nghìn đô. Mọi đồng đều đến tay nạn nhân.

Tòa Thái Lan tuyên: Bảo mười năm tù, bồi thường cho nạn nhân bốn quốc gia tổng bảy triệu đô."""),

("Chương 9: Triển Lãm 'Tro Tàn' Tại Bảo Tàng Nghệ Thuật Đương Đại", """Bảo tàng Nghệ thuật Đương đại Singapore (SAM) mời Trí triển lãm solo — 'Tro Tàn: From Ashes' — triển lãm NFT art đầu tiên của nghệ sĩ Đông Nam Á tại bảo tàng quốc gia.

999 tác phẩm được hiển thị trên màn hình LED khổng lồ, mỗi tác phẩm kèm QR code liên kết blockchain — người xem có thể thấy lịch sử giao dịch, ai đang sở hữu, và câu chuyện đằng sau.

Bảy mươi nghìn người đến xem trong hai tuần. The Straits Times: "Hoàng Minh Trí là Banksy của Đông Nam Á — nghệ thuật từ nỗi đau, phi tập trung từ lòng tin."

Trí không nhận giải thưởng gì cả. Anh không cần. 999 tác phẩm treo trên tường bảo tàng — đó là giải thưởng."""),

("Chương 10: Quay Về Studio Tầng Áp Mái", """Trí quay về studio tầng áp mái ở Thảo Điền — nơi bắt đầu và nơi bị cướp. Anh không chuyển đi, không upgrade. Vẫn cái bàn vẽ cũ, cái iPad Pro có vết xước, và cái ghế xoay kêu cót két.

Bà ngoại gửi cho anh một hộp bánh cuốn từ chợ Bến Thành, kèm tờ giấy viết nguệch ngoạc (nhờ hàng xóm viết hộ): "Con vẽ đẹp lắm. Bà tự hào."

Trí ăn bánh cuốn, mở Procreate, bắt đầu vẽ bộ sưu tập thứ ba. Lần này không phải vì bị cướp, không phải vì tức giận. Mà vì anh yêu vẽ — giống hệt cậu bé bảy tuổi vẽ Thánh Gióng trên giấy vở cho bà xem.

Ngoài cửa sổ, Sài Gòn về đêm nhấp nháy ánh đèn. Trên blockchain, 999 "Tro Tàn" vẫn sống, vẫn được giao dịch, vẫn mang theo câu chuyện của anh đi khắp thế giới.

Trí mỉm cười, tay cầm bút stylus, và vẽ nét đầu tiên."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 2: NỮ KIẾN TRÚC SƯ BỊ ĐẠO THIẾT KẾ
# ═══════════════════════════════════════════════════════════════════════════════

S2_TITLE = "BỊ ĐẠO TOÀN BỘ THIẾT KẾ BẢO TÀNG, TÔI XÂY CÔNG TRÌNH KHIẾN THẰNG ĐẠO NHÁI BỊ CẤM HÀNH NGHỀ TRÊN TOÀN THẾ GIỚI"
S2_AUTHOR = "Nguyễn Thanh Vân"
S2_COVER = "base_cover_5.png"
S2_INTRO = """<p><strong>"Hai năm tôi thiết kế bảo tàng lịch sử Việt Nam mới — công trình mơ ước của đời KTS. Đổi lại, sếp cũ gửi bản vẽ của tôi cho văn phòng KTS Trung Quốc, họ xây trước, và cả thế giới nghĩ tôi là kẻ đạo nhái."</strong></p>
<p>Nguyễn Thanh Vân, KTS trẻ tài năng nhất thế hệ, bị Giám đốc văn phòng KTS Hùng Phát là Lê Trọng Hùng bán bản vẽ bảo tàng cho đối tác Trung Quốc — ZhangWei Architecture — xây trước ở Thượng Hải.</p>
<p>Bị mang tiếng đạo nhái, bị tước giải thưởng kiến trúc, Vân chứng minh mình là tác giả gốc và thiết kế công trình mới vĩ đại hơn, khiến kẻ ăn cắp bị UIA cấm hành nghề toàn cầu.</p>"""

S2_CHAPTERS = [
("Chương 1: Bản Vẽ Bị Đánh Cắp", """Nguyễn Thanh Vân nhận cuộc gọi từ bạn đại học lúc sáu giờ sáng: "Vân ơi, mày xem ArchDaily ngay đi. Có công trình ở Thượng Hải giống y hệt thiết kế bảo tàng của mày!"

Vân mở laptop, tay run. ArchDaily — trang kiến trúc uy tín nhất thế giới — đang feature "Shanghai Cultural Center" của ZhangWei Architecture. Và nó giống thiết kế bảo tàng lịch sử Việt Nam mà Vân đã làm hai năm — giống chín mươi phần trăm.

Mái vòm hình nón lá cách điệu, hệ khung thép uốn cong mô phỏng sông Hồng, sảnh chính hình chữ V — tất cả đều là concept original của Vân. Thậm chí góc nghiêng mái đúng 23.5 độ — con số mà Vân tính dựa trên góc chiếu nắng Hà Nội vĩ tuyến 21, không có lý do gì để một công trình ở Thượng Hải vĩ tuyến 31 dùng.

"Ai đã gửi bản vẽ cho bọn Trung Quốc?" Vân lẩm bẩm.

Câu trả lời rõ ràng: chỉ có một người ngoài Vân có access vào toàn bộ file AutoCAD và Revit — Lê Trọng Hùng, Giám đốc văn phòng KTS Hùng Phát, nơi Vân làm việc.

Vân lao đến văn phòng. Hùng ngồi uống cà phê đọc báo, bình thản như mọi ngày.

"Anh Hùng, anh giải thích cái này đi." Vân đặt laptop lên bàn, mở ArchDaily.

Hùng liếc qua, nhún vai: "Trùng hợp thôi. Kiến trúc hiện đại thì concept hay trùng nhau."

"TRÙNG HỢP? Góc mái 23.5 độ — góc chiếu nắng Hà Nội — trên công trình Thượng Hải? Hệ khung kết cấu đúng tỷ lệ module 3.6 mét mà tôi tính cho đất Hà Nội? Anh bán bản vẽ của tôi!"

Hùng đứng dậy, giọng lạnh: "Vân, cô là nhân viên. Mọi thiết kế tạo ra trong thời gian làm tại Hùng Phát đều thuộc sở hữu công ty. Cô muốn kiện? Kiện đi. Nhưng trên giấy tờ, tác giả là Hùng Phát Architecture, không phải Nguyễn Thanh Vân."

Và tệ hơn: giới kiến trúc quốc tế bắt đầu gọi Vân là "kẻ đạo nhái" — vì Shanghai Cultural Center xây trước, bảo tàng Hà Nội mới trên giấy. Ai tin người vẽ sau?"""),

("Chương 2: Chứng Minh Bằng Metadata", """Vân không khóc. Cô lập tức liên hệ luật sư sở hữu trí tuệ và chuyên gia digital forensics. Bằng chứng: file AutoCAD gốc trên máy Vân có metadata tạo ngày — hai năm trước Shanghai Cultural Center khởi công. Lịch sử Git commits trên server nội bộ ghi rõ từng lần sửa, từ concept đến final.

Nhưng Hùng cũng không ngu. Gã đã xóa lịch sử server nội bộ và tuyên bố: "File gốc là của công ty, Vân chỉ thực hiện theo brief của tôi."

Vân mở tủ hồ sơ cá nhân — ba cuốn sketchbook vẽ tay, mỗi trang ghi ngày, ký tên, đóng dấu bưu điện. Thói quen từ thời sinh viên: mỗi concept mới, Vân vẽ tay, chụp ảnh, gửi bưu điện cho chính mình — "bằng sáng chế nghèo" — phong bì chưa mở, dấu bưu điện là bằng chứng thời gian.

Ba phong bì, ba dấu bưu điện, hai năm trước Shanghai khởi công. Không thể giả mạo."""),

("Chương 3: UIA Vào Cuộc", """Vân nộp đơn khiếu nại lên UIA — Liên đoàn Kiến trúc sư Quốc tế — với bằng chứng: sketchbook, metadata, email nội bộ (Vân lưu bản sao), và phân tích kỹ thuật chứng minh góc 23.5 độ chỉ có ý nghĩa ở Hà Nội.

UIA thành lập hội đồng điều tra. ZhangWei Architecture bị yêu cầu giải trình. Kết quả: ZhangWei thừa nhận nhận bản vẽ từ "đối tác Việt Nam" nhưng "tưởng đó là thiết kế gốc của Hùng Phát."

UIA tuyên: Hùng Phát Architecture vi phạm đạo đức nghề nghiệp, bán trái phép thiết kế của nhân viên. ZhangWei bị cảnh cáo. Vân được công nhận là tác giả gốc.

Hùng mất mặt trước giới kiến trúc. Nhưng gã không nhận thua."""),

("Chương 4: Hùng Phản Công", """Hùng thuê luật sư kiện Vân "vi phạm hợp đồng lao động — tiết lộ bí mật thương mại." Gã tuyên bố Vân đã mang thiết kế nội bộ ra ngoài trái phép.

Đồng thời, gã liên hệ các văn phòng KTS lớn ở Việt Nam, cảnh báo: "Không thuê Nguyễn Thanh Vân — cô ta là nhân viên phản bội, tiết lộ bí mật công ty."

Vân bị blacklist ngầm trong ngành. Không ai dám thuê. Cô gần như phá sản — tiền tiết kiệm cạn, tiền thuê nhà chưa đóng, mẹ gọi điện lo lắng.

"Con ơi, hay con về quê dạy vẽ, đừng theo nghề KTS nữa..."

"Không, mẹ. Con không bỏ cuộc." """),

("Chương 5: Phát Hiện Đường Dây Bán Thiết Kế", """Trong quá trình UIA điều tra, một KTS trẻ người Indonesia tên Adi liên hệ Vân: "Chị Vân, tôi cũng bị. Hùng Phát bán thiết kế resort của tôi cho một công ty Hàn Quốc."

Rồi thêm một KTS Philippines. Rồi một KTS Campuchia. Hùng không chỉ bán thiết kế của Vân — gã đã bán thiết kế của ít nhất năm KTS nhân viên cho đối tác nước ngoài trong ba năm. Tổng giá trị: hơn hai triệu đô.

Vân gọi đó là "đường dây buôn bản vẽ xuyên biên giới." Cô tập hợp chứng cứ từ năm nạn nhân, viết báo cáo chi tiết gửi UIA, Hội KTS Việt Nam, và cả Bộ Xây dựng.

Scandal nổ tung trên Dezeen, ArchDaily, và Archinect. "Vietnamese architecture firm ran cross-border design theft ring" — headline khắp thế giới."""),

("Chương 6: Văn Phòng KTS Riêng — Tái Sinh", """Với danh tiếng được phục hồi, Vân mở văn phòng KTS riêng: "VÂN Studio" — chuyên kiến trúc bền vững, lấy cảm hứng từ văn hóa Việt.

Dự án đầu tiên: thiết kế lại bảo tàng lịch sử Việt Nam — phiên bản mới, đẹp hơn, hoàn toàn khác concept bị đánh cắp. Lần này, mái không phải nón lá mà là hình dáng thuyền rồng, kết hợp solar panel.

Bộ Văn hóa chọn thiết kế của Vân. Bảo tàng khởi công — công trình quốc gia đầu tiên thiết kế bởi nữ KTS dưới ba mươi lăm tuổi."""),

("Chương 7: Mẹ Và Ngôi Nhà Lá", """Vân theo nghề kiến trúc vì mẹ. Bà Nguyễn Thị Hoa, nông dân Quảng Nam, sống trong căn nhà lá dột nát. Mỗi mùa mưa, mẹ con Vân phải kê chậu hứng dột, ngủ co ro trong góc khô duy nhất.

"Mẹ ơi, lớn lên con sẽ xây cho mẹ ngôi nhà đẹp nhất, không dột nữa," Vân nói khi mười tuổi.

Giờ Vân đã thiết kế bảo tàng quốc gia, resort năm sao, tòa nhà văn phòng. Nhưng công trình đầu tiên cô tự tay thiết kế và xây: ngôi nhà nhỏ cho mẹ ở Quảng Nam — hai tầng, mái ngói đỏ, sân trước trồng hoa giấy.

Ngày khánh thành nhà mới, mẹ Vân đứng trước cửa, sờ tay lên tường gạch, mắt ướt: "Nhà đẹp quá con ơi. Mưa không dột nữa rồi." """),

("Chương 8: Hùng Bị Cấm Hành Nghề — Climax", """UIA ra phán quyết cuối cùng: Lê Trọng Hùng bị cấm hành nghề KTS trên toàn thế giới — lệnh cấm áp dụng tại tất cả quốc gia thành viên UIA, một trăm năm mươi quốc gia.

Hùng Phát Architecture bị rút giấy phép. Năm KTS bị bán thiết kế được bồi thường tổng một triệu đô từ tài sản Hùng bị kê biên.

Hùng đứng trước cổng văn phòng bị niêm phong, mặt tái xanh. Từ giám đốc văn phòng KTS ba trăm nhân viên, giờ không được cầm bút vẽ ở bất kỳ quốc gia nào.

Vân không dự phiên xét xử. Cô đang ở Quảng Nam, cùng mẹ trồng hoa giấy trước sân nhà mới."""),

("Chương 9: Venice Architecture Biennale", """VÂN Studio được mời tham gia Venice Architecture Biennale — triển lãm kiến trúc lớn nhất thế giới. Gian trưng bày: mô hình bảo tàng lịch sử Việt Nam mới, kèm timeline từ bản vẽ bị cướp đến công trình tái sinh.

Người xem đứng trước timeline, đọc câu chuyện, và hiểu: mỗi nét vẽ trên bản vẽ này đều mang theo nước mắt, sự phản bội, và lòng kiên trì.

The Guardian: "Nguyễn Thanh Vân — The architect who rebuilt her career from stolen blueprints."

Vân đứng trước gian trưng bày, nhìn mô hình bảo tàng — công trình mà cô suýt mất, giờ đẹp hơn bao giờ hết."""),

("Chương 10: Đi Qua Bảo Tàng", """Hai năm sau, bảo tàng lịch sử Việt Nam hoàn thành. Vân đứng trước công trình lúc hoàng hôn — mái hình thuyền rồng phản chiếu ánh nắng cuối ngày, solar panel lấp lánh như vảy rồng.

Mẹ Vân từ Quảng Nam ra Hà Nội, lần đầu thấy bảo tàng con gái thiết kế. Bà đứng ngây nhìn, tay ôm ngực: "Con ơi, cái nhà này to quá! To hơn cả đình làng mình!"

Vân cười, nắm tay mẹ dẫn vào bên trong. Trong sảnh chính, một tấm biển đồng ghi: "Thiết kế: KTS Nguyễn Thanh Vân — VÂN Studio."

Mẹ sờ tay lên tấm biển, đọc tên con gái, mắt ướt — giống hệt ngày sờ tường nhà mới ở Quảng Nam.

"Con vẽ nhà cho mẹ, rồi vẽ nhà cho cả nước," bà nói, giọng run run tự hào.

Vân ôm mẹ, đứng giữa bảo tàng mình thiết kế, trong ánh hoàng hôn Hà Nội."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 3: DEV BỊ COPY SOURCE CODE
# ═══════════════════════════════════════════════════════════════════════════════

S3_TITLE = "BỊ COPY TOÀN BỘ SOURCE CODE ỨNG DỤNG 10 TRIỆU USER, TÔI VIẾT LẠI TỪ ĐẦU KHIẾN BẢN COPY THÀNH ĐỒ RÁC"
S3_AUTHOR = "Trần Đình Khải"
S3_COVER = "base_cover_6.png"
S3_INTRO = """<p><strong>"Bốn năm tôi code không nghỉ, xây dựng EduViet — ứng dụng học tiếng Anh miễn phí cho mười triệu học sinh Việt Nam. Đổi lại, CEO cướp toàn bộ source code, fork thành app trả phí, và sa thải tôi ngay trước vòng gọi vốn Series B."</strong></p>
<p>Trần Đình Khải, CTO và developer duy nhất viết core engine của EduViet, bị CEO Phạm Tuấn Kiệt cướp source code, fork thành app trả phí EduPro, và đuổi Khải ngay trước khi gọi vốn năm triệu đô.</p>
<p>Mất code, mất app, mất mười triệu user — Khải viết lại từ đầu, lần này hay hơn, nhanh hơn, và hoàn toàn miễn phí mãi mãi.</p>"""

S3_CHAPTERS = [
("Chương 1: Git Push Cuối Cùng", """Trần Đình Khải commit code cuối cùng vào nửa đêm — pull request #4,271 — fix bug voice recognition cho phát âm tiếng Anh giọng miền Trung. Bốn năm, bốn nghìn hai trăm bảy mươi mốt pull requests, một mình code toàn bộ core engine của EduViet.

EduViet — ứng dụng học tiếng Anh miễn phí cho học sinh Việt Nam — mười triệu user, rating 4.8 trên App Store, top 1 Education category Việt Nam. Core engine: AI speech recognition tùy chỉnh cho tiếng Việt, adaptive learning algorithm, và gamification system.

Sáng hôm sau, Khải đến văn phòng thì bảo vệ chặn cửa: "Anh Khải, anh không được vào. Lệnh CEO."

Phạm Tuấn Kiệt — CEO, đồng sáng lập — gọi Khải ra quán cà phê đối diện.

"Khải, công ty đang restructure trước vòng Series B. Vị trí CTO sẽ được thay thế bởi người có kinh nghiệm quản lý hơn. Cảm ơn sự đóng góp của cậu."

"Cậu đuổi tao? Tao viết toàn bộ code!"

"Code thuộc về công ty. Hợp đồng lao động điều khoản 7.3 — mọi sản phẩm trí tuệ tạo ra trong thời gian làm việc thuộc sở hữu công ty."

Kiệt đẩy qua bàn một tờ giấy: "Thỏa thuận không cạnh tranh. Ký đi, cậu nhận một trăm triệu tiền bồi thường."

Khải đọc thỏa thuận: cấm phát triển ứng dụng giáo dục trong ba năm. Nếu vi phạm, bồi thường năm tỷ.

"Mày điên rồi Kiệt." Khải xé tờ giấy làm đôi, đứng dậy bỏ đi.

Ba ngày sau, Kiệt launch "EduPro" — bản fork từ EduViet, tính phí 199k/tháng. Mười triệu user nhận thông báo: "EduViet miễn phí sẽ ngừng hoạt động. Nâng cấp EduPro để tiếp tục học." """),

("Chương 2: Rewrite From Scratch", """Khải về nhà, mở laptop cá nhân. Không có source code EduViet — tất cả trên server công ty. Nhưng anh có thứ quan trọng hơn: kiến thức. Bốn năm viết mọi dòng code, anh nhớ từng algorithm, từng architecture decision, từng bug và cách fix.

Anh bắt đầu viết lại từ dòng đầu tiên: "LearnFree" — ứng dụng học tiếng Anh mới, miễn phí vĩnh viễn, open source. Lần này, license MIT — ai cũng có thể dùng, không ai có thể cướp.

Hai tháng code không ngủ. Stack mới: Flutter thay React Native (nhanh hơn), Rust thay Python cho AI engine (hiệu suất gấp mười), và một speech recognition model mới train trên hai mươi nghìn giờ audio tiếng Việt giọng vùng miền.

LearnFree launch trên GitHub: một trăm nghìn stars trong tuần đầu. Product Hunt #1 Product of the Day. Mười triệu user cũ của EduViet chuyển sang LearnFree — vì nó miễn phí, nhanh hơn, và hay hơn."""),

("Chương 3: EduPro Sụp Đổ", """EduPro mất tám triệu user trong một tháng — vì ai trả 199k/tháng khi có LearnFree miễn phí và tốt hơn? Rating EduPro rớt từ 4.8 xuống 2.1 — review tràn ngập: "App cũ tính phí, dùng LearnFree miễn phí tốt hơn nhiều."

Kiệt hoảng loạn. Vòng gọi vốn Series B — năm triệu đô từ quỹ Sequoia — bị hủy vì user base sụt giảm. Investor rút vì "core product không có competitive advantage khi open source alternative tốt hơn."

EduViet Inc. cạn vốn trong sáu tháng."""),

("Chương 4: Kiệt Phản Công Bằng Kiện Tụng", """Kiệt thuê luật sư kiện Khải: "vi phạm thỏa thuận không cạnh tranh" và "sử dụng bí mật thương mại."

Khải phản bác: "Tôi không ký thỏa thuận không cạnh tranh — tôi xé nó trước mặt Kiệt. Và LearnFree viết lại hoàn toàn từ đầu — stack khác, language khác, architecture khác. Mời so sánh code."

Tòa thuê chuyên gia phân tích code. Kết quả: LearnFree và EduViet có zero code overlap — không một dòng code trùng. Architecture hoàn toàn khác. "Đây là hai sản phẩm độc lập," chuyên gia kết luận.

Tòa bác đơn kiện. Kiệt mất thêm tiền luật sư."""),

("Chương 5: Bí Mật: Kiệt Đã Bán Data User", """Trong quá trình kiện tụng, luật sư Khải phát hiện: EduPro không chỉ tính phí user — Kiệt còn bán data cá nhân của mười triệu học sinh cho công ty quảng cáo. Tên, tuổi, trường, lịch sử học — data trẻ em bị bán cho bên thứ ba.

Vi phạm Luật An ninh mạng Điều 17 và Luật Bảo vệ trẻ em. Khải gửi bằng chứng cho Bộ Thông tin và Truyền thông.

Scandal nổ. Báo chí đưa tin: "CEO EduPro bán data mười triệu học sinh Việt Nam." Phụ huynh giận dữ. App Store gỡ EduPro."""),

("Chương 6: LearnFree — Open Source Toàn Cầu", """LearnFree mở rộng: phiên bản tiếng Thái, tiếng Indonesia, tiếng Philippines. Cộng đồng open source đóng góp — ba trăm developer từ hai mươi quốc gia cùng phát triển.

Google.org tài trợ hai triệu đô cho LearnFree Foundation — tổ chức phi lợi nhuận vận hành app. UNESCO công nhận LearnFree là "Best Practice in Digital Education" tại Đông Nam Á.

Ba mươi triệu user trên bốn quốc gia — tất cả miễn phí."""),

("Chương 7: Mẹ Và Cuốn Từ Điển Cũ", """Khải code vì mẹ. Bà Trần Thị Mai, công nhân may ở Bình Dương, mơ ước con trai nói tiếng Anh. Bà mua cho Khải cuốn từ điển Oxford bìa cứng — ba tháng lương — khi Khải mười tuổi.

"Con ơi, mẹ không biết tiếng Anh, nhưng mẹ biết: biết tiếng Anh thì thoát nghèo."

Cuốn từ điển đó — bìa sờn, gáy gãy — giờ nằm trên bàn code của Khải. Mỗi khi debug mệt, anh lật vài trang, đọc vài từ, nhớ mẹ.

"Mẹ mua từ điển cho con bằng ba tháng lương. Con làm app miễn phí cho ba mươi triệu đứa trẻ. Đó là lãi suất tốt nhất con biết." """),

("Chương 8: Kiệt Lĩnh Án — Climax", """Tòa tuyên: Phạm Tuấn Kiệt ba năm tù giam về tội "xâm phạm dữ liệu cá nhân trẻ em" và "lừa đảo chiếm đoạt tài sản." EduViet Inc. phá sản.

Nhưng climax thật không phải bản án. Mà là khoảnh khắc trước tòa, khi Kiệt nhìn Khải lần cuối.

"Khải, mày có thể tha thứ cho tao không?"

Khải im lặng mười giây. "Tao không tha thứ. Nhưng tao cũng không thù. Tao chỉ muốn mười triệu đứa trẻ được học miễn phí. Đó là lý do tao code. Còn mày — mày chọn tiền. Đó là lý do mày ở đây."

Kiệt cúi đầu. Công an dẫn gã đi."""),

("Chương 9: GitHub Stars Và Lớp Học Vùng Cao", """LearnFree đạt năm trăm nghìn stars trên GitHub — top 50 repo nhiều stars nhất thế giới. Nhưng con số Khải tự hào nhất: ba mươi nghìn em nhỏ vùng cao dùng LearnFree offline — phiên bản không cần internet, chạy trên điện thoại cũ.

Khải đến thăm một lớp học vùng cao ở Sapa. Cô giáo bản cho học sinh dùng LearnFree trên chiếc tablet cũ — các em lặp theo giọng AI: "Hello, my name is..."

Một em gái mười tuổi, má đỏ vì lạnh, chạy đến: "Anh ơi, em nói tiếng Anh được rồi! Hello! Thank you! I love Vietnam!"

Khải cười, mắt cay. Năm trăm nghìn stars không bằng câu "Hello" của em bé Sapa."""),

("Chương 10: Commit Tiếp Theo", """Khải ngồi ở nhà, laptop mở, terminal chạy. Pull request #8,547 — thêm giọng đọc tiếng Anh giọng Huế cho LearnFree.

Mẹ gọi video call: "Con ơi, mấy đứa con bạn mẹ ở xưởng may đều dùng app của con. Tụi nó nói tiếng Anh hay lắm!"

"Dạ mẹ, con vui."

Khải commit code, push lên GitHub. Commit message: "Add Hue dialect voice model. For Mom."

Ngoài cửa sổ, Sài Gòn về đêm. Trên GitHub, ba trăm developer khắp thế giới đang đồng thời code cho LearnFree. Mỗi pull request là một viên gạch, mỗi viên gạch là một đứa trẻ được học.

Khải mở terminal, bắt đầu dòng code tiếp theo."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 4: BS DA LIỄU BỊ CƯỚP CÔNG THỨC MỸ PHẨM
# ═══════════════════════════════════════════════════════════════════════════════

S4_TITLE = "BỊ CƯỚP CÔNG THỨC SERUM TÁI TẠO DA, TÔI LẬP THƯƠNG HIỆU MỸ PHẨM SẠCH KHIẾN KẺ TRỘM PHẢI THU HỒI SẢN PHẨM"
S4_AUTHOR = "Mai Phương Linh"
S4_COVER = "base_cover_7.png"
S4_INTRO = """<p><strong>"Năm năm tôi nghiên cứu, bào chế thành công serum tái tạo da từ chiết xuất sen Việt Nam — hiệu quả hơn retinol nhưng không gây kích ứng. Đổi lại, đồng nghiệp cướp công thức, pha loãng thêm hóa chất rẻ tiền, và bán với giá gấp mười."</strong></p>
<p>BS Mai Phương Linh, chuyên gia da liễu nghiên cứu dược mỹ phẩm, bị TS Hoàng Minh Đức — đồng nghiệp cùng khoa — cướp công thức serum sen và bán cho tập đoàn mỹ phẩm GlowMax với giá hai tỷ.</p>
<p>Mất công thức, bị vu oan "nghiên cứu sai quy trình," Linh tự lập thương hiệu dược mỹ phẩm sạch, chứng minh công thức gốc, và buộc GlowMax phải thu hồi sản phẩm giả mạo trên toàn quốc.</p>"""

S4_CHAPTERS = [
("Chương 1: Công Thức Sen Bị Đánh Cắp", """Phòng lab da liễu, Bệnh viện Da liễu Trung ương, mười giờ đêm. BS Mai Phương Linh vừa hoàn thành thử nghiệm cuối cùng cho LotuSera — serum tái tạo da từ chiết xuất flavonoid của sen Việt Nam.

Năm năm nghiên cứu. Ba trăm bốn mươi mẫu thử nghiệm. Kết quả: LotuSera kích thích tái tạo collagen hiệu quả hơn retinol 0.5% ba mươi phần trăm, nhưng không gây kích ứng — vì chiết xuất sen có khả năng chống viêm tự nhiên.

Linh lưu kết quả vào server lab, ghi chép vào sổ nghiên cứu, rồi về nhà ngủ — giấc ngủ đầu tiên sau ba mươi sáu giờ thức.

Sáng hôm sau, cô nhận tin nhắn từ bạn đồng nghiệp: "Linh ơi, mày xem Shopee đi. GlowMax vừa launch serum sen 'LotusGlow' — nghe giống công thức của mày quá!"

Linh mở Shopee, tim đập thình thịch. LotusGlow — serum sen tái tạo da — thành phần ghi trên bao bì: "Chiết xuất flavonoid sen Tây Hồ, nồng độ 3.5%." Đúng nồng độ mà Linh tối ưu sau năm năm.

Cô gọi TS Hoàng Minh Đức — đồng nghiệp cùng lab, người duy nhất có quyền truy cập vào server lab ngoài Linh.

"Anh Đức, anh giải thích đi. GlowMax dùng đúng công thức của em!"

Đức im lặng hai giây, rồi cười: "Linh, cô paranoid rồi. Chiết xuất sen thì ai nghiên cứu cũng ra kết quả tương tự."

"3.5% nồng độ flavonoid? Chính xác tỷ lệ em tối ưu sau ba trăm bốn mươi thử nghiệm? Anh nghĩ em ngu?"

Một tuần sau, Linh bị triệu tập lên phòng Giám đốc bệnh viện: "BS Linh, chúng tôi nhận được báo cáo rằng chị sử dụng thiết bị lab cho mục đích cá nhân, vi phạm quy trình nghiên cứu." Người báo cáo: TS Hoàng Minh Đức.

Linh bị đình chỉ công tác ba tháng."""),

("Chương 2: Lab Trong Phòng Ngủ", """Bị đình chỉ, Linh biến phòng ngủ thành mini lab — máy khuấy từ cũ mua trên Shopee, bình thủy tinh, cân tiểu ly, và chiết xuất sen mua trực tiếp từ nông dân trồng sen Tây Hồ.

Cô bào chế lại LotuSera phiên bản 2.0 — cải tiến hơn: thêm niacinamide từ gạo lứt và hyaluronic acid thực vật. Hiệu quả tái tạo da tốt hơn v1.0 bốn mươi phần trăm.

Đồng thời, cô gửi mẫu LotusGlow của GlowMax đi xét nghiệm tại phòng thí nghiệm độc lập. Kết quả sốc: LotusGlow chứa chỉ 0.8% chiết xuất sen (thay vì 3.5% ghi trên bao bì) — phần còn lại là paraben rẻ tiền và silicon. Sản phẩm giả mạo.

Không chỉ cướp công thức — Đức còn pha loãng để giảm giá thành, rồi ghi sai nồng độ trên bao bì."""),

("Chương 3: Thương Hiệu LinhSen Ra Đời", """Linh thành lập "LinhSen Cosmetics" — thương hiệu dược mỹ phẩm sạch, sản xuất tại nhà, bán online. Mỗi sản phẩm kèm giấy xét nghiệm nồng độ thành phần từ lab độc lập — "Transparent Beauty."

LotuSera v2.0 bán trên Shopee: giá 350k/chai — rẻ hơn LotusGlow (890k) hơn phân nửa, nhưng chất lượng cao hơn gấp nhiều lần.

Khách hàng đầu tiên review: "Dùng LotusGlow không thấy gì. Chuyển sang LotuSera, da mềm mịn sau hai tuần. Và giấy xét nghiệm minh bạch quá!"

Ba tháng, mười nghìn chai bán hết. Rating 4.9, năm nghìn review tích cực."""),

("Chương 4: GlowMax Phản Công", """GlowMax — tập đoàn mỹ phẩm doanh thu nghìn tỷ — thuê luật sư kiện LinhSen: "sử dụng thương hiệu gây nhầm lẫn" và "cạnh tranh không lành mạnh."

Đồng thời, gã Đức lên mạng tố Linh "ăn cắp nghiên cứu của bệnh viện" và "bán mỹ phẩm không phép."

Linh đáp trả bằng bằng chứng: sổ lab ghi chép cá nhân có ngày tháng, email nội bộ lab gửi kết quả cho Đức (Đức forward cho GlowMax), và kết quả xét nghiệm chứng minh LotusGlow ghi sai nồng độ.

"GlowMax bán sản phẩm ghi 3.5% chiết xuất sen, thực tế chỉ 0.8%. Ai mới là kẻ lừa đảo?" Linh đăng trên Facebook kèm giấy xét nghiệm."""),

("Chương 5: Phát Hiện Dị Ứng Hàng Loạt", """Twist: ba mươi hai khách hàng sử dụng LotusGlow bị dị ứng da — mẩn đỏ, ngứa, viêm tiếp xúc. Nguyên nhân: paraben nồng độ cao trong công thức pha loãng của Đức.

Cục Quản lý Dược vào cuộc. Xét nghiệm LotusGlow xác nhận: nồng độ thành phần sai sự thật, chứa chất bảo quản vượt ngưỡng cho phép.

GlowMax bị buộc thu hồi toàn bộ LotusGlow trên thị trường — năm mươi nghìn chai."""),

("Chương 6: LinhSen Bùng Nổ", """Sau scandal GlowMax, khách hàng đổ xô sang LinhSen. Doanh thu tăng hai mươi lần trong một tháng. Linh thuê nhà máy sản xuất đạt chuẩn GMP, mở rộng danh mục: serum, kem dưỡng, toner — tất cả từ chiết xuất thực vật Việt Nam.

Quỹ đầu tư Wavemaker Partners rót ba triệu đô Series A. LinhSen trở thành thương hiệu dược mỹ phẩm tăng trưởng nhanh nhất Việt Nam."""),

("Chương 7: Bà Nội Và Hoa Sen Tây Hồ", """Linh yêu sen vì bà nội. Bà Mai Thị Hương, bán hoa sen ở Hồ Tây bốn mươi năm. Mỗi sáng tinh mơ, bà chèo thuyền hái sen, mang ra chợ bán.

"Bà ơi, sao sen đẹp thế mà rẻ vậy?"

"Vì sen mọc trong bùn mà, cháu ơi. Đẹp nhất mà rẻ nhất."

Linh thề: "Cháu sẽ làm cho sen Việt Nam có giá." Và cô đã làm — LotuSera biến chiết xuất sen thành thành phần dược mỹ phẩm giá trị hàng triệu đô.

Logo LinhSen là hình hoa sen Tây Hồ — vẽ theo bức tranh bà nội tặng Linh ngày tốt nghiệp y khoa."""),

("Chương 8: Đức Bị Tước Bằng — Climax", """Bộ Y tế và Cục Quản lý Dược điều tra: TS Hoàng Minh Đức bị tước giấy phép hành nghề vì "bán trái phép kết quả nghiên cứu y khoa" và "gian lận nồng độ thành phần dược phẩm."

GlowMax bị phạt năm tỷ đồng, CEO bị cấm hoạt động trong lĩnh vực mỹ phẩm.

Tại phiên xử, Đức nhìn Linh — cô ngồi hàng ghế bên kia, bình thản như ngày nào trong lab.

"Linh, tao chỉ muốn kiếm tiền. Tao không nghĩ công thức sen đáng giá nhiều đến thế."

"Nó không đáng giá vì tiền, anh Đức. Nó đáng giá vì năm năm tôi nghiên cứu để người phụ nữ Việt Nam có làn da khỏe mà không cần hóa chất độc hại." """),

("Chương 9: Hội Nghị Dermatology Quốc Tế", """Linh được mời thuyết trình tại World Congress of Dermatology — hội nghị da liễu lớn nhất thế giới — về "Plant-based Skincare: The Lotus Revolution."

"Sen mọc trong bùn. Tôi cũng vậy — bị phản bội, bị đình chỉ, bị kiện. Nhưng giống sen, tôi mọc lên sạch hơn," Linh nói trước hai nghìn bác sĩ da liễu.

Standing ovation. Ba công ty dược Nhật Bản và Hàn Quốc ký hợp đồng license chiết xuất sen LotuSera."""),

("Chương 10: Quay Về Hồ Tây", """Linh đưa bà nội ra Hồ Tây một sáng sớm mùa hè. Sen nở rực cả mặt hồ — hồng, trắng, phớt tím — giống hệt những sáng bà chèo thuyền hái sen bốn mươi năm trước.

"Bà ơi, con làm mỹ phẩm từ sen rồi. Sen Tây Hồ giờ bán sang Nhật, Hàn Quốc."

Bà Hương cười, tay sờ cánh sen mỏng manh: "Sen nhà mình tốt lắm, cháu ơi. Bà biết mà."

Linh ôm bà, ngửi mùi sen trên tóc bà — mùi tuổi thơ, mùi lab, mùi thành công.

"Sen mọc trong bùn mà vẫn đẹp," bà nói.

"Dạ, bà. Giống con." """),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 5: NHÀ VĂN BỊ ĐẠO VĂN
# ═══════════════════════════════════════════════════════════════════════════════

S5_TITLE = "BỊ ĐẠO TOÀN BỘ TIỂU THUYẾT BESTSELLER, TÔI VIẾT PHẦN TIẾP THEO KHIẾN BẢN ĐẠO TRỞ THÀNH TRÒ CƯỜI"
S5_AUTHOR = "Đỗ Hoàng Anh"
S5_COVER = "base_cover_8.png"
S5_INTRO = """<p><strong>"Ba năm tôi viết 'Mùa Hè Cuối' — tiểu thuyết về tuổi trẻ Việt Nam thời đổi mới. Gửi cho NXB, biên tập viên bảo 'không đủ thương mại.' Sáu tháng sau, sách ra dưới tên người khác, bán ba trăm nghìn bản."</strong></p>
<p>Đỗ Hoàng Anh, nhà văn trẻ tài năng, gửi bản thảo "Mùa Hè Cuối" cho NXB Ánh Sáng. Biên tập viên Trương Quốc Hải từ chối xuất bản, nhưng lén gửi bản thảo cho nhà văn "thương mại" Lâm Đình Phúc — người xuất bản dưới tên mình, thành bestseller quốc gia.</p>
<p>Bị cướp tác phẩm đời mình, Anh chứng minh mình là tác giả gốc và viết phần tiếp theo khiến bản đạo trở nên vô nghĩa.</p>"""

S5_CHAPTERS = [
("Chương 1: Bestseller Của Người Khác", """Đỗ Hoàng Anh đứng trong hiệu sách Fahasa Nguyễn Huệ, tay run. Trên kệ bestseller, cuốn "Mùa Hè Cuối" — bìa đỏ, chữ vàng — nằm ở vị trí số một. Tác giả ghi trên bìa: Lâm Đình Phúc.

Ba trăm nghìn bản. Đứng đầu bảng xếp hạng Tiki mười hai tuần liên tiếp. Bản quyền phim đã bán cho CJ Entertainment. Review năm sao tràn ngập: "Tác phẩm vĩ đại nhất văn học Việt đương đại."

Anh cầm cuốn sách lên, mở trang đầu. Dòng đầu tiên: "Mùa hè năm 1986, khi bố tôi đem về nhà chiếc radio Sanyo cũ, cả xóm Bảy kéo đến nghe." Đúng từng chữ, từng dấu phẩy, từng nhịp thở — của Anh.

Anh đã viết câu đó ba năm trước, trong căn phòng trọ mười hai mét vuông ở quận 4, trên chiếc laptop Dell cũ, lúc ba giờ sáng. Anh nhớ vì lúc đó ngoài cửa sổ có con mèo hoang kêu, và Anh dừng lại nghe, rồi viết tiếp.

Sáu tháng trước, Anh gửi bản thảo cho NXB Ánh Sáng qua email. Biên tập viên Trương Quốc Hải đọc, rồi trả lời: "Bản thảo hay, nhưng giọng văn quá 'thuần văn học,' khó bán thương mại. Xin từ chối."

Anh buồn nhưng chấp nhận. Anh không biết: Hải đã forward bản thảo cho Lâm Đình Phúc — nhà văn "thương mại" mà Hải làm biên tập. Phúc sửa vài chi tiết phụ, thêm một tuyến tình cảm lãng mạn, rồi xuất bản.

Anh đứng trong hiệu sách, ôm cuốn "Mùa Hè Cuối" — tác phẩm đời mình, mang tên người khác."""),

("Chương 2: Bằng Chứng Trong Email", """Anh không biết luật. Nhưng anh biết email. Bản thảo gốc gửi cho NXB Ánh Sáng có timestamp email: ngày 15 tháng 3, hai năm trước. File Word đính kèm có metadata: author "Đỗ Hoàng Anh," created date trùng khớp.

Phiên bản của Phúc xuất bản ngày 1 tháng 10 — bảy tháng sau email của Anh.

Nhưng Anh cần thêm bằng chứng. Anh mở laptop cũ: lịch sử file trên Google Drive, hai mươi phiên bản chỉnh sửa từ bản thảo đầu đến bản final, mỗi phiên bản có timestamp tự động. Ba năm revision history — không thể giả mạo.

Anh viết thread Facebook dài, đăng toàn bộ bằng chứng: email, metadata, revision history, và so sánh song song giữa bản gốc và bản "Phúc." Thread đạt mười triệu lượt đọc trong hai ngày."""),

("Chương 3: Cộng Đồng Văn Học Dậy Sóng", """Giới văn học Việt Nam chia đôi. Phe ủng hộ Anh: các nhà văn trẻ, nhà phê bình độc lập. Phe ủng hộ Phúc: NXB Ánh Sáng và hệ thống xuất bản truyền thống.

Phúc họp báo, phủ nhận: "Tôi viết 'Mùa Hè Cuối' từ trải nghiệm cá nhân. Sự trùng hợp trong văn học là bình thường."

Nhưng anh ta phạm sai lầm: khi phóng viên hỏi chi tiết về quá trình viết, Phúc không nhớ nổi tên nhân vật phụ, không biết xóm Bảy nằm ở quận nào Sài Gòn, và lúng túng khi được hỏi về bối cảnh lịch sử đổi mới 1986.

Anh — tác giả thật — trả lời mọi câu hỏi chi tiết: tên từng nhân vật, lý do đặt tên, bối cảnh lịch sử chính xác, và cả tiếng mèo kêu lúc ba giờ sáng khi viết dòng đầu tiên."""),

("Chương 4: NXB Phản Công", """NXB Ánh Sáng thuê luật sư, tuyên bố: "Bản thảo gửi cho NXB nhưng bị từ chối — quyền sở hữu không tự động thuộc về tác giả nếu NXB đã xử lý và phát triển thêm."

Hải — biên tập viên — lên báo phủ nhận đã forward email: "Tôi chỉ từ chối bản thảo, không gửi cho ai."

Nhưng anh ta quên: email server của NXB lưu log forwarding. Luật sư Anh yêu cầu tòa trát đòi log server. NXB từ chối. Tòa ra lệnh cưỡng chế.

Log server hiện rõ: ngày 20 tháng 3 — năm ngày sau khi Anh gửi bản thảo — Hải forward email kèm file Word cho Phúc."""),

("Chương 5: Bí Mật: Hải Nhận Hoa Hồng 30%", """Twist: log server còn cho thấy nhiều hơn — Hải không chỉ forward một bản thảo. Trong hai năm, gã đã forward hơn hai mươi bản thảo bị từ chối cho Phúc. Phúc chọn lọc, sửa, xuất bản dưới tên mình. Hải nhận hoa hồng ba mươi phần trăm doanh thu.

"Mùa Hè Cuối" không phải lần đầu. Phúc đã "viết" mười hai cuốn sách — tất cả đều từ bản thảo ăn cắp. "Nhà văn bestseller" thực chất là kẻ đạo văn chuyên nghiệp.

Scandal chấn động ngành xuất bản Việt Nam."""),

("Chương 6: Viết Phần Tiếp Theo", """Trong khi vụ kiện diễn ra, Anh không ngồi chờ. Anh viết "Mùa Thu Tiếp Theo" — phần hai của "Mùa Hè Cuối." Phần hai kết nối trực tiếp, tiết lộ bí mật mà phần một chỉ gợi mở — bí mật mà chỉ tác giả thật mới biết, vì nó nằm trong outline ban đầu.

"Mùa Thu Tiếp Theo" xuất bản — tự xuất bản qua Amazon KDP — và bán một trăm nghìn bản trong tuần đầu. Độc giả đọc xong phần hai, quay lại đọc phần một, và nhận ra: phần một dưới tên Phúc thiếu chiều sâu, thiếu foreshadowing — vì Phúc không biết outline phần hai.

"Mùa Hè Cuối" của Phúc trở thành trò cười — cuốn sách nửa vời, không có kết."""),

("Chương 7: Ông Ngoại Và Chiếc Radio Sanyo", """Dòng đầu tiên "Mùa Hè Cuối" — "bố tôi đem về chiếc radio Sanyo cũ" — là ký ức thật của Anh.

Ông ngoại Anh — Đỗ Văn Bình, công nhân nhà máy dệt Phong Phú — mang chiếc radio Sanyo cũ về nhà năm 1986. Cả xóm kéo đến nghe đài VOV. Anh lúc đó ba tuổi, ngồi trên đùi ông, nghe tiếng phát thanh viên đọc tin đổi mới.

"Con ơi, đất nước thay đổi rồi," ông nói.

Câu đó Anh nhớ mãi. Và nó trở thành linh hồn của "Mùa Hè Cuối" — câu chuyện về thế hệ đổi mới, về hy vọng, về tuổi trẻ Việt Nam tin vào tương lai.

Chiếc radio Sanyo giờ nằm trên bàn viết của Anh — không còn chạy, nhưng vẫn giữ tiếng nói của ông."""),

("Chương 8: Phúc Và Hải Lĩnh Án — Climax", """Tòa tuyên: Lâm Đình Phúc ba năm tù về tội "xâm phạm quyền tác giả có tổ chức." Trương Quốc Hải hai năm tù treo và cấm hành nghề xuất bản. NXB Ánh Sáng bồi thường Anh và hai mươi tác giả bị đạo văn tổng năm tỷ đồng.

Ba trăm nghìn bản "Mùa Hè Cuối" dưới tên Phúc bị thu hồi và in lại — lần này đúng tên: Đỗ Hoàng Anh.

Anh cầm bản in mới, sờ lên tên mình trên bìa sách. Ba năm viết, hai năm đấu tranh — giờ tên anh mới được đứng đúng chỗ."""),

("Chương 9: Hội Sách Quốc Tế Frankfurt", """Anh được mời tham gia Hội sách Quốc tế Frankfurt — hội sách lớn nhất thế giới — với "Mùa Thu Tiếp Theo." Bản quyền dịch bán cho mười hai quốc gia.

"Tôi bị cướp cuốn sách đầu tiên. Nhưng không ai cướp được câu chuyện trong đầu tôi," Anh phát biểu trước đám đông nhà xuất bản quốc tế.

The New York Times Book Review: "Đỗ Hoàng Anh writes with the authority of someone who has lived every sentence twice — once in creation, once in theft." """),

("Chương 10: Quay Về Phòng Trọ Quận 4", """Anh quay về thăm phòng trọ cũ ở quận 4 — mười hai mét vuông, bàn gỗ cũ, cửa sổ nhìn ra con hẻm. Phòng giờ có người khác thuê, nhưng chủ nhà cho Anh vào xem lại.

Anh đứng ở cửa sổ — đúng vị trí ngày xưa ngồi viết. Ngoài cửa sổ, con hẻm vẫn vậy. Con mèo hoang vẫn kêu lúc ba giờ sáng.

"Mùa hè năm 1986, khi bố tôi đem về nhà chiếc radio Sanyo cũ..."

Anh lẩm bẩm dòng đầu tiên, mỉm cười.

Rồi anh mở laptop, bắt đầu viết cuốn sách thứ ba. Dòng đầu tiên: "Mùa đông năm 2024, khi tôi mất cuốn sách đầu tiên, tôi nghĩ mình sẽ không bao giờ viết lại. Nhưng con mèo ngoài cửa sổ vẫn kêu, và tay tôi vẫn gõ phím."

Câu chuyện mới. Bắt đầu lại. Như mọi khi."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# ASSEMBLY & PUBLISHING
# ═══════════════════════════════════════════════════════════════════════════════

ALL_STORIES = [
    {"title": S1_TITLE, "author": S1_AUTHOR, "cover": S1_COVER, "intro": S1_INTRO, "chapters": S1_CHAPTERS},
    {"title": S2_TITLE, "author": S2_AUTHOR, "cover": S2_COVER, "intro": S2_INTRO, "chapters": S2_CHAPTERS},
    {"title": S3_TITLE, "author": S3_AUTHOR, "cover": S3_COVER, "intro": S3_INTRO, "chapters": S3_CHAPTERS},
    {"title": S4_TITLE, "author": S4_AUTHOR, "cover": S4_COVER, "intro": S4_INTRO, "chapters": S4_CHAPTERS},
    {"title": S5_TITLE, "author": S5_AUTHOR, "cover": S5_COVER, "intro": S5_INTRO, "chapters": S5_CHAPTERS},
]

def build_all():
    novels = []
    for s in ALL_STORIES:
        chapters = []
        total = 0
        for title, raw in s["chapters"]:
            html = fmt(raw)
            c = html.count("<p>")
            total += c
            chapters.append({"title": title, "content": html})
        novels.append({
            "title": s["title"], "author": s["author"], "genre": "Sảng Văn",
            "intro": s["intro"], "chapters": chapters, "cover_base": s["cover"],
            "_stats": f"{len(chapters)} chapters, {total} sentences"
        })
        log(f"✓ {s['title'][:55]}... — {total} sentences")
    return novels

def get_ftp():
    for i in range(5):
        try:
            ftp = ftplib.FTP(FTP_HOST, timeout=60)
            ftp.login(FTP_USER, FTP_PASS)
            return ftp
        except Exception as e:
            log(f"FTP retry {i+1}: {e}")
            time.sleep(5*(i+1))
    raise Exception("FTP failed")

def publish_all(novels):
    log("🚀 MIX BATCH 1 — 5 STORIES (Sảng Văn Cải Tiến)")
    ftp = get_ftp()
    with open(os.path.join(BASE_DIR, "publish_novel.php"), "rb") as f:
        ftp.storbinary("STOR publish_novel.php", f)
    ftp.quit()
    log("✓ Helper uploaded")

    results = []
    for i, n in enumerate(novels):
        log(f"\n{'='*60}\n📖 PUBLISHING {i+1}/5: {n['title'][:55]}...\n{'='*60}")
        cover_file = ""
        base = os.path.join(BASE_DIR, n["cover_base"])
        if os.path.exists(base):
            out = os.path.join(BASE_DIR, "pending_cover.png")
            cmd = ["python3", os.path.join(BASE_DIR, "cover_overlay_standard.py"),
                   "--input", base, "--output", out, "--title", n["title"],
                   "--subtitle", f"Sảng văn của {n['author']}"]
            r = subprocess.run(cmd, capture_output=True, text=True)
            if r.returncode == 0 and os.path.exists(out):
                rid = random.randint(100000,999999)
                cover_file = f"cover_sideload_{rid}.png"
                ftp = get_ftp(); ftp.cwd("wp-content/uploads")
                with open(out,"rb") as cf: ftp.storbinary(f"STOR {cover_file}", cf)
                ftp.quit(); os.remove(out)
                log(f"✓ Cover uploaded: {cover_file}")

        payload = {"secret_token": SECRET_TOKEN, "title": n["title"], "intro": n["intro"],
                   "author": n["author"], "genre": "Sảng Văn", "chapters": n["chapters"]}
        if cover_file: payload["cover_local_filename"] = cover_file

        try:
            res = requests.post(f"{WP_URL}/publish_novel.php", json=payload, timeout=300).json()
            if res.get("success"):
                log(f"🎉 Published! ID={res['story_id']}, chapters={res['chapters_count']}")
                results.append({"id": res["story_id"], "title": n["title"]})
                reg_path = os.path.join(BASE_DIR, "existing_novels.json")
                reg = json.load(open(reg_path,"r",encoding="utf-8")) if os.path.exists(reg_path) else []
                reg.append({"id": res["story_id"], "title": n["title"], "slug": n["title"].lower().replace(" ","-"), "intro": n["intro"]})
                json.dump(reg, open(reg_path,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
            else:
                log(f"❌ API Error: {res}")
        except Exception as e:
            log(f"❌ Exception: {e}")
        time.sleep(5)

    try:
        ftp = get_ftp(); ftp.delete("publish_novel.php"); ftp.quit()
    except: pass

    log(f"\n🏁 MIX BATCH 1 COMPLETE: {len(results)}/5 published")
    for r in results: log(f"  → ID {r['id']}: {r['title'][:60]}")

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--live", action="store_true")
    a = p.parse_args()
    if not a.dry_run and not a.live:
        print("Use --dry-run or --live"); sys.exit(1)
    novels = build_all()
    if a.dry_run:
        print(f"\n{'='*60}\n🔬 DRY-RUN: {len(novels)} stories\n{'='*60}")
        for n in novels:
            print(f"\n📖 {n['title']}")
            print(f"   ✍️ {n['author']} | 📊 {n['_stats']}")
            for ch in n["chapters"]:
                print(f"   → {ch['title']} ({ch['content'].count('<p>')} sentences)")
    elif a.live:
        publish_all(novels)
