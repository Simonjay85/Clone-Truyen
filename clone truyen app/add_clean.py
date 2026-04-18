import glob
import re

for filepath in glob.glob("src/components/*DramaView.tsx") + glob.glob("src/components/*EconomicView.tsx") + glob.glob("src/components/ComboRoyalView.tsx"):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check if already has clear logic
    if "Dọn Sạch" in content:
        continue
        
    # 1. Add handleClearBoard function before handlePushAutopilot
    handle_clear = """
  const handleClearBoard = () => {
    if (confirm("Chắc chắn muốn xóa toàn bộ kịch bản hiện tại?")) {
       setPitchOptions([]);
       setGradingStatus({});
       setSelectedPitches([]);
       setRefineFeedback('');
       sessionStorage.removeItem('md_pitchOptions');
    }
  };

"""
    content = content.replace("  const handlePushAutopilot", handle_clear + "  const handlePushAutopilot")
    
    # 2. Add confirm to clear after push
    autopilot_success = "alert(`🚀 Đã nối ${items.length} kịch bản! Vui lòng chuyển sang Tab Auto-Pilot để theo dõi tốc độ cày chữ!`);"
    if autopilot_success in content:
        new_success = """if (confirm(`🚀 Đã đẩy ${items.length} kịch bản vào lò Auto-Pilot!\n\nBạn có muốn XÓA TRẮNG Bảng kịch bản hiện tại để viết bộ mới không?`)) {
       setPitchOptions([]);
       setGradingStatus({});
    } else {
       // Filter out the pushed ones so they don't get pushed again by mistake
       const newOptions = pitchOptions.filter((_, idx) => !selectedPitches.includes(idx));
       setPitchOptions(newOptions);
       setGradingStatus({}); // Reset grading as indexes shift
    }"""
        content = content.replace(autopilot_success, new_success)
        
    # 3. Add Clear Button to Toolbar
    toolbar_div = "{pitchOptions.length > 0 ? `${selectedPitches.length}/${pitchOptions.length} Đã Chọn` : '0 từ'}"
    if toolbar_div in content:
        new_toolbar = """{pitchOptions.length > 0 && <button onClick={handleClearBoard} className="bg-red-500/10 text-red-400 hover:bg-red-500/20 px-3 py-1.5 rounded-lg text-sm font-bold flex items-center gap-1 transition-all">🗑 Dọn Sạch</button>}
                 """ + toolbar_div
        content = content.replace(toolbar_div, new_toolbar)

    with open(filepath, 'w') as f:
        f.write(content)
        print(f"Updated clear logic in {filepath}")
