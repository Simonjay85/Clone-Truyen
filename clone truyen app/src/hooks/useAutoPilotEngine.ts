/* eslint-disable @typescript-eslint/ban-ts-comment */
/* eslint-disable @typescript-eslint/no-explicit-any */
import { useEffect, useRef } from 'react';
import { useStore } from '../store/useStore';
import { agentSeasonArchitect, agentPremiumPolish, agentEpisodeDrafter, agentEpisodeRewriter, agentMarketingAssets } from '../lib/advanced_engine';
import { agentMicroDramaExpand, agentMicroDramaRewrite, agentGrokDramaExpand, agentGrokDramaRewrite, agentClaudeDramaExpand, agentClaudeDramaRewrite, agentGeminiDramaExpand, agentGeminiDramaRewrite, agentQwenDramaRewrite, agentQwenDramaExpand, agentDeepSeekDramaExpand, agentDeepSeekDramaRewrite, sanitizeChapterTitle } from '../lib/engine';
import { STORY_GENRES, StoryGenreId } from '../config/storyStyles';

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
        // Failsafe: if stuck for > 15 minutes (due to hot-reload or API hang), unlock it!
        // LLM generation can take up to 2-3 minutes per request, plus retries.
        if (now - lastProcessTime.current > 900000) {
           console.warn("AutoPilot Auto-Unlock: isProcessing stuck for > 15 mins, resetting...");
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
             else if (outlineEngine === 'deepseek') // @ts-ignore
 timeline = await agentDeepSeekDramaExpand(useStore.getState().deepseekKey, activeItem.bible, bounds);
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
            let currBeat = currBeatObj?.outline || 'Mâu thuẫn bùng nổ';
            if (activeItem.storyStyle && STORY_GENRES[activeItem.storyStyle as StoryGenreId]) {
               const overridePrompt = STORY_GENRES[activeItem.storyStyle as StoryGenreId]?.overridePrompt || '';
               if (overridePrompt) currBeat = overridePrompt + currBeat;
            }
            let shortBeatTitle = currBeatObj?.title || currBeatObj?.outline?.split('.')[0].split(',')[0] || 'Chương mới';
            shortBeatTitle = sanitizeChapterTitle(shortBeatTitle); // 🛡️ Strip leaked prompt labels
            shortBeatTitle = shortBeatTitle.replace(/^(Chương|Tập|Episode)\s*\d+[:\-]?\s*/i, '').trim();
            if (shortBeatTitle.length > 40) shortBeatTitle = shortBeatTitle.substring(0, 37) + '...';
            const finalChapterTitle = `Chương ${currentEp}: ${shortBeatTitle}`;
            
            // 1. Phác thảo khung thô (Drafter)
            const prevChapterContext = activeItem.chaptersContent?.length ? activeItem.chaptersContent[activeItem.chaptersContent.length - 1].content.slice(-3000) : '';
            let finalDraft = await agentEpisodeDrafter(drafterEngine, drafterKey, drafterModel, fullBible, currentEp, currBeat, prevChapterContext);
            
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
              errorLog: undefined,
              ...(isDone ? { completedAt: Date.now() } : {})
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
          
          const prevChapterContent = activeItem.chaptersContent?.length ? activeItem.chaptersContent[activeItem.chaptersContent.length - 1].content : '';
          const prevContextWindow = prevChapterContent ? prevChapterContent.slice(-3000) : '';
          currOutline = prevContextWindow ? `NỘI DUNG CUỐI CỦA CHƯƠNG TRƯỚC (Đọc để tiếp nối NGAY LẬP TỨC mạch văn, không gian và diễn biến, KHÔNG LẶP LẠI TÌNH TIẾT ĐÃ CÓ):\n"""\n${prevContextWindow}\n"""\n\n==========\n\nNHIỆM VỤ HIỆN TẠI (Chương ${currentEp}):\nHãy BẮT ĐẦU VIẾT NGAY phần nội dung tiếp theo dựa trên dàn ý sau:\n${rawOutline}` : rawOutline;
          
          if (activeItem.storyStyle && STORY_GENRES[activeItem.storyStyle as StoryGenreId]) {
             const overridePrompt = STORY_GENRES[activeItem.storyStyle as StoryGenreId]?.overridePrompt || '';
             if (overridePrompt) currOutline = overridePrompt + currOutline;
          }
          let shortOutlineTitle = currTimelineObj?.title || currOutline.split('.')[0].split(',')[0];
          shortOutlineTitle = sanitizeChapterTitle(shortOutlineTitle); // 🛡️ Strip leaked prompt labels
          shortOutlineTitle = shortOutlineTitle.replace(/^(Chương|Tập|Episode)\s*\d+[:\-]?\s*/i, '').trim();
          if (shortOutlineTitle.length > 40) shortOutlineTitle = shortOutlineTitle.substring(0, 37) + '...';
          const finalChapterOutlineTitle = `Chương ${currentEp}: ${shortOutlineTitle}`;
          
          if (writeEngine === 'gemini') draft = await agentGeminiDramaRewrite(activeKey, activeItem.bible, currOutline, currentEp);
          else if (writeEngine === 'openai') draft = await agentMicroDramaRewrite(openAIKey, activeItem.bible, currOutline, currentEp);
          else if (writeEngine === 'grok') draft = await agentGrokDramaRewrite(grokKey, activeItem.bible, currOutline, currentEp);
          else if (writeEngine === 'claude') draft = await agentClaudeDramaRewrite(claudeKey, activeItem.bible, currOutline, currentEp);
          else if (writeEngine === 'qwen') draft = await agentQwenDramaRewrite(qwenKey, activeItem.bible, currOutline, currentEp);
          else if (writeEngine === 'deepseek') draft = await agentDeepSeekDramaRewrite(useStore.getState().deepseekKey, activeItem.bible, currOutline, currentEp);
          
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
            errorLog: undefined,
            ...(isDone ? { completedAt: Date.now() } : {})
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
        const errMsgLower = errMsg.toLowerCase();
        // 1. Transient API Rate Limits (OpenAI TPM, Anthropic RPM, etc)
        if (errMsgLower.includes('rate limit') || errMsgLower.includes('429') || errMsgLower.includes('too many requests') || errMsgLower.includes('retry')) {
          console.warn("Got Temporary API Rate Limit. Auto-retrying without crashing...");
          updateQueueItem(activeItem.id, { status: 'pending', errorLog: undefined });
        } 
        // 2. Hard Quota Exhausted (Ran out of credits or monthly free tier)
        else if (errMsgLower.includes('quota') || errMsgLower.includes('insufficient') || errMsgLower.includes('exhausted') || errMsgLower.includes('resource_exhausted')) {
          if (!usePaidAPI) setSettings({ isFreeApiExhausted: true });
          updateQueueItem(activeItem.id, { status: 'error', errorLog: "Đã cạn tài nguyên API (Hết Credit/Quota). Vui lòng kiểm tra lại Key!\nChi tiết: " + errMsg });
        } 
        // 3. Network Outages & 5xx Overloads
        else if (errMsgLower.includes('503') || errMsgLower.includes('502') || errMsgLower.includes('504') || errMsgLower.includes('quá tải') || errMsgLower.includes('overload') || errMsgLower.includes('fetch failed') || errMsgLower.includes('network error') || errMsgLower.includes('socket hang up') || errMsgLower.includes('etimedout')) {
          console.warn("Got Server Overload/Network Error (5xx / fetch failed). Auto-retrying without crashing...");
          updateQueueItem(activeItem.id, { status: 'pending', errorLog: undefined });
        } 
        // 4. Other Fatal Errors
        else {
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
