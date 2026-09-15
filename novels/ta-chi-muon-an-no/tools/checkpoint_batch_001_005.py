#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'planning' / 'master_manifest.json'
LEDGER = ROOT / 'continuity' / 'ledger.json'

entries = {
    1: {
        'pov':'Tạ Tiểu Bảo','start_location':'nhà Tiểu Bảo, Lạc Kê Thôn','end_location':'Lạc Kê Thôn',
        'cultivation_changes':'none; thể lực/thân pháp bắt gà chỉ được show, không đặt tên cảnh giới','injuries':[],
        'inventory_changes':[],'relationship_beat':'thiết lập Lạc Kê là gia đình và nơi thuộc về',
        'knowledge_gained':['Tiểu Bảo biết ngày mai sinh nhật 13 tuổi, không biết kế hoạch rời làng'],
        'hooks_opened':['H001','H002'],'hooks_paid':[],
        'foreshadow_seeds':['Ô Gia có vệt đỏ trong mắt','dân làng đồng loạt phản ứng với tuổi mười ba'],
        'next_immediate_objective':'hoàn tất việc nhà và sinh nhật'
    },
    2: {
        'pov':'Tạ Tiểu Bảo','start_location':'đường suối/làng','end_location':'nhà Tiểu Bảo',
        'cultivation_changes':'none; thế chẻ củi cho thấy lực và độ chính xác phi chuẩn','injuries':[],
        'inventory_changes':['nhận hai cân xương có thịt; nấu bằng nồi đen'],
        'relationship_beat':'Thôi Đại Tráng biểu lộ quan tâm bằng việc làm hơn lời nói',
        'knowledge_gained':['Tiểu Bảo vẫn tin phiến đá chỉ là đá mục'],
        'hooks_opened':['H002','H003'],'hooks_paid':[],
        'foreshadow_seeds':['khách Trúc Cơ sợ đường rìu','nồi đen tự giữ ấm/rung nhẹ'],
        'next_immediate_objective':'chuẩn bị sinh nhật ngày mai'
    },
    3: {
        'pov':'Tạ Tiểu Bảo','start_location':'Lạc Kê Thôn','end_location':'nhà Tiểu Bảo',
        'cultivation_changes':'none; nhịp thở gánh nước và nghe gió được củng cố','injuries':[],
        'inventory_changes':[],
        'relationship_beat':'Tiểu Bảo chọn cứu bà Mạnh rồi tự làm lại thử thách; xác lập giá trị người quan trọng hơn luật nhưng lời đã nhận vẫn giữ',
        'knowledge_gained':['ước mơ cụ thể: căn nhà không dột, kho gạo, bếp lớn, có nơi để về'],
        'hooks_opened':['H002','H003'],'hooks_paid':[],
        'foreshadow_seeds':['gió/đường về motif','nồi đen ấm khi bếp tắt'],
        'next_immediate_objective':'dự sinh nhật và tìm hiểu vì sao người lớn khác thường'
    },
    4: {
        'pov':'Tạ Tiểu Bảo','start_location':'Lạc Kê Thôn','end_location':'đường về nhà sau khi nghe lén',
        'cultivation_changes':'none','injuries':[],
        'inventory_changes':['được bà Mạnh cho bánh','được Thôi Đại Tráng cho thịt khô'],
        'relationship_beat':'bữa sinh nhật cho thấy cả làng thương hắn; Tiểu Bảo nghe nửa câu và hiểu lầm rằng mình bị đuổi',
        'knowledge_gained':['nghe được kế hoạch cho mình xuống núi nhưng chưa biết lý do đầy đủ'],
        'hooks_opened':['H001'],'hooks_paid':[],
        'foreshadow_seeds':['người lớn dặn kỹ như chuẩn bị cho thế giới ngoài làng'],
        'next_immediate_objective':'quyết định có rời làng trước khi bị nói thẳng hay không'
    },
    5: {
        'pov':'Tạ Tiểu Bảo','start_location':'nhà Tiểu Bảo','end_location':'nhà Tiểu Bảo',
        'cultivation_changes':'none','injuries':[],
        'inventory_changes':['đóng gói bánh, thịt khô, dao cũ, dây đỏ và nồi đen để xuống núi'],
        'relationship_beat':'hiểu rằng xuống núi không phải bị đuổi; Lạc Kê vẫn là nhà; chủ động chọn đi',
        'knowledge_gained':['người ngoài có khái niệm Trúc Cơ','dân làng che giấu nhiều chuyện','họ sẽ không ép hắn rời nếu hắn không muốn'],
        'hooks_opened':['H001','H002','H003'],'hooks_paid':[],
        'foreshadow_seeds':['câu “ngươi không phải chìa khóa”','Thôi nói Trúc Cơ rất yếu','trận che làng và ba châu yêu được nhắc mơ hồ'],
        'next_immediate_objective':'sáng mai chính thức rời Lạc Kê Thôn'
    }
}

manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
for c in manifest['chapters']:
    n = c['chapter']
    if 1 <= n <= 5:
        chapter_file = ROOT / f'chapters/chapter_{n:03d}.md'
        heading = chapter_file.read_text(encoding='utf-8').splitlines()[0].lstrip('#').strip()
        c['title'] = heading
        c['title_status'] = 'draft_locked'
        c['status'] = 'draft_passed_qa'
MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')

ledger = json.loads(LEDGER.read_text(encoding='utf-8'))
ledger['last_completed_chapter'] = 5
ledger['timeline_day'] = 2
ledger['current_state']['ta_tieu_bao']['location'] = 'Lạc Kê Thôn, chuẩn bị xuống núi'
ledger['current_state']['ta_tieu_bao']['inventory'] = ['dao cũ','nồi đen','quần áo','bánh bà Mạnh','thịt khô Thôi Đại Tráng','dây đỏ cũ']
existing = [row for row in ledger.get('entries', []) if not (1 <= int(row.get('chapter', 0)) <= 5)]
for n in range(1, 6):
    existing.append({'chapter': n, **entries[n]})
ledger['entries'] = sorted(existing, key=lambda row: row['chapter'])
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2), encoding='utf-8')
print('checkpointed chapters 001-005')
