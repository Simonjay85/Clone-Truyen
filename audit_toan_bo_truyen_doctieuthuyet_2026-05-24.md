# Audit toàn bộ truyện doctieuthuyet.com

- Thời điểm audit: 2026-05-24 18:26:09 +07
- Nguồn đọc: `https://doctieuthuyet.com/wp-json/wp/v2/truyen`, `https://doctieuthuyet.com/wp-json/wp/v2/chuong`, trang HTML từng truyện để map danh sách chương.
- Phạm vi: 91 truyện public, 1210 chương public trong REST API.
- Ghi chú: đây là audit biên tập tự động có đọc text từng mô tả/chương và bắt lỗi bằng rule nội dung; các mục bị flag nặng nên được đọc lại thủ công trước khi sửa live.

## Tóm tắt nhanh

- **Vua Sầu Riêng Đắk Nông: Bị Đốt Vườn Nghìn Tỷ, Tôi Trồng Lại Từ Tro Tàn**: 10 chương, mô tả 162 từ. Ổn ở mức tổng quan.
- **Nghệ Nhân Sơn Mài Bị Khinh Rẻ Đuổi Khỏi Xưởng Tìm Ra Màu Sơn Thất Truyền Đè Bẹp Tập Đoàn Tranh Giả**: 8 chương, mô tả 243 từ. Cần xem: tên truyện rất dài, dễ vỡ layout/SEO
- **Đạo Diễn Phim Trường Cần Giờ: Bị Cướp Kịch Bản Oscar, Tôi Quay Phim Chấn Động Cannes**: 10 chương, mô tả 132 từ. Ổn ở mức tổng quan.
- **Thiên Tài Blockchain Phố Nguyễn Huệ: Bị Cướp Token Nghìn Tỷ, Tôi Hack Ngược Cả Sàn**: 10 chương, mô tả 173 từ. Ổn ở mức tổng quan.
- **Chúa Đảo Resort Phú Quốc: Bị Đuổi Khỏi Resort Mình Xây, Tôi Mua Cả Hòn Đảo**: 10 chương, mô tả 166 từ. Ổn ở mức tổng quan.
- **Bác Sĩ Đông Y Bị Đuổi Khỏi Viện Phổi, Mũi Kim Thần Đông Tây Kết Hợp Vả Sập Tập Đoàn Phản Bội**: 8 chương, mô tả 317 từ. Ổn ở mức tổng quan.
- **Thần Đồng Piano Nhạc Viện: Bị Cấm Biểu Diễn, Tôi Chấn Động Chopin Competition**: 10 chương, mô tả 138 từ. Ổn ở mức tổng quan.
- **Nghệ Nhân Cacao Bị Vị Hôn Thê Đuổi Đi, Socola Trăm Tỷ Vả Sập Tập Đoàn Hóa Chất Ngày Hội Chợ**: 8 chương, mô tả 392 từ. Cần xem: mô tả dài (392 từ), nên cô lại
- **Vua Trà Shan Tuyết Bị Hào Môn Đuổi Khỏi Cửa Lật Kèo Nhờ Bằng Sáng Chế Trăm Tỷ Tiễn Kẻ Phản Bội**: 8 chương, mô tả 313 từ. Ổn ở mức tổng quan.
- **THẦN Y BỊ ĐUỔI, VỢ CŨ HỐI HẬN MUỘN MÀNG**: 8 chương, mô tả 182 từ. Ổn ở mức tổng quan.
- **Kiến Trúc Sư Phố Cổ Hà Nội: Bị Cướp Bản Vẽ Di Sản, Tôi Cứu Cả Khu Phố**: 10 chương, mô tả 174 từ. Ổn ở mức tổng quan.
- **Bác Sĩ Thẩm Mỹ Sài Gòn: Bị Vu Oan Phẫu Thuật Hỏng, Tôi Lật Mặt Cả Bệnh Viện**: 10 chương, mô tả 165 từ. Ổn ở mức tổng quan.
- **Nữ Hoàng Trà Sen Tây Hồ: Bị Đuổi Khỏi Gia Tộc, Cô Xây Đế Chế Trà Nghìn Tỷ**: 10 chương, mô tả 209 từ. Ổn ở mức tổng quan.
- **Thợ Nuôi Trai Bị Cướp Ngọc Đen Đuổi Khỏi Vịnh, Trở Lại Lật Kèo Đoạt Lại Tập Đoàn Ngọc Trai Nghìn Tỷ**: 8 chương, mô tả 267 từ. Cần xem: tên truyện rất dài, dễ vỡ layout/SEO
- **Vua Lúa Gạo Đồng Tháp: Nông Dân Bị Ép Giá, Tôi Xây Đế Chế Gạo Xuất Khẩu**: 10 chương, mô tả 157 từ. Ổn ở mức tổng quan.
- **Người Đưa Thư Bị Cả Tòa Nhà Khinh, Hóa Ra Anh Là Chủ Toàn Bộ Tháp**: 8 chương, mô tả 133 từ. Ổn ở mức tổng quan.
- **Kỹ Sư Vắc Xin Bị Sa Thải Vì Không Gian Lận, Bản Quyền Vắc Xin Vả Sập Tập Đoàn Phản Bội**: 8 chương, mô tả 173 từ. Ổn ở mức tổng quan.
- **Ông Trùm Logistics Tân Cảng: Bị Phản Bội Mất Container Nghìn Tỷ, Tôi Thâu Tóm Ngược**: 10 chương, mô tả 119 từ. Ổn ở mức tổng quan.
- **Nghệ Nhân Trà Sen Bị Khinh Rẻ Trục Xuất, Lật Kèo Đêm Hội Trà Quốc Tế Đưa Kẻ Phản Bội Vào Tù**: 8 chương, mô tả 165 từ. Ổn ở mức tổng quan.
- **Bị Đuổi Khỏi Lab Đêm Trước IPO, Hóa Ra Anh Nắm Công Thức Trăm Tỷ**: 11 chương, mô tả 109 từ. Ổn ở mức tổng quan.
- **Giáo Viên Làng Bị Hiệu Trưởng Sỉ Nhục, Bộ Giáo Dục Bổ Nhiệm Anh Làm Thanh Tra**: 8 chương, mô tả 144 từ. Ổn ở mức tổng quan.
- **Trọng Tài Bị Ngôi Sao Nhổ Nước Bọt, Hóa Ra Là Cựu Đội Trưởng Tuyển QG**: 8 chương, mô tả 124 từ. Ổn ở mức tổng quan.
- **Người Làm Vườn Bị Chủ Biệt Thự Đuổi, Hóa Ra Anh Thiết Kế Cả Khu Đô Thị**: 8 chương, mô tả 120 từ. Ổn ở mức tổng quan.
- **Thợ Sửa Xe Bị Cả Xóm Khinh, Khi Đội Đua F1 Quốc Gia Tìm Đến Thuê Anh Làm Kỹ Sư Trưởng**: 8 chương, mô tả 234 từ. Ổn ở mức tổng quan.
- **Tài Xế Taxi Bị Khách VIP Khinh Thường, Tài Xế Đó Sở Hữu Công Ty Taxi Lớn Nhất Thành Tâm**: 8 chương, mô tả 350 từ. Cần xem: mô tả dài (350 từ), nên cô lại
- **Trợ Lý Bị Sếp Nữ CEO Ngược Đãi, Sếp Mới Của Cô Chính Là Anh Sau Thâu Tóm Công Ty**: 8 chương, mô tả 256 từ. Ổn ở mức tổng quan.
- **Cô Gái Bán Hoa Bị Đuổi Khỏi Tiệc Cưới Hào Môn, Cùng Ngày Cô Gõ Sàn HOSE**: 8 chương, mô tả 123 từ. Ổn ở mức tổng quan.
- **Con Trai Nuôi Bị Đuổi Ra Khỏi Tập Đoàn, Di Chúc Ông Nội Trao Lại 70% Cổ Phần**: 8 chương, mô tả 218 từ. Ổn ở mức tổng quan.
- **Chồng Nghèo Bị Họ Hàng Khinh Dự Tiệc Hào Môn, Hóa Ra Anh Là Khách Mời VIP Của Sự Kiện Đó**: 8 chương, mô tả 246 từ. Ổn ở mức tổng quan.
- **Vợ Đòi Ly Hôn Vì Chồng Thất Nghiệp, Ngày Ký Đơn Chồng Nhận Danh Hiệu Kiến Trúc Sư Quốc Gia**: 8 chương, mô tả 178 từ. Ổn ở mức tổng quan.
- **Cô Gái Làng Bị Nhà Trai Hào Môn Từ Chối, Startup Nông Nghiệp Của Cô Niêm Yết 500 Tỷ**: 8 chương, mô tả 124 từ. Ổn ở mức tổng quan.
- **Thuyền Trưởng Tàu Cá Bị Chủ Cảng Ép Nợ, Hóa Ra Là Đại Gia Hàng Hải Đang Điều Tra Thâu Tóm**: 8 chương, mô tả 196 từ. Ổn ở mức tổng quan.
- **Trưởng Phòng Bán Hàng Khinh Nhân Viên Mới, Nhân Viên Đó Là Chuyên Gia Tư Vấn Của Tập Đoàn Mẹ**: 8 chương, mô tả 220 từ. Ổn ở mức tổng quan.
- **Nhà Chồng Khinh Tôi Không Biết Nấu Ăn, Tôi Giật Giải Đầu Bếp Số 1 Đông Nam Á Trước Mặt Họ**: 8 chương, mô tả 99 từ. Ổn ở mức tổng quan.
- **Giáo Sư Đuổi Học Trò Ra Khỏi Lớp Vì Dốt, Học Trò Đó Là Tác Giả Giáo Trình Giáo Sư Đang Dạy**: 8 chương, mô tả 141 từ. Ổn ở mức tổng quan.
- **Bố Vợ Ép Ly Hôn Vì Tôi Nghèo Hèn, Công Ty Tỷ Đô Của Tôi Niêm Yết Sàn Chứng Khoán Hôm Đó**: 8 chương, mô tả 99 từ. Ổn ở mức tổng quan.
- **Giám Đốc Bệnh Viện Sa Thải Bác Sĩ Thực Tập, Hội Đồng Y Tế Quốc Gia Cử Người Điều Tra**: 8 chương, mô tả 102 từ. Ổn ở mức tổng quan.
- **Chàng Rể Ngọc Linh Lật Kèo Cứu Bị Cướp**: 8 chương, mô tả 148 từ. Ổn ở mức tổng quan.
- **Sư Phụ Đuổi Tôi Khỏi Võ Quán Vì Hèn Yếu, Giải Vô Địch Quốc Gia Lộ Ra Thân Phận Thật**: 8 chương, mô tả 111 từ. Ổn ở mức tổng quan.
- **Cô Vợ Hào Môn Khinh Tôi Vô Dụng, Cả Hà Ngoại Biết Tôi Là Chủ Tịch Tập Đoàn Thép**: 8 chương, mô tả 96 từ. Ổn ở mức tổng quan.
- **Đế Chế Gốm Sứ Bát Tràng: Phản Bội và Bùng Nổ**: 8 chương, mô tả 150 từ. Ổn ở mức tổng quan.
- **Chàng Rể Vạch Trần Âm Mưu Gia Tộc Trầm Hương**: 8 chương, mô tả 136 từ. Ổn ở mức tổng quan.
- **Thiên Tài Cầu Đường: Kỹ Sư Bị Sa Thải Đối Đầu Với Kẻ Cướp Bản Quyền**: 8 chương, mô tả 113 từ. Ổn ở mức tổng quan.
- **Người Thừa Kế Trăm Tỷ Giả Nghèo: Thử Lòng Đại Gia**: 8 chương, mô tả 149 từ. Ổn ở mức tổng quan.
- **Công Thức Thuốc Bị Cướp: Bẫy IPO Dược Phẩm Nghìn Tỷ**: 8 chương, mô tả 162 từ. Ổn ở mức tổng quan.
- **Ngọc Hoàng Tôm Hùm: Trận Chiến Khốc Liệt Giữa Ngư Dân Và Thương Láii**: 8 chương, mô tả 200 từ. Ổn ở mức tổng quan.
- **Bão Nổi Miền Tây: Vương Quốc Sầu Riêng Trăm Tỷ**: 8 chương, mô tả 121 từ. Ổn ở mức tổng quan.
- **Vương Quốc Nước Mắm Truyền Thống Phú Quốc: Chàng Rể Ẩn Thế Vực Dậy Quốc Hồn**: 8 chương, mô tả 108 từ. Ổn ở mức tổng quan.
- **Thiên Tài Fintech: Lật Kèo Tại PayBlock**: 8 chương, mô tả 100 từ. Ổn ở mức tổng quan.
- **Bảo Vệ Quèn Là Võ Thần: Phá Bẫy Buôn Lậu 500 Tỷ Cảng Đình Vũ**: 8 chương, mô tả 123 từ. Ổn ở mức tổng quan.
- **Nguyễn Tấn Đạt: Chàng Rể Bùn Lầy Lật Kèo Vườn Sầu Riêng Trăm Tỷ**: 8 chương, mô tả 135 từ. Ổn ở mức tổng quan.
- **Trọng Sinh 2008: Vua Đất Đông Anh Thiết Lập Đế Chế**: 8 chương, mô tả 180 từ. Ổn ở mức tổng quan.
- **Võ Thần Đất Cảng: Vệ Sĩ Ẩn Thân Phá Bẫy Buôn Lậu 500 Tỷ Cảng Đình Vũ**: 11 chương, mô tả 108 từ. Ổn ở mức tổng quan.
- **Cuộc Chiến Sinh Tử Của Trà Ô Long Hữu Cơ Việt**: 8 chương, mô tả 127 từ. Ổn ở mức tổng quan.
- **Đế Chế Dệt May Bình Thịnh: Chiến Tranh Tài Chính**: 8 chương, mô tả 89 từ. Ổn ở mức tổng quan.
- **Cuộc Chiến Nghệ Thuật Tại Nhà Hát Phương Nam**: 8 chương, mô tả 136 từ. Ổn ở mức tổng quan.
- **Cướp Mã Nguồn Nghìn Tỷ, Kích Hoạt Bẫy Chôn Vùi Tập Đoàn**: 8 chương, mô tả 137 từ. Ổn ở mức tổng quan.
- **Cuộc Chiến Bánh Mì: Bảo Vệ Di Sản Ẩm Thực Hội Nguyên**: 8 chương, mô tả 133 từ. Ổn ở mức tổng quan.
- **Vương Quốc Bất Động Sản: Cuộc Chiến Sinh Tử**: 8 chương, mô tả 119 từ. Ổn ở mức tổng quan.
- **Nhà Thiết Kế Tàng Hình: Cuộc Chiến Tại Hội Nghị Thời Trang Quốc Gia**: 8 chương, mô tả 140 từ. Ổn ở mức tổng quan.
- **Thiên Tài Lập Trình: Đà Lạt Sương Mù và Kế Hoạch Lật Đổ Tập Đoàn Tài Chính**: 8 chương, mô tả 106 từ. Ổn ở mức tổng quan.
- **Bóng Tối Điện Lực Vạn Thịnh: Cuộc Chiến Chống Tham Nhũng**: 8 chương, mô tả 154 từ. Ổn ở mức tổng quan.
- **Triều Đại Cà Phê Bazan: Cuộc Chiến Giành Bằng Sáng Chế**: 8 chương, mô tả 114 từ. Ổn ở mức tổng quan.
- **Thợ Hồ Nghìn Tỷ: Đập Tan Kiêu Ngạo**: 8 chương, mô tả 124 từ. Ổn ở mức tổng quan.
- **Bị Bạn Thân Cướp Startup, Tôi Lật Kèo Đế Chế FinTech**: 8 chương, mô tả 127 từ. Ổn ở mức tổng quan.
- **Mẹ Vợ Đòi Sính Lễ 5 Tỷ, Tôi Là Người Thừa Kế Landmark 81**: 8 chương, mô tả 139 từ. Ổn ở mức tổng quan.
- **Sếp Cướp Công Thức Thuốc, Tôi Phá Sập IPO Nghìn Tỷ**: 8 chương, mô tả 164 từ. Ổn ở mức tổng quan.
- **Thần Tài Chứng Khoán: Đấu Trường Phố Wall Hà Nội**: 8 chương, mô tả 133 từ. Ổn ở mức tổng quan.
- **Tiểu Thư Khinh Tôi Là Bảo Vệ: Đặc Nhiệm Giữa Đế Chế Buôn Lậu**: 8 chương, mô tả 142 từ. Ổn ở mức tổng quan.
- **Thuyền Trưởng Cảng Đà Thành: Cuộc Chiến Bên Bến Cả**: 8 chương, mô tả 118 từ. Ổn ở mức tổng quan.
- **Người Thợ Sửa Xe Ở Hầm B2**: 8 chương, mô tả 223 từ. Ổn ở mức tổng quan.
- **Độc Bản Dược Thần: Kẻ Lật Kèo Thế Kỷ**: 8 chương, mô tả 181 từ. Cần xem: thiếu số chương: 4
- **Mẹ Vợ Bắt Rửa Bát, Tôi Nấu Tiệc Michelin Chấn Động Phú Quốc**: 8 chương, mô tả 230 từ. Ổn ở mức tổng quan.
- **Cô Gái Bán Trà Sữa Và Hợp Đồng Trăm Tỷ**: 8 chương, mô tả 221 từ. Ổn ở mức tổng quan.
- **Trọng Sinh 2008: Ôm Đất Đông Anh Trước Cơn Sốt Nghìn Tỷ**: 8 chương, mô tả 152 từ. Ổn ở mức tổng quan.
- **Thần Y Quận 5: Kẻ Cướp Công Trình và Siêu Tỷ Phú**: 8 chương, mô tả 126 từ. Ổn ở mức tổng quan.
- **Bị Đuổi Khỏi Khách Sạn, Tôi Mua Luôn Chuỗi Năm Sao**: 8 chương, mô tả 165 từ. Ổn ở mức tổng quan.
- **Chàng Rể Ẩn Thân Miền Tây: Cứu Vườn Sầu Riêng Trăm Tỷ**: 8 chương, mô tả 105 từ. Ổn ở mức tổng quan.
- **Bị Sa Thải Trước Giờ Đấu Thầu: Một Mình Thắng Gói AI Nghìn Tỷ**: 8 chương, mô tả 116 từ. Ổn ở mức tổng quan.
- **Kẻ Phế Vật Trở Về: Đòi Lại Gia Tộc Sau 12 Năm**: 8 chương, mô tả 182 từ. Ổn ở mức tổng quan.
- **Phế Vật Trở Về: Cuộc Báo Thù Rực Lửa**: 8 chương, mô tả 99 từ. Ổn ở mức tổng quan.
- **Kỹ Sư Bị Cả Xã Khinh Là Kẻ Nói Điên, Lá Thư Cuối Cùng Của Biển Cứu Sống Cát Hải Trong Đêm Bão**: 8 chương, mô tả 131 từ. Ổn ở mức tổng quan.
- **Hệ Thống Trí Tuệ Nhân Tạo: Xuyên Không Đến Tương Lai**: 8 chương, mô tả 136 từ. Ổn ở mức tổng quan.
- **Tôi Giả Nghèo Đi Ra Mắt, Mẹ Người Yêu Đòi Sính Lễ 900 Triệu Và Bị Vả Mặt Ngay Tại Chung Cư Hoài Đức**: 8 chương, mô tả 121 từ. Cần xem: tên truyện rất dài, dễ vỡ layout/SEO
- **Thành Phố Chìm Trong Bóng Tối, Kỹ Sư Bị Xem Là Kẻ Điên Kích Hoạt Nguồn Sáng Cuối Cùng**: 8 chương, mô tả 117 từ. Ổn ở mức tổng quan.
- **Mẹ Chồng Gọi Tôi Là Người Ngoài, Sổ Đỏ Biệt Thự Gò Vấp 5 Tỷ Khiến Cả Mâm Giỗ Câm Lặng**: 8 chương, mô tả 110 từ. Ổn ở mức tổng quan.
- **Họa Sĩ Mù Bị Thiếu Gia Cướp Tranh, Ánh Sáng Trong Đêm Khiến Cả Phòng Đấu Giá Hà Nội Im Phăng Phắc**: 8 chương, mô tả 136 từ. Cần xem: tên truyện rất dài, dễ vỡ layout/SEO
- **Giám Đốc Ngầm Đi Thực Tập Bị Trưởng Phòng Cướp Dự Án, Một Cuộc Họp Khiến Cả Công Ty Đứng Hình**: 8 chương, mô tả 121 từ. Ổn ở mức tổng quan.
- **Nhân Viên Bị Sếp Cướp Công Thức Dạ Dày, Log Lab Khiến Buổi IPO Nghìn Tỷ Đổ Sập Trước Truyền Thông**: 8 chương, mô tả 139 từ. Cần xem: tên truyện rất dài, dễ vỡ layout/SEO
- **Cô Gái Bị Gọi Là Con Bé Gần Máy In, Gấu Bông Quỷ Vương Giúp Cô Lật Mặt Cả Phòng Kế Toán**: 8 chương, mô tả 123 từ. Ổn ở mức tổng quan.
- **Con Dâu Dân Tỉnh Bị Khinh Trong Căn Nhà 4,8 Tỷ, Một Bộ Hồ Sơ Khiến Cả Nhà Chồng Trắng Mặt**: 8 chương, mô tả 119 từ. Ổn ở mức tổng quan.

## Việc nên sửa ưu tiên

1. Rút gọn các tên truyện quá dài để tránh vỡ UI và tăng CTR: giữ motif vả mặt nhưng bỏ bớt cụm giải thích kỹ thuật trong title.
2. Giảm các đoạn giải quyết quá nhanh ở chương cuối/cao trào: thêm lực cản, phản đòn hụt, chứng cứ bị nghi ngờ hoặc chi phí nhỏ cho nhân vật chính.
3. Hạ mật độ cụm cường điệu như “tuyệt đối”, “thần y”, “kinh thiên”, “giáng thế” ở những chương bị flag; thay bằng hành động/chứng cứ cụ thể.
4. Dọn các chương ngắn hoặc mất nhịp bằng cách bổ sung cảnh chuyển tiếp, cảm xúc sau va chạm, và hậu quả thực tế.

## Chi tiết từng truyện

### Vua Sầu Riêng Đắk Nông: Bị Đốt Vườn Nghìn Tỷ, Tôi Trồng Lại Từ Tro Tàn

- Link: https://doctieuthuyet.com/truyen/vua-sau-rieng-dak-nong-bi-dot-vuon-nghin-ty-toi-trong-lai-tu-tro-tan/
- Mô tả: 162 từ. Ổn.
- Mở đầu mô tả: Y Ksor Thành mày chỉ là một thằng người Ê đê quê mùa bám vườn sầu riêng Năm mươi hecta Musang King của mày giờ chỉ là đống tro tàn hợp đồng nghìn tỷ với đối tác Trung Quốc đã thuộc về...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1418 | Ổn | Gió lộng từ hướng cao nguyên Đắk Nông thổi thốc qua thung lũng Đắk Song mang theo mùi khét lẹt của nhựa sầu riêng... |
| 2 | 1148 | Ổn | Tại văn phòng khang trang của Công ty Nông sản Tây Nguyên Nam Phát ở trung tâm thành phố Gia Nghĩa không khí vô... |
| 3 | 1305 | Ổn | Sáng hôm sau Nguyễn Thị Hồng Vân dẫn đầu đoàn làm việc đến trụ sở Vietcombank chi nhánh tỉnh Đắk Nông n Đi cạnh... |
| 4 | 1240 | Ổn | Những ngày tiếp theo trên cao nguyên Đắk Nông là cuộc chạy đua gay cấn với thời gian của Y Ksor Thành và Nguyễn... |
| 5 | 1042 | Ổn | Thời tiết Đắk Nông bước vào những ngày nắng đẹp rực rỡ tạo điều kiện hoàn hảo cho sự hồi sinh kỳ diệu của... |
| 6 | 1109 | Ổn | Một tuần sau vụ bắt giữ hai tên phá hoại Đỗ Danh Nam vẫn tỏ ra vô cùng bình thản và ngạo mạn như... |
| 7 | 1343 | Ổn | Dưới cái nắng gắt rực lửa giữa trưa của cảng ICD Tân Cảng không khí bỗng trở nên ngột ngạt và căng thẳng đến... |
| 8 | 1064 | Ổn | Ngay sau khi kết quả kiểm nghiệm của Viện quốc gia được công bố bầu không khí tại cảng ICD Tân Cảng bỗng trở... |
| 9 | 1108 | Ổn | Sáu tháng sau vụ bắt giữ chấn động tại cảng ICD Tân Cảng cao nguyên Đắk Nông bước vào mùa thu hoạch sầu riêng... |
| 10 | 1102 | Ổn | Bữa tiệc mừng công và công bố thành lập Tập đoàn Nông sản Hữu cơ Đắk Nông được tổ chức vô cùng hoành tráng... |

### Nghệ Nhân Sơn Mài Bị Khinh Rẻ Đuổi Khỏi Xưởng Tìm Ra Màu Sơn Thất Truyền Đè Bẹp Tập Đoàn Tranh Giả

- Link: https://doctieuthuyet.com/truyen/nghe-nhan-son-mai-bi-khinh-re-duoi-khoi-xuong-tim-ra-mau-son-that-truyen-de-bep-tap-doan-tranh-gia/
- Mô tả: 243 từ. Cần sửa: tên truyện rất dài, dễ vỡ layout/SEO
- Mở đầu mô tả: Cút khỏi xưởng sơn mài họ Lâm ngay lập tức loại tàn phế tay run như mày chỉ làm bẩn danh tiếng tranh truyền thống trăm năm Lời mắng chửi tàn nhẫn của Lâm Thế Hùng ông chủ xưởng sơn mài Hùng...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 743 | Ổn | Cút khỏi xưởng sơn mài họ Lâm ngay lập tức Loại tàn phế tay run như mày chỉ làm bẩn danh tiếng tranh truyền... |
| 2 | 710 | Ổn | Căn phòng trọ mười hai mét vuông nằm sâu trong con hẻm nhỏ dột nát ở ngoại ô Thủ Dầu Một ngập tràn mùi... |
| 3 | 502 | ngắn (502 từ) | Dưới ánh đèn huỳnh quang sáng trưng của phòng thí nghiệm thuộc viện nghiên cứu hóa chất TP HCM Trần Hoài Nam chăm chú... |
| 4 | 396 | ngắn (396 từ) | Tại văn phòng làm việc sang trọng của Quỹ Đầu tư Vạn An tọa lạc trên tầng cao của tòa tháp Bitexco Quận 1... |
| 5 | 428 | ngắn (428 từ) | Cơn mưa dông giăng kín bầu trời Bình Dương sấm sét xé toạc màn đêm lạnh lẽo hắt ánh sáng xanh mét vào xưởng... |
| 6 | 406 | ngắn (406 từ) | Cuộc họp báo khẩn cấp do Quỹ Đầu tư Vạn An tổ chức diễn ra tại khách sạn Sheraton Sài Gòn thu hút hàng... |
| 7 | 452 | ngắn (452 từ) | Khán phòng sang trọng của Trung tâm Triển lãm Nghệ thuật Quốc tế Phú Mỹ Hưng ngập tràn tiếng nhạc giao hưởng du dương... |
| 8 | 447 | ngắn (447 từ) | Tiếng còi xe cảnh sát rú vang inh ỏi bên ngoài cổng Trung tâm Triển lãm Phú Mỹ Hưng xua tan hoàn toàn không... |

### Đạo Diễn Phim Trường Cần Giờ: Bị Cướp Kịch Bản Oscar, Tôi Quay Phim Chấn Động Cannes

- Link: https://doctieuthuyet.com/truyen/dao-dien-phim-truong-can-gio-bi-cuop-kich-ban-oscar-toi-quay-phim-chan-dong-cannes/
- Mô tả: 132 từ. Ổn.
- Mở đầu mô tả: Cậu chỉ là thằng đạo diễn quèn từ Cần Giờ không có Hãng phim Thiên Nam thì kịch bản của cậu chỉ là giấy lộn Bị gã sản xuất tráo trở cướp đi kịch bản dốc lòng viết suốt ba năm đạo...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1213 | Ổn | Nắng chiều Sài Gòn hắt qua những ô kính cường lực của tòa nhà văn phòng Hãng phim Thiên Nam tại trung tâm Quận... |
| 2 | 1203 | Ổn | Cơn mưa giông chiều hè bất chợt đổ ập xuống vùng đất rừng ngập mặn Cần Giờ xóa nhòa ranh giới giữa bầu trời... |
| 3 | 1086 | Ổn | Bình minh lên trên phim trường Cần Giờ hoang sơ nắng sớm trải dài trên những cánh rừng đước bạt ngàn ngập mặn và... |
| 4 | 1259 | Ổn | Cái nóng oi bức cuối tháng năm của vùng ngập mặn Cần Giờ hầm hập phả lên từ những bãi bùn đen nhầy nhụa... |
| 5 | 1079 | Ổn | Cơn bão tố thực sự không chỉ gầm rú ngoài cửa biển Cần Giờ hoang dã mà nó đã tràn ngập khắp các trang... |
| 6 | 1110 | Ổn | Cơn mưa giông lịch sử bất ngờ quét qua vùng đất rừng ngập mặn Cần Giờ vào một đêm không trăng tiếng sóng biển... |
| 7 | 1031 | Ổn | Cơn bão truyền thông bẩn bỗng chốc quay ngoắt một trăm tám mươi độ khi một văn bản chính thức được công bố từ... |
| 8 | 1054 | Ổn | Gió Địa Trung Hải thổi nhẹ mang theo hương vị mặn mòi của biển cả và ánh nắng vàng rực rỡ trải dài trên... |
| 9 | 1027 | Ổn | Rạp Debussy bên trong cung điện Palais des Festivals sáng rực ánh đèn pha lê ấm áp toàn bộ hơn một ngàn ghế ngồi... |
| 10 | 1130 | Ổn | Đêm bế mạc LHP Cannes diễn ra trong bầu không khí trang nghiêm và xa hoa rực rỡ sắc màu tại nhà hát lớn... |

### Thiên Tài Blockchain Phố Nguyễn Huệ: Bị Cướp Token Nghìn Tỷ, Tôi Hack Ngược Cả Sàn

- Link: https://doctieuthuyet.com/truyen/thien-tai-blockchain-pho-nguyen-hue-bi-cuop-token-nghin-ty-toi-hack-nguoc-ca-san/
- Mô tả: 173 từ. Ổn.
- Mở đầu mô tả: Năm năm đổ máu và mồ hôi trên từng dòng code blockchain tại căn penthouse phố Nguyễn Huệ tôi tạo ra NexaSphere giao thức DeFi nghìn tỷ đầu tiên của người Việt Thế nhưng kẻ đồng sáng lập mà tôi từng coi...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1333 | Ổn | Cơn mưa dông tháng năm quất liên hồi vào những tấm kính cường lực bóng loáng của căn penthouse tầng bốn mươi hai Từ... |
| 2 | 1103 | Ổn | Đức bước đi lếch thếch dọc theo phố đi bộ Nguyễn Huệ nước mưa từ tóc nhỏ giọt xuống vỉa hè đá hoa cương... |
| 3 | 937 | Ổn | Trụ sở làm việc của Cục An ninh mạng A05 tại TP HCM nằm trong một tòa nhà nghiêm trang trên đường Nguyễn Trãi... |
| 4 | 1042 | Ổn | Không khí trong phòng tác chiến A05 đột ngột chùng xuống căng thẳng bao trùm toàn bộ không gian số Ngọc Bích khẽ vẫy... |
| 5 | 802 | Ổn | Sau chiến tích bẻ khóa ngoạn mục Trương Minh Đức đã hoàn toàn chinh phục được lòng tin của toàn bộ đội đặc nhiệm... |
| 6 | 860 | Ổn | Đêm Thảo Điền tĩnh mịch gió từ sông Sài Gòn thổi vào mang theo hơi nước mát lạnh nhưng không làm giảm bớt sự... |
| 7 | 717 | Ổn | Đúng chín giờ tối ngày hôm sau không khí tại căn biệt thự Thảo Điền vô cùng náo nhiệt và sang trọng Lâm Thế... |
| 8 | 523 | ngắn (523 từ) | Sự hoảng loạn nhanh chóng biến căn biệt thự Thảo Điền thành một đống hỗn độn Lâm Thế Hùng thở dốc gã túm lấy... |
| 9 | 614 | ngắn (614 từ) | Tại phòng tác chiến A05 Quận 1 Trương Minh Đức nghe thấy toàn bộ lời thách thức của Hùng qua thiết bị đàm thoại... |
| 10 | 637 | ngắn (637 từ) | Sáng ngày hôm sau ánh nắng bình minh ấm áp trải dài khắp phố đi bộ Nguyễn Huệ xua tan hoàn toàn những tàn... |

### Chúa Đảo Resort Phú Quốc: Bị Đuổi Khỏi Resort Mình Xây, Tôi Mua Cả Hòn Đảo

- Link: https://doctieuthuyet.com/truyen/chua-dao-resort-phu-quoc-bi-duoi-khoi-resort-minh-xay-toi-mua-ca-hon-dao/
- Mô tả: 166 từ. Ổn.
- Mở đầu mô tả: Cậu nghĩ một kiến trúc sư tay trắng không thế lực như cậu có thể giữ nổi một thiên đường nghìn tỷ này sao Biến khỏi Phú Quốc trước khi tôi khiến cậu biến mất vĩnh viễn n Trịnh Gia Bảo kiến...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1215 | Ổn | Gió biển Phú Quốc về đêm mang theo vị mặn mòi đặc trưng thổi lướt qua những rặng dừa xanh mướt chạy dọc bãi... |
| 2 | 1236 | Ổn | Ba ngày sau cơn ác mộng ở Bãi Sao Trịnh Gia Bảo lặng lẽ bước lên chuyến phà cao tốc từ cảng Bãi Vòng... |
| 3 | 1165 | Ổn | Tại Băng Dương Resort không khí chuẩn bị cho lễ khai trương đang diễn ra vô cùng khẩn trương và náo nhiệt Lê Văn... |
| 4 | 1154 | Ổn | Đêm Phú Quốc yên bình lạ thường tại một quán cà phê nhỏ ẩn mình dưới những rặng phi lao rì rào bên bờ... |
| 5 | 1130 | Ổn | Một tuần sau tại trung tâm hội nghị tỉnh Kiên Giang diễn ra buổi đấu giá quyền sử dụng đất quần đảo An Thới... |
| 6 | 1203 | Ổn | Sau chiến thắng vang dội tại buổi đấu giá cấp tỉnh dự án Kỳ Quan Xanh trên Hòn Dăm Ngoài của Trịnh Gia Bảo... |
| 7 | 1097 | Ổn | Đúng ngày khai trương hoành tráng của Băng Dương Resort bầu trời Bãi Sao trong xanh không một gợn mây nắng vàng trải dài... |
| 8 | 1116 | Ổn | Sau đêm kinh hoàng tại lễ khai trương Băng Dương Resort bị cơ quan công an ra quyết định đình chỉ hoạt động hoàn... |
| 9 | 1191 | Ổn | Ba tháng sau khi vụ án Băng Dương Resort chấn động dư luận Phú Quốc bị triệt phá hoàn toàn dự án Kỳ Quan... |
| 10 | 1103 | Ổn | Lễ trao giải Du lịch Quốc gia lần thứ 15 được tổ chức vô cùng hoành tráng tại trung tâm hội nghị quốc tế... |

### Bác Sĩ Đông Y Bị Đuổi Khỏi Viện Phổi, Mũi Kim Thần Đông Tây Kết Hợp Vả Sập Tập Đoàn Phản Bội

- Link: https://doctieuthuyet.com/truyen/bac-si-dong-y-bi-duoi-khoi-vien-phoi-va-sap-tap-doan/
- Mô tả: 317 từ. Ổn.
- Mở đầu mô tả: Cút khỏi Viện Phổi Quốc tế ngay lập tức Loại bác sĩ Đông y quèn chỉ biết bốc lá cây và châm cứu rác rưởi như mày không xứng đáng đứng chung hàng ngũ với chúng tao Lời mắng chửi tàn nhẫn...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1148 | Ổn | Tiếng mưa giông rền rĩ ngoài cửa kính lớn của phòng họp giao ban tầng năm Viện Phổi Quốc tế Việt Đức vang lên... |
| 2 | 1192 | Ổn | Cơn mưa đêm Hà Nội mỗi lúc một nặng hạt từng hạt mưa quất liên tiếp vào cửa kính xe Maybach màu đen sang... |
| 3 | 1113 | Ổn | Ánh nắng sớm mai ấm áp của mùa thu Hà Nội khẽ xuyên qua những kẽ lá sấu già cổ kính đổ những vệt... |
| 4 | 1029 | Ổn | Tại căn phòng tổng giám đốc lộng lẫy và hiện đại của Viện Phổi Quốc tế Việt Đức bầu không khí vô cùng hân... |
| 5 | 1087 | Ổn | Bên ngoài văn phòng chủ tịch của liên doanh Vạn An Trần Gia những hạt mưa thu Hà Nội quất mạnh vào lớp kính... |
| 6 | 1009 | Ổn | Đêm muộn trước ngày diễn ra Hội thảo Y học Hô hấp Quốc gia chấn động giới y học sương mù mùa thu mờ... |
| 7 | 1124 | Ổn | Trung tâm Hội nghị Quốc gia Hà Nội chiều hôm đó rực rỡ dưới hàng ngàn ánh đèn LED công suất lớn vô cùng... |
| 8 | 1059 | Ổn | Giữa lúc cả hội trường lớn của Trung tâm Hội nghị Quốc gia đang chìm trong sự hỗn loạn hoảng sợ tột đỉnh và... |

### Thần Đồng Piano Nhạc Viện: Bị Cấm Biểu Diễn, Tôi Chấn Động Chopin Competition

- Link: https://doctieuthuyet.com/truyen/than-dong-piano-nhac-vien-bi-cam-bieu-dien-toi-chan-dong-chopin-competition/
- Mô tả: 138 từ. Ổn.
- Mở đầu mô tả: Một đứa không cha không mẹ sống bằng học bổng như cậu lấy tư cách gì đòi đứng chung hàng ngũ với con trai tôi ở đấu trường quốc tế Lâm Hoàng Phúc bị cướp đi bản giao hưởng độc tấu piano...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1119 | Ổn | Tiếng đàn Steinway Sons vang vọng khắp phòng hòa nhạc lớn của Nhạc viện Thành phố Hồ Chí Minh trên đường Nguyễn Du Lâm... |
| 2 | 1305 | Ổn | Trời Sài Gòn đổ cơn mưa rào lớn nước mưa xối xả trút xuống những con đường Quận 1 Lâm Hoàng Phúc ôm chặt... |
| 3 | 1115 | Ổn | Chiều tối hôm đó Trần Diệu Linh đưa Lâm Hoàng Phúc về căn biệt thự cổ kính của cô nằm ven sông Sài Gòn... |
| 4 | 1258 | Ổn | Ánh đèn chùm pha lê rực rỡ tỏa ánh sáng lộng lẫy xuống đại sảnh Nhà hát Thành phố tại trung tâm Quận 1... |
| 5 | 1262 | Ổn | Sáng hôm sau trang chủ chính thức của Chopin Competition tại Warsaw Ba Lan công bố danh sách thí sinh chính thức bước vào... |
| 6 | 1059 | Ổn | Trước ngày diễn ra buổi họp báo chính thức của Lâm Hoàng Phúc mạng xã hội âm nhạc cổ điển Việt Nam bùng nổ... |
| 7 | 1268 | Ổn | Cơn gió lạnh buốt của mùa đông Ba Lan thổi qua những hàng cây rụng lá dọc theo đại lộ Krakowskie Przedmieście Warsaw chào... |
| 8 | 1081 | Ổn | Trong khi Lâm Hoàng Phúc đang tỏa sáng rực rỡ tại Warsaw thì tại Việt Nam một trận cuồng phong pháp lý đã chính... |
| 9 | 1142 | Ổn | Đêm chung kết của cuộc thi piano danh giá nhất hành tinh Chopin Competition lần thứ 19 chính thức diễn ra Khán phòng của... |
| 10 | 1044 | Ổn | Sáng ngày tiếp theo buổi lễ trao giải chính thức của Chopin Competition lần thứ 19 được tổ chức trang trọng tại Nhà hát... |

### Nghệ Nhân Cacao Bị Vị Hôn Thê Đuổi Đi, Socola Trăm Tỷ Vả Sập Tập Đoàn Hóa Chất Ngày Hội Chợ

- Link: https://doctieuthuyet.com/truyen/nghe-nhan-cacao-bi-vi-hon-the-duoi-di-socola-tram-ty-va-sap-tap-doan-hoa-chat-ngay-hoi-cho/
- Mô tả: 392 từ. Cần sửa: mô tả dài (392 từ), nên cô lại
- Mở đầu mô tả: Trịnh Gia Bách anh chỉ là một thằng gác bếp lên men cacao quê mùa chân lấm tay bùn Thứ men rừng vô danh của anh không bằng một phần mười bột ca cao hóa chất nhập khẩu của Vạn Gia Ký...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1267 | Ổn | Cơn mưa dông tầm tã cuối chiều tháng Năm trút xuống đầu hẻm Quận 3 như muốn nhấn chìm cả thành phố Sài Gòn... |
| 2 | 1275 | Ổn | Cơn mưa tầm tã buốt giá dường như muốn trút hết mọi giận dữ xuống con đường Nam Kỳ Khởi Nghĩa sầm uất Trịnh... |
| 3 | 1136 | Ổn | Sáng hôm sau Trịnh Gia Bách có mặt tại tầng thượng của tòa nhà Bitexco Financial Tower theo lời mời chính thức của Nguyễn... |
| 4 | 1098 | Ổn | Trong khi đó tại căn hộ penthouse hai tầng lộng lẫy rộng hơn ba trăm mét vuông trị giá hàng chục tỷ đồng tọa... |
| 5 | 1261 | Ổn | Chỉ hai tuần trước khi diễn ra Hội chợ Triển lãm Specialty Food Expo quốc tế lớn nhất tại trung tâm SECC Quận 7... |
| 6 | 1058 | Ổn | Đêm hôm đó bên trong phòng nghiên cứu hiện đại của nhà máy An Nam tại Bến Tre không khí tĩnh lặng bao trùm... |
| 7 | 1068 | Ổn | Đúng 8 giờ sáng hôm sau thời hạn 24 giờ đình chỉ thanh tra kết thúc đột ngột trong sự ngỡ ngàng của toàn... |
| 8 | 943 | Ổn | Triển lãm Vietnam International Specialty Food Expo diễn ra vô cùng hoành tráng tại sảnh lớn của trung tâm hội nghị SECC Quận 7... |

### Vua Trà Shan Tuyết Bị Hào Môn Đuổi Khỏi Cửa Lật Kèo Nhờ Bằng Sáng Chế Trăm Tỷ Tiễn Kẻ Phản Bội

- Link: https://doctieuthuyet.com/truyen/vua-tra-shan-tuyet-bi-hao-mon-duoi-khoi-cua-lat-keo-nho-bang-sang-che-tram-ty-tien-ke-phan-boi/
- Mô tả: 313 từ. Ổn.
- Mở đầu mô tả: Loại nghèo hèn bốc mùi bùn đất như mày thì lấy gì làm sính lễ bước vào hào môn Lâm Gia Mang mấy cân lá trà dại hái trên vách đá khô cằn Hoàng Su Phì này đi cút khỏi đây ngay...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1142 | Ổn | Đêm mưa Hà Nội lạnh buốt thấu xương nhưng bầu không khí bên trong khán phòng VIP của khách sạn Sofitel Legend Metropole lại... |
| 2 | 1307 | Ổn | Ba ngày sau khi chịu đựng sự sỉ nhục cay đắng tại Hà Nội Lê Trọng Nhân đã trở lại căn nhà gỗ nhỏ... |
| 3 | 1376 | Ổn | Bão tố thực sự ập xuống vùng núi Hoàng Su Phì vào ngày tiếp theo khi những tia nắng hiếm hoi vừa le lói... |
| 4 | 1283 | Ổn | Chiều muộn sương mù Hoàng Su Phì dày đặc như những dải lụa trắng xóa bao phủ lấy xưởng chè đang bị niêm phong... |
| 5 | 1394 | Ổn | Trong căn phòng họp nhỏ của xưởng chè lúc nửa đêm ánh đèn dầu ấm áp xua đi cái lạnh buốt của núi rừng... |
| 6 | 1269 | Ổn | Khán phòng Đại yến của Trung tâm Hội nghị Quốc gia Hà Nội ngập tràn trong ánh sáng rực rỡ và âm nhạc cổ... |
| 7 | 1401 | Ổn | Giữa tiếng la hét hỗn loạn và tiếng còi báo động nháo nhác của hội trường Trung tâm Hội nghị Quốc gia cánh cửa... |
| 8 | 1135 | Ổn | Sáng hôm sau phòng họp báo khẩn cấp tại Bệnh viện Đại học Y Hà Nội chật kín phóng viên báo chí và các... |

### THẦN Y BỊ ĐUỔI, VỢ CŨ HỐI HẬN MUỘN MÀNG

- Link: https://doctieuthuyet.com/truyen/than-y-bi-duoi-vo-cu-hoi-han-muon-mang/
- Mô tả: 182 từ. Ổn.
- Mở đầu mô tả: Anh cống hiến sáu năm ròng rã cứu sống hàng ngàn người nhưng đến ngày bài thuốc gan gia truyền của anh có kết quả kiểm nghiệm đột phá họ vu oan anh kê đơn sai gây chết người rồi đuổi anh...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1484 | Ổn | Tờ quyết định sa thải được đặt trên bàn làm việc của Lương Minh Khải vào đúng 7 giờ sáng thứ Hai lạnh lẽo... |
| 2 | 1347 | Ổn | Quán cà phê cổ kính nằm trên phố Tràng Tiền chỉ có đúng ba bàn khách vào buổi sáng giữa tuần lạnh giá Trần... |
| 3 | 1214 | Ổn | Ông nội của Lương Minh Khải cụ Lương Văn Đạo năm nay đã bước sang tuổi bảy mươi hai Cụ sống tĩnh lặng trong... |
| 4 | 1150 | Ổn | Ba tuần trôi qua kể từ ngày bị sa thải khỏi bệnh viện Hà Thành Khải lúc này đang miệt mài làm việc trong... |
| 5 | 1230 | Ổn | Bước sang tuần thứ năm sau khi Khải rời khỏi bệnh viện Hà Thành Hùng người bạn thân thiết nhất từ thời đại học... |
| 6 | 1235 | Ổn | Hai tháng sau ngày bị sa thải khỏi bệnh viện Hà Thành Phòng họp lớn của Cục Sở hữu trí tuệ thuộc Bộ Khoa... |
| 7 | 1263 | Ổn | Hai mươi phút trôi qua trong sự căng thẳng tột độ ở hành lang phòng chờ của Cục Sở hữu trí tuệ Cánh cửa... |
| 8 | 1335 | Ổn | Bốn tháng sau ngày bị sa thải khỏi bệnh viện Hà Thành Lễ ký kết hợp đồng hợp tác chiến lược toàn diện giữa... |

### Kiến Trúc Sư Phố Cổ Hà Nội: Bị Cướp Bản Vẽ Di Sản, Tôi Cứu Cả Khu Phố

- Link: https://doctieuthuyet.com/truyen/kien-truc-su-pho-co-ha-noi-bi-cuop-ban-ve-di-san-toi-cuu-ca-khu-pho/
- Mô tả: 174 từ. Ổn.
- Mở đầu mô tả: Một kẻ xuất thân từ gia đình nghèo hèn không tiền không thế như mày thì lấy tư cách gì đòi bảo vệ di sản của Thăng Long hả Tuấn Bản vẽ này từ nay mang tên tao còn mày thì chuẩn...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1288 | Ổn | Tiếng mưa đêm phố cổ rơi lộp bộp trên những mái ngói rêu phong của ngõ Phất Lộc Bên trong căn nhà cổ hai... |
| 2 | 1248 | Ổn | Tòa nhà Sở Quy hoạch Kiến trúc Hà Nội tọa lạc trên con phố Tràng Thi sầm uất sáng rực ánh đèn giữa buổi... |
| 3 | 1205 | Ổn | Chiều muộn gió từ Hồ Tây thổi vào mang theo hơi nước mát lạnh làm dịu đi cái nóng hầm hập của mùa hè... |
| 4 | 1451 | Ổn | Đồng hồ điểm mười hai giờ đêm phố cổ Hàng Bạc chìm trong màn sương mù và những hạt mưa phùn mùa hạ Bên... |
| 5 | 1209 | Ổn | Sáng hôm sau trụ sở của Tập đoàn địa ốc Thịnh Phát tại khu đô thị mới Cầu Giấy hiện ra sừng sững như... |
| 6 | 1190 | Ổn | Bão tố thực sự bùng nổ tại văn phòng Sở Quy hoạch Kiến trúc Hà Nội vào buổi sáng ngày tiếp theo Hoàng Văn... |
| 7 | 1235 | Ổn | Tiếng sấm rền vang trên bầu trời Hà Nội báo hiệu một trận cuồng phong sắp đổ ập xuống thành phố Bên trong văn... |
| 8 | 1141 | Ổn | Trưa hè Hà Nội oi ả bỗng chốc bị xé toạc bởi một cơn giông cực mạnh kéo theo mưa gió bão bùng đổ... |
| 9 | 1123 | Ổn | Sáng hôm sau bầu trời Hà Nội sau cơn bão trở nên quang đãng và trong vắt như gương Tại khu đất vàng xung... |
| 10 | 1259 | Ổn | Một tháng sau ngày liên minh bẩn thỉu của Thịnh Phát bị triệt phá hoàn toàn dưới ánh sáng pháp luật Phố cổ Hàng... |

### Bác Sĩ Thẩm Mỹ Sài Gòn: Bị Vu Oan Phẫu Thuật Hỏng, Tôi Lật Mặt Cả Bệnh Viện

- Link: https://doctieuthuyet.com/truyen/bac-si-tham-my-sai-gon-bi-vu-oan-phau-thuat-hong-toi-lat-mat-ca-benh-vien/
- Mô tả: 165 từ. Ổn.
- Mở đầu mô tả: Ngô Hoàng Khải y đức và tay nghề của anh cũng chỉ đến thế thôi sao Cả đời này anh đừng mong chạm vào dao mổ nữa Giữa phòng họp lộng lẫy của Bệnh viện Thẩm mỹ Hoàng Gia Sài Gòn tại...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1284 | Ổn | Ánh đèn mổ LED công suất lớn rọi xuống bàn phẫu thuật tạo nên một vầng sáng lạnh lẽo nhưng cực kỳ tinh khiết... |
| 2 | 1290 | Ổn | Tiếng chuông điện thoại rít lên liên hồi trong đêm tĩnh mịch xé toạc không gian yên bình tại căn hộ chung cư cao... |
| 3 | 1250 | Ổn | Sáng hôm sau khi ánh nắng ban mai của Sài Gòn còn chưa kịp xua tan đi làn sương ẩm ướt của cơn mưa... |
| 4 | 1170 | Ổn | Trụ sở Sở Y tế Thành phố Hồ Chí Minh nằm trên đường Nguyễn Thị Minh Khai Quận 3 rợp bóng mát của những... |
| 5 | 1027 | Ổn | Buổi chiều muộn Khải hẹn gặp y tá trưởng Oanh tại một quán cà phê nhỏ nằm khuất trong một con hẻm yên tĩnh... |
| 6 | 1229 | Ổn | Đúng mười một giờ đêm Bệnh viện Thẩm mỹ Quốc tế Hoàng Gia Sài Gòn chìm trong sự im ắng tĩnh mịch dưới cơn... |
| 7 | 1348 | Ổn | Phân viện Kiểm nghiệm Thuốc Trung ương tại Thành phố Hồ Chí Minh nằm tĩnh lặng trên đường Quận 5 trung tâm của khu... |
| 8 | 1103 | Ổn | Buổi tối hôm đó một cơn gió mát lạnh từ hồ Con Rùa thổi qua những tán lá cây sao đen cổ thụ trên... |
| 9 | 1257 | Ổn | Tòa án hành chính của Sở Y tế Thành phố Hồ Chí Minh sáng hôm nay chật kín người từ rất sớm bầu không... |
| 10 | 1126 | Ổn | Những chiến sĩ cảnh sát kinh tế C03 nhanh chóng bước tới còng tay Trịnh Xuân Huy ngay tại bàn nghị sự trước sự... |

### Nữ Hoàng Trà Sen Tây Hồ: Bị Đuổi Khỏi Gia Tộc, Cô Xây Đế Chế Trà Nghìn Tỷ

- Link: https://doctieuthuyet.com/truyen/nu-hoang-tra-sen-tay-ho-bi-duoi-khoi-gia-toc-co-xay-de-che-tra-nghin-ty/
- Mô tả: 209 từ. Ổn.
- Mở đầu mô tả: Hơn một trăm năm Lê Gia Trà danh chấn Hà Thành nay lại để một đứa con gái đứng tên thừa kế sao Minh Nguyệt mày cút khỏi đầm sen Tây Hồ này ngay lập tức cho tao một cọng trà của...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1188 | Ổn | Cơn mưa phùn cuối đông Hà Nội quất từng đợt lạnh buốt vào những khung cửa kính của biệt thự cổ số 86 Tô... |
| 2 | 1115 | Ổn | Tiếng chuông chùa Trấn Quốc ngân vang trầm ấm giữa màn sương mù dày đặc bao phủ khắp Hồ Tây Lê Minh Nguyệt đứng... |
| 3 | 1235 | Ổn | Một gian nhà cổ nhỏ xập xệ nằm sâu trong ngõ phố Xuân Diệu nhìn thẳng ra một góc Hồ Tây lộng gió Đây... |
| 4 | 999 | Ổn | Gian nhà cổ nhỏ xập xệ ven Hồ Tây của Thiên Hương Trà bắt đầu rộn rã những bước chân của những vị khách... |
| 5 | 993 | Ổn | Đêm muộn ở phố Xuân Diệu một nhóm thanh niên xăm trổ hung hãn mang theo gậy sắt đột ngột xông vào gian nhà... |
| 6 | 1057 | Ổn | Ánh nắng ban mai dịu mát rọi xuống những đồi chè xanh mướt trải dài vô tận của vùng chè Tân Cương Thái Nguyên... |
| 7 | 1382 | Ổn | Không khí tại văn phòng tổng công ty Thiên Hương Trà đặt tại số 120 đường Xuân Diệu lúc này vô cùng khẩn trương... |
| 8 | 1336 | Ổn | Cơn bão truyền thông kinh hoàng và sự cố ngộ độc nghiêm trọng bất ngờ ập xuống đầu tập đoàn Lê Gia Trà vào... |
| 9 | 1316 | Ổn | Đại hội cổ đông bất thường của Công ty Cổ phần Lê Gia Trà được triệu tập vô cùng khẩn cấp tại hội trường... |
| 10 | 1228 | Ổn | Sau vụ bê bối chấn động dư luận cả nước của Lê Minh Hùng tập đoàn Lê Gia Trà chính thức rơi vào cảnh... |

### Thợ Nuôi Trai Bị Cướp Ngọc Đen Đuổi Khỏi Vịnh, Trở Lại Lật Kèo Đoạt Lại Tập Đoàn Ngọc Trai Nghìn Tỷ

- Link: https://doctieuthuyet.com/truyen/tho-nuoi-trai-bi-cuop-ngoc-den-duoi-khoi-vinh-tro-lai-lat-keo-doat-lai-tap-doan-ngoc-trai-nghin-ty/
- Mô tả: 267 từ. Cần sửa: tên truyện rất dài, dễ vỡ layout/SEO
- Mở đầu mô tả: Trịnh Hoàng Lâm cút khỏi vịnh Vân Đồn ngay lập tức Thứ nghèo hèn rách nát như mày không có tư cách sờ vào lồng trai của Royal Pearl Năm năm ròng rã dầm mưa dãi nắng giữa sóng gió vịnh Vân...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 752 | Ổn | Trịnh Hoàng Lâm cút khỏi vịnh Vân Đồn ngay lập tức Thứ nghèo hèn rách nát như mày không có tư cách sờ vào... |
| 2 | 772 | Ổn | Ba ngày sau khi bị trục xuất khỏi vịnh Vân Đồn Trịnh Hoàng Lâm ngồi trong phòng VIP của một khách sạn năm sao... |
| 3 | 734 | Ổn | Nhờ nguồn vốn khổng lồ một trăm năm mươi tỷ đồng được giải ngân nhanh chóng và sòng phẳng từ Vạn An Capital Trịnh... |
| 4 | 720 | Ổn | Sự sỉ nhục của Trần Thế Hùng khiến Huỳnh Gia Kiệt điên tiết tột độ Hắn quyết định không dùng đến các biện pháp... |
| 5 | 641 | ngắn (641 từ) | Cơn bão đi qua để lại một vùng biển Cô Tô lặng gió nhưng Trịnh Hoàng Lâm thì rơi vào tình trạng nguy kịch... |
| 6 | 553 | ngắn (553 từ) | Năm ngày sau biến cố bão tố Trịnh Hoàng Lâm đã hoàn toàn bình phục nhờ phương pháp Đông Tây y kết hợp hoàn... |
| 7 | 585 | ngắn (585 từ) | Triển lãm Trang sức Quốc tế Đà Nẵng diễn ra vô cùng hoành tráng tại Trung tâm Hội nghị Quốc tế bên bờ sông... |
| 8 | 712 | Ổn | Giữa tiếng xôn xao náo loạn của toàn thể hội trường triển lãm Trịnh Hoàng Lâm trong bộ vest xám lịch lãm sải bước... |

### Vua Lúa Gạo Đồng Tháp: Nông Dân Bị Ép Giá, Tôi Xây Đế Chế Gạo Xuất Khẩu

- Link: https://doctieuthuyet.com/truyen/vua-lua-gao-dong-thap-nong-dan-bi-ep-gia-toi-xay-de-che-gao-xuat-khau/
- Mô tả: 157 từ. Ổn.
- Mở đầu mô tả: Đất này là của tao lúa này tao muốn mua giá nào là quyền của tao Mày không bán cho Đại Đạt này thì cứ để mặc ba trăm tấn lúa ST25 đó thối rữa ngoài đồng đi Lời tuyên bố ngạo...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1488 | Ổn | Cơn gió chiều hanh hao từ sông Tiền thổi qua cánh đồng lúa huyện Lấp Vò mang theo hương thơm ngọt ngào của lúa... |
| 2 | 1350 | Ổn | Đêm Đồng Tháp tĩnh mịch trôi qua trong sự lo âu tột cùng của ba mươi hộ dân thuộc tổ hợp tác Sen Vàng... |
| 3 | 1167 | Ổn | Sau đêm giải cứu lúa lịch sử lò sấy công nghệ cao tại Sa Đéc đã hạ độ ẩm của ba trăm tấn thóc... |
| 4 | 1098 | Ổn | Dưới ánh nắng rực rỡ hắt xuống cảng xuất khẩu gạo Mỹ Thới bên dòng sông Hậu hiền hòa bầu không khí làm việc... |
| 5 | 1001 | Ổn | Sự điên cuồng của kẻ thua cuộc đã thúc đẩy Huỳnh Đạt tìm đến một liên minh đen tối và thâm độc hơn gấp... |
| 6 | 1115 | Ổn | Khủng hoảng thực sự bùng nổ khi thế lực hắc ám phía sau Huỳnh Đạt bắt đầu kích hoạt chiến dịch truyền thông bẩn... |
| 7 | 1051 | Ổn | Ngay trong đêm xảy ra khủng hoảng nghiêm trọng Nguyễn Thị Cẩm Tú cùng các cộng sự khoa học đã đáp chuyến bay khẩn... |
| 8 | 1034 | Ổn | Với đầy đủ chứng cứ khoa học từ Cẩm Tú và hồ sơ theo dõi bí mật của Tùng đòn phản công pháp lý... |
| 9 | 1006 | Ổn | Sự sụp đổ của đế chế thương lái Đại Đạt đã mở ra một trang sử mới hoàn toàn cho nông nghiệp vùng Đồng... |
| 10 | 1032 | Ổn | Ngày khánh thành nhà máy chế biến gạo hữu cơ Sen Vàng tại cảng Mỹ Thới diễn ra trong không khí lễ hội vô... |

### Người Đưa Thư Bị Cả Tòa Nhà Khinh, Hóa Ra Anh Là Chủ Toàn Bộ Tháp

- Link: https://doctieuthuyet.com/truyen/nguoi-dua-thu-bi-ca-toa-nha-cao-cap-coi-thuong-anh-la-chu-so-huu-toa-nha-do/
- Mô tả: 133 từ. Ổn.
- Mở đầu mô tả: Trong một tòa nhà văn phòng hiện đại ở trung tâm Hà Nội người đưa thư Đinh Xuân Phú trở thành mục tiêu chế giễu của mọi người Nhưng không ai biết rằng đằng sau bộ dạng bình dị ấy là một...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1000 | Ổn | Đinh Xuân Phú đứng giữa sảnh tòa nhà cao tầng nơi mà ánh đèn neon rực rỡ chiếu sáng như ban ngày Áo sơ... |
| 2 | 891 | Ổn | Bích Phượng ngồi bên chiếc bàn làm việc nhỏ nhắn ánh sáng từ chiếc đèn bàn vàng ấm áp chiếu rọi lên những trang... |
| 3 | 1010 | Ổn | Bích Phượng ngồi đối diện Đinh Xuân Phú trong quán cà phê nhỏ ở phố Tràng Tiền nơi mà ánh sáng vàng nhạt từ... |
| 4 | 979 | Ổn | Phú đứng bên cửa sổ văn phòng ánh mắt dõi theo đường phố nhộn nhịp bên dưới Những chiếc ô tô nối đuôi nhau... |
| 5 | 1046 | Ổn | Bích Phượng ngồi bên chiếc bàn làm việc ánh đèn neon từ bên ngoài chiếu vào tạo nên những bóng đổ kì quái trên... |
| 6 | 1015 | Ổn | Đinh Xuân Phú đứng trước cánh cửa của cơ quan chức năng nơi mà những ánh mắt châm chọc của những người từng khinh... |
| 7 | 1236 | Ổn | Không khí trong phòng họp của tòa nhà Diamond Tower trở nên nặng nề như một lớp sương mù dày đặc che khuất mọi... |
| 8 | 1099 | Ổn | Đinh Xuân Phú đứng giữa sảnh lớn của tòa nhà Bitexco Financial Tower ánh đèn neon lấp lánh phản chiếu trên mặt kính như... |

### Kỹ Sư Vắc Xin Bị Sa Thải Vì Không Gian Lận, Bản Quyền Vắc Xin Vả Sập Tập Đoàn Phản Bội

- Link: https://doctieuthuyet.com/truyen/ky-su-vac-xin-bi-sa-thai-vi-khong-gian-lan-ban-quyen-vac-xin-va-sap-tap-doan-phan-boi/
- Mô tả: 173 từ. Ổn.
- Mở đầu mô tả: Nếu các người dùng sinh mạng của hàng triệu đàn lợn cả nước để đánh cược cho một thương vụ IPO giả tạo tôi sẽ đưa cả gia tộc các người vào chốn lao tù Phát hiện vắc xin dịch tả lợn...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1073 | Ổn | Đèn huỳnh quang trong phòng thí nghiệm an toàn sinh học cấp 3 BSL 3 của Tập đoàn Khánh An tỏa ra thứ ánh... |
| 2 | 857 | Ổn | Lời từ chối đanh thép của Đăng Khoa như một gáo nước lạnh dội thẳng vào tham vọng nghìn tỷ của cha con nhà... |
| 3 | 1016 | Ổn | Trong khi Nguyễn Đăng Khoa đang đứng trước bờ vực của sự cô độc và khốn cùng tại trụ sở của Tập đoàn Nông... |
| 4 | 974 | Ổn | Sự hợp tác giữa Nguyễn Đăng Khoa và Tập đoàn Vạn An lập tức vấp phải sự cản trở tàn bạo từ liên minh... |
| 5 | 896 | Ổn | Cuộc chiến sinh tử tại trang trại Xuân Lộc bước vào giai đoạn nghẹt thở nhất Dưới sự chỉ đạo trực tiếp của Nguyễn... |
| 6 | 870 | Ổn | Trận chiến tại trang trại Xuân Lộc kết thúc thắng lợi rực rỡ mở đường cho sự lật kèo toàn diện của Nguyễn Đăng... |
| 7 | 1060 | Ổn | Ngày định mệnh cuối cùng cũng đã đến Trung tâm Hội nghị Quốc gia Hà Nội hôm nay được trang hoàng vô cùng lộng... |
| 8 | 774 | Ổn | Cơn bão chấn động giới y dược và nông nghiệp Việt Nam cuối cùng cũng qua đi để lại một bầu trời quang đãng... |

### Ông Trùm Logistics Tân Cảng: Bị Phản Bội Mất Container Nghìn Tỷ, Tôi Thâu Tóm Ngược

- Link: https://doctieuthuyet.com/truyen/ong-trum-logistics-tan-cang-bi-phan-boi-mat-container-nghin-ty-toi-thau-tom-nguoc/
- Mô tả: 119 từ. Ổn.
- Mở đầu mô tả: Hưng mày nghĩ mình là ai Ở cái Cảng Cát Lái này không có chữ ký của tao đống container nghìn tỷ kia chỉ là sắt vụn Phạm Gia Hưng giám đốc trẻ đầy thực lực của một công ty logistics lớn...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1391 | Ổn | Tiếng mưa xối xả trút xuống những rặng cẩu trục khổng lồ của Cảng Cát Lái tiếng động cơ gầm rú của những chiếc... |
| 2 | 1299 | Ổn | Chiếc xe hơi hiệu Volvo màu đen tuyền lướt êm ru qua những con đường ngập nước của bán đảo Thảo Điền Quận 2... |
| 3 | 1026 | Ổn | Ba ngày sau cuộc gặp mật tại Thảo Điền một bầu không khí căng thẳng bao trùm khắp các bãi container tại cảng Cát... |
| 4 | 1205 | Ổn | Mười giờ tối mưa trên sông Sài Gòn vẫn rơi không ngớt mặt nước đen ngòm phản chiếu ánh đèn đường nhấp nhô như... |
| 5 | 1232 | Ổn | Sáng hôm sau bầu trời Sài Gòn sau cơn mưa đêm trở nên trong vắt ánh nắng sớm vàng nhạt hắt lên những ô... |
| 6 | 1081 | Ổn | Sau cú sốc chấn động diễn ra tại khách sạn Park Hyatt công ty Hải Nam của Trần Thế Hải lập tức rơi vào... |
| 7 | 1027 | Ổn | Đêm muộn tại khu vực bãi bốc xếp số 4 của Cảng Cát Lái bầu không khí trở nên tĩnh mịch và căng thẳng... |
| 8 | 1015 | Ổn | Sáng hôm sau thông tin chi tiết về vụ triệt phá đường dây buôn lậu gỗ quý nghìn tỷ tại cảng Cát Lái và... |
| 9 | 1051 | Ổn | Một tuần sau cuộc thâu tóm ngược ngoạn mục Trần Thế Hải dưới sự bảo lãnh tạm thời của luật sư vì lý do... |
| 10 | 1048 | Ổn | Ba tháng sau cơn địa chấn tài chính tài cảng Cát Lái toàn bộ vụ án buôn lậu gỗ quý quy mô lớn của... |

### Nghệ Nhân Trà Sen Bị Khinh Rẻ Trục Xuất, Lật Kèo Đêm Hội Trà Quốc Tế Đưa Kẻ Phản Bội Vào Tù

- Link: https://doctieuthuyet.com/truyen/nghe-nhan-tra-sen-bi-khinh-re-truc-xuat-lat-keo-dem-hoi-tra-quoc-te-dua-ke-phan-boi-vao-tu/
- Mô tả: 165 từ. Ổn.
- Mở đầu mô tả: Đêm mưa bão tại đầm sen Tây Hồ Quảng An nghệ nhân trà trẻ tuổi Duy Anh chịu đựng sự sỉ nhục tột cùng Lê Hoài Nam CEO của Trà Hoài Nam Corp cấu kết với mụ Lan để tịch thu đầm...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1076 | Ổn | Mặt hồ Tây Hồ sáng sớm tháng Sáu lăn tăn gợn sóng bạc dưới làn gió hiu hiu thổi từ phía đông nam mang... |
| 2 | 1478 | Ổn | Quán trà Nguyệt Hồ nằm lùi sâu vào con ngõ nhỏ trên phố Từ Hoa phường Quảng An quận Tây Hồ cách mặt hồ... |
| 3 | 1384 | Ổn | Buổi sáng ngày thứ ba của tháng Tư sương Hồ Tây còn chưa tan hết trên mặt nước thì hai chiếc xe bán tải... |
| 4 | 1424 | Ổn | Phòng thí nghiệm của Vạn An Capital nằm ở tầng hầm tòa nhà trụ sở trên phố Láng Hạ lạnh và im lặng như... |
| 5 | 1441 | Ổn | Khách sạn InterContinental Westlake Hà Nội sáng rực ánh đèn từ tầng một đến tầng bảy mặt tiền kính cường lực phản chiếu lại... |
| 6 | 1414 | Ổn | Tiếng nhạc dân tộc vừa dứt thì một tiếng ho khan xé toạc bầu không khí ấm áp của Đêm hội trà quốc tế... |
| 7 | 1414 | Ổn | Ánh đèn sân khấu chính của Đêm Hội Trà Quốc Tế tại khu nhà thủy tạ phường Quảng An quận Tây Hồ Hà Nội... |
| 8 | 1469 | Ổn | Hội trường khách sạn Sofitel Legend Metropole im phắc như tờ Không ai nói một lời Không ai dám thở mạnh Chỉ có tiếng... |

### Bị Đuổi Khỏi Lab Đêm Trước IPO, Hóa Ra Anh Nắm Công Thức Trăm Tỷ

- Link: https://doctieuthuyet.com/truyen/ky-su-son-mai-bi-duoi-khoi-lab-hop-dong-sinh-hoc-tram-ty-lat-keo-phut-chot-ngay-ipo/
- Mô tả: 109 từ. Ổn.
- Mở đầu mô tả: Có những thứ bị cướp đi không phải bằng vũ lực mà bằng một tờ giấy một chữ ký và một cái bắt tay sau cánh cửa phòng lạnh Trần Hữu Nam biết điều đó hơn ai hết Anh mất ba năm...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 706 | Ổn | Mưa bắt đầu từ chín giờ tối loại mưa tháng Năm Hà Nội đổ xuống không báo trước nặng và dày như ai dốc... |
| 2 | 682 | ngắn (682 từ) | Làng Hạ Bằng cách trung tâm Hà Nội hơn hai mươi kilômet nằm ép mình giữa cánh đồng lúa chín vàng và dãy xưởng... |
| 3 | 744 | Ổn | Quỹ Đầu tư Xanh Vạn An đặt văn phòng tại tầng mười lăm tòa nhà Cornerstone đường Láng Hạ quận Đống Đa Nam đến... |
| 4 | 590 | ngắn (590 từ) | Cục Sở Hữu Trí Tuệ nằm tại số 386 Nguyễn Chí Thanh tòa nhà màu vàng nhạt bốn tầng cửa kính xanh phản chiếu... |
| 5 | 600 | ngắn (600 từ) | Chiến dịch bắt đầu lúc sáu giờ sáng thứ Năm khi một bài viết xuất hiện trên trang tin tức kinh doanh có lượng... |
| 6 | 638 | ngắn (638 từ) | Trung tâm Giám định Kỹ thuật số của Bộ Công an tiếp nhận USB lúc bốn giờ bốn mươi lăm chiều năm phút trước... |
| 7 | 577 | ngắn (577 từ) | Bốn ngày sau khi nộp đơn lên NOIP điện thoại của Nam nhận được cuộc gọi từ số cố định lạ đầu số Hà... |
| 8 | 640 | ngắn (640 từ) | Phiên giám định tại NOIP diễn ra lúc tám giờ sáng thứ Hai trong phòng họp tầng ba tòa nhà 386 Nguyễn Chí Thanh... |
| 9 | 610 | ngắn (610 từ) | Sự kiện IPO của Tập đoàn Mỹ Nghệ Hoàng Gia được tổ chức tại Grand Ballroom tầng hai của khách sạn InterContinental Hồ Tây... |
| 10 | 445 | ngắn (445 từ) | Ủy ban Chứng khoán Nhà nước ra quyết định đình chỉ hồ sơ đăng ký IPO của Tập đoàn Mỹ Nghệ Hoàng Gia vào... |
| 11 | 607 | ngắn (607 từ) | Tháng Bảy làng Hạ Bằng vào mùa phơi vóc Những tấm vải màn đã qua nước sơn đầu được căng ra trên giá tre... |

### Giáo Viên Làng Bị Hiệu Trưởng Sỉ Nhục, Bộ Giáo Dục Bổ Nhiệm Anh Làm Thanh Tra

- Link: https://doctieuthuyet.com/truyen/giao-vien-lang-bi-hieu-truong-khinh-thuong-bo-giao-duc-bo-nhiem-anh-lam-thanh-tra-dac-biet/
- Mô tả: 144 từ. Ổn.
- Mở đầu mô tả: Trong một ngôi làng nhỏ ở Ba Vì Lê Thanh Bình một giáo viên tận tâm bị hiệu trưởng Trần Hữu Đạo sỉ nhục trước mặt học sinh Vũ Thu Hà một nữ luật sư sắc sảo quyết định đứng về phía...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 949 | Ổn | Trời chiều ở Ba Vì những tia nắng cuối cùng của ngày dần tắt nhuộm vàng cả triền đồi Lê Thanh Bình đứng giữa... |
| 2 | 941 | Ổn | Trong một buổi chiều oi ả của Hà Nội ánh mặt trời chói chang chiếu qua cửa kính văn phòng luật sư tạo ra... |
| 3 | 849 | Ổn | Chiều muộn ánh nắng vàng rực rỡ xuyên qua những tán cây xanh mướt của trường Tiểu học Nguyễn Trãi tạo nên những vệt... |
| 4 | 1172 | Ổn | Trời Hà Nội đang vào mùa thu những cơn gió nhẹ nhàng thổi qua từng tán cây vàng lá nhưng không khí trong lòng... |
| 5 | 1036 | Ổn | Bình và Vũ Thu Hà đứng giữa một cánh đồng rộng lớn nơi mà ánh nắng mặt trời như thiêu đốt mọi thứ xung... |
| 6 | 895 | Ổn | Thời gian trôi qua và cuộc khủng hoảng đã kéo dài hơn 24 giờ khiến cho môi trường xung quanh trở nên ngột ngạt... |
| 7 | 1129 | Ổn | Vũ Thu Hà ngồi đối diện với Bình ánh đèn vàng ấm áp từ chiếc đèn bàn chiếu xuống tạo nên một không gian... |
| 8 | 957 | Ổn | Trong phòng họp của trường Trung học phổ thông Lê Quý Đôn không khí nặng nề như bao trùm bởi một làn sương mù... |

### Trọng Tài Bị Ngôi Sao Nhổ Nước Bọt, Hóa Ra Là Cựu Đội Trưởng Tuyển QG

- Link: https://doctieuthuyet.com/truyen/trong-tai-bong-da-bi-cau-thu-ngoi-sao-xuc-pham-hoa-ra-la-cuu-danh-thu-so-1-quoc-gia/
- Mô tả: 124 từ. Ổn.
- Mở đầu mô tả: Trong một trận đấu bóng đá căng thẳng tại sân vận động Thống Nhất trọng tài Trương Hùng Cường bất ngờ bị một ngôi sao bóng đá nổi tiếng nhổ nước bọt vào mặt Sự việc này không chỉ khiến Cường mất...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 859 | Ổn | Sân vận động Thống Nhất nơi mà những giấc mơ và hy vọng của hàng triệu người hâm mộ bóng đá Việt Nam hòa... |
| 2 | 1051 | Ổn | Cường quay về văn phòng của mình mặt mày ướt đẫm mồ hôi từng giọt mồ hôi lăn dài trên trán khiến anh cảm... |
| 3 | 906 | Ổn | Ánh nắng chiều lấp lánh trên mặt sân vận động Mỹ Đình nơi mà Nguyễn Gia Bảo vẫn thường tỏa sáng với những cú... |
| 4 | 882 | Ổn | Lê Mai Chi ngồi trước chiếc bàn gỗ cũ kỹ ánh đèn vàng vọt từ chiếc bóng đèn trên trần nhà chiếu xuống tạo... |
| 5 | 988 | Ổn | Cường đứng giữa căn phòng tối tăm ánh đèn vàng nhè nhẹ hắt lên gương mặt đầy lo âu của anh Hơi thở anh... |
| 6 | 1147 | Ổn | Trời Hà Nội hôm nay âm u những đám mây xám xịt như đang chuẩn bị đổ mưa nhưng không khí trong văn phòng... |
| 7 | 1180 | Ổn | Buổi chiều tại văn phòng của Gia Bảo ánh sáng vàng ấm từ chiếc đèn bàn phản chiếu lên những tờ giấy tán loạn... |
| 8 | 1070 | Ổn | Trời Hà Nội hôm nay u ám những đám mây xám xịt che khuất ánh mặt trời như thể đang chuẩn bị cho một... |

### Người Làm Vườn Bị Chủ Biệt Thự Đuổi, Hóa Ra Anh Thiết Kế Cả Khu Đô Thị

- Link: https://doctieuthuyet.com/truyen/nguoi-lam-vuon-bi-gia-dinh-chu-biet-thu-khinh-lo-ra-la-kien-truc-su-thiet-ke-ca-khu-do-thi-do/
- Mô tả: 120 từ. Ổn.
- Mở đầu mô tả: Vũ Quốc Hùng một người làm vườn tại một biệt thự hạng sang ở Hồ Chí Minh bị chủ nhà Nguyễn Lan Hương đuổi vì cho rằng công việc của anh không đủ tốt Nhưng đằng sau vẻ ngoài tầm thường Hùng...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 858 | Ổn | Vũ Quốc Hùng đang cúi thấp người chăm sóc từng khóm hoa trong khu vườn của biệt thự Nguyễn Lan Hương Ánh nắng vàng... |
| 2 | 916 | Ổn | Hùng ngồi bên bàn làm việc của mình ánh sáng từ chiếc đèn bàn hắt lên những trang giấy tờ lộn xộn những con... |
| 3 | 1096 | Ổn | Nguyễn Lan Hương ngồi giữa bầu không khí nặng nề của phòng họp ánh đèn neon chói chang phản chiếu lên khuôn mặt căng... |
| 4 | 1221 | Ổn | Hùng ngồi trước màn hình máy tính ánh sáng xanh nhấp nháy từ những bảng số liệu phản chiếu lên khuôn mặt anh Mồ... |
| 5 | 1025 | Ổn | Hùng ngồi tại bàn làm việc của mình ánh sáng vàng ấm áp từ chiếc đèn bàn chiếu lên những tài liệu rải rác... |
| 6 | 1093 | Ổn | Hùng đứng bên cửa sổ lớn của văn phòng ánh nắng mặt trời chiếu vào làm nổi bật những vết bụi trong không khí... |
| 7 | 1029 | Ổn | Trong căn phòng họp rộng lớn của công ty TNHH Đầu Tư Xây Dựng Hữu Chiến không khí ngột ngạt như có thể cắt... |
| 8 | 1160 | Ổn | Hùng đứng giữa căn phòng họp ngột ngạt của văn phòng Vạn Hoa Group ánh sáng chói chang từ những chiếc đèn neon phản... |

### Thợ Sửa Xe Bị Cả Xóm Khinh, Khi Đội Đua F1 Quốc Gia Tìm Đến Thuê Anh Làm Kỹ Sư Trưởng

- Link: https://doctieuthuyet.com/truyen/tho-sua-xe-bi-ca-xom-khinh-khi-doi-dua-f1-quoc-gia-tim-den-thue-anh-lam-ky-su-truong/
- Mô tả: 234 từ. Ổn.
- Mở đầu mô tả: Thợ sửa xe máy cùi bắp học nghề cũng dở mở tiệm cũng ế cả xóm này không ai thèm vào tiệm ông nữa đâu Tiệm sửa xe Đức Nghĩa nằm ở cuối hẻm 78 đường Trường Chinh quận Tân Bình Thành...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1177 | Ổn | Hẻm 78 đường Trường Chinh quận Tân Bình Thành phố Hồ Chí Minh nằm lẩn khuất giữa những tòa nhà cao tầng đang mọc... |
| 2 | 1217 | Ổn | Tiếng động cơ khẽ rít lên đoàn xe đen bóng loáng dừng lại ngay giữa hẻm 78 đường Trường Chinh Ánh sáng mặt trời... |
| 3 | 1127 | Ổn | Nguyễn Đức Nghĩa đứng giữa xưởng cơ khí nhỏ bé của mình ánh sáng từ những bóng đèn neon trên trần nhà chói lòa... |
| 4 | 1220 | Ổn | Mặt trời đã bắt đầu lặn dần ánh sáng vàng vọt len lỏi qua những rãnh mái tôn tô điểm cho không gian hẻm... |
| 5 | 1234 | Ổn | Mặt trời đã bắt đầu nhô cao trên bầu trời thành phố Hồ Chí Minh ánh sáng chói chang rọi vào từng góc ngách... |
| 6 | 1140 | Ổn | Nguyễn Đức Nghĩa ngồi lặng lẽ giữa tiệm sửa xe nhỏ bé của mình ánh sáng nhạt từ chiếc bóng đèn neon trên cao... |
| 7 | 1123 | Ổn | Trời Sài Gòn những cơn mưa mùa hạ bất chợt ập đến không khí ẩm ướt khiến mồ hôi đổ xuống từng giọt trên... |
| 8 | 1228 | Ổn | Ánh nắng chói chang chiếu xuống đường đua Mỹ Đình khiến mặt đường nhựa phản chiếu ánh sáng rực rỡ như một tấm gương... |

### Tài Xế Taxi Bị Khách VIP Khinh Thường, Tài Xế Đó Sở Hữu Công Ty Taxi Lớn Nhất Thành Tâm

- Link: https://doctieuthuyet.com/truyen/tai-xe-taxi-bi-khach-vip-khinh-thuong-tai-xe-do-so-huu-cong-ty-taxi-lon-nhat-thanh-tam/
- Mô tả: 350 từ. Cần sửa: mô tả dài (350 từ), nên cô lại
- Mở đầu mô tả: Cậu chỉ là một gã tài xế taxi truyền thống rác rưởi cả đời này cũng không ngẩng đầu lên được trước ứng dụng gọi xe công nghệ của chúng tôi Tại Sân bay Quốc tế Nội Bài lúc 14 giờ 37...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1316 | Ổn | Giữa sảnh Terminal 2 của Sân bay Quốc tế Nội Bài không khí như trở nên đặc quánh hơn khi ánh đèn huỳnh quang... |
| 2 | 1168 | Ổn | Trần Thanh Mai đứng trước tòa nhà Sunwah Tower 115 Nguyễn Huệ Quận 1 TP HCM không khỏi cảm thấy hồi hộp Ánh nắng... |
| 3 | 1154 | Ổn | Tầng 26 của Vietcombank Tower không gian rộng rãi và hiện đại ánh sáng mạnh từ các cửa kính lớn tạo nên khung cảnh... |
| 4 | 1182 | Ổn | Tại tầng 26 của tòa nhà Vietcombank Tower không khí trong phòng họp 26A căng thẳng như dây đàn bị kéo căng Những ánh... |
| 5 | 1133 | Ổn | Đêm Hà Nội đã buông xuống những ánh đèn neon từ các tòa nhà chọc trời phản chiếu lấp lánh trên mặt hồ Hoàn... |
| 6 | 1206 | Ổn | Trong không khí căng thẳng của phòng họp tại trụ sở chính của Go Fast Nguyễn Quốc Hùng CEO của công ty ngồi đối... |
| 7 | 1115 | Ổn | Ánh nắng chói chang chiếu rọi qua cửa kính lớn của tòa nhà Vietcombank Tower tạo nên những vệt sáng chói lọi trên nền... |
| 8 | 1540 | Ổn | Thứ Bảy tuần tiếp theo bầu trời Hà Nội vẫn mang sắc xanh của mùa hè ánh nắng len lỏi qua những tán cây... |

### Trợ Lý Bị Sếp Nữ CEO Ngược Đãi, Sếp Mới Của Cô Chính Là Anh Sau Thâu Tóm Công Ty

- Link: https://doctieuthuyet.com/truyen/tro-ly-bi-sep-nu-ceo-nguoc-dai-sep-moi-cua-co-chinh-la-anh-sau-thau-tom-cong-ty/
- Mô tả: 256 từ. Ổn.
- Mở đầu mô tả: Phạm Tuấn Khoa Anh có biết hồ sơ dự án anh làm không đúng tiêu chuẩn không Anh làm việc kiểu này thì đừng trách tôi ký giấy buộc thôi việc Phạm Tuấn Khoa trợ lý Giám đốc kinh doanh tại Công...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1263 | Ổn | Phạm Tuấn Khoa đứng im lặng giữa không gian rộng lớn của văn phòng tầng 14 Bitexco Financial Tower nơi ánh sáng tự nhiên... |
| 2 | 1214 | Ổn | Vũ Hoài An ngồi ở văn phòng tầng 15 của Bitexco Financial Tower nơi ánh sáng mặt trời chiếu qua những ô kính trong... |
| 3 | 1114 | Ổn | Sáng thứ Ba với bầu không khí ngột ngạt của thành phố Hồ Chí Minh Phạm Tuấn Khoa bước ra từ sảnh thang máy... |
| 4 | 1009 | Ổn | Chương 4 Cảnh Cáo Giữa Đêm Khuya 23 giờ đêm ánh đèn neon mờ ảo từ các tòa nhà cao tầng chiếu rọi xuống... |
| 5 | 1175 | Ổn | Phạm Tuấn Khoa đứng bên cửa sổ phòng họp HĐQT Gia Nguyên Holdings nơi mà ánh sáng mặt trời xuyên qua những tấm kính... |
| 6 | 1299 | Ổn | Phạm Tuấn Khoa đứng trước cánh cửa phòng họp lớn tại tầng 14 của Bitexco Financial Tower nhịp tim anh đập mạnh từng đợt... |
| 7 | 1320 | Ổn | Ánh sáng chói lóa từ các cửa sổ kính ở tầng 15 của Bitexco Financial Tower đổ xuống phản chiếu những khối hình hài... |
| 8 | 1150 | Ổn | Phạm Tuấn Khoa ngồi trong văn phòng mới của mình ở tầng 14 Bitexco Financial Tower ánh sáng mặt trời xuyên qua lớp kính... |

### Cô Gái Bán Hoa Bị Đuổi Khỏi Tiệc Cưới Hào Môn, Cùng Ngày Cô Gõ Sàn HOSE

- Link: https://doctieuthuyet.com/truyen/co-gai-ban-hoa-bi-dam-cuoi-nha-giau-duoi-ra-tap-doan-hoa-tuoi-cua-co-niem-yet-ngay-hom-do/
- Mô tả: 123 từ. Ổn.
- Mở đầu mô tả: Câu chuyện xoay quanh Phạm Thị Hương một cô gái bán hoa tại Hà Nội người có ước mơ lớn lao và đam mê kinh doanh Ngày hôm đó cô được mời đến một tiệc cưới hào môn nhưng không ngờ lại...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 737 | Ổn | Phạm Thị Hương đứng bên chiếc bàn gỗ lim bóng loáng đôi tay nắm chặt túi xách nhỏ xinh thận trọng quan sát không... |
| 2 | 1221 | Ổn | Phạm Thị Hương đứng giữa cửa hàng hoa nhỏ bé của mình nơi không gian tràn ngập hương thơm của những bông hoa tươi... |
| 3 | 1124 | Ổn | Phạm Thị Hương ngồi bên bàn làm việc ánh đèn vàng ấm áp trong căn phòng nhỏ phản chiếu lên những trang tài liệu... |
| 4 | 920 | Ổn | Phạm Thị Hương đứng giữa không gian rộng lớn của hội trường nơi ánh đèn chói lòa phản chiếu lên những chiếc bàn tiệc... |
| 5 | 1179 | Ổn | Phạm Thị Hương đứng giữa sảnh làm việc của cơ quan thi hành án trái tim cô đập rộn ràng như thể một nhạc... |
| 6 | 999 | Ổn | Phạm Thị Hương ngồi trước màn hình máy tính ánh sáng xanh nhấp nháy phản chiếu lên gương mặt cô làm nổi bật đôi... |
| 7 | 1136 | Ổn | Phạm Thị Hương đứng giữa phòng xử án ánh đèn chói lòa chiếu thẳng vào cô làm nổi bật từng đường nét trên khuôn... |
| 8 | 959 | Ổn | Phạm Thị Hương đứng trong căn phòng hội nghị lớn của công ty GreenFlora nơi mà ánh đèn rực rỡ chiếu sáng từng ngóc... |

### Con Trai Nuôi Bị Đuổi Ra Khỏi Tập Đoàn, Di Chúc Ông Nội Trao Lại 70% Cổ Phần

- Link: https://doctieuthuyet.com/truyen/con-trai-nuoi-bi-duoi-ra-khoi-tap-doan-di-chuc-ong-noi-trao-lai-70-co-phan/
- Mô tả: 218 từ. Ổn.
- Mở đầu mô tả: Con nuôi thì suốt đời là con nuôi không có chỗ trong Tập đoàn Minh Long đâu Ra đi đi đừng làm xấu mặt dòng họ Nguyễn Gia Khải con trai nuôi duy nhất của cố Chủ tịch Nguyễn Minh Long bị...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1113 | Ổn | Hà Nội sáng sớm ngày 15 tháng 3 ánh nắng nhẹ nhàng len lỏi qua những tán cây cổ thụ bên đường Lý Thường... |
| 2 | 1172 | Ổn | Ánh nắng buổi trưa len lỏi qua những tán cây xanh rì rào ngoài cửa sổ văn phòng tạo nên những vệt sáng vàng... |
| 3 | 1051 | Ổn | Nguyễn Gia Phú đứng trong văn phòng rộng rãi của mình tại tầng 20 tòa nhà Minh Long Tower ánh sáng chiếu vào từ... |
| 4 | 1026 | Ổn | Giữa cái nắng chói chang của Hà Nội vào giữa trưa dưới tán cây sấu cổ thụ ở đường Lý Thường Kiệt Nguyễn Gia... |
| 5 | 1289 | Ổn | Tại một căn phòng lớn thuộc tòa nhà sang trọng của Hội Đồng Gia Tộc nằm trên phố Hoàng Diệu ánh đèn vàng ấm... |
| 6 | 1166 | Ổn | Ánh nắng buổi chiều xuyên qua các tán cây xanh mướt ở con phố Nhân Hàng Hành tạo nên những mảng sáng tối đan... |
| 7 | 1350 | Ổn | Nguyễn Gia Phú ngồi tại văn phòng của mình ở tầng 20 của tòa nhà Minh Long Tower không gian xung quanh im ắng... |
| 8 | 1308 | Ổn | Ánh sáng từ những tấm kính lớn của phòng họp 18B tại tòa nhà Minh Long Tower chiếu rọi khắp không gian rộng lớn... |

### Chồng Nghèo Bị Họ Hàng Khinh Dự Tiệc Hào Môn, Hóa Ra Anh Là Khách Mời VIP Của Sự Kiện Đó

- Link: https://doctieuthuyet.com/truyen/chong-ngheo-bi-ho-hang-khinh-du-tiec-hao-mon-hoa-ra-anh-la-khach-moi-vip-cua-su-kien-do/
- Mô tả: 246 từ. Ổn.
- Mở đầu mô tả: Anh ấy không có chỗ ở tiệc này Nhà tôi mời người có địa vị không mời người làm thuê tháng năm triệu Lúc 7 giờ tối thứ Bảy tại biệt thự gia tộc nhà họ Trần ở khu Thảo Điền quận...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1151 | Ổn | Tại biệt thự gia tộc nhà họ Trần không khí trong sảnh rộng lớn tràn ngập sự xa hoa Những chiếc đèn chùm pha... |
| 2 | 1157 | Ổn | Quán cà phê ven sông Sài Gòn nơi mà ánh đèn lung linh phản chiếu trên mặt nước dường như là một thế giới... |
| 3 | 1430 | Ổn | Nguyễn Minh Tú đứng lặng lẽ bên ngoài quán cà phê ven sông Sài Gòn nơi mà những ánh đèn vàng ấm áp từ... |
| 4 | 1174 | Ổn | Khung cảnh bên trong biệt thự nhà họ Trần thật lộng lẫy ánh đèn chùm lung linh phản chiếu lên những chiếc bàn được... |
| 5 | 1136 | Ổn | Bầu không khí trong biệt thự nhà họ Trần vào buổi tối thứ Bảy trở nên căng thẳng như một sợi dây đàn kéo... |
| 6 | 1502 | Ổn | Khi tiếng nhạc nhẹ nhàng từ dàn loa Bose vang lên trong không gian sang trọng của biệt thự nhà họ Trần Nguyễn Minh... |
| 7 | 1175 | tên chương dài | Ánh đèn rực rỡ từ những chiếc đèn chùm pha lê sáng lấp lánh trong biệt thự nhà họ Trần bên ngoài không khí... |
| 8 | 1193 | Ổn | Ánh nắng ban mai tràn ngập không gian những tia sáng lấp lánh như hạt sương trên những nhành cây xanh mướt trong khu... |

### Vợ Đòi Ly Hôn Vì Chồng Thất Nghiệp, Ngày Ký Đơn Chồng Nhận Danh Hiệu Kiến Trúc Sư Quốc Gia

- Link: https://doctieuthuyet.com/truyen/vo-doi-ly-hon-vi-chong-that-nghiep-ngay-ky-don-chong-nhan-danh-hieu-kien-truc-su-quoc-gia/
- Mô tả: 178 từ. Ổn.
- Mở đầu mô tả: Kiến trúc sinh mệnh không phải là những khối bê tông vô hồn vươn lên giữa bầu trời ô nhiễm mà là sự hòa quyện tuyệt đối giữa hơi thở của đất mẹ tre đan truyền thống và công nghệ xanh bền...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 339 | ngắn (339 từ) | Căn nhà số 47 ngõ Lý Quốc Sư Hoàn Kiếm Hà Nội nhà ba tầng tường gạch cũ mái ngói đỏ đã bạc màu... |
| 2 | 383 | ngắn (383 từ) | Trần Khánh Vy ba mươi lăm tuổi Quản lý Dự án của Tập đoàn Địa ốc Phúc An vóc người cao ăn mặc luôn... |
| 3 | 331 | ngắn (331 từ) | Bốn ngày sau cuộc nói chuyện với Vy Minh nhận được email từ Ban Tổ chức Giải thưởng Kiến trúc Quốc gia giải thưởng... |
| 4 | 380 | ngắn (380 từ) | Văn phòng luật sư Ngô Thị Lan Phương nằm ở tầng sáu tòa nhà Hoàng Anh 25 Lý Thường Kiệt Hà Nội văn phòng... |
| 5 | 343 | ngắn (343 từ) | Hội Kiến trúc sư Việt Nam nhận được đơn phản đối chính thức của Lê Quang Minh vào ngày 28 tháng 10 hai tuần... |
| 6 | 288 | ngắn (288 từ) | Trần Khánh Vy ký vào tờ đơn ly hôn trước đặt bút xuống bàn công chứng viên tại phòng công chứng số 14 phố... |
| 7 | 376 | ngắn (376 từ) | Phiên chung kết Giải thưởng Kiến trúc Quốc gia 2025 tổ chức tại Trung tâm Hội nghị Quốc gia đường Phạm Hùng Hà Nội... |
| 8 | 380 | ngắn (380 từ) | Tháng Giêng năm sau Lê Quang Minh chuyển ra khỏi căn nhà số 47 ngõ Lý Quốc Sư Anh không chuyển đến chỗ lớn... |

### Cô Gái Làng Bị Nhà Trai Hào Môn Từ Chối, Startup Nông Nghiệp Của Cô Niêm Yết 500 Tỷ

- Link: https://doctieuthuyet.com/truyen/co-gai-lang-bi-nha-trai-hao-mon-tu-choi-startup-nong-nghiep-cua-co-niem-yet-500-ty/
- Mô tả: 124 từ. Ổn.
- Mở đầu mô tả: Hôm nay các người coi thường nông nghiệp hữu cơ xua đuổi tôi như một kẻ nghèo hèn vô dụng Ngày mai các người sẽ phải quỳ gối cầu xin tôi chia sẻ công nghệ vi sinh để cứu vớt cái tập...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 433 | ngắn (433 từ) | Biệt thự của nhà họ Lương nằm cuối con đường nhựa mới đổ ở phường Tân An thành phố Buôn Ma Thuột tòa nhà... |
| 2 | 380 | ngắn (380 từ) | Xã Đắk Minh huyện Đắk R lấp tỉnh Đắk Nông nơi Lan sinh ra là vùng đất đỏ bazan điển hình của Tây Nguyên... |
| 3 | 348 | ngắn (348 từ) | Hai năm sau ngày Lan trở về Đắk Minh diện tích thử nghiệm LAN 09 đã mở rộng từ mười hectare lên một trăm... |
| 4 | 341 | ngắn (341 từ) | Tập đoàn Thực phẩm Lương Phát của nhà Lương bắt đầu gặp rắc rối vào đúng mùa hạn hán năm thứ ba liên tiếp... |
| 5 | 323 | ngắn (323 từ) | Lan nhận được yêu cầu hợp tác từ Tập đoàn Lương Phát qua email của trợ lý Khoa lúc chín giờ sáng thứ Hai... |
| 6 | 335 | ngắn (335 từ) | Công ty kiểm toán KPMG Việt Nam hoàn thành báo cáo tài chính của Nông nghiệp Xanh LAN vào tháng Chín tám tháng trước... |
| 7 | 290 | ngắn (290 từ) | Phiên giao dịch đầu tiên của cổ phiếu LAN trên Sàn giao dịch Chứng khoán Thành phố Hồ Chí Minh diễn ra vào thứ... |
| 8 | 354 | ngắn (354 từ) | Bà Lương Thị Hạnh không gọi điện cho Lan sau ngày niêm yết Bà viết thư tay trên giấy trắng viền xanh bằng mực... |

### Thuyền Trưởng Tàu Cá Bị Chủ Cảng Ép Nợ, Hóa Ra Là Đại Gia Hàng Hải Đang Điều Tra Thâu Tóm

- Link: https://doctieuthuyet.com/truyen/thuyen-truong-tau-ca-bi-chu-cang-ep-no-hoa-ra-la-dai-gia-hang-hai-dang-dieu-tra-thau-tom/
- Mô tả: 196 từ. Ổn.
- Mở đầu mô tả: Nguyễn Hải Long ẩn thân làm thuyền trưởng một con tàu cá nhỏ suốt ba tháng tại cảng Hải Bình hứng chịu đủ sự chà đạp và ép nợ của tập dịch vụ bến cảng Trần Đại Nghĩa ông chủ cảng Hải...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 388 | ngắn (388 từ) | Cảng Hải Bình nằm ở cuối con đường nhựa đã bong tróc phía nam thị xã Đồ Sơn Hải Phòng nơi mùi muối biển... |
| 2 | 423 | ngắn (423 từ) | Trần Đại Nghĩa gặp Long lần đầu tiên vào buổi chiều thứ Năm trong văn phòng gỗ ép cũ nằm kề nhà kho số... |
| 3 | 461 | ngắn (461 từ) | Bão số 7 đổ bộ vào vịnh Bắc Bộ lúc mười một giờ đêm thứ Sáu gió giật cấp mười hai sóng cao bốn... |
| 4 | 427 | ngắn (427 từ) | Trịnh Minh Anh đến Hải Phòng lúc sáu giờ sáng thứ Bảy đi xe khách từ Hà Nội mặc áo khoác nhẹ màu xanh... |
| 5 | 349 | ngắn (349 từ) | Nghĩa gọi Long đến văn phòng lần thứ hai vào sáng Chủ Nhật Lần này có thêm hai người ngồi ở góc phòng anh... |
| 6 | 294 | ngắn (294 từ) | Xe của Bộ Công an đến cảng Hải Bình lúc hai giờ chiều Chủ Nhật hai xe Lexus đen không biển theo sau là... |
| 7 | 318 | ngắn (318 từ) | Phiên họp cổ đông bất thường của Công ty Cổ phần Dịch vụ Cảng Hải Bình được triệu tập khẩn cấp vào thứ Tư... |
| 8 | 454 | ngắn (454 từ) | Hải Long trở về Hà Nội vào một buổi sáng thứ Hai không bằng xe khách mà bằng chiếc Range Rover đen mà anh... |

### Trưởng Phòng Bán Hàng Khinh Nhân Viên Mới, Nhân Viên Đó Là Chuyên Gia Tư Vấn Của Tập Đoàn Mẹ

- Link: https://doctieuthuyet.com/truyen/truong-phong-ban-hang-khinh-nhan-vien-moi-nhan-vien-do-la-chuyen-gia-tu-van-cua-tap-doan-me/
- Mô tả: 220 từ. Ổn.
- Mở đầu mô tả: Trần Minh Hoàng ba mươi lăm tuổi một chuyên gia xoay chuyển tình thế doanh nghiệp lừng danh từng vực dậy hàng chục tập đoàn lớn quyết định ẩn thân làm nhân viên bán hàng thử việc tại một chi nhánh siêu...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 414 | ngắn (414 từ) | Chi nhánh Vạn An Plaza nằm ở góc đường Nguyễn Văn Cừ và Trần Phú thành phố Thành Tâm tỉnh lỵ của một tỉnh... |
| 2 | 346 | ngắn (346 từ) | Ba tuần đầu làm việc tại Vạn An Plaza Trần Minh Hoàng làm những việc sau bốc vác hàng hóa dọn dẹp khu vực... |
| 3 | 347 | ngắn (347 từ) | Lê Mai Chi ba mươi ba tuổi Giám đốc Pháp chế và Quản trị rủi ro của Tập đoàn VAN đơn vị mẹ sở... |
| 4 | 277 | ngắn (277 từ) | Tuần thứ tư Hoàng được Thắng giao việc phụ trách kiểm kê hàng tồn kho cuối tháng việc thường do nhân viên cũ làm... |
| 5 | 317 | ngắn (317 từ) | Phòng họp lớn tầng mười lăm tòa nhà VAN Tower có sức chứa sáu mươi người Ngày 18 tháng 11 phòng này có mặt... |
| 6 | 343 | ngắn (343 từ) | Hoàng trình bày trong bốn mươi hai phút Không cần phong cách hùng biện Chỉ cần số liệu biểu đồ và đối chiếu từng... |
| 7 | 310 | ngắn (310 từ) | Hợp đồng M A với Siam Retail được ký tắt ngay trong buổi chiều hôm đó điều kiện từ phía Thái Lan là VAN... |
| 8 | 367 | ngắn (367 từ) | Tuần cuối trước khi Hoàng chính thức nhận nhiệm vụ mới tại VAN Trưởng dự án Tái cơ cấu Quản trị Toàn chuỗi anh... |

### Nhà Chồng Khinh Tôi Không Biết Nấu Ăn, Tôi Giật Giải Đầu Bếp Số 1 Đông Nam Á Trước Mặt Họ

- Link: https://doctieuthuyet.com/truyen/nha-chong-khinh-toi-khong-biet-nau-an-toi-giat-giai-dau-bep-so-1-dong-nam-a-truoc-mat-ho/
- Mô tả: 99 từ. Ổn.
- Mở đầu mô tả: Lê Mai một đầu bếp xuất sắc sống dưới cái bóng của gia đình chồng cũ Bà mẹ chồng Hà Thịnh coi thường cô khinh bỉ món ăn cô làm Cao Hùng chồng cô ký đơn ly hôn ngay trong mưa tầm...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 742 | Ổn | Trời Hà Nội hôm nay mưa tầm tã những giọt nước lăn dài trên những tấm kính của biệt thự tạo nên âm thanh... |
| 2 | 905 | Ổn | Trong ánh đèn mờ ảo của nhà bếp Lê Mai ngồi lặng lẽ nhìn ngắm những dụng cụ nấu ăn xung quanh Đó là... |
| 3 | 906 | Ổn | Ánh nắng mặt trời chiếu rọi qua những tán cây xanh mát khiến bầu không khí Đà Nẵng trở nên rực rỡ hơn bao... |
| 4 | 1003 | Ổn | Ánh đèn lung linh của thành phố Đà Nẵng phản chiếu trên mặt biển tạo nên một khung cảnh đẹp như tranh vẽ nhưng... |
| 5 | 970 | Ổn | Lê Mai đứng lặng lẽ trong bếp nhỏ của căn hộ mình ánh đèn vàng hắt lên gương mặt cô tạo thành những bóng... |
| 6 | 1009 | Ổn | Ánh đèn rực rỡ chiếu sáng khắp không gian của đấu trường ẩm thực nơi mà cả hàng ngàn ánh mắt đang dõi theo... |
| 7 | 1112 | Ổn | Lê Mai đứng giữa căn bếp rộng lớn nơi mà mùi thơm của các loại gia vị hòa quyện vào nhau tạo nên một... |
| 8 | 899 | Ổn | Ánh đèn sân khấu chói lòa phản chiếu những giọt mồ hôi lăn dài trên trán Lê Mai khi cô đứng đối diện với... |

### Giáo Sư Đuổi Học Trò Ra Khỏi Lớp Vì Dốt, Học Trò Đó Là Tác Giả Giáo Trình Giáo Sư Đang Dạy

- Link: https://doctieuthuyet.com/truyen/giao-su-duoi-hoc-tro-ra-khoi-lop-vi-dot-hoc-tro-do-la-tac-gia-giao-trinh-giao-su-dang-day/
- Mô tả: 141 từ. Ổn.
- Mở đầu mô tả: Đinh Tuấn Anh cống hiến mười năm ròng rã tại Đại học Kỹ thuật Munich để viết nên thuật toán tối ưu hóa động lực học đa vật thể song song PMDO chấn động giới cơ điện tử toàn cầu Thế nhưng...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 548 | ngắn (548 từ) | Sáng thứ Hai đầu tháng Mười sương mù Hà Nội phủ dày trên mặt Hồ Tây như một tấm vải trắng chưa kịp dệt... |
| 2 | 391 | ngắn (391 từ) | Thưa Giáo sư phương trình ở slide 3 có lỗi ở số hạng thứ tư Giọng Tuấn Anh bình thản không hề có chút... |
| 3 | 515 | ngắn (515 từ) | Văn phòng Cục Sở hữu trí tuệ Việt Nam nằm trên đường Nguyễn Chí Thanh quận Đống Đa là nơi luật sư Phạm Hương... |
| 4 | 477 | ngắn (477 từ) | Hà Nội vào đêm cuối tháng Mười có cái lạnh của đợt gió mùa đông bắc đầu tiên trong năm loại lạnh ngấm qua... |
| 5 | 456 | ngắn (456 từ) | Buổi họp của Hội đồng Thẩm định kỹ thuật gói thầu được tổ chức tại Hội trường A của Bộ Y tế số 138A... |
| 6 | 382 | ngắn (382 từ) | Tin tức về phiên điều trần bất thường tại Bộ Y tế lan ra ngoài trước khi buổi họp kết thúc Trần Lan Anh... |
| 7 | 390 | ngắn (390 từ) | Bốn mươi tám giờ sau phiên điều trần là bốn mươi tám giờ Lê Hữu Phước hiểu thế nào là mất kiểm soát hoàn... |
| 8 | 415 | ngắn (415 từ) | Ba tháng sau Cơ quan Cảnh sát điều tra Bộ Công an ra kết luận điều tra sơ bộ đủ cơ sở khởi tố... |

### Bố Vợ Ép Ly Hôn Vì Tôi Nghèo Hèn, Công Ty Tỷ Đô Của Tôi Niêm Yết Sàn Chứng Khoán Hôm Đó

- Link: https://doctieuthuyet.com/truyen/bo-vo-ep-ly-hon-vi-toi-ngheo-hen-cong-ty-ty-do-cua-toi-niem-yet-san-chung-khoan-hom-do/
- Mô tả: 99 từ. Ổn.
- Mở đầu mô tả: Nguyễn Văn Dũng đã dành ba năm cống hiến để phát triển hệ thống logistics thông minh LogiChain Nhưng gia đình vợ anh chỉ nhìn thấy một kẻ nghèo hèn không có tương lai Vào đêm trước ngày LogiChain niêm yết trên...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 879 | Ổn | Nguyễn Văn Dũng ngồi thất thần trước màn hình máy tính đôi tay run rẩy khi thông báo chính thức từ sàn chứng khoán... |
| 2 | 1010 | Ổn | Nguyễn Văn Dũng đứng tại góc phòng khách ánh đèn vàng nhạt phản chiếu lên gương mặt anh làm nổi bật những nét mệt... |
| 3 | 1127 | Ổn | Ánh đèn neon chói lòa từ những tòa nhà chọc trời phản chiếu xuống mặt đường nhựa khiến cho không khí trong thành phố... |
| 4 | 996 | Ổn | Nguyễn Văn Dũng ngồi trầm ngâm bên bàn làm việc ánh đèn vàng quạnh quẽ chiếu rọi lên khuôn mặt anh nơi mà những... |
| 5 | 1194 | Ổn | Nguyễn Văn Dũng ngồi trong căn phòng nhỏ hẹp của mình ánh sáng mờ nhạt từ chiếc đèn bàn chiếu lên những tờ giấy... |
| 6 | 970 | Ổn | Hà Nội một buổi tối yên tĩnh nhưng bên trong lòng Nguyễn Văn Dũng là những cơn sóng dữ dội không ngừng cuộn trào... |
| 7 | 932 | Ổn | Nguyễn Văn Dũng đứng trước cánh cửa tòa án lòng anh như lửa đốt Những tiếng ồn ào từ bên trong vọng ra khiến... |
| 8 | 972 | Ổn | Nguyễn Văn Dũng đứng trước màn hình lớn của sàn giao dịch chứng khoán HOSE nhịp tim của anh đập như trống trận Các... |

### Giám Đốc Bệnh Viện Sa Thải Bác Sĩ Thực Tập, Hội Đồng Y Tế Quốc Gia Cử Người Điều Tra

- Link: https://doctieuthuyet.com/truyen/giam-doc-benh-vien-sa-thai-bac-si-thuc-tap-hoi-dong-y-te-quoc-gia-cu-nguoi-dieu-tra/
- Mô tả: 102 từ. Ổn.
- Mở đầu mô tả: Trong một đêm đầy bão tố tại Bệnh viện Đa khoa Quốc tế Thành Tâm sự thật bất ngờ được phơi bày Phạm Quốc Bảo một tiến sĩ y khoa tài năng quyết định ẩn danh để điều tra đường dây mổ...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1071 | Ổn | Trong một đêm đầy bão tố tại Bệnh viện Đa khoa Quốc tế Thành Tâm ánh đèn neon chập chờn như những ngọn đuốc... |
| 2 | 790 | Ổn | Ánh đèn neon chói lóa từ các phòng bệnh viện rọi vào bóng tối của hành lang dài hun hút tạo nên một không... |
| 3 | 952 | Ổn | Ánh đèn neon rực rỡ của quận Hoàn Kiếm sáng lấp lánh như những vì sao giữa đêm Hà Nội mờ ảo Phạm Quốc... |
| 4 | 1034 | Ổn | Khung cảnh văn phòng của Phạm Quốc Bảo ngập tràn ánh đèn vàng tạo nên không khí u ám của một cuộc chiến không... |
| 5 | 996 | Ổn | Ánh đèn neon mờ ảo của Bệnh viện Đa khoa Quốc tế Thành Tâm chiếu xuống sàn nhà ẩm ướt tạo ra những bóng... |
| 6 | 998 | Ổn | Ánh sáng của bệnh viện Đa khoa Quốc tế Thành Tâm lấp lánh trong đêm tối nhưng không khí ở đây lại ngột ngạt... |
| 7 | 965 | Ổn | Bệnh viện Đa khoa Quốc tế Thành Tâm vào lúc này như một chiếc nồi áp suất sôi sùng sục với những bí mật... |
| 8 | 991 | Ổn | Ngày hôm sau ánh nắng rực rỡ le lói qua những tấm kính của Bệnh viện Đa khoa Quốc tế Thành Tâm nhưng không... |

### Chàng Rể Ngọc Linh Lật Kèo Cứu Bị Cướp

- Link: https://doctieuthuyet.com/truyen/chang-re-ngoc-linh-bi-cuop-bang-sam-nghin-ty-lat-keo-dong-tay-y-dua-tap-doan-phan-boi-vao-tu/
- Mô tả: 148 từ. Ổn.
- Mở đầu mô tả: Ngày công bố thành quả Trần Hoàng Vũ đứng giữa rừng sâu Ngọc Linh ánh mắt lấp lánh niềm tự hào Nhưng chỉ sau một giây hắn cảm nhận được cú sốc khi gia đình vị hôn thê Phạm Gia những kẻ...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1037 | Ổn | Ngày công bố thành quả Trần Hoàng Vũ đứng giữa rừng sâu Ngọc Linh ánh mắt lấp lánh niềm tự hào Hắn không thể... |
| 2 | 1211 | Ổn | Ngày công bố thành quả Trần Hoàng Vũ đứng giữa rừng sâu Ngọc Linh ánh mắt lấp lánh niềm tự hào Hắn đã bỏ... |
| 3 | 1021 | Ổn | Ngày công bố thành quả Trần Hoàng Vũ đứng giữa rừng sâu Ngọc Linh ánh mắt lấp lánh niềm tự hào Hắn đã dành... |
| 4 | 1115 | Ổn | Trời đã dần ngả về chiều ánh sáng vàng rực rỡ của hoàng hôn len lỏi qua những tán cây tạo nên những mảng... |
| 5 | 1356 | Ổn | Giữa không gian tĩnh lặng của rừng Ngọc Linh Trần Hoàng Vũ đứng lặng ánh mắt tràn đầy quyết tâm Hình ảnh những cây... |
| 6 | 1042 | Ổn | Ngày thứ tư sau khi Trần Hoàng Vũ phát hiện ra sự phản bội tàn nhẫn của gia đình vị hôn thê Phạm Gia... |
| 7 | 1198 | Ổn | Ngày hôm nay tại Hội nghị Expo Quốc tế diễn ra tại trung tâm hội nghị lớn nhất Hà Nội không khí thật sự... |
| 8 | 1169 | Ổn | Ngày công bố thành quả Trần Hoàng Vũ đứng giữa rừng sâu Ngọc Linh ánh nắng xuyên qua tán lá tạo thành những vệt... |

### Sư Phụ Đuổi Tôi Khỏi Võ Quán Vì Hèn Yếu, Giải Vô Địch Quốc Gia Lộ Ra Thân Phận Thật

- Link: https://doctieuthuyet.com/truyen/su-phu-duoi-toi-khoi-vo-quan-vi-hen-yeu-giai-vo-dich-quoc-gia-lo-ra-than-phan-that/
- Mô tả: 111 từ. Ổn.
- Mở đầu mô tả: Trần Hải Phong cựu vô địch kickboxing giờ chỉ là kẻ lau dọn tại võ quán Thành Tâm xập xệ Cuộc đời anh thay đổi khi bị sư phụ Lý Bách vu khống hèn yếu nhát gan Không chấp nhận tham gia...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 963 | Ổn | Trần Hải Phong đứng tần ngần ở cửa võ quán Thành Tâm đôi tay gân guốc của anh nắm chặt cây chổi tre nhưng... |
| 2 | 821 | Ổn | Trần Hải Phong đứng một mình trong võ quán Thành Tâm nơi ánh đèn mờ nhạt chỉ đủ soi sáng những vết bụi bám... |
| 3 | 837 | Ổn | Trần Hải Phong đứng giữa căn phòng chật chội nơi từng là niềm tự hào của anh với những chiếc huy chương lấp lánh... |
| 4 | 876 | Ổn | Ánh đèn neon nhấp nháy trên con phố Trần Hưng Đạo nơi mà những chiếc xe máy hối hả lao đi như những bóng... |
| 5 | 902 | Ổn | Trần Hải Phong đứng giữa không gian chật chội của quán cà phê Tâm An nơi ánh đèn vàng hắt lên những bức tường... |
| 6 | 1114 | Ổn | Ánh đèn neon mờ ảo trong con hẻm tối tăm của quận Hoàn Kiếm dường như không thể xua đi cái cảm giác nặng... |
| 7 | 928 | Ổn | Hải Phong đứng giữa sàn đấu nơi ánh đèn chói lòa phản chiếu trên những bức tường phủ bụi nhịp tim của anh đập... |
| 8 | 935 | Ổn | Hải Phong đứng yên trong căn phòng nhỏ của võ quán Thành Tâm nơi mà anh từng gọi là nhà nhưng giờ đây chỉ... |

### Cô Vợ Hào Môn Khinh Tôi Vô Dụng, Cả Hà Ngoại Biết Tôi Là Chủ Tịch Tập Đoàn Thép

- Link: https://doctieuthuyet.com/truyen/co-vo-hao-mon-khinh-toi-vo-dung-ca-ha-ngoai-biet-toi-la-chu-tich-tap-doan-thep/
- Mô tả: 96 từ. Ổn.
- Mở đầu mô tả: Đêm mưa lạnh ở Hà Nội Trần Đông Hải cảm thấy một nỗi đau không thể tả Chiếc hộp thiếc rỉ sét đựng bút mực cũ kỹ là tất cả những gì còn lại của anh trong căn biệt thự xa hoa...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 851 | Ổn | Đêm mưa lạnh ở Hà Nội những giọt nước từ bầu trời đổ xuống như những mũi dao sắc lạnh xé toạc không gian... |
| 2 | 828 | Ổn | Trần Đông Hải ngồi một mình trong quán cà phê nhỏ bên đường Nguyễn Thái Học mưa vẫn rơi lác đác bên ngoài tạo... |
| 3 | 987 | Ổn | Hà Nội đêm trở nên rét mướt hơn bao giờ hết từng hạt mưa rơi nhẹ nhàng như những giọt nước mắt của bầu... |
| 4 | 1034 | Ổn | Trần Đông Hải ngồi lặng lẽ trong văn phòng tối tăm ánh đèn neon nhấp nháy bên ngoài cửa sổ kính lớn tạo nên... |
| 5 | 901 | Ổn | Đêm mưa Hà Nội vẫn như cơn ác mộng không dứt từng giọt nước từ mái hiên xối xả đổ xuống tạo ra những... |
| 6 | 887 | Ổn | Trần Đông Hải ngồi trước bàn làm việc ánh đèn vàng ấm áp chiếu sáng khuôn mặt đầy âu lo của anh Những giọt... |
| 7 | 901 | Ổn | Trần Đông Hải đứng sừng sững trước cánh cổng lớn của biệt thự Lê Gia ánh đèn vàng từ bên trong hắt ra tạo... |
| 8 | 986 | Ổn | Trần Đông Hải đứng trước gương nhìn vào đôi mắt mình phản chiếu trong ánh đèn vàng nhạt của căn phòng Ánh mắt anh... |

### Đế Chế Gốm Sứ Bát Tràng: Phản Bội và Bùng Nổ

- Link: https://doctieuthuyet.com/truyen/de-che-gom-su-bat-trang-nghe-nhan-bi-phan-boi-thieu-dot-ca-lang-nghe/
- Mô tả: 150 từ. Ổn.
- Mở đầu mô tả: Ở làng Bát Tràng ngàn năm nơi gốm sứ giao thoa với nghệ thuật một bi kịch đang xảy ra Nguyễn Quang Minh nghệ nhân tài ba bỗng dưng bị phản bội bởi học trò ruột Trần Thế Hải Hắn không chỉ...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1053 | Ổn | Ở làng Bát Tràng ngàn năm nơi gốm sứ giao thoa với nghệ thuật một bi kịch đang xảy ra Nguyễn Quang Minh nghệ... |
| 2 | 1351 | Ổn | Trong không gian âm u và nóng bức của xưởng gốm Nguyễn Quang Minh ngồi lặng lẽ ánh mắt trĩu nặng nhìn vào những... |
| 3 | 1121 | Ổn | Nguyễn Quang Minh đứng giữa lò gốm không khí nặng nề như bao trùm lên chiếc lò nung đang tỏa ra hơi nóng rực... |
| 4 | 1036 | Ổn | Giữa không gian tĩnh lặng của làng Bát Tràng nơi mà những chiếc bình gốm vẫn còn mang hơi thở của nghệ thuật truyền... |
| 5 | 1093 | Ổn | Ánh nắng rực rỡ của buổi sáng Bát Tràng len lỏi qua những tán cây cổ thụ chiếu xuống con đường đất đỏ dẫn... |
| 6 | 1056 | Ổn | Nguyễn Quang Minh đứng giữa lò gốm ánh mắt mờ mịt như sương khói mơ hồ trước mắt Hơi ấm từ lò gốm không... |
| 7 | 1286 | Ổn | Tại làng Bát Tràng giữa những tiếng gõ bát tiếng nước chảy từ những vòi gốm không khí đang nặng nề hơn bao giờ... |
| 8 | 1212 | Ổn | Nguyễn Quang Minh đứng lặng giữa xưởng gốm ánh sáng mờ ảo từ những chiếc đèn dầu chiếu rọi lên những sản phẩm gốm... |

### Chàng Rể Vạch Trần Âm Mưu Gia Tộc Trầm Hương

- Link: https://doctieuthuyet.com/truyen/chang-re-bi-truc-xuat-khoi-gia-toc-tram-huong-tim-ra-ky-nam-nghin-ty-va-sap-tap-doan-phan-boi/
- Mô tả: 136 từ. Ổn.
- Mở đầu mô tả: Giữa cơn mưa giông của phố biển Nha Trang Diệp Thiên Lang bị ném khỏi gia tộc trầm hương Hắn bị Lâm Vĩnh Nghiệp vua trầm đất Khánh Hòa chửi rủa thậm tệ chỉ vì một tai nạn chấn thương khứu giác...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1397 | Ổn | Giữa cơn mưa giông trắng trời gào rú bên bờ biển Nha Trang sấm sét rạch những vệt sáng chói lòa trên nền trời... |
| 2 | 1039 | Ổn | Giữa cơn mưa tầm tã của phố biển Nha Trang Diệp Thiên Lang đứng dưới mái hiên của một quán cà phê nhỏ ánh... |
| 3 | 1060 | Ổn | Giữa cơn mưa rào ào ạt từng giọt nước lớn như hạt đậu rơi xuống mặt đất tạo nên những vũng nước lấp lánh... |
| 4 | 1043 | Ổn | Giữa cơn mưa giông của phố biển Nha Trang Diệp Thiên Lang đứng lặng lẽ bên bờ biển ánh mắt nhìn xa xăm ra... |
| 5 | 1008 | Ổn | Giữa cơn mưa giông của phố biển Nha Trang Diệp Thiên Lang đứng giữa cánh đồng trầm hương chỉ còn lại những thân cây... |
| 6 | 1045 | Ổn | Giữa cơn mưa giông của phố biển Nha Trang Diệp Thiên Lang đứng ở cửa văn phòng của Tập đoàn Vạn An lòng trĩu... |
| 7 | 1239 | Ổn | Trong không khí nặng nề của cơn mưa đổ xuống Nha Trang Diệp Thiên Lang đứng trước cửa văn phòng Tập đoàn Vạn An... |
| 8 | 1052 | Ổn | Trời Nha Trang xám xịt những cơn mưa nặng hạt rơi xuống như thể đang khóc thương cho những gì đang diễn ra trong... |

### Thiên Tài Cầu Đường: Kỹ Sư Bị Sa Thải Đối Đầu Với Kẻ Cướp Bản Quyền

- Link: https://doctieuthuyet.com/truyen/thien-tai-cau-duong-cao-toc-ky-su-bi-sa-thai-xay-cau-vuot-bien-nghin-ty/
- Mô tả: 113 từ. Ổn.
- Mở đầu mô tả: Giữa cơn bão Hải Phòng tôi bị đẩy ra khỏi Viện Thiết Kế Cầu Đường chỉ vì dám phản biện sai sót trong dự án Lê Khắc Nam kẻ cướp bản quyền thiết kế của tôi lớn tiếng châm chọc Mày chỉ...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1397 | Ổn | Giữa cơn bão Hải Phòng gầm rú trắng xóa trời đất mưa rơi như trút những bầu nước khổng lồ xuống mặt đường gió... |
| 2 | 1002 | Ổn | Giữa những cơn gió mạnh rít lên từ biển tôi đứng trên bãi biển Hải Phòng nơi mà những cơn sóng đánh vào bờ... |
| 3 | 1092 | Ổn | Giữa cơn bão Hải Phòng những giọt mưa lớn như những viên đạn lạnh lẽo bắn vào mặt đường nhựa tạo thành những vũng... |
| 4 | 1222 | Ổn | Ánh sáng lạnh lẽo của màn hình máy tính chiếu sáng khuôn mặt tôi làm nổi bật từng nếp nhăn lo âu trên trán... |
| 5 | 1084 | Ổn | Giữa cái không khí ngột ngạt của buổi chiều mưa tôi ngồi ở quán cà phê nhỏ bên đường Trần Phú Hải Phòng tâm... |
| 6 | 1194 | Ổn | Hà Nội sáng sớm hôm nay không khí nặng nề như một cơn bão sắp đổ bộ Tôi đứng trước cổng Cục Bản quyền... |
| 7 | 1085 | Ổn | Giữa không gian ngột ngạt của căn phòng làm việc chật chội tôi đứng đối diện với Đỗ Phương Vy ánh mắt chúng tôi... |
| 8 | 1244 | Ổn | Những cơn gió mạnh thổi qua từng góc phố Hải Phòng mang theo âm thanh rì rào của biển cả và sự nhộn nhịp... |

### Người Thừa Kế Trăm Tỷ Giả Nghèo: Thử Lòng Đại Gia

- Link: https://doctieuthuyet.com/truyen/nguoi-thua-ke-tram-ty-gia-ngheo-2/
- Mô tả: 149 từ. Ổn.
- Mở đầu mô tả: Trong một buổi chiều nắng vàng Nguyễn Minh Triết chọn xe ôm thay vì xe sang để đến ra mắt gia đình người yêu Khi anh xuất hiện trước cánh cửa biệt thự lộng lẫy ở quận 2 ánh mắt của mẹ...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1093 | Ổn | Trong một buổi chiều nắng vàng Nguyễn Minh Triết chọn xe ôm thay vì xe sang để đến ra mắt gia đình người yêu... |
| 2 | 1205 | Ổn | Trong không gian lấp lánh của căn biệt thự mùi hương của nước hoa đắt tiền hòa quyện cùng ánh sáng vàng ấm áp... |
| 3 | 1118 | Ổn | Nguyễn Minh Triết đứng trước cánh cửa biệt thự lộng lẫy của gia đình Lê Vy Anh cảm giác như từng giọt mồ hôi... |
| 4 | 1008 | Ổn | Buổi chiều nắng vàng ánh sáng mặt trời hắt qua những tán cây tạo ra những vệt sáng lung linh trên đường phố quận... |
| 5 | 1404 | Ổn | Trong không gian tấp nập của Sài Gòn ánh đèn neon phản chiếu trên các tòa nhà chọc trời Nguyễn Minh Triết bước vào... |
| 6 | 1000 | Ổn | Ánh nắng đã dần tắt nhường chỗ cho bóng đêm bao trùm thành phố Hồ Chí Minh Nguyễn Minh Triết đứng giữa căn phòng... |
| 7 | 974 | Ổn | Trong không khí hồi hộp của buổi chiều ánh đèn sân khấu chói lòa khiến mọi người xung quanh cảm thấy như đang đứng... |
| 8 | 1312 | Ổn | Trong một buổi chiều nắng vàng rực rỡ Nguyễn Minh Triết đứng trước cánh cửa biệt thự lộng lẫy tại quận 2 lòng anh... |

### Công Thức Thuốc Bị Cướp: Bẫy IPO Dược Phẩm Nghìn Tỷ

- Link: https://doctieuthuyet.com/truyen/chien-than-duoc-pham-doc-ban-2/
- Mô tả: 162 từ. Ổn.
- Mở đầu mô tả: Nguyễn Đức Trí đứng sững trước cánh cửa phòng lab tại Đà Lạt không thể tin vào mắt mình Ngày mai công thức thuốc gan của anh sẽ bước vào vòng gọi vốn nhưng giờ đây mọi thứ đã bị cướp mất...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 941 | Ổn | Nguyễn Đức Trí đứng sững trước cánh cửa phòng lab tại Đà Lạt không thể tin vào mắt mình Ngày mai công thức thuốc... |
| 2 | 1146 | Ổn | Nguyễn Đức Trí đứng sững trước cánh cửa phòng lab tại Đà Lạt không thể tin vào mắt mình Ngày mai công thức thuốc... |
| 3 | 1319 | Ổn | Nguyễn Đức Trí đứng sững trước cánh cửa phòng lab tại Đà Lạt không thể tin vào mắt mình Từng giọt mồ hôi lạnh... |
| 4 | 1260 | Ổn | Nguyễn Đức Trí đứng sững trước cánh cửa phòng lab tại Đà Lạt không thể tin vào mắt mình Ngày mai công thức thuốc... |
| 5 | 1331 | Ổn | Nguyễn Đức Trí nắm chặt tay đôi mắt anh ánh lên sự quyết tâm khi đối diện với cánh cửa gỗ nâu sẫm nơi... |
| 6 | 1133 | Ổn | Nguyễn Đức Trí đứng sững trước cánh cửa phòng lab tại Đà Lạt không thể tin vào mắt mình Ngày mai công thức thuốc... |
| 7 | 1004 | Ổn | Nguyễn Đức Trí đứng sững trước cánh cửa phòng lab tại Đà Lạt không thể tin vào mắt mình Ngày mai công thức thuốc... |
| 8 | 1324 | Ổn | Nguyễn Đức Trí đứng sừng sững tại sảnh chính của trung tâm hội nghị lớn nhất Đà Lạt nơi mà ánh đèn chớp nhoáng... |

### Ngọc Hoàng Tôm Hùm: Trận Chiến Khốc Liệt Giữa Ngư Dân Và Thương Láii

- Link: https://doctieuthuyet.com/truyen/vua-tom-hum-phu-yen-chang-ngu-dan-bi-khinh-re-thau-tom-vung-bien-nghin-ty/
- Mô tả: 200 từ. Ổn.
- Mở đầu mô tả: Ngày định mệnh cha con chủ nhiệm Hợp tác xã đã tước đoạt toàn bộ lồng tôm hùm gia truyền của Trần Hải Phong Hình ảnh người cha già nằm liệt giường chấn thương cột sống nỗi đau khôn nguôi khiến Hải...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1018 | Ổn | Ngày định mệnh ánh nắng chói chang của buổi sớm không thể xua tan được bầu không khí nặng nề bao trùm lên bãi... |
| 2 | 1077 | Ổn | Trần Hải Phong đứng giữa bãi biển Phú Yên gió biển phả vào mặt như một bàn tay lạnh lẽo mang theo hương vị... |
| 3 | 1157 | Ổn | Trần Hải Phong đứng bên bờ biển Phú Yên gió biển thổi mạnh khiến mái tóc anh rối bù nhưng không gì có thể... |
| 4 | 1075 | Ổn | Ngày định mệnh đã đến khi mà bầu trời xanh thẳm của Phú Yên bỗng trở nên u ám báo hiệu một cơn bão... |
| 5 | 1143 | Ổn | Ngày định mệnh đã đến khi ánh mặt trời đầu tiên của bình minh chiếu rọi lên những cồn cát trắng xóa của bãi... |
| 6 | 1036 | Ổn | Ngày hôm ấy bầu trời Phú Yên u ám những đám mây đen kịt như đang chất chứa một cơn giận dữ sắp sửa... |
| 7 | 1291 | Ổn | Trời sáng dần lên ánh nắng len lỏi qua những tán cây xanh rì rào bên ngoài phiên tòa mang theo hơi ấm của... |
| 8 | 1085 | Ổn | Ngày định mệnh đã đến khi ánh nắng chói chang lấp lánh trên những con sóng bạc đầu vỗ về bãi biển Phú Yên... |

### Bão Nổi Miền Tây: Vương Quốc Sầu Riêng Trăm Tỷ

- Link: https://doctieuthuyet.com/truyen/bao-noi-mien-tay-vuong-quoc-sau-rieng-tram-ty-cua-chang-re-hao-mon-2/
- Mô tả: 121 từ. Ổn.
- Mở đầu mô tả: Giữa cơn bão truyền thông và áp lực nợ nần Nguyễn Tấn Đạt một người làm vườn vô danh lại mang trong mình bí mật khôn nguôi Vườn sầu riêng Monthong 50 hecta của Trần Mỹ Duyên đột ngột bị đầu độc...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1039 | Ổn | Giữa cơn bão truyền thông và áp lực nợ nần Nguyễn Tấn Đạt một người làm vườn vô danh lại mang trong mình bí... |
| 2 | 1046 | Ổn | Trần Mỹ Duyên đứng giữa vườn sầu riêng của mình ánh nắng chói chang của miền Tây khiến cô cảm nhận rõ hơn nỗi... |
| 3 | 1096 | Ổn | Nguyễn Tấn Đạt đứng giữa vườn sầu riêng Monthong ánh nắng chói chang của miền Tây như thiêu đốt nhưng cái lạnh trong lòng... |
| 4 | 1021 | Ổn | Giữa không khí căng thẳng Trần Mỹ Duyên ngồi thu mình trong văn phòng nhỏ của mình ánh đèn vàng nhạt hắt lên khuôn... |
| 5 | 1174 | Ổn | Giữa không khí nặng nề của những lời đe dọa Nguyễn Tấn Đạt ngồi co mình trong góc vườn ánh mắt như thiêu đốt... |
| 6 | 1479 | Ổn | Giữa bầu không khí ngột ngạt của những đám mây đen kịt Nguyễn Tấn Đạt đứng giữa vườn sầu riêng Monthong ánh mắt anh... |
| 7 | 1102 | Ổn | Giữa không gian ngột ngạt của căn phòng nhỏ Nguyễn Tấn Đạt ngồi im lặng hai tay siết chặt vào nhau mồ hôi lạnh... |
| 8 | 1317 | Ổn | Giữa không khí ngột ngạt của cuộc khủng hoảng Nguyễn Tấn Đạt đứng giữa vườn sầu riêng Monthong rộng lớn nơi những cây sầu... |

### Vương Quốc Nước Mắm Truyền Thống Phú Quốc: Chàng Rể Ẩn Thế Vực Dậy Quốc Hồn

- Link: https://doctieuthuyet.com/truyen/vuong-quoc-nuoc-mam-truyen-thong-phu-quoc-chang-re-an-the-vuc-day-quoc-hon/
- Mô tả: 108 từ. Ổn.
- Mở đầu mô tả: Trịnh Gia Huy nghệ nhân ủ chượp nước mắm nổi tiếng bị vu oan trộm cắp công thức Gã anh rể Trần Thế Vinh hách dịch đã đạp ngã hắn bên sườn đồi Dương Đông Ba trăm thùng chượp nước mắm hoàng...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1027 | Ổn | Trịnh Gia Huy đứng giữa nhà thùng Dương Đông nơi mà mùi hương đặc trưng của nước mắm truyền thống quện vào cái nắng... |
| 2 | 1372 | Ổn | Trịnh Gia Huy đứng lặng lẽ bên sườn đồi Dương Đông ánh nắng chiều dần tắt để lại một màu đỏ rực rỡ trên... |
| 3 | 1117 | Ổn | Trời vừa hửng sáng ánh nắng len lỏi qua những tán cây dừa xanh mướt ánh lên những giọt sương còn đọng lại trên... |
| 4 | 1052 | Ổn | Trời đã sập tối ánh đèn vàng nơi phố thị Dương Đông bắt đầu lấp lánh như những vì sao trôi nổi trên mặt... |
| 5 | 1062 | Ổn | Trời đã tối những ánh đèn lấp lánh của thị trấn Dương Đông như những vì sao rực rỡ trên mặt biển nhưng trong... |
| 6 | 1191 | Ổn | Ánh nắng mặt trời đang dần lặn xuống phía chân trời nhuộm vàng bầu trời Phú Quốc nhưng không khí xung quanh lại ngột... |
| 7 | 1119 | Ổn | Ánh nắng rực rỡ của buổi sớm mai rọi xuống mặt nước biển trong xanh tạo nên những tia sáng lấp lánh như những... |
| 8 | 1065 | Ổn | Trời đã vào chiều ánh nắng vàng rực rỡ chiếu rọi trên những con đường nhỏ quanh co của Dương Đông Phú Quốc Trịnh... |

### Thiên Tài Fintech: Lật Kèo Tại PayBlock

- Link: https://doctieuthuyet.com/truyen/thien-tai-khoi-nghiep-fintech-2/
- Mô tả: 100 từ. Ổn.
- Mở đầu mô tả: Phạm Tuấn Kiệt từng là thiên tài fintech với dự án PayViet đang chuẩn bị gọi vốn Series B Nhưng khi đồng sáng lập Đỗ Thế Nam âm thầm cướp app anh rơi vào cảnh khốn cùng Trong bóng tối bí mật...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 972 | Ổn | Ánh đèn vàng nhợt nhạt từ màn hình máy tính lập lòe phản chiếu lên gương mặt của Phạm Tuấn Kiệt khiến anh trông... |
| 2 | 987 | Ổn | Giữa không khí nhộn nhịp của tòa nhà Keangnam Landmark 72 Phạm Tuấn Kiệt đứng ở lối vào ánh mắt sắc bén quét quanh... |
| 3 | 1098 | Ổn | Phạm Tuấn Kiệt đứng giữa căn phòng tối tăm ánh đèn neon lờ mờ từ màn hình máy tính chiếu lên gương mặt anh... |
| 4 | 1118 | Ổn | Phạm Tuấn Kiệt ngồi trong góc quán cà phê nhỏ ở phố Tràng Tiền ánh đèn vàng nhạt từ chiếc đèn bàn phát ra... |
| 5 | 1082 | Ổn | Ánh nắng ban mai len lỏi qua các tán cây bên đường phố Hà Nội tạo nên những mảng sáng lung linh trên mặt... |
| 6 | 1129 | Ổn | Đã là 16 giờ ánh sáng nhạt dần nơi phố phường Hà Nội nhưng trong không gian chật chội của căn phòng nhỏ tại... |
| 7 | 1042 | Ổn | Ánh sáng chói chang của buổi chiều Hà Nội len lỏi qua những tấm kính lớn của tòa nhà văn phòng hiện đại nơi... |
| 8 | 1260 | Ổn | Ánh sáng của buổi sáng Hà Nội len lỏi qua cửa kính văn phòng PayBlock chiếu lên gương mặt đầy lo âu của Phạm... |

### Bảo Vệ Quèn Là Võ Thần: Phá Bẫy Buôn Lậu 500 Tỷ Cảng Đình Vũ

- Link: https://doctieuthuyet.com/truyen/vo-than-bao-ve-dai-tieu-thu-2/
- Mô tả: 123 từ. Ổn.
- Mở đầu mô tả: Giữa sự tấp nập của cảng Đình Vũ một người đàn ông lặng lẽ đứng gác không ai biết đến quá khứ oai hùng của anh Hoàng Việt bảo vệ với mức lương 8 triệu một tháng bị xem như người thừa...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1036 | Ổn | Giữa sự tấp nập của cảng Đình Vũ một người đàn ông lặng lẽ đứng gác không ai biết đến quá khứ oai hùng... |
| 2 | 1203 | Ổn | Giữa cái không khí ẩm ướt của cảng Đình Vũ tiếng sóng vỗ rì rào vào bờ hòa cùng tiếng máy móc ồn ào... |
| 3 | 1027 | Ổn | Giữa cái nắng oi ả của buổi chiều ở cảng Đình Vũ Hoàng Việt đứng lặng lẽ như một bức tượng ánh mắt chăm... |
| 4 | 1155 | Ổn | Đêm xuống cảng Đình Vũ chìm trong bóng tối và sự tĩnh lặng đáng sợ Chỉ còn ánh đèn le lói từ những chiếc... |
| 5 | 1010 | Ổn | Giữa sự tấp nập của cảng Đình Vũ những tiếng động ồn ào từ các xe container tiếng máy móc làm việc không ngừng... |
| 6 | 1254 | Ổn | Giữa sự tấp nập của cảng Đình Vũ những cơn gió lạnh từ biển thổi vào mang theo mùi mặn mòi của muối và... |
| 7 | 1037 | Ổn | Giữa khung cảnh tấp nập của cảng Đình Vũ từng chiếc container vươn lên như những tòa nhà chọc trời Hoàng Việt cảm nhận... |
| 8 | 1252 | Ổn | Giữa những âm thanh ồn ào của cảng Đình Vũ Hoàng Việt đứng lặng lẽ nơi góc tối ánh mắt sắc bén như một... |

### Nguyễn Tấn Đạt: Chàng Rể Bùn Lầy Lật Kèo Vườn Sầu Riêng Trăm Tỷ

- Link: https://doctieuthuyet.com/truyen/bao-noi-mien-tay-vuong-quoc-sau-rieng-tram-ty-cua-chang-re-hao-mon/
- Mô tả: 135 từ. Ổn.
- Mở đầu mô tả: Giữa cánh đồng sầu riêng bạt ngàn ở Chợ Lách Nguyễn Tấn Đạt chỉ là một người làm vườn lấm bùn Nhưng ẩn sau đôi ủng cao su sờn rách là bí mật về sự giàu có và quyền lực không ai...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1023 | Ổn | Giữa cánh đồng sầu riêng bạt ngàn ở Chợ Lách Nguyễn Tấn Đạt chỉ là một người làm vườn lấm bùn Những chiếc ủng... |
| 2 | 1142 | Ổn | Những tia nắng đầu tiên của buổi sáng len lỏi qua những tán lá sầu riêng tạo nên một bức tranh thiên nhiên tuyệt... |
| 3 | 1008 | Ổn | Giữa ánh nắng chói chang của buổi sớm Nguyễn Tấn Đạt đứng giữa vườn sầu riêng Monthong mồ hôi chảy ròng ròng trên trán... |
| 4 | 1234 | Ổn | Giữa khung cảnh u ám của vườn sầu riêng Monthong dưới ánh nắng chói chang của buổi chiều Nguyễn Tấn Đạt đứng giữa những... |
| 5 | 1114 | Ổn | Giữa cánh đồng sầu riêng bạt ngàn ở Chợ Lách Nguyễn Tấn Đạt chỉ là một người làm vườn lấm bùn Đôi ủng cao... |
| 6 | 932 | Ổn | Giữa cái nắng chói chang của buổi trưa ở Chợ Lách Nguyễn Tấn Đạt đứng giữa vườn sầu riêng ánh mắt của anh như... |
| 7 | 963 | Ổn | Ánh sáng mặt trời xuyên qua những tán lá sầu riêng tạo nên những điểm sáng lung linh trên mặt đất chiếu rọi lên... |
| 8 | 1108 | Ổn | Giữa cái nóng oi ả của buổi trưa Chợ Lách Nguyễn Tấn Đạt đứng giữa cánh đồng sầu riêng nơi mà mùi hương ngọt... |

### Trọng Sinh 2008: Vua Đất Đông Anh Thiết Lập Đế Chế

- Link: https://doctieuthuyet.com/truyen/trong-sinh-2008-vua-dat-dong-anh-thiet-lap-de-che/
- Mô tả: 180 từ. Ổn.
- Mở đầu mô tả: Nguyễn Hoàng Minh một chuyên gia phân tích tài chính hàng đầu năm 2026 đứng trên cầu Nhật Tân ánh mắt tràn đầy uất hận Hắn không thể ngờ rằng kẻ thù đã gài bẫy khiến hắn phá sản và giờ đây...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1503 | Ổn | Nguyễn Hoàng Minh một chuyên gia phân tích tài chính hàng đầu năm 2026 đứng trên cầu Nhật Tân ánh mắt tràn đầy uất... |
| 2 | 1119 | Ổn | Nguyễn Hoàng Minh đứng giữa dòng người tấp nập trên phố cảm giác như cả thế giới đang quay lưng lại với mình Ánh... |
| 3 | 1009 | Ổn | Nguyễn Hoàng Minh đứng trước một quán cà phê trên đường Trường Sa lòng tràn đầy lo lắng Ánh nắng ban mai chiếu rọi... |
| 4 | 1261 | Ổn | Lê Vy Anh ngồi trên chiếc ghế da cao cấp trong văn phòng sang trọng của mình ánh đèn vàng dịu dàng chiếu rọi... |
| 5 | 1287 | Ổn | Nguyễn Hoàng Minh đứng giữa những tòa nhà chọc trời của Hà Nội lòng anh trĩu nặng nỗi lo âu Hôm nay là một... |
| 6 | 1009 | Ổn | Nguyễn Hoàng Minh đứng giữa phòng làm việc chật chội của mình ánh đèn neon chói lóa phản chiếu lên khuôn mặt căng thẳng... |
| 7 | 1267 | Ổn | Nguyễn Hoàng Minh đứng giữa phiên tòa ánh mắt hắn lạnh lùng và quyết tâm như một chiến binh chuẩn bị cho trận chiến... |
| 8 | 1005 | Ổn | Nguyễn Hoàng Minh đứng trước cánh cửa phòng xử án lòng anh tràn ngập lo âu Thời gian chỉ còn chưa đầy một giờ... |

### Võ Thần Đất Cảng: Vệ Sĩ Ẩn Thân Phá Bẫy Buôn Lậu 500 Tỷ Cảng Đình Vũ

- Link: https://doctieuthuyet.com/truyen/vo-than-dat-cang-ve-si-an-than-pha-bay-buon-lau-500-ty-cang-dinh-vu/
- Mô tả: 108 từ. Ổn.
- Mở đầu mô tả: Có những người chọn biến mất không phải vì nhát gan mà vì họ biết rõ hơn ai hết rằng ánh đèn sân khấu đôi khi là mồi nhử tốt nhất cho kẻ thù Lê Gia Bách từng là Đại úy Đặc...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 684 | ngắn (684 từ) | Ba giờ mười bảy phút sáng nhiệt kế treo ở trụ đèn cổng B của cảng Đình Vũ chỉ mười chín độ Lê Gia... |
| 2 | 654 | ngắn (654 từ) | Cuộc gọi đến điện thoại của tổ trưởng bảo vệ Hoàng vào lúc mười giờ bốn mươi lăm phút đêm thứ Sáu Đầu dây... |
| 3 | 618 | ngắn (618 từ) | Sáng thứ Hai Nguyễn Hoài An ngồi vào bàn làm việc lúc bảy giờ ba mươi phút sớm hơn ba mươi phút so với... |
| 4 | 761 | Ổn | Cuộc gặp diễn ra vào thứ Tư lúc chín giờ sáng Bách vào phòng họp với bộ đồng phục bảo vệ đã giặt sạch... |
| 5 | 602 | ngắn (602 từ) | Ngày thứ mười chín của Bách trong vai trò mới lúc năm giờ bốn mươi phút sáng một chiếc xe của C03 Bộ Công... |
| 6 | 654 | ngắn (654 từ) | Lúc tám giờ mười lăm phút sáng cùng ngày email đầu tiên đến từ phía đối tác quốc tế Maersk Line Vietnam gửi công... |
| 7 | 695 | ngắn (695 từ) | Trong khi Hoài An đối phó với áp lực từ đối tác và báo chí Bách xin phép C03 được hỗ trợ kỹ thuật... |
| 8 | 571 | ngắn (571 từ) | C03 ra lệnh tạm giữ Trần Anh Khoa lúc ba giờ mười lăm phút chiều ngay tại văn phòng của ông ta ở tầng... |
| 9 | 773 | Ổn | Lúc tám giờ tối trời bắt đầu đổ mưa từ hướng biển Mưa đầu hè tại Hải Phòng không to nhưng dai loại mưa... |
| 10 | 638 | ngắn (638 từ) | Buổi họp báo diễn ra lúc mười giờ sáng ngày hôm sau tại hội trường tầng ba tòa nhà HPL trên đường Điện Biên... |
| 11 | 567 | ngắn (567 từ) | Bãi biển Đồ Sơn vắng người vào lúc tám giờ tối Mùa du lịch chưa bắt đầu gió từ biển thổi vào mang cái... |

### Cuộc Chiến Sinh Tử Của Trà Ô Long Hữu Cơ Việt

- Link: https://doctieuthuyet.com/truyen/vua-ban-le-duong-pho-sai-gon-tran-chien-sinh-tu-cua-chuoi-tra-o-long-organic-viet/
- Mô tả: 127 từ. Ổn.
- Mở đầu mô tả: Giữa lòng Sài Gòn nhộn nhịp Trần Quốc Bảo người sáng lập chuỗi trà Bảo Long Tea bất ngờ đối mặt với cơn bão truyền thông Đối thủ Royal Sip đã ra tay hãm hại bôi nhọ thương hiệu bằng những thông...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1068 | Ổn | Giữa lòng Sài Gòn nhộn nhịp nơi những dòng xe cộ tấp nập như dòng người hối hả trong cuộc sống thường nhật Trần... |
| 2 | 1130 | Ổn | Trời Sài Gòn sáng thứ Hai những tia nắng rực rỡ xuyên qua các tán cây xanh mướt ven đường nhưng trong lòng Trần... |
| 3 | 1117 | Ổn | Ánh sáng vàng rực rỡ của buổi sáng Sài Gòn chiếu qua những tán cây xanh mướt bên lề đường nhưng trong lòng Trần... |
| 4 | 1229 | Ổn | Giữa lòng Sài Gòn nhộn nhịp cái nắng vàng rực rỡ của buổi sáng ngày thứ Hai xuyên qua những tán cây xanh mướt... |
| 5 | 931 | Ổn | Giữa lòng Sài Gòn nhộn nhịp Trần Quốc Bảo ngồi bất động tại văn phòng của mình đôi mắt như ngọn lửa đang cháy... |
| 6 | 1146 | Ổn | Ánh nắng rực rỡ của buổi sáng thứ Hai len lỏi qua từng kẽ lá trên con đường Trần Hưng Đạo Sài Gòn dường... |
| 7 | 1293 | Ổn | Giữa không gian ngột ngạt của văn phòng Bảo Long Tea ánh đèn neon nhấp nháy phản chiếu lên gương mặt nghiêm túc của... |
| 8 | 1143 | Ổn | Giữa không khí căng thẳng của Sài Gòn vào sáng thứ Hai Trần Quốc Bảo ngồi trên chiếc ghế da màu đen ánh mắt... |

### Đế Chế Dệt May Bình Thịnh: Chiến Tranh Tài Chính

- Link: https://doctieuthuyet.com/truyen/cuoc-chien-phap-ly-dam-mau-giua-thieu-gia-bi-cha-nuoi-tay-chay-va-nu-luat-su-ma-ha-noi-khi-tap-doan-det-may-2000-ty-bi-de-doa-tu-scic-tai-kcn-binh-duong/
- Mô tả: 89 từ. Ổn.
- Mở đầu mô tả: Trần Minh Khải ông chủ của tập đoàn dệt may lớn nhất Bình Thịnh đang ở trong tình thế ngàn cân treo sợi tóc Quỹ đầu tư nước ngoài đang âm thầm thâu tóm cổ phần trong khi đối thủ nội địa...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1280 | Ổn | Trong ánh sáng lấp lánh của tòa nhà Landmark 81 Trần Minh Khải người đàn ông bốn mươi tuổi đứng giữa không gian rộng... |
| 2 | 1449 | Ổn | Trần Minh Khải ngồi trong phòng làm việc rộng lớn của mình ánh đèn vàng ấm áp phản chiếu lên những tấm gỗ sồi... |
| 3 | 1078 | Ổn | Trần Minh Khải đứng giữa phòng họp sang trọng ánh đèn neon rực rỡ chiếu xuống nhưng tâm trạng ông lại nặng nề như... |
| 4 | 1287 | Ổn | Trần Minh Khải đứng giữa căn phòng rộng lớn ánh đèn vàng ấm áp như cố gắng xoa dịu sự căng thẳng đang dâng... |
| 5 | 1212 | Ổn | Trần Minh Khải đứng giữa văn phòng sáng choang ánh đèn neon từ những tòa nhà chọc trời bên ngoài hắt vào tạo thành... |
| 6 | 1111 | Ổn | Trần Minh Khải đứng giữa văn phòng rộng lớn của mình ở tầng 15 tòa nhà Bình Thịnh Tower ánh mắt anh tăm tối... |
| 7 | 1027 | Ổn | Trần Minh Khải đứng giữa văn phòng của mình ánh đèn neon vàng hắt lên gương mặt trầm ngâm của anh làm nổi bật... |
| 8 | 1040 | Ổn | Trần Minh Khải đứng giữa phòng họp lớn của tập đoàn ánh đèn neon rực rỡ hắt lên gương mặt anh tạo nên những... |

### Cuộc Chiến Nghệ Thuật Tại Nhà Hát Phương Nam

- Link: https://doctieuthuyet.com/truyen/dao-dien-ballet-nga-tro-ve-doi-mat-voi-am-muu-cuop-dien-xuat-cua-gd-nghe-thuat-trong-cuoc-chien-khong-khoan-nhuong-tai-nha-hat-lon-ha-noi/
- Mô tả: 136 từ. Ổn.
- Mở đầu mô tả: Nguyễn Hoàng Long một đạo diễn ballet tài năng vừa trở về từ châu Âu đứng trước thách thức lớn tại Nhà hát Phương Nam Hội đồng nghệ thuật già cỗi đang bám víu vào truyền thống từ chối đổi mới Trong...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 981 | Ổn | Nguyễn Hoàng Long bước chân vào Nhà hát Phương Nam nơi mà ánh đèn sân khấu chói lọi hòa cùng những âm thanh du... |
| 2 | 1164 | Ổn | Nguyễn Hoàng Long đứng trước gương lớn trong phòng làm việc của Nhà hát Phương Nam ánh đèn vàng ấm áp chiếu lên khuôn... |
| 3 | 1178 | Ổn | Ánh đèn vàng nhạt của Nhà hát Phương Nam rọi xuống sàn diễn nơi mà những bước nhảy ballet tinh tế đang được chuẩn... |
| 4 | 1048 | Ổn | Đêm đã buông xuống ánh đèn vàng nhạt từ Nhà hát Phương Nam rọi xuống con đường nhựa bóng loáng tạo nên một khung... |
| 5 | 1123 | Ổn | Nguyễn Hoàng Long đứng trước gương ánh đèn mờ ảo phản chiếu hình ảnh của một người đàn ông đang trăn trở Hơi thở... |
| 6 | 1023 | Ổn | Ánh đèn vàng ấm áp từ những chiếc đèn chùm lớn trên trần nhà hát Phương Nam chiếu rọi xuống tạo ra một không... |
| 7 | 1292 | Ổn | Nguyễn Hoàng Long đứng giữa phòng tập tại Nhà hát Phương Nam ánh đèn neon vàng nhạt chiếu sáng từng góc nhỏ của không... |
| 8 | 1229 | Ổn | Giờ đây ánh đèn vàng rực rỡ của Nhà hát Phương Nam chiếu sáng khắp khán phòng tạo nên một không gian ấm áp... |

### Cướp Mã Nguồn Nghìn Tỷ, Kích Hoạt Bẫy Chôn Vùi Tập Đoàn

- Link: https://doctieuthuyet.com/truyen/bay-thau-tom-cong-nghe-su-phuc-thu-cua-thien-tai-lap-trinh/
- Mô tả: 137 từ. Ổn.
- Mở đầu mô tả: Mày hết chỗ đứng ở đây rồi Đức Cút ra khỏi tòa nhà của tao Giọng Hoàng Thế Vinh lạnh như băng không một chút dao động Phạm Minh Đức vị đồng sáng lập CyberShield vừa bị tống ra khỏi nơi mình...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1021 | Ổn | Mày hết chỗ đứng ở đây rồi Đức Cút ra khỏi tòa nhà của tao Giọng Hoàng Thế Vinh lạnh như băng không một... |
| 2 | 1159 | Ổn | Phạm Minh Đức đứng chôn chân ở lối vào tòa nhà CyberShield nơi mà anh đã dày công xây dựng từ những ngày đầu... |
| 3 | 1144 | Ổn | Mày hết chỗ đứng ở đây rồi Đức Cút ra khỏi tòa nhà của tao Giọng Hoàng Thế Vinh lạnh như băng không một... |
| 4 | 1203 | Ổn | Một cơn gió lạnh lẽo thổi qua cửa sổ phòng hội nghị mang theo sự tĩnh lặng nặng nề Hoàng Thế Vinh đứng giữa... |
| 5 | 1051 | Ổn | Đức ngồi bên bàn làm việc cũ kỹ ánh đèn neon từ màn hình máy tính phát ra những tia sáng yếu ớt chiếu... |
| 6 | 1133 | Ổn | Ánh đèn neon chói lòa từ tòa nhà CyberShield phản chiếu lên mặt đường ẩm ướt nơi mà từng chiếc ô tô vội vã... |
| 7 | 1055 | Ổn | Phạm Minh Đức đứng chôn chân tại cửa ra vào của tòa nhà CyberShield nơi mà anh đã từng gọi là nhà Ánh đèn... |
| 8 | 1188 | Ổn | Đức đứng lặng lẽ trước tòa nhà CyberShield ánh đèn neon rực rỡ phản chiếu trên gương mặt đầy mệt mỏi của anh Những... |

### Cuộc Chiến Bánh Mì: Bảo Vệ Di Sản Ẩm Thực Hội Nguyên

- Link: https://doctieuthuyet.com/truyen/dau-bep-via-he-hoi-an-doi-dau-voi-nghich-canh-cuop-cong-thuc-banh-mi-70-nam-va-cuoc-chien-danh-du-truoc-hoi-dong-michelin-asia-pacific/
- Mô tả: 133 từ. Ổn.
- Mở đầu mô tả: Phạm Hoàng Minh có thể mất tất cả chỉ trong vòng 24 giờ Tiệm bánh mì gia truyền bảy mươi năm nơi cha ông đã thổi hồn vào từng chiếc bánh đang đứng trước nguy cơ bị xóa sổ Đối thủ độc...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1017 | Ổn | Phạm Hoàng Minh đứng giữa tiệm bánh mì Hội Nguyên ánh mắt tràn ngập lo âu và tuyệt vọng Tiếng đồng hồ trên tường... |
| 2 | 1169 | Ổn | Tiếng chuông cửa leng keng khi Trần Diệu Linh bước vào tiệm bánh mì gia truyền Hội Nguyên tạo ra một âm thanh trong... |
| 3 | 1204 | Ổn | Phạm Hoàng Minh đang đứng trước quầy bánh ánh mắt mệt mỏi và đầy lo lắng khi nghe tiếng chuông cửa kêu leng keng... |
| 4 | 1091 | Ổn | Ánh đèn neon chói lòa từ những cửa tiệm xung quanh hắt lên mặt đường ẩm ướt phản chiếu những giọt nước mắt của... |
| 5 | 976 | Ổn | Phạm Hoàng Minh đứng giữa tiệm bánh mì của gia đình ánh đèn vàng nhạt chiếu sáng từng chiếc bánh trên kệ nhưng lòng... |
| 6 | 1276 | Ổn | Phạm Hoàng Minh đứng trước tủ bánh ánh mắt đắm chìm trong những chiếc bánh mì vàng ruộm hương thơm phức mùi bơ và... |
| 7 | 1013 | Ổn | Phạm Hoàng Minh đứng trước quầy bánh ánh mắt mờ mịt tay siết chặt thành nắm đấm trong lòng như lửa đốt Tiếng chuông... |
| 8 | 1422 | Ổn | Trời đã vào giữa trưa ánh nắng chói chang chiếu rọi qua những ô cửa kính của tiệm bánh mì gia truyền Hội Nguyên... |

### Vương Quốc Bất Động Sản: Cuộc Chiến Sinh Tử

- Link: https://doctieuthuyet.com/truyen/bi-vu-khong-an-hoa-hong-chuyen-gia-dinh-gia-dat-noi-mau-phuc-thu-khi-ceo-quy-reit-5000-ty-dinh-bay-mua-lai-toa-nha-quan-7/
- Mô tả: 119 từ. Ổn.
- Mở đầu mô tả: Đinh Thanh Tùng tên tuổi lừng lẫy trong lĩnh vực bất động sản đang đứng trước bờ vực của sự sụp đổ Ba thế lực đối thủ cùng lúc tấn công tạo nên vòng vây pháp lý tài chính và truyền thông...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1092 | Ổn | Đinh Thanh Tùng tên tuổi lừng lẫy trong lĩnh vực bất động sản đang đứng trước bờ vực của sự sụp đổ Ánh sáng... |
| 2 | 1061 | Ổn | Trong ánh sáng mờ ảo của buổi sáng sớm Đinh Thanh Tùng đứng bên cửa sổ kính của văn phòng tại tầng 25 tòa... |
| 3 | 997 | Ổn | Đinh Thanh Tùng đứng giữa khu vực tiếp tân của tòa nhà Landmark 81 ánh mắt anh như ngọn đèn pin rọi vào màn... |
| 4 | 1157 | Ổn | Đinh Thanh Tùng đứng giữa văn phòng lớn của mình ánh đèn trắng lóa chiếu rọi lên gương mặt anh làm nổi bật những... |
| 5 | 1133 | Ổn | Ánh sáng từ những tòa nhà chọc trời ở khu đô thị Phú Mỹ Hoa chiếu rọi xuống đường phố nhưng không gian tràn... |
| 6 | 1116 | Ổn | Đinh Thanh Tùng ngồi bất động tại văn phòng của mình ánh đèn neon từ tòa nhà Landmark 81 chiếu sáng mặt phố bên... |
| 7 | 969 | Ổn | Đinh Thanh Tùng đứng tại phòng họp lớn của tòa nhà Landmark 81 nơi ánh đèn chói lọi phản chiếu trên sàn gạch bóng... |
| 8 | 895 | Ổn | Đinh Thanh Tùng đứng sững tại văn phòng của mình ở tầng 16 tòa nhà Landmark 81 ánh mắt sắc lạnh quét qua những... |

### Nhà Thiết Kế Tàng Hình: Cuộc Chiến Tại Hội Nghị Thời Trang Quốc Gia

- Link: https://doctieuthuyet.com/truyen/kham-pha-am-muu-den-toi-cua-startup-da-lat-ky-su-bao-mat-bi-danh-cap-bang-sang-che-bi-blacklist-tu-bo-cong-an-a05-voi-200-trieu-usd-tu-quy-vc-singapore/
- Mô tả: 140 từ. Ổn.
- Mở đầu mô tả: Châu Minh Hải một nhà thiết kế trẻ tài năng vừa bị phản bội bởi người yêu cũ Trong cú sốc lớn anh phát hiện ra bộ sưu tập dạ hội độc bản của mình đã bị cướp trắng bởi đối thủ...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1156 | Ổn | Châu Minh Hải đứng bần thần giữa căn phòng thiết kế ngập tràn ánh sáng nơi mà từng đường kim mũi chỉ đều mang... |
| 2 | 884 | Ổn | Gió đêm thổi nhẹ qua khung cửa sổ mang theo hơi lạnh của mùa thu Hà Nội Châu Minh Hải ngồi lặng lẽ trong... |
| 3 | 1335 | Ổn | Châu Minh Hải đứng giữa căn phòng nhỏ hẹp ánh đèn vàng nhợt nhạt từ chiếc bóng đèn trên trần nhà phản chiếu lên... |
| 4 | 1057 | Ổn | Hải đứng lặng giữa không gian lạnh lẽo của phòng làm việc ánh đèn vàng nhạt chiếu sáng từng góc cạnh của những bản... |
| 5 | 1003 | Ổn | Ánh đèn neon chói lòa của thành phố Hà Nội hắt lên những giọt sương mỏng manh tạo nên một bức tranh huyền ảo... |
| 6 | 1027 | Ổn | Ánh sáng chói chang của buổi chiều nắng vàng hắt qua cửa kính tạo nên những vệt sáng lấp lánh trên sàn nhà của... |
| 7 | 1320 | Ổn | Ánh đèn rực rỡ của Hội Nghị Thời Trang Quốc Gia sáng rực rỡ tạo nên không khí hồi hộp và căng thẳng như... |
| 8 | 1081 | Ổn | Hải đứng giữa căn phòng tối tăm của văn phòng thiết kế mình ánh đèn neon bên ngoài hắt sáng qua khung cửa sổ... |

### Thiên Tài Lập Trình: Đà Lạt Sương Mù và Kế Hoạch Lật Đổ Tập Đoàn Tài Chính

- Link: https://doctieuthuyet.com/truyen/thien-tai-ma-hoa-da-lat-suong-mu/
- Mô tả: 106 từ. Ổn.
- Mở đầu mô tả: Giữa rừng thông Đà Lạt tĩnh lặng Trần Hưng sống một cuộc đời ẩn dật như một cựu kỹ sư bảo mật Nhưng bất ngờ cuộc sống yên bình của anh bị xáo trộn khi phát hiện ra backdoor rửa tiền nghìn...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1145 | Ổn | Giữa rừng thông Đà Lạt tĩnh lặng Trần Hưng sống một cuộc đời ẩn dật như một cựu kỹ sư bảo mật Những ngày... |
| 2 | 1078 | Ổn | Giữa bầu không khí se lạnh của Đà Lạt sương mù nhẹ nhàng bao phủ những cánh rừng thông tạo nên một không gian... |
| 3 | 1166 | Ổn | Giữa rừng thông Đà Lạt tĩnh lặng không khí trong lành mang theo hương vị của những cánh hoa dại nở rộ Trần Hưng... |
| 4 | 1126 | Ổn | Giữa không khí se lạnh của Đà Lạt ánh đèn vàng từ căn nhà gỗ nhỏ của Trần Hưng hòa quyện với sương mù... |
| 5 | 1105 | Ổn | Trời Đà Lạt vào buổi chiều tối những đám mây sà xuống thấp hòa quyện cùng với làn sương mờ ảo khiến không gian... |
| 6 | 1463 | Ổn | Giữa rừng thông Đà Lạt ánh sáng yếu ớt của buổi chiều tà len lỏi qua những tán cây tạo nên những mảng sáng... |
| 7 | 1019 | Ổn | Giữa không gian yên tĩnh của rừng thông Đà Lạt Trần Hưng đứng một mình đôi mắt chăm chú vào màn hình máy tính... |
| 8 | 1229 | Ổn | Trong ánh sáng yếu ớt của buổi sáng Đà Lạt Trần Hưng ngồi trước màn hình máy tính đôi mắt anh dán chặt vào... |

### Bóng Tối Điện Lực Vạn Thịnh: Cuộc Chiến Chống Tham Nhũng

- Link: https://doctieuthuyet.com/truyen/thuyen-truong-ty-phu-cang-tien-sa/
- Mô tả: 154 từ. Ổn.
- Mở đầu mô tả: Trong một đêm mưa bão Phan Đức Thành đã phát hiện ra đường dây tham nhũng thiết bị trạm biến áp đe dọa sự an toàn của lưới điện quốc gia Với trái tim đầy nhiệt huyết và tâm huyết với nghề...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1042 | Ổn | Đêm mưa bão những cơn gió mạnh mẽ như muốn cuốn trôi mọi thứ trên con đường nhỏ dẫn vào khu công nghiệp Điện... |
| 2 | 1165 | Ổn | Trời vẫn mưa rả rích những giọt nước lăn dài trên mặt kính của chiếc xe ô tô đậu lại bên lề đường lớn... |
| 3 | 1265 | Ổn | Trong ánh đèn mờ ảo của văn phòng Phan Đức Thành và Nguyễn Thu Trang ngồi đối diện nhau không khí căng thẳng như... |
| 4 | 1211 | Ổn | Trong không khí nặng nề của buổi tối mưa bão Phan Đức Thành đứng lặng giữa căn phòng làm việc ngập tràn bóng tối... |
| 5 | 1030 | Ổn | Giữa những cơn gió lạnh buốt Phan Đức Thành đứng lặng im trước cửa văn phòng của Điện lực Vạn Thịnh Ánh đèn neon... |
| 6 | 1040 | Ổn | Trời vẫn mưa như trút nước từng hạt nước lạnh buốt như những mũi dao đâm vào da thịt nhưng Phan Đức Thành không... |
| 7 | 1258 | Ổn | Giữa những cơn mưa tầm tã Phan Đức Thành đứng trước cửa sổ văn phòng của mình ánh mắt dán chặt vào những giọt... |
| 8 | 1294 | Ổn | Trong không khí ngột ngạt của buổi chiều mưa tầm tã Phan Đức Thành và Nguyễn Thu Trang đứng trước cổng trụ sở Điện... |

### Triều Đại Cà Phê Bazan: Cuộc Chiến Giành Bằng Sáng Chế

- Link: https://doctieuthuyet.com/truyen/cuu-thuyen-truong-cang-tien-sa-dot-pha-hop-dong-ma-phoi-bay-am-muu-thau-tom-da-nang-cua-tap-doan-ngoai-c03-xuat-hien-bao-ve-thanh-pho/
- Mô tả: 114 từ. Ổn.
- Mở đầu mô tả: Y Dhăm Nie một người nông dân trồng cà phê tài năng đang đứng trước bờ vực thua cuộc Đối tác ngoại bang xảo quyệt đã cướp đi bằng sáng chế máy rang cà phê bằng tia hồng ngoại của gia đình...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1056 | Ổn | Y Dhăm Nie đứng giữa rừng cà phê xanh mướt nơi những cây cà phê cao lớn đang trĩu quả nhưng trong lòng anh... |
| 2 | 1159 | Ổn | Y Dhăm Nie đứng giữa cánh đồng cà phê xanh mướt ánh nắng chiếu rọi qua từng tán lá tạo nên những vệt sáng... |
| 3 | 1160 | Ổn | Y Dhăm Nie ngồi thu mình trong góc phòng làm việc nhỏ hẹp của mình nơi ánh đèn neon nhấp nháy tỏa ra thứ... |
| 4 | 1162 | Ổn | Y Dhăm Nie đứng giữa vườn cà phê xanh mướt những cây cà phê cao lớn như những người lính canh giữ cho giấc... |
| 5 | 1056 | Ổn | Y Dhăm Nie đứng giữa không gian chật chội của văn phòng nhỏ ánh mắt anh dán chặt vào màn hình máy tính Những... |
| 6 | 1074 | Ổn | Y Dhăm Nie đứng giữa cánh đồng cà phê trải dài như bất tận ánh nắng chói chang của buổi trưa Đắk Lắk rọi... |
| 7 | 1187 | Ổn | Ánh nắng chói chang xuyên qua những tán cây cà phê xanh rì nhưng lòng Y Dhăm Nie lúc này không thể nào cảm... |
| 8 | 1157 | Ổn | Đêm Đắk Minh nặng nề và ngột ngạt không khí như bị đè nén bởi áp lực của một khủng hoảng không thể lường... |

### Thợ Hồ Nghìn Tỷ: Đập Tan Kiêu Ngạo

- Link: https://doctieuthuyet.com/truyen/tho-ho-nghin-ty/
- Mô tả: 124 từ. Ổn.
- Mở đầu mô tả: Ngày tôi đến ra mắt bà ấy phẩy tay ánh mắt khinh bỉ Thợ hồ mà dám đòi cưới con gái tôi Trọng Khải con rể tương lai là thiếu gia nhà giàu đi xe hơi bóng loáng còn tôi chỉ là...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 900 | Ổn | Ngày tôi đến ra mắt bà ấy phẩy tay ánh mắt khinh bỉ Thợ hồ mà dám đòi cưới con gái tôi Ánh sáng... |
| 2 | 1024 | Ổn | Ngày hôm sau ánh nắng chói chang xuyên qua những tấm kính trong suốt của văn phòng Tập đoàn Đế Vương nơi Trần Hùng... |
| 3 | 1068 | Ổn | Ngày hôm đó ánh nắng chói chang xuyên qua những tán cây xanh mướt của công viên trung tâm thành phố nơi mà tôi... |
| 4 | 881 | Ổn | Ngày hôm đó ánh nắng chói chang xuyên qua những tán cây xanh rì rào phản chiếu xuống mặt đường nhựa trải dài của... |
| 5 | 1199 | Ổn | Ánh sáng rực rỡ từ những tấm kính phản chiếu trên tòa nhà cao tầng của Tập đoàn Đế Vương làm cho không gian... |
| 6 | 1283 | Ổn | Ánh sáng trắng chói lóa từ những đèn neon trên đường phố Hà Nội khiến tôi cảm thấy như bị lạc giữa một mê... |
| 7 | 937 | Ổn | Ánh nắng chiều nhuộm vàng cả không gian bóng dáng của Trần Hùng ngồi im lìm trước màn hình máy tính đôi bàn tay... |
| 8 | 1481 | Ổn | Trời đã bắt đầu tối ánh đèn neon rực rỡ từ các tòa nhà cao tầng ở trung tâm thành phố phản chiếu xuống... |

### Bị Bạn Thân Cướp Startup, Tôi Lật Kèo Đế Chế FinTech

- Link: https://doctieuthuyet.com/truyen/thien-tai-khoi-nghiep-fintech/
- Mô tả: 127 từ. Ổn.
- Mở đầu mô tả: Tôi từng là người viết những dòng code đầu tiên cho PayViet trong căn phòng trọ 15 mét vuông tại phố Duy Tân Ba năm sau khi app trở thành hiện tượng với 2 triệu người dùng và vừa gọi vốn Series...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1145 | Ổn | Tôi từng là người viết những dòng code đầu tiên cho PayViet trong căn phòng trọ 15 mét vuông tại phố Duy Tân Những... |
| 2 | 1013 | Ổn | Hà Nội sáng thứ Hai những tia nắng đầu tiên len lỏi qua khung cửa kính của quán cà phê nhỏ nằm ở phố... |
| 3 | 1029 | Ổn | Thời gian trôi qua chậm chạp như những giọt nước rơi từ vòi nước rỉ rả trong căn phòng trọ nhỏ bé của tôi... |
| 4 | 1151 | Ổn | Ánh sáng yếu ớt của buổi sáng thứ Hai len lỏi qua khung cửa sổ chiếu rọi lên bàn làm việc ngổn ngang giấy... |
| 5 | 1106 | Ổn | Ánh nắng ban mai len lỏi qua những khe hở của rèm cửa sổ chiếu rọi lên chiếc bàn làm việc bừa bộn với... |
| 6 | 1218 | Ổn | 8h sáng thứ Hai ánh nắng chói chang tràn vào qua cửa sổ nhỏ hẹp của cái căn phòng trọ cũ kỹ Tôi ngồi... |
| 7 | 1000 | Ổn | 8 giờ sáng thứ Hai ánh nắng chói chang chiếu xuống con đường Duy Tân nơi tôi đã bắt đầu mọi thứ trong căn... |
| 8 | 1074 | Ổn | Tôi ngồi trên chiếc ghế gỗ cũ ánh sáng vàng vọt từ chiếc đèn bàn lập lòe soi sáng những dòng code lướt qua... |

### Mẹ Vợ Đòi Sính Lễ 5 Tỷ, Tôi Là Người Thừa Kế Landmark 81

- Link: https://doctieuthuyet.com/truyen/nguoi-thua-ke-tram-ty-gia-ngheo/
- Mô tả: 139 từ. Ổn.
- Mở đầu mô tả: Hôm nay là ngày định mệnh trong cuộc đời tôi Tôi bước xuống từ chiếc xe ôm cũ kỹ cảm giác lạnh lẽo bao trùm Mẹ cô ấy một bà mẹ khó tính ngồi đó với ánh mắt khinh bỉ chờ đợi...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 2 | 1110 | Ổn | Hôm nay là ngày định mệnh trong cuộc đời tôi Tôi bước xuống từ chiếc xe ôm cũ kỹ cảm giác lạnh lẽo bao... |
| 3 | 1191 | Ổn | Hôm nay là ngày tôi phải chứng minh giá trị thật của mình Tôi ngồi trên chiếc ghế gỗ cũ kỹ trong quán cà... |
| 4 | 943 | Ổn | Hôm nay là ngày định mệnh trong cuộc đời tôi Tôi bước xuống từ chiếc xe ôm cũ kỹ cảm giác lạnh lẽo bao... |
| 5 | 964 | Ổn | Hôm nay là ngày định mệnh trong cuộc đời tôi Tôi bước xuống từ chiếc xe ôm cũ kỹ cảm giác lạnh lẽo bao... |
| 6 | 956 | Ổn | Hôm nay là ngày tôi đã chờ đợi từ lâu Bầu không khí trong đại sảnh Phú Mỹ Hưng ngột ngạt những chiếc đèn... |
| 7 | 1096 | Ổn | Hôm nay là ngày định mệnh trong cuộc đời tôi Tôi bước xuống từ chiếc xe ôm cũ kỹ cảm giác lạnh lẽo bao... |
| 8 | 1134 | Ổn | Hôm nay là ngày định mệnh trong cuộc đời tôi Tôi bước xuống từ chiếc xe ôm cũ kỹ cảm giác lạnh lẽo bao... |
|  | 1333 | Ổn | Hôm nay là ngày định mệnh trong cuộc đời tôi Tôi bước xuống từ chiếc xe ôm cũ kỹ cảm giác lạnh lẽo bao... |

### Sếp Cướp Công Thức Thuốc, Tôi Phá Sập IPO Nghìn Tỷ

- Link: https://doctieuthuyet.com/truyen/chien-than-duoc-pham-doc-ban/
- Mô tả: 164 từ. Ổn.
- Mở đầu mô tả: Trong căn phòng lab lạnh giá ở Đà Lạt nơi mà không khí tràn ngập mùi thuốc thử và âm thanh lách cách của dụng cụ thí nghiệm tôi đã lao động miệt mài suốt năm năm Cuối cùng công sức của...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1220 | Ổn | Trong căn phòng lab lạnh giá ở Đà Lạt nơi mà không khí tràn ngập mùi thuốc thử và âm thanh lách cách của... |
| 2 | 973 | Ổn | Trong không khí lạnh lẽo của Đà Lạt tôi ngồi lặng lẽ bên chiếc bàn làm việc ánh sáng từ màn hình laptop hắt... |
| 3 | 1082 | Ổn | Đà Lạt thành phố ngàn hoa nhưng trong khoảnh khắc này tôi chỉ cảm nhận được sự lạnh lẽo của không gian lab Ánh... |
| 4 | 1189 | Ổn | Đà Lạt vào buổi sáng sớm sương mù vẫn còn bao phủ các con đường nhỏ khiến cảnh vật trở nên huyền ảo nhưng... |
| 5 | 1033 | Ổn | Đà Lạt trong cái lạnh se sắt của buổi sáng sớm ánh nắng mờ ảo len lỏi qua những tán thông cao vút tạo... |
| 6 | 1293 | Ổn | Trong căn phòng lab vẫn lạnh lẽo như trước không khí như đặc quánh lại tôi ngồi bên chiếc bàn thí nghiệm gương mặt... |
| 7 | 1452 | Ổn | Đã hai ngày trôi qua kể từ khi Vũ Đăng công bố kế hoạch IPO cho công ty dược phẩm của hắn Tôi ngồi... |
| 8 | 1035 | Ổn | Trong không khí nặng nề của căn phòng họp tại một tòa nhà cao tầng ở trung tâm Thành phố Hồ Chí Minh tôi... |

### Thần Tài Chứng Khoán: Đấu Trường Phố Wall Hà Nội

- Link: https://doctieuthuyet.com/truyen/vua-ban-le-duong-pho-blockchain-lat-keo-the-ky/
- Mô tả: 133 từ. Ổn.
- Mở đầu mô tả: Hoàng Đức Minh một nhà đầu tư trẻ tuổi đứng trơ trọi giữa sàn giao dịch Sở GDCK Phương Bắc Ánh mắt anh vằn tia máu tim đập loạn xạ khi bị giám đốc quỹ đầu tư vạch mặt trước hàng trăm...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 923 | Ổn | Hoàng Đức Minh một nhà đầu tư trẻ tuổi đứng trơ trọi giữa sàn giao dịch Sở GDCK Phương Bắc Ánh mắt anh vằn... |
| 2 | 1073 | Ổn | Hoàng Đức Minh đứng trơ trọi giữa sàn giao dịch Sở GDCK Phương Bắc nơi mà không khí ngột ngạt như thể hàng ngàn... |
| 3 | 1116 | Ổn | Hoàng Đức Minh đứng trơ trọi giữa sàn giao dịch Sở GDCK Phương Bắc nơi mà ánh đèn neon chói lòa phản chiếu lên... |
| 4 | 1048 | Ổn | Hoàng Đức Minh một nhà đầu tư trẻ tuổi đứng trơ trọi giữa sàn giao dịch Sở GDCK Phương Bắc nơi mà không khí... |
| 5 | 1225 | Ổn | Hoàng Đức Minh đứng giữa sàn giao dịch Sở GDCK Phương Bắc nơi ánh đèn neon chớp nháy liên hồi phản chiếu lên lớp... |
| 6 | 1164 | Ổn | Hoàng Đức Minh đứng bất động giữa sàn giao dịch Sở GDCK Phương Bắc cảm giác như mọi ánh mắt đều đổ dồn về... |
| 7 | 1130 | Ổn | Hoàng Đức Minh đứng giữa sàn giao dịch Sở GDCK Phương Bắc nơi mà tiếng nói và cử chỉ của hàng trăm người tạo... |
| 8 | 1033 | Ổn | Hoàng Đức Minh đứng trân trối giữa sàn giao dịch Sở GDCK Phương Bắc nơi mà ánh đèn chói lóa cùng với những âm... |

### Tiểu Thư Khinh Tôi Là Bảo Vệ: Đặc Nhiệm Giữa Đế Chế Buôn Lậu

- Link: https://doctieuthuyet.com/truyen/vo-than-bao-ve-dai-tieu-thu/
- Mô tả: 142 từ. Ổn.
- Mở đầu mô tả: Khi tôi bước vào công ty Tập đoàn Vạn Xuân mức lương 8 triệu đồng một tháng khiến tôi không khỏi mỉm cười Đại tiểu thư Phan Khánh Vy với đôi mắt sắc sảo và vẻ mặt kiêu ngạo nhìn tôi như...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1057 | Ổn | Khi tôi bước vào công ty Tập đoàn Vạn Xuân mức lương 8 triệu đồng một tháng khiến tôi không khỏi mỉm cười Ánh... |
| 2 | 1001 | Ổn | Khi ánh nắng chiếu rọi qua cửa kính của văn phòng Tập đoàn Vạn Xuân tôi cảm nhận được từng hạt bụi lơ lửng... |
| 3 | 1124 | Ổn | Giá như tôi có thể quên đi ánh mắt lạnh lẽo của Đại tiểu thư Phan Khánh Vy nhưng thực tế không cho phép... |
| 4 | 1138 | Ổn | Khi đồng hồ điểm 12 giờ trưa tôi đứng giữa một thế giới hỗn độn nơi mà ánh sáng và bóng tối giao nhau... |
| 5 | 1008 | Ổn | Khi đồng hồ điểm 12 giờ trưa ánh nắng chói chang từ những ô cửa kính trong suốt của Tập đoàn Vạn Xuân chiếu... |
| 6 | 1164 | Ổn | Khi chiếc đồng hồ treo tường trong văn phòng điểm 12 giờ trưa lòng tôi như bị siết chặt lại Đại tiểu thư Phan... |
| 7 | 1114 | Ổn | Ánh nắng đã bắt đầu lặn dần phía chân trời nhuộm sắc đỏ rực rỡ lên bầu trời Hà Nội Tôi đứng tại bến... |
| 8 | 1025 | Ổn | Khi đồng hồ vừa điểm 12 giờ trưa không khí trong văn phòng Tập đoàn Vạn Xuân trở nên căng thẳng hơn bao giờ... |

### Thuyền Trưởng Cảng Đà Thành: Cuộc Chiến Bên Bến Cả

- Link: https://doctieuthuyet.com/truyen/bi-duoi-khoi-cang-tien-sa-toi-nhan-chim-am-muu-thau-tom-cang-da-nang-nghin-ty/
- Mô tả: 118 từ. Ổn.
- Mở đầu mô tả: Lê Quang Vũ thuyền trưởng kỳ cựu đứng giữa những sóng gió của biển cả và cuộc đời Sa thải sau một lần dũng cảm đối mặt với quản lý nước ngoài anh trở thành kẻ bị đuổi khỏi vị trí mà...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1214 | Ổn | Lê Quang Vũ thuyền trưởng kỳ cựu của cảng Đà Thành đứng giữa những sóng gió của biển cả và cuộc đời Ánh nắng... |
| 2 | 1049 | Ổn | Lê Quang Vũ đứng giữa bến cảng Đà Thành ánh mắt dõi theo những con sóng vỗ về bờ cát như những nỗi niềm... |
| 3 | 1012 | Ổn | Thời gian trôi qua bến cảng Đà Thành đã nhuốm màu nắng chiều vàng vọt ánh sáng lấp lánh trên mặt nước như những... |
| 4 | 1003 | Ổn | Ánh nắng buổi sáng phản chiếu trên mặt biển xanh biếc như hứa hẹn một ngày mới đầy hứa hẹn Tuy nhiên không khí... |
| 5 | 1064 | Ổn | Ánh nắng ban mai rực rỡ chiếu xuống cảng Đà Thành tạo nên một khung cảnh tuyệt đẹp nhưng cũng đầy căng thẳng Lê... |
| 6 | 1392 | Ổn | Ánh sáng mờ ảo của buổi sáng sớm len lỏi qua những đám mây chiếu xuống bến cảng Đà Thành nơi làn sóng vỗ... |
| 7 | 1136 | Ổn | Ánh nắng ban mai chiếu rọi lên mặt biển Đà Thành tạo nên những vệt sáng lấp lánh như những mảnh vụn của kim... |
| 8 | 1055 | Ổn | Thời gian trôi qua như một cơn lốc chỉ còn 24 giờ nữa là đến cuộc họp cổ đông quyết định số phận của... |

### Người Thợ Sửa Xe Ở Hầm B2

- Link: https://doctieuthuyet.com/truyen/nguoi-tho-sua-xe-o-ham-b2/
- Mô tả: 223 từ. Ổn.
- Mở đầu mô tả: Một thằng sửa xe quần áo dính đầy dầu mỡ rác rưởi như mày mà dám dạy đời tao về cách vận hành siêu xe Lamborghini sao Cút Một cú tát nổ đom đóm mắt giáng thẳng xuống mặt Đỗ Nhật Nam...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 483 | ngắn (483 từ) | Dưới hầm xe B2 của trung tâm thương mại Vincom Center Đồng Khởi quận một tiếng động cơ gầm rú vang dội từ chiếc... |
| 2 | 402 | ngắn (402 từ) | Mười phút sau tiếng gót giày cao gót nhọn Louboutin gõ sắc lạnh trên nền bê tông hầm B2 vang lên dồn dập phá... |
| 3 | 365 | ngắn (365 từ) | Một giờ sáng hầm B2 vắng lặng không một bóng người Nhật Nam đang ngồi trong phòng kỹ thuật của xưởng sửa xe mắt... |
| 4 | 403 | ngắn (403 từ) | Chín giờ sáng ngày hôm sau tại trường đua biểu diễn tạm thời ở bán đảo Thủ Thiêm tiếng động cơ siêu xe gầm... |
| 5 | 427 | ngắn (427 từ) | Lê Duy mặt tái mét cố gắng bào chữa cho hành vi của mình Thưa ban tổ chức đây là sự vu khống vô... |
| 6 | 345 | ngắn (345 từ) | Mặc dù Lê Duy đã bị bắt và xưởng dịch vụ đã được mua lại thế nhưng Vương Quốc Anh và gia đình gã... |
| 7 | 405 | ngắn (405 từ) | Chiều hôm đó tại phòng tiếp nhận chứng cứ của Tòa án nhân dân Quận 1 ông Vương Thế Hùng cùng nhóm luật sư... |
| 8 | 356 | ngắn (356 từ) | Một tháng sau lễ khai trương chuỗi Trung tâm dịch vụ bảo dưỡng siêu xe công nghệ cao Munich Sài Gòn được tổ chức... |

### Độc Bản Dược Thần: Kẻ Lật Kèo Thế Kỷ

- Link: https://doctieuthuyet.com/truyen/doc-ban-duoc-than-ke-lat-keo-the-ky/
- Mô tả: 181 từ. Ổn.
- Mở đầu mô tả: Năm năm trước Trần Huy Hoàng một thiên tài dược lý đã trải qua một cú sốc không tưởng Hắn Đường Vĩnh Khang đã cướp đi công trình nghiên cứu của anh và đuổi anh ra khỏi Khang Thị nơi mà Hoàng...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1013 | Ổn | Năm năm trước Trần Huy Hoàng một thiên tài dược lý đã trải qua một cú sốc không tưởng Trong những ngày tháng ấy... |
| 2 | 1120 | Ổn | Ánh sáng từ những chiếc đèn neon nhấp nháy trên các con phố Đà Lạt tạo nên một bầu không khí huyền ảo nhưng... |
| 3 | 1119 | Ổn | Tiếng chuông điện thoại reo vang trong không gian tĩnh lặng của văn phòng làm việc Trần Huy Hoàng với đôi tay siết chặt... |
| 5 | 1031 | Ổn | Ánh sáng vàng nhạt của buổi chiều ngả dần về phía tây chiếu xuyên qua những chiếc lá xanh mướt của cây thông trên... |
| 6 | 1331 | Ổn | Đường Vĩnh Khang đứng trước cửa kính lớn của văn phòng Khang Thị nơi ánh đèn neon sáng rực rỡ phản chiếu những giọt... |
| 7 | 1117 | Ổn | Ánh sáng nơi văn phòng Khang Thị chói chang nhưng trong lòng Trần Huy Hoàng lại tối tăm như bầu trời Đà Lạt giữa... |
| 8 | 1349 | Ổn | Ánh mặt trời le lói xuyên qua những đám mây dày đặc tạo nên một bầu không khí ngột ngạt tại trụ sở Khang... |
|  | 1192 | Ổn | Cảnh vật xung quanh Khang Thị một tòa nhà hiện đại lấp lánh ánh đèn neon giữa đêm Đà Lạt huyền ảo như một... |

### Mẹ Vợ Bắt Rửa Bát, Tôi Nấu Tiệc Michelin Chấn Động Phú Quốc

- Link: https://doctieuthuyet.com/truyen/chang-re-bep-truong-an-the/
- Mô tả: 230 từ. Ổn.
- Mở đầu mô tả: Mày chỉ là một thằng rửa bát vô dụng ăn bám nhà tao cút ngay xuống bếp lau sạch đống chén đĩa đó đi Tiếng thét chói tai của mẹ vợ vang lên giữa căn biệt thự sang trọng tại Phú Quốc...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 491 | ngắn (491 từ) | Ánh nắng vàng giòn của vùng biển Phú Quốc chiếu qua ô cửa kính lớn của căn biệt thự sang trọng nằm trong khu... |
| 2 | 451 | ngắn (451 từ) | Nửa giờ sau tại văn phòng Tổng giám đốc khu nghỉ dưỡng siêu sang JW Marriott Phú Quốc không khí căng thẳng bao trùm... |
| 3 | 462 | ngắn (462 từ) | Đêm khuya trong gian bếp thử nghiệm vô trùng của JW Marriott Phú Quốc ánh đèn neon chiếu sáng rực rỡ lên những chiếc... |
| 4 | 383 | ngắn (383 từ) | Tám giờ sáng ngày hôm sau tại khu bếp trung tâm của JW Marriott Phú Quốc bầu không khí căng thẳng dâng cao tột... |
| 5 | 364 | ngắn (364 từ) | Nhìn thấy vẻ mặt hoảng hốt của Lê Hữu Đạt Quốc Bảo khẽ nhếch mép cười lạnh Lê Hữu Đạt ông đang tự hỏi... |
| 6 | 340 | ngắn (340 từ) | Mặc dù Lê Hữu Đạt và Nguyễn Minh Hùng đã bị bắt thế nhưng cuộc chiến thâu tóm ẩm thực Phú Quốc vẫn chưa... |
| 7 | 395 | ngắn (395 từ) | Bốn giờ chiều tại phòng họp khẩn cấp của Sở Du lịch tỉnh Kiên Giang ông Giám đốc Sở cùng đại diện tập đoàn... |
| 8 | 431 | ngắn (431 từ) | Đúng bảy giờ tối đại tiệc Michelin phục vụ đoàn ngoại giao quốc tế được tổ chức vô cùng hoành tráng và lộng lẫy... |

### Cô Gái Bán Trà Sữa Và Hợp Đồng Trăm Tỷ

- Link: https://doctieuthuyet.com/truyen/co-gai-ban-tra-sua-va-hop-dong-tram-ty/
- Mô tả: 221 từ. Ổn.
- Mở đầu mô tả: Một ly trà sữa ba mươi nghìn đồng rách nát cũng đòi bước chân vào hào môn nhà chúng tôi sao Cô chỉ xứng đáng đi phục vụ bưng bê thôi Trong tiệc đính hôn lộng lẫy mẹ chồng tương lai lạnh...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 545 | ngắn (545 từ) | Hương nước hoa đắt tiền quyện cùng mùi rượu vang đỏ thượng hạng lan tỏa khắp sảnh tiệc của trung tâm hội nghị tiệc... |
| 2 | 637 | ngắn (637 từ) | Bước ra khỏi trung tâm tiệc cưới Lâm Vy lập tức cởi bỏ bộ váy cưới vướng víu thay vào đó là bộ đồ... |
| 3 | 437 | ngắn (437 từ) | Đêm hôm đó tại trụ sở văn phòng của chuỗi trà sữa Royal Tea Việt Nam Hoàng Minh và Phương Trinh đang ngồi trước... |
| 4 | 470 | ngắn (470 từ) | Đúng chín giờ sáng ngày hôm sau ngõ nhỏ Nguyễn Đình Chiểu chật kín người khi đoàn thanh tra liên ngành của Sở Y... |
| 5 | 381 | ngắn (381 từ) | Nhìn thấy đoàn thanh tra tuyên bố Sen Việt đạt chuẩn Phương Trinh mặt tái xám vội vàng lên tiếng phá bĩnh Cho dù... |
| 6 | 350 | ngắn (350 từ) | Mặc dù Hoàng Minh và Phương Trinh đã bị bắt thế nhưng gia đình bạn trai cũ vẫn cố gắng dùng mối quan hệ... |
| 7 | 404 | ngắn (404 từ) | Chiều hôm đó tại phòng tiếp dân của Sở Kế hoạch và Đầu tư Thành phố Hồ Chí Minh ông Hoàng Văn Hùng cùng... |
| 8 | 363 | ngắn (363 từ) | Một tháng sau lễ ký kết hợp đồng hợp tác chiến lược và nhượng quyền thương hiệu trị giá một trăm tỷ đồng giữa... |

### Trọng Sinh 2008: Ôm Đất Đông Anh Trước Cơn Sốt Nghìn Tỷ

- Link: https://doctieuthuyet.com/truyen/trong-sinh-2008-con-sot-dat-dong-anh/
- Mô tả: 152 từ. Ổn.
- Mở đầu mô tả: Đông Anh chỉ là vùng đất hoang sơ nghèo đói ven sông Hồng ai mua đất ở đây đều là kẻ điên Nhưng Trần Huy biết chỉ vài năm nữa khi cầu Nhật Tân thông xe và trục Võ Nguyên Giáp hoàn...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 852 | Ổn | Cơn mưa rào mùa hạ năm 2008 trút xuống thị trấn Đông Anh như trút nước từng hạt mưa nặng trĩu đập liên hồi... |
| 2 | 735 | Ổn | Sáng hôm sau ánh nắng chói chang của mùa hè Hà Nội trải dài trên những con phố nhộn nhịp Trần Huy bước vào... |
| 3 | 660 | ngắn (660 từ) | Rời khỏi Sofitel Plaza Trần Huy lập tức bắt xe ôm chạy thẳng sang trụ sở Sở Quy hoạch Kiến trúc Hà Nội trên... |
| 4 | 539 | ngắn (539 từ) | Đúng bốn giờ hai mươi lăm phút chiều Trần Huy bước vào văn phòng của Lê Thu Trang tại tòa nhà Capital Tower trên... |
| 5 | 718 | Ổn | Đúng năm giờ chiều tại mảnh đất hai mẫu ven sông Hồng của Trần Huy ở xã Đông Hội bầu không khí căng thẳng... |
| 6 | 503 | ngắn (503 từ) | Sau đòn vả mặt đau đớn tại khu đất Đông Hội Trần Đức và Đại Long Biên không chịu dừng lại Chúng quyết định... |
| 7 | 497 | ngắn (497 từ) | Trần Huy bước xuống sân văn phòng đối diện với hơn hai trăm người dân đang giận dữ gào thét Anh cầm chiếc loa... |
| 8 | 406 | ngắn (406 từ) | Hai tháng sau khi tập đoàn Hùng Phát sụp đổ bầu trời Đông Anh trong xanh vời vợi gió từ sông Hồng thổi vào... |

### Thần Y Quận 5: Kẻ Cướp Công Trình và Siêu Tỷ Phú

- Link: https://doctieuthuyet.com/truyen/than-y-phong-kham-quan-5/
- Mô tả: 126 từ. Ổn.
- Mở đầu mô tả: Giữa cơn mưa tầm tã trên đường Nguyễn Trãi Trần Duy bị đẩy ra khỏi bệnh viện tay cầm hồ sơ nghiên cứu đã bị cướp Ánh mắt anh vằn tia máu lòng đầy căm phẫn nhưng không còn đường lùi Từ...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 862 | Ổn | Giữa cơn mưa tầm tã trên đường Nguyễn Trãi Trần Duy đứng như một bức tượng gỗ đôi bàn tay lạnh ngắt cầm chặt... |
| 2 | 746 | Ổn | Trong cơn mưa tầm tã những giọt nước từ mái hiên rơi xuống tạo thành những vũng nước nhỏ trên mặt đường Nguyễn Trãi... |
| 3 | 953 | Ổn | Giữa cơn mưa tầm tã trên đường Nguyễn Trãi Trần Duy đứng giữa phố lòng tràn đầy hoang mang và quyết tâm Hồ sơ... |
| 4 | 1087 | Ổn | Giữa cơn mưa nặng hạt trên đường Nguyễn Trãi không khí như bị nén lại tạo ra một cảm giác căng thẳng và hồi... |
| 5 | 990 | Ổn | Trời vẫn mưa tầm tã những giọt nước như những mũi tên sắc nhọn đâm vào mặt Trần Duy khi anh chạy ra khỏi... |
| 6 | 910 | Ổn | Từng giọt mưa rơi xuống như những mũi dao sắc nhọn đâm vào gương mặt Trần Duy khi anh đứng lặng lẽ dưới mái... |
| 7 | 1082 | Ổn | Trần Duy đứng lặng lẽ giữa cơn mưa ánh mắt anh quét qua những tấm biển quảng cáo nhòe nhoẹt trong lòng trào dâng... |
| 8 | 1022 | Ổn | Giữa cơn mưa tầm tã bệnh viện Quận 5 trở thành một chốn hỗn loạn nơi mà sự sống và cái chết chỉ cách... |

### Bị Đuổi Khỏi Khách Sạn, Tôi Mua Luôn Chuỗi Năm Sao

- Link: https://doctieuthuyet.com/truyen/bi-duoi-khoi-khach-san-toi-mua-luon-chuoi-nam-sao/
- Mô tả: 165 từ. Ổn.
- Mở đầu mô tả: Không có tập đoàn Hoàng Gia nâng đỡ anh chỉ là một thằng phục vụ mặc vest vô dụng Lời sỉ nhục của người yêu cũ kiêm Trưởng phòng thương hiệu vang lên giữa sảnh tiệc năm sao chói lọi trước sự...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 543 | ngắn (543 từ) | Ánh đèn chùm pha lê khổng lồ trong sảnh tiệc Grand Ballroom của khách sạn năm sao Hoàng Gia tỏa ra những tia sáng... |
| 2 | 528 | ngắn (528 từ) | Dưới làn mưa xối xả một chiếc xe sedan siêu sang Rolls Royce Ghost màu đen bóng loáng âm thầm dừng lại sát mép... |
| 3 | 449 | ngắn (449 từ) | Đêm khuya Sài Gòn vẫn nhộn nhịp ánh đèn Gia Huy âm thầm quay trở lại hầm B2 của khách sạn Hoàng Gia dưới... |
| 4 | 502 | ngắn (502 từ) | Chín giờ sáng ngày hôm sau tại phòng hội nghị cấp cao của Tổng cục Thuế Thành phố Hồ Chí Minh không khí căng... |
| 5 | 364 | ngắn (364 từ) | Chủ tịch Nguyễn Văn Hoàng nhìn văn bản mua bán nợ đóng dấu đỏ chót của VAMC và Cục Thuế đặt trên bàn khuôn... |
| 6 | 378 | ngắn (378 từ) | Mặc dù Lê Khắc Huy và Nguyễn Mỹ Hạnh đã bị bắt thế nhưng cuộc chiến thâu tóm vẫn chưa hoàn toàn kết thúc... |
| 7 | 400 | ngắn (400 từ) | Chiều hôm đó tại phòng tiếp nhận hồ sơ của Tòa án nhân dân Thành phố Hồ Chí Minh Trần Thế Xương cùng luật... |
| 8 | 364 | ngắn (364 từ) | Một tháng sau đêm tiệc kỷ niệm mười năm thành lập chuỗi khách sạn năm sao Hoàng Gia được tổ chức vô cùng hoành... |

### Chàng Rể Ẩn Thân Miền Tây: Cứu Vườn Sầu Riêng Trăm Tỷ

- Link: https://doctieuthuyet.com/truyen/chang-re-hao-mon-mien-tay/
- Mô tả: 105 từ. Ổn.
- Mở đầu mô tả: Lâm Phong giấu kín thân phận thiếu gia chọn làm công trong vườn sầu riêng Bến Tre Chỉ vì một lý do duy nhất tìm kiếm những người thật lòng với mình Minh Thư cô gái gánh vác khu vườn đang đứng...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 892 | Ổn | Ánh nắng sớm mai xuyên qua những tán lá xanh mướt của vườn sầu riêng Bến Tre tạo nên một khung cảnh vừa ấm... |
| 2 | 840 | Ổn | Gió miền Tây thổi nhẹ đưa theo hương vị ngọt ngào của những trái sầu riêng đang vào mùa Lâm Phong đứng giữa khu... |
| 3 | 752 | Ổn | Ánh sáng mờ ảo của buổi sớm ban mai len lỏi qua những tán lá xanh mướt của khu vườn sầu riêng tạo nên... |
| 4 | 868 | Ổn | Ánh nắng chiều vàng vọt nhuộm lên những tán cây sầu riêng trong khu vườn Bến Tre tạo nên một khung cảnh vừa bình... |
| 5 | 1007 | Ổn | Trong không khí ngột ngạt của vườn sầu riêng Bến Tre Lâm Phong cảm nhận rõ ràng sự căng thẳng đang bao trùm mọi... |
| 6 | 1054 | Ổn | Mặt trời đang nhô lên trên những hàng dừa xanh mướt của Bến Tre ánh sáng vàng rực rỡ chiếu rọi qua ô cửa... |
| 7 | 885 | Ổn | Ánh sáng nhạt nhòa của buổi chiều tà nhuộm vàng cả khu vườn sầu riêng nhưng trong lòng Lâm Phong một cơn bão đang... |
| 8 | 984 | Ổn | Ánh nắng rực rỡ của buổi sáng miền Tây chiếu rọi qua những tán cây sầu riêng làm cho không khí trong vườn trở... |

### Bị Sa Thải Trước Giờ Đấu Thầu: Một Mình Thắng Gói AI Nghìn Tỷ

- Link: https://doctieuthuyet.com/truyen/sau-khi-bi-sa-thai-toi-thang-goi-thau-nghin-ty/
- Mô tả: 116 từ. Ổn.
- Mở đầu mô tả: Ba giờ trước giờ G mọi thứ như sụp đổ trước mắt Nguyễn Minh Khang Thẻ nhân viên của anh bị bẻ đôi laptop bị niêm phong như một tội đồ Người yêu cũ đứng bên đối thủ ánh mắt mỉm cười...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 820 | Ổn | Ba giờ trước giờ G mọi thứ như sụp đổ trước mắt Nguyễn Minh Khang Trong không khí căng thẳng của văn phòng mùi... |
| 2 | 1107 | Ổn | Ánh đèn neon chói mắt từ những tòa nhà xung quanh hòa quyện với nhịp sống của thành phố Hồ Chí Minh nhưng trong... |
| 3 | 946 | Ổn | Nguyễn Minh Khang đứng giữa lòng thành phố nơi mà ánh đèn neon chói lóa phản chiếu lên mặt đường ẩm ướt tạo nên... |
| 4 | 902 | Ổn | Ba giờ trước giờ G Nguyễn Minh Khang cảm giác như tim mình đập loạn xạ từng nhịp đập vang lên như tiếng trống... |
| 5 | 984 | Ổn | Nguyễn Minh Khang đứng bên cửa sổ ánh mắt nhìn ra ngoài đường phố tấp nập của Hà Nội nơi những chiếc xe cộ... |
| 6 | 1036 | Ổn | Ánh đèn neon chói lòa từ những tòa nhà cao tầng ở trung tâm Hà Nội phản chiếu lên mặt đường ướt sũng sau... |
| 7 | 1003 | Ổn | Nguyễn Minh Khang đứng lặng lẽ bên ngoài hội trường cảm giác hồi hộp như cơn gió lạnh bất chợt thổi qua tâm trí... |
| 8 | 824 | Ổn | Ánh đèn rọi sáng sân khấu khiến Nguyễn Minh Khang cảm thấy như đang đứng giữa một cơn bão tố Tim anh đập loạn... |

### Kẻ Phế Vật Trở Về: Đòi Lại Gia Tộc Sau 12 Năm

- Link: https://doctieuthuyet.com/truyen/ke-phe-vat-ngay-ay-hom-nay-tro-ve/
- Mô tả: 182 từ. Ổn.
- Mở đầu mô tả: Mười hai năm trước đêm mưa tầm tã Lâm Phong bị ném khỏi Lâm gia như một phế vật Chú ruột hắn Lâm Minh đứng cười nhạo với quyền thừa kế trong tay Hôn thê của hắn Ngọc Anh lạnh lùng quay...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 688 | ngắn (688 từ) | Đêm mưa tầm tã tiếng gió rít qua từng khe cửa sổ Lâm Phong đứng lặng lẽ bên ngoài cánh cổng lớn của Lâm... |
| 2 | 895 | Ổn | Lâm Phong đứng trước tòa nhà cao tầng sang trọng của tập đoàn Ngọc Gia nơi mà Ngọc Anh hiện đang làm việc Ánh... |
| 3 | 962 | Ổn | Đêm đang buông xuống ánh đèn vàng nhạt chiếu rọi qua cửa sổ của căn phòng cũ kỹ thuộc về Lâm gia Lâm Phong... |
| 4 | 894 | Ổn | Ánh đèn chói lóa từ những chiếc đèn chùm mạ vàng trong sảnh tiệc Lâm gia làm nổi bật từng chi tiết xa hoa... |
| 5 | 959 | Ổn | Lâm Phong đứng trước cánh cửa lớn của Lâm gia lòng tràn đầy quyết tâm nhưng cũng không thiếu phần lo lắng Đêm đã... |
| 6 | 876 | Ổn | Ánh đèn neon nhấp nháy bên ngoài cửa sổ khung kính của văn phòng Lâm Phong tạo nên một bầu không khí mờ ảo... |
| 7 | 892 | Ổn | Gió đêm thổi qua những tán cây bên ngoài mang theo một cơn rùng mình lạnh lẽo vào không gian tĩnh lặng trong căn... |
| 8 | 913 | Ổn | Ánh sáng chói chang của những chiếc đèn chùm trong đại sảnh Lâm gia rọi xuống tạo nên một không khí nặng nề và... |

### Phế Vật Trở Về: Cuộc Báo Thù Rực Lửa

- Link: https://doctieuthuyet.com/truyen/do-phe-vat-nam-do-hom-nay-ta-tro-ve/
- Mô tả: 99 từ. Ổn.
- Mở đầu mô tả: Trong đêm mưa bão tơi tả Lâm Phong bị đẩy ra khỏi gia tộc mà không chút thương tiếc Hắn chỉ là một phế vật nhưng trong lòng lại chứa đựng lửa giận chưa bao giờ tắt Bàn tay của người chú...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 756 | Ổn | Đêm mưa bão tơi tả những hạt mưa to như những viên bi sắt rơi xuống mặt đất tạo ra âm thanh rào rạt... |
| 2 | 932 | Ổn | Trời vẫn mưa những giọt nước nặng trĩu như muốn đè bẹp mọi hi vọng trong lòng Lâm Phong Hắn đứng trước một tòa... |
| 3 | 898 | Ổn | Giữa cơn bão đêm gió lồng lộng thổi qua những tán cây cổ thụ Lâm Phong đứng bên ngoài ngôi nhà của gia tộc... |
| 4 | 1254 | Ổn | Trong ánh đèn mờ ảo của quán cà phê ven đường Lâm Phong và Nguyễn Thùy Linh ngồi đối diện nhau ánh mắt họ... |
| 5 | 962 | Ổn | Đêm đã buông xuống những giọt mưa như những mũi dao sắc nhọn đâm thẳng vào mặt đất tạo ra âm thanh lộp độp... |
| 6 | 1226 | Ổn | Ánh đèn vàng của những ngọn đèn đường hắt lên mặt đường ẩm ướt sau trận mưa như dát vàng nhưng với Lâm Phong... |
| 7 | 931 | Ổn | Trong không gian ngột ngạt của phòng họp gia tộc Lâm mùi ẩm mốc hòa với hơi thở nặng nề của sự căng thẳng... |
| 8 | 1007 | Ổn | Trời đã vào đêm bão tố bên ngoài vẫn chưa có dấu hiệu dừng lại Lâm Phong đứng trước tòa nhà cao tầng của... |

### Kỹ Sư Bị Cả Xã Khinh Là Kẻ Nói Điên, Lá Thư Cuối Cùng Của Biển Cứu Sống Cát Hải Trong Đêm Bão

- Link: https://doctieuthuyet.com/truyen/buc-thu-cuoi-cung-cua-bien/
- Mô tả: 131 từ. Ổn.
- Mở đầu mô tả: Hoàng Quân bị chủ thầu Trịnh mắng là kẻ phá đám khi anh cảnh báo nền đất Cát Hải đang rỗng ruột trước bão số 3 Đình Vũ Cả phòng họp cười nhạt dân làng chửi anh làm chậm dự án nghìn...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1119 | Ổn | Hoàng Quân đứng trên mũi Cát Hải gió biển thổi từng cơn xô vào mặt anh như những nhát dao sắc bén Mồ hôi... |
| 2 | 1074 | Ổn | Hoàng Quân đứng giữa phòng làm việc chật chội ánh mắt dõi theo từng hình ảnh hiện lên từ máy quét 3D địa chất... |
| 3 | 1605 | Ổn | html Trong căn phòng họp nhỏ ánh đèn neon lạnh lẽo phản chiếu lên những khuôn mặt căng thẳng của Hoàng Quân và Vũ... |
| 4 | 1018 | Ổn | Gió từ biển Đông thổi vào bờ với sức mạnh không thể tưởng tượng nổi từng cơn cuồng phong gầm thét như một con... |
| 5 | 1216 | Ổn | Ánh sáng le lói từ chiếc đèn pin thủng thẳng chiếu sáng không gian hẹp nơi mà Hoàng Quân và Vũ Phương Mai đang... |
| 6 | 1105 | Ổn | Hoàng Quân đứng trên nền đất Cát Hải ẩm ướt gió biển rít từng cơn lạnh lẽo gương mặt anh căng ra như một... |
| 7 | 1087 | Ổn | Cát Hải Hải Phòng bầu trời ngày hôm nay như muốn trút hết những gì còn lại trong lòng mình sau cơn bão số... |
| 8 | 1061 | Ổn | Hoàng Quân và Vũ Phương Mai đứng trên bờ biển Cát Hải nơi mà những con sóng ầm ầm vỗ vào đất liền như... |

### Hệ Thống Trí Tuệ Nhân Tạo: Xuyên Không Đến Tương Lai

- Link: https://doctieuthuyet.com/truyen/he-thong-tri-tue-nhan-tao-xuyen-khong-den-tuong-lai/
- Mô tả: 136 từ. Ổn.
- Mở đầu mô tả: Bùi Thu Hà một kỹ sư tài năng đột nhiên bị cuốn vào thế giới tương lai năm 2046 với sự hiện diện của hệ thống trí tuệ nhân tạo Genesis 08 Trong bối cảnh Sài Gòn bị tàn phá bởi những...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1094 | Ổn | Ánh đèn chói lóa từ những chiếc đèn LED trên trần nhà phản chiếu lên mặt bàn kính tạo ra những hình ảnh lấp... |
| 2 | 1006 | Ổn | Ánh sáng trắng lạnh lẽo từ những đèn huỳnh quang trên trần nhà phản chiếu xuống từng ngóc ngách của phòng nghiên cứu tạo... |
| 3 | 1058 | Ổn | Bùi Thu Hà ngồi ở bàn làm việc ánh sáng xanh mờ ảo từ màn hình máy tính phản chiếu lên gương mặt cô... |
| 4 | 1138 | Ổn | Cơn bão số 3 ập đến như một cơn thịnh nộ của thiên nhiên cuốn theo gió xoáy lạnh lẽo và những cơn mưa... |
| 5 | 1004 | Ổn | Ánh sáng xanh nhạt từ màn hình máy tính phản chiếu lên khuôn mặt Bùi Thu Hà khiến đôi mắt cô sáng rực như... |
| 6 | 1134 | Ổn | Ánh đèn neon từ những tòa nhà chọc trời ở Sài Gòn 2046 phản chiếu lên mặt đường ẩm ướt tạo nên một bức... |
| 7 | 1165 | Ổn | Trong không khí oi bức của Sài Gòn năm 2046 Bùi Thu Hà đứng giữa phòng làm việc với đôi tay siết chặt lại... |
| 8 | 1076 | Ổn | Ánh sáng chói lóa từ màn hình máy tính phản chiếu lên gương mặt Bùi Thu Hà khiến cô cảm nhận rõ từng đường... |

### Tôi Giả Nghèo Đi Ra Mắt, Mẹ Người Yêu Đòi Sính Lễ 900 Triệu Và Bị Vả Mặt Ngay Tại Chung Cư Hoài Đức

- Link: https://doctieuthuyet.com/truyen/toi-gia-ngheo-di-ra-mat-me-nguoi-yeu-doi-sinh-le-900-trieu/
- Mô tả: 121 từ. Cần sửa: tên truyện rất dài, dễ vỡ layout/SEO
- Mở đầu mô tả: Trần Tuấn Anh mặc chiếc áo sơ mi bạc màu đi ra mắt để thử lòng nhà người yêu không ngờ vừa ngồi xuống đã bị mẹ vợ tương lai đòi sính lễ 900 triệu Bà ta gõ đũa lên mâm cơm...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 979 | Ổn | Trần Tuấn Anh đứng trước gương cảm giác như mình đang đóng một vai diễn nào đó trong một bộ phim không hồi kết... |
| 2 | 1030 | Ổn | Ánh đèn vàng nhạt từ chiếc quạt trần lồng lộng giữa gian phòng khách nhà Thùy Chi ánh sáng chao chao như muốn xua... |
| 3 | 1127 | Ổn | Ánh nắng buổi chiều len lỏi qua những tán cây tạo ra những mảng sáng tối đan xen trên mặt đất Tuấn Anh đứng... |
| 4 | 1037 | Ổn | Ánh nắng ban mai len lỏi qua từng khe cửa sổ chiếu rọi xuống mặt bàn nơi Tuấn Anh ngồi trong lòng anh tràn... |
| 5 | 1193 | Ổn | Mặt trời đã khuất sau những dãy nhà cao tầng ở trung tâm Sài Gòn ánh đèn neon bắt đầu nhấp nháy tạo nên... |
| 6 | 923 | Ổn | Tuấn Anh đứng giữa không gian tĩnh lặng của căn phòng nơi ánh sáng nhợt nhạt từ chiếc đèn bàn chiếu lên những giấy... |
| 7 | 1032 | Ổn | Ánh mặt trời nhạt nhòa len lỏi qua khung cửa sổ kính của phòng họp trong tòa án nhân dân quận 1 nhưng không... |
| 8 | 1230 | Ổn | Gió từ dòng sông Hồng thổi vào phố cổ Hà Nội mang theo hơi lạnh của buổi chiều muộn khiến không khí trở nên... |

### Thành Phố Chìm Trong Bóng Tối, Kỹ Sư Bị Xem Là Kẻ Điên Kích Hoạt Nguồn Sáng Cuối Cùng

- Link: https://doctieuthuyet.com/truyen/bong-dem-va-anh-sang/
- Mô tả: 117 từ. Ổn.
- Mở đầu mô tả: Sau đại thảm họa mất điện thành phố chìm trong bóng tối và những nhóm người sống sót tranh nhau từng bình ắc quy cuối cùng Minh bị đội bảo vệ khu trú ẩn gọi là kẻ hoang tưởng khi anh nói...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1104 | Ổn | Hà Nội thành phố từng nổi tiếng với khung cảnh nhộn nhịp giờ đã chìm trong màn đêm dày đặc và tĩnh lặng đến... |
| 2 | 851 | Ổn | Gò Vấp nơi những ngôi nhà cũ kỹ vẫn đứng sừng sững như những gã khổng lồ bị lãng quên mờ mịt trong bóng... |
| 3 | 854 | Ổn | Ánh sáng lờ mờ từ chiếc đèn pin yếu ớt trong tay Lê Vân chỉ đủ để soi sáng một khoảng không nhỏ trước... |
| 4 | 844 | Ổn | Trời đã tối hẳn những con đường hoang vắng của thành phố đổ nát hiện ra dưới ánh đèn pin lờ mờ Lê Vân... |
| 5 | 893 | Ổn | Ánh sáng mờ nhạt từ chiếc đèn pin cầm tay của Lê Vân chiếu rọi xuống những bức tường đổ nát của một tòa... |
| 6 | 929 | Ổn | Ánh sáng từ chiếc đèn pin yếu ớt lướt qua những bóng tối dày đặc khiến không khí trở nên ngột ngạt và nặng... |
| 7 | 953 | Ổn | Ánh sáng của chiếc đèn pin loang lổ trên những bức tường cũ kỹ nơi mà bụi bặm đã tích tụ trong suốt hàng... |
| 8 | 912 | Ổn | Trong khoảnh khắc yên lặng trước bão tố Lê Vân đứng giữa vòng tròn ánh sáng vàng vọt từ những ngọn đuốc ánh mắt... |

### Mẹ Chồng Gọi Tôi Là Người Ngoài, Sổ Đỏ Biệt Thự Gò Vấp 5 Tỷ Khiến Cả Mâm Giỗ Câm Lặng

- Link: https://doctieuthuyet.com/truyen/nha-cua-me-chong-khong-cua-toi/
- Mô tả: 110 từ. Ổn.
- Mở đầu mô tả: Trong mâm giỗ ba chồng tôi bị mẹ chồng chỉ thẳng mặt gọi là người ngoài và bắt dọn khỏi căn biệt thự Gò Vấp sau bốn năm nhẫn nhịn Chị chồng cười nhạo tôi dân tỉnh chồng cúi đầu không nói...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 693 | ngắn (693 từ) | Mâm cơm giỗ ba chồng bày biện trang trọng nhưng không khí lại nặng nề như thể có một tảng đá lớn đè lên... |
| 2 | 729 | Ổn | Tôi ngồi một mình trong căn phòng nhỏ ánh đèn vàng ấm áp hắt lên những món đồ nội thất giản dị Những ký... |
| 3 | 877 | Ổn | Buổi sáng hôm sau ánh nắng len lỏi qua những tán cây xanh rì ngoài cửa sổ nhuộm vàng cả không gian trong căn... |
| 4 | 1127 | Ổn | Lê Vân đứng giữa phòng khách rộng lớn của căn biệt thự nơi mà cô đã từng mơ ước có được Từng bức tranh... |
| 5 | 875 | Ổn | Ánh nắng chói chang xuyên qua khung cửa sổ của căn phòng nhỏ nhưng lòng tôi vẫn tối tăm như bầu trời u ám... |
| 6 | 903 | Ổn | Đêm đã buông xuống không khí trong nhà vẫn tĩnh lặng nhưng nặng nề như một bầu trời u ám Tôi ngồi trên chiếc... |
| 7 | 852 | Ổn | Ánh sáng chói chang từ bóng đèn trong phòng khách biệt thự Gò Vấp khiến tôi cảm thấy như bị dồn vào một cái... |
| 8 | 960 | Ổn | Hơi thở của tôi như ngưng lại khi cánh cửa của phòng xử án mở ra Ánh mắt tôi hướng về phía bàn xét... |

### Họa Sĩ Mù Bị Thiếu Gia Cướp Tranh, Ánh Sáng Trong Đêm Khiến Cả Phòng Đấu Giá Hà Nội Im Phăng Phắc

- Link: https://doctieuthuyet.com/truyen/anh-sang-trong-dem/
- Mô tả: 136 từ. Cần sửa: tên truyện rất dài, dễ vỡ layout/SEO
- Mở đầu mô tả: Lê Gia Minh là họa sĩ sơn mài mù bị thiếu gia họ Lâm cười nhạo là kẻ ăn may rồi ngang nhiên cướp bức tranh cuối cùng của anh để đem bán tại phòng đấu giá Bạn bè quay lưng chủ...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1016 | Ổn | Gió nhẹ nhàng thổi qua phố Hàng Bông mang theo hương vị của những quán cà phê và mùi sơn mài thơm nồng Lê... |
| 2 | 1153 | Ổn | Gia Minh đứng giữa không gian tăm tối của sảnh Metropole Hà Nội ánh đèn vàng ấm áp từ những chiếc đèn chùm lung... |
| 3 | 1161 | Ổn | Trong không gian mang hơi thở của những ngày cuối tháng Bảy ánh nắng len lỏi qua những tán cây lớn ở công viên... |
| 4 | 1103 | Ổn | Đêm tối buông xuống như một tấm màn dày đặc bao trùm mọi thứ xung quanh Ánh đèn đường yếu ớt le lói chỉ... |
| 5 | 1271 | Ổn | Gia Minh đứng trước màn hình máy tính ánh sáng từ nó phản chiếu lên khuôn mặt anh làm nổi bật đôi mắt sáng... |
| 6 | 1185 | Ổn | Gia Minh đứng trước cánh cửa kính của ngân hàng Techcombank trên đường Trần Hưng Đạo lòng ngổn ngang trăm mối Hơi thở dồn... |
| 7 | 1309 | Ổn | Hà Nội một buổi chiều oi ả ánh nắng chói chang như muốn nướng chảy mọi thứ dưới lòng đất Tuệ An đứng trước... |
| 8 | 1080 | Ổn | Phiên tòa sáng nay diễn ra tại Tòa án Nhân dân thành phố Hồ Chí Minh không khí nặng nề và căng thẳng như... |

### Giám Đốc Ngầm Đi Thực Tập Bị Trưởng Phòng Cướp Dự Án, Một Cuộc Họp Khiến Cả Công Ty Đứng Hình

- Link: https://doctieuthuyet.com/truyen/giam-doc-ngam-thuc-tap-sinh-khong-de-choc/
- Mô tả: 121 từ. Ổn.
- Mở đầu mô tả: Lâm Uyển Nhu giấu thân phận ái nữ tập đoàn để làm thực tập sinh quèn tại văn phòng Quận 1 chỉ muốn xem công ty vận hành thật ra sao Trưởng phòng nhân sự Tô Khanh Khanh tưởng cô dễ bắt...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 974 | Ổn | Ngày đầu tiên tại văn phòng Lâm Thị Lâm Uyển Nhu cảm thấy hồi hộp đến mức mồ hôi lạnh chảy dọc sống lưng... |
| 2 | 1018 | Ổn | Ánh đèn neon chói lóa của thành phố Hồ Chí Minh rọi xuống những con đường trong Quận 1 nơi mà Lâm Uyển Nhu... |
| 3 | 756 | Ổn | Lâm Uyển Nhu ngồi thừ người trên chiếc ghế da màu đen bóng loáng ánh đèn neon từ những cửa sổ lớn của văn... |
| 4 | 847 | Ổn | Ánh nắng đầu giờ chiều lấp lánh qua những tấm kính của tòa nhà văn phòng hiện đại ở Quận 1 TP HCM Lâm... |
| 5 | 950 | Ổn | Trong căn phòng làm việc rộng rãi của giám đốc điều hành Lục Dạ Minh ánh đèn vàng ấm áp chiếu sáng mặt bàn... |
| 6 | 1070 | Ổn | Ánh nắng từ những ô cửa sổ lớn của văn phòng tầng 12 tòa nhà Lâm Thị chiếu rọi vào không gian tạo nên... |
| 7 | 857 | Ổn | Ánh đèn neon từ những tấm kính lớn của tòa nhà Lâm Thị phản chiếu xuống sàn gạch bóng loáng Lâm Uyển Nhu đứng... |
| 8 | 981 | Ổn | Ánh sáng vàng ấm áp từ những chiếc đèn trong phòng họp sáng rực nhưng không thể xua tan nổi bầu không khí căng... |

### Nhân Viên Bị Sếp Cướp Công Thức Dạ Dày, Log Lab Khiến Buổi IPO Nghìn Tỷ Đổ Sập Trước Truyền Thông

- Link: https://doctieuthuyet.com/truyen/lot-mat-nguoi-sep-cuop-cong/
- Mô tả: 139 từ. Cần sửa: tên truyện rất dài, dễ vỡ layout/SEO
- Mở đầu mô tả: Lâm Trạch thức trắng sáu tháng trong phòng lab để hoàn thiện công thức thuốc dạ dày nhưng đến ngày công ty chuẩn bị IPO sếp Hoàng Quốc Trung đứng trên sân khấu nhận hết công lao Anh bị tịch thu thẻ...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 1098 | Ổn | Lâm Trạch đứng trước gương nhìn chằm chằm vào hình ảnh phản chiếu của mình Ánh đèn trong phòng sáng rực nhưng tâm trạng... |
| 2 | 1014 | Ổn | Hàng Bông sớm tinh mơ không khí trong lành hòa quyện với hương thơm của những ly cà phê mới pha Ánh nắng vàng... |
| 3 | 908 | Ổn | Một buổi sáng ảm đạm tại Hà Nội không khí trong văn phòng Lotte mang một màu sắc u ám hơn thường lệ Khánh... |
| 4 | 1195 | Ổn | Một buổi sáng u ám tại trụ sở Công ty Dược phẩm Lâm Trạch không khí nặng nề như bầu trời xám xịt bên... |
| 5 | 1005 | Ổn | Trời Hà Nội dường như đang gồng mình trước cơn bão lớn những cơn gió mạnh thổi qua khiến cây cối bên ngoài văn... |
| 6 | 1252 | Ổn | Đêm Hà Nội chìm trong bóng tối chỉ còn lại những ánh đèn vàng vọt le lói từ các tòa nhà cao tầng Khánh... |
| 7 | 1084 | Ổn | Trong căn phòng nhỏ hẹp tại một quán cà phê ven đường ở Hà Nội không khí nặng nề như bầu trời trước cơn... |
| 8 | 1141 | Ổn | Không khí trong phòng họp tại một khách sạn sang trọng ở Sài Gòn trở nên ngột ngạt như thể mọi người đều đang... |

### Cô Gái Bị Gọi Là Con Bé Gần Máy In, Gấu Bông Quỷ Vương Giúp Cô Lật Mặt Cả Phòng Kế Toán

- Link: https://doctieuthuyet.com/truyen/dung-goi-toi-la-con-be-gan-may-in/
- Mô tả: 123 từ. Ổn.
- Mở đầu mô tả: Tô Khanh Khanh bị cả văn phòng gọi là con bé gần máy in ngày nào cũng bị đẩy việc trừ lương và đổ lỗi sai số liệu Đêm tăng ca cô nhặt được một con gấu bông cũ trong kho hồ...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 883 | Ổn | Tô Khanh Khanh một nữ nhân viên văn phòng bình thường vừa trải qua một ngày mệt mỏi Cô ngồi thụp xuống bên bàn... |
| 2 | 869 | Ổn | Đêm buông xuống không gian trong căn hộ nhỏ của Tô Khanh Khanh trở nên mờ mịt và tĩnh lặng đến kỳ lạ Cô... |
| 3 | 847 | Ổn | Ánh nắng chiều nhuộm vàng góc phố nhỏ nơi Tô Khanh Khanh và Thẩm Triệt đang đứng nhưng không khí xung quanh lại nặng... |
| 4 | 906 | Ổn | Tô Khanh Khanh đứng giữa phòng khách bừa bộn ánh đèn vàng nhạt trên trần nhà lấp lánh như những vì sao trong đêm... |
| 5 | 900 | Ổn | Tô Khanh Khanh đứng giữa phòng khách chật chội ánh đèn vàng nhạt hắt lên chiếc gấu bông Pikachu đang ngồi chễm chệ trên... |
| 6 | 1062 | Ổn | Giữa không gian ngột ngạt của căn phòng nhỏ Tô Khanh Khanh ngồi co ro trên ghế sofa ánh mắt dán chặt vào gấu... |
| 7 | 1009 | Ổn | Tô Khanh Khanh đứng giữa căn phòng tối tăm ánh đèn mờ ảo chiếu lên gương mặt căng thẳng của cô Ánh mắt cô... |
| 8 | 1164 | Ổn | Ánh sáng mặt trời xuyên qua những tán cây xanh mướt của công viên Thống Nhất nơi mà Tô Khanh Khanh và Thẩm Triệt... |

### Con Dâu Dân Tỉnh Bị Khinh Trong Căn Nhà 4,8 Tỷ, Một Bộ Hồ Sơ Khiến Cả Nhà Chồng Trắng Mặt

- Link: https://doctieuthuyet.com/truyen/dan-tinh-len-pho-khi-con-dau-khong-con-im-ru/
- Mô tả: 119 từ. Ổn.
- Mở đầu mô tả: Lan Anh ngồi cuối bàn trong bữa cơm giỗ nghe mẹ chồng mắng cô là dân tỉnh lên phố bám nhà chồng để đổi đời Chị chồng đẩy tới một tờ giấy vay nợ ép cô gánh thêm tiền sửa nhà còn...

| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |
|---:|---:|---|---|
| 1 | 866 | Ổn | Trong bữa cơm giỗ chồng không khí ngột ngạt bao trùm căn phòng sang trọng Lan Anh con dâu dân tỉnh lên phố ngồi... |
| 2 | 735 | Ổn | Trong cái không gian tĩnh lặng của căn phòng Lan Anh cảm thấy lòng mình như đang dấy lên một cơn sóng dữ Ánh... |
| 3 | 942 | Ổn | Trong không gian ngột ngạt của bữa cơm giỗ Lan Anh cảm nhận từng ánh mắt soi mói đổ dồn về phía mình Mẹ... |
| 4 | 911 | Ổn | Trời đã ngả màu chiều những tia nắng cuối ngày len lỏi qua các khe cửa sổ tạo nên những vệt sáng lấp lánh... |
| 5 | 978 | Ổn | Trong bầu không khí ngột ngạt của căn nhà sang trọng Lan Anh cảm thấy như mình đang bị dồn vào chân tường Ánh... |
| 6 | 990 | Ổn | Trong bữa cơm giỗ chồng không khí ngột ngạt và nặng nề như một lớp bụi dày đè nén lên mọi người Lan Anh... |
| 7 | 1045 | Ổn | Trong không khí căng thẳng như dây đàn Lan Anh cảm thấy từng nhịp tim đập điên cuồng trong lồng ngực Ánh đèn neon... |
| 8 | 949 | Ổn | Ánh sáng nhạt dần khi mặt trời lặn bóng tối dần bao trùm căn nhà sang trọng nơi mà Lan Anh đang phải đối... |

## Chương chưa map được vào trang truyện

Các chương dưới đây có trong REST API nhưng không thấy trong danh sách chương của 6 trang truyện public. Nên kiểm tra parent/post meta hoặc truyện bị ẩn.

- Chương 5: Thâu Tóm Ngược – Đòn Chí Mạng (873 từ): https://doctieuthuyet.com/chuong/chuong-5-thau-tom-nguoc-don-chi-mang/ 
- Chương 4: Cơn Bão Pháp Lý (850 từ): https://doctieuthuyet.com/chuong/chuong-4-con-bao-phap-ly/ 
- Chương 3: Bẫy Tài Chính Đang Chờ Sẵn (765 từ): https://doctieuthuyet.com/chuong/chuong-3-bay-tai-chinh-dang-cho-san/ 
- Chương 2: Ánh Sáng Giữa Bóng Tối (751 từ): https://doctieuthuyet.com/chuong/chuong-2-anh-sang-giua-bong-toi/ 
- Chương 1: Cơn Bão Tại Trụ Sở (716 từ): https://doctieuthuyet.com/chuong/chuong-1-con-bao-tai-tru-so/ 
- Chương 13: Giao Diện Mới (455 từ): https://doctieuthuyet.com/chuong/chuong-13-giao-dien-moi/ ==> ngắn (455 từ)
- Chương 12: Sau Cơn Bão (357 từ): https://doctieuthuyet.com/chuong/chuong-12-sau-con-bao/ ==> ngắn (357 từ)
- Chương 11: Sụp Đổ (678 từ): https://doctieuthuyet.com/chuong/chuong-11-sup-do/ ==> ngắn (678 từ)
- Chương 10: Lời Thú Tội Trên Sóng (730 từ): https://doctieuthuyet.com/chuong/chuong-10-loi-thu-toi-tren-song/ 
- Chương 9: Buổi Nói Chuyện “mẹ – Con” (776 từ): https://doctieuthuyet.com/chuong/chuong-9-buoi-noi-chuyen-me-con/ 
- Chương 8: Setup Livestream (513 từ): https://doctieuthuyet.com/chuong/chuong-8-setup-livestream/ ==> ngắn (513 từ)
- Chương 7: Bẫy Ngược (569 từ): https://doctieuthuyet.com/chuong/chuong-7-bay-nguoc/ ==> ngắn (569 từ)
- Chương 5: Quá Khứ Chôn Vùi (407 từ): https://doctieuthuyet.com/chuong/chuong-5-qua-khu-chon-vui/ ==> ngắn (407 từ)
- Chương 6: Ảnh Hậu Đạo Đức (322 từ): https://doctieuthuyet.com/chuong/chuong-6-anh-hau-dao-duc/ ==> ngắn (322 từ)
- Chương 3: Bóng Đen Trong Hệ Thống (374 từ): https://doctieuthuyet.com/chuong/chuong-3-bong-den-trong-he-thong/ ==> ngắn (374 từ)
- Chương 4: Shadow Backup (658 từ): https://doctieuthuyet.com/chuong/chuong-4-shadow-backup/ ==> ngắn (658 từ)
- Chương 2: Viên Thuốc Màu Trắng (588 từ): https://doctieuthuyet.com/chuong/chuong-2-vien-thuoc-mau-trang/ ==> ngắn (588 từ)
- Chương 1: Nàng Dâu Ngoan Hiền (568 từ): https://doctieuthuyet.com/chuong/chuong-1-nang-dau-ngoan-hien/ ==> ngắn (568 từ)
- Chương 5: Ảnh Hậu Sập Vai (1287 từ): https://doctieuthuyet.com/chuong/chuong-5-anh-hau-sap-vai/ 
- Chương 4: Cái Bẫy Ngoại Tình (1059 từ): https://doctieuthuyet.com/chuong/chuong-4-cai-bay-ngoai-tinh/ 
- Chương 3: Người Đàn Bà Trong Ảnh Cũ (1347 từ): https://doctieuthuyet.com/chuong/chuong-3-nguoi-dan-ba-trong-anh-cu/ 
- Chương 2: Ly Trà Trước Giờ Họp (1181 từ): https://doctieuthuyet.com/chuong/chuong-2-ly-tra-truoc-gio-hop/ 
- Chương 1: Người Mẹ Chồng Hoàn Hảo (1185 từ): https://doctieuthuyet.com/chuong/chuong-1-nguoi-me-chong-hoan-hao/ 
- Chương 5: Cái Bàn Không Còn Thuộc Về Họ (1544 từ): https://doctieuthuyet.com/chuong/chuong-5-cai-ban-khong-con-thuoc-ve-ho-4/ 
- Chương 3: Căn Nhà Đổi Lấy Sự Yên Ổn (1079 từ): https://doctieuthuyet.com/chuong/chuong-3-can-nha-doi-lay-su-yen-on-4/ 
- Chương 4: File Cuối Cùng (1163 từ): https://doctieuthuyet.com/chuong/chuong-4-file-cuoi-cung-4/ 
- Chương 2: Người Chồng Biết Muộn (997 từ): https://doctieuthuyet.com/chuong/chuong-2-nguoi-chong-biet-muon-4/ 
- Chương 1: Sáu Trăm Triệu Tiền Ở Nhờ (1894 từ): https://doctieuthuyet.com/chuong/chuong-1-sau-tram-trieu-tien-o-nho-4/ 
- Chương 5: Cái Bàn Không Còn Thuộc Về Họ (1543 từ): https://doctieuthuyet.com/chuong/chuong-5-cai-ban-khong-con-thuoc-ve-ho-3/ 
- Chương 4: File Cuối Cùng (1163 từ): https://doctieuthuyet.com/chuong/chuong-4-file-cuoi-cung-3/ 
- Chương 3: Căn Nhà Đổi Lấy Sự Yên Ổn (1150 từ): https://doctieuthuyet.com/chuong/chuong-3-can-nha-doi-lay-su-yen-on-3/ 
- Chương 2: Người Chồng Biết Muộn (997 từ): https://doctieuthuyet.com/chuong/chuong-2-nguoi-chong-biet-muon-3/ 
- Chương 1: Sáu Trăm Triệu Tiền Ở Nhờ (1894 từ): https://doctieuthuyet.com/chuong/chuong-1-sau-tram-trieu-tien-o-nho-3/ 
- Chương 5: Cái Bàn Không Còn Thuộc Về Họ (1543 từ): https://doctieuthuyet.com/chuong/chuong-5-cai-ban-khong-con-thuoc-ve-ho-2/ 
- Chương 4: File Cuối Cùng (1163 từ): https://doctieuthuyet.com/chuong/chuong-4-file-cuoi-cung-2/ 
- Chương 3: Căn Nhà Đổi Lấy Sự Yên Ổn (1150 từ): https://doctieuthuyet.com/chuong/chuong-3-can-nha-doi-lay-su-yen-on-2/ 
- Chương 2: Người Chồng Biết Muộn (997 từ): https://doctieuthuyet.com/chuong/chuong-2-nguoi-chong-biet-muon-2/ 
- Chương 1: Sáu Trăm Triệu Tiền Ở Nhờ (1894 từ): https://doctieuthuyet.com/chuong/chuong-1-sau-tram-trieu-tien-o-nho-2/ 
- Chương 5: Cái Bàn Không Còn Thuộc Về Họ (1543 từ): https://doctieuthuyet.com/chuong/chuong-5-cai-ban-khong-con-thuoc-ve-ho/ 
- Chương 4: File Cuối Cùng (1163 từ): https://doctieuthuyet.com/chuong/chuong-4-file-cuoi-cung/ 
- Chương 2: Người Chồng Biết Muộn (997 từ): https://doctieuthuyet.com/chuong/chuong-2-nguoi-chong-biet-muon/ 
- Chương 3: Căn Nhà Đổi Lấy Sự Yên Ổn (1150 từ): https://doctieuthuyet.com/chuong/chuong-3-can-nha-doi-lay-su-yen-on/ 
- Chương 1: Sáu Trăm Triệu Tiền Ở Nhờ (1894 từ): https://doctieuthuyet.com/chuong/chuong-1-sau-tram-trieu-tien-o-nho/ 
- Chương 15: Người Lau Sàn Và Căn Phòng Sáng Đèn (1726 từ): https://doctieuthuyet.com/chuong/chuong-15-nguoi-lau-san-va-can-phong-sang-den/ 
- Chương 14: Ngày Mười Lăm, Chủ Tịch Không Còn Cửa Kính Để Đứng Sau (1538 từ): https://doctieuthuyet.com/chuong/chuong-14-ngay-muoi-lam-chu-tich-khong-con-cua-kinh-de-dung-sau/ 
- Chương 13: Người Đếm Tiền Cuối Cùng Quay Lưng (1165 từ): https://doctieuthuyet.com/chuong/chuong-13-nguoi-dem-tien-cuoi-cung-quay-lung/ 
- Chương 12: Cái Va Li Đầy Tiền Giả Sự Thật (1277 từ): https://doctieuthuyet.com/chuong/chuong-12-cai-va-li-day-tien-gia-su-that/ 
- Chương 11: Ba Mươi Phút Trước Khi Người Ta Ra Tay (974 từ): https://doctieuthuyet.com/chuong/chuong-11-ba-muoi-phut-truoc-khi-nguoi-ta-ra-tay/ 
- Chương 10: Tấm Thẻ Ngành Trước Ống Kính (1236 từ): https://doctieuthuyet.com/chuong/chuong-10-tam-the-nganh-truoc-ong-kinh/ 
- Chương 9: Đình Chỉ Một Người Đang Đeo Mặt Nạ (1205 từ): https://doctieuthuyet.com/chuong/chuong-9-dinh-chi-mot-nguoi-dang-deo-mat-na/ 
- Chương 8: Tờ Giấy Trong Thang Máy (1094 từ): https://doctieuthuyet.com/chuong/chuong-8-to-giay-trong-thang-may/ 
- Chương 7: Chủ Tịch Đã Biết Tên Thật (1108 từ): https://doctieuthuyet.com/chuong/chuong-7-chu-tich-da-biet-ten-that/ 
- Chương 5: Năm Trăm Triệu Để Mua Một Cái Mồm Im (1204 từ): https://doctieuthuyet.com/chuong/chuong-5-nam-tram-trieu-de-mua-mot-cai-mom-im/ 
- Chương 6: Chiếc Điện Thoại Trong Cặp Xách (1395 từ): https://doctieuthuyet.com/chuong/chuong-6-chiec-dien-thoai-trong-cap-xach/ 
- Chương 4: Năm Mươi Triệu Đặt Trên Nắp Capo (1132 từ): https://doctieuthuyet.com/chuong/chuong-4-nam-muoi-trieu-dat-tren-nap-capo/ 
- Chương 2: Cuốn Sổ Hai Mặt Trong Căn Bếp Quận 2 (1620 từ): https://doctieuthuyet.com/chuong/chuong-2-cuon-so-hai-mat-trong-can-bep-quan-2/ 
- Chương 3: Sao Kê Không Biết Nói Dối (1166 từ): https://doctieuthuyet.com/chuong/chuong-3-sao-ke-khong-biet-noi-doi/ 
- Chương 1: Ly Cà Phê Và Cái Quỳ Gối Đầu Tiên (1691 từ): https://doctieuthuyet.com/chuong/chuong-1-ly-ca-phe-va-cai-quy-goi-dau-tien/ 
- Chương 12: Sau Chiếc Mặt Nạ (756 từ): https://doctieuthuyet.com/chuong/chuong-12-sau-chiec-mat-na/ 
- Chương 10: Phòng Họp Tầng Hai Mươi (785 từ): https://doctieuthuyet.com/chuong/chuong-10-phong-hop-tang-hai-muoi/ 
- Chương 11: Ly Cà Phê Đậm Nhất (1268 từ): https://doctieuthuyet.com/chuong/chuong-11-ly-ca-phe-dam-nhat/ 
- Chương 9: Bữa Tiệc Trước Ngày Sập (446 từ): https://doctieuthuyet.com/chuong/chuong-9-bua-tiec-truoc-ngay-sap/ ==> ngắn (446 từ)
- Chương 7: Cái Bẫy Dành Cho Kế Toán Trưởng (586 từ): https://doctieuthuyet.com/chuong/chuong-7-cai-bay-danh-cho-ke-toan-truong/ ==> ngắn (586 từ)
- Chương 8: Hai Tỷ Và Một Cái Tát Không Đau (1133 từ): https://doctieuthuyet.com/chuong/chuong-8-hai-ty-va-mot-cai-tat-khong-dau/ 
- Chương 6: Bắt Con Cáo Ký Vào Bẫy (707 từ): https://doctieuthuyet.com/chuong/chuong-6-bat-con-cao-ky-vao-bay/ 
- Chương 5: Người Ngồi Ghế Trước (629 từ): https://doctieuthuyet.com/chuong/chuong-5-nguoi-ngoi-ghe-truoc/ ==> ngắn (629 từ)
- Chương 4: Bị Đuổi Khỏi Cửa Trước (572 từ): https://doctieuthuyet.com/chuong/chuong-4-bi-duoi-khoi-cua-truoc/ ==> ngắn (572 từ)
- Chương 2: Người Đàn Bà Giữ Sổ (712 từ): https://doctieuthuyet.com/chuong/chuong-2-nguoi-dan-ba-giu-so/ 
- Chương 3: Ba Lần Cúi Đầu (573 từ): https://doctieuthuyet.com/chuong/chuong-3-ba-lan-cui-dau/ ==> ngắn (573 từ)
- Chương 1: Ly Cà Phê Đầu Tiên (1088 từ): https://doctieuthuyet.com/chuong/chuong-1-ly-ca-phe-dau-tien/ 
- Chương 1 (0 từ): https://doctieuthuyet.com/chuong/chuong-1-2/ ==> ngắn (0 từ)
- Chương 13: (1169 từ): https://doctieuthuyet.com/chuong/chuong-13/ 
- Chương 12: (1117 từ): https://doctieuthuyet.com/chuong/chuong-12/ 
- Chương 11: (1110 từ): https://doctieuthuyet.com/chuong/chuong-11/ 
- Chương 10: (1480 từ): https://doctieuthuyet.com/chuong/chuong-10-2/ 
- Chương 9: (841 từ): https://doctieuthuyet.com/chuong/chuong-9-2/ 
- Chương 8: (993 từ): https://doctieuthuyet.com/chuong/chuong-8-2/ 
- Chương 7: (752 từ): https://doctieuthuyet.com/chuong/chuong-7-2/ 
- Chương 5: (908 từ): https://doctieuthuyet.com/chuong/chuong-5-2/ 
- Chương 6: (1354 từ): https://doctieuthuyet.com/chuong/chuong-6-2/ 
- Chương 4: (1091 từ): https://doctieuthuyet.com/chuong/chuong-4-2/ 
- Chương 3: (978 từ): https://doctieuthuyet.com/chuong/chuong-3-2/ 
- Chương 2: (1269 từ): https://doctieuthuyet.com/chuong/chuong-2-2/ 
- Chương 1: Con mèo trên trang nhất (1072 từ): https://doctieuthuyet.com/chuong/chuong-1/ ==> body có thể lặp lại tiêu đề chương
- Chương 9: (1441 từ): https://doctieuthuyet.com/chuong/chuong-9/ 
- Chương 10: (1977 từ): https://doctieuthuyet.com/chuong/chuong-10/ 
- Chương 8: (899 từ): https://doctieuthuyet.com/chuong/chuong-8/ 
- Chương 7: (900 từ): https://doctieuthuyet.com/chuong/chuong-7/ 
- Chương 6: (903 từ): https://doctieuthuyet.com/chuong/chuong-6/ 
- Chương 5: (1014 từ): https://doctieuthuyet.com/chuong/chuong-5/ 
- Chương 4: (913 từ): https://doctieuthuyet.com/chuong/chuong-4/ 
- Chương 3: (944 từ): https://doctieuthuyet.com/chuong/chuong-3/ 
- Chương 2: (1121 từ): https://doctieuthuyet.com/chuong/chuong-2/ 
- Chương 1: Người phụ nữ vô dụng (1491 từ): https://doctieuthuyet.com/chuong/chuong-1-nguoi-phu-nu-vo-dung/ 
- Chương 12: Cuộc sống mới (1023 từ): https://doctieuthuyet.com/chuong/chuong-12-cuoc-song-moi/ 
- Chương 11: Kết thúc ở đồn cảnh sát (1031 từ): https://doctieuthuyet.com/chuong/chuong-11-ket-thuc-o-don-canh-sat/ 
- Chương 10: Cuộc đột kích đêm khuya (1213 từ): https://doctieuthuyet.com/chuong/chuong-10-cuoc-dot-kich-dem-khuya/ 
- Chương 9: Bản năng mẹ và con mèo (1017 từ): https://doctieuthuyet.com/chuong/chuong-9-ban-nang-me-va-con-meo/ 
- Chương 8: Kẻ phản bội trong đội (1014 từ): https://doctieuthuyet.com/chuong/chuong-8-ke-phan-boi-trong-doi/ 
- Chương 5: Vết thương và con tin (1045 từ): https://doctieuthuyet.com/chuong/chuong-5-vet-thuong-va-con-tin/ 
- Chương 7: Cuộc gọi trong nhà vệ sinh (1002 từ): https://doctieuthuyet.com/chuong/chuong-7-cuoc-goi-trong-nha-ve-sinh/ 
- Chương 6: Thỏa thuận bất khả thi (1141 từ): https://doctieuthuyet.com/chuong/chuong-6-thoa-thuan-bat-kha-thi/ 
- Chương 3: Chiếc vòng cổ cho mèo (1135 từ): https://doctieuthuyet.com/chuong/chuong-3-chiec-vong-co-cho-meo/ 
- Chương 4: Sập bẫy từ bên trong (1399 từ): https://doctieuthuyet.com/chuong/chuong-4-sap-bay-tu-ben-trong/ 
- Chương 2: Bệnh viện và bí mật (893 từ): https://doctieuthuyet.com/chuong/chuong-2-benh-vien-va-bi-mat/ 
- Chương 1: Áo mưa trong đêm (730 từ): https://doctieuthuyet.com/chuong/chuong-1-ao-mua-trong-dem/ 
- Chương 8: Đóng Đinh Án Tử (1008 từ): https://doctieuthuyet.com/chuong/chuong-8-dong-dinh-an-tu/ 
- Chương 6: Tát Lật Mặt Trước Linh Đường (830 từ): https://doctieuthuyet.com/chuong/chuong-6-tat-lat-mat-truoc-linh-duong/ 
- Chương 7: Phơi Bày Hợp Đồng Giết Người (1243 từ): https://doctieuthuyet.com/chuong/chuong-7-phoi-bay-hop-dong-giet-nguoi/ 
- Chương 5: Nghiền Nát Lời Thề (980 từ): https://doctieuthuyet.com/chuong/chuong-5-nghien-nat-loi-the/ 
- Chương 3: Đuổi Cổ Giữa Đêm (831 từ): https://doctieuthuyet.com/chuong/chuong-3-duoi-co-giua-dem/ 
- Chương 4: Bóc Trần Hóa Đơn (1119 từ): https://doctieuthuyet.com/chuong/chuong-4-boc-tran-hoa-don/ 
- Chương 1: Giẫm Đạp Tự Tôn (580 từ): https://doctieuthuyet.com/chuong/chuong-1-giam-dap-tu-ton-5/ ==> ngắn (580 từ)
- Chương 2: Tước Đoạt Không Tiếng (828 từ): https://doctieuthuyet.com/chuong/chuong-2-tuoc-doat-khong-tieng/ 
- Chương 8: Tiêu Diệt Danh Dự (1332 từ): https://doctieuthuyet.com/chuong/chuong-8-tieu-diet-danh-du/ 
- Chương 7: Nghiền Nát Đính Hôn (1656 từ): https://doctieuthuyet.com/chuong/chuong-7-nghien-nat-dinh-hon/ 
- Chương 6: Đuổi Cổ Luật Sư Gia Đình (1259 từ): https://doctieuthuyet.com/chuong/chuong-6-duoi-co-luat-su-gia-dinh/ 
- Chương 5: Lật Đổ Hồ Sơ Bịt Miệng (1029 từ): https://doctieuthuyet.com/chuong/chuong-5-lat-do-ho-so-bit-mieng/ 
- Chương 4: Đào Bới Di Chúc Giả (1441 từ): https://doctieuthuyet.com/chuong/chuong-4-dao-boi-di-chuc-gia/ 
- Chương 3: Tước Đoạt Thẻ Quyền (1203 từ): https://doctieuthuyet.com/chuong/chuong-3-tuoc-doat-the-quyen/ 
- Chương 2: Xé Nát Hình Ảnh (1255 từ): https://doctieuthuyet.com/chuong/chuong-2-xe-nat-hinh-anh/ 
- Chương 9: BẮT TAY LINH TRÊN BẬC CẦU THANG TÒA ÁN (887 từ): https://doctieuthuyet.com/chuong/chuong-9-bat-tay-linh-tren-bac-cau-thang-toa-an/ 
- Chương 8: GIẢI MÃ TÀI KHOẢN EMAIL CỦA NGƯỜI THỨ BA (1116 từ): https://doctieuthuyet.com/chuong/chuong-8-giai-ma-tai-khoan-email-cua-nguoi-thu-ba/ 
- Chương 7: LỘ DIỆN CAMERA TRONG PHÒNG KHÁM (893 từ): https://doctieuthuyet.com/chuong/chuong-7-lo-dien-camera-trong-phong-kham/ 
- Chương 6: THỬ NGHIỆM MÁU TRÊN TAY LINH (1258 từ): https://doctieuthuyet.com/chuong/chuong-6-thu-nghiem-mau-tren-tay-linh/ 
- Chương 5: ĐỌC LẠI NHẬT KÝ CỦA KẺ SÁT NHÂN (1310 từ): https://doctieuthuyet.com/chuong/chuong-5-doc-lai-nhat-ky-cua-ke-sat-nhan/ 
- Chương 4: PHÁ KHÓA NHẬT KÝ GIẤU TRONG Ổ CỨNG (1032 từ): https://doctieuthuyet.com/chuong/chuong-4-pha-khoa-nhat-ky-giau-trong-o-cung/ 
- Chương 3: TẠM GIỮ TÔI TRONG PHÒNG CÔNG AN (950 từ): https://doctieuthuyet.com/chuong/chuong-3-tam-giu-toi-trong-phong-cong-an/ 
- Chương 2: ĐÀO MỘ TÔI THÀNH XÁC SỐNG (901 từ): https://doctieuthuyet.com/chuong/chuong-2-dao-mo-toi-thanh-xac-song/ 
- Chương 1: ĐĂNG STORY GIẾT NGƯỜI (1096 từ): https://doctieuthuyet.com/chuong/chuong-1-dang-story-giet-nguoi/ 
- Chương 4: Bản sao cuối cùng (1420 từ): https://doctieuthuyet.com/chuong/chuong-4-ban-sao-cuoi-cung/ 
- Chương 5: Đứa trẻ trong gương (1781 từ): https://doctieuthuyet.com/chuong/chuong-5-dua-tre-trong-guong/ 
- Chương 2: Băng ghi hình bị mất (1633 từ): https://doctieuthuyet.com/chuong/chuong-2-bang-ghi-hinh-bi-mat/ 
- Chương 3: Ký ức vỡ vụn (2616 từ): https://doctieuthuyet.com/chuong/chuong-3-ky-uc-vo-vun/ 
- Chương 1: Nhân chứng cuối cùng (1192 từ): https://doctieuthuyet.com/chuong/chuong-1-nhan-chung-cuoi-cung/ 
- Chương 11: Khuyết điểm lộ diện (1685 từ): https://doctieuthuyet.com/chuong/chuong-11-khuyet-diem-lo-dien/ 
- Chương 12: Quyết định trốn thoát (1835 từ): https://doctieuthuyet.com/chuong/chuong-12-quyet-dinh-tron-thoat/ 
- Chương 10: Gặp mặt định mệnh (1317 từ): https://doctieuthuyet.com/chuong/chuong-10-gap-mat-dinh-menh/ 
- Chương 9: Chuẩn bị cho màn trình diễn (1446 từ): https://doctieuthuyet.com/chuong/chuong-9-chuan-bi-cho-man-trinh-dien/ 
- Chương 8: Bằng chứng bị hủy (1249 từ): https://doctieuthuyet.com/chuong/chuong-8-bang-chung-bi-huy/ 
- Chương 7: Cái bẫy trong bóng tối (1089 từ): https://doctieuthuyet.com/chuong/chuong-7-cai-bay-trong-bong-toi/ 
- Chương 6: Đồng minh bất ngờ (1376 từ): https://doctieuthuyet.com/chuong/chuong-6-dong-minh-bat-ngo/ 
- Chương 5: Bài kiểm tra chết người (1204 từ): https://doctieuthuyet.com/chuong/chuong-5-bai-kiem-tra-chet-nguoi/ 
- Chương 4: Bản sao số 2 (1641 từ): https://doctieuthuyet.com/chuong/chuong-4-ban-sao-so-2/ 
- Chương 3: Lần đầu đối mặt (1137 từ): https://doctieuthuyet.com/chuong/chuong-3-lan-dau-doi-mat/ 
- Chương 2: Quy tắc tử thần (950 từ): https://doctieuthuyet.com/chuong/chuong-2-quy-tac-tu-than/ 
- Chương 1: Nhật ký đẫm máu (1345 từ): https://doctieuthuyet.com/chuong/chuong-1-nhat-ky-dam-mau/ 
- Chương 15: Hậu quả và mở đầu mới (1190 từ): https://doctieuthuyet.com/chuong/chuong-15-hau-qua-va-mo-dau-moi/ 
- Chương 14: Lật bài và kết cục (1488 từ): https://doctieuthuyet.com/chuong/chuong-14-lat-bai-va-ket-cuc/ 
- Chương 12: Đối mặt và thương lượng (1901 từ): https://doctieuthuyet.com/chuong/chuong-12-doi-mat-va-thuong-luong/ 
- Chương 13: Hợp đồng dàn xếp và cái bẫy cuối cùng (2065 từ): https://doctieuthuyet.com/chuong/chuong-13-hop-dong-dan-xep-va-cai-bay-cuoi-cung/ 
- Chương 11: Đột nhập và phát hiện chấn động (1809 từ): https://doctieuthuyet.com/chuong/chuong-11-dot-nhap-va-phat-hien-chan-dong/ 
- Chương 10: Bước vào đường cùng và quyết định liề… (2295 từ): https://doctieuthuyet.com/chuong/chuong-10-buoc-vao-duong-cung-va-quyet-dinh-lie/ 
- Chương 9: Phỏng vấn và cú đánh ngược bất ngờ (1755 từ): https://doctieuthuyet.com/chuong/chuong-9-phong-van-va-cu-danh-nguoc-bat-ngo/ 
- Chương 8: Đồng minh bất ngờ và kế hoạch cuối (1890 từ): https://doctieuthuyet.com/chuong/chuong-8-dong-minh-bat-ngo-va-ke-hoach-cuoi/ 
- Chương 7: Hồ sơ bảo hiểm và cái bẫy pháp lý (1801 từ): https://doctieuthuyet.com/chuong/chuong-7-ho-so-bao-hiem-va-cai-bay-phap-ly/ 
- Chương 6: Luật sư già và manh mối mới (1128 từ): https://doctieuthuyet.com/chuong/chuong-6-luat-su-gia-va-manh-moi-moi/ 
- Chương 5: Mất trắng và điểm tựa cuối cùng (1120 từ): https://doctieuthuyet.com/chuong/chuong-5-mat-trang-va-diem-tua-cuoi-cung/ 
- Chương 4: Đối chất thất bại và bẫy ngược (1526 từ): https://doctieuthuyet.com/chuong/chuong-4-doi-chat-that-bai-va-bay-nguoc/ 
- Chương 3: Bằng chứng đầu tiên và sự phản bội (1775 từ): https://doctieuthuyet.com/chuong/chuong-3-bang-chung-dau-tien-va-su-phan-boi/ 
- Chương 1: Đám cưới hoành tráng và cú sốc tột cùng (1251 từ): https://doctieuthuyet.com/chuong/chuong-1-dam-cuoi-hoanh-trang-va-cu-soc-tot-cung/ 
- Chương 2: Sự thật đầu tiên và kế hoạch điều tra (1840 từ): https://doctieuthuyet.com/chuong/chuong-2-su-that-dau-tien-va-ke-hoach-dieu-tra/ 
- Chương 17: Mở đầu mới (1353 từ): https://doctieuthuyet.com/chuong/chuong-17-mo-dau-moi/ 
- Chương 16: Giá phải trả (1589 từ): https://doctieuthuyet.com/chuong/chuong-16-gia-phai-tra/ 
- Chương 15: Kết cục không ngờ (1163 từ): https://doctieuthuyet.com/chuong/chuong-15-ket-cuc-khong-ngo/ 
- Chương 14: Phản công dữ dội (1717 từ): https://doctieuthuyet.com/chuong/chuong-14-phan-cong-du-doi/ 
- Chương 13: Lật ngược tình thế (1701 từ): https://doctieuthuyet.com/chuong/chuong-13-lat-nguoc-tinh-the/ 
- Chương 12: Liên minh bất đắc dĩ (2361 từ): https://doctieuthuyet.com/chuong/chuong-12-lien-minh-bat-dac-di/ 
- Chương 11: Bằng chứng thứ hai bị hủy (1045 từ): https://doctieuthuyet.com/chuong/chuong-11-bang-chung-thu-hai-bi-huy/ 
- Chương 10: Đối đầu trực diện (1149 từ): https://doctieuthuyet.com/chuong/chuong-10-doi-dau-truc-dien/ 
- Chương 8: Lựa chọn đau đớn (1104 từ): https://doctieuthuyet.com/chuong/chuong-8-lua-chon-dau-don/ 
- Chương 9: Manh mối bất ngờ (1674 từ): https://doctieuthuyet.com/chuong/chuong-9-manh-moi-bat-ngo/ 
- Chương 7: Bị dồn vào chân tường (1298 từ): https://doctieuthuyet.com/chuong/chuong-7-bi-don-vao-chan-tuong/ 
- Chương 6: Đồng minh phản bội (1726 từ): https://doctieuthuyet.com/chuong/chuong-6-dong-minh-phan-boi/ 
- Chương 5: Bẫy tình cảm (1454 từ): https://doctieuthuyet.com/chuong/chuong-5-bay-tinh-cam/ 
- Chương 2: Cuộc đối chất đầu tiên (1085 từ): https://doctieuthuyet.com/chuong/chuong-2-cuoc-doi-chat-dau-tien/ 
- Chương 4: Âm mưu lộ diện (1279 từ): https://doctieuthuyet.com/chuong/chuong-4-am-muu-lo-dien/ 
- Chương 3: Hậu quả tức thì (1260 từ): https://doctieuthuyet.com/chuong/chuong-3-hau-qua-tuc-thi/ 
- Chương 1: Bức ảnh định mệnh (1011 từ): https://doctieuthuyet.com/chuong/chuong-1-buc-anh-dinh-menh/ 
- Chương 12: Sự Thật Cuối Cùng Và Cái Giá Phải Trả (1403 từ): https://doctieuthuyet.com/chuong/chuong-12-su-that-cuoi-cung-va-cai-gia-phai-tra/ 
- Chương 11: Lật Ngược Ván Cờ (1109 từ): https://doctieuthuyet.com/chuong/chuong-11-lat-nguoc-van-co/ 
- Chương 10: Đối Chất Tại Tông Từ – Phần Mở Đầu (2396 từ): https://doctieuthuyet.com/chuong/chuong-10-doi-chat-tai-tong-tu-phan-mo-dau/ 
- Chương 7: Mảnh Ghép Bị Thiếu Trong Ký Ức (983 từ): https://doctieuthuyet.com/chuong/chuong-7-manh-ghep-bi-thieu-trong-ky-uc/ 
- Chương 8: Kho Báu Thật Sự (1685 từ): https://doctieuthuyet.com/chuong/chuong-8-kho-bau-that-su/ 
- Chương 9: Chuẩn Bị Cho Trận Chiến Cuối (2301 từ): https://doctieuthuyet.com/chuong/chuong-9-chuan-bi-cho-tran-chien-cuoi/ 
- Chương 6: Vượt Ngục Và Sự Phản Bội (1368 từ): https://doctieuthuyet.com/chuong/chuong-6-vuot-nguc-va-su-phan-boi/ 
- Chương 5: Trong Ngục Tối Và Người Bạn Bất Ngờ (1895 từ): https://doctieuthuyet.com/chuong/chuong-5-trong-nguc-toi-va-nguoi-ban-bat-ngo/ 
- Chương 3: Vả Mặt Trong Đại Điển – Phần Một (1463 từ): https://doctieuthuyet.com/chuong/chuong-3-va-mat-trong-dai-dien-phan-mot/ 
- Chương 4: Phản Đòn Tàn Khốc (1443 từ): https://doctieuthuyet.com/chuong/chuong-4-phan-don-tan-khoc/ 
- Chương 1: Tỉnh Lại Ở Thời Điểm Định Mệnh (1452 từ): https://doctieuthuyet.com/chuong/chuong-1-tinh-lai-o-thoi-diem-dinh-menh/ 
- Chương 2: Cuộc Gặp Bất Ngờ Và Lời Cảnh Báo (2312 từ): https://doctieuthuyet.com/chuong/chuong-2-cuoc-gap-bat-ngo-va-loi-canh-bao/ 
- Chương 15: Cuộc Sống Mới (1210 từ): https://doctieuthuyet.com/chuong/chuong-15-cuoc-song-moi/ 
- Chương 16: Bãi Rác Biến Mất (1374 từ): https://doctieuthuyet.com/chuong/chuong-16-bai-rac-bien-mat/ 
- Chương 14: Lời Thú Tội (999 từ): https://doctieuthuyet.com/chuong/chuong-14-loi-thu-toi/ 
- Chương 12: Án Phạt Độc Đáo (1055 từ): https://doctieuthuyet.com/chuong/chuong-12-an-phat-doc-dao/ 
- Chương 13: Sự Sụp Đổ (1237 từ): https://doctieuthuyet.com/chuong/chuong-13-su-sup-do/ 
- Chương 10: Lật Lại Thế Cờ (1609 từ): https://doctieuthuyet.com/chuong/chuong-10-lat-lai-the-co/ 
- Chương 11: Phiên Tòa Thứ Hai (1658 từ): https://doctieuthuyet.com/chuong/chuong-11-phien-toa-thu-hai/ 
- Chương 9: Đòn Phủ Đầu (1588 từ): https://doctieuthuyet.com/chuong/chuong-9-don-phu-dau/ 
- Chương 7: Bằng Chứng Quý Giá (1087 từ): https://doctieuthuyet.com/chuong/chuong-7-bang-chung-quy-gia/ 
- Chương 8: Bị Phản Bội (1424 từ): https://doctieuthuyet.com/chuong/chuong-8-bi-phan-boi/ 
- Chương 5: Hậu Quả Bất Ngờ (1168 từ): https://doctieuthuyet.com/chuong/chuong-5-hau-qua-bat-ngo/ 
- Chương 6: Kế Hoạch Ẩn Mình (1452 từ): https://doctieuthuyet.com/chuong/chuong-6-ke-hoach-an-minh/ 
- Chương 4: Cú Lật Bài Ở Tòa (1444 từ): https://doctieuthuyet.com/chuong/chuong-4-cu-lat-bai-o-toa/ 
- Chương 3: Đơn Kiện Đầu Tiên (1311 từ): https://doctieuthuyet.com/chuong/chuong-3-don-kien-dau-tien/ 
- Chương 2: Lời Đe Dọa (1438 từ): https://doctieuthuyet.com/chuong/chuong-2-loi-de-doa/ 
- Chương 1: Bức Tường Lấn Chiếm (775 từ): https://doctieuthuyet.com/chuong/chuong-1-buc-tuong-lan-chiem/ 
- Chương 14: Chia Đôi Xương Máu (897 từ): https://doctieuthuyet.com/chuong/chuong-14-chia-doi-xuong-mau/ 
- Chương 13: Xé Nát Bản Án (1820 từ): https://doctieuthuyet.com/chuong/chuong-13-xe-nat-ban-an/ 
- Chương 12: Tát Lật Mặt Mẹ Chồng (1806 từ): https://doctieuthuyet.com/chuong/chuong-12-tat-lat-mat-me-chong/ 
- Chương 11: Phá Tan Gia Phả (1282 từ): https://doctieuthuyet.com/chuong/chuong-11-pha-tan-gia-pha/ 
- Chương 10: Giết Chết Tin Đồn (1541 từ): https://doctieuthuyet.com/chuong/chuong-10-giet-chet-tin-don/ 
- Chương 9: Đánh Sập Tổ Quạ (1329 từ): https://doctieuthuyet.com/chuong/chuong-9-danh-sap-to-qua/ ==> body có thể lặp lại tiêu đề chương
- Chương 8: Lật Mặt Tiền Mặt (1927 từ): https://doctieuthuyet.com/chuong/chuong-8-lat-mat-tien-mat/ 
- Chương 7: Cắt Đứt Dây Nhợ (1952 từ): https://doctieuthuyet.com/chuong/chuong-7-cat-dut-day-nho/ 
- Chương 5: Xé Nát Hợp Đồng (1771 từ): https://doctieuthuyet.com/chuong/chuong-5-xe-nat-hop-dong/ 
- Chương 6: Đóng Đinh Bằng Chứng (1757 từ): https://doctieuthuyet.com/chuong/chuong-6-dong-dinh-bang-chung/ 
- Chương 4: Nghiền Nát Lời Thề (949 từ): https://doctieuthuyet.com/chuong/chuong-4-nghien-nat-loi-the/ 
- Chương 3: Tước Đoạt Danh Dự (993 từ): https://doctieuthuyet.com/chuong/chuong-3-tuoc-doat-danh-du-2/ 
- Chương 2: Giẫm Đạp Tự Tôn (1143 từ): https://doctieuthuyet.com/chuong/chuong-2-giam-dap-tu-ton-2/ 
- Chương 1: Đuổi Cổ Ra Đường (605 từ): https://doctieuthuyet.com/chuong/chuong-1-duoi-co-ra-duong/ ==> ngắn (605 từ)
- Chương 15: TỐNG GIAM TƯỚC THỜI HẠN (1192 từ): https://doctieuthuyet.com/chuong/chuong-15-tong-giam-tuoc-thoi-han/ 
- Chương 14: XÉ NÁT BẢN ÁN GIẢ (1231 từ): https://doctieuthuyet.com/chuong/chuong-14-xe-nat-ban-an-gia/ 
- Chương 13: TIÊU DIỆT CÔNG TY ĐỐI THỦ (1449 từ): https://doctieuthuyet.com/chuong/chuong-13-tieu-diet-cong-ty-doi-thu/ 
- Chương 12: CHÂM THỦY VÀO MẮT (1709 từ): https://doctieuthuyet.com/chuong/chuong-12-cham-thuy-vao-mat/ 
- Chương 11: ĐÀO MỘ TOÀN BỘ BAN LÃNH ĐẠO (1708 từ): https://doctieuthuyet.com/chuong/chuong-11-dao-mo-toan-bo-ban-lanh-dao/ 
- Chương 9: THÁO KHÓA KÉT ĐEN (1166 từ): https://doctieuthuyet.com/chuong/chuong-9-thao-khoa-ket-den/ 
- Chương 10: ĐỤNG ĐỘ TẠI PHI TRƯỜNG (1443 từ): https://doctieuthuyet.com/chuong/chuong-10-dung-do-tai-phi-truong/ 
- Chương 8: LỘT VỎ CHỨNG KHOÁN (1607 từ): https://doctieuthuyet.com/chuong/chuong-8-lot-vo-chung-khoan/ 
- Chương 6: PHÁ BỎ HỢP ĐỒNG LIÊN MINH (1162 từ): https://doctieuthuyet.com/chuong/chuong-6-pha-bo-hop-dong-lien-minh/ 
- Chương 7: TẨU THOÁT TRONG ĐÊM (1751 từ): https://doctieuthuyet.com/chuong/chuong-7-tau-thoat-trong-dem/ 
- Chương 5: ĐÁNH SẬP PHÒNG HỌP (1633 từ): https://doctieuthuyet.com/chuong/chuong-5-danh-sap-phong-hop/ 
- Chương 4: ĐỤNG ĐẦU TRONG THANG MÁY (1040 từ): https://doctieuthuyet.com/chuong/chuong-4-dung-dau-trong-thang-may/ 
- Chương 3: THẢO TÚNG BẢNG LƯƠNG (1017 từ): https://doctieuthuyet.com/chuong/chuong-3-thao-tung-bang-luong/ 
- Chương 2: GIẬT PHẲNG GIẤY ĐỀ BẠT (1389 từ): https://doctieuthuyet.com/chuong/chuong-2-giat-phang-giay-de-bat/ 
- Chương 1: ĐÁNH RƠI BÌA THẺ (1219 từ): https://doctieuthuyet.com/chuong/chuong-1-danh-roi-bia-the/ 
- Chương 14: Giải Phóng Quê Hương (928 từ): https://doctieuthuyet.com/chuong/chuong-14-giai-phong-que-huong/ 
- Chương 13: Tước Đoạt Quyền Lực (1307 từ): https://doctieuthuyet.com/chuong/chuong-13-tuoc-doat-quyen-luc/ 
- Chương 12: Nghiền Nát Đế Chế (1194 từ): https://doctieuthuyet.com/chuong/chuong-12-nghien-nat-de-che/ 
- Chương 11: Bẻ Gãy Phản Kích (1038 từ): https://doctieuthuyet.com/chuong/chuong-11-be-gay-phan-kich/ 
- Chương 9: Kích Hoạt Nỗi Sợ (880 từ): https://doctieuthuyet.com/chuong/chuong-9-kich-hoat-noi-so/ 
- Chương 10: Xé Toạc Màn Kịch (1224 từ): https://doctieuthuyet.com/chuong/chuong-10-xe-toac-man-kich/ 
- Chương 8: Đánh Sập Trụ Sở (943 từ): https://doctieuthuyet.com/chuong/chuong-8-danh-sap-tru-so/ 
- Chương 7: Vượt Ngục Sinh Tử (1291 từ): https://doctieuthuyet.com/chuong/chuong-7-vuot-nguc-sinh-tu/ 
- Chương 6: Xé Nát Giấc Mơ (976 từ): https://doctieuthuyet.com/chuong/chuong-6-xe-nat-giac-mo/ 
- Chương 5: Hãm Hại Kho Báu (1399 từ): https://doctieuthuyet.com/chuong/chuong-5-ham-hai-kho-bau/ 
- Chương 4: Đánh Đổ Uy Quyền (1475 từ): https://doctieuthuyet.com/chuong/chuong-4-danh-do-uy-quyen/ 
- Chương 3: Bóc Trần Gian Kế (1319 từ): https://doctieuthuyet.com/chuong/chuong-3-boc-tran-gian-ke/ 
- Chương 1: Phá Vỡ Màn Sương (934 từ): https://doctieuthuyet.com/chuong/chuong-1-pha-vo-man-suong/ 
- Chương 2: Xuyên Thủng Niềm Tin (1187 từ): https://doctieuthuyet.com/chuong/chuong-2-xuyen-thung-niem-tin/ 
- Chương 15: Chôn Vùi Quá Khứ (476 từ): https://doctieuthuyet.com/chuong/chuong-15-chon-vui-qua-khu/ ==> ngắn (476 từ)
- Chương 14: Tát Lật Mặt Đời (607 từ): https://doctieuthuyet.com/chuong/chuong-14-tat-lat-mat-doi/ ==> ngắn (607 từ)
- Chương 13: Nghiền Nát Gia Tộc (566 từ): https://doctieuthuyet.com/chuong/chuong-13-nghien-nat-gia-toc/ ==> ngắn (566 từ)
- Chương 12: Giết Chết Bóng Ma (616 từ): https://doctieuthuyet.com/chuong/chuong-12-giet-chet-bong-ma/ ==> ngắn (616 từ)
- Chương 11: Phá Vỡ Liên Minh (580 từ): https://doctieuthuyet.com/chuong/chuong-11-pha-vo-lien-minh/ ==> ngắn (580 từ)
- Chương 10: Bắt Cổ Tay Lừa Đảo (524 từ): https://doctieuthuyet.com/chuong/chuong-10-bat-co-tay-lua-dao/ ==> ngắn (524 từ)
- Chương 9: Đóng Đinh Âm Mưu (652 từ): https://doctieuthuyet.com/chuong/chuong-9-dong-dinh-am-muu/ ==> ngắn (652 từ)
- Chương 8: Tước Đoạt Quyền Kiểm Soát (606 từ): https://doctieuthuyet.com/chuong/chuong-8-tuoc-doat-quyen-kiem-soat/ ==> ngắn (606 từ)
- Chương 7: Lật Đổ Chứng Từ (445 từ): https://doctieuthuyet.com/chuong/chuong-7-lat-do-chung-tu/ ==> ngắn (445 từ)
- Chương 6: Phá Tan Bức Màn (455 từ): https://doctieuthuyet.com/chuong/chuong-6-pha-tan-buc-man/ ==> ngắn (455 từ)
- Chương 5: Xé Nát Thư Tín (377 từ): https://doctieuthuyet.com/chuong/chuong-5-xe-nat-thu-tin/ ==> ngắn (377 từ)
- Chương 4: Bẻ Gãy Niềm Tin (478 từ): https://doctieuthuyet.com/chuong/chuong-4-be-gay-niem-tin/ ==> ngắn (478 từ)
- Chương 3: Tước Đoạt Danh Dự (502 từ): https://doctieuthuyet.com/chuong/chuong-3-tuoc-doat-danh-du/ ==> ngắn (502 từ)
- Chương 2: Giẫm Đạp Tự Tôn (483 từ): https://doctieuthuyet.com/chuong/chuong-2-giam-dap-tu-ton/ ==> ngắn (483 từ)
- Chương 1: Đuổi Cổ Ra Cổng (474 từ): https://doctieuthuyet.com/chuong/chuong-1-duoi-co-ra-cong/ ==> ngắn (474 từ)
- Chương 15: Đốt Cháy Di Sản Giả (1029 từ): https://doctieuthuyet.com/chuong/chuong-15-dot-chay-di-san-gia/ 
- Chương 14: Công Bố Máu Cha (825 từ): https://doctieuthuyet.com/chuong/chuong-14-cong-bo-mau-cha/ 
- Chương 13: Đóng Đinh Sự Thật (958 từ): https://doctieuthuyet.com/chuong/chuong-13-dong-dinh-su-that/ 
- Chương 12: Giam Cầm Lời Nói Dối (826 từ): https://doctieuthuyet.com/chuong/chuong-12-giam-cam-loi-noi-doi/ 
- Chương 11: Tước Đoạt Danh Xưng (1196 từ): https://doctieuthuyet.com/chuong/chuong-11-tuoc-doat-danh-xung/ 
- Chương 10: Xé Nát Hồ Sơ Giả (800 từ): https://doctieuthuyet.com/chuong/chuong-10-xe-nat-ho-so-gia/ 
- Chương 8: Tiêm Độc Vào Chính Mình (726 từ): https://doctieuthuyet.com/chuong/chuong-8-tiem-doc-vao-chinh-minh/ 
- Chương 9: Đổi Chỗ Tử Thần (1244 từ): https://doctieuthuyet.com/chuong/chuong-9-doi-cho-tu-than/ 
- Chương 6: Đóng Băng Tài Khoản (952 từ): https://doctieuthuyet.com/chuong/chuong-6-dong-bang-tai-khoan/ 
- Chương 7: Bẻ Gãy Cánh Tay Ủng Hộ (963 từ): https://doctieuthuyet.com/chuong/chuong-7-be-gay-canh-tay-ung-ho/ 
- Chương 5: Cắt Đứt Dây Thần Kinh (631 từ): https://doctieuthuyet.com/chuong/chuong-5-cat-dut-day-than-kinh/ ==> ngắn (631 từ)
- Chương 4: Lật Đảo Hương Vị (1136 từ): https://doctieuthuyet.com/chuong/chuong-4-lat-dao-huong-vi/ 
- Chương 3: Nghiền Nát Niềm Tin (1335 từ): https://doctieuthuyet.com/chuong/chuong-3-nghien-nat-niem-tin/ 
- Chương 1: Giẫm Đạp Tự Tôn (729 từ): https://doctieuthuyet.com/chuong/chuong-1-giam-dap-tu-ton-3/ 
- Chương 2: Đuổi Cổ Danh Dự (1227 từ): https://doctieuthuyet.com/chuong/chuong-2-duoi-co-danh-du/ 
- Chương 12: Epilogue – Trọng Lượng Của Im Lặng (433 từ): https://doctieuthuyet.com/chuong/chuong-12-epilogue-trong-luong-cua-im-lang/ ==> ngắn (433 từ)
- Chương 11: Tiếng Vọng Từ Những Góc Quay Bị Lãng Quên (294 từ): https://doctieuthuyet.com/chuong/chuong-11-tieng-vong-tu-nhung-goc-quay-bi-lang-quen/ ==> ngắn (294 từ)
- Chương 10: Đại Hội Và Quyền Biểu Quyết (504 từ): https://doctieuthuyet.com/chuong/chuong-10-dai-hoi-va-quyen-bieu-quyet/ ==> ngắn (504 từ)
- Chương 9: Tờ Đơn Và Cái Giá Của Sự Im Lặng (407 từ): https://doctieuthuyet.com/chuong/chuong-9-to-don-va-cai-gia-cua-su-im-lang/ ==> ngắn (407 từ)
- Chương 8: Vết Nứt Lan Rộng Và Sự Chống Cự Cuối (412 từ): https://doctieuthuyet.com/chuong/chuong-8-vet-nut-lan-rong-va-su-chong-cu-cuoi/ ==> ngắn (412 từ)
- Chương 7: Âm Thanh Thật Và Bản Án Chưa Đóng Dấu (485 từ): https://doctieuthuyet.com/chuong/chuong-7-am-thanh-that-va-ban-an-chua-dong-dau/ ==> ngắn (485 từ)
- Chương 6: Đoạn Phim Và Cái Bẫy Đã Cài (288 từ): https://doctieuthuyet.com/chuong/chuong-6-doan-phim-va-cai-bay-da-cai/ ==> ngắn (288 từ)
- Chương 5: Đêm Mưa Và Câu Hỏi Không Lời Giải (343 từ): https://doctieuthuyet.com/chuong/chuong-5-dem-mua-va-cau-hoi-khong-loi-giai/ ==> ngắn (343 từ)
- Chương 4: Nỗi Sợ Ẩn Sau Lớp Sơn Móng Đỏ (246 từ): https://doctieuthuyet.com/chuong/chuong-4-noi-so-an-sau-lop-son-mong-do/ ==> ngắn (246 từ)
- Chương 3: Lời Tuyên Bố Và Vết Nứt Đầu Tiên (505 từ): https://doctieuthuyet.com/chuong/chuong-3-loi-tuyen-bo-va-vet-nut-dau-tien/ ==> ngắn (505 từ)
- Chương 2: Sân Khấu Từ Thiện Và Những Góc Quay Ẩn (546 từ): https://doctieuthuyet.com/chuong/chuong-2-san-khau-tu-thien-va-nhung-goc-quay-an/ ==> ngắn (546 từ)
- Chương 1: Bảng Giá Của Sự Im Lặng (605 từ): https://doctieuthuyet.com/chuong/chuong-1-bang-gia-cua-su-im-lang/ ==> ngắn (605 từ)
- Chương 10: Epilogue – Tiếng Nói Đầu Tiên (414 từ): https://doctieuthuyet.com/chuong/chuong-10-epilogue-tieng-noi-dau-tien/ ==> ngắn (414 từ)
- Chương 9: Cú Chốt Hạ (627 từ): https://doctieuthuyet.com/chuong/chuong-9-cu-chot-ha/ ==> ngắn (627 từ)
- Chương 8: Đơn Ly Hôn (635 từ): https://doctieuthuyet.com/chuong/chuong-8-don-ly-hon/ ==> ngắn (635 từ)
- Chương 7: Đổ Vỡ (641 từ): https://doctieuthuyet.com/chuong/chuong-7-do-vo/ ==> ngắn (641 từ)
- Chương 6: Clip Gốc Và Bản Án (673 từ): https://doctieuthuyet.com/chuong/chuong-6-clip-goc-va-ban-an/ ==> ngắn (673 từ)
- Chương 5: Tin Đồn Và Livestream (676 từ): https://doctieuthuyet.com/chuong/chuong-5-tin-don-va-livestream/ ==> ngắn (676 từ)
- Chương 4: Giấy Tờ Biết Nói (653 từ): https://doctieuthuyet.com/chuong/chuong-4-giay-to-biet-noi/ ==> ngắn (653 từ)
- Chương 2: Ba Năm Ghi Chép (953 từ): https://doctieuthuyet.com/chuong/chuong-2-ba-nam-ghi-chep/ 
- Chương 3: Tuyên Bố Cắt Quyền (776 từ): https://doctieuthuyet.com/chuong/chuong-3-tuyen-bo-cat-quyen/ 
- Chương 1: Hôn Ước Không Lời Thề (848 từ): https://doctieuthuyet.com/chuong/chuong-1-hon-uoc-khong-loi-the/ 
- Chương 13: Giật Sập Dự Án Ma (771 từ): https://doctieuthuyet.com/chuong/chuong-13-giat-sap-du-an-ma/ 
- Chương 12: Tước Quyền Đại Diện Pháp Lý (847 từ): https://doctieuthuyet.com/chuong/chuong-12-tuoc-quyen-dai-dien-phap-ly/ 
- Chương 11: Phơi Lộ Âm Mưu Chứng Khoán (745 từ): https://doctieuthuyet.com/chuong/chuong-11-phoi-lo-am-muu-chung-khoan/ 
- Chương 10: Tháo Dỡ Hệ Thống Bảo Mật (931 từ): https://doctieuthuyet.com/chuong/chuong-10-thao-do-he-thong-bao-mat/ 
- Chương 9: Đóng Cửa Ngân Hàng Gia Tộc (806 từ): https://doctieuthuyet.com/chuong/chuong-9-dong-cua-ngan-hang-gia-toc/ 
- Chương 8: Phơi Bày Hóa Đơn Thuê Giết (940 từ): https://doctieuthuyet.com/chuong/chuong-8-phoi-bay-hoa-don-thue-giet/ 
- Chương 7: Lật Đảo Hội Đồng Quản Trị (712 từ): https://doctieuthuyet.com/chuong/chuong-7-lat-dao-hoi-dong-quan-tri/ 
- Chương 6: Nghiền Nát Di Chúc (935 từ): https://doctieuthuyet.com/chuong/chuong-6-nghien-nat-di-chuc/ 
- Chương 5: Đuổi Cổ Ra Biệt Phủ (621 từ): https://doctieuthuyet.com/chuong/chuong-5-duoi-co-ra-biet-phu/ ==> ngắn (621 từ)
- Chương 4: Tước Đoạt Danh Dự (746 từ): https://doctieuthuyet.com/chuong/chuong-4-tuoc-doat-danh-du/ 
- Chương 3: Giẫm Đạp Lời Thề (686 từ): https://doctieuthuyet.com/chuong/chuong-3-giam-dap-loi-the/ ==> ngắn (686 từ)
- Chương 2: Xé Sổ Hộ Khẩu (677 từ): https://doctieuthuyet.com/chuong/chuong-2-xe-so-ho-khau/ ==> ngắn (677 từ)
- Chương 1: Đóng Cánh Cửa Nhà Chồng (626 từ): https://doctieuthuyet.com/chuong/chuong-1-dong-canh-cua-nha-chong/ ==> ngắn (626 từ)
- Chương 15: Xóa Tên Bà Trên Bia Mộ (964 từ): https://doctieuthuyet.com/chuong/chuong-15-xoa-ten-ba-tren-bia-mo/ 
- Chương 14: Phá Rào Căn Biệt Thự (703 từ): https://doctieuthuyet.com/chuong/chuong-14-pha-rao-can-biet-thu/ 
- Chương 13: Giẫm Đạp Lễ Cưới (1194 từ): https://doctieuthuyet.com/chuong/chuong-13-giam-dap-le-cuoi/ 
- Chương 12: Đóng Cửa Phòng Thờ (1006 từ): https://doctieuthuyet.com/chuong/chuong-12-dong-cua-phong-tho/ 
- Chương 11: Tước Đoạt Quyền Quản Lý (961 từ): https://doctieuthuyet.com/chuong/chuong-11-tuoc-doat-quyen-quan-ly/ 
- Chương 10: Bóc Trần Giấy Nuôi Con (954 từ): https://doctieuthuyet.com/chuong/chuong-10-boc-tran-giay-nuoi-con/ 
- Chương 9: Mở Khóa Hộp Đen Gia Tộc (571 từ): https://doctieuthuyet.com/chuong/chuong-9-mo-khoa-hop-den-gia-toc/ ==> ngắn (571 từ)
- Chương 8: Đóng Đinh Vào Hộp Kim Cương (877 từ): https://doctieuthuyet.com/chuong/chuong-8-dong-dinh-vao-hop-kim-cuong/ 
- Chương 7: Cắt Đứt Dây Dẫn Điện Thoại (620 từ): https://doctieuthuyet.com/chuong/chuong-7-cat-dut-day-dan-dien-thoai/ ==> ngắn (620 từ)
- Chương 6: Lật Đảo Bản Kê Thu Chi (925 từ): https://doctieuthuyet.com/chuong/chuong-6-lat-dao-ban-ke-thu-chi/ 
- Chương 5: Đổ Canh Nóng Lên Mặt Bà (642 từ): https://doctieuthuyet.com/chuong/chuong-5-do-canh-nong-len-mat-ba/ ==> ngắn (642 từ)
- Chương 4: Xé Rách Thư Gia Pháp (724 từ): https://doctieuthuyet.com/chuong/chuong-4-xe-rach-thu-gia-phap/ 
- Chương 5: TIỆM BÁNH MÌ GÓC ĐƯỜNG NGUYỄN TRÃI (967 từ): https://doctieuthuyet.com/chuong/chuong-5-tiem-banh-mi-goc-duong-nguyen-trai/ 
- Chương 4: CÚ ĐIỆN THOẠI (884 từ): https://doctieuthuyet.com/chuong/chuong-4-cu-dien-thoai/ 
- Chương 3: TIẾNG OXFORD TRÊN ĐÁ CẨM THẠCH (1001 từ): https://doctieuthuyet.com/chuong/chuong-3-tieng-oxford-tren-da-cam-thach/ 
- Chương 2: TỜ TIỀN NĂM TRĂM NGÀN (1161 từ): https://doctieuthuyet.com/chuong/chuong-2-to-tien-nam-tram-ngan/ 
- Chương 1: CHIẾC XE ĐIỆN MÀU TRẮNG ĐỤC (1264 từ): https://doctieuthuyet.com/chuong/chuong-1-chiec-xe-dien-mau-trang-duc/ 
- Chương 10: Màn Hình Sáng Trong Đêm (259 từ): https://doctieuthuyet.com/chuong/chuong-10-man-hinh-sang-trong-dem/ ==> ngắn (259 từ)
- Chương 9: Vết Son Nhoè Và Cánh Cửa Đóng Lại (234 từ): https://doctieuthuyet.com/chuong/chuong-9-vet-son-nhoe-va-canh-cua-dong-lai/ ==> ngắn (234 từ)
- Chương 8: Bản Giao Nhận Tài Sản (239 từ): https://doctieuthuyet.com/chuong/chuong-8-ban-giao-nhan-tai-san/ ==> ngắn (239 từ)
- Chương 7: Cuộc Gọi Từ Tầng 88 (336 từ): https://doctieuthuyet.com/chuong/chuong-7-cuoc-goi-tu-tang-88/ ==> ngắn (336 từ)
- Chương 6: Hợp Đồng Ẩn Danh (452 từ): https://doctieuthuyet.com/chuong/chuong-6-hop-dong-an-danh/ ==> ngắn (452 từ)
- Chương 5: Tờ Tiền Rơi Và Tiếng Chuông Ngân Hàng (463 từ): https://doctieuthuyet.com/chuong/chuong-5-to-tien-roi-va-tieng-chuong-ngan-hang/ ==> ngắn (463 từ)
- Chương 4: Quản Lý Gõ Cửa (550 từ): https://doctieuthuyet.com/chuong/chuong-4-quan-ly-go-cua/ ==> ngắn (550 từ)
- Chương 2: Ly Rượu Và Lời Thách Thức (612 từ): https://doctieuthuyet.com/chuong/chuong-2-ly-ruou-va-loi-thach-thuc/ ==> ngắn (612 từ)
- Chương 3: Vị Khách VIP Giả Tạo (524 từ): https://doctieuthuyet.com/chuong/chuong-3-vi-khach-vip-gia-tao/ ==> ngắn (524 từ)
- Chương 1: Bóng Người Lạ Trong Ánh Đèn Pha Lê (793 từ): https://doctieuthuyet.com/chuong/chuong-1-bong-nguoi-la-trong-anh-den-pha-le/ 
- Chương 3: Giật Rơi Vòng Tay Ngọc (842 từ): https://doctieuthuyet.com/chuong/chuong-3-giat-roi-vong-tay-ngoc/ 
- Chương 2: Bẻ Gãy Xương Đòn (723 từ): https://doctieuthuyet.com/chuong/chuong-2-be-gay-xuong-don/ 
- Chương 1: Đeo Mặt Nạ Osin (709 từ): https://doctieuthuyet.com/chuong/chuong-1-deo-mat-na-osin/ 
- Chương 10: Nghiền Nát Hy Vọng (959 từ): https://doctieuthuyet.com/chuong/chuong-10-nghien-nat-hy-vong-2/ 
- Chương 9: Phong Tỏa Tuyệt Đối (852 từ): https://doctieuthuyet.com/chuong/chuong-9-phong-toa-tuyet-doi/ 
- Chương 8: Triệu Hồi Tử Thần (1181 từ): https://doctieuthuyet.com/chuong/chuong-8-trieu-hoi-tu-than/ 
- Chương 7: Quét Sạch Niềm Tin (775 từ): https://doctieuthuyet.com/chuong/chuong-7-quet-sach-niem-tin/ 
- Chương 6: Lật Đổ Liên Minh (848 từ): https://doctieuthuyet.com/chuong/chuong-6-lat-do-lien-minh/ 
- Chương 5: Phơi Bày Dối Trá (572 từ): https://doctieuthuyet.com/chuong/chuong-5-phoi-bay-doi-tra/ ==> ngắn (572 từ)
- Chương 4: Đánh Lừa Tín Nhiệm (728 từ): https://doctieuthuyet.com/chuong/chuong-4-danh-lua-tin-nhiem/ 
- Chương 3: Gài Bẫy Thân Phận (735 từ): https://doctieuthuyet.com/chuong/chuong-3-gai-bay-than-phan/ 
- Chương 2: Tước Đoạt Danh Dự (554 từ): https://doctieuthuyet.com/chuong/chuong-2-tuoc-doat-danh-du/ ==> ngắn (554 từ)
- Chương 1: Ném Tiền Bắt Liếm Sàn (791 từ): https://doctieuthuyet.com/chuong/chuong-1-nem-tien-bat-liem-san/ 
- Chương 12: Thanh Toán Nợ Máu (683 từ): https://doctieuthuyet.com/chuong/chuong-12-thanh-toan-no-mau/ ==> ngắn (683 từ)
- Chương 11: Quét Sạch Danh Dự (999 từ): https://doctieuthuyet.com/chuong/chuong-11-quet-sach-danh-du/ 
- Chương 10: Nghiền Nát Hy Vọng (714 từ): https://doctieuthuyet.com/chuong/chuong-10-nghien-nat-hy-vong/ 
- Chương 9: Đuổi Cổ Khỏi Thế Giới (898 từ): https://doctieuthuyet.com/chuong/chuong-9-duoi-co-khoi-the-gioi/ 
- Chương 8: Phong Tỏa Tài Sản (719 từ): https://doctieuthuyet.com/chuong/chuong-8-phong-toa-tai-san/ 
- Chương 7: Cắt Đứt Đường Chạy (821 từ): https://doctieuthuyet.com/chuong/chuong-7-cat-dut-duong-chay/ 
- Chương 6: Tát Lật Mặt (694 từ): https://doctieuthuyet.com/chuong/chuong-6-tat-lat-mat/ ==> ngắn (694 từ)
- Chương 5: Gài Bẫy Tham Vọng (852 từ): https://doctieuthuyet.com/chuong/chuong-5-gai-bay-tham-vong/ 
- Chương 4: Đập Tan Ảo Tưởng (709 từ): https://doctieuthuyet.com/chuong/chuong-4-dap-tan-ao-tuong/ 
- Chương 3: Phơi Bày Dối Trá (784 từ): https://doctieuthuyet.com/chuong/chuong-3-phoi-bay-doi-tra/ 
- Chương 2: Tước Đoạt Niềm Kiêu Hãnh (901 từ): https://doctieuthuyet.com/chuong/chuong-2-tuoc-doat-niem-kieu-hanh/ 
- Chương 1: Giẫm Đạp Tự Tôn (758 từ): https://doctieuthuyet.com/chuong/chuong-1-giam-dap-tu-ton-2/ 
- Chương 10: Xóa Sổ Giả Danh (954 từ): https://doctieuthuyet.com/chuong/chuong-10-xoa-so-gia-danh/ 
- Chương 9: Nghiền Nát Thánh Thiện (297 từ): https://doctieuthuyet.com/chuong/chuong-9-nghien-nat-thanh-thien/ ==> ngắn (297 từ)
- Chương 8: Tước Trừ Dòng Họ (324 từ): https://doctieuthuyet.com/chuong/chuong-8-tuoc-tru-dong-ho/ ==> ngắn (324 từ)
- Chương 7: Đuổi Cổ Quyền Lực (1166 từ): https://doctieuthuyet.com/chuong/chuong-7-duoi-co-quyen-luc/ 
- Chương 6: Gài Bẫy Cổ Đông (478 từ): https://doctieuthuyet.com/chuong/chuong-6-gai-bay-co-dong/ ==> ngắn (478 từ)
- Chương 5: Phơi Bày Giả Diện (380 từ): https://doctieuthuyet.com/chuong/chuong-5-phoi-bay-gia-dien/ ==> ngắn (380 từ)
- Chương 4: Lật Mặt Huyết Thống (319 từ): https://doctieuthuyet.com/chuong/chuong-4-lat-mat-huyet-thong/ ==> ngắn (319 từ)
- Chương 3: Đầu Độc Niềm Tin (469 từ): https://doctieuthuyet.com/chuong/chuong-3-dau-doc-niem-tin/ ==> ngắn (469 từ)
- Chương 2: Tước Đoạt Danh Phận (295 từ): https://doctieuthuyet.com/chuong/chuong-2-tuoc-doat-danh-phan/ ==> ngắn (295 từ)
- Chương 1: Giẫm Đạp Tự Tôn (443 từ): https://doctieuthuyet.com/chuong/chuong-1-giam-dap-tu-ton/ ==> ngắn (443 từ)
- Chương 11: Thanh Tẩy Biển Cả, Hồi Sinh Làng Chài (1631 từ): https://doctieuthuyet.com/chuong/chuong-11-thanh-tay-bien-ca-hoi-sinh-lang-chai/ 
- Chương 10: Đập Tan Tường Thành Giả Dối (1594 từ): https://doctieuthuyet.com/chuong/chuong-10-dap-tan-tuong-thanh-gia-doi/ 
- Chương 9: Giải Cứu Cha: Nắm Giữ Chìa Khóa Cuộc … (1879 từ): https://doctieuthuyet.com/chuong/chuong-9-giai-cuu-cha-nam-giu-chia-khoa-cuoc/ 
- Chương 8: Bẫy Gông Cùm: Đẩy Vào Chân Tường (1611 từ): https://doctieuthuyet.com/chuong/chuong-8-bay-gong-cum-day-vao-chan-tuong/ 
- Chương 7: Chấn Động Kẻ Phản Bội Lão Làng (1608 từ): https://doctieuthuyet.com/chuong/chuong-7-chan-dong-ke-phan-boi-lao-lang/ 
- Chương 6: Bóc Trần Bộ Mặt Tổ Chức Ngầm (1362 từ): https://doctieuthuyet.com/chuong/chuong-6-boc-tran-bo-mat-to-chuc-ngam/ 
- Chương 5: Lật Tẩy Âm Mưu Dưới Lòng Biển (1383 từ): https://doctieuthuyet.com/chuong/chuong-5-lat-tay-am-muu-duoi-long-bien/ 
- Chương 4: Đánh Lừa Kẻ Đội Lốt Thần (1602 từ): https://doctieuthuyet.com/chuong/chuong-4-danh-lua-ke-doi-lot-than/ 
- Chương 3: Vén Màn Dấu Vết Cổ Xưa (1401 từ): https://doctieuthuyet.com/chuong/chuong-3-ven-man-dau-vet-co-xua/ 
- Chương 2: Xé Toang Bức Màn Mê Tín (1588 từ): https://doctieuthuyet.com/chuong/chuong-2-xe-toang-buc-man-me-tin/ 
- Chương 1: Gông Cùm Lời Nguyền Hắc Ám (1400 từ): https://doctieuthuyet.com/chuong/chuong-1-gong-cum-loi-nguyen-hac-am/ 
- Chương 12: Phá Vỡ Lời Nguyền: Khai Sáng Tương La… (1779 từ): https://doctieuthuyet.com/chuong/chuong-12-pha-vo-loi-nguyen-khai-sang-tuong-la/ 
- Chương 11: Chặn Đứng Nghi Lễ: Đại Chiến Linh Hồn (1759 từ): https://doctieuthuyet.com/chuong/chuong-11-chan-dung-nghi-le-dai-chien-linh-hon/ 
- Chương 10: Giải Mã Âm Mưu: Nguồn Gốc Tội Lỗi (1920 từ): https://doctieuthuyet.com/chuong/chuong-10-giai-ma-am-muu-nguon-goc-toi-loi/ 
- Chương 9: Xé Nát Xiềng Xích: Giao Ước Định Mệnh (1773 từ): https://doctieuthuyet.com/chuong/chuong-9-xe-nat-xieng-xich-giao-uoc-dinh-menh/ 
- Chương 8: Bẫy Gông Cùm: Âm Mưu Đoạt Hồn (1797 từ): https://doctieuthuyet.com/chuong/chuong-8-bay-gong-cum-am-muu-doat-hon/ 
- Chương 7: Lật Tẩy Bộ Mặt: Dã Tâm Phơi Bày (1603 từ): https://doctieuthuyet.com/chuong/chuong-7-lat-tay-bo-mat-da-tam-phoi-bay/ 
- Chương 6: Đập Tan Thành Kiến: Khẳng Định Giá Tr… (1680 từ): https://doctieuthuyet.com/chuong/chuong-6-dap-tan-thanh-kien-khang-dinh-gia-tr/ 
- Chương 5: Đánh Thức Dòng Máu: Lời Nguyền Hiện Hữu (1537 từ): https://doctieuthuyet.com/chuong/chuong-5-danh-thuc-dong-mau-loi-nguyen-hien-huu/ 
- Chương 4: Bóc Trần Giả Dối: Ánh Sáng Trong Bóng… (1943 từ): https://doctieuthuyet.com/chuong/chuong-4-boc-tran-gia-doi-anh-sang-trong-bong/ 
- Chương 3: Vén Màn Ám Ảnh: Dấu Hiệu Cổ Xưa (1737 từ): https://doctieuthuyet.com/chuong/chuong-3-ven-man-am-anh-dau-hieu-co-xua/ 
- Chương 2: Hóa Giải Oan Khuất: Tiếng Vọng Từ Quá… (1860 từ): https://doctieuthuyet.com/chuong/chuong-2-hoa-giai-oan-khuat-tieng-vong-tu-qua/ 
- Chương 1: Mở Màn Khinh Miệt: Thân Phận Bị Lãng … (1423 từ): https://doctieuthuyet.com/chuong/chuong-1-mo-man-khinh-miet-than-phan-bi-lang/ 
- Chương 17: Dệt Lên Bình Yên (1895 từ): https://doctieuthuyet.com/chuong/chuong-17-det-len-binh-yen/ 
- Chương 16: Tái Thiết Quyền Lực (1908 từ): https://doctieuthuyet.com/chuong/chuong-16-tai-thiet-quyen-luc/ 
- Chương 15: Rửa Oan Gia Tộc (1926 từ): https://doctieuthuyet.com/chuong/chuong-15-rua-oan-gia-toc/ 
- Chương 14: Giáng Phán Quyết Cuối Cùng (1975 từ): https://doctieuthuyet.com/chuong/chuong-14-giang-phan-quyet-cuoi-cung/ 
- Chương 13: Xoay Chuyển Bất Khả (1930 từ): https://doctieuthuyet.com/chuong/chuong-13-xoay-chuyen-bat-kha/ 
- Chương 12: Bẫy Gông Cùm Phản Đòn (1923 từ): https://doctieuthuyet.com/chuong/chuong-12-bay-gong-cum-phan-don/ 
- Chương 11: Giải Mã Thâm Cung (1609 từ): https://doctieuthuyet.com/chuong/chuong-11-giai-ma-tham-cung/ 
- Chương 10: Lật Đổ Chân Tướng (1584 từ): https://doctieuthuyet.com/chuong/chuong-10-lat-do-chan-tuong/ 
- Chương 9: Vạch Trần Hư Vọng (2081 từ): https://doctieuthuyet.com/chuong/chuong-9-vach-tran-hu-vong/ 
- Chương 8: Bóc Trần Mặt Nạ (1673 từ): https://doctieuthuyet.com/chuong/chuong-8-boc-tran-mat-na/ 
- Chương 7: Đánh Cắp Lòng Quân (1972 từ): https://doctieuthuyet.com/chuong/chuong-7-danh-cap-long-quan/ 
- Chương 6: Xé Toạc Âm Mưu (2092 từ): https://doctieuthuyet.com/chuong/chuong-6-xe-toac-am-muu/ 
- Chương 5: Đập Tan Ngụy Tạo (1898 từ): https://doctieuthuyet.com/chuong/chuong-5-dap-tan-nguy-tao/ 
- Chương 4: Phá Xiềng Trở Lại (1997 từ): https://doctieuthuyet.com/chuong/chuong-4-pha-xieng-tro-lai/ 
- Chương 3: Giáng Đòn Thăm Dò (2094 từ): https://doctieuthuyet.com/chuong/chuong-3-giang-don-tham-do/ 
- Chương 2: Lột Xác Giữa Nanh Vuốt (1867 từ): https://doctieuthuyet.com/chuong/chuong-2-lot-xac-giua-nanh-vuot/ 
- Chương 10: Củng Cố Công Lý (1325 từ): https://doctieuthuyet.com/chuong/chuong-10-cung-co-cong-ly/ 
- Chương 9: Vạch Mặt Kẻ Cầm Đầu (1437 từ): https://doctieuthuyet.com/chuong/chuong-9-vach-mat-ke-cam-dau/ 
- Chương 8: Đạp Đổ Thành Trì (1413 từ): https://doctieuthuyet.com/chuong/chuong-8-dap-do-thanh-tri/ 
- Chương 7: Phá Vỡ Màn Kịch (1725 từ): https://doctieuthuyet.com/chuong/chuong-7-pha-vo-man-kich/ 
- Chương 6: Lật Tẩy Kẻ Chỉ Điểm (Phản đòn) (1521 từ): https://doctieuthuyet.com/chuong/chuong-6-lat-tay-ke-chi-diem-phan-don-2/ 
- Chương 5: Chạm Trán Tử Thần (1588 từ): https://doctieuthuyet.com/chuong/chuong-5-cham-tran-tu-than-2/ 
- Chương 4: Phơi Bày Mưu Đồ (1550 từ): https://doctieuthuyet.com/chuong/chuong-4-phoi-bay-muu-do-2/ 
- Chương 3: Xé Toạc Lưới Che Đậy (1432 từ): https://doctieuthuyet.com/chuong/chuong-3-xe-toac-luoi-che-day-2/ 
- Chương 1: Chôn Vùi Ngọc Nát (1441 từ): https://doctieuthuyet.com/chuong/chuong-1-chon-vui-ngoc-nat/ 
- Chương 2: Đánh Hơi Sai Trái (1524 từ): https://doctieuthuyet.com/chuong/chuong-2-danh-hoi-sai-trai/ 
- Chương 1: Mở Màn Nghi Ngại (1511 từ): https://doctieuthuyet.com/chuong/chuong-1-mo-man-nghi-ngai/ 
- Chương 4: Đập Tan Hoài Nghi Cố Chấp (645 từ): https://doctieuthuyet.com/chuong/chuong-4-dap-tan-hoai-nghi-co-chap/ ==> ngắn (645 từ)
- Chương 3: Vạch Trần Lớp Bụi Thời Gian (738 từ): https://doctieuthuyet.com/chuong/chuong-3-vach-tran-lop-bui-thoi-gian/ 
- Chương 2: Lần Mở Những Mảnh Ký Ức Đứt Gãy (728 từ): https://doctieuthuyet.com/chuong/chuong-2-lan-mo-nhung-manh-ky-uc-dut-gay/ 
- Chương 1: Đánh Thức Ám Ảnh Cổ Xưa (850 từ): https://doctieuthuyet.com/chuong/chuong-1-danh-thuc-am-anh-co-xua/ 
- Chương 13: Kiến Tạo Tương Lai (910 từ): https://doctieuthuyet.com/chuong/chuong-13-kien-tao-tuong-lai/ 
- Chương 12: Tái Sinh Cuộc Đời (709 từ): https://doctieuthuyet.com/chuong/chuong-12-tai-sinh-cuoc-doi/ 
- Chương 11: Đánh Sập Đế Chế Đen (658 từ): https://doctieuthuyet.com/chuong/chuong-11-danh-sap-de-che-den/ ==> ngắn (658 từ)
- Chương 10: Vạch Trần Kẻ Chủ Mưu (809 từ): https://doctieuthuyet.com/chuong/chuong-10-vach-tran-ke-chu-muu/ 
- Chương 9: Nối Lại Huyết Thống (736 từ): https://doctieuthuyet.com/chuong/chuong-9-noi-lai-huyet-thong/ 
- Chương 8: Phá Tan Âm Mưu (527 từ): https://doctieuthuyet.com/chuong/chuong-8-pha-tan-am-muu/ ==> ngắn (527 từ)
- Chương 7: Giáng Đòn Phản Công (642 từ): https://doctieuthuyet.com/chuong/chuong-7-giang-don-phan-cong/ ==> ngắn (642 từ)
- Chương 6: Khiêu Chiến Quyền Năng (707 từ): https://doctieuthuyet.com/chuong/chuong-6-khieu-chien-quyen-nang/ 
- Chương 5: Truy Lùng Dấu Vết (601 từ): https://doctieuthuyet.com/chuong/chuong-5-truy-lung-dau-vet/ ==> ngắn (601 từ)
- Chương 4: Kích Hoạt Đồng Minh (717 từ): https://doctieuthuyet.com/chuong/chuong-4-kich-hoat-dong-minh/ 
- Chương 3: Cản Trở Truy Tìm (699 từ): https://doctieuthuyet.com/chuong/chuong-3-can-tro-truy-tim/ ==> ngắn (699 từ)
- Chương 2: Chấn Động Thân Phận (554 từ): https://doctieuthuyet.com/chuong/chuong-2-chan-dong-than-phan/ ==> ngắn (554 từ)
- Chương 1: Hóa Giải Xiềng Xích (705 từ): https://doctieuthuyet.com/chuong/chuong-1-hoa-giai-xieng-xich/ 
- Chương 12: Bí Mật Gia Đình Phơi Bày (779 từ): https://doctieuthuyet.com/chuong/chuong-12-bi-mat-gia-dinh-phoi-bay/ 
- Chương 11: Lật Ngược Tình Thế Trong Gang Tấc (658 từ): https://doctieuthuyet.com/chuong/chuong-11-lat-nguoc-tinh-the-trong-gang-tac/ ==> ngắn (658 từ)
- Chương 10: Bẫy Hoàn Hảo Của Mẹ Chồng (765 từ): https://doctieuthuyet.com/chuong/chuong-10-bay-hoan-hao-cua-me-chong/ 
- Chương 9: Cuốn Nhật Ký Định Mệnh (877 từ): https://doctieuthuyet.com/chuong/chuong-9-cuon-nhat-ky-dinh-menh/ 
- Chương 8: Chiếc Camera Đáng Ngờ (757 từ): https://doctieuthuyet.com/chuong/chuong-8-chiec-camera-dang-ngo/ 
- Chương 7: Lật Bài Ngửa Phản Công Đầu Tiên (630 từ): https://doctieuthuyet.com/chuong/chuong-7-lat-bai-ngua-phan-cong-dau-tien/ ==> ngắn (630 từ)
- Chương 6: Bí Mật Gia Đình Rúng Động (839 từ): https://doctieuthuyet.com/chuong/chuong-6-bi-mat-gia-dinh-rung-dong/ 
- Chương 5: Món Quà Bí Ẩn (813 từ): https://doctieuthuyet.com/chuong/chuong-5-mon-qua-bi-an/ 
- Chương 4: Cuộc Gặp Bí Ẩn (757 từ): https://doctieuthuyet.com/chuong/chuong-4-cuoc-gap-bi-an/ 
- Chương 3: Những Tin Nhắn Đe Dọa (476 từ): https://doctieuthuyet.com/chuong/chuong-3-nhung-tin-nhan-de-doa/ ==> ngắn (476 từ)
- Chương 2: Chiếc Điện Thoại Bí Mật (889 từ): https://doctieuthuyet.com/chuong/chuong-2-chiec-dien-thoai-bi-mat/ 
- Chương 1: Lời Khiêu Khích Trong Bữa Cơm (609 từ): https://doctieuthuyet.com/chuong/chuong-1-loi-khieu-khich-trong-bua-com/ ==> ngắn (609 từ)

## Thống kê lỗi

- Truyện có vấn đề ở mô tả/thứ tự: 8/91
- Chương bị flag: 110/1210
- Nhóm lỗi phổ biến:
  - chương ngắn dưới 700 từ: 109 chương
  - tên chương dài: 1 chương

## Gợi ý biên tập theo truyện

- **Bị Đuổi Khỏi Lab Đêm Trước IPO, Hóa Ra Anh Nắm Công Thức Trăm Tỷ**: 9 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
- **Võ Thần Đất Cảng: Vệ Sĩ Ẩn Thân Phá Bẫy Buôn Lậu 500 Tỷ Cảng Đình Vũ**: 9 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
- **Vợ Đòi Ly Hôn Vì Chồng Thất Nghiệp, Ngày Ký Đơn Chồng Nhận Danh Hiệu Kiến Trúc Sư Quốc Gia**: 8 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
- **Cô Gái Làng Bị Nhà Trai Hào Môn Từ Chối, Startup Nông Nghiệp Của Cô Niêm Yết 500 Tỷ**: 8 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
- **Thuyền Trưởng Tàu Cá Bị Chủ Cảng Ép Nợ, Hóa Ra Là Đại Gia Hàng Hải Đang Điều Tra Thâu Tóm**: 8 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
- **Trưởng Phòng Bán Hàng Khinh Nhân Viên Mới, Nhân Viên Đó Là Chuyên Gia Tư Vấn Của Tập Đoàn Mẹ**: 8 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
- **Giáo Sư Đuổi Học Trò Ra Khỏi Lớp Vì Dốt, Học Trò Đó Là Tác Giả Giáo Trình Giáo Sư Đang Dạy**: 8 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
- **Người Thợ Sửa Xe Ở Hầm B2**: 8 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
- **Mẹ Vợ Bắt Rửa Bát, Tôi Nấu Tiệc Michelin Chấn Động Phú Quốc**: 8 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
- **Cô Gái Bán Trà Sữa Và Hợp Đồng Trăm Tỷ**: 8 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
- **Bị Đuổi Khỏi Khách Sạn, Tôi Mua Luôn Chuỗi Năm Sao**: 8 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
- **Nghệ Nhân Sơn Mài Bị Khinh Rẻ Đuổi Khỏi Xưởng Tìm Ra Màu Sơn Thất Truyền Đè Bẹp Tập Đoàn Tranh Giả**: 6 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
- **Trọng Sinh 2008: Ôm Đất Đông Anh Trước Cơn Sốt Nghìn Tỷ**: 5 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
- **Thiên Tài Blockchain Phố Nguyễn Huệ: Bị Cướp Token Nghìn Tỷ, Tôi Hack Ngược Cả Sàn**: 3 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
- **Thợ Nuôi Trai Bị Cướp Ngọc Đen Đuổi Khỏi Vịnh, Trở Lại Lật Kèo Đoạt Lại Tập Đoàn Ngọc Trai Nghìn Tỷ**: 3 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
- **Chồng Nghèo Bị Họ Hàng Khinh Dự Tiệc Hào Môn, Hóa Ra Anh Là Khách Mời VIP Của Sự Kiện Đó**: 1 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
- **Kẻ Phế Vật Trở Về: Đòi Lại Gia Tộc Sau 12 Năm**: 1 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
- **Mẹ Chồng Gọi Tôi Là Người Ngoài, Sổ Đỏ Biệt Thự Gò Vấp 5 Tỷ Khiến Cả Mâm Giỗ Câm Lặng**: 1 flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.
