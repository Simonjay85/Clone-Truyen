import { useEffect, useRef } from 'react';
import { useStore } from '../store/useStore';
import { agentSeasonArchitect, agentPremiumPolish, agentEpisodeDrafter, agentEpisodeRewriter, agentMarketingAssets } from '../lib/advanced_engine';
import { callWordPress, agentMicroDramaExpand, agentMicroDramaRewrite, agentGrokDramaExpand, agentGrokDramaRewrite, agentClaudeDramaExpand, agentClaudeDramaRewrite, agentGeminiDramaExpand, agentGeminiDramaRewrite } from '../lib/engine';

export function useAutoPilotEngine() {
  const { 
    queue, isAutoPilotRunning, geminiKey, geminiPaidKey, openAIKey, grokKey, claudeKey,
    usePaidAPI, isFreeApiExhausted, wpUrl, wpUser, wpAppPassword, 
    updateQueueItem, setSettings
  } = useStore();
  
  const isProcessing = useRef(false);

  useEffect(() => {
    const activeKey = usePaidAPI ? geminiPaidKey : geminiKey;
    if (!isAutoPilotRunning || !activeKey || queue.length === 0) return;
    if (!usePaidAPI && isFreeApiExhausted) return;

    const tick = async () => {
      if (isProcessing.current) return;
      
      const activeItem = queue.find(q => q.status === 'draft_outline' || q.status === 'pending' || q.status === 'writing' || q.status === 'final_review');
      if (!activeItem) return;

      isProcessing.current = true;
      try {
        if (activeItem.status === 'draft_outline') {
          // Tạo bài truyen trên WP nếu chưa có
          let wpPostId = activeItem.wpPostId;
          if (!wpPostId) {
            if (wpUrl && wpUser && wpAppPassword) {
              // Chuẩn bị thể loại gán tự động
              const genreTerms = activeItem.genres
                ? activeItem.genres.split(',').map((g: string) => g.trim()).filter(Boolean)
                : [];
              const wpRes = await callWordPress({
                wpUrl, wpUser, wpAppPassword,
                endpoint: 'truyen',
                method: 'POST',
                payload: {
                  title: activeItem.title,
                  content: activeItem.bible?.overallSizzle || activeItem.prompt,
                  status: 'draft',
                  ...(genreTerms.length > 0 ? { the_loai: genreTerms } : {}),
                }
              });
              wpPostId = wpRes.id;
              if (!wpPostId) throw new Error('WP trả về không có ID bài viết truyen');
            }
            // Nếu không có WP config → chạy local không đăng bài (wpPostId vẫn = undefined)
            if (wpPostId) updateQueueItem(activeItem.id, { wpPostId });
          }

          
          updateQueueItem(activeItem.id, { status: 'writing' }); // Mượn status writing để hiển thị đang làm Timeline
          
          let timeline = activeItem.bible?.timeline;
          if (!timeline) {
             const outlineEngine = activeItem.outlineEngine || 'gemini';
             const bounds = { minChapters: activeItem.targetChapters, maxChapters: activeItem.maxChapters || activeItem.targetChapters };
             if (outlineEngine === 'gemini') timeline = await agentGeminiDramaExpand(activeKey, activeItem.bible, bounds);
             else if (outlineEngine === 'openai') timeline = await agentMicroDramaExpand(openAIKey, activeItem.bible, bounds);
             else if (outlineEngine === 'grok') timeline = await agentGrokDramaExpand(grokKey, activeItem.bible, bounds);
             else if (outlineEngine === 'claude') timeline = await agentClaudeDramaExpand(claudeKey, activeItem.bible, bounds);
          }
          
          updateQueueItem(activeItem.id, { status: 'pending_approval', bible: { ...activeItem.bible, timeline }, targetChapters: timeline.length });
        } 

        else if (activeItem.status === 'pending') {
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
            const currBeatObj = fullBible.timeline?.[currentEp - 1];
            const currBeat = currBeatObj?.outline || 'Mâu thuẫn bùng nổ';
            let shortBeatTitle = currBeatObj?.title || currBeat.split('.')[0].split(',')[0];
            if (shortBeatTitle.length > 40) shortBeatTitle = shortBeatTitle.substring(0, 37) + '...';
            
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
                  title: `Tập ${currentEp}: ${shortBeatTitle}`,
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
          }

          // ================== MICRO DRAMA LOGIC (ALL ENGINES & COMBOS) ==================
          const outlineEngine = activeItem.outlineEngine || 'gemini';
          const writeEngine = activeItem.writeEngine || 'gemini';
          
          const currentEp = activeItem.chaptersDone + 1;
          let timeline = activeItem.bible.timeline;
          let draft = '';
          let currOutline = '';
          
          if (!timeline) {
             // Cứu cánh nếu user skip approval bằng cách nào đó
             return updateQueueItem(activeItem.id, { status: 'draft_outline' });
          }

          updateQueueItem(activeItem.id, { status: 'writing' });
          const currTimelineObj = timeline[currentEp - 1];
          currOutline = currTimelineObj?.outline || 'Tiếp diễn mâu thuẫn khốc liệt';
          
          let shortOutlineTitle = currTimelineObj?.title || currOutline.split('.')[0].split(',')[0];
          if (shortOutlineTitle.length > 40) shortOutlineTitle = shortOutlineTitle.substring(0, 37) + '...';
          
          if (writeEngine === 'gemini') draft = await agentGeminiDramaRewrite(activeKey, activeItem.bible, currOutline, currentEp);
          else if (writeEngine === 'openai') draft = await agentMicroDramaRewrite(openAIKey, activeItem.bible, currOutline, currentEp);
          else if (writeEngine === 'grok') draft = await agentGrokDramaRewrite(grokKey, activeItem.bible, currOutline, currentEp);
          else if (writeEngine === 'claude') draft = await agentClaudeDramaRewrite(claudeKey, activeItem.bible, currOutline, currentEp);
          
          if (activeItem.wpPostId) {
            let finalStr = draft.replace(/```markdown/gi, '').replace(/```/g, '');
            finalStr = finalStr.replace(/\*\*([\s\S]*?)\*\*/g, '<strong>$1</strong>').replace(/\*([\s\S]*?)\*/g, '<em>$1</em>').replace(/\n/g, '<br/>');

            await callWordPress({
              wpUrl, wpUser, wpAppPassword,
              endpoint: 'chuong',
              method: 'POST',
              payload: {
                title: `Tập ${currentEp}: ${shortOutlineTitle}`,
                content: finalStr,
                status: 'publish',
                meta: { _truyen_id: activeItem.wpPostId }
              }
            });
          }

          const nextEpsDone = activeItem.chaptersDone + 1;
          const isDone = nextEpsDone >= activeItem.targetChapters;
          updateQueueItem(activeItem.id, { 
            chaptersDone: nextEpsDone,
            status: isDone ? 'final_review' : 'pending',
            wordCount: activeItem.wordCount + draft.split(' ').length
          });
        }
      } catch (err: unknown) {
        let errMsg = 'Internal Server Error';
        if (err instanceof Error) {
           errMsg = err.message;
        } else if (typeof err === 'string') {
           errMsg = err;
        }
        console.error("AutoPilot Error for item", activeItem.title, err);
        
        // Catch 429 Quota Exceeded for Free Tier
        if (!usePaidAPI && (errMsg.includes('429') || errMsg.includes('Quota') || errMsg.includes('exhausted') || errMsg.includes('rate limit'))) {
          if (errMsg.includes('retry') || errMsg.includes('Rate Limit') || errMsg.includes('too many requests')) {
            updateQueueItem(activeItem.id, { status: 'error', errorLog: "Nghẽn API tạm thời do gọi quá nhanh! Vui lòng đợi 15 giây rồi bấm THỬ LẠI.\\nChi tiết: " + errMsg });
          } else {
            setSettings({ isFreeApiExhausted: true, isAutoPilotRunning: false });
            updateQueueItem(activeItem.id, { errorLog: "Đã cạn tài nguyên Free API. Vui lòng bật API Trả phí!" });
          }
        } else {
          updateQueueItem(activeItem.id, { status: 'error', errorLog: errMsg });
        }
      } finally {
        isProcessing.current = false;
      }
    };

    // If using free tier, cooldown 21s to respect rate limits (Gemini 15/min limit). If paid, push aggressively!
    const delay = usePaidAPI ? 3000 : 21000;
    const interval = setInterval(tick, delay); 
    return () => clearInterval(interval);
  }, [
    isAutoPilotRunning, queue, geminiKey, geminiPaidKey, openAIKey, grokKey, claudeKey,
    usePaidAPI, isFreeApiExhausted, wpUrl, wpUser, wpAppPassword, 
    updateQueueItem, setSettings
  ]);
}
