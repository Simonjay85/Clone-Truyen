import re

path = "clone truyen app/src/hooks/useAutoPilotEngine.ts"
with open(path, "r") as f:
    content = f.read()

# 1. Add advanced_engine imports
if "agentSeasonArchitect" not in content:
    content = content.replace("import { callWordPress", "import { agentSeasonArchitect, agentEpisodeDrafter, agentEpisodeRewriter, agentMarketingAssets } from '../lib/advanced_engine';\nimport { callWordPress")

# 2. Add isAdvancedPipeline branching
advanced_logic = """
          if (activeItem.isAdvancedPipeline) {
            const outlineEngine = activeItem.outlineEngine || 'gemini';
            const writeEngine = activeItem.writeEngine || 'gemini';
            
            const outlineKey = outlineEngine === 'openai' ? openAIKey : outlineEngine === 'grok' ? grokKey : outlineEngine === 'claude' ? claudeKey : activeKey;
            const writeKey = writeEngine === 'openai' ? openAIKey : writeEngine === 'grok' ? grokKey : writeEngine === 'claude' ? claudeKey : activeKey;
            
            const currentEp = activeItem.chaptersDone + 1;
            let fullBible = activeItem.bible;
            
            if (!fullBible.timeline) {
               updateQueueItem(activeItem.id, { status: 'writing' }); 
               fullBible = await agentSeasonArchitect(outlineEngine, outlineKey, activeItem.bible);
               updateQueueItem(activeItem.id, { bible: fullBible });
            }

            updateQueueItem(activeItem.id, { status: 'writing' });
            const currBeat = fullBible.timeline?.[currentEp - 1]?.outline || 'Mâu thuẫn bùng nổ';
            
            const draft = await agentEpisodeDrafter(writeEngine, writeKey, fullBible, currentEp, currBeat);
            const finalDraft = await agentEpisodeRewriter(writeEngine, writeKey, draft, fullBible.emotional_escalation_ladder || '');
            
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
            const isDone = nextEpsDone >= activeItem.targetChapters;
            
            if (isDone) {
               try {
                 const marketing = await agentMarketingAssets(writeEngine, writeKey, fullBible.series_premise);
                 console.log("Marketing Assets Gen:", marketing);
               } catch(e){}
            }
            
            updateQueueItem(activeItem.id, {
              chaptersDone: nextEpsDone,
              status: isDone ? 'completed' : 'pending',
              wordCount: activeItem.wordCount + finalDraft.split(' ').length
            });
            return;
          }
"""

# regex replace
match_str = "else if (activeItem.status === 'pending') {"
if advanced_logic not in content:
    content = content.replace(match_str, match_str + advanced_logic)

with open(path, "w") as f:
    f.write(content)
