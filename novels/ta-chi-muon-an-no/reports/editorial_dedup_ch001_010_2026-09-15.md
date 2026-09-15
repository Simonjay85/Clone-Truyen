# Editorial Dedup Audit — Chương 001–010

**Ngày:** 2026-09-15  
**Phạm vi:** local source only; không publish WordPress tự động.  
**QA:** PASS — hard failures 0, warnings 0.  
**Active chapters còn “Trúc Cơ”:** NO.  
**Export SHA256:** `e7c3ebbb74add35dd2cc9990296d3e7de94228922665d35fd405bed873709468`

## Kết luận biên tập

- Đã tách chức năng Ch1/Ch2: Ch1 = bình thường từ bên trong; Ch2 = bất thường qua mắt người ngoài.
- Đã xóa vòng lặp gánh nước/nhịp thở ở Ch3 và chuyển Ch3 thành chương neo cảm xúc + mở rộng thế giới.
- Đã giảm chuỗi lặp sinh nhật/dặn dò/tiễn đi ở Ch4–6 mà vẫn giữ payoff cảm xúc.
- Đã giảm vòng lặp Ô Kê ở Ch7 và đưa reveal trận che lên sớm.
- Đã tách rõ Ch8 benchmark tu sĩ, Ch9 pháp thuật/kinh tế, Ch10 dị thường tu luyện + external threat.
- Canon cảnh giới đã khóa theo story bible: `Dẫn Khí → Khai Mạch → Trúc Đài → Kim Đan → Nguyên Anh`.

## Vai trò riêng và thay đổi từng chương

### Chương 1: Chương 1: Con Gà Cuối Cùng Của Lạc Kê
- **New-information payload:** Giới thiệu Tiểu Bảo + Ô Kê + Lạc Kê như một gia đình; mốc 13 tuổi là hook chính.
- **Chỉnh sửa:** Trim phần liệt kê sức mạnh cụ thể của dân làng để không spoil Ch2.
- **Word count QA:** 2263

### Chương 2: Chương 2: Thôi Đồ Tể Lại Đánh Người
- **New-information payload:** Dùng góc nhìn người ngoài để xác nhận Tiểu Bảo/Lạc Kê bất thường; payoff đường rìu.
- **Chỉnh sửa:** Rewrite nặng: rút Ô Kê/gánh nước; giữ thương lượng thịt; tập trung đường rìu → Thanh Cương Thạch → outsider; bỏ ending ăn canh/sinh nhật lặp.
- **Word count QA:** 1705

### Chương 3: Chương 3: Trên Đỉnh Vọng Phong
- **New-information payload:** Mở rộng thế giới + neo cảm xúc “nhà”; seed nồi đen, không lặp bài luyện gánh nước.
- **Chỉnh sửa:** Rewrite nặng, đổi tên “Trên Đỉnh Vọng Phong”; bỏ trial gánh nước lặp; thêm world-scale/home dream/nồi đen.
- **Word count QA:** 1634

### Chương 4: Chương 4: Sinh Nhật Mười Ba Tuổi
- **New-information payload:** Sinh nhật và không khí chia tay; Tiểu Bảo nghe nửa câu và hiểu lầm mình bị đuổi.
- **Chỉnh sửa:** Trim vòng hỏi từng người về bí mật, giữ birthday + eavesdrop payoff.
- **Word count QA:** 1992

### Chương 5: Chương 5: Hội Nghị Đuổi Trẻ Con
- **New-information payload:** Đảo ngược hiểu lầm; hé lore người làng; Tiểu Bảo tự chọn xuống núi.
- **Chỉnh sửa:** Trim recap trò phá làng; sửa continuity Xích Tâm Căn “hôm qua”; chuẩn hóa Trúc Đài.
- **Word count QA:** 2958

### Chương 6: Chương 6: Ba Đồng Tiền
- **New-information payload:** Trao ba đồng tiền/vật dụng; chia tay; trận che Lạc Kê đóng sau lưng.
- **Chỉnh sửa:** Trim nostalgia mở chương; giữ ba đồng tiền, quà tiễn và trận che.
- **Word count QA:** 1895

### Chương 7: Chương 7: Con Gà Tự Đi Theo
- **New-information payload:** Độc lập lần đầu; không tìm được đường về; nhận Ô Kê làm bạn đồng hành; gặp người ngoài thường.
- **Chỉnh sửa:** Trim dài phần cãi với Ô Kê; vào nhanh reveal không tìm thấy Lạc Kê từ bên ngoài.
- **Word count QA:** 1886

### Chương 8: Chương 8: Người Tu Tiên Đầu Tiên
- **New-information payload:** Thiết lập benchmark tu sĩ bình thường và hệ cảnh giới canonical.
- **Chỉnh sửa:** Bỏ giải thích “tên cảnh giới vùng khác”; khóa Dẫn Khí → Khai Mạch → Trúc Đài → Kim Đan → Nguyên Anh.
- **Word count QA:** 1874

### Chương 9: Chương 9: Tu Tiên Thật Đáng Sợ
- **New-information payload:** Thiết lập pháp thuật/yêu thú/kinh tế linh thạch bằng một biến cố hành động.
- **Chỉnh sửa:** Giữ cấu trúc vì payload riêng đã rõ: chiến đấu thật + phù + kiếm khí + linh thạch.
- **Word count QA:** 1778

### Chương 10: Chương 10: Ước Mơ Mới Của Tạ Tiểu Bảo
- **New-information payload:** Tiểu Bảo bắt đầu kiếm tiền, giấu sức; thử cảm khí thất bại và mở nguy cơ Hắc Nha Pha.
- **Chỉnh sửa:** Rewrite phần đầu: bỏ recap giá tài nguyên dài; vào nhanh việc làm 300 đồng → giấu sức → cảm khí dị thường → Hắc Nha Pha.
- **Word count QA:** 1568

## Guardrails cho Chương 11+

1. Mỗi chương phải có **một new-information payload chính**; không dùng lại cùng payoff của chương trước.
2. Không lặp pattern `việc nhà → hóa ra là luyện công → người lớn bí ẩn → Tiểu Bảo không hiểu` quá 1 lần trong cùng sub-arc.
3. Running gag Ô Kê/đồ ăn chỉ là seasoning; không dùng làm opening engine hai chương liên tiếp.
4. Không kết một chương bằng cùng hook `13 tuổi / người lớn có chuyện giấu` sau khi hook đã được trả.
5. Nếu callback đến “nhà không dột / ăn no / tiền”, phải tạo quyết định hoặc hậu quả mới, không diễn lại cùng monologue.
6. Power reveal ưu tiên **external calibration** hoặc hậu quả mới; tránh liên tục “Tiểu Bảo làm việc bình thường nhưng thực ra rất mạnh”.
7. Trước batch mới, đọc `continuity/ledger.json` + hai chương gần nhất; `scratch/batch_011_021_context.md` đã được regenerate theo canon mới.

## Rollback / artifacts

- Backup trước chỉnh sửa: `backups/pre_dedup_2026-09-15/` (10 chương).
- Review export mới: `exports/Ta_Chi_Muon_An_No_Chuong_001-010.md`.
- Live site vẫn đang là bản cũ cho đến khi có workflow publish được ủy quyền riêng.
