import glob

# 1. Fix the `agentConceptScorer` prompt
filepath = "src/lib/advanced_engine.ts"
with open(filepath, 'r') as f:
    content = f.read()

old_sys = 'Bạn là Concept Scorer. Chấm điểm các concept trong mảng được đưa vào theo rubric sau:'
if old_sys in content:
    # We will replace the entire system prompt assigned to `sys` in `agentConceptScorer`
    import re
    content = re.sub(
        r'const sys = `Bạn là Concept Scorer.*?}`;',
        '''const sys = `Bạn là Giám Khảo Tối Cao (Supreme Judge) khắc nghiệt nhất. Chấm điểm các concept trong mảng được đưa vào.
NHIỆM VỤ: Chấm điểm (1-10) và viết 1 dòng NHẬN XÉT CỰC KỲ GAY GẮT, CHỈ ĐÍCH DANH ĐIỂM YẾU/MẠNH.
TUYỆT ĐỐI KHÔNG DÙNG VĂN MẪU kiểu "Hook rõ, pain mạnh". PHẢI nhắc trực tiếp đến tình tiết Plot Twist hoặc Bối cảnh của chính kịch bản đó. Nếu motif sáo rỗng, vả mặt chưa đủ đau, hãy chê thậm tệ và trừ điểm. Nếu độc đáo, bạo não, thưởng điểm.
Trả về JSON đúng cấu trúc mảng:
{
  "scores": [
    {"index": 0, "title": "...", "score": 9.5, "reason": "Nhận xét chi tiết gay gắt..."}
  ],
  "winner_index": 0
}`;''',
        content,
        flags=re.DOTALL
    )
    with open(filepath, 'w') as f:
        f.write(content)
        print("Updated advanced_engine.ts prompt")


# 2. Fix the scroll clipping on mobile for all Views
for view_file in glob.glob("src/components/*DramaView.tsx") + glob.glob("src/components/*EconomicView.tsx") + glob.glob("src/components/ComboRoyalView.tsx"):
    with open(view_file, 'r') as f:
        view_content = f.read()
    
    # Change flex wrapper to allow y-overflow on mobile
    old_wrapper = 'className="flex flex-col md:flex-row flex-1 overflow-hidden relative"'
    new_wrapper = 'className="flex flex-col md:flex-row flex-1 overflow-y-auto overflow-x-hidden md:overflow-hidden relative"'
    if old_wrapper in view_content:
        view_content = view_content.replace(old_wrapper, new_wrapper)
        
    # Remove shrink-0 from aside to prevent rigid height stretching? 
    # Actually, if the wrapper is overflow-y-auto, the aside will just take its full height.
    # To be totally safe, let's remove `overflow-y-auto custom-scrollbar` from aside on mobile!
    old_aside = 'className="w-full md:w-[540px] bg-[#13131f] border-r border-white/5 flex flex-col overflow-y-auto custom-scrollbar p-6 shrink-0 z-10 transition-all"'
    new_aside = 'className="w-full md:w-[540px] bg-[#13131f] border-b md:border-b-0 md:border-r border-white/5 flex flex-col md:overflow-y-auto custom-scrollbar p-6 shrink-0 z-10 transition-all"'
    if old_aside in view_content:
        view_content = view_content.replace(old_aside, new_aside)

    # 3. Main content should also not be independently scrolled on mobile to prevent double scrollbar trap
    old_main_wrap = 'className="flex-1 overflow-y-auto custom-scrollbar'
    new_main_wrap = 'className="flex-1 md:overflow-y-auto custom-scrollbar'
    if old_main_wrap in view_content:
        view_content = view_content.replace(old_main_wrap, new_main_wrap)

    with open(view_file, 'w') as f:
        f.write(view_content)
        print(f"Fixed scroll logic in {view_file}")
