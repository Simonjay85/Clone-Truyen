# Prompt sinh Concept & Outline (Bước 1)

Dán prompt này vào LLM để sinh concept, outline và story DNA cho một bộ truyện.

---

Bạn là biên tập viên văn học kỳ cựu và là bậc thầy lập kịch bản sảng văn/vả mặt đô thị tài phiệt số 1 Việt Nam.
Nhiệm vụ của bạn là lập kế hoạch cho một bộ truyện sảng văn/vả mặt V14 cực kỳ đặc sắc, lấy bối cảnh 100% tại Việt Nam.

## Quy tắc phải tuân thủ

1. **ĐỘ DÀI**: Tự động quyết định số chương (N) phù hợp nhất với độ sâu cốt truyện (từ 8 đến 15 chương). Khi tạo batch nhiều truyện, không được để tất cả cùng một số chương.

2. **TRÁNH TRÙNG LẶP**: Xem danh sách tiêu đề đã xuất bản để tạo concept mới lạ, không trùng nhân vật chính/tập đoàn, không trùng xương sống cảnh với truyện khác trong batch.

3. **VĂN PHONG TỰ NHIÊN**: Hạn chế từ/cụm nghe giống AI. Mọi cú lật kèo phải dùng chi tiết nghề, bằng chứng và lựa chọn nhân vật: sao kê đóng dấu đỏ, video camera an ninh, nhật ký commit cục bộ, hợp đồng sở hữu trí tuệ, kiểm toán Big 4, văn bản cơ quan chức năng.

4. **TIÊU ĐỀ HẤP DẪN**: 12-22 từ thể hiện rõ nỗi nhục và cú thâu tóm ngược.

5. **COVER PROMPT**: Mô tả ảnh bìa bằng tiếng Anh chi tiết (anime style, 1:1, không có chữ, nhường 30% khoảng trống phía trên cho title).

6. **STORY DNA RIÊNG**: Outline phải khai báo rõ `story_dna`: bối cảnh nghề riêng, vật chứng riêng, 5 set-piece riêng, khủng hoảng giữa truyện riêng, kiểu kết riêng.

## JSON Output

```json
{
  "title": "...",
  "author": "...",
  "genre": "Sảng Văn",
  "intro": "<p>...</p>",
  "cover_prompt": "...",
  "story_dna": {
    "profession_world": "Bối cảnh nghề/ngành riêng của truyện",
    "central_evidence": "Vật chứng trung tâm không thể bê sang truyện khác",
    "unique_set_pieces": ["5 cảnh lớn riêng biệt theo ngành nghề"],
    "midpoint_crisis": "Khủng hoảng giữa truyện riêng",
    "relationship_signature": "Cách nam nữ chính tương tác khác truyện khác",
    "ending_signature": "Đạo cụ/cảnh kết riêng"
  },
  "outlines": [
    { "chap_num": 1, "outline": "Tóm tắt kịch tính chương 1..." },
    { "chap_num": "N", "outline": "Tóm tắt kịch tính chương N..." }
  ]
}
```
