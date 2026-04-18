import re

files_configs = [
    ("src/components/MicroDramaView.tsx", "openAIKey", "openai", "gpt-4o-mini"),
    ("src/components/GeminiDramaView.tsx", "geminiKey", "gemini", "gemini-1.5-flash"),
    ("src/components/GrokDramaView.tsx", "grokKey", "grok", "grok-base"),
    ("src/components/ClaudeDramaView.tsx", "claudeKey", "claude", "claude-3-5-sonnet")
]

for path, key_name, engine, default_model in files_configs:
    with open(path, "r") as f:
        content = f.read()

    # Verify script doctor import
    if "agentPitchRefiner" not in content:
        content = content.replace("agentConceptScorer } from", "agentConceptScorer, agentPitchRefiner } from")

    # Add State
    state_str = "const [refineFeedback, setRefineFeedback] = useState('');\n  const [isRefining, setIsRefining] = useState(false);"
    if "refineFeedback" not in content:
        content = content.replace("const [title, setTitle] = useState('');", state_str + "\n  const [title, setTitle] = useState('');")

    # Add Refine Logic
    refine_logic = f"""
  const refineSelectedPitches = async () => {{
     if (!{key_name}) return alert("Chưa có API Key");
     if (selectedPitches.length === 0) return alert("Vui lòng tick chọn ít nhất 1 kịch bản để sửa chữa!");
     if (!refineFeedback.trim()) return alert("Vui lòng nhập lời khuyên/hướng sửa đổi làm kim chỉ nam cho AI!");
     
     setIsRefining(true);
     try {{
         const newPOptions = [...pitchOptions];
         for (let i = 0; i < selectedPitches.length; i++) {{
             const idx = selectedPitches[i];
             const result = await agentPitchRefiner('{engine}', {key_name}, selectedModel || '{default_model}', newPOptions[idx], refineFeedback);
             if (result && (result.super_title || result.protagonist)) {{
                 newPOptions[idx] = result;
             }}
         }}
         
         setPitchOptions(newPOptions);
         
         setIsGradingParam(-1);
         const res = await agentConceptScorer('{engine}', {key_name}, selectedModel || '{default_model}', newPOptions);
         const newGradingStatus: any = {{}};
         if (res.scores && Array.isArray(res.scores)) {{
             res.scores.forEach((s: any) => {{
                 newGradingStatus[s.index] = {{ score: s.score || 0, grading: s.reason || s.grading || '' }};
             }});
             setGradingStatus(newGradingStatus);
         }}
         
         alert("✅ Phẫu thuật thành công " + selectedPitches.length + " kịch bản và đã Chấm điểm lại xong! Lên Top chưa anh zai?");
         
     }} catch(e: any) {{
         alert("Lỗi Phẫu Thuật: " + e.message);
     }} finally {{
         setIsRefining(false);
         setIsGradingParam(null);
     }}
  }};
"""
    if "refineSelectedPitches" not in content:
        content = content.replace("const gradeAllPitches = async () => {", refine_logic + "\n  const gradeAllPitches = async () => {")

    # Add UI Area
    ui_jsx = """
              {/* SCRIPT DOCTOR AREA */}
              {selectedPitches.length > 0 && pitchOptions.length > 0 && !isGenerating && (
                 <div className="bg-gradient-to-r from-red-500/10 to-orange-500/10 border border-red-500/20 rounded-xl p-6 mb-8 mx-10 mt-2 animation-fade-in relative overflow-hidden">
                    <div className="absolute top-0 right-0 p-4 opacity-10 pointer-events-none">
                        <PenTool size={100} />
                    </div>
                    <h3 className="text-[17px] font-black text-rose-400 mb-3 flex items-center gap-2">🛠 Khu Vực Kỹ Sư Kịch Bản (Cấp Cứu)</h3>
                    <p className="text-[#cbd5e1] text-[13px] mb-4 font-medium">Gõ hoặc Dán lời khuyên, phê bình vào đây. AI sẽ bứt tóc sửa lại <strong className="text-white">{selectedPitches.length} kịch bản đang chọn</strong> cho đến khi hoàn hảo và cập nhật lại Bảng Xếp Hạng.</p>
                    <textarea 
                        className="w-full bg-black/40 text-rose-100 border border-red-500/30 rounded-lg p-3 text-[14px] leading-relaxed resize-none focus:border-red-400 focus:bg-black/60 outline-none min-h-[90px] mb-4 shadow-inner"
                        placeholder="Ví dụ: Đổi plot twist thành nam phụ đã âm thầm giật dây từ đầu..."
                        value={refineFeedback}
                        onChange={e => setRefineFeedback(e.target.value)}
                    ></textarea>
                    
                    <button 
                        onClick={refineSelectedPitches} disabled={isRefining || isGradingParam !== null}
                        className="bg-gradient-to-r from-red-600 to-orange-600 text-white font-bold text-[13px] uppercase tracking-wide px-6 py-3 rounded-lg flex items-center gap-2 hover:opacity-90 transition-all shadow-[0_4px_20px_rgba(220,38,38,0.3)] disabled:opacity-50">
                        {isRefining ? '🪄 Bác Sĩ Đang Gọt Giũa Kịch Bản... (Vui lòng chờ)' : '🪄 Bơm Máu Phẫu Thuật Kịch Bản Đi! (Auto-Fix)'}
                    </button>
                 </div>
              )}
"""
    if "Khu Vực Kỹ Sư Kịch Bản" not in content:
        content = content.replace("              {pitchOptions.length > 0 && !isGenerating && (", ui_jsx + "\n              {pitchOptions.length > 0 && !isGenerating && (")

    # Optional: Fix leaderboard mapping to not break if grid items moved or so. 
    # the insertion point is clean.

    with open(path, "w") as f:
        f.write(content)
    print("Done " + path)

