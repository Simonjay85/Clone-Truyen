import React, { useState } from 'react';
import { useStore } from '../store/useStore';
import { Bot, Globe, Eraser, Feather } from 'lucide-react';

export function ChapterSplitterView() {
   const { wpUrl, wpUser, wpAppPassword, qwenKey, addApiLog } = useStore();

   const [rawText, setRawText] = useState('');
   const [introText, setIntroText] = useState('');
   const [chapters, setChapters] = useState<{ id: string; num: number; rawTitle: string; name: string; content: string }[]>([]);

   const [metaInfo, setMetaInfo] = useState({
      finalTitle: '',
      blurb: '',
      categories: [] as string[],
      seoTitle: '',
      seoDescription: '',
      seoFocusKeyword: '',
      coverPrompt: '',
      coverUrl: ''
   });

   const [isSplitting, setIsSplitting] = useState(false);
   const [isAiProcessing, setIsAiProcessing] = useState(false);
   const [publishStatus, setPublishStatus] = useState<'idle' | 'publishing' | 'done'>('idle');
   const [publishLogs, setPublishLogs] = useState<string[]>([]);

   const handleSplit = () => {
      setIsSplitting(true);
      setTimeout(() => {
         // Split by "Chương N:" or "Chương N -" or "Chương N ".
         // We use a regex that matches "Chương" followed by space and numbers at the start of a line.
         const regex = /^\s*(Chương\s+\d+[:.\-\s]*(.*))$/gim;

         const foundChapters = [];
         let prefixText = '';

         let nextMatch = regex.exec(rawText);
         if (!nextMatch) {
            alert("Không tìm thấy chữ 'Chương [số]' nào trong văn bản!");
            setIsSplitting(false);
            return;
         }

         prefixText = rawText.substring(0, nextMatch.index).trim();

         let chapterNum = 1;
         while (nextMatch !== null) {
            const _matchStart = nextMatch.index;
            const toTitleCase = (str: string) => str.toLowerCase().split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
            const rawTitleLine = toTitleCase(nextMatch[1].trim());
            const maybeName = nextMatch[2] ? toTitleCase(nextMatch[2].trim()) : '';

            // Find next match to determine end of current chapter
            const nextNextMatch = regex.exec(rawText);
            let chapterContent = '';
            if (nextNextMatch) {
               chapterContent = rawText.substring(_matchStart + nextMatch[0].length, nextNextMatch.index).trim();
               nextMatch = nextNextMatch;
            } else {
               chapterContent = rawText.substring(_matchStart + nextMatch[0].length).trim();
               nextMatch = null;
            }

            foundChapters.push({
               id: Math.random().toString(36).substring(7),
               num: chapterNum++,
               rawTitle: rawTitleLine,
               name: maybeName,
               content: chapterContent
            });
         }

         setIntroText(prefixText);
         setChapters(foundChapters);
         setIsSplitting(false);
      }, 100);
   };

   const handleAiOptimize = async () => {
      if (!qwenKey) return alert("Vui lòng nhập Qwen API Key trong Cài đặt!");
      if (!introText && chapters.length === 0) return alert("Cần tách chương trước!");

      setIsAiProcessing(true);
      try {
         const previewText = introText + "\n" + (chapters[0] ? chapters[0].content.substring(0, 1500) : '');
         const prompt = `Bạn là một copywriter sừng sỏ chuyên viết tóm tắt truyện mạng (Web Novel). Hãy đọc phần mở đầu của truyện sau đây:\n\n"""\n${previewText}\n"""\n\nHãy phân tích và trả về đúng định dạng JSON sau:\n{"finalTitle": "Tên truyện hay nhất (dựng lại nếu chưa rõ)", "blurb": "Viết tóm tắt DÀI (mức 150-250 chữ), chia thành 2-3 đoạn. Đoạn 1: Đánh mạnh vào HOOK (cú sốc/nỗi đau/sự bất ngờ). Đoạn 2: Xung đột vô lý hoặc sự lật mặt/vả mặt. Đoạn 3: Kết thúc bằng một câu hỏi vách núi gây tò mò tột độ. Văn phong phải cực kỳ giật gân, cuốn hút như review phim TikTok.", "categories": ["Tên thể loại 1", "Tên thể loại 2"], "seoTitle": "Tiêu đề SEO 60 ký tự", "seoDescription": "Mô tả SEO 155 ký tự", "seoFocusKeyword": "Từ khóa SEO chính", "coverPrompt": "Miêu tả hình ảnh Thumbnail (bằng tiếng Anh chân thực, cinematic, tỉ lệ 3:2) để dán vào công cụ vẽ AI. Không có chữ/text."}`;

         const res = await fetch('/api/qwen', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
               apiKey: qwenKey,
               systemPrompt: "Bạn là hệ thống tự động bóc tách thông tin truyện. Trả về JSON.",
               userPrompt: prompt,
               jsonMode: true,
               temperature: 0.5,
               model: 'qwen-max'
            })
         });
         if (!res.ok) {
            const errData = await res.json();
            throw new Error(errData.error?.message || JSON.stringify(errData.error) || "API qwen lỗi");
         }
         const data = await res.json();
         let text = data.text.trim();
         if (text.startsWith('```json')) text = text.replace('```json', '').replace(/```$/, '').trim();
         else if (text.startsWith('```')) text = text.replace('```', '').replace(/```$/, '').trim();

         const json = JSON.parse(text);
         const genCoverPrompt = json.coverPrompt || 'cinematic poster style, amazing scenery';
         const genCoverUrl = `https://pollinations.ai/p/${encodeURIComponent(genCoverPrompt.substring(0, 400))}?width=1200&height=800&nologo=true&model=flux&seed=${Math.floor(Math.random() * 100000)}`;

         setMetaInfo({
            finalTitle: json.finalTitle || 'Chưa rõ tên truyện',
            blurb: json.blurb || '',
            categories: json.categories || [],
            seoTitle: json.seoTitle || '',
            seoDescription: json.seoDescription || '',
            seoFocusKeyword: json.seoFocusKeyword || '',
            coverPrompt: genCoverPrompt,
            coverUrl: genCoverUrl
         });

         addApiLog({
            engineType: 'OpenAI',
            model: 'qwen3-max', // Default for Qwen abstraction
            station: 'Splitter',
            project: json.finalTitle,
            promptTokens: data.usage?.promptTokens || 0,
            completionTokens: data.usage?.completionTokens || 0,
            totalTokens: data.usage?.totalTokens || 0,
            cost: 0
         });
      } catch (e: unknown) {
         alert("Lỗi AI: " + (e as Error).message);
      } finally {
         setIsAiProcessing(false);
      }
   };

   const publishToWordPress = async () => {
      if (!metaInfo.finalTitle) return alert("Vui lòng nhờ AI điền Tên Truyện trước!");
      if (chapters.length === 0) return alert("Chưa có chương nào để đăng!");

      if (!wpUrl || !wpUser || !wpAppPassword) {
         return alert("Thiếu cấu hình WordPress trong Settings!");
      }

      setPublishStatus('publishing');
      setPublishLogs(["🚀 Bắt đầu tạo Truyện (Parent Post)..."]);

      try {
         // 1. Tạo Truyện
         const createStoryRes = await fetch('/api/wordpress', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
               wpUrl, wpUser, wpAppPassword,
               endpoint: 'truyen',
               payload: {
                  title: metaInfo.finalTitle,
                  content: (metaInfo.coverUrl ? `<div style="text-align: center; margin-bottom: 20px;"><img src="${metaInfo.coverUrl}" alt="${metaInfo.finalTitle}" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);" /></div>\n\n` : '') + metaInfo.blurb,
                  status: 'publish',
                  the_loai: metaInfo.categories,
                  meta: {
                     rank_math_title: metaInfo.seoTitle,
                     rank_math_description: metaInfo.seoDescription,
                     rank_math_focus_keyword: metaInfo.seoFocusKeyword
                  }
               }
            })
         });

         if (!createStoryRes.ok) throw new Error(await createStoryRes.text());
         const storyData = await createStoryRes.json();
         const parentId = storyData.id;
         setPublishLogs(p => [...p, "✅ Đã tạo truyện thành công! ID: " + parentId, "⏳ Bắt đầu đăng các chương..."]);

         // 2. Tạo từng chương
         for (let i = 0; i < chapters.length; i++) {
            const chap = chapters[i];
            const chapTitle = chap.name ? `Chương ${chap.num}: ${chap.name}` : `Chương ${chap.num}`;
            setPublishLogs(p => [...p, `👉 Đang đăng Chương ${chap.num}...`]);

            const createChapRes = await fetch('/api/wordpress', {
               method: 'POST',
               headers: { 'Content-Type': 'application/json' },
               body: JSON.stringify({
                  wpUrl, wpUser, wpAppPassword,
                  endpoint: 'chuong',
                  payload: {
                     title: chapTitle,
                     content: chap.content,
                     status: 'publish',
                     meta: {
                        _truyen_id: String(parentId)
                     }
                  }
               })
            });

            if (!createChapRes.ok) {
               const errorData = await createChapRes.text();
               setPublishLogs(p => [...p, `❌ Lỗi khi đăng Chương ${chap.num}: ${errorData}`]);
            } else {
               setPublishLogs(p => [...p, `✅ Hoàn thành Chương ${chap.num}`]);
            }
         }

         setPublishLogs(p => [...p, "🎉 HOÀN THÀNH TOÀN BỘ!"]);
         setPublishStatus('done');
      } catch (e: unknown) {
         setPublishLogs(p => [...p, "🚨 LỖI NGHIÊM TRỌNG: " + (e as Error).message]);
         setPublishStatus('idle');
      }
   };

   return (
      <div className="py-6 min-h-full">
         <div className="flex items-center gap-3 mb-8">
            <div className="w-12 h-12 bg-blue-500/10 rounded-xl flex items-center justify-center border border-blue-500/20">
               <Feather size={24} className="text-blue-400" />
            </div>
            <div>
               <h2 className="text-2xl font-bold bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent">
                  Nhập Sỉ Truyện (Chapter Splitter)
               </h2>
               <p className="text-slate-400 text-sm mt-1">Dán nguyên 1 bộ truyện text vào đây, AI sẽ bóc tách chương và đăng thẳng lên web.</p>
            </div>
         </div>

         <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Cột trái: Đầu vào và công cụ */}
            <div className="space-y-6">
               <div className="bg-slate-800/40 border border-slate-700/50 rounded-2xl p-6 relative">
                  <div className="flex justify-between items-center mb-4">
                     <h3 className="text-sm font-semibold text-slate-300">Văn Bản Chữ Thô (Raw Text)</h3>
                     <button onClick={() => { setRawText(''); setChapters([]); setIntroText(''); }} className="text-slate-500 hover:text-red-400 text-xs flex items-center gap-1"><Eraser size={14} /> Xóa sạch</button>
                  </div>
                  <textarea
                     value={rawText}
                     onChange={e => setRawText(e.target.value)}
                     placeholder="Dán toàn bộ text truyện vào đây... (Ví dụ chứa Chương 1:, Chương 2: ...)"
                     className="w-full h-80 bg-slate-900/50 border border-slate-700 rounded-xl p-4 text-slate-300 text-sm font-mono leading-relaxed focus:ring-2 focus:ring-blue-500/50 outline-none"
                  />
                  <button
                     onClick={handleSplit}
                     disabled={!rawText || isSplitting}
                     className="mt-4 w-full py-3 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded-xl flex justify-center items-center gap-2 transition-all shadow-lg shadow-blue-900/20 disabled:opacity-50"
                  >
                     <Bot size={18} /> {isSplitting ? 'Đang Băm...' : '🔪 Phân Tích & Tách Chương'}
                  </button>
               </div>

               {(introText || chapters.length > 0) && (
                  <div className="bg-slate-800/40 border border-slate-700/50 rounded-2xl p-6">
                     <div className="flex justify-between items-center mb-4">
                        <h3 className="text-sm font-semibold text-blue-400">Meta Truyện (AI)</h3>
                        <button
                           onClick={handleAiOptimize}
                           disabled={isAiProcessing}
                           className="px-3 py-1 bg-purple-600/20 hover:bg-purple-600/40 text-purple-400 text-xs rounded-lg flex items-center gap-1 font-medium border border-purple-500/30 transition-colors"
                        >
                           <Bot size={14} /> {isAiProcessing ? 'Đang nghĩ...' : 'Tối Ưu Bằng AI'}
                        </button>
                     </div>

                     <div className="space-y-4">
                        <div>
                           <label className="text-xs text-slate-500 mb-1 block">Tên truyện</label>
                           <input type="text" value={metaInfo.finalTitle} onChange={e => setMetaInfo({ ...metaInfo, finalTitle: e.target.value })} className="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-sm text-white" />
                        </div>
                        <div>
                           <label className="text-xs text-slate-500 mb-1 block">Mô tả (Blurb Hook)</label>
                           <textarea value={metaInfo.blurb} onChange={e => setMetaInfo({ ...metaInfo, blurb: e.target.value })} className="w-full h-24 bg-slate-900 border border-slate-700 rounded-lg p-2 text-sm text-white leading-relaxed" />
                        </div>

                        <div>
                           <label className="text-xs text-slate-500 mb-1 block flex items-center justify-between">
                              <span className="text-emerald-400 font-bold">Thumbnail (Tự động tạo)</span>
                              <button onClick={() => setMetaInfo({ ...metaInfo, coverUrl: `https://pollinations.ai/p/${encodeURIComponent((metaInfo.coverPrompt || 'cinematic poster').substring(0, 400))}?width=1200&height=800&nologo=true&model=flux&seed=${Math.floor(Math.random() * 100000)}` })} className="text-[10px] bg-slate-700 hover:bg-slate-600 px-2 py-1 rounded text-white transition-colors">🔄 Đảo hình</button>
                           </label>
                           {metaInfo.coverUrl && (
                              <div className="relative group rounded-xl overflow-hidden shadow-[0_5px_15px_rgba(0,0,0,0.3)] mb-3 aspect-[3/2] w-full border border-slate-700 bg-black/40">
                                 {/* eslint-disable-next-line @next/next/no-img-element */}
                                 <img src={metaInfo.coverUrl} className="w-full h-full object-cover" alt="Cover" />
                              </div>
                           )}
                           <input type="text" placeholder="URL ảnh bìa/thumbnail..." value={metaInfo.coverUrl} onChange={e => setMetaInfo({ ...metaInfo, coverUrl: e.target.value })} className="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-xs text-slate-400 font-mono mb-2" />
                           <textarea placeholder="Cover Prompt tiếng anh để Gen AI..." value={metaInfo.coverPrompt} onChange={e => setMetaInfo({ ...metaInfo, coverPrompt: e.target.value })} className="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-xs text-slate-500 italic h-16 resize-none" />
                        </div>
                        <div>
                           <label className="text-xs text-slate-500 mb-1 block">Thể loại (Ngăn cách phẩy)</label>
                           <input type="text" value={metaInfo.categories.join(', ')} onChange={e => setMetaInfo({ ...metaInfo, categories: e.target.value.split(',').map(s => s.trim()) })} className="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-sm text-white" />
                        </div>

                        <div className="grid grid-cols-2 gap-4 pt-4 border-t border-slate-700">
                           <div>
                              <label className="text-xs text-slate-500 mb-1 block">SEO Title</label>
                              <input type="text" value={metaInfo.seoTitle} onChange={e => setMetaInfo({ ...metaInfo, seoTitle: e.target.value })} className="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-xs text-slate-300" />
                           </div>
                           <div>
                              <label className="text-xs text-slate-500 mb-1 block">Focus Keyword</label>
                              <input type="text" value={metaInfo.seoFocusKeyword} onChange={e => setMetaInfo({ ...metaInfo, seoFocusKeyword: e.target.value })} className="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-xs text-slate-300" />
                           </div>
                        </div>
                     </div>
                  </div>
               )}
            </div>

            {/* Cột phải: Log và kết quả */}
            <div className="space-y-6">
               {chapters.length > 0 && (
                  <div className="bg-slate-800/40 border border-slate-700/50 rounded-2xl p-6 flex flex-col h-[800px]">
                     <div className="flex justify-between items-center mb-4 shrink-0">
                        <h3 className="text-sm font-semibold text-emerald-400">Đã tách được {chapters.length} chương</h3>

                        <button
                           onClick={publishToWordPress}
                           disabled={publishStatus === 'publishing'}
                           className="px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white text-sm font-bold rounded-lg flex items-center gap-2 shadow-lg shadow-emerald-900/20 disabled:opacity-50"
                        >
                           <Globe size={16} /> Đăng Toàn Bộ Lên WP
                        </button>
                     </div>

                     {publishLogs.length > 0 && (
                        <div className="bg-black/50 rounded-lg p-4 mb-4 font-mono text-xs text-emerald-400 h-32 overflow-y-auto shrink-0 border border-emerald-900/50">
                           {publishLogs.map((lg, idx) => <div key={idx} className="mb-1">{lg}</div>)}
                        </div>
                     )}

                     <div className="overflow-y-auto pr-2 space-y-3 custom-scrollbar flex-1">
                        {chapters.map((chap) => (
                           <div key={chap.id} className="bg-slate-900/50 rounded-lg p-3 border border-slate-700/50">
                              <div className="flex justify-between items-start mb-2">
                                 <h4 className="text-sm font-bold text-slate-300">Chương {chap.num} {chap.name ? ` - ${chap.name}` : ''}</h4>
                                 <span className="text-xs text-slate-500">{chap.content.length} ký tự</span>
                              </div>
                              <p className="text-xs text-slate-400 line-clamp-3">{chap.content}</p>
                           </div>
                        ))}
                     </div>
                  </div>
               )}

               {chapters.length === 0 && (
                  <div className="h-full border-2 border-dashed border-slate-700 rounded-2xl flex flex-col items-center justify-center text-slate-500 px-10 text-center">
                     <Feather size={48} className="text-slate-700 mb-4" />
                     <p>Kết quả tách chương sẽ hiện ở đây.</p>
                  </div>
               )}
            </div>
         </div>
      </div>
   );
}
