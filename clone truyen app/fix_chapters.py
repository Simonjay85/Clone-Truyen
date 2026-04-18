import glob
import re

for filepath in glob.glob("src/components/*DramaView.tsx") + glob.glob("src/components/*EconomicView.tsx") + glob.glob("src/components/ComboRoyalView.tsx"):
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Update systemPrompt to include suggestedGenres and suggestedChapters
    if "suggestedChapters" not in content:
        content = content.replace('"overallSizzle": "Sự bạo não tóm tắt"', '"overallSizzle": "Sự bạo não tóm tắt",\n      "suggestedGenres": "Thể loại phù hợp nhất (VD: Xuyên không, Vả mặt)",\n      "suggestedChapters": 30')
        print(f"Added suggested parameters to system prompt in {filepath}")

    # 2. Add editable targetChapters array / logic 
    # To keep it simple, we can just allow editing the pitch.suggestedChapters directly and use it to push to Autopilot!
    # Let's find handlePushAutopilot
    push_logic = "targetChapters: targetChapters,"
    new_push_logic = "targetChapters: pitchOptions[idx].suggestedChapters || targetChapters,"
    content = content.replace(push_logic, new_push_logic)
    
    # 3. Add the UI rendering of the tags at the bottom of the card!
    # The bottom of the card is usually after "overallSizzle"
    # Find: <textarea ... value={pitch.overallSizzle ... /></div></div>
    
    # Let's just find the Supreme Judge block or end of card
    if "📚 Số chương" not in content:
        card_end = "{grading && grading.grading && ("
        new_card_end = """
                             <div className="mt-4 pt-3 border-t border-white/5 flex gap-4 text-xs font-medium">
                                <div className="bg-emerald-500/10 text-emerald-400 px-3 py-1.5 rounded-lg flex items-center gap-1.5">
                                   <span className="text-emerald-500">🔖</span> Thể loại gợi ý: 
                                   <input className="bg-transparent border-b border-transparent focus:border-emerald-500 focus:bg-black/20 outline-none px-1 max-w-[150px]"
                                        value={pitch.suggestedGenres || ''}
                                        onChange={(e) => updatePitch(idx, 'suggestedGenres', e.target.value)}
                                        placeholder="Nhập thể loại..."
                                   />
                                </div>
                                <div className="bg-amber-500/10 text-amber-500 px-3 py-1.5 rounded-lg flex items-center gap-1.5">
                                   📚 Số chương: 
                                   <input type="number" className="bg-transparent border-b border-transparent focus:border-amber-500 focus:bg-black/20 outline-none px-1 w-[60px]"
                                        value={pitch.suggestedChapters || ''}
                                        onChange={(e) => updatePitch(idx, 'suggestedChapters', e.target.value)}
                                        placeholder="VD: 30"
                                        title="Chỉnh sửa số chương mục tiêu cho truyện này trước khi xả vào hệ thống"
                                   />
                                </div>
                             </div>
                             """ + card_end
        content = content.replace(card_end, new_card_end)

    with open(filepath, 'w') as f:
        f.write(content)
