# Chapter 011 Context Evidence

- story_bible.md SHA256: `886211f0fa5c15b06a93d7b3cffec03b08d2ad4aa834ca56ec4adef8c214a747`
- writer_contract.md SHA256: `5cb18d4f8717fc27d7f80fd292488adbac19bf5bb542ecea39cf7a9e527a6df9`
- master_manifest.json SHA256: `248444c17a82984f967c4d23570156161a22da31744f4e181e903bf56e787c13`
- continuity/ledger.json SHA256: `fc86a47e4f4a70d64bed50ecf688671e0542b56f179a74f2dbcc2ec9611b7212`
- latest block review: `none`

## Manifest record
```json
{
  "chapter": 11,
  "volume": 1,
  "volume_title": "Thiên Hạ Sao Yếu Vậy?",
  "subarc": "V01A2",
  "subarc_title": "Không Phải Ta Mạnh",
  "title": "Chương 11: Không Phải Ta Mạnh — Mở Cửa",
  "title_status": "provisional_until_batch_draft",
  "beat_function": "setup",
  "objective": "Thiết lập tình trạng mới và mục tiêu cụ thể của sub-arc; dùng opening làm set-piece đầu. Trọng tâm riêng chương: Tiểu Bảo gia nhập thương đội.",
  "conflict": "Thương đội bị cướp tu sĩ; hắn muốn trốn nhưng không chịu nhìn trẻ con bị giết.",
  "character_beat": "Chưa romance; định hình giới hạn đạo đức của main.",
  "mystery_beat": "Linh khí vào người biến mất; nồi đen phản ứng với linh thạch.",
  "power_guardrail": "Lần đầu thử Dẫn Khí thất bại trên bề mặt; sức thân thể đánh văng Dẫn Khí cao tầng.",
  "foreshadow_or_payoff": "Linh khí vào người biến mất; nồi đen phản ứng với linh thạch.",
  "cliffhanger_type": "arrival",
  "status": "planned",
  "draft_file": "chapters/chapter_011.md"
}
```

## Current state
```json
{
  "ta_tieu_bao": {
    "age": 13,
    "cultivation": "chưa nhập Dẫn Khí; thử cảm khí thất bại trên bề mặt",
    "location": "đoàn xe Tống Ký, gần Hắc Nha Pha trên đường Thanh Hà",
    "injuries": [],
    "inventory": [
      "ba đồng tiền cũ",
      "dao cũ đã mài",
      "nồi đen gia cố quai",
      "quần áo",
      "thuốc bà Mạnh",
      "muối",
      "ít bánh/thịt khô còn lại"
    ],
    "relationship_with_thanh_nghi": "chưa gặp",
    "known_truths": [
      "Lạc Kê vẫn là nhà dù hắn rời đi",
      "người ngoài có hệ Dẫn Khí/Khai Mạch/Trúc Đài",
      "linh thạch là tiền của tu sĩ",
      "tu sĩ có thể dùng phù/pháp khí",
      "bản thân chưa cảm được linh khí theo cách thông thường"
    ]
  },
  "luc_thanh_nghi": {
    "age": 17,
    "cultivation": "Thiên tài kiếm đạo, chi tiết cảnh giới sẽ khóa khi xuất hiện",
    "location": "ngoài màn truyện",
    "injuries": [],
    "relationship_with_tieu_bao": "chưa gặp",
    "known_truths": [
      "mình thuộc Lục gia",
      "mình được gia tộc kỳ vọng như kiếm tu thiên tài"
    ]
  },
  "o_gia": {
    "state": "gà đen, huyết mạch bị khóa; tự ý theo Tiểu Bảo ra khỏi Lạc Kê",
    "location": "cùng Tiểu Bảo ở đoàn xe Tống Ký",
    "speech": false
  }
}
```

## Unresolved hooks
```json
[
  {
    "id": "H001",
    "seed_range": "1-10",
    "question": "Dân Lạc Kê thật sự là ai?",
    "reveal_target": "601-650",
    "status": "planned"
  },
  {
    "id": "H002",
    "seed_range": "1-20",
    "question": "Vì sao việc nhà Lạc Kê giống đại đạo?",
    "reveal_target": "301-350/601-650",
    "status": "planned"
  },
  {
    "id": "H003",
    "seed_range": "3-19",
    "question": "Cái nồi đen là gì?",
    "reveal_target": "97/580+/620+",
    "status": "planned"
  },
  {
    "id": "H004",
    "seed_range": "10-100",
    "question": "Vì sao linh khí vào người Tiểu Bảo biến mất?",
    "reveal_target": "98/150+/580+",
    "status": "planned"
  },
  {
    "id": "H005",
    "seed_range": "47-100",
    "question": "Vì sao đá linh căn phản ứng dị thường?",
    "reveal_target": "580+",
    "status": "planned"
  },
  {
    "id": "H006",
    "seed_range": "79-200",
    "question": "Ai đang theo dõi Tiểu Bảo?",
    "reveal_target": "191-200",
    "status": "planned"
  },
  {
    "id": "H007",
    "seed_range": "98",
    "question": "Nhân Gian Lô là gì?",
    "reveal_target": "580/620/760",
    "status": "planned"
  },
  {
    "id": "H008",
    "seed_range": "125-350",
    "question": "Vì sao người Lạc Kê xuất hiện trong di tích cổ?",
    "reveal_target": "325/601-650",
    "status": "planned"
  },
  {
    "id": "H009",
    "seed_range": "201-250",
    "question": "Quá khứ Mộc Vô Nhai và sai lầm 'vì đại cục' là gì?",
    "reveal_target": "231-240",
    "status": "planned"
  },
  {
    "id": "H010",
    "seed_range": "401-500",
    "question": "Thiên Môn thu hoạch gì và cho ai?",
    "reveal_target": "431-500",
    "status": "planned"
  },
  {
    "id": "H011",
    "seed_range": "451-600",
    "question": "Tại sao Thiên Mệnh Điện cần thu hoạch các giới?",
    "reveal_target": "571-590",
    "status": "planned"
  },
  {
    "id": "H012",
    "seed_range": "501-700",
    "question": "Thiên Ngoại là gì?",
    "reveal_target": "691-710",
    "status": "planned"
  },
  {
    "id": "H013",
    "seed_range": "601-640",
    "question": "Cha mẹ Tiểu Bảo là ai và vì sao hắn thành Nhân Gian Lô?",
    "reveal_target": "621-640",
    "status": "planned"
  },
  {
    "id": "H014",
    "seed_range": "651-700",
    "question": "Cửu Thiên từng là gì và vì sao bị chia?",
    "reveal_target": "681-700",
    "status": "planned"
  },
  {
    "id": "H015",
    "seed_range": "741-770",
    "question": "Reset Cửu Thiên phải trả giá gì?",
    "reveal_target": "761-770",
    "status": "planned"
  }
]
```

## Required previous five full-chapter sources
- Ch006: `chapters/chapter_006.md` — `1251b763e7d9b28b3563c22b2981fff95f483c2d79c218bc5f5af276a59f4af0` — # Chương 6: Ba Đồng Tiền
- Ch007: `chapters/chapter_007.md` — `0990324ef90bb047e11e431a4f7629d6a003d448a35fabe7ea14b5243da7e7fd` — # Chương 7: Con Gà Tự Đi Theo
- Ch008: `chapters/chapter_008.md` — `d8538478185ebd10e36e42eabd21dfa80ffcda3e06b00ef58bbc62a5e66c2885` — # Chương 8: Người Tu Tiên Đầu Tiên
- Ch009: `chapters/chapter_009.md` — `89b16e330b7c9cae28c41234c8657347a477cfe261ab28e82316422ead81f597` — # Chương 9: Tu Tiên Thật Đáng Sợ
- Ch010: `chapters/chapter_010.md` — `5a6ffcded63ed191c96e4b844639466c47792150a10f1c971ddef8822d98e362` — # Chương 10: Ước Mơ Mới Của Tạ Tiểu Bảo

## Pre-draft review fields
- Current location/time: Gần nửa đêm, trại tạm của đoàn Tống Ký ngay trước Hắc Nha Pha trên đường tới Thanh Hà; Ch10 vừa kết bằng ba mũi tên lửa và cướp tu sĩ xuất hiện.
- Character states: Tiểu Bảo 13 tuổi, chưa nhập Dẫn Khí và vừa thử cảm khí thất bại; đang làm chân chạy cho Tống Ký với tiền công 300 đồng, mang 3 đồng cũ, dao, nồi đen, thuốc và ít lương khô. Ô Kê đi cùng. Hà thúc là hộ vệ; Chu tiên sinh là tu sĩ trẻ dùng phù/kiếm khí; Tống phu nhân chỉ huy đoàn.
- Must be new in this chapter: Lần đầu Tiểu Bảo đối diện bạo lực có tổ chức do người gây ra và phải tham gia bảo vệ người khác; cho thấy năng lực quan sát/ứng biến chứ chưa bùng toàn bộ sức mạnh. Thương đội chính thức coi hắn là người cùng phe trong khủng hoảng.
- Motifs/scenes NOT to repeat from previous five: Không mở bằng Ô Kê ăn vụng; không mặc cả giá đồ; không giải thích lại Dẫn Khí/linh thạch; không hồi tưởng chia tay Lạc Kê; không dùng cảnh “Tiểu Bảo làm việc thường nhưng quá khỏe” làm payoff chính; không lặp câu hỏi có mất tiền không.
- Intended state change: Đoàn Tống Ký từ hành trình thương mại chuyển sang trạng thái bị phục kích; Tiểu Bảo từ khách/nhân công tạm thời thành người chủ động giữ một tuyến bảo vệ dân thường và hàng hóa.
- Intended cliffhanger/payoff: Sau đợt tấn công đầu, phe cướp ném bình khói xám làm linh khí của tu sĩ trong đoàn bị trì trệ; mở cửa cho anomaly Ch12.
- Confirmation: story bible + writer contract + manifest + ledger + all five prior chapters Ch006–Ch010 were read in full before drafting: CONFIRMED 2026-09-16

> This file is evidence/checklist only. It does not replace actually reading the referenced sources.
