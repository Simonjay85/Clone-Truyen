import os

files = [
    "src/components/ClaudeDramaView.tsx",
    "src/components/MicroDramaView.tsx",
    "src/components/ComboEconomicView.tsx",
    "src/components/ComboRoyalView.tsx",
    "src/components/GrokDramaView.tsx",
    "src/components/GeminiDramaView.tsx"
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply all replacements
    content = content.replace('TẠO ĐÚNG 20 KỊCH BẢN', 'TẠO ĐÚNG 5 KỊCH BẢN')
    content = content.replace('ARRAY 20 KỊCH BẢN', 'ARRAY 5 KỊCH BẢN')
    content = content.replace('.slice(0, 20)', '.slice(0, 5)')
    
    # Also if it previously had 10 in the prompt
    content = content.replace('TẠO ĐÚNG 10 KỊCH BẢN', 'TẠO ĐÚNG 5 KỊCH BẢN')
    content = content.replace('ARRAY 10 KỊCH BẢN', 'ARRAY 5 KỊCH BẢN')
    content = content.replace('.slice(0, 10)', '.slice(0, 5)')

    # UI adjustments
    content = content.replace('thiết lập 10 kịch bản', 'thiết lập 5 kịch bản')
    content = content.replace('AI Đang Lên 10 Kịch Bản', 'AI Đang Lên 5 Kịch Bản')
    content = content.replace('AI ĐANG LÊN 10 KỊCH BẢN', 'AI ĐANG LÊN 5 KỊCH BẢN')
    content = content.replace('thiết lập 20 kịch bản', 'thiết lập 5 kịch bản')
    content = content.replace('AI Đang Lên 20 Kịch Bản', 'AI Đang Lên 5 Kịch Bản')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated perfectly for 5 kich ban.")
