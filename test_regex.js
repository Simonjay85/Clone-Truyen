const content = `

Chương 1: Sụp đổ

Chương 1: Sụp đổ

[TEASER SEO]: Cô dâng cả thanh xuân cho hắn, hắn đưa cô lên đỉnh cao rồi đạp xuống vực.
`;

let cleanContent = content.trim();
const titleRegex = new RegExp(`^(?:\\s*)*(?:#+\\s*)?(?:\\*\\*)?(?:Chương|Tập|Episode)\\s*\\d+[:\\-]?\\s*([^\\n]*)(?:\\*\\*)?(?:\\s*)*`, 'i');

while (titleRegex.test(cleanContent)) {
  cleanContent = cleanContent.replace(titleRegex, '').trim();
}

console.log("CLEAN CONTENT:\n" + cleanContent);
