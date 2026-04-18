import os, re

path = "clone truyen app/src/hooks/useAutoPilotEngine.ts"

with open(path, "r") as f:
    content = f.read()

# Make sure agentPremiumPolish is imported
if "agentPremiumPolish" not in content:
    content = content.replace("import { agentSeasonArchitect", "import { agentSeasonArchitect, agentPremiumPolish")

# The advanced logic string
advanced_logic = """
          if (activeItem.isAdvancedPipeline) {
            const currentEp = activeItem.chaptersDone + 1;
            const totalEps = activeItem.targetChapters || 30;
            const isImportantEp = currentEp === 1 || currentEp === 2 || currentEp === totalEps || currentEp % 5 === 0;
            const isFinaleOrFirst = currentEp === 1 || currentEp === totalEps;
            
            const isCombo6 = activeItem.comboType === 6;
            
            // Workflow Routing Matrix
            const architectEngine = 'openai';
            const architectKey = openAIKey;
            const architectModel = 'gpt-4o';
            
            const drafterEngine = 'openai';
            const drafterKey = openAIKey;
            const drafterModel = 'gpt-4o-mini';
            
            const rewriterEngine = 'openai';
            const rewriterKey = openAIKey;
            const rewriterModel = 'gpt-4o';
            
            const polishEngine = 'claude';
            const polishKey = claudeKey;
            const polishModel = 'claude-3-5-sonnet-20241022';
            
            let fullBible = activeItem.bible;
            
            if (!fullBible.timeline) {
               updateQueueItem(activeItem.id, { status: 'writing' }); 
               fullBible = await agentSeasonArchitect(architectEngine, architectKey, architectModel, activeItem.bible);
               updateQueueItem(activeItem.id, { bible: fullBible });
            }

            updateQueueItem(activeItem.id, { status: 'writing' });
            const currBeat = fullBible.timeline?.[currentEp - 1]?.outline || 'Mâu thuẫn bùng nổ';
            
            // 1. Phác thảo khung thô (Drafter)
            let finalDraft = await agentEpisodeDrafter(drafterEngine, drafterKey, drafterModel, fullBible, currentEp, currBeat);
            
            // 2. Head Writer sửa lại (Chỉ tập quan trọng)
            if (isImportantEp) {
               finalDraft = await agentEpisodeRewriter(rewriterEngine, rewriterKey, rewriterModel, finalDraft, fullBible.emotional_escalation_ladder || '');
            }
            
            // 3. Phủ nhung lụa cảm xúc (Chỉ tập Đinh 1 & Finale)
            if (isFinaleOrFirst) {
               finalDraft = await agentPremiumPolish(polishEngine, polishKey, polishModel, finalDraft);
            }
            
            if (activeItem.wpPostId) {
              await callWordPress({
                wpUrl, wpUser, wpAppPassword,
                endpoint: 'chuong',
                method: 'POST',
                payload: {
                  title: `Tập ${currentEp}: ${currBeat}`,
                  content: finalDraft.replace(/\\n/g, '<br/>'),
                  status: 'draft',
                  meta: { _truyen_id: activeItem.wpPostId }
                }
              });
            }

            const nextEpsDone = activeItem.chaptersDone + 1;
            const isDone = nextEpsDone >= totalEps;
            
            if (isDone) {
               try {
                 const marketingEngine = 'gemini';
                 const marketingModel = 'gemini-1.5-flash';
                 const marketing = await agentMarketingAssets(marketingEngine, geminiKey, marketingModel, fullBible.series_premise);
                 console.log("Marketing Assets Gen:", marketing);
               } catch(e){}
            }
            
            updateQueueItem(activeItem.id, {
              chaptersDone: nextEpsDone,
              status: isDone ? 'completed' : 'pending',
              wordCount: activeItem.wordCount + finalDraft.split(' ').length
            });
            return;
          }"""

import re
# Regex to replace existing advanced_logic block
content = re.sub(r"\n          if \(activeItem\.isAdvancedPipeline\) \{.+?return;\n          \}", advanced_logic, content, flags=re.DOTALL)

with open(path, "w") as f:
    f.write(content)
