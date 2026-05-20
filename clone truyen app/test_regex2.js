const text = `
# Chê Tôi Đi Vision Nghèo Hèn, Nhà Chồng Bắt Trả 600 Triệu Tiền Ở Nhờ

**Subtitle:** Đến Ngày Chia Tài Sản, Tôi Mở Laptop Cho Họ Xem 3 Căn Nhà Cho Thuê
**Thể loại:** Đô thị vả mặt / Hôn nhân / Gia đình / Tài sản riêng
**Bối cảnh:** Sài Gòn hiện đại
**Độ dài:** 5 chương

---

## CHươNG 1: Sáu Trăm Triệu Tiền Ở Nhờ
`;

const regex = /^\s*(?:#{1,4}\s*)?(?:chương|chuong)\s+(\d+)\s*[:.;\-–—]?\s*(.*?)$/gmiu;

let match;
while ((match = regex.exec(text)) !== null) {
  console.log("MATCH:", match[0]);
}
