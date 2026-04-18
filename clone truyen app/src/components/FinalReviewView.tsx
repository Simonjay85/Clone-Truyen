import React, { useState } from 'react';
import { useStore, QueueItem } from '../store/useStore';
import { ShieldAlert, BookOpen, Star, UploadCloud, Rocket, RefreshCw, PenTool, Image as ImageIcon } from 'lucide-react';
import { agentStoryEvaluator, agentPublisherMetadata } from '../lib/advanced_engine';

export function FinalReviewView() {
  const { queue, updateQueueItem, geminiPaidKey, geminiKey, usePaidAPI, wpUrl, wpUser, wpAppPassword } = useStore();
  const [loadingAction, setLoadingAction] = useState<string | null>(null);

  const reviewItems = queue.filter(q => q.status === 'final_review' || q.status === 'published');

  const getActiveKey = () => usePaidAPI && geminiPaidKey ? geminiPaidKey : geminiKey;

  const handleEvaluate = async (item: QueueItem) => {
    setLoadingAction(`eval_${item.id}`);
    try {
      const evalData = await agentStoryEvaluator('gemini', getActiveKey(), 'gemini-2.5-flash', item.bible);
      updateQueueItem(item.id, { finalEvaluation: { ...evalData, evaluator: 'Gemini 2.5 Flash' } });
    } catch (e: any) {
      alert("Lỗi Đánh giá: " + e.message);
    }
    setLoadingAction(null);
  };

  const handleCraftMetadata = async (item: QueueItem) => {
    setLoadingAction(`meta_${item.id}`);
    try {
      const promptTitle = item.finalEvaluation ? item.title + " - Overview: " + item.finalEvaluation.review : item.title;
      const meta = await agentPublisherMetadata('gemini', getActiveKey(), 'gemini-2.5-flash', item.bible, promptTitle);
      
      const pollUrl = `https://image.pollinations.ai/prompt/${encodeURIComponent(meta.coverImagePrompt + " --no-logo")}?width=800&height=1200&nologo=true`;
      
      updateQueueItem(item.id, { publishData: { ...meta, coverUrl: pollUrl } });
    } catch (e: any) {
      alert("Lỗi Đóng gói SEO: " + e.message);
    }
    setLoadingAction(null);
  };

  const handlePublishToWeb = async (item: QueueItem) => {
    if (!wpUrl || !wpUser || !wpAppPassword || !item.wpPostId) {
      alert("Thiếu kết nối WordPress hoặc chưa có ID bài viết! Vui lòng kiểm tra lại cài đặt.");
      return;
    }
    if (!item.publishData) {
      alert("Vui lòng Bấm Đóng gói SEO trước khi đăng lên web!");
      return;
    }

    setLoadingAction(`publish_${item.id}`);
    try {
      const { finalTitle, categories, tags, coverUrl, seoTitle, seoDescription, seoFocusKeyword } = item.publishData;
      
      const authHeaders = new Headers();
      if (wpAppPassword.startsWith('M-CORE-')) {
        authHeaders.set('X-Mac-Core-Token', wpAppPassword);
      } else {
        authHeaders.set('Authorization', 'Basic ' + Buffer.from(wpUser + ":" + wpAppPassword).toString('base64'));
      }
      authHeaders.set('Content-Type', 'application/json');

      // 1. Convert Categories & Tags strings to WordPress IDs. 
      // Do this is complex if categories don't exist, we will just pass string terms natively if supported,
      // But standard REST API requires integer IDs. 
      // For now, we will add them as inline text at the bottom or if they have a plugin that accepts arrays of strings.
      // We will embed the cover image inside the content to guarantee cross-theme compatibility.
      
      let htmlIntro = `<div style="text-align: center; margin-bottom: 20px;"><img src="${coverUrl}" alt="${finalTitle}" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);" /></div>`;
      htmlIntro += `\n<p><strong>Danh mục AI gán:</strong> ${categories.join(', ')} | <strong>Tags:</strong> ${tags.join(', ')}</p><hr/>\n`;

      // 2. Format RankMath Meta
      const metaObj = {
        rank_math_title: seoTitle,
        rank_math_description: seoDescription,
        rank_math_focus_keyword: seoFocusKeyword
      };

      const res = await fetch(`${wpUrl.replace(/\/$/, "")}/wp-json/wp/v2/truyen/${item.wpPostId}`, {
        method: 'POST',
        headers: authHeaders,
        body: JSON.stringify({
          title: finalTitle,
          status: 'publish',
          meta: metaObj
        })
      });

      if (!res.ok) {
        const d = await res.text();
        throw new Error(d);
      }
      
      // Update the actual TRUYEN content prepended with image
      // Note: we might need an endpoint or we just prepend it to the description content of the parent post
      await fetch(`${wpUrl.replace(/\/$/, "")}/wp-json/wp/v2/truyen/${item.wpPostId}`, {
         method: 'POST',
         headers: authHeaders,
         body: JSON.stringify({ content: htmlIntro + (item.bible?.series_premise || item.prompt) })
      });

      updateQueueItem(item.id, { status: 'published' });
      alert("✅ Lên sàn thành công! Đã tự động tối ưu SEO RankMath và chèn Cover AI.");

    } catch (error: any) {
      alert("Lỗi WordPress: " + error.message);
    }
    setLoadingAction(null);
  };

  return (
    <div className="max-w-7xl mx-auto py-10 animation-fade-in flex flex-col h-[calc(100vh-80px)] px-4">
      <div className="mb-8 flex justify-between items-end flex-shrink-0">
        <div>
          <h2 className="text-3xl font-bold bg-gradient-to-r from-pink-500 to-violet-500 bg-clip-text text-transparent tracking-tight">Cổng Tổng Duyệt (Gatekeeper)</h2>
          <p className="text-slate-400 mt-2">Duyệt và tối ưu hóa SEO trọn gói trước khi cho truyện lên sàn.</p>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto space-y-6 custom-scrollbar pr-2">
        {reviewItems.length === 0 ? (
          <div className="h-full flex flex-col items-center justify-center border-2 border-dashed border-slate-800 rounded-2xl text-slate-500">
            <ShieldAlert size={40} className="mb-4 text-slate-700" />
            <p>Kho lưu trữ trống rỗng. Chờ cày xong truyện ở Auto-Pilot rồi quay lại nhé!</p>
          </div>
        ) : (
          reviewItems.map(item => (
            <div key={item.id} className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-2xl flex flex-col lg:flex-row">
               
               {/* Left Column: Cover & AI Status */}
               <div className="w-full lg:w-72 bg-slate-950 border-r border-slate-800 p-6 flex flex-col items-center relative">
                  {item.publishData?.coverUrl ? (
                     <div className="w-full aspect-[2/3] rounded-lg overflow-hidden shadow-2xl mb-4 relative group">
                        <img src={item.publishData.coverUrl} alt="Cover" className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" />
                        <div className="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex items-end p-3 opacity-0 group-hover:opacity-100 transition-opacity">
                           <span className="text-xs text-slate-300 font-medium line-clamp-3">Prompt: {item.publishData.coverImagePrompt}</span>
                        </div>
                     </div>
                  ) : (
                     <div className="w-full aspect-[2/3] rounded-lg border-2 border-dashed border-slate-700 bg-slate-900/50 flex flex-col items-center justify-center text-slate-600 mb-4">
                        <ImageIcon size={32} className="mb-2 opacity-50" />
                        <span className="text-xs font-bold uppercase tracking-wider">Chưa có Ảnh Bìa</span>
                     </div>
                  )}

                  {item.status === 'published' && (
                     <div className="absolute top-4 right-4 bg-emerald-500 text-white text-[10px] font-black uppercase px-2 py-1 rounded shadow-lg flex items-center gap-1">
                        <Rocket size={12}/> Đã Lên Sàn
                     </div>
                  )}

                  <div className="w-full space-y-2 mt-auto">
                     <button
                        onClick={() => handleEvaluate(item)}
                        disabled={loadingAction === `eval_${item.id}`}
                        className="w-full py-2.5 rounded-lg font-bold text-sm bg-blue-500/10 text-blue-400 border border-blue-500/30 hover:bg-blue-500/20 transition-all flex justify-center items-center gap-2"
                     >
                        {loadingAction === `eval_${item.id}` ? <RefreshCw className="animate-spin" size={16}/> : <Star size={16}/>}
                        {item.finalEvaluation ? "Chấm Lại Điểm" : "Gọi AI Đánh Giá"}
                     </button>

                     <button
                        onClick={() => handleCraftMetadata(item)}
                        disabled={loadingAction === `meta_${item.id}`}
                        className="w-full py-2.5 rounded-lg font-bold text-sm bg-fuchsia-500/10 text-fuchsia-400 border border-fuchsia-500/30 hover:bg-fuchsia-500/20 transition-all flex justify-center items-center gap-2"
                     >
                        {loadingAction === `meta_${item.id}` ? <RefreshCw className="animate-spin" size={16}/> : <PenTool size={16}/>}
                        {item.publishData ? "Đóng Gói Lại SEO" : "Đóng Gói SEO & Bìa"}
                     </button>
                  </div>
               </div>

               {/* Right Column: Info & Actions */}
               <div className="p-6 flex-1 flex flex-col">
                  <div className="mb-6">
                     <div className="flex gap-2 mb-2">
                        <span className="bg-slate-800 text-slate-300 px-2 py-0.5 rounded text-[10px] font-bold uppercase">{item.genres}</span>
                        <span className="bg-slate-800 text-slate-300 px-2 py-0.5 rounded text-[10px] font-bold uppercase">{item.wordCount} Chữ</span>
                     </div>
                     <h3 className="text-2xl font-black text-white leading-tight mb-2">
                        {item.publishData?.finalTitle || item.title}
                     </h3>
                     <p className="text-sm text-slate-400 leading-relaxed line-clamp-2">
                        {item.publishData?.seoDescription || item.prompt}
                     </p>
                  </div>

                  {/* Rating Section */}
                  {item.finalEvaluation && (
                     <div className="bg-amber-500/10 border border-amber-500/20 rounded-xl p-4 mb-6">
                        <div className="flex items-center gap-3 mb-2">
                           <div className="w-10 h-10 rounded-full bg-amber-500/20 flex items-center justify-center text-amber-400 font-black text-xl border border-amber-500/40">
                              {item.finalEvaluation.score}
                           </div>
                           <div>
                              <h4 className="text-sm font-bold text-amber-500 uppercase tracking-wide">Nhận Xét Của {item.finalEvaluation.evaluator}</h4>
                           </div>
                        </div>
                        <p className="text-amber-200/80 text-sm leading-relaxed italic border-l-2 border-amber-500/30 pl-3">"{item.finalEvaluation.review}"</p>
                     </div>
                  )}

                  {/* SEO Section */}
                  {item.publishData && (
                     <div className="bg-emerald-500/5 border border-emerald-500/10 rounded-xl p-4 mb-6 grid grid-cols-2 gap-4">
                        <div className="col-span-2">
                           <h4 className="text-[10px] font-bold text-emerald-500 uppercase tracking-widest mb-1">RankMath SEO Title</h4>
                           <div className="text-emerald-100 text-sm bg-black/20 p-2 rounded">{item.publishData.seoTitle}</div>
                        </div>
                        <div>
                           <h4 className="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-1">Focus Keyword</h4>
                           <div className="text-emerald-400 font-bold bg-emerald-400/10 inline-block px-2 py-1 rounded text-xs">{item.publishData.seoFocusKeyword}</div>
                        </div>
                        <div>
                           <h4 className="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-1">Chuyên Mục (Categories)</h4>
                           <div className="flex gap-1 flex-wrap">
                              {item.publishData.categories.map((c, i) => <span key={i} className="text-indigo-300 font-bold bg-indigo-500/20 px-2 py-1 rounded text-xs">{c}</span>)}
                           </div>
                        </div>
                     </div>
                  )}

                  {/* Publish Area */}
                  <div className="mt-auto pt-6 border-t border-slate-800/50 flex justify-end">
                     <button
                        onClick={() => handlePublishToWeb(item)}
                        disabled={!item.publishData || item.status === 'published' || loadingAction === `publish_${item.id}`}
                        className={`px-8 py-3 rounded-xl font-black text-sm uppercase tracking-wider flex items-center gap-2 transition-all ${
                           item.status === 'published' 
                           ? 'bg-slate-800 text-slate-500 cursor-not-allowed'
                           : !item.publishData 
                              ? 'bg-slate-800 text-slate-600 opacity-50 cursor-not-allowed'
                              : 'bg-gradient-to-r from-emerald-500 to-teal-400 hover:from-emerald-400 hover:to-teal-300 text-slate-900 shadow-[0_0_20px_rgba(16,185,129,0.4)] hover:shadow-[0_0_30px_rgba(16,185,129,0.6)] transform hover:-translate-y-0.5'
                        }`}
                     >
                        {loadingAction === `publish_${item.id}` ? <RefreshCw className="animate-spin" size={18}/> : <UploadCloud size={18}/>}
                        {item.status === 'published' ? 'Đã Xuất Bản' : 'Bắn Lên Báo Dịch'}
                     </button>
                  </div>
               </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
