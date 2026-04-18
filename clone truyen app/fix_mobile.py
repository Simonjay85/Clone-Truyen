import os
import re

components_dir = "src/components"
for filename in os.listdir(components_dir):
    if filename.endswith("View.tsx") and filename != "MicroDramaView.tsx" and filename != "GeminiDramaView.tsx":
        filepath = os.path.join(components_dir, filename)
        with open(filepath, 'r') as f:
            content = f.read()

        # Check if already has isConfigExpanded
        if "isConfigExpanded" not in content:
            # 1. Add state state
            content = re.sub(r'(const \[maxChapters, setMaxChapters\] = useState\(40\);)',
                             r'\1\n  const [isConfigExpanded, setIsConfigExpanded] = useState(true);', content)
            
            # 2. Add collapse logic on generate
            content = re.sub(r'(setTitle\(.*?\);)',
                             r'\1\n      if (pitches.length > 0) setIsConfigExpanded(false);', content)

            # 3. Update Navbar
            content = content.replace('<nav className="h-[60px]',
                                      '<nav className="h-auto md:h-[60px] py-4 md:py-0')
            content = content.replace('px-6 flex items-center justify-between',
                                      'px-4 md:px-6 flex flex-col md:flex-row items-center justify-between gap-4 md:gap-0')

            # 4. Update Main Layout Wrapper
            content = content.replace('<div className="flex flex-1 overflow-hidden">',
                                      '<div className="flex flex-col md:flex-row flex-1 overflow-hidden relative">')

            # 5. Update Aside (Left Panel)
            content = re.sub(r'(<aside className="w-\[540px\].*?p-6 shrink-0 z-10)(">)',
                             r'{isConfigExpanded && (\n        \1 transition-all\2\n          <div className="flex justify-between items-center mb-5">\n             <h3 className="text-xs font-bold text-[#6b7a99] uppercase tracking-[1.5px]">⚙️ Cấu Hình</h3>\n             <button onClick={() => setIsConfigExpanded(false)} className="text-slate-500 hover:text-white p-1 rounded-md hover:bg-white/5">✕</button>\n          </div>', content)
            
            content = content.replace('</aside>', '</aside>\n        )}')

            # 6. Update Main (Right Panel)
            content = content.replace('<main className="flex-1 bg-[#0a0a10] flex flex-col min-w-0">',
                                      '<main className={`flex-1 bg-[#0a0a10] flex flex-col min-w-0 ${!isConfigExpanded ? \'md:ml-8\' : \'\'}`}>')

            content = content.replace('<div className="h-[48px] bg-[#17172a] border-b border-white/5 px-6 flex justify-between items-center shrink-0">',
                                      '<div className="min-h-[48px] py-3 md:py-0 bg-[#17172a] border-b border-white/5 px-6 flex flex-col md:flex-row justify-between items-center shrink-0 gap-3">')
            
            content = content.replace('{isGenerating ? \'Hệ thống AI',
                                      '{!isConfigExpanded && (<button onClick={() => setIsConfigExpanded(true)} className="bg-white/10 hover:bg-white/20 text-white px-3 py-1 rounded-md text-xs font-bold mr-2 transition-all">Mở Cấu Hình ☰</button>)}\n                 {isGenerating ? \'Hệ thống AI')
            
            # Write back
            with open(filepath, 'w') as f:
                f.write(content)
                print(f"Updated {filename}")
