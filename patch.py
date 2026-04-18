import os, re

def patch_view(filename, engine_name, api_key_var):
    path = f"clone truyen app/src/components/{filename}"
    with open(path, "r") as f:
        content = f.read()
    
    # 1. Fix imports. Replace ALL lib/engine imports
    content = re.sub(r"import \{ .*? \} from '\.\./lib/engine';", "import { agentConceptGenerator, agentConceptScorer } from '../lib/advanced_engine';", content)
    
    # 2. Rewrite handleGenerateOutline
    new_handler = f"""  const handleGenerateOutline = async () => {{
    if (!{api_key_var}) return alert("⚠️ Bạn chưa nhập API Key trong Settings!");
    if (!prompt) return alert("Vui lòng nhập Ý tưởng cốt truyện!");

    setIsGenerating(true);
    setPitchOptions([]);
    setGradingStatus({{}});
    
    try {{
      const criteria = {{
         genres: selectedGenres.length > 0 ? selectedGenres.join(', ') : 'Hỗn hợp',
         prompt: prompt
      }};
      
      const concepts = await agentConceptGenerator('{engine_name}', {api_key_var}, criteria);
      setPitchOptions(concepts);
      if (!title && concepts[0]?.title) setTitle(concepts[0].title);
      
      const scoreResult = await agentConceptScorer('{engine_name}', {api_key_var}, concepts);
      const newGrading: Record<number, any> = {{}};
      scoreResult.scores.forEach((s: any) => {{
         newGrading[s.index] = {{ score: s.score, grading: s.reason }};
      }});
      setGradingStatus(newGrading);
      setSelectedPitches([scoreResult.winner_index]);
    }} catch (e: any) {{
      alert("Lỗi AI: " + e.message);
    }} finally {{
      setIsGenerating(false);
    }}
  }};"""
    
    # Regex to replace handleGenerateOutline block
    content = re.sub(r"  const handleGenerateOutline = async \(\) => \{.*?(?=\n  const gradePitch)", new_handler + "\n", content, flags=re.DOTALL)
    
    # Regex to replace gradePitch block
    content = re.sub(r"  const gradePitch = async \(index: number\) => \{.*?(?=\n  const \[selectedPitches)", "", content, flags=re.DOTALL)
    
    content = content.replace("outlineEngine: ", "isAdvancedPipeline: true, outlineEngine: ")

    content = re.sub(r"\{grading \? \(.*?(?=\n                             <\/div>)", r"{grading ? (\n                                   <div className=\"bg-black/40 border border-white/10 px-4 py-2 rounded-lg flex items-center gap-3\">\n                                      <div className=\"text-xs text-slate-400 font-medium\">ĐIỂM SỐ</div>\n                                      <div className={`text-2xl font-black ${grading.score >= 8 ? 'text-emerald-400' : grading.score >= 6 ? 'text-amber-400' : 'text-red-400'}`}>{grading.score}</div>\n                                   </div>\n                                ) : <div/>}", content, flags=re.DOTALL)

    content = content.replace("pitch.protagonist", "pitch.title")
    content = content.replace("pitch.worldSettings", "pitch.trope")
    content = content.replace("pitch.characterArc", "pitch.core_conflict")
    content = content.replace("pitch.plotTwists", "pitch.twist")
    content = content.replace("pitch.overallSizzle", "pitch.hook")
    
    with open(path, "w") as f:
        f.write(content)

patch_view("ComboEconomicView.tsx", "gemini", "geminiKey")
patch_view("ComboRoyalView.tsx", "grok", "grokKey")
