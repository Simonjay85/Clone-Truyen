# Chapter 012 Context Evidence

- story_bible.md SHA256: `886211f0fa5c15b06a93d7b3cffec03b08d2ad4aa834ca56ec4adef8c214a747`
- writer_contract.md SHA256: `5cb18d4f8717fc27d7f80fd292488adbac19bf5bb542ecea39cf7a9e527a6df9`
- master_manifest.json SHA256: `d9cf6d581296348e9f8d4fb0f40720e4c5e0a14faeed05c418bf8c227342c021`
- continuity/ledger.json SHA256: `01f7ad6f11404deea2cdfdd84fa012fece6c2a957bf12db29a8a3484607ce77f`
- latest block review: `none`

## Manifest record
```json
{
  "chapter": 12,
  "volume": 1,
  "volume_title": "Thiên Hạ Sao Yếu Vậy?",
  "subarc": "V01A2",
  "subarc_title": "Không Phải Ta Mạnh",
  "title": "Chương 12: Không Phải Ta Mạnh — Một Việc Không Đúng",
  "title_status": "provisional_until_batch_draft",
  "beat_function": "complication",
  "objective": "Đưa chi tiết lệch chuẩn đầu tiên khiến kế hoạch ban đầu khó hơn; conflict phải hiện thành hành động. Trọng tâm riêng chương: Thương đội bị cướp tu sĩ; hắn muốn trốn nhưng không chịu nhìn trẻ con bị giết.",
  "conflict": "Thương đội bị cướp tu sĩ; hắn muốn trốn nhưng không chịu nhìn trẻ con bị giết.",
  "character_beat": "Chưa romance; định hình giới hạn đạo đức của main.",
  "mystery_beat": "Linh khí vào người biến mất; nồi đen phản ứng với linh thạch.",
  "power_guardrail": "Lần đầu thử Dẫn Khí thất bại trên bề mặt; sức thân thể đánh văng Dẫn Khí cao tầng.",
  "foreshadow_or_payoff": "Giữ continuity; không reveal ngoài mốc sub-arc.",
  "cliffhanger_type": "anomaly",
  "status": "planned",
  "draft_file": "chapters/chapter_012.md"
}
```

## Current state
```json
{
  "ta_tieu_bao": {
    "age": 13,
    "cultivation": "chưa nhập Dẫn Khí; thử cảm khí thất bại trên bề mặt",
    "location": "đoàn Tống Ký trước Hắc Nha Pha, đang bị cướp tu sĩ phục kích",
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
      "bản thân chưa cảm được linh khí theo cách thông thường",
      "Tán Linh Tán áp chế tu sĩ nhưng gần như không tác dụng lên bản thân"
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
    "location": "cùng Tiểu Bảo tại Hắc Nha Pha",
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
- Ch007: `chapters/chapter_007.md` — `0990324ef90bb047e11e431a4f7629d6a003d448a35fabe7ea14b5243da7e7fd` — # Chương 7: Con Gà Tự Đi Theo
- Ch008: `chapters/chapter_008.md` — `d8538478185ebd10e36e42eabd21dfa80ffcda3e06b00ef58bbc62a5e66c2885` — # Chương 8: Người Tu Tiên Đầu Tiên
- Ch009: `chapters/chapter_009.md` — `89b16e330b7c9cae28c41234c8657347a477cfe261ab28e82316422ead81f597` — # Chương 9: Tu Tiên Thật Đáng Sợ
- Ch010: `chapters/chapter_010.md` — `5a6ffcded63ed191c96e4b844639466c47792150a10f1c971ddef8822d98e362` — # Chương 10: Ước Mơ Mới Của Tạ Tiểu Bảo
- Ch011: `chapters/chapter_011.md` — `18b5153559021cdac0855045af345f48ae5129da938732e7d40c560f7e5b6ed3` — # Chương 11: Hắc Nha Pha Mở Cửa

## Pre-draft review fields
- Current location/time: Đêm ngày 4, giữa cuộc phục kích Hắc Nha Pha; Tán Linh Tán vừa phủ đoàn xe, tu sĩ Tống Ký suy yếu trong khi phe cướp đã chuẩn bị thuốc giải.
- Character states: Tiểu Bảo chưa nhập Dẫn Khí, vừa nhận ra Tán Linh Tán gần như không tác dụng lên mình; không bị thương. Hà thúc và Chu tiên sinh suy giảm linh lực. Tống phu nhân đang tổ chức rút dân thường/hàng quan trọng. Ô Kê ở cạnh Tiểu Bảo.
- Must be new in this chapter: Cụ thể hóa anomaly cơ thể Tiểu Bảo bằng tương tác trực tiếp với linh lực của một kẻ Dẫn Khí; cho thấy linh lực xâm nhập rồi biến mất, nhưng không gọi tên Nhân Gian Lô hay giải thích cơ chế.
- Motifs/scenes NOT to repeat from previous five: Không thêm set-piece tên lửa/cứu xe; không lặp bài học linh thạch/tu sĩ; không dùng tiền làm punchline; không lặp “giữ xe bằng sức”; không dùng Ô Kê làm comic engine.
- Intended state change: Phe cướp nhận ra Tiểu Bảo là biến số bất thường; Tiểu Bảo biết “không cảm được linh khí” không đồng nghĩa cơ thể hoàn toàn không tương tác với linh khí.
- Intended cliffhanger/payoff: Một tên Dẫn Khí đẩy linh lực vào tay Tiểu Bảo, luồng lực biến mất không dấu; kẻ đó hoảng hốt gọi đồng bọn tập trung vào hắn.
- Confirmation: story bible + writer contract + manifest + ledger + all five prior chapters Ch007–Ch011 were read in full before drafting: CONFIRMED 2026-09-16

> This file is evidence/checklist only. It does not replace actually reading the referenced sources.
