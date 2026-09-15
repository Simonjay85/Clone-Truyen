# Chapter 017 Context Evidence

- story_bible.md SHA256: `886211f0fa5c15b06a93d7b3cffec03b08d2ad4aa834ca56ec4adef8c214a747`
- writer_contract.md SHA256: `5cb18d4f8717fc27d7f80fd292488adbac19bf5bb542ecea39cf7a9e527a6df9`
- master_manifest.json SHA256: `fb94dfbb6885218f586f280e59f88bd27ae0a75c035ad2f79d2a8addf1afaf88`
- continuity/ledger.json SHA256: `be45f0aa6a25097d25cd097f29bcc521a8bf46af2270a967f02c799f3f05042e`
- latest block review: `none`

## Manifest record
```json
{
  "chapter": 17,
  "volume": 1,
  "volume_title": "Thiên Hạ Sao Yếu Vậy?",
  "subarc": "V01A2",
  "subarc_title": "Không Phải Ta Mạnh",
  "title": "Chương 17: Không Phải Ta Mạnh — Đổi Cách Chơi",
  "title_status": "provisional_until_batch_draft",
  "beat_function": "counterplan",
  "objective": "Nhân vật dùng điều đã học để thiết kế cách phản công mới; không deus ex machina. Trọng tâm riêng chương: Cho Tiểu Bảo va vào chuẩn sức mạnh bên ngoài.",
  "conflict": "Thương đội bị cướp tu sĩ; hắn muốn trốn nhưng không chịu nhìn trẻ con bị giết.",
  "character_beat": "Chưa romance; định hình giới hạn đạo đức của main.",
  "mystery_beat": "Linh khí vào người biến mất; nồi đen phản ứng với linh thạch.",
  "power_guardrail": "Lần đầu thử Dẫn Khí thất bại trên bề mặt; sức thân thể đánh văng Dẫn Khí cao tầng.",
  "foreshadow_or_payoff": "Giữ continuity; không reveal ngoài mốc sub-arc.",
  "cliffhanger_type": "plan",
  "status": "planned",
  "draft_file": "chapters/chapter_017.md"
}
```

## Current state
```json
{
  "ta_tieu_bao": {
    "age": 13,
    "cultivation": "chưa nhập Dẫn Khí; thử cảm khí thất bại trên bề mặt",
    "location": "lối mỏ cũ phía tây Hắc Nha Pha",
    "injuries": [
      "lòng bàn tay phải đã băng",
      "chấn thương sườn phải còn đau"
    ],
    "inventory": [
      "ba đồng tiền cũ",
      "dao cũ đã mài",
      "nồi đen gia cố quai",
      "quần áo",
      "thuốc bà Mạnh",
      "muối",
      "ít bánh/thịt khô còn lại",
      "mảnh linh thạch nhỏ đã mờ linh quang",
      "mẫu Tán Linh Tán và mảnh phù/gốm dấu chim một cánh",
      "sợi dây thép"
    ],
    "relationship_with_thanh_nghi": "chưa gặp",
    "known_truths": [
      "Lạc Kê vẫn là nhà dù hắn rời đi",
      "người ngoài có hệ Dẫn Khí/Khai Mạch/Trúc Đài",
      "linh thạch là tiền của tu sĩ",
      "tu sĩ có thể dùng phù/pháp khí",
      "bản thân chưa cảm được linh khí theo cách thông thường",
      "Tán Linh Tán áp chế tu sĩ nhưng gần như không tác dụng lên bản thân",
      "linh lực ngoại lai chạm vào cơ thể bản thân có thể biến mất không rõ nguyên nhân"
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
- Ch012: `chapters/chapter_012.md` — `fb55112c85aa48b987b89b7b9727c5e5b018fd08b9e779b28ab07a295687f558` — # Chương 12: Có Một Việc Không Đúng
- Ch013: `chapters/chapter_013.md` — `4dc674699332af2ceb87e668d470f55a72424ce203177c1d80ac3bd3581ecfa8` — # Chương 13: Giá Của Một Lựa Chọn
- Ch014: `chapters/chapter_014.md` — `711a136e1860d490111063680cb5899361a9fc0c4f38e4c3ee9c016e6d62f6c8` — # Chương 14: Dấu Vết Trong Cái Nồi
- Ch015: `chapters/chapter_015.md` — `a6f18ef1809ad6f375d5ff92430c3f955dc5e5f17ebbafa689ba0c7836ad01a1` — # Chương 15: Một Cái Tát
- Ch016: `chapters/chapter_016.md` — `6587c02af6c17ce508e83f207de8ace6d039d05cf5f0e5d22f90dbe0afaa81bb` — # Chương 16: Không Thể Đi Như Cũ

## Pre-draft review fields
- Current location/time: Rạng sáng ngày 5, đoàn Tống Ký vừa bỏ xe/hàng và bước vào lối mỏ cũ phía tây Hắc Nha Pha; cầu gỗ sau lưng đã sập.
- Character states: Tiểu Bảo chưa Dẫn Khí, tay phải băng, sườn phải đau; giữ dấu vết chim một cánh/Tán Linh Tán/mảnh linh thạch/nồi đen. Tống phu nhân còn 5 hộp; mất 1 hộp do nội gián Phùng Mộc. Chu hồi linh lực chậm, Hà bị thương. Tề Hạc đã được phe cướp cứu.
- Must be new in this chapter: Counterplan dựa trên địa hình mỏ: đọc luồng gió/tiếng vọng/đường ray cũ để không đi đúng tuyến Phùng Mộc muốn; dùng xe goòng bỏ hoang + đá làm mồi âm thanh kéo phục kích sang nhánh sai, đồng thời lần dấu dầu/chim để xác định Phùng Mộc chưa ra khỏi mỏ.
- Motifs/scenes NOT to repeat from previous five: Không one-shot ai; không dùng anomaly linh lực làm giải pháp; không điều tra nồi; không moral-choice beat; không thêm mất hàng lớn thứ hai; không chạy running gag.
- Intended state change: Đoàn từ bị động chạy vào mỏ chuyển sang chủ động che dấu hướng di chuyển; phát hiện Phùng Mộc/hộp đang ở khu bốc quặng cũ, chưa thoát. Tống phu nhân cho phép một nhóm nhỏ trinh sát thay vì cả đoàn lao theo.
- Intended cliffhanger/payoff: Mồi xe goòng kéo phần lớn phục kích đi sai nhánh; ở cuối nhánh thông gió, Tiểu Bảo nghe giọng Phùng Mộc và một người lạ đang nói về “giao hộp trước khi trời sáng”.
- Confirmation: story bible + writer contract + manifest + ledger + all five prior chapters Ch012–Ch016 were read in full / authored-and-reviewed in the active loop before drafting: CONFIRMED 2026-09-16

> This file is evidence/checklist only. It does not replace actually reading the referenced sources.
