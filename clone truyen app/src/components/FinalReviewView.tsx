/* eslint-disable @typescript-eslint/no-explicit-any */
import React, { useState, useEffect } from 'react';
import { useStore, QueueItem } from '../store/useStore';
import { ShieldAlert, BookOpen, Star, UploadCloud, Rocket, RefreshCw, PenTool, Image as ImageIcon, FileText, CheckCircle2 } from 'lucide-react';
import { agentStoryEvaluator, agentPublisherMetadata } from '../lib/advanced_engine';
import { callWordPress } from '../lib/engine';

export function FinalReviewView() {
  const { queue, updateQueueItem, geminiPaidKey, geminiKey, usePaidAPI, wpUrl, wpUser, wpAppPassword } = useStore();
  const [loadingAction, setLoadingAction] = useState<string | null>(null);
  
  const reviewItems = queue.filter(q => q.status === 'final_review' || q.status === 'completed' || q.status === 'published');
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<'overview' | 'bible' | 'chapters'>('overview');
  const [customCoverUrl, setCustomCoverUrl] = useState('');
  const [customPrompt, setCustomPrompt] = useState('');
  const [readingChapterIdx, setReadingChapterIdx] = useState<number>(0);
  const [isSidebarHidden, setIsSidebarHidden] = useState<boolean>(false);

  useEffect(() => {
    if (!selectedId && reviewItems.length > 0) {
      setTimeout(() => setSelectedId(reviewItems[0].id), 0);
    } else if (selectedId && !reviewItems.find(q => q.id === selectedId)) {
      setTimeout(() => setSelectedId(null), 0);
    }
  }, [selectedId, reviewItems]);

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
  }, [selectedItem?.publishData?.coverUrl, selectedItem?.publishData?.coverImagePrompt]);

  useEffect(() => {
    setTimeout(() => {
      setReadingChapterIdx(0);
      setActiveTab('overview');
    }, 0);
  }, [selectedItem?.id]);

  const getActiveKey = () => usePaidAPI && geminiPaidKey ? geminiPaidKey : geminiKey;

  const handleEvaluate = async (item: QueueItem) => {
    setLoadingAction(`eval_${item.id}`);
    try {
      const evalData = await agentStoryEvaluator('gemini', getActiveKey(), 'gemini-2.5-flash', item.bible, item.chaptersContent);
      updateQueueItem(item.id, { finalEvaluation: { ...evalData, evaluator: 'Gemini 2.5 Flash' } });
      alert("✅ Đánh giá toàn bộ tác phẩm thành công!");
    } catch (e: unknown) {
      alert("Lỗi Đánh giá: " + (e as Error).message);
    }
    setLoadingAction(null);
  };

  const generateCoverPolli = (promptStr: string) => {
      const safePrompt = (promptStr || 'cinematic poster').substring(0, 400);
      return `https://image.pollinations.ai/prompt/${encodeURIComponent(safePrompt + " --no-logo")}?width=800&height=1200&nologo=true&seed=${Math.floor(Math.random()*1000)}`;
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
    if (!selectedItem || !selectedItem.publishData) return;
    updateQueueItem(selectedItem.id, { publishData: { ...selectedItem.publishData, coverUrl: customCoverUrl } });
    alert("✅ Cập nhật Custom Cover URL thành công!");
  };

  const handleRegenerateCover = () => {
    if (!selectedItem || !selectedItem.publishData) return;
    const pollUrl = generateCoverPolli(customPrompt);
    setCustomCoverUrl(pollUrl);
    updateQueueItem(selectedItem.id, { publishData: { ...selectedItem.publishData, coverUrl: pollUrl, coverImagePrompt: customPrompt } });
  };

  const handlePublishToWeb = async (item: QueueItem) => {
    if (!wpUrl || !wpUser || !wpAppPassword || !item.wpPostId) {
      alert("Thiếu kết nối WordPress hoặc chưa có ID bài viết! Vui lòng kiểm tra lại cài đặt.");
      return;
    }

    setLoadingAction(`publish_${item.id}`);
    try {
      const pData = item.publishData || {
         finalTitle: item.title,
         categories: item.genres ? item.genres.split(',').map(s => s.trim()) : [],
         tags: [],
         coverUrl: '',
         seoTitle: item.title,
         seoDescription: (item.bible as any)?.summary || (item.bible as any)?.series_premise || item.prompt,
         seoFocusKeyword: '',
         blurb: (item.bible as any)?.summary || (item.bible as any)?.series_premise || item.prompt
      };
      
      const { finalTitle, categories, coverUrl, seoTitle, seoDescription, seoFocusKeyword, blurb } = pData;
      
      const authHeaders = new Headers();
      if (wpAppPassword.startsWith('M-CORE-')) {
        authHeaders.set('X-Mac-Core-Token', wpAppPassword);
      } else {
        authHeaders.set('Authorization', 'Basic ' + Buffer.from(wpUser + ":" + wpAppPassword).toString('base64'));
      }
      authHeaders.set('Content-Type', 'application/json');

      const htmlIntro = coverUrl ? `<div style="text-align: center; margin-bottom: 20px;"><img src="${coverUrl}" alt="${finalTitle}" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);" /></div>\n` : '';

      const metaObj = {
        rank_math_title: seoTitle,
        rank_math_description: seoDescription,
        rank_math_focus_keyword: seoFocusKeyword,
        seo_title: seoTitle,
        seo_description: seoDescription,
        primary_focus_keyword: seoFocusKeyword
      };

      // 1. Update Title & SEO Meta
      await callWordPress({
        wpUrl, wpUser, wpAppPassword,
        endpoint: `truyen/${item.wpPostId}`,
        method: 'POST',
        payload: {
          title: finalTitle,
          status: 'publish',
          the_loai: categories,
          meta: metaObj
        }
      });
      
      // 2. Append Cover & Metadata to intro
      const storyIntro = blurb || (item.bible as any)?.series_premise || (item.bible as any)?.summary || item.prompt;
      await callWordPress({
         wpUrl, wpUser, wpAppPassword,
         endpoint: `truyen/${item.wpPostId}`,
         method: 'POST',
         payload: {
           content: htmlIntro + storyIntro
         }
      });
      updateQueueItem(item.id, { status: 'published' });
      alert("✅ Lên sàn thành công! Đã tự động tối ưu SEO RankMath và chèn Cover AI vô bài viết.");

    } catch (error: unknown) {
      alert("Lỗi WordPress: " + (error as Error).message);
    }
    setLoadingAction(null);
  };

  return (
    <div className="flex w-full h-[calc(100vh-60px)] font-sans bg-[#0a0a10] text-[#e2e8f0] overflow-hidden animation-fade-in relative z-10">
       
       {/* MASTER SIDEBAR: List of Stories */}
       <div className="w-[340px] bg-[#13131f] border-r border-white/5 flex flex-col shrink-0 z-20">
          <div className="p-6 border-b border-white/5 bg-[#0a0a10]/50 backdrop-blur-md sticky top-0">
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
                   <button key={item.id} onClick={() => { setSelectedId(item.id); setIsSidebarHidden(true); }} className={`w-full text-left p-4 rounded-xl border transition-all relative overflow-hidden group ${selectedId === item.id ? 'bg-indigo-500/10 border-indigo-500/50 shadow-[0_4px_20px_rgba(99,102,241,0.15)]' : 'bg-white/5 border-transparent hover:bg-white/10'}`}>
                      {selectedId === item.id && <div className="absolute left-0 top-0 bottom-0 w-1 bg-indigo-500 rounded-l-xl"></div>}
                      <div className="flex gap-2 mb-2 items-center">
                         <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 bg-black/40 px-2 py-0.5 rounded">{item.genres.split(',')[0]}</span>
                         {item.status === 'published' && <span className="text-[10px] font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-1"><Rocket size={10}/> Đã Đăng</span>}
                      </div>
                      <h3 className={`font-bold line-clamp-2 leading-tight mb-2 ${selectedId === item.id ? 'text-indigo-300' : 'text-white group-hover:text-indigo-200'} transition-colors`}>{item.publishData?.finalTitle || item.title}</h3>
                      <div className="text-[11px] text-slate-500 font-medium">
                         {item.chaptersDone}/{item.targetChapters} Tập • {item.wordCount} Chữ
                      </div>
                   </button>
                ))
             )}
          </div>
       </div>

       {/* DETAIL AREA */}
       {selectedItem ? (
           <div className="flex-1 flex flex-col min-w-0 bg-[#0a0a10] relative z-10 transition-all">
              
              {/* Header */}
              <div className="h-auto md:h-[80px] shrink-0 border-b border-white/5 bg-[#17172a] px-6 py-4 md:py-0 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
                 <div className="flex-1 min-w-0 pr-4">
                    <div className="flex items-center gap-3">
    {isSidebarHidden && (
      <button onClick={() => setIsSidebarHidden(false)} className="bg-white/5 hover:bg-white/10 p-2 rounded-lg text-slate-300 transition-colors shrink-0" title="Hiện danh sách">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
      </button>
    )}
    <h2 className="text-xl font-black text-white line-clamp-1 leading-snug" title={selectedItem.publishData?.finalTitle || selectedItem.title}>{selectedItem.publishData?.finalTitle || selectedItem.title}</h2>
  </div>
                    <div className="text-xs text-slate-400 mt-1 flex flex-wrap gap-x-4 gap-y-1 font-medium">
                        <span className="text-emerald-400 flex items-center gap-1"><PenTool size={12}/>{selectedItem.wordCount} chữ</span>
                        <span className="flex items-center gap-1"><BookOpen size={12}/>{selectedItem.chaptersDone}/{selectedItem.targetChapters} chương</span>
                        <span className="uppercase text-slate-500">• {selectedItem.status === 'published' ? '✅ Đã Lên Sàn' : '⏳ Chờ Xét Duyệt'}</span>
                    </div>
                 </div>
                 <div className="flex items-center shrink-0">
                     <button onClick={() => handlePublishToWeb(selectedItem)} disabled={selectedItem.status === 'published' || loadingAction === `publish_${selectedItem.id}`} className="bg-gradient-to-r from-emerald-500 to-teal-500 text-slate-900 font-extrabold text-xs uppercase tracking-widest px-6 py-3 rounded-xl flex items-center gap-2 hover:opacity-90 disabled:opacity-50 disabled:grayscale transition-all shadow-[0_4px_20px_rgba(16,185,129,0.3)] hover:shadow-[0_4px_30px_rgba(16,185,129,0.5)] transform hover:-translate-y-0.5">
                        {loadingAction === `publish_${selectedItem.id}` ? <RefreshCw className="animate-spin" size={16}/> : <UploadCloud size={16}/>}
                        {selectedItem.status === 'published' ? 'Đã Tự Động Đăng Mạng' : 'Bắn Lên WP Ngay'}
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
              <div className="flex-1 overflow-y-auto custom-scrollbar p-6 lg:p-8 relative">
                  
                  {activeTab === 'overview' && (
                     <div className="flex flex-col lg:flex-row gap-8 animation-fade-in max-w-[1200px] mx-auto">
                        {/* Cột trái: Ảnh bìa & Trình sửa Meta */}
                        <div className="w-full lg:w-[360px] flex flex-col shrink-0">
                           <div className="bg-[#17172a] border border-white/5 rounded-2xl p-6 mb-6 shadow-xl">
                               {selectedItem.publishData?.coverUrl ? (
                                  <div className="relative group rounded-xl overflow-hidden shadow-[0_10px_30px_rgba(0,0,0,0.5)] mb-6 aspect-[2/3]">
                                      {/* eslint-disable-next-line @next/next/no-img-element */}
                                      <img src={selectedItem.publishData.coverUrl} className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Cover" />
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
                              <div className="flex justify-between items-center mb-6 relative z-10">
                                  <h3 className="text-xl font-black text-amber-400 flex items-center gap-2"><Star className="text-amber-400"/> Phán Xét Của Lãnh Chúa (AI Review)</h3>
                                  <button onClick={() => handleEvaluate(selectedItem)} disabled={loadingAction === `eval_${selectedItem.id}`} className="bg-amber-500/10 hover:bg-amber-500/20 text-amber-400 border border-amber-500/30 font-bold text-xs px-5 py-2.5 rounded-xl flex items-center gap-2 transition-all">
                                     {loadingAction === `eval_${selectedItem.id}` ? <RefreshCw className="animate-spin" size={14}/> : <CheckCircle2 size={14}/>} {selectedItem.finalEvaluation ? 'Yêu Cầu Chấm Lại' : 'Phân Tích Toàn Bộ Truyện'}
                                  </button>
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
                     <div className="flex flex-col md:flex-row h-full gap-8 animation-fade-in max-w-[1400px] mx-auto">
                         {(!selectedItem.chaptersContent || selectedItem.chaptersContent.length === 0) ? (
                             <div className="w-full flex-1 flex flex-col items-center justify-center text-slate-500 py-32 border-2 border-dashed border-white/5 rounded-3xl bg-black/20">
                                 <FileText size={64} className="mb-6 opacity-30 text-indigo-500"/>
                                 <h4 className="text-xl font-bold text-slate-400 mb-2">Chưa có dữ liệu chương nội bộ</h4>
                                 <p className="font-medium text-center max-w-lg leading-relaxed text-sm">
                                     (Kể từ bản nâng cấp hệ thống này, các chương được AI viết ở phần Auto-Pilot sẽ được lưu lại trực tiếp vào đây để anh tổng duyệt. Tuy nhiên, truyện này được gen trước đó nên nội dung không được lưu cục bộ. Hãy ra ngoài xem trên WordPress nhé!)
                                 </p>
                             </div>
                         ) : (
                             <>
                                {/* Mục lục Sidebar */}
                                <div className="w-full md:w-1/3 md:max-w-[340px] flex flex-col bg-[#17172a] border border-white/5 rounded-2xl overflow-hidden shrink-0 shadow-xl">
                                    <div className="p-5 bg-black/40 border-b border-white/5 font-black text-sm text-indigo-400 uppercase tracking-widest flex items-center justify-between">
                                        <span>DANH SÁCH TẬP</span>
                                        <span className="bg-indigo-500/20 text-indigo-300 px-2 py-0.5 rounded text-[10px]">{selectedItem.chaptersContent.length} / {selectedItem.targetChapters}</span>
                                    </div>
                                    <div className="flex-1 overflow-y-auto custom-scrollbar p-3 space-y-1.5">
                                       {[...selectedItem.chaptersContent]
                                          .sort((a,b) => a.episode - b.episode)
                                          .map((ch, idx) => (
                                           <button key={idx} onClick={() => setReadingChapterIdx(idx)} className={`w-full text-left p-3.5 text-sm rounded-xl transition-all font-bold line-clamp-2 ${readingChapterIdx === idx ? 'bg-indigo-500 border border-indigo-400 text-white shadow-lg' : 'text-slate-400 hover:bg-white/5 hover:text-white border border-transparent'}`}>
                                               {ch.title}
                                           </button>
                                       ))}
                                    </div>
                                </div>
                                
                                {/* Viewer View */}
                                <div className="flex-1 bg-[#17172a] border border-white/5 rounded-2xl overflow-y-auto custom-scrollbar p-6 md:p-10 text-[#cbd5e1] relative shadow-xl">
                                     {typeof readingChapterIdx === 'number' && selectedItem.chaptersContent[readingChapterIdx] && (
                                         <div className="max-w-3xl mx-auto pb-10">
                                             <h2 className="text-3xl font-black text-white mb-8 leading-snug line-clamp-3 pb-6 border-b border-white/5">{selectedItem.chaptersContent[readingChapterIdx].title}</h2>
                                             
                                             {/* Target Outline of the Episode */}
                                             {(selectedItem.bible as any)?.timeline?.[selectedItem.chaptersContent[readingChapterIdx].episode - 1]?.outline && (
                                                 <div className="bg-amber-500/5 border-l-4 border-amber-500 p-5 mb-10 rounded-r-xl shadow-sm">
                                                     <div className="text-[10px] font-black text-amber-500 uppercase tracking-widest mb-2 flex items-center gap-1.5"><ShieldAlert size={12}/> Nhiệm vụ thiết lập dàn ý gốc</div>
                                                     <div className="text-[15px] font-semibold text-amber-200/90 italic leading-relaxed border-t border-amber-500/10 pt-2">{(selectedItem.bible as any)?.timeline[selectedItem.chaptersContent[readingChapterIdx].episode - 1]?.outline}</div>
                                                 </div>
                                             )}
                  
                                             {/* Actual Content Rendered */}
                                             <div className="text-[16px] leading-[2] font-medium space-y-5 text-slate-300" dangerouslySetInnerHTML={{__html: selectedItem.chaptersContent[readingChapterIdx].content.replace(/\\n/g, '<br/>')}}></div>
                                         </div>
                                     )}
                                </div>
                             </>
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
