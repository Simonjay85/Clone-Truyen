# Chapter 021 Context Evidence

- story_bible.md SHA256: `886211f0fa5c15b06a93d7b3cffec03b08d2ad4aa834ca56ec4adef8c214a747`
- writer_contract.md SHA256: `5cb18d4f8717fc27d7f80fd292488adbac19bf5bb542ecea39cf7a9e527a6df9`
- master_manifest.json SHA256: `a63ccb2ac3c055f6f7a43c4e83edc3bc09c3dc260beaf835b117528e5bded5b0`
- continuity/ledger.json SHA256: `ae11366f4e7839d157304d96e706c98e92e9d41cfa09cb8c7ac8eb1635f6ec53`
- latest block review: `none`

## Manifest record
```json
{
  "chapter": 21,
  "volume": 1,
  "volume_title": "Thiên Hạ Sao Yếu Vậy?",
  "subarc": "V01A3",
  "subarc_title": "Tiền Mới Là Đại Đạo",
  "title": "Chương 21: Tiền Mới Là Đại Đạo — Mở Cửa",
  "title_status": "provisional_until_batch_draft",
  "beat_function": "setup",
  "objective": "Thiết lập tình trạng mới và mục tiêu cụ thể của sub-arc; dùng opening làm set-piece đầu. Trọng tâm riêng chương: Tiểu Bảo trả phí vào thành và đau như mất thịt.",
  "conflict": "Tiểu Bảo nghèo, thiếu kiến thức, Ô Gia ăn vụng linh dược.",
  "character_beat": "Thoáng thấy Thanh Nghi lần đầu nhưng chưa tương tác.",
  "mystery_beat": "Linh dược Lạc Kê bị thương nhân nhận ra là hàng hiếm; nguồn gốc làng càng khả nghi với độc giả.",
  "power_guardrail": "Main chưa giữ được linh khí nhưng phản xạ/thể lực tiếp tục phi lý.",
  "foreshadow_or_payoff": "Linh dược Lạc Kê bị thương nhân nhận ra là hàng hiếm; nguồn gốc làng càng khả nghi với độc giả.",
  "cliffhanger_type": "arrival",
  "status": "planned",
  "draft_file": "chapters/chapter_021.md"
}
```

## Current state
```json
{
  "ta_tieu_bao": {
    "age": 13,
    "cultivation": "chưa nhập Dẫn Khí; thử cảm khí thất bại trên bề mặt",
    "location": "Thanh Hà Thành, quảng trường Đông Hà",
    "injuries": [
      "tay phải đang lành",
      "sườn phải bầm sâu/căng cơ, chưa gãy; hạn chế vận động mạnh 3 ngày",
      "vết rạch vai nông đã xử lý"
    ],
    "inventory": [
      "dao cũ đã mài",
      "nồi đen gia cố quai",
      "quần áo",
      "thuốc bà Mạnh",
      "muối",
      "ít bánh/thịt khô còn lại",
      "mảnh linh thạch nhỏ đã mờ linh quang",
      "mẫu Tán Linh Tán và mảnh phù/gốm dấu chim một cánh",
      "sợi dây thép",
      "túi trữ vật cấp thấp chưa dùng được",
      "ba đồng tiền cũ giữ riêng",
      "300 đồng tiền công mới",
      "địa chỉ Tống Ký Thanh Hà"
    ],
    "relationship_with_thanh_nghi": "chưa gặp",
    "known_truths": [
      "Lạc Kê vẫn là nhà dù hắn rời đi",
      "người ngoài có hệ Dẫn Khí/Khai Mạch/Trúc Đài",
      "linh thạch là tiền của tu sĩ",
      "tu sĩ có thể dùng phù/pháp khí",
      "bản thân chưa cảm được linh khí theo cách thông thường",
      "Tán Linh Tán áp chế tu sĩ nhưng gần như không tác dụng lên bản thân",
      "linh lực ngoại lai chạm vào cơ thể bản thân có thể biến mất không rõ nguyên nhân",
      "Thái Huyền Tông sẽ sơ tuyển tại Thanh Hà sau ba ngày; sơ trắc miễn phí"
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
    "location": "cùng Tiểu Bảo tại Thanh Hà Thành",
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
- Ch016: `chapters/chapter_016.md` — `6587c02af6c17ce508e83f207de8ace6d039d05cf5f0e5d22f90dbe0afaa81bb` — # Chương 16: Không Thể Đi Như Cũ
- Ch017: `chapters/chapter_017.md` — `8e3f1fcbe71c44ef44570ba6048fa42cc78a05ee6aa4f4d7d8076ff1ea525d99` — # Chương 17: Đổi Cách Chơi
- Ch018: `chapters/chapter_018.md` — `3ab28df1fc3fddf2c962e7d4bec3aab9d25a7ab2dcafd7a5d313b97313aa7ab2` — # Chương 18: Người Đứng Cạnh
- Ch019: `chapters/chapter_019.md` — `5873db5dd8a29e36765157932dde749b7547a260da0b73106b7f23cf0f5b0604` — # Chương 19: Túi Trữ Vật Đầu Tiên
- Ch020: `chapters/chapter_020.md` — `fbb4ce3e185a5723de81915e2a487fff1be81fe31a182c93f3c85480d909a3a5` — # Chương 20: Thanh Hà Thành

## Pre-draft review fields
- Current location/time: FILL_AFTER_READING
- Character states: FILL_AFTER_READING
- Must be new in this chapter: FILL_AFTER_READING
- Motifs/scenes NOT to repeat from previous five: FILL_AFTER_READING
- Intended state change: FILL_AFTER_READING
- Intended cliffhanger/payoff: FILL_AFTER_READING
- Confirmation: story bible + writer contract + manifest + ledger + all five prior chapters were read in full before drafting: PENDING

> This file is evidence/checklist only. It does not replace actually reading the referenced sources.
