import re

files_keys = [
    ("src/components/GeminiDramaView.tsx", "geminiKey", "gemini", "gemini-1.5-flash"),
    ("src/components/GrokDramaView.tsx", "grokKey", "grok", "grok-base"),
    ("src/components/ClaudeDramaView.tsx", "claudeKey", "claude", "claude-3-5-sonnet")
]

for path, key_name, engine, default_model in files_keys:
    with open(path, "r") as f:
        content = f.read()

    if "agentConceptScorer" not in content:
        content = content.replace("import { agentPuppetMaster, ", "import { agentPuppetMaster, callGemini } from '../lib/engine';\nimport { agentConceptScorer } from '../lib/advanced_engine';\n// ")

    if "updatePitch" not in content:
        content = content.replace("const togglePitchSelect = (idx: number) => {", "const updatePitch = (idx: number, field: string, value: string) => { const newPOptions = [...pitchOptions]; newPOptions[idx] = { ...newPOptions[idx], [field]: value }; setPitchOptions(newPOptions); }; const togglePitchSelect = (idx: number) => {")

    if "gradeAllPitches" not in content:
        grade_all_code = f"""
  const gradeAllPitches = async () => {{
     if (!{key_name}) return alert("Chưa có API Key");
     if (pitchOptions.length === 0) return alert("Chưa có kịch bản nào để chấm!");
     setIsGradingParam(-1);
     try {{
         const res = await agentConceptScorer('{engine}', {key_name}, '{default_model}', pitchOptions);
         const newGradingStatus: any = {{}};
         if (res.scores && Array.isArray(res.scores)) {{
             res.scores.forEach((s: any) => {{
                 newGradingStatus[s.index] = {{ score: s.score || 0, grading: s.reason || s.grading || '' }};
             }});
             setGradingStatus(newGradingStatus);
         }}
     }} catch (e: any) {{
         alert("Lỗi chấm điểm chùm: " + e.message);
     }} finally {{
         setIsGradingParam(null);
     }}
  }};
"""
        content = content.replace("const gradePitch = async (index: number) => {", grade_all_code + "\n  const gradePitch = async (index: number) => {")

    batch_btn = f"""                 <div className="flex gap-4 items-center">
                 {{pitchOptions.length > 0 && <button disabled={{isGradingParam === -1}} onClick={{gradeAllPitches}} className="bg-amber-500/20 text-amber-400 border border-amber-500/30 px-4 py-2 rounded-lg text-sm font-bold flex items-center gap-2 hover:bg-amber-500/40 transition-all">{{isGradingParam === -1 ? '⏳ Đang Chấm Điểm Hàng Loạt...' : '⚖️ Chấm Điểm Hàng Loạt'}}</button>}}
"""
    if "Chấm Điểm Hàng Loạt" not in content:
        content = content.replace('<div className="flex gap-4 items-center">', batch_btn)

    old_prompt = """             systemPrompt: `Bạn là Đạo Diễn Thiết Lập. Hãy tạo chính xác 20 phiên bản kịch bản gốc siêu bạo não cho Micro-Drama (short text).
BẮT BUỘC TRẢ VỀ ĐỊNH DẠNG JSON OBJECT (VỚI KEY "pitches" CHỨA ARRAY).
Format:
{
  "pitches": [
    {
      "protagonist": "Tên nhân vật",
      "worldSettings": "Bối cảnh 1-2 câu",
      "characterArc": "Sự phát triển nhân vật (vết thương lòng/bị chà đạp)",
      "plotTwists": "Mô tả Twist chính (Phản bội/Sỉ nhục)",
      "overallSizzle": "Mô tả tóm tắt sự bạo não"
    }
  ]
}`"""

    new_prompt = """             systemPrompt: `Bạn là Đạo Diễn Thiết Lập. TẠO ĐÚNG 20 KỊCH BẢN MICRO-DRAMA.
TUYỆT ĐỐI KHÔNG DÙNG TỪ TIẾNG ANH (Ví dụ: Đổi Steampunk thành Cơ Khí Cổ Đại, Kawaii thành Đáng Yêu/Linh vật). 100% tiếng Việt hoặc Hán Việt.
BẮT BUỘC TRẢ VỀ JSON OBJECT CÓ KEY "pitches" LÀ ARRAY 20 KỊCH BẢN.
{
  "pitches": [
    {
      "super_title": "Tên truyện cực ngầu (VD: Ma Tôn Truyền Kỳ, Đại Tỷ Hồi Sinh)",
      "summary": "Tóm tắt truyện (3 câu)",
      "worldSettings": "Bối cảnh",
      "characterArc": "Vết thương lòng/phát triển nhân vật",
      "plotTwists": "Cú lật bàn/Vả mặt",
      "overallSizzle": "Sự bạo não"
    }
  ]
}`"""
    content = content.replace(old_prompt, new_prompt)

    content = content.replace("if (!title && pitches[0]?.protagonist) setTitle(`Câu chuyện của ${pitches[0].protagonist}`);", "if (!title && (pitches[0]?.super_title || pitches[0]?.protagonist)) setTitle(pitches[0]?.super_title || pitches[0]?.protagonist);")

    editable_jsx = """                             <input className="w-full text-2xl font-extrabold text-white mb-6 leading-snug bg-transparent border-b border-white/10 hover:border-white/30 focus:border-teal-500 outline-none pb-2 transition-colors"
                                value={pitch.super_title || pitch.protagonist || ''}
                                onChange={(e) => updatePitch(idx, pitch.super_title !== undefined ? 'super_title' : 'protagonist', e.target.value)}
                                placeholder="Tên truyện..."
                             />

                             <div className="space-y-4 text-[14px] leading-relaxed text-[#cbd5e1] mb-6 flex-1">
                                {pitch.summary !== undefined && (
                                   <div>
                                     <h4 className="text-cyan-400 font-bold mb-1 text-xs uppercase tracking-wide">📝 Tóm Tắt</h4>
                                     <textarea className="w-full bg-black/20 text-[#cbd5e1] border border-white/5 rounded p-2 text-sm resize-none focus:border-teal-500 outline-none min-h-[60px]"
                                       value={pitch.summary || ''} onChange={(e) => updatePitch(idx, 'summary', e.target.value)} />
                                   </div>
                                )}
                                <div>
                                   <h4 className="text-indigo-400 font-bold mb-1 text-xs uppercase tracking-wide">🌍 Bối Cảnh</h4>
                                   <textarea className="w-full bg-black/20 text-[#cbd5e1] border border-white/5 rounded p-2 text-sm resize-none focus:border-teal-500 outline-none min-h-[60px]"
                                     value={pitch.worldSettings || ''} onChange={(e) => updatePitch(idx, 'worldSettings', e.target.value)} />
                                </div>
                                <div>
                                   <h4 className="text-amber-400 font-bold mb-1 text-xs uppercase tracking-wide">🤕 Vết Thương Lòng</h4>
                                   <textarea className="w-full bg-black/20 text-[#cbd5e1] border border-white/5 rounded p-2 text-sm resize-none focus:border-teal-500 outline-none min-h-[60px]"
                                     value={pitch.characterArc || ''} onChange={(e) => updatePitch(idx, 'characterArc', e.target.value)} />
                                </div>
                                <div>
                                   <h4 className="text-purple-400 font-bold mb-1 text-xs uppercase tracking-wide">🌪️ Plot Twist</h4>
                                   <textarea className="w-full bg-black/20 text-[#cbd5e1] border border-white/5 rounded p-2 text-sm resize-none focus:border-teal-500 outline-none min-h-[60px]"
                                     value={pitch.plotTwists || ''} onChange={(e) => updatePitch(idx, 'plotTwists', e.target.value)} />
                                </div>
                                <div>
                                   <h4 className="text-rose-400 font-bold mb-1 text-xs uppercase tracking-wide">🔥 Độ Bạo Não</h4>
                                   <textarea className="w-full bg-black/20 text-[#cbd5e1] border border-white/5 rounded p-2 text-sm resize-none focus:border-teal-500 outline-none min-h-[60px]"
                                     value={pitch.overallSizzle || ''} onChange={(e) => updatePitch(idx, 'overallSizzle', e.target.value)} />
                                </div>
                             </div>
"""

    static_jsx_pattern = r'<div className="text-2xl font-extrabold text-white mb-6 leading-snug">.*?</div>.*?<div className="space-y-5 text-\[14px\] leading-relaxed text-\[#cbd5e1\] mb-6 flex-1">.*?</div>'
    if '<div className="text-2xl font-extrabold' in content:
        content = re.sub(static_jsx_pattern, editable_jsx, content, flags=re.DOTALL)

    with open(path, "w") as f:
        f.write(content)
    print(f"Fixed {path}")
