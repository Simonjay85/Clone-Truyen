# MASTER NOVEL PIPELINE — doctieuthuyet.com
# Quy trình chuẩn: Viết + Xuất Bản + Tối Ưu Truyện Sảng Văn Tự Động
# Cập nhật: 2026-05-22

---

## MỤC LỤC
1. [Tổng Quan Pipeline](#phần-1--tổng-quan-pipeline)
2. [Chuẩn V12 — Quy Tắc Viết Truyện](#phần-2--chuẩn-v12--quy-tắc-viết-truyện)
3. [Cấu Trúc Dữ Liệu JSON](#phần-3--cấu-trúc-dữ-liệu-json)
4. [Quy Trình Cover Art](#phần-4--quy-trình-cover-art)
5. [Quy Trình Xuất Bản WordPress](#phần-5--quy-trình-xuất-bản-wordpress)
6. [Quy Trình SEO RankMath](#phần-6--quy-trình-seo-rankmath)
7. [Credentials & Endpoints](#phần-7--credentials--endpoints)
8. [Danh Sách Concepts Chưa Viết](#phần-8--danh-sách-concepts-chưa-viết)
9. [Hướng Dẫn Thực Thi](#phần-9--hướng-dẫn-thực-thi)

---

## PHẦN 1 — Tổng Quan Pipeline

### Workflow cho MỖI truyện:

```
Bước 1: Nhận/Tạo concept (title, nhân vật, bối cảnh, xung đột)
   ↓
Bước 2: Viết dàn ý chi tiết 8-15 chương (tùy cốt truyện)
   ↓
Bước 3: Viết từng chương đầy đủ (1000-1500 từ/chương, HTML format V12)
   ↓
Bước 4: Lưu pending_novel.json
   ↓
Bước 5: Vẽ cover bằng generate_image (KHÔNG dùng API ngoài)
   ↓
Bước 6: Áp overlay gold frame bằng cover_overlay_standard.py
   ↓
Bước 7: Lưu cover thành pending_cover.png
   ↓
Bước 8: Chạy publish_local_novel.py → Deploy WordPress
   ↓
Bước 9: Cập nhật existing_novels.json
   ↓
Bước 10: Cập nhật RankMath SEO
   ↓
Bước 11: Clear LiteSpeed Cache
```

### Nguồn lực sử dụng:
- **Viết truyện**: Model Claude Opus (Antigravity) — KHÔNG dùng OpenAI API hay API ngoài
- **Vẽ cover**: Tool `generate_image` của Gemini — KHÔNG dùng Pollinations hay API ngoài
- **Overlay cover**: Script `cover_overlay_standard.py` (Python + Pillow)
- **Publish**: FTP + PHP helper scripts trên WordPress
- **SEO**: PHP script chạy trực tiếp trên server qua FTP upload

### Các file quan trọng:

| File | Đường dẫn | Chức năng |
|------|-----------|-----------|
| Novel concepts | `/Users/aaronnguyen/TN/App/doctieuthuyet/novel_concepts_50.json` | 50 concept truyện chưa viết |
| Cover overlay | `/Users/aaronnguyen/TN/App/doctieuthuyet/cover_overlay_standard.py` | Áp gold frame lên cover |
| Cover prompt | `/Users/aaronnguyen/TN/App/doctieuthuyet/prompts/cover_prompt_master.md` | Chuẩn thiết kế bìa |
| Publisher | `/Users/aaronnguyen/TN/App/doctieuthuyet/publish_local_novel.py` | Publish truyện lên WP |
| PHP Helper | `/Users/aaronnguyen/TN/App/doctieuthuyet/publish_novel.php` | Server-side WP publisher |
| PHP Overwriter | `/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/overwrite_story_generic.php` | Ghi đè truyện có sẵn |
| Existing novels | `/Users/aaronnguyen/TN/App/doctieuthuyet/existing_novels.json` | Danh sách truyện đã publish |
| SEO updater | `/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/update_all_rankmath_seo.py` | Bulk SEO RankMath |
| Pipeline doc | `/Users/aaronnguyen/TN/App/doctieuthuyet/prompts/novel_pipeline_master.md` | **FILE NÀY** |

---

## PHẦN 2 — Chuẩn V12 — Quy Tắc Viết Truyện

### Thể loại: Sảng Văn / Vả Mặt (Slap-face / Face-slap fiction)

### Cấu trúc truyện chuẩn:
- **Số chương**: 8-15 (tùy độ phức tạp cốt truyện)
- **Độ dài chương**: 1000-1500 từ tiếng Việt (~6000-9000 ký tự)
- **Tiêu đề truyện**: Style clickbait giật gân, gây tò mò
  - VD: "Mẹ Vợ Đòi Sính Lễ 5 Tỷ Khinh Tôi Nghèo, Landmark 81 Là Của Tôi"
  - VD: "Bị Đuổi Khỏi Khách Sạn, Tôi Mua Luôn Chuỗi Năm Sao"

### 6 Quy Tắc Vàng V12:

#### 1. SHOW, DON'T TELL
- ❌ TUYỆT ĐỐI KHÔNG: "hắn vô cùng kinh hoàng", "cô vô cùng tức giận"
- ✅ BẮT BUỘC MÔ TẢ VẬT LÝ:
  - "mồ hôi rịn ra ướt đẫm lưng áo sơ mi lụa"
  - "làn da chuyển màu xám ngoét"
  - "ngón tay run rẩy bấu chặt vào cạnh bàn gỗ"
  - "nhịp tim đập loạn xạ"
  - "gót giày cao gót gõ xuống nền đá hoa cương sắc lạnh"
  - "đầu gối quỳ xuống đất cộp"
  - "ngón tay bấm rỉ máu"

#### 2. CHI TIẾT CHUYÊN MÔN CHÂN THỰC
- **Y thuật**: Huyệt đạo (Hợp Cốc, Nhân Trung, Kỳ Môn, Chương Môn, Dũng Tuyền, Thái Xung), vị thuốc Nam (nhân trần, diệp hạ châu, bồ công anh, cỏ mực, bạch hoa xà) với tỷ lệ và cơ chế
- **Thương chiến**: Kiểm toán độc lập, sáp nhập ngược (reverse merger), thâu tóm cổ phần chi phối, M&A
- **Pháp lý**: C03 Bộ Công an, A05, SCIC, UBCKNN, Cục SHTT, Luật Doanh nghiệp 2020
- **Tài chính**: Ngân hàng thật (Vietcombank, Techcombank, Agribank, MB Bank, VPBank)

#### 3. BỐI CẢNH VIỆT NAM THUẦN KHIẾT
- 100% nhân vật Việt Nam, tên Việt Nam
- Địa danh thật: cảng Tiên Sa, phố cổ Hà Nội, Phú Mỹ Hưng Q7, KCN VSIP...
- Cơ quan thật: Bộ Công Thương, Sở Y tế, EVN, Tổng cục Thủy sản...
- KHÔNG viết bối cảnh nước ngoài (trừ khi cần cho cốt truyện)

#### 4. TRÁNH VIẾT TẮT
- ✅ "thành phố Hồ Chí Minh" — KHÔNG "TPHCM"
- ✅ "khu công nghiệp" — KHÔNG "KCN"
- ✅ "ngân hàng thương mại cổ phần ngoại thương Việt Nam" — KHÔNG "Vietcombank" (lần đầu tiên đề cập)
- Lý do: Hệ thống regex tách câu tự động cần chạy chuẩn xác

#### 5. CẤU TRÚC CỐT TRUYỆN
- **Chương 1-2**: Nhân vật chính bị ức hiếp, nhục mạ, đuổi khỏi vị trí → tạo sự đồng cảm
- **Chương 2-3**: Gặp nữ chính (thường là người có quyền lực/vị trí cao) → thử thách sòng phẳng
- **Chương 3-5**: Vượt qua thử thách bằng tài năng thiên bẩm → bộc lộ năng lực
- **Chương 4-6**: Phản diện tấn công (phá hoại, vu oan, bôi nhọ) → khủng hoảng
- **Chương 5-7**: VẢ MẶT LẦN 1 — Dùng trí tuệ/bằng chứng lật ngược thế cờ
- **Chương 6-9**: Phản diện nâng cấp tấn công (cấu kết thế lực lớn hơn) → khủng hoảng lần 2
- **Chương 8-12**: VẢ MẶT LẦN 2 — Đập tan hoàn toàn phe phản diện, C03 bắt giữ
- **Chương cuối**: Nhân vật chính thắng lợi vinh quang, nữ chính chủ động bày tỏ tình cảm

#### 6. ĐỊNH DẠNG HTML V12
- Mỗi câu nằm trong THẺ `<p>` RIÊNG (V12 paragraph splitting)
- Chỉ dùng: `<p>`, `<strong>`, `<em>` — không dùng thẻ khác
- Đoạn mở đầu truyện (intro) BẮT BUỘC dùng: `<p><strong>"Trích dẫn kịch tính..."</strong></p>`

### Nữ chính — Quy tắc đặc biệt:
- Thông minh, sắc sảo, quyền lực (CEO, giám đốc, viện trưởng...)
- Đặt điều kiện sòng phẳng cho nam chính trước khi hợp tác
- KHÔNG yếu đuối, KHÔNG cần được cứu, chủ động trong mọi quyết định
- Cuối truyện: chủ động bày tỏ tình cảm chân thành tự nguyện

---

## PHẦN 3 — Cấu Trúc Dữ Liệu JSON

### pending_novel.json (Input cho publisher):
```json
{
  "title": "Tên Truyện Giật Gân Clickbait Siêu Cuốn",
  "author": "Bút Danh Ấn Tượng",
  "genre": "Sảng Văn",
  "intro": "<p><strong>\"Đoạn mở đầu kịch tính nhất...\"</strong></p><p><strong>Thế nhưng họ không ngờ...</strong></p><hr /><p>Mô tả bối cảnh chi tiết...</p>",
  "cover_prompt": "Square format Vietnamese web novel book cover...",
  "chapters": [
    {
      "title": "Chương 1: Tên Chương Giật Gân",
      "content": "<p>Mỗi câu nằm trong thẻ p riêng.</p>\n<p>Đây là câu thứ hai.</p>"
    }
  ]
}
```

### existing_novels.json (Registry tránh trùng lặp):
```json
[
  {
    "id": 2517,
    "title": "Thiên Tài Khởi Nghiệp Fintech",
    "slug": "thien-tai-khoi-nghiep-fintech",
    "intro": "<p><strong>...</strong></p>"
  }
]
```

### novel_concepts_50.json (Concept pool):
```json
[
  {
    "idx": 1,
    "title": "Vua Tôm Hùm Phú Yên...",
    "author": "Trần Hải Phong",
    "num_chapters": 10,
    "setting": "Phú Yên, vùng biển Vũng Rô...",
    "male_lead": "Mô tả nam chính...",
    "female_lead": "Mô tả nữ chính...",
    "conflict": "Xung đột chính...",
    "cover_desc": "Cover art description...",
    "genre_visual": "genre keyword"
  }
]
```

---

## PHẦN 4 — Quy Trình Cover Art

### Bước 1: Vẽ base image
- Dùng tool `generate_image` (Gemini) — KHÔNG dùng API ngoài
- Prompt theo chuẩn `cover_prompt_master.md`:
Square format Vietnamese web novel book cover illustration, realistic live-action cinematic movie poster style, high-budget Vietnamese drama film look, dramatic lighting, high detail, masterpiece, 8k resolution, photorealistic characters,
[VISUAL_DIRECTION],
[CHARACTER_DESCRIPTION],
[BACKGROUND_SCENE],
dark at the TOP 30% of image for text overlay readability,
elegant cinematic lighting, rich color grading, high detail,
no text, no letters, no watermarks, no logos, no chapter numbers, no badges.
Square 1:1 composition.
```

### Bước 2: Apply overlay (cover_overlay_standard.py)
- Input: base image + title + subtitle
- Output: 2000x2000 PNG với:
  - Top dark gradient (RGBA 0,0,0,210 → transparent)
  - Gold double border frame (#EBC350)
  - Corner ornaments
  - Title text gold (.upper(), Arial Bold, auto-fit 120px)
  - Subtitle text white
  - Bottom label "TIỂU THUYẾT VIỆT NAM"
- KHÔNG vẽ chapter badge, view count, logo

### Bước 3: Save
- Copy output → `pending_cover.png` (root thư mục project)

---

## PHẦN 5 — Quy Trình Xuất Bản WordPress

### Phương pháp 1: Truyện MỚI (dùng publish_local_novel.py)
```bash
# 1. Đảm bảo pending_novel.json và pending_cover.png tồn tại
# 2. Chạy:
cd /Users/aaronnguyen/TN/App/doctieuthuyet
python3 publish_local_novel.py
```
- Script tự động:
  - Upload cover qua FTP → wp-content/uploads/
  - Upload publish_novel.php helper → FTP root
  - POST JSON đến publish_novel.php → tạo post_type=truyen + chapters
  - Cập nhật existing_novels.json
  - Xóa pending files + remote helper

### Phương pháp 2: GHI ĐÈ truyện có sẵn (dùng overwrite_story_generic.php)
```bash
# Upload overwrite_story_generic.php via FTP trước
# Gửi POST request với story_id cụ thể
```

### WordPress Custom Post Types:
- `truyen` — Bài viết truyện chính (chứa intro, cover, metadata)
- `chuong` — Bài viết chương (liên kết qua `_truyen_id` postmeta)
- `truyen_tacgia` — Meta field tác giả
- `truyen_status` — Meta field trạng thái (ongoing/completed)

---

## PHẦN 6 — Quy Trình SEO RankMath

### Cho 1 truyện:
Sau khi publish, cập nhật RankMath postmeta:
- `_rank_math_title` / `rank_math_title` — SEO title (max 65 chars, thêm suffix clickbait)
- `_rank_math_description` / `rank_math_description` — Description (trích từ <strong> block, max 155 chars)
- `_rank_math_focus_keyword` / `rank_math_focus_keyword` — 4 từ đầu tiên lowercase
- `rank_math_rich_snippet` — "article"

### Bulk SEO (cho tất cả):
```bash
cd /Users/aaronnguyen/TN/App/doctieuthuyet
python3 scratch/update_all_rankmath_seo.py
```
- Upload temp PHP → FTP root
- Execute via HTTP → update tất cả truyện
- Xóa temp PHP
- Clear LiteSpeed cache

---

## PHẦN 7 — Credentials & Endpoints

```
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL   = "https://doctieuthuyet.com"
SECRET_TOKEN = "ZEN_TRUYEN_2026_BYPASS"
```

---

## PHẦN 8 — Danh Sách Concepts Chưa Viết

Xem file: `novel_concepts_50.json`

50 đề tài đa dạng đã chuẩn bị sẵn, mỗi concept gồm:
- Title clickbait + author + số chương (8-15)
- Setting (địa danh VN cụ thể)
- Nam chính + Nữ chính + Xung đột chính
- Cover description + Genre visual

**Khi nhận lệnh "viết N truyện":**
1. Đọc `existing_novels.json` → lấy danh sách đã publish
2. Đọc `novel_concepts_50.json` → chọn N concept chưa viết
3. Viết + publish theo pipeline ở Phần 1
4. Cập nhật `existing_novels.json`
5. Chạy bulk SEO updater

---

## PHẦN 9 — Hướng Dẫn Thực Thi

### Khi user ra lệnh: "viết 10 truyện" hoặc "viết 20 truyện"

**Bước 1**: Đọc file này (`novel_pipeline_master.md`) để nắm toàn bộ quy trình

**Bước 2**: Đọc `existing_novels.json` để biết truyện nào đã publish

**Bước 3**: Đọc `novel_concepts_50.json` để lấy concepts chưa viết

**Bước 4**: Chia batch (khuyến nghị 5-10 truyện/batch)

**Bước 5**: Cho mỗi truyện trong batch:
1. Viết intro kịch tính theo format `<p><strong>"..."</strong></p>`
2. Viết dàn ý chi tiết cho từng chương
3. Viết NỘI DUNG TỪNG CHƯƠNG (1000-1500 từ, V12 format)
4. Lưu `pending_novel.json`
5. Vẽ cover bằng `generate_image` → save `base_cover.png`
6. Chạy `cover_overlay_standard.py` → tạo `pending_cover.png`
7. Chạy `python3 publish_local_novel.py`
8. Xác nhận publish thành công

**Bước 6**: Sau khi xong batch, chạy `update_all_rankmath_seo.py`

**Bước 7**: Báo cáo kết quả cho user

### Lưu ý quan trọng:
- Dùng model Opus (chính mình) để viết — KHÔNG gọi OpenAI/API ngoài
- Dùng `generate_image` tool để vẽ cover — KHÔNG dùng Pollinations
- Mỗi truyện xử lý tuần tự (pending_novel.json là single file)
- Kiểm tra word count ≥ 1000 từ mỗi chương trước khi lưu
- Luôn cập nhật `existing_novels.json` sau mỗi truyện thành công
