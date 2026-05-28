# MASTER NOVEL PIPELINE — doctieuthuyet.com
# Quy trình chuẩn: Viết + Xuất Bản + Tối Ưu Truyện Sảng Văn Tự Động
# Cập nhật: 2026-05-27

> [!IMPORTANT]
> **CHỈ DÙNG CHATGPT IMAGE GENERATION CHO HÌNH ẢNH MỚI**
> - Cover mới phải được tạo bằng ChatGPT Image Generation hoặc lấy từ file local đã được duyệt.
> - Tuyệt đối không gọi API sinh ảnh bên thứ ba trong script/pipeline.
> - Ảnh sau khi tạo phải được lưu local, kiểm tra preview, rồi upload/gắn featured image bằng workflow cover của repo.

---

## MỤC LỤC
1. [Tổng Quan Pipeline](#phần-1--tổng-quan-pipeline)
2. [Chuẩn V13 Gold — Quy Tắc Viết Truyện](#phần-2--chuẩn-v13-gold--quy-tắc-viết-truyện)
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
Bước 2.5: Kiểm `story_dna` và chống trùng cấu trúc giữa các truyện trong batch
   ↓
Bước 3: Viết từng chương đầy đủ (1000-1500 từ/chương, HTML format V13 Gold)
   ↓
Bước 4: Lưu pending_novel.json
   ↓
Bước 5: Dùng ảnh bìa local đã duyệt hoặc ảnh mới tạo bằng ChatGPT Image Generation; tuyệt đối không gọi API sinh ảnh bên thứ ba
   ↓
Bước 6: Áp overlay tràn viền bằng cover_overlay_standard.py
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
- **Viết truyện**: ChatGPT/Codex trong phiên làm việc hoặc model chat đang được người dùng trực tiếp sử dụng — KHÔNG gọi API bên ngoài để bulk-write nội dung truyện.
- **Ảnh bìa**: Dùng ChatGPT Image Generation cho ảnh mới, hoặc dùng trực tiếp ảnh local đã duyệt (`base_cover_14.png` đến `base_cover_63.png` nếu phù hợp) — KHÔNG gọi API sinh ảnh ngoài từ script.
- **Overlay cover**: Script `cover_overlay_standard.py` (Python + Pillow)
- **Publish**: FTP + PHP helper scripts trên WordPress
- **SEO**: PHP script chạy trực tiếp trên server qua FTP upload

### Các file quan trọng:

| File | Đường dẫn | Chức năng |
|------|-----------|-----------|
| Novel concepts | `/Users/aaronnguyen/TN/App/doctieuthuyet/novel_concepts_50.json` | 50 concept truyện chưa viết |
| Cover overlay | `/Users/aaronnguyen/TN/App/doctieuthuyet/cover_overlay_standard.py` | Áp layout card tràn viền lên cover |
| Cover prompt | `/Users/aaronnguyen/TN/App/doctieuthuyet/prompts/cover_prompt_master.md` | Chuẩn thiết kế bìa |
| V13 Gold prompt | `/Users/aaronnguyen/TN/App/doctieuthuyet/prompts/codex/viet-truyen.md` | Prompt văn học mới nhất cho Chat Mode / Schedule Mode |
| Publisher | `/Users/aaronnguyen/TN/App/doctieuthuyet/publish_local_novel.py` | Publish truyện lên WP |
| PHP Helper | `/Users/aaronnguyen/TN/App/doctieuthuyet/publish_novel.php` | Server-side WP publisher |
| PHP Overwriter | `/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/overwrite_story_generic.php` | Ghi đè truyện có sẵn |
| Existing novels | `/Users/aaronnguyen/TN/App/doctieuthuyet/existing_novels.json` | Danh sách truyện đã publish |
| SEO updater | `/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/update_all_rankmath_seo.py` | Bulk SEO RankMath |
| Pipeline doc | `/Users/aaronnguyen/TN/App/doctieuthuyet/prompts/novel_pipeline_master.md` | **FILE NÀY** |

---

## PHẦN 2 — Chuẩn V13 Gold — Quy Tắc Viết Truyện

### Thể loại chính: Sảng Văn / Vả Mặt (Slap-face / Face-slap fiction)

> Pipeline này tối ưu cho thể loại sảng văn/vả mặt đô thị. Các thể loại khác (trọng sinh, cung đấu, xuyên không) xem hướng dẫn chi tiết trong skill `truyen-mang-writer` → `references/genres.md`.

### Cấu trúc truyện chuẩn:
- **Số chương**: 8-15 (tùy độ phức tạp cốt truyện)
- **Độ dài chương**: 1000-1500 từ tiếng Việt (~6000-9000 ký tự)
- **Tiêu đề truyện**: Style clickbait giật gân, gây tò mò
  - VD: "Mẹ Vợ Đòi Sính Lễ 5 Tỷ Khinh Tôi Nghèo, Landmark 81 Là Của Tôi"
  - VD: "Bị Đuổi Khỏi Khách Sạn, Tôi Mua Luôn Chuỗi Năm Sao"

### 7 Quy Tắc Vàng V13 Gold:

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

#### 4. TRÁNH VIẾT TẮT (TRONG NỘI DUNG TRUYỆN)
- ✅ "thành phố Hồ Chí Minh" — KHÔNG "TPHCM"
- ✅ "khu công nghiệp" — KHÔNG "KCN"
- ✅ "ngân hàng thương mại cổ phần ngoại thương Việt Nam" — KHÔNG "Vietcombank" (lần đầu tiên đề cập trong nội dung chương)
- Lý do: Hệ thống regex tách câu tự động cần chạy chuẩn xác
- **Ngoại lệ**: SEO title (dưới 60 ký tự) và slug (dưới 75 ký tự) ĐƯỢC dùng tên viết tắt/thương hiệu ngắn gọn (VD: "Vietcombank", "TPHCM") để đảm bảo không vượt giới hạn ký tự RankMath

#### 5. CẤU TRÚC CỐT TRUYỆN
- **Chương 1-2**: Nhân vật chính bị ức hiếp, nhục mạ, đuổi khỏi vị trí → tạo sự đồng cảm
- **Chương 2-3**: Gặp nữ chính (thường là người có quyền lực/vị trí cao) → thử thách sòng phẳng
- **Chương 3-5**: Vượt qua thử thách bằng tài năng thiên bẩm → bộc lộ năng lực
- **Chương 4-6**: Phản diện tấn công (phá hoại, vu oan, bôi nhọ) → khủng hoảng
- **Chương 5-7**: VẢ MẶT LẦN 1 — Dùng trí tuệ/bằng chứng lật ngược thế cờ
- **Chương 6-9**: Phản diện nâng cấp tấn công (cấu kết thế lực lớn hơn) → khủng hoảng lần 2
- **Chương 8-12**: VẢ MẶT LẦN 2 — Đập tan hoàn toàn phe phản diện, C03 bắt giữ
- **Chương cuối**: Nhân vật chính thắng lợi vinh quang, nữ chính chủ động bày tỏ tình cảm

#### 6. ĐỊNH DẠNG HTML V13 GOLD
- Mỗi câu hoặc nhịp thoại quan trọng nằm trong THẺ `<p>` RIÊNG (V13 paragraph splitting)

#### 7. CHỐNG TEMPLATE HÓA / DUPLICATE CONTENT GIỮA TRUYỆN
- Khi tạo nhiều truyện trong một batch, **không được dùng cùng một khung cảnh rồi thay tên nhân vật, địa danh hoặc ngành nghề**.
- Mỗi truyện phải có `story_dna` riêng trước khi viết:
  - `profession_world`: thế giới nghề nghiệp riêng.
  - `central_evidence`: vật chứng trung tâm riêng, không thể bê sang truyện khác.
  - `unique_set_pieces`: ít nhất 5 cảnh lớn riêng theo ngành.
  - `midpoint_crisis`: khủng hoảng giữa truyện riêng.
  - `relationship_signature`: cách nam nữ chính tương tác riêng.
  - `ending_signature`: đạo cụ/cảnh kết riêng.
- Cấm lặp các cụm/cảnh nhận diện trong cùng batch: "Tôi không cần cô tin tôi", "Nếu chỉ là uất ức", "bánh mì nửa đêm", "bút máy cuối truyện", "Sang chương X", "cuộc chiến bước vào lớp", "Không ăn mừng, không đăng đàn".
- Các cảnh then chốt phải là set-piece cụ thể theo ngành, không được kéo dài bằng chương template. Ví dụ:
  - Gốm: lò nung, sổ lò, mẫu tro, xương men, giám định men.
  - Y tế: điện tâm đồ, log thuốc, men gan, camera phòng trực, hội đồng chuyên môn.
  - Xây dựng: lõi bê tông, GPS xe bồn, nhật ký đổ bê tông, biên bản nghiệm thu.
  - Trà/nông nghiệp: sổ cân lá, dư lượng thuốc cỏ, kho lên men, nông hộ, vùng nguyên liệu.
- Trước khi lưu/publish, chạy cross-story audit: chọn 5-10 cụm đặc trưng dài trên 5 từ và kiểm xem có lặp ở truyện khác không. Nếu có, viết lại trước khi đăng.
- Chỉ dùng: `<p>`, `<strong>`, `<em>` — không dùng thẻ khác
- Đoạn mở đầu truyện (intro) BẮT BUỘC dùng: `<p><strong>"Trích dẫn kịch tính..."</strong></p>`

#### 8. NHẤT QUÁN TÊN NHÂN VẬT XUYÊN SUỐT
- ❌ TUYỆT ĐỐI KHÔNG: Cùng 1 nhân vật mà đổi tên giữa các chương (VD: mẹ chồng lúc "bà Hạnh" lúc "bà Hương", chị chồng lúc "Ngọc" lúc "Thúy")
- ✅ BẮT BUỘC: Lập danh sách nhân vật (character sheet) với tên đầy đủ TRƯỚC khi viết chương 1. Giữ nguyên xuyên suốt toàn bộ truyện.
- ✅ Sau khi viết xong, chạy audit kiểm tra: grep tên nhân vật chính/phụ xem có mâu thuẫn không.

#### 9. KHÔNG LỘ DẤU HIỆU AI / META-NARRATIVE
- ❌ TUYỆT ĐỐI KHÔNG:
  - Viết "nhân vật chính", "câu chuyện [tên truyện]", "Sang chương X" trong nội dung truyện
  - Đoạn template lộ ra giữa chương (VD: "Đến đoạn này, không ai trong phòng cần nghe thêm thuật ngữ...")
  - Đoạn mô tả meta như "cốt truyện bước vào giai đoạn mới", "đây là bước ngoặt"
  - Lặp nguyên đoạn giống nhau ở nhiều chương (copy-paste nội bộ)
- ✅ Truyện phải đọc tự nhiên như do người viết, KHÔNG có dấu hiệu AI-generated
- ✅ Mỗi chương phải tiến triển cốt truyện rõ ràng — KHÔNG lặp lại cùng 1 tình huống

#### 10. TỔ CHỨC / CƠ QUAN / NGÂN HÀNG PHẢI THẬT
- ❌ TUYỆT ĐỐI KHÔNG: Dùng tên tổ chức hư cấu (VD: "Việt Thương Bank", "Tập đoàn Thịnh Vương", "Đại học Minh Đức")
- ✅ BẮT BUỘC dùng tên THẬT, có thể xác minh:
  - Ngân hàng: Vietcombank, Techcombank, Agribank, MB Bank, VPBank, BIDV, Sacombank, TPBank, ACB
  - Tập đoàn: Vingroup, Hòa Phát, FPT, Masan, Novaland, TH Group, Thaco
  - Đại học: Đại học Bách Khoa, Đại học Y Hà Nội, Đại học Kinh tế thành phố Hồ Chí Minh
  - Bệnh viện: Bệnh viện Chợ Rẫy, Bệnh viện Bạch Mai, Bệnh viện Đa khoa Trung ương Huế
  - Khu đô thị: Vinhomes, Ecopark, Ciputra, Phú Mỹ Hưng, Sala
- **Ngoại lệ**: Nếu cốt truyện cần nhân vật phản diện là chủ doanh nghiệp, ĐƯỢC dùng tên công ty hư cấu cho công ty phản diện — nhưng vẫn phải dùng tên ngân hàng/cơ quan nhà nước thật.

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

### Bước 1: Chọn hoặc tạo ảnh bìa
- Ưu tiên ảnh mới tạo bằng **ChatGPT Image Generation** từ `cover_prompt` tiếng Anh của truyện, sau đó lưu PNG local và preview trước khi upload.
- Có thể dùng ảnh local đã duyệt sẵn trong workspace nếu phù hợp với truyện.
- Các file `base_cover_{idx}.png` chỉ là nguồn local/fallback đã duyệt, không phải lý do để gọi lại API sinh ảnh ngoài.
- ❌ **TUYỆT ĐỐI KHÔNG** gọi Pollinations, Imagen API, hoặc API sinh ảnh bên thứ ba trong script/pipeline.

### Bước 2: Apply overlay (cover_overlay_standard.py)
- Input: ảnh PNG local đã duyệt + title + subtitle
- Output: 2000x2000 PNG (`pending_cover.png`) với:
  - Top dark gradient (RGBA 0,0,0,200 → transparent)
  - Bottom dark gradient (RGBA 0,0,0,80 → transparent)
  - Căn lề tràn viền hoàn toàn (Full-bleed), không có khung hay viền mạ vàng
  - Tiêu đề in HOA tự động chia 3 dòng phối khối màu sắc nét (Trắng - Đỏ - Vàng) kèm drop shadow & stroke đen cực dày
  - Phụ đề trắng mờ kèm stroke đen nổi bật trên mọi hậu cảnh
  - TUYỆT ĐỐI KHÔNG vẽ chapter badge, view count (mắt 👁), hay clock (đồng hồ 🕒) trực tiếp lên ảnh bìa (bởi vì giao diện động của theme WordPress sẽ tự hiển thị các thông tin này).

### Bước 3: Save
- Lưu output thành `pending_cover.png` (root thư mục project)

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
Sau khi publish, cập nhật RankMath postmeta và thuộc tính bài viết:
- `_rank_math_title` / `rank_math_title` — SEO title (BẮT BUỘC dưới 60 ký tự để thanh RankMath hiển thị XANH, ví dụ: `<Tên ngắn gọn của truyện> Vả Sập Kẻ Phản Bội` hoặc `<Tên ngắn gọn của truyện> Lật Kèo Phản Bội`).
- `post_name` (Slug / Liên kết cố định) — Đường dẫn tĩnh (BẮT BUỘC dưới 75 ký tự, ví dụ: `bac-si-dong-y-bi-duoi-khoi-vien-phoi-va-sap-tap-doan` thay vì dùng toàn bộ tiêu đề 125 ký tự để thanh RankMath hiển thị XANH).
- `_rank_math_description` / `rank_math_description` — Description (trích từ <strong> block, dưới 160 ký tự, hiển thị XANH).
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

> **Lưu ý bảo mật**: Credentials được hardcode trong các script Python (`publish_local_novel.py`, `auto_novel_generator.py`...). Không share file này ra ngoài repo private.

```
FTP_HOST     = "51.79.53.190"
FTP_USER     = "alotoinghe"
FTP_PASS     = "Nghia234!"
WP_URL       = "https://doctieuthuyet.com"
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
2. Viết `story_dna` riêng cho truyện đó trước khi viết chương
3. Viết dàn ý chi tiết cho từng chương, bảo đảm các cảnh then chốt là set-piece riêng theo ngành
4. Viết NỘI DUNG TỪNG CHƯƠNG (tối thiểu 1000 từ/chương, mục tiêu 1000-1500 từ/chương, V13 Gold format)
5. Chạy audit chống duplicate trong batch: kiểm cụm/cảnh/đạo cụ lặp, đặc biệt giữa các truyện cùng file duyệt
6. Nếu audit báo lặp cấu trúc/câu thoại/cảnh đạo cụ, viết lại trước khi tạo payload đăng
7. Lưu JSON truyện vào `scratch/` để người dùng duyệt trước
8. Sau khi người dùng duyệt mới tạo/gắn cover và publish
9. Lấy ảnh bìa gốc đã duyệt hoặc ảnh ChatGPT Image Generation local
10. Chạy `cover_overlay_standard.py` → tạo `pending_cover.png`
11. Chạy publisher tương ứng sau khi được duyệt
12. Xác nhận publish thành công

**Bước 6**: Sau khi xong batch và đã được duyệt/publish, chạy `update_all_rankmath_seo.py`

**Bước 7**: Báo cáo kết quả cho user

### Lưu ý quan trọng:
- Dùng ChatGPT/Codex trong phiên làm việc hoặc model chat đang được người dùng trực tiếp dùng để viết chương; không gọi API bên ngoài để bulk-write nội dung truyện.
- Dùng ảnh bìa local đã duyệt hoặc ảnh mới tạo bằng ChatGPT Image Generation; không gọi API sinh ảnh ngoài trong script/pipeline.
- Mỗi truyện xử lý tuần tự.
- Kiểm tra word count tối thiểu 1000 từ/chương, mục tiêu 1000-1500 từ/chương trước khi lưu.
- Luôn chạy audit chống duplicate/copy-paste nội bộ trước khi trình duyệt hoặc đăng.
- Chỉ cập nhật `existing_novels.json` sau mỗi truyện publish thành công.
