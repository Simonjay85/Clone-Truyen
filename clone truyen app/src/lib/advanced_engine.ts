/* eslint-disable @typescript-eslint/no-explicit-any */
import { callGemini, callOpenAI, callGrok, callClaude, callQwen, callDeepSeek, STORY_IRON_RULES } from './engine';

// Helper to route dynamic calls
 
async function callDynamicEngine(engineSlug: string, params: any): Promise<any> {
  if (engineSlug === 'gemini') return callGemini(params);
  if (engineSlug === 'openai') return callOpenAI(params);
  if (engineSlug === 'grok') return callGrok(params);
  if (engineSlug === 'claude') return callClaude(params);
  if (engineSlug === 'qwen') return callQwen(params);
  if (engineSlug === 'deepseek') return callDeepSeek(params);
  throw new Error("Unknown engine: " + engineSlug);
}

const extractJson = (text: string) => {
  let t = text.trim();
  if (t.startsWith('```json')) t = t.replace('```json', '').replace(/```$/, '').trim();
  else if (t.startsWith('```')) t = t.replace('```', '').replace(/```$/, '').trim();
  return JSON.parse(t);
};

 
export async function agentConceptGenerator(engine: string, apiKey: string, model: string, criteria: unknown) {
  const sys = `Bạn là Concept Generator đỉnh cao. Nhiệm vụ: Sinh chính xác 20 concept ý tưởng truyện Micro-Drama siêu kịch tính, ngắn gọn. 
Focus: humiliation, betrayal, secret, class gap, revenge, comeback. Không viết dài lê thê.
Trả về nguyên gốc định dạng JSON ARRAY chứa 20 object, không bọc markdown. Mỗi object CÓ ĐÚNG các properties sau:
{
  "title": "Tên truyện giật gân",
  "hook": "Hook trong 3 dòng đầu",
  "trope": "Ví dụ: Tổng tài, Tu chân, Phản bội...",
  "core_conflict": "Cốt lõi mâu thuẫn",
  "twist": "Điểm lật bàn",
  "ending_type": "HE / SE / OE",
  "binge_score_reason": "Giải thích vì sao khán giả sẽ cày không dứt"
}
Lưu ý: Chỉ trả về JSON, không thêm chữ nào.`;

  const user = `Yêu cầu cụ thể của khách hàng / Thể loại: ${JSON.stringify(criteria)}\nHãy sinh đủ 20 concept đỉnh cao nhất.`;

  const res = await callDynamicEngine(engine, { apiKey, systemPrompt: sys + "\n\n" + STORY_IRON_RULES, userPrompt: user, jsonMode: true, temperature: 0.9, model });
  return extractJson(res.text);
}

 
export async function agentConceptScorer(engine: string, apiKey: string, model: string, concepts: unknown[], apiKey2?: string, apiKey3?: string) {
  const sys = `Bạn là Giám Khảo Tối Cao (Supreme Judge) khắc nghiệt nhất. Chấm điểm các concept trong mảng được đưa vào.
NHIỆM VỤ: Chấm điểm (1-10) và viết 1 dòng NHẬN XÉT CỰC KỲ GAY GẮT, CHỈ ĐÍCH DANH ĐIỂM YẾU/MẠNH.
TUYỆT ĐỐI KHÔNG DÙNG VĂN MẪU kiểu "Hook rõ, pain mạnh". PHẢI nhắc trực tiếp đến tình tiết Plot Twist hoặc Bối cảnh của chính kịch bản đó. Nếu motif sáo rỗng, vả mặt chưa đủ đau, hãy chê thậm tệ và trừ điểm. Nếu độc đáo, bạo não, thưởng điểm.
Trả về JSON đúng cấu trúc mảng:
{
  "scores": [
    {"index": 0, "title": "...", "score": 9.5, "reason": "Nhận xét chi tiết gay gắt..."}
  ],
  "winner_index": 0
}`;

  const user = JSON.stringify(concepts.map((c, i) => ({ index: i, ...(c as any) })));
  
  const res = await callDynamicEngine(engine, { apiKey, apiKey2, apiKey3, systemPrompt: sys + "\n\n" + STORY_IRON_RULES, userPrompt: user, jsonMode: true, temperature: 0.2, model });
  return extractJson(res.text);
}

 
export async function agentSeasonArchitect(engine: string, apiKey: string, model: string, winningConcept: unknown) {
  const sys = `Bạn là Season Architect. Nhiệm vụ: Thiết kế toàn bộ Story Bible và Dàn ý (Timeline) 30 tập cho concept thắng cuộc. Ưu tiên logic chặt chẽ, không cần bay bướm văn vẻ.
QUY TẮC CỐT LÕI TỪ NHÀ SẢN XUẤT: Bắt buộc thiết kế một chương 'Phản đòn' từ phe phản diện khiến nữ chính bị lộ tẩy hoặc đẩy vào chân tường trước khi cô lật kèo! VỀ TIÊU ĐỀ CHƯƠNG: TUYỆT ĐỐI KHÔNG dùng lặp lại quá 2 lần các từ chung chung như 'Bí mật', 'Bí ẩn', 'Cuộc gặp', 'Bất ngờ'. BẮT BUỘC dùng cấu trúc ĐỘNG TỪ MẠNH, SÁT THƯƠNG CAO ở mỗi đầu chương (Ví dụ: Bóc phốt, Lột mặt nạ, Tước đoạt, Đập tan tành, Xé nát sự thật, Bẫy gông cùm...).
Tuyệt đối CHỈ trả về JSON nguyên bản (không bọc \`\`\`json), format chuẩn:
{
  "series_premise": "...",
  "character_bible": "... (BẮT BUỘC GHI RÕ TÊN TỪNG NHÂN VẬT VÀ YÊU CẦU CẤM ĐỔI TÊN)",
  "hidden_secrets_map": "...",
  "emotional_escalation_ladder": "...",
  "forbidden_inconsistencies": "... (BẮT BUỘC GHI RÕ: KHÔNG ĐƯỢC THAY ĐỔI TÊN NHÂN VẬT DÙ CHỈ 1 CHỮ, PHẢN DIỆN PHẢI THÔNG MINH KHÔNG MẮC LỖI VỚ VẨN)",
  "reveal_schedule": "...",
  "timeline": [
    { "episode": 1, "title": "Tên chương giật tít", "outline": "Beat của tập" }
  ]
}
Lưu ý: timeline PHẢI có đủ 30 object (30 episodes).`;
  
  const user = `Concept thắng cuộc: ${JSON.stringify(winningConcept)}\nHãy xây dựng Kinh thánh, luật lệ thế giới và mẩu dàn ý mâu thuẫn khốc liệt cho 30 episode beats.`;

  const res = await callDynamicEngine(engine, { apiKey, systemPrompt: sys + "\n\n" + STORY_IRON_RULES, userPrompt: user, jsonMode: true, temperature: 0.4, model });
  return extractJson(res.text);
}

 
export async function agentEpisodeDrafter(engine: string, apiKey: string, model: string, bible: unknown, epNum: number, currentBeat: string, prevContext: string = '') {
  const sys = `Bạn là Episode Drafter của Micro-Drama. Nhiệm vụ: Dựa vào Bible và Beat của tập hiện tại, hãy viết nháp thô (draft).
QUY TẮC SỐNG CÒN:
1. Áp dụng triệt để quy tắc Show, Don't Tell: TUYỆT ĐỐI CẤM SỬ DỤNG NGOẶC ĐƠN hay các từ miêu tả cảm xúc sáo rỗng như (Lúng túng), (Giận dữ). Thay vì nói 'hắn ta rất giận dữ', hãy miêu tả 'hắn hất tung cốc nước nóng vào mặt cô'.
2. Tỉ lệ hội thoại phải chiếm ít nhất 60% thời lượng chương. Các nhân vật phải cãi vã, châm biếm, sắc bén. NHƯNG PHẦN VĂN MIÊU TẢ CẢM XÚC VÀ HÀNH ĐỘNG BẮT BUỘC PHẢI VIẾT THÀNH NHỮNG CÂU GHÉP DÀI MƯỢT MÀ, MỘT ĐOẠN VĂN GỘP CHUNG 4-6 CÂU. TUYỆT ĐỐI KHÔNG VIẾT CÂU MINH HỌA NGẮN NGỦN RỚT DÒNG CỘC LỐC.
3. ĐỘC MIỆNG HÀO MÔN: Đặc sản của Micro-Drama Việt là thâm thúy, chửi xéo, mỉa mai cay nghiệt. Phải dùng từ ngữ gai góc, xéo xắt, toxic cho phản diện.
4. CHIỀU DÀI: ĐÒI HỎI BẮT BUỘC 1000 - 2000 CHỮ (TRUNG BÌNH 1500 CHỮ) VÀ KHÔNG ĐƯỢC NGẮN HƠN 1000 CHỮ DÙ TRỜI CÓ SẬP XUỐNG (Mệnh lệnh cờ sinh tử).
5. MÓC CÂU (CLIFFHANGER): Kết thúc tập LUÔN bằng 1 câu MÓC CÂU khiến khán giả rợn người muốn coi tiếp (tin nhắn lạ, cuộc điện thoại bí ẩn...). Focus vào hành động chà đạp, hắt hủi nảy lửa.
6. LUẬT TÊN NHÂN VẬT (TỬ HÌNH NẾU PHẠM): TUYỆT ĐỐI KHÔNG ĐƯỢC TỰ Ý ĐỔI TÊN NHÂN VẬT. Phải đọc kỹ Character Bible bên dưới. Ai tên gì giữ nguyên tên đó (VD: Thành không được đổi thành Trí, Mai Anh không được đổi thành Mai Hương).
7. LUẬT PHẢN DIỆN: Phản diện PHẢI CỰC KỲ THÔNG MINH. Cấm viết tình tiết phản diện dán mật khẩu lên cửa, hay dùng mật khẩu ngày sinh. Main phải chật vật mới lấy được bằng chứng.
Trả về Text thuần.`;

  const user = `--- SYSTEM CORE & BIBLE (CACHE BLOCK) ---
Series Premise: ${(bible as any).series_premise}
Character Bible (TÊN NHÂN VẬT - CẤM ĐỔI): ${(bible as any).character_bible}
Secrets Map: ${(bible as any).hidden_secrets_map}
Forbidden Inconsistencies: ${(bible as any).forbidden_inconsistencies}
${prevContext ? `\n--- TRÍCH ĐOẠN CUỐI TẬP TRƯỚC (ROLLING CONTEXT) ---\nNối tiếp liền mạch bối cảnh, cảm xúc và hành động của đoạn văn này:\n"${prevContext}"\n` : ''}
--- EPISODE TASK ---
Xây dựng Episode số ${epNum}.
Episode Beat: ${currentBeat}

Yêu cầu: Kết thúc tập luôn bằng 1 câu chốt cảm xúc (emotional cliffhanger) khiến khán giả muốn bấm Next ngay lập tức. Cấm nói đạo lý.`;

  const res = await callDynamicEngine(engine, { apiKey, systemPrompt: sys + "\n\n" + STORY_IRON_RULES, userPrompt: user, temperature: 0.6, model });
  return res.text;
}

export async function agentEpisodeRewriter(engine: string, apiKey: string, model: string, draft: string, emotionalEscalationLadder: string) {
  const sys = `Bạn là Episode Rewriter tài ba (Head Writer). Hãy tiếp nhận bản nháp thô (draft) và ép cực mạnh các rewrite rules của Micro-Drama: 
- CẤM TIỆT: Bất cứ dấu ngoặc đơn "( )" nào đang tóm tắt cảm xúc nhân vật (ví dụ: (Giận dữ), (Cười nhạt)) PHẢI ĐƯỢC XÓA BỎ và chuyển thành miêu tả ngôn ngữ cơ thể (Ví dụ: "hắn cong môi", "mắt nổi vằn đỏ").
- CẤM TIỆT: Xóa sạch 100% các câu văn tả không gian, thời tiết vô thưởng vô phạt (Nắng dịu, đèn lấp lánh).
- Stronger humiliation (Xỉ nhục tàn nhẫn hơn).
- Sharper emotional contrast (Tương phản cảm xúc gắt hơn).
- Thoại của nhân vật ngắn gọn sắc bén (NHƯNG phần văn miêu tả không gian, hành động, tâm lý thì PHẢI VIẾT BẰNG CÂU GHÉP DÀI MƯỢT MÀ, KHÔNG ĐƯỢC CỘC LỐC).
- Stronger cliffhanger (Lưỡi lam ở cuối tập phải gài kỹ hơn).
Tuyệt đối KHÔNG chào hỏi, KHÔNG giải thích. CHỈ TRẢ VỀ NỘI DUNG SAU KHI SỬA DƯỚI DẠNG MARKDOWN.`;

  const user = `--- BỘ LỌC CẢM XÚC SERIES ---
Chiến lược leo dốc cảm xúc chung: ${emotionalEscalationLadder}

--- DRAFT GỐC TẬP ---
${draft}

Hãy gọt giũa và đẩy kịch tính lên đỉnh ngay bây giờ!`;

  const res = await callDynamicEngine(engine, { apiKey, systemPrompt: sys + "\n\n" + STORY_IRON_RULES, userPrompt: user, temperature: 0.5, model });
  return res.text;
}

export async function agentContinuityChecker(engine: string, apiKey: string, model: string, episodesContext: string, bibleStr: string) {
  const sys = `Bạn là Lính Soi Sạn (Continuity Checker). Hãy đọc cục dữ liệu 5 tập truyện vừa phát hành và đối chiếu với cốt truyện gốc (Bible). 
Phát hiện: 
- Timeline mismatch (sai lịch trình thời gian).
- Accidental reveal too early (lộ bí mật quá sớm chưa tới lúc).
- Character voice drift (nhân vật tự dưng nói chuyện không giống bản chất).
- Repeated conflict loop (cãi nhau vòng vo không lối thoát).
- Emotional logic gap (cảm xúc lố, chuyển pha không logic).
KHÔNG SỬA, chỉ phát hiện và trả về JSON Error Logs (nếu ổn, hãy trả mảng rỗng). Format chuẩn: {"issues": ["Lỗi 1", "Lỗi 2"]}`;

  const user = `--- BIBLE GỐC ---
${bibleStr}

--- QUÁ TRÌNH 5 TẬP QUA ---
${episodesContext}

Dò cặn kẽ và lập danh sách các lỗ hổng cần vá.`;
  
  const res = await callDynamicEngine(engine, { apiKey, systemPrompt: sys + "\n\n" + STORY_IRON_RULES, userPrompt: user, jsonMode: true, temperature: 0.1, model });
  return extractJson(res.text);
}

export async function agentMarketingAssets(engine: string, apiKey: string, model: string, summary: string) {
  const sys = `Marketing Assets Generator. Hãy thiết kế Tên Series, Blurb (Mô tả giật gân TikTok/FB để hút leads) và Tags cho nội dung. JSON thuần túy, format: {"title": "", "blurb": "", "tags": ["", ""]}`;
  const res = await callDynamicEngine(engine, { apiKey, systemPrompt: sys + "\n\n" + STORY_IRON_RULES, userPrompt: summary, jsonMode: true, temperature: 0.8, model });
  return extractJson(res.text);
}


export async function agentPremiumPolish(engine: string, apiKey: string, model: string, draft: string) {
  const sys = `Premium Polish Mode. Bạn là chuyên gia chải chuốt văn phong sâu sắc.
Hãy đọc lại bản draft này và viết lại sao cho câu chữ thật mượt mà, chạm đáy cảm xúc, giữ nguyên hoàn toàn tiết tấu/twist nhưng thay bộ cánh ngôn từ sang trọng hơn xịn hơn.
Đặc biệt chú ý TIÊU DIỆT TẬN GỐC lỗi Telling (những câu ngoặc đơn miêu tả cảm xúc kịch bản) và lỗi Văn Lan Man (tả cảnh thiên nhiên).
Chỉ trả Text (Markdown), không mào đầu.`;

  const user = `--- DRAFT ---
${draft}

Hãy phủ bóng màn đêm và mài sắc lưỡi dao cảm xúc!`;

  const res = await callDynamicEngine(engine, { apiKey, systemPrompt: sys + "\n\n" + STORY_IRON_RULES, userPrompt: user, model, temperature: 0.4 });
  return res.text;
}

 
export async function agentPitchRefiner(engine: string, apiKey: string, model: string, originalPitch: unknown, feedback: string, apiKey2?: string, apiKey3?: string) {
  const sys = `Bạn là Chuyên Gia Cứu Vãn Kịch Bản (Script Doctor) của Micro-Drama.
Nhiệm vụ: Phẫu thuật và viết lại toàn bộ kịch bản gốc sao cho HẤP THU ĐƯỢC 100% GÓP Ý TỪ ĐẠO DIỄN NÀY, đẩy độ "bạo não", twist và sỉ nhục lên tầm cao nhất, logic sắc bén không tì vết.
TUYỆT ĐỐI KHÔNG DÙNG TỪ TIẾNG ANH (Ví dụ: Kawaii -> Đáng Yêu, Steampunk -> Cơ Khí Cổ Đại). 100% Tiếng Việt hoặc Hán Việt.
BẮT BUỘC TRẢ VỀ JSON OBJECT DƯỚI ĐÂY (duy trì số lượng trường như cũ):
{
  "super_title": "Tên truyện cực ngầu",
  "summary": "Tóm tắt truyện đầy cay nghiệt (3 câu)",
  "worldSettings": "Bối cảnh giật gân",
  "characterArc": "Vết thương lòng/Sự phẫn uất",
  "plotTwists": "Cú lật bàn không ai ngờ/Phản bội tàn nhẫn",
  "overallSizzle": "Điểm chốt hạ độ bạo não"
}`;

  const user = `--- KỊCH BẢN GỐC (DỞ/CẦN SỬA) ---
${JSON.stringify(originalPitch)}

--- YÊU CẦU/GÓP Ý CỦA ĐẠO DIỄN CẦN PHẢI DỰA VÀO ĐỂ SỬA ---
${feedback}

Hãy đập đi xây lại kịch bản này ngay bây giờ! Chỉ trả về JSON không format code block.`;

  const res = await callDynamicEngine(engine, { apiKey, apiKey2, apiKey3, systemPrompt: sys + "\n\n" + STORY_IRON_RULES, userPrompt: user, jsonMode: true, temperature: 0.8, model });
  return extractJson(res.text);
}

 
export async function agentStoryEvaluator(engine: string, apiKey: string, model: string, bible: unknown, chaptersContent?: unknown[]) {
  const sys = `Bạn là Tổng Biên Tập siêu khó tính (Gatekeeper) của một nền tảng đọc truyện mạng hàng đầu. 
Nhiệm vụ: Đọc toàn bộ hồ sơ thiết kế truyện (Story Bible) và NỘI DUNG TẤT CẢ CÁC CHƯƠNG ĐÃ VIẾT (nếu có).
Hãy kiểm tra xem truyện có bám sát thiết lập ban đầu không, có mắc lỗi Plot Hole không, và mức độ cuốn hút (Sizzle) ở thực tế ra sao.
{
  "score": "Điểm từ 1 đến 10",
  "review": "Bài Review dài khoảng 10-15 câu, phân tích gay gắt ưu nhược điểm, độ cuốn hút, plot hole, có thật sự gây cảm xúc mạnh ở từng tập như hứa hẹn hay không.",
  "promptSuggestion": "Phân tích xem Prompt/Keywords gốc đã đủ tốt chưa. Nếu chưa, hãy gợi ý một Prompt hoặc cốt truyện mới xuất sắc hơn để tác giả đập đi làm lại."
}`;

  let user = `Hồ sơ Truyện (Bible):\n${JSON.stringify(bible)}`;
  if (chaptersContent && chaptersContent.length > 0) {
      user += `\n\n--- THỰC TẾ NỘI DUNG TỪNG CHƯƠNG ĐÃ VIẾT ---\n`;
      chaptersContent.forEach((ch: any) => {
          user += `\n[${(ch as any).title}]\n${(ch as any).content}\n`;
      });
  }
  
  const res = await callDynamicEngine(engine, { apiKey, systemPrompt: sys + "\n\n" + STORY_IRON_RULES, userPrompt: user, jsonMode: true, temperature: 0.3, model });
  return extractJson(res.text);
}

 
export async function agentPublisherMetadata(engine: string, apiKey: string, model: string, bible: unknown, title: string) {
  const sys = `Bạn là Chuyên Gia Xuất Bản & SEO Master.
Nhiệm vụ: Truyện đã hoàn thành và chuẩn bị đưa lên WordPress. Hãy sinh ra Siêu dữ liệu SEO (RankMath), Từ khóa, Danh mục, và một câu Prompt bằng tiếng Anh để AI vẽ Ảnh bìa (Cover Image).
YÊU CẦU JSON:
{
  "finalTitle": "Tên truyện tối ưu nhất để giật title",
  "seoTitle": "Tiêu đề chuẩn SEO (có độ cuốn hút, click-bait)",
  "seoDescription": "Mô tả SEO tóm tắt nội dung gây tò mò (khoảng 150 ký tự)",
  "seoFocusKeyword": "Từ khóa chính (1-2 từ khóa)",
  "categories": ["Danh mục 1", "Danh mục 2"],
  "tags": ["Từ khoá 1 (ngắn 1-2 từ)", "Từ khoá 2 (ngắn 1-2 từ)", "Từ khoá 3 (VD: Phản bội, Trùng sinh)"],
  "coverImagePrompt": "Mô tả ảnh bìa BẰNG TIẾNG ANH, chi tiết, cinematic, vivid colors, mô tả bối cảnh và ngoại hình nhân vật chính để Gen bằng AI.",
  "blurb": "Đoạn văn giới thiệu truyện (Văn án), ngôn từ cực kỳ giật gân, có hook câu khách ở đầu và bỏ lửng tạo tò mò ở cuối để độc giả muốn lao vào đọc ngay. Tuyệt đối KHÔNG ĐỂ LỘ HẬU TRƯỜNG kiểu như 'Cú twist là...'. Chỉ viết kiểu teaser."
}
* Categories tiêu biểu (ưu tiên trúng 1 trong các danh mục gốc): Ngôn Tình, Tiên Hiệp, Huyền Ảo, Kinh Dị, Đam Mỹ / Bách Hợp, Romantasy, Khoa Học Viễn Tưởng, Đoản Văn Zhihu, Kịch Tính... Có thể kèm thêm tối đa 2 danh mục phụ.`;

  const user = `Tên gốc: ${title}\nHồ sơ Truyện:\n${JSON.stringify(bible)}`;
  
  const res = await callDynamicEngine(engine, { apiKey, systemPrompt: sys + "\n\n" + STORY_IRON_RULES, userPrompt: user, jsonMode: true, temperature: 0.7, model });
  return extractJson(res.text);
}
