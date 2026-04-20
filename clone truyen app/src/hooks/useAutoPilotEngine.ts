/* eslint-disable @typescript-eslint/ban-ts-comment */
/* eslint-disable @typescript-eslint/no-explicit-any */
import { useEffect, useRef } from 'react';
import { useStore } from '../store/useStore';
import { agentSeasonArchitect, agentPremiumPolish, agentEpisodeDrafter, agentEpisodeRewriter, agentMarketingAssets } from '../lib/advanced_engine';
import { callWordPress, agentMicroDramaExpand, agentMicroDramaRewrite, agentGrokDramaExpand, agentGrokDramaRewrite, agentClaudeDramaExpand, agentClaudeDramaRewrite, agentGeminiDramaExpand, agentGeminiDramaRewrite, agentQwenDramaRewrite, agentQwenDramaExpand } from '../lib/engine';

export function useAutoPilotEngine() {
  const { 
    queue, isAutoPilotRunning, geminiKey, geminiPaidKey, openAIKey, grokKey, claudeKey, qwenKey,
    usePaidAPI, isFreeApiExhausted, wpUrl, wpUser, wpAppPassword, 
    updateQueueItem, setSettings
  } = useStore();
  
  const isProcessing = useRef(false);
  const lastProcessTime = useRef(0);

  useEffect(() => {
    const activeKey = usePaidAPI ? geminiPaidKey : geminiKey;
    if (!isAutoPilotRunning || queue.length === 0) return;
    const tick = async () => {
      const now = Date.now();
      if (isProcessing.current) {
        // Failsafe: if stuck for > 5 minutes (due to hot-reload or API hang), unlock it!
        // LLM generation can take up to 2-3 minutes, so 60s is too short and causes duplicate chapters.
        if (now - lastProcessTime.current > 300000) {
           console.warn("AutoPilot Auto-Unlock: isProcessing stuck for > 5 mins, resetting...");
           isProcessing.current = false;
        } else {
           return;
        }
      }
      
      // Giới hạn chạy 1 truyện duy nhất tại 1 thời điểm để bảo toàn hạn mức Google Free API.
      // Khi viết xong truyện 1 nó sẽ TỰ ĐỘNG bốc truyện 2 lên viết tiếp không cần chờ anh Duyệt!
      const activeItems = queue.filter(q => q.status === 'draft_outline' || q.status === 'pending' || q.status === 'writing').slice(0, 1);
      if (activeItems.length === 0) return;

      isProcessing.current = true;
      lastProcessTime.current = now;
      try {
        await Promise.all(activeItems.map(async (activeItem) => {
          try {
            if (activeItem.status === 'draft_outline') {
          let wpPostId = activeItem.wpPostId;
          // [Weaver Station]: Removed auto WP Post Creation. All content will be managed locally.
          if (!wpPostId) {
            wpPostId = Date.now();
            updateQueueItem(activeItem.id, { wpPostId });
          }

          
          updateQueueItem(activeItem.id, { status: 'writing' }); // Mượn status writing để hiển thị đang làm Timeline
          
          let timeline = (activeItem.bible as any)?.timeline;
          if (!timeline) {
             const outlineEngine = activeItem.outlineEngine || 'gemini';
             const bounds = { minChapters: activeItem.targetChapters, maxChapters: activeItem.maxChapters || activeItem.targetChapters };
             if (outlineEngine === 'gemini') // @ts-ignore
 timeline = await agentGeminiDramaExpand(activeKey, activeItem.bible, bounds);
             else if (outlineEngine === 'openai') // @ts-ignore
 timeline = await agentMicroDramaExpand(openAIKey, activeItem.bible, bounds);
             else if (outlineEngine === 'grok') // @ts-ignore
 timeline = await agentGrokDramaExpand(grokKey, activeItem.bible, bounds);
             else if (outlineEngine === 'claude') // @ts-ignore
 timeline = await agentClaudeDramaExpand(claudeKey, activeItem.bible, bounds);
             else if (outlineEngine === 'qwen') // @ts-ignore
 timeline = await agentQwenDramaExpand(qwenKey, activeItem.bible, bounds);
          }
          
          updateQueueItem(activeItem.id, { status: 'pending_approval', bible: { ...activeItem.bible, timeline }, targetChapters: (timeline as any[]).length });
        } 

        else if (activeItem.status === 'pending' || activeItem.status === 'writing') {
          if (activeItem.isAdvancedPipeline) {
            const currentEp = activeItem.chaptersDone + 1;
            const totalEps = activeItem.targetChapters || 30;
            const isImportantEp = currentEp === 1 || currentEp === 2 || currentEp === totalEps || currentEp % 5 === 0;
            const isFinaleOrFirst = currentEp === 1 || currentEp === totalEps;
            
            // const isCombo6 = activeItem.comboType === 6;
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
            
            if (!(fullBible as any).timeline) {
               updateQueueItem(activeItem.id, { status: 'writing' }); 
               fullBible = await agentSeasonArchitect(architectEngine, architectKey, architectModel, activeItem.bible);
               updateQueueItem(activeItem.id, { bible: fullBible });
            }

            updateQueueItem(activeItem.id, { status: 'writing' });
            const currBeatObj = (fullBible as any).timeline?.[currentEp - 1];
            const currBeat = currBeatObj?.outline || 'Mâu thuẫn bùng nổ';
            let shortBeatTitle = currBeatObj?.title || currBeat.split('.')[0].split(',')[0];
            shortBeatTitle = shortBeatTitle.replace(/^(Chương|Tập|Episode)\s*\d+[:\-]?\s*/i, '').trim();
            if (shortBeatTitle.length > 40) shortBeatTitle = shortBeatTitle.substring(0, 37) + '...';
            const finalChapterTitle = `Chương ${currentEp}: ${shortBeatTitle}`;
            
            // 1. Phác thảo khung thô (Drafter)
            let finalDraft = await agentEpisodeDrafter(drafterEngine, drafterKey, drafterModel, fullBible, currentEp, currBeat);
            
            // 2. Head Writer sửa lại (Chỉ tập quan trọng)
            if (isImportantEp) {
               finalDraft = await agentEpisodeRewriter(rewriterEngine, rewriterKey, rewriterModel, finalDraft, (fullBible as any).emotional_escalation_ladder || '');
            }
            
            // 3. Phủ nhung lụa cảm xúc (Chỉ tập Đinh 1 & Finale)
            if (isFinaleOrFirst) {
               finalDraft = await agentPremiumPolish(polishEngine, polishKey, polishModel, finalDraft);
            }
            
            // [Weaver Station]: No WP Chapter Upload.

            const nextEpsDone = activeItem.chaptersDone + 1;
            const isDone = nextEpsDone >= totalEps;
            
            if (isDone) {
               try {
                 const marketingEngine = 'gemini';
                 const marketingModel = 'gemini-1.5-flash';
                 const marketing = await agentMarketingAssets(marketingEngine, geminiKey, marketingModel, (fullBible as any).series_premise);
                 console.log("Marketing Assets Gen:", marketing);
               } catch { }
            }
            
            const newChaptersContent = [...(activeItem.chaptersContent || [])];
            newChaptersContent.push({ episode: currentEp, title: finalChapterTitle, content: finalDraft });

            updateQueueItem(activeItem.id, {
              chaptersDone: nextEpsDone,
              status: isDone ? 'completed' : 'pending',
              wordCount: activeItem.wordCount + finalDraft.split(' ').length,
              chaptersContent: newChaptersContent,
              errorLog: undefined
            });
            return;
          }

          // ================== MICRO DRAMA LOGIC (ALL ENGINES & COMBOS) ==================
          // (outlineEngine is unused in this block, as it was already parsed)
          const writeEngine = activeItem.writeEngine || 'gemini';
          
          const currentEp = activeItem.chaptersDone + 1;
          const timeline = (activeItem.bible as any).timeline;
          let draft = '';
          let currOutline = '';
          
          if (!timeline) {
             // Cứu cánh nếu user skip approval bằng cách nào đó
             return updateQueueItem(activeItem.id, { status: 'draft_outline' });
          }

          updateQueueItem(activeItem.id, { status: 'writing' });
          const currTimelineObj = timeline[currentEp - 1];
          const rawOutline = currTimelineObj?.outline || 'Tiếp diễn mâu thuẫn khốc liệt';
          
          const prevContext = activeItem.chaptersContent ? activeItem.chaptersContent.map(c => `[${c.title}]\n${c.content}`).join("\n\n---\n\n") : '';
          currOutline = prevContext ? `NỘI DUNG CÁC CHƯƠNG ĐÃ VIẾT TRƯỚC ĐÓ (Đọc để hiểu bối cảnh và nắm bắt diễn biến hiện tại, lưu ý KHÔNG VIẾT LẶP LẠI TÌNH TIẾT ĐÃ CÓ):\n"""\n${prevContext}\n"""\n\n==========\n\nNHIỆM VỤ HIỆN TẠI (Chương ${currentEp}):\nHãy BẮT ĐẦU VIẾT NGAY phần nội dung tiếp theo dựa trên dàn ý sau:\n${rawOutline}` : rawOutline;
          
          
          let shortOutlineTitle = currTimelineObj?.title || currOutline.split('.')[0].split(',')[0];
          shortOutlineTitle = shortOutlineTitle.replace(/^(Chương|Tập|Episode)\s*\d+[:\-]?\s*/i, '').trim();
          if (shortOutlineTitle.length > 40) shortOutlineTitle = shortOutlineTitle.substring(0, 37) + '...';
          const finalChapterOutlineTitle = `Chương ${currentEp}: ${shortOutlineTitle}`;
          
          if (writeEngine === 'gemini') draft = await agentGeminiDramaRewrite(activeKey, activeItem.bible, currOutline, currentEp);
          else if (writeEngine === 'openai') draft = await agentMicroDramaRewrite(openAIKey, activeItem.bible, currOutline, currentEp);
          else if (writeEngine === 'grok') draft = await agentGrokDramaRewrite(grokKey, activeItem.bible, currOutline, currentEp);
          else if (writeEngine === 'claude') draft = await agentClaudeDramaRewrite(claudeKey, activeItem.bible, currOutline, currentEp);
          else if (writeEngine === 'qwen') draft = await agentQwenDramaRewrite(qwenKey, activeItem.bible, currOutline, currentEp);
          
          // [Weaver Station]: No WP Chapter Upload. All text generation is buffered locally.

          const nextEpsDone = activeItem.chaptersDone + 1;
          const isDone = nextEpsDone >= activeItem.targetChapters;
          
          const newChaptersContent = [...(activeItem.chaptersContent || [])];
          newChaptersContent.push({ episode: currentEp, title: finalChapterOutlineTitle, content: draft });

          updateQueueItem(activeItem.id, { 
            chaptersDone: nextEpsDone,
            status: isDone ? 'final_review' : 'pending',
            wordCount: activeItem.wordCount + draft.split(' ').length,
            chaptersContent: newChaptersContent,
            errorLog: undefined
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
            updateQueueItem(activeItem.id, { status: 'error', errorLog: "Đã cạn tài nguyên Free API. Vui lòng bật API Trả phí hoặc đổi API Key khác ở mục Settings!" });
          }
        } else {
          updateQueueItem(activeItem.id, { status: 'error', errorLog: errMsg });
        }
      }
    }));
    } finally {
      isProcessing.current = false;
    }
  };

    // If using free tier, cooldown 21s to respect rate limits (Gemini 15/min limit). If paid, push aggressively!
    const delay = 3000;
    const interval = setInterval(tick, delay); 
    return () => clearInterval(interval);
  }, [
    isAutoPilotRunning, queue, geminiKey, geminiPaidKey, openAIKey, grokKey, claudeKey, qwenKey,
    usePaidAPI, isFreeApiExhausted, wpUrl, wpUser, wpAppPassword, 
    updateQueueItem, setSettings
  ]);
}
