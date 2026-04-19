
import fs from 'fs';
import path from 'path';

const baseDir = '/Users/aaronnguyen/TN/App/Clone Truyen/clone truyen app/src/components';
const filesToPatch = [
  'ComboRoyalView.tsx',
  'ComboEconomicView.tsx',
  'GrokDramaView.tsx',
  'MicroDramaView.tsx',
  'ClaudeDramaView.tsx',
  'GeminiDramaView.tsx'
];

const newGenresDef = `const GENRE_GROUPS = {
  "🔥 Kịch Tính Cao": ["Vả Mặt", "Gia Đấu", "Cung Đấu", "Trọng Sinh"],
  "🌍 Bối Cảnh": ["Đô Thị", "Xuyên Không", "Mạt Thế", "Hệ Thống", "Hợp Đồng Hôn Nhân", "Tổng Tài"],
  "❤️ Cảm Xúc": ["Ngược Tâm", "Sủng Ngọt", "Hài Hước", "Nữ Cường", "Trà Xanh Tiểu Tam", "Truy Thê"]
};`;

const newJSX = `             <div className="flex flex-col gap-4">
                {Object.entries(GENRE_GROUPS).map(([groupName, genres]) => (
                   <div key={groupName}>
                     <div className="text-xs font-bold text-slate-500 mb-2 uppercase">{groupName}</div>
                     <div className="flex flex-wrap gap-2">
                        {genres.map(g => (
                           <button key={g} onClick={() => toggleGenre(g)} className={\`px-3 py-1.5 rounded-full border text-[11px] font-bold transition-all uppercase tracking-wider \${selectedGenres.includes(g) ? 'border-rose-500 text-rose-400 bg-rose-500/20 shadow-[0_0_10px_rgba(244,63,94,0.3)]' : 'border-white/10 text-slate-400 hover:border-rose-500/50 hover:text-rose-300'}\`}>{g}</button>
                        ))}
                     </div>
                   </div>
                ))}
             </div>`;

filesToPatch.forEach(file => {
  const filePath = path.join(baseDir, file);
  if (!fs.existsSync(filePath)) return;
  
  let content = fs.readFileSync(filePath, 'utf8');

  // Replace definition
  content = content.replace(/const GENRE_LIST = \[\s*[\s\S]*?\];/m, newGenresDef);

  // Replace JSX
  // Locate the <div className="flex flex-wrap gap-2">...</div> wrapper containing GENRE_LIST.map
  const oldJSXRegex = /<div className="flex flex-wrap gap-2">\s*\{GENRE_LIST\.map\([\s\S]*?\}\s*<\/div>/m;
  if (oldJSXRegex.test(content)) {
    content = content.replace(oldJSXRegex, newJSX);
  } else {
    // If it's already using GENRE_GROUPS, skip or handle
    if (content.includes('GENRE_GROUPS')) {
      console.log(file + " already patched.");
    } else {
      console.log("Couldn't patch JSX in " + file);
    }
  }

  // Double check if any stray GENRE_LIST references exist (like fallback random logic)
  content = content.replace(/GENRE_LIST/g, 'Object.values(GENRE_GROUPS).flat()');

  fs.writeFileSync(filePath, content, 'utf8');
});

console.log('Finished updating genre groups in UI.');
