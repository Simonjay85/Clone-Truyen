import re

files = [
    "src/components/MicroDramaView.tsx",
    "src/components/GeminiDramaView.tsx",
    "src/components/GrokDramaView.tsx",
    "src/components/ClaudeDramaView.tsx"
]

leaderboard_jsx = """              {Object.keys(gradingStatus).length > 2 && !isGenerating && (
                 <div className="bg-[#17172a] rounded-xl border border-white/5 p-6 mb-8 animation-fade-in mx-10 mt-6">
                    <h3 className="text-lg font-bold text-amber-400 mb-4 flex items-center gap-2">📊 Bảng Tổng Sắp Kịch Bản</h3>
                    <div className="overflow-x-auto">
                       <table className="w-full text-left text-sm text-[#cbd5e1]">
                          <thead className="bg-[#1e1e32] text-xs uppercase text-[#6b7a99] font-bold border-b border-white/10">
                             <tr>
                                <th className="px-4 py-3">Chọn</th>
                                <th className="px-4 py-3">STT</th>
                                <th className="px-4 py-3">Đề Tài</th>
                                <th className="px-4 py-3 text-center">Điểm</th>
                                <th className="px-4 py-3">Nhận Xét Của Judge</th>
                             </tr>
                          </thead>
                          <tbody className="divide-y divide-white/5">
                             {pitchOptions.map((p, i) => ({ pitch: p, index: i, grade: gradingStatus[i] }))
                                .filter(item => item.grade?.score !== undefined)
                                .sort((a, b) => b.grade.score - a.grade.score)
                                .map((item) => (
                                <tr key={item.index} className={`hover:bg-white/5 transition-colors ${selectedPitches.includes(item.index) ? 'bg-teal-500/10' : ''}`}>
                                   <td className="px-4 py-3 w-[60px]">
                                      <input type="checkbox" checked={selectedPitches.includes(item.index)} onChange={() => togglePitchSelect(item.index)} className="accent-teal-500 w-4 h-4 cursor-pointer" />
                                   </td>
                                   <td className="px-4 py-3 font-mono font-bold text-slate-500 w-[60px]">#{item.index + 1}</td>
                                   <td className="px-4 py-3 font-bold text-white max-w-[200px] truncate" title={item.pitch.super_title || item.pitch.protagonist}>{item.pitch.super_title || item.pitch.protagonist}</td>
                                   <td className="px-4 py-3 text-center w-[80px]">
                                      <span className={`font-black ${item.grade.score >= 8 ? 'text-emerald-400' : item.grade.score >= 6 ? 'text-amber-400' : 'text-red-400'}`}>{item.grade.score}</span>
                                   </td>
                                   <td className="px-4 py-3 text-[13px] opacity-80 max-w-[400px] truncate" title={item.grade.grading}>{item.grade.grading}</td>
                                </tr>
                             ))}
                          </tbody>
                       </table>
                    </div>
                 </div>
              )}
"""

for path in files:
    with open(path, "r") as f:
        content = f.read()

    # Find where to inject
    target_anchor = '<div className="grid grid-cols-1 xl:grid-cols-2 gap-8 animation-fade-in pb-10'
    
    if "📊 Bảng Tổng Sắp Kịch Bản" not in content and target_anchor in content:
        # We also need to remove mx-10 mt-6 from the target string itself because the grid has padding, we need to apply padding correctly
        # Let's just insert it right before the grid grid-cols-1
        content = content.replace(target_anchor, leaderboard_jsx + "\n                 " + target_anchor)
        with open(path, "w") as f:
            f.write(content)
        print(f"Added leaderboard to {path}")
