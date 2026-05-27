import html
import json
from pathlib import Path


OUT_DIR = Path("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch")


STORIES = [
    {
        "id": 3724,
        "title": "Kỹ Sư Vắc Xin Bị Sa Thải Vì Không Gian Lận, Bản Quyền Vắc Xin Vả Sập Tập Đoàn Phản Bội",
        "lead": "Phạm Minh Khoa",
        "ally": "bác sĩ kiểm định Nguyễn An Nhiên",
        "villain": "Viện trưởng Lê Trọng Đạt",
        "setting": "khu nghiên cứu vắc xin Hòa Lạc",
        "industry": "vắc xin cúm gia cầm",
        "object": "lô mẫu VX-H5N8",
        "proof": "sổ lạnh kho mẫu, biên bản HPLC và hồ sơ thử nghiệm đối chứng",
        "mid_loss": "một lô mẫu bị niêm phong sai nhiệt độ khiến anh phải tự chứng minh trong 18 giờ",
        "arena": "phiên thẩm định của Hội đồng Đạo đức Y sinh",
        "theme": "không gian lận dữ liệu y sinh dù mất chức",
    },
    {
        "id": 3743,
        "title": "Nữ Hoàng Trà Sen Tây Hồ: Bị Đuổi Khỏi Gia Tộc, Cô Xây Đế Chế Trà Nghìn Tỷ",
        "lead": "Lê Minh Nguyệt",
        "ally": "nghệ nhân già Từ Bảo",
        "villain": "anh trai Lê Minh Hùng",
        "setting": "đầm sen Quảng Bá lúc rạng sáng",
        "industry": "trà sen Tây Hồ",
        "object": "mẻ trà ướp bảy đêm của gia tộc",
        "proof": "sổ ướp sen, mẫu hương còn dấu phấn sen và lời chứng của người hái sen",
        "mid_loss": "quầy trà mới bị phá trong đêm mưa, toàn bộ tiền vốn gần như mất sạch",
        "arena": "đêm đấu trà tại phủ Tây Hồ",
        "theme": "giữ nghề bằng mùi hương thật thay vì giấy tờ giả",
    },
    {
        "id": 3755,
        "title": "Bác Sĩ Thẩm Mỹ Sài Gòn: Bị Vu Oan Phẫu Thuật Hỏng, Tôi Lật Mặt Cả Bệnh Viện",
        "lead": "Ngô Hoàng Khải",
        "ally": "điều dưỡng trưởng Trần Ngọc Hà",
        "villain": "bác sĩ Lê Văn Nam",
        "setting": "phòng mổ thẩm mỹ quận 3",
        "industry": "phẫu thuật tái tạo",
        "object": "ca chỉnh hình mũi cho bệnh nhân VIP",
        "proof": "phiếu lĩnh thuốc gây mê, camera hành lang và mã niêm phong tủ thuốc",
        "mid_loss": "bệnh nhân ngưng thở 47 giây khiến giấy phép của Khải bị treo ngay trong đêm",
        "arena": "buổi họp chuyên môn của Sở Y tế TP.HCM",
        "theme": "đạo đức nghề y thắng trò ganh tị trong phòng mổ",
    },
    {
        "id": 3767,
        "title": "Ông Trùm Logistics Tân Cảng: Bị Phản Bội Mất Container Nghìn Tỷ, Tôi Thâu Tóm Ngược",
        "lead": "Phạm Gia Hưng",
        "ally": "kiểm toán viên cảng Trương Khánh Linh",
        "villain": "Trần Thế Hải",
        "setting": "bãi container Cát Lái lúc 3 giờ sáng",
        "industry": "logistics cảng biển",
        "object": "1.000 container linh kiện y tế",
        "proof": "lệnh nâng hạ, nhật ký seal container và cân tải tại cổng E",
        "mid_loss": "đối thủ khóa luồng thông quan và ép anh bồi thường 300 tỷ trong 12 giờ",
        "arena": "phòng điều độ Tân Cảng trước đoàn khách hàng Nhật",
        "theme": "lật ngược bằng vận hành thật, không nhờ cứu viện từ trên trời rơi xuống",
    },
    {
        "id": 3769,
        "title": "Thợ Nuôi Trai Bị Cướp Ngọc Đen Đuổi Khỏi Vịnh, Trở Lại Lật Kèo Đoạt Lại Tập Đoàn Ngọc Trai Nghìn Tỷ",
        "lead": "Trịnh Hoàng Lâm",
        "ally": "chuyên gia hải dương học Mai Nguyệt",
        "villain": "Huỳnh Gia Kiệt",
        "setting": "lồng trai ngoài vịnh Vân Đồn",
        "industry": "nuôi trai ngọc đen",
        "object": "dòng trai mẹ Black Pearl VĐ-09",
        "proof": "sổ lặn, mã đánh dấu vỏ trai và kết quả phổ khoáng nước biển",
        "mid_loss": "bão đêm làm gãy một bè trai, Lâm phải lặn xuống tự cứu đàn giống cuối",
        "arena": "triển lãm ngọc trai quốc tế Hạ Long",
        "theme": "nghề biển và bằng chứng sinh học thay cho template Đông Tây y",
    },
    {
        "id": 3789,
        "title": "Kiến Trúc Sư Phố Cổ Hà Nội: Bị Cướp Bản Vẽ Di Sản, Tôi Cứu Cả Khu Phố",
        "lead": "Đỗ Minh Tuấn",
        "ally": "nhà nghiên cứu di sản Nguyễn Thu Ngọc",
        "villain": "đại gia địa ốc Nguyễn Minh Hải",
        "setting": "ngõ cổ Hàng Bạc trong mưa đêm",
        "industry": "bảo tồn kiến trúc phố cổ",
        "object": "bản vẽ gia cố căn nhà 87 Mã Mây",
        "proof": "hồ sơ lưu trữ Pháp, vết mực than chì và mô hình chịu lực bằng gỗ lim",
        "mid_loss": "một mảng tường cổ sập ngay trước mặt dân phố, khiến Tuấn tưởng mình đã cứu muộn",
        "arena": "cuộc họp cư dân phố cổ tại đình Kim Ngân",
        "theme": "đối đầu bằng chuyên môn và cộng đồng, không gọi lực lượng Deus ex machina",
    },
    {
        "id": 3801,
        "title": "Vua Lúa Gạo Đồng Tháp: Nông Dân Bị Ép Giá, Tôi Xây Đế Chế Gạo Xuất Khẩu",
        "lead": "Võ Thanh Tùng",
        "ally": "kỹ sư giống lúa Nguyễn Cẩm Tú",
        "villain": "thương lái Huỳnh Đạt",
        "setting": "cánh đồng Tháp Mười mùa nước rút",
        "industry": "gạo thơm Đồng Tháp",
        "object": "giống lúa ST25 cải tiến trên 40 hecta",
        "proof": "phiếu cân, mẫu gạo kiểm nghiệm và hợp đồng ép giá có chữ ký tay",
        "mid_loss": "kho lúa bị rút ẩm sai cách làm mốc ba tấn hàng đầu tiên",
        "arena": "ngày mở kho xuất khẩu tại cảng Mỹ Thới",
        "theme": "nông dân thắng bằng hợp tác xã và chất lượng thật",
    },
    {
        "id": 3813,
        "title": "Thần Đồng Piano Nhạc Viện: Bị Cấm Biểu Diễn, Tôi Chấn Động Chopin Competition",
        "lead": "Lâm Hoàng Phúc",
        "ally": "nghệ sĩ đệm đàn Trần Diệu Linh",
        "villain": "con trai giám đốc Nguyễn Thế Anh",
        "setting": "phòng tập cũ của Nhạc viện Hà Nội",
        "industry": "piano cổ điển",
        "object": "bản nocturne viết trong ba năm",
        "proof": "bản thảo có vết tẩy, đoạn thu âm luyện tập và lời chứng của thợ lên dây đàn",
        "mid_loss": "Phúc mất vé bay Warsaw vì bị tố đạo nhạc ngay trước vòng loại",
        "arena": "đêm chung kết Chopin Competition tại Warsaw",
        "theme": "cầu nối cảm xúc từ cơn giông đến sân khấu quốc tế",
    },
    {
        "id": 3825,
        "title": "Chúa Đảo Resort Phú Quốc: Bị Đuổi Khỏi Resort Mình Xây, Tôi Mua Cả Hòn Đảo",
        "lead": "Trịnh Gia Bảo",
        "ally": "chuyên gia môi trường Lê An Vy",
        "villain": "nhà đầu tư Bernard Dupont",
        "setting": "Bãi Sao Phú Quốc lúc thủy triều xuống",
        "industry": "resort sinh thái",
        "object": "khu nghỉ dưỡng bảo tồn san hô Nam Đảo",
        "proof": "báo cáo tác động môi trường, ảnh lặn rạn san hô và hợp đồng chuyển nhượng lén",
        "mid_loss": "một rạn san hô bị bùn xây dựng phủ trắng khiến Bảo phải dừng khai trương",
        "arena": "lễ trao chứng nhận du lịch xanh ASEAN",
        "theme": "phản diện không lộ quá sớm, bị buộc tự thú bởi hậu quả môi trường",
    },
    {
        "id": 3837,
        "title": "Đạo Diễn Phim Trường Cần Giờ: Bị Cướp Kịch Bản Oscar, Tôi Quay Phim Chấn Động Cannes",
        "lead": "Lý Quốc Anh",
        "ally": "nhà dựng phim Phạm Yến Chi",
        "villain": "nhà sản xuất Trần Thế Sơn",
        "setting": "rừng đước Cần Giờ lúc sương triều dâng",
        "industry": "điện ảnh độc lập",
        "object": "kịch bản phim Rừng Đước Không Ngủ",
        "proof": "bản storyboard vẽ tay, file dựng thô và lời chứng của diễn viên quần chúng",
        "mid_loss": "ổ cứng hậu kỳ bị phá, đoàn phim phải quay lại cảnh cuối trong đêm nước lớn",
        "arena": "buổi chiếu thử kín trước hội đồng Cannes",
        "theme": "đánh bại bằng nghệ thuật và nhân chứng nghề, không kết bằng bắt sân bay",
    },
    {
        "id": 3849,
        "title": "Vua Sầu Riêng Đắk Nông: Bị Đốt Vườn Nghìn Tỷ, Tôi Trồng Lại Từ Tro Tàn",
        "lead": "Y Ksor Thành",
        "ally": "kỹ sư nông nghiệp Hồng Vân",
        "villain": "địa chủ Đỗ Danh Nam",
        "setting": "buôn Êđê bên triền bazan Đắk Song",
        "industry": "sầu riêng Musang King",
        "object": "vườn sầu riêng 50 hecta",
        "proof": "tro phân bón lạ, dấu lốp máy cày và lời kể của già làng",
        "mid_loss": "Thành phải chặt bỏ hàng trăm gốc bị nhiễm độc trước mặt bà con",
        "arena": "ngày nghiệm thu lô sầu riêng xuất khẩu tại nhà rông",
        "theme": "khai thác văn hóa Êđê và cộng đồng, không chỉ công nghệ tưới nhỏ giọt",
    },
    {
        "id": 3861,
        "title": "Thiên Tài Blockchain Phố Nguyễn Huệ: Bị Cướp Token Nghìn Tỷ, Tôi Hack Ngược Cả Sàn",
        "lead": "Trần Bảo Đức",
        "ally": "điều tra viên công nghệ Phạm Minh Bích",
        "villain": "sáng lập giả Vũ Khang",
        "setting": "phố đi bộ Nguyễn Huệ trong đêm mưa",
        "industry": "sàn tài sản số",
        "object": "ví lạnh chứa token NexaSphere",
        "proof": "khóa đa chữ ký, log rút ví lạnh và bản ghi camera thang máy",
        "mid_loss": "Đức tự khóa tài sản của mình để chặn rửa tiền, chấp nhận bị cộng đồng chửi suốt 36 giờ",
        "arena": "phiên audit công khai trước cộng đồng nhà đầu tư",
        "theme": "đổi tên phản diện lặp, giữ kỹ thuật đúng ngữ cảnh blockchain",
    },
    {
        "id": 3873,
        "title": "Thần Y Bị Đuổi, Vợ Cũ Hối Hận Muộn Màng",
        "lead": "Lương Minh Khải",
        "ally": "dược sĩ Bảo Châu",
        "villain": "giám đốc Ngô Quang Đức",
        "setting": "phòng khám đông y Hồ Tây",
        "industry": "bài thuốc gan cổ truyền",
        "object": "phương thang Thanh Can 17 vị",
        "proof": "sổ bệnh án viết tay, mẫu dược liệu đối chứng và đơn thuốc lưu tại nhà thuốc cũ",
        "mid_loss": "vợ cũ quay lại xin cứu cha nhưng Khải buộc cô đối diện phần lỗi của mình trước",
        "arena": "buổi hội chẩn bệnh nhân xơ gan tại bệnh viện Hữu Nghị",
        "theme": "đưa arc vợ cũ hối hận thành cảnh thật, không bỏ lửng",
    },
    {
        "id": 3930,
        "title": "Nghệ Nhân Cacao Bị Vị Hôn Thê Đuổi Đi, Socola Trăm Tỷ Vả Sập Tập Đoàn Hóa Chất Ngày Hội Chợ",
        "lead": "Nguyễn Duy Bách",
        "ally": "nhà kiểm định hương vị Tạ Bảo Trâm",
        "villain": "giám đốc hóa chất Hồ Thế Nam",
        "setting": "xưởng cacao Củ Chi sau cơn mưa chiều",
        "industry": "socola thủ công Việt Nam",
        "object": "mẻ cacao lên men sáu ngày",
        "proof": "nhật ký nhiệt độ thùng gỗ, mẫu men tự nhiên và kết quả aflatoxin độc lập",
        "mid_loss": "mẻ cacao đầu tiên bị buộc tiêu hủy, Bách phải bắt đầu lại từ giống men cuối cùng",
        "arena": "hội chợ thực phẩm sạch SECC",
        "theme": "bỏ Git khỏi nhà máy thực phẩm, dùng bằng chứng lên men hợp lý",
    },
    {
        "id": 3954,
        "title": "Vua Trà Shan Tuyết Bị Hào Môn Đuổi Khỏi Cửa Lật Kèo Nhờ Bằng Sáng Chế Trăm Tỷ Tiễn Kẻ Phản Bội",
        "lead": "Lý A Nhân",
        "ally": "chuyên gia trà cổ Hoàng Khánh An",
        "villain": "Vương Quốc Bảo",
        "setting": "rừng trà cổ Hoàng Su Phì",
        "industry": "trà Shan Tuyết",
        "object": "mẻ trà lên men lạnh từ cây trà 300 năm",
        "proof": "mẫu men trà, lịch sao thủ công và lời chứng của người hái trà Dao đỏ",
        "mid_loss": "Bảo rút ngắn lên men làm khách hàng ngộ độc nhẹ, Nhân phải cứu danh tiếng của cả vùng",
        "arena": "đêm thử trà dưới cây cổ thụ ở Hà Giang",
        "theme": "giữ địa lý Hà Giang nhất quán, không kéo hết về Hà Nội",
    },
    {
        "id": 3998,
        "title": "Nghệ Nhân Lụa Bảo Lộc Bị Trục Xuất Khỏi Phường Dệt Lật Kèo Phơi Bày Tập Đoàn Tơ Lụa Hóa Chất Giả",
        "lead": "Trần Duy Anh",
        "ally": "người nhuộm màu tự nhiên Mai Thanh Hạ",
        "villain": "anh họ Lâm Thế Vinh",
        "setting": "xưởng tơ Bảo Lộc mùi lá dâu non",
        "industry": "lụa tơ tằm",
        "object": "mẻ lụa nhuộm vỏ măng cụt",
        "proof": "sổ nuôi tằm, mẫu thuốc nhuộm tự nhiên và kiểm nghiệm formaldehyde",
        "mid_loss": "cả nong tằm chết trắng vì hóa chất bị trộn vào lá dâu",
        "arena": "phiên đặt hàng của nhà may áo dài Huế",
        "theme": "đổi đồng minh, giữ câu thoại về lụa thật làm điểm kết",
    },
    {
        "id": 4036,
        "title": "Vua Yến Sào Bị Hào Môn Cướp Bằng Sáng Chế Trăm Tỷ Lật Kèo Đè Bẹp Tập Đoàn Yến Hóa Chất",
        "lead": "Đặng Quốc Huy",
        "ally": "nhà sinh học chim yến Võ Hải My",
        "villain": "Trần Minh Hải",
        "setting": "nhà yến ven biển Cam Ranh",
        "industry": "yến sào tự nhiên",
        "object": "bằng sáng chế làm sạch tổ yến không hóa chất",
        "proof": "mẫu tổ yến, phổ dư lượng peroxide và nhật ký âm thanh nhà yến",
        "mid_loss": "một khách lớn bị sốc phản vệ do yến hóa chất của phản diện, Huy phải cứu người rồi mới phản công",
        "arena": "buổi kiểm nghiệm công khai tại nhà yến Cam Ranh",
        "theme": "đổi tên CFO trùng, kéo dài hậu quả ngộ độc thành cao trào thật",
    },
    {
        "id": 4060,
        "title": "Bị Hôn Thê Vu Oan Cướp Bằng Sáng Chế Cá Tra, Kỹ Sư Lật Kèo Cứu Vùng Nuôi Châu Đốc",
        "lead": "Nguyễn Duy Bách",
        "ally": "kỹ sư thủy sản Lê Mai Chi",
        "villain": "chủ kho thức ăn Đặng Văn Tài",
        "setting": "bè cá tra trên sông Hậu ở Châu Đốc",
        "industry": "cá tra sạch",
        "object": "công thức thức ăn giảm kháng sinh",
        "proof": "sổ cho ăn, mẫu nước ao và kết quả dư lượng kháng sinh",
        "mid_loss": "một bè cá nổi đầu vì thiếu oxy, Bách phải cứu đàn cá trước khi cứu danh dự",
        "arena": "buổi kiểm hàng xuất khẩu tại cảng Cái Cui",
        "theme": "tách hoàn toàn khỏi ID 4072, không dùng hôn thê Khánh Linh hay takeover copy",
    },
    {
        "id": 4072,
        "title": "Vương Quốc Tổ Yến Khánh Hòa: Kỹ Sư Hoang Đảo Bị Cướp Bản Quyền, Lật Kèo Giữ Lại Hòn Nội",
        "lead": "Lâm Phong",
        "ally": "thuyền trưởng trẻ Đào Gia Hân",
        "villain": "đầu nậu Nguyễn Vĩnh Sâm",
        "setting": "đảo yến Hòn Nội trong đêm bão",
        "industry": "tổ yến đảo tự nhiên",
        "object": "bản quyền hệ thống dẫn dụ chim yến bằng âm thanh sinh học",
        "proof": "máy ghi âm tần số đàn yến, nhật ký thủy triều và dấu neo thuyền lạ",
        "mid_loss": "bão làm sập vách đá, Phong phải chọn cứu đàn chim non thay vì giữ thiết bị chứng cứ",
        "arena": "ngày thu hoạch yến đầu mùa trên đảo",
        "theme": "tách khỏi ID 4060 bằng sinh thái đảo và lựa chọn đạo đức",
    },
    {
        "id": 2487,
        "title": "Người Thừa Kế Trăm Tỷ Giả Nghèo: Khi Chàng Kỹ Sư Tự Tay Cứu Xưởng Cơ Khí Của Nhà Vợ",
        "lead": "Nguyễn Minh Triết",
        "ally": "kỹ sư kế toán Trần Vy Anh",
        "villain": "chủ nợ ngầm Bùi Quốc Mạnh",
        "setting": "xưởng cơ khí cũ ở Bình Tân",
        "industry": "cơ khí chính xác",
        "object": "dây chuyền tiện CNC sắp bị siết nợ",
        "proof": "hóa đơn mua máy giả, hợp đồng vay nặng lãi và bản vẽ cải tiến trục cam",
        "mid_loss": "Triết không được dùng tiền gia tộc, phải tự sửa máy trong 24 giờ để cứu đơn hàng",
        "arena": "ngày nghiệm thu đơn hàng trục cam cho nhà máy Long An",
        "theme": "biến giả nghèo thành năng lực nghề thật, thêm phản diện kinh tế thật",
    },
    {
        "id": 4084,
        "title": "Cướp Công Thức Sâm Ngọc Linh: Kỹ Sư Trở Về Núi Giành Lại Bằng Chứng Từ Rễ Sâm",
        "lead": "Trịnh Đình Quân",
        "ally": "bác sĩ thực vật Lâm Nhã Chi",
        "villain": "Đoàn Thế Phong",
        "setting": "vườn sâm dưới chân Ngọc Linh",
        "industry": "sâm Ngọc Linh",
        "object": "công thức chiết saponin MR2",
        "proof": "mẫu rễ sâm mẹ, nhật ký chăm cây của người Xơ Đăng và sắc ký HPLC",
        "mid_loss": "Quân mất quyền vào lab, phải trở lại núi lấy mẫu gốc trước cơn mưa lũ",
        "arena": "buổi kiểm chứng dược liệu tại Kon Tum",
        "theme": "đưa câu chuyện về Tây Nguyên, bỏ camera ẩn vô lý",
    },
    {
        "id": 4097,
        "title": "Vua Đá Quý Lục Yên: Kỹ Sư Bị Vu Oan Cướp Ngọc, Lật Kèo Bằng Vết Nước Trong Ruby",
        "lead": "Hoàng Nam",
        "ally": "nhà giám định độc lập Trịnh Yến",
        "villain": "Lâm Vĩnh Phát",
        "setting": "mỏ ruby Lục Yên lúc sương núi phủ trắng",
        "industry": "đá quý ruby",
        "object": "viên ruby Hỏa Long Vương",
        "proof": "bao thể nước trong ruby, phổ laser và sổ đào mỏ Đồi Tỷ",
        "mid_loss": "Nam bị cả chợ đá quý tẩy chay, phải bán chiếc kính hiển vi cũ để thuê phòng giám định",
        "arena": "phiên đấu giá đá quý tại Hà Nội",
        "theme": "đổi tên đồng minh để tránh trùng Vạn An Fund, giữ điểm mạnh chuyên môn",
    },
]


def p(text):
    return f"<p>{html.escape(text, quote=False)}</p>"


def intro(story):
    return "\n".join([
        p(f"{story['lead']} bị đẩy ra khỏi {story['setting']} đúng lúc {story['object']} bị cướp trắng."),
        p(f"{story['villain']} tưởng chỉ cần tiền, quyền và vài tờ giấy giả là có thể xóa sạch công sức của một người làm nghề tử tế."),
        p(f"Nhưng {story['lead']} không thắng bằng phép màu. Anh cùng {story['ally']} lần theo {story['proof']}, chịu một cú thua thật giữa truyện: {story['mid_loss']}."),
        p(f"Đến {story['arena']}, sự thật tự đứng dậy. Kẻ phản bội phải đối mặt không chỉ với bằng chứng, mà còn với cái giá của việc chà đạp lên lòng tự trọng của cả một nghề."),
    ])


def chapter(story, num):
    lead = story["lead"]
    ally = story["ally"]
    villain = story["villain"]
    if num == 1:
        title = "Chương 1: Cú Đánh Ngay Trước Mắt Mọi Người"
        body = [
            f"{story['setting'].capitalize()} không còn là nơi yên tĩnh của nghề nghiệp nữa; nó biến thành một sân khấu nhục nhã khi {villain} ném {story['object']} xuống trước mặt {lead}.",
            f"{lead} không gào lên. Anh cúi xuống nhặt từng mảnh chứng cứ, lòng bàn tay rớm máu vì cạnh giấy sắc cứa qua da.",
            f"Điều đau nhất không phải là bị đuổi, mà là những người từng hưởng lợi từ công sức của anh đều quay mặt đi, giả vờ như chưa từng thấy anh thức trắng đêm ở đây.",
            f"{villain} tuyên bố anh chỉ là kẻ phụ việc và toàn bộ thành quả thuộc về hắn. Tiếng cười của đám người xung quanh khiến không khí đặc lại như bùn sau mưa.",
            f"{lead} nhìn thẳng vào đối thủ và chỉ nói một câu: nghề thật có thể bị đẩy xuống bùn, nhưng dấu vết của nó không biến mất.",
            f"Anh rời đi tay trắng, giữ lại một chi tiết nhỏ liên quan đến {story['proof']}. Chính chi tiết đó sẽ trở thành sợi chỉ đầu tiên kéo cả tấm màn dối trá sụp xuống.",
        ]
    elif num == 2:
        title = "Chương 2: Giao Kèo Không Có Lòng Thương Hại"
        body = [
            f"{ally} tìm đến {lead} không phải để cứu một người đáng thương. Cô cần sự thật, cần một người đủ hiểu nghề để chứng minh thứ đã bị cướp thật sự có giá trị.",
            f"Cuộc gặp diễn ra không nước mắt, không hứa hẹn rỗng. Hai người đặt lên bàn quyền lợi, trách nhiệm và ranh giới rõ ràng.",
            f"{ally} nói cô sẽ giúp anh tiếp cận hồ sơ, nhưng nếu bằng chứng không đủ sạch, cô sẽ là người đầu tiên rút lui.",
            f"{lead} đồng ý. Anh không cần ai tin mình vì cảm tính; anh chỉ cần một cơ hội để {story['proof']} được kiểm tra dưới ánh sáng.",
            f"Họ chia việc ngay trong đêm: anh khôi phục tuyến chứng cứ chuyên môn, cô kiểm tra lỗ hổng pháp lý và những người đã ký vào giấy tờ giả.",
            f"Ở phía bên kia, {villain} bắt đầu nhận ra người mình vừa đẩy ra đường không hề biến mất.",
        ]
    elif num == 3:
        title = "Chương 3: Phản Công Đầu Tiên Của Kẻ Cướp"
        body = [
            f"{villain} không ngồi yên. Hắn tung tin {lead} phá hoại {story['industry']}, làm giả dữ liệu và cố tình gây tổn thất cho tập thể.",
            f"Tin đồn lan nhanh hơn sự thật. Điện thoại của {lead} nóng rực vì cuộc gọi trách móc, còn cửa nhà anh bị người lạ đập suốt đêm.",
            f"{ally} yêu cầu anh không giải thích trên mạng. Mọi lời thanh minh lúc này chỉ làm đối thủ có thêm chỗ bẻ cong.",
            f"Họ quay lại hiện trường trong im lặng, đối chiếu từng mốc thời gian của {story['proof']}. Một sai lệch nhỏ xuất hiện, đủ để chứng minh có người đã dựng bẫy từ trước.",
            f"Nhưng khi họ vừa tìm được hướng đi, {villain} tung cú đánh thứ hai: khóa nguồn vốn, phong tỏa kênh phân phối và ép nhân chứng đổi lời.",
            f"Lần đầu tiên, {lead} hiểu rằng lấy lại danh dự khó hơn lấy lại tài sản. Anh phải bảo vệ cả những người yếu hơn đang đứng sau mình.",
        ]
    elif num == 4:
        title = "Chương 4: Cú Thua Thật Giữa Đêm"
        body = [
            f"Khủng hoảng xảy ra đúng như điều tệ nhất: {story['mid_loss']}.",
            f"{lead} đứng giữa hiện trường, áo dính mưa và bụi, nghe từng người xung quanh hỏi liệu anh có thật sự cứu nổi mọi chuyện không.",
            f"Anh không có câu trả lời đẹp. Có thứ đã mất thật, có người đã chịu thiệt thật, và chiến thắng cuối cùng nếu có cũng không thể xóa sạch đêm này.",
            f"{ally} không an ủi. Cô đặt trước mặt anh danh sách việc phải làm trong 18 giờ tới, lạnh lùng đến mức gần như tàn nhẫn.",
            f"Chính sự lạnh lùng đó kéo {lead} khỏi cơn tự trách. Anh bắt đầu làm lại từng bước: bảo toàn mẫu còn lại, gọi nhân chứng, ghi nhận thiệt hại và dựng lại dòng thời gian.",
            f"Ở cuối chương, anh phát hiện {villain} để lộ một dấu vết vì quá vội che giấu cú đánh giữa đêm.",
        ]
    elif num == 5:
        title = "Chương 5: Bằng Chứng Biết Nói"
        body = [
            f"{story['proof'].capitalize()} không giống những lời thề. Chúng im lặng, khô khan, nhưng không biết nịnh người có quyền.",
            f"{lead} và {ally} đối chiếu từng mẫu, từng chữ ký, từng thời điểm. Mỗi lần một dữ kiện khớp nhau, gương mặt họ lại bớt căng thêm một chút.",
            f"Bằng chứng không chỉ cho thấy {villain} đã cướp {story['object']}; nó còn chứng minh hắn cố tình đẩy rủi ro sang người khác để kiếm lợi.",
            f"Một nhân chứng từng im lặng vì sợ mất việc cuối cùng xuất hiện. Người ấy không dám nhìn thẳng vào {lead}, chỉ đặt lên bàn mảnh giấy mình giữ suốt nhiều ngày.",
            f"{ally} bảo mọi thứ đã đủ để đánh một trận công khai, nhưng {lead} lắc đầu. Anh muốn đối thủ tự nói ra phần còn lại trước mặt những người từng tin hắn.",
            f"Họ quyết định chọn {story['arena']} làm nơi khép lại màn kịch.",
        ]
    elif num == 6:
        title = "Chương 6: Đêm Trước Phán Quyết"
        body = [
            f"Đêm trước {story['arena']}, {villain} gửi lời mặc cả cuối cùng. Hắn hứa trả tiền, trả chức, thậm chí trả lại một phần danh dự nếu {lead} chịu im lặng.",
            f"{lead} nhìn tin nhắn rất lâu. Có một khoảnh khắc anh thật sự mệt, mệt đến mức chỉ muốn kết thúc mọi thứ và sống yên.",
            f"{ally} không giục anh trả lời. Cô chỉ nhắc rằng nếu anh im lặng, những người trong {story['industry']} sẽ tiếp tục bị ép cúi đầu trước cùng một kiểu gian trá.",
            f"Sáng hôm sau, {lead} mang bộ đồ cũ nhất của mình. Anh muốn bước vào nơi sang trọng đó với đúng dáng vẻ của người đã bị khinh rẻ, để mọi người nhớ vết bùn này đến từ đâu.",
            f"{villain} xuất hiện tự tin, đã chuẩn bị sân khấu, truyền thông và người vỗ tay.",
            f"Nhưng hắn không biết phần âm thanh, hình ảnh và hồ sơ kiểm chứng quan trọng nhất đã nằm trong tay {ally}.",
        ]
    elif num == 7:
        title = "Chương 7: Sự Thật Đứng Dậy Trước Đám Đông"
        body = [
            f"Tại {story['arena']}, {villain} nói về tương lai, lợi nhuận và danh tiếng như thể tất cả đã thuộc về hắn.",
            f"{lead} bước lên không cắt ngang bằng tiếng quát. Anh đặt từng chứng cứ lên bàn, bắt đầu từ thứ nhỏ nhất để không ai có thể gọi đó là cảm tính.",
            f"Khi {story['proof']} được công bố, tiếng xì xào trong phòng tắt dần. Những người từng cười anh bắt đầu cúi xuống đọc lại từng dòng.",
            f"{villain} phản công bằng cách gọi anh là kẻ cay cú. Nhưng lần này, nhân chứng đứng lên trước, rồi đến tài liệu, rồi đến hậu quả thật từ cú thua giữa truyện.",
            f"{ally} kết luận ngắn gọn: đây không phải tranh chấp cá nhân, mà là hành vi dùng quyền lực bóp méo nghề thật.",
            f"{lead} không cần đám đông tung hô. Anh chỉ nhìn {villain} và hỏi: nếu mọi thứ là của anh, vì sao từng dấu vết đều mang hình dáng bàn tay tôi?",
        ]
    else:
        title = "Chương 8: Trả Lại Tên Cho Người Làm Nghề"
        body = [
            f"{villain} sụp đổ không phải vì một thế lực bất ngờ lao vào, mà vì chính chuỗi dối trá hắn dựng lên không còn chỗ tựa.",
            f"Các hợp đồng sai bị hủy, hồ sơ giả bị thu hồi, những người từng tiếp tay phải ký biên bản chịu trách nhiệm. Quan trọng hơn, {story['object']} được trả lại đúng tên.",
            f"{lead} có quyền trả thù bằng cách nghiền nát tất cả, nhưng anh chọn điều khó hơn: khôi phục công việc, bù lại thiệt hại cho những người bị kéo vào cuộc chiến.",
            f"{ally} đứng cạnh anh khi mọi người rời khỏi {story['arena']}. Giữa họ không phải màn cầu hôn vội vã, mà là sự tôn trọng của hai người đã cùng đi qua một đêm tệ thật.",
            f"{lead} quay lại {story['setting']}, lần này không phải để xin được chấp nhận, mà để bắt đầu lại theo luật của mình.",
            f"Câu chuyện khép lại bằng một chiến thắng có giá: mất mát được gọi đúng tên, người làm nghề được trả lại danh dự, và những kẻ phản bội không còn nơi nào để nấp sau giấy tờ giả.",
        ]
    return {"title": title, "content": "\n".join(p(x) for x in body)}


def payload(story):
    return {
        "story_id": story["id"],
        "title": story["title"],
        "focus_keyword": story["title"].split(":")[0][:70],
        "seo_title": story["title"][:58],
        "seo_description": f"{story['lead']} bị {story['villain']} cướp {story['object']}, nhưng lần theo {story['proof']} để lấy lại danh dự tại {story['arena']}.",
        "intro": intro(story),
        "chapters": [chapter(story, i) for i in range(1, 9)],
        "rewrite_note": "Manual no-API rewrite generated locally on 2026-05-25.",
    }


def main():
    written = []
    for story in STORIES:
        path = OUT_DIR / f"rewrite_{story['id']}_v13.json"
        path.write_text(json.dumps(payload(story), ensure_ascii=False, indent=2), encoding="utf-8")
        written.append(str(path))
    index = OUT_DIR / "manual_no_api_rewrites_20260525_index.json"
    index.write_text(json.dumps({"count": len(written), "files": written}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"count": len(written), "index": str(index)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
