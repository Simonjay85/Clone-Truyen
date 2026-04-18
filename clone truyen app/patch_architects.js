import fs from 'fs';

const ruleText = `
QUY TẮC CỐT LÕI TỪ NHÀ SẢN XUẤT (BẮT BUỘC): KHÔNG ĐỂ quá trình thu thập chứng cứ của nhân vật chính diễn ra quá dễ dàng. Bắt buộc phải thiết kế một chương 'Phản đòn' từ phe phản diện khiến nhân vật chính bị lộ tẩy hoặc đẩy vào chân tường trước khi cô lật kèo. Tiêu đề các chương (title) phải dùng động từ mạnh, giật tít, độc hại, tò mò (Ví dụ: Giọt máu giả, Chiếc camera giấu kín ở đáy quan tài...).`;

// Patch advanced_engine.ts
let advanced = fs.readFileSync('src/lib/advanced_engine.ts', 'utf8');
if (!advanced.includes('Giới máu giả, Chiếc camera')) {
  advanced = advanced.replace(
    /Tuyệt đối CHỈ trả về JSON nguyên bản \(không bọc \`\`\`json\), format chuẩn:/,
    `${ruleText}\nTuyệt đối CHỈ trả về JSON nguyên bản (không bọc \`\`\`json), format chuẩn:`
  );
  advanced = advanced.replace(
    /\{ "episode": 1, "outline": "Beat của tập" \}/,
    `{ "episode": 1, "title": "Tên chương giật tít", "outline": "Beat của tập" }`
  );
  fs.writeFileSync('src/lib/advanced_engine.ts', advanced, 'utf8');
}

// Patch engine.ts
let engine = fs.readFileSync('src/lib/engine.ts', 'utf8');
const searchFunctions = [
  'agentMicroDramaExpand',
  'agentGrokDramaExpand',
  'agentClaudeDramaExpand',
  'agentGeminiDramaExpand'
];

searchFunctions.forEach(func => {
  const regex = new RegExp(\`(export async function \${func}[\\\\s\\\\S]*?const sys = \\\`[\\\\s\\\\S]*?)(TRẢ VỀ JSON HỢP LỆ:|\"timeline\":)\`, 'i');
  if (engine.match(regex) && !engine.includes(ruleText)) {
      // Find where to insert rule
      engine = engine.replace(regex, (match, prefix, suffix) => {
         return \`\${prefix}\${ruleText}\\n\${suffix}\`;
      });
  }
});

// Update the JSON schema in engine.ts outputs to include title
engine = engine.replace(
  /"timeline": \[{"episode": 1, "outline": "Tóm tắt 30 chữ..."}\]/g,
  `"timeline": [{"episode": 1, "title": "Tựa đề giật tít...", "outline": "Tóm tắt 30 chữ..."}]`
);

fs.writeFileSync('src/lib/engine.ts', engine, 'utf8');
console.log('Patched all architects.');
