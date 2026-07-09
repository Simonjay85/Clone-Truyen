# JSON Schema — Output truyện hoàn chỉnh

## Schema cho Chat Mode (1 lượt xuất toàn bộ)

```json
{
  "title": "Tiêu đề 12-22 từ có hook nhục → lật → vả",
  "author": "Tên tác giả",
  "genre": "Sảng Văn",
  "intro": "<p><strong>\"Câu thoại sỉ nhục hook...\"</strong></p><p>Hé lộ bí mật...</p><p>Lời hứa trả thù...</p>",
  "cover_prompt": "Square 1:1 photorealistic Vietnamese web novel cover, real human actors, cinematic movie poster, [VISUAL_DIRECTION], [CHARACTER_DESCRIPTION], [BACKGROUND_SCENE], dramatic conflict visible, dark TOP 30% for title, high contrast lighting, no watermark, no logo.",
  "chapters": [
    {
      "title": "Chương 1: [Tên chương]",
      "content": "<p>[Nội dung chi tiết 1000-1500 từ, HTML only <p>/<strong>/<em>]</p>"
    }
  ]
}
```

## Quy tắc JSON

- Chỉ trả về duy nhất JSON hợp lệ, không bọc trong ```json
- Không thêm văn bản giải thích trước hoặc sau JSON
- Mỗi chương content tối thiểu 1000 từ tiếng Việt
- HTML chỉ dùng: `<p>`, `<strong>`, `<em>`, `<hr>`
- Không lặp tiêu đề chương trong phần content
- Số chương: 8-15 (tự chọn theo độ phức tạp cốt truyện)

## Schema cho Schedule Mode

### Bước 1 — Concept Output
```json
{
  "title": "...",
  "author": "...",
  "genre": "Sảng Văn",
  "intro": "<p>...</p>",
  "cover_prompt": "...",
  "story_dna": {
    "profession_world": "...",
    "central_evidence": "...",
    "unique_set_pieces": ["..."],
    "midpoint_crisis": "...",
    "relationship_signature": "...",
    "ending_signature": "..."
  },
  "outlines": [
    { "chap_num": 1, "outline": "..." }
  ]
}
```

### Bước 2 — Chapter Output
```json
{
  "title": "Chương [X]: [Tên chương]",
  "content": "<p>...</p>"
}
```
