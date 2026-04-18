import React, { useState } from 'react';
import { useStore, QueueItem } from '../store/useStore';
import { Share2, Image as ImageIcon, Copy, CheckCircle2, Rocket, CloudLightning, Loader2, Sparkles } from 'lucide-react';
import { callGemini } from '../lib/engine';

export function SocialStudioView() {
  const { queue, updateQueueItem, geminiPaidKey, geminiKey, usePaidAPI, webhookUrl } = useStore();
  const socialItems = queue.filter(q => q.status === 'published' && !q.isSocialShared);
  
  const [loadingAction, setLoadingAction] = useState<string | null>(null);

  // Auto-generate caption if not explicitly stored
  const [captions, setCaptions] = useState<Record<string, string>>({});

  const generateCaption = async (item: QueueItem) => {
    setLoadingAction(`caption_${item.id}`);
    try {
      const activeKey = usePaidAPI ? geminiPaidKey : (geminiKey || geminiPaidKey);
      if (!activeKey) throw new Error("Vui lòng cấu hình API Key trong Settings trước.");

      const blurb = item.publishData?.blurb || item.bible?.overallSizzle || item.bible?.summary || item.prompt;
      const title = item.publishData?.finalTitle || item.title;

      const sysPrompt = `Bạn là Content Creator Tiktok/Instagram/Pinterest chuyên nghiệp. 
Nhiệm vụ: Viết 1 bài post Social siêu cuốn dựa trên tóm tắt truyện.
YÊU CẦU:
1. Mở đầu bằng một câu Hook cực gắt (viết IN HOA).
2. Tóm tắt nội dung chính bằng 2-3 câu khơi gợi sự tò mò đau đớn, giật gân, vả mặt. Tuyệt đối không spoil đoạn kết.
3. Call to Action (CTA) nảy lửa: Dẫn dắt người đọc bấm link dưới Bio/Comment để đọc trọn bộ.
4. Thêm 5-7 Hashtags xu hướng liên quan đến: #truyenchu #ngontinh #tieu_thuyet #reviewtruyen
5. Trả trực tiếp văn bản Text (kèm icon Emoji đẹp mắt), KHÔNG dùng Markdown code block.`;

      const userPrompt = `Tên truyện: ${title}\nVăn án/Tóm tắt: ${blurb}\nHãy viết Caption ngay!`;

      const res = await callGemini({
        apiKey: activeKey,
        systemPrompt: sysPrompt,
        userPrompt,
        temperature: 0.8,
        model: usePaidAPI ? 'gemini-2.5-pro' : 'gemini-2.5-flash'
      });

      setCaptions(prev => ({ ...prev, [item.id]: res.text }));
    } catch (error: any) {
      alert("Lỗi tạo Caption: " + error.message);
    } finally {
      setLoadingAction(null);
    }
  };

  const handleCopy = (text: string) => {
    navigator.clipboard.writeText(text);
    alert('Đã copy caption vào bộ nhớ đệm!');
  };

  const markAsShared = (id: string) => {
    updateQueueItem(id, { isSocialShared: true });
  };

  const shareToWebhook = async (item: QueueItem, captionText: string) => {
    if (!webhookUrl) return alert("Bạn chưa cấu hình Webhook URL trong Settings!");
    setLoadingAction(`webhook_${item.id}`);
    try {
      const payload = {
        title: item.publishData?.finalTitle || item.title,
        cover_image: item.publishData?.coverUrl || '',
        caption: captionText,
        tags: item.publishData?.tags || [],
        categories: item.publishData?.categories || [],
        source_url: `${item.wpPostId}`, // Can link directly if known
        timestamp: new Date().toISOString()
      };

      const res = await fetch(webhookUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      if (!res.ok) throw new Error(await res.text());
      
      alert("✅ Đã bắn dữ liệu sang Webhook thành công!");
      markAsShared(item.id);
    } catch (e: any) {
      alert("Lỗi gửi Webhook: " + e.message);
    } finally {
      setLoadingAction(null);
    }
  };

  return (
    <div className="max-w-6xl mx-auto py-10 animation-fade-in flex flex-col h-[calc(100vh-80px)]">
      <div className="mb-8 flex-shrink-0">
        <h2 className="text-3xl font-bold bg-gradient-to-r from-pink-500 to-rose-500 bg-clip-text text-transparent flex items-center gap-3">
          <Share2 className="text-pink-500" size={32} />
          Social Studio
        </h2>
        <p className="text-slate-400 mt-2">Phòng Marketing: Nơi ra lò các bài Post mồi câu cực gắt cho Tiktok / Instagram / Pinterest.</p>
        <p className="text-xs text-slate-500 mt-1">Lưu ý: Truyện chỉ xuất hiện ở đây sau khi đã trạng thái "Bắn Lên Báo Dịch WP".</p>
      </div>

      <div className="flex-1 overflow-y-auto space-y-6 custom-scrollbar pr-2 pb-20">
        {socialItems.length === 0 ? (
           <div className="bg-slate-900 border border-slate-800 rounded-2xl p-12 text-center text-slate-500 flex flex-col items-center shadow-xl">
              <Share2 size={48} className="mb-4 opacity-50 text-pink-400" />
              <h3 className="text-xl font-bold text-slate-300 mb-2">Hàng Chờ Trống Rỗng</h3>
              <p>Chưa có truyện nào đang đợi đăng mồi lên Social. Hãy sang mục Tổng Duyệt và xuất bản một truyện lên WP trước nhé.</p>
           </div>
        ) : (
          <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">
            {socialItems.map(item => {
               const cover = item.publishData?.coverUrl || item.coverUrl;
               const title = item.publishData?.finalTitle || item.title;
               const activeCaption = captions[item.id] || "Chưa tạo Caption mồi câu. Bấm nút Tạo Caption để AI phóng bút...";

               return (
                 <div key={item.id} className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-xl flex flex-col">
                   <div className="flex flex-col md:flex-row h-full">
                     {/* Cover Section */}
                     <div className="w-full md:w-2/5 relative border-r border-slate-800 bg-slate-950 flex flex-col justify-between group">
                       {cover ? (
                         <div className="relative w-full h-48 md:h-full">
                           <img src={cover} alt="Cover" className="absolute inset-0 w-full h-full object-cover p-2 rounded-xl" />
                           <div className="absolute inset-2 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex items-end justify-center pb-4 rounded-lg">
                              <a href={cover} target="_blank" rel="noreferrer" className="bg-white/20 hover:bg-white/40 backdrop-blur-md px-3 py-1.5 rounded-full text-xs font-bold text-white flex items-center gap-1 transition-all">
                                 <ImageIcon size={14}/> Tải Ảnh Nhanh
                              </a>
                           </div>
                         </div>
                       ) : (
                         <div className="flex-1 flex flex-col items-center justify-center text-slate-600 p-8 h-48 md:h-full">
                           <ImageIcon size={40} className="mb-2 opacity-30" />
                           <span className="text-xs text-center">Chưa có hoặc lỗi ảnh</span>
                         </div>
                       )}
                     </div>

                     {/* Content Section */}
                     <div className="w-full md:w-3/5 p-5 flex flex-col">
                        <h4 className="font-bold text-white mb-1 line-clamp-1 text-lg">{title}</h4>
                        <div className="flex gap-2 mb-4">
                           <span className="text-xs px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-400 font-bold uppercase">
                              #{item.wpPostId}
                           </span>
                           <span className="text-xs px-2 py-0.5 rounded bg-pink-500/10 border border-pink-500/30 text-pink-400 font-medium truncate">
                              Thể loại: {item.publishData?.categories?.join(', ') || item.genres || 'N/A'}
                           </span>
                        </div>

                        <div className="flex-1 bg-slate-950 rounded-xl border border-slate-800 p-3 mb-4 relative group">
                           {loadingAction === `caption_${item.id}` ? (
                              <div className="flex flex-col items-center justify-center h-full text-pink-400 py-6">
                                 <Loader2 size={24} className="animate-spin mb-2" />
                                 <span className="text-xs font-bold animate-pulse">Giám Đốc Marketing Đang Soạn Văn...</span>
                              </div>
                           ) : (
                              <div className="text-xs text-slate-300 whitespace-pre-wrap leading-relaxed max-h-48 overflow-y-auto custom-scrollbar pr-2">
                                 {activeCaption}
                              </div>
                           )}
                           
                           {captions[item.id] && loadingAction !== `caption_${item.id}` && (
                              <button 
                                onClick={() => handleCopy(activeCaption)}
                                className="absolute top-2 right-2 bg-slate-800 hover:bg-slate-700 text-slate-300 p-2 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity shadow-lg border border-slate-700"
                                title="Copy Caption"
                              >
                                <Copy size={16} />
                              </button>
                           )}
                        </div>

                        {/* Actions */}
                        <div className="flex flex-wrap items-center gap-2 mt-auto">
                           {!captions[item.id] ? (
                             <button
                               onClick={() => generateCaption(item)}
                               disabled={loadingAction === `caption_${item.id}`}
                               className="flex-1 bg-indigo-600 hover:bg-indigo-500 text-white font-bold py-2 rounded-lg text-xs flex items-center justify-center gap-2 transition-colors disabled:opacity-50"
                             >
                                <Sparkles size={14} /> AI Tạo Mồi Câu
                             </button>
                           ) : (
                              <button
                                onClick={() => generateCaption(item)}
                                disabled={loadingAction === `caption_${item.id}`}
                                className="bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold py-2 px-3 rounded-lg text-xs flex items-center justify-center gap-1.5 transition-colors disabled:opacity-50"
                                title="Tạo Lại"
                              >
                                 <RefreshCwIcon size={14} className={loadingAction === `caption_${item.id}` ? "animate-spin" : ""} /> Tạo Lại
                              </button>
                           )}

                           <button
                             onClick={() => shareToWebhook(item, activeCaption)}
                             className="flex-1 bg-pink-600 hover:bg-pink-500 text-white font-bold py-2 px-3 rounded-lg text-xs flex items-center justify-center gap-1.5 transition-colors shadow-[0_0_15px_rgba(219,39,119,0.3)] hover:shadow-[0_0_20px_rgba(219,39,119,0.5)] whitespace-nowrap"
                           >
                              <CloudLightning size={14} /> Bắn ZAPIER
                           </button>

                           <button
                             onClick={() => markAsShared(item.id)}
                             className="w-10 h-10 flex-shrink-0 bg-emerald-500/10 hover:bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 rounded-lg flex items-center justify-center transition-all"
                             title="Đánh dấu đã đăng tay thành công"
                           >
                              <CheckCircle2 size={18} />
                           </button>
                        </div>
                     </div>
                   </div>
                 </div>
               );
            })}
          </div>
        )}
      </div>
    </div>
  );
}

const RefreshCwIcon = ({ size, className }: { size: number, className?: string }) => (
  <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>
);
