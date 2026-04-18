
with open("src/components/GeminiDramaView.tsx", "r") as f:
    gemini_code = f.read()

eco_code = gemini_code.replace("GeminiDramaView", "ComboEconomicView")
eco_code = eco_code.replace("Thiên Đường Sáng Tác (Gemini)", "Thiên Đường Sáng Tác (Liên Quân KT)")
eco_code = eco_code.replace("Trạm Đạo Diễn <span className=\"bg-gradient-to-br from-teal-500 to-emerald-400 text-white px-2.5 py-0.5 rounded-full text-xs uppercase tracking-wider ml-1\">Gemini</span>", "Trạm Đại Đạo Diễn <span className=\"bg-gradient-to-br from-blue-500 to-emerald-400 text-white px-2.5 py-0.5 rounded-full text-xs uppercase tracking-wider ml-1\">Liên Quân KT</span>")
eco_code = eco_code.replace("outlineEngine: 'gemini', writeEngine: 'gemini'", "comboType: 5, outlineEngine: 'gemini', writeEngine: 'openai', isAdvancedPipeline: true")

with open("src/components/ComboEconomicView.tsx", "w") as f:
    f.write(eco_code)


with open("src/components/ClaudeDramaView.tsx", "r") as f:
    claude_code = f.read()

royal_code = claude_code.replace("ClaudeDramaView", "ComboRoyalView")
royal_code = royal_code.replace("Thiên Đường Sáng Tác (Claude Wordsmith)", "Thiên Đường Sáng Tác (Liên Quân HG)")
royal_code = royal_code.replace("Trạm Đạo Diễn <span className=\"bg-gradient-to-br from-fuchsia-500 to-purple-400 text-white px-2.5 py-0.5 rounded-full text-xs uppercase tracking-wider ml-1\">Claude</span>", "Trạm Đại Đạo Diễn <span className=\"bg-gradient-to-br from-amber-500 to-fuchsia-400 text-white px-2.5 py-0.5 rounded-full text-xs uppercase tracking-wider ml-1\">Liên Quân HG</span>")
royal_code = royal_code.replace("outlineEngine: 'claude', writeEngine: 'claude'", "comboType: 6, outlineEngine: 'claude', writeEngine: 'openai', isAdvancedPipeline: true")

with open("src/components/ComboRoyalView.tsx", "w") as f:
    f.write(royal_code)

print("Cloned Combos")
