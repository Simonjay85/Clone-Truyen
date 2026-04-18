import re

path = "clone truyen app/src/lib/advanced_engine.ts"
with open(path, "r") as f:
    content = f.read()

# Replace signatures to include model, and pass model down to callDynamicEngine.

replacements = [
    # Concept Gen
    ("agentConceptGenerator(engine: string, apiKey: string, criteria: any)", "agentConceptGenerator(engine: string, apiKey: string, model: string, criteria: any)"),
    ("userPrompt: user, jsonMode: true, temperature: 0.9", "userPrompt: user, jsonMode: true, temperature: 0.9, model"),
    
    # Concept Scorer
    ("agentConceptScorer(engine: string, apiKey: string, concepts: any[])", "agentConceptScorer(engine: string, apiKey: string, model: string, concepts: any[])"),
    ("userPrompt: user, jsonMode: true, temperature: 0.2", "userPrompt: user, jsonMode: true, temperature: 0.2, model"),

    # Season Architect
    ("agentSeasonArchitect(engine: string, apiKey: string, winningConcept: any)", "agentSeasonArchitect(engine: string, apiKey: string, model: string, winningConcept: any)"),
    ("userPrompt: user, jsonMode: true, temperature: 0.4", "userPrompt: user, jsonMode: true, temperature: 0.4, model"),

    # Drafter
    ("agentEpisodeDrafter(engine: string, apiKey: string, bible: any, epNum: number, currentBeat: string)", "agentEpisodeDrafter(engine: string, apiKey: string, model: string, bible: any, epNum: number, currentBeat: string)"),
    ("userPrompt: user, temperature: 0.6", "userPrompt: user, temperature: 0.6, model"),

    # Rewriter
    ("agentEpisodeRewriter(engine: string, apiKey: string, draft: string, emotionalEscalationLadder: string)", "agentEpisodeRewriter(engine: string, apiKey: string, model: string, draft: string, emotionalEscalationLadder: string)"),
    ("userPrompt: user, temperature: 0.5", "userPrompt: user, temperature: 0.5, model"),

    # Continuity Checker
    ("agentContinuityChecker(engine: string, apiKey: string, episodesContext: string, bibleStr: string)", "agentContinuityChecker(engine: string, apiKey: string, model: string, episodesContext: string, bibleStr: string)"),
    ("userPrompt: user, jsonMode: true, temperature: 0.1", "userPrompt: user, jsonMode: true, temperature: 0.1, model"),

    # Marketing
    ("agentMarketingAssets(engine: string, apiKey: string, summary: string)", "agentMarketingAssets(engine: string, apiKey: string, model: string, summary: string)"),
    ("userPrompt: summary, jsonMode: true, temperature: 0.8", "userPrompt: summary, jsonMode: true, temperature: 0.8, model")
]

for old, new in replacements:
    content = content.replace(old, new)


new_function = """

export async function agentPremiumPolish(engine: string, apiKey: string, model: string, draft: string) {
  const sys = `Premium Polish Mode. Bạn là chuyên gia chải chuốt văn phong sâu sắc.
Hãy đọc lại bản draft này và viết lại sao cho câu chữ thật mượt mà, chạm đáy cảm xúc, giữ nguyên hoàn toàn tiết tấu/twist nhưng thay bộ cánh ngôn từ sang trọng hơn xịn hơn.
Chỉ trả Text (Markdown), không mào đầu.`;

  const user = `--- DRAFT ---
${draft}

Hãy phủ bóng màn đêm và mài sắc lưỡi dao cảm xúc!`;

  const res = await callDynamicEngine(engine, { apiKey, systemPrompt: sys, userPrompt: user, model, temperature: 0.4 });
  return res.text;
}
"""

if "agentPremiumPolish" not in content:
    content += new_function

with open(path, "w") as f:
    f.write(content)
