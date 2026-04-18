import re

files_configs = [
    ("src/components/MicroDramaView.tsx", "indigo", "teal", "emerald"),
    ("src/components/GeminiDramaView.tsx", "indigo", "teal", "emerald"),
    ("src/components/GrokDramaView.tsx", "indigo", "teal", "emerald"),
    ("src/components/ClaudeDramaView.tsx", "fuchsia", "purple", "rose")
]

for path, primary, secondary, tertiary in files_configs:
    with open(path, "r") as f:
        content = f.read()

    # Fixed syntax error at line 363
    bad_syntax = "              {pitchOptions.length > 0 && !isGenerating && (\n                                {Object.keys(gradingStatus).length > 2 && !isGenerating && ("
    good_syntax = "              {pitchOptions.length > 0 && !isGenerating && (\n                 <>\n                                {Object.keys(gradingStatus).length > 2 && !isGenerating && ("
    if bad_syntax in content:
        content = content.replace(bad_syntax, good_syntax)
    
    # Also need to close the Fragment at the end of the grid
    end_grid = "                    })}\n                 </div>\n              )}"
    end_grid_fixed = "                    })}\n                 </div>\n              </>)}"
    if end_grid in content:
        content = content.replace(end_grid, end_grid_fixed)

    # Clean up static garbage left over by bad regex (if any)
    static_garbage = r'                                <div><h4 className="text-amber-400 font-bold mb-1 text-xs uppercase tracking-wide">🤕 Vết Thương Lòng</h4><p>{pitch.characterArc}</p></div>.*?</div>'
    content = re.sub(static_garbage, '', content, flags=re.DOTALL)

    # Clean up double </div> in Claude
    double_div = r'                             </div>\n\n                             </div>'
    content = re.sub(double_div, '                             </div>\n', content)

    # Update Prompts
    old_prompt1 = "TUYỆT ĐỐI KHÔNG DÙNG TỪ TIẾNG ANH (Ví dụ: Đổi Steampunk thành Cơ Khí Cổ Đại, Kawaii thành Đáng Yêu/Linh vật). 100% tiếng Việt hoặc Hán Việt."
    new_prompt1 = "TUYỆT ĐỐI KHÔNG DÙNG TỪ TIẾNG ANH. Viết bằng tiếng Việt hoặc Hán Việt thuần túy. Xây dựng cốt truyện mang màu sắc Châu Á (đặc biệt là Việt Nam hoặc Trung Quốc)."
    content = content.replace(old_prompt1, new_prompt1)

    old_prompt2 = '"summary": "Tóm tắt truyện (3 câu)",'
    new_prompt2 = '"summary": "Tóm tắt truyện (3 câu - Phải nhồi nhét hook chấn động, giật gân, tạo sự tò mò tột độ để thu hút độc giả click vào đọc)",'
    content = content.replace(old_prompt2, new_prompt2)

    with open(path, "w") as f:
        f.write(content)
    print("Cleaned " + path)

