/* eslint-disable @typescript-eslint/no-explicit-any */
import React, { useState, useEffect } from 'react';
import { useStore, QueueItem } from '../store/useStore';
import { ShieldAlert, BookOpen, Star, UploadCloud, Rocket, RefreshCw, PenTool, Image as ImageIcon, FileText, CheckCircle2, Copy, Trash2 } from 'lucide-react';
import { agentStoryEvaluator, agentPublisherMetadata, agentStoryFixer } from '../lib/advanced_engine';
import { callWordPress } from '../lib/engine';
import { STORY_GENRE_LIST } from '../config/storyStyles';

export function FinalReviewView() {
  const { queue, updateQueueItem, geminiPaidKey, geminiKey, usePaidAPI, wpUrl, wpUser, wpAppPassword } = useStore();
  const [loadingAction, setLoadingAction] = useState<string | null>(null);
  
  const reviewItems = [...queue]
    .filter(q => q.status === 'final_review' || q.status === 'completed' || q.status === 'published')
    .sort((a, b) => (b.createdAt || 0) - (a.createdAt || 0));
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<'overview' | 'bible' | 'chapters'>('overview');
  const [fixProgress, setFixProgress] = useState<{current: number, total: number} | null>(null);
  const [customCoverUrl, setCustomCoverUrl] = useState('');
  const [customPrompt, setCustomPrompt] = useState('');
  const [isSidebarHidden, setIsSidebarHidden] = useState<boolean>(false);
  const [evalModel, setEvalModel] = useState<'gemini'|'qwen'|'openai'>('gemini');
  const [fixModel, setFixModel] = useState<'gemini'|'qwen'|'openai'|'claude'|'deepseek'>('deepseek');
  const [regenEngine, setRegenEngine] = useState<'gemini'|'qwen'|'openai'|'claude'|'grok'|'deepseek' | ''>('');
  const [regenStyle, setRegenStyle] = useState<string>('');
  const [editableStoryText, setEditableStoryText] = useState<string>('');

  useEffect(() => {
    if (!selectedId && reviewItems.length > 0) {
      setTimeout(() => setSelectedId(reviewItems[0].id), 0);
    } else if (selectedId && !reviewItems.find(q => q.id === selectedId)) {
      setTimeout(() => setSelectedId(null), 0);
    }
  }, [selectedId, reviewItems]);

  // Removed auto-hide sidebar so users don't lose track of their story queue.

  const selectedItem = reviewItems.find(q => q.id === selectedId);

  useEffect(() => {
    if (selectedItem?.publishData) {
      setTimeout(() => {
        setCustomCoverUrl(selectedItem.publishData!.coverUrl || '');
        setCustomPrompt(selectedItem.publishData!.coverImagePrompt || '');
      }, 0);
    } else {
      setTimeout(() => {
        setCustomCoverUrl('');
        setCustomPrompt('');
      }, 0);
    }
  }, [selectedItem?.publishData, selectedItem?.publishData?.coverUrl, selectedItem?.publishData?.coverImagePrompt]);

  // Chỉ rebuild tab + textarea khi CHUYỂN SANG TRUYỆN KHÁC.
  // KHÔNG watch chaptersContent — sẽ ghi đè khi user paste/edit thủ công.
  // AI Auto-Fix tự gọi setEditableStoryText() inline nên không cần effect này.
  useEffect(() => {
    setTimeout(() => {
      setActiveTab('overview');
      if (selectedItem?.chaptersContent) {
        const allText = [...selectedItem.chaptersContent]
          .sort((a, b) => a.episode - b.episode)
          .map(ch => {
              let cleanContent = ch.content ? ch.content.trim() : '';
              const titleRegex = new RegExp(`^(?:\\s*)*(?:#+\\s*)?(?:\\*\\*)?(?:Chương|Tập|Episode)\\s*\\d+[:\\-]?\\s*([^\\n]*)(?:\\*\\*)?(?:\\s*)*`, 'i');
              while (titleRegex.test(cleanContent)) {
                cleanContent = cleanContent.replace(titleRegex, '').trim();
              }
              return `Chương ${ch.episode}: ${ch.title.replace(/^(Chương|Tập|Episode)\\s*\\d+[:\\-]?\\s*/i, '')}\n\n${cleanContent}`;
          })
          .join('\n\n========================================\n\n');
        setEditableStoryText(allText);
      } else {
        setEditableStoryText('');
      }
    }, 0);
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [selectedItem?.id]);


  const getActiveKey = () => usePaidAPI && geminiPaidKey ? geminiPaidKey : geminiKey;

  const handleEvaluate = async (item: QueueItem, overrideModel?: string) => {
    setLoadingAction(`eval_${item.id}`);
    try {
      const state = useStore.getState();
      const targetModel = overrideModel || evalModel;
      let engine = 'gemini';
      let model = 'gemini-2.5-flash';
      let key = getActiveKey();

      if (targetModel === 'qwen') {
        engine = 'qwen'; model = 'qwen-plus'; key = state.qwenKey;
      } else if (targetModel === 'openai') {
        engine = 'openai'; model = 'gpt-4o-mini'; key = state.openAIKey;
      } else if (targetModel === 'claude') {
        engine = 'claude'; model = 'claude-3-5-sonnet-20241022'; key = state.claudeKey;
      } else if (targetModel === 'deepseek') {
        engine = 'deepseek'; model = 'deepseek-reasoner'; key = state.deepseekKey;
      }

      if (!key) throw new Error(`Thiếu API Key cho mô hình ${targetModel.toUpperCase()}`);

      const evalData = await agentStoryEvaluator(engine, key, model, item.bible, item.chaptersContent);
      updateQueueItem(item.id, { finalEvaluation: { ...evalData, evaluator: `${targetModel.toUpperCase()} (${model})` } });
      alert("✅ Đánh giá toàn bộ tác phẩm thành công!");
    } catch (e: any) {
      alert("Lỗi Đánh giá: " + (e.message || JSON.stringify(e)));
    }
    setLoadingAction(null);
  };

  const handleDeleteStory = (id: string, title: string) => {
    if (window.confirm(`Xóa vĩnh viễn truyện "${title}" khỏi hệ thống?`)) {
      useStore.getState().removeQueueItem(id);
      setSelectedId(null);
    }
  };

  const handleRegenerateStory = (id: string, title: string, targetEngine: string, targetStyle?: string) => {
    if (window.confirm(`Bạn có chắc muốn vứt bỏ toàn bộ nội dung các chương đã viết của "${title}" và để AI chắp bút viết lại từ đầu bằng model [${targetEngine.toUpperCase()}] không?\n\n(Dàn ý và thiết lập nhân vật vẫn sẽ được giữ nguyên)`)) {
      const qItem = useStore.getState().queue.find(q => q.id === id);
      useStore.getState().updateQueueItem(id, {
        status: 'pending',
        chaptersDone: 0,
        wordCount: 0,
        chaptersContent: [],
        finalEvaluation: undefined,
        errorLog: undefined,
        writeEngine: targetEngine as any,
        ...(targetStyle ? { storyStyle: targetStyle as any } : {}),
        regeneratedCount: (qItem?.regeneratedCount || 0) + 1,
        regeneratedModels: [...(qItem?.regeneratedModels || [qItem?.writeEngine || '']), targetEngine]
      });
      setSelectedId(null);
    }
  };

  const generateCoverPolli = (promptStr: string) => {
      const safePrompt = (promptStr || 'cinematic poster').replace(/"/g, '').substring(0, 400);
      return `https://pollinations.ai/p/${encodeURIComponent(safePrompt)}?width=800&height=1200&nologo=true&model=flux&seed=${Math.floor(Math.random()*100000)}`;
  };

  const handleCraftMetadata = async (item: QueueItem) => {
    setLoadingAction(`meta_${item.id}`);
    try {
      const promptTitle = item.finalEvaluation ? item.title + " - Overview: " + item.finalEvaluation.review : item.title;
      const meta = await agentPublisherMetadata('gemini', getActiveKey(), 'gemini-2.5-flash', item.bible, promptTitle);
      const pollUrl = generateCoverPolli(meta.coverImagePrompt || '');
      updateQueueItem(item.id, { publishData: { ...meta, coverUrl: pollUrl } });
      alert("✅ Đóng gói SEO và tạo ảnh bìa AI thành công!");
    } catch (e: unknown) {
      alert("Lỗi Đóng gói SEO: " + (e as Error).message);
    }
    setLoadingAction(null);
  };

  const handleUpdateCoverUrl = () => {
    if (!selectedItem) return;
    updateQueueItem(selectedItem.id, { 
      publishData: { ...(selectedItem.publishData || {} as any), coverUrl: customCoverUrl } 
    });
    alert("✅ Cập nhật Custom Cover URL thành công!");
  };

  const handleRegenerateCover = () => {
    if (!selectedItem) return;
    
    let promptToUse = customPrompt.trim();
    if (!promptToUse) {
      const safeTitle = selectedItem.title.substring(0, 100).replace(/"/g, '');
      promptToUse = `Cinematic vertical web novel cover art for a story named ${safeTitle}. Extremely detailed, masterpiece, beautiful lighting, highly aesthetic, trending on artstation.`;
      setCustomPrompt(promptToUse);
    }

    const pollUrl = generateCoverPolli(promptToUse);
    setCustomCoverUrl(pollUrl);
    updateQueueItem(selectedItem.id, { 
      publishData: { ...(selectedItem.publishData || {} as any), coverUrl: pollUrl, coverImagePrompt: promptToUse } 
    });
  };

  const handlePublishToWeb = async (item: QueueItem) => {
    if (!wpUrl || !wpUser || !wpAppPassword) {
      alert("Thiếu kết nối WordPress! Vui lòng kiểm tra lại Settings.");
      return;
    }

    if (activeTab === 'chapters') {
        const savedText = [...(item.chaptersContent || [])]
          .sort((a, b) => a.episode - b.episode)
          .map(ch => `Chương ${ch.episode}: ${ch.title.replace(/^(Chương|Tập|Episode)\s*\d+[:\-]?\s*/i, '')}\n\n${ch.content}`)
          .join('\n\n========================================\n\n');
          
        if (editableStoryText && editableStoryText !== savedText) {
            if (!window.confirm("Bạn đang có thay đổi chưa lưu trong phần Soạn Thảo. Bạn có muốn tiếp tục đăng bản CŨ lên web không?\n(Bấm Cancel để quay lại và bấm 'Lưu Chỉnh Sửa' trước khi đăng)")) {
                return;
            }
        }
    }

    setLoadingAction(`publish_${item.id}`);
    try {
      // Build blurb: Cố gắng lấy Tóm tắt chuẩn từ AI
      let bibleBlurb = (item.bible as any)?.overallSizzle || (item.bible as any)?.summary || '';
      if (!bibleBlurb && typeof (item.bible as any)?.series_premise === 'string') {
         const premise = (item.bible as any).series_premise;
         const match = premise.match(/(?:\[TÓM TẮT DÀNH CHO SEO & MARKETING\]|TÓM TẮT CÂU CHUYỆN|TÓM TẮT|SUMMARY)\s*\n+([\s\S]*?)(?:\n\n#|\n\n\*\*|$)/i);
         if (match && match[1]) {
            bibleBlurb = match[1].trim();
         } else {
            bibleBlurb = premise.slice(0, 400) + '...';
         }
      } else if (!bibleBlurb) {
         bibleBlurb = item.prompt ? item.prompt.slice(0, 400) + (item.prompt.length > 400 ? '...' : '') : '';
      }

      const pData = item.publishData || {
         finalTitle: item.title,
         categories: item.genres ? (Array.isArray(item.genres) ? item.genres : item.genres.split(',').map((s: string) => s.trim())) : [],
         tags: [],
         coverUrl: '',
         seoTitle: item.title,
         seoDescription: bibleBlurb.replace(/\n/g, ' ').slice(0, 160),
         seoFocusKeyword: '',
         blurb: bibleBlurb
      };
      
      const { finalTitle, categories, coverUrl, seoTitle, seoDescription, seoFocusKeyword, blurb } = pData;
      
      const htmlIntro = coverUrl ? `<div style="text-align: center; margin-bottom: 20px;"><img src="${coverUrl}" alt="${finalTitle}" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);" /></div>\n` : '';
      
      // Bọc <p> cho phần giới thiệu truyện
      const storyIntro = (blurb || bibleBlurb)
        .split(/\n\n+/)
        .map((p: string) => {
            const trimmed = p.trim();
            if (!trimmed) return '';
            const formatted = trimmed.replace(/\n/g, '<br/>').replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
            if (formatted.startsWith('<p>') || formatted.startsWith('<div')) return formatted;
            return `<p>${formatted}</p>`;
        })
        .join('\n');

      const metaObj = {
        rank_math_title: seoTitle,
        rank_math_description: seoDescription,
        rank_math_focus_keyword: seoFocusKeyword,
        seo_title: seoTitle,
        seo_description: seoDescription,
        primary_focus_keyword: seoFocusKeyword,
        ...(coverUrl ? { fifu_image_url: coverUrl, fifu_image_alt: finalTitle } : {})
      };

      let resolvedPostId = item.wpPostId;

      // Validate existing post ID — if invalid or missing, create a new one
      if (resolvedPostId) {
        try {
          await callWordPress({ wpUrl, wpUser, wpAppPassword, endpoint: `truyen/${resolvedPostId}`, method: 'GET', payload: {} });
        } catch (checkErr: any) {
          // 404 or other error → create fresh post
          console.warn(`WP Post ID ${resolvedPostId} invalid, creating fresh post...`, checkErr.message);
          resolvedPostId = undefined as any;
        }
      }

      // 🚨 SANITIZE GENRES: Prevent AI "garbage" tags or numeric hallucination 
      // by mapping strictly against the STORY_GENRE_LIST
      let rawCategories: string[] = [];
      if (Array.isArray(categories) && categories.length > 0) {
        rawCategories = categories;
      } else if (typeof categories === 'string' && (categories as string).trim().length > 0) {
        rawCategories = (categories as string).split(',').map((s: string) => s.trim());
      } else if (item.genres) {
        rawCategories = Array.isArray(item.genres) ? item.genres : item.genres.split(',').map((g: string) => g.trim());
      }
      
      const validGenreNames = STORY_GENRE_LIST.map(g => g.name.split(' (')[0].trim().toLowerCase());
      
      const sanitizedGenres = rawCategories.filter(Boolean).map(c => {
         const catStr = String(c).trim();
         // If it's a numeric ID that the AI hallucinated (like 100, 101), drop it.
         if (/^\d+$/.test(catStr)) return null;
         
         const catLower = catStr.toLowerCase();
         // Check if this string loosely matches one of our valid genres
         const match = validGenreNames.find(v => catLower.includes(v) || v.includes(catLower));
         
         // Only return safe names. If no exact match, allow it ONLY if it's longer than 2 chars and not purely numeric
         return match ? match.charAt(0).toUpperCase() + match.slice(1) : (catStr.length > 2 ? catStr : null);
      }).filter(Boolean);

      if (!resolvedPostId) {
        const newPost = await callWordPress({
          wpUrl, wpUser, wpAppPassword,
          endpoint: 'truyen',
          method: 'POST',
          payload: {
            title: finalTitle || item.title,
            content: htmlIntro + storyIntro,
            status: 'draft',
            ...(sanitizedGenres.length > 0 ? { the_loai: sanitizedGenres } : {}),
          }
        });
        resolvedPostId = newPost.id;
        if (!resolvedPostId) throw new Error('Không tạo được bài viết mới trên WordPress!');
        updateQueueItem(item.id, { wpPostId: resolvedPostId });
      }

      // Update Title & SEO Meta
      await callWordPress({
        wpUrl, wpUser, wpAppPassword,
        endpoint: `truyen/${resolvedPostId}`,
        method: 'POST',
        payload: {
          title: finalTitle,
          status: 'publish',
          ...(sanitizedGenres.length > 0 ? { the_loai: sanitizedGenres } : {}),
          meta: metaObj
        }
      });
      
      // Append Cover & Blurb
      // Append Cover & Blurb
      await callWordPress({
         wpUrl, wpUser, wpAppPassword,
         endpoint: `truyen/${resolvedPostId}`,
         method: 'POST',
         payload: { content: htmlIntro + storyIntro }
      });

      // Upload Chapters
      if (item.chaptersContent && item.chaptersContent.length > 0) {
        for (const chap of item.chaptersContent) {
           let rawTitle = chap.title || '';
           
           // Nếu title quá ngắn hoặc rỗng, cố gắng trích xuất từ dòng đầu của content
           if (!rawTitle || rawTitle.replace(/^(?:Chương|Tập|Episode)\s*\d+[:\-]?\s*/i, '').trim().length < 2) {
               const matchContent = chap.content?.match(/(?:Chương|Tập|Episode)\s*\d+[:\-]?\s*([^\n]+)/i);
               if (matchContent && matchContent[1].trim()) {
                   rawTitle = matchContent[1].trim();
               }
           }
           
           // Dọn dẹp các ký tự markdown dư thừa
           rawTitle = rawTitle.replace(/[\*#_]/g, '').trim();
           rawTitle = rawTitle.replace(/^(?:Chương|Tập|Episode)\s*\d+[:\-]?\s*/i, '').trim();
           
           const chapTitle = rawTitle ? `Chương ${chap.episode}: ${rawTitle}` : `Chương ${chap.episode}`;

           // Xử lý nội dung: Xoá dòng tiêu đề lặp lại ở đầu và bọc <p>
           let cleanedContent = chap.content || '';
           // Xoá dòng chứa "Chương X: Y" ở đầu để khỏi lặp với tên chương của web (do web đã tự render post_title)
           const titleRegex = new RegExp(`^(?:#+\\s*)?(?:\\*\\*)?(?:Chương|Tập|Episode)\\s*${chap.episode}[:\\-]?\\s*([^\\n]*)(?:\\*\\*)?`, 'im');
           cleanedContent = cleanedContent.replace(titleRegex, '').trim();

           // Bọc <p> cho các đoạn văn để web hiển thị đúng format, không bị dính cục
           const htmlContent = cleanedContent
             .split(/\n\n+/)
             .map(p => {
               const trimmed = p.trim();
               if (!trimmed) return '';
               // Bỏ qua nếu đã là HTML tag hợp lệ (chỉ bọc nếu là text thường)
               if (trimmed.startsWith('<p>') || trimmed.startsWith('<div')) return trimmed;
               return `<p>${trimmed.replace(/\n/g, '<br/>')}</p>`;
             })
             .join('\n');

           await callWordPress({
             wpUrl, wpUser, wpAppPassword,
             endpoint: 'chuong',
             method: 'POST',
             payload: {
               title: chapTitle,
               content: htmlContent,
               status: 'publish',
               meta: {
                 _truyen_id: String(resolvedPostId)
               }
             }
           });
        }
      }

      updateQueueItem(item.id, { status: 'published', publishedAt: Date.now() });
      alert(`✅ Lên sàn thành công! Đã lên Mẹ (Truyện) và đẻ trứng (${item.chaptersContent?.length || 0} Chương) lên Web!`);

    } catch (error: unknown) {
      alert("Lỗi WordPress: " + (error as Error).message);
    }
    setLoadingAction(null);
  };

  const handleCopyAllChapters = () => {
    if (!selectedItem || !selectedItem.chaptersContent) return;
    const allText = [...selectedItem.chaptersContent]
      .sort((a, b) => a.episode - b.episode)
      .map(ch => `Chương ${ch.episode}: ${ch.title}\n\n${ch.content.replace(/\\n/g, '\n').replace(/<[^>]+>/g, '')}`)
      .join('\n\n' + '='.repeat(40) + '\n\n');
    navigator.clipboard.writeText(allText).then(() => {
      alert("✅ Đã copy toàn bộ truyện vào Clipboard!");
    });
  };

  const handleSaveEdits = () => {
    if (!selectedItem) return;
    const newChapters: {episode: number, title: string, content: string}[] = [];
    let currentEp = 1;

    if (editableStoryText.match(/={10,}/)) {
        const sections = editableStoryText.split(/={10,}/).map(s => s.trim()).filter(Boolean);
        for (const section of sections) {
            const lines = section.split('\n');
            let title = `Chương ${currentEp}`;
            let contentLines = lines;
            if (lines.length > 0 && lines[0].match(/^(Chương|Tập|Episode)\s*\d+/i)) {
                title = lines[0].trim();
                contentLines = lines.slice(1);
            }
            const content = contentLines.join('\n').trim();
            if (content) newChapters.push({ episode: currentEp++, title, content });
        }
    } else {
        const regex = /^\s*(Chương\s+\d+[:.\-\s]*(.*))$/gim;
        const match = regex.exec(editableStoryText);
        if (!match) {
            if (editableStoryText.trim()) newChapters.push({ episode: 1, title: 'Chương 1', content: editableStoryText.trim() });
        } else {
            regex.lastIndex = 0;
            let nextMatch = regex.exec(editableStoryText);
            while (nextMatch !== null) {
                const matchStart = nextMatch.index;
                const titleLine = nextMatch[1].trim();
                const nextNextMatch = regex.exec(editableStoryText);
                const content = editableStoryText.substring(matchStart + nextMatch[0].length, nextNextMatch ? nextNextMatch.index : undefined).trim();
                if (content) newChapters.push({ episode: currentEp++, title: titleLine, content });
                nextMatch = nextNextMatch;
            }
        }
    }
    
    updateQueueItem(selectedItem.id, { chaptersContent: newChapters });
    alert("✅ Đã lưu chỉnh sửa vào nội bộ thành công!");
  };

  const handleAiAutoFix = async () => {
    if (!selectedItem) return;
    setLoadingAction(`fix_${selectedItem.id}`);
    try {
      const state = useStore.getState();
      let engine = 'gemini';
      let model = 'gemini-2.5-pro'; // Use pro for larger context
      let key = getActiveKey();

      if (fixModel === 'qwen') {
        engine = 'qwen'; model = 'qwen-plus'; key = state.qwenKey;
      } else if (fixModel === 'openai') {
        engine = 'openai'; model = 'gpt-4o'; key = state.openAIKey;
      } else if (fixModel === 'claude') {
        engine = 'claude'; model = 'claude-3-5-sonnet-20241022'; key = state.claudeKey;
      } else if (fixModel === 'deepseek') {
        engine = 'deepseek'; model = 'deepseek-reasoner'; key = state.deepseekKey;
      }

      if (!key) throw new Error(`Thiếu API Key cho mô hình ${fixModel.toUpperCase()}`);

      const sections = editableStoryText.split(/={10,}/).map((s: string) => s.trim()).filter(Boolean);
      if (sections.length === 0) throw new Error("Không có nội dung để sửa.");

      const critique = selectedItem.finalEvaluation?.review || '';
      const fixedSections: string[] = [];
      const newChapters: {episode: number, title: string, content: string}[] = [];
      let currentEp = 1;

      for (let i = 0; i < sections.length; i++) {
          setFixProgress({ current: i + 1, total: sections.length });
          
          const fullStoryContext = fixedSections.concat(sections.slice(i)).join('\n\n========================================\n\n');
          
          const fixedChapterText = await agentStoryFixer(
              engine, 
              key, 
              model, 
              selectedItem.bible, 
              sections[i], 
              critique, 
              fullStoryContext
          );

          if (fixedChapterText && fixedChapterText.length > 50) {
              fixedSections.push(fixedChapterText);
              
              // Cập nhật UI theo thời gian thực để người dùng thấy chữ đang đổi
              const realTimeText = fixedSections.concat(sections.slice(i + 1)).join('\n\n========================================\n\n');
              setEditableStoryText(realTimeText);
              
              const lines = fixedChapterText.split('\n');
              let title = `Chương ${currentEp}`;
              let contentLines = lines;
              if (lines.length > 0 && lines[0].match(/^(Chương|Tập|Episode)\s*\d+/i)) {
                  title = lines[0].trim();
                  contentLines = lines.slice(1);
              }
              const content = contentLines.join('\n').trim();
              if (content) {
                  newChapters.push({ episode: currentEp, title: title, content: content });
                  currentEp++;
              }
          } else {
              throw new Error(`AI trả về kết quả rỗng cho Chương ${i + 1}.`);
          }
      }

      // Lưu chính thức
      updateQueueItem(selectedItem.id, { chaptersContent: newChapters });
      setFixProgress(null);
      
      // Auto Re-Evaluate
      const updatedItem = { ...selectedItem, chaptersContent: newChapters };
      try {
          const evalData = await agentStoryEvaluator(engine, key, model, updatedItem.bible, updatedItem.chaptersContent);
          updateQueueItem(selectedItem.id, { finalEvaluation: { ...evalData, evaluator: `${fixModel.toUpperCase()} (${model})` } });
          alert("✨ MAGIC! TỔNG BIÊN TẬP AI đã Cắt gọt, Sửa từng chương, Lưu tự động và Đánh giá lại thành công!");
      } catch (evalErr) {
          alert("✅ Đã sửa lỗi và lưu, nhưng phần Đánh giá lại bị lỗi: " + evalErr);
      }
    } catch (e: any) {
      alert("Lỗi AI Auto-Fix: " + (e.message || JSON.stringify(e)));
    }
    setFixProgress(null);
    setLoadingAction(null);
  };

  return (
    <div className="flex w-full h-full min-h-0 font-sans bg-[#0a0a10] text-[#e2e8f0] overflow-hidden animation-fade-in relative z-10">
       
       {/* MASTER SIDEBAR: List of Stories */}
       <div className={`bg-[#13131f] border-r border-white/5 flex flex-col shrink-0 z-20 transition-all duration-300 ${isSidebarHidden ? 'w-0 overflow-hidden opacity-0 border-r-0' : 'w-[340px] opacity-100'}`}>
          <div className="p-6 border-b border-white/5 bg-[#0a0a10]/50 backdrop-blur-md sticky top-0 whitespace-nowrap">
             <h2 className="text-[20px] font-black bg-gradient-to-r from-pink-500 to-violet-500 bg-clip-text text-transparent flex items-center gap-2 tracking-tight">
               <ShieldAlert className="text-pink-500"/> Gatekeeper
             </h2>
             <p className="text-xs text-slate-400 mt-1 font-medium">Duyệt & Tối ưu ({reviewItems.length} truyện)</p>
          </div>
          <div className="flex-1 overflow-y-auto custom-scrollbar p-4 space-y-3">
             {reviewItems.length === 0 ? (
                <div className="h-40 flex flex-col items-center justify-center text-slate-500 border-2 border-dashed border-white/5 rounded-xl">
                   <p className="text-xs font-bold">Chưa có truyện nào hoàn thành.</p>
                </div>
             ) : (
                reviewItems.map(item => (
                   <button key={item.id} onClick={() => setSelectedId(item.id)} className={`w-full text-left p-4 rounded-xl border transition-all relative overflow-hidden group ${selectedId === item.id ? 'bg-indigo-500/10 border-indigo-500/50 shadow-[0_4px_20px_rgba(99,102,241,0.15)]' : 'bg-white/5 border-transparent hover:bg-white/10'}`}>
                      {selectedId === item.id && <div className="absolute left-0 top-0 bottom-0 w-1 bg-indigo-500 rounded-l-xl"></div>}
                      <div className="flex flex-wrap gap-2 mb-2 items-center">
                         <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 bg-black/40 px-2 py-0.5 rounded">{(Array.isArray(item.genres) ? item.genres[0] : (item.genres || '').split(',')[0])}</span>
                         <span className="text-[10px] font-bold uppercase tracking-wider text-purple-400 bg-purple-900/30 px-2 py-0.5 rounded">
                           {item.isAdvancedPipeline ? "Sáng tác 7" : item.comboType === 6 ? "Sáng tác 6" : item.comboType === 5 ? "Sáng tác 5" : "Thủ công"}
                         </span>
                         {item.status === 'published' && <span className="text-[10px] font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-1"><Rocket size={10}/> Đã Đăng</span>}
                         {item.regeneratedCount ? <span title={item.regeneratedModels ? `Model History: ${item.regeneratedModels.join(' ➔ ')}` : ''} className="text-[10px] font-bold uppercase tracking-wider text-amber-500 bg-amber-500/10 px-2 py-0.5 rounded cursor-help">🔄 Gen lại x{item.regeneratedCount} ({item.regeneratedModels ? item.regeneratedModels[item.regeneratedModels.length - 1] : item.writeEngine})</span> : null}
                      </div>
                      <h3 className={`font-bold line-clamp-2 leading-tight mb-2 ${selectedId === item.id ? 'text-indigo-300' : 'text-white group-hover:text-indigo-200'} transition-colors`}>{item.publishData?.finalTitle || item.title}</h3>
                      <div className="text-[11px] text-slate-500 font-medium">
                         {item.chaptersDone}/{item.targetChapters} Chương • {item.wordCount} Chữ
                      </div>
                   </button>
                ))
             )}
          </div>
       </div>

       {/* DETAIL AREA */}
       {selectedItem ? (
           <div className="flex-1 flex flex-col min-w-0 min-h-0 bg-[#0a0a10] relative z-10 transition-all">
              
              {/* Header */}
              <div className="h-auto shrink-0 border-b border-white/5 bg-[#17172a] px-6 py-4 flex flex-col gap-4">
                 {/* Top Row: Title and Tags */}
                 <div className="flex flex-col w-full gap-2">
                    <div className="flex items-center gap-3">
                        {isSidebarHidden && (
                          <button onClick={() => setIsSidebarHidden(false)} className="bg-white/5 hover:bg-white/10 p-2 rounded-lg text-slate-300 transition-colors shrink-0" title="Hiện danh sách">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
                          </button>
                        )}
                        <h2 className="text-xl font-black text-white line-clamp-1 leading-snug" title={selectedItem.publishData?.finalTitle || selectedItem.title}>{selectedItem.publishData?.finalTitle || selectedItem.title}</h2>
                    </div>
                    <div className="text-xs text-slate-400 flex flex-wrap items-center gap-x-2 gap-y-2 font-medium w-full">
                        <span className="text-emerald-400 flex items-center gap-1"><PenTool size={12}/>{selectedItem.wordCount} chữ</span>
                        <span className="flex items-center gap-1"><BookOpen size={12}/>{selectedItem.chaptersDone}/{selectedItem.targetChapters} chương</span>
                        <span className="text-purple-400 font-bold uppercase tracking-wider bg-purple-900/40 px-2 py-0.5 rounded text-[10px] whitespace-nowrap">
                           {selectedItem.isAdvancedPipeline ? "Nguồn: Sáng tác 7" : selectedItem.comboType === 6 ? "Nguồn: Sáng tác 6" : selectedItem.comboType === 5 ? "Nguồn: Sáng tác 5" : "Nguồn: Thủ công"}
                        </span>
                        {selectedItem.genres && (
                          <span className="text-cyan-400 bg-cyan-900/40 border border-cyan-500/20 px-2 py-0.5 rounded text-[10px] uppercase font-bold tracking-wider whitespace-nowrap">
                            Thể loại: {Array.isArray(selectedItem.genres) ? selectedItem.genres.join(', ') : selectedItem.genres}
                          </span>
                        )}
                        {selectedItem.storyStyle && (
                          <span className="text-pink-400 bg-pink-900/40 border border-pink-500/20 px-2 py-0.5 rounded text-[10px] uppercase font-bold tracking-wider whitespace-nowrap">
                            Văn phong: {STORY_GENRE_LIST.find(g => g.id === selectedItem.storyStyle)?.name || selectedItem.storyStyle}
                          </span>
                        )}
                        {selectedItem.createdAt && (
                          <span suppressHydrationWarning className="text-slate-400 bg-slate-800/80 px-2 py-0.5 rounded border border-slate-700 text-[10px] uppercase font-bold tracking-wider whitespace-nowrap">
                            Tạo: {new Date(selectedItem.createdAt).toLocaleString('vi-VN', { hour: '2-digit', minute: '2-digit', day: '2-digit', month: '2-digit', year: 'numeric' })}
                          </span>
                        )}
                        {selectedItem.publishedAt ? (
                          <span suppressHydrationWarning className="text-emerald-400 bg-emerald-900/40 border border-emerald-500/20 px-2 py-0.5 rounded text-[10px] uppercase font-bold tracking-wider flex items-center gap-1 whitespace-nowrap">
                            <Rocket size={10}/> Đăng lúc: {new Date(selectedItem.publishedAt).toLocaleString('vi-VN', { hour: '2-digit', minute: '2-digit', day: '2-digit', month: '2-digit', year: 'numeric' })}
                          </span>
                        ) : selectedItem.completedAt ? (
                          <span suppressHydrationWarning className="text-indigo-400 bg-indigo-900/40 border border-indigo-500/20 px-2 py-0.5 rounded text-[10px] uppercase font-bold tracking-wider flex items-center gap-1 whitespace-nowrap">
                            Xong lúc: {new Date(selectedItem.completedAt).toLocaleString('vi-VN', { hour: '2-digit', minute: '2-digit', day: '2-digit', month: '2-digit', year: 'numeric' })}
                          </span>
                        ) : null}
                        {selectedItem.regeneratedCount ? (
                          <span title={selectedItem.regeneratedModels ? `History: ${selectedItem.regeneratedModels.join(' ➔ ')}` : ''} className="text-amber-500 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20 text-[10px] uppercase font-bold tracking-wider cursor-help whitespace-nowrap">
                            🔄 Đã Gen Lại {selectedItem.regeneratedCount} lần ({selectedItem.regeneratedModels ? selectedItem.regeneratedModels[selectedItem.regeneratedModels.length - 1] : selectedItem.writeEngine})
                          </span>
                        ) : null}
                        <span className="uppercase text-slate-500 flex items-center pl-1 border-l border-white/5 ml-1 whitespace-nowrap">• {selectedItem.status === 'published' ? '✅ Đã Lên Sàn' : '⏳ Chờ Xét Duyệt'}</span>
                    </div>
                 </div>

                 {/* Bottom Row: Buttons */}
                 <div className="flex items-center gap-3 w-full justify-between lg:justify-start">
                     <button onClick={() => handleDeleteStory(selectedItem.id, selectedItem.title)} className="bg-rose-500/10 text-rose-500 hover:bg-rose-500/20 px-4 py-2.5 rounded-xl flex items-center gap-2 text-xs font-bold transition-all border border-rose-500/20">
                         <Trash2 size={16}/> Xóa Bỏ
                     </button>
                     <div className="flex items-center gap-0 border border-amber-500/30 bg-amber-500/10 rounded-xl overflow-hidden transition-all hover:bg-amber-500/20">
                         <select 
                             value={regenStyle || selectedItem.storyStyle || ''} 
                             onChange={e => setRegenStyle(e.target.value)} 
                             className="bg-transparent border-r border-amber-500/30 outline-none text-[11px] text-amber-500 font-bold focus:ring-0 px-2 py-2.5 h-full cursor-pointer appearance-none text-center max-w-[120px] truncate"
                             title="Thể loại / Văn phong"
                         >
                             <option value="" disabled>-- Văn phong --</option>
                             {STORY_GENRE_LIST.map(g => (
                               <option key={g.id} value={g.id}>{g.name}</option>
                             ))}
                         </select>
                         <select value={regenEngine || selectedItem.writeEngine || 'gemini'} onChange={e => setRegenEngine(e.target.value as any)} className="bg-transparent border-r border-amber-500/30 outline-none text-[11px] text-amber-500 font-bold focus:ring-0 px-2 py-2.5 h-full cursor-pointer appearance-none text-center">
                             <option value="gemini">Gemini</option>
                             <option value="qwen">Qwen</option>
                             <option value="openai">OpenAI</option>
                             <option value="claude">Claude</option>
                             <option value="grok">Grok</option>
                             <option value="deepseek">DeepSeek</option>
                         </select>
                         <button onClick={() => handleRegenerateStory(selectedItem.id, selectedItem.title, regenEngine || selectedItem.writeEngine || 'gemini', regenStyle || selectedItem.storyStyle)} className="text-amber-500 px-4 py-2.5 flex items-center gap-2 text-xs font-bold transition-all">
                             <RefreshCw size={14} className={loadingAction ? 'animate-spin' : ''}/> Gen Lại
                         </button>
                     </div>
                     <button onClick={() => handlePublishToWeb(selectedItem)} disabled={loadingAction === `publish_${selectedItem.id}`} className="bg-gradient-to-r from-emerald-500 to-teal-500 text-slate-900 font-extrabold text-xs uppercase tracking-widest px-5 py-2.5 rounded-xl flex items-center gap-2 hover:opacity-90 disabled:opacity-50 disabled:grayscale transition-all shadow-[0_4px_20px_rgba(16,185,129,0.3)] hover:shadow-[0_4px_30px_rgba(16,185,129,0.5)] transform hover:-translate-y-0.5">
                        {loadingAction === `publish_${selectedItem.id}` ? <RefreshCw className="animate-spin" size={16}/> : <UploadCloud size={16}/>}
                        {selectedItem.status === 'published' ? 'Cập Nhật Lên WP' : 'Bắn Lên WP'}
                     </button>
                 </div>
              </div>

              {/* Tabs Nav */}
              <div className="flex border-b border-white/5 px-8 pt-5 gap-8 bg-[#17172a] shrink-0">
                  <button onClick={() => setActiveTab('overview')} className={`pb-4 text-[13px] font-black uppercase tracking-wider border-b-2 transition-all flex items-center gap-2 ${activeTab === 'overview' ? 'text-indigo-400 border-indigo-400' : 'text-slate-500 border-transparent hover:text-white'}`}><Star size={14}/> TỔNG QUAN & SEO</button>
                  <button onClick={() => setActiveTab('bible')} className={`pb-4 text-[13px] font-black uppercase tracking-wider border-b-2 transition-all flex items-center gap-2 ${activeTab === 'bible' ? 'text-indigo-400 border-indigo-400' : 'text-slate-500 border-transparent hover:text-white'}`}><BookOpen size={14}/> KINH THÁNH (STORY BIBLE)</button>
                  <button onClick={() => setActiveTab('chapters')} className={`pb-4 text-[13px] font-black uppercase tracking-wider border-b-2 transition-all flex items-center gap-2 ${activeTab === 'chapters' ? 'text-emerald-400 border-emerald-400' : 'text-slate-500 border-transparent hover:text-white'}`}>
                      <FileText size={14}/> ĐỌC TRUYỆN ({selectedItem.chaptersContent?.length || 0})
                  </button>
              </div>

              {/* Tab Contents */}
              <div className="flex-1 min-h-0 overflow-y-auto custom-scrollbar p-6 lg:p-8 relative">
                  
                  {activeTab === 'overview' && (
                     <div className="flex flex-col lg:flex-row gap-8 animation-fade-in max-w-[1200px] mx-auto">
                        {/* Cột trái: Ảnh bìa & Trình sửa Meta */}
                        <div className="w-full lg:w-[360px] flex flex-col shrink-0">
                           <div className="bg-[#17172a] border border-white/5 rounded-2xl p-6 mb-6 shadow-xl">
                               {(customCoverUrl || selectedItem.publishData?.coverUrl) ? (
                                  <div className="relative group rounded-xl overflow-hidden shadow-[0_10px_30px_rgba(0,0,0,0.5)] mb-6 aspect-[2/3] bg-black/40 border border-white/5 flex items-center justify-center">
                                      {/* eslint-disable-next-line @next/next/no-img-element */}
                                      <img src={customCoverUrl || selectedItem.publishData?.coverUrl || ''} className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 relative z-10" alt="Cover" />
                                      <div className="absolute inset-0 flex items-center justify-center z-0 text-slate-600 text-xs">
                                        <div className="animate-pulse flex flex-col items-center">
                                          <ImageIcon size={30} className="mb-2 opacity-50"/> 
                                          <span>Đang tải ảnh AI...</span>
                                        </div>
                                      </div>
                                  </div>
                               ) : (
                                  <div className="w-full aspect-[2/3] object-cover rounded-xl border-2 border-dashed border-white/10 flex items-center justify-center text-slate-500 mb-6 bg-black/20">
                                      <div className="text-center"><ImageIcon size={40} className="mx-auto mb-2 opacity-30"/> <div className="text-xs font-bold uppercase tracking-wider mt-2">Chưa Có Bìa AI</div></div>
                                  </div>
                               )}
                               
                               <div className="space-y-4 mb-6">
                                 <div>
                                   <label className="text-[10px] font-black text-slate-500 uppercase tracking-widest mb-2 block">✏️ Thay Đổi URL Ảnh Bìa Tùy Chọn</label>
                                   <div className="flex gap-2">
                                     <input type="text" value={customCoverUrl} onChange={e => setCustomCoverUrl(e.target.value)} className="flex-1 bg-black/40 border border-white/10 rounded-lg px-3 py-2 text-xs text-white outline-none focus:border-indigo-500 transition-colors" placeholder="Paste URL ảnh từ nơi khác..." />
                                     <button onClick={handleUpdateCoverUrl} className="bg-indigo-500/20 text-indigo-400 text-xs px-4 rounded-lg hover:bg-indigo-500/30 font-bold transition-colors">LƯU</button>
                                   </div>
                                 </div>
                                 <div className="pt-2 border-t border-white/5">
                                   <label className="text-[10px] font-black text-fuchsia-500 uppercase tracking-widest mb-2 block">🎨 Sửa Prompt Bắt Vẽ Lại Bìa Chuyên Sâu</label>
                                   <textarea value={customPrompt} onChange={e => setCustomPrompt(e.target.value)} rows={4} className="w-full bg-black/40 border border-white/10 rounded-lg p-3 text-xs text-slate-300 outline-none focus:border-fuchsia-500 resize-none line-clamp-4 leading-relaxed" placeholder="Miêu tả tiếng Anh để Gen AI..." />
                                   <button onClick={handleRegenerateCover} className="w-full mt-2 bg-gradient-to-r from-fuchsia-600 to-indigo-600 text-white hover:opacity-90 py-2.5 rounded-lg text-xs font-bold shadow-lg transition-all flex items-center justify-center gap-2"><PenTool size={14}/> Vẽ Lại AI Bìa Mới</button>
                                 </div>
                               </div>
                  
                               <button onClick={() => handleCraftMetadata(selectedItem)} disabled={loadingAction === `meta_${selectedItem.id}`} className="w-full py-3 bg-slate-800 hover:bg-slate-700 text-white rounded-xl text-sm font-bold border border-white/5 flex justify-center items-center gap-2 transition-all">
                                  {loadingAction === `meta_${selectedItem.id}` ? <RefreshCw className="animate-spin" size={16}/> : <Rocket size={16} className="text-amber-500"/>}
                                  Auto Đóng Gói SEO & Bìa Từ Đầu
                               </button>
                           </div>
                        </div>
                  
                        {/* Cột phải: Đánh giá & SEO RankMath */}
                        <div className="flex-1 flex flex-col gap-6">
                           <div className="bg-[#17172a] border border-white/5 rounded-2xl p-8 relative overflow-hidden">
                              <div className="flex justify-between items-center mb-6 relative z-10 flex-wrap gap-4">
                                  <h3 className="text-xl font-black text-amber-400 flex items-center gap-2"><Star className="text-amber-400"/> Phán Xét Của Lãnh Chúa (AI Review)</h3>
                                  <div className="flex items-center gap-3">
                                      <select value={evalModel} onChange={(e: any) => setEvalModel(e.target.value)} className="bg-black/40 border border-white/10 text-xs text-slate-300 rounded-lg px-3 py-2 outline-none">
                                          <option value="gemini">Gemini (Free)</option>
                                          <option value="qwen">Qwen Max</option>
                                          <option value="openai">GPT-4o Mini</option>
                                      </select>
                                      <button onClick={() => handleEvaluate(selectedItem)} disabled={loadingAction === `eval_${selectedItem.id}`} className="bg-amber-500/10 hover:bg-amber-500/20 text-amber-400 border border-amber-500/30 font-bold text-xs px-5 py-2.5 rounded-xl flex items-center gap-2 transition-all">
                                         {loadingAction === `eval_${selectedItem.id}` ? <RefreshCw className="animate-spin" size={14}/> : <CheckCircle2 size={14}/>} {selectedItem.finalEvaluation ? 'Yêu Cầu Chấm Lại' : 'Phân Tích Toàn Bộ Truyện'}
                                      </button>
                                  </div>
                              </div>
                              
                              {selectedItem.finalEvaluation ? (
                                  <div className="flex gap-6 items-start relative z-10">
                                      <div className="w-24 h-24 rounded-full bg-amber-500/10 border-4 border-amber-500/20 flex flex-col items-center justify-center text-amber-500 font-black text-4xl shrink-0 shadow-[0_0_30px_rgba(245,158,11,0.2)]">
                                          {selectedItem.finalEvaluation.score}<span className="text-[10px] text-amber-500/50 mt-1 uppercase">Điểm</span>
                                      </div>
                                      <div className="text-[15px] font-medium text-slate-300 leading-relaxed italic border-l-4 border-amber-500/30 pl-6 space-y-2">
                                         <p>{selectedItem.finalEvaluation.review}</p>
                                         <p className="text-xs text-slate-500 mt-2 font-bold uppercase tracking-wider">ĐÁNH GIÁ BỞI: {selectedItem.finalEvaluation.evaluator}</p>
                                      </div>
                                  </div>
                              ) : (
                                  <div className="text-sm text-slate-500 text-center py-10 border-2 border-dashed border-white/5 rounded-2xl bg-black/20 font-medium">
                                      Chưa có đánh giá nào cho tác phẩm này.<br/>Bấm nút &quot;Phân Tích Toàn Bộ Truyện&quot; để AI đọc hết nội dung các tập đã sinh và vạch lá tìm sâu Plot Hole nhé!
                                  </div>
                              )}
                           </div>
                  
                           {selectedItem.publishData && (
                           <div className="bg-[#1e2336] border border-emerald-500/20 rounded-2xl p-8 relative overflow-hidden shadow-lg">
                               <div className="absolute top-0 right-0 p-4 opacity-5 pointer-events-none"><Rocket size={150}/></div>
                               <h3 className="text-xl font-black text-emerald-400 mb-6 relative z-10 flex items-center gap-2"><UploadCloud size={20}/> Tối Ưu Hóa Chuẩn SEO RankMath</h3>
                               <div className="grid grid-cols-1 md:grid-cols-2 gap-6 relative z-10">
                                   <div className="col-span-full">
                                       <label className="text-[10px] font-black text-emerald-500/70 uppercase tracking-widest block mb-1">Tên Bài Đăng Thực Tế (Giật Tít)</label>
                                       <div className="text-white font-bold bg-black/40 p-3 rounded-lg border border-white/5 text-[15px]">{selectedItem.publishData.finalTitle}</div>
                                   </div>
                                   <div className="col-span-full">
                                       <label className="text-[10px] font-black text-slate-500 uppercase tracking-widest block mb-1">RankMath SEO Title</label>
                                       <div className="text-indigo-200 font-medium text-sm bg-black/40 p-3 rounded-lg border border-white/5 italic">{selectedItem.publishData.seoTitle}</div>
                                   </div>
                                   <div className="col-span-1">
                                       <label className="text-[10px] font-black text-slate-500 uppercase tracking-widest block mb-1">RankMath Focus Keyword</label>
                                       <div className="text-emerald-400 font-bold bg-emerald-500/10 inline-block px-3 py-1.5 rounded-lg text-sm border border-emerald-500/20">{selectedItem.publishData.seoFocusKeyword}</div>
                                   </div>
                                   <div className="col-span-1">
                                       <label className="text-[10px] font-black text-slate-500 uppercase tracking-widest block mb-1">Danh Mục WP Tự Gán</label>
                                       <div className="flex flex-wrap gap-2 mt-1">
                                           {selectedItem.publishData.categories?.map((c,i)=> <span key={i} className="bg-indigo-500/20 text-indigo-300 text-[11px] font-bold px-2 py-1 rounded-md border border-indigo-500/30 uppercase tracking-wider">{c}</span>)}
                                       </div>
                                   </div>
                                   <div className="col-span-full">
                                       <label className="text-[10px] font-black text-slate-500 uppercase tracking-widest block mb-1">RankMath Meta Description</label>
                                       <div className="text-slate-300 font-medium text-sm bg-black/40 p-3 rounded-lg border border-white/5 leading-relaxed">{selectedItem.publishData.seoDescription}</div>
                                   </div>
                               </div>
                           </div>
                           )}
                        </div>
                     </div>
                  )}

                  {activeTab === 'bible' && (
                     <div className="max-w-[1200px] mx-auto space-y-8 animation-fade-in text-[15px] text-slate-300 leading-[1.8] font-medium pb-10">
                        <div className="bg-[#17172a] border border-white/5 p-8 rounded-2xl shadow-lg relative overflow-hidden">
                           <div className="absolute left-0 top-0 bottom-0 w-1.5 bg-indigo-500"></div>
                           <h3 className="text-indigo-400 font-black mb-4 uppercase tracking-widest text-sm flex items-center gap-2"><BookOpen size={16}/> Series Premise (Tóm Tắt Tổng Thể)</h3>
                           <div className="whitespace-pre-wrap">{(selectedItem.bible as any)?.series_premise || (selectedItem.bible as any)?.summary || selectedItem.prompt}</div>
                        </div>
                        
                        {(selectedItem.bible as any)?.character_bible ? (
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                                <div className="bg-[#17172a] border border-emerald-500/20 p-8 rounded-2xl shadow-lg relative overflow-hidden">
                                   <div className="absolute left-0 top-0 bottom-0 w-1.5 bg-emerald-500"></div>
                                   <h3 className="text-emerald-400 font-black mb-4 uppercase tracking-widest text-sm">🎭 Character Bible (Hồ Sơ Nhân Vật)</h3>
                                   <div className="whitespace-pre-wrap">{(selectedItem.bible as any)?.character_bible || 'Chưa có thông tin'}</div>
                                </div>
                                
                                <div className="space-y-8">
                                   <div className="bg-[#17172a] border border-amber-500/20 p-8 rounded-2xl shadow-lg relative overflow-hidden">
                                      <div className="absolute left-0 top-0 bottom-0 w-1.5 bg-amber-500"></div>
                                      <h3 className="text-amber-400 font-black mb-4 uppercase tracking-widest text-sm">🗝 Hidden Secrets Map (Bản Đồ Bí Mật)</h3>
                                      <div className="whitespace-pre-wrap">{(selectedItem.bible as any)?.hidden_secrets_map || 'Chưa có thông tin'}</div>
                                   </div>
                                   <div className="bg-[#17172a] border border-rose-500/20 p-8 rounded-2xl shadow-lg relative overflow-hidden">
                                      <div className="absolute left-0 top-0 bottom-0 w-1.5 bg-rose-500"></div>
                                      <h3 className="text-rose-400 font-black mb-4 uppercase tracking-widest text-sm">📈 Emotional Ladder (Thang Cảm Xúc)</h3>
                                      <div className="whitespace-pre-wrap">{(selectedItem.bible as any)?.emotional_escalation_ladder || 'Chưa có thông tin'}</div>
                                   </div>
                                   <div className="bg-[#17172a] border border-fuchsia-500/20 p-8 rounded-2xl shadow-lg relative overflow-hidden">
                                      <div className="absolute left-0 top-0 bottom-0 w-1.5 bg-fuchsia-500"></div>
                                      <h3 className="text-fuchsia-400 font-black mb-4 uppercase tracking-widest text-sm">🛑 Forbidden Rules (Cấm Kỵ Plot)</h3>
                                      <div className="whitespace-pre-wrap">{(selectedItem.bible as any)?.forbidden_inconsistencies || 'Chưa có thông tin'}</div>
                                   </div>
                                </div>
                            </div>
                        ) : (
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                                <div className="bg-[#17172a] border border-emerald-500/20 p-8 rounded-2xl shadow-lg relative overflow-hidden">
                                   <div className="absolute left-0 top-0 bottom-0 w-1.5 bg-emerald-500"></div>
                                   <h3 className="text-emerald-400 font-black mb-4 uppercase tracking-widest text-sm">🌍 Bối Cảnh Thế Giới</h3>
                                   <div className="whitespace-pre-wrap">{(selectedItem.bible as any)?.worldSettings || 'Chưa có thông tin'}</div>
                                </div>
                                <div className="bg-[#17172a] border border-amber-500/20 p-8 rounded-2xl shadow-lg relative overflow-hidden">
                                   <div className="absolute left-0 top-0 bottom-0 w-1.5 bg-amber-500"></div>
                                   <h3 className="text-amber-400 font-black mb-4 uppercase tracking-widest text-sm">🤕 Arc Nhân Vật / Nỗi Đau</h3>
                                   <div className="whitespace-pre-wrap">{(selectedItem.bible as any)?.characterArc || 'Chưa có thông tin'}</div>
                                </div>
                                <div className="bg-[#17172a] border border-rose-500/20 p-8 rounded-2xl shadow-lg relative overflow-hidden">
                                   <div className="absolute left-0 top-0 bottom-0 w-1.5 bg-rose-500"></div>
                                   <h3 className="text-rose-400 font-black mb-4 uppercase tracking-widest text-sm">🌪️ Cú Twist Lật Bàn</h3>
                                   <div className="whitespace-pre-wrap">{(selectedItem.bible as any)?.plotTwists || 'Chưa có thông tin'}</div>
                                </div>
                                <div className="bg-[#17172a] border border-fuchsia-500/20 p-8 rounded-2xl shadow-lg relative overflow-hidden">
                                   <div className="absolute left-0 top-0 bottom-0 w-1.5 bg-fuchsia-500"></div>
                                   <h3 className="text-fuchsia-400 font-black mb-4 uppercase tracking-widest text-sm">🔥 Độ Bạo Não Truyện</h3>
                                   <div className="whitespace-pre-wrap">{(selectedItem.bible as any)?.overallSizzle || 'Chưa có thông tin'}</div>
                                </div>
                            </div>
                        )}
                     </div>
                  )}

                  {activeTab === 'chapters' && (
                     <div className="flex flex-col min-h-full animation-fade-in max-w-[1400px] mx-auto pb-10 w-full">
                         {(!selectedItem.chaptersContent || selectedItem.chaptersContent.length === 0) ? (
                             <div className="w-full flex-1 flex flex-col items-center justify-center text-slate-500 py-32 border-2 border-dashed border-white/5 rounded-3xl bg-black/20">
                                 <FileText size={64} className="mb-6 opacity-30 text-indigo-500"/>
                                 <h4 className="text-xl font-bold text-slate-400 mb-2">Chưa có dữ liệu chương nội bộ</h4>
                                 <p className="font-medium text-center max-w-lg leading-relaxed text-sm">
                                     (Kể từ bản nâng cấp hệ thống này, các chương được AI viết ở phần Auto-Pilot sẽ được lưu lại trực tiếp vào đây để anh tổng duyệt. Tuy nhiên, truyện này được gen trước đó nên nội dung không được lưu cục bộ. Hãy ra ngoài xem trên WordPress nhé!)
                                 </p>
                             </div>
                         ) : (
                             <div className="w-full flex-1 flex flex-col bg-[#17172a] border border-white/5 rounded-2xl p-6 text-[#cbd5e1] relative shadow-xl">
                                <div className="flex flex-wrap items-center justify-between gap-4 mb-4 border-b border-white/10 pb-4 shrink-0">
                                    <div className="flex items-center gap-3">
                                        <h3 className="text-lg font-black text-white flex items-center gap-2"><PenTool className="text-indigo-400" size={18}/> Soạn Thảo Siêu Tốc</h3>
                                    </div>
                                    <div className="flex items-center gap-3">
                                        <div className="flex items-center gap-0 border border-fuchsia-500/30 bg-fuchsia-500/10 rounded-lg overflow-hidden transition-all hover:bg-fuchsia-500/20">
                                            <select value={fixModel} onChange={(e: any) => setFixModel(e.target.value)} className="bg-transparent border-r border-fuchsia-500/30 outline-none text-[11px] text-fuchsia-400 font-bold focus:ring-0 px-2 h-full cursor-pointer appearance-none text-center">
                                                <option value="gemini">Gemini Pro</option>
                                                <option value="qwen">Qwen Max</option>
                                                <option value="openai">GPT-4o</option>
                                                <option value="claude">Claude Sonnet</option>
                                                <option value="deepseek">DeepSeek</option>
                                            </select>
                                            <button onClick={handleAiAutoFix} disabled={!!loadingAction} className="text-fuchsia-400 px-4 py-2 text-xs font-bold transition-all flex items-center gap-2 disabled:opacity-50">
                                                {fixProgress ? <><RefreshCw className="animate-spin" size={14}/> Sửa Chương {fixProgress.current}/{fixProgress.total}...</> : <><RefreshCw size={14}/> 1-Click: Fix & Chấm Điểm Lại</>}
                                            </button>
                                        </div>
                                        <button onClick={() => handleEvaluate(selectedItem, fixModel)} disabled={loadingAction === `eval_${selectedItem.id}`} className="bg-amber-500/10 hover:bg-amber-500/20 text-amber-400 border border-amber-500/30 font-bold text-xs px-4 py-2 rounded-lg flex items-center gap-2 transition-all">
                                            {loadingAction === `eval_${selectedItem.id}` ? <RefreshCw className="animate-spin" size={14}/> : <CheckCircle2 size={14}/>} Đánh giá toàn bộ truyện
                                        </button>
                                        <button onClick={handleCopyAllChapters} className="bg-white/10 hover:bg-white/20 text-white shadow-lg px-4 py-2 rounded-lg text-xs font-bold flex items-center gap-2 transition-all">
                                            <Copy size={14}/> Copy tất cả
                                        </button>
                                        <button onClick={handleSaveEdits} className="bg-indigo-500 hover:bg-indigo-400 text-white shadow-lg px-6 py-2 rounded-lg text-xs font-black uppercase tracking-wider flex items-center gap-2 transition-all transform hover:-translate-y-0.5">
                                            <PenTool size={14}/> Lưu Chỉnh Sửa
                                        </button>
                                    </div>
                                </div>
                                
                                {selectedItem.finalEvaluation && (
                                   <div className="mb-4 flex items-center gap-4 border border-amber-500/20 bg-amber-500/10 rounded-2xl p-4 shrink-0">
                                       <div className="flex flex-col items-center justify-center min-w-[60px]">
                                          <span className="text-3xl font-black text-amber-500 leading-none">{selectedItem.finalEvaluation.score}</span>
                                          <span className="text-[9px] text-amber-500/50 mt-1 uppercase">Điểm</span>
                                       </div>
                                       <div className="flex-1 text-sm text-amber-200/90 leading-relaxed pl-4 border-l border-amber-500/20">
                                          <p>{selectedItem.finalEvaluation.review}</p>
                                          <p className="text-[10px] text-slate-500 mt-1 font-bold uppercase tracking-wider">ĐÁNH GIÁ BỞI: {selectedItem.finalEvaluation.evaluator}</p>
                                       </div>
                                   </div>
                                )}

                                <div className="w-full flex flex-col mt-4 flex-shrink-0 min-h-[600px]">
                                    <div className="flex justify-between items-center mb-2 px-2">
                                        <span className="text-xs text-white/50 font-bold uppercase tracking-wider">
                                            Nội dung truyện (Có thể kéo góc dưới bên phải để mở rộng)
                                        </span>
                                        <span className="text-xs text-emerald-400 font-bold bg-emerald-500/10 px-3 py-1 rounded-full border border-emerald-500/20">
                                            {editableStoryText.split(/\s+/).filter(Boolean).length} chữ đang hiển thị
                                        </span>
                                    </div>
                                    <textarea
                                        value={editableStoryText}
                                        onChange={(e) => setEditableStoryText(e.target.value)}
                                        className="w-full h-[800px] flex-shrink-0 bg-[#0a0a10] border-2 border-white/10 rounded-xl p-8 text-[15px] leading-relaxed font-medium text-slate-300 focus:outline-none focus:border-indigo-500/70 custom-scrollbar shadow-inner"
                                        style={{ resize: 'vertical' }}
                                        placeholder="Nhập nội dung truyện ở đây... Dùng '========================================' hoặc bắt đầu bằng 'Chương X:' để phân cách các chương."
                                    />
                                </div>
                             </div>
                         )}
                     </div>
                  )}

              </div>
           </div>
         ) : (
             <div className="flex-1 flex flex-col items-center justify-center bg-[#0a0a10] border-l border-white/5 relative z-10 transition-all">
                <ShieldAlert size={64} className="mb-6 opacity-20 text-white" />
                <p className="text-lg font-bold text-slate-500 mb-2">Chưa chọn truyện nào</p>
                <p className="text-sm font-medium text-slate-600">Chọn 1 truyện bên tay trái để bắt đầu soi lỗi kịch bản</p>
             </div>
         )}
    </div>
  );
}
