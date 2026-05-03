/* eslint-disable @typescript-eslint/no-explicit-any */
import { callGemini, callOpenAI, callGrok, callClaude, callQwen, callDeepSeek, callOpenRouter, STORY_IRON_RULES } from './engine';

// Helper to route dynamic calls
 
async function callDynamicEngine(engineSlug: string, params: any): Promise<any> {
  if (engineSlug === 'gemini') return callGemini(params);
  if (engineSlug === 'openai') return callOpenAI(params);
  if (engineSlug === 'grok') return callGrok(params);
  if (engineSlug === 'claude') return callClaude(params);
  if (engineSlug === 'qwen') return callQwen(params);
  if (engineSlug === 'deepseek') return callDeepSeek(params);
  if (engineSlug === 'openrouter') return callOpenRouter(params);
  throw new Error("Unknown engine: " + engineSlug);
}

const extractJson = (text: string) => {
  let t = (text || '').trim();
  t = t.replace(/<think>[\s\S]*?<\/think>/gi, '').trim();
  t = t.replace(/^```(?:json)?\s*/i, '').replace(/```\s*$/i, '').trim();

  const tryParse = (raw: string) => JSON.parse(raw);
  try {
    return tryParse(t);
  } catch {
    // DeepSeek Reasoner can still add a short preface. Extract the first
    // balanced JSON object/array instead of falling back to unusable raw text.
    const start = t.search(/[\{\[]/);
    if (start === -1) throw new Error('No JSON object or array found in model output');
    let inString = false;
    let escaped = false;
    const stack: string[] = [];

    for (let i = start; i < t.length; i++) {
      const ch = t[i];
      if (inString) {
        if (escaped) {
          escaped = false;
        } else if (ch === '\\') {
          escaped = true;
        } else if (ch === '"') {
          inString = false;
        }
        continue;
      }

      if (ch === '"') {
        inString = true;
        continue;
      }
      if (ch === '{' || ch === '[') {
        stack.push(ch);
        continue;
      }
      if (ch === '}' || ch === ']') {
        const open = stack.pop();
        if ((open === '{' && ch !== '}') || (open === '[' && ch !== ']')) break;
        if (stack.length === 0) {
          const slice = t.slice(start, i + 1);
          return tryParse(slice);
        }
      }
    }
    throw new Error('Could not extract balanced JSON from model output');
  }
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
QUY TẮC CỐT LÕI TỪ NHÀ SẢN XUẤT:
1. Bắt buộc thiết kế một chương 'Phản đòn' từ phe phản diện khiến nữ chính bị lộ tẩy hoặc đẩy vào chân tường trước khi cô lật kèo! 
2. VỀ TIÊU ĐỀ CHƯƠNG: TUYỆT ĐỐI KHÔNG dùng lặp lại quá 2 lần các từ chung chung như 'Bí mật', 'Bí ẩn', 'Cuộc gặp', 'Bất ngờ'. BẮT BUỘC dùng cấu trúc ĐỘNG TỪ MẠNH, SÁT THƯƠNG CAO ở mỗi đầu chương (Ví dụ: Bóc phốt, Lột mặt nạ, Tước đoạt, Đập tan tành, Xé nát sự thật, Bẫy gông cùm...).
3. QUY TẮC VỀ TÊN NHÂN VẬT (QUAN TRỌNG NHẤT): TẤT CẢ các nhân vật (chính, phụ, phản diện) ĐỀU PHẢI ĐƯỢC TẠO HỌ VÀ TÊN ĐẦY ĐỦ (Ví dụ: Nguyễn Thùy Linh thay vì chỉ Linh, Trần Minh Khải thay vì chỉ Khải). Tuyệt đối không để thiếu Họ, tránh việc AI tự bịa họ trong các tình tiết cần văn bản pháp lý.

Tuyệt đối CHỈ trả về JSON nguyên bản (không bọc \`\`\`json), format chuẩn:
{
  "series_premise": "...",
  "character_bible": "... (BẮT BUỘC GHI RÕ HỌ VÀ TÊN ĐẦY ĐỦ CỦA TỪNG NHÂN VẬT VÀ GHI RÕ YÊU CẦU CẤM ĐỔI TÊN)",
  "hidden_secrets_map": "...",
  "emotional_escalation_ladder": "...",
  "forbidden_inconsistencies": "... (BẮT BUỘC GHI RÕ: KHÔNG ĐƯỢC THAY ĐỔI TÊN HAY HỌ CỦA NHÂN VẬT DÙ CHỈ 1 CHỮ, PHẢN DIỆN PHẢI THÔNG MINH KHÔNG MẮC LỖI VỚ VẨN)",
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

export async function agentStoryFixer(
    engine: string, 
    apiKey: string, 
    model: string, 
    bible: unknown, 
    chapterText: string, 
    critique: string = '', 
    fullStoryContext: string = ''
) {
  const sys = `Bạn là một Tiểu Thuyết Gia Thiên Tài kiêm Master Editor chuyên tu sửa kịch bản.
Nhiệm vụ: Nhận bản thảo của một chương truyện đang bị lỗi và Lời Phê Bình. Bạn phải SỬA CHỮA, TINH CHỈNH VÀ VIẾT LẠI chương này để khắc phục triệt để các lỗi được nêu, ĐỒNG THỜI giữ lại những tình tiết tốt của bản gốc.

CÁC QUY TẮC SỐNG CÒN KHI VIẾT LẠI:
1. BẢO TỒN CỐT TRUYỆN GỐC TỐT: Đừng đập bỏ những đoạn văn đã viết tốt. Chỉ viết lại những đoạn bị chê trách, tối ưu câu chữ, và giữ mạch truyện mạch lạc.
2. KHẮC PHỤC LỖI TẬN GỐC: Đọc kỹ Lời Phê Bình. Nếu chê thiếu logic, phải thêm chi tiết logic. Nếu chê hội thoại sến súa, phải sửa lại thành sắc bén, cay nghiệt, đời thường. Nếu chê Mary Sue, phải để Main chịu thiệt thòi thật sự trước khi lật kèo.
3. DIỆT TRỪ ĐỘC THOẠI NỘI TÂM: Thay các câu "Tôi nghĩ", "Tôi cảm thấy" bằng hành động vật lý hoặc lời thoại.
4. QUY TẮC 70% HỘI THOẠI: Tăng cường đối thoại bóng bàn, cắt bớt miêu tả dài dòng.
5. CLIFFHANGER KẾT CHƯƠNG: Câu cuối cùng của chương phải là một cú sốc đứt ruột.
6. TRẢ VỀ DUY NHẤT VĂN BẢN ĐÃ VIẾT LẠI. Bắt đầu bằng (Chương X:), giữ thẻ HTML (<p>, <i>...).`;

  let user = `--- STORY BIBLE (THIẾT LẬP GỐC) ---\n${JSON.stringify(bible)}\n\n`;
  if (critique) {
      user += `--- LỜI PHÊ BÌNH TỪ GATEKEEPER CẦN KHẮC PHỤC TRIỆT ĐỂ ---\n${critique}\n\n`;
  }
  if (fullStoryContext) {
      user += `--- NGỮ CẢNH TOÀN TRUYỆN (ĐỌC ĐỂ BIẾT TRƯỚC/SAU) ---\n${fullStoryContext}\n\n`;
  }
  user += `--- BẢN NHÁP CẦN SỬA ---\n${chapterText}`;

  const res = await callDynamicEngine(engine, { apiKey, systemPrompt: sys + "\n\n" + STORY_IRON_RULES, userPrompt: user, model, temperature: 0.7 });
  let fixedText = res.text.trim();
  if (fixedText.startsWith("```")) {
    fixedText = fixedText.replace(/^```[a-z]*\n/i, '').replace(/\n```$/, '');
  }
  return fixedText;
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

import {
  getStoryBiblePrompt,
  getChapterMapPrompt,
  getChapterWriterPrompt,
  getChapterRewriterPrompt,
  getIronRulesCheckerPrompt,
  getFinalAuditPrompt,
  isFaceSlapStr
} from './reasonerPrompts';

export async function agentGenerateBible(
  engine: string,
  apiKey: string,
  model: string,
  genres: string[],
  userPrompt: string,
  targetChapters = 15
) {
  const genreStr = genres.join(', ') || 'Zhihu / Kịch tính';
  const isFaceSlap = isFaceSlapStr(genreStr) || isFaceSlapStr(userPrompt);
  const chapterCount = Number.isFinite(targetChapters) && targetChapters > 0 ? targetChapters : 15;

  const params = {
    genre: genreStr,
    chapter_count: chapterCount,
    main_hook: userPrompt,
    protagonist_seed: isFaceSlap 
      ? 'Nhân vật chính có thân phận/quyền lực thật nhưng phải cải trang hoặc chịu nhục để điều tra. Main mạnh nhưng bị giới hạn bởi pháp lý, bằng chứng và an toàn đồng minh.'
      : 'Nữ chính mạnh mẽ, bị tổn thương nhưng không gục ngã',
    villain_seed: isFaceSlap
      ? 'Kẻ phản diện kiêu ngạo, hám tiền, hay khinh người, luôn tự đắc và sẽ bị vả mặt cực đau.'
      : 'Kẻ phản diện thông minh, có địa vị',
    setting: 'Việt Nam hiện đại',
    tone: isFaceSlap 
      ? 'Sảng văn, vả mặt cực gắt nhưng logic thực tế: bằng chứng có giá, phản diện biết phản công, pháp lý không giải quyết trong một cuộc gọi.'
      : 'Nhanh, sắc, cảm xúc thật',
    special_requirements: isFaceSlap
      ? 'Cấm hacker ma thuật, cấm đổi tên nhân vật, cấm đổi địa lý giữa các chương, cấm Change Log/State JSON lẫn vào nội dung truyện.'
      : 'Cấm đổi tên nhân vật, cấm đổi địa lý giữa các chương.',
  };
  const sys = getStoryBiblePrompt(params);
  const res = await callDynamicEngine(engine, {
    apiKey,
    systemPrompt: sys,   // No STORY_IRON_RULES here — saves tokens
    userPrompt: `User story idea: ${userPrompt}\n\nGenres: ${genres.join(', ')}\n\nCreate the Story Bible now. Output as valid JSON only.`,
    jsonMode: true,
    temperature: 0.45,
    model,
    taskType: 'story_bible',
  });
  // Parse JSON safely
  let data: any = null;
  try { data = extractJson(res.text); } catch { data = { raw: res.text }; }
  return { text: data?.raw ? res.text : JSON.stringify(data, null, 2), data, usedModel: res.chosenModel || model };
}

export async function agentGenerateChapterMap(
  engine: string,
  apiKey: string,
  model: string,
  bibleObjOrString: any,
  chapter_count: number
) {
  const bibleStr = typeof bibleObjOrString === 'string'
    ? bibleObjOrString
    : JSON.stringify(bibleObjOrString, null, 2);
  const sys = getChapterMapPrompt(bibleStr, chapter_count);
  const res = await callDynamicEngine(engine, {
    apiKey,
    systemPrompt: sys,   // No STORY_IRON_RULES — saves tokens
    userPrompt: `Create the Chapter Map for ${chapter_count} chapters now. Output as JSON array of chapter objects.`,
    jsonMode: true,
    temperature: 0.45,
    model,
    taskType: 'chapter_map',
  });
  let data: any = null;
  try {
    const parsed = extractJson(res.text);
    const rawMap = Array.isArray(parsed) ? parsed : (parsed?.chapters || parsed?.chapter_map || [parsed]);
    data = rawMap.map((ch: any, idx: number) => ({
      chapter: Number(ch.chapter || ch.chapter_number || ch.episode || idx + 1),
      title: ch.title || ch.chapter_title || `Chương ${idx + 1}`,
      type: ch.type || ch.chapter_type || ch.functionTag || ch.function_tag || 'BUILD',
      chapter_type: ch.chapter_type || ch.type || ch.functionTag || ch.function_tag || 'BUILD',
      functionTag: ch.functionTag || ch.function_tag || ch.FunctionTag || ch.type || 'BUILD',
      protagonist_goal: ch.protagonist_goal || ch.goal || ch.protagonistGoal || '',
      main_obstacle: ch.main_obstacle || ch.obstacle || ch.mainObstacle || '',
      evidence_or_loss: ch.evidence_or_loss || ch.evidenceOrLoss || ch.evidence_loss || '',
      beats: ch.beats || ch.key_beats || ch.beat_sheet || [],
      win: ch.win || '',
      loss: ch.loss || ch.loss_misread || '',
      foreshadowing: ch.foreshadowing || '',
      cliffhanger: ch.cliffhanger || ch.final_question || '',
      identityRevealLayer: ch.identityRevealLayer || ch.identity_reveal_layer || '',
    }));
  } catch { data = []; }
  return { text: data.length ? JSON.stringify(data, null, 2) : res.text, data, usedModel: res.chosenModel || model };
}

export async function agentWriteChapter(
  engine: string,
  apiKey: string,
  model: string,
  bibleObjOrString: any,
  beat: any,
  prevContext = '',
  riskLevel = 'low',
  currentStateStr = '{}',
  totalChapters = 14
) {
  const bibleStr = typeof bibleObjOrString === 'string'
    ? bibleObjOrString
    : JSON.stringify(bibleObjOrString, null, 2);

  // ── Build structured previous-chapter context from currentState ──────────
  // This is the #1 fix: instead of just sending raw tail-text (500 chars),
  // we inject a structured summary so the writer knows EXACTLY what happened
  // last chapter and cannot accidentally duplicate it.
  let structuredPrevContext = prevContext;
  try {
    const st = JSON.parse(currentStateStr || '{}');
    const prevChNum   = st.chapterNumber   || '?';
    const prevFnTag   = st.chapterFunction || '?';
    const revealLayer = st.identityRevealLayer || '?';
    const evidenceList = Array.isArray(st.validEvidence)
      ? st.validEvidence.map((e: any) => typeof e === 'string' ? e : e?.name || JSON.stringify(e)).join(', ')
      : (Array.isArray(st.mainHas) ? st.mainHas.join(', ') : '');
    const openThreads = Array.isArray(st.openThreads) ? st.openThreads.join(' | ') : '';
    const villainKnows = Array.isArray(st.villainKnows) ? st.villainKnows.join(', ') : '';
    const mainLost     = Array.isArray(st.mainLost)     ? st.mainLost.join(', ') : '';
      // Character name map — prevents AI from renaming characters mid-story
    const charMap = st.characterMap || {};
    const roleRows = Array.isArray(st.fixedFacts?.characterRoles)
      ? st.fixedFacts.characterRoles.map((r: any) => `  ${r.name}: ${r.role || ''}${r.status ? ` — ${r.status}` : ''}`).join('\n')
      : '';
    const charMapStr = Object.entries(charMap).map(([role, name]) => `  ${role}: ${name}`).join('\n') || roleRows;
    // Villain arrest status — prevents double-arrest bug
    const villainArrested = st.villainArrested || '';

    structuredPrevContext = [
      `[PREVIOUS CHAPTER LOCK — Ch.${prevChNum}]`,
      `FunctionTag: ${prevFnTag}   ← chương hiện tại PHẢI dùng tag KHÁC`,
      `IdentityRevealLayer hiện tại: ${revealLayer}`,
      charMapStr ? `[CHARACTER NAME MAP — PHẢI dùng ĐÚNG tên này, KHÔNG đổi]\n${charMapStr}` : '',
      villainArrested ? `⚠️ VILLAIN STATUS: ${villainArrested} — KHÔNG viết villain này xuất hiện tự do nếu đã bị bắt/giam` : '',
      `ValidEvidence (đã có — KHÔNG thu thập lại): ${evidenceList || 'chưa có'}`,
      `MainLost (đã mất — KHÔNG lấy lại tức thì): ${mainLost || 'chưa mất gì'}`,
      `VillainKnows (villain đã biết): ${villainKnows || 'chưa có'}`,
      `OpenThreads chưa giải quyết: ${openThreads || 'chưa có'}`,
      `--- KẾT THÚC CHƯƠNG TRƯỚC (500 ký tự) ---`,
      prevContext.slice(-500),
    ].filter(Boolean).join('\n');
  } catch {
    // currentState unparseable — fall back to raw text
    structuredPrevContext = prevContext;
  }

  const params = {
    story_bible: bibleStr,
    chapter_map: JSON.stringify(beat),
    chapter_number: beat?.chapter || 1,
    chapter_title: beat?.title || '',
    chapter_type: beat?.type || 'ACTION',
    chapter_beats: JSON.stringify(beat?.beats || beat?.key_beats || []),
    previous_summary: structuredPrevContext,
    current_state: currentStateStr,
  };
  const sys = getChapterWriterPrompt(params);
  const currentChapter = beat?.chapter || 1;
  const revealGateChapter = Math.ceil(totalChapters * 0.6); // 60% mark

  // Detect if identity has already been revealed from structured state only.
  // Keyword-scanning previous prose produced false positives for ordinary words
  // like "chủ tịch" before the actual public reveal.
  let revealAlreadyHappened = false;
  try {
    const st = JSON.parse(currentStateStr || '{}');
    const rl = (st.identityRevealLayer || '').toLowerCase();
    const publicIdentityKnown = st.publicIdentityKnown === true || st.identityPublic === true;
    const revealedAtChapter = Number(st.revealedAtChapter || st.identityRevealedAt || 0);
    if (publicIdentityKnown || revealedAtChapter > 0 || rl.includes('4') || rl.includes('công khai') || rl.includes('lộ diện')) {
      revealAlreadyHappened = true;
    }
  } catch { /* ignore */ }

  // Detect villain arrested status
  let villainArrestedBanner = '';
  try {
    const st = JSON.parse(currentStateStr || '{}');
    if (st.villainArrested) {
      villainArrestedBanner = `⚠️ VILLAIN ĐÃ BỊ BẮT: ${st.villainArrested}
KHÔNG ĐƯỢC viết villain này xuất hiện tự do, ngồi họp, hoặc hành động bên ngoài.
Nếu villain cần xuất hiện → chỉ trong phòng giam, phòng đối chất, hoặc qua lời khai.\n\n`;
    }
  } catch { /* ignore */ }

  let revealBanner = '';
  if (revealAlreadyHappened) {
    revealBanner = `🚫🚫🚫 CẢNH BÁO TUYỆT ĐỐI — IDENTITY ĐÃ LỘ 🚫🚫🚫
Main ĐÃ lộ thân phận chủ tịch ở chương trước. MỌI NGƯỜI ĐÃ BIẾT.
KHÔNG ĐƯỢC VIẾT: cởi áo shipper, giơ thẻ đen, tuyên bố "Tôi là chủ tịch", cảnh mọi người sốc khi biết main là ai.
Chương này PHẢI tiến triển SAU reveal: xử lý hậu quả, đối chất, hoặc villain phản công.
Nếu vi phạm → toàn bộ chương bị loại.\n\n`;
  } else if (currentChapter < revealGateChapter) {
    revealBanner = `🔒🔒🔒 REVEAL GATE — Chương ${currentChapter}/${totalChapters} — TUYỆT ĐỐI CHƯA LỘ THÂN PHẬN 🔒🔒🔒
Main PHẢI giữ vai shipper/nhân viên bình thường TOÀN BỘ chương này.

CẤM TUYỆT ĐỐI (cả HÀNH ĐỘNG lẫn KẾT QUẢ):
❌ Giơ thẻ đen, tuyên bố thân phận
❌ Bất kỳ nhân vật nào gọi main là "chủ tịch", "sếp lớn", "CEO", "boss"
❌ Villain biết/phát hiện/nghi ngờ main là chủ tịch
❌ Nhân viên (trừ trợ lý riêng) nói "thưa chủ tịch" hoặc biết thân phận thật
❌ Viết cảnh mọi người sốc khi biết main là ai
❌ Main ra lệnh với tư cách chủ tịch (chỉ được điều tra bí mật)
❌ Mở đầu chương với "villain đã biết main là chủ tịch" — KHÔNG ĐƯỢC skip reveal

CHỈ ĐƯỢC PHÉP:
✅ Main bị đối xử như shipper bình thường (bị mắng, bị khinh)
✅ Main điều tra bí mật, thu thập bằng chứng
✅ Trợ lý riêng/đồng minh đã ghi trong CHARACTER NAME MAP biết thân phận — nhưng CHỈ khi nói chuyện riêng
✅ Main ghi âm, chụp ảnh, quan sát

Reveal chỉ được phép TỪ CHƯƠNG ${revealGateChapter} TRỞ ĐI (60% truyện).
Nếu vi phạm bất kỳ điều nào ở trên → toàn bộ chương bị loại.\n\n`;
  }

  const res = await callDynamicEngine(engine, {
    apiKey,
    systemPrompt: sys,
    userPrompt: `${revealBanner}${villainArrestedBanner}Viết Chương ${currentChapter} ngay bây giờ theo đúng Story Bible, Chapter Map và Current State.

QUY TẮC OUTPUT SẠCH:
- KHÔNG in PRE-WRITE DECLARATION.
- KHÔNG in SELF-CHECK.
- KHÔNG in CHANGE LOG, Updated, Audit Report, hoặc lời giải thích kiểu "Dưới đây là phiên bản...".
- Chỉ được in đúng OUTPUT CONTRACT V1 trong system prompt: tiêu đề chương, teaser SEO, nội dung truyện, rồi STATE UPDATE JSON ở cuối.
- STATE UPDATE JSON phải là JSON hợp lệ, không bọc markdown fence, không comment, không trailing comma, và không có chữ nào sau dấu } cuối cùng.
- Địa lý, tên người, chức vụ, số tiền phải copy từ Story Bible/Current State. Nếu bối cảnh là TP.HCM/Quận 3 thì KHÔNG tự chuyển sang Hà Nội.

QUY TẮC BẮT BUỘC BỔ SUNG:

🔒 IDENTITY REVEAL ONCE-ONLY:
Nếu IdentityRevealLayer trong [CURRENT STATE LOCK] đã = "Tầng 4" hoặc "công khai" hoặc "lộ diện", hoặc publicIdentityKnown/revealedAtChapter đã có giá trị:
→ TUYỆT ĐỐI KHÔNG viết lại cảnh lộ thân phận. Main đã lộ rồi. Mọi nhân vật đã biết.
→ Không cởi áo shipper. Không giơ thẻ đen. Không tuyên bố "Tôi là chủ tịch" lần nữa.
→ Chương này phải tiến triển plot SAU reveal, không lặp lại reveal.

🔒 ANTI-REPEAT SCENE:
Không viết lại cảnh đã xảy ra ở chương trước. Kiểm tra [PREVIOUS CHAPTER LOCK]:
→ Nếu đã có [FACESLAP_BIG] → chương này KHÔNG faceslap cùng kiểu
→ Nếu đã có [IDENTITY_REVEAL] → chương này là HẬU QUẢ, không phải reveal lại
→ Nếu đã có [EVIDENCE_FOUND] → bằng chứng đó ĐÃ CÓ, không tìm lại

Viết chương bằng tiếng Việt. Show, don't tell. Kết thúc bằng STATE UPDATE JSON hợp lệ để app parse được.`,
    temperature: 0.7,
    model,
    taskType: 'chapter_writer',
    riskLevel,
  });
  return { text: res.text, usedModel: res.chosenModel || model };
}


export async function agentRewriteChapter(
  engine: string,
  apiKey: string,
  model: string,
  chapterContent: string,
  patchNotes: string,
  storyBible = '',
  currentState = '{}'
) {
  const params = {
    chapter_draft: chapterContent,
    audit_report: patchNotes,
    story_bible: storyBible,
    current_state: currentState,
  };
  const sys = getChapterRewriterPrompt(params);
  const res = await callDynamicEngine(engine, {
    apiKey,
    systemPrompt: sys,
    userPrompt: 'Revise the chapter now. Return only the revised story content. Do not include Change Log, Self-Check, Audit Report, or explanatory preface.',
    temperature: 0.65,
    model,
    taskType: 'chapter_rewriter',
  });
  return { text: res.text, usedModel: res.chosenModel || model };
}

export async function agentIronRulesV2(
  engine: string,
  apiKey: string,
  model: string,
  params: { story_bible: string; chapter_map: string; previous_state: string; chapter_draft: string; chapter_number: number; extra_rules?: string }
) {
  const { extra_rules, ...coreParams } = params;
  const sys = getIronRulesCheckerPrompt({
    ...coreParams,
    custom_iron_rules: extra_rules
  });
  const res = await callDynamicEngine(engine, {
    apiKey,
    systemPrompt: sys,
    userPrompt: 'Audit the chapter now.',
    temperature: 0.1,
    model,
    taskType: 'iron_rules_checker',
  });
  return { text: res.text, usedModel: res.chosenModel || model };
}

export async function agentFinalAudit(
  engine: string,
  apiKey: string,
  model: string,
  params: { story_bible: string; chapter_map: string; all_chapters: string; current_state: string; audit_reports: string; extra_rules?: string }
) {
  const { extra_rules, ...coreParams } = params;
  const sys = getFinalAuditPrompt({
    ...coreParams,
    custom_iron_rules: extra_rules
  });
  const res = await callDynamicEngine(engine, {
    apiKey,
    systemPrompt: sys,
    userPrompt: 'Conduct the final story audit now.',
    temperature: 0.1,
    model,
    taskType: 'final_audit',
  });
  return { text: res.text, usedModel: res.chosenModel || model };
}
