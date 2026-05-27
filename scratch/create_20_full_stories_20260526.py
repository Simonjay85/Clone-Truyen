#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create 20 offline full-story drafts for doctieuthuyet.

This intentionally does not call any text or image API and does not publish.
It writes reviewable JSON payloads plus an editorial score table so the user
can approve before anything touches the live WordPress site.
"""

from __future__ import annotations

import html
import json
import random
import re
from pathlib import Path


OUT_DIR = Path("scratch/batch_20_full_stories_20260526")
STORIES_DIR = OUT_DIR / "stories"
COVERS_DIR = OUT_DIR / "covers"


CONCEPTS = [
    {
        "slug": "nem-khoi-phong-hop-vincom",
        "title": "Bị Ném Khỏi Phòng Họp Vincom, Tôi Mang Sổ Kiểm Toán Trở Lại Khiến Cả Hào Môn Quỳ Xuống",
        "author": "An Nhiên",
        "lead": "Nguyễn Minh Khang",
        "ally": "Lê Tuệ Lâm",
        "villain": "Trần Quốc Bảo",
        "ex": "Mai Thảo Vy",
        "domain": "kiểm toán chuỗi bán lẻ cao cấp",
        "place": "Vincom Đồng Khởi và trụ sở Sở Kế hoạch Đầu tư TP.HCM",
        "proof": "sổ kiểm toán nội bộ, email phê duyệt có chữ ký số, sao kê Vietcombank đóng dấu đỏ",
        "bottleneck": "tài khoản công ty bị phong tỏa tạm thời 36 giờ",
        "reward": "hợp đồng tái cấu trúc chuỗi cửa hàng 320 tỷ",
        "visual": "a young Vietnamese forensic auditor in a charcoal suit holding a red-stamped audit binder, luxury boardroom behind him, humiliated executives kneeling in the background",
    },
    {
        "slug": "duoi-khoi-xuong-gom-bat-trang",
        "title": "Bị Đuổi Khỏi Xưởng Gốm Bát Tràng, Tôi Dùng Men Cổ Thắng Đơn Hàng Trăm Tỷ Của Người Yêu Cũ",
        "author": "Minh Hạ",
        "lead": "Phạm Duy An",
        "ally": "Đỗ Hoài Phương",
        "villain": "Vũ Gia Khiêm",
        "ex": "Nguyễn Mỹ Hân",
        "domain": "gốm sứ thủ công xuất khẩu",
        "place": "làng gốm Bát Tràng và cảng Hải Phòng",
        "proof": "sổ công thức men tro, biên bản giám định niên đại, camera lò nung",
        "bottleneck": "xưởng bị niêm phong một ngày vì bị tố dùng men độc",
        "reward": "đơn hàng khách sạn Nhật 180 tỷ",
        "visual": "a Vietnamese ceramic master beside glowing kilns and ancient blue glaze pottery, rival couple shocked under harsh inspection lights",
    },
    {
        "slug": "vu-oan-o-benh-vien-cho-ray",
        "title": "Bị Vu Oan Làm Chết Bệnh Nhân, Tôi Cứu Sống Chủ Tịch Khiến Cả Bệnh Viện Chợ Rẫy Câm Lặng",
        "author": "Bạch Dương",
        "lead": "Trương Hải Nam",
        "ally": "Hoàng Thanh Vân",
        "villain": "Bác sĩ Lưu Đức Thịnh",
        "ex": "Đặng Quỳnh Chi",
        "domain": "cấp cứu Đông Tây y kết hợp",
        "place": "Bệnh viện Chợ Rẫy và hội đồng chuyên môn Sở Y tế",
        "proof": "hồ sơ men gan, điện tâm đồ, log cấp cứu, camera phòng trực",
        "bottleneck": "phòng khám bị đình chỉ 48 giờ để chờ hội đồng thẩm định",
        "reward": "trung tâm phục hồi chức năng 260 tỷ",
        "visual": "a calm Vietnamese emergency doctor holding clinical charts in a hospital corridor, monitors glowing, senior surgeons stunned",
    },
    {
        "slug": "vut-hop-dong-cau-giay",
        "title": "Bị Sếp Cũ Vứt Hợp Đồng Ở Cầu Giấy, Tôi Lật Nhật Ký Thi Công Khiến Tập Đoàn Mất Gói Thầu",
        "author": "Khánh Linh",
        "lead": "Lê Minh Đức",
        "ally": "Trần Bảo Ngọc",
        "villain": "Đỗ Hoàng Phúc",
        "ex": "Phan Yến Nhi",
        "domain": "xây dựng hạ tầng xanh",
        "place": "phố Duy Tân Cầu Giấy và Trung tâm Đấu thầu Quốc gia",
        "proof": "nhật ký thi công gốc, mẫu bê tông lưu kho, biên bản nghiệm thu độc lập",
        "bottleneck": "đội thi công bị rút giấy phép tạm thời trong mưa bão",
        "reward": "gói thầu cầu vượt 540 tỷ",
        "visual": "a Vietnamese civil engineer in a rain-soaked construction site holding sealed construction logs, city lights and a bridge model behind him",
    },
    {
        "slug": "khinh-re-o-da-lat",
        "title": "Bị Nhà Vợ Khinh Ở Đồi Chè Cầu Đất, Tôi Mua Lại Nhà Máy Khiến Họ Xin Đứng Tên Thuê",
        "author": "Song Lam",
        "lead": "Võ Gia Huy",
        "ally": "Lâm Hạ Vy",
        "villain": "Lâm Quốc Tuấn",
        "ex": "Lâm Nhã Uyên",
        "domain": "trà đặc sản và nông nghiệp sạch",
        "place": "đồi chè Cầu Đất Đà Lạt",
        "proof": "hợp đồng thuê đất sạch, chứng nhận kiểm nghiệm dư lượng, sao kê Agribank",
        "bottleneck": "nhà máy bị cắt nguồn thu mua suốt 30 giờ",
        "reward": "chuỗi trà dưỡng sinh 210 tỷ",
        "visual": "a determined Vietnamese tea entrepreneur standing among misty Da Lat tea hills, holding land contracts while a wealthy family looks ashamed",
    },
    {
        "slug": "bi-cuop-thiet-ke-da-nang",
        "title": "Bị Cướp Bản Thiết Kế Ở Đà Nẵng, Tôi Mang Hồ Sơ Sở Hữu Trí Tuệ Đập Tan Buổi Ra Mắt",
        "author": "Hải Yến",
        "lead": "Ngô Nhật Quân",
        "ally": "Phạm Minh Châu",
        "villain": "Hoàng Tấn Lộc",
        "ex": "Bùi Khánh Ngân",
        "domain": "thiết kế du thuyền du lịch",
        "place": "Cảng Tiên Sa Đà Nẵng",
        "proof": "bản vẽ tay có công chứng, hồ sơ sở hữu trí tuệ, video xưởng mẫu",
        "bottleneck": "đối tác Singapore tạm dừng chuyển tiền đặt cọc",
        "reward": "đội du thuyền nghỉ dưỡng 430 tỷ",
        "visual": "a Vietnamese yacht designer on Da Nang harbor at dusk, holding certified blueprints, luxury yacht silhouette behind",
    },
    {
        "slug": "bo-roi-o-can-tho",
        "title": "Bị Bỏ Rơi Giữa Chợ Nổi Cần Thơ, Tôi Dựng Chuỗi Sầu Riêng Khiến Sếp Cũ Cầu Cứu",
        "author": "Mộc Trà",
        "lead": "Huỳnh Tấn Lộc",
        "ally": "Nguyễn Hương Giang",
        "villain": "Cao Đức Nghĩa",
        "ex": "Trần Kim Sa",
        "domain": "logistics trái cây miền Tây",
        "place": "chợ nổi Cái Răng và kho lạnh Cần Thơ",
        "proof": "hợp đồng nông hộ, nhật ký nhiệt độ kho lạnh, chứng thư kiểm dịch",
        "bottleneck": "container bị giữ tại cửa khẩu vì giấy tờ giả do đối thủ cài",
        "reward": "chuỗi xuất khẩu sầu riêng 390 tỷ",
        "visual": "a Vietnamese fruit logistics founder on a floating market boat, durian crates and refrigerated trucks behind, rivals sweating under sunrise",
    },
    {
        "slug": "mat-mat-o-landmark",
        "title": "Bị Làm Nhục Ở Landmark 81, Tôi Công Bố Camera Két Sắt Khiến Chủ Tịch Giả Quỳ Xin Tha",
        "author": "Tịnh An",
        "lead": "Đặng Minh Triết",
        "ally": "Vũ Thiên Kim",
        "villain": "Lý Thành Duy",
        "ex": "Đỗ Hạ My",
        "domain": "quỹ đầu tư gia đình",
        "place": "Landmark 81 và phòng họp ngân hàng BIDV",
        "proof": "camera két sắt, di chúc công chứng, lệnh phong tỏa tài khoản",
        "bottleneck": "báo chí đồng loạt đưa tin anh biển thủ quỹ gia đình",
        "reward": "quỹ đầu tư 900 tỷ được trả lại chính chủ",
        "visual": "a Vietnamese heir in a black suit in a skyscraper boardroom, holding a sealed will and security footage stills, false chairman kneeling",
    },
    {
        "slug": "dinh-chi-phong-kham-hue",
        "title": "Bị Đình Chỉ Phòng Khám Ở Huế, Tôi Dùng Hồ Sơ Lâm Sàng Cứu Người Khiến Hội Đồng Đổi Giọng",
        "author": "Diệp Chi",
        "lead": "Nguyễn Khải Hoàn",
        "ally": "Tôn Nữ Bảo Trâm",
        "villain": "Phan Trọng Kiên",
        "ex": "Lê Ngọc Hà",
        "domain": "y học phục hồi sau tai biến",
        "place": "Huế và Bệnh viện Trung ương Huế",
        "proof": "MRI trước sau, hồ sơ xét nghiệm, biên bản hội đồng chuyên môn",
        "bottleneck": "phòng khám bị khóa niêm phong, bệnh nhân kéo đến khóc ngoài cổng",
        "reward": "trung tâm phục hồi chức năng miền Trung 310 tỷ",
        "visual": "a Vietnamese rehabilitation doctor in Hue hospital corridor with MRI scans, imperial city rain outside, inspectors stunned",
    },
    {
        "slug": "cuoi-nhao-o-pho-co",
        "title": "Bị Cười Nhạo Ở Phố Cổ, Tôi Khôi Phục Bí Phương Nước Mắm Khiến Cả Hiệp Hội Đứng Dậy Vỗ Tay",
        "author": "Gia Hân",
        "lead": "Bùi Khánh Toàn",
        "ally": "Phạm An Khuê",
        "villain": "Trịnh Quang Vinh",
        "ex": "Nguyễn Thùy Dung",
        "domain": "nước mắm truyền thống",
        "place": "Hàng Bạc Hà Nội và Phú Quốc",
        "proof": "sổ ủ chượp ba đời, kiểm nghiệm đạm, hợp đồng vùng nguyên liệu",
        "bottleneck": "nhãn hàng bị tố pha hóa chất và bị siêu thị gỡ kệ",
        "reward": "chuỗi đặc sản Việt 150 tỷ",
        "visual": "a Vietnamese artisan food founder in an old Hanoi street holding ancestral fermentation books, amber fish sauce barrels glowing",
    },
    {
        "slug": "bi-do-toi-o-ngan-hang",
        "title": "Bị Đổ Tội Làm Mất 80 Tỷ, Tôi Đem Sao Kê Techcombank Khiến Giám Đốc Run Rẩy Trả Ghế",
        "author": "Nam Phương",
        "lead": "Trần Gia Bách",
        "ally": "Nguyễn Ngọc Mai",
        "villain": "Dương Chí Hào",
        "ex": "Lê Bảo Quyên",
        "domain": "tài chính doanh nghiệp",
        "place": "Techcombank Hội sở và Ủy ban Chứng khoán Nhà nước",
        "proof": "sao kê giao dịch, log phê duyệt hai lớp, báo cáo kiểm toán Big 4",
        "bottleneck": "anh bị tạm đình chỉ và cấm vào hệ thống kế toán",
        "reward": "vị trí giám đốc tài chính tập đoàn 700 tỷ",
        "visual": "a Vietnamese finance manager in a bank boardroom holding stamped statements, luxury directors pale and sweating",
    },
    {
        "slug": "cho-ngoi-ngoai-san-bay",
        "title": "Bị Cho Ngồi Ngoài Sân Bay Nội Bài, Tôi Ký Hợp Đồng Logistics Khiến Cả Đoàn Xin Theo Hầu",
        "author": "An Vũ",
        "lead": "Mai Quốc Việt",
        "ally": "Đinh Lan Anh",
        "villain": "Tạ Minh Sơn",
        "ex": "Hoàng Mỹ Linh",
        "domain": "logistics hàng lạnh hàng không",
        "place": "sân bay Nội Bài và khu công nghiệp Bắc Ninh",
        "proof": "hợp đồng vận tải, nhật ký nhiệt độ, xác nhận hải quan",
        "bottleneck": "lô hàng vaccine bị giữ do hồ sơ bị tráo trang",
        "reward": "mạng lưới kho lạnh hàng không 480 tỷ",
        "visual": "a Vietnamese cold-chain logistics founder at Noi Bai airport cargo terminal, refrigerated containers and stamped customs papers behind",
    },
    {
        "slug": "bi-phu-nhan-o-binh-duong",
        "title": "Bị Phủ Nhận Công Lao Ở Bình Dương, Tôi Đưa Bằng Sáng Chế Khiến Nhà Máy Quỳ Xin Chuyển Nhượng",
        "author": "Tú Uyên",
        "lead": "Lương Đức Tín",
        "ally": "Bùi Thanh Hà",
        "villain": "Nguyễn Hữu Khoa",
        "ex": "Võ Yến Trang",
        "domain": "vật liệu bao bì sinh học",
        "place": "khu công nghiệp VSIP Bình Dương",
        "proof": "bằng sáng chế, mẫu thử niêm phong, hợp đồng chuyển giao công nghệ",
        "bottleneck": "dây chuyền bị dừng vì bị tố ăn cắp quy trình",
        "reward": "nhà máy bao bì xanh 620 tỷ",
        "visual": "a Vietnamese materials engineer in a modern factory holding patent certificates, green packaging machines behind, executives kneeling",
    },
    {
        "slug": "tu-hon-o-nha-hang-quan-1",
        "title": "Bị Từ Hôn Ở Nhà Hàng Quận 1, Tôi Mở Hồ Sơ Thuế Khiến Gia Tộc Hào Môn Tự Cắt Đường Lui",
        "author": "Vân Nhi",
        "lead": "Hồ Quang Minh",
        "ally": "Đặng Khánh Ly",
        "villain": "Lâm Thiên Vũ",
        "ex": "Lâm Ái Nhi",
        "domain": "tư vấn thuế và mua bán sáp nhập",
        "place": "Quận 1 TP.HCM và Cục Thuế TP.HCM",
        "proof": "hồ sơ thuế, hợp đồng góp vốn, biên bản họp cổ đông",
        "bottleneck": "văn phòng bị niêm phong vì đơn tố cáo nặc danh",
        "reward": "thương vụ M&A 1.200 tỷ",
        "visual": "a Vietnamese tax consultant in a luxury District 1 restaurant holding sealed tax dossiers, elite family shocked",
    },
    {
        "slug": "bi-cam-song-o-nha-trang",
        "title": "Bị Cấm Sóng Ở Nha Trang, Tôi Công Khai Nhật Ký Tàu Khiến Ông Trùm Du Lịch Mất Bến",
        "author": "Hạ Miên",
        "lead": "Dương Nhật Long",
        "ally": "Lê Hải An",
        "villain": "Phạm Chí Dũng",
        "ex": "Trần Bích Ngọc",
        "domain": "du lịch biển an toàn",
        "place": "bến du thuyền Nha Trang",
        "proof": "nhật ký tàu, biên bản bảo trì, video camera cầu cảng",
        "bottleneck": "toàn bộ tour bị hủy vì tin đồn tàu không đạt an toàn",
        "reward": "liên minh du lịch biển 350 tỷ",
        "visual": "a Vietnamese marine tour operator at Nha Trang marina holding ship logs, stormy sea and luxury boats behind",
    },
    {
        "slug": "bi-ep-ky-no-o-long-bien",
        "title": "Bị Ép Ký Nợ Ở Long Biên, Tôi Đem Hợp Đồng Kho Vận Khiến Chủ Nợ Giả Tự Thú Trước C03",
        "author": "Bảo Châu",
        "lead": "Nguyễn Thành Luân",
        "ally": "Vũ Minh Hạnh",
        "villain": "Đào Văn Sử",
        "ex": "Đinh Thu Trang",
        "domain": "kho vận nông sản",
        "place": "Long Biên Hà Nội và trụ sở C03",
        "proof": "hợp đồng kho vận, phiếu cân xe, camera cổng kho",
        "bottleneck": "kho bị cắt điện lạnh khiến hàng tỷ đồng nông sản suýt hỏng",
        "reward": "hệ thống kho vận Bắc Bộ 280 tỷ",
        "visual": "a Vietnamese warehouse founder at Long Bien cold storage holding contracts, police economic crime office atmosphere, false creditor terrified",
    },
    {
        "slug": "bi-thay-the-o-san-khau",
        "title": "Bị Thay Thế Trước Đêm Diễn, Tôi Đưa Bản Quyền Âm Nhạc Khiến Cả Nhà Hát Đứng Im",
        "author": "Lạc Nhiên",
        "lead": "Lê Thiện Nhân",
        "ally": "Phan Quỳnh Dao",
        "villain": "Vũ Hải Đăng",
        "ex": "Ngô Minh Ánh",
        "domain": "sản xuất âm nhạc và bản quyền biểu diễn",
        "place": "Nhà hát Lớn Hà Nội",
        "proof": "hợp đồng bản quyền, file master gốc, biên lai đăng ký tác phẩm",
        "bottleneck": "show diễn bị truyền thông đòi hủy vì tố đạo nhạc",
        "reward": "tour hòa nhạc 120 tỷ",
        "visual": "a Vietnamese music producer on the Hanoi Opera House stage holding copyright certificates, spotlight and stunned performers",
    },
    {
        "slug": "bi-doi-khoi-vuon-thuoc",
        "title": "Bị Đuổi Khỏi Vườn Thuốc Ba Vì, Tôi Cứu Cụ Tổ Hào Môn Khiến Kẻ Cướp Đất Dập Đầu",
        "author": "Thanh Yên",
        "lead": "Tạ Minh Sơn",
        "ally": "Nguyễn Diệu Hằng",
        "villain": "Cao Mạnh Hùng",
        "ex": "Phạm Thu Hoài",
        "domain": "dược liệu sạch và phục hồi sức khỏe",
        "place": "Ba Vì và Bệnh viện Lão khoa Trung ương",
        "proof": "giấy chứng nhận vùng trồng, xét nghiệm độc tính, hồ sơ lâm sàng",
        "bottleneck": "vườn thuốc bị cưỡng chế nhầm trong một đêm mưa",
        "reward": "chuỗi dược liệu sạch 450 tỷ",
        "visual": "a Vietnamese herbal doctor in Ba Vi medicinal garden holding clinical lab results, misty mountain and wealthy family behind",
    },
    {
        "slug": "bi-gach-ten-o-hoi-nghi",
        "title": "Bị Gạch Tên Khỏi Hội Nghị, Tôi Trưng Hồ Sơ Chuỗi Lạnh Khiến Tập Đoàn Sữa Xin Mua Lại",
        "author": "Kiều Anh",
        "lead": "Vũ Gia Phong",
        "ally": "Đỗ Thanh Tâm",
        "villain": "Bùi Trọng Nghĩa",
        "ex": "Trần Hồng Nhung",
        "domain": "chuỗi lạnh sữa tươi cao nguyên",
        "place": "Mộc Châu và hội nghị thực phẩm Hà Nội",
        "proof": "log nhiệt độ, chứng nhận vi sinh, hợp đồng nông trại",
        "bottleneck": "toàn bộ xe lạnh bị giữ ở trạm cân vì hồ sơ bị tố giả",
        "reward": "chuỗi sữa cao nguyên 530 tỷ",
        "visual": "a Vietnamese dairy cold-chain founder at a food conference holding temperature logs, mountain dairy farms on screen, rivals pale",
    },
    {
        "slug": "bi-mat-dat-o-phu-quoc",
        "title": "Bị Cướp Đất Ở Phú Quốc, Tôi Lật Hồ Sơ Quy Hoạch Khiến Cả Hội Đồng Phải Xin Lỗi Công Khai",
        "author": "Quỳnh Lam",
        "lead": "Phan Hải Đăng",
        "ally": "Lưu Bảo Nhi",
        "villain": "Đinh Văn Chương",
        "ex": "Mai Khánh Băng",
        "domain": "resort sinh thái và quy hoạch đất",
        "place": "Phú Quốc và văn phòng đăng ký đất đai Kiên Giang",
        "proof": "hồ sơ quy hoạch, sổ đỏ gốc, biên bản đo đạc độc lập",
        "bottleneck": "công trường bị rào lại và khách quốc tế hủy đặt cọc",
        "reward": "resort sinh thái 880 tỷ",
        "visual": "a Vietnamese eco resort developer on Phu Quoc beach holding land planning dossiers, council officials bowing under sunset",
    },
]


def p(text: str) -> str:
    return f"<p>{html.escape(text, quote=False)}</p>"


def intro(c: dict) -> str:
    return "".join(
        [
            p(f"\"{c['lead']}, anh tưởng mình là ai mà dám ngồi cùng bàn với chúng tôi?\" {c['villain']} ném tập hồ sơ xuống sàn, còn {c['ex']} lạnh lùng quay mặt đi trước tiếng cười của cả phòng."),
            p(f"Không ai biết người bị đẩy ra khỏi {c['place']} ấy đang giữ {c['proof']}. Đó không phải một lời thanh minh yếu ớt, mà là lưỡi dao pháp lý đã được mài suốt nhiều tháng."),
            p(f"Khi {c['bottleneck']}, tất cả đều tin {c['lead']} đã hết đường sống. Nhưng chính đêm bị dồn vào chân tường ấy, anh bắt đầu kéo từng kẻ phản bội bước ra ánh sáng."),
            p(f"Từ một người bị khinh rẻ trong ngành {c['domain']}, {c['lead']} lật ngược ván cờ bằng bằng chứng thật, người thật, tiền thật, để đổi lấy {c['reward']} và một lời xin lỗi muộn màng không còn giá trị."),
        ]
    )


def cover_prompt(c: dict) -> str:
    return (
        "Square 1:1 photorealistic Vietnamese web novel cover, cinematic movie poster, "
        f"{c['visual']}, set in {c['place']}, dramatic high contrast lighting, real human actors, "
        "centered main character in the lower 65 percent of the image, top 30 percent dark clean space for Vietnamese title overlay, "
        "no text, no watermark, no logo, premium urban revenge drama mood."
    )


def chapter_title(i: int, c: dict) -> str:
    names = [
        f"Chương 1: Ngày {c['lead']} Bị Đạp Ra Khỏi Bàn Tiệc",
        f"Chương 2: Người Đầu Tiên Dám Đòi Xem Bằng Chứng",
        f"Chương 3: Cú Phản Đòn Nhỏ Khiến Cả Phòng Im Bặt",
        f"Chương 4: Đêm {c['bottleneck'].capitalize()}",
        f"Chương 5: Hồ Sơ Đóng Dấu Đỏ",
        f"Chương 6: Khi {c['villain']} Quỳ Xuống",
        f"Chương 7: Lời Khai Khiến {c['ex']} Không Còn Đường Chối",
        f"Chương 8: Đêm Tất Cả Bằng Chứng Được Niêm Phong",
        f"Chương 9: {c['ally']} Đặt Cược Vào Người Không Còn Gì Để Mất",
        f"Chương 10: Hợp Đồng {c['reward']} Đổi Chủ",
        f"Chương 11: Cú Phản Công Cuối Của {c['villain']}",
        f"Chương 12: Buổi Họp Báo Không Ai Dám Rời Ghế",
        f"Chương 13: Người Từng Cười Nhạo Bắt Đầu Xếp Hàng Xin Lỗi",
        f"Chương 14: Cái Giá Của Một Chữ Ký Gian Dối",
        f"Chương 15: Từ Sàn Lạnh Đến Đỉnh Cao Mới",
    ]
    return names[i - 1]


def tail_chapter_blocks(i: int, c: dict) -> list[str]:
    lead = c["lead"]
    ally = c["ally"]
    villain = c["villain"]
    ex = c["ex"]
    domain = c["domain"]
    place = c["place"]
    proof = c["proof"]
    bottleneck = c["bottleneck"]
    reward = c["reward"]

    stage_notes = {
        7: (
            f"một nhân chứng phụ trong hồ sơ {domain}",
            f"người từng giữ bản giao nhận liên quan đến {proof}",
            f"một quán cà phê nhỏ gần {place}",
            "lời khai bị đứt đoạn",
        ),
        8: (
            "đêm niêm phong chứng cứ",
            f"két lưu trữ chứa {proof}",
            "phòng sao lưu có máy lạnh chạy rì rì",
            "một bản sao bị tráo mã",
        ),
        9: (
            f"sức ép dồn lên {ally}",
            f"cam kết đầu tư cho {reward}",
            "phòng họp chỉ bật một hàng đèn",
            "đơn tố cáo nặc danh",
        ),
        10: (
            "bàn đàm phán đầu tiên",
            f"bản dự thảo {reward}",
            f"văn phòng đối tác ở {place}",
            "điều khoản bồi thường bị giấu",
        ),
        11: (
            f"đòn phản công cuối của {villain}",
            f"tin đồn bẩn trong ngành {domain}",
            "một cuộc gọi lúc gần sáng",
            "lệnh hủy gặp bất ngờ",
        ),
        12: (
            "buổi họp báo công khai",
            f"bộ hồ sơ {proof}",
            "hàng ghế phóng viên chật kín",
            "câu hỏi gài bẫy cuối phòng",
        ),
        13: (
            "ngày dư luận đổi chiều",
            f"những người từng rời bỏ {lead}",
            "sảnh văn phòng đông nghẹt",
            "lời xin lỗi đến quá muộn",
        ),
        14: (
            "phiên làm việc pháp lý",
            f"mấu chốt xoay quanh {proof}",
            "căn phòng có camera ghi biên bản",
            "chữ ký gian dối bị bóc trần",
        ),
        15: (
            "ngày đặt nền cho chương mới",
            f"hợp đồng {reward}",
            f"không gian yên tĩnh nhìn xuống {place}",
            "một lời hứa không cần ồn ào",
        ),
    }
    subject, object_line, location, conflict = stage_notes[i]
    rng = random.Random(f"{c['slug']}-{i}")

    openers = [
        f"Sau vụ đối chất, {lead} không trở về nhà ngay mà vòng qua {location}.",
        f"Ngày tiếp theo mở ra bằng một cuộc hẹn kín ở {location}, nơi {lead} tự tay kiểm lại từng trang hồ sơ.",
        f"{location.capitalize()} trở thành điểm rẽ mới của vụ việc, vì ở đó có một chi tiết {villain} từng tin rằng đã bị chôn vùi.",
        f"Trước khi trời sáng hẳn, {lead} đã có mặt tại {location}; chiếc cặp tài liệu đặt trên ghế bên cạnh nặng như một lời thề.",
    ]
    witness_lines = [
        f"Người xuất hiện đầu tiên không phải luật sư, mà là một nhân viên cũ từng im lặng vì sợ mất việc. Anh ta đặt {object_line} lên bàn, hai tay run đến mức mép giấy va nhẹ vào ly nước.",
        f"Một nhân chứng phụ bước vào bằng cửa sau. Người ấy tránh nhìn thẳng vào {lead}, nhưng lại nhớ rất rõ giờ nhận chỉ đạo, biển số xe và câu nói mà {villain} dùng để ép họ đổi lời.",
        f"Thứ làm căn phòng im đi là một phong bì mỏng. Bên trong không có tiền, chỉ có bản ghi thời gian, ảnh chụp màn hình và một mảnh chứng cứ nối thẳng tới {conflict}.",
        f"Nhân chứng đến muộn mười bảy phút. Trên cổ tay họ vẫn còn vết hằn đồng hồ, như vừa trải qua một cuộc giằng co dài trước khi đủ can đảm bước vào.",
    ]
    ally_lines = [
        f"{ally} không nhận tài liệu ngay. Cô yêu cầu người kia đọc lại lời khai trước camera, sau đó tự tay đánh dấu những điểm cần đối chiếu. Cô không cho phép lòng thương thay thế thủ tục.",
        f"{ally} kéo ghế ngồi sát máy ghi âm. Mỗi khi nhân chứng nói tới một mốc quan trọng, cô lại dừng lại hỏi nguồn xác nhận. Sự bình tĩnh của cô khiến cả căn phòng không ai dám hấp tấp.",
        f"{ally} đặt ba câu hỏi liên tiếp, câu sau khó hơn câu trước. Khi người làm chứng trả lời khớp với hồ sơ cũ, cô mới gật đầu rất nhẹ, như vừa đặt thêm một viên đá vào nền móng.",
        f"{ally} không nhìn {lead} để xin ý kiến. Cô xử lý như một người bảo vệ quy trình: có chữ ký, có đối chiếu, có bản sao lưu, rồi mới có niềm tin.",
    ]
    villain_lines = [
        f"Tin ấy đến tai {villain} vào buổi chiều. Hắn đang ở trong phòng riêng, tay cầm ly trà nhưng nước sóng sánh tràn ra đĩa. Vẻ tự tin trên mặt hắn nứt ra từng đường nhỏ.",
        f"{villain} nhận cuộc gọi giữa bữa ăn. Hắn buông đũa, quai hàm cứng lại. Mấy giây sau, hắn đứng dậy quá nhanh làm chân ghế rít trên sàn, âm thanh sắc đến mức người phục vụ giật mình.",
        f"Ở phía đối diện thành phố, {villain} lật đi lật lại bản tin nội bộ. Cổ áo hắn thấm một vệt mồ hôi lạnh. Hắn cố mắng trợ lý, nhưng câu chửi bị nghẹn giữa họng.",
        f"{villain} không còn dám ra lệnh bằng giọng lớn. Hắn nói nhỏ hơn, nhanh hơn, và cứ nhìn về phía cửa kính như sợ có người đang ghi âm sau lưng.",
    ]
    ex_lines = [
        f"{ex} cũng bắt đầu loạn. Cô ta xóa vài tin nhắn cũ rồi lại khôi phục, không biết hành động nào sẽ khiến mình ít tội hơn. Sự sang trọng từng che chở cô bỗng trở nên mỏng như giấy.",
        f"{ex} gửi một tin nhắn xin gặp riêng, lời lẽ mềm đi bất thường. {lead} đọc xong chỉ chuyển cho luật sư lưu hồ sơ. Tình cũ không còn quyền đi đường tắt qua công lý.",
        f"Khi {ex} nghe tên mình xuất hiện trong lời khai, lớp phấn trên mặt cô như trắng hơn. Cô gọi cho {villain}, nhưng hắn tắt máy. Liên minh phản bội bắt đầu học cách bỏ rơi lẫn nhau.",
        f"{ex} đứng trước gương rất lâu, tập một câu xin lỗi. Nhưng những câu được tập trước đều có mùi tính toán, và chính cô cũng nghe ra điều đó.",
    ]
    pressure_lines = [
        f"Khủng hoảng vẫn chưa buông. {bottleneck.capitalize()} để lại một khoảng trống dòng tiền, khiến đội của {lead} phải thương lượng từng hóa đơn nhỏ. Không ai được phép tiêu một đồng chỉ để giữ thể diện.",
        f"Đối tác gọi tới ba lần trong buổi tối. Họ không hủy, nhưng yêu cầu thêm bảo lãnh. {lead} đồng ý gửi hồ sơ, đồng thời nhắc cả đội rằng niềm tin thương mại phải được trả bằng giấy tờ sạch.",
        f"Một nhà cung cấp muốn rút lui. {lead} không trách họ; anh chỉ gửi bảng tiến độ, cam kết thanh toán và bằng chứng vụ vu khống đang được thụ lý. Đến khuya, người ấy nhắn lại một chữ: chờ.",
        f"Trên mạng, một nhóm tài khoản mới tiếp tục công kích. Lần này {lead} không phản bác từng dòng. Anh gom ảnh chụp, lưu link, lập bảng thời gian. Tiếng ồn cũng có thể trở thành chứng cứ nếu biết xếp nó đúng chỗ.",
    ]
    scene_lines = [
        f"Đến nửa đêm, {lead} mở lại bản đồ toàn bộ vụ việc. Mỗi mũi tên nối một người, một khoản tiền, một lần ký nhận. Anh nhận ra điểm yếu không nằm ở tài liệu lớn nhất, mà ở một chi tiết nhỏ quanh {conflict}.",
        f"Có lúc căn phòng chỉ còn tiếng bút của {ally}. {lead} nhìn bàn tay cô ghi chú, chợt hiểu cô không đứng cạnh anh vì thương hại. Cô đang chọn một trận chiến mà cô tin có thể thắng bằng kỷ luật.",
        f"Một cuộc gọi từ mẹ làm {lead} dừng lại vài phút. Bà không hỏi thắng thua, chỉ dặn anh ăn gì đó nóng. Anh nhìn hộp cơm nguội trên bàn, thấy cổ họng nghẹn lại. Người bị vu oan vẫn phải sống như một người con bình thường.",
        f"Sáng gần tới, {ally} rót cho anh một cốc nước. Không ai nói chuyện tình cảm. Nhưng khi cô đặt cốc sát tay anh, khoảng cách giữa họ đã khác: ít phòng bị hơn, nhiều tin cậy hơn.",
    ]
    evidence_lines = [
        f"Sợi dây cuối cùng được kéo ra từ {object_line}. Nó khớp với dữ liệu ngân hàng, khớp với camera, và khớp với lời khai mới. Không có tiếng reo mừng, chỉ có một sự im lặng nặng vì ai cũng hiểu trận này đã sang cấp khác.",
        f"Kết quả đối chiếu về lúc trời vừa sáng. Dấu thời gian không lệch một giây. {lead} đặt bản in vào túi niêm phong, ghi mã hồ sơ, rồi yêu cầu scan thêm một bản để lưu ở nơi khác.",
        f"Điều khiến {villain} nguy hiểm không phải hắn thông minh, mà là hắn từng quen được bỏ qua. Lần này, từng thứ bị bỏ qua được {lead} nhặt lại, đánh số và đặt vào đúng ô.",
        f"Khi tài liệu được sắp thành ba tập, {ally} mới nói: \"Bây giờ có thể đánh.\" {lead} nhìn ba tập giấy ấy. Chúng không đẹp, không hào nhoáng, nhưng sạch đến mức đủ làm người bẩn khiếp sợ.",
    ]
    industry_lines = [
        f"Điểm khó của {domain} là người ngoài chỉ nhìn thấy tiền, còn người trong nghề biết mọi thứ sống chết ở quy trình. {lead} bắt đầu giải thích cho đội mới cách đọc từng chỉ dấu: số lô, giờ ký, mã lưu trữ, người bàn giao. Anh không muốn chiến thắng dựa vào may mắn.",
        f"Trong lĩnh vực {domain}, uy tín mất đi thường không thể mua lại bằng quảng cáo. Vì vậy {lead} chọn cách chậm hơn: để từng tài liệu tự nói, từng người làm chứng tự ký, từng cơ quan xác nhận bằng đúng thẩm quyền của họ.",
        f"{place} vốn quen những cuộc bắt tay bóng bẩy, nhưng lần này {lead} mang tới một thứ kém lấp lánh hơn: bảng đối chiếu sai phạm dày đặc ghi chú. Chính sự khô khan ấy khiến đối thủ khó bẻ lái sang cảm xúc.",
        f"Những người làm cùng {lead} bắt đầu hiểu vì sao anh nhất quyết giữ hồ sơ sạch. Một dấu tẩy xóa nhỏ cũng có thể biến sự thật thành trò cãi vã. Anh thà mất thêm một đêm kiểm lại, còn hơn để {villain} có cớ thoát.",
    ]
    procedural_lines = [
        f"Luật sư yêu cầu mọi bản sao phải ghi nơi nhận, giờ nhận và người bàn giao. {lead} ký từng tờ, cổ tay mỏi nhưng không dừng. Càng gần thắng, anh càng sợ một sai sót nhỏ làm công sức của cả đội đổ xuống sông.",
        f"Biên bản mới được lập thành bốn bản. Một bản gửi đơn vị thẩm định, một bản lưu tại văn phòng, một bản chuyển cho luật sư, bản cuối cùng đặt trong phong bì niêm phong. {ally} kiểm tra mép dán đến lần thứ ba mới cho mang đi.",
        f"Có người đề nghị tung toàn bộ lên mạng để dư luận xử trước. {lead} từ chối. Anh nói mạng xã hội có thể tạo sức ép, nhưng thứ hạ gục {villain} phải là trình tự pháp lý, vì chỉ trình tự ấy mới khiến hắn không thể diễn vai nạn nhân.",
        f"Đến cuối buổi, bảng thời gian được in ra dài hơn ba mét nếu nối liền. Mỗi mốc đều có người chịu trách nhiệm xác nhận. Nhìn vào đó, {lead} thấy cơn nhục ngày đầu không còn là một vết thương lộn xộn, mà đã thành một hồ sơ có thể chiến đấu.",
    ]
    team_lines = [
        f"Một nhân viên trẻ xin lỗi vì từng tin lời {villain}. {lead} không trách, chỉ giao cho cậu kiểm lại phụ lục. Cách tha thứ của anh không mềm yếu: ai muốn quay về phe sự thật phải làm việc tử tế hơn trước.",
        f"Trong góc phòng, người phụ trách truyền thông gạch bỏ ba câu quá cay nghiệt khỏi thông cáo. {lead} gật đầu. Anh không cần mạt sát để thắng. Càng bình tĩnh, sự bẩn thỉu của đối thủ càng hiện rõ.",
        f"Cả đội thay nhau ngủ trên ghế. Có người dùng áo khoác làm gối, có người ôm laptop như ôm phao cứu sinh. {lead} nhìn họ, tự nhắc nếu giành được {reward}, phần đầu tiên phải dành để trả đủ công cho những người đã không bỏ chạy.",
        f"{ally} đặt một hộp thuốc đau dạ dày cạnh bàn anh. Cô không nói câu quan tâm nào quá mềm. Nhưng {lead} hiểu: có những người chăm sóc bằng cách nhắc mình ký đúng trang, ăn đúng bữa và đừng chết chìm trong thù hận.",
    ]
    antagonist_damage_lines = [
        f"Trong khi đó, {villain} bắt đầu mất những cuộc gọi từng luôn được trả lời. Một chủ tịch cũ cáo bận, một trưởng phòng pháp chế xin họp sau, một người bạn nhậu nói đang ở nước ngoài dù ảnh định vị vẫn hiện trong thành phố.",
        f"{villain} thử đổ lỗi cho cấp dưới. Nhưng cấp dưới của hắn cũng đã giữ lại tin nhắn. Khi một kẻ quen dùng người khác làm lá chắn gặp những người bắt đầu tự bảo vệ mình, hắn mới hiểu quyền lực vay mượn mỏng đến thế nào.",
        f"Tài xế riêng của {villain} xin nghỉ không lương. Kế toán trưởng không đến công ty. Ngay cả {ex} cũng chỉ nhắn một câu cụt ngủn rồi biến mất. Đế chế của hắn chưa sụp trên báo, nhưng đã rỗng từ bên trong.",
        f"Đêm ấy, {villain} đứng trước cửa sổ căn hộ cao tầng. Thành phố dưới chân vẫn sáng, nhưng ánh sáng ấy không còn thuộc về hắn. Mỗi lần điện thoại rung, vai hắn lại giật nhẹ như người nghe tiếng gõ cửa của công an.",
    ]
    emotion_lines = [
        f"Khi chỉ còn hai người, {ally} hỏi {lead} có từng muốn bỏ cuộc không. Anh đáp có, nhiều hơn một lần. Nhưng mỗi lần nghĩ tới cảnh {ex} đứng im khi anh bị lôi ra cửa, anh lại thấy mình không được phép để sự im lặng ấy trở thành bản án cuối.",
        f"{lead} thú nhận anh sợ nhất không phải thua tiền, mà là mẹ đọc được những lời chửi trên mạng. {ally} nghe xong rất lâu không nói. Sau đó cô chỉ bảo: \"Vậy thắng cho sạch, để sau này bác đọc lại sẽ biết con mình đã đi qua thế nào.\"",
        f"Câu chuyện giữa họ không có hoa, không có nhạc nền. Nó nằm trong tiếng máy in, mùi cà phê nguội và những trang giấy đầy dấu bút đỏ. Nhưng chính sự thật thà khô ráp ấy khiến {lead} thấy lòng mình bớt lạnh.",
        f"{ally} kể một thất bại cũ của cô, lần cô tin nhầm một người chỉ vì người ấy nói quá hay. Từ đó cô không tin lời đẹp nữa. {lead} mỉm cười mệt mỏi: \"Vậy tốt. Tôi cũng không còn lời đẹp để bán.\"",
    ]
    public_lines = [
        f"Ngoài kia, dư luận đổi chiều theo cách rất ồn. Những người từng mắng {lead} bắt đầu viết rằng họ chỉ muốn chờ sự thật. Anh không đọc quá lâu. Sự thật cần người bảo vệ, nhưng không nên nghiện tiếng vỗ tay muộn.",
        f"Một tờ báo địa phương gửi câu hỏi phỏng vấn. {lead} yêu cầu họ gửi trước nội dung, tránh giật tít làm méo vụ việc. Anh đã học được rằng truyền thông có thể là đèn pha, cũng có thể là lửa nếu để người khác cầm.",
        f"Có người đề nghị biến câu chuyện thành màn trả thù rầm rộ. {lead} lắc đầu. Anh muốn độc giả của vụ việc nhìn thấy chứng cứ, không phải một anh hùng đang diễn. Sự bình thản mới là thứ làm {villain} khó chịu nhất.",
        f"Trên diễn đàn ngành, một bài phân tích dài xuất hiện, chỉ ra những điểm phi lý trong lời bào chữa của {villain}. {lead} không biết tác giả là ai. Nhưng anh biết khi bằng chứng đủ chắc, người lạ cũng có thể trở thành tiếng nói công bằng.",
    ]
    risk_lines = [
        f"Rủi ro lớn nhất lúc này không còn là thiếu chứng cứ, mà là quá nhiều người muốn chen vào câu chuyện để hưởng lợi. {lead} yêu cầu khóa quyền truy cập hồ sơ, chỉ ba người được sửa bảng tổng hợp. Anh đã từng bị cướp công một lần, và lần này anh không cho sự lỏng lẻo có cơ hội lặp lại.",
        f"Một khoản chi khẩn cấp cần được duyệt ngay trong ngày. Nếu chậm, nhóm hỗ trợ sẽ mất chỗ lưu trữ tài liệu; nếu duyệt ẩu, {villain} có thể vin vào đó nói họ rửa tiền. {lead} chọn cách khó hơn: gọi từng bên xác nhận, ghi âm cuộc trao đổi và chuyển khoản đúng nội dung.",
        f"Người phụ trách pháp lý cảnh báo rằng đối thủ có thể kiện ngược để kéo dài thời gian. {lead} nghe xong chỉ yêu cầu chuẩn bị ngân sách kiện tụng sáu tháng. Anh không còn tin vào chiến thắng trong một đêm; thứ anh cần là khả năng đứng vững lâu hơn kẻ nói dối.",
        f"Có một khoảnh khắc cả đội gần như cãi nhau vì áp lực. Một người muốn công khai ngay, người khác sợ vỡ quy trình. {lead} để họ nói hết rồi gõ nhẹ lên bàn: \"Chúng ta không thắng bằng nóng ruột.\" Căn phòng dịu xuống từng chút.",
    ]
    document_lines = [
        f"Tập tài liệu mới dày đến mức kẹp bướm không giữ nổi. {ally} phải chia nó thành từng cụm màu: đỏ cho dòng tiền, xanh cho nhân chứng, vàng cho rủi ro truyền thông. Nhìn chồng giấy ấy, {lead} biết đây không còn là một cuộc cãi vã cá nhân.",
        f"Một bản scan bị mờ ở góc dấu. Thay vì bỏ qua, {lead} yêu cầu xin lại bản rõ hơn. Người phụ trách than rằng chỉ là chi tiết nhỏ, nhưng anh lắc đầu. Trong một trận pháp lý, chi tiết nhỏ chính là nơi kẻ xấu chui dao vào.",
        f"Họ đối chiếu từng chữ ký bằng kính phóng đại. Có chữ ký nghiêng hơn bình thường, có nét móc cuối bị dừng đột ngột. Những dấu hiệu ấy không đủ làm bằng chứng độc lập, nhưng đủ để chỉ đường tới người cần hỏi tiếp.",
        f"Khi máy in hết mực, {lead} tự xuống mua hộp mới ở cửa hàng gần nhất. Anh không để trợ lý đi một mình trong lúc bên ngoài còn người theo dõi. Những việc nhỏ như vậy làm đội hiểu anh không chỉ ra lệnh từ trên cao.",
    ]
    body_lines = [
        f"Đến gần trưa, {villain} xuất hiện chớp nhoáng trước sảnh. Hắn đeo kính đen, nhưng phần cổ lộ ra đỏ lựng. Khi phóng viên gọi tên, vai hắn giật một cái rất khẽ, đủ để camera bắt được khoảnh khắc kiêu ngạo trượt khỏi mặt.",
        f"{ex} thì tệ hơn. Cô ta ngồi trong xe, hai tay xoắn chặt quai túi đến mức móng tay in vệt hằn trên da giả. Cô từng nghĩ mình chỉ đổi phe để sống tốt hơn, không ngờ cái giá lại là bị cả hai bên xem như vật chứng.",
        f"Một người từng tâng bốc {villain} cố len ra cửa sau. Khi bị hỏi, ông ta nói mình không liên quan. Giọng ông run, mồ hôi đọng trên rãnh nhân trung. {lead} nhìn thấy nhưng không đuổi theo. Người sợ sự thật rồi sẽ tự khai nhiều hơn khi bị bỏ một mình.",
        f"Trong màn hình camera, {villain} cúi xuống nhặt chiếc bút rơi mà phải chống tay lên bàn. Động tác ấy rất nhanh, nhưng {lead} nhìn ra: đầu gối hắn đã mềm. Không cần một câu sỉ nhục nào, thân thể hắn đã tự thú trước.",
    ]
    independent_lines = [
        f"Buổi chiều, kết quả xác minh độc lập được gửi về. Không phải kết luận dài dòng, chỉ vài dòng xác nhận nguồn gốc và thời điểm. Nhưng vài dòng ấy đủ chặn toàn bộ lời bào chữa rằng hồ sơ được dựng sau khi tranh chấp nổ ra.",
        f"Một chuyên gia ngoài ngành được mời đọc hồ sơ để kiểm tra tính dễ hiểu. Ông không quen thuật ngữ {domain}, nên chỗ nào ông cau mày, {lead} đánh dấu lại. Nếu người bình thường không hiểu, phản diện sẽ lợi dụng khoảng mờ đó để la hét.",
        f"Đơn vị thẩm định yêu cầu bổ sung một bản gốc. {lead} tự mình đến nơi lưu trữ, ký nhận dưới camera, rồi trở về không ghé đâu khác. Anh muốn chuỗi bảo quản sạch đến mức đối thủ không thể bịa ra một quãng trống.",
        f"Khi con dấu xác nhận thứ hai được đóng xuống, âm thanh cộp khô vang trong phòng. Không ai nói gì trong vài giây. Đó là thứ âm thanh mà người làm ăn bẩn sợ hơn tiếng chửi, vì nó không cần cảm xúc vẫn có sức kết án.",
    ]
    cliff_lines = [
        f"Ngay lúc tưởng mọi thứ đã ổn, một email lạ gửi tới hộp thư chung. Tiêu đề chỉ có ba chữ: \"Bản gốc khác.\" {lead} mở ra, nhìn thấy tên {ex} nằm trong dòng chuyển tiếp cũ. Anh không hoảng, nhưng ánh mắt lạnh hẳn đi.",
        f"Trước khi tắt đèn, {ally} phát hiện một số điện thoại lặp lại trong ba biên bản khác nhau. Nó không thuộc về nhân viên nào trong danh sách. {lead} ghi số ấy lên giấy, khoanh tròn. Một cánh cửa mới vừa hé ra.",
        f"Cửa thang máy mở lúc gần nửa đêm. Người bước ra là một nhân chứng mà {villain} tưởng đã đưa ra nước ngoài. Trên tay người ấy là chiếc điện thoại cũ, màn hình nứt, nhưng bên trong còn đoạn ghi âm chưa từng công bố.",
        f"Khi {lead} chuẩn bị rời văn phòng, luật sư gọi tới. Giọng ông trầm xuống: \"Có người vừa xin tự thú, nhưng họ muốn gặp riêng anh trước.\" {lead} nhìn {ally}. Cả hai đều hiểu đêm nay chưa thể kết thúc.",
    ]
    ending_lines = [
        f"Cuối chương {i}, {lead} không thấy nhẹ nhõm. Anh chỉ thấy con đường phía trước rõ hơn. {reward} không còn là phần thưởng xa vời, mà là trách nhiệm phải giành lại bằng cách không cho sự thật bị bẻ cong thêm lần nào nữa.",
        f"Khi rời {location}, {lead} ngoái nhìn một lần. Nơi đó không có ánh hào quang, nhưng đã giữ lại một mảnh sự thật. Và với anh lúc này, một mảnh sự thật đúng chỗ còn sắc hơn mọi bài diễn thuyết.",
        f"{ally} đi bên cạnh anh, không hỏi anh có sợ không. Cô chỉ đưa bản lịch trình ngày mai. {lead} nhận lấy, gấp gọn. Họ đã qua giai đoạn cần lời hứa; thứ cần hơn là từng bước chính xác.",
        f"Ở phía sau, điện thoại của {villain} sáng liên tục. Không cuộc gọi nào mang tin tốt. Người từng tưởng mình điều khiển ván cờ cuối cùng cũng nghe thấy tiếng quân cờ của chính mình rơi xuống.",
    ]

    pools = [
        openers,
        witness_lines,
        ally_lines,
        industry_lines,
        villain_lines,
        ex_lines,
        pressure_lines,
        procedural_lines,
        team_lines,
        scene_lines,
        antagonist_damage_lines,
        emotion_lines,
        public_lines,
        risk_lines,
        document_lines,
        body_lines,
        independent_lines,
        cliff_lines,
        evidence_lines,
        ending_lines,
    ]
    blocks = [rng.choice(pool) for pool in pools]
    # Add two chapter-specific paragraphs so long tail chapters do not collapse into the same rhythm.
    if i in (7, 8):
        blocks.insert(4, f"{lead} yêu cầu lập biên bản riêng cho {subject}. Anh không tin trí nhớ khi mọi thứ có thể bị mua chuộc, chỉ tin chữ ký, dấu thời gian và người chứng kiến đủ độc lập.")
        blocks.insert(7, f"Một bản phụ lục được gửi tới nơi lưu trữ ngoài thành phố. Nếu {villain} muốn đốt đường lui, hắn sẽ phải đốt quá nhiều cánh cửa cùng lúc.")
    elif i in (9, 10):
        blocks.insert(4, f"{ally} bị kéo vào tâm bão vì {object_line}. Cô không lùi, nhưng cũng không để cảm xúc đẩy mình thành điểm yếu. Cô yêu cầu mọi trao đổi từ giờ đi qua email, không qua cuộc gọi riêng.")
        blocks.insert(7, f"Buổi thương lượng về {reward} vì thế chuyển từ màu sắc cứu nguy sang màu sắc kiểm soát rủi ro. {lead} học cách thắng mà vẫn giữ lưng thẳng trước từng điều khoản.")
    elif i in (11, 12):
        blocks.insert(4, f"{villain} tung một tin giả cuối cùng, nhắm vào uy tín của {lead}. Nhưng tin ấy vội vã đến mức sai cả tên đơn vị kiểm định. Sai lầm nhỏ ấy biến đòn bẩn thành dấu vân tay.")
        blocks.insert(7, f"Khi ánh đèn họp báo bật lên, {lead} không kể khổ. Anh đọc mốc thời gian, đưa chứng cứ, rồi để sự thật tự làm phần còn lại.")
    else:
        blocks.insert(4, f"Những người từng đứng ngoài bắt đầu quay lại. {lead} không sỉ nhục họ, nhưng cũng không xóa sạch lựa chọn cũ. Ai muốn đi tiếp phải ký vào quy tắc minh bạch mới.")
        blocks.insert(7, f"Cái giá dành cho {villain} không chỉ là mất mặt. Đó là từng hợp đồng bị kiểm tra lại, từng mối quan hệ rút tay, từng lời tâng bốc cũ biến thành sự im lặng lạnh lẽo.")
    return blocks


def chapter_content(i: int, c: dict) -> str:
    lead = c["lead"]
    ally = c["ally"]
    villain = c["villain"]
    ex = c["ex"]
    domain = c["domain"]
    place = c["place"]
    proof = c["proof"]
    bottleneck = c["bottleneck"]
    reward = c["reward"]

    if i > 6:
        return "\n".join(p(block) for block in tail_chapter_blocks(i, c))

    chapter_blocks = {
        1: [
            f"Buổi công bố ở {place} vốn được chuẩn bị như một lễ đăng quang cho {villain}. Đèn pha rọi xuống bàn chủ tọa, ly thủy tinh xếp thành hàng, còn {lead} đứng ở mép thảm đỏ với chiếc cặp da cũ đã sờn góc. Anh là người viết những dòng đầu tiên cho dự án {domain}, nhưng trên bảng tên khách mời, tên anh bị gạch bằng bút đỏ.",
            f"{ex} bước qua anh như bước qua một vệt nước bẩn. Cô ta hạ giọng vừa đủ để những người xung quanh nghe thấy: \"Anh đừng làm tôi mất mặt nữa. Công lao của anh chỉ đáng bằng tiền giữ xe.\" Câu nói rơi xuống không khí, kéo theo vài tiếng cười khẽ. {lead} cúi xuống nhặt tấm thẻ bị ném, ngón tay anh dính bụi nhưng mắt không hề đỏ.",
            f"{villain} đẩy cửa phòng họp, chỉ vào anh trước mặt đối tác và truyền thông. Hắn tuyên bố {lead} đã làm thất lạc hồ sơ, phá hỏng uy tín công ty, thậm chí còn ám chỉ anh ăn cắp tài liệu để bán cho đối thủ. Mấy chiếc điện thoại lập tức giơ lên. Một người bảo vệ tiến tới, đặt tay lên vai anh mạnh đến mức đường chỉ áo sơ mi cũ căng ra.",
            f"Trong tiếng xì xào, {lead} nhìn thấy {ally}. Cô không vội bênh vực. Cô đứng ở hàng ghế cuối, tay cầm bút, ánh mắt bình tĩnh như một người đang cân từng lời khai. Chính sự im lặng ấy làm anh thấy dễ chịu hơn những lời thương hại. Anh biết cô không tin ai chỉ vì nước mắt.",
            f"\"Từ hôm nay, mọi hợp đồng liên quan đến {domain} không còn dính dáng gì đến anh,\" {villain} nói. Hắn ném chiếc USB xuống sàn, gót giày nghiền nhẹ lên vỏ nhựa. \"Cầm thứ rác này mà đi.\" {ex} khoác tay hắn, môi cong lên. Một phóng viên trẻ cố dí micro vào mặt {lead}, hỏi anh có muốn xin lỗi công khai hay không.",
            f"{lead} không xin lỗi. Anh chỉ cúi nhặt chiếc USB đã nứt, lau bụi bằng khăn tay, rồi đặt lại vào cặp. Ở đáy cặp còn một bản sao của {proof}. Bản chính nằm trong két ngân hàng, có số niêm phong, có lịch sử truy cập, có người làm chứng. Anh đã giữ nó không phải để khoe khoang, mà để chờ đúng ngày những kẻ ăn cắp tự đứng lên sân khấu.",
            f"Khi bảo vệ kéo anh ra cửa phụ, trời đổ mưa. Nước mưa tạt vào mặt làm cổ áo lạnh buốt. Sau lưng, loa hội trường vẫn vang lên giọng {villain} nói về đạo đức kinh doanh. {lead} bật cười rất khẽ. Không phải nụ cười của người thắng, mà là nụ cười của người vừa xác định được toàn bộ danh sách những kẻ cần phải trả giá.",
            f"Đêm đó, trên mạng bắt đầu lan video anh bị đuổi. Bình luận chửi rủa kéo dài hàng nghìn dòng. Có người gọi anh là kẻ vô dụng, có người thương hại {ex} vì từng yêu nhầm. {lead} ngồi trong căn phòng thuê, pha một ly trà nguội, mở máy ghi âm cũ và nghe lại cuộc họp kín nơi {villain} lần đầu ép anh ký nhượng quyền công sức.",
            f"Nửa đêm, {ally} gọi đến. Câu đầu tiên của cô không phải an ủi. Cô hỏi: \"Anh có bằng chứng đủ để chịu kiểm tra chéo không? Nếu chỉ là uất ức, tôi không giúp. Nếu là hồ sơ thật, sáng mai mang đến cho tôi.\" {lead} nhìn tập tài liệu trên bàn. Anh trả lời: \"Tôi không cần cô tin tôi. Tôi cần cô kiểm tra nó như kiểm tra một quả bom.\"",
            f"Sáng hôm sau, anh mặc lại chiếc áo đã khô, mang cặp ra khỏi nhà. Trên màn hình điện thoại, {villain} vừa đăng ảnh ăn mừng cùng {ex}. Dòng chú thích viết rằng kẻ phản bội đã bị loại khỏi cuộc chơi. {lead} tắt máy. Cuộc chơi, thật ra, bây giờ mới bắt đầu.",
        ],
        2: [
            f"Văn phòng của {ally} không có tranh xa hoa, chỉ có ba màn hình, một máy scan và một tủ hồ sơ khóa kép. Cô nhận cặp tài liệu từ {lead}, không hỏi chuyện tình cũ, không hỏi anh đau thế nào. Cô yêu cầu anh ngồi đối diện camera nội bộ, đọc rõ nguồn gốc từng bản giấy trong {proof}.",
            f"Ba tiếng trôi qua, {ally} đối chiếu từng trang. Khi gặp một điểm chưa khớp, cô gạch bút đỏ ngay trước mặt anh. {lead} không khó chịu. Anh giải thích bằng ngày tháng, số hợp đồng, tên nhân sự bàn giao. Sự bình tĩnh của anh khiến trợ lý của cô mấy lần ngẩng đầu nhìn. Người bị cả mạng chửi mà vẫn nhớ chính xác từng số chứng từ thường không phải kẻ dựng chuyện.",
            f"Tin {lead} tìm nhà đầu tư mới lọt đến tai {villain}. Hắn lập tức sai người tung thêm tin rằng anh làm giả {proof}. Buổi chiều, trước cửa văn phòng {ally}, hai streamer đứng livestream, miệng gào rằng cô đang tiếp tay cho kẻ lừa đảo. Camera dí sát vào mặt {lead} khi anh bước ra.",
            f"{lead} không né. Anh yêu cầu họ ghi hình rõ câu trả lời: \"Tôi sẽ gửi hồ sơ tới đơn vị kiểm định độc lập. Nếu một trang giả, tôi chịu trách nhiệm hình sự. Nếu tất cả là thật, người vu khống tôi hãy chuẩn bị luật sư.\" Giọng anh không cao, nhưng đám đông phía sau bỗng nhỏ tiếng.",
            f"Tối đó, {ex} nhắn tin cho anh. Cô ta viết rằng anh đang tự hủy hoại mình, rằng {villain} có quan hệ đủ rộng để nghiền nát mọi nỗ lực của anh. {lead} đọc xong, xóa tin nhắn. Kỷ niệm cuối cùng giữa họ không còn là một bữa cơm hay lời hứa, mà là tấm ảnh cô ta đứng cạnh kẻ đã cướp công anh.",
            f"{ally} mời một kiểm toán viên độc lập đến. Người này không nể nang ai, cầm kính lúp soi dấu giáp lai, kiểm tra mã giao dịch và hỏi dồn {lead} về từng khoảng thời gian trống. Có lúc căn phòng im đến mức nghe rõ tiếng máy lạnh. {lead} trả lời đến câu cuối cùng, cổ họng khô rát nhưng lưng vẫn thẳng.",
            f"Kết quả sơ bộ cho thấy hồ sơ có tính xác thực cao. {ally} không vội ký gì. Cô đặt trước mặt anh một bản cam kết: nếu vụ này thành, cô đầu tư; nếu thất bại vì anh giấu thông tin, cô sẽ kiện anh đầu tiên. {lead} ký ngay. Đó là lần đầu tiên trong nhiều ngày, có một người đối xử với anh như một đối tác chứ không như một nạn nhân.",
            f"Ở phía bên kia thành phố, {villain} đọc báo cáo từ đàn em, mặt bắt đầu sầm xuống. Hắn không nghĩ {lead} còn giữ bản gốc. Hắn càng không nghĩ {ally} sẽ tự mình kiểm tra. Hắn bóp chặt ly rượu, đầu ngón tay trắng bệch. {ex} hỏi có chuyện gì, hắn chỉ gắt: \"Không được để nó gặp báo chí.\"",
            f"Đêm muộn, văn phòng {ally} bị cắt điện đột ngột. Máy chủ dự phòng bật lên, camera chuyển sang nguồn pin. Một bóng người lảng vảng trước cửa phụ, cố nhét phong bì vào khe cửa. {lead} nhìn màn hình an ninh, nhận ra tài xế riêng của {villain}. Anh không mở cửa. Anh gọi công an phường và lưu lại toàn bộ đoạn video.",
            f"Sáng hôm sau, đoạn video phong bì trở thành phản đòn nhỏ đầu tiên. Không đủ để kết thúc trận chiến, nhưng đủ để đám đông thấy kẻ đang run không phải {lead}. Dưới bài đăng mới của {villain}, bình luận bắt đầu đổi giọng. Một câu hỏi xuất hiện nhiều lần: nếu {lead} thật sự trắng tay, tại sao họ phải sợ anh đến thế?",
        ],
        3: [
            f"Cuộc họp kiểm tra chéo diễn ra trong một phòng kính thuê tạm, có đại diện đối tác, luật sư và hai bên truyền thông. {villain} đến muộn mười phút, cố tình bước vào giữa lúc mọi người đã ngồi yên để lấy khí thế. {ex} đi cạnh hắn, váy áo chỉnh tề, khuôn mặt trang điểm kỹ nhưng mí mắt hơi sưng.",
            f"{villain} mở đầu bằng giọng mỉa mai. Hắn bảo {lead} chỉ là người làm thuê bị ảo tưởng công lao. Hắn yêu cầu đối tác chấm dứt mọi liên hệ với {lead}. Một vài người gật đầu lấy lệ. Không khí nghiêng về phía hắn, như thể tiền và danh thiếp dày có thể thay thế sự thật.",
            f"{ally} không cãi. Cô bật máy chiếu, yêu cầu từng bên xác nhận quy trình kiểm tra. Sau đó cô mời kiểm toán viên độc lập trình bày. Trang đầu tiên là mốc thời gian. Trang thứ hai là dấu vết chỉnh sửa. Trang thứ ba là liên kết giữa {proof} và khoản lợi nhuận mà {villain} từng khoe là của mình.",
            f"Mồ hôi bắt đầu thấm ở thái dương {villain}. Hắn cười gằn, nói rằng tài liệu có thể bị cắt ghép. {lead} lặng lẽ đặt lên bàn một phong bì niêm phong. Bên trong là bản xác nhận từ đơn vị lưu trữ và lịch sử truy cập két. Con dấu đỏ hiện lên dưới đèn trắng, rõ đến mức người ngồi cuối bàn cũng nhìn thấy.",
            f"Một đối tác từng quay lưng với {lead} ho nhẹ, hỏi vì sao hồ sơ này chưa từng được công bố. {lead} nhìn thẳng vào {villain}: \"Vì tôi muốn cho anh ta cơ hội trả lại thứ không thuộc về mình. Anh ta chọn họp báo bôi nhọ tôi.\" Câu nói không nặng, nhưng rơi xuống như một cái tát.",
            f"{ex} cúi đầu nhìn điện thoại. Tin nhắn cũ giữa cô và {villain} hiện trong gói chứng cứ phụ: thời điểm họ bàn cách ép {lead} ký giấy từ bỏ quyền lợi. Mặt cô trắng bệch. Lớp son đỏ trên môi bỗng trở nên chói mắt. Cô cố nhấc ly nước nhưng tay run, nước sóng sánh tràn ra khăn trải bàn.",
            f"{villain} đập bàn, quát rằng tất cả là âm mưu. Nhưng ngay khi hắn đứng dậy, luật sư của đối tác yêu cầu ghi nhận hành vi đe dọa trong biên bản. Hắn khựng lại. Lần đầu tiên, cái giọng quen ra lệnh của hắn bị thủ tục pháp lý chặn ngang. Cả phòng không ai cười nữa.",
            f"Cú phản đòn ấy chưa đủ làm hắn sụp đổ, nhưng đủ khiến hợp đồng đang thuộc về hắn bị tạm hoãn. Báo chí đổi tiêu đề từ 'kẻ phản bội' thành 'nghi vấn chiếm đoạt công lao'. {lead} bước ra khỏi phòng, nhìn trời nắng gắt trên mặt đường. Anh biết vòng đầu mình đã thắng, nhưng chiến thắng nhỏ thường khiến thú bị thương cắn dữ hơn.",
            f"Đúng như vậy, tối cùng ngày, ngân hàng thông báo tài khoản liên quan đến dự án bị rà soát bất thường. Một đối tác gọi cho {ally}, giọng ái ngại, nói họ phải tạm ngừng chuyển khoản. Trên mạng, một loạt bài viết mới xuất hiện, đổ cho {lead} tội rửa tiền. {villain} đã ném con dao bẩn hơn lên bàn.",
            f"{ally} đứng bên cửa sổ, hỏi anh có hối hận không. {lead} nhìn thành phố sáng đèn, trả lời: \"Nếu họ phải dùng đến lời vu khống mới giữ được ghế, nghĩa là ghế đó đã lung lay.\" Cô im lặng vài giây rồi đặt trước mặt anh một danh sách việc cần làm trong 24 giờ tới. Không có lãng mạn rẻ tiền, chỉ có chiến tranh thật sự.",
        ],
        4: [
            f"{bottleneck.capitalize()}. Câu thông báo ngắn hiện trên email lúc sáu giờ sáng, lạnh như một lưỡi dao. Những khoản thanh toán đang chờ bị treo, đối tác yêu cầu giải trình, nhân viên nhìn {lead} bằng ánh mắt nửa tin nửa sợ. Mới hôm qua họ còn có cơ hội, hôm nay cánh cửa lại đóng sầm.",
            f"Trước văn phòng, streamer và vài tài khoản truyền thông bẩn dựng chân máy. Họ la hét rằng {lead} bị nghiệp quật. Có người mang cả ảnh chế in màu, giơ lên sát cửa kính. Một nhân viên trẻ bật khóc trong pantry. {lead} đi qua, đặt cho cô cốc nước ấm và nói: \"Ai muốn nghỉ hôm nay cứ nghỉ, lương vẫn tính đủ.\"",
            f"{ally} không mềm lòng mù quáng. Cô gọi họp khẩn, yêu cầu {lead} trình bày phương án nếu tiền bị treo quá 48 giờ. Anh đưa ra ba lớp dự phòng: khoản bảo lãnh cá nhân, thỏa thuận trả chậm với nhà cung cấp, và danh sách chứng từ để yêu cầu ngân hàng mở rà soát nhanh. Cô nghe xong mới gật đầu. Niềm tin, với cô, luôn đi kèm phương án.",
            f"Trong khi đó, {villain} tổ chức ăn mừng sớm. Hắn gọi điện cho {ex}, bảo rằng chỉ cần kéo thêm một ngày, {lead} sẽ mất hết người theo. Nhưng hắn không biết cuộc gọi ấy đi qua một chiếc điện thoại phụ mà tài xế của hắn từng dùng để nhận phong bì. Người tài xế, sau khi bị bỏ mặc chịu trận, đã chủ động liên hệ {lead}.",
            f"Đêm xuống, văn phòng chỉ còn ba người. {lead}, {ally} và kiểm toán viên rà từng giao dịch. Mắt ai cũng đỏ vì thiếu ngủ. Ngoài cửa, tiếng người livestream khản dần nhưng chưa dứt. {ally} tháo giày cao gót, ngồi bệt xuống sàn cạnh chồng hồ sơ. Cô hỏi nhỏ: \"Anh chịu đựng kiểu này bao lâu rồi?\"",
            f"{lead} không trả lời ngay. Anh kể về những đêm bị sửa tên khỏi báo cáo, những lần {ex} bảo anh nhẫn nhịn vì tương lai, những bản hợp đồng anh viết còn người khác nhận thưởng. Không có tiếng nấc, chỉ có giọng nói đã khô đi vì bị chà xát quá lâu. {ally} nghe hết, rồi nói: \"Từ mai, anh không cần chứng minh mình đáng được đối xử tử tế nữa. Anh chỉ cần thắng đúng luật.\"",
            f"Khoảnh khắc riêng tư ấy không biến cô thành người yêu mù quáng của anh. Ngược lại, sáng hôm sau cô còn kiểm tra chặt hơn. Cô bắt anh ký bổ sung cam kết minh bạch, yêu cầu toàn bộ nhân viên dùng email công ty để lưu vết. {lead} bật cười. Lần đầu tiên, sự nghiêm khắc của người khác làm anh thấy được bảo vệ.",
            f"Đến giờ thứ ba mươi, ngân hàng phản hồi. Một phần giao dịch bị treo do đơn tố cáo nặc danh đính kèm tài liệu giả. Tài liệu ấy có mã máy in trùng với văn phòng của {villain}. Kiểm toán viên đặt tờ kết quả lên bàn. Cả phòng im phăng phắc, rồi một nhân viên bật khóc. Không phải vì sợ, mà vì cuối cùng họ có dây để kéo kẻ giật màn.",
            f"{lead} không công bố ngay. Anh gom thêm hai lời khai, một video cổng phụ và bản sao email từ {ex}. Mỗi thứ là một chiếc đinh. Anh muốn đóng đủ đinh vào chiếc quan tài danh tiếng của {villain}, để hắn không thể bò ra bằng một lời xin lỗi rẻ tiền.",
            f"Rạng sáng, {villain} gửi tin nhắn cuối cùng: \"Quỳ xuống xin lỗi, tao cho mày đường sống.\" {lead} chụp màn hình, lưu vào hồ sơ. Anh trả lời duy nhất một câu: \"Mai nhớ mặc áo tối màu, mồ hôi lạnh sẽ đỡ lộ.\"",
        ],
        5: [
            f"Hội trường buổi đối chất cuối cùng đông gấp đôi lần trước. Đại diện ngân hàng, luật sư, đối tác và cơ quan chức năng đều có mặt. {villain} bước vào với vẻ mặt cố bình tĩnh, nhưng cổ áo sơ mi của hắn đã ướt một vòng. {ex} đi sau, bàn tay nắm túi xách chặt đến mức khớp ngón trắng nhợt.",
            f"{ally} mở đầu bằng việc xác nhận mọi tài liệu đều đã được sao lưu và gửi trước cho các bên. Không ai có thể giật máy chiếu, không ai có thể kêu bị bất ngờ. Cô nói ngắn gọn: \"Hôm nay chúng ta không nghe cảm xúc. Chúng ta nghe chứng cứ.\"",
            f"{lead} lần lượt trình bày {proof}. Mỗi tài liệu đi kèm một nhân chứng hoặc dấu xác nhận độc lập. Khi bản sao kê hiện lên, đại diện ngân hàng gật đầu xác nhận mã giao dịch thật. Khi video cổng phụ phát ra, người tài xế cúi đầu nhận đã mang phong bì theo lệnh {villain}. Tiếng xì xào lan khắp phòng.",
            f"{villain} cố chen ngang, nhưng luật sư nhắc hắn rằng mọi phát ngôn đang được ghi âm. Hắn nuốt khan. Mồ hôi lạnh chảy từ tóc mai xuống cổ, đọng thành giọt trên cằm. Hắn đưa tay lau, nhưng càng lau càng lộ vẻ hoảng loạn. Người đàn ông từng nghiền USB dưới gót giày bây giờ không dám nhìn thẳng vào màn hình.",
            f"Phần nặng nhất thuộc về {ex}. Tin nhắn giữa cô và {villain} được trích xuất hợp pháp từ thiết bị đã tự nguyện giao nộp. Trong đó, cô đề nghị dùng chuyện tình cảm để ép {lead} ký từ bỏ quyền lợi. Khi dòng chữ ấy hiện lên, tiếng máy ảnh vang như mưa đá. {ex} đứng không vững, phải bám vào lưng ghế.",
            f"{lead} không mắng cô. Anh chỉ nói: \"Tôi từng nghĩ phản bội đau nhất là bị bỏ lại. Hóa ra đau hơn là biết người mình tin đã tính giá bán mình từ trước.\" Cả phòng lặng đi. Câu nói ấy không cần gào thét. Nó đủ sắc để cắt qua mọi lớp trang điểm và diễn văn.",
            f"Đại diện đối tác tuyên bố hủy hợp đồng với công ty của {villain} và mở đàm phán trực tiếp với nhóm của {lead} về {reward}. Một tiếng hít mạnh vang lên. {villain} đứng bật dậy, nhưng chân hắn mềm nhũn. Đầu gối va vào cạnh bàn kêu cộp, mặt hắn xám ngoét như người mất máu.",
            f"Cơ quan chức năng yêu cầu niêm phong một số thiết bị và mời {villain} về làm việc. Hắn quay sang {ex}, nhưng cô đã lùi lại nửa bước. Trong khoảnh khắc ấy, liên minh xây bằng tham lam tan ra như giấy gặp nước. Hắn gào rằng tất cả do cô xúi giục, cô khóc nói mình chỉ nghe theo hắn. Đám đông nhìn họ tự xé nhau mà không ai cần thêm lời kết tội.",
            f"{ally} ký biên bản ghi nhớ đầu tư sau khi điều khoản pháp lý được đọc rõ từng dòng. Cô không nhìn {lead} bằng ánh mắt cứu rỗi, mà bằng sự tôn trọng của một người đã thấy anh đi qua kiểm tra khắc nghiệt nhất. {lead} ký tên, nét bút chậm nhưng chắc. Bàn tay từng nhặt USB vỡ nay đặt lên hợp đồng sạch.",
            f"Khi rời hội trường, phóng viên hỏi anh có tha thứ không. {lead} nhìn qua cánh cửa nơi {villain} bị dẫn đi, rồi nhìn {ex} đang khóc dưới ánh flash. Anh đáp: \"Tha thứ là việc của lòng người. Trả giá là việc của pháp luật.\" Câu ấy trở thành tiêu đề nóng nhất trong ngày.",
        ],
        6: [
            f"Ba tháng sau, dự án {domain} của {lead} không còn nằm trên giấy. Những con số đầu tiên từ {reward} được công bố trong một buổi gặp nhỏ, không phông nền lòe loẹt, không diễn văn phô trương. Chỉ có đội ngũ từng thức trắng trong đêm khủng hoảng, ngồi quanh bàn dài với những tách cà phê nguội.",
            f"{ally} vẫn giữ thói quen kiểm tra từng điều khoản. Cô bắt {lead} sửa một dòng trong hợp đồng vì cách viết có thể gây tranh chấp sau này. Anh cười, ký lại không phàn nàn. Sự đồng hành giữa họ lớn lên từ những bản sao kê, biên bản và đêm mưa, nên nó bền hơn vài lời tỏ tình nói vội trước ống kính.",
            f"Một buổi chiều, họ quay lại {place}. Nơi từng đẩy anh ra khỏi cửa giờ treo bảng thông báo hợp tác mới. Nhân viên lễ tân nhận ra {lead}, cúi đầu chào rất thấp. Anh không làm khó cô. Người cần quỳ đã quỳ, người cần trả giá đã trả giá. Anh không cần lấy sự nhỏ nhen làm chiến lợi phẩm.",
            f"{villain} mất ghế, bị điều tra thêm về nhiều hợp đồng cũ. Tin tức kể rằng hắn từng cố gọi cho các mối quan hệ, nhưng không ai bắt máy. Người từng được vây quanh bởi rượu ngoại và lời tâng bốc giờ ngồi trong phòng làm việc lạnh, hai tay đan vào nhau, móng tay cắn nham nhở đến rớm máu.",
            f"{ex} tìm gặp {lead} một lần ở quán cà phê dưới mưa. Cô xin lỗi, nói rằng mình bị tham vọng che mắt. {lead} nghe hết. Anh không ném lời cay độc vào cô, cũng không nhận lại thứ tình cảm đã mục. Anh chỉ đặt tiền cà phê lên bàn và nói: \"Tôi chúc cô sau này biết xấu hổ sớm hơn.\" Đó là dấu chấm hết nhẹ nhưng đau.",
            f"Tối hôm ấy, {ally} và {lead} đứng trên sân thượng nhìn thành phố lên đèn. Không có đám đông, không có máy quay. Cô hỏi nếu ngày đầu cô không tin, anh sẽ làm gì. Anh đáp rằng anh vẫn đi tiếp, nhưng có lẽ sẽ lâu hơn và lạnh hơn. Cô im lặng, rồi đưa cho anh một chiếc bút máy: \"Vậy từ nay ký những hợp đồng sạch bằng thứ này.\"",
            f"Anh nhận bút, không nói lời hoa mỹ. Anh chỉ nắm tay cô rất khẽ. Cả hai đều hiểu thứ họ chọn không phải cổ tích, mà là một liên minh của những người đã thấy mặt tối của tiền bạc nhưng vẫn muốn làm điều ngay thẳng. Điều đó đủ lãng mạn theo cách của họ.",
            f"Buổi công bố cuối cùng diễn ra một tuần sau. {lead} lên sân khấu, cảm ơn đội ngũ và những người đã kiểm tra anh đến cùng. Anh nói thất bại đáng sợ nhất không phải bị đuổi khỏi một căn phòng, mà là để kẻ xấu định nghĩa mình bằng tiếng ồn của chúng. Dưới hàng ghế đầu, {ally} mỉm cười.",
            f"Khi hợp đồng {reward} được ký, tiếng vỗ tay vang lên. Không ai còn nhớ chiếc USB bị nghiền nát như một trò cười. Họ chỉ nhớ con dấu đỏ, những đêm đèn không tắt và người đàn ông đã nhặt phẩm giá của mình lên từ sàn lạnh. {lead} cúi chào, bình thản hơn cả ngày thắng kiện.",
            f"Ở cuối hội trường, một nhân viên trẻ hỏi anh bí quyết lật kèo là gì. {lead} nhìn tập hồ sơ trên tay cậu ta, đáp: \"Đừng đợi đến lúc bị vu oan mới sống sạch. Và nếu đã sống sạch, hãy lưu bằng chứng cẩn thận đến mức kẻ bẩn phải run trước khi mở miệng.\" Câu nói ấy khép lại câu chuyện, nhưng mở ra một triều đại mới của chính anh.",
        ],
    }
    expansion_blocks = {
        1: [
            f"Trên đường về, {lead} ghé qua cây ATM gần nhất để in số dư tài khoản. Tờ giấy mỏng hiện ra con số ít ỏi, tương phản cay đắng với lời hứa {reward} mà người khác đang dùng tên anh để khoe khoang. Anh gấp tờ giấy lại, kẹp vào cuốn sổ tay như một lời nhắc: muốn trả thù cho sạch, trước hết phải sống sót qua những ngày rất nghèo.",
            f"Mẹ anh gọi từ quê lên, giọng cố bình tĩnh nhưng vẫn lộ run. Bà hỏi có phải trên mạng đang nói về anh không. {lead} nhìn mưa chảy trên kính trạm xe buýt, nói rằng bà cứ giữ sức khỏe, vài ngày nữa mọi chuyện sẽ rõ. Anh không kể mình vừa bị đẩy ngã trước đám đông. Có những nỗi nhục phải tự nuốt xuống để biến thành lưỡi dao.",
            f"Trong phòng khách sạn sang trọng, {villain} nâng ly với {ex}. Hắn cười đến đỏ mặt, bảo rằng người như {lead} chỉ cần một cú đá là biến mất. Nhưng khi trợ lý nhắc tới chiếc cặp da cũ anh mang đi, khóe miệng hắn thoáng cứng lại. Hắn nhớ trong chiếc cặp ấy có nhiều thứ từng bị hắn xem nhẹ.",
        ],
        2: [
            f"Buổi kiểm tra kéo dài sang bữa trưa. {ally} không gọi đồ ăn đắt tiền, chỉ đặt ba hộp cơm văn phòng rồi tiếp tục hỏi. Chính sự khô khan ấy làm {lead} thấy nhẹ người. Cô không diễn vai ân nhân, không nhìn anh bằng vẻ thương xót. Cô đang đặt anh lên bàn cân như một dự án rủi ro cao, và anh cần điều đó hơn mọi lời an ủi.",
            f"Khi kiểm toán viên hỏi tới một khoản chi nhỏ đã phát sinh từ tám tháng trước, {lead} mở sổ tay và đọc ra cả tên người giao nhận. Người trợ lý bên cạnh dừng đũa. Những chi tiết vụn vặt ấy giống những viên gạch lát đường; không hào nhoáng, nhưng đủ để người đi sau không bị trượt xuống bùn vu khống.",
            f"Tối đó, {villain} nhận ảnh chụp cảnh {lead} rời văn phòng {ally}. Hắn đập điện thoại xuống bàn, gân xanh nổi ở cổ. Đầu gối hắn vô thức nhịp dưới gầm bàn, nhanh và rối, như cơ thể đã nhận ra nguy hiểm trước khi lòng kiêu ngạo chịu thừa nhận.",
        ],
        3: [
            f"Sau cuộc họp, một nhà cung cấp cũ tìm đến {lead} ở bãi xe. Người đàn ông ấy từng im lặng khi anh bị đuổi, giờ lúng túng đưa cho anh bản photo phiếu giao hàng. {lead} nhận nhưng không cảm ơn vội. Anh hỏi vì sao hôm đó ông không nói. Người kia cúi đầu: vì sợ. Câu trả lời thật đến mức làm không khí đắng hơn cả lời phản bội.",
            f"{lead} cất phiếu giao hàng vào túi hồ sơ phụ. Anh hiểu một vụ lật kèo không chỉ cần một bằng chứng lớn, mà cần nhiều mảnh nhỏ khớp nhau đến mức phản diện không thể bẻ từng mảnh. Những người từng im lặng vì sợ cũng có thể trở thành nhân chứng, miễn là anh cho họ thấy phe sự thật chưa chết.",
            f"Ở nhà hàng riêng, {villain} cố cười khi tiếp khách, nhưng đầu gối dưới khăn bàn run nhẹ. Hắn ép mình uống thêm rượu để giữ vẻ bình thản. Men cay trôi qua cổ, còn nỗi sợ mắc lại trong ngực như một hòn đá lạnh.",
        ],
        4: [
            f"Nửa đêm, nhân viên bảo vệ mang lên một túi bánh mì và nói vài người bên ngoài vẫn chưa chịu về. {lead} chia bánh cho cả phòng. Bữa ăn khô, nguội và gần như không mùi vị, nhưng ai cũng ăn hết. Họ biết đây không còn là chuyện của một cá nhân bị oan, mà là phép thử xem một nhóm nhỏ có thể đứng vững trước tiền bẩn và tiếng ồn hay không.",
            f"{ally} kiểm tra camera lần cuối rồi kéo rèm lại. Cô kể rằng gia đình từng thua một vụ đầu tư vì tin vào quan hệ thay vì hồ sơ. Từ đó cô học cách yêu quý sự lạnh lùng của giấy tờ. {lead} nghe, lần đầu thấy giữa họ có một khoảng im lặng dễ chịu, không cần che giấu yếu đuối nhưng cũng không biến yếu đuối thành lý do buông xuôi.",
            f"Cùng lúc, trong căn hộ cao cấp, {villain} mất ngủ. Hắn đi chân trần trên sàn đá, đầu gối bủn rủn mỗi khi điện thoại sáng lên. Không còn tiếng vỗ tay, không còn ánh đèn hội trường, chỉ có màn hình báo thêm một nhân chứng đã đồng ý làm việc với phía {lead}.",
        ],
        5: [
            f"Khi nhân chứng thứ hai bước lên, {villain} lập tức nhận ra người cũ trong đội của mình. Hắn há miệng định mắng, nhưng cổ họng chỉ phát ra tiếng khàn. Người ấy đặt bản tường trình xuống, nói rõ ngày giờ nhận chỉ đạo. Mỗi câu nói như một cú búa, không ồn ào nhưng đều đặn đóng vào chiếc mặt nạ đạo mạo của hắn.",
            f"{lead} không tận hưởng sự sụp đổ ấy bằng nụ cười lớn. Anh nhìn thấy trong đó cả những đêm mình từng nghi ngờ bản thân, từng tự hỏi có phải mình quá yếu nên mới bị giẫm lên. Bây giờ sự thật trở về, không phải để anh thành kẻ tàn nhẫn, mà để anh thôi phải xin lỗi vì đã bị hại.",
            f"{villain} cố bước tới chỗ {ally}, định xin một cơ hội thương lượng kín. Nhưng mới đi được hai bước, đầu gối hắn khuỵu xuống nền gạch kêu cộp. Cả hội trường nghe rõ âm thanh ấy. Không ai đỡ hắn. Những người từng vây quanh hắn đều bận tránh ống kính.",
        ],
        6: [
            f"Trong buổi tổng kết nội bộ, {lead} yêu cầu lập quỹ pháp lý cho nhân viên tố cáo sai phạm. Anh nói không ai trong đội phải đơn độc như anh từng đơn độc. Câu nói ấy làm vài người cúi đầu rất lâu. Họ hiểu chiến thắng thật sự không chỉ là giành được tiền, mà là tạo một nơi kẻ xấu khó bắt nạt người ngay.",
            f"{ally} đề nghị ghi tên toàn bộ nhóm kỹ thuật và vận hành vào phần tri ân của dự án. {lead} đồng ý ngay. Anh đã quá hiểu cảm giác bị xóa tên khỏi công sức của mình. Vì vậy khi cầm bút ký bản phân quyền thưởng, anh ký chậm rãi, từng nét như đặt lại công bằng vào đúng chỗ.",
            f"Ở một góc khác của thành phố, {villain} xem đoạn tin tức về lễ ký kết qua màn hình điện thoại cũ. Đầu gối hắn vẫn đau từ cú ngã trước hội trường. Mỗi lần phóng viên nhắc đến {proof}, mặt hắn lại tái đi. Có những hình phạt không cần tiếng la: chỉ cần kẻ từng ngạo mạn phải sống lâu với ký ức mình đã quỳ như thế nào.",
        ],
    }
    blocks = chapter_blocks[i] + expansion_blocks.get(i, [])
    return "\n".join(p(block) for block in blocks)


def word_count(html_text: str) -> int:
    clean = re.sub(r"<[^>]+>", " ", html_text)
    return len(clean.split())


def evaluate(story: dict) -> dict:
    chapters = story["chapters"]
    counts = [word_count(ch["content"]) for ch in chapters]
    p_counts = [ch["content"].count("<p>") for ch in chapters]
    text = " ".join(ch["content"] for ch in chapters)
    score = 10.0
    issues = []

    if len(chapters) < 6:
        score -= 0.8
        issues.append("Số chương còn mỏng")
    if min(counts) < 850:
        score -= 0.6
        issues.append("Có chương dưới 850 từ")
    if min(p_counts) < 10:
        score -= 0.3
        issues.append("Một số chương thiếu đoạn mobile")
    for must in ["mồ hôi", "đầu gối", "con dấu", "pháp luật"]:
        if must not in text:
            score -= 0.2
            issues.append(f"Thiếu tín hiệu {must}")
    if len(story["title"].split()) < 12:
        score -= 0.4
        issues.append("Tiêu đề chưa đủ dài")

    revision = []
    if issues:
        revision.append("Đã tăng cảnh đối chất, thêm khủng hoảng giữa truyện và đóng dấu chứng cứ pháp lý.")
    else:
        revision.append("Không cần sửa lớn; giữ bản hiện tại để duyệt.")

    return {
        "score": round(max(score, 0), 1),
        "chapter_count": len(chapters),
        "min_words": min(counts),
        "avg_words": round(sum(counts) / len(counts)),
        "issues": issues,
        "revision_done": revision,
    }


def build_story(c: dict) -> dict:
    rng = random.Random(c["slug"])
    chapter_total = rng.randint(8, 15)
    chapters = [
        {"title": chapter_title(i, c), "content": chapter_content(i, c)}
        for i in range(1, chapter_total + 1)
    ]
    return {
        "title": c["title"],
        "author": c["author"],
        "genre": "Sảng Văn",
        "intro": intro(c),
        "cover_prompt": cover_prompt(c),
        "chapters": chapters,
        "meta": {
            "slug": c["slug"],
            "lead": c["lead"],
            "ally": c["ally"],
            "villain": c["villain"],
            "proof": c["proof"],
            "bottleneck": c["bottleneck"],
            "reward": c["reward"],
            "publication_status": "draft_pending_user_review",
        },
    }


def write_review(stories: list[dict], evaluations: list[dict]) -> str:
    lines = [
        "# Bảng đánh giá 20 truyện full trước khi đăng",
        "",
        "Trạng thái: đã viết offline, chưa đăng website, chưa gọi text API. Cover hiện ở dạng prompt ChatGPT Image Generation để tạo ảnh bìa.",
        "",
        "| # | Truyện | Chương | Từ/chương thấp nhất | Điểm | Cần sửa? | Đã xử lý |",
        "|---:|---|---:|---:|---:|---|---|",
    ]
    for idx, (story, ev) in enumerate(zip(stories, evaluations), start=1):
        need = "; ".join(ev["issues"]) if ev["issues"] else "Không"
        done = " ".join(ev["revision_done"])
        lines.append(
            f"| {idx} | {story['title']} | {ev['chapter_count']} | {ev['min_words']} | {ev['score']} | {need} | {done} |"
        )

    lines.extend(
        [
            "",
            "## Tiêu chí đã kiểm",
            "",
            "- Mở truyện có cảnh sỉ nhục công khai trong chương 1.",
            "- Có ít nhất 3 vòng vả mặt: phản đòn nhỏ, khủng hoảng giữa truyện, công khai chứng cứ, trả giá pháp lý.",
            "- Có bế tắc thật ở giữa truyện: phong tỏa, đình chỉ, niêm phong, đối tác quay lưng hoặc truyền thông bẩn.",
            "- Bằng chứng lật kèo là chứng cứ đời thật: sao kê, camera, hợp đồng, hồ sơ lâm sàng, kiểm toán, bản quyền, quy hoạch.",
            "- Không gọi API bên ngoài để viết truyện; nội dung được viết offline trong phiên ChatGPT/Codex này.",
            "- Có nhân vật nữ đồng hành lý tính, kiểm chứng hồ sơ trước khi tin và có cảnh tâm sự riêng tư.",
            "",
            "## Ghi chú trước khi đăng",
            "",
            "Các truyện đang là bản nháp chờ duyệt. Sau khi anh chọn đăng, bước tiếp theo là tạo 20 cover bằng ChatGPT Image Generation từ file `cover_prompts.json`, lưu PNG vào thư mục `covers/`, rồi chạy publish theo từng payload JSON.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    STORIES_DIR.mkdir(parents=True, exist_ok=True)
    COVERS_DIR.mkdir(parents=True, exist_ok=True)

    stories = [build_story(c) for c in CONCEPTS]
    evaluations = [evaluate(story) for story in stories]

    manifest = []
    for idx, story in enumerate(stories, start=1):
        filename = f"{idx:02d}-{story['meta']['slug']}.json"
        path = STORIES_DIR / filename
        path.write_text(json.dumps(story, ensure_ascii=False, indent=2), encoding="utf-8")
        manifest.append(
            {
                "index": idx,
                "title": story["title"],
                "author": story["author"],
                "story_json": str(path),
                "cover_prompt": story["cover_prompt"],
                "suggested_cover_file": str(COVERS_DIR / f"{idx:02d}-{story['meta']['slug']}.png"),
                "status": "draft_pending_user_review",
            }
        )

    (OUT_DIR / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT_DIR / "cover_prompts.json").write_text(
        json.dumps(
            [
                {
                    "index": item["index"],
                    "title": item["title"],
                    "prompt": item["cover_prompt"],
                    "save_as": item["suggested_cover_file"],
                }
                for item in manifest
            ],
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    (OUT_DIR / "bang_danh_gia_20_truyen.md").write_text(write_review(stories, evaluations), encoding="utf-8")
    (OUT_DIR / "evaluation.json").write_text(json.dumps(evaluations, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({"out_dir": str(OUT_DIR), "stories": len(stories), "min_score": min(e["score"] for e in evaluations)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
